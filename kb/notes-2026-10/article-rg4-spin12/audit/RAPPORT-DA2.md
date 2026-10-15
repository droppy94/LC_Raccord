# RAPPORT DA-2 : audit adverse aveugle de « A massive Dirac field at future conformal infinity » (v2) et de `dirac_scri_check_v2.py`

Date : 2026-10-14. Pièces lues : la consigne `PROMPT-AVEUGLE-DA2.md`, le source `dirac-mass-scri-v2.tex` (en entier), le script `dirac_scri_check_v2.py` (en entier). Aucun autre fichier, aucun document de projet, aucune recherche web. Les références bibliographiques n'ont donc pas pu être contrôlées.

Scripts de contrôle écrits et exécutés dans `/tmp/claude-0/da2/` :

| Script | Objet | Résultat |
|---|---|---|
| `dirac_scri_check_v2.py` (copie) | exécution du script fourni | s'exécute, sorties conformes à la section Verification |
| `t1_bound.py` | borne de la Prop. 1 sur le système 4x4 complet (représentation de Dirac), vecteurs k et données aléatoires | rapport max ‖χ−χ₀‖/(k\|η\|‖χ₀‖) = 0,18 à 0,87 < 1 ; norme conservée à 1e-11 |
| `t2_lemma2.py` | contre-exemples dans la classe littérale du Lemme 2 | (A) solution qui tend vers 0, norme non conservée ; (B) croissance logarithmique |
| `t3_lcdm_bd.py` | (1) couplage de courbure ajusté sur ΛCDM ; (2) mélange de Bogoliubov du mode Bunch-Davies | (1) champ convergent et ρ̂ borné ; (2) \|χ₀⁻\|² = 1/(e^{2πm/H}+1) à 5 chiffres |
| `t4_balanced.py` | donnée tardive équilibrée ‖χ₀⁺‖ = ‖χ₀⁻‖ | ρ̂ reste borné (oscille, ~0,2) |

---

## Conventions vérifiées en préalable

* Métrique : avec a = e^{Ht}, η = −1/(aH), Ω = 1/a = −Hη, on a Ω²a² = 1 : ĝ est bien plat, 𝓘⁺ = {η = 0}, ln Ω = −Ht. Correct.
* Covariance conforme : avec ĝ = Ω²g, ψ̂ = Ω^{−3/2}ψ, l'équation massive donne i∇̸̂ψ̂ = Ω^{−5/2}·mΩ^{3/2}ψ̂ = (m/Ω)ψ̂. Équation (3) correcte.
* Équation de mode (4) : en multipliant par γ⁰ (γ⁰² = 1) on obtient i∂_η u = (α·k + βma)u. Correct, **à condition** que l'algèbre de Clifford soit {γᵃ,γᵇ} = −2gᵃᵇ. Avec la signature (−,+,+,+) et la convention {γ,γ} = +2g, l'équation (i∇̸ − m)ψ = 0 donne (∂ₜ² − ∇² − m²)ψ = 0, c'est-à-dire un tachyon, et γ⁰ n'est pas hermitienne. Le texte ne précise pas la convention (voir C2).
* Densité d'énergie : avec la tétrade e₀ = ∂ₜ de FLRW, ω_t = 0, donc T_tt = Re(ψ† i∂ₜψ) (au signe de convention près, fixé par la positivité pour une particule au repos). Avec ψ = Ω^{3/2}e^{ik·x}u, le terme ∂ₜΩ^{3/2} donne −(3H/2)i|u|²Ω³, imaginaire pur, et il reste Ω⁴u†ℋu. D'où ρ̂ = Ω⁻⁴T_tt = u†(α·k)u + (m/Ω)u†βu. Formule (6) correcte. T̂_ηη = Ω⁻²T_ηη = Ω⁻²a²T_tt = Ω⁻⁴T_tt : l'équivalence annoncée est correcte.
* Section scalaire : (□̂ − R̂/6)φ̂ = Ω⁻²[m² + (ξ−1/6)R]φ̂ ; R = 12H² = 4λ ; m² = 2H² = 2λ/3 ; comportement |η|^{1/2 ± iν}. Tout est correct.
* Ordres de grandeur : H₀√Ω_Λ ≈ 1,44e-33 × 0,83 ≈ 1,2e-33 eV ; m_e/H_∞ = 4,26e38. Correct.
* Ordre des Hankel : en éliminant g, f'' + (k² + m²/η² + im/η²)f = 0, donc ν² = (1/2 − im/H)². L'énoncé « Hankel d'ordre 1/2 ∓ im/H » est correct ; les poids Δ = 3/2 ± im/H aussi.

---

## E1. Lemme 1 et Proposition 1

**Verdict : correct avec correction mineure.**

* Lemme 1 : ℋ(η) hermitien, donc évolution unitaire. Correct (sous la convention de Clifford ci-dessus).
* Borne : u = U₀χ avec U₀ = exp(iβ(m/H)ln Ω) solution exacte pour k = 0 (∫ma dη = −(m/H)ln Ω + c). Alors iχ' = Vχ, V = U₀†(α·k)U₀, ‖V‖ = k car (α·k)² = k². Comme ‖χ‖ = ‖u‖ est constant, ‖χ(η')−χ(η)‖ ≤ k\|η'−η\|‖χ‖ ; χ est de Cauchy, converge vers χ₀ avec ‖χ₀‖ = ‖u‖ ≠ 0, et en passant à la limite η' → 0, ‖χ(η)−χ₀‖ ≤ k\|η\|‖χ₀‖. Argument complet et correct. Vérifié numériquement sur le système 4x4 complet (`t1_bound.py`) : la borne est respectée avec une marge (rapport ≤ 0,87).
* Absence de limite : la composante β = +1 (ou −1) non nulle de χ₀ est multipliée par e^{±i(m/H)ln Ω} ; les deux suites indiquées donnent ±χ₀⁺. Correct pour tout m ≠ 0.
* L'énoncé s'étend sans peine à un paquet d'ondes : U₀ ne dépend pas de k, donc ψ̂ = U₀X(η,x) avec X → X₀ dans L² (si ∫k\|f\|² < ∞). Il serait utile de le dire, puisque la Définition 1 porte sur le champ et non sur un mode.

**Correction demandée (A3 ci-dessous)** : la formule (5) avec exp(iβ(m/H)ln Ω) n'est exacte que sur de Sitter exact. Si H(t) → H_∞ sans être constant, il faut écrire U₀ = exp(−iβθ), θ = ∫m dt ; la preuve passe alors mot pour mot (c'est d'ailleurs ce que fait la Prop. 4). La phrase « Nothing below depends on exact de Sitter » est donc trop forte pour la forme littérale de (5), et toute l'analyse suppose de plus un fond FLRW spatialement plat (décomposition de Fourier, ĝ plat), pas un fond « asymptotiquement de Sitter » au sens général.

## E2. Proposition 2 (jauge)

**Verdict : correct avec corrections mineures (deux erreurs de signe, une généralisation à mentionner).**

* Covariance : avec D = ∂ − ieA, ψ̂ → e^{−iλ}ψ̂, A → A − e⁻¹dλ, on a D'ψ̂' = e^{−iλ}Dψ̂. Correct.
* (a) λ' intégrable ⇒ λ converge ⇒ e^{−iλ} converge vers un nombre de module 1 ⇒ e^{−iλ}u converge ssi u converge. Correct.
* (b) Le bilinéaire u⁺(u⁻)† = e^{2i(m/H)ln Ω}χ⁺(χ⁻)† est invariant par phase commune et n'a pas de limite dès que χ₀⁺, χ₀⁻ ≠ 0. Correct ; l'argument vaut aussi pour λ(η,x) (point par point).
* (c) e^{−iλ}u = (χ⁺, e^{−2iλ}χ⁻) avec ‖χ⁻‖ ≤ k\|η\|‖χ₀‖. Correct.
* Phrase finale : si A est continu jusqu'à 𝓘⁺, A_η est borné donc intégrable et (a) s'applique ; si λ' n'est pas intégrable, A n'est pas continu. La conclusion « no gauge in which both ψ̂ and A extend continuously » est donc correcte, pour un potentiel initial nul et des λ = λ(η). Elle reste vraie pour λ(η,x) par le même argument point par point ; il faut l'écrire, car la Définition 1 parle d'une jauge quelconque.
* **Erreur de signe 1** : avec la règle A → A − e⁻¹dλ et A = 0 au départ, le potentiel transformé est **−e⁻¹dλ = −(m/eH)dΩ/Ω**, et non +e⁻¹dλ. Le module et le caractère non intégrable du pôle ne changent pas.
* **Erreur de signe 2 (lecture physique)** : λ = (m/H)ln Ω = −mt est correct, ψ → e^{imt}ψ est correct, mais A_t → A_t **+** m/e (et non − m/e). Contrôle direct : pour ψ' constant, iγ⁰D_tψ' = eA_tγ⁰ψ' = mψ' impose eA_t = +m. Cohérent avec −(m/eH)dΩ/Ω = +(m/e)dt puisque dΩ = −HΩdt.
* A_η = aA_t (car dt = a dη) qui diverge comme 1/Ω : correct. La remarque sur Dψ̂ ~ m/Ω est correcte (au moins une composante de D_μψ̂ diverge), et elle donne même un énoncé plus fort (pas de jauge C¹).
* Réserve de fond, sans erreur : le résultat suppose un potentiel électromagnétique de départ nul (champ libre couplé à une jauge pure). Un champ de Maxwell physique non trivial n'est pas couvert ; c'est cohérent avec la section 6.

## E3. Proposition 3 et formule (6)

**Verdict : le calcul et l'invariance de jauge sont corrects ; l'affirmation sur l'état à une particule est correcte dans sa conclusion mais l'argument présenté a une lacune (à corriger).**

* Formule (6) : vérifiée (voir Conventions). Invariance de jauge : avec D à la place de ∂, T_ab est invariant. Correct.
* Preuve : Ω·u†(α·k)u ≤ Ωk‖u‖² → 0 ; u†βu = χ†βχ car U₀ commute avec β. Correct. Le script vérifie Ωρ̂ → 0,905606 ; je retrouve indépendamment 1 − 2\|χ₀⁻\|² = 1 − 2(0,21725)² = 0,90561 avec la valeur de \|χ₀⁻\| de la vérification de jauge. Cohérent.
* Remarque : pour des données équilibrées (‖χ₀⁺‖ = ‖χ₀⁻‖) ρ̂ est **borné** (il oscille sans limite). Vérifié (`t4_balanced.py` : ρ̂ ≈ ±0,2 jusqu'à η = −1e-8). La Prop. 3 ne le nie pas, mais cela compte pour la Prop. 5(b) (voir E6).
* **Lacune dans l'argument quantique.** L'identité ω_f(T) − ω(T) = T_classique(f) suppose que f appartient à l'espace à une particule de l'état quasi-libre ω (partie de « fréquence positive » de ω). Or :
  1. Pour l'état de Bunch-Davies (Hadamard), un mode de fréquence positive n'est **pas** « particle-like at late times » : son poids tardif dans β = −1 vaut exactement \|χ₀⁻\|² = 1/(e^{2πm/H}+1) (vérifié numériquement pour m/H = 0,1 ; 0,3 ; 0,6 ; 1, accord à 5 chiffres, `t3_lcdm_bd.py`).
  2. Un état dont l'espace à une particule contient les modes purement β = +1 tardifs est l'état « out », dont les coefficients de Bogoliubov par rapport à Bunch-Davies sont indépendants de k ; il est vraisemblablement non Hadamard (de type α-vide), si bien que « the renormalisation subtraction is the same in both states » perd son objet pour ω(T) lui-même (la différence reste, elle, bien définie). Je n'ai pas démontré ce point de non-Hadamardité ; je le signale comme fragilité.

  **Correction proposée** : prendre ω = Bunch-Davies et f de fréquence positive ; alors Ωρ̂_f → m(1 − 2/(e^{2πm/H}+1))‖f‖² = m·tanh(πm/H)‖f‖² > 0 pour m > 0. Le pôle en 1/Ω subsiste, avec un coefficient explicite, et l'énoncé « one electron suffices » est sauvé pour l'électron de Bunch-Davies (tanh(πm/H) = 1 à 10^{−10^{38}} près pour l'électron).
* **Précision à ajouter** : « independently of how the vacuum contribution is renormalised » est vrai pour la **différence**, pas pour le ρ̂ total. Sur de Sitter, ω(T_ab) = c·g_ab pour un état invariant, d'où ω(T̂_ηη) = −cΩ⁻⁴, divergence bien plus forte que 1/Ω, sauf choix de renormalisation c = 0 (absorption dans Λ). Le critère « rescaled stress tensor bounded » de la Prop. 5(b) exige ce choix ; il faut le dire.

## E4. Lemme 2 (couplages locaux sur de Sitter exact)

**Verdict : faux tel qu'énoncé (contre-exemples dans la classe littérale) ; correct après restriction de la classe.**

La partie « tenseurs invariants » de la preuve est juste : sur de Sitter exact les seuls tenseurs invariants sont g et ε, les scalaires de courbure sont constants, les dérivées de la courbure sont nulles ; les termes d'ordre 0 se réduisent à c₁ + c₂γ₅, les termes d'ordre 1 à (Z₁ + Z₂γ₅)γᵃ∇ₐ (aucun vecteur invariant, donc pas de σᵃᵇ∇_b libre). Mais la classe énoncée (« any modification … built locally from the metric … at most first order ») admet :

1. **Terme cinétique axial dominant, Z₂² > Z₁² (hermitien, coefficients réels).** Après multiplication par (Z₁+Z₂γ₅)⁻¹, on obtient iγ∇ψ = (a + bγ₅)ψ avec a² − b² = (m² + m₅²)/(Z₁² − Z₂²). Pour Z₂² > Z₁² la masse effective est **tachyonique** : U₀ a des valeurs propres Ω^{±\|m_eff\|/H}, la norme n'est pas conservée et il existe une solution qui **tend vers 0** à 𝓘⁺ (extension continue). Vérifié pour Z₁ = 0, Z₂ = 1, m = 0,3, k = 1 (`t2_lemma2.py`, cas A) : valeurs singulières du propagateur ∝ Ω^{∓0,3}, solution décroissante \|u\| = 4,5e-3 à η = −1e-8. La preuve n'exige que Z₁² ≠ Z₂² ; il faut Z₁² > Z₂² (pas de fantôme de chiralité).
2. **Coefficients non hermitiens / complexes.** La preuve écrit « m + i m₅γ₅ » puis « masse réelle √(m²+m₅²) », ce qui suppose m, m₅ réels. Un terme f(R)γ₅ψ à coefficient réel (sans i), avec f(12H²) = m, donne m_eff² = m² − m² = 0 et une matrice de masse nilpotente : croissance en ln Ω pour les données génériques, décroissance en 1/ln Ω pour d'autres (cas B). Des coefficients complexes donnent des facteurs Ω^{±κ/H} réels.
3. **Terme antilinéaire (Majorana)** m_M ψ^c : local, d'ordre 0, coefficient constant, donc dans la classe littérale ; masses propres m ± m_M, un secteur sans masse pour m_M = m. Exclu seulement si l'on impose la linéarité et l'invariance U(1), ce qui est implicite (la section 3.2 couple à l'électromagnétisme) mais non écrit.
4. Cas dégénéré Z₁² = Z₂² : exclu dans la preuve (« when this matrix is invertible ») mais pas dans l'énoncé (on trouve alors ψ ≡ 0 si m ≠ ±im₅). Cosmétique.

**Correction proposée** : « termes linéaires en ψ, invariants U(1), issus d'une action réelle, avec terme cinétique de signe défini (Z₁² > Z₂²) ». Sous ces hypothèses le lemme est correct, avec m_eff² = (m² + m₅²)/(Z₁² − Z₂²) ≥ 0, et la redéfinition constante des chiralités préserve limites et absences de limite.

**Point à ne pas confondre** : même dans la classe corrigée, m_eff peut être **nul** par ajustement fin (par exemple ψ̄(m − ℓR)ψ avec ℓ = m/(12H²)). Le lemme reste vrai (il ne dit rien pour m_eff = 0), mais cela réfute la Prop. 5(c) (voir E6). La phrase de la p. 165 (« cannot remove the obstruction while keeping a non-zero effective mass ») est exacte ; c'est la Prop. 5(c) qui perd le qualificatif.

## E5. Proposition 4 (masse variable)

**Verdict : correct, avec deux compléments mineurs.**

* (a) La preuve de la Prop. 1 s'applique telle quelle (‖V‖ = k ne dépend pas de m) avec U₀ = exp(−iβθ), θ = ∫ma dη = ∫m dt. Pour m ≥ 0 continu, θ est monotone : soit il converge (u converge), soit θ → +∞ et la composante non nulle de χ₀ tourne indéfiniment. La reprise de la Prop. 2 vaut avec λ = −θ (A_η = ma/e non intégrable). Correct. L'hypothèse m ≥ 0 est nécessaire pour la réciproque telle qu'écrite (sinon il faudrait parler de θ et non de ∫m).
* (b) ρ̂ = u†(α·k)u + ma·χ†βχ, avec χ†βχ → ‖χ₀‖² > 0 pour une solution tardive particule : borné ssi ma borné. Correct. Existence des solutions de χ₀ prescrit : assurée par la convergence de la série de Dyson (opérateur d'onde unitaire) ; à mentionner.
* (c) Tautologique (μ = m/Ω), correct.
* Ordre strict : (c) ⇒ (b) (μ lisse donc borné) ⇒ (a) (m ≤ C e^{−Ht} intégrable). (a) ⇏ (b) : m ∝ Ω^{1/2} donne ∫m dt fini et ρ̂ ∝ Ω^{−1/2} ; confirmé par le script (ρ̂ × 10 quand Ω ÷ 100). (b) ⇏ (c) : vrai mais **aucun exemple n'est donné** ; proposer m = Ω(1 + Ω^{1/2}). L'exemple m ∝ 1/t (phase logarithmiquement divergente) est correct.
* Remarque physique : quand ma → 0 (cas (b) strict), le hamiltonien tardif est dominé par α·k, et « particule » ne correspond plus à l'espace propre β = +1. L'énoncé (b) reste mathématiquement juste pour χ₀⁻ = 0, mais l'étiquette « late-time particle solution » perd son sens physique dans ce régime ; préciser.

## E6. Proposition 5 et section 5

**Verdict : la structure conditionnelle est bonne et le ton est globalement proportionné, mais 5(c) est faux tel qu'énoncé et 5(b) a une prémisse insuffisante.**

* 5(a) : découle de la Prop. 2 et de la Prop. 4(a). Correct. Mais c'est un énoncé sur une solution classique non nulle : la prémisse « at least one quantum present » n'est ni nécessaire ni pertinente ici (au niveau opératoriel, le champ ψ̂ lui-même porte la phase U₀ dans n'importe quel état).
* 5(b) : nécessite que le quantum présent ait un contenu tardif non équilibré (‖χ₀⁺‖ ≠ ‖χ₀⁻‖). Pour des données équilibrées, ρ̂ est borné (`t4_balanced.py`). La correction est simple : « au moins un quantum de fréquence positive pour Bunch-Davies (ou particule tardive) », avec le coefficient m·tanh(πm/H) de E3, et en ajoutant le choix de renormalisation c = 0 du vide. La parenthèse « as is needed for the conformal Einstein equations to be posed there » n'est pas démontrée ni référencée : à justifier ou à retirer.
* **5(c) faux tel qu'énoncé.** « With a constant non-zero mass … no local coupling to the geometry of the class of Lemma 2 changes this. » Contre-exemple hermitien, dans la classe même corrigée : ψ̄(m − ℓR)ψ avec ℓ = m/(12H_∞²).
  * Sur de Sitter exact : m_eff = 0, l'équation devient conforme sans masse, ψ̂ et T̂ sont réguliers.
  * Sur le fond de la Prop. 5 (asymptotiquement de Sitter, ici ΛCDM plat, R = 12H_∞² + 3H_∞²(Ω_m/Ω_Λ)a⁻³) : m_eff(t) = −(m/4)(Ω_m/Ω_Λ)a⁻³, donc ∫m_eff dt < ∞, m_eff·a → 0 et m_eff = Ωμ avec μ ∝ Ω² lisse : **les trois conditions de la Prop. 4 sont remplies**. Vérifié numériquement (`t3_lcdm_bd.py`, m = 3, k = 2) : u converge (\|Δu\| = 2e-7 à a = 1e9), ρ̂ constant à −0,24361.
  * De plus 5(c) mélange les cadres : le Lemme 2 est prouvé sur de Sitter exact, la Prop. 5 suppose seulement H → H_∞ ; sur un fond non exact, les couplages de courbure rendent la masse effective dépendante du temps et le Lemme 2 ne s'applique plus.
  * Ce couplage est physiquement exclu (ℓ ~ m/H_∞², masse de l'électron dépendante de la densité locale de matière, d'où violation massive du principe d'équivalence), mais l'énoncé est mathématique. **Correction** : « no coupling of the class with m_eff ≠ 0 on exact de Sitter » et mention explicite de l'ajustement fin m − 12ℓH_∞² = 0, analogue spinoriel de la condition scalaire m² = R/6 de la section 3. La phrase « This makes Penrose's postulate of fading mass a necessary condition » reste vraie si « mass » s'entend « masse effective », ce qu'il faut écrire.
* Le paragraphe de portée (section 6) est honnête et cohérent avec ce qui est démontré, sauf qu'il range le Lemme 2 dans « established » sans les restrictions de E4.

## E7. Script

**Verdict : le script fait ce que la section Verification affirme pour la v2 ; pas de défaut de signe ni de normalisation ; quelques faiblesses de méthode et de documentation.**

* Conventions : bloc d'hélicité i u' = [[M, k],[k, −M]]u, M = m(η)a(η), conforme à (4) en représentation de Dirac (l'autre hélicité, −k, est équivalente). ρ̂ = 2k Re(f̄g) + M(\|f\|² − \|g\|²) = u†(α·k)u + Mu†βu : conforme à (6), normalisation correcte. λ = m ln(−η) = (m/H)ln Ω avec H = 1 : correct.
* Résultats reproduits : jauge (générique : \|g'\| constant 0,21725 / 0,29096 et rotation ; particule pure : f' → 1, \|g'\| ∝ \|η\|) ; énergie (Ωρ̂ → 0,905606) ; masse variable (ε = 1/2 : convergence lente ∝ Ω^{1/2}, ρ̂ ∝ Ω^{−1/2} ; ε = 1 : ρ̂ = 3 exactement, ce qui est trivial car ℋ devient indépendant de η et l'énergie est conservée).
* Faiblesses :
  1. La solution « pure particle » est construite avec χ(η_f) = (1,0) à η_f = −1e-8, pas avec χ₀ ; l'erreur est ≤ k·1e-8, mais la dernière ligne (\|g'\| = 0) est imposée par construction.
  2. Le contrôle d'énergie compare Ωρ̂ à m(\|f\|² − \|g\|²) **au même η** : quasi-tautologique (différence = Ω·2kRe(f̄g)). Il ne compare pas à la limite prédite m(‖χ₀⁺‖² − ‖χ₀⁻‖²) calculée indépendamment (je l'ai fait : accord à 5 chiffres).
  3. Le docstring annonce un contrôle (1) « norm conserved; chi converges » qui n'est pas implémenté dans la v2 (le texte l'attribue à `dirac_scri_check.py`, que je n'avais pas le droit de lire : non vérifié).
  4. Le titre du docstring (« No non-zero rest mass for a Dirac field across future conformal infinity ») ne correspond pas au titre du manuscrit.
  5. Ni la réciproque de 4(a), ni le Lemme 2, ni l'énoncé quantique ne sont testés ; la section Verification ne le prétend pas.

---

## Liste des erreurs classées par gravité

### Bloquante
| # | Lieu | Erreur | Correction |
|---|---|---|---|
| B1 | Prop. 5(c) | Faux tel qu'énoncé : le couplage hermitien ψ̄(m − ℓR)ψ, ℓ = m/(12H_∞²), annule m_eff sur de Sitter exact et, sur ΛCDM, donne m_eff ∝ a⁻³ qui satisfait (a), (b), (c) de la Prop. 4 (vérifié). De plus 5(c) applique un lemme de de Sitter exact à un fond asymptotique. | Restreindre à m_eff ≠ 0 sur de Sitter exact, signaler l'ajustement fin, parler de masse effective. Correction simple, mais indispensable avant diffusion. |

### À corriger
| # | Lieu | Erreur | Correction |
|---|---|---|---|
| A1 | Lemme 2 | Classe trop large : contre-exemples (Z₂² > Z₁² tachyonique, solution → 0 vérifiée ; coefficients non hermitiens ; terme de Majorana antilinéaire) ; l'énoncé omet la condition d'inversibilité. | Linéaire en ψ, U(1)-invariant, action réelle, Z₁² > Z₂² ; m_eff² = (m²+m₅²)/(Z₁²−Z₂²). |
| A2 | §3.3, état à une particule | Les modes « particle-like at late times » ne sont pas dans l'espace à une particule de Bunch-Davies (poids tardif antiparticule 1/(e^{2πm/H}+1), vérifié) ; l'état qui les contient est vraisemblablement non Hadamard. Le ρ̂ total contient −cΩ⁻⁴ du vide sauf si c = 0. | Utiliser Bunch-Davies : Ωρ̂_f → m·tanh(πm/H)‖f‖² > 0 ; préciser que seule la différence est indépendante de la renormalisation et que 5(b) exige c = 0. |
| A3 | Abstract, §2, Prop. 1 | « Asymptotically de Sitter » et « nothing below depends on exact de Sitter » : tout est prouvé sur FLRW spatialement plat, et (5) sous la forme exp(iβ(m/H)ln Ω) n'est exacte que pour H constant. | Énoncer pour FLRW plat avec H → H_∞ et U₀ = exp(−iβ∫m dt). |
| A4 | Prop. 5(a)(b) | Prémisse « at least one quantum present » : inutile pour (a) (énoncé classique), insuffisante pour (b) (données équilibrées ⇒ ρ̂ borné, vérifié). Parenthèse sur les équations d'Einstein conformes non justifiée. | (a) : « une solution classique non nulle » ; (b) : « un quantum de fréquence positive Bunch-Davies (ou particule tardive) » ; justifier ou retirer la parenthèse. |

### Cosmétique
| # | Lieu | Erreur | Correction |
|---|---|---|---|
| C1 | Prop. 2(c) et paragraphe suivant | Signes : le potentiel transformé est −e⁻¹dλ = −(m/eH)dΩ/Ω, et A_t → A_t **+** m/e. | Corriger les deux signes (sans effet sur les conclusions). |
| C2 | §3.1 | Convention de Clifford non dite ; avec (−,+,+,+) il faut {γᵃ,γᵇ} = −2gᵃᵇ pour que (i∇̸ − m)ψ = 0 soit non tachyonique et β hermitien. | L'écrire. |
| C3 | Définition 1 | Φ̂ = Ω^w Φ avec « weight 3/2 » contredit ψ̂ = Ω^{−3/2}ψ (et φ̂ = Ω⁻¹φ). | Φ̂ = Ω^{−w}Φ, ou poids −3/2. |
| C4 | Prop. 2 | Restreinte à λ(η) ; la conclusion vaut pour λ(η,x) par le même argument. | Le dire. |
| C5 | Prop. 4 | Pas d'exemple pour (b) ⇏ (c) ; sens physique de « particle » perdu quand ma → 0. | Exemple m = Ω(1+Ω^{1/2}) ; une phrase. |
| C6 | Prop. 1 | Extension mode → paquet d'ondes (champ) non écrite. | Une phrase (U₀ indépendant de k). |
| C7 | Bibliographie | Clé Friedrich2014 et date (2013) incohérentes ; références non vérifiables ici (pas de web). | Harmoniser. |
| C8 | §3.5 | « coefficient of the pole … electron mass in units of H_∞ » : formulation ambiguë (le coefficient de Ωρ̂ est m‖χ₀‖²). | Reformuler. |
| C9 | Script | Docstring : titre différent du manuscrit ; contrôle (1) annoncé mais absent ; « pure particle » imposée à η_f et non à χ₀ ; contrôle d'énergie quasi tautologique. | Harmoniser le docstring ; comparer Ωρ̂ à la limite calculée indépendamment. |

---

## Verdict global

Le noyau mathématique (Lemme 1, Prop. 1 avec sa borne, Prop. 2, formule (6) et Prop. 3, Prop. 4) est **correct** et je n'ai trouvé aucune erreur de calcul qui l'atteigne ; seules deux erreurs de signe sans conséquence (C1). Le script est fidèle aux conventions du texte et reproduit ce qu'annonce la section Verification.

Les faiblesses sont dans les énoncés de portée : le Lemme 2 est faux pour sa classe littérale (A1) ; la Prop. 5(c) est fausse telle qu'écrite, à cause d'un couplage de courbure ajusté qui supprime la masse effective (B1) ; l'argument « one electron suffices » doit passer par l'état de Bunch-Davies, ce qui le sauve avec le coefficient m·tanh(πm/H) (A2) ; le cadre « asymptotiquement de Sitter » est en réalité FLRW plat (A3). Tout se corrige sans changer la conclusion centrale, qui est conditionnelle : avec une masse effective constante non nulle, ni ψ̂ (avec son potentiel) ni T̂ ne sont réguliers à 𝓘⁺.

**Recommandation : publiable après corrections B1, A1 à A4 et C1 à C3.**
