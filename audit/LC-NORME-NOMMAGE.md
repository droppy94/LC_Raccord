---
id: LC-NORME-NOMMAGE
titre: "Norme de nommage des fichiers du dépôt LC-RACCORD — grammaire unique, vocabulaire de types fermé"
codename: LC-RACCORD
session: S11
date: 2026-07-24
version: 1.0
type: "pièce de gouvernance — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
statut: PROPOSITION — non arbitrée, non déposée à l'écriture de la présente version.
perimetre_liant: "audit/ , instruments/ , hors-KB/ , racine. kb/ EXCLU tant que G-4 n'est pas tranchée."
---

# Norme de nommage LC-RACCORD

## §0. Pourquoi

Les noms de fichiers ne sont choisis par personne : chaque session les invente.
Sans règle, la dérive est structurelle et non fautive — elle se répète à chaque
reprise. Le constat mesuré en S11 sur `audit/` (41 pièces) :

- le mot de TYPE change de position : `GEL-R11.md`, `GEL-V1-F2F5.md` le placent
  devant, `CSE-R4R5-GEL.md` derrière ;
- deux notes d'adjudication de même famille ont l'ordre INVERSE l'une de
  l'autre : `NOTE-ADJUDICATION-V1-F2F5.md` / `NOTE-V1BIS-D5-ADJUDICATION.md` ;
- `RAPPORT-R11.md` est sujet-dernier, ses onze voisines `R#-REDEMONSTRATION.md`
  sont sujet-premier ;
- un fichier sur 41 est en snake_case minuscule.

La famille majoritaire — 22 sur 41 — est **sujet d'abord, type ensuite**. C'est
la seule qui fasse qu'un `ls` regroupe les pièces d'un même sujet. La norme la
retient : elle NORMALISE L'USAGE DOMINANT, elle n'impose pas un goût.

## §1. Grammaire

    <SUJET>-<TYPE>[-AMENDEMENT-<n>].<ext>

- **SUJET** — un ou plusieurs segments identifiant CE DONT il s'agit
  (`R11`, `V1-F2F5`, `V1BIS-D5`, `CSE-R4R5`, `SCEAUX`). Vient TOUJOURS en tête.
- **TYPE** — un et un seul mot du vocabulaire fermé du §2. Vient TOUJOURS en
  queue, juste avant l'extension.
- **AMENDEMENT-\<n\>** — seul suffixe autorisé après le TYPE. `n` entier,
  strictement croissant, jamais réattribué, même après rétractation. Un
  amendement rétracté RESTE au dépôt et garde son numéro.
- **\<ext\>** — `.md` par défaut ; une autre extension seulement si le contenu
  n'est réellement pas du markdown.

## §2. Vocabulaire de TYPE — fermé

    GEL · CIBLES-GELEES · REDEMONSTRATION · ADJUDICATION · VERDICT
    RAPPORT · INSTRUCTION · RESERVE · INVENTAIRE · REJEU · NORME · SYNTHESE

Fermé signifie fermé : un type neuf s'ajoute **par amendement à la présente
norme**, jamais par le fait accompli d'un fichier qui l'emploie.

`NOTE` n'est PAS un type : c'est un mot vide qui ne distingue rien — toute
pièce du dépôt est une note. Les pièces qui le portent aujourd'hui relèvent en
réalité de `ADJUDICATION`, `RAPPORT` ou `REPRISE`.

## §3. Forme des caractères

- ASCII majuscules, chiffres, et le tiret `-` comme **seul** séparateur.
- Interdits : underscore, accent, espace, point (hors extension), minuscule —
  sauf lorsqu'une minuscule appartient à l'identifiant lui-même (`R4b`).
- Pas de date dans le nom : elle est en front-matter `date:`.
- **Pas de version dans le nom** : elle est en front-matter `version:`. La
  norme de nommage et la règle de versionnage sont deux règles distinctes et
  la seconde n'est pas modifiée ici.

## §4. Règle de cohérence, vérifiable

> Le nom de fichier, extension retirée, est **identique** au champ `id:` du
> front-matter.

C'est la seule règle mécaniquement contrôlable de la norme, et c'est elle qui
empêche la dérive de recommencer : un `id` et un nom qui divergent se voient.

## §5. Exceptions NOMMÉES — pièces de gouvernance de la racine

    PROMPT-OUVERTURE-S<n>.md
    NOTE-REPRISE-GIT-S<n>.md   (et son -AMENDEMENT-<n>)

Ces deux formes sont TYPE-PREMIER et dérogent au §1. Elles sont maintenues
telles quelles : elles sont citées littéralement par la règle d'unicité de la
reprise et par le piège R-36, et les renommer casserait des pièces opposables
pour un gain d'esthétique. L'exception est **nommée ici pour ne pas devenir un
précédent tacite** ; elle ne s'étend à aucune autre pièce.

## §6. Portée — ce que la norme NE fait PAS

1. **Elle ne renomme rien.** Elle lie les pièces NOUVELLES. L'existant est
   acquis ; toute migration est un geste distinct, arbitré séparément.
2. **Elle ne touche pas `kb/`.** La KB scellée est sous R-54 : le mount est
   autoritaire, le git est miroir. Renommer côté miroir romperait la relation
   de miroir sans que rien ne l'autorise. Une migration de `kb/` est **bloquée
   sur G-4** et relève du volet 3.
3. **Elle ne crée aucun instrument.** Le contrôle du §4 est mécanisable ; écrire
   le vérificateur exigerait un arbitrage, il n'est pas écrit.

## §7. Ce que la norme donnerait, appliquée à `audit/` (ILLUSTRATION, non exécutée)

    GEL-V1-F2F5.md                 -> V1-F2F5-GEL.md
    NOTE-ADJUDICATION-V1-F2F5.md   -> V1-F2F5-ADJUDICATION.md
    GEL-V1BIS-D5.md                -> V1BIS-D5-GEL.md
    NOTE-V1BIS-D5-ADJUDICATION.md  -> V1BIS-D5-ADJUDICATION.md
    GEL-R11.md                     -> R11-GEL.md
    RAPPORT-R11.md                 -> R11-RAPPORT.md
    rejeu_sceaux_resultats.json    -> SCEAUX-REJEU-RESULTATS.json
    CSE-R4R5-GEL.md                -> inchangé (déjà conforme)
    R#-REDEMONSTRATION.md          -> inchangés (déjà conformes, 22 pièces)

Vingt-deux pièces sur 41 sont déjà conformes. La migration porterait sur sept.

---

*§6.4 — normer, proposer, illustrer : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit.*
