# Degree 1 - Full Occupation

This is a special case: we have full occupation.

When the space, in which we are quantum mechanically wobbling around, has exactly the same dimensionality as the number of particles within, we have full occupation.

More precisely:

$$
    \begin{gathered}
        \text{dim}\,\mathcal{H}=N \quad \text{or equivalently} \quad \mathcal{H}=\text{ran}\left\{\phi_k\right\}_{k\in\{1, 2, \dots, N\}} \\
        \Downarrow \\
        \hat{\rho}=1 \qquad \braket{\hat{T}}=\text{tr}\,\hat{T}=\text{const.}
    \end{gathered}
$$

## Proof

$$
    \begin{aligned}
        \hat{\rho} &= \sum_{k=1}^N\ket{\phi_k}\bra{\phi_k} \\
        &= 1 \\
        \braket{\hat{T}} &= \text{tr}\,\hat{\rho}\hat{T} \\
        &= \text{tr}\,\hat{T}
    \end{aligned}
$$

## Hermite function case

The basis:

$$
    \left(\ket{0}, \ket{1}\right)
$$

The parametrised set of all admissible wavefunction pairs:

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
