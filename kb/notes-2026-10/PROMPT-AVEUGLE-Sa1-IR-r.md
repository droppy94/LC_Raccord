# Prompt S-a1 : re-derivation independante (cecite stricte), terme de charge de Weyl de l'anomalie sur une onde gravitationnelle de de Sitter

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_sa1/ ; ne cherche pas de notes, scripts ou resultats anterieurs (en particulier rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/ ni dans d'autres dossiers audit_*) ; ne consulte pas de sources externes. Tout ce qu'il faut est ci-dessous. Travaille avec sympy (python3). Reponds en francais, sans tirets longs. Etiquettes : [calcule] (sortie de script), [derive] (raisonnement).

## Cadre
- Metrique physique ĝ = s⁻²(η + ε h), η = diag(−1, 1, 1, 1) en (s, x, y, z), s = −τ > 0 (τ temps conforme), facteur conforme Ω = s, H = 1. 𝓘⁺ en s → 0. Premier ordre en ε.
- h : mode tensoriel, k selon x, polarisation « plus » : h_yy = −h_zz = u(s) cos kx, avec u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks) (A, B constantes). Verifie que u est solution de l'equation du mode tensoriel de de Sitter.
- Action : S_C = b ∫ d⁴x √ĝ φ Ĉ_abcd Ĉ^abcd, avec φ = −ln s (fonction fixee) et b une constante. Utilise l'invariance de Weyl de √g C² pour travailler avec g = η + ε h si tu le souhaites, en le justifiant.
- Tenseur physique : T̂_ab = (2/√ĝ) δS_C/δĝ^{ab}, au premier ordre en ε. **Obtiens-le par ta propre methode** (variation brute d'Euler-Lagrange, ou forme fermee que tu verifies toi-meme contre une variation brute).
- Equation testee (Friedrich, second membre de l'equation (2.17)) : L̂ = (κ/2)(T̂ − ⅓ ĝ tr_ĝ T̂) ; R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), ∇̂ connexion de Levi-Civita du fond ĝ₀ = s⁻²η (suffisant au premier ordre en ε puisque T̂ est deja d'ordre ε).

## Questions
1. Donne T̂_ab au premier ordre en ε, developpe en puissances de s (et ln s s'il y en a) pres de s = 0. Est-il sans trace ? Conserve (∇̂^a T̂_ab = 0) ? Contient-il des ln s ? Quelles donnees (A, B) portent quels ordres ?
2. Developpe toutes les composantes non nulles de R_ρνλ en s pres de 0. Quelle est la plus basse puissance de s ? Y a-t-il un pole, un ln s, ou rien de singulier ? Donne les coefficients en fonction de A, B, k, b, κ.
3. Calcule la partie electrique du Weyl rescale W = C[g]/Ω (C[g] tenseur de Weyl de g = η + εh, indices bas, composantes C_sisj/s) a 𝓘⁺. Exprime le terme dominant de R a l'aide de cette quantite.
4. Le terme dominant de R est-il un artefact de jauge (diffeomorphisme infinitesimal) ou de repere conforme ? Justifie.
5. Si R contient un terme en Ω⁻¹ proportionnel a W, que devient W pres de 𝓘⁺ quand on l'integre dans une equation de transport de type ∂_s W ~ R (raisonnement qualitatif, sans equation de transport complete) ?

Rends un rapport structure (questions 1 a 5) avec les noms et empreintes sha256 de tes scripts et sorties.
