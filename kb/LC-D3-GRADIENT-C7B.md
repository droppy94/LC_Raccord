---
id: LC-D3-GRADIENT-C7B
titre: "Front (a)/GWE — C7-b (rétro-action des spikes), VOIE 1.5 EXÉCUTÉE : l'énergie de gradient NON-LOCALE des spikes, calculée semi-analytiquement sur la SOLUTION DE SPIKE EXACTE de Lim (0710.0628 §4.5-4.6) et pondérée par la statistique log₃ scellée. RÉSULTAT : l'énergie de gradient d'un spike, en unités d'horizon, vaut I_spike(τ)=2π·A(τ)²·w/cosh(wτ) → 0 (exponentiel ~e^{−|w|τ}) ; même sup_w I_spike(τ)~O(1/τ)→0 ; le ratio ⟨Ω_σ^grad⟩_spikes/⟨Ω_σ⟩_bulk → 0 pour toute densité de spikes bornée ou en prolifération polynomiale. Le casser exigerait une prolifération EXPONENTIELLE de spikes (n_s~e^{+|w|τ}), non supportée (bounces BKL ~ linéaires). ⟹ le SEUL facteur résiduel de la voie 1 (gradient non-local) est BORNÉ sur le profil exact. Sceau verif_D3_C7b_gradient.py (19/19 PASS, vérifs symboliques+numériques). RÉSERVE : sceau semi-analytique sur la solution EXACTE (G₂/Gowdy, un gradient spatial) ; le cas pleinement générique (sans symétrie, gradients multiples) reste `décision ouverte`. STATUT C7-b : PASS PARTIEL → PASS SUBSTANTIEL (3/3 facteurs bornés sur le profil exact)."
codename: LC-RACCORD
type: note de résultat (chaînon) — consigne l'exécution de la voie 1.5 de C7-b (LC-WORK-REPRISE-C7B-VOIE2 §3, Tâche 1). Subordonnée à la discipline LC-AUDIT-VERDICT §6.4.
version: 1.1
langue: fr
date: 2026-06-08
portee: "Consigne UNIQUEMENT le delta : la VOIE 1.5 de C7-b est codée, exécutée, et borne le SEUL facteur que la voie 1 laissait ouvert — l'énergie de gradient non-locale — sur la solution de spike EXACTE de Lim. Ne refait NI la statistique de spikes (1212.5500, voie 1), NI l'oracle (LC-D3-INTERAEON-P6), NI le pont ⟨Ω_σ⟩_bulk (LC-D3-WCH-GWE), NI l'amplitude α_s (voie 1). Discipline §6.4 : sceau SEMI-ANALYTIQUE — il borne le gradient pour le profil exact (un gradient spatial, classe G₂/Gowdy) ; il NE PROUVE PAS le cas pleinement générique. C7-b : PASS substantiel ; C7 reste `formalisable (borné)` ; (A) physique conditionnel."
prerequis_kb: [LC-D3-SPIKES-C7B, LC-D3-SILENCE-POC, LC-WORK-BIBLIO-SPIKES-C7B, LC-WORK-REPRISE-C7B-VOIE2, LC-D3-INTERAEON-P6, LC-D3-WCH-GWE, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_C7b_gradient.py, verif_D3_C7b_spikes.py, verif_D3_P6_specB_oracle.py]
source_externe: ["Lim, New explicit spike solution — non-local component of the generalized Mixmaster attractor, CQG 25 045014 (2008), arXiv:0710.0628 (§4.5 profil exact c(x)=(u²−1)/(u²+1), s(x)=2u/(u²+1), u=kx, k=w·e^τ·sech(wτ), éq.36-39 ; §4.6 rayon du spike éq.41-43 : rayon/horizon=(1/w)cosh(wτ), super-horizon ∀τ pour 0<|w|<1). Heinzle-Uggla, Spike statistics, arXiv:1212.5500 (distribution log₃ K̄(m) éq.17, carte BKL² — déjà scellée voie 1). Tous en KB (LC-WORK-BIBLIO-SPIKES-C7B v1.1)."]
tags_epistemiques: [établi, formalisable, à inventer, décision ouverte]
---

# C7-b (rétro-action des spikes), voie 1.5 — l'énergie de gradient non-locale

> **But.** Consigner l'exécution de la **voie 1.5** (`LC-WORK-REPRISE-C7B-VOIE2 §3`) :
> calculer l'**énergie de gradient NON-LOCALE** d'un spike — le seul facteur de `R_s` que la
> voie 1 (`LC-D3-SPIKES-C7B`) laisse ouvert — **analytiquement, sur la solution de spike
> EXACTE de Lim** (`0710.0628`), puis la pondérer par la **statistique de spikes scellée**.
> Discipline `LC-AUDIT-VERDICT §6.4` : sceau **semi-analytique** — il borne le gradient pour le
> **profil exact**, il ne **prouve pas** le cas pleinement générique.

---

## 0. État en une ligne `[résultat]`

La voie 1.5 **borne le facteur résiduel**. Sur la solution de spike exacte, l'énergie de
gradient non-locale d'un spike — en unités d'horizon (la mesure physiquement pertinente) — vaut
```
I_spike(τ) = 2π · A(τ)² · w/cosh(wτ)  →  0   (décroissance exponentielle ~ e^{−|w|τ})
```
et même, optimisé sur `w`, `sup_w I_spike(τ) ~ O(1/τ) → 0`. Pondéré par la densité de spikes
(statistique `log₃` scellée), **bornée ou même en prolifération polynomiale**, le ratio
`⟨Ω_σ^grad⟩_spikes/⟨Ω_σ⟩_bulk → 0`. **Le casser exigerait une prolifération EXPONENTIELLE de
spikes** (`n_s~e^{+|w|τ}`), non supportée. ⟹ **C7-b : PASS PARTIEL → PASS SUBSTANTIEL** (les
**trois** facteurs de `R_s` bornés *sur le profil exact*). **Réserve honnête** : sceau sur la
solution **EXACTE** (classe G₂/Gowdy, **un** gradient spatial) ; le cas **pleinement générique**
(sans symétrie) reste `décision ouverte`.

---

## 1. Le profil exact et l'observable `[établi (sceau) — verif_D3_C7b_gradient.py §0-§2]`

**Profil (Lim 0710.0628 §4.5).** Toute la dépendance spatiale des variables β-normalisées du
spike `(Σ−,N×,Σ×,N−)` (éq.36) est portée par deux fonctions (éq.37-38), avec `u=kx` :
```
c(u) = (u²−1)/(u²+1)   (pic en u=0, zéros en u=±1)
s(u) = 2u/(u²+1)       (zéro en u=0, pics opposés en u=±1)
```
Le sceau vérifie symboliquement `c²+s²=1` : `(c,s)` est une **rotation de repère** (les spikes
sont des structures de repère, pas d'amplitude — cohérent avec voie 1). L'échelle est
`k=w·e^τ·sech(wτ)` (éq.32/39) ; en coordonnée **horizon-normalisée** `X=e^τ x` (éq.44, horizon
à `X=±1`), `u=κ(τ)·X` avec `κ(τ)=w·sech(wτ)=w/cosh(wτ)`.

**Énergie de gradient.** La densité de gradient du profil, réduite **symboliquement** :
```
g(u) = (dc/du)² + (ds/du)² = 4/(1+u²)²        ∫_{−∞}^{+∞} g(u) du = 2π
```
La contribution de gradient Hubble-normalisée (par horizon) d'un spike s'intègre alors en forme
**close** (validée contre quadrature directe ∀`w,τ` testés) :
```
I_spike(τ) = ∫ (∂_X champ)² dX = A(τ)²·κ·∫g du = 2π·A(τ)²·κ(τ)
```
où `A(τ)² = Σ−²_Taub + N−²_Taub` (éq.27) est l'**amplitude bornée** (max `A²=3.33`, →`(w−1)²/3`),
le même facteur que la voie 1 borne (`α_s` borné).

---

## 2. Le résultat : le gradient s'éteint `[établi (sceau) §3-§4]`

**Décroissance.** `κ(τ)=w/cosh(wτ) → 0` ⟹ `I_spike(τ) → 0`, **exponentiellement au taux `|w|`**
(vérifié numériquement : taux=0.500 pour `w=0.5`). Pour les spikes **super-horizon** `0<|w|<1`
(rayon/horizon `=(1/w)cosh(wτ)≥1/w>1`, éq.43), la décroissance est monotone vers 0.

**Pire cas sur `w`.** `f(w)=w/cosh(wτ)` est maximal à `coth(wτ)=wτ` (`y*≈1.1997`), donnant
`sup_w I_spike(τ) ≈ 2π·A²·0.66/τ ~ O(1/τ) → 0`. **Même le `w` le plus défavorable décroît.**

**Physique (la nuance du §3 de SPIKES-C7B, tranchée).** Le caractère super-horizon « coupe dans
les deux sens » : structure fine à `±1/k`, mais largeur `≫` horizon. Le calcul tranche : à
l'échelle de l'horizon le champ varie **peu** ⟹ gradient Hubble-normalisé **doux** (`∝κ`), et
l'intégrale sur la largeur **ne le compense pas** (`I_spike∝κ→0`). *Le gradient local doux
l'emporte sur l'extension super-horizon.*

---

## 3. Pondération par la statistique de spikes `[établi (sceau) §5-§6]`

Le ratio cherché est `R_grad = n_s · I_spike(τ) / ⟨Ω_σ⟩_bulk`, où `n_s` = nombre de spikes
**actifs par horizon** et `⟨Ω_σ⟩_bulk=O(1)`. Le sceau retrouve la distribution d'ère scellée
(Heinzle-Uggla éq.17, normalisée, `K̄(1)=0.369` — raccord exact à la voie 1) et teste `R_grad`
sous trois modèles de densité :

| densité de spikes `n_s` | `R_grad(τ=40)`, `w=0.5` | verdict |
|---|---|---|
| constante (recurrence stationnaire) | `6·10⁻⁹` | → 0 |
| linéaire `~(1+τ)` (prolifération) | `3·10⁻⁷` | → 0 |
| cubique `~(1+τ)³` (très généreuse) | `4·10⁻⁴` | → 0 |

**Stress-test.** Pour maintenir `R_grad~O(1)` il faudrait `n_s ~ e^{+|w|τ}` — une prolifération
**exponentielle** de spikes (taux requis vérifié `≈|w|`). Or le nombre de bounces BKL jusqu'à `τ`
croît **~linéairement** (statistique de Gauss-Kuzmin), **pas** exponentiellement. ⟹ aucune
prolifération supportée par la littérature ne défait la décroissance. **`R_grad → 0` robuste.**

---

## 4. Statut de C7-b et de C7 `[bilan]`

| Facteur de `R_s` | Statut après voie 1 | Statut après **voie 1.5** | Source |
|---|---|---|---|
| Mesure `μ_s` (statistique) | `formalisable` (Gauss-Kuzmin) | inchangé | §1 voie1 |
| Amplitude `α_s` (instantanée) | **borné** `W²_K≤12` | inchangé | §2a voie1 |
| Amplitude `α_s` (moyennée) | **→1** (spike≡bulk) | inchangé | §2b voie1 |
| **Gradient non-local** | `décision ouverte` | **BORNÉ (profil exact)** → `établi (sceau)` | **ici** |
| *résidu* : mesure de spikes générique `n_s^gen` (facteur A2) | — | **`décision ouverte`** | A1 a borné le gradient/spike générique (`LC-D3-A1-SUPERHORIZON`) ; verdict A2 : `LC-D3-C7B-VERDICT-A2` |

- **C7-b** : `PASS PARTIEL` → **PASS SUBSTANTIEL**. Les **trois** facteurs de `R_s` sont bornés
  *sur le profil de spike exact* ; le résidu n'est plus « le secteur non-local » en bloc, mais
  le seul **cas pleinement générique** (multi-gradient, sans symétrie).
- **C7** : reste `formalisable (borné)`. Réduction nette : `C7 = C7-a` (`formalisable`, dichotomie
  WCH pointwise) `+ C7-b` (amplitude ✓, statistique ✓, gradient ✓ *sur profil exact* ; reste le
  générique).
- **(A) physique** : reste `formalisable`, conditionnel au **résidu générique** de C7-b
  (+ C7-a pointwise, cadre CCC). **Si** le cas générique était borné ⟹ **C7 levée** ⟹
  **(A) `établi (sous WCH/A3-A4, CCC)`** ⟹ front (a) clos par la physique.

---

## 5. La voie 2, et ce qui reste `[décision ouverte — discipline]`

**La voie 1.5 rend la voie 2 (Gowdy PDE) largement redondante** : la solution exacte de Lim
**est** une solution G₂/Gowdy (un gradient spatial), et un solveur PDE Gowdy
(`LC-WORK-REPRISE-C7B-VOIE2 §4`) confirmerait la même **classe de symétrie**. Le calcul
analytique sur le profil exact est plus fort qu'un solve numérique sur la même classe (pas de
problème de résolution des spikes qui se raidissent — l'écueil noté en §4 de la reprise). ⟹ la
voie 2 n'ajouterait pas de borne nouvelle ; elle vérifierait ce que la voie 1.5 a déjà établi.

**Le résidu honnête** est le cas **pleinement générique** (sans symétrie, gradients spatiaux
multiples), que **ni la voie 1.5 ni la voie 2** (toutes deux G₂/Gowdy) n'atteignent — et que la
**littérature elle-même** ne ferme pas (`LC-WORK-BIBLIO-SPIKES-C7B §F` : mesure de spikes
générique partiellement ouverte). C'est un **héritage d'ouverture** assumé, pas un échec :
`décision ouverte` / possiblement `hors de portée`.

> **MàJ voie A1/A2 — le résidu n'est plus le gradient mais la mesure A2 (`LC-D3-A1-SUPERHORIZON`,
> `LC-D3-C7B-VERDICT-A2`).** A1 (sceau `verif_D3_C7b_A1_superhorizon.py`, 10/10) **généralise** le
> présent résultat : l'énergie de gradient **par spike** est bornée **sans profil exact** —
> `I(ℓ)=C_F/ℓ`, scaling `1/ℓ` **profil-indépendant** (le profil n'entre que par `C_F=∫F'²du`),
> éteint par le silence (`ℓ→∞`), y compris pour les profils **multi-gradient à spectre comobile
> fixe** (la réserve ci-dessus). ⟹ le résidu générique se réduit au **seul facteur A2** — la
> **mesure de spikes générique** `n_s^gen(τ)` : `R_grad,gen=n_s^gen·I_spike^gen→0` **dès que**
> `n_s^gen` croît plus lentement que `e^{|w|τ}` (condition faible). A2 est **attendue** (bounces
> BKL ~ linéaires) mais **non prouvée** (Garfinkle `gr-qc/0312117`) ⟹ `à inventer` / `hors de
> portée`. **C7-b reste PASS SUBSTANTIEL (renforcé par A1)** ; (A) physique conditionnel au **seul
> A2**. Discipline §6.4 : l'attente physique n'est **pas scellée**.

> **Sans surclassement (§6.4).** Le sceau est `établi (sceau)` = « l'énergie de gradient du
> profil EXACT → 0, ratio borné ». Il ne dit PAS « C7 est levée » ni « la physique de la CCC est
> établie ». C7 levée resterait conditionnelle à : silence (A∧B∧C) ∧ WCH pointwise (C7-a) ∧
> spikes négligeables (amplitude ✓ + statistique ✓ + gradient ✓ *profil exact* + **générique [à
> faire]**). « Le bang gagne » (P6 B) intact.

---

## 6. Propagation suggérée `[à faire — housekeeping, hors de cette note]`

`00-INDEX` (ajout de `LC-D3-GRADIENT-C7B` ; bump) ; `LC-D3-SPIKES-C7B` §3 (marquer voie 1.5
EXÉCUTÉE, gradient borné sur profil exact, renvoyer ici) ; `LC-WORK-REPRISE-C7B-VOIE2` §6
(Tâche 1 exécutée) ; `LC-D3-WCH-GWE` §6.2 (C7-b : 3/3 facteurs bornés sur profil exact, résidu =
générique) ; `LC-AUDIT-VERDICT` §8bis (enregistrer voie 1.5, sans surclassement) ;
`LC-03-GLOSSAIRE` (entrées *énergie de gradient non-locale* / *profil exact de Lim* / *I_spike*).

---

## Appendice — chiffres scellés (à ne pas re-prouver)

- **§1 profil** : `c²+s²=1` ; `g(u)=(c')²+(s')²=4/(1+u²)²` ; `∫g du=2π` (tous symboliques).
- **§2 spike** : `I_spike(τ)=2π·A²·w/cosh(wτ)` (forme close validée vs quadrature, rel.err<1e−6) ;
  `max A²=3.33` (borné) ; décroissance exponentielle taux `=|w|`.
- **§4 pire cas** : `coth(y)=y → y*=1.1997` ; `sup_w I_spike ≈ 0.66/τ → 0`.
- **§5 ratio** : `Σ K̄(m)=1` ; `K̄(1)=0.369` ; `R_grad(40)=6·10⁻⁹` (n_s const), `4·10⁻⁴` (n_s~τ³).
- **§6 stress** : densité requise pour `R_grad~O(1)` croît `~e^{+|w|τ}` (taux requis `≈|w|`).
- **Sceau** : `verif_D3_C7b_gradient.py` — **19/19 PASS**.

**Tags.** Profil exact, densité `g(u)`, intégrale, décroissance `I_spike→0`, ratio `R_grad→0` :
`établi (sceau)`. Gradient non-local **sur profil exact** : **borné** (PASS substantiel). Gradient
par spike **générique** : borné (A1, `LC-D3-A1-SUPERHORIZON`, `établi (sceau)`). Résidu = **mesure A2** `n_s^gen` (`LC-D3-C7B-VERDICT-A2`) : `décision ouverte` / `hors de portée`. C7-b : **PASS
substantiel**. C7 : `formalisable (borné)`. (A) physique : `formalisable`, conditionnel.
*Discipline §6.4 maintenue.*
