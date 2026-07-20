# Immediate Deductions

## Natural units

Natural units $\hbar=m=1$ used everywhere like in the [original Challenge-Question document](challenge_question.md).

!!! danger "Natural units"

    TODO everything with SI-units.

## Mathematical foundation

We assume all states correspond to position space wavefunctions and they are in $L^2(\mathbb{R})$. Implying $\braket{f|g}=\int_\mathbb{R}f^*(x)g(x)\,\mathrm{d}x$.

!!! danger "Space of wavefunctions"

    - Are in general all states representable as position space wavefunctions?
    - What is the space of possible wavefunctions? Maybe more than $L^2(\mathbb{R})$?
    - What about unbounded (unormalisable) states and their amplitude in the infinite?
    
    So many questions about the mathematical foundation of quantum mechanics ...
    
    Proposed formulation:
    
    Let $\mathcal{H}$ be a complex Hilbert space, with a continuous (orthonormal and complete) basis $\ket{x}$ where $x\in\mathbb{R}$.
    Then we name
    
    - the position operator $\hat{X}=\int_\mathbb{R}x\ket{x}\bra{x}\,\mathrm{d}x$,
    - the momentum operator $\hat{P}=\int_\mathbb{R}p\ket{p}\bra{p}\,\mathrm{d}p$ with $\braket{x|p}=\frac{e^{+\frac{i}{\hbar}xp}}{\sqrt{2\pi\hbar}}$ and
    - the kinetic energy $\hat{T}=\frac{\hat{P}^2}{2m}$.
    
    Then let
    
    - the potential operator $\hat{V}$ be local and position dependent,
    - the Hamiltonian operator $\hat{H}=\hat{T}+\hat{V}$,
    - $\left\{\ket{\phi_k}\right\}_k$ be eigenstates of the Hamiltonian,
    - $\hat{\rho}=\sum_k\ket{\phi_k}\bra{\phi_k}$ the density operator and
    - $n(x)=\braket{x|\hat{\rho}|x}$ the probability density distribution.

## Complex wavefunctions

We will try to do as many for the general case of complex wavefunctions, but it may not be possible everywhere.

!!! danger "Real wavefunction always possible"

    Should be possible for such a *well-behaving* Hamiltonian to always chose the states to be real?

## Density norm

All particles must be somewhere.

$$
    \begin{aligned}
        \int_\mathbb{R}n(x)\,\mathrm{d}x &= \int_\mathbb{R}\sum_{k=1}^N|\phi_k(x)|^2\,\mathrm{d}x \\
        &= \sum_{k=1}^N\int_\mathbb{R}|\phi_k(x)|^2\,\mathrm{d}x &&\mid ||\phi_k||^2=1 \\
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
        &= +\frac{1}{2}\sum_{k=1}^N||\phi_k'||^2
    \end{aligned}
$$

## Unitary decomposition invariance

The density operator $\hat{\rho}$ and therefore also the kinetic energy $\braket{\hat{T}}$ are invariant over unitary changes of ensemble decompositions:

$$
    \begin{aligned}
        \hat{\rho}_\psi &= \sum_k\ket{\psi_k}\bra{\psi_k} &&\mid \sum_jv_jv_j^\dagger=\text{tr}\,\vec{v}\vec{v}^\dagger \\
        &= \text{tr}\,\begin{pmatrix}
            \ket{\psi_1} \\
            \ket{\psi_2} \\
            \vdots
        \end{pmatrix}\begin{pmatrix}
            \ket{\psi_1} \\
            \ket{\psi_2} \\
            \vdots
        \end{pmatrix}^\dagger &&\mid \begin{pmatrix}
            \ket{\psi_1} \\
            \ket{\psi_2} \\
            \vdots
        \end{pmatrix} = U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix} \\
        &= \text{tr}\,U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}\left(U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}\right)^\dagger \\
        &= \text{tr}\,U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}^\dagger U^\dagger &&\mid \text{tr}\,ABC = \text{tr}\,CAB \\
        &= \text{tr}\,U^\dagger U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}^\dagger &&\mid U^\dagger U=1 \\
        &= \text{tr}\,\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}^\dagger &&\mid \sum_jv_jv_j^\dagger=\text{tr}\,\vec{v}\vec{v}^\dagger \\
        &= \sum_k\ket{\phi_k}\bra{\phi_k} \\
        &= \hat{\rho}_\phi
    \end{aligned}
$$

This means that all ensembles, that can be reached by a unitary transformation, have the same density operator $\hat{\rho}$ and yield the same measurements

$$
    \braket{\hat{A}}_\psi = \text{tr}\,\hat{\rho}_\psi\hat{A} = \text{tr}\,\hat{\rho}_\phi\hat{A} = \braket{\hat{A}}_\phi
$$

### Plane invariance for two real particles

For two particles this means that rotations within the plane they span don't change the density nor kinetic energy.

#### Explicit proof

Let there be an orthonormal pair of wavefunctions $\phi_1, \phi_2$. All orthonormal pairs of wavefunctions within this plane reachable by rotation

$$
    \begin{aligned}
        \ket{\psi_1} &= \cos\varphi\ket{\phi_1}-\sin\varphi\ket{\phi_2} \\
        \ket{\psi_2} &= \sin\varphi\ket{\phi_1}+\cos\varphi\ket{\phi_2}
    \end{aligned}
$$

have the same density

$$
    \begin{aligned}
        \hat{\rho}_\psi &= \ket{\psi_1}\bra{\psi_1}+\ket{\psi_2}\bra{\psi_2} \\
        &= \left(\cos\varphi\ket{\phi_1}-\sin\varphi\ket{\phi_2}\right)\left(\cos\varphi\bra{\phi_1}-\sin\varphi\bra{\phi_2}\right) \\
        &\qquad +\left(\sin\varphi\ket{\phi_1}+\cos\varphi\ket{\phi_2}\right)\left(\sin\varphi\bra{\phi_1}+\cos\varphi\bra{\phi_2}\right) \\
        &= \cos^2\varphi\ket{\phi_1}\bra{\phi_1}-\cos\varphi\sin\varphi\ket{\phi_1}\bra{\phi_2}-\cos\varphi\sin\varphi\ket{\phi_2}\bra{\phi_1}+\sin^2\varphi\ket{\phi_2}\bra{\phi_2} \\
        &\qquad +\sin^2\varphi\ket{\phi_1}\bra{\phi_1}+\cos\varphi\sin\varphi\ket{\phi_1}\bra{\phi_2}+\cos\varphi\sin\varphi\ket{\phi_2}\bra{\phi_1}+\cos^2\varphi\ket{\phi_2}\bra{\phi_2} \\
        &= 1\ket{\phi_1}\bra{\phi_1}+0\ket{\phi_1}\bra{\phi_2}+0\ket{\phi_2}\bra{\phi_1}+1\ket{\phi_2}\bra{\phi_2} \\
        &= \ket{\phi_1}\bra{\phi_1}+\ket{\phi_2}\bra{\phi_2} \\
        &= \hat{\rho}_\phi
    \end{aligned}
$$

and the same kinetic energy

$$
    \braket{\hat{T}}_\psi = \text{tr}\,\hat{\rho}_\psi\hat{T} = \text{tr}\,\hat{\rho}_\phi\hat{T} = \braket{\hat{T}}_\phi
$$

!!! danger "Converse"

    TODO: prove
    
    $$
        \left\{\ket{\phi_k}\right\}_{k=1}^N, \left\{\ket{\psi_k}\right\}_{k=1}^N \ \text{both orthonormal}, \ \hat{\rho}_\phi = \hat{\rho}_\psi \qquad \Rightarrow \qquad \exists U\in U(N) \mid \begin{pmatrix}
            \ket{\psi_1} \\
            \ket{\psi_2} \\
            \vdots
        \end{pmatrix} = U\begin{pmatrix}
            \ket{\phi_1} \\
            \ket{\phi_2} \\
            \vdots
        \end{pmatrix}
    $$
    
    would close the "Unitary decomposition invariance" from a $\Rightarrow$ to a $\Leftrightarrow$.
