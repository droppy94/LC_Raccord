---
id: GEL-V1BIS-D5-AMENDEMENT-1
amende: GEL-V1BIS-D5 (sha256 bd0b40c8c7f72bee779296c535c369ce9bfb51431ddb785db0dd6490b2fe5560)
session: S11
date: 2026-07-24
type: "amendement — FICHIER SÉPARÉ DATÉ. La pièce amendée reste BYTE-INTACTE et re-vérifiable après coup. Ne scelle rien (§6.4)."
---

# Amendement 1 au gel V1-bis — deux défauts du cadrage, nommés

Le gel `GEL-V1BIS-D5` est vérifié byte-intact au moment d'écrire le présent
amendement (sha256 relevé identique au sha d'antériorité). Il n'est PAS modifié.

## A. Défaut du §5.5 — la borne « marge gauche du corps » ne borne pas ici

**Énoncé fautif.** Le §5.5 borne le bloc d'affichage de l'équation (10) « de
part et d'autre de l'étiquette, par la première ligne dont l'abscisse de départ
coïncide avec la marge gauche du corps de texte ».

**Mesure qui l'invalide.** Colonne de droite de la page 4 de
`2312_12498v2.pdf` : marge gauche du corps mesurée à **302,0 pt** ; la bande
principale du bloc d'affichage portant l'étiquette « (10) » commence elle-même
à **301,7 pt**. Le critère sélectionne donc l'équation comme sa propre borne
supérieure — il est **dégénéré** sur ce cas et ne sépare rien.

C'est la leçon S10 qui se répète sous une autre forme : un critère de bornage
qui n'a pas été confronté au cas d'espèce ne borne rien. Le défaut est du gel,
pas de la mesure, et il est imputable au pilote.

**Règle de remplacement, applicable au seul bloc d'affichage.** Le bloc est le
plus grand ensemble de bandes contenant l'étiquette dont les écarts verticaux
consécutifs restent inférieurs à 1,6 × la hauteur de ligne médiane de la
colonne ; il est borné, de part et d'autre, par le premier écart supérieur à ce
seuil. La vérification d'implémentation du §5.4 reste intégralement due.

**Application et vérification, produites AVANT usage** : h_med = 9,96 pt,
seuil = 15,94 pt ; bloc retenu = bandes 244,4 → 252,6 (bas 259,6) ; écart amont
24,9 pt, écart aval 18,2 pt, tous deux au-dessus du seuil. Condition « where »
du §5.5 évaluée : la bande suivante (top 270,8) s'ouvre par `bispectrum,` et non
par `where` — la clause définitionnelle n'est donc **PAS** incluse au périmètre.
La règle énoncée est celle appliquée.

## B. Défaut du §5.1 — le gel a figé le SUPPORT là où seul le BORNAGE importait

**Énoncé trop étroit.** Le §5.1 impose que « toute lecture passe par un
recadrage du rendu raster », au motif que « la coupe EST le bornage ».

**Ce qui manquait.** Le raisonnement du §5.1 porte sur la GÉOMÉTRIE, pas sur le
support. Une extraction de texte bornée à des coordonnées identiques réalise
exactement le même bornage, et évite qu'une adjudication documentaire ne repose
sur ma transcription d'une image.

**Complément.** Chaque coupe est lue par DEUX chemins d'implémentation aux
**coordonnées strictement identiques** : le recadrage raster déclaré au gel, et
une extraction de texte bornée à la même boîte. Le second est un CONTRÔLE DE
TRANSCRIPTION, non un élargissement : aucune coordonnée n'est modifiée. Le
signaler est nécessaire parce que c'est un écart à la lettre d'une pièce gelée.

## C. DÉBORDEMENT DE PÉRIMÈTRE — un, consigné, NON EMPLOYÉ

Le §4 borne la pièce (b) au **panneau inférieur** de Table II, à sa légende et à
ses **en-têtes de colonnes**. En cherchant les en-têtes, j'ai coupé la bande
y = 66 → 83 pt de la page 15 en la croyant l'en-tête, alors que la géométrie
montrait qu'elle se situe **sous** le filet d'en-tête (82,3) : c'est la première
ligne de données du **panneau supérieur**, hors périmètre. Les en-têtes réels
sont au-dessus du double filet (y ≈ 46 → 66).

Le débordement a livré la ligne fiduciaire T+E+B du panneau supérieur, avec ses
trois cellules. **Cette information est déclarée NON EMPLOYÉE.** Elle ne fonde
aucun discriminant, aucune case de l'espace-verdict, aucune conclusion de la
présente adjudication. Elle est nommée ici pour ne pas circuler en contrebande
dans une session ultérieure : si une session future en a besoin, elle la
mesurera elle-même, sous son propre gel.

Cause : bande présumée d'après un rang supposé au lieu d'être confrontée à la
position des filets déjà mesurés. C'est un échec d'exécution, distinct du défaut
d'énoncé du point A, et il s'impute pareillement.

## D. Ce que le présent amendement NE fait PAS

Il n'ajoute aucune case à l'espace-verdict du §7, ne modifie aucun discriminant
du §6, ne touche ni au plafond du §3 ni au périmètre du §4. Les cinq cases
W1–W5 restent celles pré-déclarées avant toute lecture.

---

*§6.4 — amender un gel ne scelle, ne réduit, ne compte, ne démontre rien.*
