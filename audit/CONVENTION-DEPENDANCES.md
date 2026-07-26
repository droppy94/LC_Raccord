---
id: LC-CONVENTION-DEPENDANCES
titre: "Déclaration des dépendances — l'amont se déclare, l'aval se calcule"
codename: LC-RACCORD
type: "convention de conduite — HORS base scellée, OPÉRATIONNELLE. Elle ne scelle rien, ne compte rien, ne démontre rien."
version: 1.0
langue: fr
date: 2026-07-26
session: S21
arbitrages_operateur: "clé = `id:` (et non nom de fichier) · amont seul, aval calculé · partition front-matter / registre selon éditabilité"
---

# Déclaration des dépendances

## §1. LA RÈGLE, en une phrase

> **Une pièce déclare ce dont elle dépend. Elle ne déclare jamais ce qui dépend
> d'elle.**

L'aval n'est pas écrit : il s'obtient en inversant le graphe des déclarations
amont. Motif : si `A` déclarait alimenter `B` et que `B` ne déclarait pas dépendre
de `A`, rien ne dirait laquelle des deux a raison. **Un lien, une déclaration, un
seul endroit où se tromper.**

## §2. LE CHAMP

```yaml
depend_de: [LC-D-D1-STABILITE, LC-BORD-EON-06-WEYL-VERDICT]
```

- Les valeurs sont des **`id:`**, jamais des noms de fichiers. Un `id:` survit au
  renommage ; c'est ce qui a été arbitré, et c'est le prix payé : un renvoi ne se
  résout qu'après lecture des en-têtes du corpus. L'instrument construit cet index
  en une passe.
- Liste vide autorisée et **signifiante** : `depend_de: []` dit « mesuré, aucune
  dépendance », ce qui n'est pas la même chose qu'un champ absent.
- Champ absent = **non encore annoté**. L'instrument les distingue.

### Le cas des pièces de couverture

Un index, un manifeste, un inventaire dépendent du corpus **par construction** :
les énumérer produirait 270 arêtes et noierait toute propagation utile.

```yaml
depend_de: [CORPUS]
```

`CORPUS` est un marqueur réservé, non un `id:`. L'instrument le reconnaît, le
sort du graphe de propagation, et le traite à part.

## §3. CE QUI COMPTE COMME DÉPENDANCE

Le test est opérationnel, et il est unique :

> **`A` dépend de `B` si une modification de `B` peut rendre `A` faux, périmé,
> ou à reprendre.**

Ce n'est **pas** « `A` mentionne `B` ». Une note qui cite une pièce en passant
n'en dépend pas ; une note dont un chiffre vient de cette pièce en dépend.
Le critère est la **conséquence**, pas la présence du nom.

**Pas de typage des arêtes.** Une seule sorte de lien, tant qu'aucune mesure ne
montre que les fermetures aval sont trop larges pour être exploitables. Le typage
s'ajoutera contre un défaut mesuré, jamais par anticipation.

## §4. OÙ LA DÉCLARATION VIT — partition mécanique

Mesuré au 2026-07-26 : **306 pièces `.md`, dont 271 portent un front-matter et
35 n'en portent aucun.** Ces 35 sont des gels, verdicts et cibles gelées :
**scellés, byte-intacts, inéditables**. On ne peut pas leur ajouter un champ sans
rompre ce qui fait leur valeur.

| population | où la déclaration vit |
|---|---|
| pièce **éditable** (front-matter présent) | champ `depend_de:` de son front-matter |
| pièce **scellée** (front-matter absent) | `audit/REGISTRE-DEPENDANCES-SCELLEES.md` |

La partition est mécanique, pas discrétionnaire : elle se déduit de l'éditabilité.
**Aucun lien n'est déclaré aux deux endroits.** Le registre porte les mêmes
`depend_de:`, indexés par chemin de fichier puisque ces pièces n'ont pas d'`id:`.

## §5. ABSORPTION DE `parent:`

Deux pièces portent déjà un champ `parent:` en texte libre :

```
kb/NOTE-BORD-EON-06… : parent: NOTE-BORD-EON-05 (§6, §10-V1.d.i.α.1)
kb/NOTE-BORD-EON-07… : parent: NOTE-BORD-EON-06 (§6, §8-V1.d.i.α.1.b)
```

C'est une convention de dépendance amont, antérieure et informelle. Elle est
**absorbée, pas doublée** : `parent:` disparaît au profit de `depend_de:`, et la
coordonnée de section qu'il portait passe au champ `coordonnee:`.

Laisser coexister les deux produirait deux déclarations du même lien — la
désynchronisation que cette convention existe pour empêcher.

## §6. CE QUE L'INSTRUMENT DOIT RENDRE

1. **Cycles.** `A → B → … → A`. C'est la référence circulaire du point 2 du
   cahier des charges, mécanisée.
2. **Fermeture aval** d'une pièce donnée : tout ce qui peut hériter d'une mise à
   jour si on la touche. C'est l'usage quotidien.
3. **Arêtes pendantes** — un `depend_de:` dont l'`id:` ne résout pas.
   *C'est probablement le premier gisement.* Sur deux références vérifiées le
   2026-07-26, deux pointaient vers des pièces réelles **jamais déposées** :
   `NOTE-BORD-EON-01…05` et `LC-WORK-REPRISE-POST-G3T-4`. Une arête pendante ne
   dit pas « erreur » : elle dit **dette de fourniture**, et les deux se
   distinguent en regardant si la pièce existe hors dépôt.
4. **Propagation impossible.** Si l'aval d'une pièce modifiée contient une pièce
   **scellée**, la mise à jour ne peut pas être héritée : un scellé ne se corrige
   pas en place. L'instrument le signale comme tel — il faut un **amendement
   daté**, pas une propagation. C'est un signal, pas une erreur.
5. **Couverture** : combien de pièces annotées, combien avec `depend_de: []`,
   combien sans champ.

## §7. DÉPLOIEMENT — pas de passe unique

Annoter 306 pièces d'un coup serait long, fait sans contexte sur des fichiers que
personne ne rouvrira, et à moitié faux. Deux mouvements :

1. **La branche active d'abord**, annotée avec le contexte sous les yeux.
2. **Puis à la touche** : le champ devient **obligatoire à toute modification**
   d'une pièce. On paie l'annotation le jour où on a déjà le fichier ouvert.

La couverture progresse donc avec le travail réel, et l'instrument mesure où elle
en est plutôt que de prétendre qu'elle est complète.

## §8. RÈGLE DE VERSION, applicable ici et ailleurs

> **Un recalage qui ne touche pas le corps ne fait pas avancer `version:`.**
> Il se consigne au champ `recalages:`, daté et motivé.

Ajouter `depend_de:` à une pièce est un recalage de métadonnée. Sans cette règle,
le déploiement du §7 ferait avancer 306 numéros de version sans qu'une ligne de
substance ait bougé. Arbitrée par l'opérateur le 2026-07-26.

## §9. CE QUE CETTE CONVENTION NE FAIT PAS

Elle ne retire aucune pièce, ne modifie aucun attendu, ne touche aucun scellé,
n'annote rien par elle-même. Un graphe de dépendances ne scelle, ne réduit, ne
compte, ne démontre rien : il dit ce qui devra être relu, pas ce qui est vrai.
`W³` reste sans valeur, `O₂` n'est pas construite, β `T-b` demeure son seul
facteur ouvert. **CCC n'est ni démontrée ni réfutée.**
