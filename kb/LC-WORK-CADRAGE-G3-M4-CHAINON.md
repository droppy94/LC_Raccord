---
id: LC-WORK-CADRAGE-G3-M4-CHAINON
codename: LC-RACCORD
titre: "Cadrage gelé R-36 — m4-CHAÎNON (étape (b) de la séquence a→b sur β ; item de tête V50 §4.1). Fige AVANT toute algèbre : construction d'un sceau NEUF testant l'énoncé L²-SYMPLECTIQUE de (non-)normalisabilité de la branche Δ₊=3 (g₍ₙ₎ Neumann/VEV, spin-2 TT) en dS₄ genuine, dans le but de CASSER la sign(Λ)-symétrie EXHIBÉE au bloc C du sceau verif_G3_adm_imports.py (sha a0b962c8 : indiciel s(s−3) IDENTIQUE AdS↔dS, seul k²z² flippe). Résidu ciblé = BP-2 (routé depuis LC-D-G3-ADM-IMPORTS v1.1 §4bis) : la MARCHE H_b-décroissant → L²-symplectique-normalisable (mesure symplectique ≠ mesure H_b de Sobolev à poids). PORTÉE HONNÊTE PRÉ-DÉCLARÉE : ce sceau est l'UNIQUE marche restante entre la structure indicielle internalisée et un verrou β propre ; le m4-chaînon de LC-D-G3-ADMISSIBILITE v1.4 est VACANT et le reste tant que ce sceau n'exhibe pas une quantité DIFFÉRANT AdS↔dS. Espace de verdicts FIGÉ : ASYMÉTRIQUE-NON-NORM (⟹ candidat T-c propre, R-53 vers TRANSPORT, audit froid OBLIGATOIRE) / NORMALISABLE-dS (⟹ ouvre construction, requalifie β) / SYMÉTRIQUE (⟹ m4 reste vacant, T-b maintenu) / INDÉTERMINÉ (⟹ import re-nommé). SANS SURCLASSEMENT (§6.4) : trancher une marche de normalisabilité ne fixe NI N NI Λ ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
type: "cadrage gelé R-36 (work-active) — arme l'étape (b) de la séquence a→b (item de tête V50 §4.1). NE scelle rien, NE vote pas. Gel sha256 consigné HORS-FICHIER au manifeste au dépôt (anti-auto-référence R-36 : ce fichier N'EMBARQUE PAS son propre hash)."
statut: "work-active — GELÉ au dépôt (R-36), NON consommé. Le sceau NEUF verif_G3_m4_chainon.py incrémente .py 76→77 ⟹ §0-full OBLIGATOIRE au lot de dépôt de sa consommation. Phase 0 KB-only : 0 fetch, 0 amendement R-7 de source (structure FG + solutions radiales dérivables ab initio depuis les ODE déjà internalisées, blocs A/C du sceau a0b962c8)."
version: 1.0
langue: fr
date: 2026-07-06
maj: "2026-07-06 — v1.0 : création sur GO Thierry (fork V50 §4 item de tête = m4-chaînon, étape (b)). Rédigé APRÈS §0-lite PASS (baseline v2.49, PKG-SHA 6e1b7ffe…733d1a reproduit byte-exact, 236 hachés = 160 .md + 76 .py) et APRÈS vérification R-54 (verdicts de tête LC-D-G3-ADM-IMPORTS v1.1 + LC-D-G3-ADMISSIBILITE v1.4 + LC-D-G3-TRANSPORT v0.4 lus sur mount ⟹ m4 VACANT confirmé, BP-2 routé confirmé, sign(Λ)-symétrie du bloc C confirmée). AUCUNE algèbre exécutée, AUCUN fetch engagé avant ce gel."
prerequis_kb: [LC-D-G3-ADM-IMPORTS, LC-D-G3-ADMISSIBILITE, LC-D-G3-TRANSPORT, LC-D-O2-SCATTERING-FG, LC-D-GAMMA-NSTAR-ADS4]
tags: [cadrage, gel-R36, anti-fit, R-7, m4-chainon, etape-b, sequence-a-b, L2-symplectique, normalisabilite, branche-Delta3, spin-2-TT, g-n-Neumann-VEV, genuine-dS, sign-Lambda-symetrie, casser-symetrie, BP-2, marche-Hb-symplectique, sceau-neuf, phase-0-KB-only, verrou-beta-candidat, R-53, R-54, §6.4, A4, A2star, N]
---

# Cadrage gelé — m4-chaînon (étape (b)) : test L²-symplectique de la branche `Δ₊=3` en dS genuine

> **Objet.** Le verdict `LC-D-G3-ADMISSIBILITE` v1.4 est **`T-c`-conditionnel** ; son unique
> résidu vivant après l'étape (a) (V50 §1.3, `I-SFG` CONVERTI-PARTIEL) est **`BP-2`** :
> l'énoncé de (non-)normalisabilité de la branche `Δ₊=3` au sens **norme FG-symplectique**
> reste un **import routé** (`LC-D-G3-ADM-IMPORTS` v1.1 §4bis, `mE` tenu). Ce cadrage fige les
> cibles du sceau qui **teste** cette marche, **AVANT** toute algèbre. C'est l'**unique marche
> restante** entre la structure indicielle déjà internalisée et un verrou `β` propre.

> **Note anti-auto-référence R-36.** Ce fichier N'EMBARQUE PAS son propre hash post-dépôt ;
> le gel sha256 vit exclusivement au manifeste (consigné hors-fichier au dépôt).

## §1 — Question figée `Q-m4`
La branche `Δ₊=3` (racine `g₍ₙ₎`, condition Neumann/VEV, mode spin-2 TT sous-dominant) est-elle
**normalisable au sens de la norme FG-symplectique** en dS₄ genuine (`R_MN = +(d/L²)G_MN`,
`𝓘⁺` spacelike, sans cutoff) — **et ce verdict CASSE-T-IL la sign(Λ)-symétrie**, c.-à-d. diffère-t-il
du verdict AdS₄ (`R_MN = −(d/L²)G_MN`) ?

> Le sceau `a0b962c8` (bloc C) a établi que l'**indiciel** `s(s−3)` est identique AdS↔dS (seul le
> terme sous-dominant `k²z²` flippe de signe). La question `Q-m4` porte sur la **NORME**, pas
> l'indiciel : le flip de `k²z²` change la solution radiale complète `f(z)` (Bessel modifiée
> monotone en AdS vs Bessel oscillante en dS) ⟹ peut changer la convergence de l'intégrale
> symplectique là où l'exposant seul ne le voit pas.

## §2 — Cibles figées `[AVANT toute algèbre]`

- **`M4-1` — solutions radiales complètes des deux signes.** Dériver ab initio, depuis les ODE
  radiales déjà internalisées (bloc A euclidien/AdS `z²f″ − 2z f′ − k²z² f = 0` ; bloc C
  lorentzien-dS `z²f″ − 2z f′ + k²z² f = 0`), les solutions complètes
  `f(z) = z^{3/2} Z_{3/2}(κz)` avec `κ` **réel** (AdS : `I_{3/2}/K_{3/2}`, comportement monotone)
  vs `κ` **imaginaire** (dS : `J_{3/2}/Y_{3/2}` ou Hankel `H^{(1,2)}_{3/2}`, comportement
  **oscillant**). Confirmer explicitement que la **structure** des solutions DIFFÈRE alors que les
  exposants indiciels `{0, 3}` coïncident. Identifier la solution portant la branche `Δ₊=3`
  (sous-dominante `∼ z³` au bord).

- **`M4-2` — norme FG-symplectique de la branche `Δ₊=3`.** Construire la **mesure symplectique
  FG** (courant symplectique KG conservé `Ω = ∫ dz √g · z^{2Δ+1−d} |f_{Δ₊=3}|²`, ou forme
  bilinéaire symplectique `⟨f, f⟩_Ω` du crochet de Klein-Gordon sur les tranches FG) et **évaluer
  la convergence** de l'intégrale : (i) près du **bord** `z → 0` ; (ii) dans le **bulk vers `𝓘⁺`**
  (grand `z` / point conforme). Faire cette évaluation **dans les DEUX signes** (AdS et dS), avec la
  même prescription de mesure. `mE` : la mesure testée est la mesure **symplectique**, PAS la mesure
  `H_b` de Sobolev à poids de S1.

- **`M4-3` — test de sign(Λ)-symétrie sur le VERDICT de normalisabilité.** Comparer le statut
  (normalisable / non-normalisable) de la branche `Δ₊=3` entre dS et AdS obtenu en `M4-2`. Trancher
  la question centrale : la **norme casse-t-elle la symétrie** que l'**indiciel préserve** ? Le
  critère de succès du sceau (`m4`, ci-dessous) est qu'il **exhibe** une quantité prenant des valeurs
  DIFFÉRENTES en AdS et en dS ; à défaut, il reste vacant comme ses prédécesseurs.

## §3 — Firewall `[hérité + spécifique]`
- **`m1` (anti-tautologie)** : le verdict (normalisable / non) doit être **DÉRIVÉ** de l'intégrale
  évaluée, jamais **posé** en hypothèse ni lu depuis un import.
- **`m2` / `m3` (anti-circularité)** : **aucun** élément de `{A4 ; A2★ ; N}` en entrée ; entrées =
  métrique FG + équation d'Einstein + mode spin-2 TT, rien d'autre. Bookkeeping des entrées exigé.
- **`m4` (anti-effacement-de-signe) `[LE POINT]`** : le sceau DOIT exhiber au moins une quantité
  observable (convergence/divergence de l'intégrale, exposant de queue, phase asymptotique) qui
  **DIFFÈRE** entre AdS et dS. Un mécanisme reposant sur une **indépendance en signe triviale**
  (`i² = −1` absorbé, symétrisation qui efface AdS/dS par construction) est **DISQUALIFIÉ** — il
  reproduirait le `m4`-vacant des sceaux `010a0562` / `a0b962c8`. Le sceau doit **tester** le pas
  genuine-dS, pas l'effacer.
- **`m5` (bookkeeping)** : aucune preuve d'anti-circularité posée comme théorème ; traçabilité des
  hypothèses de contour / prescription seulement.
- **`mE` (mesure)** : distinction stricte **mesure symplectique** vs **mesure `H_b`** de Sobolev ;
  toute traduction `H_b → symplectique` non dérivée reste un import nommé (ne pas la **supposer**).

## §4 — Espace de verdicts FIGÉ
1. **`ASYMÉTRIQUE-NON-NORM`** — la branche `Δ₊=3` est **non-normalisable en dS** ET le verdict
   **DIFFÈRE** d'AdS (sign(Λ)-symétrie **CASSÉE**) ⟹ le pas **genuine-dS EST testé** par le sceau ⟹
   **candidat `T-c` propre** (verrou `β`). ⟹ **R-53** vers `LC-D-G3-TRANSPORT` (bascule `T-b → T-c`
   NON automatique) ; **audit froid OBLIGATOIRE** (Mode A/B, pilote disqualifié) AVANT toute
   propagation ; patch aval du chaînon `LC-D-G3-ADMISSIBILITE` (m4-chaînon rempli).
2. **`NORMALISABLE-dS`** — la branche `Δ₊=3` est **normalisable en dS** ⟹ le mode de bord `g₍ₙ₎` est
   **admissible** ⟹ **ouvre une construction** (ne ferme PAS `β`), **requalifie** le front ; audit
   froid selon criticité ; consignation d'un affaiblissement de la direction `T-c` (pas de
   « réfutation », §6.4).
3. **`SYMÉTRIQUE`** — le statut de normalisabilité est **lui-même** sign(Λ)-symétrique ⟹ le sceau
   **ne teste pas** genuine-dS ⟹ **`m4` reste structurellement VACANT** ; `T-c`-conditionnel
   INCHANGÉ ; `G3-TRANSPORT` reste `T-b`. Le résidu `BP-2` reste import (re-consigné).
4. **`INDÉTERMINÉ`** — l'intégrale ne tranche pas KB-only (dépendance à une prescription `iε` / choix
   de contour / condition de rayonnement à `𝓘⁺` non dérivable sans source) ⟹ **import re-nommé** ;
   éventuel amendement R-7 fetch daté en aval (hors ce cadrage).

## §5 — Régime opératoire
- **Phase 0 KB-only** : 0 fetch, 0 amendement R-7 de source. Les solutions radiales et la mesure
  symplectique sont **dérivables ab initio** depuis les ODE des blocs A/C du sceau `a0b962c8` déjà
  internalisé (SymPy 1.14.0).
- **Sceau NEUF** `verif_G3_m4_chainon.py` : dépôt incrémente `.py` **76 → 77** ⟹ **§0-full
  OBLIGATOIRE au lot de dépôt** (rejeu 76 sceaux + le neuf). Lourds éventuels (intégrales
  symboliques Bessel) : standalone `setsid`, timeout ≥ 600 s (1 CPU).
- **Ordre figé** : `M4-1` (solutions) → `M4-2` (norme, deux signes) → `M4-3` (test de symétrie) →
  verdict dans l'espace figé §4.
- **Audit froid** : OBLIGATOIRE sur `ASYMÉTRIQUE-NON-NORM` (bascule de substance) ; selon criticité
  sur `NORMALISABLE-dS` ; le pilote fournit le paquet d'audit, pas le verdict.
- Chaînon-verdict aval `LC-D-G3-M4-CHAINON` en `⟳` (patch de `G3-ADMISSIBILITE` selon verdict).

## §6.4 — Non-surclassement `[terminal]`
Tester la marche de normalisabilité `H_b → L²-symplectique` de la branche `Δ₊=3` **tranche une
question d'admissibilité de mode**, RIEN de plus : même un verdict `ASYMÉTRIQUE-NON-NORM` ne
donnerait qu'un **candidat** `T-c` propre soumis à audit froid, ne **fixerait NI `N` NI `Λ`**, ne
**construirait PAS `O₂`**, ne **réduirait PAS `A4`**. `{A4 ; A2★ ; N}` INCHANGÉ ; D1 non clos ;
N non fixé (≡Λ) ; A4 non réduit ; A2★ non tranché ; O₂ non construit ; `β` reste `T-b` tant que
le sceau n'a pas rendu son verdict et passé l'audit ; CCC non démontrée NI réfutée.
(cf. `LC-D-G3-ADM-IMPORTS` v1.1, `LC-D-G3-ADMISSIBILITE` v1.4, `LC-D-G3-TRANSPORT` v0.4,
`LC-WORK-AMENDEMENT-R7-G3-IMPORT-BIENPOSE-DS`, `LC-D-O2-SCATTERING-FG` v0.1)
