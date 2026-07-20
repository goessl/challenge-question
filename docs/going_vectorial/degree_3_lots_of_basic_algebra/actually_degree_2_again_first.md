# Actually Degree 2 Again First

As a primer for everything that is about to come let's try to solve the degree 2 case purely with basic algebra.

For a density matrix (symmetry already baked into coefficients)

$$
    \rho = \begin{pmatrix}
        \rho_{00} & \rho_{01} & \rho_{02} \\
        \rho_{01} & \rho_{11} & \rho_{12} \\
        \rho_{02} & \rho_{12} & \rho_{22}
    \end{pmatrix}
$$

the kinetic energy is

$$
    \braket{\hat{T}} = \text{tr}\,\hat{\rho}\hat{T} = \frac{\rho_{00}}{4}-\frac{\sqrt{2}\rho_{02}}{2}+\frac{3\rho_{11}}{4}+\frac{5\rho_{22}}{4}
$$

the probability density distribution has the form

$$
    \begin{aligned}
        n(x) &= \sum_{ij}\rho_{ij}h_i(x)h_j(x) \\
        &= \frac{e^{-\frac{x^2}{2}}}{\sqrt[4]{\pi}}\sum_jp_jh_j(x) \\
        \vec{p} &= \begin{pmatrix}
            \rho_{00} + \rho_{11} + \rho_{22} \\
            2\rho_{01} + 2\sqrt{2}\rho_{12} \\
            2\rho_{02} + \sqrt{2}\rho_{11} + 2\sqrt{2}\rho_{22} \\
            2\sqrt{3}\rho_{12} \\
            \sqrt{6}\rho_{22}
        \end{pmatrix}
    \end{aligned}
$$

which can always be uniquely fitted for some test density (that stems from two orthonormal Hermite function series of degree 2 of course).

It has a quite useful property:

When one starts from the bottom up to go back from $\vec{p}(\rho)$ to $\rho(\vec{p})$

- the equations are only ever linear
- and only have at most two unknowns
- (and the particle count is always the first coefficients).

So this is easy to revert:

$$
    \begin{aligned}
        \rho &= \begin{pmatrix}
            p_0-\frac{\sqrt{2}p_2}{6}-\frac{\sqrt{6}p_4}{18}+2t_2 & \frac{p_1}{2}-\frac{\sqrt{6}p_3}{6} & \frac{p_2}{3}-\frac{2\sqrt{3}p_4}{9}+\sqrt{2}t_2 \\
            \frac{p_1}{2}-\frac{\sqrt{6}p_3}{6} & \frac{\sqrt{2}p_2}{6}-\frac{\sqrt{6}p_4}{9}-2t_2 & \frac{\sqrt{3}p_3}{6} \\
            \frac{p_2}{3}-\frac{2\sqrt{3}p_4}{9}+\sqrt{2}t_2 & \frac{\sqrt{3}p_3}{6} & \frac{\sqrt{6}p_4}{6}
        \end{pmatrix} \\
        \braket{\hat{T}} &= \frac{p_0}{4}-\frac{\sqrt{2}p_2}{12}+\frac{2\sqrt{6}p_4}{9}+2t_2
    \end{aligned}
$$

with a remaining free parameter $t_2\in\mathbb{R}$ (from the $p_2=\dots$ equation).
