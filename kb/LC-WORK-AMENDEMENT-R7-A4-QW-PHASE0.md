---
id: LC-WORK-AMENDEMENT-R7-A4-QW-PHASE0
codename: LC-RACCORD
titre: "AMENDEMENT R-7 DATÉ — armement de la Phase 0 KB-only du front A4 Phase-1, cible Q-W (limite du Weyl RESCALÉ à 𝓘⁺ sous flot no-hair, branche Bianchi/Wald seule). NE re-gèle PAS l'espace-verdict {W1/W2/W3} — celui-ci reste gelé au cadrage 91a50391 (CSE-2) ; cet amendement CITE ce gel et ARME le chemin pour l'atteindre. Fige AVANT toute algèbre : (i) la cible opératoire O-W (calcul type-par-type Bianchi de la limite du couple 𝓔/𝓑 rescalé) ; (ii) l'ordre d'exécution (types canoniques d'abord, Bianchi I en tête) ; (iii) le firewall opérationnalisé m1-m7 (contrôles PAR ÉTAPE dans le sceau) ; (iv) le régime STRICTEMENT KB-only (Phase 1 fetch = HOLD, tout besoin de source = candidat W3 + nouvel amendement) ; (v) le sceau conditionnel armé (W1/W2 ⟹ .py 5→6 ⟹ §0-full au dépôt). Départ à froid. SANS SURCLASSEMENT (§6.4) : armer une question ne la tranche pas ; {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; CCC non démontrée NI réfutée."
type: "amendement R-7 (instruction dédiée, paper-first — fige cible/ordre/firewall/régime AVANT toute algèbre). Candidat au gel R-36 : sha + horodatage à consigner HORS-FICHIER au manifeste, au dépôt. N'EMBARQUE PAS son propre sha (R-36). NON consommé."
statut: "RÉDIGÉ — candidat au gel R-36. NON consommé. Subordonné à LC-WORK-CADRAGE-A4-QW (91a50391, espace-verdict {W1/W2/W3} gelé, firewall m1-m7, bornes b1-b4). Gate amont : CSE-1 en aveugle = PASS (2026-07-12, avant le gel du cadrage). Exécution = Phase 0 KB-only (algèbre SymPy type-par-type) → chaînon-verdict LC-D-A4-QW dans l'espace gelé → CSE-5 audit froid OBLIGATOIRE sur tout verdict de substance → CSE-6 → propagation. À valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-12
prerequis_kb: [LC-WORK-CADRAGE-A4-QW, LC-D-IRREDUCTIBILITE-MOYENS, LC-D3-WEYL-BUNCHDAVIES, LC-D-CB-WEYL-MAGNETIQUE, LC-D-G3-ADM-IMPORTS, LC-SYNTHESE-SOCLES-5]
renvois: [LC-WORK-CADRAGE-A4-QW, LC-D-O2-SCATTERING-FG]
tags: [amendement, R-7, R-36, A4, Q-W, phase0, KB-only, bianchi, wald, weyl-rescale, no-hair, firewall, sceau-conditionnel, CSE, audit-froid-obligatoire, R-54, §6.4, non-surclassement]
tags_epistemiques: [formalisable, décision ouverte]
maj: "2026-07-12 — v1.0 : création sur GO Thierry (armement A4 Phase-1 Q-W, session V66). Prérequis de propreté acquitté : §0-lite V66 PASS + consignations v2.80 (ACTION #1) et v2.81 (dépôt cadrage + gel R-36 91a50391) déposées, dette 0, mount 751a6279. Séquence CSE tenue : CSE-1 aveugle PASS AVANT gel du cadrage ; cadrage CSE-2 gelé AVANT cet amendement ; cet amendement gelé AVANT toute algèbre. R-36 : sha + horodatage HORS-FICHIER au dépôt ; ce fichier N'embarque PAS son propre sha. §6.4 : armer ne scelle/réduit/compte/démontre rien ; {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; CCC non démontrée NI réfutée."
---

# Amendement R-7 — Phase 0 KB-only du front A4, cible Q-W

> **Paper-first.** Cible opératoire, ordre d'exécution, firewall opérationnalisé et régime KB-only
> **FIGÉS ICI, AVANT toute algèbre**. **R-7** : toute extension de portée post-gel = **nouvel
> amendement daté**. **R-36** : gel horodaté consigné **hors-fichier** au manifeste, au dépôt ; aucune
> auto-référence. **§6.4** : rien ici ne réduit/scelle/compte/démontre quoi que ce soit.

## 0. Provenance & objet `[ce que cet amendement arme]`

Le cadrage **CSE-2** `LC-WORK-CADRAGE-A4-QW` (gelé R-36, sha hors-fichier `91a50391`, 2026-07-12) a
figé **avant toute algèbre** : la question Q-W (§1 du cadrage), l'espace-verdict **{W1
nettoyage-tenant / W2 résidu-cassant / W3 indéterminé}** avec critère de décision et clause de
généricité (§2), le protocole Phase 0 (§3), le firewall **m1-m7** (§4) et les bornes de portée
**b1-b4** (§5). Gate amont : **CSE-1 en aveugle = PASS** (2026-07-12, incognito souverain, AVANT le
gel). Cet amendement **ne re-gèle rien** de ce qui précède : il **CITE** le gel `91a50391` et arme
l'exécution.

## 1. Cible opératoire figée `[O-W — avant toute algèbre]`

**O-W** : calculer, **type de Bianchi par type de Bianchi** (classes couvertes par Wald 1983 : tous
types sauf IX), la limite à 𝓘⁺ du couple Weyl rescalé programme :

- **𝓔** = (3/2H)·g₃ (partie électrique, scellé `LC-D3-WEYL-BUNCHDAVIES`),
- **𝓑** = (1/H)·C[g₀] (partie magnétique, scellé `LC-D-CB-WEYL-MAGNETIQUE`),

le long du flot no-hair (Λ>0, SEC+DEC), pour données initiales **génériques dans la classe** (m1 :
cisaillement/Weyl nu initial arbitrairement grand admis). Sortie par type : `lim 𝓔` et `lim 𝓑`
(0 / résidu générique / non conclu), avec identification explicite de la donnée qui porte tout résidu.
Adjudication globale ensuite CONTRE le critère §2 du cadrage (non recomputé ici).

## 2. Ordre d'exécution figé `[anti-fit d'ordonnancement]`

1. **Bianchi I** (cas canonique : cisaillement pur, Kasner→dS, solution explicite) — étalon du
   pipeline : construction du flot, rescaling, extraction FG {g₀, g₃}, limites 𝓔/𝓑, contrôle b1
   (taux effectif) exhibé.
2. **Bianchi V puis types à courbure spatiale non triviale** (II, VI, VII, VIII selon tractabilité
   SymPy) — même pipeline, mêmes contrôles ; si un type résiste, le consigner NON-CONCLU (candidat W3
   partiel) sans forcer.
3. **Argument d'uniformité** (si atteignable) : ce qui, dans la structure {racines {0,3}, sceau
   `a0b962c8`}, est indépendant du type — sinon, couverture type-par-type seule, honnêtement bornée.

L'ordre est figé pour empêcher un choix de cas post-hoc favorable à une issue (anti-fit). Aucun type
ne peut être ajouté ou retiré sans nouvel amendement.

## 3. Firewall opérationnalisé `[m1-m7 du cadrage → contrôles PAR ÉTAPE]`

Chaque étape du pipeline embarque, dans le sceau conditionnel, les contrôles suivants (mutation ou
assert dédié) :

- **m1** : les données initiales du calcul sont paramétriques (σ₀ libre, non nul générique) ; assert
  qu'aucune étape ne substitue σ₀=0 ni g₃=0 en prémisse.
- **m2** : la conclusion par type porte sur `lim 𝓔` / `lim 𝓑` (rescalés) ; la décroissance du Weyl nu
  est calculée mais JAMAIS consommée comme conclusion (assert de séparation des symboles).
- **m3** : domaine des paramètres borné à la classe admise (pas de IX, pas d'inhomogène, pas de
  rotation de signature) ; assert de domaine.
- **m4** : les seuls énoncés no-hair consommés sont ceux au grade KB (`LC-D-IRREDUCTIBILITE-MOYENS`
  §3) ; aucun énoncé nouveau attribué à Wald ; tout besoin au-delà ⟹ HOLD.
- **m5** : aucune prémisse « petites données » ; assert que les développements ne tronquent pas en
  supposant la petitesse des données initiales (perturbatif autour de dS admis SEULEMENT comme
  contrôle de cohérence, jamais comme véhicule du verdict).
- **m6** : l'exposant de compensation conforme est DÉRIVÉ dans le calcul (pas posé) et confronté au
  couple scellé ; mutation firewall : un exposant altéré (p. ex. Ω⁻¹) doit CASSER l'assert de
  cohérence avec 𝓔=(3/2H)g₃.
- **m7** : aucune étape n'utilise l'existence de 𝓘⁺ comme argument de valeur.

## 4. Régime STRICTEMENT KB-only `[Phase 1 fetch = HOLD]`

ZÉRO fetch, ZÉRO source primaire, ZÉRO consommation biblio. Tout point qui exigerait une source
externe (p. ex. taux no-hair précis d'un type non dérivable en interne) est consigné **NON-CONCLU** et
route vers un éventuel Phase 1 sous **nouvel amendement R-7** (avec CSE-3 identités R-41 au fetch).
Le présent amendement n'ouvre AUCUN droit de fetch.

## 5. Sceau conditionnel armé & séquence aval `[cité, non re-gelé]`

- **Sceau** : si l'adjudication aboutit à W1 ou W2, sceau `verif_A4_QW.py` OBLIGATOIRE (SymPy,
  asserts porteurs + mutations firewall m1-m7 intégrées, EXIT 0) ⟹ `.py` 5→6 ⟹ **§0-full au dépôt**
  (cadence §9bis/§9ter). W3 sans algèbre aboutie = pas de sceau (chaînon-verdict seul).
- **Séquence aval** (SOCLES-5 §4, citée) : chaînon-verdict `LC-D-A4-QW` dans l'espace gelé →
  **CSE-5 audit froid incognito souverain OBLIGATOIRE** sur tout verdict de substance (W1 comme W2 ;
  W3 = dispensable sauf si porteur) → CSE-6 → propagation (IDX rangée, manifeste, consignation).
- **HORS-CIBLE** (⟹ nouvel amendement) : maillon #3 générique, #1/#2/#4, Bianchi IX, inhomogène,
  toute maille A2★/N, tout fetch.

## 6. Coût, capacité & non-surclassement `[§6.4]`

Coût : algèbre SymPy en session (foreground batches si lourd) ; +1 chaînon-verdict au dépôt (+1 sceau
si W1/W2) — arbitrage capacité opérateur au dépôt. **§6.4 (terminal)** : armer une question ne la
tranche pas ; AUCUNE issue {W1/W2/W3} ne scelle/réduit/compte/démontre ; `{A4 ; A2★ ; N}` INCHANGÉ ;
D1 non clos ; N non fixé (≡Λ) ; O₂ non construit ; β T-b ; A4 non réduit ; A2★ parqué pending OA ;
CCC non démontrée NI réfutée.
