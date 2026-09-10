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

[Notebook](rho3.ipynb)

## Addendum 25.07.2026

There is an implicit polynomial solution:

$$
    \begin{aligned}
        0 &= \left(\frac{36g_1}{275}-\frac{48\sqrt{30}g_5}{1375}\right)T^2 \\
        &\qquad +\left(\frac{24\sqrt{2}g_1g_2}{275}+\frac{4\sqrt{6}g_1g_4}{275}-\frac{24\sqrt{5}g_1g_6}{275}-\frac{216g_1}{275}-\frac{38\sqrt{3}g_2g_3}{275}+\frac{108\sqrt{15}g_2g_5}{1375}+\frac{12g_3g_4}{275}+\frac{34\sqrt{30}g_3g_6}{1375}+\frac{56\sqrt{6}g_3}{275}-\frac{24\sqrt{5}g_4g_5}{275}+\frac{4\sqrt{6}g_5g_6}{125}+\frac{64\sqrt{30}g_5}{1375}\right)T \\
        &\qquad -\frac{2g_1^{3}}{275}+\frac{17\sqrt{6}g_1^2g_3}{1650}-\frac{14\sqrt{30}g_1^2g_5}{4125}-\frac{41g_1g_2^2}{550}+\frac{98\sqrt{3}g_1g_2g_4}{825}-\frac{14\sqrt{10}g_1g_2g_6}{275}-\frac{51\sqrt{2}g_1g_2}{275}-\frac{7g_1g_3^2}{275}+\frac{2\sqrt{5}g_1g_3g_5}{125}-\frac{32g_1g_4^2}{275}+\frac{8\sqrt{30}g_1g_4g_6}{375}-\frac{2\sqrt{6}g_1g_4}{75}-\frac{16g_1g_5^2}{1375}+\frac{16g_1g_6^2}{1375}+\frac{276\sqrt{5}g_1g_6}{1375}+g_1-\frac{\sqrt{6}g_2^2g_3}{66}+\frac{71\sqrt{30}g_2^2g_5}{4125}-\frac{3\sqrt{2}g_2g_3g_4}{275}+\frac{9\sqrt{15}g_2g_3g_6}{275}+\frac{93\sqrt{3}g_2g_3}{275}-\frac{2\sqrt{10}g_2g_4g_5}{55}-\frac{166\sqrt{3}g_2g_5g_6}{4125}-\frac{734\sqrt{15}g_2g_5}{4125}+\frac{\sqrt{6}g_3^{3}}{330}-\frac{4\sqrt{30}g_3^2g_5}{1375}+\frac{4\sqrt{6}g_3g_4^2}{275}-\frac{52\sqrt{5}g_3g_4g_6}{1375}-\frac{2g_3g_4}{11}+\frac{6\sqrt{6}g_3g_5^2}{1375}-\frac{4\sqrt{6}g_3g_6^2}{825}-\frac{257\sqrt{30}g_3g_6}{4125}-\frac{28\sqrt{6}g_3}{75}+\frac{8\sqrt{30}g_4^2g_5}{1375}+\frac{72g_4g_5g_6}{1375}+\frac{276\sqrt{5}g_4g_5}{1375}-\frac{8\sqrt{30}g_5^{3}}{20625}-\frac{16\sqrt{30}g_5g_6^2}{6875}-\frac{34\sqrt{6}g_5g_6}{1375}+\frac{4\sqrt{30}g_5}{125}
    \end{aligned}
$$

!!! danger "Works everytime"

    Proof that it never collapses -> always has at least one solution <=> "Solution everywhere without special cases".

!!! danger "Spurious solutions"

    Check if, when there are multiple solutions, that all are physical.

!!! danger "Complexity"

    Like a characteristic polynomial. Polynomial constructions seems easy (polynomial); root finding must not be more complex that Schrödinger, otherwise useless.

## Addendum 04.08.2026

The implicit polynomial of degree 2 $c_2(\vec{g})T^2+c_1(\vec{g})T+c_0(\vec{g})=0$ collapses for some configurations (in general 0% chance).

But fitting for degree 4 worked. There is a degree 4 polynomial $\sum_{k=0}^4c_k(\vec{g})T^k=0$ which never collapses.

## Addendum 10.09.2026

$$
    \begin{aligned}
        0 &= 1.0T^4 \\
        &\qquad +\left(-27.0g_1+1.1g_2-13.0g_3-2.6g_4+61.0g_5+2.7g_6-6.1\right)T^3 \\
        &\qquad +\left(-0.14g_1^2-34.0g_1g_2+0.56g_1g_3+12.0g_1g_4-6.4g_1g_5+18.0g_1g_6+1.7\cdot10^2g_1-0.055g_2^2+38.0g_2g_3-0.48g_2g_4-34.0g_2g_5+0.2g_2g_6-4.3g_2-5.0g_3^2+1.1g_3g_4+15.0g_3g_5-14.0g_3g_6-61.0g_3+0.25g_4^2-3.3g_4g_5+0.96g_4g_6+13.0g_4-1.4g_5^2-7.7g_5g_6-1.3\cdot10^2g_5-0.79g_6^2-18.0g_6+13.0\right)T^2 \\
        &\qquad +\left(-1.9g_1^3+0.72g_1^2g_2+3.3g_1^2g_3-2.0g_1^2g_4+2.3g_1^2g_5+4.0g_1^2g_6-1.7g_1^2+4.6g_1g_2^2-5.4g_1g_2g_3-2.9g_1g_2g_4-1.0g_1g_2g_5+3.7g_1g_2g_6+65.0g_1g_2+0.86g_1g_3^2+7.1g_1g_3g_4-14.0g_1g_3g_5-10.0g_1g_3g_6+9.0g_1g_3-1.7g_1g_4^2-7.6g_1g_4g_5+8.8g_1g_4g_6-51.0g_1g_4+12.0g_1g_5^2+17.0g_1g_5g_6+30.0g_1g_5-8.6g_1g_6^2-28.0g_1g_6-1.8\cdot10^2g_1-0.059g_2^3+5.1g_2^2g_3-0.086g_2^2g_4-6.3g_2^2g_5+0.21g_2^2g_6+0.92g_2^2+2.8g_2g_3^2-4.3g_2g_3g_4+9.1g_2g_3g_5-12.0g_2g_3g_6-70.0g_2g_3+0.17g_2g_4^2+1.5g_2g_4g_5-0.089g_2g_4g_6+1.2g_2g_4-15.0g_2g_5^2+18.0g_2g_5g_6+44.0g_2g_5-0.057g_2g_6^2-1.9g_2g_6+3.2g_2-2.8g_3^3-3.0g_3^2g_4+17.0g_3^2g_5+7.1g_3^2g_6+7.3g_3^2-1.4g_3g_4^2+1.1g_3g_4g_5+2.1g_3g_4g_6+9.0g_3g_4-25.0g_3g_5^2-19.0g_3g_5g_6-61.0g_3g_5-0.1g_3g_6^2+54.0g_3g_6+1.1\cdot10^2g_3+0.011g_4^3+4.6g_4^2g_5-0.35g_4^2g_6-1.1g_4^2+8.9g_4g_5^2-11.0g_4g_5g_6+49.0g_4g_5+0.63g_4g_6^2-2.8g_4g_6-20.0g_4+13.0g_5^3+2.2g_5^2g_6+21.0g_5^2+8.9g_5g_6^2-60.0g_5g_6+46.0g_5-0.63g_6^3+4.5g_6^2+40.0g_6-8.8\right)T \\
        &\qquad -0.019g_1^4-1.3g_1^3g_2-0.5g_1^3g_3+6.0g_1^3g_4+0.84g_1^3g_5-4.5g_1^3g_6-7.4g_1^3-0.27g_1^2g_2^2+0.35g_1^2g_2g_3+1.1g_1^2g_2g_4+1.6g_1^2g_2g_5-1.7g_1^2g_2g_6-0.46g_1^2g_2+0.92g_1^2g_3^2-12.0g_1^2g_3g_4-1.8g_1^2g_3g_5+9.7g_1^2g_3g_6+21.0g_1^2g_3-1.2g_1^2g_4^2+5.3g_1^2g_4g_5+4.1g_1^2g_4g_6+1.8g_1^2g_4+0.27g_1^2g_5^2-5.4g_1^2g_5g_6-19.0g_1^2g_5-3.4g_1^2g_6^2-5.4g_1^2g_6+5.8g_1^2-0.079g_1g_2^3+0.46g_1g_2^2g_3+1.6g_1g_2^2g_4+3.3g_1g_2^2g_5+0.69g_1g_2^2g_6+6.6g_1g_2^2+2.2g_1g_2g_3^2-2.2g_1g_2g_3g_4-5.6g_1g_2g_3g_5+3.1g_1g_2g_3g_6+11.0g_1g_2g_3-2.1g_1g_2g_4^2-8.4g_1g_2g_4g_5-2.9g_1g_2g_4g_6-48.0g_1g_2g_4+2.3g_1g_2g_5^2+6.3g_1g_2g_5g_6+1.2g_1g_2g_5+2.2g_1g_2g_6^2+43.0g_1g_2g_6+23.0g_1g_2-0.25g_1g_3^3+7.1g_1g_3^2g_4+0.21g_1g_3^2g_5-6.8g_1g_3^2g_6-22.0g_1g_3^2+2.4g_1g_3g_4^2-6.5g_1g_3g_4g_5-7.8g_1g_3g_4g_6-11.0g_1g_3g_4+0.99g_1g_3g_5^2+10.0g_1g_3g_5g_6+49.0g_1g_3g_5+7.2g_1g_3g_6^2+14.0g_1g_3g_6-24.0g_1g_3+1.2g_1g_4^3+4.0g_1g_4^2g_5-0.41g_1g_4^2g_6+34.0g_1g_4^2+2.4g_1g_4g_5^2-1.3g_1g_4g_5g_6+14.0g_1g_4g_5+1.0g_1g_4g_6^2-44.0g_1g_4g_6+40.0g_1g_4-0.67g_1g_5^3-5.7g_1g_5^2g_6-28.0g_1g_5^2-4.9g_1g_5g_6^2-32.0g_1g_5g_6-29.0g_1g_5-1.4g_1g_6^3+8.5g_1g_6^2-45.0g_1g_6-57.0g_1-0.017g_2^4-0.85g_2^3g_3+0.035g_2^3g_4+1.4g_2^3g_5+0.0085g_2^3g_6+0.21g_2^3+0.55g_2^2g_3^2+0.49g_2^2g_3g_4+0.47g_2^2g_3g_5+0.23g_2^2g_3g_6+9.8g_2^2g_3-0.02g_2^2g_4^2-3.0g_2^2g_4g_5-0.0063g_2^2g_4g_6-0.069g_2^2g_4-3.8g_2^2g_5^2-0.3g_2^2g_5g_6-20.0g_2^2g_5+0.0089g_2^2g_6^2-0.54g_2^2g_6-1.6g_2^2-1.6g_2g_3^3+0.0046g_2g_3^2g_4+6.8g_2g_3^2g_5-0.71g_2g_3^2g_6-8.6g_2g_3^2-0.94g_2g_3g_4^2+1.7g_2g_3g_4g_5+4.9g_2g_3g_4g_6+7.8g_2g_3g_4-11.0g_2g_3g_5^2-6.2g_2g_3g_5g_6-17.0g_2g_3g_5-6.2g_2g_3g_6^2-14.0g_2g_3g_6-62.0g_2g_3-0.011g_2g_4^3+4.2g_2g_4^2g_5+0.043g_2g_4^2g_6-0.091g_2g_4^2+4.5g_2g_4g_5^2-5.6g_2g_4g_5g_6+31.0g_2g_4g_5-0.085g_2g_4g_6^2+0.19g_2g_4g_6-0.57g_2g_4+6.3g_2g_5^3+3.8g_2g_5^2g_6+31.0g_2g_5^2+6.7g_2g_5g_6^2-14.0g_2g_5g_6+78.0g_2g_5+0.025g_2g_6^3+0.29g_2g_6^2+3.1g_2g_6+1.6g_2-0.15g_3^4-0.6g_3^3g_4+0.71g_3^3g_5+1.6g_3^3g_6+9.3g_3^3-0.79g_3^2g_4^2-1.3g_3^2g_4g_5+3.1g_3^2g_4g_6+6.9g_3^2g_4-1.4g_3^2g_5^2-5.2g_3^2g_5g_6-38.0g_3^2g_5-3.7g_3^2g_6^2-9.9g_3^2g_6+7.4g_3^2+0.51g_3g_4^3-1.1g_3g_4^2g_5-2.1g_3g_4^2g_6-7.4g_3g_4^2+5.0g_3g_4g_5^2+1.2g_3g_4g_5g_6-1.1g_3g_4g_5+2.9g_3g_4g_6^2+10.0g_3g_4g_6+25.0g_3g_4+1.1g_3g_5^3+6.2g_3g_5^2g_6+53.0g_3g_5^2+5.1g_3g_5g_6^2+35.0g_3g_5g_6+58.0g_3g_5+1.3g_3g_6^3+6.9g_3g_6^2-11.0g_3g_6+65.0g_3+0.019g_4^4-1.9g_4^3g_5-0.099g_4^3g_6-0.12g_4^3-1.3g_4^2g_5^2+3.5g_4^2g_5g_6-17.0g_4^2g_5+0.27g_4^2g_6^2+0.78g_4^2g_6+1.2g_4^2-4.0g_4g_5^3-2.1g_4g_5^2g_6-19.0g_4g_5^2-4.3g_4g_5g_6^2+12.0g_4g_5g_6-1.1\cdot10^2g_4g_5-0.34g_4g_6^3-1.3g_4g_6^2+1.8g_4g_6+10.0g_4-0.22g_5^4-2.4g_5^3g_6-26.0g_5^3-0.74g_5^2g_6^2-7.0g_5^2g_6-32.0g_5^2-1.5g_5g_6^3-11.0g_5g_6^2+96.0g_5g_6-25.0g_5+0.21g_6^4+0.93g_6^3-5.7g_6^2-29.0g_6
    \end{aligned}
$$

[Notebook](rho3_implicit_fit.ipynb)

Call-outs "Spurious solutions" & "Complexity" are still open.

!!! danger "Non-uniqueness"

    There are actually probably 27 independend such polynomials. Therefore it should be possible to remove some monomials in the design/feature matrix. Maybe lower degree in $T$ actually possible and just the $g$s needed a higher degree?

!!! danger "Exact fit"

    Floats are satanic, we want an exact symbolic solution.
    
    Ongoing:
    
    - [goessl/radicalfield](https://goessl.github.io/radicalfield/)
    - [goessl/linalg](https://goessl.github.io/linalg/)

