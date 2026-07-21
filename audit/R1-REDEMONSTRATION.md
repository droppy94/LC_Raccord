# R-1 — RAPPORT DE REDÉMONSTRATION (session S4, 2026-07-21)

Lot : module [A] — survie conforme à Λ>0 (𝓘⁺ spacelike, norme −Λ/3,
régularité de la métrique rescalée).
Gel : `audit/R1-CIBLES-GELEES.md`, sha256 =
`d197e40aabc1848292d0cb400bf019634759c7550ed687f39e98797e13a07314`,
figé en S4 AVANT toute redérivation. Gel non re-gelé, non amendé.

Instrument : `instruments/redemo_R1_moduleA.py` — **6/6 PASS
discriminants + 3 consignations déclarées, EXIT 0**. Harnais post-CSE ;
tolérance : algèbre symbolique exacte ; convention de signature
(−,+,+,+) déclarée en tête.

## 1. Aveuglement

Corps KB : NON lus (front-matter de LC-A-SURVIE-CONFORME + ligne R-1
du lotissement, seules sources). Code du sceau : NON lu. Aucune
lecture post-dérivation nécessaire.

## 2. Correspondance cibles → issues

| Cible | Issue | Pièces |
|---|---|---|
| Q1 existence | CONSIGNATION C1 | Friedrich 1986 (existence + stabilité, donnée libre) = théorème importé, résultat porteur du lot |
| Q2 norme | PASS (P03) | ĝ(∇Ω,∇Ω)\|𝓘⁺ = −Λ/3 EXACT, dérivé de P01 ; mutation −Λ/4 mordante |
| Q3 caractère | PASS (P04) | trichotomie complète : Λ>0 ⟹ 𝓘⁺ de genre espace ; Λ<0 timelike ; Λ=0 nul |
| Q4 régularité | PASS (P05) | ĝ = Ω²g = η_Mink, det = −1 ≠ 0 à 𝓘 ; la métrique physique y diverge ; dΩ ≠ 0 |
| Q5 dS explicite | PASS (P01, P02) | moteur de courbure : Einstein+Λ pour g = Ω(η)⁻²·η_Mink ⟺ Ω affine avec Ω'² = Λ/3 ; Ω = −Hη solution EXACTE ; mutations Ω'²=Λ/2 et Ω=−Hη² mordantes |
| Q6 Weyl | PASS (P06) | Weyl(dS) = 0 sur les composantes indépendantes, firewall coef ½→⅓ |

## 3. Réconciliations et corrections

Aucune réconciliation nécessaire ; aucune correction d'instrument ce
cycle (consigné factuellement, sans en faire une force).

## 4. Rejeu de confirmation du sceau du lot (GO opérateur reçu, S4)

Rejoué sur CE clone via `run_sceau.py` — **1/1 rc=0**, sha8 concordant
avec `audit/INVENTAIRE-SCEAUX.md` :

| sceau | statut | sha8 | rc | durée |
|---|---|---|---|---|
| verif_moduleA_scri | ARCHIVE | 690eb4c7 | 0 | 1,8 s |

## 5. Grade

**REPRODUIT-SOUS-RÉSERVE au sens E-2** — plafond annoncé AU GEL, pour
la double raison qui y est consignée : les valeurs d'arrivée étaient
révélées, ET le cœur d'existence est un import (Friedrich) — le grade
couvre la cinématique recalculée, jamais le théorème lui-même. Issue
conforme à la tête (pas d'audit froid mandaté §2.0-5). Rejeu de
confirmation §4 : 1/1 rc=0, sha concordant — la réserve conditionnelle
est levée ; le grade reste E-2 par plafond de gel.

§6.4 : « reproduit » vaut cinématique recalculée + import consigné —
JAMAIS « la CCC survit au crossover » ni « [A] prouve la CCC ». Le
maillon [A] reste ce qu'il était : le plus solide, ET conditionné à
un théorème externe. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée
NI réfutée.
