---
id: NOTE-REPRISE-GIT-S13-AMENDEMENT-1
titre: "Amendement 1 à NOTE-REPRISE-GIT-S13 — REPORT INTÉGRAL des précédents S8/S9/S10/S11, des points de vigilance et de la procédure R-55, préalable OBLIGATOIRE au retrait de NOTE-REPRISE-GIT-S11.md et PROMPT-OUVERTURE-S12.md. S13 §7 héritait PAR FORMULE ; le précédent 860c3f8 établit qu'une formule ne suffit plus dès que la pièce porteuse est retirée. Cet amendement N'AJOUTE AUCUN FAIT NEUF : il recopie ce qui allait mourir en racine. S13 reste BYTE-INTACTE."
codename: LC-RACCORD
type: "amendement à une note de reprise — HORS base scellée. Ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 1.0
langue: fr
date: 2026-07-25
amende: "NOTE-REPRISE-GIT-S13.md — §7 uniquement, par ADDITION. Aucune ligne de S13 n'est retirée ni réécrite (précédent S9 : un défaut se nomme et s'amende par fichier séparé daté, jamais en place)."
motif: "Audit de report exécuté avant le swap d'unicité, conformément au précédent 860c3f8 (« sept items non reportés ont été trouvés et recopiés dans le prompt S11 avant retrait »). L'audit a trouvé que PROMPT-OUVERTURE-S12.md est la PIÈCE DE REPORT des précédents S9 (deuxième report) et S10 (report intégral), en plus de porter les siens. Son retrait sans recopie détruirait le seul porteur EN RACINE de ~26 précédents opposables."
piege_R36: "Cet amendement NE PORTE NI son propre sha NI le commit qui le dépose. HEAD à l'ouverture d'une session neuve se vérifie par `git log`, JAMAIS par une note. État connu au 2026-07-25 : HEAD = 09d9e2a « Reprise S13 », parent cad358a « Sold P-8 », lui-même parent af97865 « Reprise S11 »."
regle_unicite: "Après dépôt de cet amendement PUIS retrait de NOTE-REPRISE-GIT-S11.md et PROMPT-OUVERTURE-S12.md, la racine doit porter EXACTEMENT DEUX pièces de reprise : NOTE-REPRISE-GIT-S13.md et le présent amendement. Un amendement daté n'est pas une seconde note : il est indissociable de sa note (précédent S9, NOTE-REPRISE-GIT-S9-AMENDEMENT-1.md)."
---

# Amendement 1 à la note S13 — report des précédents avant swap

> **Ce que cet amendement est.** Une recopie. Il ne consigne aucun fait neuf,
> n'ouvre aucun chantier, ne tranche aucune question ouverte. Il existe pour
> qu'un retrait ne fasse perdre à la racine ce que la racine portait.
>
> **Ce qu'il n'est pas.** Une seconde note de reprise. La règle d'unicité vise
> les NOTES ; un amendement daté est indissociable de la sienne.

## §1 — Pourquoi il existe

`NOTE-REPRISE-GIT-S13` §7 écrit : *« Tous les précédents S4–S12 restent
PLEINEMENT OPPOSABLES (voir historique et S12 : … etc.) »*. C'est un héritage
**par formule**, avec renvoi à `PROMPT-OUVERTURE-S12.md`.

Le commit `860c3f8` (swap −S9 +S10) a déjà rencontré et tranché ce cas :

> *« Retrait précédé d'un AUDIT DE REPORT item par item : sept items non
> reportés ont été trouvés et recopiés dans le prompt S11 avant retrait, dont
> les SEPT PRÉCÉDENTS S9 intégralement (leur pièce porteuse étant retirée,
> l'héritage par la formule « S4–S9 » ne suffisait plus). »*

Le même mécanisme s'applique ici, en plus lourd : `PROMPT-OUVERTURE-S12.md`
n'est pas seulement porteur de ses propres précédents, c'est la **pièce de
report** des précédents S9 (reportés pour la **deuxième** fois) et S10
(reportés **intégralement**). Le retirer sans recopie détruirait le seul
porteur **en racine** de l'ensemble ci-dessous.

Ces pièces survivent dans l'historique git. Ce n'est pas suffisant : la règle
d'unicité existe précisément pour qu'une session neuve lise **la racine**.

## §2 — Précédents S11 — opposables, reportés intégralement

1. **UN CRITÈRE DE BORNAGE NON CONFRONTÉ AU CAS D'ESPÈCE NE BORNE RIEN.**
   Quatre occurrences en un seul volet en S11, **après** que la leçon S10 eut
   été recopiée dans le gel. Écrire la règle ne suffit pas : **imprimer** les
   coordonnées retenues ET le dernier élément inclus, et **constater** qu'il
   appartient au bloc visé.
2. **UNE CORRECTION PEUT ÊTRE FAUSSE, ET AGGRAVANTE.** Elle se rétracte par un
   fichier séparé daté **supplémentaire** ; l'amendement fautif **reste** au
   dépôt et **garde son numéro**. On ne modifie pas un amendement, même erroné.
3. **UN ORDRE DE RÉSOLUTION FIGÉ AU GEL PROTÈGE DU FIT.** Il peut clore un
   verdict sans que tous les discriminants soient atteints, et c'est légitime ;
   le réordonner après mesure serait le fit qu'il interdit.
4. **UNE ABSENCE CONSTATÉE PAR EXTRACTION N'EST PAS UNE ABSENCE.** En S11, une
   convention d'unité donnée pour inexistante par deux sessions vivait dans les
   **en-têtes de colonnes** — invisible à la légende, aux cellules et au flux
   `pdftotext`. Avant de déclarer qu'une information manque, vérifier qu'on l'a
   cherchée **là où elle se loge**.
5. **UN VERDICT SUR UNE CHAÎNE NE RÉFUTE PAS UNE SUBSTANCE.** Reporter l'un
   pour l'autre fait circuler une demi-vérité.
6. **LE FAIT ACCOMPLI D'UN FICHIER NE CRÉE PAS UN TYPE.** Un vocabulaire fermé
   ne s'étend que par amendement à la norme qui le fixe.
7. **UN TOKEN NE S'ÉCRIT NULLE PART** : utilisé en ligne, effacé du disque,
   absent de `.git/config`, des fichiers et du commit — **et vérifié**.
8. **LA CONFRONTATION DE DÉPÔT SE FAIT PAR `diff`, PAS À L'ŒIL.** En S11 les
   cinq sha déposés ont été confrontés **mécaniquement** aux cinq annoncés.

## §3 — Précédents S10 — opposables, reportés intégralement

1. **HACHER UN CONTENANT N'EST PAS LIRE UN CONTENU.** La confrontation d'un
   intrant se fait au niveau **octet** et ne demande **aucune** lecture ;
   confondre les deux fait renoncer à une mesure disponible et écarter une
   pièce sur un obstacle inexistant.
2. **UN BORNAGE PAR NUMÉRO DE LIGNE OU PAR FIN DE PAGE NE BORNE RIEN.**
   Détecter la fin de **légende**, et **vérifier que l'implémentation applique
   la règle énoncée**. Écrire une correction et ne pas l'appliquer est un échec
   d'exécution **distinct** du défaut d'énoncé, et il s'impute pareillement.
3. **UN ESPACE-VERDICT DÉCLARÉ EXHAUSTIF DOIT PRÉVOIR « LES DEUX PARTIES ONT
   TORT ».** Ajouter une case **après** des mesures est un risque de fit : il se
   nomme, se borne par un critère **général**, et ne vaut que si l'issue écartée
   l'a été par **mesure** et non par redéfinition.
4. **UNE INFORMATION LUE HORS PÉRIMÈTRE SE DÉCLARE ET NE S'EMPLOIE PAS.** La
   nommer l'empêche de circuler en contrebande dans une session ultérieure.
5. **LE TOKEN NE REMPLACE PAS L'ANNONCE R-55.**
6. **VÉRIFICATION DE DÉPÔT SUR CLONE NEUF**, jamais sur déclaration.
7. **UNICITÉ DE LA REPRISE** : un seul fichier de reprise, au git comme au
   mount ; ce qui n'est pas réalisé en reprise N est **reporté** en N+1, jamais
   laissé en coexistence.
8. **AUTORITÉ DES PIÈCES DE GOUVERNANCE** : pour les prompts, notes de reprise
   et leurs amendements, **le git fait foi**, le mount vaut copie de travail.
   *(Portée mise à jour : voir §6, arbitrage G-4 du 2026-07-25.)*
9. **SHA DE PREMIÈRE MESURE FAISANT RÉFÉRENCE**, avec leurs tailles :
   `04d9b4f4…` (`2312_12498v2.pdf`, **1 895 152 o**) et `27a94980…`
   (`2409_10595v2.pdf`, **2 332 898 o**). S'y ajoute `113ab4a2…`
   (`2503_19957v1.pdf`, **910 410 o**, mesuré au git en S11). **Toute
   réapparition SE CONFRONTE à elles. Enregistrer n'est pas confronter.**
10. **DÉPOSER AU MIROIR N'AUTORISE PAS À RETIRER DE L'ORIGINAL.**

## §4 — Précédents S9 (et S8) — opposables, reportés intégralement

- Un **défaut du gel se nomme et s'amende par fichier séparé daté**, jamais en
  place ; la pièce amendée reste **byte-intacte** et re-vérifiable après coup.
- Un harnais doit auditer la **vacuité structurelle**, pas seulement muter : un
  assert qu'**aucun porteur mutable ne traverse** est un **faux PASS** même
  s'il est vrai. En S9 cet audit a rendu **quatre faux PASS** sur un lot qui se
  présentait à 38/38 — sans lui, R-11 se serait clos **surévalué**.
- Un **pré-tri `[D]` discriminante / `[C]` consignation AU GEL** interdit de
  reclasser après coup un échec en consignation.
- **L'antériorité se PROUVE par l'état du répertoire** (relever le sha du gel
  quand aucun instrument n'existe encore, listing à l'appui), pas par une
  déclaration.
- Une **cible non algébrisable se déclare telle AU GEL** (clause I-c), sinon
  elle devient une recopie de front-matter déguisée en PASS.
- Un **statut de présence se MESURE sur l'arbre modifié** avant d'écrire la
  note qui le déclare.
- **Annoncé puis GO ⟹ l'annoncé fait foi** ; ce qui n'a pas été arbitré se
  dépose **tel qu'annoncé**, et se corrige ensuite par amendement, jamais en
  silence.
- **PRÉCÉDENT S8**, opérant en S10 et en S11 : **un intrant refourni se
  CONFRONTE au registre AVANT extraction**, puis pièce par pièce.

## §5 — Procédure R-55 de dépôt, et points de vigilance

**R-55 — ordre non négociable :** annonce **chemin + sha256 complet + message
de commit**, **fichier par fichier**, PUIS token, PUIS push. **Si le token est
fourni AVANT l'annonce, l'annonce se fait quand même et l'on attend la
confirmation de l'opérateur.** Puis confrontation des sha déposés aux sha
annoncés **par `diff`, sur clone neuf**.

**Points de vigilance d'environnement**, en complément de ceux déjà portés par
S13 §0-lite :

- `pgrep -f` **s'auto-matche**, et `[p]ython3` ne protège **pas** du shell
  englobant.
- `simplify` **non borné** — ne pas le lancer sans borne.
- `pdfplumber` **0.11.9**, `pdftoppm` / `pdfinfo`, Pillow présents ; `pymupdf`
  **ABSENT**. Sur les mathématiques affichées, `extract_words` est **mensonger**
  — descendre au niveau `chars`.
- **Décomposition du bilan**, pour recompte indépendant :
  `35+17+16+16+12+11+6+21+40+45+16+36 = 271` PASS ;
  `5+5+6+6+8+7+3+10+14+10+8+19 = 101` consignations.
- Un **paquet ZIP de TEXTES extraits ne permet PAS la confrontation octet** ; il
  répond à une autre question (concordance de **contenu**) et il faut le dire.

## §6 — Deux mises à jour de portée, arbitrées le 2026-07-25

Reportées ici parce qu'elles modifient la lecture de précédents recopiés
ci-dessus, et non pour ouvrir quoi que ce soit.

- **G-4 — TRANCHÉ, portée PROSPECTIVE.** Régime bi-espace : le **mount** est
  l'espace vivant (conduite de projet, matériaux en cours, éléments
  intermédiaires d'une branche non finalisée ni épuisée) ; le **git** est
  l'espace de consignation (matériaux validés et vérifiés, résultats confirmés
  et audités, accompagnés du matériel permettant à une instance tierce de
  **reproduire**). La **bascule** mount → git intervient à l'épuisement d'une
  branche, après **audit froid incognito**. **L'existant reste en place.**
  Ceci solde la question ouverte de S13 §8 et transforme la clause `autorite`
  de S13 en règle. **R-54 reste debout.**
- **Périmètre de `S-B1` (chantier β) — ARBITRÉ : les deux ensembles**, soit
  `S8`/`S9`/`S10` (piste article, identités NON attestées) **et** les 4 corps
  intrants du registre de première mesure du 2026-07-24. Aucun espace de
  classement ni de verdict n'est ouvert par cet arbitrage. *(Le paquet β et son
  amendement de périmètre sont MOUNT-SEUL à ce jour et ne sont pas au dépôt.)*

## §7 — Écart constaté le 2026-07-25, et ce qu'il coûte

**HEAD attendu par S13 était faux.** Le `piege_R36` de S13 annonçait
`cad358a` *« tant que S13 n'est pas déposée »*. S13 **a été déposée** (commit
`09d9e2a`), et la note portait donc un attendu périmé sur elle-même. **Aucune
conséquence sur les comptes** — le §0-lite du 2026-07-25 est **conforme sur
toute la ligne** : 34 / 76 / 42 / 215 / 4, `sources/` 4, inventaire 6 LIVE /
76 ARCHIVE / 1 ABSENT, `verif_paquet_propre` sha8 `051e2833` rc=0,
générateur v2.1 sha256 `7d63b9ed…` auto-test 6/6, `harnais_R9` 6/6,
`harnais_R11` 7/7 + 0 vacante. Les 12 redémonstrations **non rejouées** ce
jour (bilan inchangé depuis S9, rejoué CONFORME en S9–S12).

**La leçon, et elle est double.** Une note peut mentir par âge **sur son propre
attendu** ; c'est exactement pourquoi le piège R-36 interdit de vérifier HEAD
par la note. Et la même session a, deux fois, **conclu depuis une note plutôt
que depuis le dépôt** : une fois sur HEAD, une fois en présentant l'écart des
homonymes ZIP du mount comme une découverte bloquante alors qu'il était **déjà
mesuré et consigné** aux commits `3419d49` (S10) et `af97865` (S11). Les deux
sont imputables au pilote.

## §8 — Ce que cet amendement ne fait pas

Il n'arbitre pas la **norme de nommage** (toujours PROPOSITION, `audit/LC-NORME-
NOMMAGE.md`) · ne solde ni **G-1** (16 bundles de la décharge v2.74, 72 `.py` ;
`hors-KB/A/` non fourni — `hors-KB/` ne contient que `B`) ni **G-5b/c**
(`LC-00-INDEX` ABSENT de `kb/`) · ne rouvre pas le **sort de R-23** (MAINTIEN,
corps de F5 non ouvert, `[D5]` LEVÉ / W3 intact) · n'arme aucune gate · ne
mesure pas **P-8** (P-9 le mesure à la prochaine gate, pas ici) · ne dépose
aucune pièce du chantier β.

---

*§6.4 — sentinelle terminale. Recopier des précédents ne les applique pas.
Amender, reporter, déposer, retirer : aucun de ces gestes ne scelle, ne réduit,
ne compte, ne démontre quoi que ce soit. `{ A4 ; A2★ ; N }` INCHANGÉ · D1 non
clos, D1c intacte · N non fixé (≡ Λ, R-53 0/4) · O₂ non construit · β `T-b`,
non résolu, SEUL facteur d'O₂ ouvert · nœud (i) INDÉTERMINÉ (pas A) · Silo R
clos à 12/12 · CCC non démontrée NI réfutée.*
