# Oh look, a Polynomial

Choosing the [Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions) $(h_j)_{j\in\mathbb{N}_0}$ as our wavefunction basis allows us to split all functions (wavefunctions $\phi$ and density $n$) into a Gaussian and polynomial part.

## Wavefunctions

For the wavefunctions we have

$$
    \begin{aligned}
        &\phi(x) &&\mid f=\sum_{j\in\mathbb{N}_0}\braket{f|h_j}h_j \\
        &= \sum_{j\in\mathbb{N}_0}\phi_jh_j(x) &&\mid h_j(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x) \\
        &= \sum_{j\in\mathbb{N}_0}\phi_j\frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x) \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}\sum_{j\in\mathbb{N}_0}\phi_j\frac{H_j(x)}{\sqrt{2^jj!}} &&\mid p_\phi(x)\overset{!}{=}\sum_{j\in\mathbb{N}_0}\phi_j\frac{H_j(x)}{\sqrt{2^jj!}} \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_\phi(x) && p_\phi\in\mathbb{C}[X]
    \end{aligned}
$$

Similarly for its derivative

$$
    \begin{aligned}
        &\phi'(x) &&\mid \phi(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_\phi(x) \\
        &= \frac{\mathrm{d}}{\mathrm{d}x}\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_\phi(x) &&\mid \frac{\mathrm{d}}{\mathrm{d}x}e^{-\frac{x^2}{2}}=-e^{-\frac{x^2}{2}}x \\
        &= \frac{1}{\sqrt[4]{\pi}}\left(e^{-\frac{x^2}{2}}p_\phi'(x)-e^{-\frac{x^2}{2}}xp_\phi(x)\right) \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}\left(p_\phi'(x)-xp_\phi(x)\right) &&\mid p_{\phi'}(x)\overset{!}{=}p_\phi'(x)-xp_\phi(x) \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi'}(x) && p_{\phi'}\in\mathbb{C}[X]
    \end{aligned}
$$

!!! warning "Tripping hazard"

    $$
        p_{\phi'}(x)=p_\phi'(x)-xp_\phi(x) \neq p_\phi'(x)
    $$

## Density

Similar splitting holds for the density

$$
    \begin{aligned}
        n(x) &= \sum_{k=1}^N|\phi_k(x)|^2 &&\mid \phi_k(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi_k}(x) \\
        &= \sum_{k=1}^N\left|\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi_k}(x)\right|^2 \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\sum_{k=1}^N\left|p_{\phi_k}(x)\right|^2 &&\mid p_n(x)\overset{!}{=}\sum_{k=1}^N\left|p_{\phi_k}(x)\right|^2 \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}p_n(x) && p_n\in\mathbb{C}[X]
    \end{aligned}
$$

and its derivative

$$
    \begin{aligned}
        n'(x) &= \frac{\mathrm{d}}{\mathrm{d}x}\frac{e^{-x^2}}{\sqrt{\pi}}p_n(x) &&\mid \frac{\mathrm{d}}{\mathrm{d}x}e^{-x^2}=-e^{-x^2}2x \\
        &= \frac{1}{\sqrt{\pi}}\left(e^{-x^2}p_n'(x)-e^{-x^2}2xp_n(x)\right) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(p_n'(x)-2xp_n(x)\right) &&\mid p_{n'}\overset{!}{=}p_n'(x)-2xp_n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}p_{n'}(x) && p_{n'}\in\mathbb{C}[X]
    \end{aligned}
$$

!!! warning "Tripping hazard"

    $$
        p_{n'}(x)=p_n'(x)-2xp_n(x) \neq p_n'(x)
    $$

## Conclusion

$$
    \begin{aligned}
        \phi(x)   &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_\phi(x) & \phi'(x)     &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi'}(x) & n(x)   &= \frac{e^{-x^2}}{\sqrt{\pi}}p_n(x)        & n'(x)     &= \frac{e^{-x^2}}{\sqrt{\pi}}p_{n'}(x) \\
        p_\phi(x) &= \sqrt[4]{\pi}e^{+\frac{x^2}{2}}\phi(x)            & p_{\phi'}(x) &= \sqrt[4]{\pi}e^{+\frac{x^2}{2}}\phi'(x)              & p_n(x) &= \sqrt{\pi}e^{+x^2}n(x)                   & p_{n'}(x) &= \sqrt{\pi}e^{+x^2}n'(x) \\
                  &                                                    &              &= p_\phi'(x)-xp_\phi(x)                                &        &= \sum_{k=1}^N\left|p_{\phi_k}(x)\right|^2 &           &= p_n'(x)-2xp_n(x)
    \end{aligned}
$$

This representation as polynomials will accelerate computer algebra by the necessary magnitudes.

## Kinetic energy

$$
    \begin{aligned}
        T &= \frac{1}{2}\sum_{k=1}^N\int_\mathbb{R}|\phi_k'(x)|^2\,\mathrm{d}x &&\mid \phi_k'(x)=\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi_k'}(x) \\
        &= \frac{1}{2}\sum_{k=1}^N\int_\mathbb{R}\left|\frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}p_{\phi_k'}(x)\right|^2\,\mathrm{d}x \\
        &= \frac{1}{2\sqrt{\pi}}\sum_{k=1}^N\int_\mathbb{R}e^{-x^2}\left|p_{\phi_k'}(x)\right|^2\,\mathrm{d}x
    \end{aligned}
$$
