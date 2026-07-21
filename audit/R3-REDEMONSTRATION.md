# R-3 — REDÉMONSTRATION DU SPECTRE k³ ET DE LA VARIANCE LOG (2026-07-21)

Lot du Silo R, protocole §2.0 AMENDÉ post-CSE (première application
complète de la discipline issue du verdict E-3).

## 1. Cycle du lot

1. **Gel** : `audit/R3-CIBLES-GELEES.md`, sha256 `eded7406…5479e39879`,
   figé AVANT toute redérivation, depuis le front-matter SEUL de
   LC-D3-SPECTRE-K3 v0.3 (corps non lu), lu au dépôt git (R-54 tenu,
   décision opérateur de session). Le gel DÉCLARE la révélation du
   mécanisme (règle post-CSE) : la chaîne k³ entière est révélée ⟹
   plafond E-2 annoncé AU GEL. Seule pièce non révélée : la forme
   exacte du noyau de variance.
2. **Instrument** : `instruments/redemo_R3_spectre.py` —
   **16/16 PASS discriminants + 6 consignations déclarées, EXIT 0**
   (harnais PASS/CONSIGNATION, firewalls mordants).
3. **Sceaux du lot rejoués** (confirmation, GO opérateur) :
   `verif_D3_spectre_k3.py` [ARCHIVE] sha8=706e97cc **rc=0** ·
   `verif_D3_bunchdavies.py` [ARCHIVE] sha8=7f269735 **rc=0**
   (lanceur run_sceau, kb-root du clone). Leur code n'a PAS été lu
   avant la redérivation.

## 2. Résultat central : le noyau exact reconstruit en quasi-aveugle

Le gel ne donnait que l'enveloppe (cos²x/3), la moyenne (1/6) et
β∞=0,04503. Reconstruction depuis les prémisses, ANTI-FIT consigné :
**3 candidats essayés**, discriminés par β∞ —
(ii) cos²x/(3x) : IR-divergent, rejeté avant intégration ;
(iii) x·cos²x/(3(1+x²)) : β=−0,0257, rejeté ;
(i) **K(x) = f_b(x)²/(3x³), f_b = x·cos x − sin x : RETENU**,
β∞(25 déc.) = 0,0450605.

Lecture structurelle : f_b est le SECOND MEMBRE DU DOUBLET S1 établi en
R-4 T10 (f_a, f_b) — le noyau de variance est bâti sur le partenaire
dual du mode BD (BD = f_a − i·f_b). Vérifié symboliquement : f_b
solution de l'EOM radiale ; enveloppe x·K = cos²x/3 + correction exacte
(−sin2x/3x + sin²x/3x²) ; IR-sûr (K ~ x³/27) ; décomposition UV exacte
K − 1/(6x) = cos2x/6x − sin2x/3x² + sin²x/3x³ ⟹ croissance LOG
(mesurée : I(2000)−I(200) = (1/6)ln10, le 1/6 discriminé du 1/4) —
PAS de quartique.

## 3. Écart nommé, borné, NON corrigé (anti-fit)

|β∞(recalculé) − β∞(gelé)| = |0,0450605 − 0,04503| = **3,0·10⁻⁵**
(7·10⁻⁴ relatif, 5ᵉ chiffre). La valeur gelée est « établi numérique »
dans la tête ; l'écart est compatible avec la précision de son calcul
d'origine. AUCUN ajustement du noyau n'a été opéré pour résorber
l'écart. Tolérance de l'assert déclarée (±1e-4) AVANT comparaison.
C(√(N/π)=1,02·10⁶¹) = 23,458 reproduit 23,46 à la précision affichée
de la cible (±0,01) ; seuil de finitude 0,5/C = 0,0213 calculé.
√(N/π)=√(8π)M_Pl/H=ℓ_dS/ℓ_P dérivé symboliquement.

## 4. Corrections d'instrument en cours de lot — consignées (leçon #7)

Une (1) correction : la quadrature de croissance sur [200, 2000]
(intégrande oscillant) était imprécise sans subdivision ⟹ FAIL franc au
premier passage ; corrigée par subdivision aux périodes π. Ni le noyau,
ni les cibles, ni les tolérances n'ont été modifiés. « Premier passage »
ne se présente pas comme force ; le FAIL initial est une donnée (le
harnais mord).

## 5. Sans double compte

K1 (𝒫_h) et la relation d'état g₃ sont PRÉ-COUVERTS (R-4 T1, R-5 P1) :
consignés, importés, recalcul de contrôle seul — ils ne comptent pas
dans les 16 PASS du lot au titre de contenu neuf. Le contenu propre du
lot : la composition P_{g₃}=(1/9)k⁶P_{g₀}, l'exposant exact, et tout le
bloc variance (noyau, β∞, log, cutoff, finitude).

## 6. Grade

**REPRODUIT-SOUS-RÉSERVE** — au sens E-2 (reproduction guidée pour la
chaîne révélée) **avec écart nommé borné** (β∞, §3). JAMAIS E-1
(plafond annoncé au gel). La reconstruction du noyau, seule pièce
quasi-indépendante, est adjugée par cinq contraintes gelées
indépendantes (enveloppe, moyenne, log, β∞ à ±1e-4, C) — c'est la
corroboration la plus forte que le lot pouvait produire sous son
plafond.

## §6.4

Redériver, reconstruire un noyau, rejouer deux sceaux : rien de tout
cela ne scelle, ne réduit, ne compte, ne démontre. Le verdict de la
tête (« SPECTRE k³ CONTRÔLÉ, conditionnel à A_T≪1 et au cadre CCC »)
n'est ni promu ni dégradé par ce lot. { A4 ; A2★ ; N } INCHANGÉ ·
D1 non clos · circularité LC-E intacte · CCC non démontrée NI réfutée.
