---
id: NOTE-REPRISE-GIT-S14
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S14 (2026-07-25). Consolide et REMPLACE NOTE-REPRISE-GIT-S13 et son AMENDEMENT-1 ; les notes S9–S13 vivent dans l'historique git. ACQUIS S14, tous ADMINISTRATIFS : G-4 TRANCHÉ (régime bi-espace, portée prospective) ; périmètre de S-B1 arbitré aux DEUX ensembles ; paquet β reçu et vérifié, gel confronté 34/35 byte-identiques ; §0-lite exécuté sur clone neuf, CONFORME ; swap d'unicité −S11 −PROMPT-S12 exécuté. ZÉRO mouvement scientifique : aucune source lue, aucune gate tirée, aucun verdict touché. PROCHAIN GESTE : décomposer l'écart des 4 corps β (BLOQUANT), puis P-0 (R-41) sur les sept sources. JAMAIS d'office."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S13.md et NOTE-REPRISE-GIT-S13-AMENDEMENT-1.md, retirés de la racine au même commit. Une seule note de reprise doit exister, au git comme au mount (règle d'unicité)."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture d'une session neuve : HEAD = le commit dont le message commence par « Reprise S14 », à vérifier par `git log`, JAMAIS par cette note. Ses parents remontent par b4af0c5 (swap d'unicité), 8caafa7 (amendement 1), 09d9e2a (Reprise S13), cad358a (Sold P-8), af97865 (Reprise S11). EN S14 CE PIÈGE A MORDU : S13 annonçait HEAD = cad358a « tant que S13 n'est pas déposée », alors qu'elle l'était — une note peut mentir par âge SUR SON PROPRE ATTENDU."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise. Les notes S9–S13 sont périmées et vivent dans l'historique git. Tout ce qui n'est pas réalisé en reprise N est REPORTÉ en N+1, jamais laissé en coexistence. Un amendement daté n'est pas une seconde note : il est indissociable de la sienne."
autorite: "RÉGIME G-4, TRANCHÉ le 2026-07-25, portée PROSPECTIVE. Le MOUNT est l'espace vivant : conduite de projet, matériaux en cours, éléments intermédiaires d'une branche non finalisée ni épuisée. Le GIT est l'espace de consignation : matériaux validés et vérifiés, résultats confirmés et audités, accompagnés du matériel permettant à une instance tierce de REPRODUIRE. Bascule mount → git à l'épuisement d'une branche, après audit froid incognito. L'EXISTANT RESTE EN PLACE. R-54 reste debout. Pour les pièces de GOUVERNANCE (prompts, notes de reprise, amendements), le dépôt git fait foi."
supersede: "Points où S14 corrige S13 : piège R-36 (cad358a → commit « Reprise S14 ») ; §8 G-4 « non tranchée » → TRANCHÉE, §8 ci-dessous ; §7 qui héritait des précédents PAR FORMULE → §7 les porte INTÉGRALEMENT ; §3 registre β « référence de première mesure » → NON RE-CONFRONTABLE, voir §3."
---

# Note de reprise S14 (consolidée, CLÔTURE) — état, acquis, prochain geste

> **Pourquoi cette note existe.** S13 a été déposée sans prompt d'ouverture et
> sans exécuter son propre swap d'unicité : la racine portait DEUX notes de
> reprise. S14 a soldé les deux manques, tranché G-4, arbitré le périmètre de
> `S-B1`, et vérifié le paquet β. Elle absorbe S13 et l'amendement 1, dont le
> contenu est repris ici sans perte.

## 0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S14

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -6   # HEAD = message commençant par « Reprise S14 »,
                           # puis b4af0c5, 8caafa7, 09d9e2a, cad358a, af97865
    ls instruments/*.py | wc -l                    # attendu : 34
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

**Total INCHANGÉ : 271/271 PASS + 101 consignations, 12/12 rc = 0.**
Décomposition pour recompte indépendant :
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` ;
`5+5+6+6+8+7+3+10+14+10+8+19 = 101`. Rejoué CONFORME en S9–S12.
**NON REJOUÉES en S13 ni en S14** (aucune des deux n'a touché aux
redémonstrations) — **à rejouer en S15**.

Les six comptes ci-dessus ont été **exécutés sur clone neuf le 2026-07-25 et
sont CONFORMES**. Les dépôts de S14 n'ont porté que sur des pièces de racine,
hors des cinq comptes : **aucun recalage de compte n'est dû.**

Hors compte §0-lite, rejeux de confirmation, tous CONFORMES en S14 :

    python3 instruments/harnais_R9.py    # « 6/6 mordantes », rc=0
    python3 instruments/harnais_R11.py   # « 7/7 mordantes » + « VACANTES: 0 », rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py   # rc=0 ; sha256 script = 8e386686
    python3 instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test  # 6/6 mordantes, rc=0

Intrants `sources/` — **CONFRONTÉS ET CONCORDANTS en S14**, vrais PDF (magie
`%PDF`), sha de première mesure faisant référence :

    2312_12498v2.pdf  1 895 152 o  sha8=04d9b4f4
    2409_10595v2.pdf  2 332 898 o  sha8=27a94980
    2503_19957v1.pdf    910 410 o  sha8=113ab4a2

**Toute réapparition SE CONFRONTE à ces valeurs. Enregistrer n'est pas
confronter.**

### Leçons d'environnement opposables (S2–S14, toutes maintenues)

`setsid nohup` pour rejeu long ; `ls audit/` pas `ls audit/*.md` ; jamais deux
sceaux dans le même arbre ; les durées ne sont pas des clés de sceau ;
`origin/front-pq` résiduelle et bénigne, ne pas y toucher ;
`inventaire_sceaux.py` réécrit sa date (restaurer par `git checkout`) ;
`redemo_R6_nongauss.py` imprime sans crochets (recompte au motif tolérant
`^\s*\[?PASS\]?`) ; `harnais_R11.py` crée `instruments/__pycache__/` à
nettoyer ; `pgrep -f` **s'auto-matche** et `[p]ython3` ne protège **pas** du
shell englobant ; `simplify` **non borné** ; outillage PDF `pdfplumber` 0.11.9,
`pdftoppm`/`pdfinfo`, Pillow présents, **`pymupdf` ABSENT**, `extract_words`
**mensonger** sur les mathématiques affichées — descendre au niveau `chars` ;
`${PIPESTATUS[…]}` est un bashism qui casse sous `/bin/sh` — chaîner par `;` ;
un **paquet ZIP de TEXTES extraits ne permet PAS la confrontation octet** (il
répond à la question du CONTENU, et il faut le dire).

**Réseau.** L'allowlist de `bash` **NE COUVRE PAS `arxiv.org`** ; `github.com`
**EST** couvert (clone, dépôt, push OK). **NEUF S14 :** les outils de
recherche/fetch web sont un **canal SÉPARÉ**, non soumis à cette allowlist —
pages éditeur, INSPIRE, ADS et arXiv y sont atteignables. La fiche
`LC-BETA-04` §2 affirme le contraire : **défaut d'âge**, corrigé par
l'amendement de périmètre β §3 (mount). Conséquence pratique inchangée : **les
PDF consommés viennent de l'opérateur.**

**Token.** Passé **en ligne**, jamais au disque, jamais dans `.git/config`,
jamais dans un commit — **et vérifié à 0 après usage**. Révoqué après usage :
la conversation en conserve la chaîne, la révocation est la seule opération qui
la rende inerte. **Le dépôt est PUBLIC** : le clone anonyme suffit, le token
n'est requis que pour l'écriture.

## 1. Historique des acquis (S9 → S14), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2), volet 1 (V6) et volet 1-bis ([D5]
  LEVÉ, W3) clos et déposés. Détail intégral en historique git.
- **S12** (mount-seul, jamais déposée) : VOLET 2 arbitré = β/P-1 ; sort de R-23
  = MAINTIEN (corps de F5 non ouvert). Ces acquis TIENNENT.
- **S13** : β ouvert sous discipline ; brouillon de cadrage neuf **ÉCARTÉ** (le
  dossier LC-BETA préexistant fait foi) ; deux divergences tranchées —
  intrants β = les 4 corps, route δ **DISPONIBLE** ; prérequis **P-8 surfacé,
  SOLDÉ et DÉPOSÉ** (`cad358a`).
- **S14 — administrative en totalité.**
  1. **G-4 TRANCHÉ**, portée prospective (§8). Solde la question ouverte de S13.
  2. **Périmètre de `S-B1` arbitré : LES DEUX ENSEMBLES** (§6.1).
  3. **Paquet β reçu et vérifié** (§5). Gel de dossier confronté au `kb/` :
     **34/35 byte-identiques, 0 divergente**.
  4. **§0-lite exécuté sur clone neuf : CONFORME sur toute la ligne.**
  5. **Swap d'unicité −S11 −PROMPT-S12 exécuté** (`b4af0c5`), précédé d'un
     audit de report item par item.
  6. **Prompt d'ouverture S15 déposé** — S13 n'en avait pas produit.

## 2. VOLET β (P-1) — état RÉEL, substance au git `kb/`

- **β ≡ G3 = transport AdS→dS (« T-b ») de la jonction Δ_𝒞 / gate C1, Λ>0** ;
  **seul facteur d'O₂ ouvert** ; O₂ (CFT de raccordement) À INVENTER.
- **`α` est SOLDÉ** : `α = C1-b` **POSITIF**, `p` **LIBRE** — famille à un
  paramètre, pas une construction unique ⟹ **le résidu d'O₂ se réduit
  EXACTEMENT et uniquement à β**.
- **Verdicts de transport rendus** (`LC-D-G3-TRANSPORT`) : `S-G3T-1` = T-b
  (mur en `TG-3`) ; `S-G3T-2` = T-b, mur **RE-SITUÉ** (wedge `2007.06800` =
  AdS/BCFT, perd le dictionnaire en dS genuine) ; `S-G3T-3b` (`2606.09170`,
  `2412.00183`) = T-b, **`R4′ ✓✓`** ; `S-G3T-4b` (ST `2409.08709` + de Haro
  `0808.2054`) = T-b, **`R3″ ✓ ACQUIS`** ; `§7quinquies` (levier
  d'admissibilité) = **`K-B` PRESCRIPTION-DÉPENDANT**, ne décide dans aucun
  sens — **ne pas le rejouer en croyant l'ouvrir**.
- **Le mur, nommé.** Caveat d'admissibilité de **de Haro p.3** : le graviton
  mixed/Neumann n'est admissible que dans la **fenêtre BF / Ishibashi-Wald**
  **ou** sous **cutoff** ; sinon le mode lent est non-normalisable, forcé
  Dirichlet. ST = branche **cutoff** (échoue `R4″`) ; de Haro = branche
  **fenêtre AdS₄** (échoue le dS-genuine). Chaque candidat ne couvre qu'un
  **sous-ensemble PROPRE**. `R3″` acquis ⟹ **gap résiduel = UNE seule cellule :
  `R1″ ∧ R2″ ∧ R4″`**, le plus net jamais atteint.
- **Pourquoi `T-b` et non `T-c`.** `T-c` exigerait de **PROUVER** l'absence de
  version renormalisée pour le graviton deux-bords en dS genuine. La caveat est
  un **lean structurel FORT** — un quasi-théorème. **Lean ≠ preuve** (`FB-5` :
  la tentation de convertir est le biais principal du chantier).
- **Levier NOMMÉ, NON ARMÉ** : une **preuve** d'(in)admissibilité du graviton
  propageant mixed-BC **deux-faces** au `𝓘⁺` **genuine**, **sans cutoff**.
  Non-admissible ⟹ `T-c`. Admissible ⟹ construction neuve à bâtir.
- **Cadrage figé, anti-fit** (`LC-WORK-CADRAGE-G3-HORS-WEDGE`, sha des octets
  `37bc85e5…`) : cibles **TH-1…TH-4** + firewall **TH-R**, issues
  **T-a / T-b / T-c**, gel amont réutilisé `b5276e68…f175eb`, critère
  TRIPARTITE (défaut = délimitation), **rendement attendu EN BAISSE**.
  **NE PAS re-geler, NE PAS inventer d'espace neuf** — la reprise est ce qui
  rend le 5ᵉ assaut comparable aux quatre précédents.
- **Candidats genuine-dS deux-bords ARMÉS, NON LUS**, HORS périmètre de
  `S-B1` : patch statique / deux horizons étirés ; dS/CFT & renorm au bord
  futur ; bootstrap cosmologique ; holographie céleste. Les faire entrer
  exigerait un amendement daté.
- **Deux routes** (P-sélecteur, P-3/HOLD) : (α) transport au pas C1-b
  **renormalisé** — refermée sauf ingrédient neuf, **P-8 désormais présent** ;
  (δ) invariance du poids `b` d'Odak–Speziale sous Λ<0→Λ>0 — **OUVERTE**.
- **Risques amont déclarés** : **DESI DR2 (2025)** met sous tension la
  constance de Λ — si Λ n'est pas constant, **β ne s'ouvre pas, la question
  change** · **`Δ-C` est plus étroit que son libellé** (S7 : `S-2` = FIDÈLE
  MAIS PLUS ÉTROIT, le blocage **n'est pas établi au secteur graviton**) ·
  **`p` reste libre**, P-sélecteur PENDANT sous constat BIAISÉ, **ne pas s'y
  appuyer**.
- **Anti-circularité `K`** : β prend `+i` (Bunch-Davies) et WCH (sens `D→N`)
  comme **données POSÉES**. Aucune cible ne peut présupposer `A4` comme
  résultat.

## 3. Registre de première mesure β — NON RE-CONFRONTABLE, écart BLOQUANT

Registre déclaré « mesuré au mount le 2026-07-24 » :

    2503_09372v2.pdf    979 890 o  sha256=6b89e638…a8ef62
        identifiant canonique arXiv:2503.09372v2   (FH-II)
    1909_11703v2.pdf    386 010 o  sha256=e080c5d6…c8e87d7
        identifiant canonique arXiv:1909.11703v2   (Horowitz–Wang)
    2402_04308v2.pdf  4 629 572 o  sha256=1426146d…9039d2
        identifiant canonique arXiv:2402.04308v2   (Liu–Santos–Wiseman)
    2312_17316v2.pdf  1 223 061 o  sha256=7102dcf9…370541
        identifiant canonique arXiv:2312.17316v2   (Skenderis)

**Identifiants canoniques et noms de fichiers sont deux choses distinctes.**
Le nom de fichier n'atteste rien ; l'identifiant + version est ce que R-41
confronte aux miroirs et ce qu'un registre de corpus doit porter.

**Mesuré au mount le 2026-07-25 : les quatre divergent**, en sha ET en taille
(5 788 510 / 2 314 720 / 12 826 775 / 12 680 806 o, soit ×3 à ×10). **Cause
structurelle : ce ne sont pas des PDF mais des archives ZIP** (magie
`PK\x03\x04`) de JPEG page à page + OCR + 1 `.json`.

**CE FAIT EST DÉJÀ CONSIGNÉ, il n'est pas neuf** : `3419d49` (S10, « homonymes
du mount : archives ZIP de rendu page à page, aucune entrée PDF, confrontation
octet C-3 NON CONCLUANTE ») et `af97865` (S11, « la surface `/mnt/project` a
CHANGÉ DE NATURE et expose désormais des `.pdf` directs »). La surface du mount
**alterne**. S14 l'a présenté comme une découverte bloquante : **écart imputable
au pilote (§7).**

⟹ **Le registre des 4 corps n'est pas re-confrontable en l'état.** Il faut les
**PDF ORIGINAUX**, fournis par l'opérateur. Le re-zippage explique qu'un sha
bouge ; il n'explique pas un facteur 10. **BLOQUANT pour `S-B1` sur
l'ensemble B.** Un ZIP de JPEG a un sha **non reproductible par un tiers** —
donc impropre à toute bascule sous G-4.

Extractions texte au mount (`2503_09372v2_OCR.txt`, `2402_04308v2.txt`) :
**NON LUES**. Les lire serait consommer le corpus avant la gate.

## 4. P-8 — fait, et ce que P-9 réserve

- **Déposé** : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`, sha256
  `7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`,
  commit `cad358a`. Auto-test **6/6 mordantes**, **rejoué CONFORME en S14**.
- **À la lettre du mandat** : (i) deux tranches nommées, refus tranche unique
  par défaut ; (ii) tranche unique seulement sur `--inapplicable`, clause P-6
  écrite VERBATIM ; (iii) scan P-7 de la tranche 1 → exit≠0 ; (iv) champ
  `REGIME` toujours au manifeste ; + test matériel P-1.
- **P-9** : le dépôt n'atteste QUE l'existence de l'instrument. **Sa valeur se
  mesure À LA PROCHAINE GATE** — la tranche 2 a-t-elle été expédiée APRÈS
  l'issue de Phase 2, oui/non. Écrire l'instrument ne solde pas la gate.
- **Défaut de nom déclaré** : `…-v2_1.py` porte une version DANS le nom,
  contraire à la norme *proposée* (non arbitrée) — à régulariser si la norme
  est adoptée, jamais d'office.

## 5. Localisation git / mount — constat mesuré en S14

- **Au git `kb/`** (215, conforme) : toute la substance β —
  `LC-D-G3-TRANSPORT`, `LC-WORK-CADRAGE-G3-HORS-WEDGE`, `LC-D-O2-*`,
  `LC-D-O2-P-SELECTEUR`, le mandat P-8 `LC-WORK-AMENDEMENT-R7-LIVRAISON-
  SEQUENCEE`.
- **Au git `instruments/`** : générateur v1.0 `LC-WORK-GEN-PAQUET-CSE2.py` +
  v2.1 `LC-WORK-GEN-PAQUET-v2_1.py`.
- **Au git `sources/`** : 3 PDF, tous rattachés à `R-11`/`R-23`.
- **MOUNT-SEUL, conforme au régime G-4** : le **packaging LC-BETA** (8 pièces)
  et le **journal V94**. Vérifié en S14 : **absents du git**.
- **PAQUET β vérifié en S14** — `LC-BETA-PAQUET.zip` sha256 `bbfee7b5…`,
  43 fichiers. `LC-BETA-BOOT.py` rc=0 : **42 hachés, 35 copies, 0 absente,
  0 altérée, pare-feu 0/0, `PKG_SHA_BETA_8 = dc276129`**.
  **Confrontation du gel au `kb/` du dépôt : 34/35 BYTE-IDENTIQUES,
  0 DIVERGENTE**, seule absente `LC-JOURNAL-V94.md` (mount-seul).
  **Le gel NE MENT PAS PAR ÂGE sur la substance.**
  **PARE-FEU** : aucun `LC-BETA-*` ni `BETA-COPIE-*` ne réside JAMAIS sur le
  mount principal ni au dépôt. Le paquet vit dans **son projet séparé**.
- **CORPUS — constat, plus inférence.** La partie **CALCULÉE** du programme est
  intégralement reproductible par un tiers depuis le seul dépôt (instruments,
  archives scellées, `sources/`). La partie **LUE** ne l'est pas : les corps
  consommés par les assauts β — `2007.06800`, `2606.09170`, `2412.00183`,
  `2409.08709`, `0808.2054` — et les 4 corps intrants **sont ABSENTS du git**.
  Un tiers ne peut pas vérifier la fidélité de ces lectures ; il ne peut que
  croire le pilote. **Sous G-4 prospectif ce n'est PAS une faute rétroactive**,
  mais l'écart se paiera à la première bascule de branche (§6.2).

## 6. PROCHAIN GESTE ET RESTE À FAIRE

### 6.1 Ordre de travail β — chacun sur GO séparé, jamais d'office

**Périmètre de `S-B1` — ARBITRÉ le 2026-07-25 : LES DEUX ENSEMBLES.**
*Ensemble A* : `S8`/`S9`/`S10`, pistes *Bros–Moschella*, *Nakayama*,
*Ghaffari–Luciano–Mantica* — **identités attestées NULLE PART** sur le mount
(grep exhaustif 2026-07-18), issues de la piste article + mémoire du pilote,
**deux témoins faibles et corrélés** (R-54 : UN témoignage). **PDF absents, à
réclamer à l'opérateur.** *Ensemble B* : les 4 corps du §3.
**Aucun espace de classement ni de verdict n'est ouvert par cet arbitrage.**

1. **Décomposer l'écart des 4 corps** (§3). **BLOQUANT.**
2. **`P-0` (R-41)** sur les sept sources : ≥3 miroirs **indépendants**
   (éditeurs distincts ; un agrégateur qui cite un préprint n'est pas un miroir
   de plus), **grade éditorial ÉCRIT** et non déduit, **objet vérifié et non le
   titre**, sha256 des octets consommés. **Ne pas identifier par recherche puis
   faire confirmer** : ce serait un seul témoignage corrélé. **L'issue FANTÔME
   est ouverte et honorable — R-41 a déjà intercepté un article fantôme.**
   **ANTÉRIORITÉ** : Skenderis est **déjà adjugé** au dossier (scalaire
   MONO-bord, muet sur le graviton deux-bords) — le classer sous la grille
   **PUIS confronter**, jamais l'importer comme acquis (`FB-2`/`FB-3` non
   franchis), jamais le reclasser en ignorant le dossier.
3. **GELER ET DÉPOSER l'amendement de périmètre β** (mount, sha256
   `33c7cac6…`, §1 à corriger après l'item 1) **AVANT toute lecture**. Sans
   dépôt antérieur auditable par un tiers, **tout classement est du FIT**.
4. **`S-B1`** — positionnement **STÉRILE**, espace `C-i`/`C-ii`/`C-iii`/`C-iv`
   gelé, **par source indépendamment**. **HORS anti-fit parce qu'il ne teste
   RIEN** : sa protection est sa stérilité. **S'il conclut sur la physique, il
   a violé son régime.** Pare-feu `FB-1..FB-6` intégral (régularisé ≠
   renormalisé · mono-bord ≠ deux-faces · scalaire ≠ graviton Einstein
   propageant · cutoff ≠ genuine · lean ≠ preuve · prescription-dépendance).
   **ISSUE ANTICIPÉE, DATÉE D'AVANT** : A en `C-iii`/`C-iv` pour les trois ;
   B sans aucune ligne en `C-i`, au plus une en `C-ii` ; **`S-B2` NON ARMÉ** ;
   chantier refermé sur une **DÉLIMITATION — issue COMPLÈTE, pas un échec**.
5. **`S-B2`** seulement si les CINQ conditions cumulatives de `LC-BETA-03` §3
   sont vraies, dont **au moins une source en `C-i` ou `C-ii`**. Alors
   seulement : amendement R-7 nommant **la classe désignée et elle seule**,
   scoping gelé, **livraison séquencée par le générateur v2.1** — c'est là, et
   pas avant, que **P-9 MESURERA P-8**.
   **ORDRE, corrigé en S14** : l'amendement R-7 et le scoping sont des
   conditions d'**ARMEMENT de `S-B2`**, **pas** des préalables à R-41 ni à
   `S-B1`. Les écrire avant `S-B1` obligerait à nommer une classe non encore
   établie — **c'est le fit**. S13 §6.1 comprimait cet ordre ; le cadrage du
   paquet est plus précis et il gagne.
6. **Audit froid neutralisé** obligatoire sur tout nouvel objet de positivité.
   **En cas de discordance pilote / incognito, l'incognito l'emporte.**
7. **Plafond réaliste : DÉLIMITATION (`T-b`)**, rendement en baisse. `T-a`
   exigerait la carte shadow renormalisée dS-genuine graviton deux-bords,
   **NON EXHIBÉE à ce jour**.

**NON ARBITRÉ, à poser à l'opérateur : la DISSOLUTION PAR ENSEMBLE.** Sans
elle, passer de 3 à 7 sources **affaiblit mécaniquement** la condition de
dissolution de `LC-BETA-05` §5 (conjonction sur toutes les sources ; et B est
**pré-sélectionné** pour sa pertinence supposée alors que A a été retenu pour
la synthèse d'un article) — **et laisse B masquer une éventuelle réfutation de
A**. Or `LC-BETA-05` §4 écrit que **réfuter une hypothèse du pilote est le
meilleur usage connu de ce programme**.

### 6.2 Reste à faire (reporté)

- **Norme de nommage** (`audit/LC-NORME-NOMMAGE.md`, PROPOSITION S11) : **non
  arbitrée**. Grammaire `<SUJET>-<TYPE>[-AMENDEMENT-<n>]`, vocabulaire de TYPE
  fermé, version hors du nom, nom sans extension identique au champ `id:` ;
  deux exceptions nommées (`PROMPT-OUVERTURE-S<n>`, `NOTE-REPRISE-GIT-S<n>`).
  Migration de 7 pièces de `audit/` (22 sur 41 déjà conformes) ; **`kb/`
  EXCLU** ; concerne aussi `LC-WORK-GEN-PAQUET-v2_1.py`. **Défaut assumé : la
  norme ne respecte pas sa propre grammaire.**
- **G-1** : 16 bundles de la décharge v2.74, 72 `.py` ; `hors-KB/A/`
  (`LC-A-SURVIE-CONFORME`) **non fourni** — `hors-KB/` ne contient que `B`.
- **G-5b/c** : index `LC-00-INDEX` **ABSENT de `kb/`** ; arborescence des silos.
- **Sort de R-23** : MAINTIEN — corps de F5 **non ouvert**, fond ni confirmé ni
  infirmé, `[D5]` LEVÉ (W3) intact. **GO séparé, voie (i), jamais d'office.**
- **`sources/` est « hors compte »** au §0-lite : un répertoire non compté est
  un répertoire dont **on ne détecte pas la dérive**. À faire entrer dans le
  compte, ou à assumer explicitement.
- **REGISTRE DE CORPUS** (§5, proposition **NON ARBITRÉE**) : déposer un
  `LC-WORK-REGISTRE-CORPUS` — identifiant canonique + version + sha256 des
  octets originaux + procédure de récupération + assaut d'origine — **et PAS
  les octets**. Motifs : le dépôt est **PUBLIC** (redistribution, licences
  arXiv hétérogènes) ; git conserve **tout blob binaire pour toujours** et
  chaque `git clone` futur paierait le coût, sans retour possible sans
  réécrire l'historique (ce qui détruirait l'antériorité des commits
  consignés) ; un registre est **falsifiable**, un PDF déposé ne prouve rien de
  sa provenance.

## 7. Discipline et précédents opposables — PORTÉS INTÉGRALEMENT

*S13 §7 héritait PAR FORMULE. Le précédent `860c3f8` établit qu'une formule ne
suffit plus dès que la pièce porteuse est retirée. Ils sont donc recopiés ici.*

### 7.1 Précédents S14

1. **CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE.**
   Survenue **DEUX FOIS** en S14 : sur HEAD (S13 annonçait `cad358a` alors
   qu'elle était déposée), et sur les homonymes ZIP du mount, présentés comme
   découverte bloquante alors qu'ils sont consignés depuis S10. **Le dépôt se
   mesure, il ne se déduit pas.**
2. **UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA
   DEMANDER.** Le pilote a imprimé `PKG_SHA_BETA_8` avant de réclamer la valeur
   hors-fichier : la confirmation obtenue est **indistinguable d'un écho**,
   donc **NON OPPOSABLE** (R-36, R-54). **Demander D'ABORD, comparer ENSUITE.**
3. **UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM.** Une pièce
   périmée peut être la **pièce de report** d'autres sessions.
4. **LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR** — identité de commit
   distincte.
5. **UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS.** L'existant reste ; on
   ne réorganise pas le dépôt d'office.
6. **UN ORDRE DE CONDITIONS NE SE COMPRIME PAS.** Une condition d'armement
   n'est pas un préalable ; les confondre fabrique du fit.

### 7.2 Précédents S13

Un chantier « à ouvrir » peut être **DÉJÀ cadré/gelé** : lire le dossier
existant AVANT de rédiger un cadrage neuf (**un brouillon rédigé dans
l'ignorance du dossier se JETTE, il ne se dépose pas**) · un prérequis bloquant
absent de la reprise peut vivre dans le dossier : **le chercher** avant de tirer
une gate · un repérage « locate » peut faire remonter de la substance : **le
déclarer** · un instrument mandaté se construit **à la LETTRE du mandat**
(cibles figées = antériorité, pas de gel neuf) et **se prouve par un AUTO-TEST
MORDANT** (chaque garde a un porteur mutable, sinon faux PASS) · un dépôt fait
avancer HEAD et change les comptes : **recaler §0-lite dans la reprise** ·
substance au git, packaging au mount = **à nommer, pas à réconcilier d'office**.

### 7.3 Précédents S11

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.**
   Quatre occurrences en un seul volet, APRÈS recopie de la leçon S10 dans le
   gel. **Imprimer** les coordonnées retenues ET le dernier élément inclus, et
   **constater** qu'il appartient au bloc visé.
2. **UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE.** Elle se rétracte par un
   fichier séparé daté **supplémentaire** ; l'amendement fautif **reste** au
   dépôt et **garde son numéro**. On ne modifie pas un amendement, même erroné.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.** Le réordonner après
   mesure serait le fit qu'il interdit.
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.** Une
   convention d'unité peut vivre dans les **en-têtes**, invisible à la légende,
   aux cellules et au flux `pdftotext`.
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.**
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.**
7. **UN TOKEN NE S'ÉCRIT NULLE PART**, et c'est **vérifié**.
8. **LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL.**

### 7.4 Précédents S10

1. **HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU.** La confrontation d'un
   intrant se fait au niveau **octet** et ne demande **aucune** lecture.
2. **UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN.** Écrire
   une correction et **ne pas l'appliquer** est un échec d'exécution distinct,
   et il s'impute pareillement.
3. **UN ESPACE-VERDICT DÉCLARÉ EXHAUSTIF DOIT PRÉVOIR « LES DEUX PARTIES ONT
   TORT ».** Ajouter une case APRÈS mesure est un risque de fit : il se nomme,
   se borne par un critère **général**, et ne vaut que si l'issue écartée l'a
   été par **mesure** et non par redéfinition.
4. **UNE INFORMATION LUE HORS PÉRIMÈTRE SE DÉCLARE ET NE S'EMPLOIE PAS.**
5. **LE TOKEN NE REMPLACE PAS L'ANNONCE R-55.**
6. **VÉRIFICATION DE DÉPÔT SUR CLONE NEUF**, jamais sur déclaration.
7. **UNICITÉ DE LA REPRISE**, au git comme au mount.
8. **AUTORITÉ DES PIÈCES DE GOUVERNANCE** : le git fait foi, le mount vaut
   copie de travail.
9. **SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE** (§0). **Enregistrer n'est pas
   confronter.**
10. **DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL.**

### 7.5 Précédents S9 et S8

- Un **défaut du gel se nomme et s'amende par FICHIER SÉPARÉ DATÉ**, jamais en
  place ; la pièce amendée reste **byte-intacte**.
- Un harnais doit auditer la **VACUITÉ STRUCTURELLE** : un assert qu'aucun
  porteur mutable ne traverse est un **faux PASS** même s'il est vrai. En S9,
  **quatre faux PASS** sur un lot qui se présentait à 38/38.
- Un **pré-tri `[D]`/`[C]` AU GEL** interdit de reclasser après coup.
- **L'antériorité se PROUVE par l'état du répertoire**, pas par une déclaration.
- Une **cible non algébrisable se déclare AU GEL** (clause I-c).
- Un **statut de présence se MESURE** sur l'arbre modifié avant d'écrire la
  note qui le déclare.
- **Annoncé puis GO ⟹ l'annoncé fait foi** ; correction ensuite par amendement,
  jamais en silence.
- **S8** : **un intrant refourni se CONFRONTE au registre AVANT extraction**,
  puis pièce par pièce.

### 7.6 Procédure R-55 de dépôt

**Ordre non négociable** : annonce **chemin + sha256 complet + message de
commit**, **fichier par fichier**, PUIS token, PUIS push. **Si le token est
fourni AVANT l'annonce, l'annonce se fait quand même et l'on attend la
confirmation de l'opérateur.** Puis confrontation des sha déposés aux sha
annoncés **par `diff`, sur clone neuf**, et vérification du token à **0**.
Autres : **lire pour présenter n'est pas ouvrir** · **une divergence se nomme
et se tranche par l'opérateur** · **borner AVANT de lire**.

## 8. G-4 — SOLDÉ (arbitrage opérateur du 2026-07-25)

Question posée depuis S10, reconduite en S11, S12 et S13. **Tranchée.**

> Le **mount** est l'espace vivant : conduite de projet, matériaux en cours,
> éléments intermédiaires d'une branche non finalisée ni épuisée. Le **git** est
> l'espace de consignation : matériaux validés et vérifiés, résultats confirmés
> et audités, accompagnés du matériel permettant à une instance tierce de
> **REPRODUIRE**. **Bascule** mount → git à l'épuisement d'une branche, après
> **audit froid incognito**. **Portée PROSPECTIVE : l'existant reste en place.**

Conséquences : la clause d'exception de S13 devient une **règle** · le
packaging LC-BETA et V94 sont mount-seul **de droit** · **R-54 reste debout** ·
le critère de bascule est la **reproductibilité par un tiers**, ce qui rend
recevable seulement un matériel complet (données + instruments + procédure) —
d'où le registre de corpus proposé en §6.2 · les questions de provenance des
PDF mount vs git **cessent d'être des écarts** et deviennent la description du
régime.

**Non couvert par l'arbitrage, et laissé ouvert** : rien. G-4 est clos.

## 9. Table de supersession — ce qui a été ÉCARTÉ

| Point | Ancien (périmé) | Retenu S14 |
|---|---|---|
| HEAD attendu | S13 : `cad358a` « tant que S13 n'est pas déposée » | **commit « Reprise S14 », vérifié par `git log`** |
| Racine | S11 + S13 + PROMPT-S12 coexistants | **note S14 seule + PROMPT-OUVERTURE-S15** |
| G-4 | question ouverte (S10→S13) | **TRANCHÉE, prospective (§8)** |
| Précédents | S13 : héritage PAR FORMULE | **portés intégralement (§7)** |
| Périmètre `S-B1` | non arbitré | **les DEUX ensembles (§6.1)** |
| Registre β 4 corps | S13 : « référence de première mesure » | **NON re-confrontable, écart bloquant (§3)** |
| Ordre R-7 / scoping | S13 §6.1 : « avant de lire tout corpus » | **conditions d'ARMEMENT de `S-B2` (§6.1.5)** |
| Paquet β | non vérifié | **BOOT rc=0, gel 34/35 byte-identiques (§5)** |

---

*§6.4 — sentinelle terminale. Ouvrir, cadrer, geler, solder un instrument,
déposer, retirer, consolider une note : aucun de ces gestes ne scelle, ne
réduit, ne compte, ne démontre quoi que ce soit. { A4 ; A2★ ; N } INCHANGÉ ·
[B] = B-PAUVRE · W2 = DÉLIMITATION, A4 NON réfuté · A2★ décision ouverte, C7
non levée · D1 non clos, D1c intacte · N non fixé (≡ Λ, R-53 0/4) · O₂ non
construit · β `T-b`, NON RÉSOLU, SEUL facteur d'O₂ ouvert · G3-a non levé ·
nœud (i) INDÉTERMINÉ (pas A) · Silo R CLOS à 12/12 · CCC non démontrée NI
réfutée.*
