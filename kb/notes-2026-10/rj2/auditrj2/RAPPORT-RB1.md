# Rapport RB-1 : dérivation indépendante (cécité stricte)

Fichiers lus : la consigne `PROMPT-AVEUGLE-RB1.md` et `friedrich2016.txt` (§§ 1 à 4). Aucun autre fichier de /home/claude n'a été ouvert. Tous les scripts et sorties sont dans `/home/claude/RJ2/auditrj2/work_rb1/` (SymPy 1.14).

## 0. Cadre et conventions fixées par calcul

de Sitter plat, H = 1, λ = 3, κ = 1 (équation de Friedrich (2.1) : Ĝ + λĝ = T̂). Ω = −η, g_c = Ω²g = métrique de Minkowski. Signature (−,+,+,+), {γ^a, γ^b} = −2η^{ab} : ce sont les matrices de Dirac usuelles (γ⁰ hermitienne, γ^i antihermitiennes), adjoint ψ̄ = ψ†γ⁰. Équation de Dirac : iγ^a∇_aψ = mψ (donne bien (□ − m²)ψ = 0 en signature mostly plus).

Tenseur d'énergie-impulsion retenu (sur couche ; le terme −g L s'annule sur couche) :

T_ab = −(i/2) [ ψ̄ γ_(a ∇_b) ψ − ∇_(a ψ̄ γ_b) ψ ].

| Signe ou convention | Valeur | Sortie qui la fixe |
|---|---|---|
| connexion spinorielle Γ_μ = c ω_μ^{ab} γ_a γ_b | c = −1/4 (impose ∇_μγ^ν = 0 sur un repère non conforme générique) | `q0_signes.out`, ligne (i) |
| signe global de T | T_00 = +E ψ†ψ > 0 pour une onde plane d'énergie positive | `q0_signes.out`, ligne (ii) |
| trace | T^μ_μ = −m ψ̄ψ (donc T̂ = −m ψ̄ψ, analogue de T̂ = −ρ̂ de Friedrich (3.8)) | `q0_signes.out`, ligne (iii) |
| équation conforme | D̸_phys(Ω^{3/2}ψ_c) = Ω^{5/2} D̸_c ψ_c, donc iD̸_cψ_c = (m/Ω)ψ_c | `q1_poids.out`, lignes (a) |
| matrice de Fuchs en de Sitter | K = iμγ⁰ ; Ω^{+iμ} sur γ⁰ = +1, Ω^{−iμ} sur γ⁰ = −1 | `q2_q3_K.out`, deux dernières lignes |
| coefficient de la partie 1/Ω de T_c | +m ψ̄ψ /(−n·n) | `q2_q3_K.out` |
| signe de ψ̄ψ sur les sous-espaces propres | + sur Ω^{+iμ}, − sur Ω^{−iμ} | `q3_timelike.out` |
| (3.3) | 6Ωs − 3∇Ω·∇Ω − λ = −T̂/4 | `q4_eq33.out` |
| coefficient de résonance du lapse | P₊S = −(μ/2) h₀₀⁽⁰⁾ P₊C | `q5_canaux.out` |
| jauge résiduelle | δh₀₀ = −2∂_tξ⁰ + 2ξ⁰/t | `q5_aux.out`, (3) |

Notation : Π₊ = (1+γ⁰)/2 (exposant +iμ), Π₋ = (1−γ⁰)/2 (exposant −iμ). Dans le cas général (n quelconque) j'appelle Π_± les projecteurs propres de K, sans présupposer de signe.

---

## Q1. τ = Ω T_c

**Établi.** Pour ψ = Ω^{3/2}ψ_c, g = Ω^{−2}g_c, repère physique e_a = Ω e^c_a :

- T_μν = Ω² T^c_μν en composantes de coordonnées ;
- τ_jk = Ω^{−3} T(e_j, e_k) = Ω T_c(e^c_j, e^c_k).

Le script traite ψ̄ comme une ligne indépendante de ψ (test plus fort que nécessaire) et vérifie l'identité à zéro exact pour (i) g_c plate et Ω(t,x,y,z) arbitraire, (ii) g_c diagonale non plate (A(t,x), B(t,y)) et Ω(t,x,y) arbitraire (`q1_poids.out`, six lignes True). Le mécanisme : les termes en ∂Ω/Ω issus de Ω^{3/2} s'annulent dans la combinaison antisymétrisée ψ̄γ∇ψ − ∇ψ̄γψ, et ceux de la connexion de spin s'annulent par symétrisation. Seule hypothèse : T est le tenseur cinétique, ce qui vaut sur couche.

Comptage des poids : ψ̄ψ ~ Ω³, γ_μ ~ Ω^{−1}, d'où Ω² ; puis deux vecteurs de repère physiques (Ω² en plus) et Ω^{−3} : bilan Ω¹.

---

## Q2. Matrice K, valeurs propres, partie 1/Ω de T_c

**Établi** (`q2_q3_K.out`, n_a générique à 4 composantes symboliques, repère orthonormé quelconque).

À l'ordre 1/Ω, iγ^a∇_aψ − (m/Ω)ψ = 0 avec ∇_bψ = (n_b/Ω)Kψ + régulier donne (i n̸ K − m)P = 0 pour tout P, d'où

K = −i m n̸⁻¹ = i m n̸ /(n·n),   n̸² = −(n·n) Id,   K² = m²/(n·n) Id.

Valeurs propres : ± i m /√(−n·n), chacune de multiplicité 2. Pour n·n = −1 : ±iμ. De plus K̄ = γ⁰K†γ⁰ = −K.

Partie d'ordre 1/Ω de T_c (identité exacte, sans hypothèse sur ψ) :

Ω T_c|_{1/Ω} = ( m ψ̄ψ / (−n·n) ) n_a n_b.

Elle est donc **proportionnelle à n_a n_b**, de coefficient m ψ̄ψ/(−n·n), qui vaut m ψ̄_cψ_c sur 𝓘 (où n·n = −1, voir Q4). Conséquence :

τ_ab |_𝓘 = m ψ̄_cψ_c n_a n_b,

c'est exactement la forme poussière de Friedrich (ρ U_a U_b avec ρ = m ψ̄_cψ_c, U ∝ n). L'écoulement effectif est orthogonal à 𝓘, ce qui est la condition géométrique que Friedrich dégage à la fin de son § 3 pour que (3.20) et (3.21) admettent une limite.

Réserve importante (**établi**, `q3_timelike.out`) : dans le repère où n est le temps, ψ̄ψ = |Π_aψ|² − |Π_bψ|² (un sous-espace propre positif, l'autre négatif). La « densité » ρ = m ψ̄ψ n'est donc pas de signe défini ; l'hypothèse ρ̂ ≥ 0 de Friedrich (2.5) n'est pas automatique. Elle l'est pour la classe à un seul exposant Ω^{+iμ} (Q6).

---

## Q3. Termes croisés dans ψ̄ψ

**Établi, et vrai pour tout n de genre temps** (`q3_timelike.out`, n₀ = ±√(N² + n₁² + n₂² + n₃²)) : les projecteurs propres Π_± = (1 ± n̸/N)/2 sont autoadjoints au sens de Dirac (Π̄_± = Π_±) et Π̄₊Π₋ = 0. Donc

ψ̄ψ = ψ̄₊ψ₊ + ψ̄₋ψ₋ exactement à l'ordre dominant, sans terme Ω^{±2iμ}.

Attention : cette annulation est propre au scalaire ψ̄ψ. Les bilinéaires ψ̄γ^cψ ont des termes croisés non nuls (Π̄₊γ^cΠ₋ ≠ 0 pour c = 0..3, même sortie). Les oscillations Ω^{±2iμ} apparaissent donc dans T_c dès l'ordre Ω⁰, c'est-à-dire dans τ dès Ω^{1±2iμ}.

---

## Q4. ∇Ω·∇Ω sur 𝓘 et constance de l'exposant

J'ai vérifié (3.3) moi-même (`q4_eq33.out`) : avec R̂ = Ω²R + 6Ω□Ω − 12|∇Ω|² (vérifié sur une métrique diagonale générique) et la trace d'Einstein R̂ = 4λ − T̂, on obtient exactement 6Ωs − 3∇Ω·∇Ω − λ = −T̂/4, d'où

g_c(∇Ω, ∇Ω) = −λ/3 + 2Ωs + T̂/12,   T̂ = Ω³ η^{jk}τ_jk = −m Ω³ ψ̄_cψ_c.

Dans le poids poussière, T̂ = O(Ω³) → 0. Donc **sur 𝓘, ∇Ω·∇Ω = −λ/3 = −1**, à la condition que Ωs → 0. Cette condition demande que les termes oscillants de g_c commencent à un ordre Ω^{n±2iμ} avec n ≥ 2 (un terme Ω^{1+2iμ} donnerait Ωs ~ Ω^{2iμ}, sans limite). Le calcul de Q5 donne n = 4 : la condition est satisfaite.

Conséquence : les exposants de Fuchs ±iμ/√(−n·n) valent ±iμ√(3/λ) = ±iμ **en tout point de 𝓘**. Ils sont constants le long de 𝓘. **Établi** sous l'hypothèse « Ωs → 0 », elle-même vérifiée perturbativement (Q5).

Vérification croisée (**établi**) : la solution d'ordre ε² de Q5 satisfait (3.3) ordre par ordre, dans les deux secteurs et pour j = 0, ±2, jusqu'à Ω⁵ avec μ symbolique (`q4_check_eps2_sym.out`) et jusqu'à Ω⁷ avec μ = 13/10 (`q4_check_eps2_num9.out`).

---

## Q5. Système couplé perturbatif

### Montage

- Spineur d'ordre ε : quatre modes conformes ψ_c = e^{ik·x} Σ Ω^{n+ijμ} c_{n,j} (récurrence de Frobenius c_s = −(isγ⁰+m)⁻¹ γ·k c_{s−1}, j = ±1, les deux exposants présents), avec k₁ = (1,1,0), k₂ = (−1,2,1) (non colinéaires) et leurs partenaires de parité (−k, γ⁰c). Amplitudes complexes génériques. Résidu de Dirac nul vérifié ordre par ordre (`run_*.out`).
- Pourquoi les partenaires de parité : dans le secteur homogène, l'équation 0i linéarisée est identiquement nulle à q = 0 ; il faut donc que l'impulsion homogène T_0i⁽⁰⁾ soit nulle (contrainte de stabilité de linéarisation). La configuration symétrique par parité l'assure exactement.
- Source : T_μν = Ω²T^c_μν ; conservation ∇^μT_μν = 0 vérifiée exactement, coefficient par coefficient (`run_*.out`).
- Équation : partie linéaire de G + 3g pour g = Ω^{−2}(η + ε²h), calculée par SymPy (`linE.out`).
- Secteurs calculés : q = k₁ − k₂ = (2,−1,−1) (paires (k₂,k₁) et (−k₁,−k₂)) et secteur homogène q = 0.

### Jauge

Jauge principale : **décalage nul h_0i = 0 et trace spatiale nulle δ^{ij}h_ij = 0**, lapse h₀₀ libre (c'est lui qu'on veut mesurer). Justification : (i) elle est atteinte par des ξ réguliers ; (ii) la jauge résiduelle est régulière (ξ⁰ = −(q²t/3)L, L = L₀e^{−q²t²/6}) ; (iii) `q5_aux.out` montre δh₀₀ = −2∂_tξ⁰ + 2ξ⁰/t : un ξ⁰ régulier qui ne déplace pas 𝓘 (ξ⁰ = t f(x) + O(t²)) laisse h₀₀|_𝓘 invariant, alors qu'une translation de 𝓘 (ξ⁰ = c(x)) rend h singulier (2c/t). La valeur du lapse moyen sur 𝓘 est donc un invariant parmi les jauges régulières à Ω fixé. Opérateur indiciel métrique dans cette jauge : det = 3s⁵(s−3)⁵/32, racines s = 0 et 3 seulement (`q5_aux.out`, (2)).

Jauge de contrôle : synchrone conforme (h₀₀ = h₀i = 0). Un lapse moyen non nul sur 𝓘 y forcerait un ξ⁰ ~ t ln|t| donc des logarithmes dans h_ij.

### Résultats d'ordre ε²

| Question | Réponse | Statut | Sortie |
|---|---|---|---|
| Logarithmes (résonances) ? | Aucun : système compatible sans terme en ln Ω jusqu'à Ω⁷ (μ symbolique), Ω⁹ (μ = 13/10), et en jauge synchrone jusqu'à Ω⁷ | établi aux ordres calculés | `run_7_sym.out`, `run_9_num.out`, `run_7_sync.out` |
| Pôles ? | Dénominateurs (2μ ± i), (μ ± 2i), 4μ²+1, 4μ²+9 : aucune racine réelle. Pas de pôle pour μ > 0 | établi jusqu'à Ω⁵ | `q5_poles_sym.out` |
| Ordre minimal des termes oscillants (j ≠ 0) | ψ̄ψ : aucun à l'ordre dominant ; T_c : Ω^{0±2iμ} ; τ : Ω^{1±2iμ} ; T_μν (coordonnées) : Ω^{2±2iμ} ; **h : Ω^{4±2iμ}** dans toutes les composantes, dans les deux secteurs et dans les deux jauges | établi | `q5_poles_*.out`, `q5_sync_analyse.out` |
| Lapse sur 𝓘 | h₀₀ = 0 à l'ordre Ω⁰ pour j = 0, ±2. j = 0 : terme Ω² de pure jauge résiduelle, puis Ω³ de coefficient m ψ̄ψ/3. **Lapse nul sur 𝓘** | établi | `q5_poles_sym.out` |

Échelle des exposants à l'ordre ε² (illustration) :

```
puissance de Omega :   0      1      2      3      4      5
j = 0  (h_ij)       : libre   .      .    libre   *      *     (donnees de bord et mode Omega^3, pas de log)
j = 0  (h_00)       :   0     0    jauge  m.pbp/3  *      *
j = +-2 (toutes)    :   0     0      0      0      *      *     (premier terme oscillant : Omega^{4 +- 2 i mu})
resonances possibles: s = 0, 3 (metrique, j = 0 seulement) ; s = +-i mu exactement (spineur)
```

Contrôle de cohérence sur le coefficient m ψ̄ψ/3 (secteur homogène) : la classe à un seul exposant donne h₀₀ = 22μ/3 Ω³, ce qui correspond à Σ|Π₊c|² = 2(5+6) = 22 ; avec les deux exposants on obtient 4μ/3 = μ(22 − 18)/3, où 18 = 2(6+3) = Σ|Π₋c|². La règle ψ̄ψ = |Π₊|² − |Π₋|² de Q2/Q3 est retrouvée.

Échantillon de coefficients (μ symbolique, partie libre mise à zéro, amplitudes fixées dans `q5_ordre2.py`), secteur homogène :

| terme | coefficient |
|---|---|
| h₀₀ Ω³ | 4μ/3 |
| h₀₀ Ω^{4−2iμ} | (22/3 + 2i)/(2μ + i) |
| h₀₀ Ω⁵ | 64μ/(3(4μ²+1)) |
| h₁₁ Ω^{4−2iμ} | (4 + 14i/3)/((μ+2i)(2μ+i)) |
| h₁₁ Ω⁵ | −4(20μ − 33)/(15(4μ²+1)) |

Secteur q = k₁ − k₂ : h₀₀ Ω^{4−2iμ} = (2/3 + 11i/6)/(2μ + i), h₀₀ Ω³ = 2μ/3, h₀₀ Ω⁵ = −4μ(4μ² − 5)/(9(4μ²+1)) ; liste complète dans `q5_table_sym.out`. Les termes j = +2 sont les conjugués des termes j = −2 dans cette configuration symétrique.

### Ordre ε³ : source de l'équation du spineur

J'ai écrit l'opérateur de Dirac au premier ordre pour g_c = η + h (repère symétrique), vérifié de deux façons (`deltaD_check.out`) : (a) contre la formule analytique du cas conforme, (b) contre la dérivée en ε du calcul exact (repère, Christoffel, connexion de spin) pour un h non conforme explicite comportant lapse, décalage et anisotropie. Pour h = H Ω^{s_h}e^{iqx} et ψ = C Ω^{s_ψ}e^{ipx}, la source S = −i δD̸[h]ψ vaut Ω^{s_h+s_ψ−1}[A + ΩB]. Seul A peut résonner, et seulement si h a un terme d'ordre Ω⁰ (`q5_ordre3_sym.out`, en tête).

Canaux de résonance pour un h **générique** (dix composantes, n'importe quelle jauge), `q5_canaux.out` :

| h ~ Ω^{0+ij_hμ} | ψ ~ Ω^{ij_ψμ} | source | projection résonante |
|---|---|---|---|
| j_h = 0 | +1 | Ω^{−1+iμ} | Π₊S = −(μ/2) H₀₀ Π₊C |
| j_h = 0 | −1 | Ω^{−1−iμ} | Π₋S = −(μ/2) H₀₀ Π₋C |
| j_h = +2 | −1 | Ω^{−1+iμ} | 0 identiquement |
| j_h = −2 | +1 | Ω^{−1−iμ} | 0 identiquement |

Donc, à l'ordre ε³, **la seule résonance possible est un lapse moyen non nul sur 𝓘** (h₀₀⁽⁰⁾, j = 0). Son effet est exactement un décalage de l'exposant μ → μ(1 − H₀₀/2), cohérent avec μ/√(−n·n). Un terme oscillant Ω^{0±2iμ}, dans n'importe quelle composante (lapse, trace, décalage), ne résonne jamais : les termes diagonaux conservent Π_± et le terme de décalage porte le facteur (s_h + 2s_ψ) = 0.

Avec la solution calculée, h₀₀⁽⁰⁾ = 0 et h n'a pas de terme oscillant avant Ω⁴ : **toutes les projections résonantes sont nulles** (`q5_ordre3_sym.out`, `q5_ordre3_num9.out`), y compris avec les données libres h_ij⁽⁰⁾(x) laissées symboliques. **Pas de ln Ω dans le spineur à l'ordre ε³ : établi.** Contre-test de sensibilité : un lapse h₀₀ = L Ω⁰ fournirait −μL/2 ≠ 0 (même sortie, rubrique « Contre-tests »).

---

## Q6. Classe à un seul exposant (Ω^{+iμ} seulement)

**Établi aux ordres calculés** (`run_7_sym_single.out`, `q5_poles_single.out`, `q5_ordre3_single.out`) :

- La source n'a que j = 0 (Ω^{−iμ}·Ω^{+iμ}) : T_c, τ et h sont des **séries entières en Ω**, sans terme oscillant, sans logarithme jusqu'à Ω⁷ (μ symbolique), et sans pôle réel (dénominateurs 4μ²+1, 4μ²+9 seulement).
- Lapse : h₀₀ = O(Ω²) (jauge) puis 22μ/3 Ω³ dans le secteur homogène ; nul sur 𝓘.
- À l'ordre ε³ la source ne contient que j = +1, et la projection Π₊ du coefficient de Ω^{−1+iμ} est nulle : ψ₃ reste de la forme Ω^{iμ}·(série entière). **La classe est stable à l'ordre ε³.**
- Dans cette classe ρ = m ψ̄ψ ≥ 0 à l'ordre dominant : c'est la seule classe où l'hypothèse ρ̂ ≥ 0 de Friedrich est automatiquement satisfaite.

---

## Q7. Argument à tous les ordres

Le développement est formel, double en ε et en Ω, avec des exposants n + ijμ. Voici ce que j'obtiens.

**Ce qui est prouvé (algèbre exacte, valable à tout ordre) :**

1. Spineur : det(isγ⁰ + m) = (s − im)²(s + im)² (`q5_aux.out`, (1)). Pour s = N + ijμ, la résonance n'a lieu que pour N = 0 et j = ±1, c'est-à-dire pour une source en Ω^{−1±iμ} exactement, et elle porte sur Π_±S.
2. Métrique (jauge décalage nul, trace nulle) : racines indicielles 0 et 3 seulement. Un exposant n + ijμ avec j ≠ 0 n'est jamais racine. Seuls les termes j = 0 aux ordres Ω⁰ et Ω³ peuvent créer des logarithmes.
3. Ω T_c|_{1/Ω} = m ψ̄ψ n_a n_b/(−n·n) exactement, avec n_a = −δ⁰_a en coordonnées quelle que soit la métrique. Donc à tout ordre en ε, la source physique d'ordre Ω¹ n'a qu'une composante 00 : elle ne peut pas alimenter l'obstruction TT de l'ordre Ω³.
4. Les termes croisés de ψ̄ψ s'annulent exactement (Π̄₊Π₋ = 0) : à tout ordre, la partie 1/Ω de T_c est non oscillante, et les oscillations de la source physique commencent à Ω^{2±2iμ}.
5. À l'ordre ε³, la seule voie de résonance du spineur est le lapse moyen sur 𝓘 (tableau ci-dessus). Plus généralement, le coefficient de ∂_t à l'ordre Ω⁰ dans l'opérateur de Dirac ne dépend que du lapse et du décalage sur 𝓘 ; s'ils prennent leurs valeurs de de Sitter, l'opérateur indiciel n'est pas perturbé.
6. (3.3) impose g_c(∇Ω,∇Ω)|_𝓘 = −λ/3 de façon non perturbative, dès que Ωs → 0 et que T̂ → 0 : le lapse moyen sur 𝓘 est fixé à sa valeur de de Sitter.

**Récurrence (formelle).** Hypothèse au rang k : pas de log ; termes oscillants de h seulement à partir de Ω⁴ (Ω² suffirait) ; lapse sur 𝓘 non perturbé ; décalage nul. Alors, au rang k + 1 :
- Ωs → 0, donc par 6 le lapse reste non perturbé ;
- par 1 et 5, aucune résonance spinorielle ;
- par 2, 3 et 4, aucune résonance métrique d'origine matérielle, et les termes oscillants restent à Ω^{≥4} : un terme oscillant de source à Ω^p donne h à Ω^{p+2}, et les produits non linéaires avec un facteur oscillant restent d'ordre ≥ 4.
- Dans la classe à un seul exposant, les indices restent j = +1 pour ψ et j = 0 pour h à tout ordre (la conjugaison n'apparaît que dans ψ̄ψ). La géométrie reste en séries entières et la classe est stable.

**Ce qui est supposé, non prouvé ici :**
- (S1) Partie vide non linéaire : absence d'obstruction logarithmique de type Fefferman-Graham pour les données Ω⁰ et Ω³ en dimension 3+1 avec λ > 0. C'est un résultat connu (régularité de Friedrich dans le vide, développement de Starobinsky), que je n'ai vérifié ici qu'au premier ordre en h.
- (S2) Convergence des séries, en Ω (au-delà de l'ordre 9) et en ε. Les dénominateurs ne s'annulent pas pour μ réel (j'ai vu (n + 2ijμ)(n − 3 + 2ijμ) et m ± is), mais aucune estimation n'est faite.
- (S3) Existence non linéaire réelle : τ contient Ω^{1±2iμ}, donc τ est continu mais pas C¹ en 𝓘 dans la classe à deux exposants. Le théorème lisse de Friedrich (données C^∞) ne s'applique pas tel quel ; il faudrait une théorie fuchsienne à exposants complexes. Dans la classe à un seul exposant, τ et g_c sont formellement des séries entières, mais ψ_c garde le facteur Ω^{iμ} et l'équation du spineur reste fuchsienne (terme (μn̸ + m)P/Ω) : le système n'est pas régulier au sens strict de Friedrich.
- (S4) Calculs explicites faits pour des impulsions et amplitudes numériques génériques et pour un seul secteur de Fourier non nul (plus le secteur homogène). Les arguments 1 à 6 ne dépendent pas de ces choix.

**Conclusion à tous les ordres : plausible (prouvée formellement sous S1 et S2, non prouvée au sens d'un théorème d'existence, S3).**

---

## Classement

| Énoncé | Statut |
|---|---|
| Q1 : τ = Ω T_c pour Ω quelconque (et g_c quelconque testée) | **établi** |
| Q2 : K = i m n̸/(n·n), valeurs propres ±im/√(−n·n), Ω T_c|_{1/Ω} = m ψ̄ψ n_a n_b/(−n·n) | **établi** |
| Q2 : ρ = m ψ̄ψ de signe défini | **réfuté** (signe opposé sur les deux sous-espaces propres) |
| Q3 : termes croisés nuls dans ψ̄ψ (tout n de genre temps) | **établi** |
| Q3 : termes croisés nuls dans T_c au-delà de 1/Ω | **réfuté** (oscillations dès Ω^{0±2iμ} dans T_c) |
| Q4 : ∇Ω·∇Ω = −λ/3 sur 𝓘, exposant ±iμ constant le long de 𝓘 | **établi** sous Ωs → 0, condition vérifiée perturbativement |
| Q5 : pas de log ni de pôle à l'ordre ε² (jusqu'à Ω⁷ symbolique, Ω⁹ numérique, deux jauges) | **établi** aux ordres calculés |
| Q5 : premiers termes oscillants de h en Ω^{4±2iμ} | **établi** (deux secteurs, deux jauges) |
| Q5 : lapse nul sur 𝓘 | **établi** |
| Q5 : résonance (ln Ω) dans le spineur à l'ordre ε³ | **réfuté** : aucune ; seul canal possible = lapse moyen sur 𝓘, nul |
| Q6 : classe à un seul exposant en séries entières et stable à l'ordre ε³ | **établi** aux ordres calculés |
| Q7 : absence de log à tous les ordres, stabilité de la classe à un exposant | **plausible** (formel sous S1, S2 ; S3 ouvert) |

## Index des scripts

`conv.py` (gammas), `dirac_curved.py` (Dirac et T en espace courbe), `q0_signes.py`, `q1_poids.py`, `q2_q3_K.py`, `q4_eq33.py`, `q4_check_eps2.py`, `linE.py` (Einstein linéarisé), `spinors.py` (modes de Frobenius et source), `q5_ordre2.py` (arguments : ordre, μ numérique ou `None`, `single` ; variable `GAUGE=sync`), `q5_poles.py`, `q5_table.py`, `deltaD.py`, `deltaD_check.py`, `q5_ordre3.py`, `q5_canaux.py`, `q5_aux.py`. Les sorties `.out` correspondantes sont dans le même répertoire.
