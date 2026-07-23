# Explicit Example

The basis:

$$
    \left(\ket{0}, \ket{1}, \ket{2}\right)
$$

The full-space kinetic energy:

$$
    \text{tr}\,\hat{T} = \text{tr}\,\frac{1}{4}\begin{pmatrix}
                1 &         0 & -\sqrt{2} \\
                0 &         3 &         0 \\
        -\sqrt{2} &         0 &         5
    \end{pmatrix} = \frac{9}{4}
$$

The orthonormal complement (here the [polynomial part representation](../products/oh_look_a_polynomial.md) becomes useful):

$$
    \begin{aligned}
        n^\perp(x) &= h_0(x)^2+h_1(x)^2+h_2(x)^2-n(x) \\
        &= \left(\frac{e^{-\frac{x^2}{2}}}{\sqrt{\sqrt{\pi}}}\right)^2+\left(\frac{e^{-\frac{x^2}{2}}2x}{\sqrt{2\sqrt{\pi}}}\right)^2+\left(\frac{e^{-\frac{x^2}{2}}(4x^2-2)}{\sqrt{8\sqrt{\pi}}}\right)^2-n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}\right)-n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}-p_n(x)\right) \\
        n^\perp{}'(x) &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x\right)-n'(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x-p_{n'}(x)\right)
    \end{aligned}
$$

The kinetic energy:

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{n^\perp{}'(x)^2}{n^\perp(x)}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{\left(\frac{e^{-x^2}}{\sqrt{\pi}}\left(-4x^5+8x^3-3x\right)-n'(x)\right)^2}{\frac{e^{-x^2}}{\sqrt{\pi}}\left(2x^4+\frac{3}{2}\right)-n(x)}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{4\sqrt{\pi}}\int_\mathbb{R}e^{-x^2}\frac{\left(-4x^5+8x^3-3x-p_{n'}(x)\right)^2}{4x^4+3-2p_n(x)}\,\mathrm{d}x
    \end{aligned}
$$

But additionaly we also want to have a look at the explicit parametrisation of all possible configuration as it comes together quite nicely.

## Parametrisation of 3D orthonormal pairs and their orthogonal complement

The natural choice would be to take a unit vector in (physicists') spherical coordinates

$$
    \vec{r} = \begin{pmatrix}
        \sin\theta\cos\varphi \\
        \sin\theta\sin\varphi \\
        \cos\theta
    \end{pmatrix} \qquad \theta\in[0,\pi], \ \varphi\in[0,2\pi[
$$

which has two orthonormal tangent vectors

$$
    \vec{\theta}=\begin{pmatrix}
        \cos\theta\cos\varphi \\
        \cos\theta\sin\varphi \\
        -\sin\theta
    \end{pmatrix} \qquad \vec{\varphi}=\begin{pmatrix}
        -\sin\varphi \\
        \cos\varphi \\
        0
    \end{pmatrix} \qquad \theta\in[0,\pi], \ \varphi\in[0,2\pi[
$$

where we just rotate within this two dimensional subspace with a third parameter

$$
    \begin{aligned}
        \vec{\phi_1} &= \cos\psi\vec{\theta}+\sin\psi\vec{\varphi}=\begin{pmatrix}
            \cos\theta\cos\varphi\cos\psi-\sin\varphi\sin\psi \\
            \cos\theta\sin\varphi\cos\psi+\cos\varphi\sin\psi \\
            -\sin\theta\cos\psi
        \end{pmatrix} \\
        \vec{\phi_2} &= \sin\psi\vec{\theta}-\cos\psi\vec{\varphi}=\begin{pmatrix}
            \cos\theta\cos\varphi\sin\psi+\sin\varphi\cos\psi \\
            \cos\theta\sin\varphi\sin\psi-\cos\varphi\cos\psi \\
            -\sin\theta\sin\psi
        \end{pmatrix}
    \end{aligned} \qquad \psi\in[0,2\pi[
$$

to parametrise all *oriented* orthonormal pairs in $\mathbb{R}^3$.

!!! warning "Abuse of notation"

    Here we use $\theta$ & $\varphi$ as angles, $\vec{\theta}$ & $\vec{\varphi}$ as vectors and $\ket{\theta}$ & $\ket{\varphi}$ as states.
    
    The $\vec{v}\doteq\ket{v}$ is usual in quantum mechanics, but using the symbols as angles and vectors simplifies the upcoming coefficient indexing ($\theta_1$ is easier to read than $(\vec{e}_\theta)_1$).

(But because of the [plane invariance](../../immediate_deductions.md#unitary-decomposition-invariance) we could ditch $\psi$ right here already and continue with $\vec{\theta}$ & $\vec{\varphi}$ as states. It would just change the measure by a constant factor. Let's keep it for the beginning for completeness.)

## States

$$
    \begin{aligned}
        \vec{r}       &\doteq \ket{r}       & \ket{r}       &= r_0\ket{0}+r_1\ket{1}+r_2\ket{2} \\
        \vec{\theta}  &\doteq \ket{\theta}  & \ket{\theta}  &= \theta_0\ket{0}+\theta_1\ket{1}+\theta_2\ket{2} \\
        \vec{\varphi} &\doteq \ket{\varphi} & \ket{\varphi} &= \varphi_0\ket{0}+\varphi_1\ket{1}+\varphi_2\ket{2} \\
                      &                     & \ket{\phi_1}  &= \cos\psi\ket{\theta}+\sin\psi\ket{\varphi} \\
                      &                     & \ket{\phi_2}  &= \sin\psi\ket{\theta}-\cos\psi\ket{\varphi}
    \end{aligned}
$$

## Density operators & matrices

$$
    \begin{aligned}
        \hat{\rho} &= \ket{\phi_1}\bra{\phi_1}+\ket{\phi_2}\bra{\phi_2} &&\mid \text{plane inv.} \\
        &= \ket{\theta}\bra{\theta}+\ket{\varphi}\bra{\varphi} &&\mid \ket{\theta}\bra{\theta}+\ket{\varphi}\bra{\varphi}+\ket{r}\bra{r}=1 \\
        &= 1-\ket{r}\bra{r} \\
        \rho &= 1-\vec{r}\vec{r}^T \\
        &= \begin{pmatrix}
            1-r_0^2  &  -r_0r_1 &  -r_0r_2 \\
             -r_0r_1 & 1-r_1^2  &  -r_1r_2 \\
             -r_0r_2 &  -r_1r_2 & 1-r_2^2
        \end{pmatrix} \\
        \hat{\rho}^\perp &= 1-\hat{\rho} \\
        &= \ket{r}\bra{r} \\
        \rho^\perp &= 1-\rho \\
        &= \vec{r}\vec{r}^T \\
        &= \begin{pmatrix}
             r_0^2 & r_0r_1 & r_0r_2 \\
            r_0r_1 &  r_1^2 & r_1r_2 \\
            r_0r_2 & r_1r_2 &  r_2^2
        \end{pmatrix}
    \end{aligned}
$$

Here we can already see that $\ket{r}$ is actually the hole state! Nice!

## Probability density distributions

$$
    \begin{aligned}
        n(x) &= \vec{h}(x)^T\rho\vec{h}(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}} \\
        &\qquad \left(2\left(1-r_2^2\right)x^4 \right. \\
        &\qquad -4r_1r_2x^3 \\
        &\qquad +2\left(-\sqrt{2}r_0r_2-r_1^2+r_2^2\right)x^2 \\
        &\qquad +2\left(-\sqrt{2}r_0r_1+r_1r_2\right)x \\
        &\qquad \left.-r_0^2+\sqrt{2}r_0r_2-\frac{r_2^2}{2}+\frac{3}{2} \right) \\
        n^\perp(x) &= h_0(x)^2+h_1(x)^2+h_2(x)^2 - n(x) \\
        &= \frac{e^{-x^2}}{\sqrt{\pi}} \\
        &\qquad \left(2r_2^2x^4 \right. \\
        &\qquad +4r_1r_2x^3 \\
        &\qquad +2\left(\sqrt{2}r_0r_2+r_1^2-r_2^2\right)x^2 \\
        &\qquad +2\left(\sqrt{2}r_0r_1-r_1r_2\right)x \\
        &\qquad \left.+r_0^2-\sqrt{2}r_0r_2+\frac{r_2^2}{2}\right)
    \end{aligned}
$$

*Isn't it strange that the normal vector on a plane is usually denoted as $n$, and here the plane normal vector describes the densities $n^{(\perp)}$?*

## Kinetic energy

Should be

$$
    \begin{aligned}
        \braket{\hat{T}} &= \text{tr}\,\hat{\rho}\hat{T} \\
        &= \text{tr}\,\begin{pmatrix}
            1-r_0^2 & -r_0r_1 & -r_0r_2 \\
            -r_0r_1 & 1-r_1^2 & -r_1r_2 \\
            -r_0r_2 & -r_1r_2 & 1-r_2^2
        \end{pmatrix}\frac{1}{4}\begin{pmatrix}
                    1 & 0 & -\sqrt{2} \\
                    0 & 3 & 0 \\
            -\sqrt{2} & 0 & 5
        \end{pmatrix} \\
        &= 2-\frac{r_1^2}{2}-r_2^2+\frac{r_0r_2}{\sqrt{2}}
    \end{aligned}
$$

($r$ only ever appears quadratically in $\rho^{(\perp)}$, $n^{(\perp)}$ & $T$ which makes the choice of the direction of the plane normal vector on an unoriented plane irrelevant. Exactly as needed.)

And our formula predicts

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{9}{4}-T[n^\perp] \\
        &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{n^\perp{}'(x)^2}{n^\perp(x)}\,\mathrm{d}x
    \end{aligned}
$$

where we substitute in an educated guess

$$
    r(x) = \frac{e^\frac{-x^2}{2}}{\sqrt[4]{\pi}}\left(\sqrt{2}r_2x^2+\sqrt{2}r_1x+r_0-\frac{r_2}{\sqrt{2}}\right)
$$

that luckily has the following properties

$$
    \begin{aligned}
        n^\perp(x) &= r(x)^2 \\
        n^\perp{}'(x) &= 2r(x)r'(x)
    \end{aligned}
$$

because of which we can solve the Gaussian-rational integral easily

$$
    \begin{aligned}
        \braket{\hat{T}} &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{n^\perp{}'(x)^2}{n^\perp(x)}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{8}\int_\mathbb{R}\frac{\left(2r(x)r'(x)\right)^2}{r(x)^2}\,\mathrm{d}x \\
        &= \frac{9}{4}-\frac{1}{2}\int_\mathbb{R}r'(x)^2\,\mathrm{d}x \\
        &= 2-\frac{r_1^2}{2}-r_2^2+\frac{r_0r_2}{\sqrt{2}}
    \end{aligned}
$$
