---
id: NOTE-REPRISE-GIT-S17
titre: "Note de reprise UNIQUE et autoportante — CLÔTURE de S17 (2026-07-25). Consolide et REMPLACE NOTE-REPRISE-GIT-S16 et son AMENDEMENT 1 ; les notes S9–S16 vivent dans l'historique git. ACQUIS S17, ET LE PREMIER EST UN MOUVEMENT DE POSITIONNEMENT : S-B1 RENDU sur les sept lignes, C-i 0 · C-ii 0 · C-iii 6 · C-iv 1, S-B2 NON ARMÉ, chantier refermé sur une DÉLIMITATION À CONTENU NOMMÉ dont le levier falsifiable est écrit en quatre qualificatifs. Le mount MESURÉ et sa nature réelle établie : canal de LECTURE fidèle, canal de HACHAGE nul. SIX ARBITRAGES opérateur. Paquet β SOLDÉ, journal V94 byte-confronté. Cinq corps d'assaut en PREMIÈRE MESURE. Norme de nommage ADOPTÉE. AUCUNE gate ouverte, AUCUN verdict touché."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
role: "FICHIER DE REPRISE UNIQUE. Remplace NOTE-REPRISE-GIT-S16.md ET NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md, retirées de la racine au même commit, après AUDIT DE REPORT item par item (§10)."
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture d'une session neuve : HEAD = le commit dont le message commence par « Reprise S17 », À VÉRIFIER PAR `git log`, JAMAIS par cette note — ET SANS PRÉSUMER QU'IL EST HEAD : un commit postérieur peut s'être intercalé, c'est arrivé en S17 (voir §7.1 nº1). Ses parents remontent par 7dbee86 (S-B1 rendu), 2ff65f9 (pièce de nommage S17), b79e3de (amendement S16), aedc9a2 (Reprise S16), 11e924e, 5f9874c, 20290b1, 1c90daf."
regle_unicite: "Il ne doit exister QU'UN SEUL fichier de reprise, au git comme au mount. Un amendement daté n'est pas une seconde note. ÉCART S16 §0.4 RÉSOLU : NOTE-REPRISE-GIT-S13.md a été RETIRÉE DU MOUNT par l'opérateur, constaté PAR MESURE — 0 note de reprise au mount, 28 → 27 fichiers."
autorite: "RÉGIME G-4, portée PROSPECTIVE, CLOS. Le MOUNT est l'espace vivant ; le GIT est l'espace de consignation, accompagné du matériel permettant à un tiers de REPRODUIRE. L'EXISTANT RESTE EN PLACE. R-54 reste debout. Pour les pièces de GOUVERNANCE, le dépôt git fait foi."
supersede: "Points où S17 corrige S16 : §0 audit/ 50 → 55 ; racine 5 → 4 fichiers ; piège R-36 (« Reprise S16 » → « Reprise S17 », ET avertissement de position) ; §0.4 écart de surface NON RÉSOLU → RÉSOLU par retrait opérateur ; §3.4 « le mount ne sert pas les octets » → canal de LECTURE fidèle et de HACHAGE nul, archives OUVERTES ; §2.4 limite NON ARBITRÉE → RÉSERVE PERMANENTE ; §4.2 journal V94 seul trou → BYTE-CONFRONTÉ, paquet SOLDÉ ; §6.1 S-B1 à faire → RENDU ; §6.3 paquet β non arbitré → ARCHIVE ; norme de nommage non arbitrée → ADOPTÉE ; sha des cinq corps NON MESURÉS → PREMIÈRES MESURES."
---

# Note de reprise S17 (consolidée, CLÔTURE) — état, acquis, prochain geste

> **Pourquoi cette note existe.** S17 a exécuté le §0-lite intégral, **rendu S-B1** — premier
> mouvement de positionnement du chantier β — mesuré la **nature réelle du mount** que trois
> sessions avaient classée sans l'ouvrir, porté **six arbitrages** d'opérateur, **soldé le
> paquet β** et **adopté la norme de nommage**. Aucune gate n'a été ouverte, aucune ligne
> consommée en substance, aucun verdict touché.

## 0. Attendus vérifiables à l'ouverture (§0-lite) — RECALÉS EN S17

    instruments/*.py                    34
    instruments/archives-scelees/*.py   76
    audit/                              55     (RECALÉ : 50 + 5 pièces S17)
    audit/beta-paquet-gouvernance/       8     pièces LC-BETA-*
    kb/*.md                            215
    hors-KB/B/                           4
    sources/                             4     HORS COMPTE — sa dérive n'est pas détectée
    racine                               4     fichiers, UNE SEULE note de reprise

Puis `instruments/inventaire_sceaux.py` → **6 LIVE / 76 ARCHIVE / 1 ABSENT** ;
`instruments/run_sceau.py verif_paquet_propre` → sha8 **`051e2833`**, **rc=0**.

### 0.1 Les 12 redémonstrations — bilan INCHANGÉ depuis S9

**271/271 PASS + 101 consignations, 12/12 rc = 0.** Décomposition pour recompte indépendant,
**multiensemble et NON dans l'ordre R-1…R-12** :
`35+17+16+16+12+11+6+21+40+45+16+36 = 271` · `5+5+6+6+8+7+3+10+14+10+8+19 = 101`.

**REJOUÉES ET CONFORMES EN S17.** Répartition mesurée, par script :
R-1 6/3 · R-2 12/8 · R-3 16/6 · **R-4b 35/5** · **R-5b 17/5** · R-6 16/6 · R-7 45/10 ·
R-8 21/10 · R-9 16/8 · R-10 40/14 · R-11 36/19 · R-12 11/7.

Variantes qui comptent : `redemo_R4_CT_b.py` et `redemo_R5_reductions_b.py`. Les v1 restent au
dépôt et **ne se rejouent pas**.

**RECOMPTE.** Compter sur le **marqueur en tête de ligne**, puis confronter au **bilan
auto-déclaré de chaque script** — 12/12 concordants en S17. R-8, R-10 et R-11 libellent leur
bilan différemment (accents, tirets) : **ce n'est PAS un écart**. Le piège de S16 (un motif
large rendant 115 au lieu de 101) **ne s'est pas reproduit** sous le motif du pilote S17 ; les
deux motifs employés rendent 101. **Cela ne prouve pas que le piège n'existe pas** : le motif
n'était pas le même. **Déclarer son instrument, pas seulement son résultat.**

### 0.2 Rejeux de confirmation hors compte — tous CONFORMES en S17

`harnais_R9.py` **6/6 mordantes**, rc=0 · `harnais_R11.py` **7/7 + 0 vacante**, rc=0 ·
`cd hors-KB/B && python3 verif_B_tracteur.py` rc=0, sha8 **`8e386686`** ·
`instruments/LC-WORK-GEN-PAQUET-v2_1.py --self-test` **6/6**, sha256
`7d63b9ed94b003da3af3dd765e2997c10edef3ffed85d9e44c138ed3fc2e2fc9` ·
`audit/LC-BETA-CONTROLE-DEPOT.py --self-test` **8/8 mordantes**, rc=0.

### 0.3 Intrants `sources/` — CONFRONTÉS ET CONCORDANTS en S17, vrais PDF

`2312_12498v2.pdf` 1 895 152 o sha8 `04d9b4f4` · `2409_10595v2.pdf` 2 332 898 o sha8
`27a94980` · `2503_19957v1.pdf` 910 410 o sha8 `113ab4a2`. `%PDF` lu aux octets, 3/3.

### 0.4 SURFACES — l'écart S16 est RÉSOLU, et la nature du mount est ÉTABLIE

**RÉSOLU.** `NOTE-REPRISE-GIT-S13.md`, périmée de quatre générations et porteuse du piège R-36
de S14, a été **RETIRÉE DU MOUNT par l'opérateur**. **Constaté par mesure** : 0 occurrence,
**0 note de reprise** au mount, 28 → 27 fichiers.

**ÉTABLI, ET C'EST NEUF.** Les sept `.pdf` de `/mnt/project` portent `50 4b 03 04` en tête et
`PK\x05\x06` en queue : **archives ZIP**, aucun `%PDF`, aucun `%%EOF`. Quatrième occurrence de
la classe, **élargie de quatre fichiers à sept**. Mais **les archives n'avaient jamais été
OUVERTES** :

> Chacune contient **une image de page ET un texte OCR par page**, plus un `manifest.json`.
> Les manifestes ne portent **AUCUN sha de source**.
> **Le mount est un canal de LECTURE fidèle et un canal de HACHAGE nul.**

**Contrôle du canal, le seul disponible** : sur les trois papiers dont le dépôt porte *aussi*
les vrais PDF, pagination **3/3 concordante** (20/20, 26/26, 22/22) et texte de page 1
concordant. Sur les quatre lignes `B`, pagination **4/4 concordante** au registre
(38 · 14 · 78 · 88).

**Trois sessions ont lu « ne sert rien » dans « ne sert pas les octets ».** Ce sont deux
propositions distinctes et seule la seconde était mesurée.

### 0.5 Leçons d'environnement opposables (S2–S17, toutes maintenues)

`setsid nohup` pour rejeu long ; `ls audit/` pas `ls audit/*.md` ; jamais deux sceaux dans le
même arbre ; les durées ne sont pas des clés de sceau ; `origin/front-pq` résiduelle et
bénigne ; `inventaire_sceaux.py` **réécrit sa date** (restaurer par `git checkout`) ;
`redemo_R6_nongauss.py` imprime sans crochets ; `harnais_R11.py` crée
`instruments/__pycache__/` à nettoyer ; `pgrep -f` s'auto-matche ; `simplify` non borné ;
`pdfplumber` 0.11.9, `pdftoppm`/`pdfinfo`/`pdftotext`/`unzip` présents, Pillow présente,
**`pymupdf` ABSENT**, `extract_words` **mensonger** sur les mathématiques affichées — descendre
au niveau `chars` ; **`xxd` ABSENT** — passer par `python3` ou `od` ; `rc=$?` après un pipe
mesure le **dernier élément du pipe** — chaîner par `;` et capturer le rc **avant** tout pipe.

**NEUF S17 — `grep -c` COMPTE DES LIGNES, PAS DES OCCURRENCES.** Une ligne portant trois
occurrences en rend **une**. Employer `grep -o | wc -l`, ou `re.findall` en `python3`.

**NEUF S17 — les chaînes `&&` s'interrompent sur un `grep -c` qui rend 0** (exit 1). Terminer
par `|| true` quand le zéro est un résultat attendu.

**Réseau.** L'allowlist de `bash` **NE COUVRE PAS `arxiv.org`** ; `github.com` **EST** couvert.
Les outils de recherche/fetch web sont un **canal SÉPARÉ**, non soumis à cette allowlist :
pages éditeur, INSPIRE, ADS et arXiv y sont atteignables. **CONFIRMÉ PAR USAGE en S16 et en
S17.** **Il rend du TEXTE, jamais des octets hachables** — d'où l'impossibilité de confronter
un sha par cette voie, mesurée deux fois.

**Token.** En ligne, jamais au disque, jamais dans `.git/config`, jamais dans un commit, et
**vérifié à 0 après usage**, y compris dans le contenu de **tous** les blobs jamais commités.
**Un token par dépôt, arrivant APRÈS son annonce. Révoqué après usage.**

**Identité de commit.** `LC-RACCORD pilote S<n> <pilote-s<n>@lc-raccord.local>`.
**Le pilote ne signe JAMAIS du nom de l'opérateur.**

## 1. Historique des acquis (S9 → S17), consolidé

- **S9–S11** : Silo R clos à 12/12 (E-2), volet 1 (V6) et volet 1-bis (`[D5]` LEVÉ, W3) clos et
  déposés. Détail intégral en historique git.
- **S12** (mount-seul) : VOLET 2 arbitré = β/P-1 ; sort de R-23 = MAINTIEN.
- **S13** : β ouvert sous discipline ; brouillon de cadrage neuf ÉCARTÉ ; **P-8 SOLDÉ et
  DÉPOSÉ** (`cad358a`).
- **S14 — administrative** : G-4 TRANCHÉ ; périmètre de `S-B1` arbitré aux deux ensembles ;
  swap d'unicité exécuté.
- **S15 — administrative, mais elle a MESURÉ** : §0-lite intégral ; registre des 4 corps β
  RE-CONFRONTÉ 4/4 ; arbitrages nº1 et nº2 ; amendement de périmètre nº2 DÉPOSÉ ⟹ **R-7
  SATISFAIT** ; contrôle dépôt déposé.
- **S16 — premier mouvement non administratif depuis S13, et il est d'IDENTIFICATION** :
  §0-lite conforme ; **P-0 (R-41) RENDU sur les SEPT sources**, issue fantôme écartée par
  mesure **0/7** ; arbitrage nº3 ; registre de corpus DÉPOSÉ ; boucle de refourniture COUPÉE.
- **S17 — PREMIER MOUVEMENT DE POSITIONNEMENT DU CHANTIER β.**
  1. §0-lite intégral, redémonstrations comprises, **conforme**.
  2. **`S-B1` RENDU** sur les sept lignes (§3). **`S-B2` NON ARMÉ.** Délimitation à contenu
     nommé, **levier falsifiable écrit en quatre qualificatifs**.
  3. **Nature réelle du mount ÉTABLIE** (§0.4) — trois sessions corrigées par une mesure.
  4. **Six arbitrages** d'opérateur (§2.4, §3.5, §4, §5bis).
  5. **Paquet β SOLDÉ** : journal V94 **byte-confronté**, plus aucun trou (§4).
  6. **Cinq corps d'assaut en PREMIÈRE MESURE** (§4.3).
  7. **Norme de nommage ADOPTÉE**, `DEFAUTS-DAGE` ajouté au vocabulaire fermé.
  8. **Zéro mouvement scientifique** : aucune gate, aucun verdict, aucune physique.

## 2. P-0 (R-41) — RENDU. Corps : `audit/LC-BETA-04-P0-RENDU-SEPT-SOURCES.md`.

### 2.1 Résultat

Sept lignes identifiées, **issue fantôme écartée par mesure 0/7**. Grades écrits sur cinq
lignes : SciPost Phys. Core 8 075 · JHEP 01(2020)155 · JHEP 06(2024)044 · JHEP 05(2024)053 ·
Rev. Math. Phys. 8 327-392. `S9` et `S10` : **préprints arXiv non arbitrés**, arXiv seul.

### 2.2 ARBITRAGE nº3 et sa RÉSERVE ÉCRITE — se recopie avec `S9` et `S10`, jamais séparée

`S9` et `S10` sont **CLASSABLES SOUS RÉSERVE ÉCRITE**. Une ligne qui apparaîtrait sans elle est
**incomplète**.

1. **Aucun comité de lecture ne s'est prononcé.**
2. **§1.2 n'est pas satisfait à la lettre** — classables **par arbitrage d'opérateur**, non par
   satisfaction du critère. **La distinction ne s'efface pas avec le temps.**
3. **Un seul éditeur atteste.** arXiv. Aucune contrepartie indépendante.
4. **Réversible par l'événement, dans les deux sens.** Publication ⟹ la ligne SE RE-CONFRONTE.
   Retrait ou remplacement ⟹ retour sous `SUSPENDU`.
5. **Ce n'est pas un défaut de recherche.** L'écart est une propriété des objets.

**État au 2026-07-25** : ni retrait ni remplacement constaté. **Ni `S9` ni `S10` ne retombent
sous `SUSPENDU`.** Vérifié en S17 par récupération au canal web.

### 2.3 Écart de version `S10` — NOMMÉ, NON RÉSOLU

Le registre et P-0 §3 déclarent les octets consommés en **v2 daté 09/07/2026**. Le tampon
récupéré porte **`08 Jul 2026`**. **Un jour d'écart.** Une réconciliation plausible existe —
soumission contre annonce — **et elle n'est pas retenue** (registre §5.4 : ne rien conclure,
nommer). **Ce qui est établi : v2 existe.**

### 2.4 ARBITRAGE — LIMITE grade-publié / octets-préprint : **RÉSERVE PERMANENTE**

Le grade porte sur l'**article publié**, les octets consommés sont le **préprint**, les deux
versions **n'ont jamais été confrontées**, sur **cinq lignes** : `B1` `B2` `B3` `B4` `S8`.
**On n'ira pas chercher les octets publiés.** La limite se porte **indéfiniment** et **se
recopie avec chaque usage de ces cinq lignes**.

> **CONSÉQUENCE À GARDER VISIBLE — AUCUNE LIGNE DU PÉRIMÈTRE N'EST SANS RÉSERVE.**
> **5** lignes sous réserve de décalage version-consommée / version-gradée (`B1` `B2` `B3` `B4` `S8`).
> **2** lignes sous réserve d'absence de grade (`S9` `S10`). **5 + 2 = 7.**
> C'est un **état**, pas une faiblesse. Il doit rester lisible d'un coup d'œil, faute de quoi
> il s'efface par accoutumance — l'usure exacte contre laquelle l'arbitrage a été rendu.

## 3. `S-B1` — RENDU. Corps : `audit/LC-BETA-SB1-RAPPORT.md` + son `AMENDEMENT-1`.

### 3.1 Régime tenu

`S-B1` **classe**. Il n'a confronté aucune cible, ouvert aucune gate, conclu sur aucune
physique. **Sa protection est sa stérilité.** L'espace `C-i`…`C-iv` gelé à `LC-BETA-03` §2 est
**inchangé** : aucune classe ajoutée, retirée ni redéfinie après mesure.

### 3.2 RÉPARTITION FINALE — `C-i` 0 · `C-ii` 0 · `C-iii` 6 · `C-iv` 1

| ligne | classe | canal | pare-feu mordant |
|---|---|---|---|
| `B1` `2503.09372v2` | `C-iii` | mount OCR, 38 p. | `FB-2` (deux rayons d'une même surface), `FB-4` (cutoff) |
| `B2` `1909.11703v2` | `C-iii` | mount OCR, 14 p. | `FB-2` (bord unique) |
| `B3` `2402.04308v2` | `C-iii` | mount OCR, 78 p. | `FB-2` **à la lettre**, `FB-4`, `FB-1` en vigilance |
| `B4` `2312.17316v2` | `C-iii` | mount OCR, 88 p. | `FB-3` (scalaire), `FB-2` |
| `S8` `gr-qc/9511019` | `C-iii` | P-0 octets + web | — (exemple littéral de la grille) |
| `S9` `2602.15275v2` | `C-iii` **+ réserve §2.2** | P-0 octets + web | `FB-3` en vigilance |
| `S10` `2605.11821v2` | **`C-iv`** **+ réserve §2.2** | P-0 octets + web | hors-domaine, voir §3.5 |

**AUCUNE ligne n'est classée sur des octets confrontables.** Les deux ensembles sont **lus**,
aucun n'est **haché**. Cette phrase se recopie avec la répartition.

### 3.3 ANTÉRIORITÉ — mesurée sur les SEPT

`B1` **15** · `B2` **10** · `B3` **11** · `B4` **21** · `S8` **0** · `S9` **0** · `S10` **0**
fichiers `kb/`. Le prompt S17 n'en adjugeait qu'à `B4`. **Les quatre lignes de l'ensemble B en
ont une** ; `B3` est inscrite **consommée** comme `LSW 2402.04308`, fournissant la **famille
`p`** du coin de transmission. **La partition A/B sépare le déjà-consommé du neuf.** Ordre
classer-puis-confronter **tenu sur les quatre**.

### 3.4 DÉLIMITATION À CONTENU NOMMÉ — et son levier falsifiable

Condition 3 de `LC-BETA-03` §3 **FAUSSE** ⟹ **`S-B2` NON ARMÉ**, issue **complète** et non
échec. Aucun amendement R-7 écrit, aucun scoping gelé : les écrire nommerait une classe non
établie, **c'est le fit**.

**Délimité** : les sept sources ne comblent pas la cellule `R1″ ∧ R2″ ∧ R4″` et n'attaquent pas
le levier d'admissibilité. **Approche la plus serrée : `B3`**, famille de conditions de bord
bien posée avec critère de stabilité de modes — la **forme** du levier — mais en cavité
euclidienne finie, entre deux points fixes `D` et `N`.

> **LEVIER FALSIFIABLE — ce qu'il faudrait pour `C-ii`, et qui manque à `B3` SÉPARÉMENT :**
> **lorentzien** · au **`𝓘⁺` genuine sans cutoff** · sur une **jonction à deux faces** · pour
> un **graviton d'Einstein propageant**. Une source portant les quatre **basculerait le
> classement**. C'est une cible nommée, pas une espérance.

**Aucune source n'est écartée pour non-fourniture d'octets.** La clause `SUSPENDU` ne
s'applique à personne.

### 3.5 ARBITRAGES — `C-iv` classe réelle, `S10` reclassée

**`C-iv` EST UNE CLASSE RÉELLE.** L'écart nº2 du rapport — `C-iv` inatteignable par la largeur
de `C-iii` — est **REJETÉ**. **Il reste écrit au rapport** : un écart rejeté ne s'efface pas,
il se date.

**RÈGLE DE LECTURE ÉTABLIE, valant pour tout classement futur** : *les exemples de `C-iii` sont
illustratifs **à l'intérieur de l'arène de β** ; le rattachement se juge sur l'**objet mesuré**,
jamais par la présence d'un mot dans la liste d'exemples.*

**`S10` → `C-iv`.** Motif : l'**arène**. Gravité de Cotton est une *autre théorie de la
gravitation*, sur FRW et statique à symétrie sphérique, **sans `𝓘⁺`, sans jonction, sans
graviton** — parenté de famille, pas de contact. Et ses discriminants négatifs — `0 AdS`,
`0 graviton`, `0 « boundary condition »` — sont mesurés **DANS LES OCTETS**, donc la réserve
« une absence constatée par extraction n'est pas une absence » **ne mord pas ici**.
**Clause de réversibilité** : si un lien entre thermodynamique d'horizon en Cotton et la
cellule est **exhibé**, la ligne **SE RE-CONFRONTE**.

**Ce qui ne change pas** : `C-i` 0 et `C-ii` 0 ⟹ `S-B2` non armé ⟹ **délimitation inchangée**.

### 3.6 ISSUE ANTICIPÉE — confirmée 4/4, NON RETOUCHÉE

A en `C-iii`/`C-iv` pour les trois ✓ · B sans `C-i`, au plus une `C-ii` → **0 et 0** ✓ ·
`S-B2` non armé ✓ · délimitation ✓. **Son prix reste sa date, pas son exactitude.** Une
anticipation confirmée ne lève **aucune** incertitude sur la physique.

## 4. PAQUET β — SOLDÉ, et ARCHIVE

**ARBITRAGE : le paquet β est confirmé ARCHIVE BYTE-GELÉE**, jamais rejoué, **atelier séparé
assumé**. Le défaut « un gel sur un répertoire vivant n'est pas un gel » **reste nommé** ; il
est **clos par le statut ARCHIVE**, qui interdit au répertoire de bouger.

**43 entrées soldées** : **8** pièces `LC-BETA-*` déposées byte-intactes sous
`audit/beta-paquet-gouvernance/` + **34** `BETA-COPIE-*` reconstructibles par
`audit/LC-BETA-PAQUET-CONCORDANCE.md` + **1** byte-confrontée.

### 4.1 Journal V94 — CONFRONTATION D'OCTETS, CONCORDANTE

Fourni par l'opérateur, **12 623 o**, sha256
`b11347732e7a03899a5d2f5cb16f55d138af3d3095fa8dd603ecbd86df2a691c` — **identique** au sha
déclaré à la table de concordance. **Première confrontation d'OCTETS de la session** ; tout le
reste n'a été confronté qu'en **contenu**. **Il n'y a plus de trou au paquet.**

### 4.2 LES OCTETS DU JOURNAL NE SONT PAS DÉPOSÉS — INTERDIT DUR

`BETA-COPIE-LC-JOURNAL-V94.md` est une **copie de substance** : interdite au dépôt, **arbre ET
historique**. Le fichier arrive nommé `LC-JOURNAL-V94.md` ; **le déposer sous ce nom serait le
geste interdit** — *ne renomme jamais une pièce pour passer sous un contrôle nominal*.
**Ce qui est déposé, c'est la confrontation, pas les octets.** Le journal reste **mount-seul de
droit sous G-4** ; sa fourniture ponctuelle **solde une vérification, elle n'ouvre pas un
dépôt**.

### 4.3 Cinq corps d'assaut — PREMIÈRES MESURES. Corps : `LC-WORK-REGISTRE-CORPUS-AMENDEMENT-1`.

`0808.2054v1` `fcfebce6…` 251 186 o · `2007.06800v4` `5be89da3…` 2 521 998 o ·
`2409.08709v4` `d5e3a1de…` 723 288 o · `2412.00183v1` `eb3ddc9c…` 1 140 406 o ·
`2606.09170v2` `3d8580a5…` 537 107 o. `%PDF`/`%%EOF` 5/5. **Identité lue dans les octets
d'abord, 5/5 concordante** avec l'attribution du registre.

> **CE QUE CES MESURES NE FONT PAS.** Le registre §3 **n'a jamais porté de colonne de
> version**. On ne sait pas quelle version chaque assaut a lue ⟹ **on ne peut même pas
> affirmer que les versions mesurées sont celles qui ont été lues**. **Les verdicts `S-G3T-*`
> ne deviennent PAS traçables rétroactivement.** Ils gagnent une référence **à compter d'ici**.

**Les cinq corps N'ONT PAS ÉTÉ LUS.** L'arbitrage disait mesurer, pas consommer.
**Signalé, non exploité** : `2606.09170v2` porte « Mixed Boundary Conditions » en dS/CFT dans
son titre ; c'est un corps d'**assaut**, `FB-2` enregistre déjà qu'il a fait tomber `F3′` et
`F3″`, et **`S-B1` n'est pas rouvert**.

## 5. P-8 / P-9

**P-8 SOLDÉ ET DÉPOSÉ** (`cad358a`) : `instruments/LC-WORK-GEN-PAQUET-v2_1.py`, auto-test
**6/6**, rejoué CONFORME en S15, S16 **et S17**. **P-9 opposable** : le dépôt d'un instrument
n'atteste que son existence ; **sa valeur se mesure À LA PROCHAINE GATE**. Les 8 pièces
`LC-BETA-*` **mentent par âge** sur ce point (`LC-BETA-BOOT.py` l.103, `LC-BETA-00` §6) —
défaut **sur-restrictif, non bloquant**, nommé à `audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md`,
**jamais corrigé en place**.

## 5bis. Norme de nommage — **ADOPTÉE**

`audit/LC-NORME-NOMMAGE.md` quitte le statut PROPOSITION. Périmètre liant : `audit/`,
`instruments/`, `hors-KB/`, racine — **`kb/` EXCLU** tant que G-4 n'est pas tranchée pour lui.
**L'adoption est PROSPECTIVE et NE RENOMME RIEN.** `DEFAUTS-DAGE` est **ajouté au vocabulaire
de TYPE fermé** par la voie que la norme prescrit, **régularisant deux pièces sans en renommer
aucune**. **Défaut nommé, non corrigé** : la norme ne satisfait pas sa propre grammaire §1 —
type devant, sujet derrière. Corps : `audit/LC-NORME-NOMMAGE-AMENDEMENT-1.md`.

## 6. PROCHAIN GESTE ET RESTE À FAIRE

### 6.1 Ordre de travail — chacun sur GO séparé, jamais d'office

- **`S-B1` : RENDU.** Ne pas le rouvrir sans GO ni gel neuf.
- **`S-B2` : NON ARMÉ**, et ce n'est pas un reste-à-faire — c'est un **résultat**. Il ne
  s'arme que si une source **portant les quatre qualificatifs du §3.4** entre au périmètre,
  ce qui exigerait un amendement de périmètre daté.
- **Assauts `S-G3T-*`** : non rouverts. Leur ré-ouverture exige gel + GO propres.

### 6.2 Dissolution — arbitrage nº1, INCHANGÉ

Arbitrée **PAR ENSEMBLE**, avec **clause de non-classifiabilité** et **clause de levier
falsifiable**. **Aucune des sept sources ne tombe sous `SUSPENDU`** : la clause reste debout
pour l'avenir et ne s'applique à personne aujourd'hui.
**GARDE : une clôture d'ensemble se rédige comme une DÉLIMITATION À CONTENU NOMMÉ, jamais
comme un changement de statut.**

### 6.3 Reste à faire (reporté ; ce qui a bougé est marqué)

- ~~REGISTRE DE CORPUS~~ **DÉPOSÉ (S16)** · ~~refourniture paquet β~~ **RÉSOLUE (S16)**.
- ~~Paquet ARCHIVE byte-gelée~~ — **ARBITRÉ EN S17 : ARCHIVE.**
- ~~Journal V94~~ — **SOLDÉ EN S17 : byte-confronté, octets non déposés, mount-seul de droit.**
- ~~Norme de nommage~~ — **ADOPTÉE EN S17.**
- ~~`NOTE-REPRISE-GIT-S13.md` au mount~~ — **RETIRÉE, constaté par mesure.**
- ~~LIMITE §2.4~~ — **ARBITRÉE : réserve permanente. Mais elle DOIT rester visible (§2.4).**
- ~~sha NON MESURÉS des cinq corps~~ — **PREMIÈRES MESURES RENDUES (§4.3). L'absence de colonne
  de version reste, elle, NON RÉSOLUE.**
- **G-1** : 16 bundles décharge v2.74, 72 `.py` ; `hors-KB/A/` **non fourni**. NON ARBITRÉ.
- **G-5b/c** : index `LC-00-INDEX` **ABSENT de `kb/`** ; arborescence des silos. NON ARBITRÉ.
- **Sort de R-23** : MAINTIEN — corps de F5 non ouvert, `[D5]` LEVÉ (W3) intact. **GO séparé,
  voie (i), jamais d'office.** NON ARBITRÉ.
- **`sources/` hors compte** au §0-lite : dérive non détectée. À faire entrer, ou à assumer.
  NON ARBITRÉ.
- **NEUF S17 — colonne de VERSION absente du registre §3** : les cinq premières mesures portent
  une version, le registre n'en prévoyait pas. **Structure du registre à amender.**
- **NEUF S17 — `C-iv` : classe réelle arbitrée, mais la largeur de `C-iii` n'a pas été
  retouchée.** Le déséquilibre subsiste ; la règle de lecture du §3.5 le compense sans le
  supprimer.

### 6.4 Restes-à-faire de fond, portés depuis S15 — INCHANGÉS

Audit froid incognito · plafond `T-b` / carte shadow `T-a` (non exhibée) · candidats
genuine-dS armés non lus + amendement nº3 daté · routes α/δ (Odak–Speziale) · DESI DR2 ·
`Δ-C` plus étroit que son libellé · `p` libre / P-sélecteur · anti-circularité `K`
(Bunch-Davies, WCH) · `§7quinquies` `K-B` prescription-dépendant · levier NOMMÉ NON ARMÉ ·
cadrage figé `37bc85e5` / gel amont `b5276e68` · caveat de Haro / fenêtre BF / Ishibashi-Wald ·
gap résiduel `R1″ ∧ R2″ ∧ R4″`.

## 7. Discipline et précédents opposables — PORTÉS INTÉGRALEMENT

### 7.1 Précédents S17

1. **UNE PIÈCE NE PEUT PAS DAVANTAGE CONNAÎTRE SA POSITION QUE SON SHA.** R-36 interdit de
   porter son propre sha ; **il n'autorise pas à affirmer qu'on est à HEAD**. La désignation
   par MESSAGE survit à un dépôt postérieur ; la clause « = HEAD » n'y survit pas. En S17 le
   prompt était à `HEAD~1`, et sa clause de position avait été vraie **524 secondes**.
   Corps : `audit/LC-PROMPT-S17-DEFAUTS-DAGE.md`.
2. **UN CONTENANT NON OUVERT N'EST PAS UN CONTENANT MESURÉ.** « Ne sert pas les octets » et
   « ne sert rien » sont deux propositions distinctes. Trois sessions ont lu la seconde dans la
   première ; l'ouverture a rendu **218 pages** lisibles.
3. **LE NOM D'UN CONTENANT NE DÉCRIT PAS SON CONTENU.** Trois occurrences en S17 : sept `.pdf`
   qui sont des ZIP ; un `2409_08709v4.zip` qui transporte **cinq** corpus ; un compte annoncé
   à 4 pour une livraison de 5.
4. **UN ARBITRAGE INEXÉCUTABLE NE SE DÉGRADE PAS EN SILENCE.** « Mesurer maintenant » se
   heurtait à un canal ; l'item a été **rendu à l'opérateur** plutôt que réinterprété en
   réserve. Laisser filer aurait fabriqué la réserve que l'arbitrage écartait.
5. **UNE ANTÉRIORITÉ SIGNALÉE SUR UNE LIGNE NE DIT RIEN DES AUTRES.** Le prompt n'en adjugeait
   qu'à `B4` ; les quatre lignes de B en avaient une. **Mesurer l'antériorité, ne pas la lire.**
6. **LE TOKEN CONFIRME L'ANNONCE, PAS UNE VERSION AMÉLIORÉE.** Un ajout vrai et utile au
   message de commit, écrit après l'annonce, **est un écart** — c'est la forme même du
   précédent S16 nº9. Rattrapé avant commit en S17.
7. **UN INSTRUMENT DE COMPTAGE COMPTE CE QU'IL COMPTE.** `grep -c` rend des **lignes**. Le
   pilote a écrit 11 là où le motif rendait 13 sur 52. Extension de S16 nº1.
8. **UN ÉCART REJETÉ NE S'EFFACE PAS, IL SE DATE.** L'écart nº2 du rapport `S-B1` a été rejeté
   par arbitrage et **reste écrit**.
9. **UNE MESURE SANS VERSION NE CONFRONTE RIEN**, et ne rend rien traçable rétroactivement.

### 7.2 Précédents S16

1. **UN INSTRUMENT DE MESURE SE MESURE AUSSI.** Un écart d'instrument non déclaré se présente
   comme un écart du dépôt.
2. **IDENTIFIER DANS LES OCTETS D'ABORD, CHERCHER ENSUITE.** L'ordre inverse produit un seul
   témoignage corrélé.
3. **UN GRADE ÉDITORIAL NE SE TRANSFÈRE PAS D'UNE VERSION À UNE AUTRE.**
4. **UNE RÈGLE QUI NE PRÉVOIT PAS LE CAS SE PORTE À L'OPÉRATEUR, ELLE NE S'ÉTIRE PAS. UN GO
   N'EST PAS UN ARBITRAGE.**
5. **NE PAS DÉPOSER LES OCTETS QUAND LE REGISTRE SUFFIT.**
6. **QUAND UNE RÈGLE GÊNE, LA MESURER PLUTÔT QUE LA CONTOURNER.**
7. **`rc=$?` APRÈS UN PIPE NE MESURE PAS CE QU'ON CROIT.**
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS**, même après deux réussites.
9. **L'ORDRE R-55 A ÉTÉ INVERSÉ, ET UNE INSTRUCTION DE DÉPÔT NE LE RESTAURE PAS.** Une
   instruction de déposer et la confirmation d'une annonce ne sont pas le même objet.
   **RESTAURÉ EN S17, deux fois, sans exception.**
10. **UN ÉCART QUI NE VIT QUE DANS UN MESSAGE DE COMMIT N'EST PAS PORTÉ.** Un message de commit
    est une trace ; la note est l'organe autoportant.
11. **UN CONTRÔLE PEUT MATCHER LA RÈGLE AU LIEU DE L'INCIDENT — FAUX PASS D'UN TYPE NEUF.**
    La garde trouve le mot, pas le fait.

### 7.3 Précédents S15

1. **UNE RÈGLE SE MESURE À SA SOURCE, PAS À SA GLOSE.**
2. **UN PARE-FEU NOMINAL NE PROTÈGE PAS D'UNE PIÈCE BIEN NOMMÉE.**
3. **UN GEL SUR UN RÉPERTOIRE VIVANT N'EST PAS UN GEL.**
4. **UNE CONFRONTATION PAYÉE SE PRÉSERVE HORS SURFACE TOURNANTE.**
5. **UN ZIP DE TRANSPORT N'EST PAS UN ZIP DE SUBSTITUTION.** Une leçon opposable se lit à son
   cas, sinon elle interdit ce qu'elle n'a jamais visé.
6. **UN CONTRÔLE QUI PASSE SUR L'ENSEMBLE VIDE EST UN FAUX PASS** — et sa réciproque. Il faut
   les deux gardes.
7. **UN GO N'EST PAS UN ARBITRAGE.**
8. **UNE ISSUE ANTICIPÉE NE SE RETOUCHE PAS** après une réussite partielle.

### 7.4 Précédents S14

1. **CONCLURE DEPUIS UNE NOTE PLUTÔT QUE DEPUIS LE DÉPÔT EST UNE FAUTE. Le dépôt se mesure, il
   ne se déduit pas.**
2. **UNE VÉRIFICATION SE BRÛLE SI ON PUBLIE SA VALEUR ATTENDUE AVANT DE LA DEMANDER.**
3. **UN RETRAIT SE PRÉCÈDE D'UN AUDIT DE REPORT ITEM PAR ITEM.**
4. **LE PILOTE NE SIGNE PAS DU NOM DE L'OPÉRATEUR.**
5. **UN ARBITRAGE PROSPECTIF NE SE RÉTROAPPLIQUE PAS.**
6. **UN ORDRE DE CONDITIONS NE SE COMPRIME PAS.** Une condition d'armement n'est pas un
   préalable ; les confondre fabrique du fit.

### 7.5 Précédents S13

Un chantier « à ouvrir » peut être **DÉJÀ cadré/gelé** : lire le dossier AVANT de rédiger un
cadrage neuf (**un brouillon rédigé dans l'ignorance du dossier se JETTE**) · un prérequis
bloquant absent de la reprise peut vivre dans le dossier : **le chercher** · un repérage peut
faire remonter de la substance : **le déclarer** · un instrument mandaté se construit **à la
LETTRE du mandat** et **se prouve par un AUTO-TEST MORDANT** · un dépôt fait avancer HEAD :
**recaler §0-lite dans la reprise** · substance au git, packaging au mount = **à nommer, pas à
réconcilier d'office**.

### 7.6 Précédents S11

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.**
2. **UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE.** Elle se rétracte par un fichier séparé
   daté **supplémentaire** ; l'amendement fautif **reste** et **garde son numéro**.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.**
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.**
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.**
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.** **Reste debout après l'adoption de
   la norme** : ce sont les déclarations au dépôt, non l'usage, qui ont permis l'arbitrage.
7. **UN TOKEN NE S'ÉCRIT NULLE PART**, et c'est **vérifié**.
8. **LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL.**

### 7.7 Précédents S10

1. **HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU.**
2. **UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN.**
3. **UN ESPACE-VERDICT DÉCLARÉ EXHAUSTIF DOIT PRÉVOIR LE CAS QU'IL N'A PAS PRÉVU.**
4. **UNE INFORMATION LUE HORS PÉRIMÈTRE SE DÉCLARE ET NE S'EMPLOIE PAS.**
5. **LE TOKEN NE REMPLACE PAS L'ANNONCE R-55.**
6. **VÉRIFICATION DE DÉPÔT SUR CLONE NEUF**, jamais sur déclaration.
7. **UNICITÉ DE LA REPRISE**, au git comme au mount.
8. **AUTORITÉ DES PIÈCES DE GOUVERNANCE** : le git fait foi.
9. **SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE. Enregistrer n'est pas confronter.**
10. **DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL.**

### 7.8 Précédents S9 et S8

- Un **défaut du gel se nomme et s'amende par FICHIER SÉPARÉ DATÉ**, jamais en place ; la pièce
  amendée reste **byte-intacte**.
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

### 7.9 Procédure R-55 de dépôt

**Ordre non négociable** : annonce **chemin + sha256 complet + message de commit**, **fichier
par fichier**, PUIS token, PUIS push. **Si le token est fourni AVANT l'annonce, l'annonce se
fait quand même et l'on attend la confirmation de l'opérateur.** Puis confrontation des sha
déposés aux sha annoncés **par `diff`, sur clone neuf**, et vérification du token à **0** —
arbre, `.git/config`, messages de commit, **et contenu de tous les blobs jamais commités**
(`git rev-list --objects --all`).

**PRÉCISÉ EN S17** : **un token par dépôt**, arrivant **après** son annonce. Un token qui vit
entre deux dépôts n'est pas dans le protocole — c'est le désordre qui a produit le précédent
S16 nº9. Autres : **lire pour présenter n'est pas ouvrir** · **une divergence se nomme et se
tranche par l'opérateur** · **borner AVANT de lire**.

## 8. G-4 — SOLDÉ, APPLIQUÉ en S15, S16 et S17

> Le **mount** est l'espace vivant. Le **git** est l'espace de consignation : matériaux
> validés, résultats confirmés, **plus le matériel permettant à un tiers de REPRODUIRE**.
> **Bascule** mount → git à l'épuisement d'une branche, après **audit froid incognito**.
> **Portée PROSPECTIVE : l'existant reste en place.**

**Application S17** : le journal V94 **reste mount-seul de droit** — sa fourniture ponctuelle a
soldé une **vérification**, pas ouvert un dépôt. **G-4 est clos.**

## 9. Table de supersession — ce qui a été ÉCARTÉ

| Point | Ancien (périmé) | Retenu S17 |
|---|---|---|
| HEAD attendu | commit « Reprise S16 » | **commit « Reprise S17 », vérifié par `git log`, ET SANS présumer qu'il est HEAD** |
| `audit/` | 50 | **55** |
| Racine | note S16 + amendement + PROMPT-S17, 5 fichiers | **note S17 + PROMPT-S18, 4 fichiers** |
| Mount | « ne sert pas les octets », 4 fichiers | **canal de LECTURE fidèle / HACHAGE nul, 7 fichiers, archives OUVERTES** |
| `NOTE-REPRISE-GIT-S13.md` au mount | présente, ment par âge | **RETIRÉE, constaté par mesure** |
| `S-B1` | à faire, GO séparé | **RENDU — `C-i` 0 · `C-ii` 0 · `C-iii` 6 · `C-iv` 1** |
| `S-B2` | conditionnel | **NON ARMÉ — résultat, pas reste-à-faire** |
| Limite §2.4 | NON ARBITRÉE | **RÉSERVE PERMANENTE, sur cinq lignes** |
| `C-iv` | classe dont l'écart nº2 contestait la réalité | **CLASSE RÉELLE ; écart nº2 REJETÉ et conservé** |
| `S10` | `C-iii` par la lettre de la grille | **`C-iv`, par l'ARÈNE** |
| Paquet β | statut non arbitré | **ARCHIVE byte-gelée** |
| Journal V94 | seul trou du paquet | **BYTE-CONFRONTÉ ; octets NON déposés** |
| Cinq corps d'assaut | sha NON MESURÉS | **PREMIÈRES MESURES ; versions non confrontables** |
| Norme de nommage | PROPOSITION non arbitrée | **ADOPTÉE ; `DEFAUTS-DAGE` au vocabulaire** |

## 10. AUDIT DE REPORT — ce qui a été recopié AVANT retrait

Vérifié par recherche dans les pièces **effectivement déposées**, non par déclaration.
**Trois pièces retirées de la racine au même commit** : `NOTE-REPRISE-GIT-S16.md`,
`NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md`, `PROMPT-OUVERTURE-S17.md`. Elles vivent dans
l'historique git.

**Depuis `NOTE-REPRISE-GIT-S16.md`** : §0 attendus → §0 ci-dessus, recalés · §0.1–0.3 bilans →
§0.1–0.3 · §0.4 écart de surface → §0.4, **résolu** · §0.5 leçons → §0.5, **augmentées** ·
§1 historique → §1 · §2 P-0 et réserve → §2 · §2.4 limite → §2.4, **arbitrée** · §3 volet β →
§3 et §6.4 · §4 refourniture → §4 · §5 P-8/P-9 → §5 · §6.1 ordre de travail → §6.1 · §6.2
dissolution → §6.2 · §6.3 reste à faire → §6.3, **marqué** · §7.1–7.8 précédents → §7.2–7.8,
**intégralement** · §7.8 R-55 → §7.9, **précisée** · §8 G-4 → §8 · §9 supersession → §9 ·
§11 périmètre → §11.

**Depuis `NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md`** : précédents nº9, nº10, nº11 → **§7.2 nº9–11,
intégralement** · confrontation de dépôt S16 → historique git · audit de clôture S16 → absorbé
par le présent §10.

**Depuis `PROMPT-OUVERTURE-S17.md`** : items non réalisés — ITEM 2 `S-B2` → **§6.1, tranché non
armé** · ITEM 3 gouvernance → **§6.3**, dont quatre items **arbitrés en S17** et quatre
**reportés non arbitrés** (`G-1`, `G-5b/c`, sort de `R-23`, `sources/` hors compte) ·
§5 boucle de refourniture → §4 · §7 périmètre → §11 · §8 précédents S16 → §7.2.

**SEULS MANQUES TROUVÉS, tous comblés ici** : la colonne de version absente du registre §3
(→ §6.3, neuf) ; la largeur non retouchée de `C-iii` (→ §6.3, neuf). **Aucun autre item n'a été
trouvé non reporté.**

### 10.1 ÉCARTS S17 imputables au pilote — portés, non dissimulés

1. **Instrument de comptage faux.** `grep -c` compte des lignes : 11 rendu au lieu de **13** sur
   **52**. **Corrigé avant dépôt**, le comptage remplacé par une attestation textuelle.
2. **Message de commit enrichi hors annonce.** Une phrase vraie et utile ajoutée après
   l'annonce ; **rattrapée avant `git commit`**, message rétabli au mot près, identité vérifiée
   par `diff` après push. **C'est la forme même du précédent S16 nº9.**

### 10.2 ÉCARTS S17 non imputables au pilote

3. **Défaut de portée du prompt S17** sur l'antériorité (§3.3) — sans effet, ordre tenu.
4. **Tampon de version `S10`**, 08/07 contre 09/07 (§2.3) — nommé, non résolu.
5. **Ensemble A non re-confrontable** : les octets de `S8`/`S9`/`S10`, mesurés en premières
   mesures en S16, **ne sont sur aucune surface**. Leurs sha sont des empreintes sans
   contrepartie mesurable.
6. **Défauts d'âge du prompt S17**, quatre, nommés à `audit/LC-PROMPT-S17-DEFAUTS-DAGE.md`.

## 11. PÉRIMÈTRE — INCHANGÉ

S17 a produit un **POSITIONNEMENT**, pas un mouvement scientifique : aucune gate tirée, aucun
verdict touché, aucune source consommée en substance.

`{ A4 ; A2★ ; N }` **INCHANGÉ** · `[B]` = B-PAUVRE · W2 = DÉLIMITATION, A4 **NON** réfuté,
postulat RENFORCÉ · A2★ décision ouverte, C7 non levée · D1 **non clos**, conclusion D1c
**INTACTE** · N non fixé (≡ Λ, R-53 : 0/4) · O₂ **non construit** · β **`T-b`, NON RÉSOLU,
SEUL facteur d'O₂ ouvert** · G3-a non levé · nœud (i) INDÉTERMINÉ (pas A) · Silo R **CLOS à
12/12** · **CCC non démontrée NI réfutée.**

Plafond réaliste de β : **DÉLIMITATION (`T-b`)**, rendement **EN BAISSE**. `T-a` exigerait la
carte shadow renormalisée dS-genuine graviton deux-bords, **NON EXHIBÉE**. **`S-B1` rendu ne
change rien à ce plafond** — il le **documente**.

---

*§6.4 — sentinelle terminale. Cloner, mesurer, rejouer, confronter, identifier, récupérer,
classer, délimiter, arbitrer, déposer, retirer, amender : aucun de ces gestes ne scelle, ne
réduit, ne compte, ne démontre quoi que ce soit. Un sha256 atteste des octets, jamais un titre,
des auteurs, un DOI ni un grade. `S-B1` rendu n'ouvre aucune gate ; `S-B2` non armé n'est pas
un échec ; une anticipation confirmée n'est pas une réussite. β `T-b`, non résolu, SEUL facteur
d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
