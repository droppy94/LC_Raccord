# Prompt M-a1 : re-derivation independante (cecite stricte), version inhomogene et dipole eteint

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_ma1/ ; ne cherche pas de notes, scripts ou resultats anterieurs (en particulier rien sous /mnt/user-data/ ni sous /home/claude/irm/) ; ne consulte pas de sources externes. Tout ce qu'il faut est ci-dessous. Travaille avec sympy (python3), et numpy/scipy si utile. Reponds en francais, sans tirets longs. Etiquettes : [calcule] (sortie de script), [derive] (raisonnement).

## Cadre
- de Sitter fixe, H = 1, s = −τ > 0 (τ temps conforme), Ω = s, ĝ = Ω⁻²η, η = diag(−1,1,1,1) en (s, x, y, z). 𝓘⁺ en s → 0.
- Action effective simplifiee : S = −¼ ∫ I² F_μν F^μν (indices par η), I² = e⁻²[1 + 2β(λ − ln s)], λ constante, β > 0 petit. Tout au premier ordre en β, developpement en puissances de s et de ln s quand s → 0.
- Champs du repere conforme a 𝓘⁺ : B = rot A, E = −∂_τ A = ∂_s A.
- Secteur Maxwell : X^M_μν = I²(F_μα F_νβ ĝ^{αβ} − ¼ ĝ_μν F_αβ F^αβ_ĝ), non moyenne.
- Trace anomale locale T̂(s, x) = −(β/(2e²)) F_μν F^μν|_η Ω⁴ (locale, non moyennee).
- L̂ = (κ/2)(T − ⅓ ĝ tr_ĝ T), T = X^M + X^R ; second membre R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ) (Christoffel de ĝ).
- Resultat anterieur admis (partie homogene, deja audite) : pour la partie homogene sous une fermeture isotrope, le coefficient de β ln s a l'ordre s⁰ de R_isj est (3κ/e²)(Q_ij − ⅓ δ_ij tr Q), Q = ⟨B_iB_j − E_iE_j⟩ moyenne spatiale a 𝓘⁺.

## Questions
1. **Loi locale.** Mode non moyenne A_y = u(s) cos(kx), u = u₀ cos(ks) + (c/k) sin(ks) + β u₁ (u₀ et c quelconques, equation de mode (I² u_s)_s + k² I² u = 0). Secteur non Maxwell avec fermeture locale isotrope (appelons-la H-loc) : X^R = diag(r0, r1, r1, r1)(s, x) plus une composante q(s, x) en (s, x) ; trace totale ĝ^{μν}(X^M + X^R)_μν = T̂(s, x) ; divergence covariante totale nulle aux ordres controles. Developpement polyhomogene en s, dependance en x par cos 2kx et sin 2kx ; laisse libres les fonctions d'integration.
   (a) Calcule le coefficient de ln s a l'ordre s⁰ dans toutes les composantes de R. Compare-le au tenseur local Q(x) = B_i(x)B_j(x) − E_i(x)E_j(x) (non moyenne) a 𝓘⁺.
   (b) A quel ordre en s les gradients en x (facteurs k, derivees de B² et E²) entrent-ils dans les coefficients de log ?
   (c) Les fonctions ou constantes libres de la fermeture entrent-elles dans un coefficient de log ?
2. **Dipole magnetique eteint.** Repere conforme plat, dipole m(t) = m₀ ẑ f(t) a l'origine, f marche lisse de largeur w passant de 1 a 0 autour de t = −D (extinction), avec D ≫ w. Champs exacts du dipole dependant du temps (temps retarde t_r = t − r), evalues a t = 0.
   (a) Verifie les equations de Maxwell sans source hors de l'origine.
   (b) Decris la carte de Q_tf(x) (partie sans trace de B_iB_j − E_iE_j) a t = 0 dans trois regions : r < D, coquille r ≈ D, r > D. Y a-t-il du champ, donc un log, dans r < D ?
   (c) Moyennes angulaires des parties sans trace pour la structure statique (champ proche du dipole) et pour la structure rayonnee, en unites de (m̂m̂ − ⅓𝟙). Integrales radiales par region, avec une normalisation que tu expliciteras, et comparaison a ce que tu attends analytiquement.
3. **Compensation.** Sans H-loc, une contrainte anisotrope non Maxwell d'ordre s² ln s, libre dans ce cadre, pourrait-elle annuler le log local de R ? Justifie.

Rends un rapport structure (questions 1 a 3) avec les noms et empreintes sha256 de tes scripts et sorties.
