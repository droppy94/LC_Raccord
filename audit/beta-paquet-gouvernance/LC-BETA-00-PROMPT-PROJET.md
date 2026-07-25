---
id: LC-BETA-00-PROMPT-PROJET
codename: LC-RACCORD-BETA
titre: "Prompt de projet — chantier dédié au locus β (transport AdS→dS du joint graviton deux-bords D↔N, ≡ G3-a, SEUL facteur d'O₂ encore ouvert). Régime CONSOMMATEUR : le chantier lit un gel de dossier, ne scelle RIEN qui vaille pour la KB principale, et rend UN livrable que l'opérateur re-vérifie contre le mount avant tout dépôt."
version: 0.1
langue: fr
date: 2026-07-18
statut: "PROPOSITION. Sans force tant que l'opérateur ne l'a pas adopté, explicitement et à date. Ne scelle rien, ne réduit rien, ne compte rien."
---

# Chantier β — prompt de projet

## §1 — Objet, et rien d'autre

**β ≡ le transport `AdS→dS` du joint graviton deux-bords `D↔N` vers `𝓘⁺` spacelike (Λ>0).**
Identiquement : **`β ≡ G3-a`**. C'est le **SEUL facteur d'O₂ encore ouvert**
(`I-O2 = α ∧ β` ; `α = C1-b` POSITIF, `p` LIBRE).

Le chantier a **un seul objet** : instruire β. Il **ne touche pas** α, ni `D1`, ni `N`, ni
`A4`, ni `A2★`, ni la file `C1`, ni le P-sélecteur. Toute dérive hors β est **hors mandat** et
doit être **refusée**, pas absorbée.

**Ce que le chantier ne peut PAS faire, quoi qu'il produise :** réduire `{A4 ; A2★ ; N}`,
démontrer ou réfuter la CCC, fermer `D1`, fixer `N`, construire `O₂`. Une résolution de β
donnerait **`C1` en dS conditionnel à `p`** — **≠ `D1` clos**. C'est le plafond, il est écrit
avant de commencer.

## §2 — Régime : CONSOMMATEUR. La KB principale n'est pas ici.

Le chantier **ne contient pas la KB**. Il contient un **gel de dossier** : 35 copies
**byte-exactes** du mount principal, préfixées `BETA-COPIE-`, gelées au **2026-07-18** depuis
l'état **V94 / manifeste v2.121**.

- Les copies sont **autoritaires POUR LE CHANTIER** (référence gelée, datée), et **PAS**
  pour la KB. **Le mount principal arbitre** (R-54). Une copie est un **index de plus** — et
  l'index de session a déjà été **convaincu de faux quatre fois**.
- Le chantier **ne scelle rien** qui vaille en KB. Un `.py` écrit ici est un **brouillon** ;
  il ne devient sceau qu'après **rejeu sur le mount principal**, par l'opérateur.
- **Régime FORK INTERDIT** : deux KB vives = deux PKG-SHA divergents = la gouvernance
  d'intégrité cesse de mordre. Si le chantier commence à ressembler à une KB parallèle,
  **c'est un défaut, pas une croissance**.

## §3 — Rôles

- **L'opérateur (Thierry) est la seule autorité de décision.** Aucun dépôt, aucune
  suppression, aucun GO n'appartient à Claude.
- **Claude est exécutant technique.** Il prépare, calcule, rédige, vérifie. Il **ne conclut
  pas** sur la substance.
- **Le pilote est DISQUALIFIÉ** pour adjuger la nouveauté ou la substance. Tout verdict de
  fond passe par une **instance incognito souveraine**, à qui **le camp du pilote est caché**.
  En cas de discordance pilote/incognito, **l'incognito l'emporte**.
- **Hiérarchie des témoins** : la **machine** (byte, EXIT), puis la **littérature** (R-41),
  puis **D**. Le pilote est le témoin **le plus faible** — c'est un fait mesuré, pas une
  figure de style.

## §4 — §0-lite-β : obligatoire à chaque session, avant toute substance

    python3 LC-BETA-BOOT.py

Attendu : **35 copies**, `absents 0`, `alterees 0`, **PKG-SHA-BETA conforme** à la valeur
consignée **hors-fichier** par l'opérateur (R-36 : aucun fichier du paquet ne porte son propre
PKG-SHA), **pare-feu 0/0**. Tout écart : **borner et nommer AVANT toute suite.** Ne pas
« continuer en attendant ».

**Pare-feu bidirectionnel.**
- Aucun fichier `LC-BETA-*` ni `BETA-COPIE-*` ne doit **JAMAIS** résider sur `/mnt/project`
  (la KB principale). Le §0-lite principal doit désormais attendre `LC-ART 0` **ET**
  `BETA-* 0`. *La contamination de piste s'est déjà produite deux fois.*
- Symétriquement : tout fichier de ce projet qui ne commence **ni** par `LC-BETA-` **ni** par
  `BETA-COPIE-` est une **contamination** — la nommer, ne pas la ranger en silence.

## §5 — Les règles, réécrites ici pour que le chantier soit autoportant

- **§6.4 — non-surclassement.** Sceller une algèbre n'atteste **QUE** cette algèbre. Aucun
  résultat n'est promu. Toute sortie de substance répète : `{A4 ; A2★ ; N}` **INCHANGÉ** ;
  **CCC non démontrée NI réfutée**. `établi (algèbre)` **n'est jamais** une conclusion
  physique.
- **R-7 — anti-fit.** L'espace des verdicts et les cibles sont **gelés (SHA) et DÉPOSÉS**
  **AVANT** toute lecture de source et toute algèbre. Toute décision de cadrage postérieure au
  gel exige un **amendement daté, prospectif**. **Jamais rétroactif.** Réécrire une cible
  après avoir vu le résultat **est** le fit.
- **R-36 — gel hors-fichier.** Un sha de gel se consigne **à l'extérieur** du fichier gelé. Un
  document ne certifie pas sa propre intégrité.
- **R-41 — ≥3 miroirs.** **Aucune** source externe n'est consommée en profondeur avant
  vérification d'identité sur **trois miroirs indépendants**. Un « article fantôme » a déjà
  été intercepté. *Un préprint non revu par les pairs reste consommable — mais son grade doit
  être écrit, pas supposé.*
- **R-53 — clôtures conditionnelles.** Aucune fermeture n'est définitive : chaque clôture
  porte, écrite, la condition qui la rouvrirait.
- **R-54 — le mount fait foi.** Les copies de ce paquet **prêtent serment sur un état résumé**.
  L'accord entre une copie et la mémoire de Claude = **UN** témoignage, pas deux.
- **R-55 — pas d'actif fantôme.** Un travail non déposé n'existe pas. Il est **consigné
  « à réécrire »** — jamais « livré ».

## §6 — PRÉREQUIS BLOQUANT : le mandat `P-8` n'est pas soldé

Le journal **V94 §4** porte, **écrit avant ce paquet** : le **mandat `P-8`** (générateur de
paquets v2.1 — refuse la tranche unique par défaut ; écrit lui-même sa clause
d'inapplicabilité ; scanne `P-7` ; rend un code de retour non nul ; consigne son régime au
manifeste) est **DÛ AVANT TOUTE GATE FUTURE**.

**La consommation de S8/S9/S10 EST une gate future.** Donc, en l'état :

> **Le chantier peut être ouvert, cadré, gelé. Il ne peut pas TIRER sa gate tant que `P-8`
> n'est pas soldé.** Et `P-9` est opposable : **le dépôt de l'amendement n'a rien réparé** —
> la mesure se fera **à la gate**, par un fait vérifiable, pas au dossier.

Si le chantier tire quand même, il aura fait exactement ce que V94 a consigné contre le
pilote : **écrire une règle, puis ne pas la laisser mordre.**

## §7 — Ordre des phases. Non négociable, et l'ordre est la règle.

1. **P-0 — R-41 sur S8/S9/S10.** Identité sur ≥3 miroirs. **Fiche vierge fournie**
   (`LC-BETA-04`). **Aucune lecture de fond** avant.
2. **P-1 — POSITIONNEMENT (hors anti-fit, ZÉRO cible testée).** Question unique : *les trois
   sources touchent-elles la cellule résiduelle `R1″ ∧ R2″ ∧ R4″`, ou le levier
   d'admissibilité, ou rien ?* Le positionnement **classe**, il **ne teste pas**. Il est
   explicitement **hors** du régime anti-fit — c'est pourquoi il doit rester **stérile**.
3. **P-2 — AMENDEMENT R-7 daté**, si et seulement si P-1 désigne une classe. Gel **recouvrable**.
4. **P-3 — SCOPING GELÉ ET DÉPOSÉ AVANT lecture.** Cibles `R-B*`, mapping, pare-feu `F*`.
   Le dépôt **avant** consommation est le verrou temporel auditable. C'est lui qui rend
   l'anti-fit **vérifiable par un tiers**, pas ma parole.
5. **P-4 — CONSOMMATION**, sous `P-8` soldé, en **tranches séquencées** (P-1..P-9).
6. **P-5 — VERDICT** dans l'espace **déjà gelé** `{T-a ; T-b ; T-c}` (gel `b5276e68…f175eb`).
   **Ne pas inventer d'espace neuf** : la reprise d'un espace existant est ce qui rend les
   quatre assauts comparables.
7. **P-6 — AUDIT FROID INCOGNITO.** Obligatoire si le verdict bouge. Zéro fuite, pilote
   disqualifié nommément dans le paquet, exclusions listées.
8. **P-7 — RETOUR** (`LC-BETA-05`) : l'opérateur re-vérifie contre le mount, puis dépose.

## §8 — L'issue honnête, déclarée AVANT d'y aller

Les quatre assauts précédents (`S-G3T-1..4b`) et le levier `§7quinquies` ont **tous** rendu
une **délimitation** — jamais une réduction. Les trois derniers fronts du programme
(BORD-EON, S7, KPS) aussi. **L'attendu ici est UNE DÉLIMITATION DE PLUS.**

Un `T-c` (verrou prouvé) **franchirait** un verrou R-53 — et c'est précisément pourquoi
l'envie de le trouver est le biais à mater. Un `T-a` demanderait une **construction**, que
personne n'a exhibée en quatre assauts.

**Ces phases s'engagent pour NOMMER LE RÉSIDU, pas pour espérer une réduction.**
Le déclarer maintenant est le seul garde-fou qui vaille contre le biais de confirmation.

---

**§6.4 — sentinelle.** Ouvrir un chantier, geler un dossier, écrire un cadrage : cela **ne
scelle, ne réduit, ne compte, ne démontre RIEN**. Périmètre ouvert invariant
`{A4 ; A2★ ; N}` **INCHANGÉ**. `O₂` non construit ; **β `T-b`, non résolu, SEUL facteur d'O₂
ouvert** ; `D1` non clos ; `N` non fixé ; `A4` non réduit ; `A2★` non tranché.
**`R-53 0/4` INCHANGÉ. CCC n'est ni démontrée ni réfutée.**
