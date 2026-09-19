"""Random sampling.

Normal distribution like sampling with exact `int`s & `fractions.Fraction`s.

Currently copy & pasted from [`goessl/linalg`](https://goessl.github.io/linalg/)
to not have an additional package requirement.
"""



from random import binomialvariate
from fractions import Fraction
from .vectors import vecsub, vecrmul, vecabsq, vecdot



__all__ = (
    'randz', 'randq', 'vrandz', 'vrandq', 'rand_ortho_pair'
)



def randz(sigma: int=1000) -> int:
    r"""Return a random normal distributed integer.
    
    $$
        x \qquad x\in\mathbb{Z}, \ x\sim\mathcal{N}(0,\sigma)
    $$
    
    Parameters
    ----------
    sigma
        Standard deviation.
    
    Returns
    -------
    :
        Random value.
    
    See also
    --------
    - [`vrandz`][cq.pythonic.rand.vrandz]
    
    References
    ----------
    - [`linalg.random.randz`](https://goessl.github.io/linalg/random/#linalg.random.randz)
    """
    if not sigma >= 0:
        raise ValueError('sigma must be ≥ 0')
    return binomialvariate(4*sigma**2) - 2*sigma**2

def randq(grade: int=1000) -> Fraction:
    r"""Return a random normal distributed rational.
    
    $$
        x \qquad x\in\mathbb{Q}, \ x\sim\mathcal{N}(0,1)
    $$
    
    Parameters
    ----------
    grade
        Denominator grading.
    
    Returns
    -------
    :
        Random value.
    
    See also
    --------
    - [`vrandq`][cq.pythonic.rand.vrandq]
    
    References
    ----------
    - [`linalg.random.randq`](https://goessl.github.io/linalg/random/#linalg.random.randq)
    """
    if not grade > 0:
        raise ValueError('grade must be > 0')
    return Fraction(randz(grade), grade)

def vrandz(N: int, sigma: int=1000) -> tuple[int, ...]:
    r"""Return a tuple of normally distributed integers.
    
    $$
        \vec{v} \qquad \vec{v}\in\mathbb{Z}^\text{shape}, \ \vec{v}\sim\mathcal{N}(0,\sigma)^\text{shape}
    $$
    
    Parameters
    ----------
    N
        Length.
    sigma
        Standard deviation.
    
    Returns
    -------
    :
        Random sample.
    
    See also
    --------
    - [`randz`][cq.pythonic.rand.randz]
    
    References
    ----------
    - [`linalg.random.vrandz`](https://goessl.github.io/linalg/random/#linalg.random.vrandz)
    """
    return tuple(randz(sigma) for _ in range(N))

def vrandq(N: int, grade: int=1000) -> tuple[Fraction, ...]:
    r"""Return a tuple of normally distributed rationals.
    
    $$
        \vec{v} \qquad \vec{v}\in\mathbb{Q}^\text{shape}, \ \vec{v}\sim\mathcal{N}(0,1)^\text{shape}
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
        Random sample.
    
    See also
    --------
    - [`randq`][cq.pythonic.rand.randq]
    
    References
    ----------
    - [`linalg.random.vrandq`](https://goessl.github.io/linalg/random/#linalg.random.vrandq)
    """
    return tuple(randq(grade) for _ in range(N))


def rand_ortho_pair(N: int, grade: int=1000) \
        -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    r"""Return two random uniformly sampled orthogonal non-zero vectors.
    
    $$
        \vec{v}, \ \vec{w} \qquad ||\vec{v}||\neq0, \ ||\vec{w}||\neq0, \ \Braket{\vec{v}|\vec{w}}=0
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
        Vectors.
    
    See also
    --------
    - [`cq.pythonic.vrandq`][cq.pythonic.rand.vrandq]
    
    References
    ----------
    - [Wikipedia - Stiefel manifold - Uniform measure](https://en.wikipedia.org/wiki/Stiefel_manifold#Uniform_measure)
    """
    if not N >= 2:
        raise ValueError('N must be ≥ 2')
    
    while True:
        v, w = vrandq(N, grade=grade), vrandq(N, grade=grade)
        
        #quick Gram-Schmidt
        va = vecabsq(v)
        if va == 0:
            continue
        w = vecsub(w, vecrmul(vecdot(v, w)/va, v))
        wa = vecabsq(w)
        if wa == 0:
            continue
        
        return v, w
