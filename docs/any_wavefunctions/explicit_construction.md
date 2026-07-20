# Explicit Construction

## Task

For an appropriate particle density $n$ explicitly write down one valid underlying wavefunction pair.

$$
    \left\{\phi_1, \phi_2\right\} \ \mid \ \phi_1, \phi_2 \in L^2(\mathbb{R}), \ \braket{\phi_k|\phi_l}=\delta_{kl}, \ n=|\phi_1|^2+|\phi_2|^2
$$

*Appropriate meaning that there is a solution.*

## Solution

$$
    \begin{aligned}
        \phi_1(x) &= \sqrt{n(x)}\cos\alpha(x) & \alpha(x) &= \frac{\pi}{2}s(x) \\
        \phi_2(x) &= \sqrt{n(x)}\sin\alpha(x) & s(x) &= \int_{-\infty}^xn(y)\,\mathrm{d}y
    \end{aligned}
$$

### Kinetic energy

$$
    \begin{aligned}
        T &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\alpha'(x)^2\,\mathrm{d}x &&\mid \alpha'=\frac{\pi}{2}s'=\frac{\pi}{2}n \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\left(\frac{\pi}{2}n(x)\right)^2\,\mathrm{d}x \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+\pi^2n(x)^3\,\mathrm{d}x
    \end{aligned}
$$

## Proof

In [whole solution set](whole_solution_set.md) it was shown that the wavefunctions must have the structure

$$
    \begin{aligned}
        \phi_1(x) &= \sqrt{n(x)}\cos\alpha(x) \\
        \phi_2(x) &= \sqrt{n(x)}\sin\alpha(x)
    \end{aligned} \qquad \alpha: \mathbb{R}\to[0,2\pi[, \ \int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x=0
$$

Therefore we only have to check the condition for $\alpha$:

$$
    \begin{aligned}
        &\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x &&\mid \alpha=\frac{\pi}{2}s \\
        &= \int_\mathbb{R}n(x)e^{i\pi s(x)}\,\mathrm{d}x &&\mid u\overset{!}{=}s \quad \frac{\mathrm{d}u}{\mathrm{d}x}=s'(x)=n(x) \ \Rightarrow \ \mathrm{d}x=\frac{\mathrm{d}u}{n(x)} \\
        &= \int_{x=\mathbb{R}}n(x)e^{i\pi u(x)}\,\frac{\mathrm{d}u}{n(x)} \\
        &= \int_{x=\mathbb{R}}e^{i\pi u(x)}\,\mathrm{d}u &&\mid \int e^{ax}\,\mathrm{d}x=\frac{e^{ax}}{a}+C \\
        &= \left.\frac{-i}{\pi}e^{i\pi u}\right|_{x=\mathbb{R}} &&\mid u=s \\
        &= \left.\frac{-i}{\pi}e^{i\pi s}\right|_\mathbb{R} \\
        &= \frac{-i}{\pi}\left[e^{i\pi s(+\infty)}-e^{i\pi s(-\infty)}\right] &&\mid s(-\infty)=0, \ s(+\infty)=2 \\
        &= \frac{-i}{\pi}\left[e^{i\pi 2}-e^{i\pi 0}\right] &&\mid e^{i2\pi}=+1, \ e^0=+1 \\
        &= \frac{-i}{\pi}\left[1-1\right] \\
        &= 0
    \end{aligned}
$$

---

## Explicit proof of all conditions

### Density

$$
    \begin{aligned}
        &\phi_1(x)^2+\phi_2(x)^2 \\
        &= \left(\sqrt{n(x)}\cos\alpha(x)\right)^2+\left(\sqrt{n(x)}\sin\alpha(x)\right)^2 \\
        &= n(x)\cos^2\alpha(x) + n(x)\sin^2\alpha(x) \\
        &= n(x)\left(\cos^2\alpha(x)+\sin^2\alpha(x)\right) &&\mid \cos^2\varphi+\sin^2\varphi=1 \\
        &= n(x)
    \end{aligned}
$$

### Normalisation of $\phi_1$

$$
    \begin{aligned}
        &\int_\mathbb{R}\phi_1(x)^2\,\mathrm{d}x \\
        &= \int_\mathbb{R}\left(\sqrt{n(x)}\cos\alpha(x)\right)^2\,\mathrm{d}x \\
        &= \int_\mathbb{R}n(x)\cos^2\frac{\pi}{2}s(x)\,\mathrm{d}x &&\mid \cos^2x=\frac{1+\cos2x}{2} \\
        &= \int_\mathbb{R}n(x)\frac{1+\cos2\frac{\pi}{2}s(x)}{2}\,\mathrm{d}x \\
        &= \frac{1}{2}\int_\mathbb{R}n(x)\,\mathrm{d}x+\frac{1}{2}\int_\mathbb{R}n(x)\cos\pi s(x)\,\mathrm{d}x &&\mid\int_\mathbb{R}n(x)\,\mathrm{d}x=2 \\
        &= 1+\frac{1}{2}\int_\mathbb{R}n(x)\cos\pi s(x)\,\mathrm{d}x &&\mid u\overset{!}{=}s, \quad \frac{\mathrm{d}u}{\mathrm{d}x}=n(x) \ \Rightarrow \mathrm{d}x=\frac{\mathrm{d}u}{n(x)} \\
        &= 1+\frac{1}{2}\int_{x=\mathbb{R}}n(x)\cos\pi u\,\frac{\mathrm{d}u}{n(x)} \\
        &= 1+\frac{1}{2}\int_{x=\mathbb{R}}\cos\pi u\,\mathrm{d}u &&\mid \int\cos\pi x\,\mathrm{d}x=\frac{\sin\pi x}{\pi}+C \\
        &= 1+\left.\frac{\sin\pi u}{2\pi}\right|_{x=\mathbb{R}} &&\mid u=s\\
        &= 1+\left.\frac{\sin\pi s}{2\pi}\right|_\mathbb{R} \\
        &= 1+\frac{1}{2\pi}\left[\sin\pi s(+\infty)-\sin\pi s(-\infty)\right] &&\mid s(-\infty)=0, \ s(+\infty)=2 \\
        &= 1+\frac{1}{2\pi}\left[\sin2\pi-\sin0\right] &&\mid \sin2\pi=\sin0=0 \\
        &= 1+\frac{1}{2\pi}\left[0-0\right] \\
        &= 1
    \end{aligned}
$$

### Normalisation of $\phi_2$

$$
    \begin{aligned}
        &\int_\mathbb{R}\phi_2(x)^2\,\mathrm{d}x \\
        &= \int_\mathbb{R}\left(\sqrt{n(x)}\sin\frac{\pi}{2}s(x)\right)^2\,\mathrm{d}x \\
        &= \int_\mathbb{R}n(x)\sin^2\frac{\pi}{2}s(x)\,\mathrm{d}x &&\mid \sin^2x=\frac{1-\cos2x}{2} \\
        &= \int_\mathbb{R}n(x)\frac{1-\cos2\frac{\pi}{2}s(x)}{2}\,\mathrm{d}x \\
        &= \frac{1}{2}\int_\mathbb{R}n(x)\,\mathrm{d}x-\frac{1}{2}\int_\mathbb{R}n(x)\cos\pi s(x)\,\mathrm{d}x &&\mid\int_\mathbb{R}n(x)\,\mathrm{d}x=2 \\
        &= 1-\frac{1}{2}\int_\mathbb{R}n(x)\cos\pi s(x)\,\mathrm{d}x &&\mid u\overset{!}{=}s, \quad \frac{\mathrm{d}u}{\mathrm{d}x}=n(x) \ \Rightarrow \mathrm{d}x=\frac{\mathrm{d}u}{n(x)} \\
        &= 1-\frac{1}{2}\int_{x=\mathbb{R}}n(x)\cos\pi u\,\frac{\mathrm{d}u}{n(x)} \\
        &= 1-\frac{1}{2}\int_{x=\mathbb{R}}\cos\pi u\,\mathrm{d}u &&\mid \int\cos\pi x\,\mathrm{d}x=\frac{\sin\pi x}{\pi}+C \\
        &= 1-\left.\frac{\sin\pi u}{2\pi}\right|_{x=\mathbb{R}} &&\mid u=s\\
        &= 1-\left.\frac{\sin\pi s}{2\pi}\right|_\mathbb{R} \\
        &= 1-\frac{1}{2\pi}\left[\sin\pi s(+\infty)-\sin\pi s(-\infty)\right] &&\mid s(-\infty)=0, \ s(+\infty)=2 \\
        &= 1-\frac{1}{2\pi}\left[\sin2\pi-\sin0\right] &&\mid \sin2\pi=\sin0=0 \\
        &= 1-\frac{1}{2\pi}\left[0-0\right] \\
        &= 1
    \end{aligned}
$$

### Orthogonality

$$
    \begin{aligned}
        &\int_\mathbb{R}\phi_1(x)\phi_2(x)\,\mathrm{d}x \\
        &= \int_\mathbb{R}\sqrt{n(x)}\cos\frac{\pi}{2}s(x)\sqrt{n(x)}\sin\frac{\pi}{2}s(x)\,\mathrm{d}x \\
        &= \int_\mathbb{R}n(x)\cos\frac{\pi}{2}s(x)\sin\frac{\pi}{2}s(x)\,\mathrm{d}x &&\mid \cos \varphi\sin\varphi=\frac{\sin2\varphi}{2} \\
        &= \int_\mathbb{R}n(x)\frac{\sin\pi s(x)}{2}\,\mathrm{d}x &&\mid u(x)\overset{!}{=}s(x), \quad \frac{\mathrm{d}u}{\mathrm{d}x}=n(x) \ \Rightarrow \ \mathrm{d}x=\frac{\mathrm{d}u}{n(x)} \\
        &= \frac{1}{2}\int_{x=\mathbb{R}}n(x)\sin\pi u\,\frac{\mathrm{d}u}{n(x)} \\
        &= \frac{1}{2}\int_{x=\mathbb{R}}\sin\pi u\,\mathrm{d}u &&\mid \int\sin\pi x\,\mathrm{d}x=-\frac{\cos\pi x}{\pi}+C \\
        &= \frac{1}{2}\left.\frac{-\cos\pi u}{\pi}\right|_{x=\mathbb{R}} &&\mid u=s \\
        &= -\frac{1}{2\pi}\left.\cos\pi s\right|_\mathbb{R} \\
        &= -\frac{1}{2\pi}\left[\cos\pi s(+\infty)-\cos\pi s(-\infty)\right] &&\mid s(-\infty)=0, \ s(+\infty)=2 \\
        &= -\frac{1}{2\pi}\left[\cos2\pi-\cos0\right] &&\mid \cos2\pi=\cos0=1 \\
        &= -\frac{1}{2\pi}\left[1-1\right] \\
        &= 0
    \end{aligned}
$$
