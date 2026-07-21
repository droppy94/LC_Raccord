---
id: NOTE-REPRISE-GIT-S2
titre: "Note de reprise autoportante — fin de session S2 (2026-07-21) : G-3 soldé (83 sceaux rejoués), Silo R ouvert (R-4 et R-5 REPRODUIT-SOUS-RÉSERVE), réserve d'aveuglement partiel consignée. Prochain geste : CSE incognito à froid sur R-4/R-5, PUIS R-3/R-6, en session NEUVE."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-21
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S2 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S2 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -6      # attendu : HEAD = « Reprise S2 … », puis « R-5 : … » (+ réserve),
                              #           b2c6567 (R-4), 695fb05 (G-3), 6290140 (Reprise S1), f8caccb
    ls instruments/*.py | wc -l               # attendu : 18 (15 de S1 + rejeu_sceaux + redemo_R4_CT + redemo_R5_reductions)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/                                 # attendu : INVENTAIRE-SCEAUX.md, REJEU-SCEAUX.md,
                                              #   rejeu_sceaux_resultats.json, R4-*, R5-*, RESERVE-AVEUGLEMENT-R4-R5.md
    python3 instruments/inventaire_sceaux.py  # attendu : 6 LIVE / 76 ARCHIVE / 1 ABSENT (requalifié)
    python3 instruments/run_sceau.py verif_paquet_propre   # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT.py       # attendu : 32/32 PASS, EXIT 0
    python3 instruments/redemo_R5_reductions.py  # attendu : 18/18 PASS, EXIT 0

Tout écart avec ces attendus est à décomposer AVANT de poursuivre
(leçon V62). LEÇON D'ENVIRONNEMENT S2, opposable : un processus détaché
au simple `nohup &` MEURT entre deux appels d'outil ; SEUL `setsid`
survit (constaté par test, leçon #2 confirmée sur pièce). Tout rejeu
long : `setsid nohup … &` puis poll.

## 1. Ce qui a été fait en S2 (sur GO opérateur, R-55 tenu)

1. **§0-lite S1 rejoué conforme** sur toute la ligne (aucun écart).
2. **G-3 SOLDÉ** (commit 695fb05) : `instruments/rejeu_sceaux.py`
   (harnais, 3 classes, 3 issues), `audit/REJEU-SCEAUX.md` +
   `rejeu_sceaux_resultats.json`. **Résultat : 83 sceaux rejoués = 7
   LIVE + 76 ARCHIVE ; 82 RC0 ; 0 RC≠0 ; 1 INEXECUTABLE-ICI**
   (`verif_cartographie_v11_nonregression` : selftest firewall 7/7 PASS
   puis résolution de la tête v1.0 sur /mnt/project ⟹ délimitation
   d'environnement, pas un échec). Les 7 sceaux LIVE : sha8 TOUS égaux
   au §9ter du manifeste v2.124. Le Silo G est soldé sur ses gestes
   exécutables : G-0 ✓ G-1 ✓ G-2 ✓ G-3 ✓ G-5a ✓ ; restent G-4 et
   G-5b/c (décisions/cadrages opérateur).
3. **R-4 (C_T∝N, A_T·N=16)** (commit b2c6567) : gel de cible
   `audit/R4-CIBLES-GELEES.md` (sha 044dc749…, 13 cibles T1–T13, figé
   AVANT redérivation) ; `instruments/redemo_R4_CT.py` 32/32 PASS
   EXIT 0 (deux routes convergentes redérivées, firewalls mordants) ;
   7 sceaux du lot RC0 ; deux réconciliations consignées
   (représentation ±i de la carte S ; lecture « noyau de réponse » du
   garde-fou de signe). Rapport `audit/R4-REDEMONSTRATION.md`.
4. **R-5 (trois réductions ⟹ { A4 ; A2★ ; N })** : gel
   `audit/R5-CIBLES-GELEES.md` (sha 9b84e800…, P1–P7) ;
   `instruments/redemo_R5_reductions.py` 18/18 PASS EXIT 0 (g₃=−(i/3)k³g₀
   par série du mode BD ; Π^TT(isotrope)=0 explicite ; inclusion
   S_A4⊊S_A3 STRICTE par témoin ; k³, Δ=3, invariance ; résidu = UNE
   amplitude ; A_T·N=16 re-vérifié) ; P7 consigné comme RECOMBINAISON
   (pas d'algèbre neuve). Rapport `audit/R5-REDEMONSTRATION.md`.
5. **RÉSERVE D'AVEUGLEMENT PARTIEL — constat OPÉRATEUR, consigné contre
   le pilote** : `audit/RESERVE-AVEUGLEMENT-R4-R5.md`. Les front-matters
   (source du gel) portent le MÉCANISME, pas seulement les cibles ⟹ la
   « dérivation aveugle » était GUIDÉE. **Les grades R-4 et R-5 se
   lisent REPRODUIT-SOUS-RÉSERVE.** Rapports antérieurs NON réécrits
   (historique jamais réécrit) ; la réserve fait foi en aval. Limite
   structurelle du §2.0 nommée ; correctif = adjudicateur externe.
6. Le commit qui dépose la présente note (swap −S1 +S2, S1 conservée
   par l'historique git).

**Bilan Silo R : R-4 ✓ R-5 ✓ (tous deux SOUS-RÉSERVE, adjudication
pendante) ; R-1, R-2, R-3, R-6…R-12 non ouverts.**

## 2. Décisions opérateur ACTÉES en S2

- GO G-3 (dépôt 695fb05) ; GO R-4 (b2c6567) ; GO de clôture S2
  (lot R-5 + réserve + la présente note — lu de l'instruction
  opérateur « fait tout le nécessaire », fichiers annoncés inchangés).
- La réserve d'aveuglement est un CONSTAT OPÉRATEUR ⟹ la passe CSE
  incognito (§3 de la réserve) est PRESCRITE, pas optionnelle.

## 3. Décisions opérateur EN ATTENTE (inchangées de S1 + une neuve)

- **G-4** : autorité mount vs git (hypothèse de travail : mount
  autoritaire R-54, git miroir).
- **Priorisation de substance** : β/P-1 (cartographie v1.2 : β#1
  maintenu) vs report modulaire d=3/P-3 (recommandation #1 des decks).
- **PDF du mount** (5014 Ko) : confrontation à sources/2503_19957v1.pdf
  si retrouvé.
- **NEUVE — issue du CSE R-4/R-5** : l'espace {E-1 ; E-2 ; E-3} de la
  réserve sera adjugé par l'incognito ; le pilote consigne, ne re-juge
  pas.

## 4. PROCHAIN GESTE — ordre imposé de la session neuve

1. **§0-lite du dépôt** (attendus §0 ci-dessus).
2. **CSE INCOGNITO À FROID sur R-4/R-5** — spec dans
   `audit/RESERVE-AVEUGLEMENT-R4-R5.md` §3 : geler l'espace-verdict
   {E-1 ; E-2 ; E-3} AVANT expédition (R-36, sha au bloc écrits par
   script), joindre les 7 pièces nommées, conjecture du pilote
   déclarée, incognito souverain, rapport HORS-KB opérateur + chaînon
   de consignation au dépôt sur GO. AUCUN lot R-n de substance ne
   s'ouvre AVANT cette issue (elle peut requalifier la méthode des
   lots suivants).
3. **PUIS Silo R, ordre du lotissement** : **R-3** (spectre k³ — cibles
   propres : relation BD complète, oracle ; la forme k³ est déjà
   pré-couverte par R-5/P4, à consigner sans double compte) puis
   **R-6** (⟨TTT⟩, verrou 4-pt ∝N⁻³ — sceaux verif_D_nongauss_TTT +
   variantes, en ARCHIVE, RC0 au harnais G-3). Chaque lot : cycle
   §2.0 complet, EN INTÉGRANT la leçon de la réserve (le gel nomme
   désormais explicitement ce que le front-matter révèle du mécanisme).
4. Silos P/V/X : inchangés (P-3 report d=3 recommandé #1 des decks,
   priorisation opérateur ; tracker R-53 : 0/4).

## 5. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, repo LC_Raccord seul, Contents
  R/W, courte durée) au premier message. Le token de S2 a servi aux
  pushes de cette session et RESTE LISIBLE dans la conversation S2 ⟹
  À RÉVOQUER dès maintenant. Sans token : tout reste faisable en
  local, seuls les pushes attendent.
- Aucun autre intrant requis pour le CSE (les pièces sont au dépôt).

## 6. Garde-fou terminal (§6.4)

Rejouer 83 sceaux, redémontrer deux lots, consigner une réserve,
prescrire un audit : AUCUN de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. REPRODUIT-SOUS-RÉSERVE n'est pas
« établi davantage » — c'est un grade DIMINUÉ en attente d'adjudication.
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) ·
O₂ non construit · β T-b seul facteur d'O₂ ouvert · nœud (i) INDÉTERMINÉ
(pas A) · A4 route par-ℐ⁺ délimitée (W2), postulat renforcé, non
réfuté · A2★ parqué · CCC non démontrée NI réfutée.
