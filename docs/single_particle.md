# Single Particle

## Question

For a sole wavefunction $\phi$, only the density $n=|\phi|^2$ is known. What is the kinetic energy?

## Approach

The wavefunction, up to some phase, can be reconstructed from the density:

$$
    n=|\phi|^2 \quad \Rightarrow \quad \phi=\pm\sqrt{n} \qquad \varphi:\mathbb{R}\to[0,2\pi[
$$

The $\pm$ factor may change at nodes $n(x)=0$. It can be chosen arbitrarily, as the kinetic energy $T$ is quadratic in $\phi$ which makes the sign irrelevant.

This is then plugged into the kinetic energy formula:

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{1}{2}\int_\mathbb{R}|\phi'(x)|^2\,\mathrm{d}x &&\mid \phi=\pm\sqrt{n} \\
        &= \frac{1}{2}\int_\mathbb{R}\left|\frac{\mathrm{d}}{\mathrm{d}x}\pm\sqrt{n(x)}\right|^2\,\mathrm{d}x &&\mid \frac{\mathrm{d}}{\mathrm{d}x}\sqrt{f(x)}=\frac{f'(x)}{2\sqrt{f(x)}} \\
        &= \frac{1}{2}\int_\mathbb{R}\left|\pm\frac{n'(x)}{2\sqrt{n(x)}}\right|^2\,\mathrm{d}x \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}\,\mathrm{d}x
    \end{aligned}
$$

The possibly zero denominator doesn't pose a problem because

- when $n(x)=0$ and $n'(x)\neq0$, then it is just a zero crossing node point where the quotient is undefined, and we just hope that there are only finitely many nodes because Riemann can handle that;
- when $n(x)=0$ for longer, then obviously $n'(x)=0$ for the same interval such that we can interpret the quotient as $0$.

## Solution

$$
    \braket{\hat{T}} = T[n] = \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}\,\mathrm{d}x
$$

Observe that functional is unique despite that we've never assumed $n$ to be the ground state, so it should work for all single particle densities.

This is the [von Weizsäcker functional](https://en.wikipedia.org/wiki/Orbital-free_density_functional_theory#Von_Weizs%C3%A4cker_(vW)_kinetic_energy).

[Complex version](complex/single_particle.md).
