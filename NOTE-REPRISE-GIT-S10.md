---
id: NOTE-REPRISE-GIT-S10
titre: "Note de reprise autoportante — fin de session S10 (2026-07-24) : VOLET 1 clos et déposé (adjudication documentaire F2/F5, VERDICT V6, grade CONSTAT SUR PIÈCES LOCALES). Volets 2 et 3 INTACTS, non entamés. Prochain geste : S11 s'ouvre sur l'ARBITRAGE DU SILO P, précédé d'une présentation atouts/inconvénients demandée par l'opérateur."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-24
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S10 » ; le vérifier par git log, JAMAIS par cette note."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise, au git comme au mount. Les notes S1–S9 sont retirées de la racine et vivent dans l'historique git. Tout ce qui n'est pas réalisé en reprise N est REPORTÉ en reprise N+1 — jamais laissé en coexistence."
autorite: "Pour les pièces de GOUVERNANCE (prompts d'ouverture, notes de reprise, amendements de l'un ou l'autre), le DÉPÔT GIT FAIT FOI. Le mount vaut copie de travail. Ceci ne tranche PAS G-4 : pour la KB scellée, le mount reste autoritaire (R-54) et le git reste miroir vérifiable."
---

# Note de reprise S10 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -9   # attendu : HEAD = « Reprise S10 … », puis
                           #   3419d49, ccceb6c, d43572a, 78e0ff3,
                           #   22a87c1, 9c22290, d093ae9, c683691
    ls instruments/*.py | wc -l                    # attendu : 33 (INCHANGÉ)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76 (INCHANGÉ)
    ls audit/ | wc -l                              # attendu : 36  <-- CHANGÉ
                                                   #   (32 en S9, + les 4 pièces
                                                   #    du volet 1 : gel,
                                                   #    2 amendements, note)
    ls kb/*.md | wc -l                             # attendu : 215 (INCHANGÉ)
    ls hors-KB/B/ | wc -l                          # attendu : 4 (INCHANGÉ)
    ls sources/ | wc -l                            # attendu : 4 (hors compte
                                                   #   §0-lite, pour mémoire)
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE /
                                                   #   76 ARCHIVE / 1 ABSENT
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

**Total attendu : 271/271 PASS + 101 consignations, 12/12 rc = 0. INCHANGÉ.**
Aucune des quatre pièces déposées en S10 n'est un instrument.

**L'addition est DÉCOMPOSÉE, pas supposée** — REJOUÉE en S10 sur clone neuf et
recomptée indépendamment par grep des marqueurs, lot par lot, chacun tombant
exactement sur son attendu :

    PASS  : 35 + 17 + 16 + 16 + 12 + 11 + 6 + 21 + 40 + 45 + 16 + 36 = 271
    CONS. :  5 +  5 +  6 +  6 +  8 +  7 + 3 + 10 + 14 + 10 +  8 + 19 = 101

Hors compte §0-lite, trois rejeux de confirmation, tous CONFORMES en S10 :

    python3 instruments/harnais_R9.py     # « HARNAIS R-9 : 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py    # « HARNAIS R-11 : 7/7 mordantes »
                                          #   + « aucun assert sans porteur mutable »
                                          #   + « VACANTES detectees : 0 », rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py    # rc=0, sha8=8e386686

Les cinq sceaux ARCHIVE de R-11, rejouables un par un (jamais deux dans le même
arbre), sha8 attendus : `verif_F1_spn` 19a4931e (20 assertions) ;
`verif_F4_principiel` 9947b8ed (25) ; `verif_F5_scaling` a959f137 (19) ;
`verif_F6_memoire_cisaillement` 23a7d264 (18) ; `verif_D3_WCH_GWE` 664660ee.

Tout écart est à décomposer AVANT de poursuivre (leçon V62) : d'abord
l'addition, puis le lot divergent, puis l'assert.

### Leçons d'environnement opposables

Toutes celles de S2–S9 MAINTENUES, et TOUTES REVÉRIFIÉES EN S10 :

- rejeu long en `setsid nohup` ; répertoire de logs créé en appel séparé ;
  repli `origin/main` pour la vérification de push ; `ls audit/` et non
  `ls audit/*.md` ; jamais deux sceaux en concurrence dans le même arbre ; les
  durées ne se reportent pas et ne sont pas des clés de sceau ; branche
  `origin/front-pq` résiduelle bénigne, ne pas toucher ;
- `inventaire_sceaux.py` réécrit sa ligne de date (bilan identique 6/76/1) ;
  restaurer par `git checkout -- audit/INVENTAIRE-SCEAUX.md`. **Survenu en S10.**
- **DEUX formats de marqueur** : `redemo_R6_nongauss.py` imprime sans crochets ;
  recompte au motif tolérant `^\s*\[?PASS\]?` et son pendant, sinon un lot
  conforme sort à 0/0. **Confirmé en S10** : le motif tolérant a bien rendu
  16/6 sur ce lot.
- `harnais_R11.py` crée `instruments/__pycache__/` (entrée NON SUIVIE, `?? `) ;
  `rm -rf instruments/__pycache__` après le rejeu. **Survenu en S10.**
- le motif `[p]ython3` ne protège PAS du shell englobant ; sonder dans un appel
  SÉPARÉ et court.
- un `simplify` non borné peut coûter 14 min là où substituer la contrainte
  d'abord coûte 1,6 s.

**NOUVELLES — S10, trois, toutes payées comptant :**

1. **La surface `/mnt/project` ne transporte PAS d'octets originaux pour les
   PDF.** Elle livre une archive ZIP de rendu page à page (une image JPEG par
   page, autant de `.txt` d'extraction, un `manifest.json`, AUCUNE entrée
   `.pdf`). La confrontation octet mount↔git y est **impossible par
   construction** pour ce type de fichier. Elle transporte en revanche
   byte-intactes 10 des 12 pièces texte communes vérifiées : la fidélité dépend
   du TYPE de fichier, pas du canal en bloc. Corollaire : **hacher un contenant
   n'est pas lire un contenu** — la confrontation d'un intrant ne demande
   AUCUNE lecture, et confondre les deux fait renoncer à une mesure disponible.
2. **Un bornage de lecture par numéro de ligne ou par fin de page ne borne
   rien.** En S10, DEUX débordements de périmètre successifs, le second APRÈS
   avoir écrit la correction : il faut détecter la **fin de légende**, et
   vérifier que l'implémentation applique bien la règle énoncée. Écrire la
   correction et ne pas l'appliquer est un échec d'exécution distinct du défaut
   d'énoncé, et il s'impute de la même façon.
3. **Un espace-verdict déclaré « exhaustif » doit prévoir la case « les deux
   parties ont tort ».** Le gel V1 déclarait son espace exhaustif et disjoint ;
   il n'avait pas de case pour la double inexactitude, et l'ordre de résolution
   figé y envoyait un cas que le libellé décrivait mal. Amendé par case V6.
   Introduire une case APRÈS des mesures est un risque de fit : il se **NOMME**,
   se borne par un critère général, et ne vaut que si l'issue écartée l'a été
   par MESURE et non par redéfinition.

## 1. Ce qui a été fait en S10 (sur GO opérateur, R-55 tenu)

1. **§0-lite S9 rejoué CONFORME sur toute la ligne** : 271/271 PASS, 101
   consignations, 12/12 rc = 0, comptes 33/76/32/215/4, inventaire 6/76/1,
   sceau 051e2833, trois rejeux de confirmation conformes. Recompte indépendant
   lot par lot concordant. **AUCUN écart de dépôt.**
2. **VOLET 1 CLOS ET DÉPOSÉ** (`3419d49`) — adjudication documentaire F2/F5,
   **VERDICT V6 : les deux têtes inexactes sur points distincts.**
   - `LC-D-F2-TTT-PLANCK` : inexacte sur la **LOCALISATION**. « 900 ± 700 »
     n'est pas en Table II de 2312.12498v2 — cette table donne 0 ± 7 pour le
     ttt équilatéral fiducial, σ de 7 à 436, aucune occurrence du couple.
   - `LC-D-F5-ETAT-RACCORD` v0.3 : inexacte sur la **LITTÉRALITÉ**. Le chiffre
     est imprimé DEUX FOIS verbatim, p. 1 (abstract) et p. 2 (introduction),
     avec son exposant ttt.
   - Gel `201bcfbb` figé AVANT toute lecture, antériorité prouvée par l'état du
     répertoire ; plafond **CONSTAT SUR PIÈCES LOCALES** annoncé AU GEL,
     atteint non dépassé ; deux amendements datés en fichiers séparés ; gel
     byte-intact de bout en bout, re-vérifié après chaque écriture.
   - **V1 exclu par MESURE ([D2]), non par redéfinition.**
   - **Corps ET front-matters des deux têtes JAMAIS ouverts.** La note désigne
     des ASSERTIONS telles que le prompt S10 les rapporte ; elle ne cite aucune
     chaîne des têtes.
3. Le commit qui dépose la présente note (swap −S9 +S10).

## 2. Écarts de S10 — quatre, décomposés

1. **HEAD ≠ attendu à l'ouverture.** Le prompt S10 annonçait HEAD = « Reprise
   S9 » ; le clone donnait quatre commits au-dessus (clôture S9, swap −S8 +S9,
   deux intrants du volet 1). Chaîne attendue intacte, décalée de 4. Non
   imputable au dépôt. Vérifié par `git log`, jamais par la note (R-36 tenu).
2. **Le prompt du mount n'était PAS le prompt déposé.** Mount : 109 lignes,
   sha `7a2bf268…`. Git : 132 lignes, sha `de9ce9da…`, byte-intact depuis
   `22a87c1` et redéclaré tel à deux reprises. L'écart portait précisément sur
   le §5 volet 1 : le mount laissait le choix de la voie ouvert, le git portait
   la voie (ii) déjà arbitrée. **Écart RÉEL de contenu**, non artefact de canal
   (10 des 12 pièces texte communes passent byte-intactes).
   **TRANCHÉ EN S10** : voir `autorite` en front-matter.
3. **Deux débordements de périmètre en cours d'adjudication**, imputables au
   pilote, consignés dans la note : lors de [D4] (bornage par numéros de ligne),
   puis lors de la lecture de Table I (détection de fin de PAGE au lieu de fin
   de LÉGENDE, après avoir écrit la correction). Une information hors périmètre
   en est issue et a été **déclarée NON EMPLOYÉE** — elle est nommée dans la
   note pour ne pas circuler en contrebande.
4. **[D5] non mesurable** dans le périmètre gelé → consignation par clause I-c
   pré-déclarée. Conséquence : le fond du correctif R-23 n'est **ni confirmé ni
   infirmé** alors que sa **prémisse est fausse**.

## 3. Ce qui reste — REPORTÉ EN S11, rien n'est perdu

- **VOLET 1-bis — lever [D5], puis statuer sur R-23.** Décision opérateur prise
  en S10. Trois pièces à lire, toutes locales : l'**équation (10)** de
  2312.12498v2, le **panneau inférieur de Table II** (annoncé par sa légende,
  absent de l'extraction `-layout`), la **convention d'unité** de Table II
  (aucune mention dans la table ni sa légende). Exige un GEL NEUF.
- **VOLET 2 — SILO P, arbitrage.** β / P-1 (cartographie v1.2 : β#1 maintenu)
  VS report modulaire d = 3 / P-3 (recommandation #1 des decks). Tracker R-53 :
  0/4. **L'opérateur a demandé une PRÉSENTATION atouts/inconvénients AVANT de
  trancher.** Pièces nommées, non ouvertes : `kb/LC-07-CARTOGRAPHIE.md`,
  `kb/LC-WORK-CARTOGRAPHIE-PRIORITES.md`.
- **VOLET 3 — SOLDES DE GOUVERNANCE.** G-1 solde (16 bundles de la décharge
  v2.74, 72 .py ; `hors-KB/A/` non fourni — MESURÉ en S10 : `hors-KB/` ne
  contient que `B`) · G-4 (autorité mount vs git) · G-5b/c (index `LC-00-INDEX`
  — MESURÉ en S10 : **ABSENT de `kb/`** ; arborescence des silos) · PDF du
  mount vs `sources/2503_19957v1.pdf`, confrontation non exécutée.

## 4. Périmètre — INCHANGÉ

Le volet 1 n'a retiré aucune inconnue et n'était pas un lot.

`{ A4 ; A2★ ; N }` INCHANGÉ · [B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON
réfuté, postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · **D1 non
clos**, conclusion **D1c intacte** · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) · **CCC
non démontrée NI réfutée**.

**Silo R : clos à 12/12**, INCHANGÉ. « Branche FALSIFIABILITÉ épuisée » reste un
constat de NON-EXISTENCE d'un front borné et sceau-able restant, invérifiable
par instrument, JAMAIS un acquis.

## 5. Règles de gouvernance arrêtées en S10 — opposables

1. **UNICITÉ DE LA REPRISE.** Un seul fichier de reprise, au git comme au
   mount. Les notes antérieures vivent dans l'historique git. **Tout ce qui
   n'est pas réalisé en reprise N est REPORTÉ en reprise N+1** — jamais laissé
   en coexistence. C'est le correctif direct de l'incident S9, où deux notes ont
   coexisté à la racine et où l'opérateur suivant pouvait ouvrir la mauvaise.
2. **AUTORITÉ DES PIÈCES DE GOUVERNANCE.** Prompts d'ouverture, notes de
   reprise et leurs amendements : **le git fait foi**, le mount vaut copie de
   travail. Ceci ne tranche pas G-4 : pour la KB scellée, **le mount reste
   autoritaire (R-54)**, le git reste miroir vérifiable.
3. **AMENDEMENT PAR FICHIER SÉPARÉ DATÉ**, jamais en place ; la pièce amendée
   reste byte-intacte et re-vérifiable après coup. Tenu trois fois en S10.
4. **R-55** : au dépôt, annoncer chemin + sha256 + message de commit, fichier
   par fichier, AVANT de demander le token. En S10 le token est arrivé avant
   l'annonce ; l'annonce a été faite quand même et le push n'a eu lieu qu'après
   confirmation. **Le token ne remplace pas l'annonce.**
5. **Vérification de dépôt sur CLONE NEUF**, jamais sur déclaration.

---

*§6.4 — rejouer, adjuger, déposer, clôturer : aucun de ces gestes ne scelle, ne
réduit, ne compte, ne démontre quoi que ce soit.*
