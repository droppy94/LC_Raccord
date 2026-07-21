# R-2 — RAPPORT DE REDÉMONSTRATION (session S4, 2026-07-21)

Lot : verrou D1 cartographié — atlas FLRW (Ω̂=c₁â, point fixe),
délimitation (FLRW Δ1-b + inhomogène D1c3-c), jambe amplitude.
Gel : `audit/R2-CIBLES-GELEES.md`, sha256 =
`b9b565fb0c01cac2b0173e14f4122fea07cfb34106a3314cf43997f5d5b6e24e`,
figé en S4 AVANT toute redérivation (sha consigné hors-fichier en
session). Gel non re-gelé, non amendé.

Instrument : `instruments/redemo_R2_D1.py` — **12/12 PASS
discriminants + 8 consignations déclarées, EXIT 0**. Harnais post-CSE ;
tolérance : algèbre symbolique exacte, avec UNE exception déclarée au
gel : l'adjudication de convention du coefficient Q6 (jeu de 12
conventions énuméré AVANT calcul).

## 1. Aveuglement

Corps KB du lot : NON lus (front-matters seuls, conformément au gel).
Code des sceaux : NON lu avant la dérivation aveugle ; UNE lecture
post-dérivation pour la réconciliation Q6 (protocole §2.0 :
« dérivation aveugle → réconciliation », précédent [B]) — voir §3.

## 2. Correspondance cibles → issues

| Cible | Issue | Pièces |
|---|---|---|
| Q1 famille Ω̂=c₁â | PASS partiel (P04) + CONSIGNATION C1 | convergence des 3 prescriptions = IMPORT ; « relation ≠ valeurs » dérivé : sur m̂λ̂=9k²/4, c₁=√(2λ̂/3k) dépend encore de λ̂ |
| Q2 coïncidence | PASS (P02) | élimination de c₁ entre 55d et Tod ⟺ m̂λ̂ = 9k²/4 EXACT |
| Q3 k=0 | PASS (P03) | pôle de 55d ; droite fixe → triviale |
| Q4 dynamique MS | CONSIGNATION C2 | forme de la carte éq.14 non portée par les front-matters ⟹ Jacobien/det J*/runaway = imports |
| Q5 Weyl | PASS (P08, P09) | Weyl(FLRW, a(η) GÉNÉRIQUE) ≡ 0 calculé (moteur 4D) ; Weyl(Kasner ⅔,⅔,−⅓) ≠ 0 |
| Q6 squashé | PASS (P01, P10, P11) + C3, C-ADJ | moteur Koszul indépendant (S³ ronde Einstein ✓) ; σ̌≠0 à ε=½, lim→0 ; coefficient 128 : voir §3 |
| Q7 contre-exemple | PASS (P05, P06) | Ricci-tf(e^{2x}δ₃) = (⅔,−⅓,−⅓)e^{−2x} recalculé ; Cotton ≡ 0 sur les 27 composantes, firewall Schouten R/4→R/6 mordant |
| Q8 FW-3 | PASS (P07) + CONSIGNATION C4 | strictité Einstein-3D ⊊ {Cotton=0} constructive (même g : Cotton=0 ∧ tf≠0) ; le théorème conteneur = import |
| Q9 amplitude | PASS (P12) | A_T·C_T = 1/(2π²) N-LIBRE ; C_T/N = 1/(32π²) — cross-cohérence des deux scellés |
| Q10 verdict d'axe | CONSIGNATION C5 | délimitation, A3 socle, D1c3-3 déchargée — verdicts consignés |

## 3. Réconciliation consignée (1) — le coefficient 128

La dérivation aveugle a testé un jeu DÉCLARÉ de 12 conventions
(squash axisymétrique × structure s × Misner) : AUCUNE ne donne 128
(valeurs obtenues : 32/3, 128/3, 384, 512/3, 2048/3, 6144 — rapports
rationnels simples à 128). Cet échec du jeu déclaré est CONSIGNÉ TEL
QUEL (C-ADJ[Q6]), aucun coefficient altéré.

Réconciliation (post-dérivation, lecture du sceau d'origine
`verif_D1c3_regularite.py` l.105) : la convention d'origine est un
CONTRE-SQUASH À VOLUME GELÉ, facteurs (A₁,A₂,A₃) = (e^ε, e^{−ε}, 1)
⟹ λ = (e^{2ε}, e^{−2ε}, 1) — une FAMILLE différente (biaxiale,
det gelé), pas une normalisation différente. Vérifiée par MON moteur
Koszul indépendant (jamais par le code du sceau) :
**|σ̌|² = 128·ε² + O(ε⁴) EXACT** ; mutation s=2 ⟹ 2048 (mordante).
Après réconciliation : AUCUN écart numérique résiduel sur le lot.

## 4. Corrections d'instrument consignées (2)

(1) La mutation de P07 (strictité) était VACANTE au premier passage
(tautologie — détectée par le harnais lui-même, FAIL) : remplacée par
un firewall réel (le prédicat doit échouer sur δ₃ plate).
(2) Le bloc de réconciliation Q6 a été ajouté APRÈS l'échec du jeu
déclaré. Aucune cible, aucune tolérance, aucun coefficient du premier
passage modifiés. « Premier passage sans correction » ne se présente
pas comme force — il y en a eu deux.

## 5. Rejeu de confirmation des sceaux du lot (GO opérateur reçu, S4)

Rejoués sur CE clone via `run_sceau.py` — **6/6 rc=0**, sha8 tous
concordants avec `audit/INVENTAIRE-SCEAUX.md` :

| sceau | statut | sha8 | rc | durée |
|---|---|---|---|---|
| verif_D1_facteur | ARCHIVE | fed811ea | 0 | 1,1 s |
| verif_D1_atlas | ARCHIVE | 9ec5bc60 | 0 | 0,3 s |
| verif_D1_bianchiA | ARCHIVE | 8b46efb0 | 0 | 7,2 s |
| verif_D1_stabilite | ARCHIVE | 41509a9f | 0 | 0,7 s |
| verif_D1c3_regularite | ARCHIVE | 3fc462fe | 0 | 5,3 s |
| verif_D1c3_genericite | ARCHIVE | b615d6b4 | 0 | 0,7 s |

Le sha8 attendu au gel (b615d6b4, généricité) CONCORDE. Les deux
D1c3 ont été lancés en `setsid nohup` + poll par précaution (leçon
S2) ; durées effectives < 10 s, consignées sans interprétation.

## 6. Grade

**REPRODUIT-SOUS-RÉSERVE au sens E-2** — plafond annoncé AU GEL
(front-matters massivement révélants). L'issue finale COÏNCIDE avec la
tête scellée (aucune divergence de substance ⟹ pas d'audit froid
mandaté par §2.0-5) ; la lecture post-dérivation du sceau pour la
réconciliation est signalée à l'opérateur, qui peut mander un CSE s'il
en juge autrement. Rejeu de confirmation §5 : 6/6 rc=0, sha
concordants — la réserve conditionnelle est levée ; le grade reste
E-2 par plafond de gel.

§6.4 : « reproduit » vaut cohérence d'algèbre et de coefficients —
JAMAIS « D1 fermé » (D1 reste OUVERT, cartographié : jambe sélection
délimitée, jambe amplitude absorbée dans N), ni « sélecteur trouvé »,
ni « N fixé ». { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI
réfutée.
