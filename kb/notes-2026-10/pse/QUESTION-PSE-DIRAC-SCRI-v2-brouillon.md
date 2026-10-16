# Question Physics Stack Exchange, brouillon v2 (2026-10-16)

Remplace le brouillon v1 (redige sur l'article v2.1). Aligne sur l'article v2.5 ente (NOTE-215).

## A lire avant publication (operateur)
1. **Regle du site.** Le reseau Stack Exchange interdit sur la plupart de ses sites, dont a notre connaissance Physics, de publier un texte produit par une IA. Je n'ai pas pu ouvrir la page de regles du site depuis ici (acces bloque) : a verifier sur `physics.stackexchange.com/help/gen-ai-policy`. Le texte ci-dessous est donc un **canevas** : equations, enonces et questions a reprendre avec tes propres mots. Ce n'est pas un texte a coller tel quel.
2. **Une question par message.** Le site ferme les messages qui posent plusieurs questions ou qui demandent « verifiez mon calcul ». La question principale proposee est Q1 (litterature et notion de regularite) ; Q2 peut faire un second message plus tard, ou aller sur MathOverflow si elle est reduite a l'enonce sur le systeme fuchsien.
3. **Lien.** Mettre le DOI Zenodo de la v2.5 (depot de demain) a la place de `[DOI]`. Le message doit se lire sans le lien.
4. **Etiquettes** (a choisir dans la liste proposee a la saisie) : general-relativity, cosmology, de-sitter-spacetime, dirac-equation, conformal-field-theory n'est pas la bonne (c'est la CFT) ; preferer conformal-symmetry ou boundary-conditions.
5. Longueur visee : 250 a 400 mots, deux equations affichees au plus.

## Canevas (anglais)

**Title (proposal).** Massive Dirac field at the spacelike future conformal boundary of de Sitter: which notion of regularity, and is there literature?

**Setup.** Expanding de Sitter patch, $g=-dt^2+a^2d\mathbf{x}^2$, $a=e^{Ht}$, conformal factor $\Omega=1/a$, so $\hat g=\Omega^2 g$ is flat and $\mathscr{I}^+$ is $\Omega=0$. Test Dirac field of constant mass $m$, rescaled with the conformal weight, $\hat\psi=\Omega^{-3/2}\psi$:
$$\Big(i\hat\gamma^\mu\partial_\mu-\frac{m}{\Omega}\Big)\hat\psi=0 .$$
For a Fourier mode, in the variable $\Omega$, this is a linear ODE with a **regular singular point** at $\Omega=0$, exponents $\pm i m/H$. Solutions are $\Omega^{im/H}P_+(\Omega)+\Omega^{-im/H}P_-(\Omega)$ with $P_\pm$ entire, so $\hat\psi$ has no limit at $\mathscr I^+$ (constant norm, winding phase).

**What I find (short).**
- With Friedrich's radiation-type weight, $\Omega^{-4}T_{tt}$ has a $1/\Omega$ pole with coefficient $m(|\chi_0^+|^2-|\chi_0^-|^2)$. With the weight he uses for dust, $\Omega^{-3}T_{tt}$, it has a limit: the pole is a property of the variable.
- In the dust weight, the source of the equation for the rescaled Weyl tensor has no pole on solutions. It is a power series in $\Omega$ when only one exponent is present, and bounded without limit when both are present ($\mathbf k\neq0$), through a relative factor $\Omega^{\pm 2im/H}$.
- No smooth redefinition of $\hat\psi$ removes the regular singular point; a $U(1)$ gauge removes a common phase only at the price of a non-integrable pole in $A_\eta$.

**Question (Q1).** For massive spinors near a spacelike $\mathscr I^+$, is there an accepted notion of regularity (Fuchsian, polyhomogeneous, "regular singular" in the sense of the Fuchsian methods used for Big Bang singularities) under which such a field is said to extend, and has the massive spin-1/2 case been treated in Friedrich's conformal field equations? Friedrich (arXiv:1311.0700) treats the massive scalar and finds a smooth extension exactly for $m^2=2\lambda/3$; I have not found a spinor analogue.

**Optional (Q2, separate message).** In the coupled Einstein-Dirac system, does the single-exponent class survive back-reaction, or can the coupling reintroduce poles or logarithms?

**Context (one sentence).** This bears on Penrose's Conformal Cyclic Cosmology, which needs matter to cross $\mathscr I^+$; a working paper with proofs is at [DOI] (not peer-reviewed).

## Differences avec le brouillon v1
- v1 posait trois questions et demandait de verifier le calcul ; v2 pose une question, sur la litterature et la notion de regularite.
- v1 presentait le pole $m/\Omega$ comme le resultat ; v2 le rattache au choix du poids (poids poussiere : pas de pole), conformement a RJ et a la v2.5.
- Le point singulier regulier (Fuchs) et l'interference des deux exposants deviennent le coeur de la question.
- Masse variable et argument quantique retires (dans l'article ; inutiles pour la question).
