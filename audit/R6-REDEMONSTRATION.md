# R-6 — RAPPORT DE REDÉMONSTRATION (session S4, 2026-07-21)

Lot : secteur (non-)gaussien — 3-pt ⟨TTT⟩ + verrou 4-pt ∝ N⁻³.
Gel : `audit/R6-CIBLES-GELEES.md`, sha256 =
`dfd9640f9f7bbb5554bba718d1df0269a424c6f747d57befad8907e3c6e82e51`,
déposé EN FIN de session S3 (commit 8824501) — la présente redérivation
s'est ouverte en session NEUVE (anti-fit renforcé). Gel NON re-gelé,
NON amendé.

Instrument : `instruments/redemo_R6_nongauss.py` — **16/16 PASS
discriminants + 6 consignations déclarées, EXIT 0**. Harnais à deux
issues (règle post-CSE) : chaque PASS porte une mutation nommée qui le
fait échouer ; les imports/prémisses/verdicts conditionnels sont
consignés HORS décompte. Tolérance : algèbre symbolique exacte
(sympy, `simplify(diff)==0`), déclarée avant toute comparaison.

## 1. Aveuglement

Corps KB du lot (LC-WORK-CADRAGE-NONGAUSS, -4PT ; LC-D-NONGAUSS-*) :
NON lus. Code des sceaux du lot : NON lu avant redérivation.
Seules sources : le gel lui-même (front-matters cités) + acquis R-4
(A_T·N = 16) + prémisses déclarées C5/C6.

## 2. Correspondance cibles → issues

| Cible | Issue | Pièces |
|---|---|---|
| Q1 zéro libre | PASS (P02, P04, P05) | c dérivé du mode BD : coefficient η³ de (1+ikη)e^{−ikη} = −(i/3)k³ ⟹ c³ = i/27 exact ; ⟨g₀³⟩ = 0 par moteur ⟹ ⟨g₃³⟩_libre ≡ 0 |
| Q2 map γ₃ | PASS (P08, P09) | multilinéarité ⟹ n³ ; n=2 ⟹ 8 ; catalogue {2,4,8} par énumération des 2³−1 mélanges |
| Q3 comptage d=3 | CONSIGNATION C1 | IMPORT OP∩MP — non redérivable en interne (déclaré au gel) |
| Q4 scaling 3-pt | PASS (P11, P12, P13) | (H/M_Pl)² = 8π²/N ; amplitude 64π⁴/N² = carré exact du 2-pt ; ratio π⁴/4 avec ∂/∂N = 0 (slack nul vérifié) |
| Q5 verdict tête | PASS partiel (P16) + CONSIGNATION C3 | rigidité « aucun paramètre libre neuf » testée (free_symbols = {N}) ; la décision W³ reste ouverte (P-7), consignée |
| Q6 scission 4-pt | PASS (P01, P03, P06) | moteur de moments générique : 3 appariements exactement, κ₄ = 0 ⟹ connexe au vertex |
| Q7 map γ₄ | PASS (P07, P10) | γ₄ = n⁴ dérivé PAR le moteur (⟨(nψ)⁴⟩/⟨ψ⁴⟩) ; n=2 ⟹ 16 ; catalogue {2,4,8,16} |
| Q8 scaling 4-pt | PASS (P14, P15) | (8π²/N)³ = 512π⁶/N³, exposant N = 3 ; pattern 2(κ−1) instancié sur κ = 2,3,4 |
| Q9 structure | CONSIGNATION C2 | IMPORT BGJPS/Hu (déclaré au gel) |
| Q10 verdict 4-pt | PASS partiel (P16) + CONSIGNATION C4 | RATTACHÉ-N testé par rigidité ; résidus W³/W⁴ sous Einstein pur = conditionnalité consignée |

## 3. Réconciliation consignée (1)

**Sélection de branche du mode BD.** La dérivation aveugle donne
|c| = 1/3 et c = ∓i/3 selon la branche du mode ((1±ikη)e^{∓ikη}).
La cible Q1 (préfacteur +i/27) adjuge la branche (1+ikη)e^{−ikη},
c = −i/3 : (−i/3)³ = +i/27 exact ; la branche conjuguée donne −i/27
(c'est la mutation de P04/P05). Écart : AUCUN après adjudication —
c'est une convention d'orientation du temps conforme, pas un slack.
Consigné comme réconciliation, à la manière des deux réconciliations
de R-4.

## 4. Écarts numériques

Aucun : toutes les comparaisons sont exactes (symboliques). Aucune
tolérance numérique n'a été consommée ; aucun ajustement effectué.

## 5. Rejeu de confirmation des sceaux du lot (GO opérateur reçu, S4)

Rejoués sur CE clone via `run_sceau.py` — **5/5 rc=0**, sha8 tous
concordants avec `audit/INVENTAIRE-SCEAUX.md` :

| sceau | statut | sha8 | rc | durée |
|---|---|---|---|---|
| verif_D_nongauss_TTT | ARCHIVE | c06f6f51 | 0 | 0,6 s |
| verif_D_nongauss_4pt | ARCHIVE | a46e4f6a | 0 | 0,5 s |
| verif_D_nongauss_4pt_phase1 | ARCHIVE | 1aa3f051 | 0 | 0,5 s |
| verif_D_nongauss_TTT_lourd | ARCHIVE | 2cb93432 | 0 | 1,2 s |
| verif_D_nongauss_TTT_lourd_phase1 | ARCHIVE | e494c8c6 | 0 | 0,7 s |

Les « lourds » ont été lancés en `setsid nohup` + poll (leçon S2)
mais se sont exécutés en ~1 s sur ce clone — durée CONSIGNÉE sans
interprétation (mode allégé possible côté sceau ; non investigué,
hors périmètre du lot).

ÉCART DE LIBELLÉ décomposé (V62) : le gel étiquette
`verif_D_nongauss_4pt_phase1.py` [LIVE], l'inventaire S4 le classe
[ARCHIVE] — sha8 `1aa3f0513e531ce8` CONCORDANT ⟹ artefact identique,
seul le statut d'étagère diffère (archivage probable entre S1 et S3).
Écart nommé, borné, sans effet sur les clés de sceau.

## 6. Grade

**REPRODUIT-SOUS-RÉSERVE au sens E-2** — plafond annoncé AU GEL
(les front-matters révèlent la chaîne interne entière ; reproduction
guidée, jamais E-1). Rejeu de confirmation §5 : 5/5 rc=0, sha
concordants — la réserve conditionnelle est levée ; le grade reste
E-2 par plafond de gel.

§6.4 : « reproduit » vaut cohérence de coefficients — JAMAIS « secteur
non-gaussien fermé », ni « D1 fermé », ni « N fixé ».
{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
