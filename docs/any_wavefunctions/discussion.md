# Discussion

So we've found that there may be multiple ensembles with different kinetic energies and the same particle density.

This would mean that there is no functional $T[n]$.

Luckily time will save us:

For a (precise adjectives from [mathematical foundation](../immediate_deductions.md#mathematical-foundation)) potential the total energy is

$$
    \begin{aligned}
        E &= \sum_{k=1}^NE_k \\
        &= \sum_{k=1}^N\braket{\phi_k|\hat{H}|\phi_k} \\
        &= \sum_{k=1}^N\braket{\phi_k|\hat{T}+\hat{V}|\phi_k} \\
        &= \sum_{k=1}^N\braket{\phi_k|\hat{T}|\phi_k}+\sum_{k=1}^N\braket{\phi_k|\hat{V}|\phi_k} \\
        &= \braket{\hat{T}}_\phi+\sum_{k=1}^N\bra{\phi_k}\int_\mathbb{R}V(x)\ket{x}\bra{x}\,\mathrm{d}x\ket{\phi_k} \\
        &= \braket{\hat{T}}_\phi+\int_\mathbb{R}V(x)\sum_{k=1}^N\braket{\phi_k|x}\braket{x|\phi_k}\,\mathrm{d}x \\
        &= \braket{\hat{T}}_\phi+\int_\mathbb{R}V(x)n(x)\,\mathrm{d}x
    \end{aligned}
$$

We can see that the potential energy is purely determined by the particle density, while the kinetic energy isn't. This means that the **ensemble will automatically collapse to the one with the lowest kinetic energy**.

This is precisely [Levy/Levy-Lieb(?)](https://physics.stackexchange.com/questions/69618/constrained-search-formulation-of-dft-by-levy-or-by-levy-lieb) constrained search:

$$
    T[n] = \min_{\{\phi_k\}\to n}\braket{\hat{T}}_\phi
$$

which is a functional of $n$ alone again.

We've *found* all valid canditates. We just have to pick the correct one.

## Refinement of the previous results

Applying this to the [previous result](whole_solution_set.md#real-case) for the kinetic energy for a particle density of two real wavefunctions gives

$$
    \begin{aligned}
        \braket{\hat{T}} &= \min_\alpha\left(\frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}+4n(x)\alpha'(x)^2\,\mathrm{d}x\right) \\
        &= \frac{1}{8}\int_\mathbb{R}\frac{n'(x)^2}{n(x)}\mathrm{d}x+\frac{1}{2}\min_\alpha\int_\mathbb{R}n(x)\alpha'(x)^2\,\mathrm{d}x
    \end{aligned} \qquad \alpha:\mathbb{R}\to[0,2\pi[, \ \int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x=0
$$

A constant $\alpha$ would minimise the second term, but it cannot satisfy the constraint, as $\int_\mathbb{R}n(x)e^{i2\alpha}\,\mathrm{d}x=2e^{i2\alpha}\neq0$.

## Adapting the approach

Minimising over all $\alpha:\mathbb{R}\to[0,2\pi[$ is an infinite dimensional problem. For that we will restrict the wavefunctions to a finite basis in the next part [Going Vectorial](../going_vectorial/choosing_a_basis.md).

!!! question "Kinetic energy spectrum"

    Scanning through all admissible $\alpha$ produces a whole spectrum of kinetic energies containing the genuine $T$ as its minimum. Is that spectrum an interval $[T, \infty[$?
    
    Does the space of angles $\alpha$ have a natural measure? If so, does the induced distribution of kinetic energies carry any interesting information? Maybe there is even a simple transformation.

!!! question "Variation"

    Could Euler-Lagrange be used to find the minimising $\alpha$ or minimised $T$?

!!! question "Schrödinger"

    We didn't use Schrödinger yet.
