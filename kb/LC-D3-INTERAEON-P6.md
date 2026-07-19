---
id: LC-D3-INTERAEON-P6
titre: "Front (a) / P6 — bang/Mixmaster TRANCHÉ. (A) radiation-era : σ≈0 de Tod QUIESCENTE, mais ε_out dominé par √Ω_σ. (B) deep-bang Ω_σ→1 (oracle Gauss-Kuzmin) : le bang générique chaotique N'A AUCUN cas contractant (P(ε_out<κ·ε_in)=0), injecte une forme O(1) ⊥ à l'héritage, carte inter-éon ADDITIVE/expansive ⟹ ∏κ_n→0 n'est PAS générique, c'est un artefact de σ(0)=0/WCH. LE BANG GAGNE — A3/A4 confirmés socles irréductibles ; la CCC n'est pas réfutée, l'isotropisation dynamique REQUIERT la WCH au lieu de la dériver"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, isotropisation, inter-eon, bianchi-IX, P6, bang, mixmaster, kasner, near-bang, kappa, quiescence, gauss-kuzmin, billard, DHN, WCH]
type: chaînon (exécute les POC des specs (A) ET (B) de LC-WORK-P6-SPEC-NEARBANG ; TRANCHE P6, dernier chantier du front (a))
statut: ordre dominant — (A) radiation-era ÉTABLI (IC-builder §5bis sans racine ; réduction exacte κ=0.8117 ; quiescent ; loi √Ω_σ) / (B) deep-bang TRANCHÉ à l'ordre dominant (oracle Gauss-Kuzmin validé 0.8% ; noyau forward validé Radau≡DOP853 ; le bang générique n'est PAS contractant, carte additive bang-set ⟹ ∏κ_n→0 conditionné à σ(0)=0/WCH, non générique). RÉSERVE : Type IX borne le générique inhomogène ; Ω_σ imposé petit par la WCH/GWE rouvre (A) — SCELLÉ (algèbre) LC-D3-WCH-GWE v0.3, mode exact (A) ∀ kη, conditionnel à C7 (rétro-action inhomogène, hors de portée)
version: 0.3
langue: fr
date: 2026-06-08
maj: "2026-06-08 — v0.3 : HOUSEKEEPING post-audit WCH-GWE (LC-AUDIT-LOG-WCH-GWE §4.5 ; wording, aucune touche à l'algèbre ni au verdict (B)) — §réserves(2) GWE aligné sur LC-D3-WCH-GWE v0.3 : mode régulier exact (A) ∀ kη (max 0.377), « bascule à 1.9 » = artefact leading, verrou déplacé spectre→C7. v0.2 : verdict (B) deep-bang (oracle Gauss-Kuzmin)."
statut_id: provisoire — à enregistrer si validé (LC-00-INDEX ; propager le verdict (B) à LC-D3-INTERAEON-CONVERGENCE §5, LC-D3-CROSSOVER-EINSTEIN3D §4, LC-02, LC-AUDIT-VERDICT §8bis, glossaire)
fichier_compagnon: [verif_D3_P6_poc_specA.py, verif_D3_P6_specB_poc.py, verif_D3_P6_specB_supp.py, verif_D3_P6_specB_oracle.py, diag_bounces.py, verif_D3_interaeon_kappa.py]
prerequis_kb: [LC-WORK-P6-SPEC-NEARBANG, LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-CONVERGENCE, LC-D3-INTERAEON-MATIERE, LC-WORK-CADRAGE-INTERAEON, LC-A-D1-BIANCHI, LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-WCH-GWE, LC-AUDIT-VERDICT, LC-WORK-BIBLIO-FRONT-A]
renvois: [LC-WORK-P6-SPEC-NEARBANG, LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-CONVERGENCE, LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-WCH-GWE, LC-A-D1-BIANCHI, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX, LC-WORK-REPRISE-P6-SPECB]
modules_rattachement:
  - "[A] / front (a) — A3 pivot ; P6 teste si le bang réel préserve l'isotropisation inter-éon"
  - "[D3] hypothèse de Weyl — σ̌/anisotropie de 𝓘 ; le bang est la frontière restante"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Interaeon·P6 — Le bang TRANCHÉ : (A) quiescent mais κ fragile ; (B) le bang gagne

> **Cible.** `LC-D3-INTERAEON-CONVERGENCE` a clos §5.1 (`∏κ_n→0` sous Penrose) **avec P6 exclu**
> (départ en ère radiation, `σ(0)=0` de Tod). `LC-WORK-P6-SPEC-NEARBANG` a figé la modélisation
> du départ near-bang (IC-builder §5bis, sans racine). Ce chaînon **exécute les POC des specs
> (A) et (B)** et **tranche P6** — le dernier chantier du front (a).
>
> **Verdict (A) (ordre dominant, établi ; sceau `verif_D3_P6_poc_specA.py`).** En ère radiation,
> la configuration `σ≈0` de Tod est **quiescente** (pas de cascade Mixmaster, `Σ` sous-Kasner,
> forme non culbutée ; réduction exacte `κ=0.8117`), **mais** `ε_out` est dominé par une
> contribution gelée `∝√Ω_σ` qui écrase `κ·ε` dès `Ω_σ≳1e-4`. La contraction repose donc
> entièrement sur l'hypothèse `σ(0)≈0`.
>
> **Verdict (B) (ordre dominant, tranché ; sceaux `verif_D3_P6_specB_*.py`, `diag_bounces.py`).**
> Le deep-bang générique est traité par **l'oracle de Gauss-Kuzmin** (mesure ergodique du billard
> BKL sur l'état Kasner d'entrée — `u`-map de Gauss validé à **0.8 %** — propagée par le noyau
> forward validé Radau≡DOP853). Résultat sur l'ensemble `Ω_σ→1` :
> **(i)** chaque entrée chaotique **isotropise localement** (𝓘 atteint à ~100 %, Wald intra-éon),
> mais **(ii)** **aucun bang générique ne contracte la forme** : `P(ε_out<ε_in)=0`,
> `P(ε_out<κ·ε_in)=0` à `Ω_σ=0.9` *et* `0.99` ; **tout bang amplifie** (médiane `ε_out/ε_in≈3–5`,
> queue ~40). **(iii)** La carte est **additive, pas multiplicative** : `ε_out≈ε_bang−ε_in`
> (pente `|d/dε_in|≈1`), avec `ε_bang` **fixé par le bang** O(1) ⟹ `ε_n↦ε_{n+1}` est un **pas de
> marche aléatoire O(1)** dans le plan de forme (direction ~Gauss-Kuzmin), **pas** une contraction.
> **⟹ `∏κ_n→0` (§5.1) N'EST PAS générique** : c'est un **artefact de `σ(0)=0` (Tod) / de la WCH
> (Penrose, A4).** **LE BANG GAGNE.**
>
> **Ce que cela signifie (à ne pas sur-lire).** **Pas une réfutation de la CCC.** La WCH postule
> *précisément* que le crossover n'est pas le bang chaotique générique. Le calcul établit que
> l'isotropisation inter-éon **REQUIERT** la WCH/A3 — elle ne la **dérive pas**. **A3/A4 confirmés
> socles irréductibles** (cohérent `LC-D3-CROSSOVER-EINSTEIN3D` §3, `LC-AUDIT-VERDICT` §5). Le
> front (a) est clos **conditionnellement à A3/A4**, jamais inconditionnellement.

---

## 0. Rôle et garde-fou

Ce chaînon **tranche** P6 (dernier chantier du front (a)) : (A) la variante radiation-era (la
plus proche du sceau) et (B) le deep-bang générique via l'oracle de Gauss-Kuzmin. Ce qui est
`établi` est **algébrique** (`LC-AUDIT-VERDICT` §6.4) : la réduction exacte au sceau, la
quiescence du régime radiation-era, la loi `√Ω_σ`, le map de Gauss validé, et la **structure
additive non-contractante** de la carte inter-éon au bang générique.
**Garde-fou `[à ne pas perdre]`** : « le bang gagne » NE veut PAS dire « la CCC est fausse ». Au
contraire : la WCH de Penrose **postule** que le crossover évite le bang chaotique générique ;
le résultat (B) montre que l'isotropisation `∏κ_n→0` **dépend de cette hypothèse** (elle ne la
dérive pas), confirmant A3/A4 comme **socles irréductibles**. Le verdict honnête est : front (a)
clos **conditionnellement à A3/A4**, l'isotropisation dynamique réfutée comme **mécanisme libre**.

---

## 1. Le dispositif `[établi — sceau verif_D3_P6_poc_specA.py]`

**Noyau** : identique au sceau `verif_D3_interaeon_kappa.py` (recopié verbatim — Bianchi IX +
radiation + Λ ; `dw_i/dN=σ_i/H`, `dσ_i/dN=−3σ_i−³S_i/H`, `dH/dN`, `dρ/dN=−4ρ` ; contrainte
`3H²=ρ+Λ+σ²−½³R`, `σ²=½Σσ_i²`).

**IC-builder near-bang** (`LC-WORK-P6-SPEC-NEARBANG` §5bis), ancrage `a=1`, `Λ=1` :

$$3H^2 = \frac{\rho_0 + \Lambda - \tfrac12 F(\varepsilon)}{1 - \Omega_\sigma},\quad
F(\varepsilon) = -2\cosh^2 2\varepsilon + 2\cosh 2\varepsilon + \tfrac32,\quad
\sigma_i = H\sqrt{6\Omega_\sigma}\,(\cos\psi\,\hat e_+ + \sin\psi\,\hat e_-)_i,$$

avec `ê_+=(1,−1,0)/√2` (direction de forme), `ê_−=(1,1,−2)/√6`, `ψ` = angle relatif
cisaillement↔forme. `F(ε)` vérifiée à `1e-16` contre Milnor ; **formule explicite, pas de
racine** (cf. §5bis : l'« unicité de `a` » était un faux problème d'ancrage mélangé).

---

## 2. Résultat `[établi (ordre dominant)]`

**(a) Réduction.** À `Ω_σ=0`, `ψ=0` : `σ(0)=0` exact, et la carte `ε_n↦ε_{n+1}` redonne
`κ=0.8117` (sceau : `0.81–0.816`). La trajectoire est identique à celle du sceau. ✓

**(b) Quiescence (balayage `Ω_σ∈[1e-4,0.3]`, `ε=0.05`, `ψ=0`).**

| diagnostic (§6 de la spec) | observé | lecture |
|---|---|---|
| épisodes de courbure (`|³S|`) | **1** (jamais ≥3) | pas de cascade Mixmaster |
| `Σ_max = σ/θ` | **0.32** | **< Kasner** (`1/√3≈0.577`) |
| `cos(w_0,w_∞)` (ψ=0) | **≥0.934** | rotation simple, pas de culbute |
| résidu de contrainte | **~1e-14** | intégration saine |

⟹ **régime quiescent** en ère radiation : le noyau §2 suffit, le billard DHN n'est pas requis
*pour ce régime*.

**(c) Loi d'échelle — le cisaillement écrase κ.** `ε_out/ε` croît fortement avec `Ω_σ` :
`1.04` (`Ω_σ=1e-4`) → `3.0` (`1e-2`) → `12` (`0.3`). L'excès est **additif en quadrature** :
`ε_out² − (κε)²` ≈ linéaire en `Ω_σ` (coefficient lentement décroissant `4→1.2`), soit une
contribution gelée `∝√Ω_σ`. **Dépendance en `ψ`** (`Ω_σ=0.1`) : la **magnitude** `ε_out`
varie peu (`0.30–0.39`), la **direction** du gel tourne fortement (`cos(w_0,w_∞)` : `0.98` à
`ψ=0` → `0.06` à `ψ=π/2`) — magnitude portée par `Ω_σ`, orientation par `ψ` (subtilité #3
amplifiée). 

$$\boxed{\ \varepsilon_{\rm out} \simeq \sqrt{(\kappa\varepsilon)^2 + c(\Omega_\sigma)\,\Omega_\sigma}\,,\quad c\sim 1.2\text{–}4\ \Rightarrow\ \varepsilon_{\rm out}\ \text{dominé par}\ \sqrt{\Omega_\sigma}\ \text{dès}\ \Omega_\sigma\gtrsim 10^{-4}.\ }$$

---

## 3. Ce que cela implique `[méta — établi pour (A) ; hypothèse pour (B)]`

- **(i) Cadrage confirmé pour (A).** La recommandation du cadrage (noyau §2 backbone, billard
  DHN en oracle *conditionnel*) tient : en ère radiation, aucun rebond, donc le billard est
  rangé. Le diagnostic chaos/quiescence du cadrage donne **quiescent** ici.
- **(ii) Enjeu (B) tranché (§4).** `κ<1` (et donc `∏κ_n→0`, scellé en §5.1) **présuppose
  `σ≈0` au départ**. Le POC (A) montre qu'une contamination gèle `∝√Ω_σ` qui écrase `κ·ε` ; le
  bang **générique** ayant `Ω_σ→1`, l'inquiétude « `ε_out=O(1)` ⟹ isotropisation tuée » était
  motivée. **Le §4 la confirme** : l'oracle de Gauss-Kuzmin montre que le bang générique **ne
  contracte jamais** (carte additive bang-set), donc `∏κ_n→0` n'est **pas générique** — il est
  conditionné à `σ(0)=0`/WCH. **(B) n'est plus une hypothèse : c'est tranché.**

---

## 4. (B) deep-bang TRANCHÉ — l'oracle de Gauss-Kuzmin `[établi (ordre dominant)]`

### 4.1 Pourquoi un oracle, et pas une intégration forward `[établi — diag_bounces.py]`
Diagnostic préalable (sceau `diag_bounces.py`) : l'intégration **forward** du noyau ne montre
qu'**UN mur de courbure** et **zéro renversement** de la vitesse de forme `dw/dN`, même à
`Ω_σ=1−1e-6` (`N_halt~2` e-folds). **La cascade Mixmaster multi-rebonds n'existe pas vers
l'avant** — c'est un phénomène de **l'approche** de la singularité. Le rôle correct de l'oracle
DHN/billard n'est donc pas d'intégrer une cascade forward (le forward est validé, propre), mais
de fournir la **mesure ergodique sur l'état Kasner d'ENTRÉE** que l'approche chaotique dépose à
la naissance de l'éon. C'est exactement « map Kasner entrant→sortant, puis rendre la main au
noyau » du cadrage.

### 4.2 Le dispositif `[établi — sceaux verif_D3_P6_specB_*.py]`
- **Map BKL / `u`-map de Gauss** (BKL ; Khalatnikov-Lifshitz-Sinai-Khanin 1985 ; DHN 0212256).
  Époque Kasner `p(u)=(−u,1+u,u(1+u))/(1+u+u²)` ; map d'époque `u→u−1` (même ère) / `u→1/(u−1)`
  (transition d'ère = map de Gauss `x→{1/x}`). Mesure invariante de **Gauss-Kuzmin**
  `ρ(x)=1/(ln2·(1+x))` — **validée à 0.8 %** par itération du map (sceau §0).
- **Noyau forward validé** : recopié verbatim ; IC-builder deep-bang `σ_i=H√(Ω_σ)(3p_i(u)−1)`
  (§1bis convention 3) ; **Radau≡DOP853 à 1e-10**, résidu de contrainte `≤1e-11`, réduction
  `Ω_σ=0 ⟹ κ=0.8117`.
- **Oracle** : tirer l'état d'entrée `(u,axe,orientation)` sous Gauss-Kuzmin → propager par le
  noyau jusqu'à 𝓘 → `ε_out`. Ensemble `N=2500–4000` à `Ω_σ∈{0.9,0.99}` (régimes où DOP853 est
  validé ; `Ω_σ≥0.999` par points Radau directs).

### 4.3 Le résultat `[établi (ordre dominant)]`

| diagnostic | `Ω_σ=0.9` | `Ω_σ=0.99` | lecture |
|---|---|---|---|
| 𝓘 atteint | ~100 % | ~100 % | isotropisation **locale** (Wald intra-éon) OK |
| `P(ε_out<ε_in)` | **0.00** | **0.00** | **aucun bang ne contracte** la forme |
| `P(ε_out<κ·ε_in)` | **0.00** | **0.00** | jamais aussi bon que Wald/Tod |
| médiane `ε_out/ε_in` | 4.6 | 3.1 | **tout bang amplifie** (×3–5 typique) |
| `ε_out` quantile 95 % | 1.8 | 2.2 | queue ~40× |

**Structure de la carte (décisif).** À orientation fixe, `ε_out(ε_in)=ε_bang−ε_in` à **pente
exactement −1**, `ε_bang` **fixé par le bang** (~1.7 à `u=2,Ω_σ=0.99`). La carte inter-éon est
donc **additive**, `ε_{n+1}≈|\,\mathbf b_n − \mathbf w_n\,|` avec `\mathbf b_n` une forme O(1)
de direction ~Gauss-Kuzmin **indépendante** de l'héritage `\mathbf w_n` :

$$\boxed{\ \varepsilon_{n+1}\simeq |\mathbf b_n-\mathbf w_n|,\quad |\mathbf b_n|\sim O(1)\ \text{bang-set, direction Gauss-Kuzmin}\ \Rightarrow\ \text{MARCHE ALÉATOIRE O(1), pas une contraction }\kappa\varepsilon.\ }$$

Une suite de facteurs tous `>1` (`P(contraction)=0`) **ne tend pas vers 0** — elle diverge / se
stationnarise à O(1). À orientation fixe, `ε_out` **croît** avec la profondeur (points Radau :
1.83→2.42 de `Ω_σ=0.999` à `1−1e-6`). Et dès `ε_out>0.48`, on **quitte** le régime petit-`ε`
où vivait `∏κ_n→0` (`³R` change de signe, `LC-WORK-P6-SPEC-NEARBANG` §5bis cond.3) : **un seul
bang générique invalide la prémisse linéarisée du §5.1.**

### 4.4 Verdict (B) `[établi (ordre dominant) — LE BANG GAGNE]`
Le bang **générique** (chaotique, mesure de Gauss-Kuzmin) réinjecte une anisotropie O(1)
orthogonale à l'héritage, à chaque éon, et **ne contracte jamais**. Donc **`∏κ_n→0` (§5.1) n'est
pas un mécanisme dynamique libre** : il est **conditionné à `σ(0)=0` (Tod) / WCH (Penrose, A4)**.
La CCC n'est pas réfutée — mais l'isotropisation inter-éon **requiert** la WCH au lieu de la
dériver. **A3/A4 = socles irréductibles confirmés.** Front (a) clos **conditionnellement à
A3/A4**.

### 4.5 Réserves `[discipline §6.4]`
1. **Type IX (Heinzle-Uggla)** : 3 constantes de structure de même signe — borne ce qu'on peut
   dire du **générique inhomogène**. Le verdict (B) vaut pour le bang homogène IX.
2. **GWE Meissner-Penrose (2503.24263) — SCELLÉ (algèbre), `LC-D3-WCH-GWE` v0.3.** La physique du
   crossover conforme **impose effectivement** un `Ω_σ` petit : le pont forme↦cisaillement est
   dérivé et scellé, `Ω_σ=(kη)⁴ε²/27` (sceau `verif_D3_WCH_GWE.py`). Le mode régulier **exact** est
   en **régime (A) ∀ `kη`** (plafond `Ω_σ/ε²=0.377<0.5` ; au pic CGB `~6·10⁻²⁹`) ⟹ la
   GWE retombe en (A) radiation-era et `ε_out↓`. **Conditionnel à C7** (rétro-action inhomogène,
   hors de portée ; l'ancienne « bascule (B) à coupure dure `kη_*~1.9` » était un artefact de la
   troncature leading, audit C5 — le spectre M-P n'est plus le verrou). C'est *pourquoi*
   « le bang gagne » confirme A4 (la WCH a un contenu dynamique) plutôt que de réfuter la CCC : le
   bang **générique** gagne (B), mais le crossover **réel** (GWE) est (A) si C7 tient.
3. **`Ω_σ≥0.999`** : DOP853 explicite échoue sur le mur raide ; ensemble Radau complet coûteux,
   mais les points directs confirment le trend (croissance) et la structure (additive) est
   `Ω_σ`-stable.
4. **Forme héritée petite** : le verdict porte sur le **régime bang-dominé** (le générique), pas
   sur une limite `ε_in→0` isolée.

---

## 4bis. Ce qui closerait le point au-delà de l'ordre dominant `[formalisable]`
- **Inhomogène (au-delà de IX)** : refaire l'oracle sur un bang BKL inhomogène (spikes,
  particle horizons) pour lever la réserve Heinzle-Uggla — `[hors de portée actuelle]`.
- **`Ω_σ` physique imposé** : calculer le `Ω_σ` de départ réel à partir de l'amplitude GW au
  crossover (Meissner-Penrose 2503.24263) au lieu de le poser → trancher si le crossover réel est
  régime (A) ou (B). `[FAIT — LC-D3-WCH-GWE v0.3]`
  → **Fait (algèbre)** : `LC-D3-WCH-GWE` v0.3 dérive `Ω_σ=(kη)⁴ε²/27` et chiffre le crossover réel
  en **régime (A)** — mode régulier exact (A) ∀ `kη` (plafond `0.377<0.5` ; au pic CGB `~6·10⁻²⁹`).
  Reste `formalisable` / `décision ouverte` : la **rétro-action inhomogène** (C7, hors de portée — le
  verrou ; le spectre M-P n'est plus le verrou, moot par le mode exact).

---

## 5. Format de chaînon standard

- **Zone ambiguë.** « `∏κ_n→0` est scellé *avec* `σ(0)=0` (Tod) ; le bang réel respecte-t-il
  cette CI, ou injecte-t-il un cisaillement qui regèle de l'anisotropie ? »
- **Hypothèse testée (A).** Rouvrir `Ω_σ≠0` en ère radiation change-t-il la nature de la carte
  (cascade ? renversement de `κ` ?).
- **Outil.** IC-builder §5bis (formule explicite) ; noyau §2 recopié ; DOP853 ; diagnostics §6.
  Sceau `verif_D3_P6_poc_specA.py`.
- **Critère de réfutation (de la quiescence).** Si `Ω_σ` petit déclenchait une cascade
  (épisodes ≥3, `Σ→`Kasner) ou renversait `κ`. — **Non réalisé** : quiescent, un épisode lisse,
  `Σ` sous-Kasner.
- **Verdict.** **(A) quiescent + réduction exacte ; loi `√Ω_σ`. (B) deep-bang TRANCHÉ par
  l'oracle de Gauss-Kuzmin : le bang générique n'est PAS contractant (carte additive bang-set),
  ⟹ `∏κ_n→0` conditionné à `σ(0)=0`/WCH — LE BANG GAGNE, A3/A4 socles confirmés.** `[ordre
  dominant établi pour (A) et (B) ; front (a) clos conditionnellement à A3/A4]`

---

## 6. Renvois, glossaire, références

**Renvois.** **Ouvre P6** (frontière restante de `LC-D3-CROSSOVER-EINSTEIN3D` §4 et du verdict
`LC-D3-INTERAEON-CONVERGENCE`) ; exécute la spec `LC-WORK-P6-SPEC-NEARBANG` (§4 spec A, §5bis
IC-builder, §6 diagnostics) ; noyau `LC-D3-INTERAEON-KAPPA` ; `LC-A-D1-BIANCHI` (σ̌, forme de
bang) ; `LC-AUDIT-VERDICT` §6.4 (discipline), §8 bis (registre). Reprise pour (B) :
`LC-WORK-REPRISE-P6-SPECB`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *IC-builder near-bang (§5bis)* : `3H²=(ρ0+Λ−½F(ε))/(1−Ω_σ)`, `σ_i=H√(6Ω_σ)(cosψ ê_+ +
  sinψ ê_−)` ; formule explicite, pas de racine ; `Ω_σ=0` ⟹ CI de Tod (sceau).
- *Quiescence (P6, variante A)* : en ère radiation, une contamination de cisaillement `Ω_σ` ne
  déclenche **pas** de cascade Mixmaster (un épisode lisse, `Σ` sous-Kasner) ; le noyau §2 suffit.
- *Loi `√Ω_σ` (fragilité de κ)* : `ε_out` gèle une anisotropie additive `∝√Ω_σ` qui écrase
  `κ·ε` ; `κ<1` n'a de sens que si le bang a `σ≈0`. Enjeu reporté sur (B) deep-bang.
- *Oracle de Gauss-Kuzmin (P6, variante B)* : mesure ergodique du billard BKL (map `u→{1/u}`,
  densité `1/(ln2(1+x))`) sur l'état Kasner d'entrée de l'éon, propagée par le noyau forward ;
  donne la **distribution** de `ε_out` au bang générique.
- *Carte inter-éon additive (bang-set)* : `ε_{n+1}≈|\mathbf b_n−\mathbf w_n|`, `\mathbf b_n` forme
  O(1) imposée par le bang (direction Gauss-Kuzmin), ⊥ héritage ⟹ marche aléatoire, pas de
  contraction. `P(ε_out<κ·ε_in)=0`.
- *« Le bang gagne » (P6)* : le bang générique chaotique ne contracte jamais la forme ⟹ `∏κ_n→0`
  n'est pas générique mais **conditionné à σ(0)=0/WCH**. Confirme A3/A4 socles ; ne réfute pas la CCC.

**Références (`LC-04` / biblio `LC-WORK-BIBLIO-FRONT-A`).**
- **Tod** arXiv:1309.7248 — éq.24 (`σ(0)=0` au bang), éq.27 (radiation `ρ∝Ť⁻²`).
- **Wainwright & Ellis** (1997) ; **Wainwright & Hsu** CQG 6 (1989) — variables
  expansion-normalisées, équation du cisaillement.
- **Milnor** Adv. Math. 21 (1976) — 3-Ricci. **Wald** PRD 28 (1983) — isotropisation intra-éon.
- **BKL** (Belinski-Khalatnikov-Lifshitz) ; **Khalatnikov-Lifshitz-Sinai-Khanin** J.Stat.Phys.
  38 (1985) — mesure invariante de Gauss-Kuzmin du map `u`. **Damour-Henneaux-Nicolai**
  hep-th/0212256 (billard cosmologique). **Heinzle-Uggla** 0901.0806/0901.0776 (genericité IX).
  **Meissner-Penrose** arXiv:2503.24263 (GWE — `Ω_σ` imposé ?).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte` (cf. `LC-00-INDEX`).
*Discipline d'audit : un `établi` de sceau = « l'algèbre est correcte », à l'ordre dominant ;
jamais « la physique de la CCC est établie ». Ici l'`établi` porte sur : la réduction exacte, la
quiescence et la loi `√Ω_σ` en (A) ; le map de Gauss validé, le noyau forward validé, et la
structure additive non-contractante de la carte inter-éon en (B). Le verdict « le bang gagne »
est un énoncé sur le bang GÉNÉRIQUE homogène IX ; il confirme que l'isotropisation requiert la
WCH (A4), il ne réfute pas la CCC.*
