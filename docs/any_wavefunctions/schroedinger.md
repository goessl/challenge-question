# Schrödinger

We haven't yet included the restrictions that the ensemble fulfills the Schrödinger equation or [Hohenberg & Kohn's](../further_readings.md) restriction of a non-degenerate ground state. We will now enforce the former on the solution set.

We know from the [challenge statement](../challenge.md) that the wavefunctions must fulfill the Schrödinger equation for an unknown potential $V$:

$$
    E_k\phi_k = -\frac{1}{2}\phi_k''+V\phi_k \ .
$$

Plugging in the discovered forms and equating for the unknown potential:

$$
    \begin{aligned}
        E_1\sqrt{n}\cos\alpha &= -\frac{1}{2}\left(\sqrt{n}\cos\alpha\right)''+V\sqrt{n}\cos\alpha &&\Rightarrow & 2V &= 2E_1+\frac{\left(\sqrt{n}\cos\alpha\right)''}{\sqrt{n}\cos\alpha} \\
        E_2\sqrt{n}\sin\alpha &= -\frac{1}{2}\left(\sqrt{n}\sin\alpha\right)''+V\sqrt{n}\sin\alpha &&\Rightarrow & 2V &= 2E_2+\frac{\left(\sqrt{n}\sin\alpha\right)''}{\sqrt{n}\sin\alpha} \\
        2E_1+\frac{\left(\sqrt{n}\cos\alpha\right)''}{\sqrt{n}\cos\alpha} &= 2E_2+\frac{\left(\sqrt{n}\sin\alpha\right)''}{\sqrt{n}\sin\alpha} \\
        2(E_2-E_1) &= \frac{\left(\sqrt{n}\cos\alpha\right)''}{\sqrt{n}\cos\alpha}-\frac{\left(\sqrt{n}\sin\alpha\right)''}{\sqrt{n}\sin\alpha}
    \end{aligned}
$$

Untangling the derivatives:

$$
    \begin{aligned}
        &\left(\sqrt{n}\cos\alpha\right)'' \\
        &= \left(\frac{n'\cos\alpha}{2\sqrt{n}}-\sqrt{n}\alpha'\sin\alpha\right)' \\
        &= \frac{n''\cos\alpha}{2\sqrt{n}}-\frac{n'\alpha'\sin\alpha}{2\sqrt{n}}-\frac{n'^2\cos\alpha}{4\sqrt{n^3}}-\frac{n'\alpha'\sin\alpha}{2\sqrt{n}}-\sqrt{n}\alpha''\sin\alpha-\sqrt{n}\alpha'^2\cos\alpha \\
        &= \frac{n''\cos\alpha}{2\sqrt{n}}-\frac{n'\alpha'\sin\alpha}{\sqrt{n}}-\frac{n'^2\cos\alpha}{4\sqrt{n^3}}-\sqrt{n}\alpha''\sin\alpha-\sqrt{n}\alpha'^2\cos\alpha \\
        &\left(\sqrt{n}\sin\alpha\right)'' \\
        &= \left(\frac{n'\sin\alpha}{2\sqrt{n}}+\sqrt{n}\alpha'\cos\alpha\right)' \\
        &= \frac{n''\sin\alpha}{2\sqrt{n}}+\frac{n'\alpha'\cos\alpha}{2\sqrt{n}}-\frac{n'^2\sin\alpha}{4\sqrt{n^3}}+\frac{n'\alpha'\cos\alpha}{2\sqrt{n}}+\sqrt{n}\alpha''\cos\alpha-\sqrt{n}\alpha'^2\sin\alpha \\
        &= \frac{n''\sin\alpha}{2\sqrt{n}}+\frac{n'\alpha'\cos\alpha}{\sqrt{n}}-\frac{n'^2\sin\alpha}{4\sqrt{n^3}}+\sqrt{n}\alpha''\cos\alpha-\sqrt{n}\alpha'^2\sin\alpha
    \end{aligned}
$$

Giving:

$$
    \begin{aligned}
        2(E_2-E_1) &= \frac{\frac{n''\cos\alpha}{2\sqrt{n}}-\frac{n'\alpha'\sin\alpha}{\sqrt{n}}-\frac{n'^2\cos\alpha}{4\sqrt{n^3}}-\sqrt{n}\alpha''\sin\alpha-\sqrt{n}\alpha'^2\cos\alpha}{\sqrt{n}\cos\alpha} \\
        &\qquad -\frac{\frac{n''\sin\alpha}{2\sqrt{n}}+\frac{n'\alpha'\cos\alpha}{\sqrt{n}}-\frac{n'^2\sin\alpha}{4\sqrt{n^3}}+\sqrt{n}\alpha''\cos\alpha-\sqrt{n}\alpha'^2\sin\alpha}{\sqrt{n}\sin\alpha} \\
        &= \frac{n''}{2n}-\frac{n'\alpha'\tan\alpha}{n}-\frac{n'^2}{4n^2}-\alpha''\tan\alpha-\alpha'^2 \\
        &\qquad -\frac{n''}{2n}-\frac{n'\alpha'\cot\alpha}{n}+\frac{n'^2}{4n^2}-\alpha''\cot\alpha+\alpha'^2 \\
        &= -\frac{n'\alpha'}{n}\left(\tan\alpha+\cot\alpha\right)-\alpha''\left(\tan\alpha+\cot\alpha\right) \\
        &= -\left(\frac{n'\alpha'}{n}+\alpha''\right)\left(\tan\alpha+\cot\alpha\right) \\
        &= -\left(\frac{n'\alpha'}{n}+\alpha''\right)\frac{2}{\sin2\alpha} \\
        0 &= n'\alpha'+n\alpha''+(E_2-E_1)n\sin2\alpha \\
        0 &= (n\alpha')'+(E_2-E_1)n\sin2\alpha
    \end{aligned}
$$

!!! danger "Physicists math"

    Real physicists don't require non-zero denominators.

!!! question "What now?"

    This should be an addition requirement to $\int_\mathbb{R}n(x)e^{i2\alpha(x)}\,\mathrm{d}x$. Or is it actually the same in disguise? To be investigated further.
