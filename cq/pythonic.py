"""Pythonic helpers."""



from operator import pos, neg, add, sub, mul, truediv, floordiv, mod
from itertools import repeat, starmap, tee, zip_longest
from random import binomialvariate
from fractions import Fraction
from collections.abc import Iterable



__all__ = (
    'veczero', 'vecbasis',                                      #utility
    'vecpos', 'vecneg',                                         #unary
    'vecadd', 'vecsub',                                         #additive
    'vecmul', 'vecrmul', 'vectruediv', 'vecfloordiv', 'vecmod', #multiplicative
    'vecdot', 'vecabsq',                                        #Hilbert space
    'randz', 'randq', 'vrandz', 'vrandq', 'rand_ortho_pair'     #random
)



#vector space
veczero: tuple[()] = ()
"""Zero vector."""

def vecbasis(i: int) -> tuple[int, ...]:
    """Return the `i`-th canonical basis vector."""
    return (0,)*i + (1,)


def vecpos[T](v: Iterable[T]) -> tuple[T, ...]:
    """Return the affirmation of a vector."""
    return tuple(map(pos, v))

def vecneg[T](v: Iterable[T]) -> tuple[T, ...]:
    """Return the negation of a vector."""
    return tuple(map(neg, v))


def vecadd[T, U](v: Iterable[T], w: Iterable[U]) -> tuple[T|U, ...]:
    """Return the sum of two vectors."""
    return tuple(starmap(add, zip_longest(v, w, fillvalue=0)))

def vecsub[T, U](v: Iterable[T], w: Iterable[U]) -> tuple[T|U, ...]:
    """Return the difference of two vectors."""
    return tuple(starmap(sub, zip_longest(v, w, fillvalue=0)))


def vecmul[T, U](v: Iterable[T], a: U) -> tuple[T|U, ...]:
    """Return vector-scalar product."""
    return tuple(map(mul, v, repeat(a)))

def vecrmul[T, U](a: T, v:Iterable[U]) -> tuple[T|U, ...]:
    """Return scalar-vector product."""
    return tuple(map(mul, repeat(a), v))

def vectruediv[T, U](v: Iterable[T], a: U) -> tuple[T|U, ...]:
    """Return vector-scalar true quotient."""
    return tuple(map(truediv, v, repeat(a)))

def vecfloordiv[T, U](v: Iterable[T], a: U) -> tuple[T|U, ...]:
    """Return vector-scalar floor quotient."""
    return tuple(map(floordiv, v, repeat(a)))

def vecmod[T, U](v: Iterable[T], a: U) -> tuple[T|U, ...]:
    """Return vector-scalar remainder."""
    return tuple(map(mod, v, repeat(a)))


def vecdot[T, U](v: Iterable[T], w: Iterable[U]) -> T|U|int:
    """Return the real vector dot product."""
    return sum(map(mul, v, w))

def vecabsq[T](v: Iterable[T]) -> T:
    """Return the vector norm squared."""
    #tee for single exhaustible iterables
    return vecdot(*tee(v, 2))



#random
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
        Random value.
    
    See also
    --------
    - [`vrandz`][cq.pythonic.vrandz]
    
    References
    ----------
    - [`linalg.random.randz`](https://goessl.github.io/linalg/random/#linalg.random.randz)
    """
    if sigma < 0:
        raise ValueError('sigma must be non-negative')
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
        Random value.
    
    See also
    --------
    - [`vrandq`][cq.pythonic.vrandq]
    
    References
    ----------
    - [`linalg.random.randq`](https://goessl.github.io/linalg/random/#linalg.random.randq)
    """
    if grade <= 0:
        raise ValueError('grade must be positive')
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
        Random sample.
    
    See also
    --------
    - [`randz`][cq.pythonic.randz]
    
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
        Random sample.
    
    See also
    --------
    - [`randq`][cq.pythonic.randq]
    
    References
    ----------
    - [`linalg.random.vrandq`](https://goessl.github.io/linalg/random/#linalg.random.vrandq)
    """
    return tuple(randq(grade) for _ in range(N))


def rand_ortho_pair(N: int, grade: int=1000) \
        -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    r"""Return two orthogonal non-zero vectors.
    
    $$
        \vec{v}, \ \vec{w} \qquad ||\vec{v}||\neq0, \ ||\vec{w}||\neq0, \ \Braket{\vec{v}|\vec{w}}=0
    $$
    
    Parameters
    ----------
    N
        Length.
    
    Returns
    -------
        Vectors.
    """
    if N <= 1:
        raise ValueError('N must be ≥ 2')
    
    while True:
        v, w = vrandq(N, grade=100), vrandq(N, grade=100)
        
        #quick Gram-Schmidt
        va, wa = vecabsq(v), vecabsq(w)
        if va==0 or wa==0:
            continue
        w = vecsub(w, vecrmul(vecdot(v, w)/va, v))
        wa = vecabsq(w)
        if wa == 0:
            continue
        
        return v, w
