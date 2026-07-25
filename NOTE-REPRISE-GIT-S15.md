---
id: NOTE-REPRISE-GIT-S15
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S15 (2026-07-25). Consolide et REMPLACE NOTE-REPRISE-GIT-S14 ; les notes S9–S14 vivent dans l'historique git. ACQUIS S15 : §0-lite CONFORME avec les 12 redémonstrations REJOUÉES (première fois depuis S12) ; registre des 4 corps β RE-CONFRONTÉ 4/4 au bit près, bloquant S14 §3 LEVÉ ; DEUX ARBITRAGES opérateur (dissolution PAR ENSEMBLE ; régime des surfaces) ; amendement de périmètre nº2 GELÉ ET DÉPOSÉ, donc R-7 SATISFAIT ; instrument de contrôle côté dépôt déposé, 8/8 gardes mordantes. ZÉRO mouvement scientifique : aucune source lue, aucune ligne classée, aucune gate tirée, aucun verdict touché. PROCHAIN GESTE : P-0 (R-41) sur les SEPT sources, l'ensemble A entier. JAMAIS d'office."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S14.md, retirée de la racine au même commit, après AUDIT DE REPORT item par item (§10). Une seule note de reprise doit exister, au git comme au mount."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture d'une session neuve : HEAD = le commit dont le message commence par « Reprise S15 », à vérifier PAR `git log`, JAMAIS par cette note. Ses parents remontent par 20290b1 (amendement β nº2 + contrôle dépôt), 1c90daf (Reprise S14), b4af0c5 (swap d'unicité), 8caafa7 (amendement 1 à S13), 09d9e2a (Reprise S13), cad358a (Sold P-8), af97865 (Reprise S11). EN S14 CE PIÈGE A MORDU : S13 annonçait HEAD = cad358a « tant que S13 n'est pas déposée », alors qu'elle l'était. En S15 il n'a PAS mordu, parce que HEAD a été mesuré avant d'être lu."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise. Les notes S9–S14 sont périmées et vivent dans l'historique git. Tout ce qui n'est pas réalisé en reprise N est REPORTÉ en N+1, jamais laissé en coexistence. Un amendement daté n'est pas une seconde note."
autorite: "RÉGIME G-4, TRANCHÉ le 2026-07-25, portée PROSPECTIVE. Le MOUNT est l'espace vivant : conduite de projet, matériaux en cours, éléments intermédiaires d'une branche non finalisée ni épuisée. Le GIT est l'espace de consignation : matériaux validés et vérifiés, résultats confirmés et audités, accompagnés du matériel permettant à une instance tierce de REPRODUIRE. Bascule mount → git à l'épuisement d'une branche, après audit froid incognito. L'EXISTANT RESTE EN PLACE. R-54 reste debout. Pour les pièces de GOUVERNANCE (prompts, notes de reprise, amendements), le dépôt git fait foi — CE POINT A ÉTÉ APPLIQUÉ EN S15, voir §5.2."
supersede: "Points où S15 corrige S14 : §0 audit/ 42 → 45 ; piège R-36 (« Reprise S14 » → « Reprise S15 ») ; §3 registre β « NON re-confrontable, écart BLOQUANT » → RE-CONFRONTÉ 4/4, bloquant LEVÉ ; §5 pare-feu « ni au dépôt » → GLOSE SANS SOURCE, RETIRÉE ; §5 « le gel ne ment pas par âge » → VRAI des 35 copies, FAUX des 8 pièces LC-BETA-* ; §6.1(3) amendement de périmètre « à déposer » → DÉPOSÉ (20290b1)."
---

# Note de reprise S15 (consolidée, CLÔTURE) — état, acquis, prochain geste

> **Pourquoi cette note existe.** S15 a exécuté le §0-lite intégral **redémonstrations
> comprises** (non rejouées depuis S12), levé le bloquant des 4 corps β par mesure, porté
> deux arbitrages opérateur, et **déposé** l'amendement de périmètre — ce qui satisfait
> `R-7` et retire au futur classement le caractère mécanique de fit. Elle absorbe la note
> S14 sans perte (§10).

## 0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S15

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -7   # HEAD = message commençant par « Reprise S15 », puis
                           # 20290b1, 1c90daf, b4af0c5, 8caafa7, 09d9e2a, cad358a
    ls instruments/*.py | wc -l                    # attendu : 34
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 45   <== RECALÉ (42 → 45)
    ls kb/*.md | wc -l                             # attendu : 215
    ls hors-KB/B/ | wc -l                          # attendu : 4
    ls sources/ | wc -l                            # attendu : 4 (hors compte)
    python3 instruments/inventaire_sceaux.py       # 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre   # sha8=051e2833 rc=0
    # les 12 redémonstrations : bilan INCHANGÉ depuis S9
    # R4b 35/35 · R5b 17/17 · R3 16/16 · R6 16/16 · R2 12/12 · R12 11/11
    # R1 6/6 · R8 21/21 · R10 40/40 · R7 45/45 · R9 16/16 · R11 36/36

**Total INCHANGÉ : 271/271 PASS + 101 consignations, 12/12 rc = 0.**
Décomposition pour recompte indépendant :
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` ;
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`.
**REJOUÉES ET CONFORMES EN S15** — premier rejeu depuis S12 ; S13 et S14 n'y avaient pas
touché. **Le rejeu n'est donc PAS dû en S16** au titre d'un arriéré ; il l'est au titre du
§0-lite, comme toujours.

**Recalage `audit/`, mesuré et non déduit** : le commit `20290b1` a ajouté trois pièces à
`audit/` (42 → **45**). **Les cinq autres comptes sont INCHANGÉS.** Mesuré aussi :
l'ajout d'un `.py` dans `audit/` **ne déplace pas** `inventaire_sceaux.py` (6/76/1) et **ne
déplace pas** le sceau (`051e2833`).

Les douze scripts, dans l'ordre : `redemo_R1_moduleA` `redemo_R2_D1` `redemo_R3_spectre`
**`redemo_R4_CT_b`** **`redemo_R5_reductions_b`** `redemo_R6_nongauss` `redemo_R7_A4QW`
`redemo_R8_A2star` `redemo_R9_tracteur` `redemo_R10_nonlin` `redemo_R11_falsifiabilite`
`redemo_R12_O2`. **Les variantes `_b` de R4 et R5 sont celles qui comptent** (instruction du
verdict CSE, `audit/R4b-R5b-INSTRUCTION.md`) ; les v1 restent au dépôt et ne se rejouent pas.

Hors compte §0-lite, rejeux de confirmation, tous CONFORMES en S15 :

    python3 instruments/harnais_R9.py    # « 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py   # « 7/7 mordantes » + « VACANTES: 0 », rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py   # rc=0 ; sha256 script = 8e386686
    python3 instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test  # 6/6 mordantes, rc=0
    python3 audit/LC-BETA-CONTROLE-DEPOT.py --self-test          # 8/8 mordantes, rc=0

Intrants `sources/` — **CONFRONTÉS ET CONCORDANTS en S15**, vrais PDF (magie `%PDF`) :

    2312_12498v2.pdf  1 895 152 o  sha8=04d9b4f4
    2409_10595v2.pdf  2 332 898 o  sha8=27a94980
    2503_19957v1.pdf    910 410 o  sha8=113ab4a2

**Toute réapparition SE CONFRONTE à ces valeurs. Enregistrer n'est pas confronter.**

### Leçons d'environnement opposables (S2–S15, toutes maintenues)

`setsid nohup` pour rejeu long ; `ls audit/` pas `ls audit/*.md` ; jamais deux sceaux dans
le même arbre ; les durées ne sont pas des clés de sceau ; `origin/front-pq` résiduelle et
bénigne, ne pas y toucher ; `inventaire_sceaux.py` **réécrit sa date** (restaurer par
`git checkout`) ; `redemo_R6_nongauss.py` imprime sans crochets (recompte au motif tolérant
`^\s*\[?PASS\]?`) ; `harnais_R11.py` crée `instruments/__pycache__/` à nettoyer ;
`pgrep -f` s'auto-matche ; `simplify` **non borné** ; outillage PDF `pdfplumber` 0.11.9,
`pdftoppm`/`pdfinfo`, Pillow présents, **`pymupdf` ABSENT**, `extract_words` **mensonger**
sur les mathématiques affichées — descendre au niveau `chars` ; `${PIPESTATUS[…]}` est un
bashism qui casse sous `/bin/sh` — chaîner par `;` ; **`xxd` ABSENT** du conteneur (NEUF
S15 : utiliser `python3` ou `od`) ; un **paquet ZIP de TEXTES extraits ne permet PAS la
confrontation octet**, mais **un ZIP de TRANSPORT des octets originaux le permet** (§3.3).

**Réseau.** L'allowlist de `bash` **NE COUVRE PAS `arxiv.org`** ; `github.com` **EST**
couvert (clone, dépôt, push OK). Les outils de recherche/fetch web sont un **canal SÉPARÉ**,
non soumis à cette allowlist — pages éditeur, INSPIRE, ADS et arXiv y sont atteignables.
La fiche `LC-BETA-04` §2 affirme le contraire : **défaut d'âge**, corrigé par l'amendement
de périmètre nº1 §3. Conséquence pratique inchangée : **les PDF consommés viennent de
l'opérateur.**

**Token.** Passé **en ligne**, jamais au disque, jamais dans `.git/config`, jamais dans un
commit — **et vérifié à 0 après usage**, y compris dans **le contenu de tous les blobs jamais
commités** (`git rev-list --objects --all`, pas seulement `HEAD` — NEUF S15). Révoqué après
usage : la conversation en conserve la chaîne, la révocation est la seule opération qui la
rende inerte. **Le dépôt est PUBLIC** : le clone anonyme suffit.

**Identité de commit.** Convention en vigueur : `LC-RACCORD pilote S<n>
<pilote-s<n>@lc-raccord.local>`. **Le pilote ne signe JAMAIS du nom de l'opérateur.**

## 1. Historique des acquis (S9 → S15), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2), volet 1 (V6) et volet 1-bis ([D5] LEVÉ, W3) clos
  et déposés. Détail intégral en historique git.
- **S12** (mount-seul, jamais déposée) : VOLET 2 arbitré = β/P-1 ; sort de R-23 = MAINTIEN
  (corps de F5 non ouvert). Ces acquis TIENNENT.
- **S13** : β ouvert sous discipline ; brouillon de cadrage neuf **ÉCARTÉ** ; intrants β =
  les 4 corps, route δ **DISPONIBLE** ; **P-8 surfacé, SOLDÉ et DÉPOSÉ** (`cad358a`).
- **S14 — administrative en totalité** : G-4 TRANCHÉ ; périmètre de `S-B1` arbitré aux DEUX
  ensembles ; paquet β reçu et vérifié ; §0-lite conforme ; swap d'unicité exécuté ; prompt
  S15 déposé.
- **S15 — administrative en totalité, mais elle a MESURÉ.**
  1. **§0-lite intégral, redémonstrations comprises** — premier rejeu depuis S12, conforme.
  2. **Registre des 4 corps β RE-CONFRONTÉ 4/4** au bit près (§3). **Bloquant LEVÉ.**
  3. **Arbitrage nº1** : dissolution **PAR ENSEMBLE** + non-classifiabilité + levier
     falsifiable (§6.3).
  4. **Arbitrage nº2** : régime des surfaces — glose de pare-feu **retirée**, gouvernance β
     **au git** (§5.2).
  5. **Amendement de périmètre nº2 GELÉ ET DÉPOSÉ** (`20290b1`) ⟹ **`R-7` SATISFAIT.**
  6. **Instrument `audit/LC-BETA-CONTROLE-DEPOT.py` déposé**, **8/8 gardes mordantes**.
  7. **Trois écarts imputés, dont DEUX au pilote** (§7.1).

## 2. VOLET β (P-1) — état RÉEL, substance au git `kb/`, INCHANGÉ depuis S14

- **β ≡ G3 = transport AdS→dS (« T-b ») de la jonction Δ_𝒞 / gate C1, Λ>0** ; **seul facteur
  d'O₂ ouvert** ; O₂ (CFT de raccordement) À INVENTER.
- **`α` est SOLDÉ** : `α = C1-b` **POSITIF**, `p` **LIBRE** — famille à un paramètre, pas une
  construction unique ⟹ **le résidu d'O₂ se réduit EXACTEMENT et uniquement à β**.
- **Verdicts de transport rendus** (`LC-D-G3-TRANSPORT`) : `S-G3T-1` = T-b (mur en `TG-3`) ;
  `S-G3T-2` = T-b, mur **RE-SITUÉ** (wedge `2007.06800` = AdS/BCFT, perd le dictionnaire en
  dS genuine) ; `S-G3T-3b` (`2606.09170`, `2412.00183`) = T-b, **`R4′ ✓✓`** ; `S-G3T-4b`
  (ST `2409.08709` + de Haro `0808.2054`) = T-b, **`R3″ ✓ ACQUIS`** ; `§7quinquies` = **`K-B`
  PRESCRIPTION-DÉPENDANT**, ne décide dans aucun sens — **ne pas le rejouer en croyant
  l'ouvrir**.
- **Le mur, nommé.** Caveat d'admissibilité de **de Haro p.3** : le graviton mixed/Neumann
  n'est admissible que dans la **fenêtre BF / Ishibashi-Wald** **ou** sous **cutoff** ; sinon
  le mode lent est non-normalisable, forcé Dirichlet. ST = branche **cutoff** (échoue `R4″`) ;
  de Haro = branche **fenêtre AdS₄** (échoue le dS-genuine). Chaque candidat ne couvre qu'un
  **sous-ensemble PROPRE**. `R3″` acquis ⟹ **gap résiduel = UNE seule cellule :
  `R1″ ∧ R2″ ∧ R4″`**, le plus net jamais atteint.
- **Pourquoi `T-b` et non `T-c`.** `T-c` exigerait de **PROUVER** l'absence de version
  renormalisée pour le graviton deux-bords en dS genuine. La caveat est un **lean structurel
  FORT** — un quasi-théorème. **Lean ≠ preuve** (`FB-5`).
- **Levier NOMMÉ, NON ARMÉ** : une **preuve** d'(in)admissibilité du graviton propageant
  mixed-BC **deux-faces** au `𝓘⁺` **genuine**, **sans cutoff**. Non-admissible ⟹ `T-c`.
  Admissible ⟹ construction neuve à bâtir. **Il satisfait (a) et (b) de la clause de levier
  falsifiable (§6.3.3) ; il reste NON ARMÉ.**
- **Cadrage figé, anti-fit** (`LC-WORK-CADRAGE-G3-HORS-WEDGE`, sha des octets `37bc85e5…`) :
  cibles **TH-1…TH-4** + firewall **TH-R**, issues **T-a / T-b / T-c**, gel amont réutilisé
  `b5276e68…f175eb`, critère TRIPARTITE, **rendement attendu EN BAISSE**. **NE PAS re-geler,
  NE PAS inventer d'espace neuf.**
- **Candidats genuine-dS deux-bords ARMÉS, NON LUS**, HORS périmètre de `S-B1` : patch
  statique / deux horizons étirés ; dS/CFT & renorm au bord futur ; bootstrap cosmologique ;
  holographie céleste. Les faire entrer exigerait un **amendement nº3 daté**.
- **Deux routes** (P-sélecteur, P-3/HOLD) : (α) transport au pas C1-b **renormalisé** —
  refermée sauf ingrédient neuf, **P-8 désormais présent** ; (δ) invariance du poids `b`
  d'Odak–Speziale sous Λ<0→Λ>0 — **OUVERTE**.
- **Risques amont déclarés** : **DESI DR2 (2025)** met sous tension la constance de Λ — si Λ
  n'est pas constant, **β ne s'ouvre pas, la question change** · **`Δ-C` est plus étroit que
  son libellé** (S7 : `S-2` = FIDÈLE MAIS PLUS ÉTROIT, blocage **non établi au secteur
  graviton**) · **`p` reste libre**, P-sélecteur PENDANT sous constat BIAISÉ.
- **Anti-circularité `K`** : β prend `+i` (Bunch-Davies) et WCH (sens `D→N`) comme **données
  POSÉES**. Aucune cible ne peut présupposer `A4` comme résultat.

## 3. Registre des 4 corps β — RE-CONFRONTÉ 4/4. Bloquant LEVÉ.

### 3.1 Résultat

| réf | corps | o | sha256 | issue 2026-07-25 |
|---|---|---|---|---|
| `B1` | FH-II `2503.09372v2` | 979 890 | `6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62` | **CONCORDANT** |
| `B2` | Horowitz–Wang `1909.11703v2` | 386 010 | `e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7` | **CONCORDANT** |
| `B3` | Liu–Santos–Wiseman `2402.04308v2` | 4 629 572 | `1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2` | **CONCORDANT** |
| `B4` | Skenderis `2312.17316v2` | 1 223 061 | `7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541` | **CONCORDANT** |

Magie `%PDF-1.5`, queue `%%EOF`, sur les quatre. **Aucun écart, ni en taille ni en sha256.**

**Identifiants canoniques et noms de fichiers restent deux choses distinctes.** L'archive de
transport s'appelait `2503_09372v2.zip` et portait **trois** corps.

### 3.2 Imputation

L'écart déclaré BLOQUANT par la note S14 §3 **ne venait pas du registre**, fidèle sur ses
quatre lignes, **mais de la nature de la surface** qui servait ces noms — archives ZIP de
JPEG+OCR (`PK\x03\x04`), aucune entrée `.pdf`. Fait de classe **déjà consignée** à `3419d49`
(S10) et `af97865` (S11) : **la surface du mount ALTERNE**. ⟹ `LC-BETA-04` **§1.5 FAIT** sur
les quatre lignes, par re-confrontation.

### 3.3 Canaux, et la distinction à ne pas réinventer

`B4` par le **mount** ; `B1`/`B2`/`B3` par une **archive de transport**
(`0d73fa8b…c758`, 3 entrées). **`B2` est arrivé DEUX FOIS par DEUX canaux distincts**,
`cmp` rc=0 — **seul témoignage non corrélé** de la séquence, et **il porte sur une ligne**.

> **Un ZIP de TRANSPORT n'est pas un ZIP de SUBSTITUTION.** La leçon opposable vise le cas où
> une dérivée (OCR, texte, rendu page à page) **remplace** les octets d'origine. Quand les
> entrées **sont** les octets d'origine, restitués exacts et confrontés **après** extraction,
> la confrontation octet est **préservée**.

### 3.4 Instabilité des surfaces — mesurée deux fois en une session

Mount : sept `.pdf` tous ZIP à l'ouverture ; ~20 min plus tard `B4` en vrai PDF et les trois
autres homonymes **disparus**. Pièces jointes : trois fichiers apparus entre 17:07 et 17:09,
absents à 16:56. **Dépôt git : n'a pas bougé.**

> **Une confrontation payée se préserve hors surface tournante au moment où elle est
> obtenue**, sinon elle est à repayer. Les octets des quatre corps ont été conservés en
> scratch de session — **hors dépôt, hors mount, hors KB**. Ce n'est PAS un dépôt (`R-55`),
> et **ce scratch ne survit pas à la session** : en S16 les corps sont **à refournir**.

### 3.5 Ce que la concordance N'ÉTABLIT PAS

Un sha256 atteste des **octets**, jamais un titre, des auteurs, un DOI, une date, un grade ni
un objet. **`R-41` reste dû sur les quatre lignes** : §1.2 (≥3 miroirs indépendants), §1.3
(grade éditorial écrit), §1.4 (objet vérifié, pas le titre). **`P-0` n'est pas rendu.**

## 4. P-8 — fait, et ce que P-9 réserve

- **Déposé** : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`, sha256
  `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`, commit `cad358a`.
  Auto-test **6/6 mordantes, rejoué CONFORME en S15**.
- **À la lettre du mandat** : (i) deux tranches nommées, refus tranche unique par défaut ;
  (ii) tranche unique seulement sur `--inapplicable`, clause P-6 VERBATIM ; (iii) scan P-7 de
  la tranche 1 → exit≠0 ; (iv) champ `REGIME` au manifeste ; + test matériel P-1.
- **P-9** : le dépôt n'atteste QUE l'existence de l'instrument. **Sa valeur se mesure À LA
  PROCHAINE GATE.** Écrire l'instrument ne solde pas la gate.
- **DÉFAUT D'ÂGE À NE PAS CROIRE** : le paquet β gelé (2026-07-18) écrit que `P-8` n'est PAS
  soldé — `LC-BETA-BOOT.py` l.103 et `LC-BETA-00-PROMPT-PROJET.md` §6. **C'est FAUX depuis
  `cad358a`.** Défaut **sur-restrictif**, donc non bloquant, mais il ne se corrige **jamais
  d'office** (§7.1).
- **Défaut de nom déclaré** : `…-v2_1.py` porte une version DANS le nom, contraire à la norme
  *proposée* (non arbitrée).

## 5. Localisation git / mount / projet β — régime CLARIFIÉ en S15

### 5.1 Où vit quoi

- **Au git `kb/`** (215) : toute la substance β — `LC-D-G3-TRANSPORT`,
  `LC-WORK-CADRAGE-G3-HORS-WEDGE`, `LC-D-O2-*`, `LC-D-O2-P-SELECTEUR`, le mandat P-8.
- **Au git `instruments/`** : générateur v1.0 + v2.1.
- **Au git `audit/`** (45) : gouvernance et instruction, **dont désormais** l'amendement β
  nº2, `LC-BETA-CONTROLE-DEPOT.py` et `LC-BETA-MANIFESTE-GOUVERNANCE.md`.
- **Au git `sources/`** : 3 PDF, rattachés à `R-11`/`R-23`.
- **MOUNT-SEUL, conforme à G-4** : le **journal V94**.
- **PROJET β séparé** : le packaging `LC-BETA-*` + les 35 `BETA-COPIE-*`.

### 5.2 ARBITRAGE nº2 (2026-07-25) — la glose de pare-feu est RETIRÉE

**Texte gelé, source, `LC-BETA-05` §1** : *« Aucun fichier `LC-BETA-*` ni `BETA-COPIE-*` ne
réside JAMAIS sur `/mnt/project`. »* **Il dit `/mnt/project`. Il ne dit rien du dépôt.**
Le « ni au dépôt » était une **glose** de la note S14 §5, recopiée dans le prompt S15 §5,
**sans source et sans contrôle l'implémentant**. Elle est **RETIRÉE**.

Et G-4 avait déjà tranché : *« pour les pièces de GOUVERNANCE (prompts, notes de reprise,
**amendements**), le dépôt git fait foi »*. **Il n'y avait pas de contradiction `R-7` ↔
pare-feu ; il y avait une glose sans source opposée à un arbitrage qui en avait une.**

**L'objet réel du pare-feu est l'anti-duplication, pas l'anti-préfixe.** La partition est
mesurée : **35 `BETA-COPIE-*` ont une contrepartie `kb/`** ; **8 `LC-BETA-*` n'en ont
aucune**. Deux natures, pas deux noms.

**Retournement consigné** : **le pare-feu élargi était la cause du défaut d'âge du §4.** Une
pièce mount-seul que rien ne confronte peut mentir indéfiniment ; sous contrôle de version,
un mensonge par âge devient visible par `diff`.

### 5.3 Régime par surface, et ce qui inspecte quoi

| surface | objet | interdit — dur | inspecté par |
|---|---|---|---|
| **mount `/mnt/project`** | KB active, espace vivant | toute `BETA-COPIE-*` **et** `LC-BETA-*` | `LC-BETA-BOOT.py` §pare-feu (mordant : mount monté, 0 en S15) |
| **projet β** | atelier du chantier | tout fichier sans préfixe β | `LC-BETA-BOOT.py` §intrus (0) |
| **dépôt git** | consignation, tiers-reproductible | **toute copie de substance**, arbre **et historique** | `audit/LC-BETA-CONTROLE-DEPOT.py` (**déposé en S15**) |
| **dépôt git** | — | les pièces de **gouvernance** β y sont **attendues** | même instrument : présence + sha |

### 5.4 Paquet β — état vérifié en S15

`LC-BETA-PAQUET.zip` sha256 `bbfee7b5…b5f4`, 43 fichiers. `LC-BETA-BOOT.py` **rc=0** :
**42 hachés, 35 copies, 0 absente, 0 altérée, pare-feu 0 intrus / 0 fuite,
`PKG_SHA_BETA_8 = dc276129`**. Gel confronté au `kb/` **par mesure indépendante** :
**34/35 BYTE-IDENTIQUES, 0 DIVERGENTE**, seule absente `LC-JOURNAL-V94.md` (mount-seul).

**RESTRICTION À PORTER** : « le gel ne ment pas par âge » vaut pour les **35 copies**, **pas
pour les 8 pièces `LC-BETA-*`**, qui n'ont jamais été confrontées faute de contrepartie
`kb/`. C'est là que vit le défaut du §4.

### 5.5 CORPUS — constat, plus inférence

La partie **CALCULÉE** est intégralement reproductible par un tiers depuis le seul dépôt. La
partie **LUE** ne l'est pas : les corps consommés par les assauts β — `2007.06800`,
`2606.09170`, `2412.00183`, `2409.08709`, `0808.2054` — **et les 4 corps intrants** sont
**ABSENTS du git**, y compris après leur re-confrontation. Sous G-4 prospectif ce n'est pas
une faute rétroactive ; **l'écart se paiera à la première bascule de branche** (§6.4).

## 6. PROCHAIN GESTE ET RESTE À FAIRE

### 6.1 Ordre de travail β — chacun sur GO séparé, jamais d'office

**Périmètre de `S-B1` — SEPT sources, arbitré le 2026-07-25, gelé et DÉPOSÉ** (amendement
nº1 puis nº2, `20290b1`).

1. ~~Décomposer l'écart des 4 corps~~ — **FAIT en S15, 4/4 concordants (§3).**
2. **`P-0` (R-41) sur les SEPT sources** — **PROCHAIN GESTE, ouverture de S16.**
   ≥3 miroirs **indépendants** (éditeurs distincts ; un agrégateur qui cite un préprint n'est
   pas un miroir de plus), **grade éditorial ÉCRIT** et non déduit, **objet vérifié et non le
   titre**, sha256 des octets consommés. **Ne pas identifier par recherche puis faire
   confirmer** : ce serait un seul témoignage corrélé. **L'issue FANTÔME est ouverte et
   honorable — R-41 a déjà intercepté un article fantôme.**
   **ANTÉRIORITÉ** : Skenderis est **déjà adjugé** (scalaire MONO-bord, muet sur le graviton
   deux-bords) — classer sous la grille **PUIS** confronter, jamais importer comme acquis
   (`FB-2`/`FB-3` non franchis), jamais reclasser en ignorant le dossier.
3. ~~Geler et déposer l'amendement de périmètre~~ — **FAIT, `20290b1`. `R-7` SATISFAIT.**
4. **`S-B1`** — positionnement **STÉRILE**, espace `C-i`/`C-ii`/`C-iii`/`C-iv` gelé, **par
   source indépendamment**. **HORS anti-fit parce qu'il ne teste RIEN** : sa protection est sa
   stérilité. **S'il conclut sur la physique, il a violé son régime.** Pare-feu `FB-1..FB-6`
   intégral. **ISSUE ANTICIPÉE, DATÉE D'AVANT, NON RETOUCHÉE** : A en `C-iii`/`C-iv` pour les
   trois ; B sans aucune ligne en `C-i`, au plus une en `C-ii` ; `S-B2` NON ARMÉ ; chantier
   refermé sur une **DÉLIMITATION — issue COMPLÈTE, pas un échec**.
5. **`S-B2`** seulement si les CINQ conditions cumulatives de `LC-BETA-03` §3 sont vraies,
   dont **au moins une source en `C-i` ou `C-ii`**. **ORDRE** : l'amendement R-7 nommant la
   classe et le scoping sont des conditions d'**ARMEMENT de `S-B2`**, **pas** des préalables à
   R-41 ni à `S-B1`. Les écrire avant obligerait à nommer une classe non établie — **c'est le
   fit.** *(Correction de rédaction déposée : `LC-BETA-03` §3 condition 3 disait « trois
   sources » ; lire « toutes les sources classées du périmètre », et par ensemble.)*
6. **Audit froid neutralisé** obligatoire sur tout nouvel objet de positivité. **En cas de
   discordance pilote / incognito, l'incognito l'emporte.**
7. **Plafond réaliste : DÉLIMITATION (`T-b`)**, rendement en baisse. `T-a` exigerait la carte
   shadow renormalisée dS-genuine graviton deux-bords, **NON EXHIBÉE à ce jour**.

### 6.2 État de `P-0` par ensemble, au 2026-07-25

- **Ensemble A** (`S8` *Bros–Moschella* / `S9` *Nakayama* / `S10` *Ghaffari–Luciano–Mantica*) :
  **RIEN N'EST FAIT.** Identités attestées **NULLE PART** (grep exhaustif 2026-07-18),
  provenance = piste article + mémoire du pilote = **deux témoins faibles et corrélés**, UN
  témoignage au sens R-54. **PDF ABSENTS, à réclamer à l'opérateur.** La fiche `LC-BETA-04`
  est **vierge**.
- **Ensemble B** (les 4 corps) : **§1.5 FAIT** (§3). Restent **§1.2, §1.3, §1.4** sur les
  quatre lignes. **Les octets sont à REFOURNIR** : le scratch de S15 ne survit pas.

### 6.3 ARBITRAGE nº1 (2026-07-25) — dissolution PAR ENSEMBLE

Déposé au corps de l'amendement nº2 §4. Résumé opposable :

1. **Condition évaluée séparément sur A et sur B, jamais globalement.** `E` est proposé à la
   dissolution si (i) aucune source **classée** de `E` n'est en `C-i` ni `C-ii`, **(ii) au
   moins une source de `E` a effectivement été classée**, (iii) aucun **levier neuf
   falsifiable et daté** n'est nommé pour `E`. **La décision appartient à l'opérateur.**
   **Symétrie** : `B` ne peut pas armer `S-B2` au motif que `A` resterait ouvert, ni
   l'inverse.
2. **Statut `SUSPENDU POUR NON-IDENTIFICATION`** : une source FANTÔME ou dont les octets
   manquent **n'est pas classable** (précondition dure R-41). Elle est **portée comme ligne
   écrite avec son motif**, **ne compte pas** au (i) et **ne satisfait pas** le (ii). Sans
   cette clause, `A` se dissoudrait **pour non-fourniture de PDF** — un fait administratif
   présenté comme un résultat.
3. **Levier falsifiable** : nommer ne suffit pas. Un levier compte s'il porte **(a)** ce
   qu'il faudrait exhiber, **(b)** le critère qui déciderait dans quel sens, **(c)** une date
   antérieure au rendu de `S-B1`. Sinon il ne compte pas.
4. **Garde anti-fit** : une clôture d'ensemble se rédige comme une **DÉLIMITATION À CONTENU
   NOMMÉ**, jamais comme un changement de statut. **Une délimitation sans contenu n'est pas
   une clôture.**

### 6.4 Reste à faire (reporté, aucun n'a bougé en S15 sauf mention)

- **PROPOSITION NON ARBITRÉE, NEUVE EN S15 — paquet ARCHIVE / atelier séparé** (amendement
  nº2 §8). Motif : la recette `PKG_SHA_BETA` hache **le contenu courant d'un répertoire** ;
  un gel sur un répertoire qui reçoit du travail **n'est pas un gel**. Sans arbitrage, le
  régime actuel reste **avec son défaut déclaré**.
- **Norme de nommage** (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION S11) : **non arbitrée**.
  Concerne aussi `LC-WORK-GEN-PAQUET-v2_1.py`. **Défaut assumé : la norme ne respecte pas sa
  propre grammaire.**
- **G-1** : 16 bundles de la décharge v2.74, 72 `.py` ; `hors-KB/A/` **non fourni**.
- **G-5b/c** : index `LC-00-INDEX` **ABSENT de `kb/`** ; arborescence des silos.
- **Sort de R-23** : MAINTIEN — corps de F5 **non ouvert**, `[D5]` LEVÉ (W3) intact. **GO
  séparé, voie (i), jamais d'office.**
- **`sources/` hors compte** au §0-lite : un répertoire non compté est un répertoire dont on
  ne détecte pas la dérive. À faire entrer dans le compte, ou à assumer.
- **REGISTRE DE CORPUS** (**NON ARBITRÉ**) : déposer un `LC-WORK-REGISTRE-CORPUS` —
  identifiant canonique + version + sha256 des octets originaux + procédure de récupération +
  assaut d'origine — **et PAS les octets**. Motifs : dépôt **PUBLIC**, licences arXiv
  hétérogènes, git conserve **tout blob pour toujours**. **Renforcé par S15** : les 4 corps
  sont désormais confrontés, donc le registre serait **exact** ; et ils ont dû être refournis
  **deux fois** faute de registre.

## 7. Discipline et précédents opposables — PORTÉS INTÉGRALEMENT

*Le précédent `860c3f8` établit qu'une formule ne suffit plus dès que la pièce porteuse est
retirée. Ils sont donc recopiés ici, et non hérités.*

### 7.1 Précédents S15

1. **UNE RÈGLE SE MESURE À SA SOURCE, PAS À SA GLOSE.** Le pilote a présenté à l'opérateur
   une contradiction `R-7` ↔ pare-feu **qui n'existait pas**, en lisant la note S14 §5 au lieu
   de `LC-BETA-05` §1. **Écart imputable au pilote.** Il a en outre proposé de **renommer une
   pièce pour passer sous un contrôle nominal** — contourner une règle au lieu d'en mesurer la
   portée. C'est le précédent S14 nº1, **commis une troisième fois**.
2. **UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE.** Le pilote a écrit un
   amendement **dans le répertoire du paquet gelé** : `PKG_SHA_BETA_8` est passé de
   `dc276129` à `687ed70b`, `N_haches` de 42 à 43, **et `LC-BETA-BOOT.py` a rendu rc=0**.
   **Écart imputable au pilote**, corrigé, valeurs re-mesurées et retrouvées.
3. **UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL**, c'est un haché mouvant. Ou le
   dossier est archive et le travail se fait ailleurs, ou son haché n'est pas une référence.
4. **UNE CONFRONTATION PAYÉE SE PRÉSERVE HORS SURFACE TOURNANTE** au moment où elle est
   obtenue. Deux des trois surfaces ont tourné pendant la seule session S15.
5. **UN ZIP DE TRANSPORT N'EST PAS UN ZIP DE SUBSTITUTION** (§3.3). Une leçon opposable se
   lit **à son cas**, sinon elle interdit ce qu'elle n'a jamais visé.
6. **UN CONTRÔLE QUI PASSE SUR L'ENSEMBLE VIDE EST UN FAUX PASS** — et sa **réciproque** : un
   contrôle qui échoue *toujours* satisfait toutes les mutations. **Il faut les deux gardes**
   (`G6` non-vacuité **et** `T0` nominal).
7. **UN GO N'EST PAS UN ARBITRAGE.** Un GO fait avancer un geste ; il ne tranche pas une
   question posée. En cas d'ambiguïté : exécuter le geste, **nommer la lecture retenue**, et
   ne rien déposer avant confirmation.
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS** après une réussite partielle. Ce qui lui donne
   son prix est sa date, pas son exactitude.

### 7.2 Précédents S14

1. **CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE.** Survenue DEUX fois
   en S14 (HEAD attendu ; homonymes ZIP présentés comme découverte alors que consignés depuis
   S10). **Le dépôt se mesure, il ne se déduit pas.**
2. **UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA DEMANDER.**
   **Demander D'ABORD, comparer ENSUITE.**
3. **UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM.**
4. **LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR** — identité de commit distincte.
5. **UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS.**
6. **UN ORDRE DE CONDITIONS NE SE COMPRIME PAS.** Une condition d'armement n'est pas un
   préalable ; les confondre fabrique du fit.

### 7.3 Précédents S13

Un chantier « à ouvrir » peut être **DÉJÀ cadré/gelé** : lire le dossier existant AVANT de
rédiger un cadrage neuf (**un brouillon rédigé dans l'ignorance du dossier se JETTE**) · un
prérequis bloquant absent de la reprise peut vivre dans le dossier : **le chercher** · un
repérage peut faire remonter de la substance : **le déclarer** · un instrument mandaté se
construit **à la LETTRE du mandat** et **se prouve par un AUTO-TEST MORDANT** (chaque garde a
un porteur mutable, sinon faux PASS) · un dépôt fait avancer HEAD et change les comptes :
**recaler §0-lite dans la reprise** · substance au git, packaging au mount = **à nommer, pas
à réconcilier d'office**.

### 7.4 Précédents S11

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.** **Imprimer** les
   coordonnées retenues ET le dernier élément inclus, et **constater** qu'il appartient au
   bloc visé.
2. **UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE.** Elle se rétracte par un fichier séparé
   daté **supplémentaire** ; l'amendement fautif **reste** au dépôt et **garde son numéro**.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.**
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.** Une convention d'unité peut
   vivre dans les **en-têtes**, invisible au flux `pdftotext`.
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.**
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.**
7. **UN TOKEN NE S'ÉCRIT NULLE PART**, et c'est **vérifié**.
8. **LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL.**

### 7.5 Précédents S10

1. **HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU.**
2. **UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN.** Écrire une correction
   et **ne pas l'appliquer** est un échec d'exécution distinct.
3. **UN ESPACE-VERDICT DÉCLARÉ EXHAUSTIF DOIT PRÉVOIR LE CAS QU'IL N'A PAS PRÉVU.** Ajouter
   une case APRÈS mesure est un risque de fit : il se nomme, se borne par un critère
   **général**, et ne vaut que si l'issue écartée l'a été par **mesure**.
4. **UNE INFORMATION LUE HORS PÉRIMÈTRE SE DÉCLARE ET NE S'EMPLOIE PAS.**
5. **LE TOKEN NE REMPLACE PAS L'ANNONCE R-55.**
6. **VÉRIFICATION DE DÉPÔT SUR CLONE NEUF**, jamais sur déclaration.
7. **UNICITÉ DE LA REPRISE**, au git comme au mount.
8. **AUTORITÉ DES PIÈCES DE GOUVERNANCE** : le git fait foi.
9. **SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE. Enregistrer n'est pas confronter.**
10. **DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL.**

### 7.6 Précédents S9 et S8

- Un **défaut du gel se nomme et s'amende par FICHIER SÉPARÉ DATÉ**, jamais en place ; la
  pièce amendée reste **byte-intacte**.
- Un harnais doit auditer la **VACUITÉ STRUCTURELLE** : un assert qu'aucun porteur mutable ne
  traverse est un **faux PASS** même s'il est vrai. En S9, **quatre faux PASS** sur un lot qui
  se présentait à 38/38.
- Un **pré-tri `[D]`/`[C]` AU GEL** interdit de reclasser après coup.
- **L'antériorité se PROUVE par l'état du répertoire**, pas par une déclaration.
- Une **cible non algébrisable se déclare AU GEL** (clause I-c).
- Un **statut de présence se MESURE** sur l'arbre modifié avant d'écrire la note.
- **Annoncé puis GO ⟹ l'annoncé fait foi** ; correction ensuite par amendement.
- **S8** : **un intrant refourni se CONFRONTE au registre AVANT extraction**, puis pièce par
  pièce.

### 7.7 Procédure R-55 de dépôt

**Ordre non négociable** : annonce **chemin + sha256 complet + message de commit**, **fichier
par fichier**, PUIS token, PUIS push. **Si le token est fourni AVANT l'annonce, l'annonce se
fait quand même et l'on attend la confirmation de l'opérateur.** Puis confrontation des sha
déposés aux sha annoncés **par `diff`, sur clone neuf**, et vérification du token à **0** —
arbre, `.git/config`, messages de commit, **et contenu de tous les blobs jamais commités**.
Autres : **lire pour présenter n'est pas ouvrir** · **une divergence se nomme et se tranche
par l'opérateur** · **borner AVANT de lire**.

## 8. G-4 — SOLDÉ (arbitrage du 2026-07-25), APPLIQUÉ en S15

> Le **mount** est l'espace vivant. Le **git** est l'espace de consignation : matériaux
> validés, résultats confirmés, **plus le matériel permettant à un tiers de REPRODUIRE**.
> **Bascule** mount → git à l'épuisement d'une branche, après **audit froid incognito**.
> **Portée PROSPECTIVE : l'existant reste en place.**

Conséquences : le packaging LC-BETA et V94 sont mount-seul **de droit** · **R-54 reste
debout** · le critère de bascule est la **reproductibilité par un tiers** · les questions de
provenance des PDF mount vs git **cessent d'être des écarts**. **Application S15** : les
pièces de gouvernance β sont allées **au git** (§5.2), et le contrôle qui les vérifie aussi.

**G-4 est clos.**

## 9. Table de supersession — ce qui a été ÉCARTÉ

| Point | Ancien (périmé) | Retenu S15 |
|---|---|---|
| HEAD attendu | S14 : commit « Reprise S14 » | **commit « Reprise S15 », vérifié par `git log`** |
| `audit/` | 42 | **45** |
| Racine | note S14 + PROMPT-S15 | **note S15 + PROMPT-OUVERTURE-S16** |
| Registre β 4 corps | S14 : NON re-confrontable, **BLOQUANT** | **RE-CONFRONTÉ 4/4, bloquant LEVÉ (§3)** |
| Pare-feu | S14 §5 : « ni au dépôt » | **glose SANS SOURCE, retirée (§5.2)** |
| Gel β | « ne ment pas par âge » | **vrai des 35 copies, FAUX des 8 pièces `LC-BETA-*` (§4, §5.4)** |
| Amendement de périmètre | à geler et déposer | **DÉPOSÉ, `20290b1` ⟹ `R-7` satisfait** |
| Dissolution | globale, défaut déclaré | **PAR ENSEMBLE + non-classifiabilité + levier falsifiable (§6.3)** |
| `LC-BETA-03` §3 cond. 3 | « trois sources » | **« toutes les sources classées du périmètre »** |
| Redémonstrations | non rejouées depuis S12 | **rejouées CONFORMES en S15** |

## 10. AUDIT DE REPORT — ce qui a été recopié avant retrait

*Précédent `860c3f8` : un retrait se précède d'un audit item par item.*

**Depuis `NOTE-REPRISE-GIT-S14.md`** (retirée au même commit) : §0 attendus **recalés** et
leçons d'environnement → **§0** · §1 historique S9→S14 → **§1** · §2 volet β intégral →
**§2** · §3 registre β → **§3, corrigé par mesure** · §4 P-8 → **§4** · §5 localisation,
paquet, corpus → **§5** · §6 prochain geste et reste à faire → **§6** · §7 précédents S14,
S13, S11, S10, S9/S8 et procédure R-55 → **§7.2 à §7.7, INTÉGRALEMENT** · §8 G-4 → **§8** ·
§9 supersession → **§9**.

**Depuis `PROMPT-OUVERTURE-S15.md`** (retiré au même commit) : ITEM 1 **réalisé** · ITEM 2
**non réalisé → §6.1(2), ouverture de S16** · ITEM 3 **réalisé** · ITEM 4 **non réalisé →
§6.1(4)** · ITEM 5 **non réalisé → §6.1(5)** · ITEM 6 gouvernance **non réalisé → §6.4,
item par item** · §7 périmètre → **§11** · §8 précédents → **§7.2** · §9 token → **§7.7**.

**Rien n'est laissé au seul héritage par formule.**

## 11. PÉRIMÈTRE — INCHANGÉ

S15 n'a produit **AUCUN mouvement scientifique** : aucune source lue, aucune ligne classée,
aucune gate tirée, aucun verdict touché.

`{ A4 ; A2★ ; N }` INCHANGÉ · `[B]` = B-PAUVRE · `W2` = DÉLIMITATION, `A4` NON réfuté,
postulat RENFORCÉ · `A2★` décision ouverte, `C7` non levée · `D1` non clos, conclusion `D1c`
INTACTE · `N` non fixé (≡ Λ, `R-53` : 0/4) · `O₂` non construit · β `T-b`, NON RÉSOLU, SEUL
facteur d'O₂ ouvert · `G3-a` non levé · nœud (i) INDÉTERMINÉ (pas A) · Silo R CLOS À 12/12 ·
**CCC non démontrée NI réfutée**. Plafond réaliste de β : **DÉLIMITATION (`T-b`)**, rendement
EN BAISSE.

---

*§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, arbitrer, geler, déposer,
retirer, consolider : aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi
que ce soit. Confronter des octets n'identifie aucun article. Lever un bloquant n'ouvre
aucune gate. β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni
réfutée.***
