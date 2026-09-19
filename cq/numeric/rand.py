"""Random sampling."""



import numpy as np
from numpy.typing import NDArray



__all__ = (
    'rand_ortho_pair',
)



def _rand_ortho_pair(N: int, M: int) \
        -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    """Return up to M many orthonormal N dimensional vector pairs."""
    if not N >= 2:
        raise ValueError('N must be ≥ 2')
    if not M >= 1:
        raise ValueError('M must be ≥ 1')
    
    v, w = np.random.randn(2, M, N)
    
    va = np.linalg.norm(v, axis=-1)
    ok = ~np.isclose(va, 0)
    v, w, va = v[ok], w[ok], va[ok]
    v /= va[:, np.newaxis]
    
    w -= np.vecdot(v, w)[..., np.newaxis] * v
    wa = np.linalg.norm(w, axis=-1)
    ok = ~np.isclose(wa, 0)
    v, w, wa = v[ok], w[ok], wa[ok]
    w /= wa[:, np.newaxis]
    
    return v, w

def rand_ortho_pair(N: int, M: int|None=None) \
        -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    r"""Return orthonormal vector pairs.
    
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
    :
        Orthonormal vector pairs.
    
    See also
    --------
    - [`cq.symbolic.rand_ortho_pair`][cq.symbolic.rand.rand_ortho_pair]
    
    References
    ----------
    - [Wikipedia - Stiefel manifold - Uniform measure](https://en.wikipedia.org/wiki/Stiefel_manifold#Uniform_measure)
    """
    if not N >= 2:
        raise ValueError('N must be ≥ 2')
    if not (M is None or M>=1):
        raise ValueError('M must be None or ≥ 1')
    
    L = M or 1
    v_arr, w_arr = np.empty((2, L, N), dtype=np.float64)
    filled = 0
    while filled < L:
        v, w = _rand_ortho_pair(N, L-filled)
        v_arr[filled:filled+v.shape[0]] = v
        w_arr[filled:filled+w.shape[0]] = w
        filled += v.shape[0]
    
    return (v_arr[0,:], w_arr[0,:]) if M is None else (v_arr, w_arr)
