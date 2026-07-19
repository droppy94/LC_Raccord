---
id: LC-D3-CROSSOVER-STABILITE
titre: "Module D / crossover (a3) — stabilité du point fixe g₃=0 : WCH (D3) et stabilité inter-éons (#5) coïncident"
codename: LC-RACCORD
tags: [module-D, D3, crossover, stabilite, runaway, atlas, point-fixe, weyl, WCH, candidat-5, D1, convergence, capstone]
type: chaînon (front (a) du raccord, étape a3 ; capstone : verdict du front (a))
statut: sélection P=9k²/4 par WCH = point fixe #5 établi (FLRW) / attracteur dynamique (back-réaction drive-t-elle P ?) décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (index, programme [D]/crossover, glossaire, refs)
fichier_compagnon: verif_D3_crossover_stabilite.py
renvois: [LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-BACKREACTION, LC-D3-WEYL-BUNCHDAVIES, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-E-PLANCK-RESIDUEL, LC-D-HOLOGRAPHIE-G3, LC-WORK-REPRISE-RACCORD, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D3] WCH (C→0 / marée bornée) — ici testée à travers l'itération inter-éons"
  - "[A]/D1 candidat #5 (stabilité) — montré IDENTIQUE à WCH sur la sélection P=9k²/4"
  - "[E] — la back-réaction (~λ²) qui pourrait driver P passe par la coupure N holographique"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·CROSSOVER (a3) — Stabilité : WCH et candidat #5 coïncident

> **Cible (capstone du front (a)).** (a1) a montré que la carte de crossover est homogène
> (`ǧ₍₃₎=M·ĝ₍₃₎`, point fixe à `0`), le facteur `M` étant fixé par le fond via `c₁` ;
> (a2) a montré que la back-réaction des fluctuations de Bunch–Davies est **isotrope** —
> elle ne touche pas la marée, elle **renormalise le fond `(m,λ)`**, donc alimente
> l'itération inter-éons de l'atlas (`LC-A-D1` §4-bis). Reste la question : *le point
> fixe `g₍₃₎=0` est-il **stable** sous cette itération, ou le runaway `(m,λ)`
> amplifie-t-il la marée ?*
>
> **Verdict (calculé, `verif_D3_crossover_stabilite.py`).** La récurrence de l'atlas
> **conserve le produit `P≡mλ`** et fait courir `λ` géométriquement de raison `r=P/P*`,
> `P*=9k²/4`. Or l'amplitude physique de marée scale comme `P_T ∝ H² = λ/3`. Donc le
> runaway **est** une (dé)stabilisation de la marée :
> `P>P* ⟹ λ→∞ ⟹` Weyl explose (WCH violée) ; `P<P* ⟹ λ→0` (sur-suppression) ;
> `P=P* ⟹` marée bornée et stable. **Exiger une marée gravitationnelle bornée à chaque
> Big Bang — c'est-à-dire l'hypothèse de Weyl de Penrose (D3) — exclut la branche `P>P*`
> et sélectionne `P=P*=9k²/4`**, qui est *exactement* le point fixe du candidat #5
> (stabilité inter-éons). Le Jacobien y a une **valeur propre `1` double, défective**
> (non-hyperbolique) — la signature même du candidat #5 (`LC-A-D1-STABILITE-WEYL`).
> **D3/WCH (la marée, ★) et le candidat #5 (le fond) coïncident sur une seule
> condition.** `[établi, FLRW]`
>
> **Portée honnête.** C'est une **sélection**, pas un attracteur : `P` étant conservé,
> rien ne *drive* vers `P*` si l'on démarre ailleurs — le fine-tuning `m̂λ̂=9k²/4`
> **subsiste**, désormais unifié et physiquement motivé (« faible Weyl = marée bornée =
> stabilité »). La question d'un *attracteur dynamique* — la back-réaction (a2), qui
> renormalise `λ~H⁴~λ²`, peut-elle driver `P` vers `P*` ? — reste `décision ouverte / à
> inventer` (elle requiert la coupure holographique `N` de `LC-E`).

---

## 0. Rôle et garde-fou

Ce chaînon **clôt le front (a)** en testant la stabilité inter-éons, et **unifie** deux
candidats-sélecteurs jusque-là séparés (★ BD/marée et #5 stabilité/fond). Ce qui est
`établi` (FLRW) : la coïncidence `WCH ⟺ #5` sur `P=9k²/4`, et la nature non-hyperbolique
du point fixe. Ce qui reste `décision ouverte / à inventer` : que la sélection devienne un
*attracteur* (mécanisme dynamique via back-réaction + `N`), et le cas inhomogène. On ne
surclasse pas : **« WCH sélectionne #5 » n'est pas « la dynamique impose #5 »** — le
fine-tuning demeure, mais il a maintenant *une* justification (au lieu de deux conditions
indépendantes posées à la main).

---

## 1. La récurrence de l'atlas conserve `P=mλ` `[établi]`

Sceau [1]. Classe Penrose-cohérente (`LC-A-D1` §4-bis) :

$$m' = \frac{9k^2}{4\lambda},\qquad \lambda' = \frac{4\lambda^2 m}{9k^2}
\qquad\Longrightarrow\qquad m'\lambda' = m\lambda \equiv P\ \ (\text{conservé}).$$

Le produit `P` est une **invariante** du map : on ne change jamais de level-set. `[établi]`

---

## 2. Réduction 1D : `λ' = (P/P*)\,λ`, ligne de points fixes en `P*` `[établi]`

Sceau [2]. Sur une level-set (`m=P/λ`), la récurrence se réduit à une **dilatation
linéaire** :

$$\lambda' = \frac{4P}{9k^2}\,\lambda = \frac{P}{P^\*}\,\lambda,\qquad P^\* = \frac{9k^2}{4}.$$

`P=P*` ⟹ `r=1` : **toute la level-set critique est une ligne de points fixes**. `P>P*` ⟹
`λ→∞` ; `P<P*` ⟹ `λ→0`. La raison `r=P/P*` mesure exactement l'écart au critique. (Check :
`P=2.40, k=1` ⟹ `r=1.0667`, `m` décroît de `0.9375/éon` — le chiffre du sceau
`verif_D1_atlas`.) `[établi]`

---

## 3. Le point fixe est non-hyperbolique = candidat #5 `[établi]`

Sceau [3]. Jacobien du map 2D au point fixe (`mλ=9k²/4`) :

$$J\big|_{\text{fp}} = \begin{pmatrix} 0 & -\tfrac{9k^2}{4\lambda^2}\\[4pt]
\tfrac{4\lambda^2}{9k^2} & 2\end{pmatrix},\quad \det J = 1,\ \operatorname{tr}J = 2
\ \Longrightarrow\ (\mu-1)^2 = 0:\ \mu = 1\ \text{double}.$$

`rang(J−𝟙)=1` ⟹ **défective** (bloc de Jordan) ⟹ drift **séculaire** (polynomial) des
perturbations. C'est *mot pour mot* la carte non-hyperbolique « vp 1 double » trouvée pour
le candidat #5 dans `LC-A-D1-STABILITE-WEYL` : (a3) **reconnecte** la stabilité inter-éons
à l'itération de l'atlas, et confirme qu'il s'agit du même objet. `[établi]`

---

## 4. La marée suit `λ` : le runaway est une (dé)stabilisation de Weyl `[établi (scaling)]`

Sceau [4]. L'amplitude physique de la marée à chaque Big Bang est le spectre tensoriel de
l'éon Λ-dominé, `P_T ∝ H² = λ/3` (`H²=λ/3`). Sous l'itération `λ_i = λ_0\,(P/P^\*)^i` :

| branche | `λ` | marée `P_T ∝ λ` | WCH (faible Weyl) |
|---|---|---|---|
| `P > P^\*` | `→∞` | **explose** | **violée** |
| `P = P^\*` | const | **bornée, stable** | satisfaite (steady) |
| `P < P^\*` | `→0` | s'éteint | satisfaite (sur-supprimée) |

La 1-point `⟨g₍₃₎⟩=0` reste préservée (a1,a2) ; ce que (a3) suit, c'est la **2-points**
`⟨g₍₃₎g₍₃₎⟩~k³` — l'amplitude de fluctuation — à travers les éons. Le runaway `P>P*`
fait croître le Weyl sans borne : il **détruit** l'hypothèse de faible Weyl qui fonde tout
le traitement perturbatif. `[établi au niveau du scaling P_T∝λ ; normalisation précise
formalisable]`

---

## 5. La coïncidence : WCH (D3) ⟺ stabilité (#5) `[établi, FLRW]`

Exiger que la marée gravitationnelle reste **bornée et faible** à chaque Big Bang est
*précisément* l'hypothèse de courbure de Weyl de Penrose (D3). Le §4 montre que cette
exigence **exclut `P>P*`** et, pour une marée *non nulle et stable*, **impose `P=P*=9k²/4`**.
Or `P=9k²/4` est le point fixe du candidat #5. Donc :

$$\boxed{\ \text{WCH (D3 : faible Weyl, ★)}\ \Longleftrightarrow\ \text{stabilité inter-éons (#5)}\ \Longleftrightarrow\ P=\tfrac{9k^2}{4}.\ }$$

Les deux candidats-sélecteurs de D1 qui agissaient sur des secteurs *différents* (★ sur la
**marée** `g₍₃₎`, #5 sur le **fond** `(m,λ)`) sont **la même condition**. Sous WCH, la
sous-détermination de D1 est levée — un seul énoncé physique ferme les deux secteurs.

<svg width="100%" viewBox="0 0 680 360" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>(a3) WCH et candidat #5 coïncident : la marée bornée sélectionne P=9k²/4</title>
  <desc>Le produit P égal m lambda est conservé par la récurrence de l'atlas. Trois branches selon P comparé à P étoile égal neuf k carré sur quatre. Branche du haut, P supérieur à P étoile : lambda croît vers l'infini, la marée P_T proportionnelle à lambda explose, l'hypothèse de Weyl est violée. Branche du milieu, P égal P étoile : lambda constant, marée bornée et stable, c'est la ligne de points fixes, point fixe non hyperbolique avec valeur propre un double défective, identique au candidat cinq. Branche du bas, P inférieur à P étoile : lambda tend vers zéro, marée sur-supprimée. Conclusion encadrée : exiger une marée bornée, c'est-à-dire l'hypothèse de courbure de Weyl D3, sélectionne P égal P étoile, qui est le point fixe du candidat cinq ; donc WCH et stabilité coïncident et ferment ensemble la sous-détermination de D1. En bas, réserve : c'est une sélection et non un attracteur car P est conservé ; reste ouvert si la back-réaction a2 peut driver P vers P étoile via la coupure holographique N du module E.</desc>
  <rect x="40" y="36" width="430" height="44" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="255" y="54" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">P &gt; P*  :  λ→∞  ⟹  marée P_T∝λ EXPLOSE</text>
  <text x="255" y="72" text-anchor="middle" font-size="11" fill="#73726c">faible Weyl violé — WCH exclut cette branche</text>
  <rect x="40" y="92" width="430" height="58" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.9"/>
  <text x="255" y="112" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">P = P* = 9k²/4  :  λ const  ⟹  marée bornée, STABLE</text>
  <text x="255" y="130" text-anchor="middle" font-size="11" fill="#3d3d3a">ligne de points fixes ; Jacobien : vp 1 double, défective</text>
  <text x="255" y="146" text-anchor="middle" font-size="11" fill="#0F6E56">= candidat #5 (LC-A-D1-STABILITE-WEYL)</text>
  <rect x="40" y="162" width="430" height="44" rx="8" fill="#FBF3E7" stroke="#C98A2B" stroke-width="0.7"/>
  <text x="255" y="180" text-anchor="middle" font-size="12" font-weight="500" fill="#8A5A12">P &lt; P*  :  λ→0  ⟹  marée sur-supprimée</text>
  <text x="255" y="198" text-anchor="middle" font-size="11" fill="#73726c">faible Weyl OK mais structure éteinte</text>
  <rect x="490" y="36" width="150" height="170" rx="8" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.7"/>
  <text x="565" y="60" text-anchor="middle" font-size="11.5" font-weight="500" fill="#3C3489">P = mλ</text>
  <text x="565" y="78" text-anchor="middle" font-size="11.5" font-weight="500" fill="#3C3489">CONSERVÉ</text>
  <text x="565" y="104" text-anchor="middle" font-size="10.5" fill="#73726c">r = P/P*</text>
  <text x="565" y="130" text-anchor="middle" font-size="10.5" fill="#3d3d3a">on reste sur</text>
  <text x="565" y="146" text-anchor="middle" font-size="10.5" fill="#3d3d3a">sa level-set</text>
  <text x="565" y="172" text-anchor="middle" font-size="10.5" fill="#A32D2D">=&gt; sélection,</text>
  <text x="565" y="188" text-anchor="middle" font-size="10.5" fill="#A32D2D">pas attracteur</text>
  <rect x="40" y="220" width="600" height="50" rx="9" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.9"/>
  <text x="340" y="242" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">WCH (D3 : marée bornée)  ⟺  stabilité (#5)  ⟺  P = 9k²/4</text>
  <text x="340" y="260" text-anchor="middle" font-size="11" fill="#3d3d3a">les deux secteurs (marée g₃ et fond m,λ) fermés par un seul énoncé — D1 levé sous WCH</text>
  <rect x="40" y="282" width="600" height="62" rx="9" fill="#FBF3E7" stroke="#C98A2B" stroke-width="0.7"/>
  <text x="340" y="304" text-anchor="middle" font-size="12" font-weight="500" fill="#8A5A12">question ouverte (attracteur dynamique) :</text>
  <text x="340" y="324" text-anchor="middle" font-size="11.5" fill="#3d3d3a">la back-réaction (a2), ~λ², peut-elle DRIVER P vers P* ? -> via coupure holographique N (LC-E)</text>
</svg>

*Fig. — (a3). `P=mλ` conservé (violet) ⟹ trois branches selon `P` vs `P*=9k²/4`. La marée
`P_T∝λ` explose si `P>P*` (rouge), s'éteint si `P<P*` (ambre), reste stable si `P=P*`
(vert) — où le point fixe est non-hyperbolique (= candidat #5). WCH (marée bornée)
sélectionne donc `P=P*` : **D3 et #5 coïncident**. Reste ouvert (ambre) : un mécanisme
dynamique (back-réaction → `N`) qui ferait de la sélection un attracteur.*

---

## 6. Verdict du front (a) — synthèse (a1)+(a2)+(a3)

Le front (a) du raccord (`LC-RACCORD` §10 : *crossover non linéaire — construire l'état de
raccordement et tester si `⟨g₍₃₎⟩=0` survit hors du perturbatif*) reçoit son verdict :

- **(a1) `[établi, linéaire, FLRW]`** : `ĝ₍₃₎=0 ↦ ǧ₍₃₎=0` est un **point fixe forcé** du
  matching (Weyl `(1,3)` invariant ⟹ marée partagée ; carte homogène ; pas de source TT
  sur fond isotrope), indépendant de la prescription.
- **(a2) `[établi, O(h²), conditionnel à l'isotropie de l'état]`** : `⟨g₍₃₎^{(2)}⟩=0`
  survit, car la back-réaction de Bunch–Davies est **isotrope** (part traceless nulle) ;
  elle renormalise le fond, alimentant l'itération.
- **(a3) `[établi, FLRW]`** : la stabilité de la marée à travers les éons **coïncide** avec
  l'hypothèse de Weyl et avec le candidat #5, sur `P=9k²/4`. **WCH unifie ★ et #5 et lève
  D1 sous WCH.**

**Bilan honnête.** « `⟨g₍₃₎⟩=0` survit hors du perturbatif » est **vrai sous deux
hypothèses nommées** : *isotropie/dS-invariance de l'état de raccordement* (a2) et
*imposition de WCH* (a3). Le programme ne **dérive** pas ces hypothèses ; il montre qu'elles
**suffisent et se rejoignent** — la CCC tient si et seulement si le nouvel éon naît
isotrope et à faible Weyl, et cette unique condition ferme à la fois la marée et le fond.
Les **trois portes** restantes sont précises : (i) état **anisotrope** (Bianchi A ; dS/CFT
non unitaire) → casse (a2) ; (ii) **attracteur dynamique** (back-réaction drive-t-elle `P`
vers `P*` ?) → ferait de (a3) une dérivation, via `N` (`LC-E`) ; (iii) **non-linéaire
complet** au-delà de `O(h²)`. Toutes `décision ouverte / à inventer`.

---

## 7. Format de chaînon

- **Hypothèse testée.** Le point fixe de marée `g₍₃₎=0` est-il stable sous l'itération
  inter-éons de l'atlas, ou le runaway `(m,λ)` l'amplifie-t-il ?
- **Outil.** Récurrence de l'atlas (Markwell–Stevens, `LC-A-D1` §4-bis) ; invariant
  `P=mλ` ; réduction 1D et raison `r=P/P*` ; Jacobien et valeurs propres ; scaling du
  spectre tensoriel `P_T∝λ` ; lecture WCH. Sceau `verif_D3_crossover_stabilite.py` (sympy).
- **Critère de réfutation.** *Issue « pas de sélection »* : si la marée ne dépendait pas
  de `λ` (pas de couplage fond↔amplitude), le runaway serait sans effet sur Weyl et WCH ne
  sélectionnerait rien. **Non observé** (`P_T∝λ`). *Réfutation forte (reportée)* : montrer
  que la back-réaction *éloigne* `P` de `P*` (anti-attracteur) — la CCC perdrait sa
  stabilité même sous WCH.
- **Verdict.** `WCH ⟺ #5 ⟺ P=9k²/4` `[établi, FLRW]` ; point fixe non-hyperbolique
  (vp 1 double défective) `[établi]`. Attracteur dynamique et cas inhomogène
  `[décision ouverte / à inventer]`.

---

## 8. Renvois, glossaire, références

**Renvois.** `LC-D3-CROSSOVER-MATCHING` (a1 : carte homogène, `M` fixé par `c₁`) ;
`LC-D3-CROSSOVER-BACKREACTION` (a2 : source isotrope de l'itération) ;
`LC-A-D1-FACTEUR-CONFORME` (atlas §4-bis : récurrence, `P*`, runaway) ;
`LC-A-D1-STABILITE-WEYL` (candidat #5 : carte non-hyperbolique vp 1 double — **ici
identifiée à WCH**) ; `LC-D3-WEYL-BUNCHDAVIES` (★ BD/marée) ;
`LC-E-PLANCK-RESIDUEL` (coupure `N` pour un éventuel attracteur dynamique) ;
`LC-D-HOLOGRAPHIE-G3` ; `LC-WORK-REPRISE-RACCORD` §10 (front (a)).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Invariant `P=mλ` de l'itération CCC* : conservé par la récurrence de l'atlas ;
  level-set critique `P*=9k²/4` = ligne de points fixes.
- *Sélection WCH ⟺ #5* : exiger une marée bornée (faible Weyl) à chaque Big Bang
  sélectionne `P=P*` = point fixe du candidat de stabilité ; unifie marée (★) et fond (#5).
- *Point fixe non-hyperbolique CCC* : `vp 1` double, défective (Jordan) ⟹ drift séculaire.
- *Marée vs fond (couplage)* : `P_T∝λ` ⟹ le runaway du fond (re)conditionne l'amplitude
  de la marée à travers les éons.

**Références (`LC-04`, en KB v1.8).** Markwell & Stevens, GRG **55**, 93 (2023)
`[confirmé en KB : 2212.06914v2.pdf]` — récurrence/atlas ; Penrose, *Cycles of Time*
(2010) `[confirmé]` — WCH ; Bunch & Davies, Proc. R. Soc. A **360**, 117 (1978)
`[confirmé]`. (Scaling `P_T∝H²` : standard, schématique ici.)

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
