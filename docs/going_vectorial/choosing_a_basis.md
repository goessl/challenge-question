# Choosing a Basis

To work with functions and operators in a manageable (parameterisable, computer assisted) manner, we need to represent them as vectors and matrices.

We naturally choose the solutions of the harmonic oscillator $(\ket{j})_{j\in\mathbb{N}_0}$, as they are a complete orthonormal basis and therefore don't restrict generality. To avoid confusion with the density $n(x)$, we label them $\ket{j}$ (instead of $\ket{n}$). Their position-space representatives are the [Hermite functions](https://en.wikipedia.org/wiki/Hermite_polynomials#Hermite_functions)

$$
    \braket{x|j} = h_j(x) = \frac{e^{-\frac{x^2}{2}}}{\sqrt{2^jj!\sqrt{\pi}}}H_j(x)
$$

where $H_j$ denotes the $j$-th Hermite polynomial.

## Wavefunctions

Any state $\ket{\phi}$ decomposes as

$$
    \ket{\phi}=\sum_{j\in\mathbb{N}_0}\phi_j\ket{j} \qquad \phi_j=\braket{j|\phi} \qquad \phi(x)=\sum_{j\in\mathbb{N}_0}\phi_jh_j(x)
$$

## Operators

The ladder operators become

$$
    \begin{aligned}
        a^\dagger_{ij}&=\braket{i|\hat{a}^\dagger|j} & a_{ij}&=\braket{i|\hat{a}|j} \\
        &=\braket{i|\sqrt{j+1}|j+1} & &= \braket{i|\sqrt{j}|j-1} \\
        &=\sqrt{j+1}\delta_{i,j+1} & &= \sqrt{j}\delta_{i,j-1} \\
        a^\dagger&=\begin{pmatrix}
            0 &        0 &        0 & 0 \\
            1 &        0 &        0 & 0 & \cdots \\
            0 & \sqrt{2} &        0 & 0 \\
            0 &        0 & \sqrt{3} & 0 \\
              &   \vdots &          &   & \ddots
        \end{pmatrix} & a&=\begin{pmatrix}
            0 &      1 &        0 & 0 \\
            0 &      0 & \sqrt{2} & 0        & \cdots \\
            0 &      0 &        0 & \sqrt{3} \\
            0 &      0 &        0 & 0 \\
              & \vdots &          &   & \ddots
        \end{pmatrix}
    \end{aligned}
$$

giving

$$
    \begin{aligned}
        T &= -\frac{\left(a^\dagger-a\right)^2}{4} \\
        &= \frac{1}{4}\begin{pmatrix}
                    1 &         0 &  -\sqrt{2} &          0 &          0 &          0 &          0 \\
                    0 &         3 &          0 &  -\sqrt{6} &          0 &          0 &          0 & \cdots \\
            -\sqrt{2} &         0 &          5 &          0 & -\sqrt{12} &          0 &          0 \\
                    0 & -\sqrt{6} &          0 &          7 &          0 & -\sqrt{20} &          0 \\
                    0 &         0 & -\sqrt{12} &          0 &          9 &          0 & -\sqrt{30} \\
                    0 &         0 &          0 & -\sqrt{20} &          0 &         11 &          0 \\
                    0 &         0 &          0 &            & -\sqrt{30} &          0 &         13 \\
                      &    \vdots &            &            &            &            &            & \ddots
        \end{pmatrix}.
    \end{aligned}
$$
