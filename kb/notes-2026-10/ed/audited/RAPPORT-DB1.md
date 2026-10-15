# RAPPORT DB-1 : dérivation en cécité stricte

Consigne : `PROMPT-AVEUGLE-DB1.md`. Protocole respecté : aucun autre fichier de /home/claude lu, aucun document de projet, aucune recherche web. Tout est dérivé de zéro et vérifié en sympy 1.14 dans `/tmp/claude-0/db1/` :

| script | objet | sortie |
|---|---|---|
| `q1_dirac.py` | connexion de spin, covariance de Dirac, identité T^ = Ω² T_r, traces, lagrangien | console (reproduite au §1) |
| `q2_orders.py` (+ `common_jets.py`) | ordres en Ω des quatre termes de Friedrich, hors couche, sur couche, forme « cinétique − g^ Lag » | `q2.out` |
| `q4_scalar.py` | scalaire minimal, terme d'ordre Ω⁰, coefficients Ω⁻², Ω⁻¹ du terme de Cotton | `q4.out` |
| `q4_indices.py` | exposants indiciels près de 𝓘 sur de Sitter exact | console |
| `q5_wkb.py`, `q5_dust.py` | partie singulière de ∇ψ_r imposée par l'équation de Dirac ; forme « poussière » de T_r ; compensation dans le terme de Cotton | console, `q5.out` |

Méthode pour les ordres en Ω : calcul en un point, en coordonnées normales de g (Γ_g = 0 au point, ce qui suffit puisque les seconds membres ne contiennent au plus que des dérivées premières de T^, donc pas de ∂Γ_g), avec des jets polynomiaux Ω = w + p·x + ½ x·q·x et des tenseurs génériques. L'ordre minimal en w = Ω(point) est lu sur la fraction rationnelle obtenue. Les Christoffel de g^ = Ω⁻²g sont pris sous la forme analytique Γ^ᵃ_bc − Γᵃ_bc = −Ω⁻¹(δᵃ_b ∂_cΩ + δᵃ_c ∂_bΩ − g_bc ∇ᵃΩ), vérifiée contre la définition.

Conventions. Q1 et Q3 (algèbre de Clifford) : signature (+,−,−,−), {γᵃ,γᵇ} = 2ηᵃᵇ, iγ^μ∇_μψ = mψ. Q2, Q4, Q5 (géométrie) : signature (−,+,+,+), seule compatible avec le Schouten de l'énoncé (vide : L^ = (λ/6)g^ ⇒ R^_μν = λ g^_μν, R^ = 4λ > 0 en de Sitter). Les lois d'échelle en Ω ne dépendent pas de la signature ; quand un signe en dépend, il est écrit via la quantité Θ := Ω·tr_g T_r, qui vaut ±mψ̄_rψ_r selon la signature.

Notations : ψ_r = Ω^{-3/2}ψ, T_r := T[ψ_r, g], τ_r := tr_g T_r, S := ψ̄_rψ_r, H := √(λ/3).

---

## Q1. Connexion de spin et identité T^ = Ω² T_r

### 1.1 Fixation de la connexion de spin

Ansatz le plus général linéaire en ∂Ω (g plate, γ_μ plats) :

  Γ^_μ = c₁ Ω⁻¹ γ_μ γ^ν ∂_νΩ + c₂ Ω⁻¹ ∂_μΩ · 𝟙,  avec γ^^μ = Ω γ^μ, γ^_μ = Ω⁻¹ γ_μ, ψ^ = Ω^{3/2} ψ_r.

Résultats sympy :

| condition imposée | contrainte obtenue |
|---|---|
| covariance de Dirac sans masse : D^(Ω^{3/2}ψ_r) = Ω^{5/2} Dψ_r pour tout ψ_r | 8c₁ + 2c₂ + 3 = 0 (une seule équation) |
| compatibilité ∇^_μ γ^^ν = 0 | c₁ = −1/2 (c₂ libre : partie U(1)) |
| les deux ensemble | c₁ = −1/2, c₂ = +1/2 |

D'où, de façon unique :

  **Γ^_μ = −(1/2) Ω⁻¹ (γ_μγ^ν − δ_μ^ν) ∂_νΩ = −(1/4) Ω⁻¹ [γ_μ, γ^ν] ∂_νΩ**

(c'est (1/4)[γ_μ,γ^ν]∂_νσ avec e^σ = Ω⁻¹ ; la condition c₁ + c₂ = 0 est exactement l'appartenance à so(1,3)). La covariance seule ne suffit pas : elle laisse une droite de solutions, la compatibilité tranche.

### 1.2 Identité hors couche

Avec T_μν = (i/4)(ψ̄γ_μ∇_νψ + ψ̄γ_ν∇_μψ − c.c.), pour g plate, Ω(x) arbitraire et ψ_r (8 fonctions réelles arbitraires) :

  **T^_μν[ψ^, g^] − Ω² T_μν[ψ_r, g] = 0  identiquement (hors couche)** ✔

Mécanisme (vérifié aussi par contre-tests) :
* le terme de poids (3/2)Ω⁻¹∂_νΩ ψ_r donne ψ̄_rγ_μψ_r ∂_νΩ, bilinéaire réel, éliminé par « − c.c. » ;
* le terme de connexion, symétrisé en (μν), se réduit à des courants vectoriels réels (la partie γ_[μγ_νγ_ρ] disparaît par symétrisation), éliminés de même ;
* il reste le facteur Ω^{2w}·Ω⁻¹ (γ^_μ = Ω⁻¹γ_μ). Contre-test : avec un poids w = 1 au lieu de 3/2, sympy donne exactement T^ = Ω T_r. En général **T^ = Ω^{2w−1} T_r** : l'identité ne « voit » pas le poids autrement que par la puissance ; c'est la covariance de l'opérateur de Dirac qui impose w = 3/2, donc Ω².
* contre-test : une partie U(1) réelle parasite (c₁,c₂) = (−1/4,−1/2), covariante mais hors so(1,3), laisse aussi T inchangé (même mécanisme : bilinéaire réel).

Traces et lagrangien (vérifiés) :

  tr_{g^} T^ = Ω⁴ τ_r,  τ_r = (i/2)(ψ̄_r γ^μ∇_μψ_r − c.c.)  (hors couche)

  Lag^ = Ω⁴ [ (i/2)(ψ̄_r γ^μ∇_μψ_r − c.c.) − (m/Ω) ψ̄_rψ_r ]   (voir Q3)

**Réponse Q1 : oui.** T^_μν = Ω² T_μν[ψ_r, g] est une identité hors couche, valable pour toute masse (la masse n'apparaît pas dans le tenseur cinétique).

---

## Q2. Ordres en Ω et rôle de la masse

### 2.1 Hors couche (T_r régulier quelconque, T^ = Ω²T_r)

| terme | expression exacte | ordre (sympy) |
|---|---|---|
| tr T^ | Ω⁴ τ_r | Ω⁴ |
| Ω T*_μν | Ω³ T*_r,μν (T*_r sans trace) | Ω³ |
| Ω⁻¹ ∇_μ tr T^ | Ω²(4τ_r ∇_μΩ + Ω ∇_μτ_r) | Ω² |
| 2Ω⁻¹∇^_[ν L^_λ]ρ | voir ci-dessous | **Ω⁰** |

Décomposition explicite du terme de Cotton, avec L^ = (κ/2)T^* − (κ/24) trT^ g^ + (λ/6)g^ (le terme λ disparaît car ∇^g^ = 0) :

  2Ω⁻¹∇^_[νL^_λ]ρ = (κ/2)[ Ω·2∇_[νT*_λ]ρ + 3(∇_νΩ T*_λρ − ∇_λΩ T*_νρ) − (g_νρ ∇^σΩ T*_λσ − g_λρ ∇^σΩ T*_νσ) ]
            − (κ/24) Ω⁻³ (g_λρ ∂_ν − g_νρ ∂_λ)(Ω⁴ τ_r)

et le dernier morceau vaut −(κ/24)(g_λρ∂_ν − g_νρ∂_λ)-appliqué à Ω⁴τ_r divisé par Ω³, soit −(κ/6)τ_r(g_λρ∇_νΩ − g_νρ∇_λΩ) − (κ/24)Ω(g_λρ∇_ντ_r − g_νρ∇_λτ_r).

**Conclusion hors couche : les quatre termes sont formellement réguliers, pour toute masse.** La masse n'entre pas dans T.

Remarque structurelle importante : le terme de trace du Cotton s'écrit −(κ/24)·Ω⁻²·(g ∧ [Ω⁻¹∇ trT^]). Le terme « Ω⁻¹∇ trT^ » de la liste est régulier dès que trT^ = O(Ω), mais il apparaît dans le Cotton multiplié par g^ = Ω⁻²g. **La régularité exige donc tr T^ = O(Ω⁴)**, pas seulement O(Ω).

### 2.2 Où entre la masse

Uniquement par l'équation de matière. Rescalée :

  iγ^μ∇_μψ_r = (m/Ω) ψ_r   (exact, conséquence de la covariance de D et de ψ^ = Ω^{3/2}ψ_r)

qui n'est pas formellement régulière pour m ≠ 0. Conséquence sur la trace (identité de couche) :

  τ_r = Ω⁻¹ m ψ̄_rψ_r  ⇔  tr T^ = m ψ^̄ψ^ = m Ω³ ψ̄_rψ_r.

La trace n'est plus O(Ω⁴) mais O(Ω³), ce qui casse exactement la condition du §2.1.

### 2.3 Sur couche (substitution de la trace, T*_r gardé régulier)

| terme | ordre (sympy) | expression |
|---|---|---|
| tr T^ | Ω³ | m Ω³ S |
| Ω T* | Ω³ | Ω³ T*_r |
| Ω⁻¹∇ tr T^ | Ω¹ | m(3Ω ∇Ω S + Ω² ∇S) |
| 2Ω⁻¹∇^_[νL^_λ]ρ | **Ω⁻¹** | voir ci-dessous |

Coefficient singulier (vérifié composante par composante) :

  **2Ω⁻¹∇^_[νL^_λ]ρ = −(κ/8) Ω⁻¹ (g_λρ ∇_νΩ − g_νρ ∇_λΩ) Θ + O(Ω⁰),  Θ = Ω τ_r = m ψ̄_rψ_r**

(signe de Θ selon la signature ; dans le calcul (−,+,+,+) avec τ_r = +mS/Ω on obtient −κ m S/8 exactement). Comme ∇Ω ≠ 0 sur 𝓘, ce terme est génériquement non nul. Il est **purement dans le canal de trace** : il vient de −(κ/24) trT^ g^ dans L^, et vaut −(κ/24)Ω⁻³(g∧∂)(mΩ³S) = −(κ m/8)Ω⁻¹ S (g∧∇Ω) + régulier.

Décomposition qui justifie que T*_r est « régulier » dans ce bilan : l'équation de Dirac fixe γ^μ∇_μψ_r, donc ∇_μψ_r = φ_μ − (i m/4)Ω⁻¹ γ_μψ_r avec γ^μφ_μ = 0, et la partie Ω⁻¹ de T_r est alors purement de trace : (m/4)Ω⁻¹ S g_μν. (Mais voir §5.2 : sur les vraies solutions, φ_μ lui-même n'est pas borné.)

**Réponse Q2 :** ordres Ω⁴, Ω³, Ω², Ω⁰ hors couche ; les équations géométriques sont formellement régulières pour toute masse *en tant que fonctions de (ψ_r, ∇ψ_r, ∇∇ψ_r)*, car T est cinétique pur. La masse entre par l'équation de Dirac rescalée (terme m/Ω) et, via l'identité de couche tr T^ = m ψ^̄ψ^, par la trace, qui tombe de O(Ω⁴) à O(Ω³) et produit un terme Ω⁻¹ dans le canal trace du Cotton.

---

## Q3. Forme « cinétique − g^ Lag »

Calcul exact (sympy) :

  **Lag^ = Ω⁴ Lag_r^{(m/Ω)},  Lag_r^{(m/Ω)} = (i/2)(ψ̄_r γ^μ∇_μψ_r − c.c.) − (m/Ω) ψ̄_rψ_r**

c'est-à-dire le lagrangien de Dirac sur (g, ψ_r) **avec une masse effective m/Ω**, qui diverge sur 𝓘. Alors

  T^ = T^_kin − g^ Lag^ = Ω² [ T_r,kin − g Lag_r^{(m/Ω)} ] = Ω² [ T_r,kin − τ_r g + (m/Ω) S g ].

Conséquences (sympy, cas (C) de `q2.out`, τ_r traité comme indépendant) : tr T^ = Ω⁴(−3τ_r + 4mS/Ω) d'ordre Ω³ avec m explicite, Ω⁻¹∇trT^ d'ordre Ω¹, Cotton d'ordre **Ω⁻¹ hors couche**. La masse, absente de T_kin, est déplacée de l'équation du mouvement vers le tenseur lui-même : l'irrégularité devient manifeste hors couche (terme explicite (m/Ω)S g, pure trace). Sur couche Lag = 0 et les deux formes coïncident ; ajouter « −g^ Lag » ne crée ni ne supprime la singularité, il la rend visible sans avoir à invoquer l'équation de Dirac.

**Réponse Q3 :** Lag = Ω⁴[(i/2)(ψ̄_rγ^μ∇_μψ_r − c.c.) − mΩ⁻¹ψ̄_rψ_r] ; la forme « cinétique − g^Lag » rend la singularité explicite hors couche, sous la forme d'un terme de trace (m/Ω)ψ̄_rψ_r g_μν dans T_r.

---

## Q4. Comparaison avec le scalaire massif minimal (φ^ = Ωφ)

T^ = ∇φ^⊗∇φ^ − g^(½|∇φ^|²_{g^} + ½m²φ^²), signature (−,+,+,+).

### 4.1 Le terme d'ordre Ω⁰

∇φ^ = Ω∇φ + φ∇Ω contient φ∇Ω d'ordre Ω⁰, et g^·m²φ^² = Ω⁻²g·Ω²m²φ² est d'ordre Ω⁰. Vérifié :

  **T^_μν = φ² [ ∇_μΩ∇_νΩ − ½ g_μν(|∇Ω|²_g + m²) ] + O(Ω)**,  alors que tr T^ = O(Ω²).

Comparaison avec Dirac :

```
                Dirac (w = 3/2)                    Scalaire minimal (w = 1)
terme de poids  (3/2)Ω⁻¹∇Ω ψ  -> ψ̄γψ réel -> 0     φ∇Ω  -> survit dans ∇φ^⊗∇φ^
masse dans T    absente (T cinétique pur)          ½ m² φ^² g^  ~ Ω⁰
T^              Ω² T_r  (exact, hors couche)       Ω⁰ : φ²(∇Ω∇Ω − ½g(|∇Ω|²+m²))
masse entre par trace sur couche, linéaire en m     T^ lui-même, quadratique en m
```

### 4.2 Coefficients singuliers et masse spéciale

Coefficient Ω⁻² du terme de Cotton (sympy, général) :

  **2Ω⁻¹∇^_[νL^_λ]ρ ⊃ (κφ²/3)(|∇Ω|² + m²/2)(g_λρ∇_νΩ − g_νρ∇_λΩ) Ω⁻²**

Sur 𝓘, la contrainte de Friedrich (dérivée de R^ = 24Ωs − 12|∇Ω|² = 4λ − κ trT^) donne |∇Ω|² = 2Ωs − λ/3 + (κ/12)trT^ = −λ/3 + O(Ω). Le coefficient vaut donc (κφ²/6)(m² − 2λ/3). Avec en plus ∇_μ∇_νΩ = s g_μν + O(Ω), sympy donne pour m² = 2λ/3 : **coefficients Ω⁻² et Ω⁻¹ tous deux nuls, hors couche** (sans utiliser l'équation d'onde). Pour m² générique : coefficient Ω⁻² = √3 κ√λ φ²(3m² − 2λ)/54 dans la composante (0,1,1) du repère adapté.

Équation de champ : (□^ − R^/6)(Ωφ) = Ω³(□ − R/6)φ, donc

  (□^ − m²)φ^ = Ω³[(□ − R/6)φ + Ω⁻²(R^/6 − m²)φ],  R^ = 4λ + O(Ω²),

régulière ssi m² = 2λ/3 = 2H². Exposants indiciels sur de Sitter exact (`q4_indices.py`) : φ^ ~ Ω^Δ, Δ(3 − Δ) = m²/H². Pour m² = 2H² : Δ = 1, 2, donc φ_r ~ Ω⁰, Ω¹, lisse.

### 4.3 Pourquoi pas de masse spéciale pour Dirac

Trois arguments convergents :

1. **Parité de Clifford.** Le changement de poids sur un spineur donne D^(Ω^w ψ) = Ω^{w+1}[Dψ + (w − 3/2)Ω⁻¹ γ^μ∇_μΩ ψ] : le seul terme d'ordre zéro que la géométrie engendre est Clifford-impair (∝ γ·∇Ω), et il est nul au poids conforme w = 3/2 (D est exactement covariant, sans terme de courbure, contrairement à □ qui exige le −R/6). La masse est Clifford-paire (∝ 𝟙). Rien ne peut la compenser. Pour le scalaire, la courbure R^/6 ⊃ −2Ω⁻²|∇Ω|² → (2λ/3) est un terme scalaire d'ordre zéro du même type que m² : on peut les égaler.
2. **Exposants indiciels.** Le coefficient singulier de l'équation rescalée au poids w est la matrice i(w − 3/2)γ·∇Ω − m, dont les valeurs propres ±i(w − 3/2)H − m ne s'annulent que pour **w = 3/2 ∓ i m/H** (vérifié : ψ_r ~ Ω^{∓ i m/H} selon la valeur propre ±1 de γ^0 sur de Sitter, résidu nul). Une masse « absorbable » demande un poids conforme complexe ; pour un poids réel, m = 0. Pour le scalaire, Δ = 3/2 ± √(9/4 − m²/H²) est réel et entier pour m² = 2H².
3. **Structure de T.** La compensation scalaire met en jeu deux termes Ω⁰ de T^, quadratiques : m² et |∇Ω|² = −λ/3. Chez Dirac, T^ = Ω²T_r ne contient aucun terme de type |∇Ω|², et la masse n'apparaît que linéairement via la trace ; il n'existe pas de partenaire géométrique de dimension 1 (λ entre par λ, jamais par √λ).

**Réponse Q4 :** le terme d'ordre Ω⁰ est φ²[∇Ω⊗∇Ω − ½g(|∇Ω|² + m²)] (gradient du facteur conforme et terme de masse) ; il produit un Ω⁻² dans le Cotton de coefficient (κφ²/3)(|∇Ω|² + m²/2) → (κφ²/6)(m² − 2λ/3). La masse spéciale existe pour le scalaire parce que m² et la courbure conforme R^/6 = 2λ/3 sont de même nature (scalaires, d'ordre zéro, réels) ; pour Dirac l'opérateur est conforme sans terme de courbure, la seule correction géométrique est Clifford-impaire, et l'exposant indiciel 3/2 ∓ im/H est complexe pour tout m ≠ 0.

---

## Q5. Localisation de la singularité Einstein-Dirac et condition sur m

### 5.1 Bilan formel (critère de Friedrich)

```
            hors couche                 sur couche (trace substituée)
tr T^        Ω⁴ τ_r          ──m──►     m Ω³ ψ̄ψ           (régulier)
Ω T*         Ω³ T*_r                    Ω³ T*_r            (régulier)
Ω⁻¹∇trT^     Ω²                         m Ω (…)            (régulier)
Cotton       Ω⁰                         −(κm/8) Ω⁻¹ (g∧∇Ω) ψ̄ψ   ◄── seul terme géométrique singulier
Dirac        (sans objet)               iγ∇ψ_r = (m/Ω) ψ_r  ◄── source
```

La singularité est **dans l'équation de matière** (m/Ω) et se transmet aux équations géométriques **par le seul canal de trace du terme de Cotton** 2Ω⁻¹∇^_[νL^_λ]ρ, via le morceau −(κ/24)trT^ g^ du Schouten. Critère compact : régularité ⇔ tr T^ = O(Ω⁴) ⇔ Ω⁻¹·(Ω τ_r) borné.

### 5.2 Ce que donnent les vraies solutions (au-delà de la question, mais nécessaire pour conclure honnêtement)

L'équation de Dirac rescalée impose une partie singulière de ∇ψ_r **dirigée selon ∇Ω** (analyse de type Fuchs/WKB) :

  ∇_μψ_r = −i (m/Ω) ∇_μΩ (γ·∇Ω)⁻¹ ψ_r + χ_μ,  γ^μχ_μ = 0.

Vérifié (`q5_wkb.py`) : cette partie satisfait seule l'équation de Dirac, et elle donne

  **T_r^sing = (m/Ω) ψ̄_rψ_r u_μu_ν,  u = ∇Ω/|∇Ω|**  (poussière comobile, T^_sing = mΩ ψ̄_rψ_r u⊗u, densité physique m·n^ avec n^ = Ω³ψ̄_rψ_r ∝ a⁻³).

Sa partie sans trace n'est donc pas bornée, et dans le Cotton elle contribue un Ω⁻¹ **exactement opposé** à celui du canal trace (sympy, `q5.out`, composantes (0,1,1) et (1,2,2) : sans trace −κmSp/8, trace +κmSp/8 ; ordre total Ω⁰ pour la poussière seule ; le terme de Cotton étant linéaire en T, poussière + T_r régulier reste d'ordre Ω⁰ par le cas hors couche du §2.1). Autrement dit :

* le Ω⁻¹ du §2.3 est réel au niveau formel (système fermé avec l'équation de Dirac et T*_r supposé borné), mais **il est compensé sur les solutions** dont la partie singulière est la poussière comobile ;
* ce qui reste n'est pas une puissance négative mais un **défaut de lissité** : ψ_r ~ Ω^{∓ i m/H} (exposants 3/2 ∓ im/H pour ψ^), donc oscillation log-périodique bornée, ∂_Ωψ_r ~ Ω⁻¹ ; les bilinéaires mélangeant les deux espaces propres de γ·u (par exemple ψ̄γ^jψ, j spatial) portent Ω^{±2im/H}. Les seconds membres sont bornés mais ni C¹ ni analytiques en Ω = 0 : aucune extension lisse à travers 𝓘.

(Limite : la compensation est démontrée pour la partie singulière dominante ; la régularité des restes χ_μ, bornés mais oscillants, est argumentée et non prouvée en toute généralité.)

### 5.3 Condition sur m

La singularité (formelle et de lissité) disparaît si et seulement si m/Ω est une fonction lisse jusqu'à 𝓘 et au-delà :

  **m(x) = Ω μ(x), μ lisse**  ⇒  iγ^μ∇_μψ_r = μ ψ_r (régulière), tr T^ = Ω⁴ μ S = O(Ω⁴), Cotton O(Ω⁰), exposants indiciels réels (m/H → 0 sur 𝓘).

* Masse constante m ≠ 0 : jamais régulier, quelle que soit la valeur de m (pas d'analogue de m² = 2λ/3).
* m = O(Ω^α), 0 < α < 1 : la phase ∫m dΩ/Ω converge, ψ_r est continu mais pas C¹ ; insuffisant pour le critère formel.
* Réalisation naturelle : masse de Yukawa m = y Φ^ avec Φ^ = Ω Φ_r un scalaire de poids 1, régulier au sens de Q4 (conformément couplé, ou minimal avec m_Φ² = 2λ/3, pour lequel Φ^ ~ Ω, Ω²). Alors m/Ω = yΦ_r est lisse. En langage physique, m ∝ Ω ∝ 1/a : la masse doit s'éteindre comme l'inverse du facteur d'échelle.

**Réponse Q5 :** la singularité du système couplé Einstein-Dirac est localisée dans le terme de masse de l'équation de Dirac rescalée (m/Ω) ; dans les équations géométriques, elle n'affecte que le canal trace du terme de Cotton (−(κm/8)Ω⁻¹(g∧∇Ω)ψ̄_rψ_r), tous les autres termes restant réguliers. Sur les solutions, ce Ω⁻¹ est compensé par la partie poussière comobile de T*, et l'obstruction résiduelle est la non-lissité log-périodique Ω^{∓im/H}. Elle disparaît exactement si m = Ωμ avec μ lisse (m/Ω lisse), par exemple une masse de Yukawa portée par un scalaire de poids conforme 1.

---

## Formules clés

1. Γ^_μ = −¼ Ω⁻¹[γ_μ,γ^ν]∂_νΩ ; ψ^ = Ω^{3/2}ψ_r ; D^ψ^ = Ω^{5/2}Dψ_r.
2. T^_μν = Ω² T_μν[ψ_r,g] (hors couche ; en général Ω^{2w−1}).
3. tr T^ = Ω⁴τ_r ; sur couche τ_r = mΩ⁻¹ψ̄_rψ_r, tr T^ = mΩ³ψ̄_rψ_r.
4. Cotton : régulier ⇔ tr T^ = O(Ω⁴) ; sur couche, −(κ/8)Ω⁻¹(g_λρ∇_νΩ − g_νρ∇_λΩ)·mψ̄_rψ_r.
5. Lag^ = Ω⁴[(i/2)(ψ̄_rγ∇ψ_r − c.c.) − (m/Ω)ψ̄_rψ_r].
6. Scalaire : T^ ⊃ φ²(∇Ω∇Ω − ½g(|∇Ω|² + m²)) ; Cotton Ω⁻² ∝ (κφ²/6)(m² − 2λ/3) ; Δ(3 − Δ) = m²/H².
7. Dirac : exposants 3/2 ∓ im/H ; T_r^sing = (m/Ω)ψ̄_rψ_r u⊗u (poussière comobile, compensation exacte du Ω⁻¹ dans le Cotton).
8. Condition : m = Ωμ, μ lisse.
