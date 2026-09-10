# Series Representation Where There Shouldn't Be One

Damn, but that ([the last site](oh_look_a_polynomial.md)) would have wild implications:
We all still know from kindergarden that $L^2(\mathbb{R})$ is the only $L^p(\mathbb{R})$ space that admits an inner product and is the only Hilbert space.
So one could expect that we can work with the wavefunctions as elements of a Hilbert space ($L^2(\mathbb{R})$) but the probability density distribution ($L^1(\mathbb{R})$) isn't.

But no, dear reader, don't despair, the probability density function (at least ours) has actually a finite vector representation via the polynomials. Now we just make it a little more natural:

We use the Hermite functions as basis for the wavefunctions, and for $n$ we jam half of the Gaussian and $\sqrt{\pi}$ factors back into the polynomial to also be a Hermite function series.

## Products of Hermite polynomials

From [HermitePolynomialsAndHermiteFunctions.pdf (ncatlab.org)](https://ncatlab.org/nlab/files/HermitePolynomialsAndHermiteFunctions.pdf) eq. A.8 we know that

$$
    \tilde{H}_i\tilde{H}_j = \sum_{k=0}^{\min\{i,j\}}k!\binom{i}{k}\binom{j}{k}\tilde{H}_{i+j-2k}.
$$

Therefore we have

$$
    \begin{aligned}
        &H_i(x)H_j(x) &&\mid H_j(x) = 2^\frac{j}{2}\tilde{H}_j(\sqrt{2}x) \\
        &= 2^\frac{i+j}{2} \tilde{H}_i(\sqrt{2}x) \tilde{H}_j(\sqrt{2}x) &&\mid \tilde{H}_i\tilde{H}_j = \sum_{k=0}^{\min\{i, j\}}k!\binom{i}{k}\binom{j}{k}\tilde{H}_{i+j-2k} \\
        &= 2^\frac{i+j}{2} \sum_{k=0}^{\min\{i, j\}} k!\binom{i}{k}\binom{j}{k} \tilde{H}_{i+j-2k}(\sqrt{2}x) &&\mid \cdot1=2^{k-k} \\
        &= \sum_{k=0}^{\min\{i, j\}} 2^kk!\binom{i}{k}\binom{j}{k}2^\frac{i+j-2k}{2} \tilde{H}_{i+j-2k}(\sqrt{2}x) &&\mid H_j(x)=2^\frac{j}{2} \tilde{H}_j(\sqrt{2}x) \\
        &= \sum_{k=0}^{\min\{i, j\}}2^kk!\binom{i}{k}\binom{j}{k} H_{i+j-2k}(x)
    \end{aligned}
$$

## Products of Hermite functions

Further for Hermite functions:

$$
    \begin{aligned}
        &h_i(x)h_j(x) &&\mid h_j(x) = \frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x) \\
        &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}} H_i(x)H_j(x) &&\mid H_iH_j = \sum_{k=0}^{\min{i,j}}2^kk!\binom{i}{k}\binom{j}{k}H_{i+j-2k} \\
        &= \frac{e^{-x^2}}{\sqrt{2^{i+j}i!j!\pi}}\sum_{k=0}^{\min{i,j}} 2^kk!\binom{i}{k}\binom{j}{k} H_{i+j-2k}(x) &&\mid h_k(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^kk!\sqrt{\pi}}}H_k(x) \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt{i!j! \sqrt{\pi}}}\sum_{j=0}^{\min{i,j}} k!\binom{i}{k}\binom{j}{k}\sqrt{(i+j-2k)!} h_{i+j-2k}(x) &&\mid h_0(x) = \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}} \\
        &= h_0(x)\sum_{k=0}^{\min{i,j}}k!\binom{i}{k}\binom{j}{k}\sqrt{\frac{(i+j-2k)!}{i!j!}}h_{i+j-2k}(x) \\
        &= h_0(x)\sum_{k=0}^{\min{i,j}}\frac{\sqrt{i!j!(i+j-2k)!}}{k!(i-k)!(j-k)!}h_{i+j-2k}(x)
    \end{aligned}
$$

So for two Hermite function series $f$ & $g$ we can write $\frac{fg}{h_0}$ as a Hermite function series again.

```python
from sympy import *
from math import factorial, comb

def hermfpmul(f, g):
    """Return $m$, such that $mh_0=fg$.
    
    $f$, $g$ & $m$ are sequences of coefficients
    representing Hermite function series.
    """
    r = [0] * (len(f)+len(g)-1)
    for i, fi in enumerate(f):
        for j, gj in enumerate(g):
            for k in range(min(i, j)+1):
                r[i+j-2*k] += fi * gj \
                        * factorial(k)*comb(i, k)*comb(j, k) \
                        * sqrt(Rational(factorial(i+j-2*k),
                                       (factorial(i)*factorial(j))))
    return tuple(r)
```

!!! danger "Even better product"

    Should also be possible as $f\cdot g=e^\frac{-x^2}{2}\sum_ih_i(\sqrt{2}x)$ or something like that. Would maybe be more 'natural'.
