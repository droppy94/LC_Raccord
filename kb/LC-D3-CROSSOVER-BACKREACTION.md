---
id: LC-D3-CROSSOVER-BACKREACTION
titre: "Module D / crossover (a2) — homogénéité de ⟨g₃⟩ à O(h²) : la back-réaction de Bunch–Davies est isotrope"
codename: LC-RACCORD
tags: [module-D, D3, crossover, backreaction, second-ordre, isaacson, bunch-davies, g3, isotropie, runaway, D1, planck]
type: chaînon (front (a) du raccord, étape a2 ; teste l'homogénéité de (a1) au second ordre)
statut: ⟨g₃^(2)⟩=0 établi à O(h²) CONDITIONNEL à l'invariance dS de l'état / anisotropie de l'état + non-linéaire complet décision ouverte
version: 0.2
langue: fr
date: 2026-06-07
maj: "2026-06-08 — v0.2 : PRISMA (clôture dette biblio front (a), LC-WORK-REPRISE-PIVOT-AUDIT-A action 2) — réf Isaacson (stress effectif des ondes, outil de a2) levée de `à vérifier` à `confirmé` : R. A. Isaacson, Phys. Rev. 166, 1263 (I) & 1272 (II), 1968 (vérifiée APS/DOI). Aucune touche à l'algèbre ni au verdict. v0.1 : chaînon a2 (back-réaction de Bunch–Davies isotrope à O(h²))."
statut_id: provisoire — à enregistrer si validé (index, programme [D]/crossover, glossaire, refs)
fichier_compagnon: verif_D3_backreaction.py
renvois: [LC-D3-CROSSOVER-MATCHING, LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-E-PLANCK-RESIDUEL, LC-WORK-REPRISE-RACCORD, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D3] hypothèse de Weyl (C→0) — ⟨g₃⟩=0 testée au second ordre"
  - "[A]/D1 — la part isotrope de la back-réaction renormalise le fond (m,λ) (atlas §4-bis)"
  - "[E] — la densité du bain de gravitons (UV) = énergie du vide -> coupure holographique N"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·CROSSOVER (a2) — La back-réaction de Bunch–Davies est isotrope

> **Cible.** (a1) (`LC-D3-CROSSOVER-MATCHING`) a montré que la carte de crossover est
> **homogène au niveau linéaire** : `ĝ₍₃₎=0 ↦ ǧ₍₃₎=0`, forcé. Mais Einstein est non
> linéaire, et la 2-points de Bunch–Davies est **irréductible** : `⟨g₍₃₎g₍₃₎⟩~k³ ≠ 0`
> (`LC-D3` §4). Au second ordre, ces fluctuations **back-réagissent** (stress effectif
> des ondes, Isaacson). *La 1-point de la marée acquiert-elle un terme `⟨g₍₃₎^{(2)}⟩≠0`
> qui casserait « né dans le vide » ?*
>
> **Verdict (calculé, `verif_D3_backreaction.py`).** **Non — `⟨g₍₃₎^{(2)}⟩=0` à O(h²),
> conditionnellement à l'invariance dS de l'état.** La 1-point `⟨g₍₃₎^{(2)}⟩` est la part
> traceless-symétrique du stress effectif `⟨τ_ij⟩` dans l'état. Pour **un mode**,
> `τ_ij ∝ k̂_i k̂_j` est *anisotrope* (part traceless `≠0` : une OG isolée porte un
> cisaillement). Mais le vide de Bunch–Davies est **dS-invariant**, donc statistiquement
> **isotrope** : la moyenne d'ensemble est l'intégrale angulaire `∫dΩ k̂_i k̂_j =
> (4π/3)δ_ij`, qui rend `⟨τ_ij⟩ ∝ δ_ij`. **La part traceless d'un tenseur isotrope est
> nulle** (le lemme [S4] de (a1)) ⟹ `⟨g₍₃₎^{(2)}⟩ = 0`. L'homogénéité **survit** au
> second ordre. `[établi, O(h²), conditionnel à l'isotropie de l'état]`
>
> **Où va la back-réaction (la part non nulle).** La part **isotrope** (`ρ`, `p` du bain
> de gravitons BD) ne disparaît pas : elle **renormalise le fond** — `Λ`, donc `(m,λ)` —
> c'est-à-dire qu'elle est la **source de l'itération inter-éons de l'atlas** (`LC-A-D1`
> §4-bis). La survie de la marée à O(h²) renvoie donc *exactement* la dynamique à (a3)
> (le runaway). Et son UV (`ρ~∫dk\,k³`) appelle une **coupure holographique** = le `N` de
> `LC-E` (l'énergie du vide). `[établi (canal) ; quantitatif à inventer / hors de portée]`

---

## 0. Rôle et garde-fou

Ce chaînon **teste l'homogénéité de (a1) à un ordre de plus** ; il ne traite pas le
non-linéaire complet. Ce qui est `établi` : la 1-point de la marée reste nulle à O(h²)
**si** l'état est dS-invariant, parce que la back-réaction est alors isotrope et qu'un
stress isotrope n'a pas de marée. Ce qui reste `décision ouverte / à inventer` : le cas
où l'état de raccordement **brise** l'invariance dS (anisotropie — la porte explicite
d'une marée), la valeur quantitative (UV) de `ρ`, et l'itération complète (a3). On ne
surclasse pas : le résultat est **conditionnel** et c'est tout son intérêt — il identifie
*l'isotropie de l'état* comme le seul verrou restant pour la 1-point.

---

## 1. Le test à O(h²), proprement posé `[cadre]`

La 1-point de la marée au second ordre, `⟨g₍₃₎^{(2)}⟩`, est le secteur **homogène**
(`k→0`) du tide induit par la back-réaction. Sur un fond homogène, la décomposition
scalaire–vecteur–tenseur est orthogonale : la part **TT homogène** de `g₍₃₎^{(2)}` (=
sa part traceless-symétrique, un cisaillement type Bianchi I) n'est sourcée que par la
**part traceless** du stress effectif quadratique `τ_ij[h,h]` (Isaacson). Donc

$$\langle g_{(3)}^{(2)}\rangle \ \propto\ \big(\langle \tau_{ij}\rangle\big)^{\text{traceless}}.$$

La question (a2) est donc : **la part traceless de `⟨τ_ij⟩` dans l'état est-elle nulle ?**

---

## 2. La back-réaction est réelle, et un mode unique est anisotrope `[établi]`

Sceaux [2]–[3]. La densité du bain de gravitons est non nulle (`ρ_mode ~ |h'|²+k²|h|²
= A²k²(2η²k²+1) ≠ 0`) : **la back-réaction existe** (ce n'est pas un résultat trivial
de nullité). Et pour un **mode unique** (`k̂=ẑ`), le stress spatial `τ_ij ∝ k̂_i k̂_j =
diag(0,0,1)` a une part traceless

$$\big(\tau\big)^{\text{traceless}} = \mathrm{diag}\!\left(-\tfrac13,-\tfrac13,\tfrac23\right) \neq 0:$$

une onde gravitationnelle isolée **porte un cisaillement** — elle *sourcerait* une marée
homogène. Le résultat de (a2) ne vient donc pas de l'absence de back-réaction, mais de la
**structure statistique de l'état**. `[établi]`

---

## 3. Le vide de Bunch–Davies est isotrope ⟹ `⟨τ_ij⟩ ∝ δ_ij` `[établi]`

Sceau [4]. Le vide de Bunch–Davies est **dS-invariant**, donc statistiquement homogène
et isotrope. La 1-point au point coïncident est une moyenne d'ensemble = l'intégrale sur
les directions `k̂` du contenu spectral. Les deux structures invariantes pertinentes :

$$\frac{1}{4\pi}\!\int\! d\Omega\, \hat k_i \hat k_j = \tfrac13\delta_{ij},\qquad
\frac{1}{4\pi}\!\int\! d\Omega\, \textstyle\sum_a \Lambda_{ia,ja}(\hat k) = \tfrac43\,\delta_{ij},$$

où `Λ_ij,kl = P_ik P_jl + P_il P_jk − P_ij P_kl` (`P=𝟙−k̂k̂`) est la somme de
polarisation TT. **Toutes** les contractions du stress effectif (flux de moment
`k̂k̂`, contractions de polarisation) sont donc, après moyenne, **proportionnelles à
`δ_ij`** : `⟨τ_ij⟩_{BD} ∝ δ_ij` (forme de fluide parfait : densité + pression isotrope).
`[établi]`

---

## 4. Isotrope ⟹ pas de marée ⟹ `⟨g₍₃₎^{(2)}⟩=0` `[établi, conditionnel]`

Sceau [5]. La part traceless d'un tenseur isotrope est identiquement nulle — c'est le
**lemme [S4] de (a1)** (la projection traceless de `c\,δ_ij` est `0`). Donc

$$\big(\langle\tau_{ij}\rangle_{BD}\big)^{\text{traceless}} = 0
\quad\Longrightarrow\quad \boxed{\ \langle g_{(3)}^{(2)}\rangle = 0\ }.$$

**L'homogénéité `⟨g₍₃₎⟩=0` survit à O(h²)** — « le nouvel éon naît dans le vide » tient
au second ordre, **conditionnellement à l'invariance dS de l'état**. C'est le même lemme
qui ferme (a1) (pas de source TT sur fond isotrope) et (a2) (pas de marée 1-point sur
*état* isotrope) : l'isotropie statistique est le verrou commun.

<svg width="100%" viewBox="0 0 680 360" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>(a2) La back-réaction de Bunch–Davies : un mode est anisotrope, le vide isotrope ⟹ pas de marée</title>
  <desc>À gauche, un mode unique : le stress spatial proportionnel à k chapeau i k chapeau j vaut diag 0 0 1, sa part traceless diag moins un tiers moins un tiers deux tiers est non nulle ; une onde gravitationnelle isolée porte un cisaillement et sourcerait une marée. À droite, le vide de Bunch-Davies, dS-invariant donc isotrope : la moyenne angulaire de k chapeau i k chapeau j vaut un tiers delta, le stress moyen est proportionnel à delta i j, isotrope ; sa part traceless est nulle, donc la valeur moyenne de g3 au second ordre est nulle. En bas : la part isotrope non nulle, densité et pression du bain de gravitons, renormalise le fond Lambda et m lambda, ce qui est la source de l'itération de l'atlas, renvoyée à a3 ; son ultraviolet appelle la coupure holographique N du module E. Réserve : un état anisotrope au raccordement, Bianchi A ou dS-CFT non unitaire, donnerait une moyenne non isotrope et donc une marée non nulle, c'est la porte ouverte.</desc>
  <rect x="40" y="40" width="290" height="150" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="185" y="64" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">UN MODE — anisotrope</text>
  <text x="185" y="90" text-anchor="middle" font-size="12" fill="#3d3d3a">τ_ij ∝ k̂_i k̂_j = diag(0,0,1)</text>
  <text x="185" y="116" text-anchor="middle" font-size="12" fill="#993C1D">traceless = diag(−⅓,−⅓,⅔) ≠ 0</text>
  <text x="185" y="142" text-anchor="middle" font-size="11.5" fill="#73726c">une OG isolée porte un cisaillement</text>
  <text x="185" y="166" text-anchor="middle" font-size="11.5" fill="#73726c">-> sourcerait une marée</text>
  <rect x="350" y="40" width="290" height="150" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="495" y="64" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">VIDE BD — isotrope (dS-inv.)</text>
  <text x="495" y="90" text-anchor="middle" font-size="12" fill="#3d3d3a">⟨k̂_i k̂_j⟩ = ⅓ δ_ij</text>
  <text x="495" y="116" text-anchor="middle" font-size="12" fill="#0F6E56">⟨τ_ij⟩ ∝ δ_ij  (traceless = 0)</text>
  <text x="495" y="142" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">⟹ ⟨g₍₃₎^(2)⟩ = 0</text>
  <text x="495" y="166" text-anchor="middle" font-size="11.5" fill="#73726c">homogénéité survit à O(h²)</text>
  <rect x="40" y="206" width="600" height="60" rx="9" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.7"/>
  <text x="340" y="228" text-anchor="middle" font-size="12" font-weight="500" fill="#3C3489">la part ISOTROPE (ρ, p) ne disparaît pas :</text>
  <text x="340" y="248" text-anchor="middle" font-size="11.5" fill="#3d3d3a">renormalise le fond (Λ, (m,λ)) = source de l'itération atlas → (a3)   ·   UV de ρ → coupure N (LC-E)</text>
  <rect x="40" y="282" width="600" height="62" rx="9" fill="#FBF3E7" stroke="#C98A2B" stroke-width="0.7"/>
  <text x="340" y="304" text-anchor="middle" font-size="12" font-weight="500" fill="#8A5A12">réserve (la porte d'une marée) :</text>
  <text x="340" y="324" text-anchor="middle" font-size="11.5" fill="#3d3d3a">état ANISOTROPE au raccordement (Bianchi A ; dS/CFT non unitaire) ⟹ ⟨k̂k̂⟩≠⅓δ ⟹ ⟨g₍₃₎^(2)⟩≠0</text>
</svg>

*Fig. — (a2). Un mode unique est anisotrope (rouge) et sourcerait une marée ; mais le
vide de Bunch–Davies, isotrope (vert), donne `⟨τ⟩∝δ_ij` dont la part traceless est nulle,
donc `⟨g₍₃₎^{(2)}⟩=0` : l'homogénéité survit. La part isotrope (violet) renormalise le
fond → (a3) ; un état anisotrope (ambre) serait la porte d'une marée.*

---

## 5. Conséquences pour le programme

- **(a1)+(a2) : la convergence D1+D3+[D] tient jusqu'à O(h²)** au crossover, pas
  seulement à un bord — *à la condition* que l'état de raccordement soit dS-invariant.
  Le verrou résiduel pour la 1-point est donc réduit à **un seul énoncé** : *l'état est-il
  isotrope ?*
- **(a2) referme le lien (a2)→(a3).** La back-réaction non nulle est **entièrement
  isotrope** : elle ne touche pas la marée, elle renormalise `(m,λ)`. Elle est donc, mot
  pour mot, **la source de l'itération inter-éons de l'atlas** (`LC-A-D1` §4-bis). La
  question du runaway (a3) hérite ainsi d'une source physique explicite : le bain de
  gravitons de Bunch–Davies.
- **Pont vers [E] (Planck/`N`).** La densité `ρ` du bain a un UV `~∫dk\,k³` : sa
  régularisation est l'**énergie du vide** = la coupure **holographique** `N` de
  `LC-E-PLANCK-RESIDUEL`. La back-réaction isotrope *est* le secteur `Λ`/échelle — cohérent
  avec « `N` holographique, pas sériel ». `[canal établi ; quantitatif hors de portée]`
- **WCH reste un-point.** La 2-points `⟨g₍₃₎g₍₃₎⟩~k³` est inchangée (spectre primordial) :
  conforme à `LC-D3` §4 (WCH = condition d'entropie un-point, pas champ identiquement nul).

---

## 6. Format de chaînon

- **Hypothèse testée.** L'homogénéité `⟨g₍₃₎⟩=0` (1-point de la marée) survit-elle à
  O(h²) sous la back-réaction des fluctuations de Bunch–Davies ?
- **Outil.** Stress effectif d'Isaacson (ordre `h²`) ; mode de Bunch–Davies (`LC-D3`) ;
  somme de polarisation TT `Λ_ij,kl` ; moyennes angulaires `∫dΩ` sur `k̂` ; décomposition
  SVT (la marée = part traceless homogène) ; lemme [S4] de (a1) (isotrope ⟹ pas de TT).
  Sceau `verif_D3_backreaction.py` (sympy).
- **Critère de réfutation.** *Issue « marée induite »* : si `⟨τ_ij⟩` dans l'état avait une
  part traceless non nulle, `⟨g₍₃₎^{(2)}⟩≠0` et « né dans le vide » tomberait à O(h²).
  **Non observé pour le vide BD** (isotrope ⟹ traceless nul). *Réfutation effective
  (reportée)* : un état de raccordement **anisotrope** (Bianchi A ; dS/CFT non unitaire)
  donne `⟨k̂k̂⟩≠⅓δ` et **réalise** cette issue — c'est la direction à instruire.
- **Verdict.** `⟨g₍₃₎^{(2)}⟩=0` `[établi, O(h²), conditionnel à l'isotropie/dS-invariance
  de l'état]`. Back-réaction isotrope = renormalisation du fond → (a3). Anisotropie de
  l'état et non-linéaire complet `[décision ouverte / à inventer]`.

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D3-CROSSOVER-MATCHING` (a1 ; lemme [S4] isotrope⟹pas de TT, réutilisé) ;
`LC-D3-WEYL-BUNCHDAVIES` (mode BD ; 2-points `k³` ; `E=(d/2H)g₍₃₎`) ; `LC-A-D1-FACTEUR-CONFORME`
(atlas §4-bis : la back-réaction isotrope source l'itération `(m,λ)` → (a3)) ;
`LC-A-D1-STABILITE-WEYL` (fond⊥marée ; le fond est le bon réceptacle de la part isotrope) ;
`LC-E-PLANCK-RESIDUEL` (UV de `ρ` = coupure holographique `N`) ; `LC-D-HOLOGRAPHIE-G3`
(état de raccordement non construit — l'isotropie est l'hypothèse) ; `LC-WORK-REPRISE-RACCORD`
§10 (front (a)).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Back-réaction de Bunch–Davies (O(h²))* : stress effectif `τ_ij[h,h]` des fluctuations
  du vide ; isotrope (`∝δ_ij`) car l'état est dS-invariant.
- *1-point de marée au second ordre `⟨g₍₃₎^{(2)}⟩`* : part traceless-symétrique homogène
  de `⟨τ_ij⟩` ; nulle pour un état isotrope.
- *Anisotropie de l'état comme porte d'une marée* : un état de raccordement anisotrope
  donne `⟨k̂k̂⟩≠⅓δ` ⟹ `⟨g₍₃₎^{(2)}⟩≠0`.
- *Canal isotrope de la back-réaction* : `ρ,p` renormalisent `Λ`/`(m,λ)` ; UV = `N` holographique (`LC-E`).

**Références (`LC-04`, en KB v1.8).** Bunch & Davies, Proc. R. Soc. Lond. A **360**, 117
(1978) `[confirmé]` — vide dS-invariant ; Isaacson, Phys. Rev. **166**, 1263 & 1272 (1968)
`[confirmé]` — optique géométrique (I) & stress effectif des ondes gravitationnelles (II) ; Maldacena, JHEP **05**
(2003) 013 `[confirmé]` — dS/CFT, 1-point ; de Haro–Skenderis–Solodukhin, CMP **217**,
595 (2001) `[confirmé]` — FG. (Décomposition SVT et lemme isotrope : standard / sceau (a1).)

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
