---
id: NOTE-REPRISE-GIT-S8
titre: "Note de reprise autoportante — fin de session S8 (2026-07-22) : lot R-9 dérivé, clos et déposé (REPRODUIT-SOUS-RÉSERVE E-2, plafond du gel atteint non dépassé). Tranche [B] hors-KB DÉPOSÉE au git (G-1, hors-KB/B/, 4 pièces). Silo R à 11/12. Reste : R-11, intégralement autoportant depuis le git. Prochain geste : R-11, ou arbitrage Silo P."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-22
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S8 » ; le vérifier par git log, JAMAIS par cette note."
---

# Note de reprise S8 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -4   # attendu : HEAD = « Reprise S8 … », puis les deux
                           #   commits S8 (hors-KB [B] ; lot R-9), puis
                           #   6001027 (« Reprise S7 … »)
    ls instruments/*.py | wc -l                    # attendu : 31 (29 en S7,
                                                   #   + redemo_R9_tracteur.py
                                                   #   + harnais_R9.py)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 29 (27 en S7,
                                                   #   + gel + rapport R-9)
    ls kb/*.md | wc -l                             # attendu : 215
    ls hors-KB/B/ | wc -l                          # attendu : 4  (NOUVEAU S8)
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE / 76
                                                   #   ARCHIVE / 1 ABSENT —
                                                   #   MESURÉ INCHANGÉ en S8 :
                                                   #   l'inventaire ne balaye
                                                   #   pas hors-KB/
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py          # attendu : 35/35 PASS +  5 consignations
    python3 instruments/redemo_R5_reductions_b.py  # attendu : 17/17 PASS +  5 consignations
    python3 instruments/redemo_R3_spectre.py       # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R6_nongauss.py      # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R2_D1.py            # attendu : 12/12 PASS +  8 consignations
    python3 instruments/redemo_R12_O2.py           # attendu : 11/11 PASS +  7 consignations
    python3 instruments/redemo_R1_moduleA.py       # attendu :   6/6 PASS +  3 consignations
    python3 instruments/redemo_R8_A2star.py        # attendu : 21/21 PASS + 10 consignations
    python3 instruments/redemo_R10_nonlin.py       # attendu : 40/40 PASS + 14 consignations
    python3 instruments/redemo_R7_A4QW.py          # attendu : 45/45 PASS + 10 consignations
    python3 instruments/redemo_R9_tracteur.py      # attendu : 16/16 PASS +  8 consignations
                                                   #   (NOUVEAU S8 ; sympy seul)

**Total attendu : 235/235 PASS + 82 consignations, 11/11 rc = 0.**

**L'addition est DÉCOMPOSÉE, pas supposée** — exécutée d'un bloc en S8
sur l'arbre de dépôt, et recomptée indépendamment par grep des
marqueurs dans les logs :

    PASS  : 35 + 17 + 16 + 16 + 12 + 11 + 6 + 21 + 40 + 45 + 16 = 235
    CONS. :  5 +  5 +  6 +  6 +  8 +  7 + 3 + 10 + 14 + 10 +  8 =  82

Hors compte §0-lite, deux rejeux de confirmation disponibles :

    python3 instruments/harnais_R9.py              # attendu : « HARNAIS R-9 :
                                                   #   6/6 mordantes », rc=0
                                                   #   (format de sortie propre,
                                                   #   PAS compté dans 235/82)
    cd hors-KB/B && python3 verif_B_tracteur.py    # attendu : rc=0,
                                                   #   sha8=8e386686

Tout écart est à décomposer AVANT de poursuivre (leçon V62) : d'abord
l'addition, puis le lot divergent, puis l'assert.

### Leçons d'environnement opposables

Toutes celles de S2–S7 MAINTENUES (rejeu long en `setsid nohup` ;
répertoire de logs créé en appel séparé ; repli `origin/main` pour la
vérification de push ; `ls audit/` et non `ls audit/*.md` ;
`verif_D3_P6_specB_oracle` ≈130 s, `verif_nonlin_cotton` ≈139 s,
`verif_nonlin_parity` ≈308 s canari ; jamais deux sceaux en concurrence
dans le même arbre ; `pgrep -f` s'auto-matche — sonder par
`ps -eo pid,etime,cmd | grep "[p]ython3"` ; les durées ne se reportent
pas ; branche `origin/front-pq` résiduelle bénigne, ne pas toucher).

**Écart d'arbre bénin, récurrent et attendu** : `inventaire_sceaux.py`
réécrit sa ligne de date (bilan identique 6/76/1) ; restaurer par
`git checkout -- audit/INVENTAIRE-SCEAUX.md`.

**NOUVEAU S8 — deux formats de marqueur coexistent.** La plupart des
redemo impriment `[PASS]` / `[CONSIGNATION]` (crochets) ;
`redemo_R6_nongauss.py` imprime `PASS` / `CONSIGNATION` (tabulaire,
sans crochets). Le recompte indépendant DOIT tolérer les deux formats
(motif `^\s*\[?PASS\]?` et son pendant), sinon un lot conforme apparaît
à 0/0 — écart de COMPTEUR, pas de dépôt (décomposé et clos en S8, §1).

## 1. Ce qui a été fait en S8 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S7 rejoué CONFORME** sur toute la ligne : 219/219 PASS,
   74 consignations, 10/10 rc = 0, HEAD `6001027` et comptes exacts.
   Un écart rencontré et décomposé côté compteur de session (formats de
   marqueur, §0 ci-dessus) — aucun écart du dépôt.
2. **LOT R-9 DÉRIVÉ ET CLOS.** Archive [B] refournie, sha256 vérifié
   AVANT extraction (`b0ea7a7d…5333f`, 14110 octets), 4 pièces
   concordantes au registre S7 (4/4 : sha32, octets, lignes),
   quarantaine hors dépôt. **Corps des deux têtes JAMAIS ouverts**
   (RESULTAT l.14–230 ; PAQUET l.13–183) ; `verif_B_tracteur.py`
   JAMAIS lu (rejoué par exécution seule) ; **`REIMPORT.txt` lu APRÈS
   le gel** — décision S7 close, tenue et documentée. Gel
   `7018b47e…4f91d1` figé AVANT la première ligne d'instrument,
   **plafond E-2 annoncé AU GEL** (verdict révélé par deux canaux :
   lotissement v0.1 + front-matter RESULTAT). **16/16 PASS +
   8 consignations, rc 0, premier passage sans correction
   d'instrument.** Harnais **6/6 mutations mordantes** sur les porteurs
   identifiés. Sceau fourni rejoué **rc=0 sha8=8e386686** concordant.
   Grade **REPRODUIT-SOUS-RÉSERVE (E-2)**, plafond atteint non
   dépassé ; issue conforme ⟹ pas d'audit froid (§2.0-5).
3. **G-1 partiel EXÉCUTÉ : tranche [B] déposée au git** sous
   `hors-KB/B/` (les 4 pièces, byte-identiques à l'archive S7 ;
   arborescence conforme au « dossier froid hors-KB/B/ » que
   `REIMPORT.txt` décrit). Le mount RESTE autoritaire (R-54) ; le git
   est miroir. `LC-A-SURVIE-CONFORME` reste au mount (réimport partagé
   hors-KB/A/, non fourni — sans objet pour R-9, consigné).
4. Le commit qui dépose la présente note (swap −S7 +S8 ; S1–S7 restent
   dans l'historique git).

**Bilan Silo R : 11/12 lots clos — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓
R-6 ✓ R-7 ✓ R-8 ✓ R-9 ✓ R-10 ✓ R-12 ✓, TOUS au grade
REPRODUIT-SOUS-RÉSERVE (E-2). Reste : R-11 (gabarit lourd,
intégralement autoportant depuis le git — têtes F1–F6 + WCH et les
cinq sceaux ARCHIVE, mesuré en S7).**

## 2. Contenu de substance de R-9 — pour mémoire

- **A2 (le cœur)** : sur métrique 2D GÉNÉRIQUE (E,F,G fonctions
  libres), R_abcd = K(g_ac g_bd − g_ad g_bc) IDENTIQUEMENT (16/16
  composantes) ⟹ le Riemann 2D est pure courbure scalaire ⟹ aucun
  invariant conforme local intrinsèque. La généricité PORTE AUSSI le
  durcissement (B7) : aucune rondeur n'est utilisée.
- **A3** : comptage f(n)=n(n+1)(n+2)(n−3)/12 — f(3)=0, f(4)=10 ⟹ tout
  Weyl évalué sur S² est une donnée AMBIANTE (4D restreinte).
- **A4** : K[4/(1+r²)²δ]=1 EXACT (ronde conformément plate explicite).
- **A5/A6** : Cotton[e^{2φ}δ₃]=0 (27/27, famille 3-paramètres à
  troisièmes dérivées non triviales) avec FIREWALL Cotton[Nil]≠0 à
  R=−1/2 constant — recoupe R-7/Q6, redérivé indépendamment.
- **A7** : Ω^𝒯 = Weyl ⊕ Cotton (IMPORT BEG/Čap–Gover, jambes seules
  redérivées) ⟹ deux jambes nulles sur la classe plate ⟹ Ω^𝒯=0,
  Cartan-plat ⟹ **B-PAUVRE** (« zéro invariant local »).
- **A8** : firewall dimensionnel — en 4D le même argument CASSE
  (f(4)=10 : les perturbations portent du Weyl).

**Consignations de fond, à ne pas perdre :**

- **(a) Le témoin du résidu n'est PAS redérivé.** Le sceau porte
  Weyl(SdS)≠0 ; l'instrument S8 n'établit que la COHÉRENCE (résidu
  nécessairement ambiant) + le recoupement R-7/Q4. **B3 cohérent et
  recoupé, pas redémontré en substance.**
- **(b) Le critère strict n'est PAS confronté.** Il vit au corps non
  ouvert ; lu en S8 comme « zéro invariant local ». `REIMPORT.txt`
  (post-gel) confirme une nuance réelle : « connexion sans champ propre
  mais organisatrice de donnée libre » ≠ simple « connexion plate » —
  compatible, non identique. Déclencheur de réouverture (a) de la tête.
- **(c) TODO de durcissement de la tête NON exécuté** : Ω^𝒯
  composante-à-composante sur dS perturbé portant g₍₃₎ (déclencheur (b)
  de `REIMPORT.txt`) — exigerait le corps ; c'est la voie nommée pour
  passer de « borné » à « reproduit » si le lot devait être durci.
- **(d) REIMPORT.txt identifie le résidu à g₍₃₎** — cohérent avec la
  donnée libre de Friedrich (R-5/P1) et avec la bascule de charge vers
  l'ambiant et vers [C].

## 3. Discipline en vigueur (inchangée + précédents S8)

Discipline amendée post-CSE, précédents S4–S7 : **tous maintenus**.
Précédents **S8** opposables :

- **Un intrant refourni se confronte au registre AVANT extraction**
  (sha256 de l'archive), puis pièce par pièce (sha32/octets/lignes) —
  fait en S8, 4/4 concordant.
- **Une décision différée se tient telle qu'écrite** : `REIMPORT.txt`
  lu APRÈS le gel, jamais avant — exécutée et documentée au rapport.
- **Un recompte indépendant doit tolérer les formats de marqueur**
  (crochets et sans crochets) — ou les instruments futurs unifient leur
  format ; en attendant, le motif tolérant fait foi.
- **Un statut de présence se MESURE sur l'arbre modifié** avant
  d'écrire la note qui le déclare (inventaire 6/76/1 vérifié INCHANGÉ
  après dépôt de hors-KB/B/ — l'inventaire ne balaye pas hors-KB/).

## 4. Décisions opérateur EN ATTENTE

- **G-4** : autorité mount vs git (hypothèse reconduite : mount
  autoritaire R-54, git miroir vérifiable).
- **Priorisation de substance** : β / P-1 (cartographie v1.2 : β#1)
  vs report modulaire d = 3 / P-3 (recommandation #1 des decks).
- **PDF du mount** (5014 Ko) : confrontation à
  `sources/2503_19957v1.pdf` — non exécutée.
- **G-5b/c** : index `LC-00-INDEX`, arborescence des silos — cadrages
  non exécutés.
- **G-1 solde** : les 16 bundles de la décharge v2.74 (72 .py) — le
  ré-import global reste ouvert ; seule la tranche [B] est entrée
  (hors-KB/B/). hors-KB/A/ (LC-A-SURVIE-CONFORME) non fourni.

## 5. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus, 11 redemo, 235/82).
2. **R-11 — dernier lot du Silo R**, intégralement autoportant depuis
   le git (mesuré en S7 : 20 têtes F1–F6/WCH + les cinq sceaux en
   ARCHIVE — `verif_F1_spn`, `verif_F4_principiel`, `verif_F5_scaling`,
   `verif_F6_memoire_cisaillement`, `verif_D3_WCH_GWE`). AUCUN intrant
   requis. Gel de cible AVANT la première ligne d'instrument, corps NON
   ouverts, plafond annoncé au gel. Prévoir un lot LOURD (six axes
   F1–F6 + deux têtes WCH) — le gabarit le plus large du Silo R.
3. **Silos P/V/X : inchangés** (P-3 report d = 3 recommandé #1 des
   decks ; β#1 maintenu par la cartographie v1.2 ; la priorisation
   appartient à l'opérateur ; tracker R-53 : 0/4).

## 6. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, dépôt `LC_Raccord` seul,
  Contents R/W, courte durée) — à fournir seulement une fois
  l'exécuteur confirmé vivant et les sha annoncés. **Le token de S8 est
  à RÉVOQUER après la campagne de dépôts S8** (il a servi aux push S8
  et reste lisible en conversation).
- **AUCUN intrant requis pour R-11** (autoportant, mesuré).
- **Une seule instance à la fois** sur le dépôt.
- Pour le solde G-1 : les bundles v2.74, si ré-import décidé.

## 7. Périmètre — INCHANGÉ

`{ A4 ; A2★ ; N }` INCHANGÉ · **[B] = B-PAUVRE** : constat de
PAUVRETÉ (l'objet intrinsèque sur S² est le modèle plat ; la charge
bascule vers l'ambiant — g₍₃₎ — et vers [C]), **pas une brique de
démonstration** ; résidu = Weyl rescalé, cohérent et recoupé (R-7/Q4),
non redémontré en substance ; critère strict et durcissement V98 non
confrontés (corps fermés) · W2 = DÉLIMITATION, A4 NON réfuté, postulat
RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 non clos · N non
fixé (≡Λ, R-53 : 0/4) · O₂ non construit (β ≡ G3 seul facteur ouvert) ·
nœud (i) INDÉTERMINÉ (pas A) · **CCC non démontrée NI réfutée**.

*§6.4 — sentinelle terminale. Dériver, muter, rejouer, déposer une
tranche hors-KB et consigner des réserves : aucun de ces gestes ne
scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
