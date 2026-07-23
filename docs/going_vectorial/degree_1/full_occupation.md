# Full Occupation

This is a special case: we have full occupation.

When the space, in which we are quantum mechanically wobbling around, has exactly the same dimensionality as the number of particles within, we have full occupation and only one possible constant value for the kinetic energy.

More precisely:

$$
    \begin{gathered}
        \text{dim}\,\mathcal{H}=N \quad \text{or equivalently} \quad \mathcal{H}=\text{ran}\left\{\phi_k\right\}_{k=1}^N \\
        \Downarrow \\
        \hat{\rho}=1 \qquad \braket{\hat{T}}=\text{tr}\,\hat{T}=\text{const.}
    \end{gathered}
$$

## Proof

$$
    \begin{aligned}
        \hat{\rho} &= \sum_{k=1}^N\ket{\phi_k}\bra{\phi_k} = 1 \\
        \braket{\hat{T}} &= \text{tr}\,\hat{\rho}\hat{T} = \text{tr}\,\hat{T}
    \end{aligned}
$$
