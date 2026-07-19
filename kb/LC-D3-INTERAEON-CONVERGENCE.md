---
id: LC-D3-INTERAEON-CONVERGENCE
titre: "Front (a) / clôture — l'itération ∏κ_n : sous l'hypothèse de Penrose (Λ constante), l'atlas D1 force le point fixe ⟹ ρ_0 éon-indépendante ⟹ κ constant ⟹ ∏κ_n→0 : ISOTROPISATION TOTALE dynamique multi-éon (lente). Les DEUX branches runaway (Λ→∞ et Λ→0) sont exclues par Penrose ET sans résiduel dans le domaine GO."
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, isotropisation, inter-eon, kappa, convergence, atlas-D1, point-fixe, cloture]
type: chaînon (clôture du front (a) à l'ordre dominant ; exécute §5.1 de LC-WORK-REPRISE-CLOTURE-A ; met à jour LC-D3-INTERAEON-KAPPA §5)
statut: résultat d'ordre dominant établi (∏κ_n→0 au point fixe Penrose, robuste ; runaway des DEUX côtés sans résiduel) — MAIS CONDITIONNÉ à σ(0)=0/WCH : P6 (B) (LC-D3-INTERAEON-P6 v0.2) montre que le bang générique ne préserve PAS σ(0)=0, donc ∏κ_n→0 n'est pas un mécanisme libre / valeur de κ pour bang réaliste : établi lent (κ→1)
version: 0.4
langue: fr
date: 2026-06-08
maj: "2026-06-08 — v0.4 : HOUSEKEEPING post-audit WCH-GWE (LC-AUDIT-LOG-WCH-GWE §4.5 ; wording, aucune touche à l'algèbre ni au verdict (B)) — bloc « WCH = contenu dynamique » aligné sur LC-D3-WCH-GWE v0.3 : mode régulier exact (A) ∀ kη (max 0.377), « bascule à 1.9 » = artefact leading, verrou déplacé spectre→C7. | v0.3 (addendum) : WCH = contenu dynamique (LC-D3-WCH-GWE v0.2, sceau verif_D3_WCH_GWE.py) — la conditionnalité σ(0)=0/WCH n'est pas un postulat nu au crossover réel : la GWE délivre Ω_σ=(kη)⁴ε²/27 ⟹ Ω_σ/ε²~4·10⁻³⁰–6·10⁻²⁹≪0.5 (régime A), conditionnel au spectre M-P. ∏κ_n→0 n'est plus un pur artefact de σ(0)=0 ; verdict (B) du bang générique inchangé (§5). | v0.3 : conditionnalité gravée. P6 (B) tranché (LC-D3-INTERAEON-P6 v0.2, oracle Gauss-Kuzmin) : la dérivation ∏κ_n→0 ci-dessous part de la carte ε_{n+1}=κε_n du noyau radiation-era, qui PRÉSUPPOSE σ(0)=0 (CI de Tod) à chaque éon. Or le bang GÉNÉRIQUE (Ω_σ→1) ne contracte JAMAIS (P(ε_out<κ·ε_in)=0), la carte y est additive/bang-set, non multiplicative. Donc ∏κ_n→0 est `établi CONDITIONNELLEMENT à σ(0)=0/WCH (A4)`, PAS un mécanisme dynamique libre. La CCC n'est pas réfutée (la WCH postule justement le bang non-générique) ; A3/A4 confirmés socles irréductibles. v0.2 : audit froid gravé (sceau v2) — runaway mλ>2.25 rupture éon 24 ; branche mλ<2.25 κ sature ≈0.795<1 ; aucun résiduel dans GO des deux côtés. v0.1 : couplage noyau κ ↔ atlas (m,λ), point fixe + une branche runaway."
statut_id: validé par audit (sceau v2 re-rejoué) — à enregistrer (met à jour LC-D3-INTERAEON-KAPPA §5, LC-D3-CROSSOVER-EINSTEIN3D §4, LC-02, LC-AUDIT-VERDICT, glossaire)
fichier_compagnon: [verif_D3_interaeon_convergence.py, verif_D3_interaeon_kappa.py, verif_D1_atlas.py]
prerequis_kb: [LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-MATIERE, LC-A-D1-FACTEUR-CONFORME, LC-WORK-CADRAGE-INTERAEON, LC-AUDIT-VERDICT]
renvois: [LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-MATIERE, LC-D3-WCH-GWE, LC-A-D1-FACTEUR-CONFORME, LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-CROSSOVER-ANISOTROPE, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] / front (a) — la porte (ii) sous sa seule forme licite (carte inter-éon) : franchie comme attraction TOTALE dynamique"
  - "[D3] hypothèse de Weyl — la marée g₃ ~ anisotropie de 𝓘, ici contractée à zéro multi-éon"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Interaeon·Convergence — La clôture : ∏κ_n → 0

> **Cible.** `LC-D3-INTERAEON-KAPPA` §5 laissait la **convergence de `∏κ_n`** en `décision
> ouverte` : isotropisation **totale** (`∏κ_n→0`) ou **résiduelle** (`→const>0`) ? Cela dépend
> de la suite `(ρ_{0,i}, Λ_i)` d'éon en éon. Ce chaînon couple le noyau κ à la récurrence
> `(m,λ)` de l'atlas D1 (`verif_D1_atlas.py`) et tranche.
>
> **Verdict (ordre dominant, établi ; sceau `verif_D3_interaeon_convergence.py` v2).** Penrose
> suppose **Λ constante** d'éon en éon. L'atlas D1 a montré que la condition de Penrose
> (`λ̂=λ`) n'est self-cohérente **qu'au point fixe** `mλ=9k²/4` ; hors de lui, `λ` (donc Λ)
> **s'emballe** — vers `∞` (`mλ>2.25`) ou vers `0` (`mλ<2.25`) — ce qui contredit Penrose des
> deux côtés. Donc **Λ constante FORCE `ρ_0` éon-indépendante** (point fixe) ⟹ **κ constant**
> (`<1`, robuste à la normalisation) ⟹ **`∏κ_n = κⁿ → 0`** : **ISOTROPISATION TOTALE dynamique
> multi-éon** (forme d'issue forte *dynamique*), **lente** car `κ→1` pour un bang radiation-dominé
> réaliste. **Les deux branches runaway** (Penrose-exclues) sont en outre **sans résiduel dans le
> domaine GO** : `mλ>2.25` garde `κ_n<1` (≈0.82) et `∏κ_n` décroît jusqu'à la rupture GO à
> l'**éon 24** (radiation épuisée ⟹ **P6** au-delà) ; `mλ<2.25` **reste dans GO** et `κ_n`
> **sature à ≈0.795<1** (l'intuition `Λ/ρ_0→0 ⟹ κ→1` est *fausse*), donc `∏κ_n→0` aussi.
> **Aucun indice de résiduel dans le domaine de validité, des deux côtés.**
> `[ordre dominant ; identification (m,λ)↦(ρ_0,Λ) au premier ordre ; complétude hors-GO = P6]`.
>
> **⚠ Conditionnalité révélée par P6 (B) `[v0.3 — LC-D3-INTERAEON-P6 v0.2]`.** La dérivation
> ci-dessous part de la carte `ε_{n+1}=κ ε_n` du noyau **radiation-era**, laquelle **présuppose
> `σ(0)=0`** (CI de Tod) à l'entrée de chaque éon. P6 (B) (oracle de Gauss-Kuzmin) a montré que
> le bang **générique** (`Ω_σ→1`) **ne préserve pas** `σ(0)=0` : il ne contracte **jamais**
> (`P(ε_out<κ·ε_in)=0`), la carte y est **additive/bang-set** (`ε_{n+1}≈|\mathbf b_n−\mathbf w_n|`,
> `|\mathbf b_n|∼O(1)`), non multiplicative. **Donc `∏κ_n→0` est `établi CONDITIONNELLEMENT à
> `σ(0)=0`/WCH (A4)`**, et **non** un mécanisme dynamique libre. La CCC n'est pas réfutée — la WCH
> postule précisément le bang non-générique — mais l'isotropisation inter-éon **requiert** A3/A4
> au lieu de les dériver. **« Le bang gagne » ; A3/A4 = socles irréductibles.**

---

## 0. Rôle et garde-fou

Ce chaînon **clôt le front (a)** à l'ordre dominant. **Garde-fou `[à ne pas perdre]`** :
« totale » signifie **`∏κ_n→0` (attraction dynamique multi-éon)**, **PAS** une dérivation d'A3
à éon fini ni une suppression de l'issue faible single-crossover (`LC-D3-CROSSOVER-EINSTEIN3D`
reste valide). L'identification `(m,λ)↦(ρ_0,Λ)` est **d'ordre dominant** (ρ_0∝m, Λ∝λ ; κ dépend
surtout du rapport). La complétude **hors régime GO** (runaway profond, `ρ_0→0`) exige **P6**.
**Et surtout `[v0.3]`** : tout ce qui suit présuppose `σ(0)=0` à chaque entrée d'éon ; P6 (B)
(`LC-D3-INTERAEON-P6` v0.2) ayant établi que le bang **générique** ne préserve pas cette CI, la
clôture est **conditionnelle à `σ(0)=0`/WCH**, jamais inconditionnelle. Discipline d'audit
(`LC-AUDIT-VERDICT` §6.4) maintenue.

---

## 1. Le dispositif `[établi — algèbre]`

- **κ(ρ_0,Λ)** : noyau Bianchi IX + radiation + Λ (ordre dominant, `verif_D3_interaeon_kappa.py`),
  réimplémenté en minimal. `κ` = pente de `ε_{n+1}=κ ε_n`.
- **Suite (m,λ)** : récurrence NewClass de l'atlas D1 (`verif_D1_atlas.py`, eq. 14) :
  `λ_{i+1}=4λ_i²m_i/(9k²)`, `m_{i+1}=9k²/(4λ_i)`, **invariant `mλ`**. Point fixe `mλ=9k²/4=2.25`
  (Tod=NewClass=Nurowski) ; runaway sinon (`m→0, λ→∞`).
- **Identification (ordre dominant)** : `ρ_0∝m`, `Λ∝λ` ; référence éon 0 en régime GO
  (`ρ_0=100, Λ=1` ⟹ `κ≈0.81`). Robustesse à la normalisation testée (§3).

---

## 2. Le résultat : ∏κ_n → 0 au point fixe `[établi]`

**(1) Point fixe Penrose (`mλ=2.25`)** : `(ρ_0,Λ)=(100,1)` constants ⟹ `κ=0.816` **constant** ⟹

$$\boxed{\ \prod_{i<n}\kappa_i = \kappa^n \to 0\quad(\kappa\approx0.81<1)\ \Rightarrow\ \varepsilon_n\to 0\ :\ \textbf{isotropisation TOTALE}.\ }$$

Exemple : après 7 éons, `ε_7/ε_0 = 0.24`. **Robuste** (§3) : `κ<1` pour toute normalisation
GO-admissible (`κ∈[0.70,0.94]`).

**(2) Les deux branches runaway (Λ non constante — exclues par Penrose).** L'invariant `mλ`
fixe `ρ_0Λ=const=100` ; selon `mλ≷2.25`, l'emballement va dans deux sens opposés. **Aucun ne
produit de résiduel dans le domaine GO** :

- **(2a) `mλ=2.40>2.25` : `ρ_0→0, Λ→∞`.** `κ_n` reste `<1` (≈0.82, lentement croissant) et
  `∏κ_n` décroît **monotone**. La GO (ère radiation `ρ_0>5Λ`) **tient jusqu'à l'éon 23** (et non
  ~8 comme estimé en v0.1) ; **rupture à l'éon 24** (`ρ_0` 100→21, seuil `ρ_0<√500≈22.4`), avec
  `∏κ_n=0.014` déjà atteint (~70× de contraction). Au-delà, radiation épuisée ⟹ hors noyau
  d'ordre dominant ⟹ **P6**.
- **(2b) `mλ=1.00<2.25` : `ρ_0→∞, Λ→0`** `[ajout v0.2]`. La GO **tient indéfiniment** (`Λ` reste
  au-dessus du seuil `9/64ρ_0` car `ρ_0` monte plus vite). Ici `Λ/ρ_0→0` mais **`κ_n` ne tend
  PAS vers 1** : il **sature à ≈0.795<1** (stable en `Nmax`, forme gelée `Σ→1e-50`, §3-bis).
  Donc `1−κ_n≈0.205` quasi-constant, `Σ(1−κ_n)` **diverge**, et `∏κ_n→0` : **isotropisation
  totale là aussi**. L'intuition « `Λ/ρ_0→0 ⟹ κ→1 ⟹ résiduel » est **réfutée numériquement**.

| | point fixe (physique) | runaway `mλ>2.25` | runaway `mλ<2.25` `[v0.2]` |
|---|---|---|---|
| (ρ_0,Λ) | constants | ρ_0→0, Λ→∞ | ρ_0→∞, Λ→0 |
| κ_n | constant ≈0.816 | <1 (≈0.82, croît) | **sature ≈0.795<1** |
| domaine GO | indéfini | jusqu'à **éon 24** | indéfini |
| ∏κ_n | κⁿ → **0** | → 0.014 puis P6 | → **0** |
| verdict | **TOTALE** | pas de résiduel (puis P6) | pas de résiduel |

---

## 3. Pourquoi le point fixe est le scénario physique `[établi — via atlas D1]`

Penrose pose **Λ constante** (c'est LA constante cosmologique). L'atlas D1
(`LC-A-D1-FACTEUR-CONFORME` §4-bis, `verif_D1_atlas.py` [D1.runaway]) a établi que la
prescription self-cohérente avec `λ̂=λ` **n'existe qu'au point fixe** `mλ=9k²/4` ; toute
perturbation déclenche un runaway — `λ→∞` (si `mλ>2.25`) ou `λ→0` (si `mλ<2.25`), dans les
deux cas **Λ non constante**. **Donc imposer Λ=const force le point fixe**, où `(ρ_0,Λ)` — donc
`κ` — sont éon-indépendants. La question « `ρ_0` éon-indépendante ? » (subtilité §5.2 de
`LC-D3-INTERAEON-KAPPA`) reçoit ainsi un **oui conditionnel à l'hypothèse de Penrose**.

---

## 3-bis. La saturation de κ dans la branche `Λ→0` `[établi numériquement — sceau v2 §4]`

Le point délicat de la branche `mλ<2.25` est qu'on y a `Λ` minuscule : `𝓘` (de Sitter) n'est
atteint qu'après beaucoup d'e-folds, et on pourrait craindre que la « contraction » mesurée soit
un artefact de troncature (`Nmax` trop court, forme pas encore gelée). **Sceau** : `κ` est
identique à **5 décimales** entre `Nmax=25, 40, 60`, avec `Σ=σ/θ→1e-50` (forme **parfaitement
gelée**). La saturation `κ≈0.795<1` est donc **réelle**. Mécanisme : même quand la radiation
domine arbitrairement (`Λ/ρ_0→0`), la courbure positive de S³ (`³R>0`) continue de contracter
la forme d'une fraction `1−κ≈0.20` par éon ; ce n'est pas la *durée* de l'ère radiation qui fixe
`κ`, mais le travail intégré de `³S` pendant le gel. D'où `Σ(1−κ_n)` divergent et `∏κ_n→0`.

---

## 4. Verdict épistémique — la porte (ii) franchie `[établi / renvoi P6]`

- **La porte (ii)**, sous sa seule forme licite (carte inter-éon, `LC-D3-INTERAEON-KAPPA`), est
  **franchie comme attraction TOTALE dynamique** : sous Penrose, `∏κ_n→0`.
- **Mais ce n'est pas l'issue forte single-crossover** : pas d'entraînement d'A3 à éon fini ;
  l'attraction est multi-éon et **lente** (`κ→1` pour bang réaliste).
- **Les régimes runaway sont doublement écartés** : (i) exclus par Penrose (`Λ` non constante,
  vers `∞` ou vers `0`) ; (ii) **et sans résiduel de toute façon** dans le domaine GO — la
  branche `Λ→∞` y décroît jusqu'à `∏κ=0.014` avant de sortir (puis P6), la branche `Λ→0` y reste
  et `κ` sature `<1` (`∏κ_n→0`). Le seul renvoi à P6 concerne le *sort ultime hors-GO* de la
  branche `Λ→∞`, pas un résiduel.

$$\boxed{\ \text{Sous Penrose (Λ const) ET } \sigma(0)=0\text{ à chaque éon : } \varepsilon_n=\kappa^n\varepsilon_0\to 0,\ \kappa<1.\ \text{A3 ATTEINTE multi-éon (lent) — mais } \sigma(0)=0 \text{ N'est PAS générique (P6 B).}\ }$$

**Mise à jour `LC-D3-INTERAEON-KAPPA` §5** : la convergence `∏κ_n` passe de `décision ouverte`
à **`établi (ordre dominant) : ∏κ_n→0 au point fixe Penrose ⟹ isotropisation totale dynamique ;
les deux branches runaway sans résiduel dans GO (l'une → P6 hors-GO, l'autre κ saturé <1)`**.

---

## 5. Réserves `[à inventer / établi lent]`
- **P6 TRANCHÉ `[v0.3 — LC-D3-INTERAEON-P6 v0.2]`.** Le passage à travers le bang a été traité :
  (A) quiescent en radiation-era ; (B) deep-bang générique par l'oracle de Gauss-Kuzmin. Verdict :
  le bang générique **ne contracte jamais** ⟹ `∏κ_n→0` ci-dessous est **conditionné à
  `σ(0)=0`/WCH**, non un mécanisme libre. La clôture du front (a) est donc **conditionnelle à
  A3/A4**. (Le sort hors-GO de la branche `Λ→∞` au-delà de l'éon 24 reste un détail de complétude,
  sans incidence sur ce verdict.)
- **WCH = contenu dynamique (pas un postulat nu) `[LC-D3-WCH-GWE v0.3]`.** La conditionnalité
  « `σ(0)=0`/WCH » ci-dessus n'est pas un postulat nu au crossover **réel** : la GWE
  (Meissner-Penrose) **délivre** `Ω_σ=(kη)⁴ε²/27` (sceau `verif_D3_WCH_GWE.py`) ; le mode régulier
  **exact** est en **régime (A) ∀ `kη`** (plafond `Ω_σ/ε²=0.377<0.5` ; au pic CGB `~6·10⁻²⁹`). Donc
  `∏κ_n→0` n'est plus un pur artefact de `σ(0)=0` : l'exclusion du mode `Y` + la dispersion
  super-horizon le **délivrent** au crossover GWE **à l'ordre dominant**
  — **conditionnellement à C7** (rétro-action inhomogène, hors de portée ; l'ancienne « bascule (B)
  à `kη_*~1.9` » était un artefact de la troncature leading, audit C5 — le spectre M-P n'est plus le
  verrou). Le verdict (B) du bang **générique** (P6) reste intact ; les deux
  coexistent (bang générique → (B), crossover GWE → (A) si C7 tient).
- **κ→1 (lent)** pour bang radiation-dominé réaliste : l'isotropisation totale (sous σ(0)=0) est
  **lente** (`1−κ ∝ ρ_0^{−p}`). `[établi lent]`
- **Identification `(m,λ)↦(ρ_0,Λ)`** d'ordre dominant (atlas FLRW ↦ noyau Bianchi IX) :
  qualitativement robuste (point fixe ⟹ constant ; runaway ⟹ dérive), quantitativement à
  raffiner avec la vraie prescription (Markwell-Stevens, Nurowski 2101.12670).

---

## 6. Format de chaînon standard
- **Zone ambiguë.** « κ<1 contracte par éon, mais `∏κ_n` converge-t-il vers 0 (totale) ou const>0 (résiduelle) ? »
- **Hypothèse testée.** La suite `(ρ_0,Λ)` (donc `κ_n`) rend `∏κ_n→0`.
- **Outil.** Noyau κ (ordre dominant) ⊗ récurrence `(m,λ)` de l'atlas D1 ; identification ρ_0∝m, Λ∝λ. Sceau `verif_D3_interaeon_convergence.py`.
- **Critère de réfutation.** Si `∏κ_n→const>0` (résiduel) dans le régime valide. — **Non réalisé** : `∏κ_n→0` au point fixe (mandaté par Penrose), robuste ; et **aucune** des deux branches runaway ne montre de plateau résiduel dans GO (l'une décroît jusqu'à 0.014 puis sort, l'autre sature `κ<1`).
- **Verdict.** **∏κ_n→0 : isotropisation TOTALE dynamique** (ordre dominant, sous Penrose) ; runaway des deux côtés sans résiduel (branche `Λ→∞` → P6 hors-GO). `[établi (ordre dominant) ; complétude P6]`

---

## 7. Renvois, glossaire, références

**Renvois.** **Met à jour `LC-D3-INTERAEON-KAPPA` §5** ; `LC-D3-INTERAEON-MATIERE` (P7, σ̌ ne
renverse pas κ) ; `LC-A-D1-FACTEUR-CONFORME` §4-bis (atlas (m,λ), point fixe/runaway) ;
`LC-D3-CROSSOVER-EINSTEIN3D` §4 (frontière, ici close côté porte ii) ; `LC-AUDIT-VERDICT`.
Chantier restant : **P6** (`LC-WORK-REPRISE-CLOTURE-A` §5.2).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *∏κ_n (convergence inter-éon)* : produit des taux d'isotropisation ; `→0` (totale) au point
  fixe Penrose ; **jamais `→const>0` (résiduel)** dans le domaine GO, ni au point fixe ni dans
  l'une ou l'autre branche runaway (toutes deux Penrose-exclues).
- *Point fixe de l'atlas D1 (`mλ=9k²/4`)* : seul régime où Λ=const est self-cohérent ⟹ ρ_0
  éon-indépendante ⟹ κ constant.

**Références (`LC-04`).**
- **Markwell & Stevens**, arXiv:2212.06914 (sélection du facteur conforme, point fixe).
- **P. Nurowski**, arXiv:2102.11823, **2101.12670** (carte matière éon→éon par réciprocité).
- **K. P. Tod**, arXiv:1309.7248 ; **Wainwright & Ellis** (1997).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte` (cf. `LC-00-INDEX`).
*Discipline d'audit : `établi` = l'algèbre (κ<1 robuste, ∏κ_n→0 au point fixe), à l'ordre
dominant ; jamais « la CCC isotropise ». La complétude hors-GO (P6) et la valeur de κ pour
bang réaliste restent ouvertes.*
