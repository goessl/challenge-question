# Immediate Deductions

## Natural Units

Natural units $\hbar=m=1$ used everywhere like in the [original Challenge-Question document](challenge_question.md).

!!! danger "Natural Units"

    TODO everything with SI-units.

## Density norm

Particle count.

$$
    \begin{aligned}
        \int_\mathbb{R}n(x)\,\mathrm{d}x &= \int_\mathbb{R}\sum_{i=0}^{N-1}|\phi_i(x)|^2\,\mathrm{d}x \\
        &= \sum_{i=0}^{N-1}\int_\mathbb{R}|\phi_i(x)|^2\,\mathrm{d}x &&\mid ||\phi_i||_{L^2(\mathbb{R})}=1 \\
        &= \sum_{i=0}^{N-1}1 \\
        &= N
    \end{aligned}
$$

## Partial integration

More pleasant integral for $T$.

$$
    \begin{aligned}
        T &= -\frac{1}{2}\int_\mathbb{R}\sum_{i=0}^{N-1}\phi_i^*(x)\phi_i''(x)\,\mathrm{d}x \\
        &= -\frac{1}{2}\sum_{i=0}^{N-1}\int_\mathbb{R}\phi_i^*(x)\phi_i''(x)\,\mathrm{d}x &&\mid \text{p.I.} \\
        &= -\frac{1}{2}\sum_{i=0}^{N-1}\left(\phi_i^*\phi_i'\mid_\mathbb{R}-\int_\mathbb{R}|\phi_i'(x)|^2\,\mathrm{d}x\right) &&\mid \phi_i\in\mathcal{S}(\mathbb{R}) \\
        &= +\frac{1}{2}\sum_{i=0}^{N-1}\int_\mathbb{R}|\phi_i'(x)|^2\,\mathrm{d}x
    \end{aligned}
$$

!!! danger "Space of Wavefunctions"

    What is the space of possible wavefunctions?
    
    $L^2(\mathbb{R})$? Should be sufficient to call $\phi_i(\pm\infty)=\phi_i'(\pm\infty)=0$.
    
    But just to be sure I've used $\mathcal{S}(\mathbb{R})$ which is already dense in $L^2(\mathbb{R})$.
    
    TODO

## Plane Invariance

### Lemma

The density $\hat{\rho}$ and the kinetic energy $T$ of any pairs of wavefunctions only depends on the plane they lie in, not their orientation within.

### Proof

Let there be an orthonormal pair of wavefunctions $\phi_1, \phi_2$

$$
    \braket{\phi_i|\phi_j} = \delta_{ij}
$$

All other orthonormal pairs of wavefunctions within this plane

$$
    \begin{aligned}
        \ket{\psi_1} &= \cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2} \\
        \ket{\psi_2} &= \sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}
    \end{aligned}
$$

have the same density

$$
    \begin{aligned}
        \hat{\rho}_\psi &= \ket{\psi_1}\bra{\psi_1}+\ket{\psi_2}\bra{\psi_2} \\
        &= \left(\cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2}\right)\left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right) \\
        &\qquad +\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right)\left(\sin\varphi\bra{\phi_1}-\cos\varphi\bra{\phi_2}\right) \\
        &= \cos^2\varphi\ket{\phi_1}\bra{\phi_1}+\cos\varphi\sin\varphi\ket{\phi_1}\bra{\phi_2}+\cos\varphi\sin\varphi\ket{\phi_2}\bra{\phi_1}+\sin^2\varphi\ket{\phi_2}\bra{\phi_2} \\
        &\qquad +\sin^2\varphi\ket{\phi_1}\bra{\phi_1}-\cos\varphi\sin\varphi\ket{\phi_1}\bra{\phi_2}-\cos\varphi\sin\varphi\ket{\phi_2}\bra{\phi_1}+\cos^2\varphi\ket{\phi_2}\bra{\phi_2} \\
        &= 1\ket{\phi_1}\bra{\phi_1}+0\ket{\phi_1}\bra{\phi_2}+0\ket{\phi_2}\bra{\phi_1}+1\ket{\phi_2}\bra{\phi_2} \\
        &= \ket{\phi_1}\bra{\phi_1}+\ket{\phi_2}\bra{\phi_2} \\
        &= \hat{\rho}_\phi
    \end{aligned}
$$

and the same kinetic energy

$$
    \braket{\hat{T}}_\psi = \text{tr}\hat{\rho}_\psi\hat{T} = \text{tr}\hat{\rho}_\phi\hat{T} = \braket{\hat{T}}_\phi
$$

### Explicit orthonormality check

$$
    \begin{aligned}
        \braket{\psi_1|\psi_1} &= \left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right)\left(\cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2}\right) \\
        &= \cos^2\varphi\braket{\phi_1|\phi_1}+\cos\varphi\sin\varphi\braket{\phi_1|\phi_2}+\cos\varphi\sin\varphi\braket{\phi_2|\phi_1}+\sin^2\varphi\braket{\phi_2|\phi_2} \\
        &= \cos^2\varphi+\sin^2\varphi = 1 \\
        \braket{\psi_2|\psi_2} &= \left(\sin\varphi\bra{\phi_1}-\cos\varphi\bra{\phi_2}\right)\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right) \\
        &= \sin^2\varphi\braket{\phi_1|\phi_1}-\cos\varphi\sin\varphi\braket{\phi_1|\phi_2}-\cos\varphi\sin\varphi\braket{\phi_2|\phi_1}+\cos^2\varphi\braket{\phi_2|\phi_2} \\
        &= \cos^2\varphi+\sin^2\varphi = 1 \\
        \braket{\psi_1|\psi_2} &= \left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right)\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right) \\
        &= \cos\varphi\sin\varphi\braket{\phi_1|\phi_1}-\cos^2\varphi\braket{\phi_1|\phi_2}+\sin^2\varphi\braket{\phi_1|\phi_2}-\cos\varphi\sin\varphi\braket{\phi_2|\phi_2} \\
        &= \cos\varphi\sin\varphi-\cos\varphi\sin\varphi = 0
    \end{aligned}
$$
