"""Quantum mechanics."""



import numpy as np
from numpy.typing import ArrayLike, NDArray
from .hermf import hermfpmul_coeffs



__all__ = (
    'states_to_density', 'T_matrix', 'rho_to_T', 'rho_to_g'
)



def states_to_density(*states: ArrayLike) -> NDArray:
    r"""Return the density matrix for an ensemble of state vectors.
    
    $$
        \sum_i\vec{v}_i\vec{v}_i^\dagger
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
    - [`cq.symbolic.states_to_density`][cq.symbolic.qm.states_to_density]
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
    :
        $T$ matrix.
    
    See also
    --------
    - [`hermfkin`][cq.numeric.hermf.hermfkin]
    - [`rho_to_T`][cq.numeric.qm.rho_to_T]
    - [`cq.symbolic.T_matrix`][cq.symbolic.qm.T_matrix]
    """
    T = np.zeros((D+1, D+1), dtype=np.float64)
    
    i = np.arange(D+1)
    np.fill_diagonal(T, (2*i+1)/4)
    i = i[:max(D-1, 0)]
    off_diagonal = -np.sqrt((i+1)*(i+2)) / 4
    np.fill_diagonal(T[:, 2:], off_diagonal)
    np.fill_diagonal(T[2:, :], off_diagonal)
    
    return T

def rho_to_T(rho: ArrayLike) -> np.float64|NDArray:
    r"""Return the kinetic energy of (a) density matrix/matrices.
    
    $$
        \text{tr}\,\rho T
    $$
    
    More efficient than `(rho@T_matrix(rho.shape[-1]-1)).trace()`.
    
    Parameters
    ----------
    rho
        Density matrix/matrices in Hermite function basis
        as a 2D array or multiple density matrices stacked in a 3D array.
    
    Returns
    -------
    :
        Kinetic energy/energies.
    
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
    - [`hermfkin`][cq.numeric.hermf.hermfkin]
    - [`T_matrix`][cq.numeric.qm.T_matrix]
    - [`cq.symbolic.rho_to_T`][cq.symbolic.qm.rho_to_T]
    """
    rho = np.asarray(rho)
    if rho.ndim not in {2, 3}:
        raise ValueError('rho must be two or three dimensional')
    if rho.shape[-1] != rho.shape[-2]:
        raise ValueError('rho must be square')
    
    d0 = np.diagonal(rho, 0, -2, -1)
    dp, dm = np.diagonal(rho, 2, -2, -1), np.diagonal(rho, -2, -2, -1)
    i, k = np.arange(d0.shape[-1]), np.arange(dp.shape[-1])
    return (d0 @ (2*i+1) - (dp+dm) @ np.sqrt((k+1)*(k+2))) / 4

def rho_to_g(rho: ArrayLike) -> NDArray:
    r"""Return $\vec{g}$ for density matrix $\rho$.
    
    TODO: Stabilise for higher degrees.
    
    Parameters
    ----------
    rho
        Density matrix as a 2D array
        or multiple density matrices stacked in a 3D array.
    
    Returns
    -------
    :
        Coefficient vector(s).
    
    See also
    --------
    - [`hermfpmul`][cq.numeric.hermf.hermfpmul]
    - [`cq.symbolic.rho_to_g`][cq.symbolic.qm.rho_to_g]
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
