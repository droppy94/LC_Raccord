---
id: LC-D3-CROSSOVER-ANISOTROPE
titre: "Front (a) du raccord — stress-test du pivot A3 (isotropie de l'état) hors isotropie : A3 ⟸ A4 (WCH) ?"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, WCH, A4, anisotropie, bianchi-A, consolidation, crossover, marée, weyl]
type: chaînon (verdict du front (a), porte (i) de LC-WORK-REPRISE-AUDIT §3.4 ; étage verdict)
statut: verdict établi (issue faible exhibée : l'anisotropie source une marée future ; A3 n'est PAS entraînée automatiquement par A4) / point dynamique résiduel décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (LC-02, LC-AUDIT-VERDICT §5/§8, glossaire)
fichier_compagnon: verif_D1_bianchiA.py
prerequis_kb: [LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-BACKREACTION, LC-D3-WEYL-BUNCHDAVIES, LC-AUDIT-VERDICT, LC-WORK-REPRISE-AUDIT]
renvois: [LC-A-D1-BIANCHI, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-BACKREACTION, LC-D3-CROSSOVER-STABILITE, LC-D3-WEYL-BUNCHDAVIES, LC-AUDIT-VERDICT, LC-WORK-REPRISE-AUDIT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] / front (a) — A3 est le pivot du raccord (a1)+(a2)"
  - "[D3] hypothèse de Weyl — la marée g₃ est l'objet testé"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Crossover·Anisotrope — Le stress-test du pivot A3

> **Cible.** L'audit (`LC-AUDIT-VERDICT` §5, §8) a identifié **A3** — *l'état de raccordement
> est dS-invariant / isotrope* — comme le **pivot unique** sur lequel reposent (a1), (a2),
> la « convergence » (§6.1) *et* la porte (ii). A3 n'avait **jamais été testée hors
> isotropie**. La porte (i) (`LC-WORK-REPRISE-AUDIT` §3) est ce test. Sa cartographie est
> dans `LC-A-D1-BIANCHI` (le **fait** : la carte du crossover devient inhomogène hors
> isotropie). **Ce chaînon en tire le verdict épistémique** sur la question décisive :
>
> $$\textbf{A3 (isotropie de l'état)} \;\overset{?}{\Longleftarrow}\; \textbf{A4 (WCH de Penrose)}.$$
>
> **Verdict (établi — issue faible).** **Non, pas automatiquement.** La marée future
> `σ̌ = −4·(Ricci sans-trace de 𝓘)` (Tod éq. 33) est sourcée par la 3-géométrie
> **intrinsèque** de la surface de raccordement, objet **distinct** du Weyl de cœur que la
> WCH supprime. Trois arguments convergents (§3) montrent que **la WCH ne force pas
> l'isotropie de `â_ij`** : la conjecture de consolidation `A3⟸A4` (espérée comme l'« issue
> forte ») **n'est pas acquise**. C'est une **réfutation partielle**, à consigner
> honnêtement : la CCC requiert un mécanisme d'isotropisation de la 3-géométrie de 𝓘 (ou
> A3 reste un postulat indépendant). **Reste strictement ouvert** un point dynamique précis
> (§4) : *WCH/régularité force-t-il `â_ij` à être Einstein-3D ?* — c'est `décision ouverte`.

---

## 0. Rôle et garde-fou

Ce chaînon est l'**étage verdict** de la porte (i) ; son **étage cartographie** est
`LC-A-D1-BIANCHI` (le mécanisme géométrique, `établi` au plan de l'algèbre). On sépare les
deux pour ne pas confondre un **fait géométrique** (la carte est inhomogène) avec une
**conclusion sur le programme** (le pivot A3 ne se réduit pas à A4). **Garde-fou
`[à ne pas perdre]`** : l'issue exhibée est *négative* pour la consolidation, mais ce n'est
**pas** une réfutation de la CCC — c'est la mise en évidence qu'une **hypothèse
supplémentaire** (l'isotropie de `â_ij`, ou un mécanisme qui l'assure) est nécessaire et
n'est pas gratuite. Discipline d'audit (`LC-AUDIT-VERDICT` §6.4) maintenue.

---

## 1. Le pivot et l'enjeu de consolidation `[rappel établi]`

**Pourquoi A3 est le pivot (audit §5, §6.1).** Le cœur de (D3) est : *l'état de
Bunch–Davies donne `⟨g₃⟩=0`, ce qui est WCH*. Mais pour un état **gaussien dS-invariant**,
`⟨g₃⟩=0` est **automatique** (moyenne à un point d'un tenseur TT). Tout le contenu réside
donc dans **l'hypothèse que l'état est dS-invariant/isotrope = A3**. La « convergence
D1+D3+[D] » ne *gagne* pas une inconnue : elle *révèle* que ★, D3 et l'état ne sont qu'une
seule inconnue, **A3** (audit §6.1).

**La stratégie de consolidation (`LC-WORK-REPRISE-AUDIT` §5).** La signature des avancées du
projet est : *montrer que deux inconnues n'en font qu'une*. (a3) a montré ★ **=** #5 (établi
en FLRW). La porte (i) **espérait** le pendant : **A3 ⟸ A4** (l'isotropie entraînée par la
WCH), ce qui ferait collapser les deux maillons les plus faibles de l'audit en **un seul
postulat (WCH)**. C'est l'« issue forte » du §3.4. Le présent chaînon teste si elle tient.

---

## 2. Le mécanisme (rappelé de LC-A-D1-BIANCHI) et les trois issues `[établi / cadre]`

**Le fait géométrique** (`LC-A-D1-BIANCHI` §3 ; sceau `verif_D1_bianchiA.py` [B2]) :

$$\check\sigma_{ij} = -4\Big(R^{(\hat a)}_{ij} - \tfrac13 R^{(\hat a)}\,\hat a_{ij}\Big),
\qquad |\check\sigma|^2(\varepsilon) = 128\,\varepsilon^2 + O(\varepsilon^4).$$

La marée future est `0` ssi `â_ij` est Einstein-3D (isotrope), non nulle sinon. Le test de
A3 se ramène donc à : **la WCH (A4) force-t-elle `â_ij` à être Einstein-3D ?** Trois issues
étaient possibles (`LC-WORK-REPRISE-AUDIT` §3.4) :

| issue | énoncé | conséquence |
|---|---|---|
| **forte** (espérée) | WCH ⟹ `σ̌→0` ⟹ `â` isotrope ⟹ **A3⟸A4** | le pivot disparaît comme hypothèse séparée (consolidation) |
| **faible** (stress réussi) | l'anisotropie source `σ̌≠0` **même sous WCH** | A3 irréductiblement indépendante (réfutation partielle) |
| **neutre** | `σ̌` peut être ≠0 mais sans lien établi à WCH | robustesse gagnée, consolidation non |

**Verdict de ce chaînon : c'est l'issue FAIBLE (avec un résidu neutre).** Justification au §3.

---

## 3. Pourquoi la WCH ne force pas l'isotropie de `â_ij` `[établi — trois arguments]`

### 3.1 La marée future est sourcée par un objet *intrinsèque*, pas par le Weyl de cœur
`σ̌` dépend du **Ricci sans-trace de la 3-géométrie de 𝓘** (`R^{(â)}_{ij}−⅓R^{(â)}â_{ij}`).
C'est, dans la donnée de Friedrich `(a_{ij}, c_{ij})`, une fonction de la part **`a_{ij}`
intrinsèque** — *pas* du Weyl `C_{abcd}` ni de sa dérivée normale `c_{ij}` que la WCH
contraint. **La WCH supprime le Weyl de cœur au bang ; elle ne dit rien du Ricci sans-trace
de la 3-métrique de raccordement.** Les deux objets sont indépendants dans le comptage de
Friedrich (cf. `LC-A-D1-FACTEUR-CONFORME` §3).

### 3.2 La rigidité d'Anguige–Tod ne vaut que pour un fluide parfait — inapplicable ici
Tod note en introduction (arXiv:1309.7248, §1) : **« zero Weyl tensor at the bang forces the
metric to be FRW »** (Anguige–Tod, *Ann. Phys.* 276, 1999) — *mais pour un fluide parfait*.
Or, immédiatement après, Tod conclut : *« for CCC to work, the matter content after the bang
cannot in general be as simple as a perfect fluid »*. C'est exactement ce que montre son
éq. (33) : la matière post-bang **porte `σ̌`**, donc **n'est pas un fluide parfait**. La
rigidité « Weyl nul ⟹ FRW » **ne s'applique pas** à la matière CCC. Autrement dit : on ne
peut pas invoquer « Weyl nul au bang (WCH) ⟹ isotropie » car le théorème qui le donnerait
suppose précisément ce que la CCC viole.

### 3.3 Le no-hair de Starobinsky tue le cisaillement *cinétique*, pas la *courbure gelée*
La Λ-domination du passé près de 𝓘 (de Sitter) **isotropise** : le théorème de no-hair
(Starobinsky, *JETP Lett.* 37, 1983 ; réf. [15] de Tod) fait décroître le cisaillement
**cinétique** `α̇, β̇, γ̇ → 0`. **Mais** la 3-métrique **rescalée** de 𝓘 (`â_ij`, finie par
construction de Tod, choisie à courbure scalaire constante via Yamabe) garde une
**courbure-anisotropie gelée** : les rapports d'échelle `(α₀, β₀, γ₀)` survivent, et son
Ricci sans-trace est génériquement non nul. Le no-hair éteint la *vitesse* d'anisotropie,
pas la *forme* du résidu — et c'est la forme qui source `σ̌` (§3.1). *Le sceau le modélise :
`â_ij = (e^{α₀}, e^{−α₀}, …)` gelé, `|σ̌|² = 128ε² ≠ 0`.*

$$\boxed{\ \text{WCH (A4) supprime } C_{abcd}\big|_{\text{bang}} ;\ \text{elle ne supprime pas } R^{(\hat a)}_{ij}-\tfrac13 R^{(\hat a)}\hat a_{ij}.\ \Rightarrow\ \textbf{A3} \not\Leftarrow \textbf{A4 (automatiquement)}.\ }$$

<svg width="100%" viewBox="0 0 680 300" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Pourquoi A3 ne collapse pas dans A4, contrairement à ★=#5 dans (a3)</title>
  <desc>Comparaison de deux tentatives de consolidation. En haut, l'acquis de (a3) : la sélection de la marée (étoile) et la stabilité du fond (numéro 5) collapsent en une seule inconnue, établi en FLRW. En bas, la porte (i) : on espérait que l'isotropie A3 soit entraînée par la WCH A4, mais la marée future est sourcée par le Ricci sans-trace intrinsèque de I, que la WCH ne contraint pas ; donc A3 ne collapse pas dans A4. Le lien est barré.</desc>
  <rect x="30" y="36" width="620" height="104" rx="9" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="48" y="60" font-size="12.5" font-weight="500" fill="#0F6E56">Acquis (a3) — consolidation RÉUSSIE (FLRW) :</text>
  <text x="150" y="98" text-anchor="middle" font-size="13" fill="#3d3d3a">★ (sélection marée)</text>
  <text x="345" y="98" text-anchor="middle" font-size="16" fill="#0F6E56">=</text>
  <text x="520" y="98" text-anchor="middle" font-size="13" fill="#3d3d3a">#5 (stabilité fond)</text>
  <text x="345" y="124" text-anchor="middle" font-size="11.5" fill="#0F6E56">une seule inconnue ✓ (établi)</text>
  <rect x="30" y="160" width="620" height="120" rx="9" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="48" y="184" font-size="12.5" font-weight="500" fill="#993C1D">Porte (i) — consolidation espérée A3⟸A4 : NON acquise (issue faible) :</text>
  <text x="150" y="222" text-anchor="middle" font-size="13" fill="#3d3d3a">A3 (isotropie état)</text>
  <text x="345" y="222" text-anchor="middle" font-size="16" fill="#A32D2D">⟸̸</text>
  <text x="520" y="222" text-anchor="middle" font-size="13" fill="#3d3d3a">A4 (WCH)</text>
  <line x1="318" y1="216" x2="372" y2="228" stroke="#A32D2D" stroke-width="2"/>
  <text x="345" y="250" text-anchor="middle" font-size="11.5" fill="#A32D2D">σ̌ vient du Ricci sans-trace de 𝓘 (intrinsèque),</text>
  <text x="345" y="266" text-anchor="middle" font-size="11.5" fill="#A32D2D">que la WCH (Weyl de cœur) ne contraint pas</text>
</svg>

*Fig. — (a3) a fait collapser ★ et #5 en une inconnue (vert, établi). La porte (i) espérait
le même collapse `A3⟸A4` ; il n'a pas lieu (rouge) : `σ̌` est sourcée par un objet
intrinsèque hors de portée de la WCH.*

---

## 4. Ce qui reste strictement ouvert — le point dynamique `[décision ouverte]`

Les §3 montrent que **les voies évidentes** (Anguige–Tod, no-hair) **ne** donnent **pas**
`A3⟸A4`. Mais l'issue faible n'est pas une réfutation *définitive* : il reste un énoncé
précis, non tranché, qui — s'il était vrai — sauverait une consolidation plus subtile :

> **Question dynamique résiduelle.** *Une condition de régularité au crossover (WCH étendue
> au-delà du Weyl de cœur, ou la condition d'extension conforme `C¹`/`C^∞` de Friedrich à
> travers `𝒞`) force-t-elle la 3-métrique rescalée `â_ij` de 𝓘 à être un **espace
> d'Einstein 3D** (donc, en dim. 3, à courbure constante = isotrope) ?*

En dimension 3, Einstein ⟺ courbure constante ⟺ Ricci sans-trace nul ⟺ `σ̌=0`. La question
est donc : *la régularité du recollement impose-t-elle `â_ij` Einstein-3D ?* Si **oui**,
l'issue forte est restaurée par une porte plus fine ; si **non**, l'issue faible est
définitive et A3 est un postulat séparé. **C'est le prochain calcul** (annoncé en suite de
ce chaînon), et il est `formalisable` (régularité de l'extension conforme de `â_ij` à
travers `𝒞`, dans le cadre de Friedrich/Tod).

---

## 5. Conséquence pour le programme `[méta — établi]`

- **Comptabilité des hypothèses (audit §8).** Avant la porte (i), l'espoir était : si
  `A3⟸A4`, il ne resterait comme inconnues-socle indépendantes que **A1/A2 (dS/CFT)** et
  **A4 (WCH)**. **Ce resserrement n'a pas lieu** : A3 demeure indépendante. La cible ne se
  réduit donc **pas** ; elle est précisée — *A3 est le coût explicite de l'isotropie du
  raccordement*.
- **Repriorisation (suite).** La porte (ii) (attracteur dynamique) **suppose** le point
  fixe `g₃=0` ; or la porte (i) montre que ce point fixe **n'existe pas hors isotropie**.
  Donc la porte (ii) ne peut être tentée qu'**après** avoir réglé la question §4 (la
  régularité force-t-elle l'isotropie ?). La priorité reste : §4 d'abord.
- **Honnêteté (audit §6.4).** Ce chaînon est un **résultat négatif honnête** (au sens de
  `LC-E-PLANCK-RESIDUEL`) : il borne ce que la consolidation peut faire, sans surclasser.

---

## 6. Format de chaînon standard

- **Zone ambiguë.** « L'audit dit que A3 porte tout ; on espérait qu'A3 soit entraînée par
  la WCH (A4), réduisant le programme à un seul postulat. »
- **Hypothèse testée.** *Conjecture de consolidation :* imposer WCH (A4) force `σ→0` au
  bang, donc l'isotropie de l'état de raccordement (A3).
- **Outil.** Marée future de Tod (éq. 33) ; comptage de Friedrich `(a,c)` ; rigidité
  Anguige–Tod ; no-hair de Starobinsky ; sceau `verif_D1_bianchiA.py` [B2]-[B3].
- **Critère de réfutation de l'hypothèse.** Si l'anisotropie de `â_ij` produisait `σ̌≠0`
  alors que la WCH est imposée, la consolidation `A3⟸A4` tomberait. — **Réalisé** : `σ̌`
  vient du Ricci sans-trace intrinsèque (§3.1), hors de portée de la WCH (§3.2-3.3).
- **Verdict.** **Issue faible établie** : `A3 ⟸ A4` **non acquise** ; A3 reste une
  hypothèse-socle indépendante. **Réfutation partielle** de la conjecture de consolidation.
  Point dynamique résiduel (§4) `décision ouverte`. `[verdict établi ; suite décision ouverte]`

---

## 7. Renvois, glossaire, références

**Renvois.** **Frère cartographie : `LC-A-D1-BIANCHI`** (le mécanisme géométrique) ;
`LC-D3-CROSSOVER-MATCHING` (lemme [S4], `0↦0` en FLRW) ; `LC-D3-CROSSOVER-BACKREACTION`
(a2 isotrope) ; `LC-D3-CROSSOVER-STABILITE` / `LC-D3-WEYL-BUNCHDAVIES` (★, un-point) ;
`LC-AUDIT-VERDICT` §5 (A3 pivot), §6.1 (convergence légère), §8 (suite) ;
`LC-WORK-REPRISE-AUDIT` §3.4 (les trois issues), §5 (stratégie de consolidation) ;
contraste `LC-E-PLANCK-RESIDUEL` (résultat négatif honnête).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Pivot A3* : hypothèse que l'état de raccordement est dS-invariant/isotrope ; porte (a1),
  (a2), la convergence et la porte (ii).
- *Conjecture de consolidation `A3⟸A4`* : espoir que la WCH entraîne l'isotropie ; **issue
  faible** : non acquise (la marée future vient du Ricci sans-trace intrinsèque de 𝓘).
- *Issue forte / faible / neutre* (porte i) : la WCH force / ne force pas / force sans lien
  établi l'isotropie de la 3-géométrie de raccordement.
- *Question Einstein-3D de 𝓘* : la régularité du recollement force-t-elle `â_ij` à courbure
  constante ? (= condition pour restaurer l'issue forte). `décision ouverte`.

**Références (`LC-04`) — à ajouter/préciser.**
- **K. P. Tod**, arXiv:1309.7248v2 = *GRG* **47**, 17 (2015) `[confirmé — texte intégral lu]`
  — éq. (33) (marée future = −4·Ricci sans-trace de 𝓘) ; remarque « Weyl nul ⟹ FRW pour
  fluide parfait » et « la matière post-bang n'est pas un fluide parfait ».
- **K. Anguige & K. P. Tod**, « Isotropic cosmological singularities I », *Ann. Phys.* **276**,
  257-293 (1999) `[confirmé — lève le `à vérifier` de LC-04]` — Weyl nul au bang ⟹ FRW
  (fluide parfait).
- **A. A. Starobinsky**, « Isotropization … effective cosmological constant », *JETP Lett.*
  **37**, 66-69 (1983) `[confirmé]` — no-hair / isotropisation Λ-dominée.
- Friedrich, *CMP* **107** (1986) `[confirmé, KB]` — donnée `(a,c)` à `𝓘`.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : un `établi` de sceau = « l'algèbre est correcte », jamais
« la physique est établie ». Ici l'`établi` porte sur l'issue faible (le mécanisme), pas sur
le sort dynamique final (§4, ouvert).*
