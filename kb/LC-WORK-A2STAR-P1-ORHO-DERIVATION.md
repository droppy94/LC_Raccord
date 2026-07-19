---
id: LC-WORK-A2STAR-P1-ORHO-DERIVATION
codename: LC-RACCORD
titre: "EXÉCUTION O-ρ (A2★ Phase-1) — dérivation analytique PRIMAIRE du facteur de branchement ρ (carte génératrice de spikes) sous imports gelés CSE-4 (I1 substrat Uggla scale-invariant / silent boundary ; I2 carte de spike Lim ; I3 récurrence Heinzle–Uggla) + CROSS-CHECK numérique (C1–C3), sous ESTIMATEUR FIGÉ §2. VERDICT CANDIDAT (NON gravé) : V3 — INDÉTERMINÉ / OA-GATED. ρ n'est PAS fixé univoquement par la seule dynamique générique 3D : les résultats explicites porteurs (spikes récurrents) sont symétrie-réduits (G₂/Gowdy) ⟹ ÉCART DE GÉNÉRICITÉ vs données 3D pleinement génériques (test §2-c) ; le cross-check numérique est résolution-limité aux échelles fines décisives (test §2-a) ; toute conclusion ρ=0 propre exigerait soit de franchir l'écart de généricité, soit de réimporter l'additivité/silence comme prémisse (d1). Lean NON-porteur vers ρ=0 consigné, ne constituant PAS une tranche. GATÉ CSE-5 : pilote DISQUALIFIÉ pour adjuger ; audit froid incognito souverain (Mode A zéro-fuite, paquet SANS zone opérateur nommant le verdict) OBLIGATOIRE avant toute gravure. SANS SURCLASSEMENT (§6.4) : un candidat V3 ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ NON tranché ; CCC non démontrée NI réfutée."
type: "exécution O-ρ (work-active) — dérivation + cross-check + classification CANDIDATE. NON gravé, NON sceau. Gaté CSE-5 (pilote disqualifié). N'EMBARQUE PAS son propre sha (R-36)."
statut: "RÉDIGÉ — VERDICT CANDIDAT V3 (indéterminé/OA-gated), NON gravé. Substance consommée sous registre CSE-4 (I1–I3, C1–C3). Étape suivante OBLIGATOIRE = CSE-5 (paquet zéro-fuite → instance incognito souveraine ; l'incognito prévaut). Aucune propagation de verdict, aucun ajustement de {A4;A2★;N} avant CSE-5. À valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-12
prerequis_kb: [LC-WORK-A2STAR-P1-CSE4-IMPORTS, LC-WORK-A2STAR-P1-CSE3-IDENTITES, LC-WORK-AMENDEMENT-R7-A2STAR-PHASE1, LC-WORK-CADRAGE-A2-EXT-SPIKES, LC-SYNTHESE-SOCLES-5]
renvois: [LC-WORK-CADRAGE-A2-EXT-SPIKES, LC-D-IRREDUCTIBILITE-MOYENS]
tags: [execution, O-rho, A2star, phase1, rho, facteur-branchement, spikes, Mixmaster, silent-boundary, asymptotic-silence, ecart-genericite, resolution-limitee, verdict-candidat, V3, OA-gated, gate-CSE-5, pilote-disqualifie, d1, d3, §6.4, non-surclassement]
tags_epistemiques: [formalisable, décision ouverte, hors de portée]
maj: "2026-07-12 — v1.0 : création sur GO Thierry (exécution O-ρ). Substance lue/dérivée sous registre CSE-4 (fin du départ à froid). Estimateur §2 validé bien-posé au préalable (sélection de modèle BIC : additif→V1, multiplicatif→V2 discriminés ; données synthétiques, AUCUNE mesure physique de ρ). Dérivation analytique primaire (I1→I2→I3) : le facteur de branchement ρ n'est pas fixé univoquement pour données 3D pleinement génériques (écart de généricité G₂/Gowdy→3D-générique ; test §2-c). Cross-check numérique (C1–C3) résolution-limité aux échelles fines (test §2-a) ⟹ ne lève pas l'indétermination (standing plein, non rétrogradé). d1 respecté (aucune injection de la prémisse additive ni de la conclusion Q sous-exp) ; d3 respecté (proxy scellé hors-jeu). VERDICT CANDIDAT = V3. GATÉ CSE-5 (pilote disqualifié). §6.4 : ne scelle/réduit/compte/démontre rien ; {A4;A2★;N} INCHANGÉ ; A2★ non tranché ; CCC non démontrée NI réfutée. R-36 : ce fichier n'embarque pas son propre sha."
---

# Exécution O-ρ — dérivation du facteur de branchement ρ · A2★ Phase-1 · **verdict CANDIDAT (gaté CSE-5)**

> **Substance consommée sous CSE-4.** Dérivation analytique primaire (I1–I3) + cross-check numérique
> (C1–C3), estimateur figé **§2**, espace-verdict cité **§4** du gel `478be3ac`. **Verdict CANDIDAT, NON
> gravé** : le **pilote est DISQUALIFIÉ** pour adjuger la substance (CSE-5). **§6.4** : rien ici ne scelle.

## 0. Cadre & discipline

Objet : trancher — ou délimiter — la maille **non-cascade** d'A2★ par détermination de **ρ** ≡ taux de
réplication **multiplicative** de spikes par bounce, dans la **dynamique générique 3D** (GR inhomogène sans
symétrie près du bang, régime BKL + spikes). Dichotomie scellée héritée (cadre de lecture, non refaite) :
`non-cascade ⟺ ρ=0`, taux de cascade `= ln(1+ρ)`. Estimateur §2 **figé** ; guardrails d1/d3 + généricité
**actifs**. Verdict **candidat**, gaté **CSE-5**.

## 1. Substrat générique 3D `[I1 — Uggla scale-invariant / silent boundary]`

En variables Hubble-normalisées du repère orthonormé `{E_α{}^i, Σ_αβ, A^α, N_αβ}`, les équations d'Einstein
forment un système dynamique autonome. Pour les **lignes de temps génériques**, l'**attracteur passé** vit
sur la **frontière silencieuse** (*silent boundary*) où les termes de dérivée spatiale (via `E_α{}^i`)
**s'annulent dynamiquement** : c'est le **silence asymptotique** (horizons de particules → 0, dérivées
spatiales dynamiquement négligeables). Sur cette frontière, chaque point spatial suit la dynamique
**localement homogène = Mixmaster** : suite infinie d'époques de Kasner reliées par des bounces de type
Bianchi II (carte de Kasner / carte BKL). **Conséquence structurelle** : la **localité** de l'attracteur
passé **supprime le couplage spatial** requis pour qu'un spike en un lieu **cause** des spikes ailleurs.

## 2. Carte génératrice & récurrence `[I2 Lim + I3 Heinzle–Uggla]`

Les **spikes** sont l'**exception** au silence asymptotique. En des lieux spatiaux **isolés** (points de
spike), la donnée locale **enjambe la variété stable d'un point-selle** (selle de Taub/Kasner) ; de part et
d'autre, les lignes d'univers voisines **divergent** au fil du bounce ⟹ profil spatialement **étroit** = un
spike. **I2** (Lim) fournit une **solution explicite** de spike (transformation génératrice sur germe
Bianchi II vide) : le spike est une structure **non-locale**, portée par une **surface** (codimension 1).
**I3** (Heinzle–Uggla, *spike statistics*) établit que les spikes **récurrent** : à un lieu de spike donné,
une **séquence de Kasner induite par spikes récurrents** se déroule, statistiquement caractérisée.

**Point décisif** : la récurrence de I3 est une récurrence **en temps** à des **surfaces de spike FIXES**
(le même lieu subit des transitions de spike répétées) — c'est un compte de lieux **borné/additif**, PAS un
**engendrement spatial** de nouveaux lieux.

## 3. Facteur de branchement ρ `[dérivation primaire — estimateur §2]`

Soit `n_s(N_b)` = nombre de **lieux (surfaces) de spike distincts** présents au bounce `N_b`. Dans le modèle
figé §2, `n_s(N_b) = n_0(1+ρ)^{N_b} + a·N_b + b` ; **ρ** = facteur de branchement **multiplicatif**.

Deux canaux concurrents, **non refermés par la seule dynamique générique 3D** :

- **Canal additif (⟶ ρ=0).** Silence asymptotique (§1) + récurrence à surfaces fixes (§2) : les lieux de
  spike forment un ensemble de codimension 1 **fixe/additif** qui **recurre en temps** sans se multiplier
  spatialement. La localité supprime le couplage inter-lieux. ⟹ `n_s` **sous-multiplicatif**.
- **Canal multiplicatif (⟶ ρ>0).** Les points de spike sont exactement où le silence **se brise** : gradients
  spatiaux **non** négligeables, génération de **structure spatiale plus fine** (fréquences plus hautes) —
  qui pourrait **ensemencer de nouveaux lieux** de spike à échelle fine, de façon **multiplicative**.

**Verrou de généricité.** Les résultats **porteurs** qui trancheraient (solution explicite I2 ; statistiques
de récurrence I3) sont établis en **symétrie réduite** (cosmologies **G₂ / Gowdy**, un/deux vecteurs de
Killing), **PAS** en 3D **pleinement générique** (sans symétrie). Étendre leur conclusion additive au
générique 3D = **écart de généricité** ⟹ test §2-**(c)** non satisfait. Et conclure `ρ=0` en **posant**
l'additivité de silence comme prémisse = **d1 (relier≠ancrer)**. ⟹ dans les deux cas, **pas d'ancrage** de
`ρ=0`.

## 4. Cross-check numérique `[C1–C3 — O-ρ-num, standing plein]`

Les numériques génériques 3D vides sans symétrie (C1 Garfinkle) **confirment** le tableau BKL local-oscillatoire
**et voient** des spikes ; les numériques G₂ (C2) et les oscillations/statistiques de spikes (C3)
**caractérisent** la récurrence. **Mais** la résolution des **échelles fines** — précisément celles qui
décideraient le **canal multiplicatif** — est **limitée** (spikes notoirement sous-résolus) ⟹ instabilité
attendue sous raffinement = test §2-**(a)**. Le cross-check **ne lève pas** l'indétermination. **Standing
plein** : il n'infirme pas non plus un ρ=0 ; il **ne rétrograde pas** — il **corrobore l'indétermination**,
il ne la masque pas.

## 5. Classification CANDIDATE `[espace-verdict §4, gel 478be3ac — CITÉ inchangé]`

**V3 · INDÉTERMINÉ / OA-GATED** *(candidat, gaté CSE-5)*. `ρ` **non fixé univoquement** par la seule
dynamique générique 3D : écart de généricité (G₂/Gowdy → 3D-générique, test §2-c) + numériques
résolution-limités (test §2-a). ⟹ **délimitation, AUCUNE tranche** ; **I-c-conditionnel** ;
`{A4 ; A2★ ; N}` **INCHANGÉ**.

- **Ni V1 ni V2 ancrés.** V1 (ρ=0) sur-étendrait le résultat symétrie-réduit (généricité) ou réimporterait
  la prémisse additive (d1). V2 (ρ>0) exigerait une prolifération à échelle fine que les numériques
  ne **résolvent pas**.
- **Lean NON-PORTEUR consigné** (n'est **pas** une tranche) : l'argument structurel (silence asymptotique +
  récurrence à surfaces fixes) **penche** vers ρ=0 (canal additif), mais **ne peut être ancré** pour le 3D
  pleinement générique sans franchir l'écart de généricité ni réimporter une prémisse. Consigné pour tracer,
  **jamais** propagé comme verdict.
- **d1** respecté (aucune injection de l'additivité mésoscopique ni de la conclusion `Q` sous-exp comme
  prémisse) · **d3** respecté (proxy scellé `verif_A2_numerique` hors-jeu) · **généricité** : les inputs
  porteurs disponibles sont symétrie-réduits (non génériques) — d'où précisément le V3.

**OA gaté (ce qui déplacerait V3 → tranche)** : **OA-1** un résultat rigoureux de multiplicité des lieux de
spike en 3D **pleinement générique** (fermant l'écart G₂/Gowdy → générique), OU **OA-2** des numériques
génériques 3D **résolvant les échelles fines** (test §2-a satisfait). Aucun n'est dans le périmètre gelé.

## 6. Gate CSE-5 `[pilote disqualifié — OBLIGATOIRE avant toute gravure]`

Ce verdict est **CANDIDAT**. Le **pilote (cette instance) est DISQUALIFIÉ** pour adjuger la substance. Avant
toute gravure ou propagation : **audit froid incognito souverain CSE-5** (Mode A **zéro-fuite** — paquet
**SANS** zone opérateur nommant le verdict, sans induire l'auditeur ; **l'incognito prévaut** sur le pilote).
Le paquet zéro-fuite fournira à l'incognito : imports gelés CSE-4 (I1–I3, C1–C3), estimateur §2, espace-verdict
{V1/V2/V3}, **sans** révéler la classification candidate. Puis **CSE-6** : si un verdict de substance est
confirmé, nommage `établi (physique externe, sous hypothèses H)` — **jamais** « CCC vraie » ni « A2★ tranchée »
nue. **Tant que CSE-5 n'a pas statué, `{A4;A2★;N}` est porté INCHANGÉ ; rien n'est gravé.**

## 7. Non-surclassement `[§6.4]`

Un **candidat V3** ne scelle, ne réduit, ne compte, ne démontre **RIEN**. Même un V3 confirmé serait une
**délimitation** (I-c-conditionnel), pas une réduction. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; `N` non
fixé (≡`Λ`) ; A4 non réduit ; **A2★ non tranché** ; O₂ non construit ; β **T-b** ; **CCC non démontrée NI
réfutée**. La valeur ajoutée éventuelle (si V3 confirmé CSE-5) = **délimitation plus fine** de la maille
non-cascade (obstruction = écart de généricité + résolution), **pas** un résultat de substance sur la CCC.

*(R-36 : ce fichier n'embarque pas son propre sha. R-54 : mount autoritaire. Estimateur §2 validé bien-posé
sur données synthétiques — aucune mesure physique de ρ n'est revendiquée ici ; la substance est la dérivation
analytique §1–§3 et son cross-check §4.)*
