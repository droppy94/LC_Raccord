---
id: NOTE-REPRISE-GIT-S3
titre: "Note de reprise autoportante — fin de session S3 (2026-07-21) : CSE incognito adjugé E-3 (verdict consigné verbatim), instruction R-4b/R-5b soldée, lot R-3 clos (REPRODUIT-SOUS-RÉSERVE E-2, noyau f_b²/3x³ reconstruit), gel R-6 déposé. Prochain geste : redérivation R-6 en session NEUVE sur cibles déjà gelées."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-21
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S3 » ; le vérifier par git log, jamais par cette note."
---

# Note de reprise S3 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -7   # attendu : HEAD = « Reprise S3 … », puis f7c77eb (R-3),
                           #   b803f55 (R-4b/R-5b), 2062531 (CSE E-3), e994850 (Reprise S2),
                           #   544adcf (R-5), b2c6567 (R-4)
    ls instruments/*.py | wc -l                    # attendu : 22
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/   # attendu : + CSE-R4R5-GEL.md, CSE-R4R5-VERDICT.md,
                #   R4b-R5b-INSTRUCTION.md, R3-CIBLES-GELEES.md,
                #   R3-REDEMONSTRATION.md, R6-CIBLES-GELEES.md
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py          # attendu : 35/35 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R5_reductions_b.py  # attendu : 17/17 PASS + 5 consignations, EXIT 0
    python3 instruments/redemo_R3_spectre.py       # attendu : 16/16 PASS + 6 consignations, EXIT 0

Tout écart est à décomposer AVANT de poursuivre (leçon V62). Leçon
d'environnement S2 toujours opposable : rejeu long = `setsid nohup … &`
puis poll (un simple `nohup &` meurt entre appels d'outil).

## 1. Ce qui a été fait en S3 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S2 rejoué conforme** sur toute la ligne.
2. **CSE INCOGNITO À FROID sur R-4/R-5 — ADJUGÉ** (le geste prescrit
   par la note S2). Gel d'expédition AVANT expédition
   (`audit/CSE-R4R5-GEL.md` + `instruments/cse_gel_expedition.py`,
   R-36 : sha du gel consigné hors-fichier en session). Route :
   incognito MAXIMAL (conversation neuve hors projet, sans mount ni
   mémoire — confirmé opérateur). **VERDICT : E-3 — DÉFAUT
   SUBSTANTIEL**, contre la conjecture du pilote, consigné VERBATIM
   (`audit/CSE-R4R5-VERDICT.md`, commit 2062531). L'auditeur a rejoué
   les instruments, recalculé les 7 sha (7/7 MATCH), exécuté des sondes
   adverses, et nommé : 6 tautologies/paraphrases (R-4), 7
   tautologies/consignations non déclarées (R-5), 8 défauts de
   rédaction favorisant E-1. L'incognito prévaut ; le pilote a
   consigné, pas re-jugé.
3. **INSTRUCTION R-4b/R-5b SOLDÉE** (commit b803f55) : instruments
   amendés `redemo_R4_CT_b.py` (35/35 PASS discriminants + 5
   consignations) et `redemo_R5_reductions_b.py` (17/17 + 5), rapport
   `audit/R4b-R5b-INSTRUCTION.md` (table défaut→correctif, traitement
   des 8 consignations mandatées). v1 conservés au dépôt, remplacés EN
   AVAL. **Grades en vigueur : R-4 et R-5 = REPRODUIT-SOUS-RÉSERVE au
   sens E-2 (reproduction guidée). JAMAIS E-1.**
4. **LOT R-3 CLOS** (commit f7c77eb) : gel `audit/R3-CIBLES-GELEES.md`
   (sha eded7406…, déclaration de révélation du mécanisme, plafond E-2
   annoncé AU GEL) ; `instruments/redemo_R3_spectre.py` 16/16 PASS + 6
   consignations, EXIT 0 ; rapport `audit/R3-REDEMONSTRATION.md`.
   Pièce centrale : le NOYAU EXACT de variance, seule pièce non
   révélée, reconstruit en quasi-aveugle — **K(x)=f_b(x)²/(3x³)**
   (f_b = partenaire dual du mode BD dans le doublet S1 de R-4), 3
   candidats, adjugé par 5 contraintes gelées ; écart
   β∞ = 3,0·10⁻⁵ NOMMÉ, BORNÉ, NON CORRIGÉ (anti-fit) ; 1 correction
   d'instrument (quadrature oscillante) consignée. Sceaux ARCHIVE
   rejoués : verif_D3_spectre_k3 (706e97cc) rc=0,
   verif_D3_bunchdavies (7f269735) rc=0.
   **Grade : REPRODUIT-SOUS-RÉSERVE (E-2 ; écart β∞ nommé borné).**
5. **GEL R-6 DÉPOSÉ** (`audit/R6-CIBLES-GELEES.md`, ce commit) :
   cibles Q1–Q10 (3-pt ⟨TTT⟩ + verrou 4-pt ∝N⁻³) figées depuis les
   front-matters SEULS, en FIN de session — la redérivation s'ouvrira
   en session neuve (gel précédant la session de dérivation =
   anti-fit renforcé). Révélation déclarée : chaîne interne ENTIÈRE
   révélée ⟹ plafond E-2 ; contenu discriminant attendu = moteur de
   moments gaussien générique + compositions de dictionnaire +
   catalogue γ ; comptages et fetchs externes = IMPORTS consignés.
6. Le commit qui dépose la présente note (swap −S2 +S3 ; S1 et S2
   restent dans l'historique git).

**Bilan Silo R : R-3 ✓ R-4 ✓ R-5 ✓ (tous REPRODUIT-SOUS-RÉSERVE au
sens E-2, adjudication CSE faite) ; R-6 GELÉ, non redérivé ;
R-1, R-2, R-7…R-12 non ouverts.**

## 2. Discipline AMENDÉE en vigueur (issue du CSE, opposable à tout lot)

- Harnais à deux issues : PASS (discriminant : calcule, et une
  mutation le fait échouer) / CONSIGNATION (import, trivialité,
  non-dérivable — déclarée, HORS décompte). Seuls les PASS s'agrègent.
- Aucune disjonction rendant un assert infaillible.
- Le gel DÉCLARE ce que le front-matter révèle du mécanisme et annonce
  le plafond de grade AU GEL.
- Tout espace-verdict est vérifié contre les pièces du paquet AVANT
  gel (pas d'issue morte-née).
- « Premier passage sans correction » ne se présente pas comme force ;
  les corrections d'instrument en cours de lot se consignent.
- Écart numérique vs cible : nommé, borné, JAMAIS résorbé par
  ajustement (anti-fit) ; tolérances déclarées AVANT comparaison.

## 3. Décisions opérateur EN ATTENTE (inchangées)

- **G-4** : autorité mount vs git (hypothèse de travail : mount
  autoritaire R-54, git miroir — reconduite cette session).
- **Priorisation de substance** : β/P-1 vs report modulaire d=3/P-3.
- **PDF du mount** (5014 Ko) : confrontation à sources/2503_19957v1.pdf.
- G-5b/c (index, arborescence silos) : cadrages non exécutés.

## 4. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus).
2. **R-6 — redérivation** sur les cibles DÉJÀ GELÉES
   (`audit/R6-CIBLES-GELEES.md` ; ne pas re-geler, ne pas amender le
   gel) : instrument `redemo_R6_nongauss.py` sous discipline amendée ;
   rejeu de confirmation des sceaux du lot (TTT + variantes + phase1
   1aa3f051) — GO opérateur à demander ; les canaris lourds via
   `setsid`. Rapport + grade (plafond E-2 déjà annoncé).
3. **PUIS** R-2/R-12 (racines D1/O₂ du front vif) selon l'ordre du
   lotissement, un lot = un cycle §2.0 amendé complet.
4. Silos P/V/X : inchangés (P-3 report d=3 recommandé #1 des decks ;
   tracker R-53 : 0/4).

## 5. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, repo LC_Raccord seul, Contents
  R/W, courte durée) au premier message. Le token de S3 a servi aux
  pushes de cette session et RESTE LISIBLE dans la conversation S3 ⟹
  À RÉVOQUER dès maintenant. Sans token : tout reste faisable en
  local, seuls les pushes attendent.
- Aucun autre intrant requis pour R-6 (gel et sceaux au dépôt).

## 6. Garde-fou terminal (§6.4)

Adjuger un CSE, instruire un verdict, clore un lot, geler le suivant :
AUCUN de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi
que ce soit. REPRODUIT-SOUS-RÉSERVE (E-2) est un grade DIMINUÉ — une
reproduction guidée, pas une corroboration indépendante.
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) ·
O₂ non construit · β T-b seul facteur d'O₂ ouvert · nœud (i) INDÉTERMINÉ
(pas A) · A4 route par-ℐ⁺ délimitée, non réfuté · A2★ parqué · CCC non
démontrée NI réfutée.
