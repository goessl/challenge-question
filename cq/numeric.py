"""Numerical helpers."""



from math import factorial
from functools import cache
import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.special import factorial as spyfactorial



__all__ = (
    'hermfval', 'hermfder', 'hermfkin', 'hermfpmul_coeffs', 'hermfpmul',
    'states_to_density', 'T_matrix', 'rho_to_g',
    'rand_ortho_pair'
)



#Hermite functions
def hermfval(f: ArrayLike, x: ArrayLike) \
        -> np.float64|NDArray[np.float64]:
    r"""Return the evaluation of Hermite function series `f` at point `x`.
    
    $$
        \sum_jf_jh_j(x)
    $$
    
    Parameters
    ----------
    f
        Hermite function series as a 1D array
        or multiple Hermite function series as rows in a 2D array.
    x
        Evaluation point(s), of any shape.
    
    Returns
    -------
        Value(s) of shape `f.shape[:-1]+x.shape`.
    """
    f, x = np.asarray(f), np.asarray(x)
    if f.ndim not in {1, 2}:
        raise ValueError('f must be one or two dimensional')
    if not f.shape[-1] >= 1:
        raise ValueError('f must have at least 1 coefficient (numpy.hermval is buggy)')
    
    j = np.arange(f.shape[-1], dtype=np.uint64)
    factors = np.sqrt(2**j * spyfactorial(j, exact=True) * np.sqrt(np.pi))
    return np.exp(-x**2/2) * np.polynomial.hermite.hermval(
            x, np.moveaxis(f/factors, -1, 0))

def hermfder(f: ArrayLike) -> NDArray:
    r"""Return the derivative of a Hermite function series.
    
    $$
        f'
    $$
    
    Parameters
    ----------
    f
        Hermite function series as a 1D array
        or multiple Hermite function series as rows in a 2D array.
    
    Returns
    -------
        Derivative(s).
    
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
    if f.ndim not in {1, 2}:
        raise ValueError('f must be one or two dimensional')
    
    factors = np.sqrt(np.arange(1, f.shape[-1]+1, dtype=np.uint64) / 2)
    r = np.zeros(f.shape[:-1]+(f.shape[-1]+1,),
            dtype=np.result_type(f.dtype, np.float64))
    r[..., :-2] = factors[:-1] * f[..., 1:]
    r[..., 1:] -= factors * f
    return r

def hermfkin(f: ArrayLike) -> np.float64|NDArray:
    r"""Return the kinetic energy of a Hermite function series.
    
    Parameters
    ----------
    f
        Hermite function series as a 1D array
        or multiple Hermite function series as rows in a 2D array.
    
    Returns
    -------
        Kinetic energy/energies.
    
    Notes
    -----
    $$
        T[f] = -\frac{1}{2}\int_\mathbb{R}f''(x)f(x)\,\mathrm{d}x = +\frac{1}{2}\int_\mathbb{R}f'(x)^2\,\mathrm{d}x = \frac{||f'||_{L_\mathbb{R}^2}^2}{2}
    $$
    """
    fp = hermfder(f)
    return np.sum(np.conjugate(fp)*fp, axis=-1) / 2

@cache
def hermfpmul_coeffs(i: int, j: int) \
        -> tuple[NDArray[np.uint64], NDArray[np.float64]]:
    r"""Return the pseudo product coefficients of two Hermite functions.
    
    $$
        k, c_k \qquad c_k=\frac{\sqrt{i!j!(i+j-2k)!}}{k!(i-k)!(j-k)!}
    $$
    
    Parameters
    ----------
    i, j
        Degrees.
    
    Returns
    -------
        Indices $i+j-2k$ & coefficients $c_k$, descending in index.
    
    Notes
    -----
    Cached, and both returned arrays are read-only, so callers must not
    modify them.
    
    See also
    --------
    - [`hermfpmul`][cq.numeric.hermfpmul]
    
    References
    ----------
    - [Wikipedia - Hermite polynomials](https://en.wikipedia.org/wiki/Hermite_polynomials)
    """
    k = np.arange(min(i, j)+1, dtype=np.uint64)
    indices = i + j - 2*k
    coefficients = np.sqrt(
            factorial(i) * factorial(j) * spyfactorial(i+j-2*k, exact=True)) \
            / (spyfactorial(k, exact=True) * spyfactorial(i-k, exact=True) \
                * spyfactorial(j-k, exact=True))
    indices.flags.writeable = coefficients.flags.writeable = False
    return indices, coefficients

def hermfpmul(f: ArrayLike, g: ArrayLike) -> NDArray:
    r"""Return the pseudo product of two Hermite function series.
    
    $$
        m \qquad fg=mh_0, \ m=\sum_jm_jh_j
    $$
    
    Parameters
    ----------
    f, g
        Hermite function series as 1D arrays
        or multiple Hermite function series as rows in 2D arrays.
    
    Returns
    -------
        Pseudo product.
    
    Notes
    -----
    $$
        \begin{aligned}
            &h_i(x)h_j(x) &&\mid h_j(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x) \\
            &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}}H_i(x)H_j(x) &&\mid H_iH_j=\sum_{k=0}^{\min\{i,j\}}2^kk!\binom{i}{k}\binom{j}{k}H_{i+j-2k} \\
            &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}}\sum_{k=0}^{\min\{i,j\}}2^kk!\binom{i}{k}\binom{j}{k}H_{i+j-2k}(x) &&\mid h_k(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^kk!\sqrt{\pi}}}H_k(x) \\
            &= \frac{e^{-\frac{x^2}{2}}}{\sqrt{i!j!\sqrt{\pi}}}\sum_{k=0}^{\min\{i,j\}}k!\binom{i}{k}\binom{j}{k}\sqrt{(i+j-2k)!}h_{i+j-2k}(x) &&\mid h_0(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}} \\
            &= h_0(x)\sum_{k=0}^{\min\{i,j\}}k!\binom{i}{k}\binom{j}{k}\sqrt{\frac{(i+j-2k)!}{i!j!}}h_{i+j-2k}(x) \\
            &= h_0(x)\sum_{k=0}^{\min\{i,j\}}\frac{\sqrt{i!j!(i+j-2k)!}}{k!(i-k)!(j-k)!}h_{i+j-2k}(x)
        \end{aligned}
    $$
    
    Reference implementation
    
    ```python
    def hermfmul(f: Sequence, g: Sequence) -> list:
        r = [0] * (len(f)+len(g)-1)
        for i, fi in enumerate(f):
            for j, gj in enumerate(g):
                for k in range(min(i, j)+1):
                    r[i+j-2*k] += fi * gj \
                            * factorial(k)*comb(i, k)*comb(j, k) \
                            * sqrt(factorial(i+j-2*k) \
                            / (factorial(i)*factorial(j)))
        return r
    ```
    
    See also
    --------
    - [`hermfpmul_coeffs`][cq.numeric.hermfpmul_coeffs]
    """
    f, g = np.asarray(f), np.asarray(g)
    if not {f.ndim, g.ndim} <= {1, 2}:
        raise ValueError('f & g must be one or two dimensional')
    
    r = np.zeros(np.broadcast_shapes(f.shape[:-1], g.shape[:-1])
                 + (f.shape[-1]+g.shape[-1]-1,),
            dtype=np.result_type(f, g, np.float64))
    for i in range(f.shape[-1]):
        for j in range(g.shape[-1]):
            indices, coefficients = hermfpmul_coeffs(i, j)
            r[..., indices] += f[..., i, np.newaxis] * g[..., j, np.newaxis] \
                    * coefficients
    return r



#quantum mechanics
def states_to_density(*states: ArrayLike) -> NDArray:
    r"""Return the density matrix for an ensemble of state vectors.
    
    $$
        \sum_i\vec{v}_i\vec{v}_i^\dagger
    $$
    
    Parameters
    ----------
    *states
        States as vectors of same length.
    
    Returns
    -------
        Density matrix.
    """
    if not states:
        raise ValueError('requiring at least one state')
    states = tuple(map(np.asarray, states))
    if not all(s.ndim in {1, 2} for s in states):
        raise ValueError('states must be one or two dimensional')
    if len(set(s.shape[-1] for s in states)) != 1:
        raise ValueError('all states must be of same length')
    
    return sum(s[..., :, np.newaxis] * np.conjugate(s[..., np.newaxis, :])
            for s in states)

def T_matrix(D: int) -> NDArray[np.float64]:
    r"""Return the matrix representation of $\hat{T}$.
    
    In Hermite function series as basis.
    
    Parameters
    ----------
    D
        Degree.
    
    Returns
    -------
        $T$ matrix.
    """
    T = np.zeros((D+1, D+1), dtype=np.float64)
    
    i = np.arange(D+1)
    np.fill_diagonal(T, (2*i+1)/4)
    i = i[:max(D-1, 0)]
    off_diagonal = -np.sqrt((i+1)*(i+2)) / 4
    np.fill_diagonal(T[:, 2:], off_diagonal)
    np.fill_diagonal(T[2:, :], off_diagonal)
    
    return T

def rho_to_g(rho: ArrayLike) -> NDArray:
    r"""Return $\vec{g}$ for density matrix $\rho$.
    
    Parameters
    ----------
    rho
        Density matrix as a 2D array
        or multiple density matrices stacked in a 3D array.
    
    Returns
    -------
        Coefficient vector(s).
    """
    rho = np.asarray(rho)
    if rho.ndim not in {2, 3}:
        raise ValueError('rho must be two or three dimensional')
    
    g = np.zeros(rho.shape[:-2]+(rho.shape[-2]+rho.shape[-1]-1,),
            dtype=np.result_type(rho.dtype, np.float64))
    for i in range(rho.shape[-2]):
        for j in range(rho.shape[-1]):
            indices, coefficients = hermfpmul_coeffs(i, j)
            g[..., indices] += rho[..., i, j, np.newaxis] * coefficients
    return g



#random
def rand_ortho_pair(N: int, M: int|None=None) \
        -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    r"""Return two orthonormal vectors.
    
    $$
        \vec{v}, \ \vec{w} \qquad ||\vec{v}||=||\vec{w}||=1, \ \Braket{\vec{v}|\vec{w}}=0
    $$
    
    Parameters
    ----------
    N
        Length.
    M
        Number of pairs, or `None` for a pair of 1D-vectors.
    
    Returns
    -------
        Vectors.
    
    Notes
    -----
    Symmetric orthogonalisation instead of Gram-Schmidt
    just to be perfectly sure no bias gets introduced.
    
    Begin with two unit vectors and bend them away of each other equally:
    
    $$
        \begin{aligned}
            &\Braket{\vec{v}+\alpha(\vec{w}-\vec{v}) | \vec{w}-\alpha(\vec{w}-\vec{v})} \\
            &= \Braket{\vec{v}|\vec{w}}+\alpha\Braket{\vec{w}-\vec{v}|\vec{w}}-\alpha\Braket{\vec{v}|\vec{w}-\vec{v}}-\alpha^2\Braket{\vec{w}-\vec{v}|\vec{w}-\vec{v}} \\
            &= \Braket{\vec{v}|\vec{w}}+\alpha(1-\Braket{\vec{v}|\vec{w}})-\alpha(\Braket{\vec{v}|\vec{w}}-1)-\alpha^2(1+1-\Braket{\vec{v}|\vec{w}}-\Braket{\vec{w}|\vec{v}}) \\
            &= \Braket{\vec{v}|\vec{w}} + 2\alpha(1-\Braket{\vec{v}|\vec{w}})+2\alpha^2(\Braket{\vec{v}|\vec{w}}-1) \\
            &\overset{!}{=} 0 \\
            \alpha &= \frac{\Braket{\vec{v}|\vec{w}}-1\pm\sqrt{1-\Braket{\vec{v}|\vec{w}}^2}}{2(\Braket{\vec{v}|\vec{w}}-1)} \\
            \vec{v}' &= \vec{v}+\alpha(\vec{w}-\vec{v}) \\
            \vec{w}' &= \vec{w}-\alpha(\vec{w}-\vec{v})
        \end{aligned}
    $$
    
    Then normalise again.
    
    Degenerate cases:
    
    - $\Braket{\vec{v}|\vec{w}}=1$ ($\vec{v}, \vec{w}$ parallel)
        obviously because of the denominator
    - $\Braket{\vec{v}|\vec{w}}=-1$ ($\vec{v}, \vec{w}$ antiparallel)
        because then $\vec{v}'=\vec{w}'=\frac{1}{2}(\vec{w}+\vec{v})=\vec{0}$
    """
    if not N >= 2:
        raise ValueError('N must be ≥ 2')
    if not (M is None or M>=1):
        raise ValueError('M must be ≥ 1')
    
    v_arr = np.empty(((M if M is not None else 1), N), dtype=np.float64)
    w_arr = np.empty(((M if M is not None else 1), N), dtype=np.float64)
    i = 0
    while True:
        #random unit vectors
        v_arr[i,:], w_arr[i,:] = np.random.randn(N), np.random.randn(N)
        nv, nw = np.linalg.norm(v_arr[i,:]), np.linalg.norm(w_arr[i,:])
        if np.isclose(nv, 0) or np.isclose(nw, 0):
            continue
        v_arr[i,:] /= nv
        w_arr[i,:] /= nw
        
        #orthogonalise
        vw = v_arr[i,:] @ w_arr[i,:]
        if np.isclose(vw, +1) or np.isclose(vw, -1):
            continue
        a = (vw-1+np.sqrt(1-vw*vw)) / (2*(vw-1))
        d = a * (w_arr[i,:] - v_arr[i,:])
        v_arr[i,:] += d
        w_arr[i,:] -= d
        
        #normalise
        v_arr[i,:] /= np.linalg.norm(v_arr[i,:])
        w_arr[i,:] /= np.linalg.norm(w_arr[i,:])
        
        if M is None:
            return v_arr[0,:], w_arr[0,:]
        else:
            i += 1
            if i == M:
                return v_arr, w_arr
