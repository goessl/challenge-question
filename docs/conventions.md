# Conventions

- Enumerate particles with $k\in\left\{1, 2, \dots, N\right\}$.

    $\left\{\phi_k\right\}_{k=1}^N=\left\{\phi_1, \phi_2, \dots, \phi_N\right\}$
    
    - They are countable objects: start at one.
    - $N$ is the particle count.
    - Running index $k$.
    - $n$ is already used for the probability density distribution; $j$ will also be taken.

- Enumerate series with $j\in\left\{0, 1, \dots, D\right\}$.

    $\left\{\ket{j}\right\}_{j=0}^D=\left\{\ket{0}, \ket{1}, \dots, \ket{D}\right\}$.
    
    - Most bases in functional analysis start at zero. E.g. polynomials & Hermite functions.
    - Harmonic oscillator eigenstates often enumerated with $j$.
    
    This also leaves $i$ as the imaginary unit, as it is used in physics, and breaks my engineering heart.

- Enumeration notation with ${}_{j=j_1}^{j_2}$ instead of ${}_{j\in\{j_1, \dots, j_2\}}$

    It is shorter and consistent with $\sum_{j=j_1}^{j_2}$.

- Trace order

    $\braket{\hat{O}} = \text{tr}\,\hat{\rho}\hat{O}$
    
    as in Evertz QM 2023 eq. 9.10.