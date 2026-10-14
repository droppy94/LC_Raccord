---
id: RAPPORT-OP-IR-AUDIT-AVEUGLE-Da-Db
date: 2026-10-10
objet: rapports des sous-agents D-a et D-b (audit froid aveugle conjoint de NOTE-102 et NOTE-104), substance reproduite fidelement
gel: NOTE-BORD-EON-105-ARMEMENT-AUDIT-OP-IR (2026-10-10T19:20:21Z)
---

# Rapport D-a (re-derivation independante, cecite stricte)
Aucun fichier anterieur lu, aucun article consulte (les attributions aux sources viennent du seul enonce). Scripts dans /home/claude/audit_da/ : da_calc.py (5307c28e…), da_calc_out.txt (8ab0fc5d…), da_check_rad.py (4d0a3652…), da_check_rad_out.txt (ba484935…).

1. Mode : u₁'' + k²u₁ = (2/s)u₀', λ disparait. Magnetique : u₁ = −k²u₀s² + k⁴u₀s⁴/9 − 23k⁶u₀s⁶/5400, sans ln s. Electrique : 2c s ln s + s³(−(ck²/3) ln s + ck²/9) + …, ln s des s ln s. Residus nuls a l'ordre β.
2. ⟨X^M⟩ = s² X⁰ (1 + β(A + B ln s)), diagonal, sans trace. Magnetique : X⁰ = (k²u₀²/4e²) diag(1,1,1,−1), B = −2 sur les quatre composantes. Electrique : (c²/4e²) diag(1,1,−1,1), B = +2 (F_sy ∝ 1/I²).
3. C-iso : r₀ = C s² (C invisible dans R, controle R ≡ 0 pour le rayonnement). R_xsx = R_ysy = (K/4)[1 + 2β(λ − ln s) − ⅔β], R_zsz = −2 ×, K = κk²u₀²/e². Champ uniforme : (κB₀²/2e²)[1 + 2β(λ − ln s − ⅓)]. **Coincidence exacte terme a terme a l'ordre s⁰** avec B₀² → k²u₀²/2 ; ecart a l'ordre s² (gradients).
4. Mode libre : plat 0 ; δF = 0, Hodge 0 ; □F/F = 4 (F_xy et F_sy), uniforme 4. Weitzenböck Δ_H = −□ + p(n−p)H².
5. Terme residuel de S2 : O(β²) ; branche magnetique borne ; branche electrique au plus β² ln² s, du meme ordre que (β ln s)² deja neglige.
6. Validite : u₀ ≪ k (magnetique), c ≪ k² (electrique), independantes du temps (rapport invariant de Weyl) ; ∇² a entendre comme gradient spatial (le d'Alembertien plat est nul sur couche) ; champ uniforme hors domaine (regime Euler-Heisenberg) : la coincidence de Q3 avec le champ uniforme est formelle.
7. Non : l'action plate ne voit ni a ni H ; toute la dependance en σ est dans le terme anomal exact ; le ln a est la course du couplage a k_phys. Seule echappatoire : sortir du cadre (covariantisation Bochner, non covariante de Weyl ; regime hors validite).

# Rapport D-b (audit du code et de la lecture)
Empreintes conformes. arxiv.org bloque par le proxy ; textes via alphaXiv : 1711.00135 lu en entier ; S2 §1 a §4.3 et §5. Scripts : audit_db_indep.py (0c5236c2…), audit_db_indep_sortie.txt (6f44546c…), audit_db_etat.py (0d136994…), audit_db_etat_sortie.txt (1be24714…).

| Point | Verdict |
|---|---|
| Christoffels, D, div | OK (formule conforme fermee) |
| Equation de mode, signes | OK (contre S2 3.9) |
| Resolution magnetique | OK (Green) |
| Resolution electrique | OK ; b1 = 142/105 arbitraire (sans effet sur les logs, fixe la constante) |
| Moyenne, extraction des logs | OK ; troncature mixte s² ln s en section C (cosmetique) |
| C-iso, R | OK, reproduit a l'identique |
| Bochner | OK (Hodge par etoile, Weitzenböck verifie sur 2-forme generique) |
| Sorties D1, D3 du script | **DEFAUT documentaire** : log(k²/k²) tautologique ; D3 et « R = 12 » codes en dur ; ctrl (i) tautologique |

C1-C4 confirmes ; C5 calcul exact mais portee surinterpretee (reproduit l'approximation 3.10 de S2 ; sur couche, log diverge ; S2 : « some width »).
L1 exact (nuances : une boucle, R ≪ M₀², anomalie C ignoree, pas de modes nuls). L2 exact. L3 exact mais **limite a l'ordre R³** et attribue a [8, 33]. L4 exact (de Sitter mentionne comme application). L5 exact (ecrit pour le scalaire) ; hors horizon la lecture en impulsion physique ne s'applique pas.
D1 : valide sous hypotheses, formulation trop forte : « aucun terme en H² dans l'operateur effectif » (H entre additivement par ln H absorbable dans λ, et par ks dans l'etat). Hypotheses : metrique exactement Weyl-plate ; champs charges conformes ; vide conforme ; noyau causal in-in ; action plate valide. Contre-exemple hors hypotheses (memoire, non verifie) : QED scalaire minimalement couplee en de Sitter, masse de photon ∝ H (Prokopec, Törnkvist, Woodard 2002). Forme BV non invocable en de Sitter (R² ≪ ∇²R viole).
D2 : valide a premier ordre fixe ; electrique : termes β² ln s/s probables avec le vrai noyau retarde, uniformes tant que β|ln s| ≪ 1.
D3 : valide.
D4 : **a corriger : dependance a l'etat**. Poids E et B egaux (c = ku₀, Bunch-Davies hors horizon) : les ln s s'annulent a O(β) dans ⟨X^M⟩_ss, dans la trace spatiale et dans ⟨F²⟩ (T̂ = 0) ; apres isotropisation R = 0 au premier ordre ; restent des ±(3/2) ln s anisotropes pour une direction de k fixee. Coherent avec S2 (4.12)/(4.16). Branche magnetique : X^M ∝ I², log exact dans S_simp ; electrique : ∝ 1/I². Les coefficients de ln s sont robustes (seuls de I_B) ; les constantes (−β/6, λ, b1) ne sont pas determinees (S2 note 4).
