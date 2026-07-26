---
id: GARDES-VACUITE-INSTRUCTION
titre: "Tout instrument de garde déclare N MORDANTES ET M VACANTES. Un M absent est un écart. Arbitrage opérateur S19, correctif nº5."
codename: LC-RACCORD
type: "instruction de conduite — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
---

# Mordancité et vacuité — les deux gardes, jamais une seule

## §0. Le fait mesuré en S19

| instrument | mordantes déclarées | audit de vacuité |
|---|---|---|
| `instruments/harnais_R9.py` | 6/6, rc=0 | **oui** |
| `instruments/harnais_R11.py` | 7/7, rc=0 | **oui — 0 mutation + 0 assert vacants** |
| `instruments/LC-WORK-GEN-PAQUET-v2_1.py` | 6/6, rc=0 | **oui** |
| `audit/LC-BETA-CONTROLE-DEPOT.py` | 8/8, rc=0 | **AUCUN** — 0 occurrence de « vacan » |

**Le mécanisme existe, il fonctionne, et il manque précisément à l'instrument qui en a le plus
besoin.** `LC-BETA-CONTROLE-DEPOT.py` est l'instrument de contrôle du dépôt : c'est **la forme
nominale de ce contrôle qui n'a pas détecté la contamination du paquet scellé en S15**
(`PKG_SHA_BETA_8` glissant de `dc276129` à `687ed70b` sans qu'aucune garde ne morde). Il déclare
8 gardes mordantes et **ne déclare aucune garde vacante**.

## §1. INSTRUCTION

> **Tout instrument de garde déclare, dans sa sortie et sous `--self-test`, deux nombres :
> `N mordantes` et `M vacantes`. Une sortie qui ne porte que `N` est un écart, et le pilote la
> rend comme tel au lieu de la compter comme un PASS.**

`N mordantes` : le nombre de gardes dont on a **prouvé** qu'elles échouent quand la propriété
qu'elles protègent est violée. Une garde qu'on n'a pas fait échouer n'est pas prouvée mordante.

`M vacantes` : le nombre de gardes qui **passent sans pouvoir échouer** — sur l'ensemble vide,
sur un porteur absent, ou parce qu'elles matchent la règle au lieu de l'incident. **`M = 0` est
un résultat qui se déclare ; `M` absent est un silence qui se compte comme un écart.**

## §2. Les trois formes de vacuité, toutes rencontrées au dépôt

1. **VACUITÉ STRUCTURELLE.** Un `assert` qu'aucun porteur mutable ne traverse est un **faux
   PASS même s'il est vrai**. Mesuré en S9 : **quatre faux PASS** sur un lot qui se présentait à
   38/38. C'est ce que `harnais_R11.py` audite explicitement, et pourquoi il déclare ses
   vacantes.
2. **VACUITÉ D'ENSEMBLE VIDE.** Un contrôle qui passe sur l'ensemble vide est un faux PASS — et
   sa réciproque l'est aussi. **Il faut les deux gardes** (précédent S15 nº6).
3. **VACUITÉ NOMINALE.** Le contrôle **trouve le mot, pas le fait** : il matche la règle au lieu
   de l'incident (précédent S16 nº11). C'est la forme qui a laissé passer la contamination de
   S15, et c'est aussi la forme du piège de nomenclature de S18 — *les crochets de `[D5]` sont
   son seul désambiguïsateur, et un contrôle nominal sur `D5` en rend 81 qui ne sont pas lui.*

## §3. Dette ouverte, nommée et NON exécutée ici

`audit/LC-BETA-CONTROLE-DEPOT.py` doit être amendé pour déclarer son `M`. **Ce n'est pas fait par
la présente pièce** : modifier un instrument est un geste distinct, qui exige son propre GO et
son auto-test mordant reconstruit — *un instrument mandaté se construit à la LETTRE du mandat et
se prouve par un auto-test mordant* (précédent S13). La dette est **OUVERTE**, portée à la note
de reprise, et échoit **à la prochaine gate qui emploie cet instrument** — conformément à P-9 :
*le dépôt d'un instrument n'atteste que son existence ; sa valeur se mesure à la prochaine gate.*

Second instrument à créer, également non écrit ici, également sur GO séparé :
`instruments/concordance_mount.py`, qui hache le sas contre le clone et déclare
`identiques / divergents / exclusifs`. Motif : **la divergence mesurée en S19 sur
`R10-REDEMONSTRATION.md` et `redemo_R10_nonlin.py` — deux surfaces, deux versions byte-différentes
du même nom — qu'aucun instrument existant ne pouvait voir.** Il devra, lui aussi, déclarer son
`M`.

## §4. Ce que cette instruction ne fait pas

Elle ne modifie aucun instrument, ne rejoue aucun sceau, ne retire aucune garde. Elle ne scelle,
ne réduit, ne compte, ne démontre rien. β `T-b`, non résolu, seul facteur d'`O₂` ouvert.
**CCC n'est ni démontrée ni réfutée.**
