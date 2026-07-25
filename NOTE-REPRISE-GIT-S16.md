---
id: NOTE-REPRISE-GIT-S16
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S16 (2026-07-25). Consolide et REMPLACE NOTE-REPRISE-GIT-S15 ; les notes S9–S15 vivent dans l'historique git. ACQUIS S16 : §0-lite CONFORME redémonstrations comprises ; P-0 (R-41) RENDU sur les SEPT sources, issue FANTÔME écartée par mesure 0/7 ; ARBITRAGE OPÉRATEUR nº3 (S9/S10 classables sous réserve écrite) ; REGISTRE DE CORPUS déposé ; paquet β rendu NON-REFOURNISSABLE par table de concordance et dépôt des 8 pièces de gouvernance. AUCUN mouvement scientifique : aucune ligne classée, aucune gate tirée, aucun verdict touché. PROCHAIN GESTE : S-B1, positionnement STÉRILE. JAMAIS d'office."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S15.md, retirée de la racine au même commit, après AUDIT DE REPORT item par item (§10)."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture d'une session neuve : HEAD = le commit dont le message commence par « Reprise S16 », à vérifier PAR `git log`, JAMAIS par cette note. Ses parents remontent par 11e924e (P-0 rendu), 5f9874c (Reprise S15), 20290b1, 1c90daf, b4af0c5, 8caafa7, 09d9e2a, cad358a. EN S14 CE PIÈGE A MORDU. En S15 et S16 il n'a PAS mordu, parce que HEAD a été MESURÉ avant d'être lu."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise, au git comme au mount. Un amendement daté n'est pas une seconde note. ÉCART CONNU ET NON RÉSOLU : le mount /mnt/project porte encore NOTE-REPRISE-GIT-S13.md, périmée de trois générations (§0.4)."
autorite: "RÉGIME G-4, TRANCHÉ le 2026-07-25, portée PROSPECTIVE. Le MOUNT est l'espace vivant ; le GIT est l'espace de consignation, accompagné du matériel permettant à un tiers de REPRODUIRE. Bascule à l'épuisement d'une branche, après audit froid incognito. L'EXISTANT RESTE EN PLACE. R-54 reste debout. Pour les pièces de GOUVERNANCE, le dépôt git fait foi."
supersede: "Points où S16 corrige S15 : §0 audit/ 45 → 50 ; piège R-36 (« Reprise S15 » → « Reprise S16 ») ; §6.2 ensemble A « RIEN N'EST FAIT » → P-0 RENDU sur les sept ; §6.4 registre de corpus « NON ARBITRÉ, à déposer » → DÉPOSÉ ; §5.4 paquet β « mount-seul, à refournir » → NON-REFOURNISSABLE, 34/35 reconstructibles depuis kb/, 8 pièces déposées."
---

# Note de reprise S16 (consolidée, CLÔTURE) — état, acquis, prochain geste

> **Pourquoi cette note existe.** S16 a exécuté le §0-lite intégral, **rendu P-0 sur les
> sept sources** — première identification du périmètre depuis son gel — porté un
> arbitrage opérateur, et **coupé la boucle de refourniture** : ni le paquet β ni les
> corps n'auront à être re-adressés. Elle absorbe la note S15 sans perte (§10).

## 0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S16

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -8   # HEAD = message commençant par « Reprise S16 », puis
                           # 11e924e, 5f9874c, 20290b1, 1c90daf, b4af0c5, 8caafa7, 09d9e2a
    ls instruments/*.py | wc -l                    # attendu : 34
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 50   <== RECALÉ (45 → 50)
    ls audit/beta-paquet-gouvernance/ | wc -l      # attendu : 8    <== NEUF S16
    ls kb/*.md | wc -l                             # attendu : 215
    ls hors-KB/B/ | wc -l                          # attendu : 4
    ls sources/ | wc -l                            # attendu : 4 (hors compte)
    python3 instruments/inventaire_sceaux.py       # 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre   # sha8=051e2833 rc=0

**Recalage `audit/` 45 → 50, MESURÉ** : `LC-BETA-04-P0-RENDU-SEPT-SOURCES.md` (`11e924e`),
puis `LC-BETA-PAQUET-CONCORDANCE.md`, `LC-WORK-REGISTRE-CORPUS.md`,
`LC-BETA-DEFAUTS-DAGE-PAQUET.md` et le répertoire `beta-paquet-gouvernance/` (compté 1).
**Les cinq autres comptes sont INCHANGÉS.** **MESURÉ AUSSI** : l'entrée d'un `.py` dans
`audit/beta-paquet-gouvernance/` **ne déplace PAS** l'inventaire (6/76/1) et **ne déplace
PAS** le sceau (`051e2833`).

### 0.1 Les 12 redémonstrations — bilan INCHANGÉ depuis S9

    R4b 35/35 · R5b 17/17 · R3 16/16 · R6 16/16 · R2 12/12 · R12 11/11
    R1 6/6 · R8 21/21 · R10 40/40 · R7 45/45 · R9 16/16 · R11 36/36

**271/271 PASS + 101 consignations, 12/12 rc = 0.**
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` ; `5+5+6+6+8+7+3+10+14+10+8+19 = 101`.
**REJOUÉES ET CONFORMES EN S16.** Les variantes `_b` de R4 et R5 sont celles qui comptent ;
les v1 restent au dépôt et **ne se rejouent pas**.

**PIÈGE DE RECOMPTE, mordu en S16 par le pilote** : un motif de comptage des consignations
trop large rend **115** au lieu de 101 (il attrape les en-têtes de section et la ligne de
bilan). Compter sur le **marqueur en tête de ligne**, et **confronter au bilan auto-déclaré
de chaque script** — trois d'entre eux (R8, R9, R11) libellent ce bilan différemment
(accents, tirets), ce qui n'est **pas** un écart.

### 0.2 Rejeux de confirmation hors compte — tous CONFORMES en S16

    python3 instruments/harnais_R9.py    # 6/6 mordantes, rc=0
    python3 instruments/harnais_R11.py   # 7/7 mordantes + VACANTES: 0, rc=0
    cd hors-KB/B && python3 verif_B_tracteur.py           # rc=0 ; sha8 script = 8e386686
    python3 instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test   # 6/6, rc=0
    python3 audit/LC-BETA-CONTROLE-DEPOT.py --self-test          # 8/8, rc=0

**Contrôle dépôt en usage nominal** (T0, distinct de l'auto-test) :

    python3 audit/LC-BETA-CONTROLE-DEPOT.py --depot . \
      --atelier <ATELIER> --manifeste audit/LC-BETA-MANIFESTE-GOUVERNANCE.md

En S16 : **6 déclarées / 6 confrontées / 0 copie arbre / 0 copie historique, rc=0.**

### 0.3 Intrants `sources/` — CONFRONTÉS ET CONCORDANTS en S16, vrais PDF

    2312_12498v2.pdf  1 895 152 o  sha8=04d9b4f4
    2409_10595v2.pdf  2 332 898 o  sha8=27a94980
    2503_19957v1.pdf    910 410 o  sha8=113ab4a2

**Toute réapparition SE CONFRONTE. Enregistrer n'est pas confronter.**

### 0.4 ÉCART DE SURFACE CONNU, NON RÉSOLU

Le mount `/mnt/project` porte **`NOTE-REPRISE-GIT-S13.md`**, unique au mount mais
**périmée de trois générations**. Elle écrit que HEAD attendu = `cad358a` « tant que S13
n'est pas déposée » — c'est la pièce même qui a fait mordre le piège R-36 en S14. **Elle
ment toujours par âge.** Nommée en S16, **non retirée** : le mount est en lecture seule
côté pilote, et un retrait est un geste d'opérateur.

### 0.5 Leçons d'environnement opposables (S2–S16, toutes maintenues)

`setsid nohup` pour rejeu long ; `ls audit/` pas `ls audit/*.md` ; jamais deux sceaux dans
le même arbre ; les durées ne sont pas des clés de sceau ; `origin/front-pq` résiduelle et
bénigne ; `inventaire_sceaux.py` **réécrit sa date** (restaurer par `git checkout`) ;
`redemo_R6_nongauss.py` imprime sans crochets ; `harnais_R11.py` crée
`instruments/__pycache__/` à nettoyer ; `pgrep -f` s'auto-matche ; `simplify` non borné ;
`pdfplumber` 0.11.9, `pdftoppm`/`pdfinfo`, Pillow présents, **`pymupdf` ABSENT**,
`extract_words` **mensonger** sur les mathématiques affichées — descendre au niveau `chars` ;
**`xxd` ABSENT** — passer par `python3` ou `od` ; **NEUF S16 : `rc=$?` après un pipe mesure
le DERNIER élément du pipe, pas la commande** — le pilote a cru lire le rc de `python3` et
lisait celui de `tail`. Chaîner par `;` et capturer le rc **avant** tout pipe.

**Réseau.** L'allowlist de `bash` **NE COUVRE PAS `arxiv.org`** ; `github.com` **EST**
couvert. Les outils de recherche/fetch web sont un **canal SÉPARÉ**, non soumis à cette
allowlist : pages éditeur, INSPIRE, ADS et arXiv y sont atteignables. **CONFIRMÉ EN S16 par
usage** : P-0 a été rendu par ce canal. **Il rend du TEXTE, jamais des octets hachables** —
d'où la limite du §3.4.

**Token.** En ligne, jamais au disque, jamais dans `.git/config`, jamais dans un commit, et
**vérifié à 0 après usage**, y compris dans le contenu de **tous** les blobs jamais commités.
Révoqué après usage.

**Identité de commit.** `LC-RACCORD pilote S<n> <pilote-s<n>@lc-raccord.local>`.
**Le pilote ne signe JAMAIS du nom de l'opérateur.**

## 1. Historique des acquis (S9 → S16), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2), volet 1 (V6) et volet 1-bis ([D5] LEVÉ, W3) clos
  et déposés. Détail intégral en historique git.
- **S12** (mount-seul) : VOLET 2 arbitré = β/P-1 ; sort de R-23 = MAINTIEN. Acquis TIENNENT.
- **S13** : β ouvert sous discipline ; brouillon de cadrage neuf ÉCARTÉ ; **P-8 SOLDÉ et
  DÉPOSÉ** (`cad358a`).
- **S14 — administrative** : G-4 TRANCHÉ ; périmètre de `S-B1` arbitré aux deux ensembles ;
  swap d'unicité exécuté.
- **S15 — administrative, mais elle a MESURÉ** : §0-lite intégral ; registre des 4 corps β
  RE-CONFRONTÉ 4/4 ; arbitrages nº1 (dissolution PAR ENSEMBLE) et nº2 (régime des surfaces) ;
  amendement de périmètre nº2 DÉPOSÉ ⟹ **R-7 SATISFAIT** ; contrôle dépôt déposé.
- **S16 — PREMIER MOUVEMENT NON ADMINISTRATIF DEPUIS S13, et il est d'IDENTIFICATION.**
  1. §0-lite intégral, redémonstrations comprises, **conforme**.
  2. **P-0 (R-41) RENDU sur les SEPT sources** (§2). **Issue FANTÔME écartée par mesure, 0/7.**
  3. **Arbitrage nº3** : S9/S10 classables **sous réserve écrite** (§2.3).
  4. **Registre de corpus DÉPOSÉ** — l'item quittait le reste-à-faire (§4.1).
  5. **Boucle de refourniture COUPÉE** : paquet β non-refournissable (§4.2).
  6. **Zéro mouvement scientifique** : aucune ligne classée, aucune gate, aucun verdict.

## 2. P-0 (R-41) — RENDU. Corps : `audit/LC-BETA-04-P0-RENDU-SEPT-SOURCES.md`.

### 2.1 Ordre d'exécution, opposable

Identités lues **dans les octets d'abord**, recherche **ensuite**. Aucune identité obtenue
par recherche puis soumise à confirmation de l'opérateur : cela aurait fait **un seul
témoignage corrélé** (R-54). **Cet ordre est la valeur du rendu ; il ne se rejoue pas à
l'envers.**

### 2.2 Résultat

**Sept lignes, sept identités, zéro fantôme.** Grades ÉCRITS : `B1` SciPost Phys. Core 8,
075 (2025) · `B2` JHEP 01 (2020) 155 · `B3` JHEP 06 (2024) 044 · `B4` JHEP 05 (2024) 053 ·
`S8` Rev. Math. Phys. 8 (1996) 327–392. `S9` et `S10` : **PRÉPRINTS arXiv NON ARBITRÉS**.

Octets : `B1`–`B4` **re-confrontés 4/4** au registre, hachés **en flux avant extraction** ;
`S8`/`S9`/`S10` **premières mesures faisant référence**. Sha256 complets au registre de
corpus, `audit/LC-WORK-REGISTRE-CORPUS.md` §2.

Objet vérifié et non le titre (§1.4) par recensement dans les octets : concordance sur les
sept. **Aucune ligne n'est classée.**

### 2.3 ARBITRAGE nº3 (opérateur, 2026-07-25) et sa RÉSERVE

`S9`/`S10` ne sont **ni fantômes ni sans octets**, mais **sans grade arbitré et à éditeur
unique** — cas non prévu par l'arbitrage nº1 §2, qui vise l'absence d'**identité**.
**Lecture retenue** : « préprint arXiv non arbitré » vaut **grade écrit**, et le seuil de
trois miroirs **vise le fantôme**, écarté ⟹ **classables SOUS RÉSERVE ÉCRITE**.

**La réserve se recopie avec la ligne. Une ligne `S9`/`S10` sans elle est incomplète :**
(1) aucun comité de lecture ne s'est prononcé — aucune conclusion ne peut s'adosser à un
grade ; (2) **§1.2 n'est PAS satisfait à la lettre** : classées **par arbitrage**, non par
satisfaction du critère ; (3) un seul éditeur atteste, sans contrepartie qui rattrape une
erreur ; (4) **réversible dans les deux sens** — publication ⟹ **re-confrontation**, retrait
⟹ retombée sous `SUSPENDU` ; (5) ce n'est pas un défaut de recherche mais une propriété des
objets.

**Portée** : `S9` et `S10`, **et rien d'autre**. `R-41` §1.2 n'est pas modifié dans sa lettre.

### 2.4 LIMITE OUVERTE, NON ARBITRÉE, sur CINQ lignes

**Le grade porte sur l'article PUBLIÉ ; les octets consommés sont le PRÉPRINT.** Pour `B1`–`B4`
et `S8`, le sha256 atteste une version arXiv `vN`, **pas** la version d'éditeur qui porte le
grade. Les octets publiés **n'ont pas été fournis**, les deux versions **jamais confrontées**.
§1.3 est satisfait **pour l'article**, **non transféré aux octets**. L'arbitrage nº3 **ne
touche pas** cette limite.

**Aucun sha256 externe n'atteste ces octets** : `bash` ne joint pas arxiv.org, le canal web
rend du texte. La concordance 4/4 de `B` est une **re-confrontation au registre LC**, non une
attestation indépendante.

## 3. VOLET β (P-1) — état RÉEL, substance au git `kb/`, INCHANGÉ depuis S14

- **β ≡ G3 = transport AdS→dS (« T-b ») de la jonction Δ_𝒞 / gate C1, Λ>0** ; **seul facteur
  d'O₂ ouvert** ; O₂ (CFT de raccordement) À INVENTER.
- **`α` est SOLDÉ** : `α = C1-b` POSITIF, `p` LIBRE ⟹ le résidu d'O₂ se réduit **exactement
  et uniquement à β**.
- **Verdicts de transport rendus** (`LC-D-G3-TRANSPORT`) : `S-G3T-1` = T-b (mur en `TG-3`) ;
  `S-G3T-2` = T-b, mur RE-SITUÉ (wedge `2007.06800` = AdS/BCFT) ; `S-G3T-3b`
  (`2606.09170`, `2412.00183`) = T-b, `R4′ ✓✓` ; `S-G3T-4b` (ST `2409.08709` + de Haro
  `0808.2054`) = T-b, `R3″ ✓ ACQUIS` ; `§7quinquies` = **`K-B` PRESCRIPTION-DÉPENDANT**, ne
  décide dans aucun sens — **ne pas le rejouer en croyant l'ouvrir**.
- **Le mur, nommé.** Caveat de **de Haro p.3** : le graviton mixed/Neumann n'est admissible
  que dans la **fenêtre BF / Ishibashi-Wald** **ou** sous **cutoff** ; sinon mode lent
  non-normalisable, forcé Dirichlet. ST = branche **cutoff** (échoue `R4″`) ; de Haro =
  branche **fenêtre AdS₄** (échoue le dS-genuine). Chaque candidat ne couvre qu'un
  **sous-ensemble PROPRE**. `R3″` acquis ⟹ **gap résiduel = UNE cellule : `R1″ ∧ R2″ ∧ R4″`**.
- **Pourquoi `T-b` et non `T-c`.** `T-c` exigerait de PROUVER l'absence de version
  renormalisée pour le graviton deux-bords en dS genuine. **Lean ≠ preuve** (`FB-5`).
- **Levier NOMMÉ, NON ARMÉ** : une **preuve** d'(in)admissibilité du graviton propageant
  mixed-BC **deux-faces** au `𝓘⁺` genuine, **sans cutoff**. Il satisfait (a) et (b) de la
  clause de levier falsifiable ; **il reste NON ARMÉ**.
- **Cadrage figé, anti-fit** (`LC-WORK-CADRAGE-G3-HORS-WEDGE`, sha `37bc85e5…`) : cibles
  **TH-1…TH-4** + firewall **TH-R**, issues **T-a / T-b / T-c**, gel amont `b5276e68…f175eb`,
  critère TRIPARTITE, rendement attendu EN BAISSE. **NE PAS re-geler, NE PAS inventer
  d'espace neuf.**
- **Candidats genuine-dS deux-bords ARMÉS, NON LUS**, HORS périmètre de `S-B1` : patch
  statique / deux horizons étirés ; dS/CFT & renorm au bord futur ; bootstrap cosmologique ;
  holographie céleste. Les faire entrer exigerait un **amendement nº3 daté**.
- **Deux routes** : (α) transport au pas C1-b renormalisé — refermée sauf ingrédient neuf,
  P-8 désormais présent ; (δ) invariance du poids `b` d'Odak–Speziale sous Λ<0→Λ>0 — **OUVERTE**.
- **Risques amont déclarés** : **DESI DR2 (2025)** met sous tension la constance de Λ — si Λ
  n'est pas constant, **β ne s'ouvre pas, la question change** · **`Δ-C` est plus étroit que
  son libellé** (S7) · **`p` reste libre**, P-sélecteur PENDANT sous constat BIAISÉ.
- **Anti-circularité `K`** : β prend `+i` (Bunch-Davies) et WCH comme **données POSÉES**.
  Aucune cible ne peut présupposer `A4` comme résultat.

### 3.4 Surfaces — mesuré une TROISIÈME fois

Le mount a servi les quatre corps `B` sous forme de **ZIP nommés `.pdf`** (`PK\x03\x04`).
**Ce n'est PAS une divergence du registre, c'est une surface qui ne sert pas les octets** —
classe consignée à `3419d49` (S10), `af97865` (S11), S15 §3.2, **reproduite à l'identique**.
Conséquence : **le canal 2 ne corrobore rien**, la concordance repose sur **un seul canal**.

## 4. Ce que S16 a coupé — la boucle de refourniture

### 4.1 REGISTRE DE CORPUS — DÉPOSÉ

`audit/LC-WORK-REGISTRE-CORPUS.md` : identifiant canonique, version, sha256, assaut
d'origine, **procédure de récupération**. **PAS les octets** — dépôt PUBLIC, licences arXiv
hétérogènes, git conserve tout blob pour toujours.

Il inscrit aussi, **sans les farder**, les cinq corps des assauts β (`2007.06800`,
`2606.09170`, `2412.00183`, `2409.08709`, `0808.2054`) comme **sha NON MESURÉS** : les
verdicts `S-G3T-*` reposent sur des lectures dont **aucun octet n'est traçable**. Écart
déclaré, **à payer à la première bascule de branche**.

### 4.2 PAQUET β — NON-REFOURNISSABLE

**Mesure indépendante S16** : sur les 35 `BETA-COPIE-*`, **34 BYTE-IDENTIQUES** à `kb/`,
**0 DIVERGENTE**, **1 sans contrepartie**. ⟹ **la substance du paquet était DÉJÀ au dépôt.**

- `audit/LC-BETA-PAQUET-CONCORDANCE.md` : les 43 entrées, sha256, et la contrepartie `kb/`
  de chaque copie. **Le paquet se RECONSTRUIT depuis le dépôt.**
- `audit/beta-paquet-gouvernance/` : les **8 pièces `LC-BETA-*`** déposées **BYTE-INTACTES**,
  au titre de l'arbitrage nº2. Le contrôle dépôt n'interdit que `BETA-COPIE-*` ; la partition
  35/8 est **mesurée, pas nominale**.
- `audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md` : les défauts **NOMMÉS par fichier séparé daté**,
  les pièces restant byte-intactes. **Le dépôt ne les rend pas vraies — il les rend
  falsifiables.**

**LE TROU, nommé** : `BETA-COPIE-LC-JOURNAL-V94.md` n'a **aucune contrepartie `kb/`** (journal
V94, **mount-seul DE DROIT** sous G-4). **Seule entrée des 43 non reconstituable.** Non
déposée d'office ; bascule possible **sur GO opérateur**.

**Chaîne de protection, déclarée** : le manifeste protège la table de concordance (garde 7,
sha déclaré) ; la table porte les sha des 8 pièces. Une modification silencieuse d'une pièce
β se détecte **en confrontant à la table**. La garde 4 (confrontation à un atelier
indépendant) **ne couvre pas** les 8 pièces faute d'atelier indépendant : **limitation
déclarée, non silencieuse** — un contrôle vacant est un faux PASS.

### 4.3 CE QU'IL RESTE À REFOURNIR — la liste exacte

**RIEN, sauf** : les **octets** des sept corps (récupérables par la procédure du §5 du
registre) et **`BETA-COPIE-LC-JOURNAL-V94.md`** si le journal V94 est requis.
**Le ZIP `LC-BETA-PAQUET.zip` n'a plus à être adressé.**

## 5. P-8 / P-9

**Déposé** : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`, sha256
`7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9`, `cad358a`. Auto-test
6/6, rejoué CONFORME en S16. **P-9 : le dépôt n'atteste QUE l'existence de l'instrument ; sa
valeur se mesure À LA PROCHAINE GATE.** Défaut de nom déclaré (version dans le nom, norme
non arbitrée).

## 6. PROCHAIN GESTE ET RESTE À FAIRE

### 6.1 Ordre de travail β — chacun sur GO séparé, jamais d'office

1. ~~Décomposer l'écart des 4 corps~~ — **FAIT en S15.**
2. ~~`P-0` (R-41) sur les SEPT sources~~ — **FAIT en S16 (§2). Précondition dure levée.**
3. ~~Geler et déposer l'amendement de périmètre~~ — **FAIT, `20290b1`. R-7 SATISFAIT.**
4. **`S-B1` — PROCHAIN GESTE.** Positionnement **STÉRILE**, espace `C-i`/`C-ii`/`C-iii`/`C-iv`
   gelé, **par source indépendamment**. **HORS anti-fit parce qu'il ne teste RIEN** : sa
   protection est **sa stérilité**. **S'il conclut sur la physique, il a violé son régime.**
   Pare-feu `FB-1..FB-6` intégral.
   **ISSUE ANTICIPÉE, DATÉE D'AVANT, NON RETOUCHÉE** : A en `C-iii`/`C-iv` pour les trois ;
   B sans aucune ligne en `C-i`, au plus une en `C-ii` ; `S-B2` NON ARMÉ ; chantier refermé
   sur une **DÉLIMITATION — issue COMPLÈTE, pas un échec**. **Elle n'a été retouchée ni après
   la réussite de l'item 1 de S15, ni après celle de S16.** Ce qui lui donne son prix est sa
   date, pas son exactitude.
   **Les lignes `S9`/`S10` se classent AVEC leur réserve (§2.3), jamais sans.**
5. **`S-B2`** seulement si les CINQ conditions cumulatives de `LC-BETA-03` §3 sont vraies,
   dont **au moins une source en `C-i` ou `C-ii`**. Condition 3 : lire « toutes les sources
   classées du périmètre », **et par ensemble**. **ORDRE** : l'amendement R-7 nommant la
   classe et le scoping sont des conditions d'**ARMEMENT de `S-B2`**, **pas** des préalables
   à `S-B1`. Les écrire avant obligerait à nommer une classe non établie — **c'est le fit.**
6. **Audit froid neutralisé** obligatoire sur tout nouvel objet de positivité. **En cas de
   discordance pilote / incognito, l'incognito l'emporte.**
7. **Plafond réaliste : DÉLIMITATION (`T-b`)**, rendement en baisse. `T-a` exigerait la carte
   shadow renormalisée dS-genuine graviton deux-bords, **NON EXHIBÉE à ce jour**.

### 6.2 ARBITRAGE nº1 (2026-07-25) — dissolution PAR ENSEMBLE

1. **Condition évaluée séparément sur A et sur B, jamais globalement.** `E` est proposé à la
   dissolution si (i) aucune source **classée** de `E` n'est en `C-i` ni `C-ii`, **(ii) au
   moins une source de `E` a effectivement été classée**, (iii) aucun **levier neuf
   falsifiable et daté** n'est nommé. **La décision appartient à l'opérateur.** **Symétrie** :
   `B` ne peut pas armer `S-B2` au motif que `A` resterait ouvert, ni l'inverse.
2. **Statut `SUSPENDU POUR NON-IDENTIFICATION`** : source FANTÔME ou sans octets **n'est pas
   classable**, se porte en ligne écrite avec son motif, **ne compte pas** au (i) et **ne
   satisfait pas** le (ii). **EFFET DE S16 : aucune des sept n'y tombe** — la clause reste
   debout pour l'avenir mais **ne s'applique à personne aujourd'hui**.
3. **Levier falsifiable** : nommer ne suffit pas. Il compte s'il porte **(a)** ce qu'il
   faudrait exhiber, **(b)** le critère qui déciderait dans quel sens, **(c)** une date
   antérieure au rendu de `S-B1`.
4. **Garde anti-fit** : une clôture d'ensemble se rédige comme une **DÉLIMITATION À CONTENU
   NOMMÉ**, jamais comme un changement de statut. **Une délimitation sans contenu n'est pas
   une clôture.**

### 6.3 Reste à faire (reporté ; ce qui a bougé est marqué)

- ~~REGISTRE DE CORPUS~~ — **DÉPOSÉ en S16 (§4.1).**
- ~~Refourniture du paquet β~~ — **RÉSOLUE en S16 (§4.2).**
- **Paquet ARCHIVE byte-gelée / atelier séparé** : **NON ARBITRÉE**. Motif inchangé : un gel
  qui porte sur le contenu courant d'un répertoire vivant n'est pas un gel.
- **Journal V94 au git** : **NON ARBITRÉ**, seul trou du paquet (§4.2).
- **Norme de nommage** (`audit/LC-NORME-NOMMAGE.md`) : **non arbitrée**. Défaut assumé : elle
  ne respecte pas sa propre grammaire.
- **G-1** : 16 bundles décharge v2.74, 72 `.py` ; `hors-KB/A/` **non fourni**.
- **G-5b/c** : index `LC-00-INDEX` **ABSENT de `kb/`** ; arborescence des silos.
- **Sort de R-23** : MAINTIEN — corps de F5 non ouvert, `[D5]` LEVÉ (W3) intact. **GO séparé,
  voie (i), jamais d'office.**
- **`sources/` hors compte** au §0-lite : dérive non détectée. À faire entrer, ou à assumer.
- **NEUF S16 — LIMITE §2.4** : version consommée ≠ version gradée, sur cinq lignes.
  **NON ARBITRÉE.**
- **NEUF S16 — sha NON MESURÉS** des cinq corps d'assaut (§4.1).
- **NEUF S16 — `NOTE-REPRISE-GIT-S13.md` au mount** (§0.4).

## 7. Discipline et précédents opposables — PORTÉS INTÉGRALEMENT

*Le précédent `860c3f8` établit qu'une formule ne suffit plus dès que la pièce porteuse est
retirée. Ils sont recopiés ici, et non hérités.*

### 7.1 Précédents S16

1. **UN INSTRUMENT DE MESURE SE MESURE AUSSI.** Le motif de recompte des consignations du
   pilote a rendu 115 au lieu de 101. Corrigé **par mesure**, puis contre-vérifié contre
   l'auto-déclaration des douze scripts. **Un écart d'instrument non déclaré se présente
   comme un écart du dépôt.**
2. **IDENTIFIER DANS LES OCTETS D'ABORD, CHERCHER ENSUITE.** L'ordre inverse produit **un
   seul témoignage corrélé**, quelle que soit la qualité des miroirs trouvés.
3. **UN GRADE ÉDITORIAL NE SE TRANSFÈRE PAS D'UNE VERSION À UNE AUTRE.** Le grade porte sur
   l'article publié ; le sha porte sur le préprint. **Les confondre est un faux acquis.**
4. **UNE RÈGLE QUI NE PRÉVOIT PAS LE CAS SE PORTE À L'OPÉRATEUR, ELLE NE S'ÉTIRE PAS.**
   `S9`/`S10` n'entraient dans aucun statut existant ; le pilote a **nommé les deux lectures
   sans trancher**. **UN GO N'EST PAS UN ARBITRAGE.**
5. **NE PAS DÉPOSER LES OCTETS QUAND LE REGISTRE SUFFIT.** Dépôt public, licences
   hétérogènes, blobs éternels. **Un registre récupère sans reproduire.**
6. **QUAND UNE RÈGLE GÊNE, LA MESURER PLUTÔT QUE LA CONTOURNER.** L'interdit
   `BETA-COPIE-*` semblait empêcher de solder la refourniture ; **la mesure** (34/35 déjà au
   dépôt) a montré qu'il n'y avait rien à déposer. **Renommer pour passer sous un contrôle
   nominal reste la faute commise trois fois — elle ne l'a pas été une quatrième.**
7. **`rc=$?` APRÈS UN PIPE NE MESURE PAS CE QU'ON CROIT.** Voir §0.5.
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS**, même après **deux** réussites successives.

### 7.2 Précédents S15

1. **UNE RÈGLE SE MESURE À SA SOURCE, PAS À SA GLOSE.** Contradiction `R-7` ↔ pare-feu
   **fabriquée** par lecture d'une note au lieu du texte gelé ; proposition de **renommer une
   pièce pour passer sous un contrôle nominal**. **Écart imputable au pilote.**
2. **UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE.** `PKG_SHA_BETA_8` est passé
   de `dc276129` à `687ed70b` **et `LC-BETA-BOOT.py` a rendu rc=0**.
3. **UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL**, c'est un haché mouvant.
4. **UNE CONFRONTATION PAYÉE SE PRÉSERVE HORS SURFACE TOURNANTE** au moment où elle est
   obtenue.
5. **UN ZIP DE TRANSPORT N'EST PAS UN ZIP DE SUBSTITUTION.** Une leçon opposable se lit **à
   son cas**, sinon elle interdit ce qu'elle n'a jamais visé.
6. **UN CONTRÔLE QUI PASSE SUR L'ENSEMBLE VIDE EST UN FAUX PASS** — et sa réciproque : un
   contrôle qui échoue *toujours* satisfait toutes les mutations. **Il faut les deux gardes.**
7. **UN GO N'EST PAS UN ARBITRAGE.** En cas d'ambiguïté : exécuter le geste, **nommer la
   lecture retenue**, ne rien déposer avant confirmation.
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS** après une réussite partielle.

### 7.3 Précédents S14

1. **CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE.** **Le dépôt se
   mesure, il ne se déduit pas.**
2. **UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA DEMANDER.**
3. **UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM.**
4. **LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR.**
5. **UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS.**
6. **UN ORDRE DE CONDITIONS NE SE COMPRIME PAS.** Une condition d'armement n'est pas un
   préalable ; les confondre fabrique du fit.

### 7.4 Précédents S13

Un chantier « à ouvrir » peut être **DÉJÀ cadré/gelé** : lire le dossier AVANT de rédiger un
cadrage neuf (**un brouillon rédigé dans l'ignorance du dossier se JETTE**) · un prérequis
bloquant absent de la reprise peut vivre dans le dossier : **le chercher** · un repérage peut
faire remonter de la substance : **le déclarer** · un instrument mandaté se construit **à la
LETTRE du mandat** et **se prouve par un AUTO-TEST MORDANT** · un dépôt fait avancer HEAD :
**recaler §0-lite dans la reprise** · substance au git, packaging au mount = **à nommer, pas
à réconcilier d'office**.

### 7.5 Précédents S11

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.**
2. **UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE.** Elle se rétracte par un fichier séparé
   daté **supplémentaire** ; l'amendement fautif **reste** et **garde son numéro**.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.**
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.**
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.**
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.**
7. **UN TOKEN NE S'ÉCRIT NULLE PART**, et c'est **vérifié**.
8. **LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL.**

### 7.6 Précédents S10

1. **HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU.**
2. **UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN.**
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

### 7.7 Précédents S9 et S8

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
  pièce. **APPLIQUÉ EN S16** : les 4 corps hachés **en flux dans l'archive**, avant extraction.

### 7.8 Procédure R-55 de dépôt

**Ordre non négociable** : annonce **chemin + sha256 complet + message de commit**, **fichier
par fichier**, PUIS token, PUIS push. **Si le token est fourni AVANT l'annonce, l'annonce se
fait quand même et l'on attend la confirmation de l'opérateur.** Puis confrontation des sha
déposés aux sha annoncés **par `diff`, sur clone neuf**, et vérification du token à **0** —
arbre, `.git/config`, messages de commit, **et contenu de tous les blobs jamais commités**
(`git rev-list --objects --all`). Autres : **lire pour présenter n'est pas ouvrir** · **une
divergence se nomme et se tranche par l'opérateur** · **borner AVANT de lire**.

## 8. G-4 — SOLDÉ, APPLIQUÉ en S15 et S16

> Le **mount** est l'espace vivant. Le **git** est l'espace de consignation : matériaux
> validés, résultats confirmés, **plus le matériel permettant à un tiers de REPRODUIRE**.
> **Bascule** mount → git à l'épuisement d'une branche, après **audit froid incognito**.
> **Portée PROSPECTIVE : l'existant reste en place.**

**Application S16** : les 8 pièces de gouvernance β sont allées **au git**, avec leurs défauts
nommés à part. Le **journal V94 reste mount-seul de droit**. **G-4 est clos.**

## 9. Table de supersession — ce qui a été ÉCARTÉ

| Point | Ancien (périmé) | Retenu S16 |
|---|---|---|
| HEAD attendu | commit « Reprise S15 » | **commit « Reprise S16 », vérifié par `git log`** |
| `audit/` | 45 | **50** |
| Racine | note S15 + PROMPT-S16 | **note S16 + PROMPT-OUVERTURE-S17** |
| `P-0` ensemble A | « RIEN N'EST FAIT », identités attestées NULLE PART | **RENDU, 3/3 identifiées, 0 fantôme** |
| `P-0` ensemble B | §1.5 acquis, §1.2/1.3/1.4 dus | **RENDU, 4/4, grades écrits** |
| Statut `S9`/`S10` | non prévu | **classables SOUS RÉSERVE ÉCRITE (arbitrage nº3)** |
| Registre de corpus | NON ARBITRÉ, à déposer | **DÉPOSÉ** |
| Paquet β | mount-seul, à refournir chaque session | **NON-REFOURNISSABLE : 34/35 reconstructibles, 8 pièces déposées** |
| Grade vs octets | non distingué | **LIMITE OUVERTE §2.4 : le grade porte sur le publié, le sha sur le préprint** |

## 10. AUDIT DE REPORT — ce qui a été recopié avant retrait

*Précédent `860c3f8` : un retrait se précède d'un audit item par item.*

**Depuis `NOTE-REPRISE-GIT-S15.md`** (retirée au même commit) : §0 attendus **recalés** et
leçons d'environnement → **§0** · §1 historique S9→S15 → **§1** · §2 volet β intégral →
**§3** · §3 registre des 4 corps → **§2.2 et registre de corpus §2** · §3.4 instabilité des
surfaces → **§3.4** · §4 P-8/P-9 → **§5** · §5 localisation, paquet, corpus → **§4** ·
§6 prochain geste et reste à faire → **§6** · §6.3 arbitrage nº1 → **§6.2, INTÉGRALEMENT** ·
§7 précédents S15, S14, S13, S11, S10, S9/S8 et procédure R-55 → **§7.2 à §7.8,
INTÉGRALEMENT** · §8 G-4 → **§8** · §9 supersession → **§9** · §11 périmètre → **§11**.

**Depuis `PROMPT-OUVERTURE-S16.md`** (retiré au même commit) : ITEM 1 **réalisé → §2** ·
ITEM 2 `S-B1` **non réalisé → §6.1(4), ouverture de S17** · ITEM 3 `S-B2` **non réalisé →
§6.1(5)** · ITEM 4 gouvernance **partiellement réalisé** (registre de corpus **FAIT** ;
paquet archive, norme de nommage, G-1, G-5b/c, R-23, `sources/` **reportés → §6.3**) ·
§7 périmètre → **§11** · §8 précédents → **§7.2** · §9 token → **§7.8**.

**Rien n'est laissé au seul héritage par formule.**

## 11. PÉRIMÈTRE — INCHANGÉ

S16 a produit une **IDENTIFICATION**, pas un mouvement scientifique : **aucune ligne classée,
aucune gate tirée, aucun verdict touché.**

`{ A4 ; A2★ ; N }` INCHANGÉ · `[B]` = B-PAUVRE · `W2` = DÉLIMITATION, `A4` NON réfuté,
postulat RENFORCÉ · `A2★` décision ouverte, `C7` non levée · `D1` non clos, conclusion `D1c`
INTACTE · `N` non fixé (≡ Λ, `R-53` : 0/4) · `O₂` non construit · β `T-b`, NON RÉSOLU, SEUL
facteur d'O₂ ouvert · `G3-a` non levé · nœud (i) INDÉTERMINÉ (pas A) · Silo R CLOS À 12/12 ·
**CCC non démontrée NI réfutée**. Plafond réaliste de β : **DÉLIMITATION (`T-b`)**, rendement
EN BAISSE.

---

*§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, identifier, hacher,
réserver, arbitrer, déposer, retirer, consolider : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit. **Rendre P-0 n'ouvre aucune gate et ne classe aucune
ligne.** Un sha256 atteste des octets, jamais un titre, des auteurs, un DOI ni un grade.
β `T-b`, non résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
