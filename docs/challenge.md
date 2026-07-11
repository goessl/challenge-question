# Challenge

A set of one dimensional, orthonormal wavefunctions $\{\phi_i\}_{i\in\{0,1,\dots,N-1\}}$,

$$
    \phi_i:\mathbb{R}\to\mathbb{C} \qquad \phi_i\in L^2(\mathbb{R}) \qquad \Braket{\phi_i|\phi_j}=\int_\mathbb{R}\phi_i^*(x)\phi_j(x)\,\mathrm{d}x=\delta_{ij} \ ,
$$

that all fulfill the Schrödinger equation for some unknown potential $V:\mathbb{R}\to\mathbb{R}$

$$
    -\frac{1}{2}\phi_i''+V\phi_i = E_i\phi_i \ ,
$$

have a density (probability density distribution) $n:\mathbb{R}\to\mathbb{R}_0^+$

$$
    n = \sum_{i=0}^{N-1}|\phi_i|^2 \ .
$$

What is the density to kinetic energy functional $T[n]$

$$
    T = -\frac{1}{2}\int_\mathbb{R}\sum_{i=0}^{N-1}\phi_i^*(x)\phi_i''(x)\,\mathrm{d}x \ ?
$$
