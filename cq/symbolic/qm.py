"""Quantum mechanics."""



from sympy import S, sqrt, Rational, Matrix, zeros, Expr
from ..pythonic.vectors import vecbasis
from .hermf import hermfpmul



__all__ = (
    'states_to_density', 'T_matrix', 'rho_to_T', 'rho_to_g'
)



def states_to_density(*states: Matrix) -> Matrix:
    r"""Return the density matrix for an ensemble of state vectors.
    
    $$
        \sum_i\vec{v}_i\vec{v}_i^T
    $$
    
    Parameters
    ----------
    states
        States as vectors of same length.
    
    Returns
    -------
    :
        Density matrix.
    
    See also
    --------
    - [`cq.numeric.states_to_density`][cq.numeric.qm.states_to_density]
    """
    if not states:
        raise ValueError('requiring at least one state')
    l = {s.shape[0] for s in states}
    if not (all(s.shape[1]==1 for s in states) and len(l)==1):
        raise ValueError('states must be vectors and of same length')
    l = next(iter(l))
    
    return sum((s*s.T for s in states), zeros(l, l))

def T_matrix(D: int) -> Matrix:
    r"""Return the matrix representation of $\hat{T}$.
    
    In Hermite function series as basis.
    
    Parameters
    ----------
    D
        Degree.
    
    Returns
    -------
    :
        $T$ matrix.
    
    See also
    --------
    - [`hermfkin`][cq.symbolic.hermf.hermfkin]
    - [`rho_to_T`][cq.symbolic.qm.rho_to_T]
    - [`cq.numeric.T_matrix`][cq.numeric.qm.T_matrix]
    """
    T = zeros(D+1, D+1)
    for i in range(D+1):
        T[i, i] = Rational(2*i + 1, 4)
    for i in range(D-1):
        T[i, i+2] = T[i+2, i] = -sqrt((i+1)*(i+2)) / 4
    return T

def rho_to_T(rho: Matrix) -> Expr:
    r"""Return the kinetic energy of a density matrix.
    
    $$
        \text{tr}\,\rho T
    $$
    
    More efficient than `(rho@T_matrix(rho.shape[1]-1)).trace()`.
    
    TODO: Generalise to non-square matrices.
    
    Parameters
    ----------
    rho
        Density matrix in Hermite function basis.
    
    Returns
    -------
    :
        Kinetic energy.
    
    Notes
    -----
    $$
        \begin{aligned}
            \text{tr}\,\rho T &= \sum_i(\rho T)_{ii} \\
            &= \sum_i\sum_j\rho_{ij}T_{ji} &&\mid T_{ji}=0 \ \forall \ j\notin\{i-2,i,i+2\} \\
            &= \sum_i\left(\rho_{i,i-2}T_{i-2,i}+\rho_{ii}T_{ii}+\rho_{i,i+2}T_{i+2,i}\right) \\
            &\qquad\mid T_{ii}=\frac{2i+1}{4}, \ T_{i,i+2}=T_{i+2,i}=-\frac{\sqrt{(i+1)(i+2)}}{4} \\
            &= \frac{1}{4}\left(\sum_{i=0}^D(2i+1)\rho_{ii}
                - \sum_{i=2}^D\sqrt{(i-1)i}\,\rho_{i,i-2}
                - \sum_{i=0}^{D-2}\sqrt{(i+1)(i+2)}\,\rho_{i,i+2}\right) \\
            &\qquad\mid i\to i+2 \text{ in the second sum} \\
            &= \frac{1}{4}\left(\sum_{i=0}^D(2i+1)\rho_{ii}
                - \sum_{i=0}^{D-2}\sqrt{(i+1)(i+2)}\left(\rho_{i+2,i}+\rho_{i,i+2}\right)\right)
        \end{aligned}
    $$
    
    See also
    --------
    - [`hermfkin`][cq.symbolic.hermf.hermfkin]
    - [`T_matrix`][cq.symbolic.qm.T_matrix]
    - [`cq.numeric.rho_to_T`][cq.numeric.qm.rho_to_T]
    """
    if rho.shape[0] != rho.shape[1]:
        raise ValueError('rho must be square')
    D1 = rho.shape[0]
    
    return sum((Rational(2*i+1, 4) * rho[i, i] for i in range(D1)), S.Zero) \
         - sum((sqrt((i+1)*(i+2)) * (rho[i, i+2] + rho[i+2, i]) / 4
                for i in range(D1-2)), S.Zero)

def rho_to_g(rho: Matrix) -> Matrix:
    r"""Return $\vec{g}$ for density matrix $\rho$.
    
    Parameters
    ----------
    rho
        Density matrix.
    
    Returns
    -------
    :
        Coefficient vector.
    
    See also
    --------
    - [`hermfpmul`][cq.symbolic.hermf.hermfpmul]
    - [`cq.numeric.rho_to_g`][cq.numeric.qm.rho_to_g]
    """
    g = zeros(rho.shape[0]+rho.shape[1]-1, 1)
    for i in range(rho.shape[0]):
        for j in range(rho.shape[1]):
            hi, hj = vecbasis(i), vecbasis(j)
            hihj = hermfpmul(hi, hj)
            g[:hihj.shape[0], 0] += rho[i, j] * hihj
    return g
