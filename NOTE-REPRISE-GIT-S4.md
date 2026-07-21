---
id: NOTE-REPRISE-GIT-S4
titre: "Note de reprise autoportante — fin de session S4 (2026-07-21) : quatre lots du Silo R clos et déposés (R-6, R-2, R-12, R-1, tous REPRODUIT-SOUS-RÉSERVE E-2), rejeux de confirmation 17/17 rc=0, une réconciliation majeure (convention volume-gelé, R-2/Q6), écarts décomposés (libellé phase1 ; branche front-pq bénigne). Prochain geste : R-11 OU R-7/R-8/R-10 en session NEUVE, sur décision opérateur."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-21
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S4 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S4 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -7   # attendu : HEAD = « Reprise S4 … », puis a931a4c (R-1),
                           #   9568756 (R-12), 782b600 (R-2), c99a523 (R-6),
                           #   8824501 (Reprise S3), f7c77eb (R-3)
    ls instruments/*.py | wc -l                    # attendu : 26
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l      # attendu : 21 (les 14 de S3 + R1/R2/R12-CIBLES-GELEES,
                           #   R1/R2/R6/R12-REDEMONSTRATION ; la présente note est hors audit/)
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py          # attendu : 35/35 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R5_reductions_b.py  # attendu : 17/17 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R3_spectre.py       # attendu : 16/16 PASS + 6 consignations, EXIT 0
    python3 instruments/redemo_R6_nongauss.py      # attendu : 16/16 PASS + 6 consignations, EXIT 0
    python3 instruments/redemo_R2_D1.py            # attendu : 12/12 PASS + 8 consignations, EXIT 0
    python3 instruments/redemo_R12_O2.py           # attendu : 11/11 PASS + 7 consignations, EXIT 0
    python3 instruments/redemo_R1_moduleA.py       # attendu : 6/6 PASS + 3 consignations, EXIT 0

Tout écart est à décomposer AVANT de poursuivre (leçon V62). Leçons
d'environnement opposables : rejeu long = `setsid nohup … &` puis poll
(S2) ; vérification de push = repli origin/main (la branche est `main`,
constaté S4) ; les redirections `mkdir && cmd1 > f1 & cmd2 > f2 &`
peuvent racer le mkdir — créer le répertoire dans un appel séparé (S4).
Branche distante `origin/front-pq` : RÉSIDUELLE, entièrement contenue
dans main (0 commit d'avance) — bénigne, ne pas toucher.

## 1. Ce qui a été fait en S4 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S3 rejoué conforme** sur toute la ligne.
2. **LOT R-6 CLOS** (commit c99a523) : redérivation sur le gel déposé
   fin S3 (dfd9640f, non re-gelé) ; c=−i/3 DÉRIVÉ du mode BD
   (c³=i/27), moteur de moments gaussien générique (κ₄=0, 3 Wick),
   γ_k=n^k, 64π⁴/N², 512π⁶/N³, ratio π⁴/4 slack nul. 16/16+6c rc0 ;
   rejeu 5/5 rc0 ; 1 réconciliation (branche BD) ; 1 écart de libellé
   (phase1 [LIVE] au gel / [ARCHIVE] à l'inventaire, sha8 1aa3f051
   CONCORDANT — étagère seulement). Grade E-2.
3. **LOT R-2 CLOS** (commit 782b600) : gel S4 (b9b565fb) ; moteurs
   indépendants (Koszul left-invariant SANS Milnor ; courbure 3D/4D).
   Coïncidence 55d/Tod ⟺ m̂λ̂=9k²/4 ; Weyl(FLRW générique)≡0 vs
   Kasner≠0 ; Ricci-tf(e^{2x}δ₃)=(⅔,−⅓,−⅓)e^{−2x} ∧ Cotton≡0 (27
   comp.) ; strictité FW-3 constructive ; A_T·C_T=1/(2π²) N-libre.
   RÉCONCILIATION MAJEURE : jeu déclaré de 12 conventions MANQUÉ sur
   le coefficient 128 (consigné tel quel) ; lecture post-dérivation
   du sceau (§2.0) ⟹ convention = CONTRE-SQUASH À VOLUME GELÉ
   (e^{2ε},e^{−2ε},1) ⟹ 128ε² EXACT au moteur indépendant. 12/12+8c
   rc0 ; rejeu 6/6 rc0 ; 2 corrections d'instrument consignées.
   Grade E-2.
4. **LOT R-12 CLOS** (commit 9568756) : gel S4 (4fe114de). Involution
   nue s=+1 ⟹ P²=+𝟙≠S²=−𝟙 ; J≁S (invariant de classe, GL(2)
   générique) ; C̃_T=+C_T ; i^{d−1} réel ⟺ d impair ;
   dét[v_α|S·v_α]=4μ EXACT ; J échange BD↔BD* ; ledger d=3 ;
   η=rapidité relative ; limite m2 exacte. 11/11+7c rc0 ; rejeu 5/5
   rc0 (dont 3 sha8 attendus au gel) ; 1 cycle de correction
   d'instrument. Grade E-2.
5. **LOT R-1 CLOS** (commit a931a4c) : gel S4 (d197e40a, révélation
   MODESTE mais plafond E-2 tenu : valeurs révélées + cœur d'existence
   importé). Einstein+Λ pour g=Ω⁻²·η_Mink ⟺ Ω affine, Ω'²=Λ/3 ⟹
   ĝ(∇Ω,∇Ω)|𝓘⁺=−Λ/3 EXACT ; trichotomie de caractère ; ĝ non
   dégénérée ; Weyl(dS)=0 ; Friedrich 1986 consigné importé porteur.
   6/6+3c rc0 ; rejeu 1/1 rc0 (690eb4c7). Grade E-2.
6. Le commit qui dépose la présente note (swap −S3 +S4 ; S1–S3
   restent dans l'historique git).

**Bilan Silo R : 7/12 lots clos — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓
R-6 ✓ R-12 ✓, TOUS au grade REPRODUIT-SOUS-RÉSERVE (E-2). Restent :
R-11 ; R-7/R-8/R-10 (rejeu + complétion) ; R-9 (têtes [B] à
localiser au git — possiblement ABSENTES ⟹ écart à consigner le
cas échéant).**

## 2. Discipline en vigueur (inchangée + précédents S4)

Discipline amendée post-CSE INTÉGRALE (note S3 §2) : harnais
PASS/CONSIGNATION, mutations mordantes, gel déclarant la révélation
et le plafond, tolérances avant comparaison, écarts nommés jamais
résorbés. Précédents S4 opposables :
- L'ÉCHEC d'un jeu de conventions déclaré se consigne TEL QUEL, puis
  la réconciliation §2.0 (lecture du sceau POST-dérivation) est
  licite si vérifiée par l'instrument INDÉPENDANT — les deux pièces
  coexistent au rapport (R-2/Q6).
- Un écart de LIBELLÉ (statut d'étagère) à sha concordant se
  décompose et se consigne sans effet de substance (R-6/phase1).
- Les corrections d'instrument en cours de lot (mutations vacantes
  détectées par le harnais lui-même, contournements sympy, signes
  d'orientation propres à l'instrument) se consignent nominalement.

## 3. Décisions opérateur EN ATTENTE

- **Priorisation Silo R** : R-11 d'abord (ordre du lotissement) OU
  groupé court R-7/R-8/R-10 — posée en fin de S4, NON tranchée.
- **G-4** : autorité mount vs git (hypothèse reconduite : mount
  autoritaire R-54, git miroir).
- **Priorisation de substance** : β/P-1 vs report modulaire d=3/P-3.
- **PDF du mount** (5014 Ko) : confrontation à sources/2503_19957v1.pdf.
- G-5b/c (index, arborescence silos) : cadrages non exécutés.

## 4. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus).
2. **Décision opérateur** : R-11 ou R-7/R-8/R-10 (défaut lotissement
   = R-11). Chaque lot = cycle §2.0 amendé complet (gel depuis les
   front-matters SEULS d'abord ; attention : les front-matters F1–F6
   sont du gabarit lourd D1/O₂).
3. **R-9** : localiser les têtes [B] au git AVANT d'ouvrir le lot ;
   si absentes, consigner l'écart et demander l'intrant opérateur
   (têtes au mount).
4. Silos P/V/X : inchangés (P-3 report d=3 recommandé #1 des decks ;
   tracker R-53 : 0/4).

## 5. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, repo LC_Raccord seul, Contents
  R/W, courte durée) au premier message. Le token de S4 a servi aux
  5 pushes de cette session et RESTE LISIBLE dans la conversation S4
  ⟹ À RÉVOQUER dès maintenant (de même que celui de S3 s'il ne l'a
  pas encore été). Sans token : tout reste faisable en local, seuls
  les pushes attendent.
- Aucun autre intrant requis pour R-11 ou R-7/R-8/R-10 (têtes et
  sceaux au dépôt) ; R-9 pourrait requérir les têtes [B] du mount.

## 6. Garde-fou terminal (§6.4)

Clore quatre lots, réconcilier une convention, décomposer des écarts :
AUCUN de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi
que ce soit. REPRODUIT-SOUS-RÉSERVE (E-2) est un grade DIMINUÉ — une
reproduction guidée, pas une corroboration indépendante. Le module [A]
reste conditionné à un théorème externe (Friedrich).
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos (cartographié) · N non fixé
(≡Λ, R-53 : 0/4) · O₂ non construit (β T-b seul facteur ouvert) ·
nœud (i) INDÉTERMINÉ (pas A) · A4 route par-ℐ⁺ délimitée, non
réfuté · A2★ parqué · CCC non démontrée NI réfutée.
