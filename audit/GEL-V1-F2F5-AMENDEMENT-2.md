---
id: GEL-V1-F2F5-AMENDEMENT-2
titre: "Amendement 2 au GEL V1 (adjudication F2/F5) — DEUX défauts NOMMÉS : (1) l'espace-verdict du §5 n'était pas exhaustif, il n'a pas de case pour « les deux têtes inexactes sur des points distincts » ; (2) le périmètre de lecture du §7 est trop étroit pour attribuer le chiffre à un template. Case V6 ajoutée, périmètre étendu de façon BORNÉE et déclarée AVANT lecture. Consignation d'une lecture hors périmètre déjà survenue."
codename: LC-RACCORD
type: "amendement de gel — FICHIER SÉPARÉ DATÉ. Gel et amendement 1 restent BYTE-INTACTS. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-24
session: S10
pieces_amendees:
  - "GEL-V1-F2F5.md — sha256 201bcfbb1963ea8e83efcacbb1abeaac19d6206872fa7794332024fa4ebd705a"
  - "GEL-V1-F2F5-AMENDEMENT-1.md — sha256 fbfe39bdb87813eb534e924d4feadef7151d14c9b1a390b7d7f2e8d69864cdf2"
integrite: "les deux pièces re-vérifiées byte-intactes immédiatement avant l'écriture du présent fichier"
voie: "(β) — extension bornée, choisie par l'opérateur au GO du 2026-07-24, contre l'option (α) amendement minimal."
---

# AMENDEMENT 2 au GEL V1 — daté

## 0. Antériorité et état de lecture

Relevé immédiatement avant la première ligne du présent fichier :
`volet1/` contient `GEL-V1-F2F5.md`, `GEL-V1-F2F5-AMENDEMENT-1.md`, et
`extract/` (`2312.txt`, `2409.txt`, `d1.py`, deux logs d'erreur vides).
Aucun amendement 2 préexistant.

**Ce qui a été lu à ce jour**, et rien d'autre :

- [D1] : recherche de motifs sur `2312.txt`, deux occurrences retournées avec
  leur ligne porteuse (p. 1 et p. 2).
- [D2]/[D3] : Table II de 2312.12498v2 et sa légende.
- [D4] : Table III de 2409.10595v2 et sa légende — **avec débordement**, §3.

**Ce qui n'a PAS été lu** : Table I de 2312.12498v2 ; les corps de F2 et de F5 ;
leurs front-matters ; toute autre section des deux papiers.

## 1. DÉFAUT 1 — l'espace-verdict n'était pas exhaustif

Le §5 du gel déclare son espace-verdict « EXHAUSTIF, DISJOINT ». **Il ne l'est
pas.** Les mesures [D1] et [D2] contredisent chacune une tête différente : le
chiffre est littéral dans la source (contre F5), et il n'est pas en Table II
(contre F2). L'ordre de résolution figé envoie ce cas vers **V3**, libellé
« COMPATIBLES, écart de formulation » — libellé qui **décrit mal** un constat de
double inexactitude. Le gel n'offre aucune case juste.

Défaut d'énoncé, imputable au pilote, au même titre que le défaut F4-1 de R-11.

### Correction — case V6

- **V6 — LES DEUX TÊTES INEXACTES, sur points distincts.** Retenu si et
  seulement si l'énoncé de F2 **et** l'énoncé de F5 sont **chacun** contredits
  par au moins une mesure discriminante [D1]–[D5].
- **Insertion dans l'ordre de résolution : V6 est évalué AVANT V3.** V3 reste
  réservé au cas où **une seule** des deux formulations décroche.
- V1, V2, V4, V5 : positions et définitions INCHANGÉES.

### Aveu de position — le risque de fit est NOMMÉ, pas dissimulé

Le présent amendement est écrit **après** [D1], [D2] et [D4]. Introduire une
case de verdict en connaissant déjà des mesures est précisément la manœuvre que
l'anti-fit combat. Ce risque est réel et je le borne comme suit, faute de
pouvoir l'annuler :

- le critère de V6 est **général** (« chacune contredite par une mesure »), il
  ne mentionne ni un chiffre, ni une page, ni une tête en particulier ;
- **V1 est déjà hors d'atteinte par MESURE, non par redéfinition** : [D2] a
  établi que Table II ne porte pas le chiffre, et la condition de V1 exigeait
  cette localisation. Aucun amendement n'a desserré quoi que ce soit pour l'en
  écarter ;
- aucune définition du §4 (L-STRICT, L-ARRONDI, NON LITTÉRAL, MÊME QUANTITÉ)
  n'est touchée ;
- l'alternative honnête — forcer le cas dans V3 en sachant que le libellé le
  décrit mal — aurait produit une note fausse. Nommer le défaut coûte moins que
  le taire.

## 2. DÉFAUT 2 — périmètre trop étroit

Le §7 n'autorise, pour 2312.12498v2, que Table II et sa légende. Or l'attribution
de « 900 ± 700 » à un template — nécessaire à [D3] et à [D5], et donc à
l'appréciation du fond du correctif R-23 — vit hors de cette table.

### Correction — extension BORNÉE, déclarée AVANT lecture

Ajoutées au périmètre, et **rien d'autre** :

1. **Table I de 2312.12498v2** (p. 11, « Model-independent constraints on tensor
   non-Gaussianity and parity-violation ») **et sa légende**.
2. **La phrase portant chacune des deux occurrences de [D1]**, p. 1 et p. 2 —
   la phrase seule, délimitée par ses points, non le paragraphe.

Sont **exclus** et le restent : Table III et Table IV de 2312.12498v2, toute
autre section des deux papiers, les corps de F2 et F5, leurs front-matters,
toute source externe. Aucun fetch. Aucune archive du mount.

L'extension est déclarée **avant** que la moindre ligne de Table I ne soit lue —
c'est la condition qui la rend admissible.

## 3. CONSIGNATION — lecture hors périmètre déjà survenue

Lors de [D4], la consultation de Table III a été bornée **par numéros de ligne**
sans vérifier où finissait la légende. Ont été lus en sus : une note de bas de
page sur les contributions ISW-lensing, et les premiers paragraphes de la
section V du papier 2409.10595v2.

Ce texte **a été lu**. Il ne porte sur aucun discriminant et **n'est employé
dans aucun raisonnement**. Il est consigné ici plutôt que tu, conformément au
§7.6 du gel.

**Correction de protocole** : tout bornage ultérieur se fait par **détection de
fin de légende**, non par numéro de ligne.

## 4. Ce que le présent amendement NE change PAS

Définitions du §4 : INCHANGÉES. V1, V2, V4, V5 : INCHANGÉS. Pré-tri
[D1]–[D5] / [C1]–[C5] : INCHANGÉ. Règle « [D1] avant toute table » : déjà
honorée, INCHANGÉE. Plafond **CONSTAT SUR PIÈCES LOCALES** : INCHANGÉ.
Escalade voie (i) vers les corps de tête : toujours sur GO seul, INCHANGÉE.
Périmètre de l'amendement 1 (confrontation octet du mount, verdict C-3 rendu,
non concluante par clause I-c) : INCHANGÉ.

**Aucune tolérance n'est desserrée.** Cet amendement ajoute une case de verdict
et trois lectures nommées ; il n'assouplit aucun critère et ne relève aucun
plafond.

---

*§6.4 — ajouter une case, étendre un périmètre, avouer un débordement : aucun de
ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
