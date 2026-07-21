---
id: NOTE-REPRISE-GIT-S1
titre: "Note de reprise autoportante — campagne de fiabilisation du dépôt git LC_Raccord, fin de session S1 (2026-07-21). Prochain geste : G-3 (harnais de rejeu complet), en session NEUVE."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-21
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose (son dépôt le crée). Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S1 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S1 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (l'équivalent §0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -8                      # attendu : HEAD = « Reprise S1 … », puis f8caccb, 89660d4, 365856b, e754c63, 7ec9d73, 7be89e1
    ls instruments/*.py | wc -l               # attendu : 15 (13 d'origine + inventaire_sceaux + run_sceau)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls sources/                               # attendu : 2503_19957v1.pdf + README.md
    python3 instruments/inventaire_sceaux.py  # attendu : 83 = 6 LIVE / 76 ARCHIVE / 1 ABSENT (requalifié)
    python3 instruments/run_sceau.py verif_paquet_propre   # attendu : sha8=051e2833 rc=0

Tout écart avec ces attendus est à décomposer AVANT de poursuivre (leçon V62 :
aucune valeur projetée n'est inscrite comme acquise).

## 1. Ce qui a été fait en S1 (six commits, tous poussés sur main)

1. `7ec9d73` — **G-1** : ré-import des 72 .py déchargés (v2.74) sous nom
   canonique dans `instruments/archives-scelees/`, gate d'intégrité 72/72
   byte-exact contre `INDEX-DECHARGE-72.txt`, re-vérifiés post-copie, 0
   collision avec les sceaux LIVE. + **G-0** : `inventaire_sceaux.py`
   (rejouable) et `audit/INVENTAIRE-SCEAUX.md`. + dépôt du **lotissement**
   `LC-WORK-LOTISSEMENT-SILOS-v0.1.md` (racine) — silos R/P/V/X/G.
2. `e754c63` — **G-1 suite** : 4 sceaux retrouvés (apport opérateur),
   rejoués verts : `verif_D_nongauss_4pt_phase1` (1aa3f051, EXIT 0) ·
   `verif_G3_admissibilite` (010a0562, v2 DURCI, ALL PASSED) ·
   `verif_cartographie_v11_nonregression` (81e1914b, selftest 7/7) ·
   `verif_manifeste_v2122_consignation` (5349ad47, selftest OK ; exécution
   pleine = mount). 4 doublons byte-exact consignés SANS dépôt, dont
   l'oracle `__2_` ≡ LIVE `162696c1` (= sha8 du manifeste, confirmé).
3. `365856b` — **Requalification opérateur (GO 2026-07-21)** :
   `verif_D3_P6_bang.py` = « annoncé, jamais écrit, remplacé par la chaîne
   specA/specB ». Consignée au README des archives.
4. `89660d4` — **G-5a** : dépôt `sources/2503_19957v1.pdf` (KPS, 889 Ko,
   sha256 113ab4a2…). Identité de CONTENU confirmée (titre, 3 auteurs,
   arXiv:2503.19957v1, 22 pages = OCR J3, D-09 concordant) ; identité
   d'OCTETS avec le PDF du mount (5014 Ko, retiré V95) NON établie — écart
   consigné, règle contenu-pas-hash (précédent Garfinkle, 04_references
   v1.21). Solde côté git la dette « différence à nommer » (v2.121).
5. `f8caccb` — **G-2** : constat que les sceaux résolvent la KB
   relativement au cwd (convention mount, layout plat) ⟹ correctif par
   LANCEUR `instruments/run_sceau.py` (cwd = kb/, LC_KB_ROOT overridable),
   ZÉRO octet de sceau modifié. Validation : `verif_paquet_propre`
   sha8 051e2833 rc 0 · `verif_A4_QW` sha8 a4637a2c rc 0 — **sha8 ÉGAUX au
   §9ter du manifeste** (miroir byte-conforme) · un ARCHIVE rc 0 · erreur
   propre sur sceau inexistant. Doc : `instruments/README-REJEU.md`.
6. Le commit qui dépose la présente note.

**Bilan sceaux : 83 cités = 6 LIVE + 76 ARCHIVE + 1 requalifié (P6-bang,
jamais écrit). ZÉRO vrai manquant.** Silo G : G-0 ✓ G-1 ✓ G-2 ✓ G-5a ✓.

## 2. Décisions opérateur ACTÉES en S1

- **P6-bang requalifié** (« annoncé, jamais écrit ») — GO du 2026-07-21.
- **Hypothèse de travail G-4 en vigueur, non encore actée formellement** :
  le mount reste autoritaire (R-54), le git est miroir vérifiable.

## 3. Décisions opérateur EN ATTENTE

- **G-4** : acter (ou renverser) l'autorité mount vs git.
- **Priorisation de substance** : β / P-1 (cartographie v1.2 : β#1 maintenu)
  vs report modulaire d=3 / P-3 (recommandation #1 des decks).
- **PDF du mount** : si la copie 5014 Ko (avec couche OCR probable) est
  retrouvée un jour, la confronter à `sources/2503_19957v1.pdf` (889 Ko)
  fermerait l'écart d'octets consigné au `sources/README.md`.

## 4. PROCHAIN GESTE — G-3 : harnais de rejeu complet (spec figée S1)

Motif du report : session S1 à charge de contexte élevée ; G-3 = canaris
≥ 600 s + rapport — profil exact de l'incident V85. Le dépôt précède la
consignation ; on ouvre G-3 en session NEUVE.

Spécification (à instancier telle quelle, ajustements consignés) :

- **G-3a — instrument** : `instruments/rejeu_sceaux.py` s'appuyant sur
  `run_sceau.py`. Trois classes d'exécution : (i) **LIVE rapides**
  (`verif_paquet_propre` 051e2833, `verif_A4_QW` a4637a2c,
  `verif_A4_QW_typeI_succ` 79f09a8c) ; (ii) **canaris lourds** en tâche
  longue, timeout ≥ 900 s chacun (`verif_nonlin_parity` 9df8e53e,
  `verif_D3_P6_specB_oracle` 162696c1, `verif_A2_numerique` 76e9257c,
  `diag_bounces` 804b7f9b) ; (iii) **ARCHIVES** : rejeu opportuniste,
  timeout court (120 s), avec trois issues par sceau — rc 0 / rc ≠ 0 /
  INEXÉCUTABLE-ICI (dépendance mount, réseau coupé, ou timeout) — la
  troisième N'EST PAS un échec, c'est une délimitation d'environnement.
- **G-3b — rapport** : `audit/REJEU-SCEAUX.md` généré par le script :
  par sceau → zone, sha8, rc, durée, issue ; en tête → bilan et sha8
  confrontés au §9ter pour les 7 sceaux LIVE du manifeste.
- **G-3c — grade, à ne jamais surclasser** : un rc 0 sur le clone atteste
  UNE exécution sur CE clone à CETTE date. Il ne rejoue aucune gate, ne
  requalifie aucun grade du mount, ne re-scelle rien. Un rc ≠ 0 sur une
  ARCHIVE se consigne et s'instruit au lot R-n correspondant — il ne
  « casse » rien par lui-même.
- **Ordre d'exécution recommandé** : §0-lite du dépôt (attendus §0
  ci-dessus) → G-3a/b (rapides, puis canaris détachés, puis archives) →
  commit du rapport → PUIS ouverture du Silo R par **R-4 (C_T ∝ N)** :
  sceaux `verif_D_CT_ATN` + `verif_D_CT_dual*` + `verif_D_CT_realite` +
  `verif_D_CT_gardefou_dS`, tous en ARCHIVE, protocole §2.0 du lotissement
  (cible gelée AVANT relecture → redérivation → confrontation).

## 5. Intrants à fournir en session neuve

- **Token GitHub** : celui de S1 a servi à 6 pushes et reste lisible dans
  la conversation S1 ⟹ à RÉVOQUER après S1 ; en fournir un NEUF (fine-
  grained, repo LC_Raccord seul, Contents R/W, courte durée) au premier
  message de la session de reprise. Sans token : tout reste faisable en
  local, seuls les pushes attendent.
- Aucun autre intrant requis pour G-3.

## 6. Garde-fou terminal (§6.4)

Ré-importer, inventorier, lancer, rapporter, reprendre : AUCUN de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) ·
O₂ non construit · β T-b seul facteur d'O₂ ouvert · nœud (i) INDÉTERMINÉ
(pas A) · A4 route par-ℐ⁺ délimitée (W2), postulat renforcé, non réfuté ·
A2★ parqué · CCC non démontrée NI réfutée.
