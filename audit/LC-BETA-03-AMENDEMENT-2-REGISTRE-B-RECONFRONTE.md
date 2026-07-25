---
id: LC-BETA-03-AMENDEMENT-2-REGISTRE-B-RECONFRONTE
codename: LC-RACCORD-BETA
titre: "Amendement ADDITIF nº2 à LC-BETA-03-CADRAGE. TROIS objets, tous administratifs. (1) CORRIGE le §1 de l'amendement nº1, devenu faux par mesure : le registre du 2026-07-24 a été RE-CONFRONTÉ le 2026-07-25 sur les QUATRE lignes de l'ensemble B, par deux canaux distincts, et il tombe 4/4 au bit près ; le BLOQUANT de la note S14 §3 est LEVÉ. (2) PORTE l'ARBITRAGE OPÉRATEUR nº1 du 2026-07-25 : condition de dissolution ÉVALUÉE PAR ENSEMBLE, avec clause de NON-CLASSIFIABILITÉ et exigence de LEVIER FALSIFIABLE. (3) PORTE l'ARBITRAGE OPÉRATEUR nº2 du 2026-07-25 : régime des surfaces — la glose qui étendait le pare-feu au dépôt est RETIRÉE, les pièces de GOUVERNANCE β vont au git conformément à G-4, et un contrôle côté dépôt est mandaté. N'ouvre AUCUN espace neuf, n'élargit AUCUN périmètre, ne rend NI P-0 NI S-B1, ne classe RIEN, ne lit RIEN."
version: 0.2
langue: fr
date: 2026-07-25
statut: "PROJET D'AMENDEMENT — gelé (sha recouvrable), NON DÉPOSÉ. SANS FORCE tant qu'il n'est pas déposé (R-55). Les deux arbitrages qu'il porte sont ACQUIS ; le dépôt, lui, ne l'est pas."
grade: "AMENDEMENT DE REGISTRE ET DE RÉGIME. Atteste des OCTETS et d'ARBITRAGES, rien d'autre : NI une identité éditoriale, NI une pertinence, NI une physique. R-36 : ce fichier ne porte PAS son propre sha — l'opérateur le consigne hors-fichier."
amende: "LC-BETA-03-AMENDEMENT-1-PERIMETRE-S-B1.md (v0.1, 2026-07-25, sha256 33c7cac66df17578a478b161b9b870c6d26adca5886f162a061328dba00fe209) — §1 (tableau de l'ensemble B et sa glose) et §4 (proposition de dissolution par ensemble). Additif : aucune ligne de l'amendement nº1 n'est retirée, réécrite ni renumérotée ; il reste byte-intact, vérifié ce jour."
porte_aussi: "Correction de rédaction sur LC-BETA-03-CADRAGE §3 condition 3 (§6). Correction de NOTE-REPRISE-GIT-S14 §5, glose de pare-feu sans source (§5.1). Trois écarts de session imputés (§7), dont deux au pilote."
---

# Amendement nº2 — registre re-confronté 4/4 · dissolution par ensemble · régime des surfaces

> **Pourquoi un fichier séparé et non une correction en place.** L'amendement nº1 n'est pas
> déposé, **mais son sha est porté par une pièce qui l'est** : `NOTE-REPRISE-GIT-S14.md`
> §6.1(3) écrit `33c7cac6…`. Le modifier en place ferait **pendre** une référence déposée.
> Précédents S9 et S11 nº2 : *un défaut se nomme et s'amende par fichier séparé daté, jamais
> en place ; la pièce amendée reste byte-intacte.* **Vérifié le 2026-07-25 :**
> `33c7cac66df17578a478b161b9b870c6d26adca5886f162a061328dba00fe209` — intact.

## §0 — Ce que cet amendement fait, et ce qu'il ne fait pas

**Il fait trois choses, toutes administratives** : il remplace un **constat d'impossibilité
de mesure** par une **mesure** (§1) ; il **consigne deux arbitrages opérateur** (§4, §5) ; il
**impute trois écarts** (§7).

**Il ne fait pas** : élargir le périmètre · ouvrir un espace de classement ou de verdict ·
re-geler `TH-1..TH-4` ni `TH-R` · toucher `FB-1..FB-6` · armer `S-B2` · nommer une classe
désignée · autoriser une consommation · **réputer `P-0` (R-41) rendu** · **réputer `S-B1`
rendu** · **classer une seule ligne** · lire un seul corps.

---

## §1 — CORRECTION : ce que le §1 de l'amendement nº1 doit désormais lire

### 1.1 Registre de première mesure (2026-07-24) — RE-CONFRONTÉ le 2026-07-25

| réf | corps | taille mesurée / registre | sha256 mesuré = sha256 registre | issue |
|---|---|---|---|---|
| `B1` | FH-II `2503.09372v2` | 979 890 / 979 890 | `6b89e638e3de33e6a5cb0f96974be1e525d7ffd75fda88f7f97e0dac1da8ef62` | **CONCORDANT** |
| `B2` | Horowitz–Wang `1909.11703v2` | 386 010 / 386 010 | `e080c5d6a34ed77af79152ce159208e7df3ff1424860b6b00d9fb78d6c8e87d7` | **CONCORDANT** |
| `B3` | Liu–Santos–Wiseman `2402.04308v2` | 4 629 572 / 4 629 572 | `1426146d832f165f1a9b7d55cacf793150762a39d1cf8e9f95eab71cda9039d2` | **CONCORDANT** |
| `B4` | Skenderis `2312.17316v2` | 1 223 061 / 1 223 061 | `7102dcf9eea6ef0fc9cbbfddc3c2e5ce0c94c6d68fabc4dcc4d13f5580370541` | **CONCORDANT** |

Les quatre portent la magie `%PDF-1.5` et la queue `%%EOF`. **Aucun écart, ni en taille, ni
en sha256, sur aucune des quatre lignes.**

### 1.2 Canaux de fourniture — distincts, et déclarés comme tels

- **`B4`** : déposé par l'opérateur sur le **mount principal**, horodaté 17:10, mesuré sur place.
- **`B1` / `B2` / `B3`** : archive `2503_09372v2.zip`, sha256
  `0d73fa8ba697b41321fd085ceed21f67c02760665c6baf790bbc93108e8ac758`, **3 entrées**.
  **Le nom de l'archive désigne un seul corps et en porte trois** — illustration de plus du
  principe de la note S14 §3 : *un nom de fichier n'atteste rien.*
- **Le ZIP comme CONTENANT DE TRANSPORT n'est pas le ZIP comme SUBSTITUTION DE CONTENU.**
  La leçon opposable S2–S14 — *« un paquet ZIP de TEXTES extraits ne permet PAS la
  confrontation octet »* — vise le cas où une dérivée (OCR, texte, rendu page à page)
  **remplace** les octets d'origine. Ici les entrées **sont** les octets d'origine,
  restitués exacts à l'extraction, confrontés **après** extraction. La leçon n'est ni
  contredite ni contournée : elle ne porte pas sur ce cas. **La distinction est nommée ici
  pour n'être pas à réinventer.**

### 1.3 Témoignage non corrélé sur `B2`

`B2` est parvenu **deux fois par deux canaux distincts** : dans l'archive, et en fichier
libre. `cmp` **rc=0, byte-identiques**. C'est, au sens `R-54`, le **seul** élément de la
séquence qui ne soit pas un témoignage unique. **Il porte sur une ligne, pas sur quatre.**

### 1.4 Imputation de l'écart déclaré BLOQUANT en S14

L'écart consigné par `NOTE-REPRISE-GIT-S14.md` §3 est **entièrement imputé, et il n'était
pas où le libellé le plaçait** : il ne venait **pas** du registre, fidèle sur ses quatre
lignes, mais de la **nature de la surface** qui servait ces noms. Fait de classe déjà
consignée à `3419d49` (S10) et `af97865` (S11). **Ce n'était pas une découverte en S14, et
ce n'en est pas une ici** : ce qui est neuf, c'est **la mesure qui l'impute**, pas le fait.

⟹ **`LC-BETA-04` §1.5 est FAIT sur les quatre lignes de l'ensemble B**, par
re-confrontation et non par première mesure.
⟹ La mention *« BLOQUANT pour `S-B1` sur l'ensemble B »* est **LEVÉE**.

### 1.5 Instabilité des surfaces — mesurée pendant la session

- **mount principal** : à l'ouverture, sept `.pdf` **tous** archives ZIP (`PK\x03\x04`),
  aucune entrée `.pdf` à l'intérieur ; ~20 min plus tard, `B4` en vrai PDF et les trois
  autres homonymes **disparus**.
- **pièces jointes** : trois fichiers apparus entre 17:07 et 17:09, absents à 16:56.
- **dépôt git** : **n'a pas bougé** — arbre propre à l'ouverture comme à la clôture.

**Conséquence de méthode, opposable** : sur ces surfaces, *mesurer* et *avoir mesuré* ne
sont pas la même chose. **Une confrontation payée se préserve hors surface tournante au
moment où elle est obtenue**, sinon elle est à repayer. Les octets des quatre corps sont
conservés en scratch de session, hors dépôt, hors mount, hors KB. Ce n'est **pas** un dépôt
et n'en tient pas lieu (`R-55`).

## §2 — Ce que cette concordance N'ÉTABLIT PAS

**Un sha256 atteste des octets. Il n'atteste ni un titre, ni des auteurs, ni un DOI, ni une
date, ni un grade éditorial, ni un objet.** Quatre concordances parfaites ne déplacent
**aucun** des points restants de `R-41` : §1.2 (≥3 miroirs indépendants), §1.3 (grade
éditorial écrit), §1.4 (objet vérifié, pas le titre) — **dus sur les quatre lignes**.
**Ensemble A : rien n'est fait, rien n'a bougé.** PDF absents, identités attestées nulle
part. **L'issue FANTÔME reste ouverte et honorable.**

**`P-0` n'est pas rendu. `S-B1` n'est pas ouvert. Aucune ligne n'est classée.**

## §3 — Ce qui est RECONDUIT INCHANGÉ depuis l'amendement nº1

Espace de classement `C-i`/`C-ii`/`C-iii`/`C-iv` · espace de verdict `T-a`/`T-b`/`T-c`
(gel amont `b5276e68…f175eb`) · cibles `TH-1..TH-4` + `TH-R` (`37bc85e5…e1e73f`) ·
pare-feu `FB-1..FB-6` · régime **STÉRILE** de `S-B1`, hors anti-fit parce qu'il ne teste
rien · anti-circularité `K` · hors-périmètre explicite des candidats genuine-dS deux-bords
armés non lus · **antériorité Skenderis** : `B4` se classe sous la grille **PUIS** se
confronte à l'adjudication du dossier, jamais l'inverse.

**L'ISSUE ANTICIPÉE de l'amendement nº1 §6 est RECONDUITE MOT POUR MOT et n'est pas
retouchée** — A en `C-iii`/`C-iv` pour les trois ; B sans aucune ligne en `C-i`, au plus une
en `C-ii` ; `S-B2` non armé ; chantier refermé sur une **délimitation**. **Elle a été écrite
avant la re-confrontation et elle le reste.** La réussite de l'item 1 ne l'améliore pas d'un
cran, et toute retouche à ce stade lui retirerait son prix.

---

## §4 — ARBITRAGE OPÉRATEUR nº1 (2026-07-25) — DISSOLUTION PAR ENSEMBLE

La proposition du §4 de l'amendement nº1, posée NON ARBITRÉE, est **ARBITRÉE : retenue**,
avec deux clauses complémentaires. Elle **remplace** la condition globale de `LC-BETA-05`
§5 pour le périmètre étendu.

### 4.1 Condition de dissolution — évaluée PAR ENSEMBLE

> Pour chaque ensemble `E ∈ {A, B}`, **évalué séparément et jamais globalement**, `E` est
> **PROPOSÉ À LA DISSOLUTION** si les trois conditions sont vraies :
>
> **(i)** aucune source **CLASSÉE** de `E` n'est en `C-i` ni en `C-ii` ;
> **(ii)** **au moins une source de `E` a effectivement été classée** *(clause de
> non-vacuité, §4.2)* ;
> **(iii)** aucun **levier neuf FALSIFIABLE ET DATÉ** n'est nommé pour `E` *(§4.3)*.
>
> **La décision de dissoudre appartient à l'opérateur, jamais au pilote** — `LC-BETA-05` §5,
> inchangé sur ce point.

**Symétrie, opposable dans les deux sens** : `B` ne peut pas armer `S-B2` au motif que `A`
resterait ouvert ; `A` ne peut pas être maintenu au motif que `B` resterait ouvert.

**Motif.** L'arbitrage « les deux » n'a pas élargi un périmètre : il a **fusionné deux
chantiers d'objets différents** sous une grille commune. `A` a été retenu pour la **synthèse
d'un article** ; `B` a été retenu comme **intrants de β**, donc contre le mur. Une condition
unique sur deux objets distincts n'est pas une politique sévère, c'est une **erreur de
catégorie**. Sous condition globale, **une seule ligne de `B` — l'ensemble pré-sélectionné
pour sa pertinence supposée — décide du sort des sept**, et la délimitation sur `A` peut
n'être jamais écrite. Or `LC-BETA-05` §4 pose que **réfuter une hypothèse du pilote est le
meilleur usage connu de ce programme**, et `A` **est** l'hypothèse du pilote.

### 4.2 Clause de NON-CLASSIFIABILITÉ — statut `SUSPENDU`

La précondition dure de `R-41` est : **pas d'identité ⟹ pas de positionnement**. Une source
dont l'identité est **FANTÔME**, ou dont les octets n'ont pas été fournis, **n'est pas
classable** — elle ne tombe dans aucune des cases `C-i..C-iv`.

> **Statut `SUSPENDU POUR NON-IDENTIFICATION`.** Il est **porté comme ligne écrite**, avec
> son motif (fantôme / non-fourniture / identité infirmée). Il **n'est ni un déclencheur de
> dissolution, ni un motif de maintien.** Une ligne suspendue **ne compte pas** au (i) et
> **ne satisfait pas** le (ii).

**Motif.** Sans cette clause, l'espace-verdict n'a pas de case pour le cas qu'il rend le
plus probable. Si `A` revient FANTÔME sur ses trois lignes, *« aucune source de A en
`C-i`/`C-ii` »* est **vrai par vacuité**, et `A` se dissoudrait **pour non-fourniture de
PDF** — un fait administratif présenté comme un résultat. C'est le précédent S10 nº3 : *un
espace-verdict déclaré exhaustif doit prévoir le cas qu'il n'a pas prévu*, et c'est le
précédent S9 sur la **vacuité structurelle** : *un assert qu'aucun porteur ne traverse est
un faux PASS même s'il est vrai.*

### 4.3 Clause de LEVIER FALSIFIABLE

Le second conjoint de `LC-BETA-05` §5 — *« aucun levier neuf n'est nommé »* — est, tel
qu'écrit, **entièrement à la main du pilote** : nommer ne coûte rien, donc la condition ne
se déclenche jamais.

> Un **levier neuf** ne compte que s'il est écrit avec **(a)** l'énoncé de **ce qu'il
> faudrait exhiber**, **(b)** le **critère qui déciderait dans quel sens**, et **(c)** une
> **date antérieure** au rendu de `S-B1` sur l'ensemble concerné. À défaut, **il ne compte
> pas**, et le (iii) est satisfait.

*Exemple du levier déjà au dossier, qui satisfait (a) et (b) et reste **NON ARMÉ** : une
preuve d'(in)admissibilité du graviton propageant mixed-BC deux-faces au `𝓘⁺` genuine, sans
cutoff — non-admissible ⟹ `T-c`, admissible ⟹ construction neuve à bâtir.*

### 4.4 Garde anti-fit sur la clôture — le risque que cet arbitrage crée

**Nommé contre lui-même.** La dissolution par ensemble rend les clôtures **plus faciles à
encaisser comme des acquis** : le pilote peut clore `A` à bon compte pour banquer un
livrable, puis continuer sur `B` avec le sentiment d'avoir produit. C'est un risque de fit
d'une autre forme : **produire des clôtures comme on produirait des résultats.**

> **Garde.** Une clôture d'ensemble se rédige comme une **DÉLIMITATION À CONTENU NOMMÉ** —
> *« les trois sources de la piste article ne comblent pas la cellule `R1″∧R2″∧R4″` »* —
> **jamais** comme un changement de statut. **Une délimitation sans contenu n'est pas une
> clôture.**

---

## §5 — ARBITRAGE OPÉRATEUR nº2 (2026-07-25) — RÉGIME DES SURFACES

### 5.1 La glose qui étendait le pare-feu au dépôt est RETIRÉE

**Texte gelé, source, `LC-BETA-05` §1 :** *« Sens 1 — β ⇏ KB. Aucun fichier `LC-BETA-*` ni
`BETA-COPIE-*` ne réside JAMAIS sur `/mnt/project`. »*

**Il dit `/mnt/project`. Il ne dit rien du dépôt.** Le « ni au dépôt » apparaît dans
`NOTE-REPRISE-GIT-S14.md` §5, puis est recopié dans `PROMPT-OUVERTURE-S15` §5. **C'est une
glose qui a élargi une règle gelée au-delà de sa source**, et `LC-BETA-BOOT.py`
n'implémente que la source — il inspecte le mount, jamais le dépôt. **L'instrument et la
règle sont d'accord ; c'est la note qui a dérivé.** Précédent S14 nº1 : *le dépôt se mesure,
il ne se déduit pas* — et une règle aussi.

⟹ **La glose est retirée. Le pare-feu vaut ce que dit sa source : `/mnt/project`, sens 1 ;
projet β, sens 2.**

### 5.2 Les pièces de GOUVERNANCE β vont au git — c'était déjà tranché

`NOTE-REPRISE-GIT-S14.md`, champ `autorite` (régime G-4, tranché le 2026-07-25) : *« Pour
les pièces de GOUVERNANCE (prompts, notes de reprise, **amendements**), le dépôt git fait
foi. »* Un amendement de périmètre **est** une pièce de gouvernance.

**Il n'y avait donc pas de contradiction entre `R-7` et le pare-feu.** Il y avait une glose
sans source, opposée à un arbitrage qui, lui, en avait une.

### 5.3 L'objet réel du pare-feu : l'anti-duplication, pas l'anti-préfixe

Motif écrit à `LC-BETA-05` §1 : *« La piste article a contaminé le mount principal au moins
deux fois. Le motif n'était jamais la malveillance : c'était la commodité. »* Ce que le
pare-feu protège, c'est le **§0-lite de la KB principale** contre des fichiers qui
fausseraient ses comptes, et la KB contre une **seconde copie de sa propre substance** qui
prêterait serment sur un état résumé (`R-54`).

**La partition existe déjà dans les données, mesurée le 2026-07-25** : **35 `BETA-COPIE-*`
ont une contrepartie `kb/`** (34 byte-identiques, 0 divergente) ; **8 `LC-BETA-*` n'en ont
aucune**. Ce ne sont pas deux noms, ce sont **deux natures**.

**Retournement à consigner** : **le pare-feu élargi est la cause de l'écart §7.1.** Les huit
pièces `LC-BETA-*` mentent par âge sur `P-8` précisément parce qu'elles sont mount-seul et
que **rien ne les confronte**. Sous contrôle de version, un mensonge par âge devient visible
par `diff`. **La règle telle que glosée fabriquait le défaut qu'elle ne détectait pas.**

### 5.4 Régime par surface — ce qui est interdit, ce qui est inspecté

| surface | objet (G-4) | interdit — dur | inspecté par |
|---|---|---|---|
| **mount `/mnt/project`** | KB active, espace **vivant** | toute `BETA-COPIE-*` **et** toute `LC-BETA-*` — **inchangé, c'est la source gelée** | `LC-BETA-BOOT.py` §pare-feu (**existant, mordant** : mount monté, 0 le 2026-07-25) |
| **projet β** | atelier du chantier | tout fichier **sans** préfixe β (sens 2) | `LC-BETA-BOOT.py` §intrus (existant, 0) |
| **dépôt git** | espace de **consignation**, tiers-reproductible | **toute copie de substance** (`BETA-COPIE-*`), arbre **et historique** — la duplication est ce qui est visé | **`LC-BETA-CONTROLE-DEPOT.py`, MANDATÉ ici** |
| **dépôt git** | — | les **pièces de gouvernance** β y sont **attendues**, pas interdites | **même instrument** : présence + confrontation sha atelier ↔ dépôt |

### 5.5 Mandat de l'instrument `LC-BETA-CONTROLE-DEPOT.py`

**À la lettre, et prouvé par AUTO-TEST MORDANT** (précédent S13 : *chaque garde a un porteur
mutable, sinon faux PASS*) :

1. **Zéro `BETA-COPIE-*` dans l'arbre du dépôt** ⟹ sinon `exit ≠ 0`.
2. **Zéro `BETA-COPIE-*` dans TOUT l'historique git** ⟹ sinon `exit ≠ 0`. *(Motif : git
   conserve tout blob pour toujours ; un retrait de l'arbre ne retire rien de l'historique.)*
3. **Chaque pièce de gouvernance déclarée au manifeste est PRÉSENTE au dépôt** ⟹ sinon
   `exit ≠ 0`.
4. **Chaque pièce présente est BYTE-IDENTIQUE à sa copie d'atelier** ⟹ sinon `exit ≠ 0`.
5. **Manifeste absent ⟹ `exit ≠ 0`** — un contrôle sans référentiel ne contrôle rien.
6. **Manifeste DÉCLARANT ZÉRO PIÈCE ⟹ `exit ≠ 0`** — **garde de non-vacuité** : un contrôle
   qui passe sur l'ensemble vide est un faux PASS (précédent S9).
7. **Il n'embarque AUCUNE valeur attendue** (`R-36`) et **n'atteste que des octets**.

---

## §6 — Correction de rédaction induite sur `LC-BETA-03` §3

`LC-BETA-03-CADRAGE` §3, condition 3, écrit : *« **Trois** sources en `C-iii`/`C-iv` ⟹
`S-B2` N'EST PAS ARMÉ »*. Rédigé quand le périmètre en comptait trois, **périmé par
l'extension à sept**.

> **Lire désormais** : *« **Toutes les sources classées du périmètre** en `C-iii`/`C-iv`
> ⟹ `S-B2` n'est pas armé »*, et, sous l'arbitrage §4, **par ensemble**.

Les cinq conditions cumulatives d'armement de `S-B2` sont **inchangées pour le reste**, y
compris la nº1 (`P-8` soldé — voir §7.1) et la nº2 (`P-0` rendu).

---

## §7 — ÉCARTS DE SESSION, imputés

### 7.1 Le paquet β gelé MENT PAR ÂGE sur `P-8` — imputable au paquet

`LC-BETA-BOOT.py` l.103 (*« que P-8 est soldé. Il ne l'est pas »*) et
`LC-BETA-00-PROMPT-PROJET.md` §6 (*« PRÉREQUIS BLOQUANT »*) sont **périmés** : `P-8` est
soldé et déposé (`cad358a`), instrument `7d63b9ed…2fc9`, auto-test **6/6 rejoué conforme le
2026-07-25**.

**Ce défaut n'est pas couvert par la confrontation « 34/35 byte-identiques »**, qui ne porte
que sur les copies. Les huit pièces `LC-BETA-*` n'ont **jamais** été confrontées, faute de
contrepartie `kb/`. **La formule « le gel ne ment pas par âge » est donc trop large** : elle
vaut pour les 35 copies, pas pour les 8 pièces de packaging. **À restreindre dans toute
reprise future.** Défaut **sur-restrictif** — il interdit plus que la réalité, il n'autorise
rien — donc **non bloquant**. Correction par pièce séparée datée, **jamais d'office**.

### 7.2 Contradiction fabriquée par lecture d'une note — imputable au PILOTE

Le pilote a présenté à l'opérateur une contradiction `R-7` ↔ pare-feu **qui n'existait
pas**, en lisant la glose de la note S14 §5 au lieu de la source gelée `LC-BETA-05` §1
(§5.1). Il a en outre proposé, comme conduite recevable, de **renommer une pièce pour passer
sous un contrôle nominal** — c'est-à-dire de contourner une règle plutôt que d'en mesurer la
portée. **C'est le précédent S14 nº1, commis une troisième fois dans le dossier.** L'erreur a
été relevée par la mesure de la source, pas par la mémoire.

### 7.3 Contamination du gel de dossier — imputable au PILOTE

Le pilote a écrit la v0.1 du présent amendement **dans le répertoire du paquet gelé**.
Mesuré : `PKG_SHA_BETA_8` est passé de **`dc276129` à `687ed70b`**, `N_haches` de **42 à
43** — **et `LC-BETA-BOOT.py` a rendu `rc=0`**. Le pare-feu ne l'a pas vu : il est
**nominal**, et un fichier préfixé `LC-BETA-` est réputé légitime. **Une pièce neuve déplace
donc silencieusement l'identité du paquet.** Corrigé : la pièce a été sortie du paquet, et
`dc276129` / 42 hachés ont été **re-mesurés et retrouvés**.

**Fait structurel à nommer, plus grave que l'écart lui-même** : la recette `PKG_SHA_BETA`
hache **le contenu courant d'un répertoire**. Un « gel de dossier » sur un répertoire qui
reçoit du travail **n'est pas un gel, c'est un haché mouvant**. Ou le paquet est
**archive**, et le travail se fait ailleurs ; ou son haché n'est pas une référence stable.

### 7.4 `sources/` reste hors compte au §0-lite

Reste-à-faire de la note S14 §6.2. Confronté quand même en S15 : trois intrants
**concordants** (`04d9b4f4`, `27a94980`, `113ab4a2`), plus deux réapparitions en pièces
jointes, **concordantes** elles aussi.

### 7.5 Registre de corpus — toujours NON ARBITRÉ

Les octets des quatre corps sont désormais **confrontés** mais toujours **absents du git**.
Un tiers ne peut toujours pas reproduire la partie **LUE** du programme. Sous G-4 prospectif
ce n'est pas une faute rétroactive ; l'écart se paiera à la première bascule de branche.

---

## §8 — PROPOSITION, NON ARBITRÉE : paquet ARCHIVE, atelier séparé

*Conséquence directe du §7.3, apparue APRÈS l'arbitrage nº2 et donc non couverte par lui.*

> Le répertoire `LC-BETA-PAQUET` est déclaré **ARCHIVE, byte-gelée à
> `PKG_SHA_BETA = dc276129c6ffcb55bf1bfa6fadebdd967f77a02ca3138cdf1eb9649d33c7769f`,
> 42 hachés**. **Aucune pièce n'y est jamais ajoutée.** Le travail de session vit dans un
> **atelier distinct**, et les pièces de gouvernance qui en sortent vont **au git** (§5.2).

**Motif** : c'est la logique de G-4 appliquée un cran plus bas — espace vivant / espace de
consignation. Et c'est la seule façon dont `dc276129` reste **re-vérifiable indéfiniment**
au lieu d'être une valeur qui change à chaque session.

**Cette proposition n'est pas un arbitrage.** Sans décision opérateur, le régime actuel reste
en vigueur, **avec le défaut du §7.3 déclaré et opposable**.

---

## §9 — Ce que cet amendement ne peut PAS rendre, quoi qu'il advienne

`{A4 ; A2★ ; N}` réduit · `D1` clos · `N` fixé · `A4` réduit · `A2★` tranché · `O₂`
construit · `p` fixé · le P-sélecteur tranché · CCC démontrée ou réfutée · `P-0` réputé
rendu · `S-B1` réputé rendu · `S-B2` armé · `P-8` réputé **mesuré** (`P-9` mesure `P-8` à la
gate, pas ici) · une identité éditoriale · une pertinence · une physique.

---

**§6.4 — sentinelle.** Confronter des octets n'identifie aucun article. Imputer un écart ne
lève aucune question. Arbitrer un régime ne mesure rien. Lever un bloquant n'ouvre aucune
gate. Geler n'est pas prouver ; déposer n'est pas réparer (`P-9`) ; rendre un livrable ne le
dépose pas (`R-55`). `{A4 ; A2★ ; N}` **INCHANGÉ** · `[B]` = B-PAUVRE · `D1` non clos, `D1c`
intacte · `N` non fixé (≡ Λ, `R-53` 0/4) · `O₂` non construit · **β `T-b`, NON RÉSOLU, SEUL
facteur d'O₂ ouvert** · `G3-a` non levé · nœud (i) INDÉTERMINÉ · Silo R clos à 12/12 ·
**CCC n'est ni démontrée ni réfutée.**
