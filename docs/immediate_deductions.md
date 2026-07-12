# Immediate Deductions

## Natural Units

Natural units $\hbar=m=1$ used everywhere like in the [original Challenge-Question document](challenge_question.md).

!!! danger "Natural units"

    TODO everything with SI-units.

## Function space and representability

We assume all states are representable as position space wavefunctions and they are in $L^2(\mathbb{R})$.

!!! danger "Space of wavefunctions"

    Are all states representable as position space wavefunctions?
    
    What is the space of possible wavefunctions?
    
    Does Schrödinger eigenstate imply boundedness? Does boundedness imply normalisability. Does normalisability and possiblity of orthogonalisation imply $L^2(\mathbb{R})$?
    
    So many questions about the mathematical foundation of quantum mechanics ...

## Density norm

Particle count.

$$
    \begin{aligned}
        \int_\mathbb{R}n(x)\,\mathrm{d}x &= \int_\mathbb{R}\sum_{k=1}^N|\phi_k(x)|^2\,\mathrm{d}x \\
        &= \sum_{k=1}^N\int_\mathbb{R}|\phi_k(x)|^2\,\mathrm{d}x &&\mid \int_\mathbb{R}|\phi_k(x)|^2\,\mathrm{d}x=||\phi_k||^2=1 \\
        &= \sum_{k=1}^N1 \\
        &= N
    \end{aligned}
$$

## Partial integration

More pleasant integral for $T$.

$$
    \begin{aligned}
        T &= -\frac{1}{2}\int_\mathbb{R}\sum_{k=1}^N\phi_k^*(x)\phi_k''(x)\,\mathrm{d}x \\
        &= -\frac{1}{2}\sum_{k=1}^N\int_\mathbb{R}\phi_k^*(x)\phi_k''(x)\,\mathrm{d}x &&\mid \text{p.I.} \\
        &= -\frac{1}{2}\sum_{k=1}^N\left(\phi_k^*\phi_k'\mid_\mathbb{R}-\int_\mathbb{R}|\phi_k'(x)|^2\,\mathrm{d}x\right) &&\mid \phi_k(\pm\infty)=\phi_k'(\pm\infty)=0 \\
        &= +\frac{1}{2}\sum_{k=1}^N\int_\mathbb{R}|\phi_k'(x)|^2\,\mathrm{d}x
    \end{aligned}
$$

## Plane invariance

### Lemma

The density $\hat{\rho}$ and the kinetic energy $T$ of any pair of wavefunctions only depend on the plane they lie in, not their orientation within.

### Proof

Let there be an orthonormal pair of wavefunctions $\phi_1, \phi_2$. All other orthonormal pairs of wavefunctions within this plane

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

!!! danger "Generalise"

    Should be possible for any number of particles.
    
    Particle states are the eigenstates of $\hat{\rho}$ with eigenvalue $1$, all other eigenvalues are $0$.
    
    Eigenvectors are linearly combinable. $\hat{\rho}$ only depends on the span of the states.
    
    Something like that.
