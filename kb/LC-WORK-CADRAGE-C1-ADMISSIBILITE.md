---
id: LC-WORK-CADRAGE-C1-ADMISSIBILITE
titre: "CADRAGE GELÉ R-36 — critère C1 d'admissibilité (FIREWALL anti-circularité, phase P3). Opérationnalise le critère figé C1 du cadrage-bascule (LC-WORK-CADRAGE-BASCULE-N-LAMBDA, 1fb1e26c, INTACT) en PORTE D'ADMISSIBILITÉ EN AMONT : un candidat externe N=f(intrants) ne franchit la porte qu'après un audit C1 EN AVEUGLE — AVANT tout gel de cible R-7, AVANT fetch de prédiction, AVANT toute algèbre. Ne REDÉFINIT PAS C1/C2/C3 ni la trichotomie I-a/I-b/I-c (cités, non recomputés). Grave la PROCÉDURE (graphe de dépendance symbolique mécanisable + règle d'admissibilité + protocole de blinding + ordre (b)-sûr). Conçu V34 §7 (gravé tel quel). PAPER-FIRST : ZÉRO algèbre / ZÉRO fetch / ZÉRO sceau neuf. SANS SURCLASSEMENT (§6.4) : graver un firewall ne scelle/réduit/compte/démontre rien ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé (≡Λ, terminus ouvert) ; A4 non réduit ; A2★ non tranché ; CCC non démontrée NI réfutée."
codename: LC-RACCORD
type: "cadrage gelé R-36 (work-active) — porte d'admissibilité amont. NE scelle rien, NE vote pas la substance, ZÉRO algèbre, ZÉRO fetch de prédiction."
statut: "cadrage RÉDIGÉ — candidat au gel R-36 (sha + horodatage de gel à consigner HORS-FICHIER au dépôt). Phase P3 de la séquence P1→P2→P3→(b) : P1 clos (balayage R-53, v2.10) ; P2 exécutée (LC-SYNTHESE-SOCLES-4 déposée, v2.12, audit froid = CONFIRMATION) ; P3 = ce cadrage. Le cadrage-bascule R-36 1fb1e26c… est INTACT et NON modifié (porte les critères figés C1/C2/C3 + trichotomie ; ce fichier ne touche QUE la procédure d'opération de C1). Dépôt = swap net-zéro (KB au plafond) ; à valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-01
prerequis_kb: [LC-WORK-CADRAGE-BASCULE-N-LAMBDA, LC-E-N-CROSSCHECK, LC-WORK-POSITIONNEMENT-NLAMBDA-SURVEY-EXT, LC-D-IRREDUCTIBILITE-MOYENS, LC-WORK-AUDIT-R53-PRE-BASCULE, LC-WORK-REPRISE-V34-POST-P1-PRE-P2, LC-SYNTHESE-SOCLES-4]
tags: [cadrage, gel-R-36, P3, critere-C1, admissibilite, firewall, anti-circularite, audit-aveugle, zone-verdict, graphe-dependance, mecanisable, trichotomie, I-a, I-b, I-c, collapse-N-S_dS, CSK-theta-vacua, dS-CFT, swampland-w, relier-vs-ancrer, ordre-b-sur, R-7-anti-fit, R-53, incognito-souverain, §6.4, non-surclassement]
---

# Cadrage gelé R-36 — critère C1 d'admissibilité (firewall anti-circularité, P3)

> **Paper-first.** ZÉRO algèbre / ZÉRO fetch / ZÉRO sceau. Ce cadrage **opère** C1 ; il ne le redéfinit
> pas. Les critères **C1/C2/C3** et la trichotomie **I-a/I-b/I-c** sont **figés** dans
> `LC-WORK-CADRAGE-BASCULE-N-LAMBDA` (`1fb1e26c…`, **INTACT**) — cités ci-dessous, **non recomputés**.
> **R-36** : geler le **sha de CE fichier** (+ horodatage) **hors-fichier** au dépôt. **§6.4** : graver
> un firewall ne scelle/réduit/compte/démontre rien ; `{A4 ; A2★ ; N}` **INCHANGÉ**.

## 0. Objet — pourquoi une porte AVANT la porte

La séquence pré-bascule est `P1→P2→P3→(b)`. P1 (balayage R-53) **clos** ; P2 (terminus interne
`LC-SYNTHESE-SOCLES-4`) **exécutée**, audit froid = CONFIRMATION. **P3 = ce cadrage** : rendre la
bascule `(b)` *sûre* en interposant, **en amont** de tout engagement coûteux, une porte qui élimine la
seule pathologie capable de transformer un faux succès en « rattachement » apparent — la
**circularité `N≡S_dS`** (et plus généralement toute réinjection des acquis LC).

Motivation directe : les **2 drapeaux** de P1 (`LC-WORK-AUDIT-R53-PRE-BASCULE`, §5 de V34) sont
**exactement** ce que C1 doit cribler — ce ne sont pas des dettes, ce sont les intrants à passer au
firewall (cf. §5 ci-dessous). Sans C1-amont, un candidat `∝S_dS` (CSK `θ=4π·S_dS`, dS/CFT `c∝ℓ/G`)
*relie* `N` à `Λ` **sans l'ancrer** et **paraît** fixer `N` — alors qu'il retombe sur `N≡S_dS`
(garde-fou hérité `LC-E-N-CROSSCHECK`).

## 1. Position de la porte dans le pipeline (ordre (b)-sûr, figé)

C1 est une **porte d'admissibilité EN AMONT**. Un candidat externe `N=f(intrants)` ne la franchit
**qu'après** verdict C1 :

```
positionnement (clos : SURVEY-NLAMBDA)
        │
        ▼
[C1 — admissibilité, EN AVEUGLE, 0 cible gelée, 0 fetch de prédiction, 0 algèbre]
        │   PASS uniquement
        ▼
gel R-7 des cibles (sha figé)  →  Phase-1 écrite + sceau EXIT 0  →  fetch  →  algèbre
        │
        ▼
audit froid final (incognito souverain)
```

**Invariant** : aucun gel R-7 de cible, aucun fetch de prédiction, aucune algèbre n'est engagé tant que
C1 n'a pas rendu PASS. Le gros du travail ne se déclenche **que** sur un PASS — C1 reste **léger**.

## 2. C1 opéré — la question unique (zone-verdict firewallée)

L'instance qui juge C1 répond à **une seule** question, et **rien d'autre** :

> **Q_C1** — « La chaîne d'intrants qui fixe `N` est-elle **libre de `S_dS`** et **libre de `N`** (et de
> toute relation interne LC) ? »

C'est l'expression opératoire du critère figé **C1 — anti-circularité** (cadrage-bascule §4.2 :
*« l'intrant ne présuppose NI `N≡S_dS` NI aucune relation interne LC ; sa détermination de `N` est
traçable à un cadre externe indépendant, sans réinjection des acquis LC »*).

## 3. Blinding — ce que l'auditeur C1 NE voit PAS

Audit C1 **EN AVEUGLE** : l'instance qui juge C1 n'a **aucun** accès à la toile interne scellée —
explicitement **interdits dans son paquet** : `A_T·N=16`, le facteur `16/N`, la chaîne d'amplitude D1
(`A_T`, 3-pt `64π⁴/N²`, 4-pt `∝N⁻³`), les relations CT. Raison : ces quantités sont précisément ce
qu'un candidat circulaire **réinjecterait** ; les exposer permettrait de « voir la cible » et de
rationaliser un rattachement. L'auditeur ne reçoit que la **chaîne de dépendance externe** du candidat
(intrants → `N`) et la définition de Q_C1.

**Firewall de zone-verdict** (leçon d'audit froid) : le paquet remis à l'auditeur C1 **ne nomme jamais
le verdict attendu** ni ne contient de zone-opérateur l'annonçant (blinding rompu sinon). **Incognito
souverain** : en discordance pilote↔incognito, l'incognito prévaut.

## 4. Règle d'admissibilité — mécanisable (graphe de dépendance symbolique)

Tracer le **graphe de dépendance symbolique** de `N = f(intrants)` (nœuds = quantités ; arêtes = « est
déterminé par »). Décision, **mutuellement exclusive**, alignée sur la trichotomie figée (cadrage-bascule
§4.3) :

- **INADMISSIBLE → I-b** si **au moins un** intrant porteur est :
  - (i) `≡` ou `∝ S_dS` ;
  - (ii) une **fonction de `N`** (ou d'une relation interne LC) ;
  - (iii) **calibré / back-fitté** sur le `Λ` observé.
  Et **rejeter tout cycle** `N → … → N` ou `S_dS → … → N` dans le graphe.
  *(C'est la détermination circulaire `N≡S_dS` cartographiée par `LC-E-N-CROSSCHECK` ; un rattachement
  qui la réinjecte est **nul**, pas un succès.)*

- **CONDITIONNEL → I-c** (et **non** I-a) si le **fixeur porteur** est une **conjecture non acquittée**
  (dS/CFT non-unitaire, point-fixe UV / asymptotic safety, géométrie holographique émergente, état CSK).
  Exiger un **ancrage indépendant** ⟹ **distinction décisive** :
  > **relier ≠ ancrer.** *Relier* `N` à `Λ` (dS/CFT `c∝ℓ/G` ; CSK `θ=4π·S_dS`) **n'est pas** *ancrer*
  > `N` à une valeur déterminée indépendamment de `S_dS`/`N`. Les candidats qui *relient* sont
  > **I-c-conditionnel au mieux** — falsifiabilité *gated* par la conjecture, clôture **R-53
  > conditionnelle**.

- **ADMISSIBLE (candidat I-a) → passe la porte** si la chaîne d'intrants fixe `N` **sans** (i)/(ii)/(iii),
  **sans** cycle, et **sans** dépendance à une conjecture non acquittée — c.-à-d. ancrage externe
  indépendant traçable. **PASS C1 n'est PAS I-a acquis** : C1 ne franchit que l'anti-circularité ;
  C2 (fixation chiffrée) et C3 (falsifiabilité) restent à établir **en aval**, sous R-7 (gel des cibles),
  Phase-1 + sceau, fetch, algèbre, audit froid final. I-a n'est prononcé qu'après `C1∧C2∧C3`.

**Coût** : C1 est léger (graphe symbolique ; pas d'algèbre lourde, pas de fetch de prédiction). Le coût
substantiel ne s'engage qu'après PASS.

## 5. Passage des 2 drapeaux de P1 au firewall (intrants, non dettes)

Application de la règle §4 aux drapeaux gravés (`LC-WORK-AUDIT-R53-PRE-BASCULE` ; V34 §5) :

1. **Collapse `N≡S_dS`** — candidats `∝S_dS` : **CSK/θ-vacua** (`θ=4π·S_dS`, Alexander-Bernardo-Hui
   PRL 2026) et **dS/CFT** (`c∝ℓ/G`). Au graphe : ils **relient** `N`↔`Λ` via `S_dS` ⟹ critère §4(i)
   (et « relier ≠ ancrer ») ⟹ **INADMISSIBLE→I-b** (s'ils n'apportent qu'une relation `∝S_dS`) ou
   **I-c** au mieux (s'ils livrent un nombre sous conjecture non acquittée, sans ancrage indépendant).
   **À cribler AVANT toute algèbre** sur ces candidats — conforme au verdict du survey
   (`SURVEY-NLAMBDA` : I-c-au-mieux / I-b-dominant, **aucun I-a** au 2026-06).
2. **Prémisse `w≠−1`** (swampland / TCC, énergie noire **dynamique**) : n'est pas un *fixeur* de `N` ;
   c'est une **interrogation de la prémisse** de la voie A (`N≡Λ` constant). Elle ne « passe » pas C1
   en tant que candidat — elle est **consignée** (terminus P2) et **gardée en vue** pour `(b)` ; elle
   peut *invalider la prémisse* sans fournir d'intrant admissible. *(Risque amont noté : tension DESI
   DR2 2025 sur `Λ` constant — ne touche pas l'algèbre ; relève de la prémisse, pas de C1.)*

## 6. Garde-fous (report intégral)

- **§6.4 non-surclassement** : graver/opérer un firewall ne scelle/réduit/compte rien ; `{A4 ; A2★ ; N}`
  ne bouge que par dérivation → audit froid → sceau. C1 **élimine** des candidats ; il n'en **valide**
  aucun comme réduction.
- **R-7 anti-fit** : C1 est **EN AMONT** du gel R-7 ; aucun gel de cible, aucun fetch de prédiction,
  aucune algèbre avant PASS. Toute décision de scoping post-gel = **amendement daté**.
- **R-36** : geler le **sha de ce cadrage** (+ horodatage) **hors-fichier** au dépôt ; recouvrable ;
  le cadrage-bascule `1fb1e26c…` reste **intact et distinct** (il porte les critères ; ce fichier porte
  la procédure).
- **R-53** : toute issue (notamment I-c) est conditionnelle / recouvrable ; un ordre supérieur ou une
  conjecture acquittée la rouvre (I-c → réévaluation possible).
- **Audit froid / blinding** : pilote disqualifié pour la substance ; instance incognito **séparée**
  (conversation distincte) ; paquet **sans zone-verdict** ; **incognito souverain**.
- **Net-zéro/net-négatif** : KB au plafond ; dépôt = **swap** ; ne jamais droper un porteur référencé/vif
  (orphan-guard : scan exhaustif des réf entrantes sur mount AVANT retrait).
- **Claude ne modifie jamais la KB** : travail en `/home/claude/work/`, livraison via `present_files`,
  calcul du PKG-SHA (lecture mount) ; **Thierry** exécute le delete-then-deposit et valide chaque fichier.

## 7. Non-surclassement (§6.4)

Ce cadrage **n'établit rien** : il grave la **procédure** d'admissibilité C1 (porte amont aveugle,
graphe mécanisable, ordre (b)-sûr) et range les 2 drapeaux comme intrants à cribler. Aucun sceau, aucun
compte, aucune réduction, **aucune algèbre, aucun fetch de prédiction, aucun candidat validé**.
`{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; `N` non fixé (≡`Λ`, terminus ouvert) ; A4 non réduit ;
A2★ non tranché ; **CCC non démontrée NI réfutée**.
