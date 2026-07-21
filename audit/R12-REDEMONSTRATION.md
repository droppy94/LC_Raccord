# R-12 — RAPPORT DE REDÉMONSTRATION (session S4, 2026-07-21)

Lot : arc O₂ — jonction D→N, transport de Hodge, gates P1/P2,
dimension d'interface Δ_𝒞, coin de transmission.
Gel : `audit/R12-CIBLES-GELEES.md`, sha256 =
`4fe114dee7acb03c0f6124d3889071978da97c2d0963b72bf860b78fb1bf6a69`,
figé en S4 AVANT toute redérivation. Gel non re-gelé, non amendé.

Instrument : `instruments/redemo_R12_O2.py` — **11/11 PASS
discriminants + 7 consignations déclarées, EXIT 0**. Harnais post-CSE ;
tolérance : algèbre symbolique exacte, déclarée avant comparaison.

## 1. Aveuglement

Corps KB du lot : NON lus (front-matters seuls). Code des sceaux :
NON lu. Aucune lecture post-dérivation n'a été nécessaire (aucun
écart à réconcilier).

## 2. Correspondance cibles → issues

| Cible | Issue | Pièces |
|---|---|---|
| Q1 jonction | CONSIGNATION C1 | cartographie zéro-algèbre déclarée |
| Q2 P1 | PASS (P01, P02) | z~Ω⁻² sous Ω↦−1/Ω ⟹ z↦1/z (signe carré perdu, involution vérifiée) ; P²=s·𝟙 ; s=+1 ⟹ P²=+𝟙 ≠ S²=−𝟙 ; mutation poids impair ⟹ le signe survit |
| Q3 Hodge J≁S | PASS (P03) | det(J)=−1 ≠ det(S)=+1, ordres 2/4, vp ±1/±i ; det conservé sous conjugaison GL(2) GÉNÉRIQUE ⟹ aucune base ne fait J=S |
| Q4 garde-fou | PASS (P04) | W̃=−W ∧ T=−2δW/δh ⟹ C̃_T=+C_T (deux −1 composés) ; mutation = un seul flip ⟹ −C_T |
| Q5 source unique | PASS (P05) | i^{d−1} réel ⟺ d impair, = −1 à d=3 ; S²=−𝟙 d-indépendant ⟹ deux −𝟙 distincts |
| Q6 α-vacua | PASS (P08) | **dét[v_α\|S·v_α] = 4μ EXACT** (calcul direct, base (a,b), e±=(1,∓i)) ; zéro ⟺ μ=0 ; mutation S→J casse le sélecteur |
| Q7 racines | PASS (P06, P07) | S réelle ⟹ conj échange e₊↔e₋ (paire non ordonnée) ; J·e₊∝e₋, J·e₋∝e₊ (BD↔BD*, ±i symétriques) |
| Q8 Δ_𝒞 | PASS (P09) + CONSIGNATION C2 | ledger d=3 recalculé (3<4<5<6, coeff TT̄ (d−3)/2=0), trichotomie → C1-b ; W_{N→D} et transport dS bloqué = lectures |
| Q9 coin | PASS (P10, P11) + C3, C4 | η = arcsinh(n·s) = rapidité relative, invariante de boost (dérivé) ; m2 : κ→0 ⟹ retour EXACT au η-term nu ; table b=2/⅔/0 = import ; « p libre ⟹ C1-b positif » = verdict consigné |
| Q10 verdicts | CONSIGNATION C5 | (C-O2) forte non établie ; P1→s=(−1)^w ouvert ; P2 discordance ; TC-b ; β≡G3 seul ouvert |

## 3. Réconciliations

Aucune nécessaire : toutes les valeurs d'arrivée gelées sont
reproduites exactement sous les prémisses consignées (C6).

## 4. Corrections d'instrument consignées (1 cycle, 2 retouches — C7)

P10 : (i) signe d'orientation des normales erroné dans MA propre
expression attendue (n·s = sinh(η₁−η₂) avec l'orientation choisie ;
la cible gelée ne fixe pas d'orientation) ; (ii) identité
asinh∘sinh = id sur ℝ vérifiée par dérivée (=1) + point (0↦0), sympy
ne la réécrivant pas. Aucune cible, aucune tolérance modifiées.
« Premier passage sans correction » ne se présente pas comme force.

## 5. Rejeu de confirmation des sceaux du lot (GO opérateur reçu, S4)

Rejoués sur CE clone via `run_sceau.py` — **5/5 rc=0**, sha8 tous
concordants avec `audit/INVENTAIRE-SCEAUX.md` ET avec les trois sha8
attendus au gel :

| sceau | statut | sha8 | rc | durée |
|---|---|---|---|---|
| verif_O2_P1 | ARCHIVE | 6b23b2ae ✓gel | 0 | 0,6 s |
| verif_O2_P2 | ARCHIVE | f2b110e8 ✓gel | 0 | 0,5 s |
| verif_O2_hodge | ARCHIVE | 421d5f29 ✓gel | 0 | 0,4 s |
| verif_O2_coin_transmission_fetch | ARCHIVE | 7539188d | 0 | 0,5 s |
| verif_O2_coin_transmission_ac | ARCHIVE | 0acf575d | 0 | 0,5 s |

## 6. Grade

**REPRODUIT-SOUS-RÉSERVE au sens E-2** — plafond annoncé AU GEL
(chaîne entière révélée par les front-matters). L'issue coïncide avec
les têtes scellées (aucune divergence ⟹ pas d'audit froid mandaté
par §2.0-5). Rejeu de confirmation §5 : 5/5 rc=0, sha concordants —
la réserve conditionnelle est levée ; le grade reste E-2 par plafond
de gel.

§6.4 : « reproduit » vaut cohérence d'algèbre et d'invariants —
JAMAIS « O₂ construit » (O₂ n'existe pas ; β≡G3 reste le seul facteur
ouvert), ni « A4 réduit », ni « D1 fermé », ni « N fixé ».
{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
