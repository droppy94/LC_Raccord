---
id: LC-WORK-AMENDEMENT-R7-SHA-GATE-FORMAT-NOM
titre: "Amendement R-7 PROSPECTIF ET DATÉ (γ-1) — sha-gate : FORMAT de la table (un champ par ligne, JAMAIS un tableau à pipes) + règle NOM vs SHA (LE SHA BLOQUE, LE NOM SE CONSIGNE). Successeur DATÉ ET POSTÉRIEUR de la porte 559928c3, qui reste INTACTE et NON re-gelée : ses bornes b1-b5 sont VALIDÉES PAR LE FAIT, seul son FORMAT est amendé. Traite D-b (défaut de PORTE) et D-c (nom canon NON TENU PAR LE PILOTE), consignés contre le pilote en session V84. Écrit AVANT tout geste de substance ; les écrire APRÈS un verdict de fond serait RÉTROACTIF. SANS SURCLASSEMENT (§6.4) : amender un format de porte NE SCELLE, NE RÉDUIT, NE COMPTE, NE DÉMONTRE RIEN. {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 (work-active) — règle d'INSTRUMENT et d'EXPOSITION. NE scelle rien, NE vote pas, NE contient AUCUNE algèbre, N'adjuge AUCUNE issue."
statut: "work-active — PROSPECTIF. S'applique à la PROCHAINE adjudication et aux suivantes. JAMAIS rétroactif : aucune passe rendue n'est reclassée, aucun paquet expédié n'est re-jugé, aucun re-audit n'est déclenché."
version: "0.1"
langue: fr
date: "2026-07-16"
gel_R36: "consigné HORS-FICHIER (R-36 : ce fichier n embarque NI son propre sha, NI aucune valeur qu il produirait)"
prerequis_kb: [LC-WORK-AUDIT-PAQUET-GEL, LC-WORK-AMENDEMENT-R7-CSE-SHA-GATE, PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE, LC-WORK-REPRISE-V84-POST-GATE-P-SELECTEUR]
tags: [amendement, R-7, prospectif, date, sha-gate, format, nom-vs-sha, D-b, D-c, gamma-1, monotone-sur, §6.4]
---

# (γ-1) — sha-gate : FORMAT + NOM vs SHA

## 0. Ce que cet amendement EST, et ce qu il N EST PAS

**EST** : une règle de **FORME** opposable au **pilote** qui monte un paquet, et une règle d **ARRÊT**
opposable à l **auditeur** qui le reçoit.

**N EST PAS** : un re-gel de `559928c3` ; une extension de sa portée ; une réparation de **D-d** ; un
déplacement de `G-2 BIAISÉ` ou de `S-2` ; une issue `{P-1 ; P-2 ; P-3}`.

> **`559928c3` INTACT, NON re-gelé, NON rectifié.** Cet amendement est un **successeur DATÉ et
> POSTÉRIEUR**, jamais une retouche. **La porte n est PAS retirée** — elle a été **FRANCHIE ×2** en
> Phase 0 et **ses bornes b1-b5 sont VALIDÉES PAR LE FAIT** : elle ferme **exactement** la classe V80
> (les mauvais octets expédiés), et le **défaut de cadrage est passé au travers — comme elles
> l annonçaient**. Une porte qui prétendrait couvrir les deux serait **le sur-grade suivant.**

## 1. Motif — DEUX défauts consignés CONTRE LE PILOTE, non réparés au fil de l eau (piège R-7)

**D-b — défaut de PORTE, niveau doctrine.** La table de gate était **BIEN FORMÉE AU FICHIER** mais
**FUSIONNÉE AU TRANSPORT** (tableau à pipes ⟹ collage ⟹ rendu illisible). **Une gate d ARRÊT dont le
format induit un FAUX ARRÊT est un défaut de gate.** `559928c3` a prescrit que la table monte **DANS**
le bloc PROMPT — elle **n a JAMAIS spécifié un format RÉSISTANT AU COLLAGE**. Le trou est dans la
**forme**, pas dans l intention.

**D-c — nom canon NON TENU PAR LE PILOTE.** L obligation §B-2 du harnais a été **VIOLÉE PAR LE
PILOTE** à l expédition. **L auditeur POUVAIT s arrêter ; il a jugé que le sha du fichier ENTIER
prouve l identité et que l étiquette du conteneur ne l infirme pas.** **Décision SOUVERAINE, ET ELLE
EST JUSTE.** Le pilote **CONSIGNE, il NE RE-JUGE PAS.** Le correctif est donc **prospectif** et il
**entérine l auditeur**, il ne le corrige pas.

**Fait porteur, re-vérifiable par quiconque** : un `sha256` du **fichier entier** est une preuve
**arithmétique** d identité des octets. **L étiquette du conteneur n est pas dans les octets hachés.**
Bloquer sur le **nom** produirait un **FAUX ARRÊT sur un paquet dont les octets sont EXACTS** — soit
exactement le défaut de D-b, déplacé d un cran.

## 2. Prescriptions — opposables, énumérées, CLOSES

**F-1 — FORMAT DE LA TABLE : UN CHAMP PAR LIGNE. JAMAIS un tableau à pipes.**
Le bloc de conformité monte **DANS** le bloc PROMPT (prescription `559928c3`, **inchangée**) sous la
**SEULE** forme suivante, un bloc par pièce, blocs séparés par une ligne vide :

```
PIECE   <nom canon de la piece>
SHA256  <64 caracteres hexadecimaux, COMPLETS>
OCTETS  <taille en octets>
```

**INTERDITS, sans exception** : le caractère pipe ; tout alignement de colonnes ; toute table markdown ;
tout renvoi vers une annexe ; toute abréviation de sha. **Motif** : chacun de ces procédés est
**détruit ou fusionné par le collage** — c est la cause matérielle de D-b, constatée sur pièce.

**F-2 — SHA COMPLETS, RECOMPUTÉS EN SESSION D ENVOI.**
64 hex, jamais tronqués **dans la gate**. Recomputés **dans la session qui expédie**, jamais hérités
d une session antérieure (**le reset conteneur est la NORME** ; **aucune valeur ne s hérite**, leçon
V62). L abréviation reste licite **hors gate**, en prose de consignation.

**F-3 — NOM vs SHA : LE SHA BLOQUE, LE NOM SE CONSIGNE.**
- **Un écart de SHA est BLOQUANT** : l auditeur **ARRÊTE**, **N ADJUGE PAS**, le paquet est réputé
  **CONTAMINÉ**. Issue **PLEINEMENT VALORISÉE**, au même titre qu une infirmation.
- **Un écart de NOM est CONSIGNABLE, NON bloquant** : si **tous** les sha concordent, l auditeur
  **poursuit** et **consigne l écart de nom au rapport**. Il **peut** s arrêter — sa souveraineté
  n est pas entamée — mais **il n y est pas tenu**, et **poursuivre est une décision juste**.
- **L obligation de nom canon reste opposable AU PILOTE.** Elle passe de **jambe d arrêt** à
  **obligation dont le manquement se consigne CONTRE LE PILOTE**. Le pilote ne gagne rien : il perd
  une excuse.

**F-4 — HACHE D ABORD, OUVRE ENSUITE.**
Régime A **OBLIGATOIRE** (prescription `559928c3` / doctrine v0.3, **CITÉE, NON re-gelée**) :
l auditeur recompute et confronte **AVANT** ouverture. **Rappel de grade, sans sur-grade : la porte
NE PEUT PAS DÉ-LIRE.** En régime B elle n est qu un **détecteur POST-exposition**.

## 3. Test de direction — MONOTONE-SÛR, et il joue CONTRE LE PILOTE

- **N ajoute AUCUN prior, n en retire AUCUN.** Ne peut **PAS** changer un verdict — seulement
  **empêcher qu un verdict soit rendu sur un paquet faux**, et **empêcher qu un paquet exact soit
  refusé sur une étiquette**.
- **Zéro-fuite** : un `sha256` est **à sens unique** ; les noms de la table sont ceux des pièces
  **JOINTES**, donc **déjà exposés**. **Coût de blinding NUL.**
- **Direction** : F-1 et F-2 **retirent au pilote toute latitude de format** ; F-3 **maintient
  l obligation de nom contre lui** tout en **retirant la jambe d arrêt qui l aurait protégé d un
  paquet exact mal étiqueté**. **Aucune des trois ne sert le pilote.**

## 4. Anti-fit — R-7 tenu, argumenté, non déclaré

- **PROSPECTIF ET DATÉ.** Écrit le **2026-07-16**, **APRÈS** les deux issues souveraines rendues,
  **AVANT TOUT GESTE DE SUBSTANCE**. Les écrire **après** un verdict de fond serait **RÉTROACTIF** —
  c est précisément ce que la dette (γ) interdit.
- **NON FITTABLE À L ISSUE PENDANTE.** L adjudication pendante est `2f2f9c08` (fork P-SELECTEUR,
  espace `{P-1 ; P-2 ; P-3}`). Cet amendement ne touche **NI** son mapping, **NI** ses discriminants,
  **NI** ses firewalls, **NI** ses bornes : il porte sur le **transport d octets d un paquet**.
  **`2f2f9c08` INTACT.** Aucune issue n en dépend, dans aucun sens.
- **Ne réhabilite rien.** `G-2 BIAISÉ` et `S-2` sont **les FAITS des souverains**. **Le modus ponens
  n appartient pas au pilote** : un constat d instrument souverain **n est déplacé que par un
  souverain**. **`b1` TIENT. `b6` TIENT** — **Δ-3 survit à toutes les issues**, et **cet amendement ne
  le répare PAS.**
- **F5, à l échelle de ce fichier.** *Une déclaration de retenue ne vaut pas la tenir.* Ce document
  **déclare** ne pas réparer D-d et Δ-3 — **et ne les répare pas**. Le scan de §5 le vérifie plutôt
  que de l affirmer.

## 5. Bornes CLOSES — b1 à b6

- **b1** — Ferme **exactement** la classe **D-b ∪ D-c** : *les octets exacts rendus illisibles par le
  transport* et *l étiquette qui contredit des octets exacts*. **RIEN de plus.**
- **b2** — **Ne dit RIEN d un paquet correctement assemblé mais MAL SCOPÉ.** ⟹ **le SCAN DE BLINDING
  reste DÛ et INCHANGÉ.** Les bornes b1-b5 de `559928c3` sont **reconduites telles qu écrites**.
- **b3** — **NE RÉPARE PAS D-d** (frontière S-2/S-3, mapping NON EXCLUSIF, 2e occurrence de la classe
  Δ1). **RÉSERVE PRÉ-DÉCLARÉE, CONTRE LE PILOTE : D-d N EST PAS ÉCRIVABLE PAR LE PILOTE** — tout tracé
  déplace les cotes et **il a un intérêt**. ⟹ **SOUVERAIN** (précédent NOTE-07 : la réparation fut
  **PROPOSÉE PAR LE SOUVERAIN**) **OU dissolution de la frontière** (retirer une frontière qu on a
  intérêt à tracer est **monotone-sûr** ; en tracer une **ne l est pas**).
- **b4** — **NE RÉPARE PAS Δ-3** (le paratonnerre). C est l objet de **(γ-3)**.
- **b5** — **NE SÉQUENCE PAS l anti-ancrage.** C est l objet de **(γ-2)** — **usage NEUF** de
  `559928c3` (la porte scellerait un **FUTUR**, pas un présent) ⟹ **amendement propre**, jamais un
  bricolage au fil de l eau.
- **b6** — **N ouvre, NE ferme, NE tranche AUCUNE issue** `{P-1 ; P-2 ; P-3}` ni `{S-1 ; S-2 ; S-3}`.

## 6. Contrôle de conformité de CE fichier (déclaration, à VÉRIFIER)

Le pilote **déclare** : **0 occurrence de son propre sha** (R-36, scan court **ET** complet) ; **0
tableau à pipes dans le bloc prescrit** ; **0 sha abrégé dans une prescription** ; **0 valeur
projetée**. **C est une DÉCLARATION, PAS un fait : VÉRIFIE-LA.** **Le pilote qui écrit le scan est le
pilote qui a INTÉRÊT à ce qu il passe** ⟹ le scan lui-même est **une pièce à charge potentielle**.
Le **firewall** se vérifie **PAR LS SUR LE MOUNT**, jamais par grep dans un fichier — **hors-scope
ici, donc SANS ATTENDU** : *un scan qu on déclare hors-scope n a pas d attendu.*

## 7. Non-surclassement (§6.4)

Amender un **format** de porte / entériner une décision d auditeur / consigner une obligation contre
soi **NE SCELLE, NE RÉDUIT, NE COMPTE, NE DÉMONTRE RIEN**. Une porte de conformité **n atteste que LES
OCTETS ANNONCÉS**, jamais une conclusion physique ; **un sha conforme n atteste que l identité des
octets, PAS un EXIT 0**. **`BIAISÉ` n est PAS « P-2 est faux » ; `S-2` n est PAS « P-2 est vrai » ni
« le cadrage est sauvé ».** Le pivot O₂ reste **CLOS NÉGATIF**. Les têtes scellées restent
l **AUTORITÉ**, **INTACTES**.

`{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; N non fixé (≡Λ, terminus ouvert — voie A close, clôture
R-53 conditionnelle **0/4 INCHANGÉE**) ; O₂ **NON construit** ; β **NON résolu** ; voie H ∉ périmètre ;
A4 route par-𝓘⁺ délimitée (W2), postulat renforcé, **NON réfuté** ; A2★ parqué pending OA ;
**CCC non démontrée NI réfutée**.
