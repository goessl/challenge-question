"""Hermite functions."""



from math import factorial, comb
from itertools import chain
from collections.abc import Iterable, Sequence
from sympy import S, Expr, pi, sqrt, exp, Rational, Matrix, zeros, hermite
from sympy.abc import x
from ..pythonic.vectors import vecabsq



__all__ = (
    'hermf', 'hermfexpr', 'hermfder', 'hermfkin', 'hermfpmul'
)



def hermf(j: int) -> Expr:
    """Return the `j`-th Hermite function as `sympy.Expr` in `sympy.abc.x`.
    
    Parameters
    ----------
    j
        Index.
    
    Returns
    -------
    :
        $j$-th Hermite function.
    
    See also
    --------
    - [`hermfexpr`][cq.symbolic.hermf.hermfexpr]
    
    References
    ----------
    - [Wikipedia - Hermite polynomials - Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions)
    """
    return exp(-x**2/2) * hermite(j, x) / sqrt(2**j * factorial(j) * sqrt(pi))

def hermfexpr(f: Iterable) -> Expr:
    """Return the given coefficients as a Hermite function series expression.
    
    Parameters
    ----------
    f
        Coefficients.
    
    Returns
    -------
    :
        Hermite function series expression in `sympy.abc.x`.
    
    See also
    --------
    - [`hermf`][cq.symbolic.hermf.hermf]
    - [`numeric.hermfval`][cq.numeric.hermf.hermfval]
    
    References
    ----------
    - [Wikipedia - Hermite polynomials - Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions)
    """
    return sum((fi*hermf(i) for i, fi in enumerate(f)), S.Zero)

def hermfder(f: Sequence) -> Matrix:
    r"""Return the derivative of a Hermite function series.
    
    $$
        f'
    $$
    
    Parameters
    ----------
    f
        Hermite function series.
    
    Returns
    -------
    :
        Derivative.
    
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
    
    See also
    --------
    - [`hermfkin`][cq.symbolic.hermf.hermfkin]
    - [`numeric.hermfder`][cq.numeric.hermf.hermfder]
    
    References
    ----------
    - [Wikipedia - Hermite polynomials - Recursion relation](https://en.wikipedia.org/wiki/Hermite_polynomials#Recursion_relation)
    """
    return Matrix([
            fkp1*sqrt(Rational(k+1, 2)) - fkm1*sqrt(Rational(k, 2))
            for k, (fkp1, fkm1) in
            enumerate(zip(chain(f[1:], [0, 0]), chain([0], f)))
    ])

def hermfkin(f: Sequence) -> Expr:
    r"""Return the kinetic energy of a Hermite function series.
    
    $$
        T[f] = -\frac{1}{2}\int_\mathbb{R}f''(x)f(x)\,\mathrm{d}x = +\frac{1}{2}\int_\mathbb{R}f'(x)^2\,\mathrm{d}x = \frac{||f'||_{L_\mathbb{R}^2}^2}{2}
    $$
    
    TODO: Complex conjugation.
    
    Parameters
    ----------
    f
        Hermite function series.
    
    Returns
    -------
    :
        Kinetic energy.
    
    See also
    --------
    - [`hermfder`][cq.symbolic.hermf.hermfder]
    - [`numeric.hermfkin`][cq.numeric.hermf.hermfkin]
    """
    return vecabsq(hermfder(f)) / 2

def hermfpmul(f: Sequence, g: Sequence) -> Matrix:
    r"""Return the pseudo product of two Hermite function series.
    
    $$
        m \qquad fg=mh_0, \ m=\sum_jm_jh_j
    $$
    
    Parameters
    ----------
    f, g
        Hermite function series.
    
    Returns
    -------
    :
        Pseudo product.
    
    Notes
    -----
    $$
        \begin{aligned}
            &h_i(x)h_j(x) &&\mid h_j(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x) \\
            &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}}H_i(x)H_j(x) &&\mid H_iH_j=\sum_{k=0}^{\min\{i,j\}}2^kk!\binom{i}{k}\binom{j}{k}H_{i+j-2k} \\
            &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}}\sum_{k=0}^{\min\{i,j\}}2^kk!\binom{i}{k}\binom{j}{k}H_{i+j-2k}(x) &&\mid h_k(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^kk!\sqrt{\pi}}}H_k(x) \\
            &= \frac{e^{-\frac{x^2}{2}}}{\sqrt{i!j!\sqrt{\pi}}}\sum_{k=0}^{\min\{i,j\}}k!\binom{i}{k}\binom{j}{k}\sqrt{(i+j-2k)!}h_{i+j-2k}(x) &&\mid h_0(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}} \\
            &= h_0(x)\sum_{k=0}^{\min\{i,j\}}k!\binom{i}{k}\binom{j}{k}\sqrt{\frac{(i+j-2k)!}{i!j!}}h_{i+j-2k}(x) \\
            &= h_0(x)\sum_{k=0}^{\min\{i,j\}}\frac{\sqrt{i!j!(i+j-2k)!}}{k!(i-k)!(j-k)!}h_{i+j-2k}(x)
        \end{aligned}
    $$
    
    Reference implementation
    
    ```python
    def hermfmul(f: Sequence, g: Sequence) -> list:
        r = [0] * (len(f)+len(g)-1)
        for i, fi in enumerate(f):
            for j, gj in enumerate(g):
                for k in range(min(i, j)+1):
                    r[i+j-2*k] += fi * gj \
                            * factorial(k)*comb(i, k)*comb(j, k) \
                            * sqrt(factorial(i+j-2*k) \
                            / (factorial(i)*factorial(j)))
        return r
    ```
    
    See also
    --------
    - [`numeric.hermfpmul`][cq.numeric.hermf.hermfpmul]
    """
    r = zeros(max(len(f)+len(g)-1, 0), 1)
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            for k in range(min(i, j)+1):
                r[i+j-2*k] += fi * gj \
                        * factorial(k)*comb(i, k)*comb(j, k) \
                        * sqrt(Rational(factorial(i+j-2*k),
                                             (factorial(i)*factorial(j))))
    return r
