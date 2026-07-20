# Whole Solution Set

## Task

For an appropriate particle density $n$ describe the set of all possible valid underlying wavefunction pairs:

$$
    \left\{\left\{\phi_1,\phi_2\right\} \mid \phi_1,\phi_2 \in L^2(\mathbb{R}), \ \braket{\phi_k|\phi_l}=\delta_{kl}, \ n=|\phi_1|^2+|\phi_2|^2\right\}
$$

*Appropriate meaning that the set is not empty.*

## Approach

The following conditions must be met

$$
    \begin{array}{ll}
        \text{pointwise density:} & n=|\phi_1|^2+|\phi_2|^2 \\
        \text{normalisation of $\phi_1$:} & \int_\mathbb{R}|\phi_1(x)|^2\,\mathrm{d}x=1 \\
        \text{normalisation of $\phi_2$:} & \int_\mathbb{R}|\phi_2(x)|^2\,\mathrm{d}x=1 \\
        \text{orthogonalisation:} & \int_\mathbb{R}\phi_1^*(x)\phi_2(x)\,\mathrm{d}x=0
    \end{array}
$$

### Density

The *density* requirement is actually just the complex version of the circle equation.

!!! note "Circle equation"

    For a given $c\in\mathbb{R}_0^+$ all $a, b\in\mathbb{R}$ for $a^2+b^2=c$ are
    
    $$
        \begin{aligned}
            a &= \sqrt{c}\cos\alpha \\
            b &= \sqrt{c}\sin\alpha
        \end{aligned} \qquad \alpha\in[0, 2\pi[.
    $$

!!! note "Complex circle equation"

    For a given $c\in\mathbb{R}_0^+$ all $a, b\in\mathbb{C}$ for $|a|^2+|b|^2=c$ are
    
    $$
        \begin{aligned}
            a &= e^{i\varphi_a}\sqrt{c}\cos\alpha \\
            b &= e^{i\varphi_b}\sqrt{c}\sin\alpha
        \end{aligned} \qquad \varphi_a, \varphi_b, \alpha \in[0, 2\pi[.
    $$

For wavefunctions the free parameters just have to be stretched over the whole real axis:

$$
    \begin{aligned}
        \phi_1(x) &= e^{i\varphi_1(x)}\sqrt{n(x)}\cos\alpha(x) \\
        \phi_2(x) &= e^{i\varphi_2(x)}\sqrt{n(x)}\sin\alpha(x)
    \end{aligned} \qquad \varphi_1, \varphi_2, \alpha : \mathbb{R}\to[0,2\pi[
$$

The remaining requirements become

$$
    \begin{array}{ll}
        \text{normalisation of $\phi_1$:} & \int_\mathbb{R}n(x)\cos^2\alpha(x)\,\mathrm{d}x=1 \\
        \text{normalisation of $\phi_2$:} & \int_\mathbb{R}n(x)\sin^2\alpha(x)\,\mathrm{d}x=1 \\
        \text{orthogonalisation:} & \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\cos\alpha(x)\sin\alpha(x)\,\mathrm{d}x=0 \qquad \Delta\varphi=\varphi_2-\varphi_1
    \end{array}
$$

### Normalisations

The *normalisation* requirements are equivalent now due to the form of $\phi_1$ & $\phi_2$:

$$
    \begin{aligned}
        1 &= \int_\mathbb{R}n(x)\cos^2\alpha(x)\,\mathrm{d}x &&\mid 1=\cos^2\alpha+\sin^2\alpha \\
        1 &= \int_\mathbb{R}n(x)\left(1-\sin^2\alpha(x)\right)\,\mathrm{d}x \\
        1 &= \int_\mathbb{R}n(x)\,\mathrm{d}x-\int_\mathbb{R}n(x)\sin^2\alpha(x)\,\mathrm{d}x &&\mid \int_\mathbb{R}n(x)\,\mathrm{d}x=2 \\
        1 &= 2-\int_\mathbb{R}n(x)\sin^2\alpha(x)\,\mathrm{d}x &&\mid-2 \ \mid\cdot(-1) \\
        1 &= \int_\mathbb{R}n(x)\sin^2\alpha(x)\,\mathrm{d}x \\
        \int_\mathbb{R}n(x)\cos^2\alpha(x)\,\mathrm{d}x=1 \quad &\Leftrightarrow \quad\int_\mathbb{R}n(x)\sin^2\alpha(x)\,\mathrm{d}x=1
    \end{aligned}
$$

Leaving the remaining requirements as

$$
    \begin{array}{ll}
        \text{normalisation:} & \int_\mathbb{R}n(x)\cos^2\alpha(x)\,\mathrm{d}x=1 \\
        \text{orthogonalisation:} & \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\cos\alpha(x)\sin\alpha(x)\,\mathrm{d}x=0 \qquad \Delta\varphi=\varphi_2-\varphi_1
    \end{array}
$$

### Orthogonalisation

Both requirements can be brought to similar form

$$
    \begin{aligned}
        \text{normalisation:} \quad 1 &= \int_\mathbb{R}n(x)\cos^2\alpha(x)\,\mathrm{d}x &&\mid \cos^2x=\frac{1+\cos2x}{2} \\
        1 &= \int_\mathbb{R}n(x)\frac{1+\cos2\alpha(x)}{2}\,\mathrm{d}x &&\mid \cdot2 \\
        2 &= \int_\mathbb{R}n(x)\,\mathrm{d}x+\int_\mathbb{R}n(x)\cos2\alpha(x)\,\mathrm{d}x &&\mid -2=-\int_\mathbb{R}n(x)\,\mathrm{d}x \\
        0 &= \int_\mathbb{R}n(x)\cos2\alpha(x)\,\mathrm{d}x \\
        \\
        \text{orthogonalisation:} \quad 0 &= \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\cos\alpha(x)\sin\alpha(x)\,\mathrm{d}x &&\mid \cos x\sin x=\frac{\sin2x}{2} \\
        0 &= \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\frac{\sin2\alpha(x)}{2}\,\mathrm{d}x &&\mid \cdot2 \\
        0 &= \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\sin2\alpha(x)\,\mathrm{d}x
    \end{aligned}
$$

Leaving

$$
    \begin{array}{ll}
        \text{normalisation:} & \int_\mathbb{R}n(x)\cos2\alpha(x)\,\mathrm{d}x=0 \\
        \text{orthogonalisation:} & \int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\sin2\alpha(x)\,\mathrm{d}x=0
    \end{array}
$$

### Real orthonormalisation

For real wavefunctions $\varphi_1=\varphi_2=0$ the two requirements can further be reduced to a single *real orthonormalisation* requirement:

$$
    \begin{aligned}
        \text{normalisation:} \quad 0 &= \int_\mathbb{R}n(x)\cos2\alpha(x)\,\mathrm{d}x &&\mid \cos\varphi=\Re e^{i\varphi} \\
        0 &= \int_\mathbb{R}n(x)\Re e^{i2\alpha(x)}\,\mathrm{d}x \\
        0 &= \Re\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x \\
        \\
        \text{orthogonalisation:} \quad 0 &= \int_\mathbb{R}n(x)\sin2\alpha(x)\,\mathrm{d}x &&\mid \sin\varphi=\Im e^{i\varphi} \\
        0 &= \Im\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x \\
        \\
        0 &= 0+i0 &&\mid 0=\Re\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x=\Im\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x \\
        0 &= \Re\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x+i\Im\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x \\
        0 &= \int_\mathbb{R}n(x)\left(\Re e^{i2\alpha(x)}+i\Im e^{i2\alpha(x)}\right)\,\mathrm{d}x &&\mid z=\Re z+i\Im z \\
        \text{real orthonormalisation:} \quad 0 &= \int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x
    \end{aligned}
$$

This is quite a nice little intermediate result.

## Solution

### General complex case

$$
    \begin{aligned}
        \phi_1(x) &= e^{i\varphi_1(x)}\sqrt{n(x)}\cos\alpha(x) \\
        \phi_2(x) &= e^{i\varphi_2(x)}\sqrt{n(x)}\sin\alpha(x)
    \end{aligned} \qquad \varphi_1, \varphi_2, \alpha:\mathbb{R}\to[0,2\pi[, \ \int_\mathbb{R}n(x)\cos2\alpha(x)\,\mathrm{d}x=\int_\mathbb{R}e^{i\Delta\varphi(x)}n(x)\sin2\alpha(x)\,\mathrm{d}x=0
$$

### Real case

$$
    \begin{aligned}
        \phi_1(x) &= \sqrt{n(x)}\cos\alpha(x) \\
        \phi_2(x) &= \sqrt{n(x)}\sin\alpha(x)
    \end{aligned} \qquad \alpha:\mathbb{R}\to[0,2\pi[, \ \int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x=0
$$

!!! danger "Missing restrictions"

    For wavefunction there are actually more requirements like differentiability, ...
    
    TODO: [mathematical foundation](../immediate_deductions.md#mathematical-foundation)

---

## Kinetic energy

$$
    \begin{aligned}
        |\phi_1'(x)|^2 &= \left|\frac{\mathrm{d}}{\mathrm{d}x}e^{i\varphi_1(x)}\sqrt{n(x)}\cos\alpha(x)\right|^2 \\
        &= \left|ie^{i\varphi_1(x)}\varphi_1'(x)\sqrt{n(x)}\cos\alpha(x)+e^{i\varphi_1(x)}\frac{n'(x)}{2\sqrt{n(x)}}\cos\alpha(x)-e^{i\varphi_1(x)}\sqrt{n(x)}\alpha'(x)\sin\alpha(x)\right|^2 \\
        &= \left(\varphi_1'(x)\sqrt{n(x)}\cos\alpha(x)\right)^2+\left(\frac{n'(x)}{2\sqrt{n(x)}}\cos\alpha(x)-\sqrt{n(x)}\alpha'(x)\sin\alpha(x)\right)^2 \\
        &= \varphi_1'(x)^2n(x)\cos^2\alpha(x)+\frac{n'(x)^2}{4n(x)}\cos^2\alpha(x)-n'(x)\alpha'(x)\cos\alpha(x)\sin\alpha(x)+n(x)\alpha'(x)^2\sin^2\alpha(x) \\
        |\phi_2'(x)|^2 &= \varphi_2'(x)^2n(x)\sin^2\alpha(x)+\frac{n'(x)^2}{4n(x)}\sin^2\alpha(x)+n'(x)\alpha'(x)\cos\alpha(x)\sin\alpha(x)+n(x)\alpha'(x)^2\cos^2\alpha(x) \\
        \\
        \braket{\hat{T}} &= \frac{1}{2}\int_\mathbb{R}|\phi_1'(x)|^2+|\phi_2'(x)|^2\,\mathrm{d}x \\
        &= \frac{1}{2}\int_\mathbb{R}\varphi_1'(x)^2n(x)\cos^2\alpha(x)+\frac{n'(x)^2}{4n(x)}\cos^2\alpha(x)-n'(x)\alpha'(x)\cos\alpha(x)\sin\alpha(x)+n(x)\alpha'(x)^2\sin^2\alpha(x) \\
        &\qquad +\varphi_2'(x)^2n(x)\sin^2\alpha(x)+\frac{n'(x)^2}{4n(x)}\sin^2\alpha(x)+n'(x)\alpha'(x)\cos\alpha(x)\sin\alpha(x)+n(x)\alpha'(x)^2\cos^2\alpha(x)\,\mathrm{d}x \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\left(\alpha'(x)^2+\varphi_1'(x)^2\cos^2\alpha(x)+\varphi_2'(x)^2\sin^2\alpha(x)\right)\,\mathrm{d}x
    \end{aligned}
$$

### Real

For real wavefunctions $\varphi_1=\varphi_2=0$

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\left(\alpha'(x)^2+\varphi_1'(x)^2\cos^2\alpha(x)+\varphi_2'(x)^2\sin^2\alpha(x)\right)\,\mathrm{d}x \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\alpha'(x)^2\,\mathrm{d}x
    \end{aligned}
$$
