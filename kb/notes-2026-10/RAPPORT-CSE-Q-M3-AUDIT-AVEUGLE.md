---
id: RAPPORT-CSE-Q-M3-AUDIT-AVEUGLE
date: 2026-10-09
objet: rapports des sous-agents S-a et S-b (audit froid aveugle de NOTE-92 / q_m3_log_v5), reproduits tels que rendus
gel: NOTE-BORD-EON-93-ARMEMENT-AUDIT-FROID-Q-M3 (2026-10-09T17:23:33Z)
---

# Rapport S-a (re-derivation independante, cecite stricte)

Pour A ≠ 0, il faut choisir entre deux défauts, et on ne peut éviter les deux à la fois :
- Choix 1 : R est sans puissance négative de Ω et sans ln aux ordres m ≤ 1. Dans ce cas, un terme ln Ω de coefficient fixé par A est obligatoirement présent dans hat-T.
- Choix 2 : hat-T est entièrement sans ln. Dans ce cas, R a un pôle en Ω^{-2} de coefficient Aκ/(2k²).

Pour A = 0, aucune de ces contraintes ne s'applique.

Fichiers : /home/claude/audit_a/audit_a.py (b0d64769…), audit_a_checks.py (65918c03…), audit_a.out (c12132e8…), audit_a_checks.out (00e59564…).

Conventions : ln Ω = ln(−τ), τ^m = (−1)^m Ω^m ; R_{ρνλ} = Ω^{-1}(∇̂_ν L̂_{λρ} − ∇̂_λ L̂_{νρ}) ; Christoffels directs, vérifiés par formule conforme ; composantes orthonormées physiques = Ω² Y. Ambiguïté majeure : le choix de la fonction libre (h = Y00 ou f = Yxx) n'est pas canonique, les deux sont traitées.

Q1. Trace : −Y00 + Yxx + 2Yyy = Aτ². Conservation τ : −Y00' + ik Y0x + 2Y00/τ + Aτ = 0. Conservation x : −Y0x' + ik Yxx + 2Y0x/τ = 0. Une seule fonction libre. Paramétrisation h : Y0x = (h' − 2h/τ − Aτ)/(ik), Yxx = (Y0x' − 2Y0x/τ)/(ik), Yyy = (Aτ² + h − Yxx)/2. Paramétrisation f : Y0x = τ²(c1 + ik∫f/τ²), Y00 = τ²(c0 + A ln(−τ) + ik∫Y0x/τ²).

Q2. h = Σ a_{n,j} τ^n ln^j(−τ), n de −4 à 6, j ≤ 2 (variante n de −5 à 6, j ≤ 3 : même résultat). Le coefficient de τ^m dans R ne dépend que des a_n, m+1 ≤ n ≤ m+4 : ordres m ≤ 2 exacts. En paramétrisation f polynomiale : Y00 ⊃ (A + k²f₀)τ² ln, −k²f₁ τ³ ln ; Y0x ⊃ ik f₁ τ² ln.

Q3. 104 conditions linéaires, solution unique : a_{2,1} = A, a_{4,1} = −Ak²/6 ; autres coefficients n ≤ 0 et autres ln jusqu'à n = 5 nuls ; a_1 à a_5 libres. Y00 = a1 τ + a2 τ² + A τ² ln + … ; Yxx = −2a1/(k²τ) + (A/2 − 2a4/k²)τ² + (A/3)τ² ln + … ; Yyy = a1/(k²τ) + … + (A/3)τ² ln + …. En paramétrisation f : Yxx sans τ^0, τ^1, τ^{-2}, avec (A/3)τ² ln imposé.

Q4. Non vide pour A ≠ 0, mais ln toujours présent dans hat-T : ρ_phys ⊃ A Ω⁴ ln Ω, p_x = p_y = p_z ⊃ (A/3) Ω⁴ ln Ω, partie de trace nulle, structure de fluide de radiation. Résonance séculaire : trace en a^{-4}, ρ' + 4Hρ = −H·trace force ρ ∝ Ω⁴(c + A ln Ω). Conditions supplémentaires : Y00 = O(τ) (ρ_phys = O(Ω³)), Yxx(0) = Yxx'(0) = 0. A = 0 : ensemble admissible sans ln.

Q5. f polynomiale : R_{xτx} ⊃ (κ/2)(A + k²f₀) ln Ω, R_{yτy} = R_{zτz} ⊃ −(κ/4)(A + k²f₀) ln Ω, et si f₁ ≠ 0 R_{ττx} ⊃ −iκk f₁ ln Ω. Sans pôles (f₀ = f₁ = 0) : coefficient κA/2. Suppression possible par f₀ = −A/k² (équivalent : h sans ln), T alors sans ln, au prix : anisotropie Ω², pôles R_{xτx} ⊃ Aκ/(2k²) Ω^{-2}, R_{yτy} ⊃ −Aκ/(4k²) Ω^{-2}, R_{ττx} ⊃ iAκ/(2k) Ω^{-1}, R_{yxy} ⊃ −iAκ/(4k) Ω^{-1} ; avec h₀ ≠ 0, pôles jusqu'à Ω^{-4}. Pôle ∝ A/k², divergent quand k → 0.

Contrôles : conservation et trace exactes (h générique, ansatz, paramétrisation f, vrai log numérique) ; R recalculé par formule conforme manuelle ; cas A = 0 ; robustesse de la troncature. Limites : un mode, k > 0, premier ordre, fond fixe.

# Rapport S-b (audit du code q_m3_log_v5.py)

Empreinte vérifiée d240832c…0ce74fa. Exécution 5,8 s (sympy 1.14.0). Conclusion imprimée : complétions régulières avec A non nul, A = 3·e2, paramètres libres α, β, c2, c3, e2. Verdict global : (b) confirmée avec réserves.

| # | Point | Verdict |
|---|---|---|
| 1 | Christoffels et dérivée covariante | OK |
| 2 | Conservation, trace, intégrations, log(τ) → log(−τ) | OK |
| 3 | Antisymétrisation et couverture des composantes | OK, défaut cosmétique |
| 4 | Extraction des termes non lisses | OK, défaut cosmétique |
| 5 | Argument de troncature | OK, vrai et conservateur |
| 6 | Complétude des inconnues | lacune mineure, sans effet |
| 7 | La conclusion découle-t-elle du calcul | OK, reproduite indépendamment |

Détails : Christoffels recodés par formule conforme ; calcul refait en s = −τ > 0 avec dsolve propre, mêmes a et b ; 24 composantes calculées, 6 non nulles, 2 indépendantes (R_{0 01}, R_{1 01}), couvertes ; (0,2,2) et (1,2,2) identiquement nulles (ν = λ), cosmétique ; τ^10 suffit, équation « 0 » parasite filtrée. Troncature : R_{1 01} dépend de c jusqu'à τ^(m+2), R_{0 01} jusqu'à τ^(m+1) ; ajout de τ⁴, τ⁴ ln, τ⁴ ln² : conditions et solution inchangées ; en imposant tous les ordres contrôlés pour N = 4 à 7, A reste libre, queue C2_1 = A/3, C4_1 = −k²A/10, C6_1 = k⁴A/168, ln² et ln³ nuls, coefficients impairs nuls. Inconnues manquantes f0, f1 (ln² en τ⁰, τ¹) et ln³ : forcées à 0, sans effet. Substitution de la solution : restes non lisses hors des ordres contrôlés (L τ² dans (1,0,1), L τ³ dans (0,0,1)), annulés par C4_1.

Réserves : pas de preuve à tous les ordres (vérifié jusqu'à N = 7) ; donnée d'état non lisse requise ((A/3)τ² ln et queue), sens subordonné à l'admission du polyhomogène ; linéaire, un mode, k > 0, k = 0 non traité ; défauts cosmétiques.

Scripts de contrôle : ctrl_indep.py (03df4ab4…), ctrl_trunc.py (21b47e19…), ctrl_subst.py (6b82622d…), sortie run_v5.log.
