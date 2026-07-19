---
id: LC-D3-WCH-CANCELLATION
titre: "Front (a) — la WCH un-point est une CANCELLATION (symétrie), non une perte d'amplitude : trois mécanismes distincts, et l'analogie BAO↔horizon"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, WCH, pivot-A3, cancellation, no-hair, variance, bunch-davies, bao, gurzadyan-penrose, empreinte]
type: chaînon (clarification mécaniste + résonance structurelle ; rattaché au pivot A3)
statut: distinction des trois mécanismes établie (algèbre) / analogie BAO↔horizon résonance structurelle, non dérivée / empreinte inter-éon (cercles GP) réelle mais contestée
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (LC-02, LC-03 glossaire, LC-04 réfs ; éclaire LC-AUDIT-VERDICT §6.1)
fichier_compagnon: verif_D3_cancellation.py
prerequis_kb: [LC-D3-WEYL-BUNCHDAVIES, LC-D3-CROSSOVER-BACKREACTION, LC-D3-CROSSOVER-ANISOTROPE, LC-D3-CROSSOVER-EINSTEIN3D, LC-AUDIT-VERDICT]
renvois: [LC-D3-WEYL-BUNCHDAVIES, LC-D3-CROSSOVER-BACKREACTION, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-ANISOTROPE, LC-D3-CROSSOVER-EINSTEIN3D, LC-A-D1-BIANCHI, LC-E-PLANCK-RESIDUEL, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[D3] hypothèse de Weyl — la WCH un-point est l'objet clarifié"
  - "[A] / front (a) — A3 est le pivot dont ce chaînon nomme le contenu physique"
  - "[E] retour de l'échelle — la variance survivante est le contact CMB"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·WCH·Cancellation — « Les ondes s'éteignent-elles, ou s'annulent-elles ? »

> **Cible.** Question posée frontalement : *à la frontière de de Sitter, les ondes
> gravitationnelles « disparaissent » — est-ce par **perte d'amplitude** ou parce qu'elles
> **s'annulent entre elles** ?* La réponse exige de séparer **trois** objets que l'image
> naïve « les ondes s'éteignent » confond. Une fois séparés, on obtient le **nom physique
> exact du pivot A3** — et une résonance structurelle propre avec les BAO.
>
> **Verdict (établi — algèbre ; sceau `verif_D3_cancellation.py`).** Trois mécanismes
> distincts : **[C1]** le mode inhomogène **gèle** (`f→1`), il ne perd **pas** son amplitude
> (la marée rescalée `g₃` par mode est finie) ; **[C2]** une perte d'amplitude **réelle**
> existe, mais d'un **autre** objet — le cisaillement **homogène du fond** que le no-hair
> dissipe (`σ∝a^{-3}→0`) ; **[C3]** la WCH un-point `⟨g₃⟩=0` est une **CANCELLATION** des
> contributions **signées** des modes de toutes directions (`∫k̂k̂=⅓δ` tue la part
> sans-trace) — elle **exige la symétrie**, donc elle **est** le contenu de A3 ; **[C4]** la
> **variance** `⟨g₃g₃⟩∼k³` est une somme de **carrés** — rien ne s'y compense, elle
> **survit** comme empreinte durable (spectre primordial, contact [E]/CMB). **Donc : la
> disparition des ondes au sens WCH est une cancellation [C3], pas une perte d'amplitude.**
> Analogie **BAO ↔ horizon** : `[résonance structurelle, non dérivée]` — moyenne qui se lave
> ([C3]) ↔ `⟨δ⟩=0` ; empreinte deux-points ([C4]) ↔ bosse BAO ; instanciation inter-éon
> candidate ↔ cercles de Gurzadyan–Penrose (**réel, contesté**).

---

## 0. Rôle et garde-fou

Ce chaînon est une **clarification mécaniste** : il ne produit pas un résultat neuf de
calcul, il **nomme et sépare** des mécanismes déjà présents dans les sceaux
(`verif_D3_bunchdavies`, `verif_D3_backreaction`, `verif_D1_einstein3d`), parce que leur
confusion est une source d'erreur d'intuition. **Garde-fou `[à ne pas perdre]`** : la
distinction des trois mécanismes est `établi` (algèbre vérifiée) ; l'analogie BAO↔horizon
est `[résonance structurelle]` — un pont de **vocabulaire**, pas une dérivation (discipline
d'audit §6.5, qui met en garde contre exactement ce glissement dans l'arc φ). On enregistre
l'analogie comme **féconde et non dérivée**, sans la surclasser.

---

## 1. Les trois mécanismes `[établi]`

Compagnon : `verif_D3_cancellation.py`. Les modes tensoriels de de Sitter (Bunch–Davies)
sont l'objet ; on suit ce qui leur arrive à `𝓘` (`η→0`).

**[C1] Le mode inhomogène GÈLE — il ne perd pas son amplitude.** Le mode
`f = (1+ikη)e^{−ikη} → 1` quand `η→0` : il **gèle** à une constante (le « gel des modes
super-horizon », standard en inflation). La marée *rescalée* par mode `g₃ = −ik³/3` est
**finie et non nulle**. Le Weyl *physique* (non rescalé) `E_ij = O(η) → 0`, mais uniquement
via le facteur conforme `Ω→0` ; le **datum qui devient la marée de l'éon suivant** ne
décroît pas. **« Les ondes perdent leur amplitude » est faux pour l'objet pertinent.**

**[C2] Une perte d'amplitude RÉELLE — mais d'un autre objet (le fond).** Le cisaillement
**homogène** du fond `σ_bg` obéit, en Λ-domination, à `σ̇ + 3Hσ = 0` ⟹ `σ_bg ∝ e^{−3Ht} → 0`
(no-hair de Wald/Starobinsky, `σ∝a^{−3}`). **Ceci** est une vraie dissipation — mais du
cisaillement **cinétique du fond**, pas des ondes inhomogènes [C1], ni de la courbure-
anisotropie **gelée** de `â` (qui, elle, survit — `LC-D3-CROSSOVER-EINSTEIN3D` §2). C'est la
confusion la plus fréquente : on attribue aux ondes la dissipation qui n'appartient qu'au
fond.

**[C3] La WCH un-point est une CANCELLATION (par symétrie).** L'énoncé `⟨g₃⟩ = 0` (= WCH au
niveau un-point) vient de ce que les contributions **signées** des modes de toutes les
directions se **compensent** : `⟨k̂_i k̂_j⟩ = ⅓δ_ij` annule exactement la part sans-trace
(sceau : part traceless `= 0`). Ce n'est **pas** de la dissipation — c'est de
l'**interférence destructive directionnelle**. Chaque onde porte une marée orientée
`∝ k̂_i k̂_j` ; dans un état isotrope, ces orientations s'annulent en moyenne. **Une
cancellation a besoin d'une symétrie** : casser l'isotropie la détruit. Le sceau le montre :
état anisotrope (poids quadrupolaire `ε`) ⟹ part sans-trace `∝ (−1,−1,2)ε/15 ≠ 0`
(`LC-D3-CROSSOVER-BACKREACTION`/[B3]). **[C3] est, mot pour mot, le contenu physique du pivot
A3.**

**[C4] La variance deux-points SURVIT (empreinte).** `⟨g₃g₃⟩ ∼ k³` (conforme `Δ=3`) est une
somme de **carrés** (`|g₃|² = k⁶/9 > 0`, `⟨k̂_z²⟩ = ⅓ > 0`) : rien ne s'y compense. La
variance est **irréductible** — c'est le spectre primordial invariant d'échelle, le contact
[E]/CMB (`verif_D3_bunchdavies` [6]).

$$\boxed{\ \text{ondes à 𝓘 : } \underbrace{\text{gèlent}}_{[C1]} ;\ \underbrace{\text{fond se dissipe}}_{[C2]} ;\ \underbrace{\langle g_3\rangle=0\ (\text{cancellation, = A3})}_{[C3]} ;\ \underbrace{\langle g_3 g_3\rangle\sim k^3\ (\text{empreinte})}_{[C4]}.\ }$$

<svg width="100%" viewBox="0 0 680 250" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Quatre objets à 𝓘 : gel, dissipation du fond, cancellation un-point, variance survivante</title>
  <desc>Quatre colonnes. C1 : le mode inhomogène gèle à une constante, pas de perte d'amplitude. C2 : le cisaillement homogène du fond décroît exponentiellement vers zéro par no-hair, vraie perte d'amplitude mais autre objet. C3 : la moyenne à un point des marées orientées s'annule par symétrie directionnelle, c'est la WCH un-point et le contenu du pivot A3, cassée si anisotrope. C4 : la variance à deux points est une somme de carrés qui ne s'annule pas, empreinte durable.</desc>
  <rect x="22" y="36" width="150" height="150" rx="9" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="97" y="58" text-anchor="middle" font-size="12" font-weight="600" fill="#0F6E56">[C1] mode</text>
  <text x="97" y="100" text-anchor="middle" font-size="12" fill="#3d3d3a">gèle (f→1)</text>
  <text x="97" y="120" text-anchor="middle" font-size="12" fill="#3d3d3a">g₃ fini</text>
  <text x="97" y="166" text-anchor="middle" font-size="10.5" fill="#0F6E56">pas de perte</text>
  <rect x="182" y="36" width="150" height="150" rx="9" fill="#EAF0FA" stroke="#534AB7" stroke-width="0.7"/>
  <text x="257" y="58" text-anchor="middle" font-size="12" font-weight="600" fill="#3C3489">[C2] fond</text>
  <text x="257" y="100" text-anchor="middle" font-size="12" fill="#3d3d3a">σ_bg∝e^{−3Ht}</text>
  <text x="257" y="120" text-anchor="middle" font-size="12" fill="#3d3d3a">→ 0 (no-hair)</text>
  <text x="257" y="166" text-anchor="middle" font-size="10.5" fill="#3C3489">perte RÉELLE</text>
  <rect x="342" y="36" width="150" height="150" rx="9" fill="#FAECE7" stroke="#A32D2D" stroke-width="0.9"/>
  <text x="417" y="58" text-anchor="middle" font-size="12" font-weight="600" fill="#A32D2D">[C3] ⟨g₃⟩=0</text>
  <text x="417" y="100" text-anchor="middle" font-size="12" fill="#993C1D">CANCELLATION</text>
  <text x="417" y="120" text-anchor="middle" font-size="12" fill="#993C1D">(symétrie)</text>
  <text x="417" y="160" text-anchor="middle" font-size="10.5" font-weight="600" fill="#7A1D1D">= WCH = A3</text>
  <text x="417" y="176" text-anchor="middle" font-size="10" fill="#A32D2D">cassée si anisotrope</text>
  <rect x="502" y="36" width="156" height="150" rx="9" fill="#FBF4E1" stroke="#C79A2B" stroke-width="0.7"/>
  <text x="580" y="58" text-anchor="middle" font-size="12" font-weight="600" fill="#8A6A12">[C4] ⟨g₃g₃⟩</text>
  <text x="580" y="100" text-anchor="middle" font-size="12" fill="#3d3d3a">∼ k³ (carrés)</text>
  <text x="580" y="120" text-anchor="middle" font-size="12" fill="#3d3d3a">ne s'annule pas</text>
  <text x="580" y="166" text-anchor="middle" font-size="10.5" fill="#8A6A12">EMPREINTE</text>
  <text x="340" y="218" text-anchor="middle" font-size="11" fill="#3d3d3a">« disparition des ondes » au sens WCH = [C3] cancellation — pas [C1]/[C2] perte d'amplitude</text>
  <text x="340" y="238" text-anchor="middle" font-size="10.5" fill="#8A6A12">ce qui RESTE = [C4] la variance (empreinte primordiale, contact CMB)</text>
</svg>

*Fig. — Les quatre objets distincts à 𝓘. La WCH un-point est la colonne [C3] (cancellation,
contingente à la symétrie = A3) ; l'empreinte est [C4] (variance irréductible).*

---

## 2. Ce que cela dit du pivot A3 `[établi — lecture]`

L'audit (§6.1) notait que `⟨g₃⟩=0` pour un état gaussien dS-invariant est « automatique »,
« la moyenne s'annule par symétrie ». **[C3] en est la traduction physique exacte** : la WCH
un-point n'est pas un fait dynamique robuste (les ondes ne « s'éteignent » pas) mais une
**cancellation contingente à une symétrie**. D'où, *directement* :

- **Pourquoi A3 porte tout.** Si la WCH-un-point tenait par perte d'amplitude [C1/C2], elle
  serait robuste indépendamment de l'état. Mais elle tient par cancellation [C3] : **enlever
  la symétrie suffit à la détruire** — c'est précisément ce que montrent
  `LC-D3-CROSSOVER-ANISOTROPE` (`⟨g₃⟩≠0` hors isotropie) et `LC-D3-CROSSOVER-EINSTEIN3D`
  (aucune régularité plus faible que A3 ne restaure la symétrie). **A3 est le nom de la
  symétrie dont [C3] a besoin.**
- **Le no-hair ne sauve pas A3.** [C2] (no-hair) dissipe le fond, mais [C3] dépend de la
  symétrie de l'**état des fluctuations**, pas du fond — d'où l'inefficacité du no-hair sur
  A3 (`LC-D3-CROSSOVER-ANISOTROPE` §3.3). La séparation [C2]/[C3] **est** cette inefficacité.

---

## 3. L'analogie BAO ↔ horizon `[résonance structurelle, non dérivée]`

Le squelette commun : *une onde qui se propage gèle à une surface d'horizon ; sa moyenne se
lave, sa variance laisse une échelle gelée.* Mappage précis :

| BAO / CMB | de Sitter / CCC |
|---|---|
| surface de dernière diffusion (« switch-off ») | crossover `𝒞` / `𝓘` |
| moyenne `⟨δ⟩ = 0` (se lave) | **[C3]** `⟨g₃⟩ = 0` (cancellation) |
| bosse BAO dans le **deux-points** (survit) | **[C4]** `⟨g₃g₃⟩ ∼ k³` (variance) |
| règle-étalon (empreinte durable) | spectre primordial gelé / donnée du nouvel éon |

**Ce que l'analogie capture bien** : la BAO n'est pas dans la densité moyenne (`⟨δ⟩=0`) mais
dans la corrélation à deux points — donc elle se mappe **exactement** sur la part qui
survit, [C4], pas sur la part qui s'annule, [C3]. « S'effacent mais laissent une empreinte »
= « le un-point se compense, le deux-points reste ».

**Réserves `[à ne pas perdre]`.** (i) « S'étendent » : la coquille BAO s'étend puis gèle,
tandis que l'horizon de Sitter est un tamis de **taille physique fixe** (`ℓ_dS=√(3/Λ)`) que
les échelles comobiles traversent — l'image juste est « échelle gelée à un franchissement
d'horizon », pas « sphère qui grandit ». (ii) « Information » : holographique (entropie ∝
aire, LC-E) pour l'horizon dS, vs corrélation gelée pour la BAO — deux notions distinctes ;
les souder serait le glissement de vocabulaire que l'audit §6.5 proscrit. **Tag : pont de
vocabulaire fécond, non dérivé.**

**Instanciation concrète (et son statut).** Le pendant **inter-éon** exact de la BAO existe
dans la littérature : les **cercles concentriques de faible variance** de Gurzadyan–Penrose
dans le CMB — empreintes supposées d'événements de l'éon *précédent* (rencontres de trous
noirs supermassifs) estampées sur notre surface de dernière diffusion. C'est, mot pour mot,
« des sphères d'information qui s'effacent mais laissent une empreinte géométrique »,
traversant la frontière d'éon. **Statut : revendiqué (Gurzadyan–Penrose 2010, 2013) mais
CONTESTÉ** (attribué par d'autres au hasard d'un ciel gaussien). `[réel, contesté — à
suivre]`.

---

## 4. Format de chaînon standard

- **Zone ambiguë.** « Les ondes disparaissent à 𝓘 » — par perte d'amplitude ou par
  annulation mutuelle ?
- **Hypothèse clarifiée.** Quatre objets distincts : mode (gèle), fond (se dissipe), moyenne
  (cancellation), variance (survit).
- **Outil.** Mode Bunch–Davies (gel) ; ODE du cisaillement de fond (no-hair) ; moyennes
  angulaires isotrope vs quadrupolaire ; spectre `k³`. Sceau `verif_D3_cancellation.py`.
- **Critère de réfutation.** Si `⟨g₃⟩=0` tenait par perte d'amplitude (indépendamment de la
  symétrie), un état anisotrope donnerait encore `⟨g₃⟩=0`. — **Réfuté** : anisotrope ⟹
  `⟨g₃⟩≠0` ([B3]) : c'est bien une cancellation.
- **Verdict.** La WCH un-point = **cancellation** (symétrie) = contenu de A3 ; la variance
  survit (empreinte). Analogie BAO↔horizon `[résonance structurelle]`. `[établi (algèbre) ;
  analogie non dérivée]`

---

## 5. Renvois, glossaire, références

**Renvois.** `LC-D3-WEYL-BUNCHDAVIES` (gel du mode, `g₃`, `⟨g₃g₃⟩~k³`) ;
`LC-D3-CROSSOVER-BACKREACTION` (cancellation isotrope ; sa rupture anisotrope) ;
`LC-D3-CROSSOVER-ANISOTROPE` / `LC-D3-CROSSOVER-EINSTEIN3D` (A3 = la symétrie requise) ;
`LC-A-D1-BIANCHI` (la marée gelée de `â`) ; `LC-AUDIT-VERDICT` §6.1 (« s'annule par
symétrie » — ce chaînon en est la lecture) ; `LC-E-PLANCK-RESIDUEL` (contact CMB,
holographie).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Cancellation un-point (WCH)* : `⟨g₃⟩=0` par compensation des contributions signées d'un
  état isotrope ; ≠ perte d'amplitude ; contingente à la symétrie = A3.
- *Gel des modes* : le mode tensoriel super-horizon tend vers une constante à `𝓘` (`g₃`
  fini), il ne décroît pas.
- *Empreinte deux-points* : `⟨g₃g₃⟩~k³`, somme de carrés irréductible ; spectre primordial.
- *Résonance BAO↔horizon* : analogie structurelle (moyenne se lave / variance reste) ;
  instanciation inter-éon candidate = cercles de Gurzadyan–Penrose. `[non dérivée]`.

**Références (`LC-04`) — à préciser.**
- Bunch & Davies, *Proc. R. Soc. A* **360**, 117 (1978) `[confirmé, KB]`.
- **R. M. Wald**, « Asymptotic behavior of homogeneous cosmological models with Λ », *Phys.
  Rev. D* **28**, 2118 (1983) `[confirmé]` — no-hair (dissipation du cisaillement de fond).
- Starobinsky, *JETP Lett.* **37**, 66 (1983) `[confirmé]`.
- **V. G. Gurzadyan & R. Penrose**, « Concentric low-variance circles in the CMB sky »,
  *Eur. Phys. J. Plus* **128**, 22 (2013) `[réel ; observationnellement contesté]` —
  empreinte inter-éon candidate (pendant CCC de la BAO).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : la distinction des trois mécanismes est `établi` (algèbre) ;
l'analogie BAO↔horizon est `résonance structurelle, non dérivée` ; les cercles GP sont
`réels mais contestés`. Un `établi` de sceau = « l'algèbre est correcte », jamais « la
physique est établie ».*
