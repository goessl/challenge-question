# Degree 3 - Almost all Solutions

Now we do the same as before but for the degree 3 case.

The density and other expressions:

$$
    \begin{aligned}
        \rho &= \begin{pmatrix}\rho_{00}&\rho_{01}&\rho_{02}&\rho_{03} \\
            \rho_{01}&\rho_{11}&\rho_{12}&\rho_{13} \\
            \rho_{02}&\rho_{12}&\rho_{22}&\rho_{23} \\
            \rho_{03}&\rho_{13}&\rho_{23}&\rho_{33}
        \end{pmatrix} \\
        \braket{\hat{T}} &= \frac{\rho_{00}}{4}-\frac{\sqrt{2}\rho_{02}}{2}+\frac{3\rho_{11}}{4}-\frac{\sqrt{6}\rho_{13}}{2}+\frac{5\rho_{22}}{4}+\frac{7\rho_{33}}{4} \\
        \vec{g} &= \begin{pmatrix}
            \rho_{00}+\rho_{11}+\rho_{22}+\rho_{33} \\
            2\rho_{01}+2\sqrt{2}\rho_{12}+2\sqrt{3}\rho_{23} \\
            2\rho_{02}+\sqrt{2}\rho_{11}+2\sqrt{3}\rho_{13}+2\sqrt{2}\rho_{22}+3\sqrt{2}\rho_{33} \\
            2\rho_{03}+2\sqrt{3}\rho_{12}+6\sqrt{2}\rho_{23} \\
            4\rho_{13}+\sqrt{6}\rho_{22}+3\sqrt{6}\rho_{33} \\
            2\sqrt{10}\rho_{23} \\
            2\sqrt{5}\rho_{33}
        \end{pmatrix}
    \end{aligned}
$$

## Vector to matrix

This time we have to introduce 3 free parameters $t_2, t_3, t_4\in\mathbb{R}$.

$$
    \begin{aligned}
        \rho &= \begin{pmatrix}
            g_0-\frac{\sqrt{2}g_2}{6}+\frac{\sqrt{6}g_4}{22}-\frac{9\sqrt{5}g_6}{110}+2t_2-\frac{10t_4}{3}&\frac{g_1}{2}-\frac{\sqrt{6}g_3}{8}+\frac{\sqrt{30}g_5}{40}+2\sqrt{2}t_3&\frac{g_2}{3}-\frac{2\sqrt{3}g_4}{11}+\frac{7\sqrt{10}g_6}{110}+\sqrt{2}t_2-\frac{2\sqrt{2}t_4}{3}&\frac{g_3}{8}-\frac{3\sqrt{5}g_5}{40}+2\sqrt{3}t_3 \\
            \frac{g_1}{2}-\frac{\sqrt{6}g_3}{8}+\frac{\sqrt{30}g_5}{40}+2\sqrt{2}t_3&\frac{\sqrt{2}g_2}{6}-\frac{\sqrt{6}g_4}{11}+\frac{7\sqrt{5}g_6}{110}-2t_2-\frac{2t_4}{3}&\frac{\sqrt{3}g_3}{8}-\frac{3\sqrt{15}g_5}{40}-2t_3&\frac{2g_4}{11}-\frac{3\sqrt{30}g_6}{55}-\sqrt{6}t_4 \\
            \frac{g_2}{3}-\frac{2\sqrt{3}g_4}{11}+\frac{7\sqrt{10}g_6}{110}+\sqrt{2}t_2-\frac{2\sqrt{2}t_4}{3}&\frac{\sqrt{3}g_3}{8}-\frac{3\sqrt{15}g_5}{40}-2t_3&\frac{\sqrt{6}g_4}{22}-\frac{9\sqrt{5}g_6}{110}+4t_4&\frac{\sqrt{10}g_5}{20} \\
            \frac{g_3}{8}-\frac{3\sqrt{5}g_5}{40}+2\sqrt{3}t_3&\frac{2g_4}{11}-\frac{3\sqrt{30}g_6}{55}-\sqrt{6}t_4&\frac{\sqrt{10}g_5}{20}&\frac{\sqrt{5}g_6}{10}
        \end{pmatrix} \\
        \braket{\hat{T}} &= \frac{g_0}{4}-\frac{\sqrt{2}g_2}{12}+\frac{\sqrt{5}g_6}{5}-2t_2+\frac{22t_4}{3}
    \end{aligned}
$$

## Free parameters

These are now a huge problem as they don't allow us to solve it easily.

### Eigenvalues

$\text{trace}\,\rho\overset{!}{=}2$ again fixes $g_0=2$.

The other characteristic polynomial coefficients equations are a system of polynomials in $t_2, t_3, t_4$ of degrees

- (2, 2, 2)
- (3, 2, 3)
- (3, 4, 4)

Three unknowns and three equations should be sufficient, but this system doesn't let itself solve easily. But we can deduce that $\braket{\hat{T}}$ is algebraic in $\vec{g}$ and there are at most 24 (?) solutions.

`sympy` resultants are to slow.

!!! danger "C++"

    Implement resultant elimination in C++.

### Idempotency

We again go by fixing $\rho^2\overset{!}{=}\rho$, yielding 16 equations, that we linearly combine with an arbitrary vector $\vec{a}$. It is chosen such that all qudratic terms vanish leaving:

$$
    \begin{aligned}
        \vec{a} &= \begin{pmatrix}
            a_0 \\
            a_1 \\
            a_2 \\
            a_3 \\
            f(a_0, a_1, a_2, a_3) \\
            \vdots
        \end{pmatrix} \\
        0 &= \left(2\sqrt{2}a_0g_2-2\sqrt{6}a_0g_4+2\sqrt{5}a_0g_6+2a_0-a_1g_1+\frac{5\sqrt{6}a_1g_3}{6}-\frac{2\sqrt{30}a_1g_5}{5}+a_2g_2-\frac{2\sqrt{3}a_2g_4}{3}+\frac{\sqrt{10}a_2g_6}{5}-\frac{\sqrt{6}a_3g_1}{2}+2a_3g_3-\frac{4\sqrt{5}a_3g_5}{5}\right)t_2
        &\qquad +\left(4\sqrt{2}a_0g_1-2\sqrt{3}a_0g_3+2a_1g_2-\frac{4\sqrt{3}a_1g_4}{3}+\frac{2\sqrt{10}a_1g_6}{5}-2a_2g_1+\frac{4\sqrt{6}a_2g_3}{3}-\frac{8\sqrt{30}a_2g_5}{15}\right)t_3
        &\qquad +\left(-\frac{4\sqrt{2}a_0g_2}{3}+\frac{10\sqrt{6}a_0g_4}{3}-\frac{86\sqrt{5}a_0g_6}{15}-\frac{10a_0}{3}-\frac{4a_1g_1}{3}-\frac{19\sqrt{6}a_1g_3}{18}+\frac{6\sqrt{30}a_1g_5}{5}+\frac{a_2g_2}{3}-\frac{2\sqrt{3}a_2g_4}{9}+\frac{\sqrt{10}a_2g_6}{15}-\frac{\sqrt{6}a_3g_1}{6}-\frac{7a_3g_3}{3}+\frac{32\sqrt{5}a_3g_5}{15}\right)t_4
        &\qquad -\frac{a_0g_1^2}{4}+\frac{\sqrt{6}a_0g_1g_3}{4}-\frac{\sqrt{30}a_0g_1g_5}{10}+\frac{a_0g_2^2}{6}-\frac{\sqrt{3}a_0g_2g_4}{33}-\frac{13\sqrt{10}a_0g_2g_6}{330}-\frac{\sqrt{2}a_0g_2}{6}-\frac{3a_0g_3^2}{8}+\frac{3\sqrt{5}a_0g_3g_5}{8}-\frac{3a_0g_4^2}{11}+\frac{\sqrt{30}a_0g_4g_6}{5}-\frac{5\sqrt{6}a_0g_4}{11}-\frac{3a_0g_5^2}{5}-\frac{64a_0g_6^2}{55}+\frac{56\sqrt{5}a_0g_6}{55}+2a_0-\frac{\sqrt{2}a_1g_1g_2}{6}+\frac{3\sqrt{6}a_1g_1g_4}{44}-\frac{4\sqrt{5}a_1g_1g_6}{55}+\frac{a_1g_1}{2}+\frac{11\sqrt{3}a_1g_2g_3}{72}-\frac{7\sqrt{15}a_1g_2g_5}{120}-\frac{5a_1g_3g_4}{44}+\frac{\sqrt{30}a_1g_3g_6}{1320}+\frac{7\sqrt{5}a_1g_4g_5}{220}+\frac{91\sqrt{6}a_1g_5g_6}{1320}-\frac{2\sqrt{30}a_1g_5}{15}-\frac{\sqrt{2}a_2g_1^2}{8}+\frac{5\sqrt{3}a_2g_1g_3}{24}-\frac{3\sqrt{15}a_2g_1g_5}{40}-\frac{\sqrt{2}a_2g_2^2}{12}+\frac{10\sqrt{6}a_2g_2g_4}{99}-\frac{19\sqrt{5}a_2g_2g_6}{165}+\frac{a_2g_2}{2}-\frac{\sqrt{2}a_2g_3^2}{8}+\frac{\sqrt{10}a_2g_3g_5}{10}-\frac{\sqrt{2}a_2g_4^2}{11}+\frac{4\sqrt{15}a_2g_4g_6}{55}-\frac{\sqrt{3}a_2g_4}{3}-\frac{\sqrt{2}a_2g_5^2}{10}-\frac{9\sqrt{2}a_2g_6^2}{110}+\frac{\sqrt{10}a_2g_6}{10}-\frac{\sqrt{3}a_3g_1g_2}{6}+\frac{4a_3g_1g_4}{11}-\frac{13\sqrt{30}a_3g_1g_6}{220}+\frac{\sqrt{2}a_3g_2g_3}{12}+\frac{\sqrt{10}a_3g_2g_5}{60}-\frac{3\sqrt{6}a_3g_3g_4}{44}+\frac{4\sqrt{5}a_3g_3g_6}{55}+\frac{a_3g_3}{2}-\frac{\sqrt{30}a_3g_4g_5}{110}+\frac{9a_3g_5g_6}{110}-\frac{2\sqrt{5}a_3g_5}{5}
    \end{aligned}
$$

Just by superimposing only one of the free variables could be eliminated, but never two such that one would be determined, because they all have $g_j$ as factors which can't be divided away.

### Selection

But we can plug in

$$
    \vec{a} = \vec{e}_0, \vec{e}_1, \vec{e}_2, \vec{e}_3
$$

to get four linear equations. We take the first three and write it in matrix form:

$$
    \begin{aligned}
        &\begin{pmatrix}
            2\sqrt{2}g_2-2\sqrt{6}g_4+2\sqrt{5}g_6+2&4\sqrt{2}g_1-2\sqrt{3}g_3&-\frac{4\sqrt{2}g_2}{3}+\frac{10\sqrt{6}g_4}{3}-\frac{86\sqrt{5}g_6}{15}-\frac{10}{3} \\
            -g_1+\frac{5\sqrt{6}g_3}{6}-\frac{2\sqrt{30}g_5}{5}&2g_2-\frac{4\sqrt{3}g_4}{3}+\frac{2\sqrt{10}g_6}{5}&-\frac{4g_1}{3}-\frac{19\sqrt{6}g_3}{18}+\frac{6\sqrt{30}g_5}{5} \\
            g_2-\frac{2\sqrt{3}g_4}{3}+\frac{\sqrt{10}g_6}{5}&-2g_1+\frac{4\sqrt{6}g_3}{3}-\frac{8\sqrt{30}g_5}{15}&\frac{g_2}{3}-\frac{2\sqrt{3}g_4}{9}+\frac{\sqrt{10}g_6}{15}
        \end{pmatrix} \\
        &\quad \begin{pmatrix}
            t_2 \\
            t_3 \\
            t_4
        \end{pmatrix} \\
        &= \begin{pmatrix}
            \frac{g_1^2}{4}-\frac{\sqrt{6}g_1g_3}{4}+\frac{\sqrt{30}g_1g_5}{10}-\frac{g_2^2}{6}+\frac{\sqrt{3}g_2g_4}{33}+\frac{13\sqrt{10}g_2g_6}{330}+\frac{\sqrt{2}g_2}{6}+\frac{3g_3^2}{8}-\frac{3\sqrt{5}g_3g_5}{8}+\frac{3g_4^2}{11}-\frac{\sqrt{30}g_4g_6}{5}+\frac{5\sqrt{6}g_4}{11}+\frac{3g_5^2}{5}+\frac{64g_6^2}{55}-\frac{56\sqrt{5}g_6}{55}-2 \\
            \frac{\sqrt{2}g_1g_2}{6}-\frac{3\sqrt{6}g_1g_4}{44}+\frac{4\sqrt{5}g_1g_6}{55}-\frac{g_1}{2}-\frac{11\sqrt{3}g_2g_3}{72}+\frac{7\sqrt{15}g_2g_5}{120}+\frac{5g_3g_4}{44}-\frac{\sqrt{30}g_3g_6}{1320}-\frac{7\sqrt{5}g_4g_5}{220}-\frac{91\sqrt{6}g_5g_6}{1320}+\frac{2\sqrt{30}g_5}{15} \\
            \frac{\sqrt{2}g_1^2}{8}-\frac{5\sqrt{3}g_1g_3}{24}+\frac{3\sqrt{15}g_1g_5}{40}+\frac{\sqrt{2}g_2^2}{12}-\frac{10\sqrt{6}g_2g_4}{99}+\frac{19\sqrt{5}g_2g_6}{165}-\frac{g_2}{2}+\frac{\sqrt{2}g_3^2}{8}-\frac{\sqrt{10}g_3g_5}{10}+\frac{\sqrt{2}g_4^2}{11}-\frac{4\sqrt{15}g_4g_6}{55}+\frac{\sqrt{3}g_4}{3}+\frac{\sqrt{2}g_5^2}{10}+\frac{9\sqrt{2}g_6^2}{110}-\frac{\sqrt{10}g_6}{10}
        \end{pmatrix}
    \end{aligned}
$$

Using Cramer to solve it gives three rational solutions. Plugging them in gives a rational $\rho$ to large to print here and

$$
    \braket{\hat{T}} = -\frac{\sqrt{2}g_2}{12}+\frac{\sqrt{5}g_6}{5}+\frac{1}{2}+\frac{-5\left(-2\sqrt{2}g_1+\sqrt{3}g_3\right)\left(-\left(-120g_1-95\sqrt{6}g_3+108\sqrt{30}g_5\right)\left(495\sqrt{2}g_1^2-825\sqrt{3}g_1g_3+297\sqrt{15}g_1g_5+330\sqrt{2}g_2^2-400\sqrt{6}g_2g_4+456\sqrt{5}g_2g_6-1980g_2+495\sqrt{2}g_3^2-396\sqrt{10}g_3g_5+360\sqrt{2}g_4^2-288\sqrt{15}g_4g_6+1320\sqrt{3}g_4+396\sqrt{2}g_5^2+324\sqrt{2}g_6^2-396\sqrt{10}g_6\right)+2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)\left(660\sqrt{2}g_1g_2-270\sqrt{6}g_1g_4+288\sqrt{5}g_1g_6-1980g_1-605\sqrt{3}g_2g_3+231\sqrt{15}g_2g_5+450g_3g_4-3\sqrt{30}g_3g_6-126\sqrt{5}g_4g_5-273\sqrt{6}g_5g_6+528\sqrt{30}g_5\right)\right)+55\left(-2\sqrt{2}g_1+\sqrt{3}g_3\right)\left(\left(-30g_1+25\sqrt{6}g_3-12\sqrt{30}g_5\right)\left(495\sqrt{2}g_1^2-825\sqrt{3}g_1g_3+297\sqrt{15}g_1g_5+330\sqrt{2}g_2^2-400\sqrt{6}g_2g_4+456\sqrt{5}g_2g_6-1980g_2+495\sqrt{2}g_3^2-396\sqrt{10}g_3g_5+360\sqrt{2}g_4^2-288\sqrt{15}g_4g_6+1320\sqrt{3}g_4+396\sqrt{2}g_5^2+324\sqrt{2}g_6^2-396\sqrt{10}g_6\right)-2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)\left(660\sqrt{2}g_1g_2-270\sqrt{6}g_1g_4+288\sqrt{5}g_1g_6-1980g_1-605\sqrt{3}g_2g_3+231\sqrt{15}g_2g_5+450g_3g_4-3\sqrt{30}g_3g_6-126\sqrt{5}g_4g_5-273\sqrt{6}g_5g_6+528\sqrt{30}g_5\right)\right)-\left(-\left(-120g_1-95\sqrt{6}g_3+108\sqrt{30}g_5\right)\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)+2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)^2\right)\left(330g_1^2-330\sqrt{6}g_1g_3+132\sqrt{30}g_1g_5-220g_2^2+40\sqrt{3}g_2g_4+52\sqrt{10}g_2g_6+220\sqrt{2}g_2+495g_3^2-495\sqrt{5}g_3g_5+360g_4^2-264\sqrt{30}g_4g_6+600\sqrt{6}g_4+792g_5^2+1536g_6^2-1344\sqrt{5}g_6-2640\right)+11\left(\left(-30g_1+25\sqrt{6}g_3-12\sqrt{30}g_5\right)\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)-2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)^2\right)\left(330g_1^2-330\sqrt{6}g_1g_3+132\sqrt{30}g_1g_5-220g_2^2+40\sqrt{3}g_2g_4+52\sqrt{10}g_2g_6+220\sqrt{2}g_2+495g_3^2-495\sqrt{5}g_3g_5+360g_4^2-264\sqrt{30}g_4g_6+600\sqrt{6}g_4+792g_5^2+1536g_6^2-1344\sqrt{5}g_6-2640\right)+220\left(-\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)\left(660\sqrt{2}g_1g_2-270\sqrt{6}g_1g_4+288\sqrt{5}g_1g_6-1980g_1-605\sqrt{3}g_2g_3+231\sqrt{15}g_2g_5+450g_3g_4-3\sqrt{30}g_3g_6-126\sqrt{5}g_4g_5-273\sqrt{6}g_5g_6+528\sqrt{30}g_5\right)+\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)\left(495\sqrt{2}g_1^2-825\sqrt{3}g_1g_3+297\sqrt{15}g_1g_5+330\sqrt{2}g_2^2-400\sqrt{6}g_2g_4+456\sqrt{5}g_2g_6-1980g_2+495\sqrt{2}g_3^2-396\sqrt{10}g_3g_5+360\sqrt{2}g_4^2-288\sqrt{15}g_4g_6+1320\sqrt{3}g_4+396\sqrt{2}g_5^2+324\sqrt{2}g_6^2-396\sqrt{10}g_6\right)\right)\left(\sqrt{2}g_2-\sqrt{6}g_4+\sqrt{5}g_6+1\right)-4\left(\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)\left(660\sqrt{2}g_1g_2-270\sqrt{6}g_1g_4+288\sqrt{5}g_1g_6-1980g_1-605\sqrt{3}g_2g_3+231\sqrt{15}g_2g_5+450g_3g_4-3\sqrt{30}g_3g_6-126\sqrt{5}g_4g_5-273\sqrt{6}g_5g_6+528\sqrt{30}g_5\right)-\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)\left(495\sqrt{2}g_1^2-825\sqrt{3}g_1g_3+297\sqrt{15}g_1g_5+330\sqrt{2}g_2^2-400\sqrt{6}g_2g_4+456\sqrt{5}g_2g_6-1980g_2+495\sqrt{2}g_3^2-396\sqrt{10}g_3g_5+360\sqrt{2}g_4^2-288\sqrt{15}g_4g_6+1320\sqrt{3}g_4+396\sqrt{2}g_5^2+324\sqrt{2}g_6^2-396\sqrt{10}g_6\right)\right)\left(-10\sqrt{2}g_2+25\sqrt{6}g_4-43\sqrt{5}g_6-25\right)}{264\left(75\left(-2\sqrt{2}g_1+\sqrt{3}g_3\right)\left(3g_1+4\sqrt{6}g_3-4\sqrt{30}g_5\right)\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)+5\left(-\left(-120g_1-95\sqrt{6}g_3+108\sqrt{30}g_5\right)\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)+2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)^2\right)\left(\sqrt{2}g_2-\sqrt{6}g_4+\sqrt{5}g_6+1\right)+\left(\left(-30g_1+25\sqrt{6}g_3-12\sqrt{30}g_5\right)\left(-15g_1+10\sqrt{6}g_3-4\sqrt{30}g_5\right)-2\left(15g_2-10\sqrt{3}g_4+3\sqrt{10}g_6\right)^2\right)\left(-10\sqrt{2}g_2+25\sqrt{6}g_4-43\sqrt{5}g_6-25\right)\right)}
$$

## The problem and the possible solutions

For some configurations the linear inversion might not be possible $\det=0$. These are probably the situations where $\rho[n]$ & $T[n]$ are not unique (see [the any_wavefunctions discussion](../../any_wavefunctions/discussion.md)).

!!! danger "Almost all"

    The $\det=0$ configurations have measure $0$. But at least it is a solution for almost all configurations.
    
    TODO: proof (determinant histogram).
    
    Claude say codimension 1, intersection of all triple-picks determinats 0 is dim 2.

!!! danger "Classification"

    Classify all configurations where the solution doesn't work. Maybe the hole can be patched by hand if there are only finitely many ones.

!!! danger "Picks"

    We took three out of four equations. Same will happen for another 3/4 pick, but the denominator might be different. If it could be proven that always at least one of the solutions isn't $0/0$, they could be combined to a single solution that is always correct.
    Maybe combine them by taking the pseudo inverse of the $4 \times 3$ matrix. Acc to Claude it covers all cases any 3-out-of-4-picks can solve into a single equation, but it may still happen to collapse.

!!! danger "Resultants"

    Linear combination of idempotency equations was used because sympys resultants and everything else in this package is way to slow. Maybe a result can be found by implementing faster multivariate polynomials and just resultanting the characteristic polynomial coefficient equations togethers. Will probably yield the same implicit polynomial as mentioned in the addendum.

!!! danger "Other form"

    Maybe the solution could be given as a quadratic polynomial in $T$ and $\vec{g}$, where the roots of $T$ are the possible solutions. This could have the same behaviour: when the solution is unique, the discriminant vanishes, and when the solution is two-fold, the discriminant appears and splits the solution space.
    
    THATS IIITTTTT!!!!!!!!!!!!!!!!!

!!! danger "Splitting"

    At degree 3 there is splitting. Explicit example: [Notebook](rho3_splitting_example.ipynb)

[Notebook](rho3.ipynb)

## Addendum 25.07.2026, 04.08.2026, 10.09.2026 & 19.09.2026

There is an implicit polynomial solution:

$$
    \begin{aligned}
        0 &= \left(\frac{36g_1}{275}-\frac{48\sqrt{30}g_5}{1375}\right)T^2 \\
        &\qquad +\left(\frac{24\sqrt{2}g_1g_2}{275}+\frac{4\sqrt{6}g_1g_4}{275}-\frac{24\sqrt{5}g_1g_6}{275}-\frac{216g_1}{275}-\frac{38\sqrt{3}g_2g_3}{275}+\frac{108\sqrt{15}g_2g_5}{1375}+\frac{12g_3g_4}{275}+\frac{34\sqrt{30}g_3g_6}{1375}+\frac{56\sqrt{6}g_3}{275}-\frac{24\sqrt{5}g_4g_5}{275}+\frac{4\sqrt{6}g_5g_6}{125}+\frac{64\sqrt{30}g_5}{1375}\right)T \\
        &\qquad -\frac{2g_1^{3}}{275}+\frac{17\sqrt{6}g_1^2g_3}{1650}-\frac{14\sqrt{30}g_1^2g_5}{4125}-\frac{41g_1g_2^2}{550}+\frac{98\sqrt{3}g_1g_2g_4}{825}-\frac{14\sqrt{10}g_1g_2g_6}{275}-\frac{51\sqrt{2}g_1g_2}{275}-\frac{7g_1g_3^2}{275}+\frac{2\sqrt{5}g_1g_3g_5}{125}-\frac{32g_1g_4^2}{275}+\frac{8\sqrt{30}g_1g_4g_6}{375}-\frac{2\sqrt{6}g_1g_4}{75}-\frac{16g_1g_5^2}{1375}+\frac{16g_1g_6^2}{1375}+\frac{276\sqrt{5}g_1g_6}{1375}+g_1-\frac{\sqrt{6}g_2^2g_3}{66}+\frac{71\sqrt{30}g_2^2g_5}{4125}-\frac{3\sqrt{2}g_2g_3g_4}{275}+\frac{9\sqrt{15}g_2g_3g_6}{275}+\frac{93\sqrt{3}g_2g_3}{275}-\frac{2\sqrt{10}g_2g_4g_5}{55}-\frac{166\sqrt{3}g_2g_5g_6}{4125}-\frac{734\sqrt{15}g_2g_5}{4125}+\frac{\sqrt{6}g_3^{3}}{330}-\frac{4\sqrt{30}g_3^2g_5}{1375}+\frac{4\sqrt{6}g_3g_4^2}{275}-\frac{52\sqrt{5}g_3g_4g_6}{1375}-\frac{2g_3g_4}{11}+\frac{6\sqrt{6}g_3g_5^2}{1375}-\frac{4\sqrt{6}g_3g_6^2}{825}-\frac{257\sqrt{30}g_3g_6}{4125}-\frac{28\sqrt{6}g_3}{75}+\frac{8\sqrt{30}g_4^2g_5}{1375}+\frac{72g_4g_5g_6}{1375}+\frac{276\sqrt{5}g_4g_5}{1375}-\frac{8\sqrt{30}g_5^{3}}{20625}-\frac{16\sqrt{30}g_5g_6^2}{6875}-\frac{34\sqrt{6}g_5g_6}{1375}+\frac{4\sqrt{30}g_5}{125}
    \end{aligned}
$$

This is unique, but it may collapse! Almost never, but still might.

!!! danger "Spurious solutions"

    Check if, when there are multiple solutions, that all are physical.
    
    Guess: All are physical.

!!! danger "Complexity"

    Like a characteristic polynomial. Polynomial constructions seems easy (polynomial); root finding must not be more complex that Schrödinger, otherwise useless.

Fitting a unique monic cubic and quartic worked. They never collapse.

Cubic:

$$
    \begin{aligned}
        0 &= 1.0T^3 \\
        &\qquad +\left(0.00820386275926463g_1^2g_2+0.080051268643822g_1^2g_4-0.16069517371298g_1^2g_6+0.0690613060525224g_1^2-0.0381703104207746g_1g_2g_3+0.0996444136249371g_1g_2g_5-0.0748720899961234g_1g_3g_4+0.30947618057138g_1g_3g_6-0.21819729827135g_1g_3+0.0222583971791465g_1g_4g_5-0.227843506854142g_1g_5g_6+0.00724562168511799g_1g_5+0.0864823467628957g_2^3-0.222205351220082g_2^2g_4+0.312811900966812g_2^2g_6-0.337774927952783g_2^2+0.107995331111263g_2g_3^2-0.426281748421653g_2g_3g_5+0.162615504056177g_2g_4^2-0.698812125547307g_2g_4g_6+0.954647618654152g_2g_4+0.247953636431785g_2g_5^2+0.340322502027302g_2g_6^2-0.181579290989088g_2g_6-0.00197414291462645g_2+0.0760502544965962g_3^2g_4-0.304689553533335g_3^2g_6+0.0606171638562588g_3^2+0.158968426612624g_3g_4g_5+0.151567873989889g_3g_5g_6+0.0471347385226397g_3g_5-0.0844311234706127g_4^3+0.692718665013587g_4^2g_6-0.457111763301875g_4^2-0.254882716601344g_4g_5^2-1.06876971785868g_4g_6^2+0.274440140758247g_4g_6-0.178187342734673g_4+0.257430103320162g_5^2g_6-0.0909472178348727g_5^2+0.689531487635394g_6^3-0.621773743069036g_6^2-0.424217110110501g_6-4.81424806721132\right)T^2 \\
        &\qquad +\left(-0.09349736709315g_1^4+0.212371614187413g_1^3g_3-0.144630006124082g_1^3g_5+0.0954176174988761g_1^2g_2^2+0.0127514769628656g_1^2g_2g_4-0.182607425346627g_1^2g_2g_6-0.16527703839176g_1^2g_2-0.158843240195228g_1^2g_3^2+0.221280529581512g_1^2g_3g_5-0.0782588753837427g_1^2g_4^2+0.126274368928281g_1^2g_4g_6+0.0448869752717954g_1^2g_4-0.0516674482569313g_1^2g_5^2+0.135386553898957g_1^2g_6^2-0.023608780996001g_1^2g_6+0.14321917937652g_1^2-0.18277882401048g_1g_2^2g_3+0.1942911594239g_1g_2^2g_5+0.201388758634109g_1g_2g_3g_4+0.0969457617734779g_1g_2g_3g_6+0.126228902710351g_1g_2g_3-0.335572779244596g_1g_2g_4g_5-0.0279458799183106g_1g_2g_5g_6-0.259096018187192g_1g_2g_5+0.0309162724204538g_1g_3^3+0.0118002355538057g_1g_3^2g_5-0.0536933662963496g_1g_3g_4^2+0.24244383061934g_1g_3g_4g_6-0.490909374594773g_1g_3g_4-0.169888973050259g_1g_3g_5^2-0.654709459496986g_1g_3g_6^2+0.36460845655552g_1g_3g_6+0.435548565300034g_1g_3+0.125621792052146g_1g_4^2g_5-0.0915901994718353g_1g_4g_5g_6+0.362779251046544g_1g_4g_5+0.0895053662030472g_1g_5^3+0.274125890548916g_1g_5g_6^2-0.0125872790786103g_1g_5g_6+0.161060271128102g_1g_5+0.0187151446506676g_2^4-0.128949048725604g_2^3g_4+0.0197788152998078g_2^3g_6-0.158080269604127g_2^3+0.0981052282644651g_2^2g_3^2-0.210378324660193g_2^2g_3g_5+0.312240076809927g_2^2g_4^2-0.281893884066361g_2^2g_4g_6+0.762684120416623g_2^2g_4+0.140043764820683g_2^2g_5^2-0.145585768697088g_2^2g_6^2-0.501584495681596g_2^2g_6+0.408500396445395g_2^2-0.204815249326508g_2g_3^2g_4-0.158491911302473g_2g_3^2g_6-0.101316161222496g_2g_3^2+0.572912186242878g_2g_3g_4g_5+0.479447534634591g_2g_3g_5g_6+0.335616821637729g_2g_3g_5-0.346789917398123g_2g_4^3+0.584783832768677g_2g_4^2g_6-0.604600136624242g_2g_4^2-0.438604535176434g_2g_4g_5^2+0.296980615998634g_2g_4g_6^2+0.694826460703385g_2g_4g_6-2.45798679490051g_2g_4-0.211637198233863g_2g_5^2g_6+0.0833278892531774g_2g_5^2-0.377616745094051g_2g_6^3-0.0849855663940871g_2g_6^2+0.463608282793283g_2g_6-0.575809768537715g_2+0.0130414974174139g_3^4-0.118000672195773g_3^3g_5+0.107804946618062g_3^2g_4^2-0.203707921495942g_3^2g_4g_6+0.112403625502225g_3^2g_4+0.315532160799795g_3^2g_5^2+0.50200906411093g_3^2g_6^2+0.433858184158941g_3^2g_6-0.468830767506678g_3^2-0.325526392137482g_3g_4^2g_5-0.0526587664494684g_3g_4g_5g_6-0.368646093116226g_3g_4g_5-0.302428919241996g_3g_5^3-0.295664058970073g_3g_5g_6^2-0.394835655312512g_3g_5g_6+0.667067806549695g_3g_5+0.137254160538319g_4^4-0.259003454517733g_4^3g_6+0.205782100679399g_4^3+0.270976170020961g_4^2g_5^2-0.448825347534361g_4^2g_6^2-0.959266850260707g_4^2g_6+1.35935584372697g_4^2+0.161966600505505g_4g_5^2g_6+0.141223480481954g_4g_5^2+1.11979413059592g_4g_6^3+1.06477581776802g_4g_6^2-0.0317132132142681g_4g_6+1.37527895592497g_4+0.0835625202634867g_5^4-0.238359911110197g_5^2g_6^2-0.138113427979656g_5^2g_6+0.00935501677617237g_5^2-0.731227198498025g_6^4-0.366095742467336g_6^3+1.7395780946609g_6^2-1.18711118624188g_6+8.31658945277042\right)T \\
        &\qquad +0.0249809749103989g_1^4g_2-0.0373309146520375g_1^4g_4+0.0864447739984642g_1^4g_6+0.0961660639112355g_1^4-0.00259897580016634g_1^3g_2g_3+0.00144263486140742g_1^3g_2g_5+0.032806605657568g_1^3g_3g_4-0.220859529945387g_1^3g_3g_6-0.146421069194687g_1^3g_3-0.00654602971077551g_1^3g_4g_5+0.0983827040586953g_1^3g_5g_6+0.108779272878599g_1^3g_5-0.0306075898963999g_1^2g_2^3+0.150230240405198g_1^2g_2^2g_4+0.0104400606265283g_1^2g_2^2g_6-0.443652726998672g_1^2g_2^2-0.010624327185178g_1^2g_2g_3^2-0.0463953471775828g_1^2g_2g_3g_5-0.150648403736061g_1^2g_2g_4^2-0.190107703196168g_1^2g_2g_4g_6+0.674096296068826g_1^2g_2g_4+0.012968729004955g_1^2g_2g_5^2+0.178235237879937g_1^2g_2g_6^2+0.147958036287554g_1^2g_2g_6-0.303952238791528g_1^2g_2+0.0176230039375571g_1^2g_3^2g_4+0.171517208061375g_1^2g_3^2g_6-0.0321581300264865g_1^2g_3^2+0.00664757642035437g_1^2g_3g_4g_5-0.112668361321051g_1^2g_3g_5g_6-0.0891374280220815g_1^2g_3g_5+0.0515016218271198g_1^2g_4^3+0.166213336465029g_1^2g_4^2g_6-0.328322856745984g_1^2g_4^2+0.00248125499467684g_1^2g_4g_5^2-0.225481912980536g_1^2g_4g_6^2-0.182510671001464g_1^2g_4g_6+0.419072825737065g_1^2g_4-0.0194878288497582g_1^2g_5^2g_6+0.113603581091485g_1^2g_5^2+0.0167861325888076g_1^2g_6^3+0.178903833098659g_1^2g_6^2+0.0874238527419921g_1^2g_6-0.670111193883177g_1^2-0.0480392776089379g_1g_2^3g_3+0.131586739659133g_1g_2^3g_5-0.0572747371439243g_1g_2^2g_3g_4+0.0738649564083687g_1g_2^2g_3g_6+0.419101114303695g_1g_2^2g_3-0.171841411386978g_1g_2^2g_4g_5-0.118537327223334g_1g_2^2g_5g_6-0.211742390269726g_1g_2^2g_5-0.0412965089474946g_1g_2g_3^3+0.175431095190871g_1g_2g_3^2g_5+0.0705136193682765g_1g_2g_3g_4^2+0.0706859089681443g_1g_2g_3g_4g_6-0.489976383825817g_1g_2g_3g_4-0.124833566847448g_1g_2g_3g_5^2-0.016246433874843g_1g_2g_3g_6^2-0.495450643412631g_1g_2g_3g_6+0.958650035531396g_1g_2g_3+0.109224926957362g_1g_2g_4^2g_5+0.205597656445719g_1g_2g_4g_5g_6+0.199130265231277g_1g_2g_4g_5+0.056728526083143g_1g_2g_5^3-0.137923992808632g_1g_2g_5g_6^2+0.138102949544984g_1g_2g_5g_6-0.690934996123192g_1g_2g_5-0.00891457931405788g_1g_3^3g_4-0.00892735730884557g_1g_3^3g_6+0.12096208164611g_1g_3^3-0.0632760437412924g_1g_3^2g_4g_5-0.100380793356669g_1g_3^2g_5g_6-0.105253899498954g_1g_3^2g_5-0.0207943922560457g_1g_3g_4^3-0.138087409647373g_1g_3g_4^2g_6+0.346286140737198g_1g_3g_4^2+0.054402279483081g_1g_3g_4g_5^2+0.0370463620014702g_1g_3g_4g_6^2+0.490678942158979g_1g_3g_4g_6-0.836316451756957g_1g_3g_4+0.219969598966307g_1g_3g_5^2g_6-0.03915187590862g_1g_3g_5^2+0.17763736926068g_1g_3g_6^3-0.355910814992837g_1g_3g_6^2-0.501642421799996g_1g_3g_6+0.964567958995766g_1g_3-0.0323925593379295g_1g_4^3g_5-0.0514275626995433g_1g_4^2g_5g_6-0.120754919635661g_1g_4^2g_5-0.0404646691161102g_1g_4g_5^3+0.0995970592801875g_1g_4g_5g_6^2-0.445498292292829g_1g_4g_5g_6+0.683510885919671g_1g_4g_5-0.0851989395657206g_1g_5^3g_6+0.0331435291044339g_1g_5^3-0.117069783070707g_1g_5g_6^3+0.501768222938711g_1g_5g_6^2+0.236668723419698g_1g_5g_6-0.891855060615155g_1g_5+0.0231804790375013g_2^5-0.063729254840415g_2^4g_4+0.0882926845855984g_2^4g_6-0.0320629193460772g_2^4+0.0740377601941353g_2^3g_3^2-0.174221402737463g_2^3g_3g_5+0.0377131689721987g_2^3g_4^2-0.250540975643308g_2^3g_4g_6+0.0993847294220856g_2^3g_4+0.0418647463157476g_2^3g_5^2+0.122321869363175g_2^3g_6^2+0.111977766956889g_2^3g_6-0.40821628570032g_2^3-0.0555873234473746g_2^2g_3^2g_4+0.0532942465540847g_2^2g_3^2g_6-0.25685909167632g_2^2g_3^2+0.211171030187832g_2^2g_3g_4g_5-0.253741093539613g_2^2g_3g_5g_6+0.403157205558109g_2^2g_3g_5+0.0255402560354738g_2^2g_4^3+0.290612082755373g_2^2g_4^2g_6-0.116156117132392g_2^2g_4^2-0.0291989131320917g_2^2g_4g_5^2-0.426399351225945g_2^2g_4g_6^2-0.0861020485632511g_2^2g_4g_6+0.466404517302205g_2^2g_4+0.255163284331774g_2^2g_5^2g_6-0.15695012028345g_2^2g_5^2+0.27417199250912g_2^2g_6^3+0.0582426648067082g_2^2g_6^2-0.734956313200029g_2^2g_6+1.15936568348993g_2^2+0.0348233702891216g_2g_3^4-0.160101080241341g_2g_3^3g_5+0.0391166816129984g_2g_3^2g_4^2-0.139209883759027g_2g_3^2g_4g_6+0.185328353086281g_2g_3^2g_4+0.221836769257366g_2g_3^2g_5^2+0.0334869980007928g_2g_3^2g_6^2+0.20762184129035g_2g_3^2g_6-0.199887293173326g_2g_3^2-0.132816950546407g_2g_3g_4^2g_5+0.309009138368603g_2g_3g_4g_5g_6-0.382489374643812g_2g_3g_4g_5-0.139631500858387g_2g_3g_5^3-0.0791426001688959g_2g_3g_5g_6^2-0.0119903899186042g_2g_3g_5g_6+0.424747482540797g_2g_3g_5-0.0315204494781623g_2g_4^4-0.14358186964982g_2g_4^3g_6+0.134073001423479g_2g_4^3-0.00386627007341686g_2g_4^2g_5^2+0.378679942289365g_2g_4^2g_6^2-0.240758477654188g_2g_4^2g_6-0.440454754772162g_2g_4^2-0.25275559146031g_2g_4g_5^2g_6+0.259667224611431g_2g_4g_5^2-0.405528583442347g_2g_4g_6^3-0.321111564569675g_2g_4g_6^2+1.85626054045263g_2g_4g_6+0.126461997868064g_2g_4+0.00779794284761423g_2g_5^4+0.00172950607285837g_2g_5^2g_6^2-0.190904433079924g_2g_5^2g_6-0.467961810370007g_2g_5^2+0.0587909813896631g_2g_6^4+0.518380412653973g_2g_6^3-0.553513398307279g_2g_6^2-0.0267849595198952g_2g_6-0.175679525417373g_2-0.00896209039970536g_3^4g_4-0.0269224452190558g_3^4g_6-0.0476870940834557g_3^4+0.0901444219473686g_3^3g_4g_5+0.108471399803263g_3^3g_5g_6+0.145795359186349g_3^3g_5-0.0204992680397542g_3^2g_4^3+0.10360062438698g_3^2g_4^2g_6-0.125665047068107g_3^2g_4^2-0.155688051510737g_3^2g_4g_5^2+0.00267217650581623g_3^2g_4g_6^2-0.125741480472107g_3^2g_4g_6+0.422430659306165g_3^2g_4-0.183767378083052g_3^2g_5^2g_6-0.251489846873191g_3^2g_5^2-0.140956566773096g_3^2g_6^3-0.0216392568067722g_3^2g_6^2-0.0786678212484551g_3^2g_6-0.434770904235847g_3^2+0.05145823165665g_3g_4^3g_5-0.159498788125432g_3g_4^2g_5g_6+0.209484833120636g_3g_4^2g_5+0.121503563812036g_3g_4g_5^3+0.0939625882154961g_3g_4g_5g_6^2+0.231760071642886g_3g_4g_5g_6-0.755666645034293g_3g_4g_5+0.10969278589414g_3g_5^3g_6+0.239277744367465g_3g_5^3+0.0728666709275916g_3g_5g_6^3-0.335358662281539g_3g_5g_6^2+0.00697580222719558g_3g_5g_6+0.280262562010558g_3g_5+0.00747127556616675g_4^5+0.0307409408503238g_4^4g_6-0.0743503263702694g_4^4-0.00182981373098444g_4^3g_5^2-0.148898965981505g_4^3g_6^2+0.123566028802918g_4^3g_6+0.232968064938794g_4^3+0.0929396225864081g_4^2g_5^2g_6-0.16103070339081g_4^2g_5^2+0.317501409892023g_4^2g_6^3+0.693682361807703g_4^2g_6^2-0.88691904645365g_4^2g_6-0.600157038464857g_4^2-0.0171158644007967g_4g_5^4-0.0876474408416593g_4g_5^2g_6^2-0.129562281079998g_4g_5^2g_6+0.61648589972552g_4g_5^2-0.317864959957373g_4g_6^4-1.53285465907796g_4g_6^3+1.17313009638028g_4g_6^2-0.762573575475275g_4g_6-0.925122264800303g_4-0.0158617562881765g_5^4g_6-0.046595763692245g_5^4+0.0793825522991339g_5^2g_6^3+0.532466289744593g_5^2g_6^2-0.312518578421966g_5^2g_6-0.462565640280535g_5^2+0.178576918786335g_6^5+0.925746344764767g_6^4-1.46757097835903g_6^3-0.968409976174655g_6^2+3.16447104369203g_6-4.61758344863857
    \end{aligned}
$$

Quartic:

$$
    \begin{aligned}
        0 &= 1.0T^4 \\
        &\qquad +\left(-27.0g_1+1.1g_2-13.0g_3-2.6g_4+61.0g_5+2.7g_6-6.1\right)T^3 \\
        &\qquad +\left(-0.14g_1^2-34.0g_1g_2+0.56g_1g_3+12.0g_1g_4-6.4g_1g_5+18.0g_1g_6+1.7\cdot10^2g_1-0.055g_2^2+38.0g_2g_3-0.48g_2g_4-34.0g_2g_5+0.2g_2g_6-4.3g_2-5.0g_3^2+1.1g_3g_4+15.0g_3g_5-14.0g_3g_6-61.0g_3+0.25g_4^2-3.3g_4g_5+0.96g_4g_6+13.0g_4-1.4g_5^2-7.7g_5g_6-1.3\cdot10^2g_5-0.79g_6^2-18.0g_6+13.0\right)T^2 \\
        &\qquad +\left(-1.9g_1^3+0.72g_1^2g_2+3.3g_1^2g_3-2.0g_1^2g_4+2.3g_1^2g_5+4.0g_1^2g_6-1.7g_1^2+4.6g_1g_2^2-5.4g_1g_2g_3-2.9g_1g_2g_4-1.0g_1g_2g_5+3.7g_1g_2g_6+65.0g_1g_2+0.86g_1g_3^2+7.1g_1g_3g_4-14.0g_1g_3g_5-10.0g_1g_3g_6+9.0g_1g_3-1.7g_1g_4^2-7.6g_1g_4g_5+8.8g_1g_4g_6-51.0g_1g_4+12.0g_1g_5^2+17.0g_1g_5g_6+30.0g_1g_5-8.6g_1g_6^2-28.0g_1g_6-1.8\cdot10^2g_1-0.059g_2^3+5.1g_2^2g_3-0.086g_2^2g_4-6.3g_2^2g_5+0.21g_2^2g_6+0.92g_2^2+2.8g_2g_3^2-4.3g_2g_3g_4+9.1g_2g_3g_5-12.0g_2g_3g_6-70.0g_2g_3+0.17g_2g_4^2+1.5g_2g_4g_5-0.089g_2g_4g_6+1.2g_2g_4-15.0g_2g_5^2+18.0g_2g_5g_6+44.0g_2g_5-0.057g_2g_6^2-1.9g_2g_6+3.2g_2-2.8g_3^3-3.0g_3^2g_4+17.0g_3^2g_5+7.1g_3^2g_6+7.3g_3^2-1.4g_3g_4^2+1.1g_3g_4g_5+2.1g_3g_4g_6+9.0g_3g_4-25.0g_3g_5^2-19.0g_3g_5g_6-61.0g_3g_5-0.1g_3g_6^2+54.0g_3g_6+1.1\cdot10^2g_3+0.011g_4^3+4.6g_4^2g_5-0.35g_4^2g_6-1.1g_4^2+8.9g_4g_5^2-11.0g_4g_5g_6+49.0g_4g_5+0.63g_4g_6^2-2.8g_4g_6-20.0g_4+13.0g_5^3+2.2g_5^2g_6+21.0g_5^2+8.9g_5g_6^2-60.0g_5g_6+46.0g_5-0.63g_6^3+4.5g_6^2+40.0g_6-8.8\right)T \\
        &\qquad -0.019g_1^4-1.3g_1^3g_2-0.5g_1^3g_3+6.0g_1^3g_4+0.84g_1^3g_5-4.5g_1^3g_6-7.4g_1^3-0.27g_1^2g_2^2+0.35g_1^2g_2g_3+1.1g_1^2g_2g_4+1.6g_1^2g_2g_5-1.7g_1^2g_2g_6-0.46g_1^2g_2+0.92g_1^2g_3^2-12.0g_1^2g_3g_4-1.8g_1^2g_3g_5+9.7g_1^2g_3g_6+21.0g_1^2g_3-1.2g_1^2g_4^2+5.3g_1^2g_4g_5+4.1g_1^2g_4g_6+1.8g_1^2g_4+0.27g_1^2g_5^2-5.4g_1^2g_5g_6-19.0g_1^2g_5-3.4g_1^2g_6^2-5.4g_1^2g_6+5.8g_1^2-0.079g_1g_2^3+0.46g_1g_2^2g_3+1.6g_1g_2^2g_4+3.3g_1g_2^2g_5+0.69g_1g_2^2g_6+6.6g_1g_2^2+2.2g_1g_2g_3^2-2.2g_1g_2g_3g_4-5.6g_1g_2g_3g_5+3.1g_1g_2g_3g_6+11.0g_1g_2g_3-2.1g_1g_2g_4^2-8.4g_1g_2g_4g_5-2.9g_1g_2g_4g_6-48.0g_1g_2g_4+2.3g_1g_2g_5^2+6.3g_1g_2g_5g_6+1.2g_1g_2g_5+2.2g_1g_2g_6^2+43.0g_1g_2g_6+23.0g_1g_2-0.25g_1g_3^3+7.1g_1g_3^2g_4+0.21g_1g_3^2g_5-6.8g_1g_3^2g_6-22.0g_1g_3^2+2.4g_1g_3g_4^2-6.5g_1g_3g_4g_5-7.8g_1g_3g_4g_6-11.0g_1g_3g_4+0.99g_1g_3g_5^2+10.0g_1g_3g_5g_6+49.0g_1g_3g_5+7.2g_1g_3g_6^2+14.0g_1g_3g_6-24.0g_1g_3+1.2g_1g_4^3+4.0g_1g_4^2g_5-0.41g_1g_4^2g_6+34.0g_1g_4^2+2.4g_1g_4g_5^2-1.3g_1g_4g_5g_6+14.0g_1g_4g_5+1.0g_1g_4g_6^2-44.0g_1g_4g_6+40.0g_1g_4-0.67g_1g_5^3-5.7g_1g_5^2g_6-28.0g_1g_5^2-4.9g_1g_5g_6^2-32.0g_1g_5g_6-29.0g_1g_5-1.4g_1g_6^3+8.5g_1g_6^2-45.0g_1g_6-57.0g_1-0.017g_2^4-0.85g_2^3g_3+0.035g_2^3g_4+1.4g_2^3g_5+0.0085g_2^3g_6+0.21g_2^3+0.55g_2^2g_3^2+0.49g_2^2g_3g_4+0.47g_2^2g_3g_5+0.23g_2^2g_3g_6+9.8g_2^2g_3-0.02g_2^2g_4^2-3.0g_2^2g_4g_5-0.0063g_2^2g_4g_6-0.069g_2^2g_4-3.8g_2^2g_5^2-0.3g_2^2g_5g_6-20.0g_2^2g_5+0.0089g_2^2g_6^2-0.54g_2^2g_6-1.6g_2^2-1.6g_2g_3^3+0.0046g_2g_3^2g_4+6.8g_2g_3^2g_5-0.71g_2g_3^2g_6-8.6g_2g_3^2-0.94g_2g_3g_4^2+1.7g_2g_3g_4g_5+4.9g_2g_3g_4g_6+7.8g_2g_3g_4-11.0g_2g_3g_5^2-6.2g_2g_3g_5g_6-17.0g_2g_3g_5-6.2g_2g_3g_6^2-14.0g_2g_3g_6-62.0g_2g_3-0.011g_2g_4^3+4.2g_2g_4^2g_5+0.043g_2g_4^2g_6-0.091g_2g_4^2+4.5g_2g_4g_5^2-5.6g_2g_4g_5g_6+31.0g_2g_4g_5-0.085g_2g_4g_6^2+0.19g_2g_4g_6-0.57g_2g_4+6.3g_2g_5^3+3.8g_2g_5^2g_6+31.0g_2g_5^2+6.7g_2g_5g_6^2-14.0g_2g_5g_6+78.0g_2g_5+0.025g_2g_6^3+0.29g_2g_6^2+3.1g_2g_6+1.6g_2-0.15g_3^4-0.6g_3^3g_4+0.71g_3^3g_5+1.6g_3^3g_6+9.3g_3^3-0.79g_3^2g_4^2-1.3g_3^2g_4g_5+3.1g_3^2g_4g_6+6.9g_3^2g_4-1.4g_3^2g_5^2-5.2g_3^2g_5g_6-38.0g_3^2g_5-3.7g_3^2g_6^2-9.9g_3^2g_6+7.4g_3^2+0.51g_3g_4^3-1.1g_3g_4^2g_5-2.1g_3g_4^2g_6-7.4g_3g_4^2+5.0g_3g_4g_5^2+1.2g_3g_4g_5g_6-1.1g_3g_4g_5+2.9g_3g_4g_6^2+10.0g_3g_4g_6+25.0g_3g_4+1.1g_3g_5^3+6.2g_3g_5^2g_6+53.0g_3g_5^2+5.1g_3g_5g_6^2+35.0g_3g_5g_6+58.0g_3g_5+1.3g_3g_6^3+6.9g_3g_6^2-11.0g_3g_6+65.0g_3+0.019g_4^4-1.9g_4^3g_5-0.099g_4^3g_6-0.12g_4^3-1.3g_4^2g_5^2+3.5g_4^2g_5g_6-17.0g_4^2g_5+0.27g_4^2g_6^2+0.78g_4^2g_6+1.2g_4^2-4.0g_4g_5^3-2.1g_4g_5^2g_6-19.0g_4g_5^2-4.3g_4g_5g_6^2+12.0g_4g_5g_6-1.1\cdot10^2g_4g_5-0.34g_4g_6^3-1.3g_4g_6^2+1.8g_4g_6+10.0g_4-0.22g_5^4-2.4g_5^3g_6-26.0g_5^3-0.74g_5^2g_6^2-7.0g_5^2g_6-32.0g_5^2-1.5g_5g_6^3-11.0g_5g_6^2+96.0g_5g_6-25.0g_5+0.21g_6^4+0.93g_6^3-5.7g_6^2-29.0g_6
    \end{aligned}
$$

!!! danger "Exact fit"

    Floats are satanic, we want an exact symbolic solution.
    
    Ongoing. `linalg.nullspace` & `radicalfield.QuadraticElement235` is to slow.

There one non-monic quadratic, one monic cubic and one monic quartic, all unique:

- quadratic $d_2(\vec{g})T^2+d_1(\vec{g})T+d_0(\vec{g})=0$

    Works only almost everywhere. No clear selection rule for physical $T$ roots (gives always two real numbers).

- cubic $T^3+t_2(\vec{g})T^2+t_1(\vec{g})T+t_0(\vec{g})=0$

    Works everywhere. No clear selection rule for physical $T$ roots (gives three real numbers ~50% of the time).

- quartic $T^4+q_3(\vec{g})T^3+q_2(\vec{g})T^2+q_1(\vec{g})T+q_0(\vec{g})=0$

    Works everywhere. No clear selection rule for physical $T$ roots.

Two possible selection rules:

- Calculate root sets of cubic and quartic. Intersection are the physical $T$s.
- Calculate root set of cubic, substitue into quartic, test if $0$.
- Use quartic first. When it doesn't collapse it is the cheapes.

!!! danger "TODO"

    Analyse the special/problematic subsets for $\rho$:
    
    - Boundaries to degree 2 case.
    - Where $T$ splitting occurs.
    - Where the quadratic collapses.
    
    Then sample these and add to the training and test data deliberately.

!!! danger "TODO sampling"

    Explain uniformity by Haar. Consider exponential diminishing of coefficients.
    $T$ distribution for these ensemble distributions with min & max.

[Notebook](rho3_implicit_fit.ipynb)
