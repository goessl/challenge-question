"""Vector & Hilbert spaces.

All functions take vectors as `Iterable`s and return vectors as `tuple`s.

Vectors are interpreted as of infinite length,
for which `int(0)`s may be appended.

Simplified subset of [`goessl/vector`](https://goessl.github.io/vector/).
"""



from operator import pos, neg, add, sub, mul, truediv, floordiv, mod
from itertools import repeat, starmap, tee, zip_longest
from typing import Any
from collections.abc import Iterable



__all__ = (
    'veczero', 'vecbasis',                                      #utility
    'vecpos', 'vecneg',                                         #unary
    'vecadd', 'vecsub',                                         #additive
    'vecmul', 'vecrmul', 'vectruediv', 'vecfloordiv', 'vecmod', #multiplicative
    'vecdot', 'vecabsq'                                         #Hilbert space
)



veczero: tuple[()] = ()
r"""Zero vector.

$$
    \vec{0}
$$

Notes
-----
An empty `tuple`.
"""

def vecbasis(i: int) -> tuple[int, ...]:
    r"""Return a canonical basis vector.
    
    $$
        \vec{e}_i = \begin{pmatrix}
            \delta_{ij}
        \end{pmatrix}_{j\in\{0, 1, \dots, i\}}
    $$
    
    Parameters
    ----------
    i
        Index.
    
    Returns
    -------
    :
        The $i$-th canonical basis vector.
    
    Notes
    -----
    Zero indexed. Result is of length `i+1`.
    """
    return (0,)*i + (1,)


def vecpos(v: Iterable) -> tuple[Any, ...]:
    r"""Return the affirmation.
    
    $$
        +\vec{v} = \begin{pmatrix}
            +v_j
        \end{pmatrix}_j
    $$
    """
    return tuple(map(pos, v))

def vecneg(v: Iterable) -> tuple[Any, ...]:
    r"""Return the negation.
    
    $$
        -\vec{v} = \begin{pmatrix}
            -v_j
        \end{pmatrix}_j
    $$
    """
    return tuple(map(neg, v))


def vecadd(v: Iterable, w: Iterable) -> tuple[Any, ...]:
    r"""Return the sum.
    
    $$
        \vec{v}+\vec{w} = \begin{pmatrix}
            v_j+w_j
        \end{pmatrix}_j
    $$
    """
    return tuple(starmap(add, zip_longest(v, w, fillvalue=0)))

def vecsub(v: Iterable, w: Iterable) -> tuple[Any, ...]:
    r"""Return the difference.
    
    $$
        \vec{v}-\vec{w} = \begin{pmatrix}
            v_j-w_j
        \end{pmatrix}_j
    $$
    """
    return tuple(starmap(sub, zip_longest(v, w, fillvalue=0)))


def vecmul(v: Iterable, a: Any) -> tuple[Any, ...]:
    r"""Return the product.
    
    $$
        \vec{v}a = \begin{pmatrix}
            v_ja
        \end{pmatrix}_j
    $$
    """
    return tuple(map(mul, v, repeat(a)))

def vecrmul(a: Any, v:Iterable) -> tuple[Any, ...]:
    r"""Return the product.
    
    $$
        a\vec{v} = \begin{pmatrix}
            av_j
        \end{pmatrix}_j
    $$
    """
    return tuple(map(mul, repeat(a), v))

def vectruediv(v: Iterable, a: Any) -> tuple[Any, ...]:
    r"""Return the true quotient.
    
    $$
        \frac{\vec{v}}{a} = \begin{pmatrix}
            \frac{v_j}{a}
        \end{pmatrix}_j
    $$
    """
    return tuple(map(truediv, v, repeat(a)))

def vecfloordiv(v: Iterable, a: Any) -> tuple[Any, ...]:
    r"""Return the floor quotient.
    
    $$
        \left\lfloor\frac{\vec{v}}{a}\right\rfloor = \begin{pmatrix}
            \left\lfloor\frac{v_j}{a}\right\rfloor
        \end{pmatrix}_j
    $$
    """
    return tuple(map(floordiv, v, repeat(a)))

def vecmod(v: Iterable, a: Any) -> tuple[Any, ...]:
    """Return vector-scalar remainder."""
    return tuple(map(mod, v, repeat(a)))


def vecdot(v: Iterable, w: Iterable) -> Any:
    r"""Return the real inner product.
    
    $$
        \Braket{\vec{v}|\vec{w}} = \sum_jv_jw_j
    $$
    """
    return sum(map(mul, v, w))

def vecabsq(v: Iterable) -> Any:
    r"""Return the real norm squared.
    
    $$
        ||\vec{v}||^2 = \sum_jv_j^2
    $$
    """
    #tee for single exhaustible iterables
    return vecdot(*tee(v, 2))
