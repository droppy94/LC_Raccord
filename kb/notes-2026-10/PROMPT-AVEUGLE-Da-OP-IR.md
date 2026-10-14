# Prompt D-a : re-derivation independante (cecite stricte)

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur sur ce sujet : ne lis AUCUN fichier existant sur le disque (en dehors de ceux que tu crees toi-meme dans ton repertoire de travail /home/claude/audit_da/), et ne cherche pas de notes, de scripts ou de resultats anterieurs. Tu peux consulter les deux articles cites ci-dessous (arXiv) si tu le juges utile, et tu dois alors le dire. Travaille avec sympy (python3). Reponds en francais, sans tirets longs. Donne pour chaque resultat l'etiquette [calcule] (sortie de ton script), [derive] (raisonnement) ou [extrait] (citation de source).

## Cadre
- Fond de Sitter fixe, H = 1. Coordonnee s = −τ > 0 (τ temps conforme), facteur conforme Ω = s, metrique physique ĝ = Ω⁻² η, η = diag(−1,1,1,1) en coordonnees (s, x, y, z). 𝓘⁺ est en s → 0.
- Action effective simplifiee de Benevides, Dabholkar, Kobayashi (arXiv:1808.08237, « S2 », eq. 3.12-3.15) : S = −¼ ∫ d⁴x I(τ)² F_μν F^μν (indices eleves par η), I² = e⁻² [1 + 2β (λ − ln s)], avec λ = ln(M/k) constante (choix a⋆ = k/M de S2), β > 0 petit.
- Mode : A_y = u(s) cos(kx), k > 0 fini, autres composantes nulles. Equation de mode : (I² u_s)_s + k² I² u = 0.
- Tout au **premier ordre en β**, developpement polyhomogene (puissances de s et de ln s) quand s → 0 (mode hors horizon, ks → 0).
- Secteur Maxwell : X^M_μν = I² (F_μα F_νβ ĝ^{αβ} − ¼ ĝ_μν F_αβ F_γδ ĝ^{αγ} ĝ^{βδ}), moyenne sur x sur une periode 2π/k.
- Trace anomale moyenne : T̂ = −(β/(2e²)) ⟨F_μν F^μν⟩_η Ω⁴ (indices par η).
- Fermeture isotrope (« C-iso ») : on complete X^M par X^R = diag(r0(s), r1(s), r1(s), r1(s)) (composantes covariantes en (s,x,y,z)) tel que (i) la trace totale ĝ^{μν}(X^M + X^R)_{μν} = T̂ ; (ii) la divergence covariante ∇̂^μ (X^M + X^R)_{μν} = 0 (ĝ, Christoffel de ĝ). Une constante d'integration libre peut rester.
- Tenseur de type Schouten : L̂_μν = (κ/2) (T_μν − ⅓ ĝ_μν ĝ^{αβ}T_αβ), T = X^M + X^R.
- Second membre « (2.17) » : R_ρνλ = Ω⁻¹ (∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ).

## Questions
1. Resous l'equation de mode au premier ordre en β pour deux branches : (a) « magnetique gelee », ordre zero u₀ cos(ks) ; (b) « electrique », ordre zero (c/k) sin(ks). Donne la correction d'ordre β (a l'ordre s⁴ au moins) en precisant tes choix de solution homogene. Y a-t-il des ln s dans u ?
2. Pour chaque branche, calcule ⟨X^M⟩ (diagonale) a l'ordre dominant en s, et le coefficient de β ln s rapporte a l'ordre zero, composante par composante.
3. Branche magnetique : construis X^R (C-iso), verifie conservation et trace, puis calcule toutes les composantes non nulles de R_ρνλ au premier ordre en β quand s → 0. Donne les termes en ln s et les constantes. Compare au cas d'un champ magnetique strictement uniforme F_xy = B₀ (meme procedure) avec la substitution B₀² → ⟨B²⟩ : coincidence ou non, terme par terme ?
4. Sur le mode libre (β = 0, branche magnetique), evalue : (i) l'operateur plat −∂²_η = ∂_s² − ∂_x² sur A_y ; (ii) la codifferentielle covariante δF (pour ĝ) et en deduire le laplacien de Hodge dδ + δd sur F ; (iii) le d'Alembertien de Bochner ĝ^{ab}∇̂_a∇̂_b agissant sur la 2-forme F, rapporte a F, pour les composantes F_xy et F_sy ; et pour un champ uniforme F_xy = B₀.
5. Dans S2, l'equation de mode complete (3.9) contient un terme residuel non local de la forme −β ∫dτ̃ {u'' + k²u}(τ̃) K(τ − τ̃) avec un noyau logarithmique K. A quel ordre en β ce terme contribue-t-il a l'equation de mode quand u est la solution corrigee au premier ordre ? Argumente, en distinguant si besoin les deux branches.
6. Domaine de validite : la reference Bautista, Benevides, Dabholkar (arXiv:1711.00135) calcule l'action plate sous la condition F² ≪ ∇²F (champ rapidement variable). Traduis cette condition pour le mode (dans la normalisation ci-dessus) et dis si elle depend du temps. Que devient-elle pour un champ uniforme ?
7. Sans lire de travail anterieur : selon toi, l'echelle infrarouge du terme non local log(−∂²/M²) de l'action plate peut-elle, dans le cadre de 1711.00135 (action = action plate du repere conforme + terme anomal exact), introduire une dependance en ln a (ou en H) qui compenserait le ln a du terme anomal ? Argumente.

Rends un rapport structure (questions 1 a 7), avec le nom et l'empreinte sha256 de tes scripts et sorties.
