"""Symbolic helpers."""



from math import factorial, comb
from itertools import chain
from .pythonic import vecbasis, vecsub, vecrmul, vecdot, vecabsq, vrandq
import sympy as sp
from sympy.abc import x as spx
from collections.abc import Iterable, Sequence



__all__ = (
    'symbol_matrix', 'symbol_matrix_symmetric',
    'hermf', 'hermfexpr', 'hermfder', 'hermfkin', 'hermfpmul',
    'states_to_density', 'T_matrix', 'rho_to_g',
    'linear_solutions',
    'rand_ortho_pair'
)



#sympy
def symbol_matrix(sym: str, height: int, width: int) -> sp.Matrix:
    """Return a matrix with the given symbol indexed as coefficients."""
    if height>10 or width>10:
        raise NotImplementedError('possible index ambiguity')
    return sp.Matrix([[sp.Symbol(f'{sym}{i}{j}') for j in range(width)] for i in range(height)])

def symbol_matrix_symmetric(sym: str, hw: int) -> sp.Matrix:
    """Return a symmetric matrix with the given symbol indexed as coefficients."""
    if hw > 10:
        raise NotImplementedError('possible index ambiguity')
    return sp.Matrix([[sp.Symbol(f'{sym}{min(i, j)}{max(i, j)}') for j in range(hw)] for i in range(hw)])



#Hermite functions
def hermf(j: int) -> sp.Expr:
    """Return the `j`-th Hermite function as `sympy.Expr` in `sympy.abc.x`."""
    return sp.exp(-spx**2/2) * sp.hermite(j, spx) / sp.sqrt(2**j * factorial(j) * sp.sqrt(sp.pi))

def hermfexpr(f: Iterable) -> sp.Expr:
    """Return the Hermite function series as `sympy.Expr` in `sympy.abc.x`."""
    return sum((fi*hermf(i) for i, fi in enumerate(f)), sp.Integer(0))

def hermfder(f: Sequence) -> sp.Matrix:
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
    return sp.Matrix([
            fkp1*sp.sqrt(sp.Rational(k+1, 2)) - fkm1*sp.sqrt(sp.Rational(k, 2))
            for k, (fkp1, fkm1) in
            enumerate(zip(chain(f[1:], [0, 0]), chain([0], f)))
    ])

def hermfkin(f: Sequence) -> sp.Expr:
    r"""Return the kinetic energy of `f`.
    
    $$
        T[f] = -\frac{1}{2}\int_\mathbb{R}f''(x)f(x)\,\mathrm{d}x = +\frac{1}{2}\int_\mathbb{R}f'(x)^2\,\mathrm{d}x = \frac{||f'||_{L_\mathbb{R}^2}^2}{2}
    $$
    """
    return vecabsq(hermfder(f)) / 2

def hermfpmul(f: sp.Matrix, g: sp.Matrix) -> sp.Matrix:
    """Return $m$, such that $mh_0=fg$.
    
    $f$, $g$ & $m$ are sequences of coefficients
    representing Hermite function series.
    """
    r = sp.zeros(len(f)+len(g)-1, 1)
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            for k in range(min(i, j)+1):
                r[i+j-2*k] += fi * gj \
                        * factorial(k)*comb(i, k)*comb(j, k) \
                        * sp.sqrt(sp.Rational(factorial(i+j-2*k),
                                             (factorial(i)*factorial(j))))
    return r



#quantum mechanics
def states_to_density(state: sp.Matrix, *others: sp.Matrix) -> sp.Matrix:
    """Return the density matrix for an ensemble of state vectors."""
    if not (all(s.shape[1]==1 for s in (state, *others)) \
            and len(set(s.shape[0] for s in (state, *others))) == 1):
        raise ValueError('states must be vectors and of same length')
    
    return sum((o*o.T for o in others), state*state.T)

def T_matrix(D: int) -> sp.Matrix:
    """Return the matrix representation of T in Hermite function to degree D."""
    T = sp.zeros(D+1, D+1)
    for i in range(D+1):
        T[i, i] = sp.Rational(2*i + 1, 4)
    for i in range(D-1):
        T[i, i+2] = T[i+2, i] = -sp.sqrt((i+1)*(i+2)) / 4
    return T

def rho_to_g(rho: sp.Matrix) -> sp.Matrix:
    r"""Return the $\vec{g}$ of some $\rho$."""
    g = sp.zeros(rho.shape[0]+rho.shape[1]-1, 1)
    for i in range(rho.shape[0]):
        for j in range(rho.shape[1]):
            hi, hj = vecbasis(i), vecbasis(j)
            hihj = hermfpmul(hi, hj)
            g[:hihj.shape[0], 0] += rho[i, j] * hihj
    return g



#solvers
def linear_solutions(p: sp.Poly, *t: sp.Symbol) -> sp.Matrix:
    """Return parametrised linear solution set.
    
    Returns $x$ for $ax+b=0$
    and $x$, $y$ for ax+by+c=0.
    """
    if not isinstance(p, sp.Poly):
        raise TypeError('p must be a sympy.Poly in the symbols to solve')
    if not len(t) == len(p.gens)-1:
        raise ValueError('one less free parameter than generators must be provided')
    
    d = p.as_dict()
    match len(p.gens):
        case 1: #ax+b=0
            if not d.keys() <= {(0,), (1,)}:
                raise ValueError('p is not linear')
            return sp.Matrix([p.root(0).simplify()])
        
        case 2: #ax+by+c=0
            if not d.keys() <= {(0,0), (0,1), (1,0)}:
                raise ValueError('p is not linear')
            
            a = d.get((1,0), sp.Integer(0))
            b = d.get((0,1), sp.Integer(0))
            c = d.get((0,0), sp.Integer(0))
            x = (-a*c/(a**2+b**2)+b*t[0]).simplify()
            y = (-b*c/(a**2+b**2)-a*t[0]).simplify()
            return sp.Matrix([x, y])
        
        case _:
            raise NotImplementedError("higher dimension not yet implemented")



#random
def rand_ortho_pair(N: int, grade: int=1000) -> tuple[sp.Matrix, sp.Matrix]:
    r"""Return two orthonormal vectors.
    
    $$
        \vec{v}, \ \vec{w} \qquad ||\vec{v}||=||\vec{w}||=1, \ \Braket{\vec{v}|\vec{w}}=0
    $$
    
    Parameters
    ----------
    N
        Length.
    
    Returns
    -------
        Vectors.
    
    Notes
    -----
    TODO:
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
    if N <= 1:
        raise ValueError('N must be ≥ 2')
    
    #stay pythonic as long as possible because sympy is even slower
    while True:
        #random vectors
        v, w = vrandq(N, grade), vrandq(N, grade)
        va, wa = vecabsq(v), vecabsq(w)
        if va==0 or wa==0:
            continue
        
        w = vecsub(w, vecrmul(vecdot(v, w)/va, v))
        wa = vecabsq(w)
        if wa == 0:
            continue
        
        #normalise
        v = sp.Matrix(v) / sp.sqrt(va)
        w = sp.Matrix(w) / sp.sqrt(wa)
        
        return v, w
