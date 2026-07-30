"""Pythonic helpers."""



from operator import pos, neg, add, sub, mul, truediv, floordiv, mod
from itertools import repeat, starmap, tee, zip_longest
from random import binomialvariate
from typing import Any, TypeVar
from collections.abc import Iterable



__all__ = (
    'veczero', 'vecbasis',                                      #utility
    'vecpos', 'vecneg',                                         #unary
    'vecadd', 'vecsub',                                         #additive
    'vecmul', 'vecrmul', 'vectruediv', 'vecfloordiv', 'vecmod', #multiplicative
    'vecdot', 'vecabsq',                                        #Hilbert space
    'binom', 'vbinom'                                           #random
)



T = TypeVar('T')



#vector space
veczero:tuple[()] = ()
"""Zero vector."""

def vecbasis(i:int) -> tuple[int,...]:
    """Return the `i`-th canonical basis vector."""
    return (0,)*i + (1,)


def vecpos(v:Iterable[T]) -> tuple[T,...]:
    """Return the affirmation of a vector."""
    return tuple(map(pos, v))

def vecneg(v:Iterable[T]) -> tuple[T,...]:
    """Return the negation of a vector."""
    return tuple(map(neg, v))


def vecadd(v:Iterable[T], w:Iterable[T]) -> tuple[T,...]:
    """Return the sum of two vectors."""
    return tuple(starmap(add, zip_longest(v, w, fillvalue=0)))

def vecsub(v:Iterable[T], w:Iterable[T]) -> tuple[T,...]:
    """Return the difference of two vectors."""
    return tuple(starmap(sub, zip_longest(v, w, fillvalue=0)))


def vecmul(v:Iterable[Any], a:Any) -> tuple[Any,...]:
    """Return vector-scalar product."""
    return tuple(map(mul, v, repeat(a)))

def vecrmul(a:Any, v:Iterable[Any]) -> tuple[Any,...]:
    """Return scalar-vector product."""
    return tuple(map(mul, repeat(a), v))

def vectruediv(v:Iterable[Any], a:Any) -> tuple[Any,...]:
    """Return vector-scalar true quotient."""
    return tuple(map(truediv, v, repeat(a)))

def vecfloordiv(v:Iterable[Any], a:Any) -> tuple[Any,...]:
    """Return vector-scalar floor quotient."""
    return tuple(map(floordiv, v, repeat(a)))

def vecmod(v:Iterable[Any], a:Any) -> tuple[Any,...]:
    """Return vector-scalar remainder."""
    return tuple(map(mod, v, repeat(a)))


def vecdot(v:Iterable[T], w:Iterable[T]) -> T|int:
    """Return the real vector dot product."""
    return sum(map(mul, v, w))

def vecabsq(v:Iterable[T]) -> T:
    """Return the vector norm squared."""
    #tee for single exhaustible iterables
    return vecdot(*tee(v, 2))



#random
def binom(sigma:int=1000) -> int:
    """Return a random binomial distributed integer with mean 0 and std sigma."""
    return binomialvariate(4*sigma**2) - 2*sigma**2

def vbinom(N:int, sigma:int=1000) -> tuple[int,...]:
    """Return a random binomial distributed integer with mean 0 and std sigma."""
    return tuple(binom(sigma) for _ in range(N))
