---
id: SCELLE-OPERATIONNEL-INSTRUCTION
titre: "Partition du corpus en SCELLÉ et OPÉRATIONNEL. Le régime d'inaltérabilité byte-intacte est BORNÉ aux pièces scellées ; les pièces opérationnelles — note de reprise, prompt d'ouverture, instructions de conduite — se RECALENT EN PLACE, l'historique git faisant l'audit. Arbitrage opérateur S19, correctif nº2."
codename: LC-RACCORD
type: "instruction de gouvernance — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
perimetre_liant: "audit/ , instruments/ , hors-KB/ , racine. kb/ EXCLU — sous gel du manifeste v2.124."
---

# Partition SCELLÉ / OPÉRATIONNEL

## §0. Les faits mesurés qui motivent l'instruction

Trois mesures, prises en S19 sur clone neuf, aucune déduite d'une note.

1. **`NOTE-REPRISE-GIT-S18.md` se contredit elle-même.** Son §6.3 porte
   `G-5b/c : index LC-00-INDEX ABSENT de kb/ · NON ARBITRÉ` quand son propre §5ter.2 le
   donne **déposé en S18, v1.78, 236 461 o**. Trois autres lignes du même §6.3 sont dans le
   même état (`G-1 hors-KB/A/ non fourni` · `Sort de R-23 : MAINTIEN` · `sources/ hors compte
   NON ARBITRÉ`), et son §9 porte `audit/ 55` quand son §0 porte 62. Son titre H1 annonce
   « Note de reprise **S17** ».
2. **Ni la note ni le prompt ne sont scellés.** Mesure : `NOTE-REPRISE-GIT-S18`,
   `PROMPT-OUVERTURE-S19`, `NOTE-REPRISE-GIT-S17`, `PROMPT-OUVERTURE-S18` — **0 occurrence
   sur 4** dans `manifest/LC-WORK-AUDIT-PAQUET-GEL-v2_124.md`, dont le §0 est gelé à
   « 228 = 215 `.md` + 13 `.py` ». Le front-matter de la note l'écrit d'ailleurs elle-même :
   *« note de reprise — HORS base scellée »*.
3. **Le coût est mesuré.** Lecture obligatoire à l'ouverture : 11 220 o (prompt S19)
   + 53 691 o (note S18) + 3 262 o (`S0LITE-IMPRESSION-INSTRUCTION`) = **68 173 o**. La sortie
   intégrale du §0-lite, comprimée d'un facteur 11 en S18 pour libérer précisément ce budget,
   pesait **68 966 o**. L'appareil pèse, à 1 % près, ce qu'on a comprimé pour lui faire place.

## §1. La collision de règles, nommée

Deux règles gouvernent aujourd'hui le même objet et elles sont incompatibles :

> **A.** *Un défaut se nomme et s'amende par FICHIER SÉPARÉ DATÉ, jamais en place ; la pièce
> amendée reste BYTE-INTACTE.* (précédents S8/S9)
>
> **B.** *La note de reprise est UNIQUE et AUTOPORTANTE.*

**A** est juste pour une pièce scellée : un sceau modifiable n'est pas un sceau, et l'amendement
par fichier séparé est le seul moyen de nommer un défaut sans casser un gel. **B** exige la
suffisance : une pièce dont le §6.3 contredit le §5ter **n'est pas autoportante**. Appliquer A
à l'objet de B produit mécaniquement, à chaque session, une pièce qui affirme des faits que le
pilote doit savoir ne pas croire — et savoir lesquels exige de lire N fichiers d'amendement.
**Le stock de faux croît, la taxe de lecture croît, et le risque de faux acquis avec elles.**

**Ce qui rendait A nécessaire n'existe pas ici** : A protège contre la perte des octets
antérieurs. Git rend cette perte impossible. **A est sur-appliquée à des objets que git protège
déjà.**

## §2. La partition — définitions, et le test qui classe

### SCELLÉ

- Tout ce qui est haché au manifeste `v2.124` : les **215 `.md`** de `kb/` et les **13 `.py`**.
- `instruments/archives-scelees/` (76 `.py`).
- Toute pièce de TYPE `GEL`, `CIBLES-GELEES`, `ADJUDICATION`, `VERDICT`, `REDEMONSTRATION`,
  `RAPPORT` — c'est-à-dire tout ce qui **fige une cible avant mesure** ou **rend un résultat**.
- `audit/beta-paquet-gouvernance/` (8 pièces `LC-BETA-*`), statut ARCHIVE byte-gelée.

**Régime : INCHANGÉ.** Byte-intactité absolue. Amendement par fichier séparé daté, jamais en
place, numéro strictement croissant et jamais réattribué, un amendement rétracté reste au dépôt.

### OPÉRATIONNEL

- `NOTE-REPRISE-GIT-S<n>.md` et `PROMPT-OUVERTURE-S<n>.md`.
- Les pièces de TYPE `INSTRUCTION` et `RESERVE` — conduite de session, pas résultat.
- `INVENTAIRE`, `REJEU` — dont le contenu est régénéré par un instrument.

**Régime : RECALAGE EN PLACE, versionné.** La pièce est corrigée, son `version:` de
front-matter est incrémenté, et **l'historique git fait l'audit** — `git log -p` restitue par
sha ce que la pièce disait à l'instant où le pilote a agi sur elle, mieux qu'une chaîne
d'amendements ne le fait.

### Le test, trois questions

1. **La pièce est-elle hachée au manifeste, ou fige-t-elle une cible avant mesure, ou rend-elle
   un résultat ?** Oui ⟹ SCELLÉ, sans discussion.
2. **Sa fonction est-elle de dire au pilote quoi faire, ou de dire au lecteur ce qui a été
   trouvé ?** Dire quoi faire ⟹ OPÉRATIONNEL.
3. **En cas de doute** ⟹ SCELLÉ. Le défaut d'une pièce trop protégée est une taxe de lecture ;
   le défaut d'une pièce trop peu protégée est un gel cassé. Ils ne sont pas de même gravité.

## §3. Ce que le recalage doit porter — la condition de traçabilité

Un recalage en place n'est licite que s'il est **vérifiable après coup**. Trois obligations,
cumulatives, et un recalage qui en manque une est un écart :

1. **`version:` incrémenté** en front-matter. Une pièce recalée sans bump est indistinguable
   d'une pièce réécrite en silence.
2. **Champ `recalages:`** listant, par entrée : le § touché, le fait mesuré qui l'a rendu faux,
   et la session du recalage. Le fait, jamais l'intention.
3. **Message de commit nommant les § recalés**, un par un. Un recalage qui ne vit que dans le
   diff n'est pas porté — précédent S16 nº10.

**Le registre du défaut ne disparaît pas.** Ce qui change, c'est qu'il cesse d'habiter la pièce
opérationnelle : il va dans la section d'audit de la note de reprise, où il est **daté, imputé
et confronté**. Nommer ET corriger, au lieu de nommer OU corriger.

## §4. Gardes — ce que cette instruction n'autorise pas

- **Elle n'autorise à toucher aucun gel, aucun sceau, aucune cible gelée, aucun verdict, aucun
  rapport rendu.** Le périmètre SCELLÉ est intact et son régime ne bouge pas d'une ligne.
- **Elle n'autorise pas la réécriture de l'historique git.** `rebase`, `amend`, `force-push` :
  interdits, comme avant. Le recalage est un commit de plus, jamais un commit de moins.
- **Elle n'autorise pas à effacer un écart.** Un écart imputé reste imputé, daté, et se recopie.
  Corriger la pièce n'absout pas la faute ; c'est le contraire — la correction la date.
- **Elle ne rétroagit pas.** Les pièces d'amendement déjà déposées (`LC-PROMPT-S17-DEFAUTS-DAGE`,
  `LC-BETA-DEFAUTS-DAGE-PAQUET`, les `-AMENDEMENT-<n>`) **restent au dépôt, byte-intactes**.
  Portée **PROSPECTIVE**, comme G-4 et comme la norme de nommage.
- **Elle ne classe pas `kb/`.** `kb/` reste sous le gel du manifeste, hors périmètre liant.

## §5. Application immédiate, et ce qu'elle change

- `NOTE-REPRISE-GIT-S19.md` naît **OPÉRATIONNELLE**. Les défauts d'âge mesurés sur la note S18
  (H1, §0, §9, §6.3 ×4) ne sont pas amendés par un fichier séparé : ils sont **recalés dans la
  note S19**, et **nommés dans sa section d'audit** avec le fait qui les a rendus faux.
- `PROMPT-OUVERTURE-S20.md` naît **OPÉRATIONNEL**, et porte le correctif nº1 (ouverture en deux
  messages, l'ordre imposé par le canal et non par l'exhortation).
- Les pièces `INSTRUCTION` déposées en S18 et S19 — dont `S0LITE-IMPRESSION-INSTRUCTION` et la
  présente — sont **OPÉRATIONNELLES** : elles se recalent en place quand une mesure les prend
  en défaut.
- `audit/F5-VOIE-I-CIBLES-GELEES.md` est de TYPE **`CIBLES-GELEES`** : elle reste **SCELLÉE,
  byte-intacte, défectueuse et non corrigée**. La partition ne la touche pas, et c'est le test
  de sa bonne application.

## §6. Ce que cette instruction ne fait pas

Elle ne scelle, ne réduit, ne compte, ne démontre rien. Elle ne tire aucune gate, ne classe
aucune ligne, ne touche aucun verdict. `{ A4 ; A2★ ; N }` inchangé. β `T-b`, non résolu, seul
facteur d'`O₂` ouvert. **CCC n'est ni démontrée ni réfutée.**
