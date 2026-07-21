# R-6 — CIBLES GELÉES (protocole §2.0 amendé post-CSE) — 2026-07-21

Source : front-matters SEULS de LC-WORK-CADRAGE-NONGAUSS v0.1,
LC-WORK-CADRAGE-NONGAUSS-4PT v0.1, LC-D-NONGAUSS-TTT (id/titre/statut),
LC-D-NONGAUSS-4PT (id/titre/statut) — corps NON lus. Lus au dépôt git
(R-54 tenu). Figé AVANT toute redérivation ; sha256 consigné au rapport
de lot. GEL EN FIN DE SESSION S3 ; la redérivation s'ouvrira en session
NEUVE (le gel précédant la session de dérivation renforce l'anti-fit).

## DÉCLARATION DE RÉVÉLATION DU MÉCANISME (règle post-CSE, opposable)

Les front-matters révèlent la chaîne interne ENTIÈRE : linéarité de la
relation d'état ⟹ propagation de la gaussianité (moments impairs nuls,
cumulant 4 nul, 3 appariements de Wick), map γ_k = n^k (Brown–York
n=2), dictionnaire (H/M_Pl)² = 8π²/N, pattern d'exposants connexe
∝(H/M_Pl)^{2(n−1)}, et TOUTES les valeurs d'arrivée. Ils révèlent aussi
que le comptage d=3 et les confrontations (Osborn–Petkou ∩
Maldacena–Pimentel ; BGJPS 2212.07370 ; Hu 1502.02329 ; Dymarsky
1311.4546) sont des FETCHS EXTERNES — non redérivables en interne.

⟹ PLAFOND DE GRADE ANNONCÉ AU GEL : au mieux REPRODUIT-SOUS-RÉSERVE au
sens E-2. JAMAIS E-1.

CONTENU DISCRIMINANT ATTENDU du lot (le reste = consignations) :
(a) la COMBINATOIRE GAUSSIENNE recalculée par un moteur de moments
générique (pas une redite) : ⟨g₀³⟩=0, cumulant₄=0, les 3 appariements ;
(b) les COMPOSITIONS de dictionnaire avec firewalls (8π²/N ; 64π⁴/N² ;
ratio π⁴/4 ; 512π⁶/N³ ; exposants 2(n−1)) ;
(c) le catalogue d'artefacts γ ({2,4,8}, {2,4,8,16}) dérivé de n^k et
de ses mélanges.
Les comptages de structures et le contenu des sources fetchées :
IMPORTS, consignés, jamais comptés PASS.

## Cibles

| # | cible | valeur revendiquée |
|---|---|---|
| Q1 | [3pt-A] zéro libre | ⟨g₃³⟩_libre = (i/27)k₁³k₂³k₃³·⟨g₀³⟩ = 0 IDENTIQUEMENT (BD libre gaussien) ⟹ le 3-pt vit au vertex |
| Q2 | [3pt-B] map γ₃ | γ₃ ≡ ⟨TTT⟩_canon/ψ₃ = n³ ; n=2 ⟹ γ₃=8 ; catalogue d'artefacts de mélange {2,4,8} |
| Q3 | [3pt-D] comptage d=3 | 2 formes paires + 1 impaire (hors bispectre) ; Einstein = 1 forme, W³ = l'autre ⟹ n_libre = 1 — IMPORT (OP∩MP), consignation |
| Q4 | [3pt-E] scaling | (H/M_Pl)² = 8π²/N (via A_T·N=16) ; ⟨γγγ⟩_Einstein ∝ (H/M_Pl)⁴ = CARRÉ du 2-pt ⟹ amplitude 64π⁴/N² ; ratio (H/M_Pl)⁴/A_T² = π⁴/4, slack NUL |
| Q5 | [3pt] verdict tête | aucun paramètre libre neuf sous Einstein ; liberté résiduelle = coeff. W³ ~(LH)⁴, NUL sous Einstein pur — décision ouverte, consignation |
| Q6 | [4pt-A] scission | 4-pt libre = DÉCONNECTÉ (3 appariements de Wick du 2-pt scellé) + CONNEXE NUL (cumulant gaussien d'ordre 4 = 0) ⟹ le connexe vit au vertex |
| Q7 | [4pt-B] map γ₄ | γ₄ = n⁴ ; n=2 ⟹ γ₄=16 ; catalogue {2,4,8,16} |
| Q8 | [4pt-C] scaling | pattern connexe ∝ (H/M_Pl)^{2(n−1)} ⟹ 4-pt connexe ∝ (8π²/N)³ = 512π⁶/N³ (exposant N = 3) |
| Q9 | [4pt-D] structure | contact quartique + échange (cubique×cubique) — IMPORT (BGJPS/Hu), consignation |
| Q10 | [4pt] verdict | B4-a RATTACHÉ-N : rigidement déterminé, pendu à N, aucun constant neuf ; résidu = coeff. Weyl supérieurs (W³-échange, W⁴-contact) NULS sous Einstein pur — même conditionnalité, consignation |

Sceaux du lot (rejeu de confirmation inclus, GO opérateur à demander en
session neuve) : verif_D_nongauss_TTT.py [ARCHIVE] + variantes lourd/4pt
[ARCHIVE] + verif_D_nongauss_4pt_phase1.py [LIVE, sha8 1aa3f051, apport
S1]. Leur CODE n'est pas lu avant la redérivation.

Grades possibles : REPRODUIT-SOUS-RÉSERVE (E-2) ·
REPRODUIT-SOUS-RÉSERVE (écart nommé borné) · NON-REPRODUIT.

§6.4 : figer des cibles ne scelle, ne réduit, ne compte, ne démontre
rien. « Reproduit » vaudra cohérence de coefficients — JAMAIS « secteur
non-gaussien fermé », ni « D1 fermé », ni « N fixé ».
{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
