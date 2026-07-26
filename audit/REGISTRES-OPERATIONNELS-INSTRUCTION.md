---
id: REGISTRES-OPERATIONNELS-INSTRUCTION
titre: "Les registres de kb/ sont OPÉRATIONNELS, pas scellés — arbitrage opérateur S20. Et une règle neuve qui en découle : DANS UNE PIÈCE OPÉRATIONNELLE, LE CHANGELOG N'EST PAS RECALABLE. Première application : recalage de `R-23 soldée` → `R-23 suspendue à OB`."
codename: LC-RACCORD
type: "instruction de gouvernance — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
---

# Régime des registres, et ce qu'on ne recale pas

## §1. ARBITRAGE OPÉRATEUR — les registres sont OPÉRATIONNELS

Le correctif nº2 (S19) borne le régime d'inaltérabilité **aux pièces scellées**. Il ne dit nulle
part que `kb/` l'est en bloc. **Le pilote S20 a appliqué une règle plus large que son texte** et a
écrit « `kb/` est SCELLÉ, je ne corrige rien » — **écart pilote S20 nº5**, corrigé par le présent
arbitrage.

**DEUX MESURES motivent l'arbitrage, et aucune n'est un argument :**

1. **Les registres bump leurs versions, et l'ont fait depuis F5.** `02_programme` **v1.26 → v1.28**,
   `04_references` **v1.22 → v1.29**, `LC-WORK-BRANCHE-FALSIFIABILITE` **v0.5 → v0.20** entre juin et
   juillet 2026. Une pièce qui porte un `maj:` et incrémente sa version **se recale déjà en place** ;
   la nommer scellée décrivait mal ce qu'elle subit.
2. **Le manifeste n'énumère pas les 215.** Il cite **7 noms de `.md` distincts** sur 191 138 o.
   L'appartenance d'un fichier donné à l'ensemble scellé **n'est pas établissable par mesure**.
   « Ces registres sont scellés » était donc une affirmation **invérifiable**, dans les deux sens.

**ARBITRÉ PAR L'OPÉRATEUR (S20) : les registres — `02_programme`, `04_references`, `AUD`,
`IDX_v211`, `LC-WORK-BRANCHE-FALSIFIABILITE` — sont OPÉRATIONNELS.** Ils se recalent en place sous
les trois obligations cumulatives du correctif nº2. **Les gels, cibles gelées, verdicts et rapports
rendus ne sont PAS concernés et leur régime ne bouge pas d'une ligne.**

**Mapping déclaré** : le correctif nº2 prescrit une entrée au champ `recalages:`. Les registres
portent un champ `maj:` qui **est** leur changelog. L'entrée se fait dans `maj:`, à leur convention,
**et cette substitution est déclarée ici plutôt que faite en silence.**

## §2. RÈGLE NEUVE — dans une pièce opérationnelle, LE CHANGELOG N'EST PAS RECALABLE

Découverte en exécutant le recalage, et c'est le seul acquis de méthode de l'opération.

Les 10 occurrences de `R-23 soldée` dans `kb/` ne sont pas de même nature :

| zone | occurrences | ce que la phrase fait |
|---|---|---|
| **corps** | **4** | **AFFIRME un état courant** — recalable |
| **champ `maj:`** | **6** | **ENREGISTRE ce qui a été écrit à une date** — NON recalable |

> **Un changelog dit ce qui a été écrit, jamais ce qui est vrai.** Le 14 juin 2026, le programme a
> réellement inscrit « R-23 soldée » ; c'est un **fait daté**, et il reste vrai que cela a été
> écrit. Le recaler falsifierait exactement la traçabilité que le recalage est censé servir.

**Corollaire opposable** : un recalage qui touche un champ `maj:`, `recalages:` ou tout journal daté
est un **écart**, pas une correction. La portée d'un recalage s'arrête au corps.

**Conséquence sur le compte annoncé** : le pilote avait annoncé **5 fichiers** à l'opérateur. Après
partition corps/changelog, **`LC-WORK-BRANCHE-FALSIFIABILITE` n'a AUCUNE occurrence au corps — elle
n'est pas touchée. Le recalage porte sur QUATRE fichiers.** Annonce corrigée avant exécution.

## §3. APPLICATION — mesurée, fichier par fichier

| fichier | corps | version | changelog laissé intact |
|---|---|---|---|
| `kb/02_programme.md` | 1/1 recalée | 1.28 → **1.29** | 2 traces |
| `kb/04_references.md` | 1/1 recalée | 1.29 → **1.30** | 2 traces |
| `kb/AUD.md` | 1/1 recalée | 1.71 → **1.72** | 2 traces |
| `kb/IDX_v211.md` | 1/1 recalée | 2.11 → **2.12** | 3 traces |
| `kb/LC-WORK-BRANCHE-FALSIFIABILITE.md` | **0 — NON TOUCHÉ** | inchangée | 1 trace |

**Comptabilité des 10 occurrences restantes, close** : **6** traces historiques antérieures + **4**
citations de l'ancienne formule à l'intérieur des entrées `maj:` de recalage elles-mêmes (elles
écrivent « `R-23 soldée` → `R-23 suspendue à OB` »). **Aucune occurrence orpheline.**

**Motif du recalage** : verdict `audit/R23-AU-FOND-VERDICT.md`, sha256 `07225d4d…e735c59`, commit
`7febb5f` — `C-1` = (a) CONTINGENTE.

## §4. DEUX DÉFAUTS TROUVÉS EN CHEMIN — nommés, NON corrigés

1. **Le front-matter YAML de trois registres est INVALIDE** — `AUD`, `IDX_v211` et
   `LC-WORK-BRANCHE-FALSIFIABILITE` portent un second `maj:` **à l'intérieur** d'un champ, ce qui
   casse le parsing. **Vérifié AVANT (`HEAD`) et APRÈS : INVALIDE dans les deux cas, sur les trois.**
   `LC-WORK-BRANCHE-FALSIFIABILITE`, que le recalage **n'a pas touchée**, est invalide elle aussi —
   **c'est la preuve que le défaut est antérieur et n'est pas l'œuvre du recalage.** `02_programme`
   et `04_references` sont valides avant et après.
2. **`IDX_v211.md` porte sa version dans son NOM** et son champ `version:` passe à `2.12` — le nom
   dit `v211`, le champ dit `2.12`. **Aucun renommage** : renommer casserait les renvois. Défaut
   d'âge de nommage **nommé et laissé debout**.

## §5. Ce que cette pièce ne fait pas

Arbitrer un régime, recaler un mot, partitionner un fichier en corps et journal : aucun de ces
gestes ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit. **`R-23` reste une dette** —
elle change de nom, pas de statut. `W³` reste **sans valeur**, `O₂` n'est pas construite.

`{ A4 ; A2★ ; N }` INCHANGÉ · `D1` non clos, `D1c` intacte · Silo R clos à 12/12 · β `T-b`, NON
RÉSOLU, seul facteur d'`O₂` ouvert · **CCC non démontrée NI réfutée.**
