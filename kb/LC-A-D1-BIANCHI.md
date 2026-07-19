---
id: LC-A-D1-BIANCHI
titre: "Verrou D1 — l'atlas anisotrope (Bianchi A) : la carte ĝ₃↦ǧ₃ hors isotropie"
codename: LC-RACCORD
tags: [module-A, D1, D3, ccc, bianchi-A, anisotropie, cisaillement, crossover, facteur-conforme, tod, weyl, marée]
type: chaînon (sous-investigation de LC-A-D1, porte (i) de LC-WORK-REPRISE-AUDIT §3 ; étage cartographie)
statut: cartographie établie (le fond anisotrope a un Weyl ≠0 ; la carte ĝ₃↦ǧ₃ devient inhomogène hors isotropie ; le lemme [S4] tombe) / sélection de la prescription décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (LC-A-D1 §4-bis/§5, LC-02, glossaire)
fichier_compagnon: verif_D1_bianchiA.py
prerequis_kb: [LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-BACKREACTION, LC-AUDIT-VERDICT, LC-WORK-REPRISE-AUDIT]
renvois: [LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-A-SURVIE-CONFORME, LC-D3-CROSSOVER-MATCHING, LC-D3-CROSSOVER-BACKREACTION, LC-D3-CROSSOVER-ANISOTROPE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] survie conforme — D1 en est le verrou formel"
  - "[D3] hypothèse de Weyl — la marée g₃ est son objet propre"
  - "[E] retour de l'échelle — le facteur conforme EST le champ d'échelle"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-A·D1·Bianchi — L'atlas anisotrope du crossover

> **Cible.** L'atlas FLRW (`LC-A-D1-FACTEUR-CONFORME` §4-bis) et le candidat #5
> (`LC-A-D1-STABILITE-WEYL`) ont montré que **la fermeture de D1 ne peut pas venir du
> secteur symétrique** : en FLRW le Weyl est identiquement nul, D3 y est vacant, et la
> carte du crossover `ĝ₃ ↦ ǧ₃` est forcée à `0 ↦ 0` (sceau `verif_D3_crossover_matching`,
> lemme **[S4]** : un fond isotrope n'admet aucune source TT). La route restait le
> **secteur inhomogène/anisotrope**. Ce chaînon en pose l'**étage cartographie** :
> *à quoi ressemble la carte du crossover sur un fond homogène **anisotrope** (Bianchi A) ?*
>
> **Verdict (cartographie + sceau).** Sur Bianchi A, **trois faits sont établis** (au sens
> de l'algèbre — `verif_D1_bianchiA.py`, ancré sur Tod 2015) : (1) le fond anisotrope a un
> **tenseur de Weyl non nul** (parts électrique *et* magnétique), sourcé par le cisaillement
> `σ_ij` — D3 a enfin un contenu ; (2) la marée future du crossover est `σ̌ = −4·(Ricci
> sans-trace de 𝓘)` (équation (33) de Tod) : **isotrope ⟹ `σ̌=0` (on retrouve [S4]),
> anisotrope ⟹ `σ̌≠0`** ; (3) un état de raccordement anisotrope injecte de même une marée
> de back-réaction. **La carte devient INHOMOGÈNE hors isotropie : `0 ↦ ≠0`. Le lemme [S4]
> tombe.** Ceci est l'analogue `LC-07` (cartographie), **pas** l'analogue `LC-10`
> (fermeture) : on cartographie le mécanisme, on ne sélectionne pas la prescription. Le
> verdict épistémique sur le **pivot A3** (l'anisotropie est-elle interdite par la WCH ?)
> est porté par le chaînon frère `LC-D3-CROSSOVER-ANISOTROPE`.

---

## 0. Rôle et garde-fou

Comme `LC-07` cartographiait les bundles avant d'assumer, on cartographie ici la carte du
crossover dans un secteur où elle a enfin un contenu non trivial. **Différence honnête
`[à ne pas perdre]`** : ce que ce chaînon établit est **algébrique** (le mécanisme de
sourcing de Tod est exact, [S4] tombe quantitativement) ; il **n'établit pas** que la CCC
admet — ou n'admet pas — des éons anisotropes physiquement. C'est la discipline d'audit
(`LC-AUDIT-VERDICT` §6.4) : *un `établi` de sceau = « l'algèbre est correcte », jamais « la
physique est établie »*. La conséquence physique (le sort du pivot A3) est isolée dans
`LC-D3-CROSSOVER-ANISOTROPE` pour ne pas la confondre avec le fait géométrique.

---

## 1. Le dispositif — Bianchi A, et pourquoi c'est le bon terrain `[établi, sourcé]`

Les métriques de **classe A de Bianchi** (Bianchi I/Kasner, …, Bianchi IX) sont les
cosmologies **homogènes anisotropes** dont les constantes de structure `n_i ∈ {0,±1}`
sont unimodulaires. Deux raisons en font le terrain naturel de la porte (i) :

- **Le cisaillement fournit une structure TT.** En FLRW, `C_{abcd} ≡ 0` (conformément
  plat) : il n'existe aucun tenseur sans-trace transverse local, donc [S4] vaut et la
  carte est `0↦0`. En Bianchi A, le cisaillement `σ_ij` (la part sans-trace de l'expansion)
  **source** un Weyl non nul : la structure TT existe, et [S4] peut tomber.
- **Tod (2015) traite déjà Bianchi A.** `LC-A-D1-FACTEUR-CONFORME` §4 le notait (« cas
  traité : FRW, **Bianchi A** »). La source porteuse en KB (Markwell–Stevens,
  `2212_06914v2`) est **entièrement FRW** (vérifié : aucun Bianchi, aucun cisaillement) ;
  la prescription anisotrope vient donc **uniquement** de **Tod, arXiv:1309.7248v2 = GRG
  47, 17 (2015)**, « The equations of CCC », lu intégralement. On **n'invente pas** le
  fond : on instancie celui de Tod.

**Métrique (Tod éq. 18).** `g = dt² − R²(e^{2α}σ₁² + e^{2β}σ₂² + e^{2γ}σ₃²)`, avec
`α+β+γ=0` (cisaillement sans trace) et `dσ₁ = n₁ σ₂∧σ₃` (et cycliques). La prescription du
facteur conforme reste l'EDP de Tod `φ̈ + 2H²φ = ⅙ s φ³` (éq. 13) avec `φ = Ω̂⁻¹`,
`φ₂ = 0` (Delayed Rest Mass), `φ₁` fixé par Yamabe sur la 3-métrique de 𝓘, et
`2H²φ₃ = φ₁ R^{(â)}/12` (éq. 14). La réciprocité de Penrose `Ω̂Ω̌ = −1` est inchangée.

---

## 2. [B1] — Le fond anisotrope a un Weyl non nul, sourcé par le cisaillement `[établi]`

Compagnon : `verif_D1_bianchiA.py` [B1].

**(B1a) Kasner (Bianchi I vide), exposants (2/3, 2/3, −1/3).** Calcul symbolique direct du
Weyl (0,4) :

$$C_{txtx} = \frac{2}{9\,t^{2/3}} \neq 0,\qquad
E_{\hat x\hat x},E_{\hat y\hat y},E_{\hat z\hat z} = \Big(\tfrac{2}{9t^2},\tfrac{2}{9t^2},-\tfrac{4}{9t^2}\Big),\quad \mathrm{tr}\,E = 0.$$

Ceci **retrouve exactement** le sceau `verif_D1_stabilite` [B] (`C_{txtx}=2/(9t^{2/3})`), et
montre que la part **électrique** `E_ij` est non nulle et **sans trace** : une *marée pure
de cisaillement*, sans matière ni `Λ` (Kasner est le vide).

**(B1b) Décomposition électrique/magnétique (formules de Tod (21)-(22)).** Avec
`α̇+β̇+γ̇=0` :

- **Bianchi I** (`n_i=0` ⟹ `A=B=C=0`) : `B₁₁ = 0`, `E₁₁ ≠ 0` — Weyl **purement
  électrique** (marée), comme attendu d'un fond plat spatialement.
- **Bianchi IX** (`n_i=1` ⟹ `A,B,C ≠ 0`) : `B₁₁ = α̇(B+C) − β̇C − γ̇B ≠ 0` génériquement —
  une part **magnétique** du Weyl apparaît, *absente en FLRW*.

$$\boxed{\ \text{fond anisotrope} \Rightarrow C_{abcd}\neq 0\ (\text{E + B}),\ \text{sourcé par } \sigma_{ij}.\ }$$

**Lecture.** Là où `LC-A-D1-STABILITE-WEYL` §4 concluait « Weyl ≡ 0 en FLRW ⟹ D3 vacant
dans le secteur symétrique », ici **D3 a enfin un contenu**. Le secteur de marée (`g₃`)
n'est plus vide : c'est la précondition pour que la carte du crossover soit non triviale.

---

## 3. [B2] — La carte ĝ₃↦ǧ₃ devient inhomogène : le lemme [S4] tombe `[établi]`

C'est **le cœur**. Compagnon : `verif_D1_bianchiA.py` [B2].

**Le résultat de Tod, repris fidèlement (son éq. 33).** Dans le cas général, la matière
après le bang est, à l'ordre dominant `O(Ť⁻²)`, un fluide de radiation isotrope ; mais à
l'ordre suivant `O(Ť⁻¹)` apparaît un terme **sans trace** — un **cisaillement** :

$$\check\sigma_{ij} = -4\Big(R^{(\check a)}_{ij} - \tfrac13 R^{(\check a)}\,\check a_{ij}\Big)
\ \sim\ -4\Big(R^{(\hat a)}_{ij} - \tfrac13 R^{(\hat a)}\,\hat a_{ij}\Big).$$

Autrement dit : **la marée de l'éon futur est sourcée par le tenseur de Ricci sans-trace de
la 3-géométrie `â_ij` de 𝓘.** C'est précisément le pendant anisotrope du lemme [S4] : en
FLRW, `â_ij` est de courbure constante (Einstein 3D), son Ricci sans-trace est nul, et
`σ̌ = 0` (`0↦0`). Hors isotropie, le Ricci sans-trace est génériquement non nul.

**Sceau (3-Ricci de Milnor + Tod 33).** Pour une 3-géométrie de 𝓘 de type Bianchi IX avec
facteurs d'échelle `(e^ε, e^{−ε}, 1)` (volume gelé, `α₀+β₀+γ₀=0`, anisotropie `ε`) :

- **Auto-vérification `ε=0`** : la S³ ronde est **Einstein** (`Ric_{ii} = 1/(2a²)`,
  identiques) ⟹ Ricci sans-trace nul ⟹ `σ̌=0`. *On retrouve [S4].*
- **Anisotropie `ε≠0`** : développement propre

$$\boxed{\ |\check\sigma|^2(\varepsilon) = 16\,|S|^2 = 128\,\varepsilon^2 + O(\varepsilon^4)\ }$$

la marée future croît **quadratiquement** avec l'anisotropie, nulle uniquement à `ε=0`.
Valeurs propres `σ̌_{ii}` non nulles dès `ε≠0` (table dans le sceau).

$$\boxed{\ \hat g_3 = 0 \ \longmapsto\ \check g_3 = \check\sigma \neq 0\quad(\text{si } 𝓘 \text{ anisotrope}).\ }$$

**Le lemme [S4] tombe.** Un passé **sans marée propre** (`ĝ₃=0`, Weyl `→0` à 𝓘 — ce que la
construction de Tod garantit, `E_ij=O(τ̃²)`, `B_ij=O(τ̃³)`) **hérite quand même** d'une
marée future, sourcée par l'anisotropie *intrinsèque* de la 3-surface de raccordement. La
carte de réciprocité, multiplicative et homogène dans le cas FLRW ([S3]), acquiert une
**source additive** hors isotropie.

<svg width="100%" viewBox="0 0 680 300" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>La carte du crossover : 0↦0 en isotrope (S4 tient), 0↦≠0 en anisotrope (S4 tombe)</title>
  <desc>Comparaison des deux cas. À gauche, fond FLRW isotrope : le Ricci sans-trace de la 3-géométrie de I est nul, le lemme S4 tient, la carte du crossover envoie une marée passée nulle sur une marée future nulle (0 vers 0). À droite, fond Bianchi A anisotrope : le Ricci sans-trace de I est non nul, il source une marée future sigma-check égale à moins quatre fois ce Ricci sans-trace (équation 33 de Tod), de sorte qu'une marée passée nulle est envoyée sur une marée future non nulle (0 vers non-zéro). Le lemme S4 tombe.</desc>
  <rect x="28" y="44" width="300" height="226" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="178" y="70" text-anchor="middle" font-size="13.5" font-weight="500" fill="#0F6E56">FLRW isotrope (acquis : a1)</text>
  <text x="178" y="98" text-anchor="middle" font-size="12" fill="#3d3d3a">𝓘 à courbure constante (Einstein 3D)</text>
  <text x="178" y="120" text-anchor="middle" font-size="12" fill="#3d3d3a">Ricci sans-trace de 𝓘 = 0</text>
  <text x="178" y="150" text-anchor="middle" font-size="12.5" fill="#0F6E56">lemme [S4] : pas de source TT</text>
  <text x="178" y="186" text-anchor="middle" font-size="15" font-weight="600" fill="#0F6E56">ĝ₃ = 0  ↦  ǧ₃ = 0</text>
  <text x="178" y="212" text-anchor="middle" font-size="12" fill="#3d3d3a">carte multiplicative homogène ([S3])</text>
  <text x="178" y="246" text-anchor="middle" font-size="11.5" fill="#0F6E56">✓ « né dans le vide » tient</text>
  <rect x="352" y="44" width="300" height="226" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="502" y="70" text-anchor="middle" font-size="13.5" font-weight="500" fill="#993C1D">Bianchi A anisotrope (porte i)</text>
  <text x="502" y="98" text-anchor="middle" font-size="12" fill="#3d3d3a">𝓘 anisotrope (param. ε)</text>
  <text x="502" y="120" text-anchor="middle" font-size="12" fill="#A32D2D">Ricci sans-trace de 𝓘 ≠ 0</text>
  <text x="502" y="150" text-anchor="middle" font-size="12.5" fill="#A32D2D">σ̌ = −4(R^{(â)}_ij − ⅓R^{(â)}â_ij) [Tod 33]</text>
  <text x="502" y="186" text-anchor="middle" font-size="15" font-weight="600" fill="#A32D2D">ĝ₃ = 0  ↦  ǧ₃ = σ̌ ≠ 0</text>
  <text x="502" y="212" text-anchor="middle" font-size="12" fill="#3d3d3a">|σ̌|² = 128 ε² + O(ε⁴)</text>
  <text x="502" y="246" text-anchor="middle" font-size="11.5" fill="#A32D2D">✗ le lemme [S4] tombe</text>
  <text x="340" y="290" text-anchor="middle" font-size="11" fill="#3C3489">raccord continu : σ̌ → 0 quand ε → 0</text>
</svg>

*Fig. — En FLRW (vert) la carte est `0↦0` (lemme [S4]). En Bianchi A (rouge) la 3-géométrie
de 𝓘 a un Ricci sans-trace non nul qui source `σ̌` (Tod 33) : `0↦≠0`. Les deux cas se
raccordent continûment (`σ̌ ∝ ε`).*

---

## 4. [B3] — La back-réaction anisotrope injecte aussi une marée `[établi]`

Compagnon : `verif_D1_bianchiA.py` [B3]. Reprise de (a2) (`verif_D3_backreaction`) avec un
état **non dS-invariant**. L'intégrale angulaire isotrope `⟨k̂_i k̂_j⟩ = ⅓δ_ij` (qui
donnait `⟨g₃^{(2)}⟩ = 0`) est remplacée par une moyenne pondérée par une anisotropie
quadrupolaire `ε` (poids `1 + ε P₂(cosθ)`, plus bas multipôle traceless) :

$$\langle \hat k_i \hat k_j\rangle_\varepsilon = \mathrm{diag}\Big(\tfrac13-\tfrac{\varepsilon}{15},\ \tfrac13-\tfrac{\varepsilon}{15},\ \tfrac13+\tfrac{2\varepsilon}{15}\Big),\qquad
\langle g_3^{(2)}\rangle(\varepsilon) \propto \frac{\varepsilon}{15}(-1,-1,2)\neq 0.$$

La part traceless est non nulle dès `ε≠0` et `→0` quand `ε→0`. **Un état de raccordement
anisotrope injecte donc lui aussi une marée**, par back-réaction. Ceci lève la réserve
explicite de `verif_D3_backreaction` (l.144-146 : *« un état anisotrope donnerait
⟨k̂k̂⟩≠⅓δ ⟹ ⟨g₃^{(2)}⟩≠0 : c'est LA porte d'une marée »*).

---

## 5. Ce qui est décidable — et ce qui ne l'est pas `[établi / décision ouverte]`

**Décidable (cartographié ici).** `[établi — algèbre]`

- Le fond anisotrope a un Weyl ≠0 (E + B), sourcé par le cisaillement (§2).
- La marée future du crossover est `σ̌ = −4·(Ricci sans-trace de 𝓘)` (Tod 33) (§3).
- Donc : la carte `ĝ₃↦ǧ₃` est `0↦0` **ssi 𝓘 est Einstein 3D** (courbure constante) ;
  inhomogène (`0↦≠0`) sinon. Le lemme [S4] est un **cas particulier** (isotrope).
- La back-réaction anisotrope produit `⟨g₃^{(2)}⟩≠0` (§4).

**Non décidable ici (renvoyé).** `[décision ouverte]`

- *La sélection de la prescription* reste ouverte : on a cartographié la **forme** de la
  carte, pas élu un facteur conforme unique. (Comme `LC-07`, pas `LC-10`.)
- *Le sort du pivot A3* — l'anisotropie de `â_ij` est-elle **interdite** par la WCH (A4),
  ou est-elle une donnée libre admissible ? — est l'enjeu épistémique réel. Il est porté
  par le chaînon frère **`LC-D3-CROSSOVER-ANISOTROPE`**, qui en tire le verdict (issue
  faible). Ici on ne le tranche pas : on fournit seulement le **fait** que la carte est
  inhomogène hors isotropie.

---

## 6. Format de chaînon standard

- **Zone ambiguë.** « En FLRW la carte du crossover est forcée à `0↦0` ; mais le secteur
  symétrique est aveugle à D3 (Weyl≡0). Que devient la carte là où le Weyl existe ? »
- **Hypothèse de travail.** Sur un fond Bianchi A, le cisaillement source une structure TT
  qui peut rendre la carte `ĝ₃↦ǧ₃` inhomogène.
- **Outil.** Métrique et Weyl de Bianchi A (Tod éq. 18, 21-22) ; prescription du facteur
  conforme de Tod (éq. 12-14) ; matière post-bang et cisaillement (éq. 33) ; 3-Ricci par
  formule de Milnor (auto-vérifiée Einstein à `ε=0`). Sceau `verif_D1_bianchiA.py`.
- **Critère de réfutation de l'hypothèse.** Si, sur tout fond Bianchi A, la carte restait
  `0↦0` (pas de marée future hors isotropie), [S4] survivrait et le secteur anisotrope
  n'apporterait rien. — **Réfuté** : `σ̌ = −4·(Ricci sans-trace de 𝓘) ≠ 0` hors isotropie
  (Tod 33 ; sceau `|σ̌|²=128ε²+O(ε⁴)`).
- **Verdict.** **Carte inhomogène établie** hors isotropie ; lemme [S4] tombe. Étage
  **cartographie** (`LC-07`-like), non fermeture. La sélection et le sort de A3 restent
  ouverts. `[cartographie établie ; suite décision ouverte]`

---

## 7. Renvois, glossaire, références

**Renvois.** Parent `LC-A-D1-FACTEUR-CONFORME` (§4 table « Bianchi A », §4-bis atlas FLRW) ;
`LC-A-D1-STABILITE-WEYL` (Weyl FLRW≡0 vs Kasner≠0 — ce chaînon en est la suite
anisotrope) ; `LC-D3-CROSSOVER-MATCHING` (lemme [S4], carte `0↦0` en FLRW — ici levé) ;
`LC-D3-CROSSOVER-BACKREACTION` (a2 isotrope — ici étendu §4) ; `LC-A-SURVIE-CONFORME`
(`g₃` = Weyl rescalé) ; **frère : `LC-D3-CROSSOVER-ANISOTROPE`** (verdict A3⟸A4) ;
`LC-AUDIT-VERDICT` §5/§6.4, `LC-WORK-REPRISE-AUDIT` §3.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Bianchi A / classe A* : cosmologies homogènes anisotropes, constantes de structure
  unimodulaires `n_i∈{0,±1}` ; cisaillement `σ_ij` source un Weyl non nul.
- *Cisaillement `σ_ij`* : part sans-trace de l'expansion ; en CCC, sa trace dans la marée
  future est `σ̌ = −4·(Ricci sans-trace de 𝓘)` (Tod éq. 33).
- *Lemme [S4] (cas particulier isotrope)* : un fond Einstein-3D a un Ricci sans-trace nul,
  donc aucune source TT ⟹ `0↦0` ; tombe dès que 𝓘 est anisotrope.

**Références (`LC-04`) — à ajouter/préciser.**
- **K. P. Tod**, « The equations of CCC », *Gen. Rel. Grav.* **47**, 17 (2015) ;
  **arXiv:1309.7248v2** `[confirmé — texte intégral lu]`. Source de la métrique Bianchi A
  (éq. 18), du Weyl (éq. 21-22), de la prescription `φ` (éq. 12-14) et de la marée future
  (éq. 33). **Seule source de la prescription anisotrope** (Markwell–Stevens est FRW-only).
- **J. Milnor**, « Curvatures of left invariant metrics on Lie groups », *Adv. Math.* **21**,
  293-329 (1976) `[confirmé]` — 3-Ricci des métriques invariantes (formule du sceau [B2]).
- Kasner `[établi, manuel]` ; Penrose, *Cycles of Time* (2010) `[confirmé]`.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : un `établi` de sceau = « l'algèbre est correcte », jamais
« la physique est établie ».*
