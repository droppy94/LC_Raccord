---
id: F5-ANTICIPATIONS-RESERVE
titre: "ENVELOPPE — anticipations connues sur le corps de F5 et sur R-23, sorties de la note de reprise pour cesser de contaminer la lecture d'ouverture. À N'OUVRIR QU'APRÈS dépôt du cadrage gelé sur R-23 AU FOND. Première application de ENVELOPPE-ANTICIPATIONS-INSTRUCTION."
codename: LC-RACCORD
type: "réserve — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
regime: "ENVELOPPE. Déposée, publique, hachée. Son sha256 est cité par NOTE-REPRISE-GIT-S19 et par PROMPT-OUVERTURE-S20, son CONTENU n'y est pas. Le pilote d'une session neuve NE LIT PAS cette pièce avant d'avoir DÉPOSÉ son cadrage gelé."
---

# Enveloppe — anticipations sur F5 et R-23

## §0. AVERTISSEMENT — ne lis pas la suite si tu n'as pas encore déposé ton cadrage

Si tu es le pilote d'une session neuve et que ton cadrage gelé sur `R-23` AU FOND **n'est pas
encore déposé**, **arrête ici**. Reviens après le dépôt, re-mesure le sha256 de cette pièce,
confronte-le à celui que ton cadrage cite, et alors seulement lis les §2 et §3.

Lire avant est un écart, et il est **vérifiable** : le commit de ton cadrage doit précéder, dans
l'historique git, tout usage du contenu ci-dessous.

## §1. Comment cette contamination est née — et pourquoi elle sort d'ici

En S18, un `grep -rn` non borné du pilote a importé le front-matter de
`kb/LC-D-F5-ETAT-RACCORD.md` et des blocs `[TRAITÉ]` de la branche. La contamination a été
**déclarée**, conformément à la discipline anti-fit — mais elle a été déclarée **dans la note de
reprise**, dont le prompt d'ouverture ordonne la lecture intégrale.

**Mesuré en S19 : le pilote a donc acquis les cinq points par la voie prescrite.** Le dispositif
anti-fit était devenu un vecteur de contamination, et la régression était structurelle : une note
autoportante doit tout porter, y compris ce que le pilote ne doit pas savoir.

D'où cette pièce. Le contenu reste **déposé, public et haché** — il n'est pas dissimulé au dépôt,
il est seulement retiré de la **lecture d'ouverture**.

## §2. LES CINQ POINTS — déjà connus, donc NON CRÉDITABLES

Ce qui suit provient d'une lecture non bornée, pas d'une instruction de F5 :

1. **F5 = sélection d'état / CFT de raccordement.**
2. Les **quatre obstructions** s'effondrent sur **`O₂`**.
3. **`A_T ~ 1/C_T ~ 1/N` forcé**, coefficient O(1) libre.
4. **Voie (i) déclarée FAITE en v0.3** ; **Table III** classée **`inconfrontable`**.
5. **`R-23` déclarée SOLDÉE.**

> **Toute coïncidence avec ces cinq points se rend en CONFIRMATION D'ANTICIPATION, jamais en
> découverte.** Une anticipation confirmée ne lève aucune incertitude sur la physique — son prix
> est sa date, pas son exactitude (précédent S17, issue anticipée 4/4).

## §3. Le cadre déjà tranché autour de la cible, à ne pas ré-instruire

- **`[D5]` est LEVÉ** — verdict **`W3` — PAS DE RÉFÉRENT**, tranché **négativement par absence**
  (S11) : « 900 ± 700 » et « σ = O(500) » ne sont pas la même quantité. Rendu sous
  `GEL-V1BIS-D5`, byte-intact (`bd0b40c8c7f72bee`). Le gel prescrivait lui-même que `[D5]` se
  tranche **« sans jamais ouvrir F5 »**. **NE LE RÉ-INSTRUIS PAS.**
- **`audit/F5-VOIE-I-CIBLES-GELEES.md` est DÉFECTUEUSE PAR PRÉMISSE FAUSSE** — elle présupposait
  `[D5]` objet du corps de F5. Elle reste **SCELLÉE et byte-intacte** (`aecd7ad3…`) et **NE SERT
  PAS de cadrage**.
- **Ce qui exige la voie (i)**, écrit par l'adjudication elle-même : *« Maintien, amendement ou
  retrait de **R-23** relèvent d'un GO séparé et supposent l'ouverture du corps de F5, voie (i). »*
  **Le côté `R-23` n'a jamais été ouvert.**
- **DÉSAMBIGUÏSATION OPÉRATEUR, opposable** : dans « `[D5]` levé / W3 intact », **`W3` = le
  chaînon/front `LC-D-W3-GPY`** (GPY 1104.4317) — ni la classe de verdict `W3`, ni l'opérateur
  `W³`. Il y a **DEUX `D5`** (la consignation crochetée, `audit/` seul, 0 dans `kb/` ; le cinquième
  discriminant des séries `D1–D5`, **81** occurrences `kb/`) et **TROIS `W3`** (classe de verdict
  31 · chaînon `LC-D-W3-GPY` 103 · opérateur `W³` 334 en `kb/` + 45 en `audit/`).
  **Les crochets sont le seul désambiguïsateur de `D5`, et ils n'existent que dans `audit/`.
  VÉRIFIE TOUJOURS LA FORME NON CROCHETÉE avant de conclure à une absence.**
- **Le corps de F5 n'a JAMAIS été lu en substance** — seulement compté (`R-23` 9 occurrences,
  `W³` 31). Aucune gate tirée, aucun verdict touché.

## §4. Ce que cette pièce ne fait pas

Elle ne contient **aucun résultat, aucun verdict, aucune mesure** — seulement ce qui **anticipe**.
Elle ne scelle, ne réduit, ne compte, ne démontre rien. Elle ne répare pas la contamination du
pilote S19, déjà acquise : le cadrage de la session S20 devra **lister les cinq points en tête**
comme non créditables si son pilote les a déjà lus. β `T-b`, non résolu, seul facteur d'`O₂`
ouvert. **CCC n'est ni démontrée ni réfutée.**
