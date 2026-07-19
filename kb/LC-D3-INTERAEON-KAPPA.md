---
id: LC-D3-INTERAEON-KAPPA
titre: "Front (a) — la carte d'anisotropie inter-éon ε_n↦ε_{n+1} : contractante (κ<1) à l'ordre dominant, mais faiblement pour un bang réaliste"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, isotropisation, inter-eon, bianchi-IX, wald, kappa, attracteur]
type: chaînon (résultat d'ordre dominant ; résout partiellement LC-D3-CROSSOVER-EINSTEIN3D §4)
statut: résultat d'ordre dominant établi (carte linéaire, κ≈0.81<1 : isotropisation dynamique inter-éon ; κ→1 pour bang radiation-dominé) ; convergence ∏κ_n CLOSE par LC-D3-INTERAEON-CONVERGENCE (∏κ_n→0 au point fixe Penrose) / valeur définitive (P7 fait) et complétude P6 à inventer
version: 0.2
langue: fr
date: 2026-06-07
maj: "2026-06-07 — v0.2 : §5 propagé depuis LC-D3-INTERAEON-CONVERGENCE (v0.2) et LC-D3-INTERAEON-MATIERE (P7). La convergence de ∏κ_n passe de `décision ouverte` à `établi (ordre dominant)` : sous Penrose (Λ const), l'atlas D1 force le point fixe ⟹ (ρ_0,Λ) éon-indépendants ⟹ κ constant ⟹ ∏κ_n=κⁿ→0 (isotropisation TOTALE dynamique, lente) ; les deux branches runaway sont Penrose-exclues et sans résiduel dans GO. P7 (matière) intégré : φ borné, σ̌ seul levier, ne renverse pas κ. Reste P6 (bang). v0.1 : carte contractante κ≈0.81<1, convergence en décision ouverte."
statut_id: provisoire — à enregistrer si validé (met à jour LC-D3-CROSSOVER-EINSTEIN3D §4 ; LC-02, LC-AUDIT-VERDICT §5/§8, glossaire)
fichier_compagnon: [verif_D3_interaeon_kappa.py, verif_D1_bianchiIX_domain.py, verif_D3_interaeon_convergence.py]
prerequis_kb: [LC-WORK-CADRAGE-INTERAEON, LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-D3-WCH-CANCELLATION, LC-AUDIT-VERDICT]
renvois: [LC-WORK-CADRAGE-INTERAEON, LC-D3-CROSSOVER-EINSTEIN3D, LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-D3-WCH-CANCELLATION, LC-AUDIT-VERDICT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] / front (a) — A3 est le pivot dont on teste l'isotropisation dynamique"
  - "[D3] hypothèse de Weyl — la marée g₃ ~ anisotropie de 𝓘"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Interaeon·κ — La carte d'anisotropie d'éon en éon

> **Cible.** `LC-D3-CROSSOVER-EINSTEIN3D` §4 avait laissé UNE frontière : *la carte
> d'anisotropie `ε_n ↦ ε_{n+1}` de 𝓘 d'éon en éon attire-t-elle vers `ε=0` ?* — seule route
> non postulée vers l'isotropie (A3), et seule forme licite restante de la porte (ii). Le
> cadrage (`LC-WORK-CADRAGE-INTERAEON`) l'a jugée `formalisable` à l'ordre dominant et a
> verrouillé les conditions GO. **Ce chaînon exécute le calcul.**
>
> **Verdict (résultat d'ordre dominant, établi ; sceau `verif_D3_interaeon_kappa.py`).**
> Sur Bianchi IX + radiation + Λ (variables expansion-normalisées, départ en ère de
> radiation, condition initiale de Tod : cisaillement cinétique nul au bang), la carte est
> **linéaire** et **contractante** : `ε_{n+1} = κ·ε_n` avec **`κ ≈ 0.81 < 1`** (robuste,
> `0.70–0.94` selon les paramètres). La courbure positive de S³ **rétrécit** la forme gelée
> de 𝓘 (vérifié : `|w|` baisse, direction quasi-conservée ; `Σ=σ/θ→0` Wald ; contrainte
> conservée `10⁻¹⁴`). Itérée, `ε_n ~ κⁿ ε_0 → 0` : **il EXISTE une isotropisation dynamique
> inter-éon — partielle.** *Nuance cruciale* : `κ → 1` quand la radiation domine
> (`ρ→∞` au bang réel de Tod) ⟹ l'isotropisation par éon est **réelle mais LENTE**. Donc
> l'issue faible (A3 non entraînée à UN crossover) **tient**, mais la dynamique inter-éon
> l'**adoucit** : ni issue forte (pas d'entraînement à éon fini), ni issue faible pure (il y
> a une attraction). **Milieu nuancé.** `[ordre dominant ; P6 bang/Mixmaster + P7 matière
> exacte exclus]`.

---

## 0. Rôle et garde-fou

Ce chaînon est le **premier résultat dynamique** du front (a) au-delà d'un crossover unique.
**Garde-fou `[à ne pas perdre]`** : `κ<1` est un résultat **d'ordre dominant** (Bianchi IX +
radiation + Λ ; P1-P5 du cadrage). Il **n'inclut pas** P6 (dynamique de bang/Mixmaster) ni
P7 (matière CCC exacte : `σ̌`, champ phantom, « DM » de Penrose). C'est donc une
**estimation**, pas la valeur définitive ; et un résultat *partiel* (κ<1 ne donne pas
l'isotropie à éon fini). On ne surclasse pas : « la dynamique adoucit l'issue faible »,
**pas** « A3 est dérivée ». Discipline d'audit (§6.4) maintenue.

---

## 1. Le calcul `[établi — algèbre]`

**Modèle.** Bianchi IX (`n_i=1`) + radiation + Λ. Forme log `w_i = ln A_i − ln a` (`Σw_i=0`),
cisaillement `σ_i = ẇ_i`, en temps e-fold `N = ln a` (expansion-normalisé) :

$$\frac{dw_i}{dN} = \frac{\sigma_i}{H},\quad
\frac{d\sigma_i}{dN} = -3\sigma_i - \frac{{}^3\!S_i}{H},\quad
\frac{dH}{dN} = \frac{-H^2 - \tfrac23\sigma^2 - \tfrac\rho3 + \tfrac\Lambda3}{H},\quad
\frac{d\rho}{dN} = -4\rho,$$

avec `³S_i = ³R_{ii} − ⅓³R` (courbure anisotrope, **source** du cisaillement ; `³R_{ii}` par
formule de Milnor, auto-vérifiée Einstein à `w=0`). Contrainte monitorée :
`3H² = ρ + Λ + σ² − ½³R` (conservée à `6·10⁻¹⁴` ⟹ signes mutuellement cohérents).

**Condition initiale (physiquement correcte, d'après Tod éq. 24).** Au bang,
`α = α₀ + α₁τ̃² + …` ⟹ le cisaillement **cinétique** `σ_i = ẇ_i ∝ τ̃ → 0`. L'anisotropie
est dans la **forme** (`w(0) = ε_n`), pas dans le cisaillement (`σ(0) = 0`). Le cisaillement
est **ensuite généré par la courbure** `³S`, et la forme gelée à 𝓘 donne `ε_{n+1}`.

**Conditions GO (verrouillées, `LC-WORK-CADRAGE-INTERAEON` §8).** Départ en ère de radiation
(`ρ ≫ ³R, Λ` : contourne le Mixmaster/P6) ; `Λ > 9/(64 ρ_r0)` (atteint 𝓘) ; `N=ln a` ;
solveur explicite DOP853.

---

## 2. Le résultat : carte contractante `[établi]`

- **Wald + gel.** `Σ = σ/θ : 0 → 6·10⁻²³` (isotropisation **cinétique**, Wald) ; la forme
  `|w|` **rétrécit** (`0.283 → 0.227` pour `ε_n=0.2`), direction quasi-conservée
  (`cos(w_0,w_∞) = 0.993`, rotation `~7°`) ⟹ **isotropisation géométrique réelle** (pas une
  rotation parasite).
- **Carte linéaire.** Balayage `ε_n ∈ [0.02, 0.2]` : `ε_{n+1}/ε_n` constant à `0.6 %` près.

$$\boxed{\ \varepsilon_{n+1} = \kappa\,\varepsilon_n,\qquad \kappa \approx 0.81 < 1\quad(\text{ordre dominant, } \rho_0{=}100,\ \Lambda{=}1).\ }$$

- **`κ < 1` robuste.** Sur tous les jeux testés, `κ ∈ [0.70, 0.94]` (toujours `<1`).

**Mécanisme.** La courbure **positive** de Bianchi IX (S³) a son potentiel minimal au rond
(`³R` maximal à l'isotropie, `LC-WORK-CADRAGE-INTERAEON` §8.1) : `³S` agit comme une force de
**rappel** qui contracte la forme pendant la fenêtre où la courbure est dynamiquement active
(radiation → Λ). C'est un effet **géométrique** (la fermeture spatiale), distinct du no-hair
cinétique de Wald.

<svg width="100%" viewBox="0 0 680 250" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Carte inter-éon contractante : ε_n = κⁿ ε_0 → 0, mais κ→1 (lent) pour bang réaliste</title>
  <desc>Deux courbes de décroissance géométrique de l'anisotropie ε en fonction du numéro d'éon n. Courbe 1 (κ=0.81, courbure significative) : décroissance rapide vers zéro. Courbe 2 (κ=0.97, bang radiation-dominé réaliste) : décroissance très lente. Les deux tendent vers zéro (isotropisation) mais à des rythmes très différents. Message : il y a contraction (κ<1) donc isotropisation multi-éon, mais lente pour un bang réaliste.</desc>
  <line x1="60" y1="205" x2="640" y2="205" stroke="#3d3d3a" stroke-width="1"/>
  <line x1="60" y1="205" x2="60" y2="30" stroke="#3d3d3a" stroke-width="1"/>
  <text x="350" y="235" text-anchor="middle" font-size="12" fill="#3d3d3a">numéro d'éon n</text>
  <text x="20" y="120" text-anchor="middle" font-size="12" fill="#3d3d3a" transform="rotate(-90 20 120)">anisotropie ε_n</text>
  <!-- kappa=0.81 curve -->
  <polyline fill="none" stroke="#1D9E75" stroke-width="2.2"
    points="60,40 110,73 160,100 210,121 260,138 310,151 360,162 410,170 460,177 510,182 560,186 610,189"/>
  <text x="250" y="115" font-size="11.5" fill="#0F6E56">κ ≈ 0.81 (courbure significative) — contraction nette</text>
  <!-- kappa=0.97 curve -->
  <polyline fill="none" stroke="#A32D2D" stroke-width="2.2" stroke-dasharray="6 3"
    points="60,40 110,45 160,49 210,54 260,58 310,62 360,66 410,70 460,73 510,77 560,80 610,83"/>
  <text x="370" y="55" font-size="11.5" fill="#A32D2D">κ ≈ 0.97 (bang radiation-dominé réaliste) — contraction LENTE</text>
  <circle cx="60" cy="40" r="3" fill="#3C3489"/>
  <text x="60" y="30" text-anchor="middle" font-size="11" fill="#3C3489">ε_0</text>
  <text x="350" y="120" text-anchor="middle" font-size="10.5" fill="#3d3d3a">ε_n = κⁿ ε_0 → 0 (toujours, car κ&lt;1)</text>
</svg>

*Fig. — La carte contracte (`κ<1`) donc `ε_n = κⁿ ε_0 → 0` : isotropisation multi-éon. Mais
`κ→1` pour un bang radiation-dominé (réaliste) ⟹ contraction lente (courbe rouge).*

---

## 3. La nuance : `κ → 1` pour un bang réaliste `[établi — robustesse]`

`κ` dépend de la **signifiance de la courbure** dans l'histoire (rapport `Λ/ρ_0`) :

| `Λ/ρ_0` | `κ` | lecture |
|---|---|---|
| `0.0333` (ρ₀=30, près du seuil) | `0.70` | courbure très active → contraction forte |
| `0.0100` (ρ₀=100) | `0.82` | — |
| `0.0010` (ρ₀=1000, radiation dominante) | `0.94` | courbure réprimée → contraction faible |

**Tendance décisive.** Plus la radiation domine (`ρ_0` grand), plus `³R` est réprimée, plus
`κ → 1`. Or le **bang réel de Tod** a `ρ ∝ Ť⁻² → ∞` (éq. 27) : radiation **ultra-dominante**
⟹ `κ` **très proche de 1**. L'isotropisation par éon est donc **réelle mais lente**. (Note :
si la courbure dominait — `Λ < Λ_crit ~ ³R²/ρ_0` — l'univers **recollapserait** au lieu
d'atteindre 𝓘 : `LC-WORK-CADRAGE-INTERAEON` §8.1. Donc dans le régime qui atteint 𝓘, la
courbure est toujours sous-dominante, et `κ<1` mais proche de 1.)

---

## 4. Verdict épistémique — un milieu nuancé `[établi (ordre dominant) / reste P6]`

Confronté aux trois issues de la porte (i) (`LC-D3-CROSSOVER-ANISOTROPE` §2) :

- **L'issue faible TIENT** au niveau d'**un** crossover : A3 n'est pas entraînée par
  A4+régularité (`LC-D3-CROSSOVER-EINSTEIN3D` reste valide ; `κ` n'est pas `0`).
- **Mais la dynamique inter-éon l'ADOUCIT** : `κ<1` ⟹ `ε_n → 0` sur plusieurs éons. Il y a
  une **attraction dynamique vers l'isotropie** (A3), absente du verdict single-crossover.
  C'est un **argument nouveau et positif** pour la CCC.
- **Ce n'est PAS l'issue forte** : pas d'entraînement à éon fini ; et la contraction est
  **lente** pour un bang réaliste (`κ→1`).

$$\boxed{\ \text{A3 n'est pas } \textit{dérivée}, \text{ mais elle est } \textit{dynamiquement attirée} \text{ : } \varepsilon_n = \kappa^n\varepsilon_0 \to 0,\ \kappa<1\ \text{(lent si } \rho\to\infty).\ }$$

**Mise à jour de `LC-D3-CROSSOVER-EINSTEIN3D` §4.** La frontière passe de `décision ouverte`
à **`établi (ordre dominant) : carte contractante κ<1, isotropisation multi-éon`**. La porte
(ii), sous sa seule forme licite (carte inter-éon), est **franchie** : elle contracte, et la
convergence `∏κ_n→0` (isotropisation **totale** dynamique sous Penrose) est désormais close par
`LC-D3-INTERAEON-CONVERGENCE` `[v0.2]` — sans pour autant fermer A3 à éon fini (l'attraction
est multi-éon et lente). Reste P6 pour la complétude à travers le bang.

---

## 5. Réserves et ce qui closerait le point `[à inventer — réduit à P6]`

- **P6 (bang/Mixmaster) exclu** : départ en ère de radiation. Le passage à travers le bang
  pourrait ajouter des bonds (anisotropie transitoire) ; à tester (lourd, chaotique).
  **C'est le seul chantier restant du front (a).**
- **P7 (matière CCC exacte) — FAIT** `[v0.2]` : `LC-D3-INTERAEON-MATIERE` a montré que `φ` est
  borné (isotrope, ne source pas le cisaillement), que `σ̌` est le seul levier, et que le sort
  de `κ` se réduit à 2 paramètres (signe de σ̌ — résolu — et exposant `p`). La matière **ne
  renverse pas** `κ<1`.
- **La suite `(ρ_0, Λ)` et la convergence `∏κ_n` — CLOSES** `[v0.2]` :
  `LC-D3-INTERAEON-CONVERGENCE` (sceau `verif_D3_interaeon_convergence.py`) couple cette carte à
  la récurrence `(m,λ)` de l'atlas D1. Sous Penrose (Λ const), l'atlas force le **point fixe**
  `mλ=9k²/4` ⟹ `(ρ_0,Λ)` éon-indépendants ⟹ `κ` **constant** ⟹ **`∏κ_n=κⁿ→0`** :
  isotropisation **TOTALE dynamique multi-éon** (lente). Les deux branches runaway (`Λ→∞` et
  `Λ→0`) sont Penrose-exclues **et** sans résiduel dans le domaine GO. La convergence passe donc
  de `décision ouverte` à **`établi (ordre dominant)`**.

**Pour clore.** (i) ✓ brancher la matière P7 (`LC-D3-INTERAEON-MATIERE`) ; (ii) ✓ itérer la
carte sur la suite `(ρ_0,Λ)` auto-cohérente (`LC-D3-INTERAEON-CONVERGENCE`) ; (iii) **reste** :
intégrer **P6** (bang) pour un Bianchi IX complet à travers le crossover. Ce chaînon donne le
**squelette et le signe (contraction)** ; P7 et l'itération sont faits ; **P6 est le dernier
chantier.**

---

## 6. Format de chaînon standard

- **Zone ambiguë.** « La porte (ii) (attracteur) est caduque sous sa forme `g₃=0` ; sa seule
  forme licite est la carte inter-éon — contracte-t-elle ? »
- **Hypothèse testée.** `ε_n ↦ ε_{n+1}` attire vers `ε=0`.
- **Outil.** ODE de Bianchi IX + radiation + Λ (Wainwright-Ellis) ; 3-Ricci de Milnor ;
  données de bang de Tod (σ cinétique nul) ; intégration expansion-normalisée. Sceaux
  `verif_D3_interaeon_kappa.py` (+ `verif_D1_bianchiIX_domain.py` pour le domaine GO).
- **Critère de réfutation.** Si `κ ≥ 1`, aucune isotropisation (issue faible pure / runaway).
  — **Non réalisé** : `κ ≈ 0.81 < 1` (robuste). Mais `κ→1` (lent) tempère.
- **Verdict.** **Carte contractante `κ<1`** (ordre dominant) : isotropisation dynamique
  inter-éon, **convergence `∏κ_n→0` close** (`LC-D3-INTERAEON-CONVERGENCE`, totale sous Penrose,
  lente) ; issue faible adoucie, non renversée. `[établi (ordre dominant) ; reste P6]`

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-WORK-CADRAGE-INTERAEON` (cadrage + verrou GO, dont ce chaînon est
l'exécution) ; **met à jour `LC-D3-CROSSOVER-EINSTEIN3D` §4** (la frontière) ;
`LC-D3-CROSSOVER-ANISOTROPE` (issue faible, §2 les trois issues) ; `LC-A-D1-BIANCHI`
(données de bang, Tod) ; `LC-A-D1-FACTEUR-CONFORME` §4-bis (runaway `(m,λ)` — l'analogue
isotrope de cette carte) ; `LC-D3-WCH-CANCELLATION` (no-hair cinétique vs forme gelée) ;
`LC-AUDIT-VERDICT` §5/§8.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Carte inter-éon `ε_n↦ε_{n+1}`* : transformation de l'anisotropie de 𝓘 d'un éon à l'autre ;
  linéaire à petit ε, pente `κ`.
- *`κ` (taux d'isotropisation inter-éon)* : `κ<1` ⟹ contraction (`ε_n=κⁿε_0→0`) ; `κ→1` pour
  bang radiation-dominé (lent) ; ordre dominant `≈0.81`.
- *Isotropisation dynamique inter-éon (porte ii licite)* : la courbure S³ contracte la forme
  gelée ; partielle ; adoucit l'issue faible sans dériver A3.

**Références (`LC-04`).**
- **R. M. Wald**, *Phys. Rev. D* **28**, 2118 (1983) — no-hair (isotropisation cinétique).
- **J. Wainwright & G. F. R. Ellis**, *Dynamical Systems in Cosmology*, CUP (1997) — ODE de
  Bianchi, variables expansion-normalisées.
- **K. P. Tod**, arXiv:1309.7248 (2015) — données de bang (éq. 24, 27 : `σ` cinétique nul,
  `ρ∝Ť⁻²`).
- **J. Milnor**, *Adv. Math.* **21** (1976) — 3-Ricci des métriques invariantes.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : `établi` porte sur l'ALGÈBRE (carte linéaire, `κ<1`,
contrainte conservée), à l'ORDRE DOMINANT ; la valeur exacte de `κ` et la complétude
multi-éon (P6, P7) restent `à inventer`. Jamais « la physique de la CCC est établie ».*
