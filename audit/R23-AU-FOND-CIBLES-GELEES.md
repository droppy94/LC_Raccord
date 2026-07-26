---
id: R23-AU-FOND-CIBLES-GELEES
titre: "Cadrage GELÉ NEUF sur R-23 AU FOND, déposé AVANT toute lecture du corps de F5 et AVANT ouverture de l'enveloppe d'anticipations. Remplace F5-VOIE-I-CIBLES-GELEES (S18), défectueuse par prémisse fausse, qui reste SCELLÉE et byte-intacte."
codename: LC-RACCORD
type: "cibles gelées. Un cadrage ne tranche rien, n'ouvre aucune gate, ne réduit aucun compte (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
go: "Opérateur, S20 : GO sur ITEM 1 — R-23 AU FOND, voie (i)."
enveloppe: "audit/F5-ANTICIPATIONS-RESERVE.md — sha256 3200e69b24fc9edf1f552e2bb1c03f2797962b63c1eb898f63dbc9946ef19e75 — NON OUVERTE à la date de ce dépôt."
---

# R-23 AU FOND — cibles gelées avant lecture

## §0. DÉCLARATION DE CONTAMINATION — à lire en premier

**Le pilote S20 n'est PAS aveugle**, et il l'est moins que ne le prévoyait le correctif nº3.

`ENVELOPPE-ANTICIPATIONS-INSTRUCTION` §3 impose de lister en tête les **cinq points** acquis par
la voie prescrite, comme **issues déjà connues et donc NON CRÉDITABLES** :

1. `F5` = sélection d'état / CFT de raccordement, **levier sur `D1`** ;
2. les **quatre obstructions** `O₁ / O₂ / O₃ / OB` s'effondrent sur **une racine, `O₂`** ;
3. `A_T ~ 1/C_T ~ 1/N` **forcé**, deux routes indépendantes en contenu non en exposant,
   **coefficient O(1) libre** ;
4. la **voie (i)** = extraction `R-23`, **déclarée FAITE en v0.3** : Table III de `2409.10595`
   classée L1 **`inconfrontable`** ;
5. **`R-23` déclarée SOLDÉE**, verrou `W³` **purement interne**.

**DÉFAUT NEUF DU CORRECTIF Nº3, mesuré cette séance, et il est mien.** Les cinq points sont sortis
de la lecture obligatoire vers l'enveloppe — **et sont restés, verbatim, au §0 de
`audit/F5-VOIE-I-CIBLES-GELEES.md`**, pièce non hachée dans aucun attendu, librement lisible, et
que le §7 du prompt d'ouverture **désigne nommément** au pilote. J'ai ouvert cette pièce pour
savoir ce qui y était défectueux, et j'ai **ré-importé les cinq points par une porte que le
correctif nº3 n'a pas fermée**. La contamination n'est donc pas seulement héritée de S19 : elle a
été **re-consommée en S20**, par un chemin que le dispositif laissait ouvert.

**Précédent proposé** : *déplacer un contenu contaminant ne le retire pas du dépôt ; tant qu'une
pièce lisible en porte une copie, l'enveloppe ne scelle rien.* Une enveloppe n'est opposable que
si **toutes** les copies du contenu sont derrière elle.

**Conséquence portée, non dissimulée** : l'anti-fit de cette ouverture est **dégradé**. Toute
issue coïncidant avec l'un des cinq points se rend en **CONFIRMATION D'ANTICIPATION**, jamais en
découverte — *une anticipation confirmée ne lève aucune incertitude sur la physique ; son prix est
sa date.*

## §1. Ce que le pilote NE SAIT PAS au moment du gel

- **Le corps de `kb/LC-D-F5-ETAT-RACCORD.md` n'a pas été ouvert.** 30 423 o, non lus.
- Le pilote **ne sait pas** si le mot `soldée` est **dérivé** dans ce corps ou **enregistré**
  depuis un autre chaînon.
- Le pilote **ne sait pas** de quelle NATURE est l'`inconfrontable` de la Table III — c'est
  précisément l'objet du présent cadrage, et **le savoir d'avance serait le fit**.
- Le pilote **n'a pas ouvert l'enveloppe** `F5-ANTICIPATIONS-RESERVE.md`. Il en a mesuré le sha256
  sans qu'aucune ligne de son contenu n'entre dans son contexte, et cite ce sha au front-matter.

## §2. POURQUOI UN CADRAGE NEUF — le défaut de celui de S18, décomposé

`F5-VOIE-I-CIBLES-GELEES` (S18) porte trois cibles. **Deux d'entre elles — `G-i-1` et `G-i-3` —
sont ancrées sur `[D5]`**, dont il est établi en S18 qu'il a **0 occurrence dans `kb/`** et qu'il
était **LEVÉ dès S11** sous verdict `W3` — PAS DE RÉFÉRENT. Une cible dont l'objet n'a pas de
référent ne peut recevoir aucune des issues qu'elle pré-déclare. La troisième, `G-i-2`, survit mais
est prise dans la **collision de nomenclature à trois `W3`** mesurée en S18.

**Le défaut est donc de PRÉMISSE, pas de rédaction** : il ne se répare pas en réécrivant les
issues. D'où un cadrage neuf, et non un amendement. La pièce S18 **reste SCELLÉE, byte-intacte, et
ne sert pas de cadrage** — elle reste opposable comme trace de l'écart.

## §3. LA CIBLE, ÉNONCÉE SANS PRÉSUPPOSER SON ISSUE

`R-23` est **déclarée soldée** au motif que la borne appariée en forme sur `W³` **existe**
(Table III de `2409.10595`) mais est **`inconfrontable`** faute de valeur programme (`OB`) —
d'où : verrou `W³` **purement interne**.

**`R-23` AU FOND ne rejoue pas l'extraction.** Elle pose la seule question que le mot `soldée`
laisse ouverte : **ce soldement est-il ÉTABLI, ou seulement DÉCLARÉ ?**

## §4. CIBLES — trois, gelées, issues pré-déclarées

**`C-1` — De quel TYPE est la classification `inconfrontable` ?**
- (a) **CONTINGENTE** — inconfrontable *faute de* valeur programme, donc **levable** si une valeur
  apparaît ⟹ `R-23` est une **dette dormante**, pas un solde ;
- (b) **STRUCTURELLE** — les deux objets ne sont pas comparables **en nature** (observable,
  normalisation ou forme distinctes), et le corps l'établit ⟹ `R-23` soldée au fond ;
- (c) **NON DÉTERMINABLE** en l'état des pièces déposées.

**`C-2` — Le `soldée` est-il DÉRIVÉ par F5, ou ENREGISTRÉ depuis F2 ?**
- (a) **dérivé** dans le corps de F5, avec son argument écrit ;
- (b) **enregistré** — F5 consigne un résultat venu de F2, alors que **F2 renvoie en avant à F5**
  (`renvoi-avant F5, R-23`) ⟹ **circularité de renvoi**, et `R-23` n'aurait été instruite au fond
  par aucune des deux pièces ;
- (c) ni l'un ni l'autre identifiable.

**`C-3` — LEVIER FALSIFIABLE : que faudrait-il, NOMMÉMENT, pour rendre `W³` confrontable ?**
- (a) le corps **nomme** la valeur programme manquante et ce qui la bloque ;
- (b) le corps **établit** qu'aucune valeur programme n'est possible sous le périmètre gelé ;
- (c) le corps **ne nomme rien de tel** ⟹ la clause de dissolution de `R-23` est **sans levier
  écrit**.

## §5. CRITÈRE DE VERDICT, écrit AVANT

- **`C-1` = (a) ⟹ `R-23` N'EST PAS SOLDÉE AU FOND.** Elle est **suspendue à `OB`**, et le mot
  `soldée` doit être remplacé par `suspendue à OB` partout où il est cité. C'est une
  **DÉLIMITATION**, jamais une réduction de compte.
- **`C-1` = (b) ⟹ `R-23` est soldée au fond**, et le verrou `W³` est **définitivement** interne —
  résultat, et non reste-à-faire.
- **`C-2` = (b) ⟹ circularité de renvoi `F2 ↔ F5` ÉTABLIE.** Ni l'une ni l'autre ne porte la
  dérivation. C'est un **fait de dossier**, opposable, et le seul mouvement que l'ouverture
  produirait alors.
- **`C-3` = (c) ⟹ la voie (i) AU FOND ne produit AUCUN mouvement scientifique** — **issue
  complète, et non un échec.**
- **Toute issue coïncidant avec l'un des cinq points du §0 se rend en CONFIRMATION
  D'ANTICIPATION.** Une confirmation n'est pas un acquis.

## §6. GARDES — opposables au pilote qui exécutera

- **Ordre `R-54`** : lire le corps d'abord, chercher ensuite. Aucune identité, aucun verdict obtenu
  par recherche puis soumis à confirmation dans le corps.
- **CLASSER PUIS CONFRONTER**, jamais l'inverse.
- **Aucun sceau neuf** n'est armé. **Aucune pièce `kb/` n'est modifiée**, aucun gel rejoué.
- **BORNER LES MOTIFS.** Un `grep` non borné sur `kb/` a produit la contamination de S18 ; il a
  coûté ~15 000 tokens en S20 sur `02_programme.md` (front-matter kilométrique). **Écart pilote
  S20 nº2, déclaré ici.**
- Ouvrir la voie (i) au fond **ne ferme pas `D1`**, **ne construit pas `O₂`**, **ne fixe pas `N`**,
  **ne touche pas** `{ A4 ; A2★ ; N }`, et **ne dit rien de β `T-b`**.
- **L'enveloppe ne s'ouvre qu'APRÈS le dépôt de la présente pièce**, son sha est **re-mesuré et
  confronté** à celui du front-matter, puis chaque point est classé.

## §7. Ce que ce cadrage ne fait pas

Geler des cibles ne scelle, ne réduit, ne compte, ne démontre rien. **Le corps de F5 n'est pas
ouvert par la présente pièce** — elle est déposée **pour** que l'ouverture soit datable et
non-fittable, et pour que l'ordre soit **vérifiable dans l'historique git** plutôt que confié à la
discipline interne du pilote (précédent S19 nº1).

`{ A4 ; A2★ ; N }` INCHANGÉ · `D1` non clos, `D1c` intacte · Silo R clos à 12/12 · nœud (i)
INDÉTERMINÉ · β `T-b`, NON RÉSOLU, seul facteur d'`O₂` ouvert · **CCC non démontrée NI réfutée.**
