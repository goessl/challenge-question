# Orthonormal Complement

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

!!! danger "Square root"

    Might be easier to just calculate the hole wavefunction as $\sqrt{\sum_jb_j(x)^2-n(x)}$.

!!! danger "Restriction of generality"

    Used real $T[n]$. How about complex formula?!
