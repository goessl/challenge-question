# Explicit Example

The basis:

$$
    \left(\ket{0}, \ket{1}\right)
$$

The parametrised set of all unordered admissible wavefunction pairs:

$$
    \begin{aligned}
        \vec{\phi_1} &= \begin{pmatrix}
            \cos\varphi \\
            \sin\varphi
        \end{pmatrix} \quad \vec{\phi_2}=\begin{pmatrix}
            \sin\varphi \\
            -\cos\varphi
        \end{pmatrix} \qquad \varphi\in[0,2\pi[ \\
        \\
        \ket{\phi_1} &= \cos\varphi\ket{0}+\sin\varphi\ket{1} \\
        \ket{\phi_2} &= \sin\varphi\ket{0}-\cos\varphi\ket{1}
    \end{aligned}
$$

The kinetic energy:

$$
    \begin{aligned}
        \braket{\hat{T}} &= \text{tr}\,\hat{T} \\
        &= \text{tr}\,\frac{1}{4}\begin{pmatrix}
                    1 &         0 \\
                    0 &         3
        \end{pmatrix} \\
        &= 1
    \end{aligned}
$$

So $\hat{\rho}$ and $T$ are constant one.
