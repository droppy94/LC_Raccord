---
id: GEL-V1BIS-D5-AMENDEMENT-2
amende: GEL-V1BIS-D5 (bd0b40c8…), complète GEL-V1BIS-D5-AMENDEMENT-1
session: S11
date: 2026-07-24
type: "amendement — FICHIER SÉPARÉ DATÉ. Pièce amendée byte-intacte. Ne scelle rien (§6.4)."
---

# Amendement 2 — la règle de remplacement de l'amendement 1 SOUS-BORNE

## A. Le défaut, nommé

L'amendement 1 remplaçait la borne « marge gauche » par un **isolement
vertical** (écart > 1,6 × hauteur de ligne médiane). Appliquée, cette règle a
rendu un bloc de bandes 244,4 → 252,6 dont la lecture montre qu'il **commence
au milieu d'une expression** : l'équation (10) s'affiche sur DEUX lignes, et la
règle a coupé la première.

Cause : dans une équation affichée portant des indices et exposants empilés,
l'interligne entre deux lignes de l'affichage (24,9 pt mesurés) EXCÈDE le seuil
calibré sur l'interligne du corps de texte (15,94 pt). Le seuil était calibré
sur la mauvaise population.

C'est la TROISIÈME occurrence, dans ce seul volet, de la même leçon S10 : un
critère de bornage non confronté au cas d'espèce ne borne rien. Elle s'impute au
pilote. Elle est nommée ici parce qu'un élargissement de coupe décidé APRÈS
avoir vu un contenu est un risque de fit, et qu'un risque de fit se nomme.

## B. Critère de remplacement — GÉNÉRAL, non ajusté au cas

Un bloc d'affichage est borné **par la prose qui l'encadre**, la prose étant
identifiée par une propriété typographique indépendante du contenu :

> Une bande est de la PROSE JUSTIFIÉE si son bord droit atteint la marge de
> justification de la colonne (x1 ≥ 560 pt sur cette mise en page) **et**
> qu'elle ne contient pas d'étiquette d'équation.
>
> Le bloc d'affichage portant l'étiquette (n) est l'ensemble des bandes
> strictement comprises entre la plus proche prose justifiée en amont et la
> bande portant l'étiquette, celle-ci incluse.

Ce critère ne mentionne ni l'équation (10), ni sa hauteur, ni son nombre de
lignes. Il vaut pour tout bloc d'affichage de cette mise en page.

## C. Vérification d'implémentation, produite AVANT usage (§5.4 du gel)

Localisation d'ancres, sans lecture : les étiquettes d'équation de la colonne
droite de la page 4 sont (10) à 247,2 — (11) à 298,5 — (12) à 431,1 — (13) à
622,1. **Aucune étiquette entre la prose amont et (10)**, donc la bande
intermédiaire n'est la queue d'aucune autre équation.

Bandes de prose justifiée de la colonne, hors bandes à étiquette : 206,1 et
(en aval) 298,5 est une bande à étiquette, donc écartée.

Bloc retenu pour (10) : bandes 219,5 → 252,6, coupe y = 214 → 262 pt.
Borne amont = prose justifiée à 206,1 (x1 = 562,1), EXCLUE.
La règle énoncée est celle appliquée.

## D. Portée

Aucune case ajoutée à l'espace-verdict, aucun discriminant modifié, plafond et
périmètre inchangés. L'amendement ne porte que sur la manière de découper une
pièce déjà au périmètre depuis le gel.

---

*§6.4 — corriger une règle de bornage ne scelle, ne compte, ne démontre rien.*
