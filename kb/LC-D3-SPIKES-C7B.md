---
id: LC-D3-SPIKES-C7B
titre: "Front (a)/GWE — C7-b (rétro-action des spikes), VOIE 1 EXÉCUTÉE : assemblage de R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk sur l'oracle de Gauss-Kuzmin scellé. Successeur de résultat de LC-D3-SILENCE-POC §II (cadrage C7-b) et compagnon de LC-WORK-BIBLIO-SPIKES-C7B. RÉSULTAT : deux des trois facteurs de R_s sont bornés/clos — (i) la carte de spike = carte BKL² (Heinzle-Uggla 1212.5500), donc la statistique des spikes vit dans la MÊME machinerie de fractions continues que notre oracle (LC-D3-INTERAEON-P6) ; (ii) l'amplitude α_s est BORNÉE (Weyl Hubble-normalisé W²_K≤12, compacité) ⟹ « α_s→∞ » exclu ; (iii) la statistique MOYENNÉE d'une timeline de spike = celle du bulk (Théorème 3.2 : ⟨W²_K⟩→C/log₂n, MÊME C≈19.58 pour spike et BKL) ⟹ α_s(moyenné)→1. D'où R_s = μ_s(α_s−1) → 0 INDÉPENDAMMENT de μ_s : les spikes NE SUR-SOURCENT PAS ⟨Ω_σ⟩. Le non-sequitur « mesure nulle ⟹ négligeable » est remplacé par ce résultat positif. RÉSIDU : le seul secteur non borné est le NON-LOCAL/gradient (spikes super-horizon, 0710.0628 éq.43), genuinement inhomogène ⟹ voie 2. STATUT C7-b : `formalisable` → PASS PARTIEL. Sceau verif_D3_C7b_spikes.py."
codename: LC-RACCORD
type: note de résultat (chaînon) — consigne l'exécution de la voie 1 de C7-b (LC-D3-SILENCE-POC §II). Subordonnée à la discipline LC-AUDIT-VERDICT §6.4.
version: 1.2
langue: fr
date: 2026-06-08
portee: "Consigne UNIQUEMENT le delta : la VOIE 1 de C7-b est codée, exécutée, PASS PARTIEL. Borne deux des trois facteurs de R_s (α_s, statistique=bulk) sur l'oracle scellé ; isole le résidu (gradient non-local). Ne refait NI la statistique de spikes (1212.5500), NI l'oracle (LC-D3-INTERAEON-P6), NI le pont ⟨Ω_σ⟩_bulk (LC-D3-WCH-GWE). Discipline §6.4 : sceau STATISTIQUE/ALGÉBRIQUE — il borne, il ne PROUVE pas C7-b ; le secteur non-local reste `décision ouverte`. C7 reste `formalisable (borné)` ; (A) physique conditionnel."
prerequis_kb: [LC-D3-SILENCE-POC, LC-WORK-BIBLIO-SPIKES-C7B, LC-D3-INTERAEON-P6, LC-D3-WCH-GWE, LC-WORK-C7-POC-SILENCE, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_C7b_spikes.py, verif_D3_P6_specB_oracle.py, verif_D3_A_horizon.py, verif_D3_B_curvature.py, verif_D3_C_decoupling.py]
source_externe: ["Heinzle-Uggla, Spike statistics, GRG 45 939 (2013), arXiv:1212.5500 (carte spike=BKL² éq.9 ; distribution K̄(m)=log₃ éq.17 ; Weyl W²_K éq.25 ; Théorème 3.2 ⟨W²_K⟩→19.58/log₂n, même C pour BKL et spike). Lim, New explicit spike solution, CQG 25 045014 (2008), arXiv:0710.0628 (profil de spike borné ; rayon super-horizon éq.43). Heinzle-Uggla-Lim, Spike oscillations, PRD 86 104049 (2012), arXiv:1206.0932 (localité brisée sur surfaces de spike). Tous en KB (LC-WORK-BIBLIO-SPIKES-C7B v1.1)."]
tags_epistemiques: [établi, formalisable, à inventer, décision ouverte]
---

# C7-b (rétro-action des spikes), voie 1 — assemblage de R_s

> **But.** Consigner l'exécution de la **voie 1** du cadrage de C7-b (`LC-D3-SILENCE-POC §II`) :
> assembler `R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk` à partir de la statistique des spikes
> (`LC-WORK-BIBLIO-SPIKES-C7B`), **en la raccordant à l'oracle de Gauss-Kuzmin scellé**
> (`LC-D3-INTERAEON-P6`). Discipline `LC-AUDIT-VERDICT §6.4` : sceau statistique/algébrique —
> il **borne**, il ne **prouve** pas C7-b.

---

## 0. État en une ligne `[résultat]`

La voie 1 est **PASS PARTIEL** : sur les **trois** facteurs de `R_s`, **deux sont
bornés/clos** par l'oracle scellé — (i) **amplitude** `α_s` **bornée** (Weyl Hubble-normalisé
`W²_K≤12`, compacité ⟹ « α_s→∞ » **exclu**) ; (ii) **statistique moyennée** d'une timeline de
spike **= celle du bulk** (Théorème 3.2 : même constante `C≈19.58`) ⟹ `α_s(moyenné)→1`. D'où
**`R_s = μ_s(α_s−1) → 0` indépendamment de μ_s** : les spikes **ne sur-sourcent pas**
`⟨Ω_σ⟩`. Le non-sequitur « mesure nulle ⟹ négligeable » est **remplacé** par ce résultat
positif. **Résidu** : le seul secteur non borné est le **non-local/gradient** (spikes
super-horizon), genuinement inhomogène ⟹ **voie 2**. **C7-b** : `formalisable` → **PASS
PARTIEL**.

---

## 1. Le raccord à l'oracle `[établi (sceau) — verif_D3_C7b_spikes.py §1]`

`Spike statistics` (1212.5500) établit que les spikes induisent des séquences de Kasner
régies par la **carte de spike = carte BKL appliquée deux fois** (éq.9, `u₊=f(f(u₋))`). Or la
carte BKL `u↦u−1 (u≥2) ; u↦1/(u−1) (u∈[1,2])` **est** la carte de notre oracle
(`verif_D3_P6_specB_oracle.py`, `LC-D3-INTERAEON-P6`). Le sceau retrouve numériquement les
deux distributions d'ère :
- **BKL** ↦ Khinchin/Gauss-Kuzmin `K(m)=log₂((m+1)/(m+2))−log₂(m/(m+1))` (éq.7) : empirique
  `K(1)=0.414` vs théorie `0.415`.
- **spike** ↦ `K̄(m)=log₃((m+2)/(m+3))−log₃(m/(m+1))` (éq.17) : empirique `K̄(1)=0.368` vs
  théorie `0.369`.

⟹ **Les spikes vivent dans la même machinerie de fractions continues que l'oracle scellé.**
L'hypothèse la plus fragile du cadrage (`LC-D3-SILENCE-POC §clôture` : « l'oracle homogène
peut-il livrer une mesure de spikes ? ») est ainsi **étayée par construction** : la
statistique des spikes EST une statistique de Gauss-Kuzmin.

---

## 2. Les trois facteurs de `R_s` `[formalisable]`

Décomposition (`LC-D3-SILENCE-POC §5`), avec le **Weyl Hubble-normalisé**
`W²_K=81u²(1+u)²/(1+u+u²)³` (1212.5500 éq.25) comme **proxy invariant du cisaillement/courbure
dans le régime de silence (deep-bang)** :
```
⟨Ω_σ⟩_total = (1−μ_s)·⟨Ω_σ⟩_bulk + μ_s·α_s·⟨Ω_σ⟩_bulk = ⟨Ω_σ⟩_bulk·(1 + μ_s(α_s−1))
```

**(a) α_s instantané — BORNÉ `[établi (sceau) §2]`.** `W²_K` plafonne à **12** (à `u=1`) et →0
quand `u→∞`. Par **compacité de l'espace d'états de Kasner**, un spike ne peut pas amplifier
le cisaillement/Weyl Hubble-normalisé sans borne : le scénario dangereux **« α_s→∞ » est
EXCLU**. *C'est la réfutation quantitative du non-sequitur « mesure nulle ⟹ négligeable » : ce
n'est pas la mesure qui sauve, c'est la borne d'amplitude.*

**(b) α_s moyenné — → 1 `[établi (sceau) §3, d'après Th.3.2]`.** Théorème 3.2 de 1212.5500 :
la moyenne d'ère `⟨W²_K⟩_n → C/log₂(n)` avec `C≈19.58`, **et la MÊME constante pour les
séquences BKL ET spike**. Le sceau le confirme : `⟨W²_K⟩·log₂n` plafonne à `~20` pour les
deux, ratio `⟨W²_K⟩_spike/⟨W²_K⟩_bulk = 0.91` (→1, voire légèrement **<1** car les eras de
spike sont plus courtes ⟹ plus de temps à grand `u` ⟹ Weyl plus petit). ⟹ Une timeline de
spike porte la **même** statistique de cisaillement moyennée que le bulk : `α_s(moyenné)→1`.

**(c) Assemblage.** Avec `α_s→1` : `⟨Ω_σ⟩_total ≈ ⟨Ω_σ⟩_bulk` et
**`R_s = μ_s(α_s−1) → 0`, INDÉPENDAMMENT de μ_s**. Les spikes ne créent **aucun excès** de
cisaillement moyenné : ils ne sur-sourcent pas `⟨Ω_σ⟩`.

---

## 3. Le résidu : le secteur non-local `[décision ouverte → voie 2]`

La voie 1 ne borne pas **un** facteur : l'**énergie de gradient / non-localité** des spikes.
Les spikes sont des structures **super-horizon** — rayon `= cosh(wτ)×`(rayon d'horizon)
(0710.0628 éq.43) ; la « localité asymptotique » est **brisée sur les surfaces de spike**
(1206.0932). Cet effet n'est **pas** une amplitude moyennée (que §2 borne) ni une mesure
statistique (que §1 livre) : c'est un terme de **gradient spatial** (`∂_a` aux surfaces), qui
échappe par construction à la statistique de Kasner (laquelle vit *le long* d'une timeline,
pas *entre* timelines). ⟹ **Seul secteur non clos par la voie 1.** Il relève de la **voie 2**
(probe inhomogène 1D explicite, type Garfinkle) ou d'un **théorème de mesure/largeur** des
surfaces de spike (que la littérature n'établit pas dans le cas pleinement générique).

> **Nuance physique (à creuser en voie 2).** Le caractère super-horizon coupe dans les deux
> sens : à l'échelle d'un horizon, un spike varie **peu** (sa structure fine est à `±1/k`,
> super-horizon) ⟹ gradients locaux **doux** ; mais l'intégrale sur la surface peut compter.
> La voie 1 ne tranche pas — elle **isole** proprement la question.

> **MàJ voie 1.5 — gradient non-local BORNÉ sur le profil exact (`LC-D3-GRADIENT-C7B`, sceau
> `verif_D3_C7b_gradient.py`).** La « nuance physique » ci-dessus est **tranchée** : sur la
> solution de spike EXACTE de Lim (0710.0628), l'énergie de gradient en unités d'horizon vaut
> `I_spike(τ)=2π·A²·w/cosh(wτ) → 0` (super-horizon ⟹ gradient Hubble-normalisé **doux** ;
> l'intégrale sur la largeur ne le compense pas). Pondérée par la statistique `log₃` scellée,
> `⟨Ω_σ^grad⟩/⟨Ω_σ⟩_bulk → 0` robuste. ⟹ le résidu n'est plus « le secteur non-local » en bloc
> mais le seul cas **pleinement générique** (sans symétrie), `décision ouverte`. La voie 2 (Gowdy
> PDE) est **redondante** (même classe G₂/Gowdy). **C7-b : PASS PARTIEL → PASS SUBSTANTIEL** (3/3
> facteurs bornés sur profil exact).
>
> **MàJ voie A1/A2 — le résidu générique réduit au seul facteur A2 (`LC-D3-A1-SUPERHORIZON`,
> `LC-D3-C7B-VERDICT-A2`).** A1 (sceau `verif_D3_C7b_A1_superhorizon.py`, 10/10) établit que
> l'énergie de gradient **par spike** est bornée **en générique** — pas seulement sur le profil
> exact : `I(ℓ)=C_F/ℓ`, scaling `1/ℓ` **indépendant du profil** (le profil n'entre que par
> `C_F=∫F'²du`), éteint par le silence (`ℓ→∞`). ⟹ le résidu « cas pleinement générique » n'est
> plus le **gradient** mais le **seul facteur A2** : la **mesure de spikes générique** `n_s^gen(τ)`,
> dont la borne sous-exponentielle est **attendue physiquement** (bounces BKL ~ linéaires) mais
> **non prouvée** (Garfinkle `gr-qc/0312117` : « work in progress »). A2 : `à inventer` / `hors de
> portée`. **C7-b reste PASS SUBSTANTIEL (renforcé par A1)** ; résidu = A2 seul. Discipline §6.4 :
> l'attente physique n'est **pas scellée**.

---

## 4. Statut de C7-b et de C7 `[bilan]`

| Facteur de `R_s` | Statut après voie 1 | Source |
|---|---|---|
| Mesure μ_s (statistique) | `formalisable` — machinerie Gauss-Kuzmin de l'oracle | §1 |
| Amplitude α_s (instantanée) | **borné** `établi (sceau)` — `W²_K≤12` | §2a |
| Amplitude α_s (moyennée) | **→1** `établi (sceau)` — spike≡bulk (Th.3.2) | §2b |
| **Gradient non-local (profil exact)** | **borné** `établi (sceau)` — `I_spike→0`, ratio→0 | §3, LC-D3-GRADIENT-C7B |
| *résidu : mesure de spikes générique `n_s^gen` (facteur A2)* | **`décision ouverte`** | `LC-D3-C7B-VERDICT-A2` (gradient/spike borné en générique par A1, `LC-D3-A1-SUPERHORIZON`) |

- **C7-b** : `formalisable` → **PASS PARTIEL**. La rétro-action en **amplitude/statistique**
  est **close** (`R_s→0`) ; reste le **secteur non-local**.
- **C7** : reste `formalisable (borné)`. Réduction nette : C7 = C7-a (`formalisable`, =
  dichotomie WCH scellée pointwise, `LC-D3-SILENCE-POC §2`) + C7-b, dont **deux tiers** sont
  désormais bornés.
- **(A) physique** : reste `formalisable`, conditionnel au **seul** secteur non-local de C7-b
  (+ C7-a pointwise, cadre CCC). Si la voie 2 borne le gradient non-local ⟹ **C7 levée** ⟹
  **(A) `établi (sous WCH/A3-A4, CCC)`** ⟹ front (a) clos par la physique.

---

## 5. Discipline et réserves de méthode `[méta — §6.4]`

- **Sceau = statistique/algèbre.** `verif_D3_C7b_spikes.py` est `établi (sceau)` : cartes,
  distributions, borne `W²_K≤12`, égalité spike≡bulk. Il **ne prouve pas** C7-b ; le secteur
  non-local reste ouvert. C7 levée **seulement** sous preuve conjointe : silence (A∧B∧C) ∧ WCH
  pointwise (C7-a) ∧ spikes négligeables (C7-b = amplitude ✓ + statistique ✓ + **gradient
  non-local [à prouver]**).
- **Réserve numérique.** La reproduction de la constante donne `⟨W²_K⟩·log₂n ≈ 20–22` vs
  `19.58` du papier — écart dû à la normalisation « par époque » (proxy) du sceau au lieu du
  poids exact « par ère ». Le résultat **qualitatif + semi-quantitatif** (borné, décroissant,
  spike≈bulk, ratio≈0.91) est robuste ; la 8ᵉ décimale ne l'est pas (et n'est pas requise).
- **Réserve de régime.** `W²_K` est le cisaillement/Weyl **deep-bang** Hubble-normalisé ; le
  transport jusqu'au crossover GWE (où `⟨Ω_σ⟩_bulk=(kη)⁴ε²/27`, `LC-D3-WCH-GWE`) reste la
  machinerie P6/WCH-GWE existante. La voie 1 montre que les spikes n'ajoutent **pas de source**
  deep-bang en moyenne ; elle ne re-dérive pas le transport.

---

## 6. Propagation suggérée `[à faire — housekeeping, hors de cette note]`

`00-INDEX` (ajout de `LC-D3-SPIKES-C7B` ; bump) ; `LC-D3-SILENCE-POC` §II (marquer voie 1
EXÉCUTÉE, renvoyer ici) ; `LC-D3-WCH-GWE` §6 (C7-b : amplitude/statistique closes, résidu
non-local) ; `LC-AUDIT-VERDICT` §8bis (enregistrer voie 1 PASS partiel, sans surclassement) ;
`LC-03-GLOSSAIRE` (entrées α_s / μ_s / R_s / secteur non-local).

---

## Appendice — chiffres scellés (à ne pas re-prouver)

- **§1 raccord** : BKL `K(1)`emp `0.414` / théo `0.415` ; spike `K̄(1)`emp `0.368` / théo
  `0.369` (carte spike=BKL²).
- **§2a amplitude** : `max W²_K = 12.0` à `u=1` ; `W²_K(2)=8.50`, `W²_K(10)=0.72` ; →0.
- **§2b/§3 moyenne** : `⟨W²_K⟩·log₂n ≈ 20` (BKL et spike) ; ratio spike/bulk `= 0.91 → 1`.
- **R_s** = `μ_s(α_s−1) → 0` (α_s→1) ⟹ `⟨Ω_σ⟩_total ≈ ⟨Ω_σ⟩_bulk`.

**Tags.** Raccord oracle, bornes α_s, statistique=bulk : `établi (sceau)`. Mesure μ_s
statistique : `formalisable`. R_s amplitude/statistique → 0, gradient profil exact ✓, gradient/spike générique ✓ (A1) : **C7-b PASS SUBSTANTIEL**. Résidu = **mesure A2** `n_s^gen` (`LC-D3-C7B-VERDICT-A2`) : `décision ouverte` / `hors de portée` (voie 2 redondante). C7 : `formalisable (borné)`. (A) physique :
`formalisable`, conditionnel. *Discipline §6.4 maintenue.*
