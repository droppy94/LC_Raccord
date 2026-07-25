---
id: LC-PROMPT-S17-DEFAUTS-DAGE
titre: "Défauts d'âge de `PROMPT-OUVERTURE-S17.md`, déposé à `aedc9a2` — NOMMÉS par fichier séparé daté. Le prompt reste BYTE-INTACT et garde son texte."
codename: LC-RACCORD
type: "amendement de nomination. Il ne corrige rien en place et n'autorise personne à le faire."
version: 1.0
langue: fr
date: 2026-07-25
session: S17
objet_sha256: 1b8b35f606fa5069bf41bdd02e59a68e3ffdecac4f1d5f48146048a61be78b04
objet_blob_git: 25dcf72d67c726bea1aa7f2a4a0e2087b5a8588a
---

# Défauts d'âge du prompt d'ouverture S17 — nommés, non corrigés

## 0. Règle appliquée

**Un défaut d'âge se nomme et s'amende par FICHIER SÉPARÉ DATÉ, jamais en place ; la
pièce amendée reste BYTE-INTACTE** (précédents S8/S9, appliqués en S16 à
`audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md` et à `NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md`).

`PROMPT-OUVERTURE-S17.md` n'est **pas modifié d'un octet** par la présente pièce.
Il garde son sha256 `1b8b35f606fa5069bf41bdd02e59a68e3ffdecac4f1d5f48146048a61be78b04`.

**Aucun de ces défauts n'a été corrigé d'office.** Ils ont été MESURÉS, puis nommés.

## 1. Identification de l'objet — MESURÉE, pas déduite

| fait | mesure |
|---|---|
| commit d'ajout | `aedc9a2`, 2026-07-25 18:54:44 +0000 |
| commits touchant le fichier | **1 seul** — jamais modifié depuis |
| blob à `aedc9a2` | `25dcf72d67c726bea1aa7f2a4a0e2087b5a8588a` |
| blob à HEAD | `25dcf72d67c726bea1aa7f2a4a0e2087b5a8588a` — **identique** |
| HEAD au 2026-07-25 | `b79e3deba57663c15b1aef49cb529c511d51700d`, 19:03:28 +0000 |
| ce que `b79e3de` touche | `NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md`, **et rien d'autre** |
| écart temporel | **524 secondes** |

## 2. DÉFAUT nº1 — l'ATTENDU de HEAD est FAUX. Décalage de +1, exactement.

**Porteur** : `PROMPT-OUVERTURE-S17.md` §1, l.5-8.

Le prompt écrit : `ATTENDU : HEAD = le commit dont le message commence par « Reprise
S16 »`, puis `11e924e · 5f9874c · 20290b1 · 1c90daf · b4af0c5 · 8caafa7 · 09d9e2a`.

**Mesuré** : la chaîne annoncée est **intégralement présente et dans l'ordre annoncé**,
mais elle commence à **`HEAD~1` = `aedc9a2`**. Un commit postérieur, `b79e3de`, s'est
intercalé au sommet.

**Décomposition de l'écart : décalage de position de +1, et rien d'autre.** Aucun
maillon manquant, aucun maillon permuté, aucune divergence de contenu. L'attendu est
faux **sur le seul point de la position**.

**Ce défaut n'est PAS le piège R-36 de S13/S14.** En S14, `NOTE-REPRISE-GIT-S13.md`
annonçait `HEAD = cad358a` « tant que S13 n'est pas déposée » alors qu'elle l'était,
et **rien n'avait prévu le cas** (note S16 §0.4). Ici, le prompt **pré-déclare le
mécanisme** à ses lignes 12-15 — « *une note peut mentir par âge SUR SON PROPRE
ATTENDU* », « *VÉRIFIE-LE PAR `git log`, JAMAIS PAR UNE NOTE* » — et **ordonne la
mesure qui le prend en défaut**. Le prompt a raison sur le mécanisme et tort sur la
valeur. C'est une garde qui a mordu son propre porteur : elle a fonctionné.

## 3. DÉFAUT nº2 — la CLAUSE DE POSITION est fausse, et R-36 ne la couvrait pas

**Porteur** : `PROMPT-OUVERTURE-S17.md` §1, l.9-11.

> « Le sha de HEAD n'est PAS écrit ici : ce prompt est déposé DANS ce commit et ne
> peut pas le connaître (R-36). »

**Trois propositions conjointes, mesurées séparément :**

| | proposition | verdict |
|---|---|---|
| **P1** | le prompt est déposé dans un commit `C` | **VRAIE** — `C` = `aedc9a2`, §1 |
| **P2** | `C` = HEAD | **FAUSSE** — `aedc9a2` ≠ `b79e3de` |
| **P3** | R-36 : une pièce ne peut pas porter le sha du commit qui la contient | **VRAIE** |

**Lecture alternative écartée par mesure.** Si « ce commit » désignait `aedc9a2` sans
l'identifier à HEAD, la raison pour laquelle le prompt ignore le sha de HEAD ne serait
plus l'auto-référence mais la **postériorité** — et **R-36 ne s'appliquerait pas**. Or
R-36 est cité nommément, et R-36 porte bien sur l'auto-référence — le dépôt le dit en
toutes lettres, `manifest/LC-WORK-AUDIT-PAQUET-GEL-v2_124.md` glosant la règle
**« R-36 : ne porte NI son sha NI le PKG de clôture »** et **« le journal NE PORTE PAS
son propre PKG »**, et employant **13 fois** la formule opératoire **« gel R-36
hors-fichier »** sur **52** occurrences de `R-36` : le sha d'un gel se consigne HORS du
fichier gelé, parce qu'un fichier ne peut pas porter le sien. L'invocation de R-36
**présuppose P2**. La clause affirme donc bien P2.

**P2 a été vraie 524 secondes.**

**Ce que ce défaut établit, et qui est NEUF.** Le contournement de R-36 — désigner par
le MESSAGE et jamais par un sha — a **parfaitement fonctionné** : la désignation
« *le commit dont le message commence par Reprise S16* » identifie encore correctement
`aedc9a2` après le dépôt de `b79e3de`. Ce n'est donc pas le contournement qui a échoué,
c'est **la clause de position qui lui était attachée**. R-36 interdit à une pièce de
porter son propre sha ; **il ne l'autorise pas à affirmer qu'elle se trouve au sommet**.
Une désignation par message survit à un dépôt postérieur ; une clause « = HEAD » n'y
survit pas.

**Défaut NON BLOQUANT et de nature AUTO-RÉVÉLANTE** : la seule exécution de la consigne
que le prompt lui-même impose — mesurer HEAD par `git log` avant de lire la pièce — le
découvre en un geste. Un défaut sur-restrictif produit un faux blocage ; celui-ci ne
produit ni faux acquis ni faux blocage, **à la condition stricte que l'ordre mesurer →
lire soit tenu**. Si l'ordre est inversé, il produit un faux acquis.

## 4. DÉFAUT nº3 — la fenêtre de vérification prescrite ne couvre plus l'attendu

**Porteur** : `PROMPT-OUVERTURE-S17.md` §1, l.4 — `git log --oneline -8`.

Sous le décalage du défaut nº1, cette fenêtre rend `b79e3de … 8caafa7`. **`09d9e2a`,
huitième et dernier maillon de la chaîne annoncée, tombe HORS FENÊTRE** (mesuré : 0
occurrence dans la sortie de `-8`).

**La consigne de vérification est devenue insuffisante à vérifier son propre attendu.**
Il faut `-9`. Défaut **dérivé** du nº1 : il n'a pas de cause propre et disparaîtra avec
lui. **Non corrigé en place.**

## 5. DÉFAUT nº4 — défaut de PORTÉE : le prompt renvoie à une note incomplète

**Porteur** : `PROMPT-OUVERTURE-S17.md` §2 (l.17-21) et §8 (l.157-172).

Le §2 envoie la session neuve vers `NOTE-REPRISE-GIT-S16.md` **seule**, déclarée
« UNIQUE et AUTOPORTANTE ». Le §8 liste **huit** précédents S16.

**Mesuré** : `NOTE-REPRISE-GIT-S16-AMENDEMENT-1.md`, déposé à `b79e3de`, porte **trois
précédents S16 supplémentaires** — nº9 (l'ordre R-55 inversé), nº10 (un écart au seul
message de commit n'est pas porté), nº11 (faux PASS : le contrôle a matché la règle au
lieu de l'incident) — plus la confrontation de dépôt S16 et l'audit de clôture.
`AMENDEMENT-1` apparaît **0 fois** dans le prompt et **0 fois** dans la note.

Précédents S16 réellement opposables : **8 + 3 = 11.** Le prompt en porte 8.

**Le prompt ne pouvait pas citer cette pièce** : elle lui est postérieure de 524
secondes. Même mécanisme d'âge que les défauts nº1 à nº3, autre support. **La note S16
n'est pas fautive non plus** : elle a été rédigée avant le dépôt qu'elle annonce, ce
que son propre amendement §0 consigne.

**Conséquence opposable, et c'est la plus lourde** : une session qui lirait le prompt et
la note sans l'amendement **manquerait l'obligation de restaurer l'ordre R-55** —
annonce → token → push — que le précédent nº9 impose explicitement à S17. Le §9 du
prompt **énonce la règle** mais **ne porte pas l'incident**. C'est très exactement la
configuration décrite par le précédent nº11 : trouver le mot, pas le fait.

## 6. CE QUI N'EST PAS UN DÉFAUT — l'unicité de la note est TENUE

Le §2 du prompt demande de nommer un écart si **deux notes de reprise** se trouvent en
racine. **Il n'y en a qu'une.** Mesuré : la racine porte **5 fichiers**, dont une seule
note de reprise, `NOTE-REPRISE-GIT-S16.md`, sha256
`ecde0f001adc3c3727fe752ac80528fab3b892ebba5fcd9911169e388c197eee`, **byte-intacte** et
conforme au sha annoncé par l'amendement.

**Un amendement daté n'est pas une seconde note.** Aucun écart d'unicité. Rien à
corriger.

## 7. PRÉCÉDENT PROPOSÉ À L'INSCRIPTION — sur GO, il est ici sous sa forme rédigée

**UNE PIÈCE NE PEUT PAS DAVANTAGE CONNAÎTRE SA POSITION QUE SON SHA.**

R-36 interdit à une pièce de porter le sha du commit qui la contient ; il **ne
l'autorise pas** à affirmer qu'elle se trouve à HEAD. Le contournement canonique —
désigner par le MESSAGE — protège **l'identification** et survit à tout dépôt
postérieur. Il ne protège **pas** la clause de position qu'on lui attache, laquelle
cesse d'être vraie au premier commit suivant. La position d'une pièce **se mesure sur
le dépôt, elle ne se déduit pas de son contenu** — symétrique du précédent S14 nº1.
Toute clause « = HEAD » écrite dans une pièce est **datée par construction** et doit
être lue comme telle.

**Distinction à tenir, sinon le précédent se dissout dans l'ancien** : le piège R-36 de
S13/S14 portait sur un ATTENDU non anticipé. Celui-ci porte sur la JUSTIFICATION
elle-même, dans une pièce qui avait correctement anticipé le piège et l'avait
correctement contourné. **Le contournement était bon. La clause qui l'accompagnait ne
l'était pas.**

## 8. Ce que cette pièce ne fait pas

Elle ne modifie pas `PROMPT-OUVERTURE-S17.md`, ne modifie pas `NOTE-REPRISE-GIT-S16.md`,
ne modifie pas son amendement 1, n'autorise personne à les modifier, ne rouvre aucun
item soldé, ne classe aucune source, n'ouvre aucune gate, ne touche aucun verdict, et
**n'est pas une note de reprise**.

Elle ne se substitue pas au report en note de reprise S17 : **nommer n'est pas
reporter**, et un écart nommé dans une pièce d'audit doit encore être porté par la note
autoportante (précédent S16 nº10).

**Recalage du §0-lite induit par le dépôt de la présente pièce** : `audit/` passe de
**50 à 51**. Les cinq autres comptes sont inchangés. À porter au prompt d'ouverture S18.

## 9. Conformité de nommage — NON ACQUISE, déclarée

`audit/LC-NORME-NOMMAGE.md` est au statut **PROPOSITION, NON ARBITRÉE** ; elle ne
renomme rien et ne lie rien. Le nom de la présente pièce suit sa grammaire §1 (sujet
d'abord, type en queue), mais **`DEFAUTS-DAGE` n'appartient pas au vocabulaire de TYPE
fermé du §2**. Il est employé par continuité avec la seule pièce déposée du même genre,
`audit/LC-BETA-DEFAUTS-DAGE-PAQUET.md`.

**C'est une seconde occurrence d'un type hors vocabulaire, et elle est nommée ici pour
qu'elle ne vaille pas fait accompli** : la norme dit qu'un type neuf s'ajoute **par
amendement à la norme**, jamais par l'usage. Point porté à l'arbitrage opérateur, ITEM 3.

---

*§6.4 — nommer, mesurer, décomposer, confronter, consigner : aucun de ces gestes ne
scelle, ne réduit, ne compte, ne démontre quoi que ce soit. Nommer un défaut ne le
répare pas, et le mesurer ne le corrige pas. `{ A4 ; A2★ ; N }` INCHANGÉ · β `T-b`, non
résolu, SEUL facteur d'O₂ ouvert. **CCC n'est ni démontrée ni réfutée.***
