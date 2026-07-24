---
id: GEL-V1-F2F5
titre: "Gel de cadrage — VOLET 1 S10, adjudication documentaire de la tension F2/F5 sur la provenance du chiffre « f^ttt_NL = 900 ± 700 » (consignation (a) de R-11). Cadrage figé AVANT toute lecture de source et AVANT toute ouverture de tête."
codename: LC-RACCORD
type: "gel de cadrage — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4). Adjudication DOCUMENTAIRE, pas lot de redémonstration : le Silo R est clos à 12/12 et le reste."
version: 1.0
langue: fr
date: 2026-07-24
session: S10
voie: "(ii) — arbitrée hors session par l'opérateur, confirmée au GO du 2026-07-24. (iii) écartée. (i) en escalade conditionnelle seulement, §9."
---

# GEL V1 — adjudication F2/F5

## 0. Antériorité — PROUVÉE PAR L'ÉTAT DU RÉPERTOIRE, NON DÉCLARÉE

Relevé fait immédiatement avant la première ligne du présent fichier :

- `/home/claude/s10/volet1/` : VIDE (hors `.` et `..`).
- `audit/` du clone : 32 entrées, dont **0** portant `f2|f5|adjud|volet`.
- `instruments/` du clone : 33 `.py`, dont **0** portant `f2f5|adjud|volet`.

Aucun instrument, aucun extrait, aucun log n'existe au moment du gel. Le sha256
du présent fichier est relevé après écriture et **avant** la première commande
touchant une source ; toute pièce ultérieure lui est postérieure par
construction.

## 1. Objet — ce qui est à trancher, et rien d'autre

Deux têtes du dépôt se contredisent sur un même chiffre :

- `LC-D-F2-TTT-PLANCK` porte « f^ttt_NL = 900 ± 700 » **comme lecture de
  2312.12498 Table II** ;
- `LC-D-F5-ETAT-RACCORD` v0.3 (correctif R-23) déclare ce chiffre **NON
  LITTÉRAL dans la source**, caractérisation approximative d'un **σ = O(500)**
  sur le template **gauge-field/axion FFe**.

R-11 a CONSIGNÉ cette tension et ne l'a PAS arbitrée, corps fermés.

**Question unique** : lequel des deux énoncés dit juste sur la **PROVENANCE**
du chiffre. Pas sur sa valeur physique, pas sur la conclusion qu'il sert.

## 2. État de lecture AU GEL — déclaration opposable

À l'instant du gel, et depuis l'ouverture de la session :

- `sources/2312_12498v2.pdf` : **JAMAIS OUVERT**. sha et taille mesurés seuls.
- `sources/2409_10595v2.pdf` : **JAMAIS OUVERT**. sha et taille mesurés seuls.
- Corps de `LC-D-F2-TTT-PLANCK` : **JAMAIS OUVERT**.
- Corps de `LC-D-F5-ETAT-RACCORD` : **JAMAIS OUVERT**.
- Front-matters de ces deux têtes : **NON ENCORE LUS** dans cette session.

Le libellé de la tension au §1 est repris **du prompt S10 lui-même**
(`PROMPT-OUVERTURE-S10.md`, sha256 `de9ce9da8664767e…`, §5 volet 1), et
d'aucune autre pièce. Le cadrage ci-dessous est donc construit **sans aucun
contact avec la matière à juger** — c'est le sens de l'anti-fit ici.

## 3. Pièces admissibles — intrants figés

| Pièce | Chemin | sha256 (16) | octets |
|---|---|---|---|
| Philcox–Shiraishi, *Graviton Parity* | `sources/2312_12498v2.pdf` | `04d9b4f457ef76c0` | 1 895 152 |
| Philcox–Shiraishi, *Beyond the Scalar Sector* | `sources/2409_10595v2.pdf` | `27a949802531ea91` | 2 332 898 |
| Front-matters F2 et F5 | `kb/` | mesurés à l'ouverture | — |

Ces sha sont les **premières mesures faisant référence** posées par les
AMENDEMENTS 1 et 2 au prompt. Ils seront **re-mesurés immédiatement avant
extraction** et confrontés (précédent S8 : un intrant se confronte avant
extraction).

**HORS PÉRIMÈTRE, gelé comme tel** : les pièces homonymes du mount
(`/mnt/project/2312_12498v2.pdf`, `/mnt/project/2409_10595v2.pdf`) sont des
**archives ZIP**, de tailles 3 950 791 o et 5 150 313 o, non extraites et non
mesurées en contenu. Elles ne sont **pas** admissibles au présent volet. Leur
statut relève de G-4 et reste NON TRANCHÉ.

## 4. Définitions figées AVANT lecture

Ce paragraphe est le cœur de l'anti-fit : il fixe ce qui comptera comme
« littéral » avant que quiconque ait vu la source.

- **L-STRICT** — le chiffre est littéral au sens strict si la source imprime,
  pour le mode **ttt**, un couple (valeur centrale, incertitude) rendu
  exactement par les chaînes `900` et `700`, dans un même énoncé.
- **L-ARRONDI** — la source imprime pour le mode ttt un couple distinct dont
  l'arrondi à un chiffre significatif donne 900 et 700 (p. ex. 9xx ± 6xx/7xx).
- **NON LITTÉRAL** — aucune des deux formes ci-dessus, pour aucun template.
- **MÊME QUANTITÉ** — le σ de F2 (700) et le σ de F5 (O(500)) désignent la
  même quantité s'ils portent sur le **même template** ET la **même
  statistique** (même mode, même jeu de données, même convention de
  normalisation). Toute divergence sur l'un des trois ⟹ quantités DISTINCTES.

**Pré-déclaré** : `L-ARRONDI` seul **ne suffit pas** à donner raison à F2. Il
mène à V3, pas à V1. Cette règle est posée maintenant précisément parce
qu'elle est celle qu'il serait tentant de desserrer après lecture.

## 5. Espace-verdict — PRÉ-DÉCLARÉ, EXHAUSTIF, DISJOINT

- **V1 — F2 JUSTE, F5 INEXACTE.** Chiffre L-STRICT pour le mode ttt, situé en
  Table II de 2312.12498v2, sur le template que F2 lui attribue.
- **V2 — F5 JUSTE, F2 INEXACTE.** Chiffre NON LITTÉRAL dans 2312.12498v2, sous
  aucune forme et pour aucun template.
- **V3 — COMPATIBLES, ÉCART DE FORMULATION.** Le chiffre existe dans la source
  mais pas comme F2 le situe : autre table ou autre section, ou L-ARRONDI seul,
  ou template distinct de celui visé par F5.
- **V4 — INDÉTERMINÉ SUR PIÈCES.** Les deux sources admissibles ne permettent
  pas de statuer.
- **V5 — ESCALADE REQUISE.** Trancher exige l'ouverture d'un corps de tête.

**Ordre de résolution figé** (interdit de le réordonner après lecture) :
D1 puis D2 puis D3 puis D4 puis D5 ; V1 si et seulement si D1 = L-STRICT **et**
D2 place le chiffre en Table II **et** D3 concorde sur le template ; sinon V3 si
le chiffre est trouvé sous quelque forme que ce soit ; sinon V2 si D1 rend zéro
occurrence **et** D2 est lisible ; sinon V4 ; V5 seulement si D1–D5 sont tous
mesurés et que la provenance reste indécidable sans le corps d'une tête.

**Aucune issue ne réduit le compte.** V1 comme V2 laissent
`{ A4 ; A2★ ; N }` INCHANGÉ, D1 non clos, D1c intacte, CCC non démontrée NI
réfutée. C'est déclaré ici pour qu'aucun verdict ne puisse être plus tard
présenté comme un acquis.

## 6. Pré-tri [D] / [C] — AU GEL, non reclassable

**Discriminantes [D]** — mesurables sur les pièces admissibles :

- **[D1]** Occurrences de `900` associées à `700` dans 2312.12498v2 : nombre et
  localisation. **Mesuré AVANT toute lecture de table** (une recherche informée
  par la table n'est plus une recherche).
- **[D2]** Table II de 2312.12498v2 : contient-elle une entrée **ttt**
  (f_NL^ttt) ? Valeurs et σ portés.
- **[D3]** Le template **gauge-field/axion FFe** figure-t-il en Table II ?
  Quelle σ ?
- **[D4]** 2409.10595v2, Table III et note 6 : portent-elles une σ = O(500)
  pour ce template ?
- **[D5]** D2/D3 vs D4 : σ(F2)=700 et σ(F5)=O(500) sont-ils MÊME QUANTITÉ au
  sens du §4 ?

**Consignations [C]** — déclarées consignations **maintenant**, donc jamais
reclassables et jamais comptables :

- **[C1]** Corps des têtes F2 et F5 : FERMÉS. Toute affirmation sur l'intention
  du rédacteur est hors compte.
- **[C2]** Statut des archives ZIP du mount : NON TRANCHÉ (G-4).
- **[C3]** Le correctif R-23 lui-même n'est pas réaudité ; seule sa lecture de
  la source est confrontée.
- **[C4]** Aucune conclusion physique n'est tirée ni révisée.
- **[C5]** Si un discriminant se révèle non mesurable sur pièces admissibles,
  il devient consignation **par la présente clause I-c**, et non par décision
  postérieure.

## 7. Protocole de lecture — BORNÉ

1. Re-mesure des deux sha, confrontation à `04d9b4f4…` / `27a94980…`. Écart ⟹
   ARRÊT, rien n'est lu.
2. Extraction texte intégrale vers log (`pdftotext -layout`), **sans lecture** :
   l'extraction n'est pas une consultation.
3. [D1] par recherche de motifs sur le log, **avant** toute consultation de
   table.
4. [D2]/[D3] : consultation de Table II et de sa légende **seules**.
5. [D4] : consultation de Table III et de la note 6 de 2409.10595v2 **seules**.
6. Toute lecture hors de ce périmètre se **CONSIGNE** explicitement au rapport,
   avec ce qui a été lu et pourquoi.

## 8. Plafond de grade — ANNONCÉ AU GEL

**CONSTAT SUR PIÈCES LOCALES**, plafond analogue E-2. Ce plafond ne peut pas
être dépassé, quel que soit le résultat. Il n'autorise ni sceau, ni entrée au
compte, ni retrait d'inconnue, ni changement de statut d'une tête. Le verdict
produira une **note d'adjudication** et, s'il y a lieu, la **désignation** de la
tête à corriger — la correction elle-même relevant d'un GO distinct.

## 9. Escalade — conditionnelle et sur GO seul

Si et seulement si le verdict est **V5**, la voie (i) — ouverture du corps de F2
et/ou F5, KB-local, aucun fetch — est proposée à l'opérateur. Elle ne s'ouvre
pas d'office. Elle exige un **amendement daté en fichier séparé** au présent
gel, le gel restant byte-intact et re-vérifiable après coup.

## 10. Défaut du gel

Tout défaut d'énoncé constaté après coup se **NOMME** et s'amende par **FICHIER
SÉPARÉ DATÉ** (`GEL-V1-F2F5-AMENDEMENT-n.md`), jamais en place. Aucune
tolérance ne se desserre par amendement.

---

*§6.4 — geler, extraire, chercher, lire une table, trancher une provenance :
aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce
soit.*
