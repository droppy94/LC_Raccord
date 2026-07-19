---
id: LC-D3-CROSSOVER-ATTRACTEUR
titre: "Module D / crossover — porte (ii) : la sélection WCH (P=9k²/4) NE devient PAS un attracteur dynamique — obstruction structurelle det J*=1"
codename: LC-RACCORD
tags: [module-D, D3, crossover, attracteur, back-reaction, runaway, atlas, point-fixe, weyl, WCH, candidat-5, D1, planck, preservation-aire, porte-ii]
type: chaînon (front (a) — porte (ii) ; teste si la back-réaction a2 DRIVE P vers P* ⟹ dériverait A4)
statut: porte (ii) minimale RÉFUTÉE — aucune back-réaction isotrope sur λ ne dérive A4 ; det J*=1 (préservation d'aire) interdit l'attracteur ; verdict neutre/répulseur établi, attracteur exigerait déformation de DEUX invariants (à inventer)
version: 0.1
langue: fr
date: 2026-06-08
statut_id: provisoire — à enregistrer si validé (index, programme [D]/crossover, glossaire, refs, audit-verdict)
fichier_compagnon: verif_D3_crossover_attracteur.py, verif_D3_crossover_attracteur_stress.py
renvois: [LC-D3-CROSSOVER-STABILITE, LC-D3-CROSSOVER-BACKREACTION, LC-D3-CROSSOVER-MATCHING, LC-D3-WEYL-BUNCHDAVIES, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-E-PLANCK-RESIDUEL, LC-D-HOLOGRAPHIE-G3, LC-D3-FRONT-A-SYNTHESE, LC-WORK-REPRISE-POST-FRONT-A, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D3] WCH (marée bornée) — testée comme attracteur dynamique de l'itération inter-éons"
  - "[A]/D1 candidat #5 — le point fixe non-hyperbolique reste posé, non dérivé"
  - "[E] — la coupure holographique N source la back-réaction mais ne brise pas det=1"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·CROSSOVER — Porte (ii) : la sélection WCH n'est pas un attracteur (obstruction det J*=1)

> **Cible (porte (ii) de `LC-D3-FRONT-A-SYNTHESE` / `LC-WORK-REPRISE-POST-FRONT-A`).** (a3,
> `LC-D3-CROSSOVER-STABILITE`) a montré `WCH ⟺ #5 ⟺ P=mλ=9k²/4` comme une **sélection** : `P`
> étant conservé par la récurrence de l'atlas, rien ne *drive* vers `P*` — le fine-tuning
> subsiste. (a2, `LC-D3-CROSSOVER-BACKREACTION`) a montré que la back-réaction de Bunch–Davies
> est **isotrope** et **renormalise le fond `(m,λ)`** (`δλ~H⁴~λ²`), alimentant l'itération.
> **Question testée :** cette renormalisation, régularisée par la coupure holographique `N`
> (`LC-E`), modifie-t-elle `P` d'éon en éon de façon à le **driver vers `P*`** ? Si oui, la WCH
> cesse d'être posée : elle devient une **conséquence dynamique** (A4 dérivée), et (A) passerait
> à `établi (sous A3, CCC)` — le résultat le plus fort visable par le front (a).
>
> **Verdict (calculé, `verif_D3_crossover_attracteur.py` + `..._stress.py`).** **NON. La porte
> (ii) minimale ne dérive pas A4.** La récurrence de l'atlas est **préservatrice d'aire** : son
> Jacobien au point fixe a `det J* = 1` **pour toute** back-réaction `δλ(λ)` ajoutée à `λ` seul
> (parce que `m' = P*/λ` ne dépend pas de `m`). Donc `μ₁μ₂ = 1` ⟹ `|μ₁||μ₂| = 1` ⟹ on **ne peut
> pas** avoir les deux valeurs propres dans le disque unité : **un attracteur linéaire est
> impossible**. Le verdict ne dépend que de `s ≡ δλ′(λ*)` : `s=0` ⟹ `μ=1` double défective
> (NEUTRE) ; `−4<s<0` ⟹ centre marginal `|μ|=1` (NEUTRE) ; `s>0` ou `s≤−4` ⟹ `|μ|>1`
> (RÉPULSEUR). **Jamais attracteur.** `[établi]`
>
> **Portée honnête.** C'est un résultat **`neutre`/`répulseur`** au sens de
> `LC-WORK-REPRISE-POST-FRONT-A §5` — **légitime et fort** : il transforme la *question ouverte*
> (« la back-réaction drive-t-elle `P` ? ») en une **obstruction structurelle précise** (la
> préservation d'aire de la récurrence Penrose-cohérente). **A4 reste un socle posé** ; **(A)
> reste `formalisable` conditionnel à A2 — inchangé.** Le seul chemin restant vers un attracteur
> — déformer **les deux** invariants `tr` *et* `det` du point fixe de Jordan — requiert **deux**
> ingrédients holographiques non fournis par a2/a3/E : `à inventer / hors de portée`.

---

## 0. Rôle et garde-fou

Ce chaînon **instruit la porte (ii)** — la voie la plus décisive ouverte par la synthèse du
front (a) — et lui donne son verdict. Ce qui est `établi` : l'obstruction `det J* = 1` (analytique,
confirmée numériquement à `2,2×10⁻¹⁶` sur 192 configurations) et la classification complète des
verdicts par `s = δλ′(λ*)`. Ce qui reste `à inventer / hors de portée` : un mécanisme qui
déformerait simultanément `tr` et `det` (back-réaction *dissipative* sur `m'` + frein sur `λ'`),
nécessairement issu d'une physique holographique non dérivée (circularité `N` de `LC-E` non brisée).

**On ne surclasse pas (discipline `LC-AUDIT-VERDICT §6.4`).** Un sceau d'attracteur aurait attesté
« la récurrence numérique converge », **jamais** « la WCH est prouvée ». Symétriquement, le présent
verdict atteste « la récurrence ne converge pas (obstruction d'aire) », **non** « la CCC est
réfutée » : c'est A4 *comme attracteur de cette récurrence minimale* qui est réfutée, pas la CCC.
A3/A4 ne sont **pas rouverts** ; « le bang gagne » (P6 B) reste le cadre. **Aucune régression** :
la synthèse du front (a) est intacte, A4 reste un socle posé exactement comme avant.

---

## 1. La récurrence modifiée et le critère pré-enregistré `[cadre]`

Squelette `établi` (a3) — récurrence de l'atlas, classe Penrose-cohérente, `P* = 9k²/4` :

$$m' = \frac{9k^2}{4\lambda} = \frac{P^\*}{\lambda},\qquad
\lambda' = \frac{4\lambda^2 m}{9k^2} = \frac{P}{P^\*}\,\lambda\quad(P=m\lambda).$$

Canal `établi` (a2) — la back-réaction isotrope renormalise `λ(=Λ)` ; scaling `δλ~H⁴~λ²`, la
forme paramétrée portant la régularisation holographique étant `δλ(λ) = c(λ;N)\,λ²`. **Récurrence
modifiée** (la back-réaction s'ajoute à `λ'` seul — c'est tout ce que a2 autorise) :

$$\boxed{\ m_{i+1} = \frac{P^\*}{\lambda_i},\qquad
\lambda_{i+1} = \frac{P_i}{P^\*}\,\lambda_i + \delta\lambda(\lambda_i)\ }
\quad\Longrightarrow\quad
\delta P_i = P_{i+1}-P_i = \frac{P^\*}{\lambda_i}\,\delta\lambda(\lambda_i).$$

**Critère pré-enregistré (CONSORT / `LC-AUDIT-VERDICT §9`, figé AVANT exécution).** Le candidat
`(m*,λ*)`, `m*λ*=P*`, n'est un point fixe que si `δλ(λ*)=0` (sinon `P*` n'est pas conservé). Alors,
sur la linéarisation 2D (valeurs propres `μ` de `J*`) :

| verdict | condition | lecture |
|---|---|---|
| **attracteur** | `P*` fixe ET `max\|μ\|<1` | `sign(dP/déon)` change `+→−` en traversant `P*` ⟹ **A4 dérivée** |
| **répulseur** | `max\|μ\|>1` (ou `P*` non fixe, `P` dérive) | CCC instable même sous WCH (réfutation partielle) |
| **neutre** | `max\|μ\|=1` (centre/Jordan) | `P` orbite, ne converge pas — sélection **reste posée** |

Les trois sont publiables (`LC-WORK-REPRISE-POST-FRONT-A §5`).

---

## 2. Obstruction structurelle : `det J* = 1` pour toute back-réaction sur `λ` `[établi]`

Sceau [1] (`verif_D3_crossover_attracteur.py §1`, `..._stress.py §S1`). Le Jacobien de la récurrence
modifiée au point fixe, en `(m,λ)` :

$$J^\* = \begin{pmatrix} \partial_m m' & \partial_\lambda m' \\ \partial_m \lambda' & \partial_\lambda \lambda' \end{pmatrix}
= \begin{pmatrix} 0 & -\,P^\*/\lambda^2 \\[3pt] \lambda^2/P^\* & \ 2 + s \end{pmatrix},\qquad s \equiv \delta\lambda'(\lambda^\*).$$

Le point décisif : **`m' = P*/λ` ne dépend pas de `m`** (`∂_m m' = 0`). Donc

$$\det J^\* = (\partial_m m')(\partial_\lambda \lambda') - (\partial_\lambda m')(\partial_m \lambda')
= 0 - \Big(-\tfrac{P^\*}{\lambda^2}\Big)\Big(\tfrac{\lambda^2}{P^\*}\Big) = 1
\qquad \textbf{indépendamment de } \delta\lambda.$$

La récurrence reste **préservatrice d'aire** (symplectique 2D) quelle que soit la back-réaction
isotrope ajoutée à `λ`. **Vérifié numériquement** : sur une grille `(c0,λ*,k)` × {douce,dure,balance}
de **192 configurations**, `det J* = 1` à `2,2×10⁻¹⁶`. `[établi]`

**Conséquence immédiate.** `μ₁μ₂ = det J* = 1` ⟹ `|μ₁|\,|μ₂| = 1`. On ne peut donc **pas** avoir
`|μ₁|<1` *et* `|μ₂|<1` : **l'attracteur linéaire est structurellement impossible.** Le baseline
conservatif (`δλ=0`, `s=0`) redonne exactement `μ=1` double défective — le point non-hyperbolique de
(a3) / candidat #5 (cohérence avec `LC-D3-CROSSOVER-STABILITE [3]`). `[établi]`

---

## 3. Classification complète des verdicts par `s = δλ′(λ*)` `[établi]`

Sceau [2]–[S3]. Avec `det J* = 1` fixé, le verdict ne dépend que de la trace `tr J* = 2 + s` (donc
du seul `s = δλ′(λ*)`). Discriminant `Δ = tr² − 4 = s(s+4)` :

| régime de `s` | valeurs propres `μ` | verdict |
|---|---|---|
| `s = 0` | `μ=1` double, **défective** (Jordan) | **NEUTRE** (drift séculaire polynomial) |
| `−4 < s < 0` | complexes conjuguées, `\|μ\|=√det=1` (**centre**) | **NEUTRE** (`P` orbite `P*`) |
| `s > 0` | réelles, produit `1`, une `>1` | **RÉPULSEUR** |
| `s ≤ −4` | réelles `<0`, produit `1`, une `\|μ\|>1` | **RÉPULSEUR** (instabilité de période 2) |

**Application aux trois closures** (`N = S_dS = 3π/(Λℓ_P²)`, `Λ=λ` ⟹ `N∝1/λ`) :

- **douce** (coupure de Hubble, `ρ~Λ²` ⟹ `c≈const`) : `δλ(λ*)≠0` ⟹ `P*` **pas un point fixe**,
  `P` dérive (`ΔP>0`) ⟹ **RÉPULSEUR / runaway**.
- **dure** (Cohen–Kaplan–Nelson, `ρ~Λ²N`, `N∝1/λ` ⟹ `c` croît) : `δλ(λ*)≠0` de même ⟹ **RÉPULSEUR**
  (runaway plus raide).
- **balance** (compétition bain de gravitons `↑` vs reset d'entropie de Weyl `↓`, `LC-E §5` ; zéro
  en `λ*`) : `δλ(λ*)=0` ⟹ `P*` **fixe** ; `s = δλ′(λ*) = −c_0λ^\* < 0` ⟹ pour `c_0λ^\*<4`, centre
  marginal `|μ|=1` ⟹ **NEUTRE** ; pour `c_0λ^\*≥4` ⟹ **RÉPULSEUR**. (Réf : `μ=0,9625±0,271i`,
  `|μ|=1`, `tr=1,925` à `c_0=0,05, λ^\*=1,5`.)

**Robustesse (stress-test, `..._stress.py`).** Le balayage `(c0,λ*,k)` (S2) et **8 formes** de
closure balance (S3 : zéro simple, `λ³`, `λ`, zéro **double** → `s=0`, `sin`, `tanh` saturant,
balance **inversée** → `s>0`, zéro+courbure) donnent **toutes** NEUTRE ou RÉPULSEUR : **aucun
attracteur, nulle part.** Le verdict est une **obstruction structurelle**, pas un accident de
paramétrage ni de forme. `[établi]`

---

## 4. Ce qu'il faudrait pour un attracteur : déformer DEUX invariants `[à inventer / hors de portée]`

Sceau [3]. Au point fixe non modifié, `(tr, det) = (2, 1)` : c'est le **sommet** du triangle de
stabilité de Schur (`|tr| < 1+det` et `det < 1`). Pour `|μ₁|,|μ₂|<1` il faut **descendre `tr` ET
`det`** :

- **(3a) un seul terme dissipatif sur `m'`** (`m' = (P^\*/λ)(1+g(λ−λ^\*)/λ^\*)`, `g=0,3`) :
  abaisse `det` à `1−g=0,70`, mais `tr≈2` est **hérité du bloc de Jordan** (`∂_λλ' = 2mλ/P^\* = 2`)
  et reste hors du triangle ⟹ `|μ|max=1,44` ⟹ **RÉPULSEUR (saddle)**. *Un `δm` seul ne suffit pas.*
- **(3b) déformer aussi `∂_λλ'`** (frein sur la croissance de `λ`, `g=0,3, q=0,6`) : `det=0,70`,
  `tr=1,33` ⟹ `|μ|max=0,84` ⟹ **ATTRACTEUR** — mais au prix de **deux** ingrédients indépendants.

Ces deux déformations ne sont **pas** fournies par a2 (qui ne donne qu'une renormalisation isotrope
de `λ`, donc `δλ` sur `λ'` seul) ni par a3, ni par E (qui fournit `N`, pas une dissipation). Elles
sont **pure conjecture** : la coupure `N` reste circulaire (`LC-E`), et rien ne dérive un canal
dissipatif sur `m'`. `[à inventer / hors de portée]`

---

## 5. La coïncidence est confirmée, mais reste une SÉLECTION `[synthèse]`

(a3) avait établi `WCH ⟺ #5 ⟺ P=9k²/4` comme **sélection**. La porte (ii) testait si la dynamique
la promeut en **dérivation**. Le verdict : **non, par obstruction d'aire.** La sélection est donc
**confirmée dans son statut** — unifiée, physiquement motivée (« faible Weyl = marée bornée =
stabilité »), mais **non dérivée**. Le fine-tuning `m̂λ̂ = 9k²/4` subsiste. A4 reste un socle posé.

<svg width="100%" viewBox="0 0 680 392" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Porte (ii) : la back-réaction ne dérive pas A4 — obstruction det J*=1</title>
  <desc>La récurrence modifiée a m prime égal P étoile sur lambda, qui ne dépend pas de m ; donc le déterminant du Jacobien au point fixe vaut un, indépendamment de la back-réaction delta lambda. Le produit des valeurs propres vaut donc un, ce qui interdit que les deux soient dans le disque unité : aucun attracteur n'est possible. Le verdict ne dépend que de s égal la dérivée de delta lambda en lambda étoile. Trois closures : douce et dure, de signe constant, donnent un répulseur ou runaway car P étoile n'est même pas un point fixe ; la closure balance, qui s'annule en lambda étoile, donne un centre marginal de module un, donc neutre, P orbite sans converger. Verdict global : jamais attracteur, la sélection WCH reste posée, A4 reste un socle. Pour obtenir un attracteur il faudrait déformer les deux invariants trace et déterminant du point fixe de Jordan, deux ingrédients holographiques non dérivés, à inventer.</desc>
  <rect x="40" y="34" width="600" height="52" rx="9" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.9"/>
  <text x="340" y="56" text-anchor="middle" font-size="12.5" font-weight="500" fill="#3C3489">récurrence modifiée : m′=P*/λ (indép. de m) ,  λ′=(P/P*)λ + δλ(λ)</text>
  <text x="340" y="76" text-anchor="middle" font-size="12.5" font-weight="600" fill="#3C3489">⟹ det J* = 1  ∀ δλ  (préservation d'aire)  ⟹  |μ₁||μ₂|=1  ⟹  attracteur IMPOSSIBLE</text>
  <rect x="40" y="100" width="190" height="118" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="135" y="122" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">douce (ρ~Λ²)</text>
  <text x="135" y="146" text-anchor="middle" font-size="11" fill="#3d3d3a">δλ(λ*)≠0 ⟹ P* non fixe</text>
  <text x="135" y="166" text-anchor="middle" font-size="11" fill="#3d3d3a">P dérive (ΔP&gt;0)</text>
  <text x="135" y="194" text-anchor="middle" font-size="12.5" font-weight="600" fill="#993C1D">RÉPULSEUR</text>
  <rect x="245" y="100" width="190" height="118" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="340" y="122" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">dure (CKN, ρ~Λ²N)</text>
  <text x="340" y="146" text-anchor="middle" font-size="11" fill="#3d3d3a">δλ(λ*)≠0 ⟹ P* non fixe</text>
  <text x="340" y="166" text-anchor="middle" font-size="11" fill="#3d3d3a">runaway plus raide</text>
  <text x="340" y="194" text-anchor="middle" font-size="12.5" font-weight="600" fill="#993C1D">RÉPULSEUR</text>
  <rect x="450" y="100" width="190" height="118" rx="8" fill="#FBF3E7" stroke="#C98A2B" stroke-width="0.7"/>
  <text x="545" y="122" text-anchor="middle" font-size="12" font-weight="500" fill="#8A5A12">balance (zéro en λ*)</text>
  <text x="545" y="146" text-anchor="middle" font-size="11" fill="#3d3d3a">P* fixe ; s=−c₀λ*&lt;0</text>
  <text x="545" y="166" text-anchor="middle" font-size="11" fill="#3d3d3a">centre |μ|=1 (orbite)</text>
  <text x="545" y="194" text-anchor="middle" font-size="12.5" font-weight="600" fill="#8A5A12">NEUTRE</text>
  <rect x="40" y="232" width="600" height="50" rx="9" fill="#FBF3E7" stroke="#C98A2B" stroke-width="0.9"/>
  <text x="340" y="254" text-anchor="middle" font-size="12.5" font-weight="600" fill="#8A5A12">VERDICT : jamais attracteur ⟹ la sélection WCH (P=9k²/4) RESTE POSÉE</text>
  <text x="340" y="272" text-anchor="middle" font-size="11" fill="#3d3d3a">A4 reste un socle ; (A) reste « formalisable » conditionnel à A2 — INCHANGÉ ; aucune régression</text>
  <rect x="40" y="296" width="600" height="64" rx="9" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="340" y="318" text-anchor="middle" font-size="12" font-weight="500" fill="#0F6E56">seul chemin vers un attracteur (à inventer) :</text>
  <text x="340" y="338" text-anchor="middle" font-size="11.5" fill="#3d3d3a">quitter le sommet du triangle de Schur (tr=2, det=1) en déformant DEUX invariants</text>
  <text x="340" y="354" text-anchor="middle" font-size="11.5" fill="#3d3d3a">δm dissipatif sur m′ ET frein sur λ′ — deux ingrédients holographiques NON dérivés (N circulaire)</text>
  <text x="340" y="382" text-anchor="middle" font-size="10.5" fill="#73726c">§6.4 : « la récurrence ne converge pas » ≠ « la CCC est réfutée » — c'est A4-comme-attracteur qui l'est.</text>
</svg>

*Fig. — Porte (ii). `m′=P*/λ` indépendant de `m` ⟹ `det J*=1` (violet) quelle que soit la
back-réaction ⟹ attracteur impossible. Les closures de signe constant (rouge) sont répulseurs
(`P*` pas fixe) ; la balance (ambre) est un centre marginal (neutre). Verdict (ambre) : la
sélection reste posée, A4 reste socle. Un attracteur (vert) exigerait de déformer `tr` ET `det` —
`à inventer`.*

---

## 6. Format de chaînon

- **Hypothèse testée.** La back-réaction isotrope de Bunch–Davies (a2), régularisée par `N` (E),
  drive-t-elle l'invariant `P=mλ` vers `P*=9k²/4` (attracteur dynamique) — ce qui **dériverait A4** ?
- **Outil.** Récurrence de l'atlas modifiée (`m′=P*/λ`, `λ′=(P/P*)λ+δλ(λ)`) ; Jacobien 2D et
  valeurs propres via `tr/det` (snap du point de Jordan) ; triangle de stabilité de Schur ; trois
  closures holographiques (douce/dure/balance) ; balayage `(c0,λ*,k)` et 8 formes de balance ;
  critère pré-enregistré. Sceaux `verif_D3_crossover_attracteur.py` (+ `..._stress.py`), numpy.
- **Critère de réfutation.** *Issue « attracteur »* : si une closure donnait `max|μ|<1` à `P*`
  fixe, A4 serait dérivée. **Non observé** — `det J*=1` l'interdit structurellement. *Issue
  symétrique testée* : la closure balance EST un point fixe, et donne un centre (neutre), jamais
  un puits. La réfutation de la porte (ii) minimale est donc **constructive** (obstruction d'aire).
- **Verdict.** `det J* = 1 ∀ δλ(λ)` `[établi]` ⟹ attracteur linéaire impossible `[établi]`.
  Closures douce/dure → **répulseur** ; balance → **neutre** `[établi, robuste S1–S4]`. **A4 NON
  dérivée ; sélection P=9k²/4 reste posée ; (A) `formalisable` cond. A2 inchangé.** Déformation des
  deux invariants (`tr` ET `det`) pour un attracteur `[à inventer / hors de portée]`.

---

## 7. Conséquences pour le programme

- **La porte (ii) — la plus décisive du front (a) — est close sur un `neutre`/`répulseur`.** Le
  front (a) reste **cartographié, non démontré** : `LC-D3-FRONT-A-SYNTHESE` est **inchangée** ((A)
  `formalisable` conditionnel à A2 ; A3/A4 socles posés). Le présent chaînon **ne propage aucun
  surclassement** ; il *renforce* l'honnêteté de la synthèse en fermant la seule voie qui aurait
  pu dériver A4 par la dynamique minimale.
- **Acquis propre (publiable).** L'obstruction `det J*=1` est un énoncé **positif** : la récurrence
  Penrose-cohérente de l'atlas est **symplectique** ; aucune back-réaction isotrope (le seul canal
  que a2 autorise) ne peut la rendre dissipative. C'est *pourquoi* la WCH ne peut être qu'une
  sélection dans ce cadre, et non un attracteur — un fait structurel, pas un échec numérique.
- **Redirection.** Si l'on insiste sur un attracteur, le terrain devient la **back-réaction
  anisotrope / non-linéaire complète** (porte (i)/(iii) de `LC-D3-CROSSOVER-STABILITE §6`), seule
  capable de toucher `m'` et de briser `det=1` — mais c'est exactement le secteur `décision
  ouverte / à inventer`, et il rouvrirait A3 (anisotropie), ce que la discipline déconseille sans
  idée neuve. **Alternative recommandée** : pivoter vers `LC-D3-WEYL-BUNCHDAVIES` (résidu `k³`,
  spectre primordial), physique neuve en aval du même crossover, sans dépendre de `N`.

---

## 8. Renvois, glossaire, références

**Renvois.** `LC-D3-CROSSOVER-STABILITE` (a3 : la sélection `P=9k²/4`, point fixe non-hyperbolique
— **ici testée comme attracteur**) ; `LC-D3-CROSSOVER-BACKREACTION` (a2 : la back-réaction isotrope
sur `λ`, source de `δλ`) ; `LC-D3-CROSSOVER-MATCHING` (a1) ; `LC-A-D1-FACTEUR-CONFORME` (atlas
§4-bis : la récurrence et `P*`) ; `LC-A-D1-STABILITE-WEYL` (candidat #5, le point de Jordan
reproduit ici) ; `LC-E-PLANCK-RESIDUEL` (coupure `N`, circulaire — ne brise pas `det=1`) ;
`LC-D3-WEYL-BUNCHDAVIES` (alternative `k³`) ; `LC-D3-FRONT-A-SYNTHESE` (verdict du front (a),
**inchangé**) ; `LC-WORK-REPRISE-POST-FRONT-A §3` (spec de la porte (ii)) ; `LC-AUDIT-VERDICT §6.4`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Porte (ii) (attracteur)* : test de promotion de la sélection `P=9k²/4` en attracteur dynamique
  par la back-réaction a2 ; **réfutée** dans sa forme minimale par l'obstruction `det J*=1`.
- *Obstruction de préservation d'aire (`det J*=1`)* : `m′=P*/λ` indépendant de `m` ⟹ la récurrence
  modifiée est symplectique ∀ `δλ(λ)` ⟹ `|μ₁||μ₂|=1` ⟹ aucun attracteur possible.
- *Classification par `s=δλ′(λ*)`* : `s=0` Jordan défectif (neutre) ; `−4<s<0` centre (neutre) ;
  `s>0` ou `s≤−4` répulseur. Jamais attracteur.
- *Triangle de stabilité (Schur/Jury)* : `|μ|<1` (2D) ⟺ `|tr|<1+det` et `det<1` ; le point fixe CCC
  est au **sommet** `(tr,det)=(2,1)`.
- *Closures holographiques (douce/dure/balance)* : régularisations de `ρ~∫dk k³` par `N` ; seule la
  balance (zéro en `λ*`) fait de `P*` un point fixe, et n'y produit qu'un centre.

**Références (`LC-04`, en KB v1.9).** Markwell & Stevens, GRG **55**, 93 (2023)
`[confirmé : 2212.06914v2.pdf]` — récurrence/atlas ; Penrose, *Cycles of Time* (2010) `[confirmé]`
— WCH ; Bunch & Davies, Proc. R. Soc. A **360**, 117 (1978) `[confirmé]` — back-réaction (canal,
via a2). *Méthode dynamique* (standard) : critère de Schur–Cohn / Jury (stabilité des cartes 2D) ;
cartes préservatrices d'aire (structure symplectique) — manuels de systèmes dynamiques discrets.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
