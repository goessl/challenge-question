# Challenge

An ensemble of one-dimensional, orthonormal wavefunctions $\{\phi_k\}_{k\in\{1,\dots,N\}}$

$$
    \phi_k:\mathbb{R}\to\mathbb{C} \qquad \phi_k\in L^2(\mathbb{R}) \qquad \Braket{\phi_k|\phi_l}=\delta_{kl} \ ,
$$

that all fulfill the Schrödinger equation for some unknown potential $V:\mathbb{R}\to\mathbb{R}$

$$
    -\frac{1}{2}\phi_k''+V\phi_k = E_k\phi_k \ ,
$$

have a probability density distribution $n:\mathbb{R}\to\mathbb{R}_0^+$

$$
    n = \sum_{k=1}^N|\phi_k|^2 \ .
$$

What is the density to kinetic energy functional $T[n]$

$$
    T = -\frac{1}{2}\int_\mathbb{R}\sum_{k=1}^N\phi_k^*(x)\phi_k''(x)\,\mathrm{d}x \ ?
$$
