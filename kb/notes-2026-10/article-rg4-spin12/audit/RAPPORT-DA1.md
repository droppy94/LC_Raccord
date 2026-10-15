# RAPPORT DA-1 : dérivation en cécité stricte

Rédigé sans accès à aucun autre document que la consigne. Tous les calculs ci-dessous ont été refaits de zéro ; les vérifications symboliques et numériques sont dans `/tmp/claude-0/da1/` (scripts `s1_spinconn.py`, `s2_modes.py`, `s3_quasifree.py`, `s4_nonrel.py`).

## 0. Conventions et réduction de l'équation

* Signature (-,+,+,+), Clifford {γ^a, γ^b} = -2 η^{ab}, donc (γ^0)^2 = 1, (γ^j)^2 = -1. Représentation de Dirac : β = γ^0 = diag(1,1,-1,-1), α^j = γ^0 γ^j = [[0, σ_j],[σ_j, 0]]. Avec ces choix (iγ·∇ + m)(iγ·∇ - m) = □ - m², donc l'équation (iγ^μ∇_μ - m)ψ = 0 est la bonne.
* g = a(η)² (-dη² + dx²), a = -1/(Hη), Ω = 1/a = -Hη, ĝ = Ω² g = métrique de Minkowski en (η, x). On note μ := m/H.
* Repère comobile e_a = a^{-1} ∂_a. En résolvant ∇_μ γ^ν = 0 (script `s1`), on trouve Γ_η = 0 et Γ_j = (a'/2a) γ_j γ_0 (à la convention de signe près), d'où l'identité vérifiée symboliquement :

```
i γ^μ ∇_μ ( a^{-3/2} ψ̂ ) = a^{-5/2} i γ^a ∂_a ψ̂        (γ^a plates)
```

  Donc, avec ψ = Ω^{3/2} ψ̂ :

```
(i γ^a ∂_a - M(η)) ψ̂ = 0 ,     M(η) := m a(η) = m/Ω = μ/|η| .
```

  L'équation rescalée est l'équation de Dirac plate avec une masse dépendant du temps conforme, qui diverge comme 1/|η| en scri+. Remarque utile : ∫ M dη = ∫ m a dη = ∫ m dt. La phase accumulée en η est exactement la phase de masse au repos en temps physique.

## Q1. Mode de Fourier, conservation, limite en scri+

**Équation.** Avec ψ̂ = e^{ik·x} u(η), on a iγ^0 u' - (γ·k) u - M u = 0 ; en multipliant par γ^0 :

```
i u'(η) = h(η) u(η),     h(η) = α·k + β M(η) ,  h hermitienne.
```

**Norme.** d(u†u)/dη = i u†(h - h†)u = 0. **Vrai : u†u est conservée** (c'est la densité de charge rescalée, conservation exacte).

**k = 0.** u(η) = exp(-iβ ∫M) u_0 = exp(iβ μ ln|η|) u_0 :

```
P+ u = e^{+iμ ln|η|} P+ u_0 ,   P- u = e^{-iμ ln|η|} P- u_0 ,   P± = (1 ± β)/2 .
```

Quand η → 0^-, ln|η| → -∞ : chaque composante non nulle tourne indéfiniment sur un cercle de rayon fixe. **Pas de limite** pour toute solution non nulle si m ≠ 0. En temps physique, μ ln|η| = -m t + cste : ce n'est rien d'autre que la phase e^{∓imt} d'énergie au repos, parfaitement régulière dans le repère physique, que la compression t → η = -e^{-Ht}/H accumule en un nombre infini de tours sur un intervalle fini de η.

**k ≠ 0 : preuve (représentation d'interaction).** Posons θ(η) = μ ln|η|, U(η) = e^{iβθ} (propagateur exact du terme de masse) et u = U v. Comme β anticommute avec les α^j, U^{-1} α U = α e^{2iβθ}, et l'équation devient

```
i v' = (α·k) e^{2iβθ(η)} v .
```

1. Le second membre est borné : |v'| ≤ |k| |v| = |k| |u_0|. Donc v est lipschitzienne sur (η_0, 0) et **v(η) → v_0** (critère de Cauchy), avec |v(η) - v_0| ≤ |k||u_0| |η|.
2. v_0 ≠ 0 car |v_0| = |u_0| (l'évolution de v est unitaire).
3. u(η) = e^{iβθ} v_0 + O(|η|). Or P± u = e^{±iθ} P± v_0 + O(|η|), et au moins une des deux projections P± v_0 est non nulle ; la composante correspondante n'a pas de limite puisque e^{±iθ} n'en a pas.

**Conclusion Q1 : faux, u n'a pas de limite en scri+, pour toute solution non nulle, pour tout k, dès que m ≠ 0.** Forme asymptotique exacte :

```
u(η) = exp(iβ (m/H) ln|η|) [ v_0 + O(|η|) ] ,     |P± u(η)|² → n± := |P± v_0|² .
```

Les modules |P± u| convergent ; seules les phases relatives aux deux sous-espaces β = ±1 divergent. (Les solutions exactes sont des fonctions de Hankel d'ordre 1/2 ± iμ en k|η| ; z^{1/2} H_{1/2±iμ}(z) ~ z^{∓iμ} en 0, ce qui redonne la même oscillation logarithmique.)

Pour m = 0, M = 0 et u = e^{-iα·kη} u_0 se prolonge analytiquement à travers η = 0 (invariance conforme).

Vérifications numériques (`s2`, μ = 0.7, k = (0.3, -0.5, 1.1)) : dérive de norme 1.6e-11 ; |v - v_0|/|η| constant ≈ 0.72 (donc O(|η|)) ; u[0] continue de tourner jusqu'à |η| = 4e-18.

```
   plan complexe de P+u                     plan de v
        .-----.                                 
      /    ↺   \     tours infinis              •  v_0   (converge)
     |  rayon   |    quand ln|η| → -∞          
      \  √n+   /                                
        '-----'                                 
```

## Q2. Couplage à un potentiel de jauge pure A = A_η(η) dη

Couplage minimal ∂ → ∂ - iqA. L'équation de mode devient i u' = (h - qA_η) u. Sous ψ̂ → e^{-iλ(η)} ψ̂, on a A_η → A_η - λ'/q (le signe dépend de la convention de charge, sans incidence sur ce qui suit). Partons de la jauge A = 0 (A est de jauge pure, dA = 0) ; une jauge générale est u_λ = e^{-iλ} u avec A_η = -λ'/q.

**(a) Faux.** Une phase scalaire commute avec β ; elle multiplie P+ u et P- u par le même facteur. Si e^{-iλ} u → w, alors e^{i(θ-λ)} P+ v_0 et e^{-i(θ+λ)} P- v_0 convergent. Si n+ et n- sont tous deux non nuls, le quotient e^{2iθ} convergerait : contradiction. Aucune jauge ne fait converger une solution qui a à la fois une composante β = +1 et une composante β = -1 asymptotiques.

**(b) Les solutions qui convergent dans une jauge convenable sont exactement celles avec P- v_0 = 0 (type particule asymptotique) ou P+ v_0 = 0 (type antiparticule).** Pour P- v_0 = 0, on prend λ = θ = μ ln|η| (plus toute fonction ayant une limite) :

```
e^{-iθ} u = P+ v + e^{-2iθ} P- v  →  v_0 ,   car P- v = O(|η|).
```

Il s'agit d'un sous-espace de dimension complexe 2 sur 4 par mode k (non générique, mais une seule et même jauge, indépendante de k, convient à tous les paquets d'ondes de type particule ; la jauge opposée λ = -θ convient au type antiparticule ; aucune ne convient aux deux à la fois). Toute jauge qui marche impose λ = θ + c + o(1), donc λ diverge logarithmiquement et le potentiel transformé vérifie

```
A_η  ~  ∓ (m/(qH)) · 1/η ,    ∫_{η_0}^{0} A_η dη  diverge (logarithmiquement).
```

**Le potentiel transformé n'est pas intégrable en η = 0** (pas L¹, sa ligne de Wilson jusqu'à scri+ diverge). Vérifié numériquement : solution de type particule, |u_g(s) - u_g(∞)| ≈ 3e-5, 1.5e-9, 1.5e-11 à s = -ln|η| = 10, 20, 30 dans la jauge λ = θ, contre des écarts O(1) sans jauge ; pour une solution générique, la phase invariante de jauge arg(u_0 ū_2) continue de tourner.

**(c) Dans le repère physique, la transformation est parfaitement régulière.** θ = μ ln|η| = -m t - μ ln H, donc e^{-iλ} = e^{imt} × cste, et

```
A' = A ∓ (m/q) dt ,    soit A'_t = constante = m/q.
```

C'est le décalage constant du potentiel scalaire qui retire l'énergie au repos (équivalent d'un potentiel chimique constant). La singularité en conformel vient uniquement de dt = a dη = -dΩ/(HΩ) = -d ln Ω / H : la 1-forme dt n'est pas une 1-forme lisse (ni même intégrable) sur la variété compactifiée en Ω = 0. La transformation est régulière sur l'espace-temps physique et singulière exactement sur le bord ajouté.

**(d) Faux (pour m ≠ 0).** Si A'_η est continu sur [η_0, 0], il est intégrable, et le λ correspondant a une limite ; la convergence de ψ̂ est alors équivalente à sa convergence en jauge A = 0, qui n'a lieu pour aucune solution non nulle (Q1). Réciproquement toute jauge qui fait converger ψ̂ rend A non intégrable. Il n'existe donc aucune jauge U(1) où ψ̂ et A sont simultanément continus en scri+. L'obstruction est invariante de jauge : c'est le défaut de convergence de la quantité e^{iq∫A} u, ou de façon équivalente la phase relative entre P+ u et P- u.

Remarque : la « rotation » e^{-iβθ} qui fait converger toutes les solutions (passage à v) n'est pas une transformation de jauge : elle ne commute pas avec α et transforme l'opérateur cinétique (α·k → α·k e^{2iβθ}, coefficient oscillant sans limite).

## Q3. Densité d'énergie rescalée

Tenseur symétrisé T_μν = (i/2) ψ̄ γ_(μ D_ν) ψ + h.c. ; on fixe le signe global pour que l'énergie d'une solution de fréquence positive soit positive. Sur couche, le terme g_μν L s'annule. Comme Γ_t = 0 dans le repère comobile (script `s1`) :

```
T_tt = Re( ψ† i D_t ψ ).
```

Avec ψ = a^{-3/2} ψ̂, ∂_t = a^{-1} ∂_η : le terme provenant de ∂_t a^{-3/2} est réel × ψ̂†ψ̂ multiplié par i, donc imaginaire pur, et disparaît. D'où

```
ρ̂ = Ω^{-4} T_tt = Re( u† (i ∂_η + q A_η) u ) = u† h(η) u = u† (α·k) u + M(η) u† β u     (sur couche).
```

**Asymptotique.** u†βu = v†βv = n+ - n- + O(|η|) et u†(α·k)u = v†(α·k)e^{2iβθ} v est borné (oscillant). Donc

```
ρ̂(η) = (m/(H|η|)) (n+ - n-) + O(1) = m a (n+ - n-) + O(1).
```

Pour une solution de type particule (n- = 0, |u| = 1), le calcul adiabatique (χ = P- u ≈ |η| (σ·k) φ/(2μ - i)) donne le terme suivant :

```
ρ̂ = m a + (2μ k²/(4μ² + 1)) |η| + o(|η|)    →   m a + (k² H/(2m)) |η|   si m ≫ H.
```

Vérifié numériquement : ρ̂|η| → μ(n+ - n-) à 1e-15 près ; coefficient du terme en |η| mesuré 0.7331 contre 2μk²/(4μ²+1) = 0.7331 (μ = 0.7, k² = 1.55).

**Divergence : ρ̂ ~ 1/|η| → ∞** dès que n+ ≠ n-.

**Invariance de jauge : vrai.** Avec la dérivée covariante, u → e^{-iλ}u et qA_η → qA_η - λ' laissent i∂_η + qA_η covariant ; sur couche ρ̂ = u† h u ne dépend pas de A. Dans la jauge de Q2(b) où ψ̂ converge, la divergence passe intégralement dans le terme qA_η |u|² ~ m a. La densité « canonique » Re(u† i u') seule n'est pas invariante de jauge et serait bornée dans cette jauge : c'est un artefact.

**Interprétation physique.** En physique, ρ = a^{-4} ρ̂ = m (n+ - n-) a^{-3} + [p²/2m] a^{-3} + ..., avec p = k/a l'impulsion physique : c'est la **densité d'énergie de masse au repos d'une poussière non relativiste**, diluée en a^{-3}, plus la correction cinétique p²/2m. Le poids conforme -4 est celui du rayonnement ; appliqué à de la matière massive diluée en a^{-3}, il produit Ω^{-4}ρ ∝ a = 1/Ω → ∞. La divergence traduit donc un mauvais poids conforme pour la matière massive, pas une pathologie locale. Classiquement les antiparticules contribuent avec le signe - (énergie indéfinie du Dirac classique) ; en théorie quantique (Q5) elles contribuent positivement.

| quantité | comportement en scri+ (m ≠ 0) | invariante de jauge ? |
|---|---|---|
| u†u | constante | oui |
| \|P± u\|² | → n± | oui |
| u (phase relative de P+u et P-u) | pas de limite | oui (obstruction) |
| u à une phase globale près, n- = 0 | converge dans la jauge λ = θ | non |
| ρ̂ = Ω^{-4} T_tt | ~ m a (n+ - n-) → ∞ | oui |

## Q4. Masse dépendant du temps m(t) ≥ 0 continue

La réduction de §0 est valable telle quelle : M(η) = m(t(η)) a(η), et Θ(t) := ∫^η M dη = ∫^t m dt'. La représentation d'interaction u = e^{-iβΘ} v donne i v' = (α·k) e^{2iβΘ} v (second membre borné), donc **v → v_0 ≠ 0 dans tous les cas**, avec |v - v_0| = O(|η|).

**(a) Toute solution converge en scri+ ⇔ ∫^∞ m(t) dt < ∞** (⇔ M ∈ L¹ près de η = 0).
* ⇐ : ||h(η)|| ≤ |k| + M(η) intégrable, |u'| ≤ ||h|| |u_0|, donc u est de Cauchy.
* ⇒ : si ∫ m dt = ∞, Θ croît vers +∞ (m ≥ 0), e^{±iΘ} n'a pas de limite et u = e^{-iβΘ} v_0 + o(1) ne converge pour aucune solution non nulle.
* C'est une **dichotomie** : soit toutes les solutions convergent, soit aucune. (Sans hypothèse de signe, le critère serait : Θ(t) a une limite finie.)

**(b) ρ̂ bornée pour une solution de type particule (n- = 0, ou plus généralement n+ ≠ n-) ⇔ m(t) = O(e^{-Ht}) = O(Ω)** (⇔ M borné près de η = 0).
* ρ̂ = u†(α·k)u + M v†βv, avec v†βv = (n+ - n-) + δ(η), |δ| ≤ 2|k||u_0|²|η|.
* ⇐ : immédiat.
* ⇒ : pour |η| assez petit, |δ| ≤ |n+ - n-|/2, donc |ρ̂| ≥ M |n+ - n-|/2 - |k||u_0|² ; si M n'est pas borné, ρ̂ ne l'est pas.

**(c) Le coefficient du terme de masse, M = m/Ω vu comme fonction de Ω = e^{-Ht}, se prolonge en fonction lisse en Ω = 0 ⇔ m(t) = Ω F(Ω) = e^{-Ht} F(e^{-Ht}) avec F ∈ C^∞([0, ε)), F ≥ 0.** De façon équivalente, m(t) admet un développement m ~ Σ_{n≥1} c_n e^{-nHt} au sens fort (compatible avec les dérivées en Ω). La structure lisse en scri+ est celle donnée par Ω (ou η = -Ω/H, équivalente).

**Ordre : (c) ⇒ (b) ⇒ (a), implications strictes.** (c) ⇒ M continu sur [0, ε) ⇒ borné ⇒ (b) ; (b) ⇒ M borné sur un intervalle fini ⇒ L¹ ⇒ (a).

```
  (c) M lisse en Ω=0   ⊂   (c0) M continu   ⊂   (b) M borné   ⊂   (a) M ∈ L¹(dη) ⇔ ∫ m dt < ∞
   m = Ω F(Ω)               m/Ω → limite        m = O(e^{-Ht})       ∫^∞ m dt < ∞
```

**Exemples séparateurs** (vérifiés numériquement, `s2`, H = 1, solution de type particule) :

| m(t) | ∫ m dt | M = m a | (a) | (b) | (c) | numérique |
|---|---|---|---|---|---|---|
| m_0 (constante) | ∞ | μ/\|η\| | non | non | non | Q1 |
| 1/(1+t) | ∞ (log) | non borné | non | non | non | u dérive encore, ρ̂ ~ 5e15 |
| 1/(1+t)² | fini | non borné | **oui** | non | non | u converge, ρ̂ ~ 1e14 |
| e^{-Ht/2} | fini | (H\|η\|)^{-1/2} | **oui** | **non** | non | \|u(35)-u(40)\| = 5e-8, ρ̂ ≈ 2e4, 3e6, 4e8 à s = 20, 30, 40 |
| e^{-Ht}(1 + e^{-Ht/2}) | fini | 1 + Ω^{1/2} | oui | oui | non (C^0 seulement) | |
| e^{-Ht}(2 + sin t) | fini | 2 + sin(-ln Ω/H) | oui | oui | non (même pas continu) | |
| e^{-Ht} | fini | 1 | oui | oui | oui | ρ̂ = 1.44 constant |

**Exemple demandé (a) sans (b) : m(t) = m_0 e^{-Ht/2}** (ou toute masse polynomialement décroissante intégrable, par ex. 1/(1+t)²) : toutes les solutions convergent en scri+, mais ρ̂ ~ m_0 (H|η|)^{-1/2} → ∞ pour une particule. La convergence du champ rescalé ne garantit donc pas la finitude de l'énergie rescalée. Notons que (c) exige que la masse physique s'annule en scri+ au moins comme Ω.

## Q5. Différence d'énergie-impulsion entre ω_f et ω (théorie quantique)

Cadre : champ de Dirac quantifié (CAR), ω quasi-libre invariant de jauge, de type Hadamard ; opérateur à deux points ω(ψ*(g)ψ(h)) = ⟨h, S g⟩ sur l'espace de Hilbert à une particule des solutions (0 ≤ S ≤ 1). État excité ω_f(X) = ω(ψ(f) X ψ*(f)) / ω(ψ(f)ψ*(f)), f lisse (à support compact).

**Indépendance vis-à-vis de la renormalisation : vrai.** La renormalisation de Hadamard soustrait un parametrix H(x,y) indépendant de l'état et ajoute des termes locaux C_ab[g, m] (ambiguïtés de Wald / Hollands-Wald, y compris le terme qui rétablit la conservation et celui qui fixe l'échelle du logarithme), tous multiples c-nombres de l'identité et identiques pour les deux états. ω_f est encore de Hadamard (sa fonction à deux points diffère de celle de ω par un noyau lisse, voir ci-dessous). Les deux états étant normalisés, toutes ces contributions se compensent dans la différence ; il n'y a même pas de limite de coïncidence singulière à prendre. Le choix d'ordonnancement des opérateurs (ψ̄ψ ou antisymétrisé) n'importe pas non plus, car l'anticommutateur est un c-nombre indépendant de l'état.

**Valeur.** Par le théorème de Wick fermionique (le terme ⟨ψψ⟩ s'annule par invariance de jauge) :

```
ω(ψ(f) ψ*(g) ψ(h) ψ*(f)) = ⟨f,(1-S)g⟩⟨h,(1-S)f⟩ + ⟨f,(1-S)f⟩ ω(ψ*(g)ψ(h))
⇒  Δω(ψ*(g)ψ(h)) = ⟨h, Φ⟩⟨Φ, g⟩ / N ,    Φ := (1 - S) f ,   N := ⟨f, (1-S) f⟩ .
```

(Vérifié exactement sur un espace de Fock à 3 modes avec un état quasi-libre mixte aléatoire, `s3`.) La différence de fonction à deux points est le noyau de rang un, lisse, Φ̄(x) ⊗ Φ(y) / N. Comme T_ab est une forme bilinéaire différentielle en (ψ̄, ψ) :

```
ω_f(T_ab) - ω(T_ab) = T_ab^{classique}[Φ] / N .
```

* État pur (vide de Fock, S = P_-) : Φ = P_+ f est la projection de fréquence positive, N = ||Φ||², donc **Δ⟨T_ab⟩ = T_ab^{cl}[Φ/||Φ||], le tenseur classique de la fonction d'onde à une particule normalisée.**
* Excitation de type trou (antiparticule), ω^f(X) = ω(ψ*(f) X ψ(f))/ω(ψ*(f)ψ(f)) : Δω(ψ*(g)ψ(h)) = -⟨h,Sf⟩⟨Sf,g⟩/⟨f,Sf⟩ (vérifié, `s3`), donc Δ⟨T_ab⟩ = -T_ab^{cl}[Φ'] / ⟨f,Sf⟩ avec Φ' = S f de fréquence négative ; le signe moins rend positive l'énergie totale de l'antiparticule (le T^{cl} d'une solution de fréquence négative est négatif).
* Pour un état mixte, N = ⟨f,(1-S)f⟩ ≥ ||Φ||² (blocage de Pauli partiel).

Conséquence pour Q3 : la divergence ρ̂ ~ m a trouvée classiquement est, pour un état à une particule, une quantité **physique et indépendante de la renormalisation** : Ω^{-4}(ω_f - ω)(T_tt) ~ m a |P_+ ...|² → ∞, avec un signe positif pour particules et antiparticules. Mise en garde : la densité locale T_tt^{cl}[Φ] d'une solution de fréquence positive n'est pas positive ponctuellement en général (seules les inégalités quantiques d'énergie la contrôlent) ; aux temps tardifs, pour un paquet de type particule, elle est dominée par m a^{-3}|Φ|² > 0.

## Q6. Un couplage local à la géométrie peut-il supprimer le comportement de Q1 avec une masse effective non nulle ?

**Réponse : non.** Sur de Sitter exact, tout couplage de la classe ci-dessous se réduit à une équation de Dirac standard de masse effective constante m_eff, et le comportement de Q1 (avec μ = m_eff/H) est supprimé si et seulement si m_eff = 0.

**Argument.**
1. dS est maximalement symétrique : R_abcd = H²(g_ac g_bd - g_ad g_bc), R = 12H², tenseur de Weyl nul, ∇R_abcd = 0. Tout tenseur construit localement à partir de g (métrique, courbure, dérivées covariantes de la courbure, ε_abcd) est invariant sous le groupe d'isotropie SO(3,1) en chaque point, donc combinaison à coefficients constants de g_ab, δ et ε_abcd. Il n'existe aucun vecteur local (pas de ∇R, pas de champ de Hubble privilégié).
2. Opérateurs linéaires d'ordre ≤ 1 en ∇ψ : les seules structures sont ψ, γ5ψ, γ^a∇_a ψ, γ5γ^a∇_a ψ (les termes σ^{ab}R_ab, σ^{ab}γ^c R_abc^d ∇_d, γ^{[a}γ^bγ^{c]}∇... se réduisent à celles-ci via R_abcd ∝ g g et γ^{[abc]} = ε γ5 γ). L'équation la plus générale (lagrangien hermitien) est

```
[ i (A + B γ5) γ^a ∇_a - (m_1 + i m_2 γ5) ] ψ = 0 ,   A, B, m_1, m_2 constantes réelles sur dS,
```

   où les constantes peuvent être des fonctions quelconques (même non polynomiales) des invariants de courbure, par exemple m_1 = m + ξR : elles sont constantes sur dS.
3. En composantes chirales, renormaliser ψ_L, ψ_R par des constantes (A ± B ≠ 0) puis faire une rotation chirale constante e^{iαγ5} ramène à (iγ·∇ - m_eff)ψ = 0 avec m_eff = |m_1 + i m_2| / |A² - B²|^{1/2}, constante. Ces redéfinitions sont constantes en η et préservent la (non-)convergence.
4. Par Q4(a), ∫^∞ m_eff dt = ∞ dès que m_eff ≠ 0 : aucune solution non nulle ne converge en scri+.

Le seul « succès » possible est l'annulation exacte m_eff = 0, par exemple m + ξR = 0 avec ξ = -m/(12H²) : la convergence est alors restaurée, mais au prix d'une masse effective nulle. C'est l'alternative exacte : convergence ⇔ m_eff = 0.

**Classe couverte par l'argument :** couplages (i) locaux et covariants, construits à partir de g seule (courbure, dérivées covariantes, ε, coefficients fonctions arbitraires des invariants de courbure) ; (ii) linéaires en ψ (lagrangien bilinéaire) ; (iii) d'ordre au plus un en dérivées de ψ ; (iv) hermitiens (évolution unitaire). Le résultat reste vrai pour des opérateurs d'ordre supérieur à coefficients constants qui se factorisent en produits (iγ·∇ - m_i) (solutions = sommes de solutions de masses constantes m_i ; il faudrait tous les m_i nuls).

**Hors de la classe (et c'est précisément là que la conclusion peut changer) :**
* couplages au facteur conforme Ω, au temps t, à a(t) ou au champ de vitesse comobile u^a : ce ne sont pas des fonctionnelles locales de g sur dS (ils dépendent du choix du feuilletage plat et de la compactification conforme). La masse m(t) de Q4 est exactement de ce type, et m(t) = m_0 Ω y réalise (c), mais alors la masse physique s'annule en scri+ et seule la masse « rescalée » M = m_0 reste non nulle ;
* champs supplémentaires (scalaire de type Higgs roulant, dilaton) ou masse dynamique ;
* auto-interactions non linéaires (ψ̄ψ)², etc. ;
* couplages non hermitiens (masse complexe) : la norme n'est plus conservée et u se comporte en |η|^{±Im μ}, ce qui ne donne pas génériquement de limite non triviale ;
* écarts à dS exact (sur un FLRW asymptotiquement dS, R(t) → 12H² et la question devient celle de Q4 : la convergence exige ∫ m_eff(t) dt < ∞, donc une masse effective qui tend vers zéro de façon intégrable).

## Récapitulatif des réponses

| Q | Affirmation |
|---|---|
| Q1 | i u' = (α·k + β m/(H\|η\|)) u ; u†u conservée (vrai) ; pour m ≠ 0, pas de limite (faux qu'elle existe), pour tout k et toute solution non nulle : u = e^{iβ(m/H)ln\|η\|}(v_0 + O(\|η\|)). |
| Q2 | (a) faux ; (b) seulement si P- v_0 = 0 ou P+ v_0 = 0 (type particule ou antiparticule pur), avec λ = ±(m/H) ln\|η\| et A_η ~ m/(qHη) non intégrable ; (c) en temps t : e^{±imt}, A' = A ∓ (m/q) dt, régulière ; (d) faux : aucune jauge avec ψ̂ et A tous deux continus (si m ≠ 0). |
| Q3 | ρ̂ = u† h u = m a (n+ - n-) + O(1) → ∞ ; invariante de jauge (vrai) ; terme dominant = énergie de masse au repos de poussière non relativiste, ρ ∝ m a^{-3}, incompatible avec le poids -4. |
| Q4 | (a) ⇔ ∫^∞ m dt < ∞ ; (b) ⇔ m = O(e^{-Ht}) ; (c) ⇔ m = Ω F(Ω), F lisse ; (c) ⇒ (b) ⇒ (a) strictes ; m = e^{-Ht/2} sépare (a) de (b). |
| Q5 | Vrai, indépendante ; Δ⟨T_ab⟩ = T_ab^{cl}[Φ]/⟨f,(1-S)f⟩, Φ = (1-S)f (vide : T^{cl} de la fonction d'onde à une particule normalisée P_+f). |
| Q6 | Non : sur dS exact la classe se réduit à une masse effective constante ; convergence ⇔ m_eff = 0. Classe : local en g, linéaire, ordre ≤ 1, hermitien ; exclus : dépendance en Ω/t/feuilletage, champs externes, non-linéarités. |
