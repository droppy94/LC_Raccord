# RAPPORT YA-1 : états quasi-libres sur le demi-espace de Minkowski η < 0, dérivation aveugle

Auditeur froid, sans accès au travail antérieur. Aucun fichier lu hors de /home/claude/audit_ya1/. Aucune recherche bibliographique : les théorèmes sont cités de mémoire, avec leur énoncé et leurs hypothèses, et signalés comme tels. Calculs : sympy 1.14, mpmath 1.3, scripts dans /home/claude/audit_ya1/work/ (empreintes en section 6).

Étiquettes : [calculé] = résultat sorti d'un script ; [dérivé] = raisonnement fait ici ; [cité de mémoire] = théorème ou résultat connu, rappelé sans source consultée.

Conventions. Métrique −dη² + dx², champ scalaire sans masse, □ = −∂_η² + Δ. Modes u_k(x) = e^{−ikη + ik·x}/√(2k), k = |k|, mesure d³k/(2π)³. Vide de Minkowski :
H(x, x′) = ∫ d³k/((2π)³ 2k) e^{−ik(η−η′) + ik·(x−x′)} = 1/(4π² [ |x−x′|² − (η−η′ − i0)² ]) [cité de mémoire].
Domaine M⁻ = {η < 0}, Σ_τ = {η = τ} (τ < 0), réflexion R(η′, x′) = (−η′, x′).

---

## 0. Résumé des réponses

| Question | Réponse courte |
|---|---|
| 1 (classe homogène) | Le terme en α_k β_k* dépend de η + η′ (pas de η − η′). T^w ~ 1/η ⟺ N = 3 (coefficient ∝ sin φ). N = 4 : log. N ≥ 5 : limite finie mais seulement C^{N−5}. Lisse en η = 0 pour aucun N fini ; lisse (et même analytique) pour la classe (a). |
| 2 (admissibilité) | supp sing du terme αβ* = {|x − x′| = |η + η′|} : cône de lumière de l'image miroir Rx′. Il rencontre le domaine. Ces états (N fini) ne sont pas Hadamard ; Hadamard ⟺ β_k à décroissance rapide (tous les moments UV finis), et alors w est C^∞ sur R⁴ × R⁴, donc lisse à travers η = 0. |
| 3 (classe générale) | Oui : pour tout état quasi-libre Hadamard sur M⁻, w se prolonge en une bisolution C^∞ sur R⁴ × R⁴, régularité **jointe** en (x, x′), y compris près de la diagonale quand les deux points tendent vers {η = 0}. Deux routes : problème de Cauchy des bisolutions (Kirchhoff) ; ou axiome de tranche temporelle + propagation de la forme de Hadamard (Fulling-Narcowich-Wald / Radzikowski). |
| 4 (conclusion) | Non. Aucun état Hadamard sur M⁻ n'a ∂∂w|_coinc ~ 1/η. Ce qui l'interdit : w est la restriction d'une bisolution lisse globale, donc T^w est une fonction lisse de η sur tout R. Les états qui produisent 1/η (classe b, N = 3) ont une pathologie de localisation : singularités portées par le cône réfléchi (charge image) et singularités de fréquence négative sur le cône de lumière réel. |

Schéma de la géométrie (coupe (η, x¹)) :

```
        η
        ^
        |      Rx' = (-η', x')   <-- image miroir, hors domaine (η > 0)
   η=0  +---------o--------------------  bord futur {η = 0}
        |        / \
        |       /   \      cône de lumière PASSÉ de Rx' :
        |      /     \     |x - x'| = -(η + η')  = |η| + |η'|
        |     /       \    = lieu singulier du terme α β*  (dans le domaine !)
        |    /    x'   \
        |   /     o     \        cône de lumière réel de x' :
        |  /     / \     \       |x - x'| = |η - η'|  = seul lieu singulier
        | /     /   \     \      autorisé par la condition de Hadamard
        +---------------------------------> x
   (domaine physique : η < 0)
```

---

## 1. Classe homogène (états de Bogoliubov)

### 1.1 Partie dépendante de l'état [dérivé], [calculé]

Avec v_k = α_k u_k + β_k u_k*, ω₂(x, x′) = ∫ d³k/(2π)³ v_k(x) v_k*(x′). En développant et en utilisant |α_k|² = 1 + |β_k|² (vérifié symboliquement, script Q1) :

w(x, x′) = ∫ d³k/((2π)³ 2k) { |β_k|² [ e^{−ik(η−η′) + ik·(x−x′)} + e^{+ik(η−η′) − ik·(x−x′)} ]
      + α_k β_k* e^{−ik(η+η′) + ik·(x−x′)} + α_k* β_k e^{+ik(η+η′) − ik·(x−x′)} }.

Le terme en α_k β_k* (et son conjugué) dépend de la somme η + η′ et non de la différence : il brise l'invariance par translation temporelle. Les termes en |β_k|² sont stationnaires. La partie antisymétrique de ω₂ est inchangée (les termes croisés sont symétriques en (x, x′) pour α, β isotropes), ce qui est le contenu de |α|² − |β|² = 1.

Cas isotrope, intégration angulaire (∫dΩ e^{ik·r} = 4π sin(kr)/(kr)), avec r = |x − x′| :

w = (1/4π²) ∫_0^∞ k dk [sin(kr)/(kr)] { 2|β_k|² cos(k(η−η′)) + 2 Re[ α_k β_k* e^{−ik(η+η′)} ] }.

### 1.2 Limites de coïncidence [dérivé], [calculé]

w(x, x) = (1/2π²) ∫_0^∞ k dk { |β_k|² + Re[ α_k β_k* e^{−2ikη} ] }.

Deux dérivées (mesure d³k/(2k), donc k³ dk après intégration angulaire) :
- ∂_η ∂_η′ w|_c = (1/2π²) ∫ k³ dk { |β_k|² − Re[α_k β_k* e^{−2ikη}] }  (car ∂_η∂_η′ e^{−ik(η+η′)} = −k², vérifié symboliquement) ;
- Σ_i ∂_i ∂_i′ w|_c = (1/2π²) ∫ k³ dk { |β_k|² + Re[α_k β_k* e^{−2ikη}] }.

Remarque [dérivé] : pour le champ sans masse en espace plat, la densité d'énergie ρ^w = ½(∂_η∂_η′ + Σ∂_i∂_i′)w|_c = (1/2π²)∫ k³ |β|² dk ne contient pas le terme oscillant ; la pression p^w = (½∂_η∂_η′ − ⅙Σ∂_i∂_i′)w|_c en contient −(2/3) J(η). La quantité pertinente pour la question est donc

J(η) := (1/2π²) ∫_0^∞ k³ Re[ α_k β_k* e^{−2ikη} ] dk,

qui entre dans ∂_η∂_η′ w|_c avec le signe −, dans Σ∂_i∂_i′ w|_c avec le signe +, dans p^w avec −2/3. T^w ~ ∂∂w|_c se comporte, quand η → 0⁻, comme J(η) à une constante près.

### 1.3 Classe (a) : α β* à décroissance plus rapide que toute puissance [dérivé], [calculé]

Si ∫_0^∞ k^{3+m} |α_k β_k*| dk < ∞ pour tout m, la dérivation sous le signe somme est licite à tout ordre : J ∈ C^∞(R), y compris à travers η = 0. De même w(x, x) et w(x, x′) tout entière (voir Q2). Exemples en forme fermée [calculé] :
- α β* = e^{iφ} e^{−k/k_c} : ∫ k³ e^{−k(1/k_c + 2iη)} dk = 6 k_c⁴/(1 + 2iηk_c)⁴, réelle-analytique en η, pôles seulement en η = ± i/(2k_c) ;
- α β* gaussien : fonction entière de η.
Conclusion (a) : w(x, x) et T^w sont lisses (et typiquement analytiques) en η = 0.

### 1.4 Classe (b) : α_k β_k* ~ k^{−N} e^{iφ} [calculé]

Modèle UV : α β* = e^{iφ} k^{−N} pour k ≥ 1 (coupure IR sans effet sur η → 0). Alors

∫_1^∞ k^{3−N} e^{−2ikη} dk = E_{N−3}(2iη), E_n(z) = ∫_1^∞ e^{−zt} t^{−n} dt,

et les développements en z = 2iη → 0 (sympy, vérifiés contre une quadrature oscillante mpmath indépendante à 10⁻¹¹ près ou mieux) donnent :

| N | ∫ k^{3−N} e^{−2ikη} dk, η → 0 | Comportement de J(η) | Régularité en η = 0 |
|---|---|---|---|
| 3 | 1/z − 1 + z/2 + … | J = sin(φ − 2η)/(4π² η) → **sin φ /(4π² η)** | pôle 1/η |
| 4 | −ln z − γ + z + … | −cos φ · ln(2|η|)/(2π²) + saut (π/2) sin φ · sgn η | log (ou saut) |
| 5 | 1 + z(ln z − 1 + γ − iπ) + … | fini ; J′ ~ ln|η| | C⁰, pas C¹ |
| 6 | ½ − z + z²(−½ ln z + …) | fini ; J″ ~ 4 ln|η| (vérifié : pente 4 ln 10 par décade) | C¹, pas C² |
| N | Γ(4−N)(2iη)^{N−4} + … | J ~ Re[e^{iφ} Γ(4−N)(2iη)^{N−4}] | C^{N−5}, pas C^{N−4} |

Vérification numérique [calculé] : pour N = 3, φ = π/2, η·J(η)·2π² = 0,490 ; 0,4999 ; 0,499999 ; 0,49999999 pour η = −10⁻¹ … −10⁻⁴ (limite sin φ/2 = 0,5).

Réponses :
- **T^w ~ 1/η pour N = 3** (générique : coefficient ∝ sin φ ; si α β* est exactement réel à grand k, le pôle disparaît et il reste la correction suivante). Avec N = 3, les termes |β|² ~ k^{−6} donnent une densité de particules ∫k²|β|² et une densité d'énergie ∫k³|β|² finies : l'état est « raisonnable » au sens des nombres d'occupation et pourtant T^w diverge.
- **Limite lisse en η = 0 pour aucun N fini** : la m-ième dérivée de J est ∫ k^{3−N+m} e^{−2ikη} dk, finie en η = 0 ssi m ≤ N − 5 ; à m = N − 4 divergence logarithmique. Donc J ∈ C^{N−5} \ C^{N−4}. La limite est finie (continue) pour N ≥ 5, mais jamais C^∞. Seule la classe (a) donne une limite lisse.
- Pour w(x, x) (mesure k dk) : ∫ k^{1−N} e^{−2ikη} dk = E_{N−1}(2iη) : 1/η pour N = 1, log pour N = 2, fini avec terme η ln|η| pour N = 3 [calculé].

Homogénéité [dérivé] : pour α β* = c k^{−N} exactement, w_{αβ*}(λs, λr) = λ^{N−2} w_{αβ*}(s, r) (s = η + η′, r = |x − x′|) ; deux dérivées ont le degré N − 4 ; à la coïncidence, s = 2η, r = 0, d'où |η|^{N−4}, cohérent avec le tableau.

---

## 2. Admissibilité : support singulier du terme α β* et condition de Hadamard

### 2.1 Support singulier [calculé], [dérivé]

w_{αβ*}(x, x′) = ∫ d³k/((2π)³ 2k) α_k β_k* e^{iΦ} + c.c., Φ(k) = k·(x − x′) − |k|(η + η′).

Pour α β* ~ k^{−N} e^{iφ}, l'amplitude α β*/(2k) est un symbole d'ordre −N − 1 : w_{αβ*} est une distribution intégrale de Fourier (oscillatoire) de phase Φ. Phase stationnaire (sympy) : ∇_k Φ = (x − x′) − k̂ (η + η′) = 0 ⟺ x − x′ = k̂ (η + η′) ⟺ **|x − x′| = |η + η′|**. Hors de ce lieu, la phase est non stationnaire et l'intégrale est C^∞ (intégrations par parties). Sur ce lieu, le symbole homogène d'ordre fini produit une singularité conormale d'ordre fini.

Interprétation : w_{αβ*}(x, x′) = G(x, Rx′) avec Rx′ = (−η′, x′) et G une bidistribution « de type Wightman » à fréquence positive (symbole α β*/(2k) e^{−ik(η − η_y) + ik·(x − x_y)}) : singularité sur le cône de lumière du **point image** Rx′ par réflexion sur l'hyperplan η = 0 (structure de charge image).

Rencontre avec le domaine : pour η, η′ < 0, |η + η′| = |η| + |η′| > 0 ; le lieu |x − x′| = |η| + |η′| est atteint dans M⁻ × M⁻ (ex. η = η′ = −1, |x − x′| = 2). Il ne coïncide avec le cône de lumière réel |x − x′| = |η − η′| que si η η′ = 0, c'est-à-dire sur le bord. Le sommet du cône singulier est en η + η′ = 0, x = x′, soit les deux points coïncidents sur le bord.

Nature de la singularité [calculé] : en forme fermée (N = 3, isotrope, k ≥ 1), avec s = η + η′ et r = |x − x′|,
w_{αβ*}(s, r) = (1/(4π² r)) Im[ e^{−iφ} E_N(−i(r + s)) + e^{iφ} E_N(−i(r − s)) ],
et E_N(z) = … + z^{N−1}(−ln z)/(N − 1)! + … : terme (r + s)^{N−1} ln|r + s|, donc w_{αβ*} est C^{N−2} mais pas C^{N−1} à travers le cône réfléchi. Pour N = 3 : C¹, dérivées secondes à divergence logarithmique. Vérifié numériquement (script Q2, s = −1) : ∂²_r w_{αβ*} en r = 1 ± δ croît de 0,0585 par décade de δ, soit ln 10/(4π²) = 0,0583 ; la même dérivée est finie en r = 0,5, 2, 3 et lisse sur le cône de lumière réel (η = −0,3, η′ = −0,7, r = 0,4) ; ∂_r w est continue.

### 2.2 Ces états sont-ils Hadamard sur le domaine ? [dérivé]

Non, pour tout N fini, et ce pour deux raisons indépendantes.

(i) Le terme |β_k|² ~ k^{−2N} : w_{|β|²} = (1/(2π² r)) ∫ k^{−2N} sin(kr) cos(k(η − η′)) dk est singulier sur le cône de lumière réel |x − x′| = |η − η′| (terme (r − |t|)^{2N−1} ln|r − |t||, C^{2N−2} mais pas C^{2N−1} ; vérifié pour N = 3 : ∂⁵_r diverge logarithmiquement). Ce terme viole déjà la **forme locale** (w doit être C^∞ près de la diagonale) ; au sens microlocal, la partie |β|² u_k*(x) u_k(x′) est à fréquence négative, donc son front d'onde a un covecteur dans V⁻ au premier point, ce qu'exclut la condition spectrale microlocale.

(ii) Le terme α β* porte une singularité sur le cône réfléchi, hors du cône de lumière entre x et x′ : violation de la **forme globale** (Kay-Wald) et de la condition microlocale WF(ω₂) = C⁺ (voir énoncés en Q3). Notons que ce terme seul est lisse au voisinage de la diagonale de M⁻ × M⁻ (la distance de (x, x) au cône réfléchi est 2|η| > 0) : il illustre pourquoi la forme locale seule ne suffit pas sans la positivité (cf. remarque 3.4).

Classe Hadamard [dérivé] : l'état est Hadamard sur M⁻ si et seulement si β_k est à décroissance rapide, au sens ∫_{k≥1} k^m |β_k| d³k < ∞ pour tout m.
- Suffisance : alors |α_k β_k*| = |β_k|√(1 + |β_k|²) est aussi à décroissance rapide, les trois termes de w sont dérivables sous le signe somme à tout ordre : w ∈ C^∞(R⁴ × R⁴), donc ω₂ = H + w est Hadamard sur M⁻ (et sur R⁴), et **w est lisse à travers η = 0** (prolongement évident : la même formule).
- Nécessité : si w est C^∞ sur M⁻ × M⁻, alors à x = x′ et η + η′ = 2τ fixé, la dépendance en t = η − η′ de w est exactement (1/2π²) ∫ k |β_k|² cos(kt) dk (le terme α β* ne dépend pas de t) : transformée de Fourier de la mesure positive k|β_k|² dk. Une transformée de Fourier d'une mesure positive qui est C^{2m} en 0 a un moment d'ordre 2m fini [cité de mémoire, fait classique] ; donc tous les moments UV de |β|² sont finis, puis, par Cauchy-Schwarz (∫ k^m |β| d³k ≤ (∫ k^{2m+4}|β|² d³k)^{1/2} (∫_{k≥1} k^{−4} d³k)^{1/2}), ceux de |β| aussi.
Exemple en forme fermée [calculé] : α β* = e^{iφ} e^{−k/k_c} donne w_{αβ*}(s, r) = (1/(2π² r)) Re[e^{iφ} k_c² r/(k_c² r² + (1 + ik_c s)²)], dont le dénominateur réel est un produit de sommes de carrés : réelle-analytique sur R × R₊ ; le cône réfléchi est repoussé à distance imaginaire s = ± r + i/k_c.

---

## 3. Classe générale : prolongement de w à travers {η = 0}

### 3.1 Cadre et théorèmes utilisés [cité de mémoire]

(T0) Géométrie. M⁻ = {η < 0} ⊂ R⁴ est un ouvert causalement convexe (ensemble passé) de Minkowski, globalement hyperbolique, avec surfaces de Cauchy Σ_τ = {η = τ}, τ < 0 ; chaque Σ_τ est aussi surface de Cauchy de R⁴ (D(Σ_τ) = R⁴). [dérivé, élémentaire]

(T1) Problème de Cauchy pour l'équation des ondes dans R^{1+3}. Pour f₀, f₁ ∈ C^∞(R³) (sans condition de croissance), il existe une unique u ∈ C^∞(R⁴) avec □u = 0, u|_{η=τ} = f₀, ∂_η u|_{η=τ} = f₁ ; elle est donnée par la formule de Kirchhoff u(τ + t, x) = ∂_t[ t M_t f₀(x) ] + t M_t f₁(x), M_t f(x) = (1/4π)∫_{S²} f(x + tν) dν, valable pour t de signe quelconque. Unicité : méthode de l'énergie (vitesse finie de propagation), valable vers le futur comme vers le passé, et sur tout ouvert contenu dans le domaine de dépendance de la surface des données. Dépendance lisse en tout paramètre dont les données dépendent de façon lisse (dérivation sous l'intégrale sphérique). [cité de mémoire ; vérifié sur un exemple polynomial, script Q3 : □u = 0, données reproduites, u polynomiale donc lisse de part et d'autre de η = 0]

(T2) Théorème de propagation des singularités de Hörmander. Soit P un opérateur (pseudo)différentiel à support propre d'ordre m, de type principal réel, de symbole principal p réel ; pour u ∈ D′, WF(u) \ WF(Pu) ⊂ Char(P) = {p = 0} et WF(u) \ WF(Pu) est invariant sous le flot hamiltonien de p (réunion de bicaractéristiques maximales dans Char(P) \ WF(Pu)). Pour P = □ : Char = covecteurs nuls, bicaractéristiques = géodésiques nulles portant leur covecteur transporté parallèlement. [cité de mémoire]

(T3) Théorème de Radzikowski (1996). Sur un espace-temps globalement hyperbolique (M, g), soit ω₂ une bidistribution bisolution de l'équation de Klein-Gordon dont la partie antisymétrique est iE/2 (E = propagateur avancé moins retardé, commutateur correct). Sont équivalents : (i) ω₂ est de forme de Hadamard globale (au sens de Kay-Wald : forme locale H + w avec w lisse, sur un voisinage causal normal d'une surface de Cauchy, pour toutes les paires de ce voisinage) ; (ii) WF′(ω₂) = C⁺ := {(x, k ; x′, k′) ∈ T*M × T*M \ 0 : (x, k) ∼ (x′, k′), k ∈ V⁺_x}, où ∼ signifie qu'une géodésique nulle joint x à x′ en transportant k sur k′ (ou x = x′, k = k′ nul). Corollaire : la différence de deux fonctions à deux points Hadamard sur le même M est C^∞(M × M) (WF(ω₂ − ω₂′) ⊂ C⁺ et, par symétrie de la différence, ⊂ C⁻ ; C⁺ ∩ C⁻ = ∅). La paramétrix H est unique modulo C^∞. [cité de mémoire]

(T4) Propagation de la forme de Hadamard (Fulling, Narcowich, Wald, 1981 ; preuve microlocale par Radzikowski via T2). Si ω₂ (bisolution, commutateur correct) est de forme de Hadamard dans un voisinage causal normal d'une surface de Cauchy Σ d'un espace-temps globalement hyperbolique, elle est de forme de Hadamard globale sur M. [cité de mémoire]

(T5) Axiome de tranche temporelle (Dimock, 1980). Si O ⊂ M est un ouvert causalement compatible contenant une surface de Cauchy de M, l'algèbre CCR A(O) coïncide avec A(M). Ici A(M⁻) = A(R⁴). Un état quasi-libre sur A(M⁻) est donc un état quasi-libre sur A(R⁴), et sa fonction à deux points sur R⁴ est l'unique bisolution prolongeant ω₂|_{M⁻×M⁻}. [cité de mémoire]

### 3.2 Argument général, route A (problème de Cauchy pour les bisolutions) [dérivé]

Hypothèse : ω état quasi-libre Hadamard sur M⁻ (forme locale ou microlocale, voir remarque 3.4), ω₂ = H + w. Par (T3) appliqué sur M⁻ (H|_{M⁻×M⁻} est Hadamard sur M⁻), w ∈ C^∞(M⁻ × M⁻), symétrique, bisolution : □_x w = □_{x′} w = 0.

Étape 1 : données de Cauchy de w sur Σ_τ × Σ_τ (τ < 0) : d_ab(y, y′) = ∂_η^a ∂_η′^b w|_{η=η′=τ}, a, b ∈ {0, 1}, lisses sur R³ × R³.

Étape 2 : construction. Pour y ∈ R³ fixé, soit F₀(y, ·) la solution globale (T1) en x′ de données (d₀₀(y, ·), d₀₁(y, ·)) et F₁(y, ·) celle de données (d₁₀(y, ·), d₁₁(y, ·)) ; F₀, F₁ ∈ C^∞(R³ × R⁴) (dépendance lisse en y). Pour x′ ∈ R⁴ fixé, soit w̃(·, x′) la solution globale en x de données (F₀(·, x′), F₁(·, x′)) sur Σ_τ. Alors w̃ ∈ C^∞(R⁴ × R⁴), □_x w̃ = 0 par construction et □_{x′} w̃ = 0 car l'opérateur de résolution en x commute avec □_{x′} (dérivation sous l'intégrale de Kirchhoff) et □_{x′}F_a = 0. w̃ = (E ⊗ E)(données), E opérateur de Kirchhoff.

Étape 3 : identification. Pour x′ ∈ M⁻ fixé et y ∈ R³, les fonctions F₀(y, ·) et w((τ, y), ·) sont deux solutions en x′ sur M⁻ de mêmes données sur Σ_τ ⇒ égales sur M⁻ (unicité, T1 et T0). Idem F₁(y, ·) = ∂_η w((τ, y), ·). Donc pour x′ ∈ M⁻ fixé, w̃(·, x′) et w(·, x′) ont mêmes données sur Σ_τ ⇒ égales sur M⁻. Conclusion : w̃|_{M⁻×M⁻} = w.

Résultat : **w se prolonge en une bisolution w̃ ∈ C^∞(R⁴ × R⁴)**, et ω̃₂ = H + w̃ est la fonction à deux points d'un état Hadamard sur tout Minkowski prolongeant ω (positivité : ω̃₂ est déterminée par les mêmes données symplectiques que ω₂ via T5, donc est positive).

### 3.3 Route B (tranche temporelle + propagation de Hadamard) [dérivé à partir de T3, T4, T5]

Par (T5), ω s'étend en un unique état quasi-libre ω̃ sur A(R⁴) ; ω̃₂ est une bisolution sur R⁴ × R⁴ de commutateur correct, égale à ω₂ sur M⁻ × M⁻. M⁻ est un voisinage (causal normal, ou en contient un) de la surface de Cauchy Σ_τ de R⁴, sur lequel ω̃₂ est de forme de Hadamard ; par (T4) ω̃₂ est Hadamard sur R⁴. Par (T3), w̃ = ω̃₂ − H ∈ C^∞(R⁴ × R⁴), et w̃|_{M⁻×M⁻} = w. Même conclusion, par des théorèmes « lourds » ; la route A est élémentaire et autosuffisante.

### 3.4 Régularité jointe, et portée des hypothèses [dérivé]

- Régularité **jointe** : les deux routes donnent w̃ ∈ C^∞(R⁴ × R⁴), c'est-à-dire la régularité jointe en (x, x′), y compris sur la diagonale {x = x′} ∩ {η = 0} et dans tous ses voisinages ; en particulier toutes les limites de coïncidence ∂^α_x ∂^β_{x′} w̃(x, x) sont des fonctions C^∞ de x ∈ R⁴. L'argument ne se contente pas de la régularité en chaque variable séparément : la construction E ⊗ E agit sur des données lisses jointes et la formule de Kirchhoff itérée est manifestement lisse en (x, x′) ; la route B donne directement w̃ ∈ C^∞ du produit.
- Forme locale vs globale : si l'hypothèse est seulement la forme locale (w lisse près de la diagonale de M⁻ × M⁻), il faut passer à la forme globale sur M⁻. Théorème local-vers-global (Radzikowski, avec appendice de Verch, 1996) [cité de mémoire] : pour un **état** (positivité !) quasi-libre de forme de Hadamard locale sur un espace-temps globalement hyperbolique, la forme est globale ; la positivité sert via l'inégalité de Cauchy-Schwarz, qui contrôle le front d'onde hors diagonale par le front d'onde sur la diagonale ; ensuite (T2) propage. L'exemple H + w_{αβ*} (sans les termes |β|², donc non positif) de la section 2 montre que l'hypothèse de positivité est nécessaire : il est localement Hadamard près de la diagonale de M⁻ mais porte la singularité du cône réfléchi.
- Pas d'homogénéité requise ; l'argument vaut pour tout état quasi-libre Hadamard sur M⁻, et plus généralement pour tout espace-temps globalement hyperbolique dans lequel M⁻ s'inclut de façon causalement compatible en contenant une surface de Cauchy du grand espace (ici R⁴).
- Ce qui n'est **pas** couvert : des états définis seulement sur un sous-ensemble de M⁻ qui ne contient aucune Σ_τ entière (par ex. un diamant) ; des états non quasi-libres (la condition de Hadamard porte alors sur ω₂ et le résultat sur w reste vrai pour ω₂, mais les fonctions à n points ne sont pas contraintes par cet argument) ; des bords où {η = 0} serait une vraie frontière de l'espace-temps (conditions au bord) et non un hyperplan intérieur de Minkowski.

---

## 4. Conclusion : existe-t-il un état Hadamard sur M⁻ avec ∂∂w|_coinc ~ 1/η ?

**Non.** [dérivé] Par la section 3, pour tout état quasi-libre Hadamard sur M⁻, w = w̃|_{M⁻×M⁻} avec w̃ ∈ C^∞(R⁴ × R⁴). Donc T^w(x) := (∂∂ w̃)(x, x) est une fonction C^∞ de x sur R⁴ : elle a une limite finie en η → 0⁻, se prolonge lisse à η > 0, et ne peut diverger comme 1/η (ni comme un log, ni avoir de saut). Illustration [calculé] : β_k = 0,5 e^{−k}, α_k = √(1+β²) e^{−iπ/3} : T^w_{ηη′}(η) = −0,0724 ; −0,0714 ; −0,0703 pour η = −10⁻³, 0, +10⁻³, continu et lisse à travers le bord.

Propriété qui l'interdit : la condition de Hadamard sur M⁻ (singularités de ω₂ sur le seul cône de lumière, à fréquence positive) plus le fait que M⁻ contient une surface de Cauchy de Minkowski ; par le problème de Cauchy (ou par tranche temporelle et propagation de Hadamard), w est entièrement déterminée par ses données lisses sur Σ_τ × Σ_τ et ne « voit » pas le bord η = 0, qui n'est pas une singularité de l'espace-temps mais une hypersurface intérieure.

Pathologie des états qui produisent 1/η [dérivé], [calculé] : d'après la section 1, la divergence ∂∂w|_c ~ 1/η exige un terme de Bogoliubov α_k β_k* ~ k^{−3} e^{iφ} (sin φ ≠ 0), ou plus généralement une w non lisse. Ces états ont :
1. une singularité de w sur le **cône réfléchi** |x − x′| = |η + η′| (cône de lumière de l'image miroir de x′ par η → −η) : c'est une singularité de type charge image, portée par des paires de points qui ne sont pas reliées par une géodésique nulle ; le sommet de ce cône singulier est le point de coïncidence sur le bord, et la limite de coïncidence à η → 0⁻ s'en approche à distance 2|η|, d'où, par homogénéité de degré N − 2 = 1 de w_{αβ*}, la loi ∂∂w ~ |η|^{N−4} = 1/η ;
2. une singularité de **fréquence négative** sur le cône de lumière réel, due aux termes |β_k|² ~ k^{−6} (C⁴ mais pas C⁵) ;
3. en termes de front d'onde : WF(ω₂) ⊄ C⁺ ; il contient des covecteurs dans V⁻ sur le cône réel et des points hors de la relation ∼ (cône réfléchi). Ce sont les états « adiabatiques d'ordre fini » plutôt que Hadamard : nombre de particules et densité d'énergie finis pour N = 3, mais pression (et toute quantité sensible au terme α β*) divergente à l'approche du bord. Le bord η = 0 n'y joue aucun rôle géométrique : la divergence est un artefact du choix d'état (phase α β* figée au bord, e^{−ik(η+η′)} se synchronisant en η = η′ = 0), et un tel état est tout aussi non-Hadamard loin du bord.

Pour ces états, w ne se prolonge pas en fonction lisse à travers η = 0 ; il se prolonge en revanche comme distribution (la même formule de modes), mais avec la singularité du cône réfléchi qui traverse η = 0 et dont le sommet est sur le bord.

---

## 5. Points de vigilance signalés par l'auditeur

- Le coefficient du pôle 1/η pour N = 3 est proportionnel à sin φ (phase relative de α β* à grand k) ; pour une phase réelle exacte, le pôle disparaît mais la non-régularité demeure (terme suivant).
- La densité d'énergie du champ sans masse en espace plat est insensible au terme α β* ; c'est la pression (ou ∂_η∂_η′ w, ou Σ∂_i∂_i′ w pris isolément) qui porte le 1/η. L'énoncé « T^w ~ ∂∂w » doit donc être lu composante par composante.
- Le théorème local-vers-global requiert la positivité ; sans elle, une bisolution localement Hadamard peut porter une singularité de type cône réfléchi (exemple explicite ci-dessus).
- Tous les énoncés de théorèmes sont cités de mémoire ; les hypothèses rappelées (global hyperbolicité, commutateur correct, positivité pour le local-vers-global, données lisses sans condition de croissance pour Kirchhoff) sont celles que je tiens pour exactes, à vérifier sur les sources avant usage formel.

---

## 6. Empreintes SHA-256 [calculé]

```
3989bda6869eb536d2651c92006279d3f770d5e9f48db27a063bccaebab5b179  PROMPT-AVEUGLE-YA1-ETAT-HADAMARD.md
971d37c02bf6b04810f43dfc4a06a6cccab95e1e168cb9c5f1b9444720f7d00d  work/ya1_q1_homogene.py
b2bc056b846d06e605b26272051139ed99d8befb306818eb700690128c3c8851  work/ya1_q1_homogene.out
67b6876620b2a2a4454a5741e7d1898193f3d9a4b6ea7fddf6093261051bd7c2  work/ya1_q2_support_singulier.py
03af5223d8dc7676d13a970899bd26ce32d2baf91795d2369c23fc2ae04e2b94  work/ya1_q2_support_singulier.out
73ea5ae8d7a1dfb6d29831bc7f245c23e58da0a2269901dc6f9c855d49376b5c  work/ya1_q3q4_prolongement.py
fc49e0f4f0bf71502badf38c9836918ab2de3ffcf1d1c88a4586db05f1a7628c  work/ya1_q3q4_prolongement.out
```

Contenu des scripts : Q1 = structure de w, formes fermées E_n(2iη), développements, quadrature oscillante de contrôle, régularité C^{N−5}, classe (a) ; Q2 = phase stationnaire, forme fermée de w_{αβ*}(s, r), divergence logarithmique de ∂²_r w sur le cône réfléchi, lissité sur le cône réel, terme |β|², classe (a) analytique ; Q3/Q4 = vérification □w = 0, formule de Kirchhoff sur données polynomiales, T^w à travers η = 0 pour un état Hadamard explicite, et le pôle 1/η de l'état N = 3.
