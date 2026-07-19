---
id: LC-WORK-P6-SPEC-NEARBANG
titre: "P6 — spec de l'état initial near-bang : comment paramétrer le départ quand σ(0)=0 n'est plus disponible (préambule de modélisation du chaînon P6 à venir)"
codename: LC-RACCORD
type: note de travail (spec de modélisation, à figer avant code ; deviendra le §1 de LC-D3-INTERAEON-P6)
version: 0.3
langue: fr
date: 2026-06-07
portee: "Fige par écrit le SEUL point de modélisation neuf de P6 : la paramétrisation de l'état initial quand on recule le départ du noyau §2 vers a→0 et que la condition de Tod σ(0)=0 cesse d'être disponible. Ne refait rien du noyau (LC-WORK-REPRISE-P6 §2). Établit (i) pourquoi σ(0)=0 n'existe pas à a→0, (ii) le vecteur d'état et les paramètres dimensionnés Ω, (iii) les boutons, (iv) deux specs (A radiation-era / B deep-bang Kasner), (v) la satisfaction de contrainte SANS racine (formule H² explicite), (vi) la réduction au sceau, (vii) les diagnostics. v0.2 : conventions §1bis épinglées contre verif_D3_interaeon_kappa.py. v0.3 : angle mort de l'unicité de a RÉSOLU (§5bis) — a est un ancrage, pas une racine ; H² explicite et linéaire en Ω_σ ; F(ε) closed-form vérifiée 1e-16 vs Milnor ; spec auto-suffisante."
maj: "2026-06-07 — v0.3 : §5 réécrit + §5bis ajouté. L'unicité de la racine a était un faux problème (formulation mélangeant ancrages) : en ancrant a=1 (Λ=1 fixe l'unité) et en spécifiant le cisaillement par Ω_σ, H² est EXPLICITE et linéaire : 3H²=(ρ0+Λ−½F(ε))/(1−Ω_σ), F(ε)=−2cosh²2ε+2cosh2ε+3/2 (vérifiée 1e-16 vs ricci3_components du sceau ; change de signe à ε=0.4812). Conditions de validité = 3 inégalités (Ω_σ<1 ; numérateur>0 ; signe F), pas une racine. Conséquence spec B : courbure positive ⟹ pas d'IC Kasner statique ; IX oscillatoire ⟹ état entre-murs (inégalité a^{-2}F≪σ²). v0.2 : §1bis (conventions épinglées)."
prerequis_kb: [LC-WORK-REPRISE-P6, LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-MATIERE, LC-D3-INTERAEON-CONVERGENCE, LC-WORK-CADRAGE-INTERAEON, LC-A-D1-BIANCHI, LC-WORK-BIBLIO-FRONT-A]
fichiers_compagnons_kb: [verif_D3_interaeon_kappa.py, verif_D3_interaeon_convergence.py]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# P6 — Spec de l'état initial near-bang

> **But.** Avant d'écrire `verif_D3_P6_bang.py`, figer la seule pièce de modélisation neuve :
> **comment spécifier l'état de départ** quand on prolonge le noyau §2 vers `a→0`. Le noyau
> sealé partait en ère radiation avec la CI de Tod `σ(0)=0` (cisaillement cinétique nul,
> anisotropie dans la forme `w(0)=ε_n`). En reculant vers le bang, cette CI **cesse d'être
> disponible** (cf. §1) ; il faut la remplacer par une paramétrisation explicite qui (a) se
> réduit au sceau dans la limite quiescente, (b) ouvre le secteur cisaillement pour tester la
> stabilité Mixmaster, (c) reste sur la surface de contrainte.
>
> **Garde-fou `[à ne pas perdre]`.** Cette note **spécifie** un dispositif ; elle ne tranche
> pas P6. Tout ce qui sera `établi` au sceau restera « l'algèbre est correcte, à l'ordre
> dominant » (`LC-AUDIT-VERDICT` §6.4). Les conventions de signe/normalisation sont **épinglées
> en §1bis** (lues dans le code sealé) ; toute IC-builder doit s'y conformer.

---

## 1. Le fait structurel : `σ(0)=0` à `a→0` N'EXISTE PAS `[établi]`

La contrainte de Friedmann du noyau (cf. `LC-D3-INTERAEON-MATIERE` §1) :

$$3H^2 = \rho + \rho_\varphi + \Lambda + \sigma^2 - \tfrac12\,{}^3R,\qquad \sigma^2 := \tfrac12\textstyle\sum_i\sigma_i^2\ \ \text{(§1bis, confirmé code)}.$$

En paramètres de densité sans dimension (`Ω_X := X/3H²`), elle se lit :

$$\Omega_{\rm rad} + \Omega_\varphi + \Omega_\Lambda + \Omega_\sigma + \Omega_{\rm courb} = 1,
\qquad \Omega_\sigma=\frac{\sigma^2}{3H^2},\ \ \Omega_{\rm courb}=\frac{-{}^3R}{6H^2}.$$

**Scaling near-bang** (`a→0`, lois de redshift) :

| composante | densité ∝ | `Ω_X` ∝ | limite `a→0` |
|---|---|---|---|
| cisaillement `σ²` | `a^{-6}` | `O(1)` | **domine** (→ Kasner) |
| courbure `−³R` | `a^{-2}·f(w)` | `a^{4}` | → 0 (sauf *pics* de mur, cf. §6) |
| radiation `ρ` | `a^{-4}` | `a^{2}` | → 0 |
| `ρ_φ` (raide possible) | `a^{-6}` (si cinétique) | `O(1)` | concurrence le cisaillement *si* présent |
| `Λ` | `a^{0}` | `a^{6}` | → 0 |

**Conséquence.** À `a→0`, génériquement `Ω_σ→1` (Kasner sous vide), tout le reste `→0`. Donc
**il n'y a pas de point `Ω_σ=0` sur la surface de contrainte au bang** : poser `σ=0` exigerait
qu'une autre composante porte la contrainte, or toutes `→0` plus vite que `σ²`. La CI `σ(0)=0`
de Tod est en réalité imposée **en ère radiation** (`a` fini, `Ω_rad≈1`), pas à `a=0`.

> **Reformulation du contournement levé par P6.** Tod ne décrit pas le bang à `a=0` ; il décrit
> son **voisinage radiation-dominé**, où l'isotropisation de Wald a déjà rendu `σ≈0`. Le `σ(0)=0`
> sealé est un **aboutissement** à `a` fini, pas une donnée à `a=0`. Reculer le départ revient
> donc à demander : *en deçà de l'ère radiation, la trajectoire qui produit `σ≈0` est-elle
> l'attracteur, ou une orbite Kasner-avec-rebonds qui ré-injecte de l'anisotropie ?* C'est la
> question de stabilité de §2 du cadrage, et elle interdit de réutiliser `σ(0)=0` comme CI.

---

## 1bis. Conventions épinglées contre le code sealé `[établi — lu dans verif_D3_interaeon_kappa.py]`

Les trois conventions de la v0.1 (`σ²`, signe `³R`, normalisation Kasner) sont fixées comme le
code les implémente. Toute IC-builder DOIT s'y conformer pour que la limite `Ω_σ→0` reproduise
le sceau.

1. **Cisaillement.** `σ² := ½ Σ_i σ_i²` (lignes 55/65/85 ; `σ_3=−σ_1−σ_2`). C'est cette quantité
   qui entre dans la contrainte et dans `dH/dN = (−H²−⅔σ²−ρ/3+Λ/3)/H`.
2. **Courbure.** `³R := Σ_i ³R_ii` avec `³R_ii = 2μ_jμ_k` (Milnor ; `λ_i=A_i/(A_jA_k)`,
   `s=½Σλ`, `μ_i=s−λ_i`), **positif près de l'isotropie** (S³). Elle entre dans la contrainte en
   **`−½³R`** (ligne 56/91 : `3H² = ρ+Λ+σ²−½³R`). **Donc `Ω_courb := −³R/6H² < 0` près de
   l'isotropie** (modèle fermé) : dans `Ω_rad+Ω_Λ+Ω_σ+Ω_courb=1`, les parts positives somment à
   **>1**, `Ω_courb` négatif comblant l'excès. Scaling : `³R ∝ a^{-2}·f(w)` (car
   `λ_i∝a^{-1}e^{2w_i}`), donc `Ω_courb ∝ a^{4}→0` au bang. *(Pic transitoire = mur de rebond.)*
3. **Cercle de Kasner — carte code-cohérente.** Le code mesure `Σ_code := σ/(3H)` (ligne 86,
   `θ=3H`), de valeur **`1/√3` sous vide Kasner** (pas 1). On retient le paramètre sans dimension
   `Ω_σ := σ²/3H²` (Kasner = 1 ; lien : `Ω_σ = 3 Σ_code²`). La **direction** sur le cercle est
   donnée par les exposants BKL via la relation dérivée du noyau (`dw_i/dN=σ_i/H`, `a∝t^{1/3}`) :
   $$\boxed{\ \sigma_i/H = 3p_i - 1\ }\quad p_i(u)\ \text{Kasner},\ \Sigma p_i=\Sigma p_i^2=1
   \ \Rightarrow\ \Sigma\,\sigma_i/H = 0\ \text{✓},\ \ \tfrac16\textstyle\sum(3p_i-1)^2=1=\Omega_\sigma\ \text{✓}.$$
   Un état sous-Kasner (`Ω_σ<1`) de même direction : `σ_i/H = √(Ω_σ)·(3p_i−1)`.

**Direction de forme du sceau (épinglée).** Le sceau part de `w0=(ε,−ε,0)`, soit la direction
**`(1,−1,0)/√2`** ; `ε := |w|/√2` y vaut exactement `ε`. C'est le `n̂` (angle `χ`) de référence ;
tout balayage de `χ` doit contenir ce point.

**Divergence de la forme au bang (conséquence directe).** Près du bang, `σ_i/H→3p_i−1=const`
⟹ `dw_i/dN=const` ⟹ **`w_i` croît linéairement en `N` et diverge à `a→0`**. Le petit-`ε`
n'a donc de sens qu'en **ère radiation (spec A)** ; la **spec B (deep-bang) doit travailler en
variables `Σ_i`/`u` (cercle de Kasner), pas en `w` petit**. La forme gelée `ε_out` reste
l'observable, mesurée à 𝓘 *après* l'isotropisation.

---

## 2. Vecteur d'état et espace des phases `[formalisable]`

État du noyau §2 (diagonal Bianchi IX, `8πG=1`, `N=ln a`) :

$$\big(\,w_1,w_2\ (w_3=-w_1-w_2)\ ;\ \sigma_1,\sigma_2\ (\sigma_3=-\sigma_1-\sigma_2)\ ;\ \rho\ ;\ H\,\big),\quad \varphi,\dot\varphi\ \text{si P7 activé}.$$

- **Forme** `w_i` : 2 ddl, plan `Σw_i=0`. Direction `n̂` + magnitude `ε := |w|/√2` (def du sceau).
- **Cisaillement** `σ_i=ẇ_i` : 2 ddl, plan `Σσ_i=0`. Magnitude sans dimension `Ω_σ=σ²/3H²`
  (Kasner = 1) ; direction par `σ_i/H=3p_i−1` (§1bis). Le code monitore `Σ_code=σ/3H` (Kasner
  `1/√3`).
- **Échelle** : `H` fixé par la contrainte une fois `(w,σ,ρ,Λ,φ)` choisis ; `a` porté par `N`.

La tranche sealée = `{σ_1=σ_2=0 ; w(0)=ε·n̂ ; ρ,Λ en ère radiation}` (1-paramètre `ε`, secteur
cisaillement fermé). P6 **ouvre le secteur cisaillement**.

---

## 3. Les boutons de la paramétrisation `[formalisable]`

Cinq paramètres, dont **un** est le levier de stabilité :

1. **`ε`** — magnitude d'anisotropie de forme (petit pour le POC ; balayé ensuite). Bouton hérité.
2. **`n̂`** — direction de la forme dans le plan `w` (angle `χ`). Le sceau a fixé une direction ;
   à varier pour exclure une dépendance d'orientation parasite (subtilité #3, rotation ~7°).
3. **`Ω_σ`** (ou `δ:=Σ_code=σ/3H`, avec `Ω_σ=3δ²`) — **magnitude du cisaillement = le levier de
   stabilité.** `Ω_σ=0` ⟶ limite quiescente (récupère le sceau) ; `Ω_σ=1` ⟶ bang Kasner sous vide.
4. **`ψ`** — direction du cisaillement *relativement à* `n̂` (angle relatif). `ψ=0` : le
   cisaillement renforce la forme existante ; `ψ≠0` : il la fait tourner (worst-case à chercher).
5. **`u`** (variante deep-bang seulement) — paramètre BKL de Kasner sur le cercle
   (`p_i(u)`, `u∈[1,∞)`), qui fixe *quel axe* s'effondre. Sélectionne le point de départ sur le
   cercle de Kasner ; n'intervient qu'en spec (B).

**Contenu matière** : `ρ`, `Λ` au **point fixe de l'atlas** (`mλ=9k²/4`, identification
`ρ_0∝m, Λ∝λ` — réf. `ρ_0=100, Λ=1`), exprimés au point de départ near-bang via leur scaling.
φ (P7) : optionnel, isotrope ⟹ n'ouvre pas de ddl anisotrope mais peut concurrencer `σ²` s'il
est cinétiquement raide (`Ω_φ∝a^{-6}`) — `[à activer en variante, décision ouverte]`.

---

## 4. Deux specs de départ `[formalisable]`

### (A) Départ ère-radiation, résolu plus profond — **POC / test de stabilité**
- **État** : `Ω_rad≈1` (radiation dominante), `Ω_σ=δ²·(…)` *petit* (le bouton), forme `ε·n̂`,
  à `a=a_start` où la radiation domine encore mais plus profond que le sceau.
- **Teste** : la configuration `σ≈0` radiation-era est-elle **stable** contre une perturbation
  de cisaillement `δ` quand on la résout plus près du bang ? `ε_out(δ)` retourne-t-il à la
  valeur sealée quand `δ→0` (quiescent/stable) ou diverge/erratique (chaotique) ?
- **Vertu** : départ minimal du sceau, **continu** avec `κ≈0.81` (limite `δ→0`). Intégrable au
  noyau §2 + Radau **sans** billard. C'est le premier calcul.

### (B) Départ deep-bang Kasner — **P6 complet**
- **État** : sur/près du cercle de Kasner (`Ω_σ≈1`), paramétré par `u` + axe, germe de radiation
  `Ω_rad` petit ; intégrer **en avant** à travers les rebonds éventuels → isotropisation Wald →
  ère radiation → 𝓘 suivant.
- **Teste** : le bang *générique* — l'anisotropie de forme CCC est-elle même atteignable, et
  quelle **distribution** de `κ` en émerge ?
- **Coût** : si rebonds chaotiques, l'accumulation est non intégrable par solveur direct ⟹
  **brancher l'oracle DHN/billard** (carte de Kasner / `u`-map de Gauss : map état entrant →
  sortant analytiquement, puis rendre la main au noyau §2). À ne payer que si (A) révèle des
  rebonds.

**Ordre prescrit** : (A) d'abord (tranche les variables ET sert de POC) ; (B) seulement si (A)
montre que la quiescence est instable.

---

## 5. Procédure de satisfaction de contrainte `[formalisable — conventions §1bis]`

On ne peut PAS fixer `(w,σ,ρ,Λ,H)` librement : la contrainte (§1) lie le tout, et `³R` est
**déterminé** par `w_i` et `a` (Milnor), non libre. **Mais il n'y a aucune racine à chercher**
si l'on ancre l'échelle au lieu de la « résoudre » (cf. §5bis). Recette propre :

1. **Ancrer l'échelle** `a_start = 1` (comme le sceau ; `Λ=1` fixe l'unité). Alors `³R = F(ε)`
   est un **nombre** (Milnor à `a=1`), pas une fonction d'un inconnu.
2. Choisir la **forme** : magnitude `ε`, direction `n̂` (réf. `(1,−1,0)/√2`, §1bis).
3. Choisir le **cisaillement** : magnitude `Ω_σ` (le bouton), direction par `p_i(u)` (carte
   `σ_i/H=3p_i−1`, §1bis) ; angle relatif `ψ` entre direction de cisaillement et `n̂`.
4. **`H²` est alors EXPLICITE** (équation linéaire, cf. §5bis), puis
   `σ_i = H√(Ω_σ)(3p_i−1)`, `ρ=ρ0`, `Λ=1`. **Vérifier le résidu de contrainte `< 1e-12`**
   (analogue du `1e-14` de P7).

---

## 5bis. Non-ambiguïté de l'IC-builder — formule explicite `[établi — vérifié vs Milnor]`

**Diagnostic de l'angle mort.** La crainte d'une racine `a` multiple venait d'une formulation
qui demandait de *résoudre* `−³R(ε,a)/6H² = Ω_courb` pour `a` — ce qui mélange deux ancrages
(dimensionnel `vs` sans-dimension) et fabrique une équation implicite **inutile**. `a` est un
**ancrage de jauge**, pas une inconnue à résoudre.

**Formule.** Ancré `a=1`, `Λ=1`, cisaillement spécifié par `Ω_σ` : la contrainte
`3H²=ρ0+Λ+σ²−½³R` avec `σ²=3H²Ω_σ` et `³R=F(ε)` donne une équation **linéaire** en `H²` :

$$\boxed{\ 3H^2 = \frac{\rho_0 + \Lambda - \tfrac12 F(\varepsilon)}{1 - \Omega_\sigma}\ },\qquad
F(\varepsilon) = -2\cosh^2 2\varepsilon + 2\cosh 2\varepsilon + \tfrac32\ \approx\ \tfrac32 - 4\varepsilon^2.$$

`F(ε)` est la courbure scale-free de la direction `(1,−1,0)/√2` (Milnor) — **vérifiée à 1e-16
contre `ricci3_components` du sceau** sur `ε∈[0,0.7]`. Solution **unique et explicite** : pas
de racine, pas de branche. Puis `σ_i = H√(Ω_σ)(3p_i−1)`. À `Ω_σ=0` : `3H²=ρ0+Λ−½F(ε)`, soit
**exactement le `H0` du sceau** (vérifié : `ε=0.02⟹H0=5.7807` des deux côtés).

**Conditions de validité** (ce qui *remplace* « unicité » — trois inégalités, pas une racine) :
1. `1 − Ω_σ > 0` ⟺ `Ω_σ < 1`. `Ω_σ=1` = bord Kasner sous vide (`H→∞`), le bang même ;
   approché, pas atteint.
2. numérateur `ρ0 + Λ − ½F(ε) > 0` (trivial pour `ρ0≫1` ; ne casse que si `ρ0` minuscule ∧
   `F` grand positif — hors régime).
3. **signe de `F`** : `F>0` pour `ε < 0.48121` (`cosh2ε<3/2` : courbure S³ positive) ;
   `F<0` au-delà (le squash bascule en courbure scalaire **négative**). Le POC petit-`ε` est
   toujours dans `F>0`. *(À `ε=0.4812`, `F=0` : la courbure ne fixe plus de signe — cas
   dégénéré à éviter comme point de départ.)*

**`a` n'est pas une racine, c'est un ancrage.** « Partir plus tôt dans le bang » ne se code
**pas** en choisissant un `a` plus petit (pure jauge, relabel de `N`) : la profondeur physique
est portée par les **ratios sans dimension** `(Ω_σ, Λ/ρ0, ε)`. Le levier neuf de P6 est `Ω_σ`,
qui entre `H²` linéairement — donc sans aucune ambiguïté.

**Conséquence pour la spec (B) `[à graver]`.** Avec courbure **positive** (petit `ε`), un état
Kasner deep-bang *statique* **n'existe pas** : `³R>0` se soustrait à `3H²`, incompatible avec
`σ²≈3H²` (Kasner). Bianchi IX près du bang est **intrinsèquement oscillatoire** — époques de
Kasner (`³R` négligeable entre murs) + rebonds (`³R` spike quand un axe s'effondre). L'IC de (B)
n'est donc pas un point fixe mais un **état Kasner entre-murs** : `Ω_σ=1`, germes `ρ,Λ`
négligeables, `a` choisi assez petit pour que `a^{−2}F ≪ σ²` — **inégalité unilatérale**, pas
une racine. La direction de forme **tourne** à travers les rebonds (donc `F` n'y est pas fixe :
c'est `verif_D3_P6_bang.py` qui suivra cette rotation, pas une formule fermée).

---

## 6. Réduction au sceau & diagnostics `[formalisable]`

**Test de réduction (obligatoire, avant tout balayage).** L'IC-builder avec `Ω_σ=0`, direction
de forme `(1,−1,0)/√2`, départ remis en ère radiation (`ρ0=100, Λ=1`) doit produire une
trajectoire **identique** à `evolve()` du sceau (même chemin de code) ⟹ `ε_{n+1}=κ ε_n` avec la
valeur imprimée par le sceau (`κ≈0.81–0.816` selon `Nmax` ; pente moyenne sur `ε∈{0.02..0.2}`).
Concrètement : appeler l'IC-builder puis le `rhs` du noyau doit redonner `eps_out()` à la
précision machine. Si l'écart dépasse `~1e-10`, la paramétrisation ou une convention §1bis est
mal reportée — corriger avant d'aller plus loin.

**Diagnostics à enregistrer** (le diagnostic chaos/quiescence du cadrage) :
- `Ω_σ(N)=σ²/3H²` et son maximum le long de l'orbite (reste ≪1 ⟹ quiescent).
- amplitude des `N_i` de Bianchi IX (pics = murs/rebonds) ; **compter les rebonds**.
- `ε_out` (forme gelée à 𝓘) **en fonction de `Ω_σ`, `ψ`, `χ`** : plateau en `δ→0` ⟹ stable.
- angle `cos(w_0,w_∞)` (précession parasite, subtilité #3).
- résidu de contrainte tout du long (`< 1e-12`).

**Issues** (= les trois du cadrage) : `Ω_σ` reste ≪1 ⟹ quiescent (κ nombre, billard rangé) ;
un-deux rebonds puis isotropisation ⟹ intermédiaire (κ nombre corrigé) ; rebonds qui se
multiplient ⟹ chaotique (κ distribution, oracle DHN).

---

## 7. Décisions de modélisation à trancher dans la note `[décision ouverte]`

1. **Orientation worst-case `ψ`.** Faut-il rapporter `κ` pour `ψ` aligné, orthogonal, ou la pire
   valeur sur `[0,π)` ? Proposition : balayer `ψ` au POC, rapporter l'enveloppe.
2. **GWE Meissner-Penrose (`2503.24263`, subtilité #4).** Si le crossover est dominé par des
   ondes gravitationnelles, le bang porte une source de Weyl directe ⟹ `Ω_σ` de départ **non
   nul imposé par la physique**, pas un simple bouton. À confronter : la spec (A) avec `δ` fixé
   par l'amplitude GW plutôt que balayé. `[lien P6 ↔ D3, à examiner]`
3. **Genericité (piège Heinzle-Uggla).** Type IX = 3 constantes de structure de même signe,
   *trompeur* pour le générique : toute conclusion de chaos/quiescence en IX **borne** ce qu'on
   peut dire du cas inhomogène. À écrire comme réserve explicite du verdict P6.
4. **φ raide ?** Activer `ρ_φ∝a^{-6}` en variante pour voir s'il *supprime* le chaos (mécanisme
   de quiescence Belinski-Khalatnikov / AVTD) — mais P7 a établi φ **homogène/isotrope**, donc il
   ne crée pas d'anisotropie ; son rôle serait seulement de concurrencer `σ²` dans la contrainte.
   `[variante secondaire]`

---

## 8. Premier pas concret (après validation de cette spec)
> Coder l'IC-builder de §5bis (formule `H²` explicite, `σ_i=H√Ω_σ(3p_i−1)`, résidu `<1e-12`)
> → **test de réduction §6** (`Ω_σ=0` ⟹ trajectoire ≡ `evolve()` sealé, `κ≈0.81`) → spec (A)
> POC : balayer `Ω_σ` à petit `ε`, enregistrer les diagnostics §6 → lire l'issue (quiescent /
> intermédiaire / chaotique) → décider si (B)+billard. Consigner dans `LC-D3-INTERAEON-P6`
> (sceau `verif_D3_P6_bang.py`).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte` (cf. `LC-00-INDEX`).
*Discipline d'audit : un `établi` de sceau = « l'algèbre est correcte », à l'ordre dominant ;
jamais « la physique de la CCC est établie ». Ici sont `établi` : le fait §1 (σ(0)=0 absent à
a→0), la structure de la contrainte, et les conventions §1bis (lues dans le code sealé) ; le
reste — paramétrisation, specs (A)/(B), diagnostics — est `formalisable`, non encore exécuté.*
