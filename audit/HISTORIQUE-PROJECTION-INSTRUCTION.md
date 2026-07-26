---
id: HISTORIQUE-PROJECTION-INSTRUCTION
titre: "Correctif nº3 REFAIT, sur directive opérateur S20. L'enveloppe échouait parce qu'elle DÉPLAÇAIT du contenu ; on ne cache rien par relocalisation dans un dossier où tout ce qui est traçable est lu. Le correctif borne la PROJECTION que la lecture d'ouverture prend de l'historique. REMPLACE ENVELOPPE-ANTICIPATIONS-INSTRUCTION."
codename: LC-RACCORD
type: "instruction de conduite — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
remplace: "audit/ENVELOPPE-ANTICIPATIONS-INSTRUCTION.md (S19, correctif nº3 v1) — qui reste DÉPOSÉE et lisible, et dont le §4 (garde contre le détournement) est REPRIS ci-dessous."
---

# La contamination ne se règle pas par l'emplacement

## §1. Le fait qui a tué la version 1, mesuré en S20

Le correctif nº3 v1 a sorti cinq points contaminants de la note de reprise vers une enveloppe
hachée. **Mesuré à l'ouverture S20 : ils sont rentrés deux fois, par deux portes qu'il ne fermait
pas.**

- **Porte 1 — la pièce défectueuse.** Les cinq points sont restés **verbatim** au §0 de
  `audit/F5-VOIE-I-CIBLES-GELEES.md`, librement lisible, et que le prompt d'ouverture **désigne
  nommément** au pilote.
- **Porte 2 — l'historique, et c'est la porte structurelle.** Les huit marqueurs du §3 de
  l'enveloppe sont **8/8 présents** dans la sortie de `git log --oneline -14` — **le tout premier
  geste prescrit du protocole**, avant même que le prompt soit lu.

**Cause racine.** Dans ce dossier, tout ce qui est traçable est lu : la note est lue intégralement,
le prompt est lu, l'historique est lu **en premier**. **On ne peut pas cacher par relocalisation.**
Une enveloppe n'est opposable que si TOUTES les copies du contenu sont derrière elle — et une
consignation autoportante garantit qu'elles ne le sont pas.

## §2. Le mécanisme exact, et il est mécanique

Mesuré sur les 14 derniers commits :

| | caractères |
|---|---|
| en **sujet** (`%s`) | **31 189** |
| en **corps** (`%b`) | 4 911 |
| commits **sans aucun corps** | **11 / 14** |

**Toute la substance est dans la ligne de sujet**, et `--oneline` rend exactement les sujets. Le coût
et la contamination de la première lecture ne sont pas une propriété de l'historique : ce sont une
propriété de **la projection choisie**.

## §3. INSTRUCTION — deux volets, l'un immédiat, l'autre prospectif

### Volet A — RÉTROACTIF, applicable aujourd'hui, sans réécrire quoi que ce soit

> **La mesure d'ouverture n'est plus `git log --oneline -N`. Elle est :**
>
> ```
> git log --format='%h %<(72,trunc)%s' -N
> ```

**Mesuré sur l'historique EXISTANT : 34 676 → 1 190 caractères. Facteur 29.** Aucune réécriture,
aucun sha déplacé, aucune annonce invalidée.

**Rien n'est caché** : le message intégral reste au dépôt et se restitue par
`git log --format=%B <sha>`, à la demande, **après** que le cadrage est déposé. La troncature est
une **projection**, pas un retrait.

### Volet B — PROSPECTIF, à partir du prochain dépôt

> **Le sujet d'un commit est court (≤ 72 caractères) et purement DÉSIGNATIF. Toute la substance va
> dans le CORPS du message.**

Quand l'historique aura assez de commits conformes, le volet A deviendra redondant. **Il ne se
retire pas pour autant** : la troncature protège aussi des sujets longs d'un pilote distrait.

**RÉÉCRIRE L'HISTORIQUE EST EXCLU.** Cela casserait tous les sha annoncés et déposés depuis S14. Les
sujets gras restent gras ; la projection les borne.

## §4. Pourquoi ce correctif tient là où le précédent a cédé

| | correctif nº3 v1 | correctif nº3 refait |
|---|---|---|
| moyen | **déplacer** le contenu | **borner la projection** |
| vérifiable ? | non — dépend de toutes les copies | **oui — une commande, une mesure** |
| cache-t-il ? | oui, et incomplètement | **non — rien n'est retiré du dépôt** |
| tient si le pilote est distrait ? | non | **oui, c'est le canal qui borne** |

C'est le précédent S19 nº1 appliqué à lui-même : *une consigne qui régule l'ordre interne du pilote
n'est pas vérifiable, donc n'est pas une garde.* Le v1 demandait au pilote de ne pas savoir. Le
refait **ne lui montre pas**, et cela se mesure.

## §5. Ce qui SURVIT de la version 1

L'enveloppe **n'est pas abolie** — elle reste utile pour ce qui n'est ni versionné ni projetable :
anticipations d'issue rédigées exprès, verdicts déjà écrits sur une cible non encore ouverte. Les
**trois interdits du §4 de la v1 sont repris intégralement** :

- **Aucun résultat, aucun verdict, aucune mesure ne va en enveloppe** — seulement ce qui anticipe.
- **L'enveloppe est déposée, publique, hachée.** Cachée au moment de la lecture, jamais au dépôt.
- **Le pilote ne décide pas seul de ce qui y va** : il propose et déclare, il ne trie pas.

Et la **procédure en cinq pas** (cadrage déposé avant ouverture, sha cité puis re-mesuré,
classement point par point) reste **en vigueur**, avec une correction rendue par S20 :

> **Le classement `CONFIRMATION` / `DIVERGENCE` est INCOMPLET.** Il faut une troisième classe,
> **`NON ANTICIPÉ`**, pour ce que le cadrage ne portait pas du tout. S20 a mesuré 0 divergence,
> plusieurs confirmations, et deux points non anticipés qu'aucune des deux classes n'accueillait.

## §6. Ce que cette instruction ne fait pas

Borner une projection ne scelle, ne réduit, ne compte, ne démontre rien. Elle ne répare aucune
contamination déjà acquise — celle de S18/S19/S20 est **consommée** et se paie. Elle vaut pour la
prochaine ouverture.

`{ A4 ; A2★ ; N }` INCHANGÉ · β `T-b`, non résolu, seul facteur d'`O₂` ouvert · **CCC n'est ni
démontrée ni réfutée.**
