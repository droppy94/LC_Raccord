# Brouillon de question pour Physics Stack Exchange (a reformuler par l'auteur avant publication)

Titre propose :
**Is the 1/Ω pole in the rescaled energy density of a massive Dirac field at future conformal infinity of de Sitter gauge-invariant and unavoidable?**

Etiquettes suggerees (a choisir parmi celles que le site propose a la saisie) : general-relativity, de-sitter-spacetime, dirac-equation, quantum-field-theory-in-curved-spacetime, conformal-symmetry.

---

## Setup

Take the expanding patch of de Sitter space, $g=-\mathrm{d}t^2+a^2\mathrm{d}\mathbf{x}^2$, $a=e^{Ht}$, conformal time $\eta=-1/(aH)\in(-\infty,0)$, and the conformal factor $\Omega=1/a=-H\eta$, so that $\hat g=\Omega^2 g$ is flat and future conformal infinity $\mathscr{I}^+$ is $\eta=0$. Consider a test Dirac field of constant mass $m$, $(i\gamma^\mu\nabla_\mu-m)\psi=0$ with $\{\gamma^a,\gamma^b\}=-2g^{ab}$, and rescale it with the standard weight, $\hat\psi=\Omega^{-3/2}\psi$. Since the massless Dirac operator is conformally covariant, the rescaled equation is

$$\Big(i\hat{\gamma}^\mu\partial_\mu-\frac{m}{\Omega}\Big)\hat\psi=0 .$$

For a Fourier mode $\hat\psi=e^{i\mathbf{k}\cdot\mathbf{x}}u(\eta)$ this is $i\,\partial_\eta u=(\boldsymbol\alpha\cdot\mathbf{k}+\beta\,m a)\,u$, with a Hermitian generator, so $u^\dagger u$ is conserved.

## What I find

1. **Phase.** Writing $u=\exp\!\big(i\beta\tfrac{m}{H}\ln\Omega\big)\chi$, the equation for $\chi$ has a bounded generator of norm $k=|\mathbf{k}|$, so $\chi\to\chi_0\neq0$ with $\|\chi-\chi_0\|\le k|\eta|\,\|\chi_0\|$. Hence $u$ itself has no limit at $\eta=0$ for $m\neq0$: its $\beta=\pm1$ components wind as $e^{\pm i(m/H)\ln\Omega}=e^{\mp imt}$.

2. **Gauge.** With minimal coupling to electromagnetism, for a solution whose limit $\chi_0$ lies in the $\beta=+1$ eigenspace (a particle at rest at late times), the gauge transformation $\lambda=(m/H)\ln\Omega=-mt$ removes the winding. In the physical frame this is harmless ($\psi\to e^{imt}\psi$, $A_t\to A_t+m/e$), but in the conformal frame $A_\eta=aA_t$ acquires a non-integrable $1/\eta$ pole. So, as far as I can see, there is no gauge in which both $\hat\psi$ and $A$ extend continuously to $\mathscr{I}^+$, and for solutions with both $\beta$ components non-zero no gauge gives a limit at all.

3. **Energy density.** With $\hat T_{ab}=\Omega^{-2}T_{ab}$ (Friedrich's weight), so that $\hat\rho:=\hat T_{\eta\eta}=\Omega^{-4}T_{tt}$, I get for a mode

$$\hat\rho=u^\dagger(\boldsymbol\alpha\cdot\mathbf{k})\,u+\frac{m}{\Omega}\,u^\dagger\beta u ,$$

so $\Omega\hat\rho\to m\big(\|\chi_0^+\|^2-\|\chi_0^-\|^2\big)$. This is just dust: $\rho\propto m\,a^{-3}$, hence $\Omega^{-4}\rho\propto m/\Omega$. For a one-particle excitation of the Bunch–Davies state, the difference $\langle T\rangle_f-\langle T\rangle_{\rm BD}$ is free of renormalisation ambiguity, and I find $\Omega\,\Delta\hat\rho\to m\tanh(\pi m/H)\,\|f\|^2$.

4. **Variable mass.** If $m$ depends on time, the winding stops if and only if $\int^\infty m\,\mathrm{d}t<\infty$, and the pole in $\hat\rho$ is absent if and only if $m\,a$ stays bounded, i.e. the physical mass decays at least as fast as $1/a$.

On exact de Sitter space, any local coupling to curvature of at most first order in derivatives of $\psi$, derived from a real $U(1)$-invariant action, only produces a constant effective mass. It removes the pole only by tuning that mass to zero (e.g. $(m-\ell R)\bar\psi\psi$ with $\ell=m/12H^2$).

## Questions

1. Is the computation in item 3 correct, and is $\hat T_{ab}=\Omega^{-2}T_{ab}$ the right weight to ask about regularity of the matter source at $\mathscr{I}^+$ (as in Friedrich's conformal field equations)? Or is there an accepted notion of regularity at $\mathscr{I}^+$ under which a constant-mass Dirac field extends?
2. Is the gauge statement in item 2 standard, or is there a reason to regard the singular gauge as admissible, so that only the energy density matters?
3. Friedrich (arXiv:1311.0700) treats the massive scalar coupled to gravity and finds a smooth extension exactly for $m^2=2\lambda/3$. Is there a published treatment of the spin-1/2 case, or of the $1/\Omega$ pole above, that I should read?

**Context, briefly.** This bears on Penrose's Conformal Cyclic Cosmology, which needs matter to cross $\mathscr{I}^+$ regularly and postulates that rest mass fades there. A longer write-up with proofs and a numerical check is at [LIEN VERS L'ARTICLE v2.1, A DEPOSER] (working paper; not peer-reviewed). The question above is meant to stand on its own.
