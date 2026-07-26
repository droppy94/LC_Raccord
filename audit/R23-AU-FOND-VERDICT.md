---
id: R23-AU-FOND-VERDICT
titre: "Verdict de la voie (i) AU FOND sur R-23, rendu sous les cibles gelées de R23-AU-FOND-CIBLES-GELEES (85b1a0e). R-23 N'EST PAS SOLDÉE : elle est SUSPENDUE À OB. Délimitation, aucune réduction de compte."
codename: LC-RACCORD
type: "verdict de front. Un verdict ne scelle rien, n'ouvre aucune gate, ne réduit aucun compte (§6.4)."
version: 1.0
langue: fr
date: 2026-07-26
session: S20
cadrage: "audit/R23-AU-FOND-CIBLES-GELEES.md — sha256 b5308815ac16cd634e0eabc3c408eb0fbab9c27b80d4f0524e7b32978d73d4b5 — déposé à 85b1a0e AVANT toute lecture du corps."
enveloppe: "audit/F5-ANTICIPATIONS-RESERVE.md — sha256 3200e69b24fc9edf1f552e2bb1c03f2797962b63c1eb898f63dbc9946ef19e75 — ouverte APRÈS 85b1a0e, sha re-mesuré conforme."
---

# R-23 AU FOND — verdict

## §0. Ordre tenu, et il est vérifiable

Cadrage déposé à `85b1a0e`. Enveloppe ouverte après, sha re-confronté. Corps de
`kb/LC-D-F5-ETAT-RACCORD.md` (30 423 o) lu **ensuite**, intégralement, **avant** toute recherche
(`R-54`). Classer puis confronter, tenu. **Aucun sceau armé, aucune pièce `kb/` modifiée, aucun gel
rejoué.**

## §1. `C-1` = **(a) CONTINGENTE** — et c'est le verdict de la séance

La classification `inconfrontable` de la Table III est **levable**, et **le corps de F5 écrit
lui-même sa condition de levée** :

- §4ter : *« Les valeurs ci-dessus sont consignées comme intrant futur. Elles deviendront
  confrontables **dès que** O₂ fournira le coefficient `W³` (renvoi-avant, **pas une fermeture**). »*
- §2, `OB` : *« construire O₂ fournit `⟨TTT⟩`, donc le coefficient `W³`, donc **rend la Table III
  confrontable**. »*
- §4ter, `L3 non déclenché` : la forme des templates `W³` de la source **n'est pas en contradiction**
  avec la forme programme. La borne est **appariée en FORME**.

L'issue **(b) STRUCTURELLE est donc écartée par le texte** : rien n'établit une non-comparabilité de
nature — au contraire, l'appariement de forme est constaté et l'incompatibilité explicitement non
déclenchée. L'`inconfrontable` est **contingent à l'absence d'une valeur programme**, non à la
nature des objets.

**CRITÈRE DE VERDICT, appliqué tel qu'écrit avant lecture :**

> `C-1` = (a) ⟹ **`R-23` N'EST PAS SOLDÉE AU FOND. Elle est SUSPENDUE À `OB`.** Le mot `soldée` doit
> être remplacé par `suspendue à OB` partout où il est cité. **DÉLIMITATION**, jamais une réduction.

**Ce point n'est PAS anticipé.** Les cinq points de l'enveloppe portent `R-23 déclarée SOLDÉE` et
`Table III inconfrontable` — **aucun ne porte le TYPE de cet `inconfrontable`**. La distinction
contingent / structurel n'était écrite nulle part avant le présent cadrage. **Ce n'est donc pas une
confirmation d'anticipation.**

## §2. `C-2` = **(b) ENREGISTRÉ** — mais c'est une CONFIRMATION, pas une trouvaille

**Déclaré pré-empté au §1 du cadrage, avant lecture** : l'enveloppe §3 portait *« Le côté `R-23` n'a
jamais été ouvert »*. L'issue (b) était donc annoncée. **Elle se rend en CONFIRMATION
D'ANTICIPATION.**

Le corps écrit : *« le verrou reste purement interne (`OB`), **exactement comme l'audit F2 l'avait
établi** (`R-23`) »*, et renvoie en §7 à `LC-AUDIT-LOG-F2`. Le bullet F2 du programme écrit, lui,
*« verrou `W³` purement interne, **renvoi-avant F5**, `R-23` »*. **F2 renvoie en avant à F5 ; F5
renvoie en arrière à F2. CIRCULARITÉ DE RENVOI ÉTABLIE.**

**DÉFAUT DE RÉSOLUTION DE MA PROPRE GRILLE, nommé et non corrigé** — troisième occurrence de cette
classe dans la séance. La partition (a) *dérivé* / (b) *enregistré* est trop grossière : F5 **dérive**
l'extraction (valeurs de la Table III, coefficient `0,5291` de la note 6, et une **note d'honnêteté
de source** corrigeant l'annotation graine « 900 ± 700 » en `O(500)` littéral) ; F5 **enregistre** la
classification et le verdict d'internalité. **Le geste bibliographique est de F5, le soldement ne
l'est pas.** Modifier la grille après mesure est ce que son gel interdit : la grille reste, le défaut
est écrit.

**DEUX MESURES, l'une décisive, l'autre à ne pas surclasser.**

1. **`soldé` / `soldée` a 0 occurrence dans le corps de F5.** Le mot n'existe que dans les
   **registres** — `02_programme`, `04_references`, `LC-WORK-BRANCHE-FALSIFIABILITE`, `AUD`,
   `IDX_v211`. **Le chaînon censé avoir soldé `R-23` n'emploie jamais le mot.** Le soldement est une
   **inscription de registre**, propagée depuis le bullet F2.
2. **`LC-AUDIT-LOG-F2`, pièce à laquelle F5 attribue l'établissement, est ABSENTE du dépôt.**
   **MAIS — et c'est une garde contre un faux écart — la classe entière est absente : `0` pièce
   `LC-AUDIT-LOG-*` dans `kb/`**, sur 13 prérequis de F5 dont 11 présents, les 2 absents étant les
   deux pièces d'audit. **Ce n'est donc PAS un défaut propre à `R-23`.** L'énoncé juste est :
   *le soldement de `R-23` est attribué à une pièce qui, par classe, n'est pas déposée — il n'est
   donc pas confrontable À L'INTÉRIEUR du dépôt.* **Délimitation d'auditabilité, pas réfutation.**

## §3. `C-3` = **(a) LEVIER ÉCRIT** — la clause de dissolution n'est pas vide

Le corps nomme la valeur manquante **et** ce qui la bloque :

- **Valeur manquante** — les `(a,b,c)` propres du Weyl cubique, à dériver *« depuis le trois-point
  `⟨TTT⟩` de la CFT de raccordement — c'est-à-dire ses constantes de structure »* (§2, `OB`).
- **Bloqueur** — `O₂`, `à inventer`, et **localisé** : une **condition aux limites de jonction mixte
  Dirichlet ↔ Neumann** au `𝒞` (graviton-dual de de Haro, `LC-D-CT-DUAL`), traduisant la
  **réciprocité conforme de Penrose**. *« On sait quoi construire et où »* (§4).

L'issue **(c)** — *aucun levier écrit*, qui aurait rendu la voie (i) au fond vide — **est écartée**.

## §4. CONSÉQUENCE DE CHAÎNAGE — consolidation, et rien de plus

`R-23 ⊂ OB ⊂ O₂` est établi par la cartographie (a) de F5. Le périmètre porte par ailleurs que
**β `T-b` est le SEUL facteur d'`O₂` ouvert**. Donc **`R-23` est en aval de β `T-b`** : ce n'est pas
une dette indépendante.

**SANS SURCLASSEMENT (§6.4).** Rattacher une dette à une racine déjà au périmètre est une
**consolidation**, pas une réduction. `R-23` n'a jamais figuré dans `{ A4 ; A2★ ; N }` et n'y entre
pas. Aucune valeur n'est fixée, aucune borne n'est convertie, `W³` reste **sans valeur**.

## §5. DÉFAUT D'ÂGE DES REGISTRES — nommé, NON corrigé

Cinq pièces `kb/` portent `R-23 soldée`. `kb/` est **SCELLÉ** : le correctif ne se fait pas en place
et **ne se fait pas ici**. Le recalage de `soldée` → `suspendue à OB` est porté en **reste-à-faire,
dépendant de `G-4` volet 3** (migration de `kb/`), comme le volet de recalage de la constitution.
**Aucun octet de `kb/` n'est touché par la présente pièce.**

## §6. Ce que ce verdict ne fait pas

Trancher le type d'un `inconfrontable` ne construit pas `O₂`, ne dérive aucun `(a,b,c)`, ne fixe pas
`N`, ne convertit aucune borne, ne ferme pas `D1`, n'arme aucun sceau et ne dit rien de β `T-b` au
fond. **Une dette requalifiée reste une dette.**

`{ A4 ; A2★ ; N }` INCHANGÉ · `D1` non clos, `D1c` intacte · Silo R clos à 12/12 · nœud (i)
**TRANCHÉ en délimitation** · β `T-b`, NON RÉSOLU, seul facteur d'`O₂` ouvert · **CCC non démontrée
NI réfutée.**
