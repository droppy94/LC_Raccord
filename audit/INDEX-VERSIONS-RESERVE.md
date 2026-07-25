---
id: INDEX-VERSIONS-RESERVE
titre: "Réserve écrite sur le dépôt de LC-00-INDEX — la pièce est déposée byte-intacte en audit/, l'écart de version qu'elle porte NE se referme PAS. 68 pièces kb/ la référencent, 3 nomment une version, max v1.64 ; la pièce déposée est v1.78."
codename: LC-RACCORD
type: "réserve écrite. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
session: S18
arbitrage: "Opérateur, S18 : (b) dépôt en audit/ — hors ensemble scellé, §0-lite recalé, manifeste v2.124 INTACT."
---

# Réserve — dépôt de `LC-00-INDEX`, et ce que ce dépôt NE fait pas

## 1. Ce qui est déposé, mesuré

`audit/00_index.md` — **byte-intact**, `cmp` identique à la pièce fournie par l'opérateur.

    id        : LC-00-INDEX
    version   : 1.78          maj 2026-06-25
    octets    : 236 461
    sha256    : 479df5067a62550b... (complet à l'annonce R-55)
    lignes    : 249

Identité **lue dans les octets** (`id:` du front-matter), **jamais déduite du nom du fichier**
— précédent S17 : *le nom d'un contenant ne décrit pas son contenu.*

## 2. L'état ANTÉRIEUR, mesuré avant dépôt

- `LC-00-INDEX` **absent** de `kb/`, absent de tout le dépôt (`find` : 0 occurrence).
- **68 pièces `kb/` sur 215 (32 %) le référencent** — renvoi pendant depuis la constitution
  de la base.
- `kb/` porte **exactement 215 `.md`**, et le **manifeste v2.124** déclare son §0 à
  « 228 = 215 .md + 13 .py ». **L'index n'a donc JAMAIS fait partie de l'ensemble scellé.**
  Son absence de `kb/` est une **exclusion de construction**, pas une perte.

## 3. LA RÉSERVE — ce que le dépôt ne referme pas

**Sur les 68 pièces qui citent l'index, 3 seulement nomment une version.** La plus récente
nommée est **v1.64**. La pièce déposée est **v1.78** : **quatorze versions d'écart**. Les
**65 autres** citent l'index **sans version**.

> **On ne sait pas quelle version chacune des 68 pièces a lue.**
> Déposer v1.78 rend le renvoi **résoluble**, il ne le rend **pas traçable**.

**C'est exactement la classe de défaut du registre de corpus §3** — un identifiant sans
version, et une mesure tardive qui produit une première mesure, jamais une confrontation.
Deux endroits, un seul défaut, et il se paiera au même endroit : à la première bascule
qui exigera de savoir *ce qui a été lu*.

## 4. Emplacement — pourquoi `audit/` et pas `kb/`

Déposer en `kb/` aurait fait **216 `.md`** ⟹ recalage du §0-lite **et** rupture du gel du
paquet v2.124. La racine est plafonnée à 4 fichiers par règle écrite. `audit/` est le seul
emplacement qui **ne touche ni l'ensemble scellé ni le manifeste**.
Recalage induit, et lui seul : **`audit/` 55 → 62** (7 pièces S18).

## 5. Non-conformité de nommage — DÉCLARÉE, non corrigée

`00_index.md` **ne satisfait pas** la grammaire `<SUJET>-<TYPE>` de `LC-NORME-NOMMAGE` §1.
**La pièce n'est PAS renommée**, pour deux raisons qui tiennent chacune seule :

1. la norme est **prospective** et ne renomme aucune pièce existante ;
2. renommer casserait les 68 renvois — et le pare-feu écrit interdit, en dur, de
   **renommer une pièce pour passer sous un contrôle nominal**.

## 6. Ce que cette pièce ne fait pas

Déposer un index ne scelle, ne réduit, ne compte, ne démontre rien. Aucune pièce `kb/` n'est
touchée ; `kb/` reste à 215 `.md` ; le manifeste v2.124 reste intact ; aucun sceau n'est
rejoué du fait de ce dépôt. `{ A4 ; A2★ ; N }` INCHANGÉ · CCC non démontrée NI réfutée.
