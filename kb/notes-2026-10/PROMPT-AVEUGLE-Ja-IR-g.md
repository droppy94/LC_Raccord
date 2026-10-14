# Prompt J-a : re-derivation independante (cecite stricte)

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_ja/, ne cherche pas de notes, scripts ou resultats anterieurs, et ne consulte pas de sources externes (tout ce qu'il faut est ci-dessous). Travaille avec sympy (python3). Reponds en francais, sans tirets longs. Etiquettes : [calcule] (sortie de script), [derive] (raisonnement).

## Cadre
- de Sitter fixe, H = 1, s = −τ > 0 (τ temps conforme), Ω = s, ĝ = Ω⁻²η, η = diag(−1,1,1,1) en (s, x, y, z). 𝓘⁺ en s → 0.
- Action effective simplifiee : S = −¼ ∫ I² F_μν F^μν (indices par η), I² = e⁻²[1 + 2β(λ − ln s)], λ constante, β > 0 petit. Tout au premier ordre en β, developpement en puissances de s et ln s quand s → 0.
- Champ : superpositions de modes A_j = u(s) ε_j cos(k·x) (jauge de Coulomb, ε ⊥ k). Equation de mode (I² u_s)_s + k² I² u = 0. Pres de 𝓘⁺ chaque mode s'ecrit u = u₀ cos(ks) + (c/k) sin(ks) + β u₁, et les champs du repere conforme a s = 0 sont B = rot A et E = −∂_τ A = ∂_s A.
- Secteur Maxwell : X^M_μν = I²(F_μα F_νβ ĝ^{αβ} − ¼ ĝ_μν F_αβ F^αβ_ĝ). Partie homogene : moyenne spatiale.
- Trace anomale moyenne T̂ = −(β/(2e²)) ⟨F_μν F^μν⟩_η Ω⁴. Fermeture isotrope C-iso : X^R = diag(r0, r1, r1, r1)(s), trace totale ĝ^{μν}(X^M + X^R)_μν = T̂, divergence covariante totale nulle (Christoffel de ĝ).
- L̂ = (κ/2)(T − ⅓ ĝ tr_ĝ T), T = X^M + X^R ; second membre R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ).

## Questions
1. Pour un mode unique (k selon x, ε selon y), u₀ et c quelconques : calcule le coefficient de β ln s dans X^M non moyenne a l'ordre s², composante par composante (y compris la composante (s, x)). Exprime-le a l'aide de B(x) et E(x) a 𝓘⁺.
2. Meme mode, partie homogene, C-iso : coefficients de ln s a l'ordre s⁰ dans toutes les composantes non nulles de R. Exprime-les en fonction du tenseur Q_ij = ⟨B_iB_j − E_iE_j⟩ (sa trace et sa partie sans trace). Trouve la loi generale si elle existe (coefficient numerique explicite). La trace de Q contribue-t-elle ?
3. Teste ta loi sur une configuration ou Q n'est pas diagonal dans les axes (s, x, y, z) : par exemple deux modes de directions de k differentes, ou un mode de polarisation oblique. Les termes croises entre modes, apres moyenne spatiale, comptent-ils ?
4. Source eteinte : le mode est libre apres τ = −D avec u(−D) = a, u'(−D) = 0. Donne B et E a 𝓘⁺, et la partie de Q qui ne depend pas de D. Moyenne cos(2kD) sur un spectre kⁿ e^{−k/k⋆} pour n = 2 et x = 2k⋆D grand.
5. Source coherente : dipole magnetique m, courant transverse J_k ∝ i k × m, de sorte que le potentiel de chaque mode est selon k × m. Calcule la moyenne sur les directions de k de (ε_Bε_B − ε_Eε_E), ε_E le long de A et ε_B le long de k × ε_E (vecteurs non normalises, poids inclus). Puis la moyenne sur des orientations isotropes de m.
6. Conclusion : quel objet a 𝓘⁺ decide de la presence d'un ln dans R ? La dichotomie « champ a dominante magnetique / E = B en module » est-elle le bon critere ?

Rends un rapport structure (questions 1 a 6) avec les noms et empreintes sha256 de tes scripts et sorties.
