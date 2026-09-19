"""Polynomials."""



from warnings import warn
from typing import Any, Final, Self
from collections.abc import Generator
import numpy as np
from numpy.typing import ArrayLike, NDArray
from sklearn.preprocessing import PolynomialFeatures
from sympy import Symbol, Poly



__all__ = (
    'powers', 'transform', 'dimker', 'ImplicitPolynomial'
)



def powers(n_features: int, deg: int, degl: int|None=None, monic: bool=False) \
        -> NDArray[np.uint8]:
    r"""Return monomial exponents, optionally capped in the last feature.
    
    All monomials of total degree $\leq$ `deg`, keeping only those of
    degree $\leq$ `degl` in the last feature.
    
    Basically filterable `sklearn.preprocessing.PolynomialFeatures` `.powers_`.
    
    Parameters
    ----------
    n_features
        Number of features.
    deg
        Maximum total degree.
    degl
        Maximum degree in the last feature, or `None` for `deg`.
    monic
        If `True`, the last feature may reach `degl` only in the bare
        monomial $x_{n-1}^{\text{degl}}$, forcing a constant leading
        coefficient. With `degl=0` this leaves the constant monomial alone.
    
    Returns
    -------
    :
        Exponents, one monomial per row.
    
    See also
    --------
    - [`transform`][cq.numeric.poly.transform]
    - [`ImplicitPolynomial.fit`][cq.numeric.poly.ImplicitPolynomial.fit]
    """
    if not n_features >= 1:
        raise ValueError('n_features must be ≥ 1')
    degl = degl if degl is not None else deg
    if not 0 <= degl <= deg:
        raise ValueError('it must be 0 ≤ degl ≤ deg')
    
    p = PolynomialFeatures(degree=deg, include_bias=True) \
            .fit(np.zeros((1, n_features))).powers_
    
    if not monic:
        p = [e for e in p if e[-1]<=degl]
    else:
        p = [e for e in p
             if e[-1]<degl or e[-1]==degl and not e[:-1].any()]
    
    return np.array(p, np.uint8)

def transform(X: ArrayLike, pows: ArrayLike) -> NDArray[Any]:
    r"""Polynomial transform features to monomials.
    
    Basically `sklearn.preprocessing.PolynomialFeatures` `.transform`
    but with custom exponents and type agnostic.
    
    Parameters
    ----------
    X
        Features.
    pows
        Exponents.
    
    Returns
    -------
    :
        Monomials.
    
    See also
    --------
    - [`powers`][cq.numeric.poly.powers]
    - [`ImplicitPolynomial.fit`][cq.numeric.poly.ImplicitPolynomial.fit]
    """
    X, pows = np.asarray(X), np.asarray(pows)
    if not (X.ndim==2 and pows.ndim==2 and X.shape[1]==pows.shape[1]):
        raise ValueError('wrong shape')
    
    #return np.prod(X[:, np.newaxis, :] ** pows, axis=2)
    #more memory efficient:
    r = np.empty((X.shape[0], pows.shape[0]),
                 dtype=np.result_type(X, pows))
    for i, p in enumerate(pows):
        r[:,i] = np.prod(X ** p, axis=-1)
    return r

def dimker(A: ArrayLike) -> int:
    r"""Return the dimensionality of the kernel.
    
    $$
        \dim\ker A
    $$
    
    Uses SVD. Zero tolerance acc. to [`numpy.linalg.matrix_rank`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html).
    
    Parameters
    ----------
    A
        Matrix.
    
    Returns
    -------
    :
        Dimensionality of the kernel.
    
    References
    ----------
    - [`numpy.linalg.matrix_rank`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html)
    """
    A = np.asarray(A, np.float64)
    if not A.ndim == 2:
        raise ValueError('A must be two dimensional')
    S= np.linalg.svd(A, compute_uv=False)
    tol = S[0] * max(A.shape) * np.finfo(float).eps
    return A.shape[1] - sum(map(int, S>tol))

class ImplicitPolynomial:
    r"""Implicit polynomial.
    
    $$
        p(x_0, x_1, \dots, x_{\text{n_features}-1}) = 0
    $$
    
    Stores powers explicitly instead of [`sklearn.preprocessing.PolynomialFeatures`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html)
    such that minimal monomial sets can be explored.
    """
    pows: Final[NDArray[np.uint8]]
    coefs: Final[NDArray]
    
    @classmethod
    def fit(cls, X: ArrayLike, degree_or_powers: int|ArrayLike) \
            -> tuple[bool, tuple[Self, ...]]:
        """Return fitted `ImplicitPolynomial`s.
        
        Flag is `True` if a single polynomial converged.
        `False` if either none or more than one converged.
        
        If none converged, the best candidate is still returned.
        If one or more converged, all converged are returned.
        
        Parameters
        ----------
        X
            Samples.
        degree_or_powers
            Single degree in all features or predefined powers.
        
        Returns
        -------
        :
            Flag if unique fit converged and implicit polynomials.
        """
        X = np.asarray(X, dtype=np.float64)
        if X.ndim != 2:
            raise ValueError('malformed samples')
        
        if isinstance(degree_or_powers, (int, np.integer)):
            pows = powers(X.shape[1], degree_or_powers)
        else:
            pows = np.asarray(degree_or_powers, dtype=np.uint8)
            if not (pows.ndim==2 and pows.shape[1]==X.shape[1]):
                raise ValueError('malformed powers or coefficients')
        
        A = transform(X, pows)
        if X.shape[0] < pows.shape[0]:
            warn(f'less samples than coefficients to fit (coverage: {X.shape[0]/pows.shape[0]})', UserWarning, stacklevel=2)
        
        #keep singular values for diagnostics
        _, S, Vt = np.linalg.svd(A, full_matrices=A.shape[0]<A.shape[1])
        #https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_rank.html
        tol = S[0] * max(A.shape) * np.finfo(float).eps
        k = pows.shape[0] - sum(map(int, S>tol))
        if k == 0:
            warn(f'Fit didn\'t converge: {S[-1]}!', UserWarning, stacklevel=2)
            return False, (cls(pows, Vt[-1]),) #still return best candidate
        if k > 1:
            warn(f'Kernel dimensionality {k}; solution is not unique!',
                    UserWarning, stacklevel=2)
            return False, tuple(cls(pows, c) for c in reversed(Vt[-k:]))
        return True, (cls(pows, Vt[-1,:]),)
    
    
    def __init__(self, pows: ArrayLike, coefs: ArrayLike) -> None:
        pows, coefs = np.asarray(pows, np.uint8), np.asarray(coefs)
        if not (pows.ndim==2 and coefs.ndim==1 and pows.shape[0]==coefs.shape[0]):
            raise ValueError('malformed powers or coefficients')
        
        self.pows, self.coefs = pows, coefs
    
    def __call__(self, xyz: ArrayLike) -> NDArray:
        r"""Evaluate $p(x_0, x_1, \dots)$."""
        A = transform(np.asarray(xyz, dtype=np.float64), self.pows)
        return A @ self.coefs
    
    def reduce(self, X: ArrayLike, feature: int=-1) -> NDArray:
        """Substitute in features except one to get a univariate polynomial."""
        X = np.asarray(X)
        n = self.pows.shape[1]
        if not -n <= feature < n:
            raise ValueError('feature index out of range')
        
        monomials = self.coefs \
                * transform(X, np.delete(self.pows, feature, axis=1))
        degrees = self.pows[:, feature]
        return monomials @ (degrees[:, np.newaxis] == np.arange(np.max(degrees)+1))
    
    def items(self) -> Generator[tuple[tuple[int,...],float], None, None]:
        """Yield the terms like a `dict`."""
        for k, v in zip(self.pows, self.coefs, strict=True):
            yield tuple(map(int, k)), v
    
    def to_sympy(self, *gens: Symbol, trim: bool=True) -> Poly:
        """Return as a `sympy.Poly`."""
        return Poly.from_dict({
            k: v for k, v in self.items()
            if not trim or not np.isclose(v, 0)
        }, *gens)
