# Single Particle

## Question

For a sole wavefunction $\phi$, only the density $n=|\phi|^2$ is known. What is the kinetic energy?

## Approach

The wavefunction, up to some phase, can be reconstructed from the density:

$$
    n=|\phi|^2 \quad \Rightarrow \quad \phi=e^{i\varphi}\sqrt{n} \qquad \varphi:\mathbb{R}\to\mathbb{R}
$$

This is then plugged into the kinetic energy formula:

$$
    \begin{aligned}
        T &= \frac{1}{2}\int_\mathbb{R}|\phi'(x)|^2\,\mathrm{d}x &&\mid \phi=e^{i\varphi}\sqrt{n} \\
        &= \frac{1}{2}\int_\mathbb{R}\left|\frac{\mathrm{d}}{\mathrm{d}x}e^{i\varphi(x)}\sqrt{n(x)}\right|^2\,\mathrm{d}x &&\mid \frac{\mathrm{d}}{\mathrm{d}x}e^{af(x)}=ae^{af(x)}f'(x), \ \frac{\mathrm{d}}{\mathrm{d}x}\sqrt{f(x)}=\frac{f'(x)}{2\sqrt{f(x)}} \\
        &= \frac{1}{2}\int_\mathbb{R}\left|ie^{i\varphi(x)}\varphi'(x)\sqrt{n(x)}+e^{i\varphi(x)}\frac{n'(x)}{2\sqrt{n(x)}}\right|^2\,\mathrm{d}x &&\mid \left|e^{i\theta}z\right|=|z| \\
        &= \frac{1}{2}\int_\mathbb{R}\left|i\varphi'(x)\sqrt{n(x)}+\frac{n'(x)}{2\sqrt{n(x)}}\right|^2\,\mathrm{d}x &&\mid |a+ib|^2=a^2+b^2 \\
        &= \frac{1}{2}\int_\mathbb{R}\varphi'(x)^2n(x)+\frac{n'(x)^2}{4n(x)}\,\mathrm{d}x \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4\varphi'(x)^2n(x)\,\mathrm{d}x
    \end{aligned}
$$

And for a real wavefunction $\text{ran}\,\phi\subseteq\mathbb{R} \ \Rightarrow \ \varphi'=0$:

$$
    T = \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}\,\mathrm{d}x
$$

!!! danger "Rational integrand"

    Prove that there are only finite points $x$ with $n(x)=0$. Longer intervals shouldn't be a problem because then $n'(x)=0$ also.
    
    Todo everywhere.

## Solution

### Complex

$$
    T[n] = \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4\varphi'(x)^2n(x)\,\mathrm{d}x
$$

### Real

$$
    T[n] = \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}\,\mathrm{d}x
$$
