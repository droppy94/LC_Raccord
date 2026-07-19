---
id: LC-WORK-AMENDEMENT-R7-ANTI-ANCRAGE-SEQUENCE
titre: "Amendement R-7 PROSPECTIF ET DATÉ (γ-2) — anti-ancrage RÉELLEMENT SÉQUENCÉ : la Phase 3 est GELÉE R-36 à l avance et SEUL SON SHA est communiqué AU MOMENT DE LA PHASE 2 ; son TEXTE n est délivré qu APRÈS l issue de Phase 2, et l auditeur VÉRIFIE LUI-MÊME que le sha concorde. USAGE NEUF de la porte 559928c3 — elle scellerait un FUTUR, pas un présent — donc AMENDEMENT PROPRE, jamais un bricolage au fil de l eau. Traite D-a (anti-ancrage DÉCORATIF : Phase 2 avant Phase 3 MATÉRIELLEMENT INEXÉCUTABLE, les deux libellés étant délivrés DANS LE MÊME BLOC, l.50 vs l.65, VÉRIFIÉ AU FICHIER). Clause d honnêteté CENTRALE : en régime one-shot le séquencement est INAPPLICABLE ⟹ il se DÉCLARE INAPPLICABLE, il ne se PRÉTEND PAS tenu. SANS SURCLASSEMENT (§6.4) : séquencer une porte NE SCELLE, NE RÉDUIT, NE COMPTE, NE DÉMONTRE RIEN. {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "amendement R-7 (work-active) — règle d'INSTRUMENT et d'EXPOSITION, usage NEUF d'une porte existante. NE scelle rien, NE vote pas, NE contient AUCUNE algèbre, N'adjuge AUCUNE issue."
statut: "work-active — PROSPECTIF. S'applique à la PROCHAINE adjudication et aux suivantes. JAMAIS rétroactif : aucune passe rendue n'est reclassée, aucun rapport d'auditeur n'est re-jugé, aucun re-audit n'est déclenché. Le précédent CSE-1 / CSE-1-bis reste tel qu'il est, avec son anti-ancrage DÉCORATIF consigné."
version: "0.1"
langue: fr
date: "2026-07-16"
gel_R36: "consigné HORS-FICHIER (R-36 : ce fichier n embarque NI son propre sha, NI aucune valeur qu il produirait)"
prerequis_kb: [LC-WORK-AUDIT-PAQUET-GEL, LC-WORK-AMENDEMENT-R7-CSE-SHA-GATE, LC-WORK-AMENDEMENT-R7-SHA-GATE-FORMAT-NOM, PROMPT-INCOGNITO-AUDIT-FROID-GENERIQUE, LC-WORK-REPRISE-V84-POST-GATE-P-SELECTEUR]
tags: [amendement, R-7, prospectif, date, anti-ancrage, sequencement, usage-neuf, D-a, gamma-2, monotone-sur, inapplicable-one-shot, §6.4]
---

# (γ-2) — anti-ancrage réellement séquencé

## 0. Le défaut, tel qu il a été constaté — et il l a été AU FICHIER

**D-a — l anti-ancrage était DÉCORATIF.** La doctrine prescrivait d exécuter la **Phase 2** *avant* de
lire la **Phase 3**. Or **les deux libellés étaient délivrés DANS LE MÊME BLOC** — l.50 et l.65,
**vérifié au fichier**, pas supposé. **L auditeur avait la Phase 3 sous les yeux pendant la Phase 2.**

> **Une prescription d ordre adressée à quelqu un qui détient déjà la suite N EST PAS UNE CONTRAINTE :
> c est une DEMANDE POLIE.** Elle repose sur la bonne volonté de celui qu elle prétend contraindre.
> **Un contrôle qui n est pas une porte n est pas un contrôle** (leçon V81, inchangée).

Le défaut est **de FORME MATÉRIELLE**, comme D-b : la doctrine **posait l intention** et
**n instrumentait pas** le moyen. Elle **n a pas menti** — elle **n a rien tenu**.

## 1. La prescription — et POURQUOI elle est un usage NEUF

**Le geste** : la **Phase 3 est rédigée À L AVANCE**, **GELÉE R-36**, et **SEUL SON SHA256 est
communiqué AU MOMENT DE LA PHASE 2**. Son **TEXTE n est délivré qu APRÈS** que l auditeur a **rendu**
son issue de Phase 2. **L auditeur recompute alors le sha du texte reçu et le confronte lui-même au
sha pré-communiqué.**

**Ce que cela change, exactement, et rien de plus** :

- **L anti-ancrage devient EXÉCUTABLE** : l auditeur **ne peut pas** lire la Phase 3 pendant la
  Phase 2 — **il ne l a pas**. Le respect de l ordre cesse de dépendre de sa discipline.
- **L anti-fit devient OPPOSABLE AU PILOTE** : le sha pré-communiqué **prouve arithmétiquement** que
  la Phase 3 **n a pas été taillée après avoir vu l issue de Phase 2**. **Le pilote perd la
  possibilité d adapter son mandat au résultat.**
- **La charge est TRANSFÉRÉE** : c est **l auditeur** qui recompute et qui confronte. **Un contrôle
  côté pilote ne protège pas d une faute du pilote** — argument portant de `559928c3`, ici étendu.

**Pourquoi c est un USAGE NEUF, et donc un amendement PROPRE.** La porte `559928c3` atteste des octets
que l auditeur **s apprête à ouvrir** : elle scelle un **PRÉSENT**. Ici elle attesterait des octets
que l auditeur **n a pas encore** et **ne doit pas avoir** : elle scellerait un **FUTUR**. C est un
**engagement**, pas une vérification d intégrité. **Étendre une porte à un usage qu elle n a jamais eu
par un ajustement au fil de l eau serait exactement le bricolage que la discipline interdit** ⟹
**amendement daté, ou rien.**

## 2. Prescriptions — opposables, énumérées, CLOSES

**S-1 — GEL PRÉALABLE.** La Phase 3 est **rédigée et gelée R-36 AVANT expédition du paquet**. Son sha
est consigné **HORS-FICHIER**. Le texte gelé **n est pas joint** au paquet initial.

**S-2 — COMMUNICATION DU SHA AU MOMENT DE LA PHASE 2.** Le sha de la Phase 3 monte **DANS** le bloc
PROMPT, **au format prescrit par (γ-1)** — **un champ par ligne, sha COMPLET, jamais un tableau à
pipes**. Il est accompagné de la mention **explicite** que la pièce **existe**, qu elle est **figée**,
et qu elle **sera délivrée après l issue de Phase 2**. **Rien n est dissimulé quant à son EXISTENCE.**

**S-3 — DÉLIVRANCE APRÈS ISSUE, JAMAIS AVANT.** Le texte de la Phase 3 est délivré **uniquement après**
que l auditeur a **rendu** son issue de Phase 2. **Une issue rendue ne se retire pas, ne se reformule
pas, ne se complète pas** à la lecture de la Phase 3 — elle est **acquise** et **consignée telle
qu elle a été rendue**.

**S-4 — VÉRIFICATION PAR L AUDITEUR, PAS PAR LE PILOTE.** À réception, l auditeur **recompute** le
sha du texte reçu et le **confronte** au sha pré-communiqué. **Écart de sha ⟹ ARRÊT** : le mandat de
Phase 3 est réputé **CONTAMINÉ**, l auditeur **N ADJUGE PAS la Phase 3**, et **l issue de Phase 2
RESTE ACQUISE** (elle a été rendue avant, elle est hors d atteinte). **Issue PLEINEMENT VALORISÉE.**
Conformément à **(γ-1) F-3** : **le sha bloque, le nom se consigne.**

**S-5 — CLAUSE D INAPPLICABILITÉ, ET ELLE EST LE CŒUR DE CET AMENDEMENT.**
Le séquencement **exige un échange en PLUSIEURS TOURS** avec l auditeur. **Si le dispositif est
one-shot** — paquet unique, aucun tour de retour possible — **le séquencement est MATÉRIELLEMENT
INAPPLICABLE**. Dans ce cas :

> **L anti-ancrage se DÉCLARE INAPPLICABLE. Il ne se PRÉTEND PAS tenu.**
> Le paquet **écrit**, en toutes lettres : *anti-ancrage NON instrumenté, Phase 3 délivrée dans le
> même bloc, l ordre de lecture est une DEMANDE et non une CONTRAINTE.*

**Aucune rédaction ne répare le matériel.** Prétendre tenir un anti-ancrage inexécutable **est
exactement D-a**, et le redire après l avoir consigné serait **F5 à l échelle d une doctrine** :
**une déclaration de retenue ne vaut pas la tenir.** **La clause qui suit est donc la seule honnête :
on instrumente, ou on déclare qu on n instrumente pas. On ne décore pas.**

## 3. Grade — tenu, SANS sur-grade

Ce que le séquencement atteste : **que l auditeur n avait pas la Phase 3 pendant la Phase 2**, et
**que la Phase 3 est antérieure à l issue de Phase 2**. **RIEN D AUTRE.**

Ce qu il **N atteste PAS** :

- **Il ne rend pas la Phase 2 non-ancrante.** Si la **Phase 2 elle-même** est rédigée de façon à
  diriger l auditeur, le séquencement **n y touche pas**. C est **Δ-3**, et **Δ-3 SURVIT À TOUTES LES
  ISSUES** — **`b6` TIENT**. Cet amendement **ne le répare pas** ; c est **(γ-3)**.
- **Il ne dé-lit pas.** Si le pilote colle la Phase 3 malgré tout, la porte devient un **détecteur
  POST-exposition** et **rien de plus**. **La porte NE PEUT PAS DÉ-LIRE** — grade de `559928c3`,
  reconduit tel quel, jamais élargi.
- **Il ne prouve pas l antériorité au sens cryptographique fort.** Le sha est communiqué **par le
  pilote** dans un canal qu il contrôle. Ce qu il **ferme**, c est l adaptation **après l issue** —
  ce qu il **ne ferme pas**, c est la rédaction **avant** le paquet, où le pilote est **libre**.
  **Limitation STRUCTURELLE, consignée, non escamotée** (précédent : *antériorité non prouvable
  cryptographiquement*, constat 4/4 d un audit antérieur).

## 4. Test de direction — MONOTONE-SÛR, et il joue CONTRE LE PILOTE

- **N ajoute AUCUN prior, n en retire AUCUN.** Ne peut **PAS** changer un verdict — seulement
  **empêcher qu un mandat soit taillé sur une issue déjà connue**.
- **Direction, sans ambiguïté** : le pilote **perd** le droit d écrire sa Phase 3 après coup, **perd**
  la latitude de format (par renvoi à (γ-1)), et **gagne** une obligation de délivrance en deux temps.
  **L auditeur gagne** l instrument de contrôle. **Rien dans cet amendement ne sert le pilote.**
- **Coût : RÉEL, NON NUL — et il se déclare.** Contrairement à `559928c3` dont le coût de blinding
  était **nul**, le séquencement **coûte un tour d échange** et **exige un canal multi-tours**.
  **Prétendre que c est gratuit serait le sur-grade suivant.** C est précisément **pourquoi S-5
  existe**.
- **Zéro-fuite** : un `sha256` est **à sens unique**. Le sha d une Phase 3 **ne dit rien** de son
  contenu. Ce qui est exposé — **qu elle existe et qu elle est figée** — est **ce qu on veut exposer**.

## 5. Anti-fit — R-7 tenu, argumenté

- **PROSPECTIF ET DATÉ**, écrit le **2026-07-16**, **AVANT TOUT GESTE DE SUBSTANCE**. L écrire
  **après** un verdict de fond serait **RÉTROACTIF**.
- **NON FITTABLE À L ISSUE PENDANTE.** L adjudication pendante est `2f2f9c08` (fork P-SELECTEUR).
  Cet amendement porte sur la **séquence de délivrance d un paquet** : **NI** son mapping, **NI** ses
  discriminants, **NI** ses firewalls, **NI** ses bornes. **`2f2f9c08` INTACT.** Aucune issue
  `{P-1 ; P-2 ; P-3}` n en dépend, dans aucun sens.
- **Ne réhabilite RIEN.** `G-2 BIAISÉ` et `S-2` sont **les FAITS des souverains**. **Le modus ponens
  n appartient pas au pilote.** **`b1` TIENT.**
- **Ne reclasse aucune passe.** Le précédent CSE-1 / CSE-1-bis **reste tel qu il est**, **avec son
  anti-ancrage DÉCORATIF CONSIGNÉ**. Réparer prospectivement **n efface pas** le défaut passé — **il
  reste au dossier, contre le pilote**.

## 6. Bornes CLOSES — b1 à b6

- **b1** — Ferme **exactement** la classe **D-a** : *la Phase 3 lue pendant la Phase 2, et la Phase 3
  écrite après l issue de Phase 2*. **RIEN de plus.**
- **b2** — **Ne dit RIEN d une Phase 2 qui ancre par sa PROPRE rédaction.** C est **Δ-3** ⟹ **(γ-3)**.
  **`b6` TIENT : Δ-3 survit à toutes les issues.**
- **b3** — **NE RÉPARE PAS D-d** (frontière S-2/S-3). **RÉSERVE PRÉ-DÉCLARÉE, CONTRE LE PILOTE :
  D-d N EST PAS ÉCRIVABLE PAR LE PILOTE** — tout tracé déplace les cotes et **il a un intérêt** ⟹
  **SOUVERAIN** (précédent NOTE-07) **OU dissolution de la frontière** (retirer une frontière qu on a
  intérêt à tracer est **monotone-sûr** ; en tracer une **ne l est pas**).
- **b4** — **Ne dit RIEN d un paquet MAL SCOPÉ.** **Le SCAN DE BLINDING reste DÛ et INCHANGÉ.** Les
  bornes b1-b5 de `559928c3` sont **reconduites telles qu écrites** ; **la porte n est PAS retirée**,
  et **elle n est PAS élargie** — elle reçoit un **second usage, nommé et borné**.
- **b5** — **`559928c3` INTACT, NON re-gelé, NON rectifié.** Cet amendement est un **successeur DATÉ
  et POSTÉRIEUR**. Idem `bd495c65` (γ-1), **cité et appliqué**, **non re-gelé**.
- **b6** — **N ouvre, NE ferme, NE tranche AUCUNE issue** `{P-1 ; P-2 ; P-3}` ni `{S-1 ; S-2 ; S-3}`.

## 7. Contrôle de conformité de CE fichier (déclaration, à VÉRIFIER)

Le pilote **déclare** : **0 occurrence de son propre sha** (R-36, scan **court ET complet**) ; **0
caractère pipe** ; **0 valeur projetée** ; **0 sha abrégé dans une prescription** — les renvois
`559928c3` et `bd495c65` sont des **renvois EN PROSE vers des gels existants**, **expressément
licites** par **(γ-1) F-2**. **C est une DÉCLARATION, PAS un fait : VÉRIFIE-LA.** **Le pilote qui
écrit le scan est le pilote qui a INTÉRÊT à ce qu il passe.** Le firewall se vérifie **PAR LS SUR LE
MOUNT**, jamais par grep dans un fichier — **hors-scope ici, donc SANS ATTENDU** : *un scan qu on
déclare hors-scope n a pas d attendu.*

## 8. Non-surclassement (§6.4)

Séquencer une délivrance / geler un futur / transférer une charge de contrôle **NE SCELLE, NE RÉDUIT,
NE COMPTE, NE DÉMONTRE RIEN**. Une porte de conformité **n atteste que LES OCTETS ANNONCÉS**, jamais
une conclusion physique ; **un sha conforme n atteste que l identité des octets, PAS un EXIT 0**.
Un anti-ancrage **instrumenté** n atteste que **l ordre de lecture** — **PAS** que le paquet est
honnête. **`BIAISÉ` n est PAS « P-2 est faux » ; `S-2` n est PAS « P-2 est vrai » ni « le cadrage est
sauvé ».** Le pivot O₂ reste **CLOS NÉGATIF**. Les têtes scellées restent l **AUTORITÉ**, **INTACTES**.

`{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; N non fixé (≡Λ, terminus ouvert — voie A close, clôture
R-53 conditionnelle **0/4 INCHANGÉE**) ; O₂ **NON construit** ; β **NON résolu** ; voie H ∉ périmètre ;
A4 route par-𝓘⁺ délimitée (W2), postulat renforcé, **NON réfuté** ; A2★ parqué pending OA ;
**CCC non démontrée NI réfutée**.
