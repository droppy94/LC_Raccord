---
id: TOPOLOGIE-DEPOTS-INSTRUCTION
titre: "Topologie des dépôts — CINQ et non quatre. Le git y entre. R-54 est BORNÉ AUX INTRANTS. La KB active ne porte plus aucune pièce de kb/, mesuré. Le §2 de LC-CONST-V1 est NOMMÉ PÉRIMÉ et NON TOUCHÉ, la pièce étant scellée. Arbitrage opérateur S19, correctif nº6."
codename: LC-RACCORD
type: "instruction de gouvernance — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
perimetre_liant: "audit/ , instruments/ , hors-KB/ , racine, et la SURFACE /mnt/project. kb/ EXCLU — sous gel du manifeste v2.124."
---

# Topologie des dépôts

## §0. Les faits mesurés en S19, aucun déduit d'une note

1. **`kb/LC-CONST-V1.md` §2 énumère QUATRE dépôts, et le git n'en est pas.** Le tableau porte
   *chez D (hors KB)* · *prompt projet* · **KB active `/mnt/project`** · *session*. La KB active
   y est définie comme **« working set seul, cible 25–35 fichiers »**, de coût **ÉLEVÉ**.
2. **G-4 a institué le git comme espace de consignation en S14 et a été CLOS**, sans que le §2
   de la constitution ne soit recalé — il ne pouvait pas l'être, la pièce est **scellée**.
   **Deux topologies de mémoire sont donc en vigueur simultanément, et aucune n'a été écrite
   comme remplaçant l'autre.**
3. **La KB active ne porte plus aucune pièce de `kb/`.** Mesuré : intersection **0**. Les trois
   `LC-D-O2-*` en étaient les dernières et ont été retirées en S19. Cardinal de la surface au
   cours de la séance : **27 → 14 → 8 → 7** fichiers, masse **48 463 832 → 7 416 114 o**.
4. **`LC-NORME-NOMMAGE` §6.2 bloque la migration de `kb/`** au motif que *« R-54 : le mount est
   autoritaire, le git est miroir »*. **Le côté mount de ce miroir est vide.**
5. **Trois objets distincts se disputent le mot « KB »** : la **KB scellée**, 228 fichiers hachés
   au manifeste v2.124 (215 `.md` + 13 `.py`, PKG `914c077a`) — et `kb/` ne porte **aucun `.py`**,
   les 13 vivent ailleurs, question non tranchée ici ; la **KB active**, `/mnt/project` ; et
   `kb/` comme répertoire du dépôt git.
6. **Deux surfaces ont porté deux versions byte-différentes du même nom, sans que personne ne le
   sache** : `R10-REDEMONSTRATION.md` et `redemo_R10_nonlin.py`, divergence mesurée en S19 —
   CRLF, newline final, un échappement, et une ligne `hh_unused = None` présente au git seul.
   Divergence **cosmétique, non sémantique**, résolue par retrait. **Aucun instrument du dépôt ne
   pouvait la voir.**
7. **Les quatre corps de l'ensemble B sont désormais CONFRONTÉS 4/4 AU BIT** contre
   `audit/LC-WORK-REGISTRE-CORPUS.md` — `B1` `6b89e638…` 979 890 o · `B2` `e080c5d6…` 386 010 o ·
   `B3` `1426146d…` 4 629 572 o · `B4` `7102dcf9…` 1 223 061 o — vrais PDF, `%PDF` et `%%EOF` aux
   octets, **pagination `38 · 14 · 78 · 88` recoupant celle établie par le canal OCR en S17.**
8. **La condition d'arrêt du protocole de boot V97 n'a été exécutée dans aucune des cinq
   dernières sessions.** `LC-WORK-BOOT-SESSION*.py` est présent au git, **absent de la KB
   active**. Le protocole prescrit de recomputer le PKG de la KB active et de **STOPPER** si
   l'écart au manifeste n'est pas nommé. Dette **OUVERTE**, désormais **mesurable**. Rien n'est
   conclu de son issue.

## §1. La table — CINQ dépôts

| dépôt | autorité | contenu | ce qu'on y perd |
|---|---|---|---|
| **chez l'opérateur**, hors KB | l'opérateur seul | l'archive intégrale, byte-exacte, à jamais | **invisible au pilote, non opposable** |
| **git** | **FAIT FOI** — gouvernance, résultats, reproductibilité | tout le haché, l'historique, les instruments, les gels | rien : c'est **la** mémoire |
| **KB active** `/mnt/project` | **INTRANTS SEULS** (§2) | ce que le pare-feu interdit de déposer, et **rien d'autre** | ni version, ni sha propre, ni historique |
| **prompt projet** | la constitution | ~200 lignes plafond | **vieillit sans pouvoir être recalé** (scellé) |
| **discussion** | **aucune** | brouillon, exploration, calcul jetable | tout, à la fermeture |

## §2. ARBITRAGE — R-54 est BORNÉ AUX INTRANTS

> **La KB active fait foi pour ce qu'elle est SEULE à porter — les corps sources que le pare-feu
> interdit de déposer — et pour rien d'autre. Partout ailleurs, et pour toute pièce dont le git
> porte un homologue, LE GIT FAIT FOI.**

Motif, et il est mesuré, non argumenté : sur les deux seules pièces où les deux surfaces ont
divergé, c'est **la version git qui s'exécute et qui rend le `40/14` conforme** du §0-lite. Une
autorité qui n'est jamais celle qu'on exécute n'est pas une autorité.

**Ce que cet arbitrage NE fait PAS :**

- **Il ne débloque pas la migration de `kb/`.** Celle-ci reste **bloquée sur G-4, volet 3**. Le
  présent arbitrage retire un *motif* devenu faux ; il ne rend pas la migration décidée.
- **Il ne touche ni `LC-CONST-V1`, ni `LC-NORME-NOMMAGE`, ni le manifeste v2.124.** Aucune de ces
  pièces n'est modifiée d'un octet.
- **Il ne rétroagit pas.** Portée **PROSPECTIVE**, comme G-4, comme la norme de nommage, comme le
  correctif nº2.

## §3. Gardes — dont une NEUVE, mesurée aujourd'hui

- **NEUVE, S19 — SUR UNE SURFACE SANS VERSION, UNE FOURNITURE DE MÊME NOM EST UNE OPÉRATION
  DESTRUCTRICE SANS TRACE.** Mesuré : le vrai PDF de `B1` a **écrasé** le ZIP-OCR homonyme, qui a
  disparu sans geste de retrait et sans qu'aucune surface n'en garde copie. L'issue fut bonne ; le
  mécanisme eût été le même avec un fichier faux. **Conséquence opposable : toute fourniture à la
  KB active s'annonce avec ses octets et son sha256 AVANT d'être posée, et se confronte après.**
- **La KB active ne porte que des intrants.** Toute pièce qui s'y trouve et dont le git porte un
  homologue est un **écart à nommer**, non une commodité. Trois formes rencontrées en S19 :
  duplicata byte-identique (13 fichiers), duplicata inférieur d'un objet mieux détenu (3 ZIP-OCR
  contre les vrais PDF de `sources/`), copie divergente (2 fichiers).
- **La « cible 25–35 fichiers » du §2 de `LC-CONST-V1` est PÉRIMÉE.** Elle a été écrite pour un
  modèle à quatre dépôts où le git n'existait pas et où la KB active devait porter la substance.
  **Nouvelle cible : le strict nécessaire, sans plancher.** Sept fichiers n'est pas un déficit.
- **Un `%PDF` aux octets n'est pas une identité.** La confrontation de `B1`–`B4` ne vaut que
  parce que le **REGISTRE** porte les sha : la surface, elle, n'en garde aucun. **La KB active
  peut désormais servir des octets confrontables ; elle n'est toujours pas une mémoire.**
- **Dette, portée depuis le correctif nº5** : `instruments/concordance_mount.py`, qui hache la KB
  active contre le clone et déclare `identiques / divergents / exclusifs`, avec auto-test mordant
  **et déclaration de vacuité**. Sans lui, la garde ci-dessus reste une intention. **NON ÉCRIT
  ICI**, GO séparé.

## §4. Le défaut d'âge est ICI INÉVITABLE, et il est choisi en le sachant

`kb/LC-CONST-V1.md` est **scellée** : son §2 périmé ne peut pas être recalé en place, et le
correctif nº2 exclut explicitement `kb/` de son régime. La présente pièce **dit** que le §2 est
périmé **sans le toucher** — c'est-à-dire qu'elle emploie exactement le mécanisme dont le
correctif nº2 vient de mesurer le coût : un lecteur de la constitution y lira une table à quatre
dépôts sans savoir qu'une cinquième colonne existe ailleurs.

**Ce n'est pas une inadvertance, c'est le prix du sceau, et il est payé les yeux ouverts.** La
seule voie qui le supprimerait est un **volet de recalage de la constitution**, geste tout autre,
qui dépend de G-4 pour `kb/` et n'est **pas ouvert ici**. Il est nommé comme reste-à-faire.

## §5. Ce que cette instruction ne fait pas

Elle ne scelle rien, ne recompute aucun PKG, ne rejoue aucun boot, ne vérifie pas la continuité
V96→V97, ne migre aucun fichier, ne tire aucune gate, ne classe aucune ligne, ne touche aucun
verdict. `{ A4 ; A2★ ; N }` inchangé · `D1` non clos, `D1c` intacte · Silo R clos à 12/12 ·
β `T-b`, non résolu, **SEUL facteur d'`O₂` ouvert** · **CCC n'est ni démontrée ni réfutée.**
