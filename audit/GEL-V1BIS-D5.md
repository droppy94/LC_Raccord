---
id: GEL-V1BIS-D5
titre: "Gel de cadrage — volet 1-bis S11 : lever [D5] (« 900 ± 700 » et le sigma = O(500) du correctif R-23 sont-ils MÊME QUANTITÉ ?)"
codename: LC-RACCORD
session: S11
date: 2026-07-24
type: "pièce de cadrage — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
gabarit: LÉGER
statut: "FIGÉ AVANT TOUTE LECTURE. Byte-intact obligatoire jusqu'à clôture. Amendement par FICHIER SÉPARÉ DATÉ uniquement, jamais en place."
relation_gel_V1: "Le gel V1 (201bcfbb) et ses deux amendements sont CLOS. Ce gel ne les rouvre pas, ne les amende pas, ne s'y substitue pas. Il est neuf et autonome."
---

# GEL V1-bis — cadrage de [D5]

## §1. Question, telle que reçue

[D5] : « 900 ± 700 » — établi en S10 comme imprimé DEUX FOIS verbatim dans
`sources/2312_12498v2.pdf`, p. 1 (abstract) et p. 2 (introduction), avec son
exposant ttt — et le « sigma = O(500) » invoqué par le correctif R-23
désignent-ils **la même quantité** ?

« Même quantité » est décomposée en TROIS composantes **conjonctives**, fixées
ici et non renégociables :

- **T** — même TEMPLATE (même forme de bispectre / même modèle paramétré) ;
- **S** — même STATISTIQUE (même estimateur, même jeu de données, même
  combinaison T / T+E / T+E+B, même traitement marginalisé ou non) ;
- **N** — même NORMALISATION (même convention d'amplitude et même convention
  d'unité, préfixe multiplicatif inclus).

## §2. ASYMÉTRIE STRUCTURELLE DE LA COMPARAISON — déclarée au gel

Le côté R-23 de la comparaison **n'est pas ouvrable dans ce volet**. Le corps
de `LC-D-F5-ETAT-RACCORD` relève de la voie (i) et d'un GO distinct ; aucune
pièce KB n'est au périmètre. Le côté R-23 entre donc ici **uniquement tel que
le prompt S11 le rapporte** : une dispersion d'ordre 500, **sans template,
sans statistique et sans normalisation déclarés**.

Conséquence, actée maintenant et non après mesure : les discriminants ne
peuvent PAS confronter directement deux fiches. Ils opèrent **entièrement du
côté documentaire**, et la question devient opérationnellement :

> Dans les trois pièces au périmètre, le porteur de « 900 ± 700 » et un
> éventuel porteur d'une dispersion d'ordre 500 sont-ils un seul et même
> objet, ou deux objets distincts ?

Si deux objets distincts existent, [D5] se tranche NÉGATIVEMENT sans jamais
ouvrir F5. Si un seul existe, [D5] se tranche POSITIVEMENT sous réserve
explicite que le côté R-23 n'a pas été vérifié — cette réserve est
**inéliminable** et fait partie du plafond.

## §3. Plafond, annoncé AU GEL

**CONSTAT SUR PIÈCES LOCALES.**

Ce gel peut produire, au mieux, une **désignation documentaire** portant sur la
commensurabilité de deux quantités. Il ne peut PAS, et ne prétendra pas :

- trancher le FOND du correctif R-23 (maintien / amendement / retrait) — GO
  séparé, après ;
- ouvrir le corps ou le front-matter de `LC-D-F5-ETAT-RACCORD` ni de
  `LC-D-F2-TTT-PLANCK` ;
- statuer sur la valeur physique, la validité de l'analyse du papier, ou la
  correction d'un chiffre ;
- retirer une inconnue de `{ A4 ; A2★ ; N }`, ni toucher au Silo R (clos 12/12) ;
- produire un instrument, un sceau, un PASS ou une consignation de lot.

Atteindre ce plafond n'est pas le dépasser. Le dépasser est un échec.

## §4. PÉRIMÈTRE DE LECTURE — exhaustif, fermé

Trois pièces, toutes locales, aucune récupération externe :

- **(a)** l'ÉQUATION (10) de `sources/2312_12498v2.pdf` ;
- **(b)** le PANNEAU INFÉRIEUR de Table II de `sources/2312_12498v2.pdf`,
  avec sa LÉGENDE et ses EN-TÊTES de colonnes ;
- **(c)** la CONVENTION D'UNITÉ de cette même Table II.

**Comparateur autorisé, à ce seul titre** : Table III de
`sources/2409_10595v2.pdf`, sa légende et ses préfixes de ligne — nommée par le
prompt S11 comme point de comparaison de la convention d'unité. Autorisée pour
[D5-c] EXCLUSIVEMENT ; toute autre exploitation serait un débordement.

**Hors périmètre, nommément** : tout autre passage des deux PDF ; les corps et
front-matters de F2 et F5 ; toute pièce de `kb/` ; toute source externe.
`sources/2503_19957v1.pdf` est HORS PÉRIMÈTRE.

## §5. RÈGLE DE BORNAGE — et sa vérification

Leçon S10 opposable : **un bornage par numéro de ligne ou par fin de page ne
borne rien**. Le bornage retenu ici est **géométrique et matériel** :

1. **Toute lecture passe par un RECADRAGE du rendu raster de la page.** La
   coupe EST le bornage : ce qui est hors coupe ne parvient pas au lecteur.
   Aucune lecture par flux texte non borné n'est autorisée.
2. **Localisation des ancres sans lecture.** Les coordonnées de coupe sont
   dérivées d'une recherche mécanique de chaînes d'ancrage rendant
   **numéro de page + boîte englobante seulement**, jamais le texte alentour.
3. **Fin de LÉGENDE, pas fin de page ni de ligne n.** Le bloc de légende de
   Table II est défini par continuité verticale à partir de la ligne portant
   l'étiquette de table : une ligne appartient au bloc tant que son écart
   vertical à la précédente reste inférieur à 1,6 × la hauteur de ligne
   médiane du bloc. La coupe s'arrête au bas de la dernière ligne du bloc.
4. **VÉRIFICATION D'IMPLÉMENTATION OBLIGATOIRE.** Écrire la règle ne suffit
   pas : avant toute coupe, le code doit IMPRIMER les coordonnées retenues et
   le dernier élément inclus, et il doit être constaté que cet élément
   appartient bien au bloc visé. Écrire une correction et ne pas l'appliquer
   est un échec d'exécution distinct, et il s'impute pareillement.
5. **Bloc d'affichage de l'équation (10).** Coupe verticale bornée, de part et
   d'autre de l'étiquette « (10) », par la première ligne dont l'abscisse de
   départ coïncide avec la marge gauche du corps de texte. La clause
   définitionnelle suivante n'est incluse que si elle s'ouvre par « where », et
   s'arrête à la fin de cette clause. Vérification par impression, idem §5.4.
6. **DÉBORDEMENT.** Est en périmètre tout ce qui figure à l'intérieur d'une
   coupe conforme à la présente règle. Est un DÉBORDEMENT toute coupe plus
   large que la règle ne l'autorise, et toute lecture hors coupe. Un
   débordement se CONSIGNE nommément, avec ce qu'il a livré, et **ne s'emploie
   pas** — le nommer l'empêche de circuler en contrebande.

## §6. DISCRIMINANTS — pré-déclarés, avec pré-tri [D] / [C]

- **[D5-d]** *(discriminante, résolue EN PREMIER)* — EXISTENCE. Le panneau
  inférieur de Table II porte-t-il, pour le template de l'équation (10), une
  incertitude d'ordre 500 (après application de la convention d'unité de
  [D5-c]) ? Mesure : lecture des cellules du panneau inférieur.
- **[D5-a]** *(discriminante)* — TEMPLATE. L'étiquette portée par
  « 900 ± 700 » (ttt, établie en S10) et l'étiquette du template défini en (10),
  et celles des lignes de Table II, désignent-elles le même template ?
- **[D5-b]** *(discriminante)* — STATISTIQUE. Légende et en-têtes de colonnes de
  Table II : même estimateur, même jeu de données, même combinaison T/T+E/T+E+B
  pour les deux porteurs ?
- **[D5-c]** *(discriminante)* — NORMALISATION. Table II porte-t-elle une
  convention d'unité (préfixe multiplicatif) dans ses cellules, ses en-têtes ou
  sa légende ? Comparateur : Table III de 2409.10595v2.
- **[C-1]** *(consignation)* — toute information relevée dans une coupe conforme
  mais étrangère aux quatre discriminants.

## §7. ESPACE-VERDICT — exhaustif, disjoint, ordre de résolution figé

Cinq cases. **La case W4 est la case « aucune des deux lectures ne tient »**,
prévue AVANT toute mesure, conformément à la leçon S10.

- **W1 — MÊME QUANTITÉ.** Un seul et même porteur : T ∧ S ∧ N concordants, et la
  dispersion d'ordre 500 est celle-là même qui s'imprime « ± 700 » (écart
  absorbé par l'arrondi d'ordre de grandeur). Réserve inéliminable du §2.
- **W2 — QUANTITÉS DISTINCTES.** Il existe, pour le template de (10), un porteur
  de dispersion d'ordre 500 DIFFÉRENT du porteur de « 900 ± 700 », au moins un
  de T / S / N les séparant. [D5] tranché NÉGATIVEMENT.
- **W3 — PAS DE RÉFÉRENT.** Aucune dispersion d'ordre 500 n'existe dans les
  trois pièces. Le « sigma = O(500) » de R-23 n'a pas de correspondant local.
  [D5] tranché NÉGATIVEMENT, par absence.
- **W4 — AUCUNE DES DEUX LECTURES.** Les deux grandeurs ne sont pas
  commensurables parce qu'elles ne sont pas du même TYPE d'objet (p. ex. l'une
  contrainte marginalisée sur une amplitude, l'autre erreur sur un observable
  distinct), de sorte que ni « même quantité » ni « quantités distinctes du même
  genre » ne décrit correctement la situation. La question est mal posée des
  deux côtés.
- **W5 — INDÉCIDABLE DANS LE PÉRIMÈTRE** *(clause I-c, résiduelle)*. Au moins
  une des trois composantes T / S / N n'est pas déterminable à partir des trois
  pièces. **Consignation, PAS verdict.**

**Ordre de résolution, figé** : [D5-c] (convention d'unité, car elle conditionne
la lecture des nombres) → [D5-d] (existence) → [D5-a] (template) → [D5-b]
(statistique). Puis : si [D5-d] négatif ⟹ W3. Si [D5-d] positif et les deux
porteurs coïncident sur T ∧ S ∧ N ⟹ W1. Si [D5-d] positif et au moins un de
T / S / N sépare les porteurs ⟹ W2. Si les porteurs ne sont pas du même type
d'objet ⟹ W4. Si une composante reste indéterminable ⟹ W5.

**Anti-fit** : aucune case ne sera ajoutée après mesure. Si une issue non
prévue apparaissait, elle serait NOMMÉE comme défaut du présent gel et amendée
par fichier séparé daté, jamais en place, et le risque de fit serait consigné.

## §8. CLAUSE I-c — non-algébrisable déclarée d'avance

Si l'une des composantes T / S / N n'est pas déterminable par les trois pièces,
elle est déclarée NON MESURABLE DANS LE PÉRIMÈTRE et consignée comme telle
(W5). Elle ne sera PAS remplacée par une recopie de front-matter, ni par une
inférence de plausibilité, ni par un raisonnement sur ce que le papier « devrait »
faire. Un pré-tri [D] / [C] est arrêté ici : aucun échec de discriminante ne
sera reclassé en consignation après coup.

## §9. Antériorité

Le sha256 du présent fichier est relevé alors qu'aucune coupe, aucun texte
extrait, aucun log de localisation, aucun rendu raster n'existe — listing du
répertoire de travail à l'appui. L'antériorité se PROUVE par l'état du
répertoire, jamais par déclaration.

---

*§6.4 — cadrer, geler, localiser, recadrer, lire, adjuger : aucun de ces gestes
ne scelle, ne réduit, ne compte, ne démontre quoi que ce soit.*
