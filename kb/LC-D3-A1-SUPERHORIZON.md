---
id: LC-D3-A1-SUPERHORIZON
titre: "Front (a)/GWE — C7-b (rétro-action des spikes), VOIE A FACTEUR A1 EXÉCUTÉ : lemme super-horizon GÉNÉRIQUE. Généralise le gradient par spike de la voie 1.5 SANS profil exact. RÉSULTAT : pour toute structure de spike de largeur ℓ en unités d'horizon, l'énergie de gradient Hubble-normalisée intégrée vaut I(ℓ)=C_F/ℓ, où C_F=∫(dF/du)²du est une constante O(1) DU PROFIL ; le scaling 1/ℓ est INDÉPENDANT du profil détaillé (démontré symboliquement par changement de variable, vérifié sur 6 profils qualitativement distincts : pente log-log=−1 à 1e-6). Le silence asymptotique (E_i^a→0, gr-qc/0402051 : horizons→0) impose ℓ(τ)→+∞, donc I_spike^gen(τ)=C_F/ℓ(τ)→0 pour TOUT profil super-horizon à charge de gradient C_F bornée — y compris les profils à spectre d'échelles comobile FIXE (multi-gradient). Le profil exact de Lim (voie 1.5) est le cas C_F^Lim=2π·A², exactement reproduit. Sceau verif_D3_C7b_A1_superhorizon.py (10/10 PASS). RÉSERVE : A1 borne le facteur PAR spike ; il NE traite PAS le facteur A2 (mesure/production de spikes générique n_s^gen) — la seule brèche au scaling 1/ℓ est une CASCADE (C_F divergent par régénération sous-horizon), qui EST la question A2, `à inventer` / hors A1. C7-b reste PASS substantiel ; le résidu générique-mesure reste `décision ouverte`."
codename: LC-RACCORD
type: note de résultat (chaînon) — consigne l'exécution du facteur A1 de la voie A générique (LC-WORK-REPRISE-C7B-GENERIQUE §3, Tâche 1). Subordonnée à la discipline LC-AUDIT-VERDICT §6.4.
version: 1.0
langue: fr
date: 2026-06-08
portee: "Consigne UNIQUEMENT le delta : le facteur A1 du résidu générique de C7-b (LC-WORK-REPRISE-C7B-GENERIQUE §2 N2) est codé, exécuté, PASS. Il généralise le gradient PAR spike de la voie 1.5 (I_spike∝κ, LC-D3-GRADIENT-C7B) au cas GÉNÉRIQUE sans profil exact : le scaling I∝1/ℓ est profil-indépendant, et le silence (ℓ→∞) l'éteint. Ne refait NI la voie 1.5 (profil exact, LC-D3-GRADIENT-C7B), NI la statistique de spikes (voie 1, LC-D3-SPIKES-C7B), NI le silence (LC-D3-SILENCE-POC). Discipline §6.4 : A1 est un LEMME D'ÉCHELLE (analytique + numérique) ; il borne le facteur PAR spike, il ne PROUVE PAS la mesure générique (A2). C7-b : PASS substantiel (renforcé) ; C7 reste `formalisable (borné)` ; (A) physique conditionnel au seul facteur A2."
prerequis_kb: [LC-D3-GRADIENT-C7B, LC-WORK-REPRISE-C7B-GENERIQUE, LC-D3-SPIKES-C7B, LC-D3-SILENCE-POC, LC-WORK-BIBLIO-SPIKES-C7B, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_C7b_A1_superhorizon.py, verif_D3_C7b_gradient.py]
source_externe: ["Uggla-van Elst-Wainwright-Ellis, The past attractor in inhomogeneous cosmology, PRD 68 103502 (2003), arXiv:gr-qc/0304002 (variables Hubble-normalisées, opérateur de dérivée de repère e_a=E_a^i ∂_i, E_a^i→0). Andersson-van Elst-Lim-Uggla, Asymptotic silence of generic cosmological singularities, PRL 94 051101 (2005), arXiv:gr-qc/0402051 (silence asymptotique générique : horizons→0 ⟹ toute structure devient super-horizon). Lim, arXiv:0710.0628 (profil exact, cas particulier C_F^Lim=2π·A² ; déjà scellé voie 1.5). Tous en KB (LC-WORK-BIBLIO-SPIKES-C7B v1.1)."]
tags_epistemiques: [établi, formalisable, à inventer, décision ouverte]
---

# C7-b (rétro-action des spikes), voie A — facteur A1 (lemme super-horizon générique)

> **But.** Consigner l'exécution du **facteur A1** de la voie A
> (`LC-WORK-REPRISE-C7B-GENERIQUE §3`) : **généraliser** l'énergie de gradient **par spike** de
> la voie 1.5 (`LC-D3-GRADIENT-C7B`, `I_spike∝κ`, calculée sur le **profil exact**) au cas
> **pleinement générique**, **sans** profil exact. Discipline `LC-AUDIT-VERDICT §6.4` : A1 est un
> **lemme d'échelle** (analytique + numérique) ; il borne le facteur PAR spike, il ne **prouve
> pas** la mesure générique (facteur A2).

---

## 0. État en une ligne `[résultat]`

A1 **borne le gradient par spike en générique**. Pour toute structure de spike de largeur `ℓ` en
unités d'horizon, l'énergie de gradient Hubble-normalisée intégrée vaut
```
I(ℓ) = C_F / ℓ ,   C_F = ∫ (dF/du)² du   (constante O(1), DÉPEND du profil F)
```
où le **scaling `1/ℓ` est INDÉPENDANT du profil** `F` (le profil n'entre que par la constante
`C_F`). Le silence asymptotique (`E_i^a→0`, `gr-qc/0402051` : horizons→0) impose `ℓ(τ)→+∞`, donc
```
I_spike^gen(τ) = C_F / ℓ(τ)  →  0   ∀ profil super-horizon à C_F bornée.
```
Le profil **exact de Lim** (voie 1.5) est le cas `C_F^Lim=2π·A²`, et `I=2π·A²·κ` est exactement
reproduit. Sceau `verif_D3_C7b_A1_superhorizon.py` (**10/10 PASS**). **Réserve honnête** : A1
borne le facteur **par spike** ; il ne traite **pas** le facteur **A2** (mesure/production de
spikes générique `n_s^gen`). ⟹ **C7-b : PASS substantiel (renforcé)** ; résidu = **A2 seul**,
`décision ouverte`.

---

## 1. Le cadre et l'observable `[établi (sceau) §0-§1]`

**Cadre Hubble-normalisé** (Uggla et al. `gr-qc/0304002`). L'inhomogénéité spatiale entre dans
`Ω_σ` via l'opérateur de dérivée de repère `e_a = E_a^i ∂_i` ; l'énergie de gradient d'un champ
`Σ` s'écrit `Ω_σ^grad ∝ (E_a^i ∂_i Σ)²`. Le **silence asymptotique** (`gr-qc/0402051`) est
précisément `E_a^i → 0` (horizons→0) — c'est le terme que le silence annule.

**Lemme d'échelle (symbolique).** Une structure de largeur `ℓ` en unités d'horizon s'écrit
`Σ(X)=F(X/ℓ)` (coordonnée horizon-normalisée `X`, profil de forme `F` d'amplitude `O(1)` —
cohérent avec la borne d'amplitude `α_s` de la voie 1). Alors
```
∂_X Σ = (1/ℓ) F'(X/ℓ)
I(ℓ) = ∫ (∂_X Σ)² dX = ∫ (1/ℓ²) F'(X/ℓ)² dX = [u=X/ℓ] = (1/ℓ) ∫ F'(u)² du = C_F / ℓ.
```
Le changement de variable est **linéaire** ⟹ l'exposant `−1` est exact **pour tout profil** `F` ;
`F` n'entre que par `C_F=∫F'²du`. (Vérifié symboliquement sur la gaussienne : `C_F=√π/2`.)

---

## 2. Profil-indépendance du scaling `[établi (sceau) §2]`

Le sceau teste une **bibliothèque de profils qualitativement distincts** et vérifie, pour chacun,
(a) que `I(ℓ)·ℓ` est **constant** (= `C_F`, scaling `1/ℓ` exact) et (b) que `C_F` numérique
**égale** sa valeur analytique :

| profil `F` | `C_F` (analytique) | pente log-log `I` vs `ℓ` |
|---|---|---|
| gaussienne `e^{−u²/2}` | `√π/2 ≈ 0.886` | `−1.00000` |
| lorentzienne `1/(1+u²)` | `π/4 ≈ 0.785` | `−1.00000` |
| sech `1/cosh u` | `2/3` | `−1.00000` |
| kink `tanh u` (marche) | `4/3` | `−1.00000` |
| double-pic `u·e^{−u²/2}` | `3√π/4 ≈ 1.329` | `−1.00000` |
| bump compact `(1−u²)²·𝟙_{|u|<1}` | `256/105 ≈ 2.438` | `−1.00000` |

⟹ **le profil n'affecte QUE la constante `C_F` ; le scaling `1/ℓ` est universel** (pente `−1` à
`1e-6` près, `|I·ℓ−C_F|/C_F < 1e-6`).

---

## 3. Raccord exact à la voie 1.5 `[établi (sceau) §3]`

Le **profil exact de Lim** est **un cas particulier** de A1 : sa densité de gradient
`g(u)=(c')²+(s')²=4/(1+u²)²` a pour charge `C_F^Lim=∫g du=2π` (symbolique), et la largeur en
unités d'horizon est `ℓ(τ)=(1/w)cosh(wτ)=1/κ(τ)` (rayon spike/horizon, Lim éq.43). D'où
```
I(τ) = C_F^Lim/ℓ(τ) = 2π·A²·κ(τ)   ≡   I_spike(τ) de la voie 1.5  (raccord exact ∀ w,τ testés).
```
La voie 1.5 est donc **le point** `C_F=2π·A²` d'une **famille à un paramètre `C_F`** ; A1 montre
que **n'importe quel autre profil** donne le même comportement, à la constante `C_F` près.

---

## 4. Super-horizon ⟹ extinction `[établi (sceau) §4]`

Le silence (`gr-qc/0402051`) fait `ℓ(τ)≥1` (super-horizon garanti) puis `ℓ(τ)→+∞` (horizons→0).
Le sceau évalue `I(τ)=C_F/ℓ(τ)` pour **toute la bibliothèque simultanément** (`ℓ(τ)` modèle
`(1/w)cosh(wτ)`) : décroissance **monotone**, `<1e-3` à `τ=40` pour **tous** les profils.
**Borne uniforme** : `ℓ≥1 ⟹ I≤C_F`, puis `→0` quand `ℓ→∞` — le profil ne fixe **jamais** le
scaling, seulement le préfacteur.

---

## 5. La vraie frontière : multi-échelle et cascade `[décision ouverte — délimite A2]`

**Spectre comobile FIXE (multi-gradient) — A1 tient.** Un profil à plusieurs échelles comobiles
(`F=F_large+a·F_fin(u/δ)`) a une charge `C_F` **finie** ; le sceau vérifie que le scaling `1/ℓ`
est **préservé** (pente `−1`). Si toutes les échelles sont transportées par la même expansion,
même la plus fine devient super-horizon (`ℓ·δ≥1`), et `I=C_F/ℓ→0`. ⟹ **A1 couvre le cas
multi-gradient à spectre fixe**, qui était la réserve explicite de la voie 1.5.

**La SEULE brèche = la CASCADE.** Si une structure fine est **régénérée plus fine que l'horizon à
chaque instant** (`δ=δ(τ)→0` plus vite que `ℓ(τ)` croît), alors `C_F=C_F(τ)~1/δ` **diverge** et
le scaling `1/ℓ` ne suffit plus. Mais c'est exactement une question de **production/mesure de
spikes** — le **facteur A2** (`n_s^gen`, `LC-WORK-REPRISE-C7B-GENERIQUE §3 A2`) — et **non** une
propriété du gradient par spike. A1 **délimite** donc proprement le résidu : tout repose désormais
sur A2.

> **Réduction nette opérée par A1.** Avant A1, le gradient générique entier était `décision
> ouverte`. Après A1, le résidu se réduit au **seul** facteur A2 : « la mesure de spikes
> générique `n_s^gen(τ)` croît-elle **sous-exponentiellement** ? » — car
> `I_spike^gen~C_F·2w·e^{−|w|τ}`, donc `R_grad,gen=n_s^gen·I_spike^gen→0` **dès que** `n_s^gen`
> croît plus lentement que `e^{|w|τ}`. C'est une condition **faible** (toute croissance
> polynomiale suffit), **physiquement attendue** (bounces BKL ~ linéaires), mais **non établie
> rigoureusement** en générique par la littérature.

---

## 6. Statut de C7-b et de C7 `[bilan]`

| Facteur de `R_s` | Statut après voie 1.5 | Statut après **A1** | Source |
|---|---|---|---|
| Amplitude `α_s` | borné (profil exact) | inchangé | voie 1 |
| Statistique = bulk | `α_s(moy)→1` (profil exact) | inchangé | voie 1 |
| Gradient — profil exact | **borné** `établi (sceau)` | inchangé | voie 1.5 |
| Gradient — **par spike, générique** (A1) | — | **borné** `établi (sceau)` — `I∝1/ℓ→0` ∀ profil | **ici** |
| **Mesure générique** `n_s^gen` (A2) | — | **`décision ouverte`** — sous-exp. attendu, non prouvé | §5, GENERIQUE §3 A2 |

- **C7-b** : **PASS substantiel (renforcé)**. Les 3 facteurs sont bornés *sur le profil exact*
  **et** le gradient par spike est borné **en générique** (A1). Le résidu n'est plus « le gradient
  générique » en bloc, mais le **seul facteur A2** (mesure/production de spikes générique).
- **C7** : reste `formalisable (borné)`. `C7 = C7-a` (WCH pointwise, `formalisable`) `+ C7-b`
  (amplitude ✓, statistique ✓, gradient profil exact ✓, gradient générique par spike ✓ [A1] ;
  reste A2).
- **(A) physique** : reste `formalisable`, conditionnel au **seul facteur A2** (+ C7-a pointwise,
  cadre CCC). **Si** A2 était bornée sous-exponentiellement ⟹ **C7-b complet ⟹ C7 levée** ⟹
  **(A) `établi (sous WCH/A3-A4, CCC)`** ⟹ front (a) clos par la physique.

---

## 7. Sans surclassement `[discipline §6.4]`

> Le sceau est `établi (sceau)` = « le gradient **par spike** s'éteint en générique (`I∝1/ℓ→0`),
> indépendamment du profil ». Il ne dit **PAS** « C7 est levée » ni « la physique de la CCC est
> établie ». C7 levée resterait conditionnelle à : silence (A∧B∧C) ∧ WCH pointwise (C7-a) ∧
> spikes négligeables (amplitude ✓ + statistique ✓ + gradient profil exact ✓ + gradient générique
> par spike ✓ [A1] + **mesure générique A2 [à faire / à inventer]**). « Le bang gagne » (P6 B)
> intact.

---

## Appendice — chiffres scellés (à ne pas re-prouver)

- **§1 lemme** : `I(ℓ)=C_F/ℓ` (symbolique, gaussienne `C_F=√π/2`) ; exposant `−1` exact par
  changement de variable `u=X/ℓ` (∀ profil).
- **§2 bibliothèque** : `C_F` analytique = numérique pour 6 profils ; pente log-log `=−1` à
  `1e-6` ; `|I·ℓ−C_F|/C_F < 1e-6`.
- **§3 raccord** : `C_F^Lim=∫[(c')²+(s')²]du=2π` (symbolique) ; `C_F^Lim/ℓ(τ)=2π·κ(τ)` (∀ `w,τ`).
- **§4 extinction** : `ℓ(τ)≥1` ; `I(τ)→0` monotone, `<1e-3` à `τ=40`, tous profils.
- **§5 frontière** : profil 2-échelles comobile ⟹ pente `−1` préservée, `C_F` fini ; cascade ⟹
  `C_F(τ)~1/δ` diverge = question A2.
- **Sceau** : `verif_D3_C7b_A1_superhorizon.py` — **10/10 PASS**.

**Tags.** Lemme d'échelle, profil-indépendance, raccord Lim, extinction `I→0` : `établi (sceau)`.
Gradient **par spike générique** (A1) : **borné**. Mesure générique `n_s^gen` (A2) : `décision
ouverte` (sous-exp. attendu, non prouvé) / possiblement `hors de portée`. C7-b : **PASS
substantiel** (renforcé). C7 : `formalisable (borné)`. (A) physique : `formalisable`, conditionnel
au seul A2. *Discipline §6.4 maintenue.*
