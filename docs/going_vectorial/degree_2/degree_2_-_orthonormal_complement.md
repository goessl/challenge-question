# Degree 2 - Orthonormal Complement

This is also a special case:

When the space, in which we are quantum mechanically wobbling around, has exactly one degree of freedom more than the number of particles within, the orthonormal complement becomes a sole particle-like hole.

More precisely:

$$
    \begin{gathered}
        \text{dim}\,\mathcal{H}=N+1 \quad \text{or equivalently} \quad \text{rank}\,\hat{\rho}=\text{dim}\,\mathcal{H}-1 \\
        \Downarrow \\
        \text{rank}\,\hat{\rho}^\perp = \text{rank}\left(1-\hat{\rho}\right) = 1
    \end{gathered}
$$

Then we can simply use the [single particle solution](../../single_particle.md) and subtract it from the *full space kinetic energy*:

$$
    \begin{aligned}
        \braket{\hat{T}} &= \text{tr}\,\hat{\rho}\hat{T} &\mid \hat{\rho}+\hat{\rho}^\perp=1 \\
        &= \text{tr}\,\left(1-\hat{\rho}^\perp\right)\hat{T} \\
        &= \text{tr}\,\hat{T}-\text{tr}\,\hat{\rho}^\perp\hat{T} &\mid \text{rank}\,\hat{\rho}^\perp=1 \\
        &= \text{tr}\,\hat{T}-T[n^\perp]
    \end{aligned}
$$

with

$$
    \begin{aligned}
        n^\perp(x) &= \Braket{x|\hat{\rho}^\perp|x} \\
        &= \Braket{x|1-\hat{\rho}|x} \\
        &= \Braket{x|1|x} - \Braket{x|\hat{\rho}|x} \\
        &= \sum_jb_j(x)^2 - n(x)
    \end{aligned}
$$

and therefore

$$
    \begin{aligned}
        \braket{\hat{T}} &= \text{tr}\,\hat{T}-\frac{1}{8}\int_\mathbb{R}\frac{n^\perp{}'(x)^2}{n^\perp(x)}\,\mathrm{d}x \\
        &= \text{tr}\,\hat{T}-\frac{1}{8}\int_\mathbb{R}\frac{\left(\frac{\mathrm{d}}{\mathrm{d}x}\left(\sum_jb_j(x)^2-n(x)\right)\right)^2}{\sum_jb_j(x)^2-n(x)}\,\mathrm{d}x \\
        &= \text{tr}\,\hat{T}-\frac{1}{8}\int_\mathbb{R}\frac{\left(\sum_j2b_j(x)b_j'(x)-n'(x)\right)^2}{\sum_jb_j(x)^2-n(x)}\,\mathrm{d}x
    \end{aligned}
$$

where $\left\{\ket{b_j}\right\}_j$ is any complete orthonormal basis of $\mathcal{H}$.

## Hermite function case

The basis:

$$
    \left(\ket{0}, \ket{1}, \ket{2}\right)
$$

The full-space kinetic energy:

$$
    \text{tr}\,\hat{T} = \text{tr}\,\frac{1}{4}\begin{pmatrix}
                1 &         0 & -\sqrt{2} \\
                0 &         3 &         0 \\
        -\sqrt{2} &         0 &         5
    \end{pmatrix} = \frac{9}{4}
$$

The orthonormal complement (here the [polynomial part representation](../products/oh_look_a_polynomial.md) becomes useful):

$$
    \begin{aligned}
        n^\perp(x) &= h_0(x)^2+h_1(x)^2+h_2(x)^2-n(x) \\
        &= \left(\frac{e^{-\frac{x^2}{2}}}{\sqrt{\sqrt{\pi}}}\right)^2+\left(\frac{e^{-\frac{x^2}{2}}2x}{\sqrt{2\sqrt{\pi}}}\right)^2+\left(\frac{e^{-\frac{x^2}{2}}(4x^2-2)}{\sqrt{8\sqrt{\pi}}}\right)^2-n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}\right)-n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}-p_n(x)\right) \\
        n^\perp{}'(x) &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x\right)-n'(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x-p_{n'}(x)\right)
    \end{aligned}
$$

The kinetic energy:

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{n^\perp{}'(x)^2}{n^\perp(x)}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{\left(\frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x\right)-n'(x)\right)^2}{\frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}\right)-n(x)}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{4\sqrt{\pi}}\int_\mathbb{R}e^{-x^2}\frac{\left(-4x^5+8x^3-3x-p_{n'}(x)\right)^2}{4x^4+3-2p_n(x)}\,\mathrm{d}x
    \end{aligned}
$$
