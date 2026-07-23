# Some Algebra

$N=2$, $D=3$ is the first actually non trivial case. The occupied orbitals and the vacant ones have both rank 2.

We will try to study this with basic algebra.

## Linear equations

Some parametric solutions that are needed later on.

### In one variable

$$
    kx+d=0 \qquad \Rightarrow \qquad x=-\frac{d}{k}
$$

Obviously.

### In two variables

A [linear equation](https://en.wikipedia.org/wiki/Linear_equation#Two_variables)

$$
    ax+by+c = 0
$$

has a [closest point to the origin](https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line#Line_defined_by_an_equation)

$$
    \begin{pmatrix}
        x_0 \\
        y_0
    \end{pmatrix} = \frac{-c}{a^2+b^2}\begin{pmatrix}
        a \\
        b
    \end{pmatrix}
$$

from which the line goes of perpendicularly

$$
    \begin{pmatrix}
        d_x \\
        d_y
    \end{pmatrix} = \begin{pmatrix}
        y_0 \\
        -x_0
    \end{pmatrix} = \frac{-c}{a^2+b^2}\begin{pmatrix}
        +b \\
        -a
    \end{pmatrix} \propto \begin{pmatrix}
        +b \\
        -a
    \end{pmatrix}
$$

resulting in

$$
    \begin{pmatrix}
        x(t) \\
        y(t)
    \end{pmatrix} = \begin{pmatrix}
        x_0 \\
        y_0
    \end{pmatrix}+\begin{pmatrix}
        d_x \\
        d_y
    \end{pmatrix}t = \frac{-c}{a^2+b^2}\begin{pmatrix}
        a \\
        b
    \end{pmatrix}+\begin{pmatrix}
        +b \\
        -a
    \end{pmatrix}t \qquad t\in\mathbb{R}
$$

or equivalently

$$
    \begin{aligned}
        x &= \frac{-ac}{a^2+b^2}+bt \\
        y &= \frac{-bc}{a^2+b^2}-at
    \end{aligned} \qquad t\in\mathbb{R}
$$
