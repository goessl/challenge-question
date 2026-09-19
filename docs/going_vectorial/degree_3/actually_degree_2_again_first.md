# Actually Degree 2 Again First

As a primer for everything that is about to come let's try to solve the degree 2 case again, but just with basic algebra.

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
        &= h_0(x)\sum_jg_jh_j(x) \\
        \vec{g} &= \begin{pmatrix}
            \rho_{00} + \rho_{11} + \rho_{22} \\
            2\rho_{01} + 2\sqrt{2}\rho_{12} \\
            2\rho_{02} + \sqrt{2}\rho_{11} + 2\sqrt{2}\rho_{22} \\
            2\sqrt{3}\rho_{12} \\
            \sqrt{6}\rho_{22}
        \end{pmatrix}
    \end{aligned}
$$

where $g_j$ are the [pseudo product Hermite function coefficients](../products/series_representation_where_there_shouldnt_be_one.md).

$\vec{g}$ can always be fitted for some test density (that stems from two orthonormal Hermite function series of degree 2 of course).

!!! danger "Uniqueness"

    Is $\vec{g}$ unique?! Should be unique. Not that we redo what we have proved in the [Any Wavefunctions chapter](../../any_wavefunctions/discussion.md).

## Vector to matrix

The equations are of a useful form: they are sort of triangular.

When one starts from the bottom up to go back from $\vec{g}(\rho)$ to $\rho(\vec{g})$

- the equations are only ever linear
- and only have at most two unknowns
- (and the particle count is always the first coefficients).

So this is easy to revert:

$$
    \begin{aligned}
        \rho &= \begin{pmatrix}
            g_0-\frac{\sqrt{2}g_2}{6}-\frac{\sqrt{6}g_4}{18}+2t_2 & \frac{g_1}{2}-\frac{\sqrt{6}g_3}{6} & \frac{g_2}{3}-\frac{2\sqrt{3}g_4}{9}+\sqrt{2}t_2 \\
            \frac{g_1}{2}-\frac{\sqrt{6}g_3}{6} & \frac{\sqrt{2}g_2}{6}-\frac{\sqrt{6}g_4}{9}-2t_2 & \frac{\sqrt{3}g_3}{6} \\
            \frac{g_2}{3}-\frac{2\sqrt{3}g_4}{9}+\sqrt{2}t_2 & \frac{\sqrt{3}g_3}{6} & \frac{\sqrt{6}g_4}{6}
        \end{pmatrix} \\
        \braket{\hat{T}} &= \frac{g_0}{4}-\frac{\sqrt{2}g_2}{12}+\frac{2\sqrt{6}g_4}{9}-2t_2
    \end{aligned}
$$

with a remaining free parameter $t_2\in\mathbb{R}$ (from the $g_2=\dots$ equation).

## Free parameter

The free parameter must be fixed such that $\rho$ is a valid density matrix.

### Eigenvalues

The first choice would be to fix the eigenvalues to $\{0, 1, 1\}$ by equating coefficients of the characteristic polynomial:

$$
    \begin{aligned}
        \det\left(\rho-\lambda\right) &\overset{!}{=} \lambda(\lambda-1)^2 \\
        \lambda^3-g_0\lambda^2+\left(\dots t_2^2\dots\right)\lambda+\left(\dots t_2^3\dots\right) &= \lambda^3-2\lambda^2+\lambda \\
        \begin{pmatrix}
            1 \\
            g_0 \\
            \dots t_2^2\dots \\
            \dots t_2^3\dots
        \end{pmatrix} &= \begin{pmatrix}
            1 \\
            2 \\
            1 \\
            0
        \end{pmatrix}
    \end{aligned}
$$

!!! danger "Monic"

    sympy uses $\det\left(\lambda-\rho\right)$ so signs are flipping in here. TODO

We can see that $g_0$ always has to be $2$. We substitute that in to remove some of the many symbols.

The last two equations we could use to fix $t_2$ are higher order polynomials, which are unpleasant to solve. There is a better way.

### Idempotency

We can also force idempotency on $\rho$, which might not be sufficient, but is surely necessary. This gives an overdetermined system of lower degree polynomials; linear and at most quadratic. (Exact duplicates not listed.)

!!! danger "Sufficient with trace"

    Idempotency forces all eigenvalues $\{0, 1\}$, traces forces sum of eigenvalues $2$, so together they are sufficient.

$$
    \begin{aligned}
        \rho^2 &\overset{!}{=} \rho \\
        0 &= \rho^2-\rho \\
        0 &= \begin{pmatrix}
            6t_2^2+\left(-\frac{2\sqrt{6}g_4}{3}+6\right)t_2+\frac{g_1^2}{4}-\frac{\sqrt{6}g_1g_3}{6}+\frac{g_2^2}{6}-\frac{\sqrt{3}g_2g_4}{9}-\frac{\sqrt{2}g_2}{2}+\frac{g_3^2}{6}+\frac{g_4^2}{6}-\frac{\sqrt{6}g_4}{6}+2 \\
            \frac{\sqrt{6}g_3}{6}t_2-\frac{\sqrt{6}g_1g_4}{12}+\frac{g_1}{2}+\frac{\sqrt{3}g_2g_3}{18}+\frac{g_3g_4}{18}-\frac{\sqrt{6}g_3}{6} \\
            2\sqrt{2}t_2^2+\left(\frac{g_2}{3}-\frac{2\sqrt{3}g_4}{9}+\sqrt{2}\right)t_2+\frac{\sqrt{3}g_1g_3}{12}-\frac{\sqrt{2}g_2^2}{18}+\frac{2\sqrt{6}g_2g_4}{27}+\frac{g_2}{3}-\frac{\sqrt{2}g_3^2}{12}-\frac{2\sqrt{2}g_4^2}{27}-\frac{2\sqrt{3}g_4}{9} \\
            4t_2^2+\left(-\frac{2\sqrt{2}g_2}{3}+\frac{4\sqrt{6}g_4}{9}+2\right)t_2+\frac{g_1^2}{4}-\frac{\sqrt{6}g_1g_3}{6}+\frac{g_2^2}{18}-\frac{2\sqrt{3}g_2g_4}{27}-\frac{\sqrt{2}g_2}{6}+\frac{g_3^2}{4}+\frac{2g_4^2}{27}+\frac{\sqrt{6}g_4}{9} \\
            \left(\frac{\sqrt{2}g_1}{2}-\frac{2\sqrt{3}g_3}{3}\right)t_2+\frac{g_1g_2}{6}-\frac{\sqrt{3}g_1g_4}{9}-\frac{\sqrt{6}g_2g_3}{36}+\frac{5\sqrt{2}g_3g_4}{36}-\frac{\sqrt{3}g_3}{6} \\
            2t_2^2+\left(\frac{2\sqrt{2}g_2}{3}-\frac{4\sqrt{6}g_4}{9}\right)t_2+\frac{g_2^2}{9}-\frac{4\sqrt{3}g_2g_4}{27}+\frac{g_3^2}{12}+\frac{17g_4^2}{54}-\frac{\sqrt{6}g_4}{6}
        \end{pmatrix}
    \end{aligned}
$$

We **must not** just chose any of the linear equations and solve for $t_2$, as the $t_2$ factor might be zero (first coefficient in all linear equations dependent on $\vec{g}$) collapsing the linear equation to degeneracy!

### Linear combination

To get a linear equation in $t_2$ with a non-zero linear coefficient such that it can be solved every time without any singularities/edge cases we linearly combine the equations in a clever way (lots of recursive linear equation solving in the notebook; $\begin{pmatrix} 0 & 0 & \sqrt{2} & -\frac{1}{2} & 0 & -1 \end{pmatrix}$):

$$
    0 = t_2-\frac{g_1^2}{8}+\frac{\sqrt{6}g_1g_3}{6}-\frac{g_2^2}{4}+\frac{\sqrt{3}g_2g_4}{3}+\frac{5\sqrt{2}g_2}{12}-\frac{3g_3^2}{8}-\frac{g_4^2}{2}-\frac{\sqrt{6}g_4}{9}
$$

This uniquely fixes $t_2$. Solving and substituting into $\rho$ and $\braket{\hat{T}}$ finally gives:

$$
    \begin{aligned}
        \rho &= \begin{pmatrix}
            \frac{g_1^2}{4}-\frac{\sqrt{6}g_1g_3}{3}+\frac{g_2^2}{2}-\frac{2\sqrt{3}g_2g_4}{3}-\sqrt{2}g_2+\frac{3g_3^2}{4}+g_4^2+\frac{\sqrt{6}g_4}{6}+2 & \frac{g_1}{2}-\frac{\sqrt{6}g_3}{6} & \frac{\sqrt{2}g_1^2}{8}-\frac{\sqrt{3}g_1g_3}{3}+\frac{\sqrt{2}g_2^2}{4}-\frac{\sqrt{6}g_2g_4}{3}-\frac{g_2}{2}+\frac{3\sqrt{2}g_3^2}{8}+\frac{\sqrt{2}g_4^2}{2} \\
            \frac{g_1}{2}-\frac{\sqrt{6}g_3}{6} & -\frac{g_1^2}{4}+\frac{\sqrt{6}g_1g_3}{3}-\frac{g_2^2}{2}+\frac{2\sqrt{3}g_2g_4}{3}+\sqrt{2}g_2-\frac{3g_3^2}{4}-g_4^2-\frac{\sqrt{6}g_4}{3} & \frac{\sqrt{3}g_3}{6} \\
            \frac{\sqrt{2}g_1^2}{8}-\frac{\sqrt{3}g_1g_3}{3}+\frac{\sqrt{2}g_2^2}{4}-\frac{\sqrt{6}g_2g_4}{3}-\frac{g_2}{2}+\frac{3\sqrt{2}g_3^2}{8}+\frac{\sqrt{2}g_4^2}{2} & \frac{\sqrt{3}g_3}{6} & \frac{\sqrt{6}g_4}{6}
        \end{pmatrix} \\
        \braket{\hat{T}} &= -\frac{g_1^2}{4}+\frac{\sqrt{6}g_1g_3}{3}-\frac{g_2^2}{2}+\frac{2\sqrt{3}g_2g_4}{3}+\frac{3\sqrt{2}g_2}{4}-\frac{3g_3^2}{4}-g_4^2+\frac{1}{2}
    \end{aligned}
$$

There were no steps that would reduce generality, so the solution should be unique (no multiple $\rho$ or $T$ for some $\vec{g}$).

We weren't just able to find $\braket{\hat{T}}$, but also $\rho$!

!!! warning "Form of terms"

    WHY ARE ALL TERMS QUADRATIC EXCEPT $g_2$?! Because we've already substituted in $g_0=2$.

!!! danger "Numerical fitting 1"

    Show that numerical fitting also yields only one equation. Stengthens uniqueness finding.

!!! danger "Numerical fitting 2"

    Show that using the quadratic from the char poly coef equations would yield two $T$ candidates, and the cubic would then always verify only a single one.

[Notebook](rho2.ipynb)

## Uniqueness & boundaries

By doing a numeric implicit polynomial fit it can further be stated:

- $p(\vec{g}, T)=0$ quadratic in $\vec{g}$, monic and linear in $T$ is unique.
- This was for basis $\left(\ket{0}, \ket{1}, \ket{2}\right)$.
    For
    
    - $\left(\ket{0}, \ket{1}, \ket{3}\right)$
    - $\left(\ket{0}, \ket{2}, \ket{3}\right)$
    - $\left(\ket{1}, \ket{2}, \ket{3}\right)$
    
    the polynomial $p(\vec{g}, T)=0$ linear in $\vec{g}$ & $T$ converges.
    Always yielding two such polynomials:
    
    - one switch ($p(\vec{g})=0$ for an arbitrary degree 3 ensemble
        when on the corresponding degree 2 boundary)
    - one monic $p(\vec{g}, T)=0$ which can always be used to calculate $T$.

| Basis                                    | Switch                                               | $T$                                                                                                                                             |
| ---------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| $\left(\ket{0}, \ket{1}, \ket{2}\right)$ | $g_5$, $g_6$                                         | $T=-\frac{g_1^2}{4}+\frac{\sqrt{6}g_1g_3}{3}-\frac{g_2^2}{2}+\frac{2\sqrt{3}g_2g_4}{3}+\frac{3\sqrt{2}g_2}{4}-\frac{3g_3^2}{4}-g_4^2+\frac{1}{2}$ |
| $\left(\ket{0}, \ket{1}, \ket{3}\right)$ | $g_5$                                                | $T=\frac{\sqrt{2}g_2}{4}-\frac{\sqrt{6}g_4}{4}+\frac{9\sqrt{5}g_6}{20}+\frac{1}{2}$                                                               |
| $\left(\ket{0}, \ket{2}, \ket{3}\right)$ | $- \frac{\sqrt{30}}{3}g_1+g_5$                       | $T=-\frac{\sqrt{2}g_2}{4}+\frac{\sqrt{6}g_4}{3}-\frac{3\sqrt{5}g_6}{10}+\frac{1}{2}$                                                              |
| $\left(\ket{1}, \ket{2}, \ket{3}\right)$ | $\frac{\sqrt{30}}{3}g_1- \frac{2\sqrt{5}}{3}g_3+g_5$ | $T=-\frac{5\sqrt{2}g_2}{4}+\frac{\sqrt{6}g_4}{2}-\frac{3\sqrt{5}g_6}{10}+\frac{13}{2}$                                                            |

## Unorthonormalised

Interestingly $p(\vec{g}, T)=0$ can also be fitted uniquely and monic in $T$ for degree 3 EVEN WHEN THE TWO WAVEFUNCTIONS AREN'T ORTHONORMAL!!!

$$
    0=T^3+\left(-\frac{3g_0}{4}-\frac{\sqrt{2}g_2}{4}\right)T^2+\left(\frac{3g_0^2}{16}+\frac{\sqrt{2}g_0g_2}{8}-\frac{\sqrt{6}g_0g_4}{3}+\frac{\sqrt{6}g_1g_3}{6}-\frac{g_2^2}{8}+\frac{2\sqrt{3}g_2g_4}{3}-\frac{g_3^2}{2}-g_4^2\right)T-\frac{g_0^3}{64}-\frac{\sqrt{2}g_0^2g_2}{64}+\frac{\sqrt{6}g_0^2g_4}{12}-\frac{\sqrt{6}g_0g_1g_3}{24}+\frac{g_0g_2^2}{32}-\frac{\sqrt{3}g_0g_2g_4}{3}+\frac{7g_0g_3^2}{24}+\frac{11g_0g_4^2}{12}+\frac{\sqrt{6}g_1^2g_4}{12}-\frac{\sqrt{3}g_1g_2g_3}{12}-\frac{g_1g_3g_4}{3}+\frac{\sqrt{2}g_2^3}{32}+\frac{\sqrt{2}g_2g_3^2}{24}-\frac{\sqrt{2}g_2g_4^2}{4}+\frac{\sqrt{6}g_3^2g_4}{12}+\frac{\sqrt{6}g_4^3}{9}
$$

!!! danger "Splitting"

    Current guess:
    
    - At degree 2 there is no splitting. There is only one $\rho$ for every $\vec{g}$ and therefore also just one $T$.
    - Even if $\vec{g}(\rho)$ has a one dimensional kernel, it only ever intersects the symmetric matrices with eigenvalues 0, 1, 1 just once.
    - For the unorthonormalised case there is probably splitting. The implicit polynomial looks like $\det\rho$. Maximum branches 3 so that the polynomial yield all and only physical $T$s?

[Notebook](rho2_implicit_fit.ipynb)
