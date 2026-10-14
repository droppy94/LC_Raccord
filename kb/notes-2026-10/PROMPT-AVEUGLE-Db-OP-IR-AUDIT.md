# Prompt D-b : audit du code et de la lecture de source (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail qui a produit les fichiers ci-dessous. Lis uniquement les fichiers de /home/claude/audit_db/ (copies des scripts et de leurs sorties) et les sources arXiv citees ; ne cherche pas d'autres notes ou fichiers sur le disque. Travaille avec sympy (python3) dans /home/claude/audit_db/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive], [extrait].

## Fichiers
- op_ir_v2.py et op_ir_v2_sortie.txt (calcul principal) ; op_ir_v2_ctrl.py et op_ir_v2_ctrl_sortie.txt (controles) ; op_ir.py et op_ir_v1_sortie.txt (premiere version, echouee, conservee).
- Verifie d'abord les empreintes sha256 : op_ir_v2.py 77620a4161cedaab8a0e3172d4f5eee5ab5bb98df8ac421f2c81ab3c34396fb5 ; op_ir_v2_ctrl.py 1b24fd9de15a29467a14acc1155bedf66ff48f3732918cb1d334dd1e485c4fbe.

## Cadre (rappel)
de Sitter H = 1, s = −τ = Ω > 0, ĝ = Ω⁻²η ; action simplifiee de S2 (arXiv:1808.08237, eq. 3.12-3.15) I² = e⁻²[1 + 2β(λ − ln s)], λ = ln(M/k) ; mode A_y = u(s)cos(kx) ; premier ordre en β ; X^M = I²(F F ĝ⁻¹ − ¼ĝ F·F) moyenne en x ; fermeture isotrope C-iso (X^R = diag(r0,r1,r1,r1), trace totale = trace anomale T̂ = −(β/2e²)⟨F²⟩_η Ω⁴, conservation) ; L̂ = (κ/2)(T − ⅓ĝ trT) ; R_ρνλ = Ω⁻¹(∇̂_νL̂_λρ − ∇̂_λL̂_νρ).

## Affirmations soumises a l'audit
**Calcul (scripts)**
- C1 : branche magnetique, U1 = −u₀k²s² + u₀k⁴s⁴/9 + … sans ln s ; branche electrique, U1 contient 2c s ln s ; residus nuls a l'ordre tronque.
- C2 : ⟨X^M⟩ magnetique = (k²u₀²s²/4e²) diag(1,1,1,−1) a l'ordre 0 ; coefficient de β ln s = −2 × ordre 0 sur les 4 composantes ; electrique : diag(1,1,−1,1) et rapport +2.
- C3 : R (2.17) partie homogene, branche magnetique : R_xsx = κk²u₀²/(4e²) − βκk²u₀²/(6e²) + βκk²u₀²λ/(2e²) − (βκk²u₀²/(2e²)) ln s ; R_zsz = −2 × R_xsx ; identique au champ uniforme F_xy = B₀ avec B₀² → k²u₀²/2, a la constante en λ pres.
- C4 : sur le mode libre, −∂²_η A_y = 0 ; δF = 0 donc Hodge Δ F = 0 ; Bochner −□F = −4F (champ uniforme et mode).
- C5 : (S2, terme residuel) −β log((k² − k₀²)/k²) = 0 a k₀ = 0 ; condition (3.16) de S2 : β/(1 + 2β ln(aM/k)) → 0 vers 𝓘⁺.

**Lecture de source (arXiv:1711.00135, reference [21] de S2)**
- L1 : la partie anomale de l'action (I_B) est exacte a une boucle sur toute metrique Weyl-plate, sans approximation de courbure ; toute la dependance en Ω y est contenue.
- L2 : la partie non locale restante est l'action plate du repere conforme, avec le d'Alembertien plat ; elle ne depend pas de Ω.
- L3 : 1711.00135 ecarte l'interpretation par log du d'Alembertien covariant seul ; dans la forme covariante de Barvinsky-Vilkovisky, tous les termes sauf F(−⅙∇⁻²R)F sont invariants de Weyl et se reduisent a l'action plate.
- L4 : l'action plate n'y est calculee que sous F² ≪ ∇²F ; le regime de champ constant est cite comme extension non faite ; de Sitter, H, l'infrarouge et le comportement de log(p²) a p² = 0 n'y sont pas traites.
- L5 : la lecture « impulsion physique » (p² = e^{−2Ω}k²) suppose un facteur d'echelle lentement variable ; pour un facteur rapidement variable, la base d'impulsion ne s'applique plus mais l'action reste valide.

**Conclusions derivees**
- D1 : dans le cadre de 1711.00135, aucune echelle en H ne peut apparaitre ; la valeur −4H² de Bochner provient d'une covariantisation tronquee.
- D2 : le terme residuel de S2 (seconde ligne de son eq. 3.9) agit sur {u'' + k²u}, d'ordre β, donc il n'entre qu'a l'ordre β² dans l'equation de mode ; les resultats au premier ordre n'en dependent pas.
- D3 : la condition F² ≪ ∇²F s'ecrit u₀ ≪ k pour le mode et ne depend pas du temps ; elle est violee par un champ uniforme (k = 0).
- D4 : verdict : le ln a du secteur Maxwell persiste a k fini (coefficient 2β), la partie homogene reproduit le cas uniforme ; l'echelle infrarouge est fixee par la structure de 1711.00135 ; reste ouvert le domaine de validite de l'action plate (champ quasi constant).

## Mission
1. Audite le code (Christoffels, derivees covariantes, moyenne spatiale, resolution du mode, troncatures, extraction des logs, fermeture C-iso, R, Bochner) : verdict OK / DEFAUT par point, avec controles independants la ou un controle du script serait tautologique.
2. Reproduis independamment C1 a C5 (au moins C2, C3, C4).
3. Lis les sources (1711.00135 en entier si possible ; S2 §2 et §3.1) et juge L1 a L5 : exact, inexact, ou surinterprete, avec citations courtes.
4. Juge D1 a D4 : valide, valide sous hypotheses (nomme-les), ou invalide. Cherche activement un contre-exemple, en particulier pour D1 (une dependance en Ω ou en H par l'etat, l'infrarouge, les bords en s → 0, ou le noyau non local) et D2 (branche electrique, singularite en 1/s).
5. Liste les reserves et corrections.

Rends un rapport structure avec les empreintes de tes scripts et sorties.
