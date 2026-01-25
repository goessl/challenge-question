## Density norm
$$
	\begin{aligned}
		\int_\mathbb{R}n(x)\,\mathrm{d}x &= \int_\mathbb{R}\sum_{i=1}^N|\phi_i(x)|^2\,\mathrm{d}x \\
		&= \sum_{i=1}^N\int_\mathbb{R}|\phi_i(x)|^2\,\mathrm{d}x &&\mid ||\phi_i||_{L_\mathbb{R}^2}=1 \\
		&= \sum_{i=1}^N1 \\
		&= N
	\end{aligned}
$$
## Partial integration
$$
	\begin{aligned}
		T &= -\frac{1}{2}\int_\mathbb{R}\sum_{i=1}^N\phi_i^*(x)\phi_i''(x)\,\mathrm{d}x \\
		&= -\frac{1}{2}\sum_{i=1}^N\int_\mathbb{R}\phi_i^*(x)\phi_i''(x)\,\mathrm{d}x &&\mid \text{p.I.} \\
		&= -\frac{1}{2}\sum_{i=1}^N\left(\phi_i^*\phi_i'\mid_\mathbb{R}-\int_\mathbb{R}|\phi_i'(x)|^2\,\mathrm{d}x\right) &&\mid \phi_i(\pm\infty)=\phi_i^{(k)}(\pm\infty)=0 \\
		&= +\frac{1}{2}\sum_{i=1}^N\int_\mathbb{R}|\phi_i'(x)|^2\,\mathrm{d}x
	\end{aligned}
$$
## Plane Invariance
### Lemma
The kinetic energy of any pairs of wavefunctions only depends on the plane they lie in, not their orientation within.
### Proof
Let there be a basis $\phi_1, \phi_2$
$$
	\braket{\phi_i|\phi_j} = \delta_{ij}
$$
All other pairs of wavefunctions within this span
$$
	\begin{aligned}
		\ket{\psi_1} &= \cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2} \\
		\ket{\psi_2} &= \sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2} \\
		\braket{\psi_1|\psi_1} &= \left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right)\left(\cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2}\right) \\
		&= \cos^2\varphi\braket{\phi_1|\phi_1}+\cos\varphi\sin\varphi\braket{\phi_1|\phi_2}+\cos\varphi\sin\varphi\braket{\phi_2|\phi_1}+\sin^2\varphi\braket{\phi_2|\phi_2} \\
		&= \cos^2\varphi+\sin^2\varphi = 1 \\
		\braket{\psi_2|\psi_2} &= \left(\sin\varphi\bra{\phi_1}-\cos\varphi\bra{\phi_2}\right)\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right) \\
		&= \sin^2\varphi\braket{\phi_1|\phi_1}-\cos\varphi\sin\varphi\braket{\phi_1|\phi_2}-\cos\varphi\sin\varphi\braket{\phi_2|\phi_1}+\cos^2\varphi\braket{\phi_2|\phi_2} \\
		&= \cos^2\varphi+\sin^2\varphi = 1 \\
		\braket{\psi_1|\psi_2} &= \left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right)\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right) \\
		&= \cos\varphi\sin\varphi\braket{\phi_1|\phi_1}-\cos^2\varphi\braket{\phi_1|\phi_2}+\sin^2\varphi\braket{\phi_1|\phi_2}-\cos\varphi\sin\varphi\braket{\phi_2|\phi_2} \\
		&= \cos\varphi\sin\varphi-\cos\varphi\sin\varphi = 0
	\end{aligned}
$$
have the same kinetic energy
$$
	\begin{aligned}
		\braket{\hat{T}}_{\psi_1}+\braket{\hat{T}}_{\psi_2} &= \braket{\psi_1|\hat{T}|\psi_1}+\braket{\psi_2|\hat{T}|\psi_2} \\
		&= \left(\cos\varphi\bra{\phi_1}+\sin\varphi\bra{\phi_2}\right)\hat{T}\left(\cos\varphi\ket{\phi_1}+\sin\varphi\ket{\phi_2}\right) \\
		&\qquad+ \left(\sin\varphi\bra{\phi_1}-\cos\varphi\bra{\phi_2}\right)\hat{T}\left(\sin\varphi\ket{\phi_1}-\cos\varphi\ket{\phi_2}\right) \\
		&= \cos^2\varphi\braket{\phi_1|\hat{T}|\phi_1}+\cos\varphi\sin\varphi\braket{\phi_1|\hat{T}|\phi_2}+\cos\varphi\sin\varphi\braket{\phi_2|\hat{T}|\phi_1}+\sin^2\varphi\braket{\phi_2|\hat{T}|\phi_2} \\
		&\qquad+ \sin^2\varphi\braket{\phi_1|\hat{T}|\phi_1}-\cos\varphi\sin\varphi\braket{\phi_1|\hat{T}|\phi_2}-\cos\varphi\sin\varphi\braket{\phi_2|\hat{T}|\phi_1}+\cos^2\varphi\braket{\phi_2|\hat{T}|\phi_2} \\
		&= 1\braket{\phi_1|\hat{T}|\phi_1}+0\braket{\phi_1|\hat{T}|\phi_2}+0\braket{\phi_2|\hat{T}|\phi_1}+1\braket{\phi_2|\hat{T}|\phi_2} \\
		&= \braket{\hat{T}}_{\phi_1}+\braket{\hat{T}}_{\phi_2}
	\end{aligned}
$$
