"""Numerical helpers."""



from math import factorial
from functools import cache, partial
import numpy as np
import numpy.typing as npt
from scipy.special import factorial as spyfactorial
spyfactorial = partial(spyfactorial, exact=True)



__all__ = (
    'hermfval', 'hermfder', 'hermfkin', 'hermfpmul',
    'states_to_density', 'T_matrix', 'rho_to_g',
    'rand_ortho_pair'
)



#Hermite functions
def hermfval(f:npt.ArrayLike, x:float|npt.NDArray[np.floating]) \
        -> np.float64|npt.NDArray[np.float64]:
    """Return the evaluation of Hermite function series `f` at point `x`."""
    f = np.asarray(f)
    if not f.ndim == 1:
        raise ValueError('f must be one dimensional')
    if not f.size >= 1:
        raise ValueError('f have at least 1 coefficient (numpy.hermval is buggy)')
    
    return np.exp(-x**2/2) * np.polynomial.hermite.hermval(
        x,
        [fj / np.sqrt(2**j * factorial(j) * np.sqrt(np.pi))
            for j, fj in enumerate(f)]
    )

def hermfder(f:npt.ArrayLike) -> npt.NDArray:
    r"""Return the derivative of Hermite function series `f`.
    
    $$
        f'
    $$
    
    Notes
    -----
    $$
        \begin{aligned}
            h'_j &= \sqrt{\frac{j}{2}}h_{j-1}-\sqrt{\frac{j+1}{2}}h_{j+1} \\
            f' &= \sum_j f_jh_j' \\
            &\qquad\mid h'_j=\sqrt{\frac{j}{2}}h_{j-1}-\sqrt{\frac{j+1}{2}}h_{j+1} \\
            &= \sum_j f_j\left(\sqrt{\frac{j}{2}}h_{j-1}-\sqrt{\frac{j+1}{2}}h_{j+1}\right) \\
            &= \sum_{j=0}^\infty f_j\sqrt{\frac{j}{2}}h_{j-1} - \sum_{j=0}^\infty f_j\sqrt{\frac{j+1}{2}}h_{j+1} \\
            &\qquad\mid j-1\to j\ \&\ j+1\to j \\
            &= \sum_{j=-1}^\infty\sqrt{\frac{j+1}{2}}f_{j+1}h_j - \sum_{j=1}^\infty\sqrt{\frac{j}{2}}f_{j-1}h_j \\
            &\qquad\mid -0+0=-\sqrt{\frac{-1+1}{2}}f_{-1+1}h_{-1}+\sqrt{\frac{0}{2}}f_{0-1}h_0 \\
            &= \sum_{j=0}^\infty\sqrt{\frac{j+1}{2}}f_{j+1} h_j - \sum_{j=0}^\infty\sqrt{\frac{j}{2}}f_{j-1}h_j \\
            &= \sum_j\left(\sqrt{\frac{j+1}{2}}f_{j+1}-\sqrt{\frac{j}{2}}f_{j-1}\right)h_j
        \end{aligned}
    $$
    
    References
    ----------
    - [Wikipedia - Hermite polynomials - Recursion relation](https://en.wikipedia.org/wiki/Hermite_polynomials#Recursion_relation)
    """
    f = np.asarray(f)
    if not f.ndim == 1:
        raise ValueError('f must be a one dimensional')
    
    i = np.arange(1, len(f)+1)
    r = np.zeros(len(f)+1, dtype=np.result_type(f.dtype, np.float64))
    r[:-2] = np.sqrt(i[:-1]/2) * f[1:]
    r[1:] -= np.sqrt(i/2) * f
    return r

def hermfkin(f:npt.ArrayLike) -> np.float64:
    r"""Return the kinetic energy of `f`.
    
    $$
        T[f] = -\frac{1}{2}\int_\mathbb{R}f''(x)f(x)\,\mathrm{d}x = +\frac{1}{2}\int_\mathbb{R}f'(x)^2\,\mathrm{d}x = \frac{||f'||_{L_\mathbb{R}^2}^2}{2}
    $$
    """
    fp = hermfder(f)
    return np.sum(fp*fp) / 2

@cache
def _hermfpmul_coeffs(i:int, j:int) \
        -> tuple[npt.NDArray[np.uin64], npt.NDArray[np.float64]]:
    k = np.arange(min(i, j)+1, dtype=np.uint64)
    indices = i + j - 2*k
    coefficients = np.sqrt(factorial(i)*factorial(j)*spyfactorial(i+j-2*k)) \
            / (spyfactorial(k)*spyfactorial(i-k)*spyfactorial(j-k))
    indices.flags.writeable = coefficients.flags.writeable = False
    return indices, coefficients

def hermfpmul(f:npt.ArrayLike, g:npt.ArrayLike) -> npt.NDArray:
    """Return $m$, such that $mh_0=fg$.
    
    $f$, $g$ & $m$ are sequences of coefficients
    representing Hermite function series.
    """
    f, g = np.asarray(f), np.asarray(g)
    if not f.ndim == g.ndim == 1:
        raise ValueError('f & g must be 1 dimensional')
    
    r = np.zeros(len(f)+len(g)-1, dtype=np.result_type(f, g, np.float64))
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            indices, coefficients = _hermfpmul_coeffs(i, j)
            r[indices] += fi * gj * coefficients
    return r



#quantum mechanics
def states_to_density(state:npt.ArrayLike, *others:npt.ArrayLike) \
        -> npt.NDArray:
    """Return the density matrix for an ensemble of state vectors."""
    states = tuple(np.asarray(s) for s in (state, *others))
    if not (all(s.ndim==1 for s in states) \
            and len(set(s.size for s in states)) == 1):
        raise ValueError('states must be one dimensional and of same length')
    
    return sum((np.outer(o, o) for o in states[1:]),
            np.outer(states[0], states[0]))

def T_matrix(D:int) -> npt.NDArray[np.float64]:
    r"""Return the matrix representation of $\hat{T}$ in Hermite function to degree `D`."""
    T = np.zeros((D+1, D+1), dtype=np.float64)
    
    i = np.arange(D+1)
    np.fill_diagonal(T, (2*i+1)/4)
    i = i[:max(D-1, 0)]
    off_diagonal = -np.sqrt((i+1)*(i+2)) / 4
    np.fill_diagonal(T[:, 2:], off_diagonal)
    np.fill_diagonal(T[2:, :], off_diagonal)
    
    return T

def rho_to_g(rho:npt.ArrayLike) -> npt.NDArray:
    r"""Return $\vec{g}$ for density matrix $\rho$."""
    rho = np.asarray(rho)
    if not rho.ndim == 2:
        raise ValueError('rho must be two dimensional')
    
    g = np.zeros(rho.shape[0]+rho.shape[1]-1,
            dtype=np.result_type(rho.dtype, np.float64))
    for i in range(rho.shape[0]):
        for j in range(rho.shape[1]):
            indices, coefficients = _hermfpmul_coeffs(i, j)
            g[indices] += rho[i, j] * coefficients
    return g



#random
def rand_ortho_pair(N:int) \
        -> tuple[npt.NDArray[np.float64], npt.NDArray[np.float64]]:
    """Return two orthonormal vectors of length `N`."""
    if not N >= 2:
        raise ValueError('N must be >= 2')
    
    v, w = np.random.randn(N), np.random.randn(N)
    v /= np.linalg.norm(v)
    w /= np.linalg.norm(w)
    
    w -= (v @ w) * v
    w /= np.linalg.norm(w)
    
    return v, w
