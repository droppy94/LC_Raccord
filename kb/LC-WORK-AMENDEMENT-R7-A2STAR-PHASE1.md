---
id: LC-WORK-AMENDEMENT-R7-A2STAR-PHASE1
codename: LC-RACCORD
titre: "AMENDEMENT R-7 DATÉ — armement de la Phase 1 du programme externe A2★ (#1, spikes), ciblé sur la SEULE maille non scellée : détermination du taux de réplication ρ dans la DYNAMIQUE GÉNÉRIQUE 3D (GR classique inhomogène sans symétrie près du bang, régime BKL + spikes). NE re-gèle PAS l'espace-verdict {V1/V2/V3} — celui-ci reste gelé au cadrage 478be3ac (CSE-2) ; cet amendement CITE ce gel et ARME le chemin pour l'atteindre. Fige AVANT tout fetch/algèbre/simulation : (i) la cible opératoire O-ρ ; (ii) l'ESTIMATEUR de ρ (anti-back-fit d2) ; (iii) le protocole de données GÉNÉRIQUES (anti-proxy d3) ; (iv) le firewall Phase-1 (CSE-1 re-confirmé + opérationnalisation du drapeau relier≠ancrer d1) ; (v) le PÉRIMÈTRE DE SOURCES armé (fetch-gaté, identités R-41 ≥3 miroirs résolues AU fetch — CSE-3 ; biblio non vérifiée = JAMAIS consommée). Départ à froid. SANS SURCLASSEMENT (§6.4) : armer une question ne la tranche pas ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranché ; CCC non démontrée NI réfutée."
type: "amendement R-7 (instruction dédiée, paper-first — fige cible/estimateur/firewall/périmètre AVANT tout fetch/simulation). Candidat au gel R-36 : sha + horodatage à consigner HORS-FICHIER au manifeste, au dépôt. N'EMBARQUE PAS son propre sha (R-36). NON consommé."
statut: "RÉDIGÉ — candidat au gel R-36. NON consommé. Subordonné à LC-WORK-CADRAGE-A2-EXT-SPIKES (478be3ac, espace-verdict gelé) et à LC-SYNTHESE-SOCLES-5 §4 (CSE-1…6). Exécution = CSE-3 (identités R-41) → CSE-4 (gel des imports) → fetch/simulation générique 3D → algèbre/estimation ρ → CSE-5 (audit froid incognito souverain) → CSE-6 (nommage H). Audit froid OBLIGATOIRE sur tout verdict de substance (V1/V2/V3). À valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-12
prerequis_kb: [LC-WORK-CADRAGE-A2-EXT-SPIKES, LC-SYNTHESE-SOCLES-5, LC-WORK-CADRAGE-C1-ADMISSIBILITE, LC-D-A2-NUMERIQUE, LC-WORK-A2-CONJECTURE, LC-D-F3-A2STAR]
renvois: [LC-WORK-CADRAGE-A2-EXT-SPIKES, LC-D-IRREDUCTIBILITE-MOYENS]
tags: [amendement, R-7, R-36, R-41, A2star, spikes, phase1, rho, replication-multiplicative, generique-3D, BKL, non-cascade, estimateur-fige, anti-back-fit, relier-vs-ancrer, restore-on-demand, fetch-gate, CSE-1, CSE-3, audit-froid-obligatoire, R-54, §6.4, non-surclassement]
tags_epistemiques: [formalisable, décision ouverte, hors de portée]
maj: "2026-07-12 — v1.0 : création sur GO Thierry (armement A2★ Phase-1, reprise V63). Prérequis de propreté acquitté : §0-lite d'ouverture V63 PASS (mount PKG-SHA courant b8fd1ce1 = manifeste §0 post-ACTION #1, R-54 ; baseline clean-170 = 2f4a7392) ; consignation manifeste v2.75 déposée (dette → 0). Capacité : le déchargement effectif des 72 .py (~758 Ko) a débloqué ce front. R-36 : sha + horodatage HORS-FICHIER au dépôt ; ce fichier N'embarque PAS son propre sha. §6.4 : armer ne scelle/réduit/compte/démontre rien ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranché ; CCC non démontrée NI réfutée."
---

# Amendement R-7 — Phase 1 du programme externe A2★ (#1, spikes)

> **Paper-first.** Cible opératoire, estimateur de ρ, protocole de données génériques, firewall et
> périmètre de sources **FIGÉS ICI, AVANT tout fetch, toute simulation et toute algèbre**. **R-7** :
> toute extension de portée post-gel = **nouvel amendement daté**. **R-36** : gel horodaté consigné
> **hors-fichier** au manifeste, au dépôt ; aucune auto-référence. **CSE-1…6** = `LC-SYNTHESE-SOCLES-5`
> §4. **§6.4** : rien ici ne réduit/scelle/compte/démontre quoi que ce soit.

## 0. Provenance & objet `[ce que cet amendement arme]`

Le cadrage **CSE-2** `LC-WORK-CADRAGE-A2-EXT-SPIKES` (gelé R-7/R-36, sha hors-fichier `478be3ac`) a figé
**avant tout fetch** l'espace-verdict falsifiable de la seule maille non scellée d'A2★ — la
**non-cascade** — via le discriminant **ρ** (§2 du cadrage) et les verdicts **{V1 additif-confirmant /
V2 cascade-réfutant / V3 indéterminé-OA-gated}** (§4 du cadrage), sous la **clause d'ancrage** (§3) et
les drapeaux **d1/d2/d3** (§5). Le firewall **CSE-1** y est **PASS-CONDITIONNEL** (aveugle, 2026-07-08 :
`ρ=0` ne présuppose pas la non-cascade ; graphe `ρ→Q` sans cycle ; drapeau unique **relier≠ancrer**).

**Cet amendement n'ajoute ni verdict ni discriminant** : il **arme l'exécution** Phase-1 en figeant, par
écrit et avant engagement, *comment* ρ sera déterminé dans le générique 3D, *avec quelles sources*, *sous
quel firewall opérationnel*. Il lève le HOLD de fetch du cadrage pour un **périmètre figé** (§4), sans
rien consommer.

**Question opératoire figée (Q-ρ)** — *inchangée du cadrage, restatée pour l'exécution* : dans la
dynamique **générique 3D** (GR classique inhomogène **sans symétrie** près du bang, régime **BKL** +
**spikes**), le taux de réplication **multiplicative** de spikes par bounce, **ρ**, est-il **nul**
(production strictement **additive/bulk** `O(1)`, indépendante de `n_s`) ou **strictement positif**
(réplication multiplicative générique) ? La dichotomie scellée `non-cascade ⟺ ρ=0` et le taux
`= ln(1+ρ)` (hérités de `LC-D-A2-NUMERIQUE`, `verif_A2_numerique.py` EXIT 0/22) **ne sont pas refaits** :
ils sont le **cadre de lecture**, pas une prémisse à réimporter (cf. §3, d1/d3).

## 1. Cible opératoire figée `[O-ρ — avant toute consommation]`

**O-ρ** = établir ρ comme **fait de la dynamique générique 3D**, par l'une OU l'autre voie (les deux
admissibles ; la voie retenue est déclarée AU fetch, sans changer l'estimateur §2) :

- **O-ρ-num** — *évidence numérique de singularité générique* : évolution numérique de données initiales
  **génériques** (sans symétrie imposée, cf. §3) en régime BKL/spikes, suivi de la **densité de spikes**
  `n_s(N_b)` à travers les bounces successifs `N_b`.
- **O-ρ-an** — *dérivation analytique/asymptotique* : caractérisation du **mécanisme de génération** des
  spikes (transition de Kasner, formation/effacement de spikes, silence asymptotique) déterminant si un
  spike **engendre** de nouveaux spikes (multiplicatif) ou non (additif).

**Ce qui est HORS cible Phase-1** (⟹ nouvel amendement requis) : tout raffinement de A4 (no-hair) ou N
(≡Λ) ; toute maille A2★ déjà scellée en interne ; toute extension au-delà du générique 3D BKL/spikes.

## 2. Estimateur de ρ FIGÉ `[anti-back-fit d2 — gelé AVANT de voir les données]`

Pour interdire l'ajustement a posteriori (**d2**), l'estimateur est fixé **maintenant** :

- Modèle de comptage : `n_s(N_b) = n_0 · (1+ρ)^{N_b} + a·N_b + b` sur une fenêtre de bounces générique.
- **ρ est lu comme le taux de la composante MULTIPLICATIVE** : régression de `ln(n_s)` vs `N_b` après
  soustraction contrôlée de la dérive additive `a·N_b` ; **ρ=0** ⟺ `n_s` croît **sous-multiplicativement**
  (bornée, ou additive `∝ N_b`) au sens du test figé ci-dessous ; **ρ>0** ⟺ pente log positive robuste.
- **Test de décision figé** : `ρ` déclaré `>0` **seulement si** la pente log est positive à un seuil
  fixé ET stable sous (a) raffinement de résolution, (b) variation de la fenêtre `N_b`, (c) ré-échantillon
  des données génériques (§3). Instabilité sous (a)/(b)/(c) ⟹ **V3** (non fixé univoquement), **jamais V1
  par défaut**.
- **Aucun seuil n'est réglé pour matcher un `Q` sous-exp visé** : le critère est symétrique V1/V2 et gelé
  ici. Tout changement d'estimateur post-gel = **amendement R-7 daté** (d2).

## 3. Firewall Phase-1 `[CSE-1 re-confirmé + opérationnalisation de relier≠ancrer]`

Le drapeau unique du CSE-1 (**relier≠ancrer**) est opérationnalisé en règles d'exécution **bloquantes** :

- **d1 — non-réimport de la conclusion/prémisse mésoscopique.** ρ **ne peut pas** être fixé en réutilisant
  (a) l'input **Garfinkle mésoscopique** comme prémisse, ni (b) l'hypothèse `Q` sous-exp (la conclusion).
  Toute chaîne d'établissement de ρ qui passe par (a) ou (b) ⟹ **relie sans ancrer** ⟹ **V3** (clause
  d'ancrage §3 du cadrage).
- **d3 — non-substitution du proxy scellé.** Le modèle mésoscopique scellé (`verif_A2_numerique.py`,
  déchargé en annexe) **ne tient pas lieu** de générique 3D. S'il est requis en **cross-check**
  (jamais comme source de ρ), il est **restauré-on-demand** depuis sa grappe (byte-exact, index interne),
  **rejoué LIVE** (déclencheur §9ter) avant usage, puis **ré-archivé** — **jamais ré-importé en KB** sans
  décision opérateur. Le proxy interne A2 **n'est pas** reclassé « actif A2★ ».
- **Généricité des données** (condition de non-d3) : données initiales **sans symétrie imposée**, échantillon
  représentatif ; des données **non génériques** (symétrie, fine-tuning) qui forceraient ρ ⟹ **V3**
  (« données initiales non génériques » du verdict V3).

## 4. Périmètre de sources ARMÉ `[fetch-gaté — identités R-41 ≥3 miroirs résolues AU fetch, CSE-3]`

Périmètre **figé par CLASSES de descripteurs**, pas par IDs présumés (anti-fabrication d'attribution).
Les **identifiants exacts (arXiv/DOI) sont résolus et vérifiés R-41 sur ≥3 miroirs AU moment du fetch
(CSE-3)** ; **toute source non identité-vérifiée n'est JAMAIS consommée** ; aucune biblio consommée « en
bloc ».

- **S1 — BKL / oscillations near-singularity** : corpus fondateur Belinski–Khalatnikov–Lifshitz (comportement
  oscillatoire générique près d'une singularité spatiale) + revues modernes de la conjecture BKL.
- **S2 — Spikes & silence asymptotique** : travaux de relativité numérique et d'analyse asymptotique sur la
  **formation de spikes** en cosmologie inhomogène générique (dynamique de Mixmaster inhomogène, transitions
  de Kasner, asymptotic silence) — famille Garfinkle / Berger–Moncrief / Uggla–Elst–Wainwright–others,
  **au niveau générique 3D** (le proxy mésoscopique scellé est explicitement **exclu** du périmètre, d3).
- **S3 — (optionnel, gaté) données/outils numériques** générique-3D near-singularity, si une voie **O-ρ-num**
  est retenue.

**Règle R-41 (CSE-3)** : pour chaque source, identité vérifiée sur ≥3 miroirs (titre, auteurs, année, abstract
concordants) **avant** toute lecture de contenu. Divergence d'identité ⟹ source écartée. **CSE-4** : toute
valeur/hypothèse importée est **gelée** (sha hors-fichier) avant consommation ; **R-54** mount-autoritaire.

## 5. Séquence & espace-verdict CITÉ `[non re-gelé ici]`

Séquence d'exécution (chaque cran = livrable validé file-by-file ; départ à froid) :

1. **CSE-3** — résolution + vérification d'identité R-41 (≥3 miroirs) du périmètre §4. Livrable = table
   d'identités. **Aucune lecture de contenu avant PASS d'identité.**
2. **CSE-4** — gel des imports retenus (sha + horodatage hors-fichier). Livrable = registre d'imports gelés.
3. **Exécution O-ρ** (§1) sous estimateur figé (§2) et firewall (§3) — fetch/simulation/algèbre.
4. **CSE-5** — **audit froid incognito souverain** (Mode A zéro-fuite ; paquet SANS zone opérateur nommant
   le verdict ; l'incognito **prévaut**). OBLIGATOIRE sur tout verdict de substance.
5. **CSE-6** — nommage des hypothèses. En cas de **V1**, étiquette **`établi (physique externe, sous
   hypothèses H)`** — **jamais** « CCC vraie » ni « A2★ prouvée » nue.

**Espace-verdict = CITÉ du gel `478be3ac`, INCHANGÉ** : **V1** additif-confirmant (ρ=0 ⟹ réduction
**candidate** à valider CSE-5) / **V2** cascade-réfutant (ρ>0 ⟹ A2★ **réfutée** — élimination d'hypothèse
légitime ; §6.4 : ne réfute pas la CCC par ce seul point) / **V3** indéterminé-OA-gated (délimitation,
`{A4 ; A2★ ; N}` inchangé). Mutuellement exclusifs, nommés **avant** fetch/algèbre.

## 6. Coût, capacité & non-surclassement `[§6.4]`

**Capacité** : dépôt **net +1** (cet amendement), budgété par la capacité réellement libérée au
déchargement des 72 .py (~758 Ko) — front A2★ Phase-1 explicitement débloqué (V63 §3). Orphan-guard :
in-degree entrant assuré par `renvois` (cité par le cadrage `478be3ac` à l'exécution) ; non orphelin.
Couplage swap éventuel = décision opérateur au dépôt.

**§6.4 — non-surclassement.** Armer la Phase-1 (figer cible, estimateur, firewall, périmètre) **n'établit,
ne scelle, ne réduit, ne compte, ne démontre RIEN**. Aucune algèbre, aucun fetch, aucune simulation,
aucun sceau à ce stade. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; `N` non fixé (≡`Λ`) ; A4 non
réduit ; **A2★ non tranché** ; O₂ non construit ; β **T-b** ; **CCC non démontrée NI réfutée**. Une
éventuelle réduction (V1) ne sera qu'un **candidat** à valider en CSE-5, étiqueté sous hypothèses H
(CSE-6) — un moyen **externe**, jamais une démonstration de la CCC.

*(R-36 : ce fichier n'embarque pas son propre sha ; gel sha + horodatage consignés HORS-FICHIER au
manifeste, au dépôt. R-54 : mount autoritaire, §0-lite d'ouverture V63 PASS = b8fd1ce1.)*
