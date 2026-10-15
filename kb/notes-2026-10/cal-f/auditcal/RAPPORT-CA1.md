# Rapport CA-1 (dérivation en cécité stricte)

Conditions : seule la consigne `PROMPT-AVEUGLE-CA1.md` a été lue. Aucun autre fichier du dépôt, aucune note, aucune source, aucune recherche. Tous les calculs sont refaits ici et vérifiés par sympy ; scripts dans `/tmp/claude-0/ca1/` :

| script | contenu |
|---|---|
| `cotton.py` | noyau : Christoffel de g^, Schouten physique, second membre de (E) (covariant ou "partiel") |
| `q1q2q3.py` | Q1, Q2, Q3 |
| `q4.py` | Dirac : Clifford, covariance conforme, équation rescalée, solutions, carré de l'opérateur |
| `scalar_friedrich.py` | contrôle du résultat scalaire Ω^{-2}(m² − 2λ/3) |
| `q5.py`, `q5b.py` | tests de la règle de comptage sur des champs tests conservés |

## 0. Cadre et conventions

* Signature (−,+,+,+). Coordonnées (η, x, y, z), η < 0, s = −η > 0.
* g^ = η^{-2} η_{μν} = s^{-2} η_{μν}, a = 1/s, Ω = s. Donc g = Ω² g^ = η_{μν} : la métrique non physique est **plate** (Minkowski).
* H = 1 ⇒ Ric^ = λ g^ avec **λ = 3** ; R^ = 4λ = 12. Contrôle du Schouten donné : avec G^ + λ g^ = κ T^, on a bien L^ = ½(Ric^ − R^/6 g^) = (κ/2)(T^ − ⅓ tr T^ g^) + (λ/6) g^.
* Christoffels de g^ : Γ^σ_{μν} = δ^σ_μ Υ_ν + δ^σ_ν Υ_μ − η_{μν} η^{στ} Υ_τ, avec Υ_μ = ∂_μ ln a = δ^0_μ / s.
* Second membre noté
  **RHS_{ρνλ} := 2 Ω^{-1} ∇^_[ν L^_λ]ρ = Ω^{-1}(∇^_ν L^_λρ − ∇^_λ L^_νρ).**
  Le terme (λ/6) g^ disparaît (∇^ g^ = 0), donc RHS = (κ/2) Ω^{-1} C[S], où S = T^ − ⅓ tr T^ g^ et C[S]_{νλρ} = ∇^_ν S_λρ − ∇^_λ S_νρ (Cotton de la partie matière).

Formule développée utile (coordonnées conformes, exacte) :

```
C_{νλρ} = ∂_ν S_λρ − ∂_λ S_νρ − Υ_ν S_λρ + Υ_λ S_νρ + η_νρ Υ^σ S_λσ − η_λρ Υ^σ S_νσ        (★)
```

## Q1. Fluide parfait test homogène isotrope

T^ = (ρ+p) u u + p g^, u = a^{-1}∂_η (u_μ = −a δ^0_μ). Alors S = (ρ+p) u u + (ρ/3) g^.

Calcul covariant (∇^_ν u_λ = H h_νλ, symétrique ; ∂_μ f = −u_μ ḟ) :

```
C_{νλρ} = (u_λ h_νρ − u_ν h_λρ) · [ (ρ+p) H + ρ̇/3 ]
```

Seules composantes non nulles (sympy), i, j spatiaux :

```
RHS_{j 0 i} = − (κ / 6η⁴) · [ η ρ'(η) − 3(ρ + p) ] δ_ij
            = − (κ / 6η³) · 𝓔 δ_ij ,     𝓔 := ρ' + 3 (a'/a)(ρ+p) = ρ' − 3(ρ+p)/η
```

(ρ' = dρ/dη). 𝓔 = 0 est exactement l'équation de continuité ∇^_μ T^{μ0} = 0 (la composante spatiale de la conservation est triviale par homogénéité).

**Réponse Q1** : le second membre est proportionnel à l'équation de conservation ; il **s'annule identiquement dès que le fluide test est conservé**, quelle que soit l'équation d'état p(ρ) et quel que soit le comportement de ρ en s. Il n'y a donc aucun pôle en Ω = 0 pour un fluide test conservé (physiquement : la section homogène isotrope reste conformément plate, le Cotton de la matière ne voit que la non-conservation).

## Q2. Champ scalaire test homogène φ(η), masse m

T^ = dφ dφ − g^(½ |dφ|² + ½ m² φ²). C'est un fluide parfait comoving avec ρ = ½φ̇² + ½m²φ², p = ½φ̇² − ½m²φ², et ρ̇ + 3H(ρ+p) = φ̇ (φ̈ + 3Hφ̇ + m²φ).

Résultat sympy :

```
RHS_{j 0 i} = (κ / 6η³) · φ'(η) · KG[φ] δ_ij ,     KG[φ] = □^φ − m²φ = −η²φ'' + 2ηφ' − m²φ
```

**Réponse Q2** : le second membre est (κ/6η³) φ' × (opérateur de Klein-Gordon). **Sur couche il est identiquement nul, pour toute masse m** (contrôlé aussi sur les solutions explicites φ = s^Δ±, Δ± = 3/2 ± √(9/4 − m²)). Le résultat ne dépend pas de m. La masse n'intervient que hors couche, via KG.

## Q3. Erreur volontaire : ∂ au lieu de ∇^, h = φ0 s + φ1 s², m² = 2

Contrôle : KG[h] = 0 pour m² = 2 (h est sur couche ; c'est h = Ω·(φ0 + φ1 s), le cas conforme). Version covariante : RHS ≡ 0 (Q2).

Version "partielle" RHS^∂_{ρνλ} = Ω^{-1}(∂_ν L^_λρ − ∂_λ L^_νρ), seules composantes non nulles :

```
RHS^∂_{i 0 i} =  λ/(3 s⁴)   −   (2κ/3) φ0 φ1 / s   −   κ φ1²
                 \_______/      \__________________________/
             fond de Sitter         partie matière
```

Détail matière : S_ij = (ρ/3) a² δ_ij avec ρ a² = (3/2)φ0² + 4φ0φ1 s + 3φ1² s², d'où −(κ/6) s^{-1} d(ρa²)/ds.

**Réponse Q3** : on obtient (i) un pôle d'ordre 4 purement géométrique λ/(3s⁴) (= s^{-4} pour λ = 3) qui vient de ∂_η g^_ij ≠ 0, alors que ∇^ g^ = 0 ; (ii) un **faux pôle simple −(2κ/3) φ0 φ1 / s**, non nul dès que φ0 φ1 ≠ 0 ; (iii) un terme fini −κφ1². Les trois sont des artefacts : le résultat correct est 0. Les termes de Christoffel (★) ne sont pas sous-dominants ici, ils sont du même ordre (Υ ~ 1/s) que les dérivées et compensent exactement.

## Q4. Champ de Dirac

Vérifié symboliquement (tétrade e_a = a^{-1}∂_a, connexion de spin explicite, matrices γ de Clifford mostly-plus) :

```
D^ ψ^ = a^{-5/2} γ^a ∂_a ( a^{3/2} ψ^ )          (covariance conforme de Dirac, sans terme de courbure)
```

Avec ψ_r = Ω^{-3/2} ψ^ = a^{3/2} ψ^ et l'équation physique (γ^μ ∇^_μ − m) ψ^ = 0, l'**équation rescalée** sur g = η plate est

```
γ^a ∂_a ψ_r − (m / Ω) ψ_r = 0        (Ω = s)
```

Comparaison :

| | poids | équation rescalée | terme singulier | régulier en Ω = 0 ssi |
|---|---|---|---|---|
| scalaire | 1 | (□_g − R_g/6) φ_r = Ω^{-2} (m² − 2λ/3) φ_r | Ω^{-2}, quadratique en m | m² = 2λ/3 (= 2) |
| Dirac | 3/2 | γ·∂ ψ_r = Ω^{-1} m ψ_r | Ω^{-1}, linéaire en m | m = 0 |

(Le résultat scalaire est recontrôlé dans `scalar_friedrich.py` : □_g(Ω^{-1}φ) = Ω^{-3}(□^ − R^/6)φ, R^/6 = 2λ/3.)

Pourquoi la différence : pour le scalaire, la courbure apporte un décalage R^/6 = 2λ/3 que m² peut compenser ; l'opérateur de Dirac est conformément covariant **sans** terme de courbure, rien ne décale m.

Solutions homogènes : sur les espaces propres de γ^0 (valeurs propres ±i), dψ_r/ds = (m/s) γ^0 ψ_r ⇒ **ψ_r ∝ s^{± i m}** = e^{± i m ln s} : borné, mais oscillant sans limite en s → 0 (non continu, dérivée ~ 1/s) pour tout m réel ≠ 0. Au second ordre, le carré de l'opérateur rescalé contient s^{-2} M avec M de valeurs propres **−m(m ∓ i)** (H = 1 ; en général −m(m ∓ iH)) : l'analogue de "m² − 2λ/3" serait m² ± i m H, qui ne s'annule pour aucun m réel non nul.

Couplage local à la courbure : sur dS exact, tout terme local de dimension masse construit à partir de la courbure se réduit, par symétrie maximale (Weyl = 0, Ric^ ∝ g^, σ^{ab}R_ab = 0), à une matrice constante invariante de Lorentz dans l'espace des spineurs, donc à M_eff + i M5 γ^5 avec M_eff, M5 constants (par ex. M_eff = m + ξ R^ = m + 4ξλ). L'équation rescalée devient γ·∂ψ_r = Ω^{-1}(M_eff + i M5 γ^5) ψ_r, régulière ssi M_eff = M5 = 0.

**Réponse Q4** : non, aucune masse constante non nulle ne régularise le Dirac rescalé (poids 3/2) ; le terme singulier est m Ω^{-1}, sans compensation possible. Un couplage local à la courbure ne peut régulariser **qu'en annulant la masse effective** (m = −ξR^ réglé finement), ce qui revient au cas sans masse ; il ne peut pas le faire avec masse effective non nulle. Seule une masse non constante s'annulant en Ω (m_eff = O(Ω)) échapperait à cette conclusion.

## Q5. La règle de comptage

Énoncé testé : « T ~ s^p Y, Y lisse ⇒ RHS ~ s^{p−2}, et pôle ssi p = 1 ».

Ce qui est vrai : de (★), en composantes de coordonnées conformes, si S = s^p Y alors

```
RHS = (κ/2) s^{-1} C = s^{p−2} A_p[Y|_{s=0}] + O(s^{p−1}),
A_p[Y]_{νλρ} = (κ/2)[ −(p+1)(δ^0_ν Y_λρ − δ^0_λ Y_νρ) − η_νρ Y_λ0 + η_λρ Y_ν0 ]   (convention ∂_η = −∂_s)
```

donc **RHS = O(s^{p−2}) est seulement une borne supérieure** ; le coefficient A_p peut s'annuler (et s'annule souvent sous la conservation). L'exposant dépend aussi de la base (en repère orthonormé, T_frame = s² T_coord, RHS_frame = s³ RHS_coord), point que la règle ne précise pas.

Contre-exemples (champs tests conservés, tous vérifiés sympy) :

| exemple | p (T en coord.) | règle prédit | RHS réel |
|---|---|---|---|
| poussière ρ = ρ0 s³ | 1 | pôle s^{-1} | **0** |
| rayonnement ρ = ρ0 s⁴ | 2 | régulier | 0 |
| scalaire homogène, toute m (Q2) | quelconque | selon p | **0** |
| scalaire m = 0, φ = x | 0 | pas de pôle (p ≠ 1) | **−κ/(3s²) (pôle double)** |
| scalaire m² = 2, φ = s x | 0 | pas de pôle | −2κ/3, fini |
| scalaire φ = x s^Δ, Δ² − 3Δ + m² = 0, Δ > 0 | 2Δ − 2 | s^{2Δ−4} | **−κ(Δ+1) s^{2Δ−2}/3 = O(s^p)** |

Le dernier cas montre en plus que l'ordre réel peut être s^p (deux ordres mieux que la règle) et qu'il y a pôle pour tout 0 < Δ < 1 (0 < m² < 2), avec p = 2Δ − 2 non entier, différent de 1.

**Réponse Q5** : la règle est **fausse dans les deux sens**. p = 1 sans pôle (poussière conservée : RHS ≡ 0) ; pôle avec p ≠ 1 (scalaire sans masse φ = x : p = 0, pôle double ; φ = x s^Δ : pôle d'ordre 2 − 2Δ non entier). La seule affirmation correcte est la borne RHS = O(s^{p−2}) en composantes de coordonnées, le coefficient dominant étant l'expression algébrique A_p[Y(0)], qu'il faut calculer (et que la conservation de T annule souvent).

## Synthèse

| Q | réponse nette |
|---|---|
| Q1 | RHS_{j0i} = −(κ/6η³) [ρ' − 3(ρ+p)/η] δ_ij ∝ équation de continuité ; nul ssi le fluide est conservé, toute équation d'état |
| Q2 | RHS_{j0i} = (κ/6η³) φ' KG[φ] δ_ij ; nul sur couche, indépendant de m |
| Q3 | λ/(3s⁴) − (2κ/3)φ0φ1/s − κφ1² : faux pôles (géométrique d'ordre 4 et matière simple), artefact ; la valeur correcte est 0 |
| Q4 | γ·∂ψ_r = (m/Ω)ψ_r ; solutions s^{±im} ; aucune masse constante ≠ 0 ne régularise ; un couplage à la courbure ne régularise qu'en annulant la masse effective |
| Q5 | règle fausse (contre-exemples poussière p = 1 sans pôle, φ = x p = 0 pôle double) ; seule la borne O(s^{p−2}) tient |
