---
id: NOTE-REPRISE-GIT-S13
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S13 (2026-07-24). Consolide et remplace NOTE-REPRISE-GIT-S12 (mount-seul, périmée) ; les notes S9–S11 vivent dans l'historique git. ACQUIS S13 : chantier β OUVERT sous discipline, puis prérequis BLOQUANT P-8 découvert et SOLDÉ + DÉPOSÉ (commit cad358a, instruments/LC-WORK-GEN-PAQUET-v2_1.py sha8=7d63b9ed, auto-test 6/6 mordantes). Deux divergences note S12 / dossier tranchées par l'opérateur : (#1) intrants β = les 4 corps de la note, placés en KB active ; (#2) route δ (poids b Odak–Speziale) = VOIE DISPONIBLE, non gelée sous G-2. Le DOSSIER LC-BETA (mount-seul, V94/v2.121) FAIT FOI comme guide ; la SUBSTANCE β est au git kb/. Mon brouillon GEL-BETA-P1 est ÉCARTÉ (jamais déposé). PROCHAIN GESTE : β peut TIRER SA GATE (P-8 levé) SOUS le cadrage LC-BETA existant + R-41 (≥3 miroirs + espace-verdict gelé) + amendement R-7 daté AVANT lecture + scoping gelé, en EMPLOYANT le générateur v2.1 pour la livraison séquencée. JAMAIS d'office."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-24
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S12.md (encore au mount, périmée par le dépôt P-8 et les arbitrages S13). Une seule note de reprise doit exister, au git comme au mount (règle d'unicité)."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture d'une session neuve, TANT QUE S13 n'est pas déposée : HEAD = le commit `cad358a` dont le message commence par « Sold P-8 … » (c'est le dépôt du générateur v2.1 fait EN S13, PAS un commit de reprise), à vérifier par `git log`, JAMAIS par cette note. Son parent est `af97865` « Reprise S11 »."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise. Les notes S9–S12 sont périmées : S9/S10/S11 en historique git, S12 encore au mount et à RETIRER lors du dépôt de S13. Tout ce qui n'est pas réalisé en reprise N est REPORTÉ en N+1, jamais laissé en coexistence."
autorite: "Pour les pièces de GOUVERNANCE (prompts, notes de reprise, amendements), le DÉPÔT GIT FAIT FOI, le mount vaut copie de travail. EXCEPTION FACTUELLE constatée en S13 et NON tranchée : le dossier LC-BETA et le journal V94 sont MOUNT-SEUL (absents du git) tout en faisant foi comme guide de lecture ; la SUBSTANCE β qu'ils indexent est, elle, au git kb/. Ceci ne tranche pas G-4 (§8)."
supersede: "Points où S13 corrige S12 (seul le récent est reporté, voir §9) : §0-lite HEAD « Reprise S11 » → cad358a « Sold P-8 » ; instruments/*.py 33 → 34 ; cadre β « à ouvrir sous gel R-7 neuf » (S12) → « dossier LC-BETA préexistant fait foi, prérequis P-8 d'abord » (S13) ; prérequis P-8 (absent de S12) SURFACÉ puis SOLDÉ."
---

# Note de reprise S13 (consolidée, CLÔTURE) — état, acquis, prochain geste

> **Pourquoi cette note existe.** S12 était au mount, jamais déposée au git.
> En S13, sur le « prochain geste » de S12 (ouvrir β), trois faits que S12 ne
> portait PAS ont émergé et vivaient uniquement dans l'échange : (a) β est un
> chantier DÉJÀ cadré et gelé (dossier LC-BETA, mount-seul) que S12
> sous-décrivait ; (b) un prérequis BLOQUANT — le mandat P-8 — interdisait de
> tirer la gate ; (c) les 4 intrants β ont été confrontés (première mesure).
> P-8 a été soldé et déposé. Cette note fond ce qui reste vivant de S12,
> capte ces trois faits, et redevient l'UNIQUE fichier de reprise.

## 0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S13

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -10   # attendu tant que S13 non déposée :
                            #   HEAD = cad358a « Sold P-8 … » (dépôt S13), puis
                            #   af97865 (Reprise S11), 63cac9f, 860c3f8,
                            #   3419d49, ccceb6c, d43572a, 78e0ff3, 22a87c1
    ls instruments/*.py | wc -l                    # attendu : 34  (33 + P-8)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 42
    ls kb/*.md | wc -l                             # attendu : 215
    ls hors-KB/B/ | wc -l                          # attendu : 4
    ls sources/ | wc -l                            # attendu : 4 (hors compte)
    python3 instruments/inventaire_sceaux.py       # 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre   # sha8=051e2833 rc=0
    # les 12 redémonstrations : bilan INCHANGÉ depuis S9
    # R4 35/35 · R5 17/17 · R3 16/16 · R6 16/16 · R2 12/12 · R12 11/11
    # R1 6/6 · R8 21/21 · R10 40/40 · R7 45/45 · R9 16/16 · R11 36/36

**Total INCHANGÉ : 271/271 PASS + 101 consignations, 12/12 rc = 0.** Recompté
deux fois de façon indépendante, rejoué CONFORME en S9–S12 (non re-rejoué en
S13 : S13 n'a pas touché aux redémonstrations).

Hors compte §0-lite, rejeux de confirmation, tous CONFORMES :

    python3 instruments/harnais_R9.py    # « 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py   # « 7/7 mordantes » + « VACANTES: 0 », rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py   # rc=0 ; sha256 script = 8e386686
    python3 instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test  # 6/6 mordantes, rc=0 (NEUF S13)

Intrants R-11/R-23 (sources/), à CONFRONTER au registre de première mesure :

    2312_12498v2.pdf  sha8=04d9b4f4 ; 2409_10595v2.pdf  sha8=27a94980
    2503_19957v1.pdf  sha8=113ab4a2

**Registre de première mesure β — NOUVEAU S13, chat-only avant cette note (§3).**

### Leçons d'environnement opposables (S2–S13, toutes maintenues)

Toutes celles de S12 tiennent : `setsid nohup` pour rejeu long ; `ls audit/`
pas `ls audit/*.md` ; jamais deux sceaux dans le même arbre ; les durées ne
sont pas des clés ; `origin/front-pq` bénigne ; `inventaire_sceaux.py` réécrit
sa date (restaurer par `git checkout`) ; `redemo_R6` imprime sans crochets
(recompte tolérant) ; `harnais_R11` crée `__pycache__` à nettoyer ;
outillage PDF `pdfplumber`/`pdftoppm`, `pymupdf` ABSENT, descendre au niveau
`chars` sur les maths affichées ; **allowlist réseau NE COUVRE PAS arxiv.org**.
**NEUF S13** : `github.com` EST couvert (dépôt/push OK) ; le token se passe EN
LIGNE, jamais au disque/`.git/config`/commit (vérifié à 0 après le push) ;
`${PIPESTATUS[…]}` est un bashism qui casse sous `/bin/sh` — chaîner par `;`.

## 1. Historique des acquis (S9 → S13), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2), volet 1 (V6) et volet 1-bis ([D5]
  LEVÉ, W3) clos et déposés. Détail intégral en historique git.
- **S12** (mount-seul) : §0-lite conforme ; VOLET 2 arbitré = β/P-1 ; sort de
  R-23 = MAINTIEN (corps de F5 non ouvert). Ces acquis TIENNENT.
- **S13 — β ouvert sous discipline ; P-8 découvert bloquant, SOLDÉ + DÉPOSÉ.**
  1. Brouillon de cadrage β rédigé PUIS **ÉCARTÉ** : le dossier LC-BETA
     préexistant fait foi (décision opérateur). Le brouillon n'a JAMAIS été
     déposé ; ne pas le ressusciter.
  2. **Deux divergences note S12 / dossier, tranchées opérateur** :
     - **#1 intrants** : les **4 corps de la note** gouvernent β (FH-II
       `2503.09372`, Horowitz–Wang `1909.11703`, Liu–Santos–Wiseman
       `2402.04308`, Skenderis `2312.17316`), placés en **KB active** (mount)
       et **confrontés en première mesure** (§3).
     - **#2 route δ** (poids `b` d'Odak–Speziale) = **VOIE DISPONIBLE**, NON
       gelée sous le constat biaisé G-2.
  3. **Prérequis P-8 SURFACÉ** (absent de S12) : le mandat P-8 de
     `LC-WORK-AMENDEMENT-R7-LIVRAISON-SEQUENCEE` (gel `cc856f67`, journal V94
     §4) rend le générateur de paquets DÛ avant toute gate. « Tirer sans P-8
     referait ce que V94 a consigné contre le pilote. »
  4. **P-8 SOLDÉ + DÉPOSÉ** (§4). Commit `cad358a` sur `main`.

## 2. VOLET β (P-1) — état RÉEL récupéré du dossier consigné (au git kb/)

La substance ci-dessous VIT au git `kb/` (pointeurs, non re-transcrite) ; elle
est rappelée parce que S12 la sous-décrivait.

- **β ≡ G3 = transport AdS→dS (« T-b ») de la jonction Δ_𝒞 / gate C1, Λ>0** ;
  seul facteur d'O₂ ouvert ; O₂ (CFT de raccordement) À INVENTER.
- **Base établie (R-12, Silo R)** : `Δ_𝒞 = d` au pas C1-b, coin `α = C1-b
  POSITIF`, `p ≡ b` LIBRE ⟹ résidu d'O₂ = β SEUL (`LC-D-O2-COIN-TRANSMISSION`,
  `LC-D-O2-DELTA-C`, `LC-D-O2-JONCTION`).
- **Verdicts de transport DÉJÀ rendus** (`LC-D-G3-TRANSPORT`) : S-G3T-1 = T-b
  (délimitation, à pencher-obstruction) ; **S-G3T-2 = T-b MAINTENU, mur
  RE-SITUÉ vers TG-3** (carte shadow renormalisée du graviton DEUX-BORDS au pas
  marginal C1-b), **gaté fetch**. Skenderis = scalaire MONO-bord (muet sur le
  cas graviton deux-bords) ; wedge `2007.06800` = AdS/BCFT (perd le dictionnaire
  en dS genuine).
- **Cadrage β figé, anti-fit** (`LC-WORK-CADRAGE-G3-HORS-WEDGE`, sha in-fichier
  R-36) : cibles **TH-1…TH-4** + firewall **TH-R** (m1 Λ→0⁻ ; m2 scalaire→
  Skenderis ; m3 braneworld→verdict wedge ; m4 mauvaise continuation), issues
  **T-a (construction) / T-b (délimitation) / T-c (obstruction)**, critère
  TRIPARTITE (défaut = délimitation), rendement attendu EN BAISSE.
- **Candidats genuine-dS deux-bords ARMÉS, NON LUS** (identité à confirmer au
  fetch, R-41) : (i) patch statique / deux horizons étirés (Susskind ;
  Shaghoulian) ; (ii) dS/CFT & renorm au bord futur (Strominger ; Maldacena ;
  Anninos) ; (iii) bootstrap cosmologique (Arkani-Hamed–Baumann) ; (iv)
  holographie céleste (long shot). Risque amont **DESI DR2 (2025)** sur le
  prérequis dS asymptotique, en positionnement séparé, zéro cible gelée.
- **Deux routes** (P-sélecteur, P-3/HOLD) : (α) transport au pas C1-b
  **renormalisé** (route refermée sauf ingrédient neuf = **P-8/générateur
  v2.1**, désormais présent) ; (δ) invariance/non du poids `b` d'Odak–Speziale
  sous Λ<0→Λ>0 — **OUVERTE** (arbitrage #2).

## 3. Registre de première mesure β — CHAT-ONLY avant cette note (À CONSIGNER)

Les 4 intrants β, mesurés au mount le 2026-07-24, AUCUN registre antérieur
(la note S12 n'en portait pas ; le dossier les déclarait « non lus, identité à
confirmer au fetch »). **Ces valeurs deviennent la référence de première
mesure** (S10) — à confronter avant toute consommation ; tout écart se
décompose avant de poursuivre.

    2503_09372v2.pdf  979 890 o   sha256=6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62   (FH-II)
    1909_11703v2.pdf  386 010 o   sha256=e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7   (Horowitz–Wang)
    2402_04308v2.pdf  4 629 572 o sha256=1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2   (Liu–Santos–Wiseman)
    2312_17316v2.pdf  1 223 061 o sha256=7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541   (Skenderis)

Extractions texte présentes au mount (`2503_09372v2_OCR.txt`,
`2402_04308v2.txt`) : NON LUES en S13 (les lire serait extraire du contenu
avant le gel/scoping R-41). Rester scellé jusqu'à la gate.

## 4. P-8 — ce qui est fait, ce que P-9 réserve

- **Déposé** : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`,
  `sha256=7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`,
  commit `cad358a` sur `main` (parent `af97865`). Auto-test **6/6 mordantes**
  rejoué sur la copie déposée.
- **Ce qu'il fait, à la lettre du mandat (§2 de LC-WORK-AMENDEMENT-R7-
  LIVRAISON-SEQUENCEE)** : (i) deux tranches nommées, refus tranche unique par
  défaut ; (ii) tranche unique seulement sur `--inapplicable`, clause P-6
  écrite VERBATIM par le script ; (iii) scan P-7 de la tranche 1 → exit≠0 ;
  (iv) champ `REGIME` toujours au manifeste ; + test matériel P-1 (aval
  déclaré ⇒ multi-tours ⇒ `--inapplicable` refusé). Générique, réutilisable.
- **P-9 rappelé** : le dépôt n'atteste QUE l'existence de l'instrument. Sa
  valeur se mesure À LA PROCHAINE GATE — la tranche 2 a-t-elle été expédiée
  APRÈS l'issue de Phase 2, oui/non. Écrire l'instrument ne solde pas la gate.
- **À FAIRE, opérateur** : **RÉVOQUER le PAT** utilisé pour le push (il a
  transité en clair dans le chat S13 ; discipline = token révoqué après usage).
- **Défaut de nom déclaré** : `…-v2_1.py` porte une version DANS le nom,
  contraire à la norme de nommage *proposée* (non arbitrée) — à régulariser si
  la norme est adoptée, jamais d'office.

## 5. Localisation git / mount — ce qui est consigné, et où (constat S13)

- **Au git `kb/`** (consigné, fait foi substance) : toute la substance β —
  `LC-D-G3-TRANSPORT`, `LC-WORK-CADRAGE-G3-HORS-WEDGE`, `LC-D-O2-*`,
  `LC-D-O2-P-SELECTEUR`, **le mandat P-8** `LC-WORK-AMENDEMENT-R7-LIVRAISON-
  SEQUENCEE`. Compte kb/ = 215, conforme.
- **Au git `instruments/`** : générateur v1.0 `LC-WORK-GEN-PAQUET-CSE2.py` +
  v2.1 `LC-WORK-GEN-PAQUET-v2_1.py` (neuf S13).
- **MOUNT-SEUL, ABSENTS DU GIT** (constat S13, extension de G-4) : le
  **packaging LC-BETA** (LC-BETA-00-PROMPT-PROJET, -01-README, -03-CADRAGE,
  -PAQUET-GEL, -BOOT.py, -02-ETAT-BETA, -04-R41-MIROIRS) et le **journal V94**.
  Ils font foi comme GUIDE DE LECTURE (V94/v2.121) mais indexent une substance
  qui, elle, est au git. À trancher : les verser au git, ou acter le régime
  mount-guide / git-substance ? (§8).
- **Note S12** : mount-seul ; le git porte `NOTE-REPRISE-GIT-S11.md` et
  `PROMPT-OUVERTURE-S12.md`. Au dépôt de S13, RETIRER S12 du mount (unicité).

## 6. PROCHAIN GESTE ET RESTE À FAIRE

### 6.1 PROCHAIN GESTE — TIRER la gate β (P-8 levé)

P-8 soldé lève le prérequis bloquant. β passe de *cadré-en-attente* à
*tirable*, MAIS **jamais d'office** et **sous le cadre existant** :

- **cadrage = `LC-WORK-CADRAGE-G3-HORS-WEDGE`** (cibles TH figées, ne PAS
  re-geler) ; le brouillon S13 est écarté ;
- **gate R-41** : ≥ 3 miroirs + espace-verdict gelé AVANT lecture ;
- **amendement R-7 daté** requis AVANT de lire tout corpus + **scoping gelé**
  recommandé (fork S-G3T-3b, FETCH HOLD) ;
- **livraison séquencée via le générateur v2.1** (P-2/P-8) : c'est ici que P-9
  MESURERA P-8 (tranche 2 après Phase 2) ;
- intrants β **confrontés au registre §3** avant extraction (précédent S8) ;
- **audit froid neutralisé** obligatoire sur tout nouvel objet de positivité ;
- plafond attendu réaliste : **DÉLIMITATION** (T-b), rendement en baisse ;
  T-a (construction) exigerait la carte shadow renormalisée dS-genuine graviton
  deux-bords, NON exhibée à ce jour.

### 6.2 Reste à faire (reporté)

- **Norme de nommage** (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION S11) : non
  arbitrée ; concerne aussi le nom `…-v2_1.py` (§4).
- **VOLET 3 — soldes de gouvernance** : G-1 (ré-import vs réécriture),
  **G-4** (autorité mount/git, §8), G-5b/c (index LC-00-INDEX absent).
- **Sort de R-23** : MAINTIEN (S12) — corps de F5 non ouvert, fond ni confirmé
  ni infirmé, [D5] LEVÉ (W3) intact.

## 7. Discipline et précédents opposables (S4–S13)

Tous les précédents S4–S12 restent PLEINEMENT OPPOSABLES (voir historique et
S12 : lire pour présenter n'est pas ouvrir ; une divergence se nomme et se
tranche par l'opérateur ; borner AVANT de lire ; un défaut se nomme et s'amende
par fichier séparé daté ; l'antériorité se prouve par l'état du répertoire ;
etc.).

**S13 —** un chantier « à ouvrir » peut être DÉJÀ cadré/gelé : lire le dossier
existant AVANT de rédiger un cadrage neuf (un brouillon rédigé dans l'ignorance
du dossier se JETTE, il ne se dépose pas) · un prérequis bloquant absent de la
reprise peut vivre dans le dossier : le chercher (V94 §4) avant de tirer une
gate · un repérage « locate » peut faire remonter de la substance : le déclarer
· un instrument mandaté se construit à la LETTRE du mandat (cibles figées =
antériorité, pas de gel neuf) et se prouve par un AUTO-TEST MORDANT (chaque
garde a un porteur mutable, sinon faux PASS) · le token se passe en ligne,
jamais au disque/config/commit, et se RÉVOQUE après usage · un dépôt fait
avancer HEAD et change les comptes : recaler §0-lite dans la reprise, jamais
laisser diverger · substance au git, packaging au mount = à nommer, pas à
réconcilier d'office (G-4).

## 8. G-4 — questions ouvertes (S12 + extension S13)

Reconduites de S12 : provenance/écart de taille des PDF mount vs git ; quel
côté fait autorité pour le CONTENU scientifique ; R-54 (mount autoritaire KB)
confirmée ou rouverte.

**Extension S13** : le **packaging LC-BETA et le journal V94 sont mount-seul**
alors qu'ils font foi comme guide, tandis que la substance qu'ils indexent est
au git. Faut-il les verser au git (unicité de gouvernance : « git fait foi »),
ou acter un régime explicite « mount = guide de lecture, git = substance +
mandats » ? Non tranché — posé à l'opérateur.

## 9. Table de supersession — ce qui a été ÉCARTÉ de S12

| Point | Ancien (périmé) | Retenu S13 |
|---|---|---|
| HEAD attendu | « Reprise S11 » (`af97865`) | **`cad358a` « Sold P-8 »** |
| instruments/*.py | 33 | **34** |
| Cadre d'ouverture de β | S12 : « ouvrir sous gel R-7 NEUF », 4 corps + 2 routes, sans P-8 ni dossier | **S13 : dossier LC-BETA préexistant FAIT FOI ; prérequis P-8 d'abord ; brouillon neuf écarté** |
| Prérequis P-8 | absent de S12 | **surfacé, SOLDÉ, déposé (cad358a)** |
| Intrants β | non mesurés | **4 sha de première mesure (§3)** |
| Route δ | présentée disponible (note) vs bloquée G-2 (dossier) | **DISPONIBLE (arbitrage opérateur)** |

**Note S12 corrigée par S13** : S12 était mount-seul et sous-décrivait β
(ni P-8, ni dossier LC-BETA, ni transport déjà à T-b). S13 UNIQUE la remplace.

---

*§6.4 — sentinelle terminale. Ouvrir, cadrer, geler, solder un instrument,
déposer, consolider une note : aucun de ces gestes ne scelle, ne réduit, ne
compte, ne démontre quoi que ce soit. { A4 ; A2★ ; N } INCHANGÉ · D1 non clos ·
N non fixé (≡ Λ, R-53 0/4) · O₂ non construit · β T-b, NON résolu, seul facteur
d'O₂ ouvert · nœud (i) INDÉTERMINÉ (pas A) · CCC non démontrée NI réfutée.*
