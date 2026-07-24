---
id: GEL-V1-F2F5-AMENDEMENT-1
titre: "Amendement 1 au GEL V1 (adjudication F2/F5) — défaut d'énoncé du §3 NOMMÉ : l'exclusion des pièces homonymes du mount reposait sur un motif faux (conflation contenant/contenu). Périmètre de confrontation corrigé, protocole octet ajouté, espace-verdict de la confrontation pré-déclaré."
codename: LC-RACCORD
type: "amendement de gel — FICHIER SÉPARÉ DATÉ. Le gel amendé reste BYTE-INTACT. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-24
session: S10
gel_amende: "GEL-V1-F2F5.md, sha256 201bcfbb1963ea8e83efcacbb1abeaac19d6206872fa7794332024fa4ebd705a — re-vérifié byte-intact immédiatement avant l'écriture du présent fichier."
---

# AMENDEMENT 1 au GEL V1 — daté

Émis le 2026-07-24, sur GO opérateur, **avant** l'exécution du §7 du gel et
**avant** tout contact avec le contenu d'une source.

## 0. Antériorité

Relevé immédiatement avant la première ligne du présent fichier :
`/home/claude/s10/volet1/` ne contenait que `GEL-V1-F2F5.md` ;
`confront/` INEXISTANT ; aucun log, aucun extrait, aucun instrument.

## 1. Le défaut — NOMMÉ, imputable au pilote

Le §3 du gel écarte les pièces homonymes du mount
(`/mnt/project/2312_12498v2.pdf`, `/mnt/project/2409_10595v2.pdf`) du périmètre,
au motif qu'elles sont des archives ZIP « non extraites et non mesurées en
contenu », et que les ouvrir avant le gel aurait cassé l'anti-fit.

**Ce motif est FAUX.** Il repose sur une conflation entre deux gestes distincts :

- **ouvrir le contenant** — lister une archive, en extraire des octets, hacher
  ces octets : aucune information sur la matière à juger n'en sort ;
- **lire le contenu** — consulter le texte, une table, une valeur : c'est cela
  seul que l'anti-fit interdit avant le gel.

La confrontation d'un intrant se fait au **niveau octet**. C'est exactement le
geste posé par les AMENDEMENTS 1 et 2 au prompt S10 (« transfert d'octets seul,
sha mesuré, contenu jamais lu »). Rien n'empêchait de le faire ; il n'y avait
pas à attendre, il y avait à ne pas confondre.

**Coût du défaut** : il laissait G-4 non mesurée là où elle était mesurable, et
justifiait par un obstacle inexistant l'écartement unilatéral de l'autorité
désignée par R-54.

## 2. Ce que le présent amendement corrige

Le §3 du gel est **complété** — jamais réécrit, le gel reste byte-intact :

- Les archives du mount entrent au périmètre **comme objet de confrontation au
  niveau octet**, et à ce titre seul.
- Les **pièces lisibles** de l'adjudication restent celles du dépôt git,
  `sources/2312_12498v2.pdf` (`04d9b4f4…`) et `sources/2409_10595v2.pdf`
  (`27a94980…`), INCHANGÉ.
- La mention « non admissibles au présent volet » du §3 s'entend désormais
  comme « non admissibles **à la lecture** », et non « hors périmètre ».

## 3. Protocole de confrontation — BORNÉ, aucun contenu lu

1. `unzip -l` sur chaque archive : **noms et tailles seuls**.
2. Extraction vers `/home/claude/s10/volet1/confront/`, répertoire séparé, hors
   du clone. Aucun fichier extrait n'est ouvert.
3. `sha256` des octets extraits, confrontation à `04d9b4f4…` / `27a94980…`.
4. **Clause de fuite d'information** : si un nom de fichier interne à l'archive
   est lui-même informatif sur la matière à juger (valeur, table, verdict), il
   se **CONSIGNE** et ne s'exploite pas. Le pré-tri du §6 du gel s'applique.
5. Aucune ouverture, aucune extraction de texte, aucun rendu de page.

## 4. Espace-verdict de la confrontation — PRÉ-DÉCLARÉ

Mesure neuve, donc espace figé avant exécution, exhaustif et disjoint :

- **C-1 — CONCORDANT.** Les octets extraits du mount rendent exactement
  `04d9b4f4…` et `27a94980…`. Mount et git portent la même pièce. G-4 gagne un
  point de mesure favorable à la thèse « git miroir fidèle ».
- **C-2 — DISCORDANT.** Un sha au moins diverge. Deux flux d'octets se disputent
  le titre de source.
- **C-3 — ARCHIVE HÉTÉROGÈNE.** L'archive ne contient pas un PDF unique
  (fichiers multiples, format autre, contenu annexe).

**Conduite en C-2, pré-déclarée** : l'adjudication F2/F5 **NE DÉMARRE PAS**. Le
§7 du gel reste inexécuté. La question remonte à l'opérateur, et G-4 cesse
d'être une hypothèse reconduite pour devenir un **écart mesuré**. Le pilote ne
choisit pas lequel des deux flux fait foi.

**Conduite en C-3** : les fichiers surnuméraires sont listés et consignés, la
confrontation porte sur la pièce PDF si elle existe, C-2 ou C-1 s'applique à
elle ; à défaut de PDF, la confrontation est déclarée non concluante par la
clause I-c ([C5] du gel).

## 5. Ce que le présent amendement NE change PAS

Définitions du §4 du gel (L-STRICT, L-ARRONDI, NON LITTÉRAL, MÊME QUANTITÉ) :
INCHANGÉES. Espace-verdict V1–V5 et son ordre de résolution figé : INCHANGÉS.
Pré-tri [D1–D5] / [C1–C5] : INCHANGÉ. Ordre [D1] avant toute table : INCHANGÉ.
Plafond CONSTAT SUR PIÈCES LOCALES : INCHANGÉ. Escalade voie (i) sur GO seul :
INCHANGÉE.

**Aucune tolérance n'est desserrée par le présent amendement.** Il élargit une
mesure, il n'assouplit aucun critère.

---

*§6.4 — nommer un défaut, lister une archive, hacher des octets : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
