---
id: NOTE-REPRISE-GIT-S9
titre: "Note de reprise autoportante — fin de session S9 (2026-07-24) : lot R-11 dérivé, clos et déposé (REPRODUIT-SOUS-RÉSERVE E-2, plafond du gel atteint non dépassé, au SECOND passage après correction d'instrument). SILO R CLOS À 12/12. Aucun lot de redémonstration ne reste. Prochain geste : arbitrage opérateur — Silo P (β/P-1 vs report modulaire d=3/P-3), ou soldes G-1/G-4/G-5b-c."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-24
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S9 » ; le vérifier par git log, JAMAIS par cette note."
---

# Note de reprise S9 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -3   # attendu : HEAD = « Reprise S9 … », puis le
                           #   commit S9 (lot R-11), puis le commit
                           #   « Reprise S8 … »
    ls instruments/*.py | wc -l                    # attendu : 33 (31 en S8,
                                                   #   + redemo_R11_falsifiabilite.py
                                                   #   + harnais_R11.py)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 32 (29 en S8,
                                                   #   + gel + amendement
                                                   #   + rapport R-11)
    ls kb/*.md | wc -l                             # attendu : 215
    ls hors-KB/B/ | wc -l                          # attendu : 4
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE /
                                                   #   76 ARCHIVE / 1 ABSENT
                                                   #   — MESURÉ INCHANGÉ en S9
                                                   #   sur arbre modifié AVANT
                                                   #   écriture de cette note
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py               # attendu : 35/35 PASS +  5 consignations
    python3 instruments/redemo_R5_reductions_b.py       # attendu : 17/17 PASS +  5 consignations
    python3 instruments/redemo_R3_spectre.py            # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R6_nongauss.py           # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R2_D1.py                 # attendu : 12/12 PASS +  8 consignations
    python3 instruments/redemo_R12_O2.py                # attendu : 11/11 PASS +  7 consignations
    python3 instruments/redemo_R1_moduleA.py            # attendu :   6/6 PASS +  3 consignations
    python3 instruments/redemo_R8_A2star.py             # attendu : 21/21 PASS + 10 consignations
    python3 instruments/redemo_R10_nonlin.py            # attendu : 40/40 PASS + 14 consignations
    python3 instruments/redemo_R7_A4QW.py               # attendu : 45/45 PASS + 10 consignations
    python3 instruments/redemo_R9_tracteur.py           # attendu : 16/16 PASS +  8 consignations
    python3 instruments/redemo_R11_falsifiabilite.py    # attendu : 36/36 PASS + 19 consignations
                                                        #   (NOUVEAU S9 ; sympy seul)

**Total attendu : 271/271 PASS + 101 consignations, 12/12 rc = 0.**

**L'addition est DÉCOMPOSÉE, pas supposée** — exécutée en S9 sur l'arbre de
dépôt et recomptée indépendamment par grep des marqueurs dans les logs :

    PASS  : 35 + 17 + 16 + 16 + 12 + 11 + 6 + 21 + 40 + 45 + 16 + 36 = 271
    CONS. :  5 +  5 +  6 +  6 +  8 +  7 + 3 + 10 + 14 + 10 +  8 + 19 = 101

Hors compte §0-lite, trois rejeux de confirmation disponibles :

    python3 instruments/harnais_R9.py     # attendu : « HARNAIS R-9 : 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py    # attendu : « HARNAIS R-11 : 7/7 mordantes »
                                          #   + « aucun assert sans porteur mutable »,
                                          #   rc=0 (NOUVEAU S9 ; ~30 s ; PAS compté
                                          #   dans 271/101)
    cd hors-KB/B && python3 verif_B_tracteur.py    # attendu : rc=0, sha8=8e386686

Les cinq sceaux ARCHIVE de R-11, rejouables un par un (jamais deux dans le
même arbre), sha8 attendus : `verif_F1_spn` 19a4931e (20 assertions) ;
`verif_F4_principiel` 9947b8ed (25) ; `verif_F5_scaling` a959f137 (19) ;
`verif_F6_memoire_cisaillement` 23a7d264 (18) ; `verif_D3_WCH_GWE` 664660ee.

Tout écart est à décomposer AVANT de poursuivre (leçon V62) : d'abord
l'addition, puis le lot divergent, puis l'assert.

### Leçons d'environnement opposables

Toutes celles de S2–S8 MAINTENUES (rejeu long en `setsid nohup` ; répertoire
de logs créé en appel séparé ; repli `origin/main` pour la vérification de
push ; `ls audit/` et non `ls audit/*.md` ; jamais deux sceaux en concurrence
dans le même arbre ; les durées ne se reportent pas et ne sont pas des clés
de sceau ; branche `origin/front-pq` résiduelle bénigne, ne pas toucher).

**Écart d'arbre bénin, récurrent et attendu** : `inventaire_sceaux.py` réécrit
sa ligne de date (bilan identique 6/76/1) ; restaurer par
`git checkout -- audit/INVENTAIRE-SCEAUX.md`.

**Deux formats de marqueur coexistent** (acquis S8, confirmé S9) : la plupart
des redemo impriment `[PASS]` / `[CONSIGNATION]` ; `redemo_R6_nongauss.py`
imprime sans crochets. Le recompte indépendant DOIT tolérer les deux formats
(motif `^\s*\[?PASS\]?` et son pendant), sinon un lot conforme apparaît à 0/0.

**NOUVEAU S9 — le motif `[p]ython3` ne protège pas du shell englobant.**
`ps -eo pid,etime,cmd | grep "[p]ython3"` s'est AUTO-MATCHÉ : non par le grep
(le motif `[p]` fait son office) mais parce que la ligne de commande du
`/bin/sh -c` parent contenait elle-même la chaîne cherchée. Sonder dans un
appel SÉPARÉ et court, ou filtrer `/bin/sh -c`, sinon une sonde propre
rapporte un faux processus vivant.

## 1. Ce qui a été fait en S9 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S8 rejoué CONFORME** sur toute la ligne : 235/235 PASS,
   82 consignations, 11/11 rc = 0, HEAD `c683691`, comptes 31/76/29/215/4,
   inventaire 6/76/1, sceau 051e2833. Recompte indépendant lot par lot
   concordant. AUCUN écart de dépôt.
2. **LOT R-11 DÉRIVÉ ET CLOS — dernier du Silo R.** Gel `298e2094` figé AVANT
   la première ligne d'instrument (antériorité auditable : le répertoire ne
   contenait que le gel au relevé du sha), plafond **E-2 annoncé AU GEL**,
   corps des 20 têtes JAMAIS ouverts (front-matters seuls), code des 5 sceaux
   JAMAIS lu. **36/36 PASS + 19 consignations, rc 0** ; harnais **7/7
   mordantes** ; 5 sceaux ARCHIVE rejoués rc=0, 4/4 comptes confrontables
   concordants. Grade **REPRODUIT-SOUS-RÉSERVE (E-2)**, plafond atteint non
   dépassé ; issue conforme ⟹ pas d'audit froid (§2.0-5).
3. Le commit qui dépose la présente note (swap −S8 +S9 ; S1–S8 restent dans
   l'historique git).

**Bilan Silo R : 12/12 lots clos** — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓ R-6 ✓
R-7 ✓ R-8 ✓ R-9 ✓ R-10 ✓ **R-11 ✓** R-12 ✓, TOUS au grade
REPRODUIT-SOUS-RÉSERVE (E-2). **Aucun lot de redémonstration ne reste.**

## 2. Écarts de S9 — trois, tous imputables au PILOTE, aucun au dépôt

À lire AVANT de juger le 36/36 : ce lot n'est pas propre de la même manière
que R-9.

1. **Défaut d'énoncé du gel (F4-1)** : le gel disait « strictement monotone
   DÉCROISSANTE », énoncé faux (l'argmin d'une f décroissante part à
   l'infini). Corrigé par AMENDEMENT-1 (`9d30fce6`) daté AVANT la première
   ligne d'instrument, gel laissé byte-intact. Aucune tolérance desserrée.
2. **QUATRE faux PASS au premier passage** : la v1 sortait 38/38 ; l'audit de
   vacuité du harnais a dénoncé F4-2, F6-2d, F6-5a, F6-5b — aucun porteur
   mutable ne les traversait, donc ils ne pouvaient pas échouer (F4-2
   comparait `{0}=={0}`). **Correction d'instrument exécutée** : deux retirés
   et consignés, F6-2d remplacé par une construction effective de l'objet à un
   epsilon avec porteur dédié (mutation m7, mordante). **R-11 n'est donc PAS
   « premier passage sans correction ».**
3. **Cible F3-1 reclassée** en consignation par la clause I-c pré-déclarée au
   gel : le fait visé vit au corps des sources, tout assert aurait été une
   recopie du front-matter.

## 3. Contenu de substance de R-11 — pour mémoire

- **WCH-GWE (le cœur mordant)** : le mode exact
  `Ω_σ/ε² = (x cos x − sin x)²/(3x²)` a pour terme dominant **exactement
  x⁴/27** (la forme scellée est retrouvée, pas recopiée), terme suivant
  **−1/135** (le tronqué SURESTIME), **sup = 0,376730 en x = 2,7437** donc
  < 0,5 avec confirmation asymptotique `cos²x/3 ≤ 1/3` ⟹ **régime (A) pour
  tout kη** ; le « basculement à kη ≈ 1,9 » est l'**artefact exact** du
  tronqué, qui atteint 0,5 en `13,5^(1/4) = 1,9168` ; au pic CGB
  `5,956·10⁻²⁹`.
- **F1** : rapport Sp(N)/programme = **π²/8 = 1,2337**, ≠ 1 et > 1.
- **F2** : exposant du plancher Einstein = **−2** exact.
- **F4** : argmin en w=0 pour six functionals croissants, **cassure sur
  `(w−1)²`** ⟹ circularité de la voie entropie-de-Weyl établie ET sa
  contingence à la monotonie exhibée.
- **F5** : `A_T·N` indépendant de ℓ **et de d** ⟹ identité ∀ d ; coefficient
  O(1) laissé LIBRE et vérifié non résolu (garde-fou anti-surclassement).
- **F6** : Hessien covariant symétrique/sans trace sur fond **Nil** (non plat),
  `R[Nil] = −1/2` et `Cotton[Nil] ≠ 0` redérivés (recoupe R-7/Q6, R-9/A5-A6) ;
  parité paire de Δσ vs impaire de l'objet à un epsilon ⟹ secteurs disjoints.
- **Transverse** : aucun front n'est de niveau « réduction » ⟹
  **{A4 ; A2★ ; N} INCHANGÉ**.

**Consignations de fond, à ne pas perdre :**

- **(a) Tension interne entre deux têtes du dépôt** : la tête F2 porte
  `f^ttt_NL = 900 ± 700` comme lecture de 2312.12498 Table II ; la tête F5
  v0.3 (correctif R-23) déclare ce chiffre **NON LITTÉRAL dans la source**,
  caractérisation approximative d'un σ = O(500). Les deux COEXISTENT au dépôt.
  **Consignée, NON arbitrée** (corps fermés). Point de reprise réel pour qui
  rouvrira F2 ou F5.
- **(b) F3-2 est borné** : non-appartenance à la famille G₂ ADAPTÉE au couple
  (∂_y,∂_z) ; n'exclut pas un autre couple de Killing commutants. Suffisant
  pour la conclusion, insuffisant comme théorème de classification.
- **(c) T-2 invérifiable par construction** : « branche entièrement épuisée »
  est un constat de NON-EXISTENCE. On ne prouve pas une absence par sympy.
- **(d) W1 (WCH-CANCELLATION) intégralement consigné, ZÉRO PASS revendiqué** —
  le contenu discriminant vit au corps, fermé.
- **(e)** Le dictionnaire `⟨T⟩=(d/16πG)g₃`, `Ω^𝒯=Weyl⊕Cotton` (BEG) et W2
  (hérité de R-7) sont des IMPORTS, non redérivés.

## 4. Discipline en vigueur (inchangée + précédents S9)

Discipline amendée post-CSE, précédents S4–S8 : **tous maintenus**.
Précédents **S9** opposables :

- **Un défaut du gel se NOMME et s'amende par fichier séparé daté, jamais en
  place.** Le gel reste byte-intact et re-vérifiable après dérivation ;
  l'amendement porte son propre sha ; l'antériorité reste auditable.
- **Un harnais doit auditer la VACUITÉ STRUCTURELLE, pas seulement muter.**
  Un assert qu'aucun porteur ne traverse est un faux PASS, même s'il est vrai.
  L'audit de vacuité a rendu quatre faux PASS sur un lot qui se présentait à
  38/38 — sans lui, le lot aurait été clos surévalué.
- **Un pré-tri [D]/[C] au gel interdit le reclassement après coup.** Trier
  discriminant vs consignation AVANT de savoir ce qui passera empêche de
  requalifier un échec en consignation.
- **L'antériorité se PROUVE par l'état du répertoire, pas par une
  déclaration** : relever le sha du gel quand aucun instrument n'existe
  encore, et le listing l'atteste.
- **Une cible non algébrisable se déclare telle AU GEL** (clause I-c), sinon
  elle devient une recopie de front-matter déguisée en PASS.

## 5. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus, 12 redemo, 271/101).
2. **Le Silo R est CLOS.** Aucun lot de redémonstration ne reste. Le prochain
   geste relève entièrement d'un ARBITRAGE OPÉRATEUR, non d'une suite
   mécanique.
3. Voies ouvertes, aucune ne s'ouvre sans décision explicite :
   - **Silo P** : β / P-1 (cartographie v1.2 : β#1 maintenu) vs report
     modulaire d = 3 / P-3 (recommandation #1 des decks). Tracker R-53 : 0/4.
   - **Soldes de gouvernance** : G-4 (autorité mount vs git — hypothèse
     reconduite : mount autoritaire R-54, git miroir) ; solde G-1 (les
     16 bundles de la décharge v2.74, 72 .py ; hors-KB/A/ non fourni) ;
     G-5b/c (index `LC-00-INDEX`, arborescence des silos) ; PDF du mount
     (5014 Ko) vs `sources/2503_19957v1.pdf`, confrontation non exécutée.
   - **Réouverture ciblée** possible sur F2/F5 au vu de la consignation (a).

## 6. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, dépôt `LC_Raccord` seul, Contents R/W,
  courte durée) — à fournir seulement une fois l'exécuteur confirmé vivant et
  les sha annoncés. **Le token de S9 est à RÉVOQUER après la campagne de
  dépôts S9.**
- **AUCUN intrant requis** pour le §0-lite ni pour les soldes de gouvernance.
- **Une seule instance à la fois** sur le dépôt.
- Pour le solde G-1 : les bundles v2.74, si ré-import décidé.

## 7. Périmètre — INCHANGÉ

`{ A4 ; A2★ ; N }` INCHANGÉ · **Silo R clos à 12/12 sans retirer une seule
inconnue** — c'est exactement ce que la cible transverse T-1 de R-11 a
vérifié, et c'est le résultat le plus important de S9 · branche
FALSIFIABILITÉ épuisée = constat de NON-EXISTENCE d'un front borné restant,
non un acquis · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON réfuté, postulat
RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non clos · N non fixé
(≡Λ, R-53 : 0/4) · O₂ non construit (β ≡ G3 seul facteur ouvert) · nœud (i)
INDÉTERMINÉ (pas A) · **CCC non démontrée NI réfutée**.

*§6.4 — sentinelle terminale. Dériver, muter, rejouer, corriger un
instrument, clore un silo et déposer un rapport : aucun de ces gestes ne
scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
