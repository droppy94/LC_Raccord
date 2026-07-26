---
id: ENVELOPPE-ANTICIPATIONS-INSTRUCTION
titre: "Les anticipations et contaminations connues sortent de la pièce à lecture obligatoire et vont en ENVELOPPE SÉPARÉE, dont seul le sha256 est cité. Le pilote dépose son cadrage gelé AVANT de l'ouvrir. Arbitrage opérateur S19, correctif nº3. Portée PROSPECTIVE."
codename: LC-RACCORD
type: "instruction de conduite — HORS base scellée. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S19
---

# Enveloppe scellée des anticipations

## §0. Le fait mesuré, et c'est une régression

En S18, un `grep -rn` non borné du pilote a importé le front-matter de
`kb/LC-D-F5-ETAT-RACCORD.md` et des blocs `[TRAITÉ]` de la branche. La contamination a été
**déclarée**, comme la discipline anti-fit l'exige, et cette déclaration a été **écrite dans la
note de reprise, au §5ter.6**.

Or le §2 du prompt d'ouverture **ordonne la lecture intégrale de la note**. Mesure S19 : le
pilote S19, en exécutant la consigne, a acquis les cinq points par la **voie prescrite** —
F5 = sélection d'état / CFT de raccordement · les quatre obstructions s'effondrent sur `O₂` ·
`A_T ~ 1/C_T ~ 1/N` forcé, coefficient O(1) libre · voie (i) déclarée FAITE en v0.3, Table III
`inconfrontable` · **R-23 déclarée SOLDÉE**.

**Le dispositif anti-fit a été converti en vecteur de contamination.** La contamination n'est
plus un accident de `grep` : elle est **structurelle**, et elle se reproduira à chaque session
tant que la note devra tout consigner tout en étant lue intégralement à l'ouverture.

**La cause est une incompatibilité de finalités**, pas une négligence : une note **autoportante**
doit tout porter, y compris ce que le pilote ne doit pas savoir avant d'avoir gelé son cadrage.
Les deux exigences ne peuvent pas tenir dans le même fichier.

## §1. INSTRUCTION

> **Le contenu contaminant ne s'écrit pas dans une pièce à lecture obligatoire. Il s'écrit dans
> une ENVELOPPE séparée. La note et le prompt n'en citent que le CHEMIN et le SHA256. Le pilote
> dépose son cadrage gelé AVANT d'ouvrir l'enveloppe, puis l'ouvre, puis confronte.**

Est « contaminant » tout ce qui, connu avant la mesure, permettrait de rendre en découverte ce
qui n'est qu'une confirmation : anticipations d'issue, conclusions d'une version antérieure du
dossier, verdicts déjà écrits sur la cible, et toute substance importée hors périmètre.

Nommage : `<SUJET>-ANTICIPATIONS-RESERVE.md`, TYPE `RESERVE` du vocabulaire fermé.

## §2. Procédure, cinq pas, vérifiable à chacun

1. **La session close écrit l'enveloppe** et la dépose. La note de reprise porte **son chemin et
   son sha256 complet**, et **rien de son contenu**.
2. **La session neuve lit la note** — qui ne la contamine plus — puis **rédige son cadrage gelé**
   sur la cible, avec ses issues pré-déclarées et son critère de verdict.
3. **Le cadrage cite le sha256 de l'enveloppe non ouverte.** C'est la garde anti-substitution :
   une enveloppe échangée après coup se voit au sha, et un cadrage qui ne cite pas le sha n'est
   pas opposable.
4. **Le cadrage est DÉPOSÉ.** Puis, et seulement puis, l'enveloppe est ouverte et son sha
   **re-mesuré et confronté** à celui écrit au cadrage.
5. **La confrontation est rendue** : chaque point de l'enveloppe est classé en
   **CONFIRMATION D'ANTICIPATION** ou en **DIVERGENCE**. Une confirmation ne lève aucune
   incertitude sur la physique ; une divergence est un fait, et elle est le seul produit
   scientifique possible de l'ouverture.

L'ordre est **vérifiable après coup** — c'est la propriété qui distingue les règles qui tiennent
de celles qui échouent : le commit du cadrage précède, dans l'historique git, tout usage du
contenu de l'enveloppe. On ne demande pas au pilote de ne pas savoir ; on rend l'ordre mesurable.

## §3. PORTÉE PROSPECTIVE — ce que l'instruction NE répare PAS

**Elle ne répare pas S19.** Le pilote S19 porte déjà les cinq points de S18 : ils lui sont
arrivés par la lecture obligatoire, avant que la présente instruction n'existe. Conséquence, à
recopier telle quelle avec l'item `R-23` :

> **Le cadrage gelé neuf sur `R-23` AU FOND est rédigé par un pilote CONTAMINÉ. Toute coïncidence
> avec les cinq points se rend en CONFIRMATION D'ANTICIPATION, jamais en découverte.** Le cadrage
> doit **lister les cinq points en tête**, comme issues déjà connues et donc non créditables.

C'est le prix d'une régression déjà consommée : il se paie, il ne s'efface pas. L'instruction vaut
pour la **prochaine** ouverture en aveugle.

## §4. Garde contre le détournement

Une enveloppe n'est pas un lieu où l'on cache ce qui dérange. Trois interdits :

- **Aucun résultat, aucun verdict, aucune mesure ne va en enveloppe.** L'enveloppe ne contient que
  ce qui **anticipe**. Y mettre un résultat serait retirer du dépôt une pièce opposable.
- **L'enveloppe est déposée, publique, hachée.** Elle est cachée au *moment* de la lecture, jamais
  au dépôt. Une enveloppe non déposée est une substance non livrée (R-55).
- **Le pilote ne décide pas seul de ce qui y va.** Le classement d'un contenu en « contaminant »
  est un arbitrage d'opérateur ; le pilote propose et déclare, il ne trie pas.

## §5. Ce que cette instruction ne fait pas

Elle ne scelle rien, n'ouvre aucune gate, ne rend aucun verdict, ne lit aucun corps. Elle ne
répare aucune contamination déjà acquise. `{ A4 ; A2★ ; N }` inchangé · nœud (i) INDÉTERMINÉ ·
β `T-b`, non résolu, seul facteur d'`O₂` ouvert · **CCC n'est ni démontrée ni réfutée.**
