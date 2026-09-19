"""Random sampling."""



from sympy import sqrt, Matrix
from ..pythonic.vectors import vecabsq
from ..pythonic.rand import rand_ortho_pair as pyrop



__all__ = (
    'rand_ortho_pair',
)



def rand_ortho_pair(N: int, grade: int=1000) -> tuple[Matrix, Matrix]:
    r"""Return two random uniformly sampled orthonormal vectors.
    
    $$
        \vec{v}, \ \vec{w} \qquad ||\vec{v}||=||\vec{w}||=1, \ \Braket{\vec{v}|\vec{w}}=0
    $$
    
    Parameters
    ----------
    N
        Length.
    grade
        Denominator grading.
    
    Returns
    -------
    :
        Two random orthonormal vectors.
    
    See also
    --------
    - [`cq.numeric.rand_ortho_pair`][cq.numeric.rand.rand_ortho_pair]
    
    References
    ----------
    - [Wikipedia - Stiefel manifold - Uniform measure](https://en.wikipedia.org/wiki/Stiefel_manifold#Uniform_measure)
    """
    if not N >= 2:
        raise ValueError('N must be ≥ 2')
    
    v, w = pyrop(N, grade)
    va, wa = vecabsq(v), vecabsq(w)
    
    return Matrix(v) / sqrt(va), Matrix(w) / sqrt(wa)
