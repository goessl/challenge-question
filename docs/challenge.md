# Challenge

An ensemble of one-dimensional, orthonormal wavefunctions $\{\phi_k\}_{k=1}^N$

$$
    \phi_k:\mathbb{R}\to\mathbb{C} \qquad \phi_k\in L^2(\mathbb{R}) \qquad \Braket{\phi_k|\phi_l}=\delta_{kl} \ ,
$$

that all fulfill the Schrödinger equation for some unknown potential $V:\mathbb{R}\to\mathbb{R}$

$$
    -\frac{1}{2}\phi_k''+V\phi_k = E_k\phi_k \ ,
$$

have a particle density $n:\mathbb{R}\to\mathbb{R}_0^+$

$$
    n = \sum_{k=1}^N|\phi_k|^2 \ .
$$

What is the density to kinetic energy functional $T[n]$

$$
    T = -\frac{1}{2}\int_\mathbb{R}\sum_{k=1}^N\phi_k^*(x)\phi_k''(x)\,\mathrm{d}x \ ?
$$

## Hohenberg-Kohn

[Hohenberg & Kohn](further_readings.md) showed that there must exist a mapping from the **non-degenerate ground state** particle density $n(x)$

- to the potential $V(x)$ up to an additive constant and
- to the kinetic energy $\braket{\hat{T}}$.

We will study the functional $T[n]$ in the more general way by neither requiring non-degeneracy nor a ground state.
