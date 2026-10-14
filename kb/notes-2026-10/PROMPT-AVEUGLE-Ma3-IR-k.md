# Prompt M-a3 : re-derivation independante (cecite stricte), completion de Riegert et secteur non Maxwell

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_ma3/ ; ne cherche pas de notes, scripts ou resultats anterieurs (en particulier rien sous /mnt/user-data/ ni sous /home/claude/irm/) ; ne consulte pas de sources externes. Tout ce qu'il faut est ci-dessous. Travaille avec sympy (python3). Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Cadre
- de Sitter fixe, H = 1, s = −η > 0 (η temps conforme), Ω = s, metrique de fond ĝ = s⁻²η_flat, η_flat = diag(−1,1,1,1) en (s, x, y, z). 𝓘⁺ en s → 0. Premier ordre en β.
- Action anomale covariante : S_B = −(β/2e²) ∫ √g Ω[g] F_μν F^μν, avec Ω[g] = ¼ Δ₄⁻¹ F₄ (completion de Riegert ; Δ₄ operateur de Paneitz-Riegert, F₄ densite d'Euler-Weyl combinee telle que √g(Δ₄ φ − ¼F₄) se transforme simplement sous g → e^{2σ}g ; sur le fond, Ω[ĝ] = −ln s).
- Decomposition : partie (a) = variation de √g F² a Ω fixe (secteur Maxwell X^M, qui porte I² = e⁻²[1 + 2β(λ − ln s)]) ; partie (b) = variation de Ω[g] a J = √g F² fixe.
- Forme locale de (b) : S_b = ∫ J φ + ∫ √g ψ (Δ₄φ − ¼F₄), φ et ψ champs auxiliaires ; sur couche φ = Ω[g] et √g Δ₄ ψ = −J, soit □_η² ψ = −J dans le repere plat (invariance de Weyl de √g Δ₄). ψ est la solution retardee ; J est d'ordre zero en β et analytique en η pres de η = 0.
- Partie W invariante de Weyl (reste de l'action effective) : tenseur de poids de Weyl, T^W[g] = s² T^W[η_flat] sur le fond conformement plat, evalue sur des champs du repere plat.
- Champ test : mode A_y = u(s) cos(kx), u = u₀ cos(ks) + (c/k) sin(ks) + β u₁, equation de mode (I² u_s)_s + k² I² u = 0. Champs a 𝓘⁺ : B = rot A (selon z), E = ∂_s A (selon y).
- Equation testee : L̂ = (κ/2)(T − ⅓ ĝ tr_ĝ T) ; R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ).
- Resultat anterieur admis (deja audite) : le coefficient de β ln s a l'ordre s⁰ de R_isj vaut (3κ/e²)(Q_ij − ⅓ δ_ij tr Q), Q = B_iB_j − E_iE_j a 𝓘⁺ (sous une fermeture isotrope du secteur non Maxwell).

## Questions
1. Montre ou infirme l'identite ∇^μ X^M_μν = −¼ ∂_ν(I²) F² sur couche, pour le mode ci-dessus non moyenne. Le coefficient de ln s dans ∇^μ X^M_μν est-il nul au premier ordre en β ?
2. Variation metrique de S_b pour la famille g = s⁻² diag(−1, 1 + εh₁, 1 + εh₂, 1 + εh₃)(s, x), au premier ordre en ε, avec ψ(s, x) et φ = −ln s. Construis Δ₄ et F₄ explicitement (formules standard que tu ecriras), verifie Δ₄(−ln s) − ¼F₄ = 0 sur le fond. Donne les tenseurs T^(b)_i = δS_b/δh_i en fonction de ψ.
   (a) Contiennent-ils ln s ? Contiennent-ils φ (ou seulement ses derivees, ou rien) ?
   (b) Pour ψ lisse en s, quelle est la plus basse puissance de s dans T^(b)_ii (composantes coordonnees) ?
   (c) T^(b) distingue-t-il les directions y et z pour un J(s, x) ?
3. Calcule R en prenant T = X^M seul (sans aucun secteur non Maxwell). Le coefficient de ln s a l'ordre s⁰ reproduit-il la loi admise ci-dessus ? D'autres logs apparaissent-ils ?
4. T^(b) peut-il compenser la partie sans trace de Q ? T^W peut-il porter un log ? Quelles hypotheses ton raisonnement utilise-t-il (etat de ψ, famille de metriques, variation de W hors orbite de Weyl) ?

Rends un rapport structure (questions 1 a 4) avec les noms et empreintes sha256 de tes scripts et sorties.
