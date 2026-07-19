---
id: LC-WORK-CADRAGE-INTERAEON
titre: "Cadrage de faisabilité — propager â à travers l'éon futur jusqu'à son 𝓘 (la carte ε_n↦ε_{n+1}) : formalisable ou à inventer ?"
codename: LC-RACCORD
type: note de cadrage (autoportante) — décision GO/NO-GO avant engagement, PAS le calcul lui-même
version: 1.1
langue: fr
date: 2026-06-07
maj: "2026-06-07 — v1.1 : ajout de l'Addendum (§8) de VERROUILLAGE (sceau verif_D1_bianchiIX_domain.py) : (Q1) domaine de Λ pour atteindre 𝓘 vs recollapse — borne sûre Λ>9/(64ρ_r0), l'anisotropie est conservatrice ; (Q2) stiffness — non raide en temps e-fold (ratio 2), ~15-20 e-folds. GO chiffré. v1.0 : cadrage initial + démonstrateur."
portee: "Juge la faisabilité de l'UNIQUE frontière ouverte du front (a) après la porte (i) : l'isotropisation dynamique inter-éon (LC-D3-CROSSOVER-EINSTEIN3D §4). Décompose le calcul, classe chaque pièce (établi / formalisable / à inventer), s'appuie sur deux sceaux (verif_D3_interaeon_poc.py : structure de la carte ; verif_D1_bianchiIX_domain.py : verrouillage domaine+stiffness), et recommande un premier pas borné avec conditions GO chiffrées. Ne PRODUIT pas la carte κ physique."
prerequis_kb: [LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-D3-WCH-CANCELLATION, LC-AUDIT-VERDICT]
fichier_compagnon: [verif_D3_interaeon_poc.py, verif_D1_bianchiIX_domain.py]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# Cadrage — l'isotropisation inter-éon est-elle calculable ?

> **But.** Décider, *avant* de s'engager, si la frontière laissée ouverte par
> `LC-D3-CROSSOVER-EINSTEIN3D` §4 — *propager `â` à travers tout l'éon futur jusqu'à son
> propre 𝓘 pour obtenir la carte `ε_n ↦ ε_{n+1}`* — est `formalisable` (extension de
> machinerie connue) ou réellement `à inventer`. **Verdict : formalisable à l'ordre dominant
> (bornée, faisable maintenant), avec une seule pièce `à inventer` (la matière CCC exacte
> au-delà des deux ordres de Tod), probablement sous-dominante pour la question
> qualitative.** Recommandation : faire d'abord la carte d'ordre dominant.

---

## 1. La question, et pourquoi c'est la seule porte restante

Après la porte (i) : `LC-D3-CROSSOVER-ANISOTROPE` (issue faible) + `LC-D3-CROSSOVER-EINSTEIN3D`
(aucune régularité plus faible que A3 ne force l'isotropie d'**un** crossover), il reste
**une** route vers une isotropisation non postulée : **dynamique et inter-éon**.

> *La carte `ε_n ↦ ε_{n+1}` de l'anisotropie de 𝓘 d'éon en éon attire-t-elle vers `ε=0` ?*

C'est l'analogue anisotrope du runaway `(m,λ)` de l'atlas FLRW (`LC-A-D1-FACTEUR-CONFORME`
§4-bis) et la **seule forme licite restante de la porte (ii)** — l'ancienne porte (ii)
(« renforcer le point fixe `g₃=0` ») étant caduque, le point fixe n'existant pas hors
isotropie. Si `|κ| < 1` (carte contractante), l'isotropisation inter-éon **restaurerait
dynamiquement** une forme d'issue forte ; si `|κ| ≥ 1`, l'anisotropie persiste ou s'emballe.

---

## 2. La subtilité qui définit le calcul `[à ne pas perdre]`

On pourrait croire que `ǧ = Ω̂⁻⁴ĝ` (Tod éq. 3) donne le futur éon « gratuitement » par
rescaling du passé. **Faux pour ce qu'on veut.** Cette relation ne couvre que la **région de
bandage** près du crossover : elle envoie le 𝓘 du passé sur le **bang** du futur. Le **𝓘 du
futur éon** est une surface *différente*, dans le futur lointain du nouvel éon — il n'est
conforme à *rien* dans le passé. Le futur éon, une fois « né » au bang avec les données de
Tod, **évolue sous ses propres équations d'Einstein** jusqu'à son 𝓘. **C'est cette évolution
— bang → 𝓘 du futur éon — qui est la pièce manquante.** Tod ne la donne qu'aux **deux
premiers ordres** près du bang (`O(Ť⁻²)`, `O(Ť⁻¹)`, éq. 27, 31-33).

---

## 3. Décomposition et registre de faisabilité

| Pièce | Contenu | Source / outil | Registre |
|---|---|---|---|
| **P1** Données de bang | `ǎ_ij = 2Hφ₁²â_ij` (éq.28), matière = radiation + `σ̌(ε_n)` + champ φ + DM | **Tod §6-7** (explicite) | `établi` (transcrire) |
| **P2** ODE d'évolution | Einstein de Bianchi A (R,α,β,γ)(t) : expansion-cisaillement-courbure | **Wainwright-Ellis** ; Tod éq.20 | `formalisable` (standard) |
| **P3** Isotropisation tardive | radiation→Λ→𝓘 ; `Σ=σ/θ→0` (no-hair) ; gel de l'anisotropie | **Wald 1983** + ODE | `formalisable` (démontré, §4) |
| **P4** Lecture de `ε_{n+1}` | rapports de facteurs d'échelle gelés à 𝓘 → anisotropie de `ǎ'_ij` | limite `t→∞` des ODE | `formalisable` (mécanique) |
| **P5** Couplage de courbure | terme de structure `n_i` (Bianchi IX) ; `σ̌` ~ Ricci sans-trace | Tod éq.20-22 + ODE | `formalisable` (plus lourd) |
| **P6** Dynamique de bang | rebonds/Mixmaster de Bianchi IX près de la singularité | littérature Mixmaster | `formalisable` mais **lourd/chaotique** |
| **P7** Matière CCC exacte | `σ̌`, phantom φ, « DM » de Penrose **au-delà** de `O(Ť⁻¹)` | — (Tod s'arrête ; M-S : « no physical interpretation ») | **`à inventer`** |

**Lecture.** Six pièces sur sept (P1-P6) sont `établi`/`formalisable` : la **structure** du
calcul est une **extension de Wainwright-Ellis (ODE de Bianchi) branchée sur les données de
bang de Tod**. Une seule pièce (P7) est `à inventer` — mais elle est **sous-dominante**
(`σ̌ = O(Ť⁻¹)` contre la radiation `O(Ť⁻²)` qui domine près du bang ; et le champ φ est
fixé par la prescription de Tod), donc à l'**ordre dominant on peut s'en passer** pour la
question qualitative « `κ ⋚ 1` ? ».

---

## 4. Ce que le démonstrateur établit `[établi — verif_D3_interaeon_poc.py]`

Démonstrateur en **champ-test** (cisaillement sur fond FRW radiation+Λ, sans back-réaction
ni courbure) — il ne donne PAS le `κ` physique, il **prouve que la structure tient** :

- **(1)-(2)** Les ODE s'intègrent ; `Σ = σ/θ : 0.061 → 5·10⁻⁴¹` à 𝓘 : **isotropisation
  cinétique** confirmée (Wald). P2-P3 marchent.
- **(3)** L'anisotropie **gelée** `Δβ_i = ∫σ_i dt` **converge** (dérive de queue `3·10⁻¹⁵`)
  vers un nombre fini : `ε_{n+1}` est **bien défini et extractible**. P4 marche.
- **(bonus)** La carte `ε_n ↦ ε_{n+1}` est **linéaire** à petit `ε`, de pente
  `κ ≈ 0.35` *à ce niveau* (champ-test, sans courbure). **Valeur non physique** (ignore
  P5-P7), mais elle prouve que **`κ` est une quantité accessible** et donne le **gabarit**
  de la réponse : une pente lue sur une carte linéaire.

**Conclusion du démonstrateur.** La carte existe, converge, est linéaire, et `κ` se lit.
La seule chose qui sépare ce `κ`-jouet du `κ`-physique, c'est P5 (courbure IX), P6 (bang) et
P7 (matière exacte) — dont deux sont `formalisable`.

---

## 5. Verdict de faisabilité

$$\boxed{\ \text{Carte } \varepsilon_n\!\mapsto\!\varepsilon_{n+1}\ :\ \textbf{formalisable à l'ordre dominant}\ (\text{P1-P6}),\ \text{une pièce } \textbf{à inventer}\ (\text{P7, sous-dominante}).\ }$$

- **Ce n'est PAS `à inventer` en bloc.** Le cœur est une extension d'une machinerie
  **standard** (ODE de Bianchi IX, Wainwright-Ellis) branchée sur des **données explicites**
  (bang de Tod). Le démonstrateur le confirme : structure intégrable, `κ` extractible.
- **Le coût réel est P5+P6.** La courbure de Bianchi IX (P5) est routine ; la dynamique de
  bang (P6, Mixmaster) est lourde et potentiellement chaotique — c'est le **vrai poste de
  difficulté**, pas une impossibilité. On peut le **contourner** en partant l'intégration
  *dans l'ère de radiation* (après le bang), ce qui isole la question de l'isotropisation
  tardive sans affronter le Mixmaster — un **premier pas borné et honnête**.
- **P7 est le seul `à inventer`**, mais sous-dominant : la carte d'ordre dominant (P1-P6 sans
  la matière CCC exacte) **suffit à trancher qualitativement** `κ ⋚ 1`. P7 ne serait requis
  que pour la valeur *précise* de `κ`.

---

## 6. Premier pas recommandé (borné)

1. Écrire les ODE de **Bianchi IX + radiation + Λ** (P2+P5) en variables expansion-
   normalisées (Wainwright-Ellis), facteurs d'échelle `A_i(t)`, terme de courbure `n_i=1`.
2. **Démarrer dans l'ère de radiation** (éviter P6/Mixmaster au premier tour), avec une
   anisotropie initiale `ε_n` reliée à `â` par les données de bang de Tod (P1).
3. Intégrer jusqu'à Λ-domination ; lire l'anisotropie gelée de 𝓘 → `ε_{n+1}` (P4).
4. Balayer `ε_n` → extraire `κ`. **Trancher** : `|κ|<1` (isotropisation, issue forte
   dynamique) / `|κ|≥1` (anisotropie persistante).
5. Consigner en chaînon `LC-D3-INTERAEON-KAPPA` (ou `-ISOTROPISATION`), tag `formalisable`,
   avec la réserve P6 (bang non traité) + P7 (matière exacte) explicitement portée.

**Effort estimé.** Un sceau de la taille de `verif_D1_bianchiA.py`, plus une intégration
numérique soignée. **Borné.** Le risque n'était pas l'impossibilité mais la **stiffness/chaos**
près du bang — désormais **verrouillé et contourné** (cf. Addendum §8 : domaine de Λ sûr,
système non raide en temps e-fold, démarrage en ère de radiation).

---

## 7. Renvois

`LC-D3-CROSSOVER-EINSTEIN3D` §4 (la frontière) ; `LC-D3-CROSSOVER-ANISOTROPE` §5 (porte (ii)
caduque, sa seule forme licite = cette carte) ; `LC-A-D1-FACTEUR-CONFORME` §4-bis (runaway
`(m,λ)` — l'analogue isotrope) ; `LC-A-D1-BIANCHI` (données de bang, Tod) ;
`LC-AUDIT-VERDICT` §8 (suite recommandée). Réfs nouvelles : **Wald**, *Phys. Rev. D* **28**,
2118 (1983) ; **Wainwright & Ellis**, *Dynamical Systems in Cosmology*, CUP (1997).

---

## 8. Addendum — verrouillage : domaine de Λ et stiffness `[établi — verif_D1_bianchiIX_domain.py]`

*Avant de lancer le premier pas (§6), on a verrouillé les deux risques qui pouvaient le
faire échouer : (Q1) le modèle atteint-il un 𝓘, ou recollapse-t-il ? (Q2) le système est-il
trop raide ? Méthode : contrainte hamiltonienne `3H² = ρ_r + Λ + σ² − ½·³R` (vérifiée sur
Kasner : `3H²=σ²`) et linéarisation au point fixe de Sitter — sans évolution complète.*

### 8.1 (Q1) Domaine de Λ — 𝓘 vs recollapse `[établi]`

Bianchi IX a une courbure positive (`³R>0`, topologie S³) : Wald (1983) exclut IX de son
no-hair *garanti* — il recollapse si Λ est trop petit. Le scalaire de Ricci 3D,
`³R = κ(ε)/a²` avec `κ(ε) = 2\cosh 2ε − \cosh 4ε + ½ = 3/2 − 4ε² + …`, est **maximal à
l'isotropie** (le rond) et **décroît avec l'anisotropie**. Le seuil de recollapse (point de
retournement `3H²=0`) a une forme close :

$$\Lambda_{\text{crit}}(\varepsilon) = \frac{\kappa(\varepsilon)^2}{16\,\rho_{r0}},\qquad
\Lambda_{\text{crit}}(0)\ [\text{rond}] = \frac{9}{64\,\rho_{r0}}.$$

(Vérif numérique, `ρ_r0=1` : recollapse à `Λ=0.10`, atteint 𝓘 à `Λ=0.18`, seuil `≈0.1406=9/64`.)
**L'anisotropie abaisse le seuil** (`Λ_crit(ε)/Λ_crit(0) = 1 − 16ε²/3 + …`) : `³R` réduit +
énergie de cisaillement `σ²>0` aident l'expansion. Démonstration (shape figé) : à
`Λ=0.0815` (entre les deux seuils), le rond recollapse (`min 3H²=−0.059`), l'anisotrope
`ε=0.4` atteint 𝓘 (`+0.059`). Donc le rond est le **pire cas**, d'où la **borne sûre** :

$$\boxed{\ \Lambda > \tfrac{9}{64\,\rho_{r0}}\ [\text{rond, conservateur}]\ \Rightarrow\ \text{𝓘 garanti, même anisotrope.}\ }$$

(`ρ_r0` et l'échelle de courbure sont fixés par les données de bang de Tod / la
normalisation Yamabe de `â`.)

### 8.2 (Q2) Stiffness `[établi]`

- **Temps cosmique : mal conditionné.** Plage dynamique `a ~ e^N` (radiation `H∝a⁻²` ⟹
  condition `~ a² ~ 10³⁺`).
- **Temps e-fold `N=ln a` (variables expansion-normalisées, Wainwright-Ellis) : NON raide.**
  Au point fixe de Sitter, les taux de décroissance sont `{−2` (courbure)`, −3` (cisaillement)`, −4` (radiation)`}`,
  ratio de raideur `|λ_max|/|λ_min| = 2` — autonome et borné.
- **Coût : `~15-20` e-folds** suffisent à geler l'anisotropie (`Σ=σ/θ` de `ε` à `<10⁻⁶` :
  `N≈(1/3)ln(ε/10⁻⁶)`). La seule raideur extrême serait la dynamique de bang (Mixmaster, P6),
  **exclue au premier tour** par le démarrage en ère de radiation.

### 8.3 Conditions GO chiffrées `[verrouillé]`

| paramètre | condition verrouillée |
|---|---|
| **Λ** | `> 9/(64 ρ_r0)` (borne ronde, conservatrice) → 𝓘 garanti |
| **départ** | dans l'ère de radiation (contourne Mixmaster/P6) |
| **variable de temps** | `N = ln a` (expansion-normalisé) → non raide (ratio 2) |
| **solveur** | RK45/DOP853 explicite ; Radau (implicite) en secours si on approche le bang |
| **durée** | `~15-20` e-folds (coût faible) |

**Effet sur le §6.** Le seul risque qui y était nommé (« stiffness/chaos près du bang ») est
désormais **borné et contourné** : le premier pas est sûr. Le risque résiduel n'est plus la
faisabilité mais la **précision** de la valeur de `κ` (qui dépend de P7, sous-dominant).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
