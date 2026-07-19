---
id: LC-WORK-AMENDEMENT-R7-PACKAGE-SHA-CONVENTION
titre: "Amendement R-7 PROSPECTIF ET DATÉ (p-2) — convention PACKAGE_SHA FIGÉE au harnais : recette UNIQUE par RENVOI à la recette C-pkgsha déjà gelée au §0 du manifeste (lignes nom deux-espaces sha256, triées, jointes par saut de ligne, SANS saut terminal), ÉCRITE AU BLOC PAR LE SCRIPT, et pré-engagée hors-KB AVANT expédition. Traite D-08 (issue souveraine CSE-KPS) : la définition du harnais laissait ouverts le séparateur et le saut de ligne terminal ; la concordance a été OBTENUE, elle n a pas été SPÉCIFIÉE. MOTIF PORTANT, CONTRE LE PILOTE : une recette ambiguë rend au pilote un DEGRÉ DE LIBERTÉ APRÈS le pré-engagement, ce qui détruit la seule fonction du pré-engagement. GRADE TENU : PACKAGE_SHA N EST PAS la gate d ARRÊT — le sur-grader fabriquerait un FAUX ARRÊT, classe D-b. SANS SURCLASSEMENT (§6.4) : figer une convention NE SCELLE, NE RÉDUIT, NE COMPTE, NE DÉMONTRE RIEN. {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 (work-active) — règle d INSTRUMENT et de FORME. NE scelle rien, NE vote pas, NE contient AUCUNE algèbre, N adjuge AUCUNE issue, NE re-juge AUCUNE issue rendue."
statut: "work-active — PROSPECTIF. DÛ AVANT TOUTE GATE FUTURE. S applique au PROCHAIN harnais et aux suivants. JAMAIS rétroactif : aucune passe rendue n est reclassée, aucun rapport souverain n est re-jugé. L issue K-B de la gate CSE-KPS reste TELLE QU ELLE A ÉTÉ RENDUE, et le PACKAGE_SHA confronté conforme de cette gate reste CONSOMMÉ, NON re-jugé."
version: "0.1"
langue: fr
date: "2026-07-17"
gel_R36: "consigné HORS-FICHIER (R-36 : ce fichier n embarque NI son propre sha, NI aucune valeur qu il produirait)"
prerequis_kb: [LC-WORK-AUDIT-PAQUET-GEL, LC-WORK-AMENDEMENT-R7-SHA-GATE-FORMAT-NOM, LC-WORK-AMENDEMENT-R7-CSE-SHA-GATE, LC-WORK-AMENDEMENT-R7-ANTI-ANCRAGE-SEQUENCE, LC-WORK-AMENDEMENT-R7-CONVERSION-R56-M1, PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE, PROMPT-INCOGNITO-CSE-KPS-PRESCRIPTION, LC-JOURNAL-V93]
tags: [amendement, R-7, prospectif, date, PACKAGE_SHA, convention, recette-unique, C-pkgsha, D-08, D-b, p-2, pre-engagement, monotone-sur, §6.4]
---

# (p-2) — convention PACKAGE_SHA figée au harnais

## 0. Le défaut, tel qu il a été constaté — PAR LE SOUVERAIN, et re-vérifié AU FICHIER

**D-08**, consigné par le souverain CSE-KPS : la **convention de calcul du PACKAGE_SHA** est **à
figer au harnais** — terminaison de ligne, encodage.

Re-vérifié au fichier ce jour, **sur le mount** (R-54). Le harnais définit, en **Phase 0** :

> le PACKAGE_SHA, sha256 de la **concaténation**, **triée par nom**, des lignes **nom deux-espaces
> sha256** des **trois pièces**.

**Ce qui est fixé** : le périmètre (les **trois pièces**, les retraits **exclus**), le séparateur
**deux espaces** à l intérieur de la ligne, l **ordre trié**.

**Ce qui NE l est PAS, et c est le défaut** :

- **(i) Le séparateur ENTRE les lignes.** Le harnais écrit **concaténation**. **Une concaténation
  n est pas une jointure par saut de ligne** — et les deux rendent des valeurs **différentes**.
- **(ii) Le saut de ligne TERMINAL.** Rien n en dit un mot. **Deux valeurs licites, au choix du
  lecteur.**
- **(iii) L encodage** et **(iv) la casse du hex**. Ici **bénins par le fait** — les noms sont ASCII,
  les sha en minuscules — **mais bénins n est pas SPÉCIFIÉS**.

## 0bis. LE FAIT AGGRAVANT : LA KB AVAIT DÉJÀ LA RECETTE, FIGÉE ET COMPLÈTE

Le **§0 du manifeste** porte, **gelée sous R-36 et conservée VERBATIM à travers deux compactions**,
la recette **C-pkgsha** :

> `sha256` des lignes `nom_canonique` **deux-espaces** `sha256`, **triées**, **jointes par un saut de
> ligne**, **SANS saut de ligne terminal**.

**Elle répond EXACTEMENT aux points (i) et (ii).** Elle est **le registre irremplaçable de toute la
lignée PKG-SHA depuis v2.66** — c est **la RECETTE, non la chaîne**, qui rend les tables
reconstructibles du mount.

> **Le harnais n a pas eu besoin d une convention : il en avait une, figée, complète, éprouvée sur
> plus de deux cents fichiers. IL EN A ÉCRIT UNE SECONDE, PARTIELLE.**
> **Deux recettes pour un même geste : la divergence est une question de temps, pas de principe.**

## 0ter. CE QUI S EST RÉELLEMENT PASSÉ — ET C EST CONTRE LE PILOTE

Le PACKAGE_SHA de la gate KPS a été **recomputé par l auditeur** et **confronté conforme** à la
valeur **pré-engagée à la table opérateur avant expédition** — la **variante sans saut de ligne
terminal**. **Le contrôle a passé.**

**Il a passé parce que l auditeur a correctement DEVINÉ l intention du pilote.**

> **Un contrôle qui repose sur une convergence et non sur une spécification n est pas un contrôle :
> il a passé CETTE FOIS.** **Un contrôle qui fonctionne parce que celui qu on contrôle a été bien
> deviné est une DEMANDE POLIE** — même famille que **D-a**, au niveau de la recette.

**LE MOTIF PORTANT, ET IL EST LE CŒUR DE CET AMENDEMENT.** La fonction du PACKAGE_SHA est le
**PRÉ-ENGAGEMENT** : une valeur **unique**, déposée **hors du paquet**, à la **table opérateur**,
**AVANT** expédition. Or :

- **La gate pièce-par-pièce ne protège PAS contre le pilote.** Elle confronte **chaque pièce au bloc
  du paquet**. Si le pilote **déplace la pièce ET sa ligne au bloc**, **elle passe** : les deux ont
  bougé ensemble.
- **Le seul témoin d une édition coordonnée du bloc est le PACKAGE_SHA PRÉ-ENGAGÉ HORS DU PAQUET**,
  détenu par **l opérateur**, hors d atteinte du pilote.
- **Et une recette AMBIGUË rend au pilote un DEGRÉ DE LIBERTÉ APRÈS le pré-engagement** : deux
  variantes licites, deux valeurs, **et le choix de celle qui concorde peut se faire APRÈS COUP**.

> **Une convention ambiguë ne dégrade pas le pré-engagement : ELLE LE DÉTRUIT.**
> Un engagement dont on choisit la règle de vérification après l avoir pris **n est pas un
> engagement**. **D-08 n est PAS cosmétique.**

## 1. Prescriptions — opposables, énumérées, CLOSES

**Q-1 — RECETTE UNIQUE, PAR RENVOI. JAMAIS UNE SECONDE COPIE.** Le PACKAGE_SHA est défini comme
**la recette C-pkgsha du §0 du manifeste**, appliquée aux **pièces énumérées au bloc**. **Le harnais
NE RÉÉCRIT PAS la recette dans ses propres mots : il l INSTANCIE.** **Une seule recette dans la KB.**

**Q-2 — ÉCRITE AU BLOC, EXÉCUTABLE SANS DEVINER.** Le bloc porte la recette **en forme exécutable**,
**tous points fixés, aucun laissé à l inférence** :

- **ligne** := nom de la pièce, **deux espaces**, sha256 en **hex minuscules** ;
- **ordre** := **tri par octets** sur le nom, **jamais** un tri dépendant de la locale ;
- **jointure** := **un saut de ligne** entre les lignes ;
- **terminaison** := **AUCUN saut de ligne terminal** ;
- **encodage** := **UTF-8**, avant hachage ;
- **périmètre** := **les pièces énumérées au bloc**, les **segments de retrait EXCLUS** ;
- **rendu** := **hex minuscules**.

**Q-3 — ÉCRITE PAR LE SCRIPT, JAMAIS À LA MAIN.** Le générateur **écrit le texte de la recette** au
bloc **et calcule la valeur**. **Précédent contraignant, déjà acquis** : le bloc sha du harnais est
**écrit par le générateur** depuis sa refonte. **Une recette recopiée à la main est une recette qui
diverge.**

**Q-4 — PRÉ-ENGAGEMENT OPÉRATEUR, CONSERVÉ TEL QUEL.** La valeur est consignée à la **table opérateur
hors-KB**, **AVANT expédition**, **jamais après**. **Geste opérateur** : **le pilote ne pré-engage
pas sa propre valeur de contrôle.** Pratique déjà tenue à deux gates ; **elle est ici FIGÉE, pas
inventée**.

**Q-5 — UNE SEULE VALEUR EST LICITE.** Sous Q-2, il n existe **plus de variante**. **Toute mention
d une variante, d une tolérance, ou d un choix de convention APRÈS pré-engagement est INTERDITE** et
constitue un **défaut à consigner par l auditeur**, **même si les valeurs concordent** — **R56-4,
appliqué tel quel.**

**Q-6 — GRADE, ET IL BORNE LE PRÉSENT AMENDEMENT.** **Le PACKAGE_SHA N EST PAS la gate d ARRÊT.**
La gate d **ARRÊT** est, et **reste**, la **confrontation pièce par pièce** de la Phase 0. Le
PACKAGE_SHA est le **témoin de pré-engagement de la COMPOSITION**. Par conséquent :

> **Écart de PACKAGE_SHA ⟹ DÉFAUT À CONSIGNER, PLEINEMENT VALORISÉ. PAS un ARRÊT.**
> **Le sur-grader en gate fabriquerait un FAUX ARRÊT sur une question de convention** — **exactement
> la classe D-b** : *une gate dont la forme induit un faux arrêt est un défaut de gate.*
> **Et l ARRÊT, lui, reste dû au premier écart pièce-par-pièce, inchangé.**

## 2. Grade — tenu, SANS sur-grade

Ce que le PACKAGE_SHA atteste : **que la LISTE des pièces et leurs sha déclarés sont ceux qui ont été
pré-engagés hors du paquet avant expédition**. **RIEN D AUTRE.**

Ce qu il **N atteste PAS** :

- **Il n atteste pas le CONTENU des pièces** — cela, c est la gate pièce-par-pièce, **et un sha
  conforme n atteste que l identité des octets, jamais un EXIT 0, jamais une conclusion**.
- **Il n atteste pas que le paquet est HONNÊTE.** Un paquet **parfaitement** pré-engagé peut être
  **mal scopé**, **ancrant**, ou **fitté**. C est **Δ-3**, **classe NON FERMÉE**, **b6 TIENT** —
  **cet amendement ne la touche pas.**
- **Il n atteste pas l antériorité au sens cryptographique fort.** La valeur transite par
  l **opérateur**, non par un tiers horodateur. Ce qu il **ferme**, c est l édition **entre
  pré-engagement et expédition** ; ce qu il **ne ferme pas**, c est la rédaction **avant** le
  pré-engagement, où le pilote est **libre**. **Limitation STRUCTURELLE, consignée, non escamotée.**
- **Il ne dé-lit pas** et **ne dé-expédie pas**. **La porte NE PEUT PAS DÉ-LIRE** — grade reconduit
  tel quel, **jamais élargi**.

## 3. Test de direction — MONOTONE-SÛR, et il joue CONTRE LE PILOTE

- **N ajoute AUCUN prior, n en retire AUCUN.** Ne peut **PAS** changer un verdict — seulement
  **retirer au pilote le choix de la règle de vérification après coup**.
- **Direction, sans ambiguïté** : le pilote **perd** le degré de liberté du §0ter, **perd** la
  latitude de rédiger la recette à sa main (Q-3), **perd** le droit d invoquer une variante (Q-5), et
  **gagne** une obligation de forme. **L auditeur et l opérateur gagnent** un contrôle qui **spécifie**
  au lieu de **deviner**. **Rien dans cet amendement ne sert le pilote.**
- **Coût : FAIBLE, MAIS NON NUL, ET IL SE DÉCLARE.** Quelques lignes au bloc, une fonction au
  générateur. **Il n est PAS gratuit — prétendre qu il l est serait le sur-grade suivant.**
- **INTÉRÊT DU PILOTE, DÉCLARÉ, CONTRE LUI :** déposer (p-2) permettrait de dire que **D-08 est
  réparé**. **Il ne l est pas** : **D-08 reste au dossier, entier**, et la valeur de (p-2) **ne sera
  établie qu à la prochaine gate**, par un fait vérifiable — **la recette figurait-elle au bloc, en
  forme exécutable, écrite par le script, oui ou non**. **Écrire un amendement n est pas réparer un
  défaut** : **(γ-2) l établit sur pièce**, et **(p-1) le consigne**.
- **Zéro-fuite** : une recette de hachage **ne dit rien** du contenu des pièces.

## 4. Anti-fit — R-7 tenu, argumenté

- **PROSPECTIF ET DATÉ**, écrit le **2026-07-17**, **AVANT TOUTE GATE FUTURE**. **AUCUNE gate n est
  armée à cette date** : il n existe **aucune issue** sur laquelle le fitter.
- **POSTÉRIEUR à l issue K-B, et sans prise sur elle.** Le PACKAGE_SHA de la gate KPS a été
  **confronté conforme** et est **CONSOMMÉ**. **Cet amendement ne le re-juge pas**, **ne rouvre pas
  la gate**, **ne déclenche aucun re-audit**. **K-B reste TELLE QU ELLE A ÉTÉ RENDUE.**
- **Ne reclasse aucune passe.** Les harnais antérieurs **restent tels qu ils sont**, **avec D-08
  CONSIGNÉ**.
- **Ne re-gèle RIEN.** La recette **C-pkgsha** du §0 du manifeste est **CITÉE ET INSTANCIÉE**,
  **NON re-gelée**, **NON rectifiée**, **NON réécrite**. **(γ-1) et la sha-gate : cités et appliqués,
  non re-gelés.**

## 5. Bornes CLOSES — b1 à b5

- **b1** — Ferme **exactement** la classe **D-08** : *la convention de calcul du PACKAGE_SHA laissée
  au choix du lecteur*. **RIEN de plus.**
- **b2** — **Ne dit RIEN du contenu, du scope, ni de l honnêteté d un paquet.** Le **scan de blinding**
  et le **scan ⑤** restent **dus et inchangés**. **Δ-3 : NON réparée, elle SURVIT.**
- **b3** — **Ne modifie NI la gate pièce-par-pièce, NI son ARRÊT, NI le format (γ-1)** — *un champ par
  ligne, sha COMPLET, jamais un tableau à pipes* — **reconduits tels qu écrits**. **La porte n est
  PAS retirée et n est PAS élargie.**
- **b4** — **Ne répare NI D-01, NI Δ-3, NI D-7, NI D-d.** D-01 est traité **séparément** par **(p-1)** ;
  **les deux amendements sont INDÉPENDANTS et ne se couvrent pas l un l autre.**
- **b5** — **Ne dit RIEN de la substance.** **AUCUNE issue** — ni `{K-A..K-D}`, ni `{P-1 ; P-2 ; P-3}`,
  ni `{S-1 ; S-2 ; S-3}`, ni `{V-A..V-D}` — n est ouverte, fermée, ni touchée.

## 6. Contrôle de conformité de CE fichier (déclaration, à VÉRIFIER)

Le pilote **déclare** : **0 occurrence de son propre sha** (R-36, scan **court ET complet**) ; **0
caractère pipe** ; **0 valeur projetée** ; **0 sha abrégé dans une prescription** — les renvois à
**C-pkgsha**, **(γ-1)**, **(γ-2)**, **(p-1)** et à la **sha-gate** sont des **renvois EN PROSE vers
des gels existants**, **expressément licites** par **(γ-1) F-2**. **Aucune valeur de PACKAGE_SHA
n est écrite ici** — **ce fichier prescrit une recette, il n en publie aucun résultat.**

**C est une DÉCLARATION, PAS un fait : VÉRIFIE-LA.** **Le pilote qui écrit le scan est le pilote qui
a INTÉRÊT à ce qu il passe.** Le firewall se vérifie **PAR LS SUR LE MOUNT**, jamais par grep dans
un fichier — **hors-scope ici, donc SANS ATTENDU** : *un scan qu on déclare hors-scope n a pas
d attendu.*

## 7. Non-surclassement (§6.4)

Figer une convention de hachage / renvoyer à une recette gelée / borner un grade **NE SCELLE, NE
RÉDUIT, NE COMPTE, NE DÉMONTRE RIEN**. Un PACKAGE_SHA conforme **n atteste que la composition
pré-engagée du paquet**, jamais que le paquet est honnête, **et jamais une conclusion physique**.

**K-B est une DÉLIMITATION** : la source KPS **ne mord pas** sur le résidu PRESCRIPTION-𝓘⁺ **tel que
nommé**. **Cet amendement n y touche pas.** Les têtes scellées restent l **AUTORITÉ**, **INTACTES**.
`LC-D-IRREDUCTIBILITE-MOYENS` **tient**.

`{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 **non clos** ; N **non fixé** (≡Λ, voie A close, **R-53 0/4
INCHANGÉE**) ; O₂ **NON construit** ; β **T-b, NON résolu, SEUL facteur d O₂ ouvert** ; A4 route
par-𝓘⁺ délimitée (W2), postulat renforcé, **NON réfuté** ; A2★ **parqué pending OA** ;
**CCC non démontrée NI réfutée**. `établi (algèbre)` atteste l algèbre correcte, **jamais** une
conclusion physique.
