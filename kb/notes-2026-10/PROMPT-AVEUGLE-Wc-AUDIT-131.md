# Prompt W-c : audit de trois affirmations et de leurs scripts, recherche de contre-exemples (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Lis uniquement les fichiers de /home/claude/audit_wc/ ; ne lis rien d'autre sur le disque (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/, ni dans d'autres dossiers audit_*). Travaille avec sympy (python3) dans /home/claude/audit_wc/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

Empreintes a verifier :
- irt_a.py 97ca373277844327960a23bcbd43b06035752a018c911afb772036e32993d95b
- irt_a_ctrl.py 62b96e1cc4df53223d85e52bae766e33430e16c2dbd2302bb35380f82ffdae37
- irt_gamma_phi.py 0d3f44cdde18ca5b5b17a8e7342e1c38ca27142fbf7aa4a29c917fe4f8b1e064

Contexte : de Sitter plat ĝ = s⁻²(η + εh), σ = −ln s ; equation de Friedrich (2.17) : R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), L̂ = (κ/2)(T̂ − ⅓ĝ trT̂), Ω = s. Mode tensoriel h_yy = −h_zz = u cos kx, u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks).

## Affirmations
- **t-1** : la partie de l'action anomale associee a la densite d'Euler, sous forme de Wess-Zumino integrable ∫√g [σ(E − ⅔□R) + 2σΔ₄σ] (g metrique de reference, Δ₄ operateur de Paneitz), donne a l'ordre ε un tenseur physique egal a 6 ĝ_ab (coefficient a = 1), donc sans effet sur R de (2.17). Un controle avec le coefficient −½ a la place de 2 donne un resultat different (le test discrimine).
- **t-2** : un T̂ sans trace, conserve, de la forme s^p × (tenseur lisse en s) donne un pole en 1/s dans R pour p = 1, et aucun pole pour p = 2.
- **t-3** : □_η²(ln s) = −6/s⁴ ≠ 0 (□_η = −∂_s² + ∂_x²) ; un φ_h lisse avec □²φ_h = 0 donne, via T = 8b ∂^c∂^d(φ_h C_acbd), T̂ = s² T, aucun pole dans R.

## Mission
1. Audite chaque script point par point (OK / DEFAUT). En particulier : t-1, la normalisation de T a partir de la variation brute (signe fixe par le fond) ; l'expression de Δ₄ ; le developpement de √g et de g⁻¹ ; t-3 (a), le calcul de □² (signe, dimension : sur l'espace-temps 4D, □_η²(ln s) ne depend que de s ; verifie).
2. Reproduis independamment t-1 (au moins le fond et un controle a l'ordre ε), t-2 et t-3.
3. **Contre-exemples** : t-2 avec un tenseur s² Y non conserve ou avec une trace ; t-2 pour p = 1 avec y₀ = 0 ; t-3 avec un φ_h non lisse (par exemple s² ln s, ou s³ ln s : solution de □² = 0 ?) ; existe-t-il un mode homogene de □² singulier en s = 0 qui produirait un pole ?
4. Juge chaque affirmation : valide, valide sous hypotheses (nomme-les), ou invalide.

Rends un rapport structure avec les empreintes de tes scripts et sorties.
