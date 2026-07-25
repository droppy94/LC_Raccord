---
id: LC-WORK-REGISTRE-CORPUS-AMENDEMENT-2
titre: "Amendement 2 au registre de corpus — la STRUCTURE du §3 est amendée : DEUX colonnes de version, non une. La colonne « version consommée par l'assaut » porte NON DÉTERMINABLE sur les cinq lignes. Le registre reste BYTE-INTACT."
codename: LC-RACCORD
type: "amendement daté. Il ne modifie pas le registre en place. Il n'atteste ni un titre, ni des auteurs, ni un DOI, ni un grade."
version: 1.0
langue: fr
date: 2026-07-25
session: S18
arbitrage: "Opérateur, S18 : « Il en faut deux, dont l'une portera NON DÉTERMINABLE sur les cinq lignes. »"
---

# Amendement 2 — structure du §3 du registre de corpus

## 1. Le défaut, mesuré

Le **§2** du registre porte une colonne `version consommée`, renseignée sur ses sept lignes.
Le **§3** porte `identifiant | assaut d'origine | sha256` — **aucune colonne de version**,
et il n'en a **jamais** porté. L'**amendement 1** a fourni, pour les cinq corps d'assaut, une
`version LIVRÉE` mesurée dans les octets en S17.

## 2. POURQUOI DEUX COLONNES ET NON UNE — c'est le cœur de l'amendement

Écrire **une** colonne « version » fusionnerait deux choses que rien ne permet d'identifier :

- la version **LIVRÉE en S17 et mesurée** — connue, hachée, confrontable ;
- la version **CONSOMMÉE par l'assaut** — inconnue, et **inconnaissable rétroactivement**.

Une colonne unique donnerait aux verdicts `S-G3T-*` une traçabilité **d'apparence**. C'est
précisément le surclassement que le registre existe pour empêcher.

## 3. STRUCTURE AMENDÉE DU §3

| identifiant | assaut d'origine | **version CONSOMMÉE par l'assaut** | **version LIVRÉE et mesurée (S17)** | sha256 de la version livrée |
|---|---|---|---|---|
| `arXiv:0808.2054` | `S-G3T-4b` (de Haro) | **NON DÉTERMINABLE** | v1 | `fcfebce6…b42d9` |
| `arXiv:2007.06800` | `S-G3T-2` (wedge, AdS/BCFT) | **NON DÉTERMINABLE** | v4 | `5be89da3…b1909` |
| `arXiv:2409.08709` | `S-G3T-4b` (ST) | **NON DÉTERMINABLE** | v4 | `d5e3a1de…4aa4f` |
| `arXiv:2412.00183` | `S-G3T-3b` | **NON DÉTERMINABLE** | v1 | `eb3ddc9c…c4e7a` |
| `arXiv:2606.09170` | `S-G3T-3b` | **NON DÉTERMINABLE** | v2 | `3d8580a5…1eecd` |

Les sha256 complets restent portés par l'**amendement 1** §1, non recopiés ici.

**`NON DÉTERMINABLE` n'est pas `NON MESURÉ`.** `NON MESURÉ` décrit un geste qui n'a pas été
fait et pourrait l'être. `NON DÉTERMINABLE` décrit une information qui **n'existe plus** :
les assauts ont été conduits avant tout registre, et rien dans leurs traces ne porte la
version lue. Aucune mesure future ne la produira.

## 4. Conséquence, inchangée et rappelée

Les verdicts `S-G3T-*` **ne deviennent pas traçables**. L'écart se paiera à la première
bascule de branche. Une re-mesure produit une **première mesure**, jamais une confrontation.

## 5. Défaut d'âge du registre — NOMMÉ, NON CORRIGÉ

Le titre du §3 lit toujours **« sha NON MESURÉS »**. C'est **faux** depuis l'amendement 1.
Le registre `audit/LC-WORK-REGISTRE-CORPUS.md` reste **byte-intact** : un défaut de portée se
nomme par fichier séparé daté, jamais en place — précédents S8/S9, appliqués trois fois depuis.

## 6. Ce que cet amendement ne fait pas

Amender une structure de table ne scelle, ne réduit, ne compte, ne démontre rien. Aucun sha
n'est ajouté, aucun verdict touché, aucune gate ouverte.
