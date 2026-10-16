# Rapport VA-1 : vérification mathématique indépendante de ARTICLE-v2.5.tex

Auditeur isolé. Seuls ont été ouverts : la consigne PROMPT-AVEUGLE-VA1.md, l'article ARTICLE-v2.5.tex et mes fichiers de /home/claude/V25/auditv25/work_va1/. La note compagnon \cite{Companion}, les scripts cités dans la section « Verification » et les références bibliographiques n'ont pas été consultés : ce qui en dépend est signalé comme non vérifiable ici.

## Scripts (dans work_va1/)

| Script | Contenu | Sortie |
|---|---|---|
| `va1_sympy_algebra.py` | Clifford, hermiticité de α, équation de mode (3), tenseur T_{μν} d'un mode plan, trace, relation de dispersion du Lemme 2, termes σ de l'annexe | `va1_sympy_algebra.out` |
| `va1_sympy_Tij.py` | forme exacte de T_ij | `va1_sympy_Tij.out` |
| `va1_desitter_numerics.py` | Prop. 1 (norme, borne), Remarque 1 (série de Frobenius, interférence), poids Bunch-Davies, paquet d'ondes (tanh), composantes en poids poussière | `va1_desitter_numerics.out` |
| `va1_flrw_varmass.py` | FLRW a = t^p (H → 0), Prop. 4 et ses exemples, ordres de grandeur | `va1_flrw_varmass.out` |

Python 3.13.16, sympy 1.14.0, numpy 2.5.3, scipy 1.18.1, DOP853 (rtol 1e-11, atol 1e-13).

## Synthèse

| Classe | Nombre | Points |
|---|---|---|
| Erreur (énoncé faux tel qu'écrit) | 3 | E1 Remarque 1 (« si et seulement si » de l'interférence) ; E2 §5 contre Remarque 2(4) (cas k = 0) ; E3 Remarque 2(1) contre Définition 1(c) |
| Correction (imprécision, preuve incomplète) | 12 | C1 à C12 |
| Remarque | 10 | R1 à R10 |

Aucun résultat central n'est renversé. Les Propositions 1, 2, 3 et 4(a)(b) sont démontrées correctement dans leur cadre ; le poids 1/(e^{2πm/H}+1) et la formule en tanh sont confirmés numériquement à 1e-7 près. Les erreurs portent sur des formulations « si et seulement si » ou « pour toute solution » trop larges, et sur une incohérence interne entre la §5 et la Remarque 2.

---

## V1. Définition 1 et cohérence d'usage

**Vérifié.** Les trois exemples (sin(ln|η|), |η|^{-1/2}, |η|^{1/2}) sont corrects. La convention de jauge (b) est cohérente avec D = ∂ − ieA : D'(e^{−iλ}ψ̂) = e^{−iλ}Dψ̂ pour A' = A − e^{−1}dλ. L'argument « potentiel régulier ⇒ λ' borné » de la dernière phrase de la Prop. 2 n'utilise que (b) et est correct.

**C1 (correction). « Pôle simple » n'est pas défini.** La Définition 1 ne définit ni « pôle simple » (Prop. 3) ni « régulier » pour une densité (§ poids). Si « pôle simple » signifie Ωρ̂ → c ≠ 0, le « si et seulement si » de la Prop. 3 est tautologique. S'il signifie ρ̂ = c/Ω + O(1), le sens réciproque (c = 0 ⇒ ρ̂ borné) n'est pas démontré : la preuve donne seulement la limite de Ωρ̂, et la borne (4) donne m a·O(k|η|), qui n'est pas bornée en général (a|η| → ∞ pour a = t^p). L'énoncé est néanmoins vrai : sur de Sitter il découle de la Remarque 1 (le terme d'interférence de u†βu commence à l'ordre Ω¹, voir E1) ; sur FLRW, une intégration par parties de la phase e^{2iθ} (pour a monotone) donne un reste O(k). Numériquement, pour a = t^{1.5}, t², t³ et une solution avec ‖χ₀⁺‖ = ‖χ₀⁻‖, max|ρ̂| ≈ 0.90 ≈ k alors que a|η| atteint 6000 (`va1_flrw_varmass.out`). À ajouter : définition et argument.

**C2 (correction). Lissité en η ou en Ω.** La Déf. 1 définit la lissité en η. La Prop. 4(c) et la Remarque 2(1) disent « μ lisse jusqu'à Ω = 0 ». Avec a seulement C¹, Ω(η) = 1/a n'est pas forcément C^∞ en η ; les deux notions ne coïncident que sur de Sitter, ou si Ω(η) est un difféomorphisme lisse près de 0. Préciser la variable.

**E3 (erreur mineure). Remarque 2(1) contre Définition 1(c).** La Déf. 1(c) n'exclut que les puissances négatives, ln Ω et exp(ic ln Ω). Avec m = Ω(1 + Ω^{1/2}), le coefficient m/Ω = 1 + Ω^{1/2} ne contient rien de cela : il est formellement régulier au sens littéral de 1(c), alors que μ = 1 + Ω^{1/2} n'est pas lisse. Le « si et seulement si μ lisse » de la Remarque 2(1) est donc faux au sens de la définition donnée. Correctif : exiger dans 1(c) une dépendance lisse (ou analytique) en Ω des seconds membres.

## V2. Proposition 1 (FLRW) et Remarque 1

**Proposition 1 : correcte sous les hypothèses du §2.** Seuls servent la continuité de a et la finitude du temps conforme. V = U₀†(α·k)U₀ est hermitien et ‖V‖ = k. ‖χ(η') − χ(η)‖ ≤ k|η' − η|‖χ‖ donne une suite de Cauchy, puis la borne (4) quand η' → 0. Absence de limite : θ = mt est continu et tend vers l'infini. L'équation (3) a été vérifiée sous sympy à partir de (iD̸ − m a)u = 0 avec {γ^a,γ^b} = −2η^{ab}. Numériquement (de Sitter) : la norme est conservée à 2e-11 près, et le rapport ‖χ − χ₀‖/(k|η|‖χ₀‖) vaut au plus 0.87, donc ≤ 1. La relation −θ = (m/H) ln Ω est correcte.

**Remarque 1 : correcte pour l'essentiel.** Le résidu iβm/H a pour exposants ±im/H, de différence 2im/H non entière. Sous la récurrence de Frobenius n X − iμ[β, X] = iK P_{n−1}, on trouve ‖P_n‖·n!/k^n borné (0.24, 0.22, 0.20, 0.19 pour n = 5, 10, 20, 40), donc P est entière. La série coïncide avec l'intégration à 1.3e-11 près. Les poids de bord 3/2 ± im/H sont corrects.

**E1 (erreur). Interférence « si et seulement si ».** La Remarque affirme que, pour *tout* bilinéaire u†Xu, le terme d'interférence est présent si et seulement si χ₀⁺ et χ₀⁻ sont tous deux non nuls. C'est faux pour X = 1 : u†u est constant (Lemme 1), donc P₊†P₋ ≡ 0. Numériquement, les coefficients de Ω⁰ à Ω⁵ de P₊†P₋ sont ≤ 3e-17. Pour X = β, le terme commence à l'ordre Ω¹ ; pour X = α₁, à l'ordre Ω⁰. Correctif : « seulement si », ou « pour un X générique ».

**C3 (correction). Normalisation et justification.**
- (i) P_±(0) = χ₀^± n'est exact que si θ = −(m/H) ln Ω, sans constante additive. Sinon P_±(0) = e^{±ic}χ₀^±. La Prop. 1 laisse θ défini « à une constante près ».
- (ii) L'argument « exposants invariants modulo les entiers » relève de la monodromie, donc d'un V analytique. Pour V seulement C^∞, il faut un autre argument, d'ailleurs plus simple : si χ' = B χ avec B lisse en 0, alors χ converge, donc u = Vχ converge si V est continu en 0, ce qui contredit la Prop. 1. Il faut aussi supposer V inversible.
- (iii) Le cas « V indépendant de k » est vrai. Preuve que je propose : à k = 0, V = Ω^{iμβ}M avec M lisse et inversible, d'où V⁻¹α_jV = M⁻¹α_jΩ^{2iμβ}M, qui n'est pas lisse.

## V3. Proposition 2

**Hypothèse de charge** : correctement posée (e ≠ 0, couplage minimal). Le cas neutre est bien exclu.

**(a), (b), (c) et la dernière phrase : preuves correctes.**
- (a) λ' intégrable ⇒ λ converge.
- (b) Si e^{−iλ}u convergeait, les rapports de composantes non nulles feraient converger e^{−2iθ}, ce qui est absurde.
- (c) e^{−iλ}u = (χ⁺, e^{2iθ}χ⁻) avec ‖χ⁻‖ ≤ k|η|‖χ₀‖.
- Dernière phrase : un potentiel régulier impose A'_η continu jusqu'en 0, donc λ' borné, donc (a) s'applique.

**Signes du potentiel : corrects.**
- λ = −θ donne A' = e^{−1}dθ = (m a/e)dη.
- Sur de Sitter, dΩ = −H dη, d'où A' = −(m/eH)dΩ/Ω.
- Le pôle n'est pas intégrable : ∫ m a dη = ∫ m dt = ∞, et ce sur tout FLRW, pas seulement sur de Sitter.
- En repère physique, A_t → A_t + m/e et A_η = a A_t : signes cohérents.

**C4 (correction).**
- (i) Les signes « positif pour une particule, négatif pour une antiparticule » (Prop. 3) supposent m > 0, alors que la Prop. 1 dit m ≠ 0.
- (ii) La Prop. 2(c) ne traite que χ₀⁻ = 0. Le cas symétrique (χ₀⁺ = 0, λ = +θ, potentiel opposé) mérite une phrase.
- (iii) Le champ chargé est traité comme champ test dans un A extérieur nul. Le courant qu'il source dans les équations de Maxwell n'est pas discuté, alors que la Déf. 1(b) parle du « champ chargé ». À signaler explicitement.

## V4. Proposition 3, formule (7), dépendance au poids

**Formule (7) : vérifiée.** Pour le tenseur symétrisé en forme cinétique d'un mode plan sur ĝ plat, on a T_ηη = u†(α·k + βma)u, au signe global de convention près. Le terme en dΩ^{3/2}/dt est imaginaire pur et disparaît, comme le dit l'article. Ω^{−4}T_tt = Ω^{−2}T_ηη. La preuve de la Prop. 3 est correcte (U₀ commute avec β, ‖α·k‖ = k).

**Poids poussière : correct**, avec les précisions suivantes.
- Ω^{−3}T_tt = Ωρ̂ → m(‖χ₀⁺‖² − ‖χ₀⁻‖²). Numériquement : 0.334846 aux trois instants, égal à la limite prédite.
- Calcul exact (sympy) : T_ηi = −k_i|u|², constant et sans masse ; T_ij = ½(k_i u†α_j u + k_j u†α_i u), sans masse ; trace = −m a ψ̄̂ψ̂. La justification {α_i, β} = 0 est correcte pour T_ηi. Pour T_ij, la masse est absente parce qu'il n'y a pas de dérivée temporelle.

**C5 (correction). Repère des « autres composantes ».**
- L'affirmation « O(Ω) pour toute solution » est vraie pour les composantes en repère orthonormé physique, ou pour Ω·T̂_ab = Ω^{−1}T_ab en coordonnées (η, x).
- Elle est fausse pour la composante coordonnée Ω^{−3}T_ti, qui vaut T̂_ηi = O(k), d'ordre 1. Préciser le repère.
- Seules les T_ij portent l'interférence ; T_ηi = −k_i|u|² n'en a jamais. Numériquement, T_η3 est constant à 4e-11 près et T_33 oscille dans [−0.67, 0.67] sans limite.
- « Bornées et sans limite » qualifie le facteur Ω^{∓2im/H}, pas les composantes, qui tendent vers 0. La densité Ωρ̂ a une limite mais n'est pas C¹ en Ω pour une solution à deux exposants : terme Ω^{1∓2iμ}. Elle est donc « régulière » au sens de la continuité seulement.

**Séries entières pour une solution à un seul exposant : correct.** u = Ω^{iμ}P₊ avec P₊ entière, donc u†Xu = P₊†XP₊.

**R1 (remarque).** À k = 0, aucune composante du tenseur ne porte d'interférence : T_ηi = 0, T_ij ∝ k et u†βu est diagonal par blocs. La phase relative de la Prop. 2(b) existe pourtant (invariante de jauge). La phrase « ce qui est indépendant du choix de variable est l'interférence, contenu invariant de jauge de la Prop. 2(b) » ne vaut donc, côté tenseur, que pour k ≠ 0. Voir aussi E2.

## V5. Version quantique

**État de Slater : correct.**
- f ∈ ran(1−P) normalisée donne ‖a*(f)Ω_ω‖² = 1.
- Les annihilations annoncées se vérifient par les CAR : a(g)a*(f)Ω = ⟨g,f⟩Ω = 0 pour g ⊥ f, et a*(f)² = 0.
- P + |f⟩⟨f| est un projecteur (f ⊥ ran P), donc l'état est pur et quasi-libre (état de Fock de la nouvelle polarisation, unique).
- La différence des deux-points est de rang un, ⟨h,f⟩⟨f,g⟩ (« au signe de convention près » est honnête).

**C6 (correction). Hypothèses possiblement incompatibles.** On exige à la fois f ∈ ran(1−P) et des données de Cauchy lisses à support compact. En Minkowski, ces deux conditions sont incompatibles (théorème de Hegerfeldt : un état d'énergie positive n'est pas strictement localisé). Pour l'état de Bunch-Davies, les paquets de modes de fréquence positive utilisés ensuite ne sont pas, en général, à support compact. Correctif : f = (1−P)g avec g à support compact. f est alors lisse, puisque le noyau de Hadamard appliqué à une fonction test donne une solution lisse, et la différence f(x)f(y)† reste lisse. Plancherel demande en outre ∫k|F|² < ∞ pour échanger limite et intégrale (convergence dominée : |Ωρ̂_k| ≤ Ωk + m).

**Axiome de Wald, statut de Bunch-Davies.**
- L'usage est logiquement correct : différence lisse ⇒ ω_f(T) − ω(T) = T[f], indépendamment de la prescription.
- Le statut de BD est exposé prudemment : restriction Hadamard par localité, identification au vide des modes de fréquence positive au passé, conditionnelle et annoncée comme telle.
- Les citations précises (Déf. 4.1 et Th. 4.1 de DHP2009, DHP2010, Allen-Lütken) ne sont pas vérifiables sous isolement.

**Poids et formule en tanh : confirmés numériquement.** Méthode : mode d'énergie positive instantanée en η₀ = −4000/k, intégré jusqu'à η = −10⁻⁸/k, poids |χ₀⁻|²/|χ₀|².

| m/H | poids numérique (6 cas : 3 k, 2 hélicités) | 1/(e^{2πm/H}+1) | écart relatif max | 1−2w | tanh(πm/H) |
|---|---|---|---|---|---|
| 0.2 | 2.215534e-01 | 2.215533e-01 | 4e-8 | 0.556893 | 0.556893 |
| 0.5 | 4.142383e-02 | 4.142383e-02 | 5e-8 | 0.917152 | 0.917152 |
| 1.0 | 1.863963e-03 | 1.863962e-03 | 7e-7 | 0.996272 | 0.996272 |
| 2.0 | 3.487455e-06 | 3.487330e-06 | 4e-5 (erreur adiabatique initiale) | 0.999993 | 0.999993 |

Le poids est indépendant de k et de l'hélicité ; c'est attendu, puisque l'équation ne dépend que de kη. Le terme croisé ⟨χ_{k,+}, βχ_{k,−}⟩ entre hélicités de même k est nul : les spineurs d'hélicité sont orthogonaux. Plancherel est donc licite dans la base d'hélicité. Pour un paquet discret de 5 vecteurs k aléatoires × 2 hélicités, on obtient ΩE/‖f‖² = 0.458576 = m tanh(πm/H) pour m/H = 0.5.

**Absence de signe ponctuel : confirmée.** Le terme croisé χ_k†βχ_{k'} entre deux k distincts vaut 0.858 + 0.425i : complexe, de phase quelconque, d'où des franges de signe variable en x.

**C7 (correction).** « Pour tout autre état quasi-libre pur Hadamard, même argument avec le poids de cet état » suppose un état invariant par translation, pour avoir un poids par k, et diagonal en hélicité. Sinon il n'y a pas de « poids » et des termes croisés survivent. Le poids peut aussi dépendre de k, et la positivité n'est plus garantie.

## V6. Lemme 2 et Annexe A

**Tenseurs invariants : correct.** Sur de Sitter, ∇Riem = 0 et Riem s'écrit avec g. Tout tenseur construit localement à partir de la métrique (avec ε, si l'on admet l'orientation) est un polynôme en g et ε à coefficients constants. Il n'y en a donc aucun de rang 1 ni de rang 3. Il n'existe pas de vecteur pour Γ = 1, γ₅ avec ∇. σ^{ab}g_ab = 0. ε_{abcd}σ^{ab} laisse deux indices, qu'aucun tenseur de rang 2 antisymétrique ne peut contracter. La base de Clifford (16 éléments) est complète, et γ₅σ ∝ εσ y est inclus.

**C8 (correction). Base incomplète, conclusion intacte.** L'annexe pose que tout terme est de la forme ψ̄ΓDψ, avec D = identité ou une dérivée. Or l'hypothèse du lemme porte sur l'*équation* (au plus du premier ordre), pas sur l'action. Elle admet donc i∇_aψ̄ σ^{ab}∇_bψ et sa version contractée avec ε (≡ γ₅σ^{ab}), qui ont deux dérivées dans l'action mais ne produisent pas de terme du second ordre, puisque σ^{ab}∇_a∇_b = ½σ^{ab}[∇_a,∇_b]. Ces termes ne figurent pas dans la liste. Ils se réduisent, à une dérivée totale près et par l'identité de Ricci, à des termes de masse constants. Calcul sympy : σ^{ab}σ_{ab} = 12·1 et σ^{ab}R_{abcd}σ^{cd} = 24H²·1 sur de Sitter. Le cas γ₅ donne une masse chirale constante. Il faut ajouter ces termes et leur réduction.

**C9 (correction). Preuve du Lemme 2 : masse effective.** « La multiplication par l'inverse redonne une équation de Dirac à masse chirale constante » est inexact tel quel. On obtient iγ∇ψ = (A + Bγ₅)ψ avec A = (Z₁m − iZ₂m₅)/(Z₁² − Z₂²) et B = (iZ₁m₅ − Z₂m)/(Z₁² − Z₂²). Cette masse n'est pas hermitienne dès que Z₂m ≠ 0 ou Z₂m₅ ≠ 0 : le hamiltonien du mode n'est plus hermitien pour la norme u†u, et la Prop. 1 ne s'applique pas directement. La relation de dispersion exacte (sympy) donne det = [(Z₁² − Z₂²)(p₀² − p²) − (m² + m₅²)]², donc **m_eff² = (m² + m₅²)/(Z₁² − Z₂²)**. La formule √(m² + m₅²) n'est juste que pour Z₁² − Z₂² = 1. On se ramène à une masse hermitienne par une remise à l'échelle non unitaire des chiralités, ψ_L → sψ_L avec s² = (Z₁ − Z₂)/(Z₁ + Z₂) > 0, puis par une rotation chirale. C'est ce que recouvre « normalisation constante du terme cinétique », mais la preuve doit le dire et donner |m_eff|. La conclusion (masse constante, cas tachyonique pour Z₂² > Z₁²) est confirmée. Le réglage ℓ = m/(12H²) est correct (R = 12H²).

**Hermiticité** : les coefficients réels de ψ̄ψ, ψ̄iγ₅ψ, ψ̄iγ^a∇_aψ et ψ̄iγ₅γ^a∇_aψ sont corrects ; la condition γ⁰M†γ⁰ = −M a été vérifiée.

## V7. Proposition 4

**(a) pour k ≠ 0 : correct.** ‖V‖ = k est intégrable sur l'intervalle conforme fini, donc χ → χ₀ ≠ 0, indépendamment de m. Si θ diverge, il est monotone et continu, donc e^{−iθ} parcourt le cercle. La Prop. 2 reste valable : le potentiel e^{−1}m dt n'est pas intégrable. **(b) : correct.** ρ̂ = m a(c + o(1)) + O(k), donc ρ̂ est borné si et seulement si m a l'est. **(c) : immédiat**, sous réserve de C2.

**Ordre strict : correct.** (c) ⇒ (b) ⇒ (a), parce que ∫m dt = ∫ m a dη ≤ sup(m a)·|η₁|. Numériquement sur de Sitter :
- m = 3Ω^{1/2} : incrément de θ sur t ∈ [19, 22] de 3.5e-4 (champ convergent), m a ≈ 1.8e5 (densité divergente).
- m = 3Ω(1 + Ω^{1/2}) : m a → 3, borné et non lisse.
- m = 1/(1+t) : θ = ln(1+t), divergence logarithmique.

**C10 (correction). Les exemples supposent de Sitter (ou H → H∞ > 0).** Sur a = t^{1.5}, qui satisfait les hypothèses du §2, m ∝ Ω^{1/2} = t^{−0.75} donne ∫m dt divergent (8.6, 36, 122 pour t = 10², 10⁴, 10⁶) : ce n'est plus un exemple de (a) sans (b). La phrase « (b) doit être lue pour m a borné loin de zéro » contredit la forme « si et seulement si » de (b), qui reste mathématiquement vraie quand m a → 0. À reformuler en commentaire d'interprétation physique.

**Comparaison avec Bachelot : cohérente.** Pour φ̂'' + (k² + m²a²)φ̂ = 0, la condition de Levinson est ∫ m²a²|η| dη < ∞. Sur de Sitter, a|η| = 1/H, ce qui donne ∫ m² dt < ∞. Le spineur demande ∫ m dt. La citation elle-même n'a pas été vérifiée.

## V8. Remarque 2 et Proposition 5 : cohérence

**E2 (erreur, cohérence interne).** La §5 affirme que la source de l'équation du Weyl rescalé est « bornée sans limite pour *toute* solution qui contient à la fois une composante particule et une composante antiparticule à 𝓘⁺ ». La Remarque 2(4) dit au contraire qu'elle est une série entière « pour les solutions à un seul exposant **et pour k = 0** ». Une solution k = 0 avec χ₀⁺ et χ₀⁻ tous deux non nuls contredit la §5. Mon calcul confirme la Remarque 2(4) : à k = 0, tout le tenseur est libre d'interférence (R1). La partition en « deux classes » distinguées par une règle de régularité formelle est donc mal énoncée : le cas k = 0 tombe du côté régulier.

**C11 (correction). Proposition 5 plus forte que ce qui est prouvé.**
- (b) s'appuie sur « au moins une particule au sens du §4.3 ». La version quantique n'est établie que pour une masse constante, sur de Sitter exact, dans l'état de Bunch-Davies, sous l'identification annoncée et en énergie intégrée relative à l'état. Pour une masse dépendant du temps (« fails unless m decays as 1/a ») et un FLRW général, il faudrait que le poids d'antiparticule soit ≠ ½. Ce n'est pas démontré : seule la version classique, avec ‖χ₀⁺‖ ≠ ‖χ₀⁻‖, l'est (Prop. 4(b)). De plus, la règle (b) porte sur un tenseur borné ponctuellement, alors que le résultat quantique est intégré et relatif à l'état. Le terme du vide de BD, ∝ g_ab, donne d'ailleurs Ω^{−2}T ~ Ω^{−4}ĝ, sauf si son coefficient est nul.
- (c) invoque le Lemme 2, établi sur de Sitter exact, alors que la Prop. 5 est posée sur FLRW. Sur FLRW, les couplages f(R)ψ̄ψ donnent une masse dépendant du temps (relevant de la Prop. 4), pas une masse constante.
- (a) est correct.

**C12 (correction). Remarque 2(3), notation.** Le terme « ξR̂|H|² » porte un chapeau, qui désigne la métrique non physique dans la convention de l'article (§2). La condition m_h² + 4λξ = 2λ/3 est celle d'un couplage à la courbure *physique* R = 4λ, par analogie avec (1) : m² + (ξ − 1/6)R = 0. Le reste du comptage est cohérent : λ_h|H|⁴ est conformément invariant, le coefficient de masse fermionique vaut yH_r, la source de Yukawa est régulière. Le calcul complet est dans la note compagnon, non consultée.

**R2.** La Remarque 2(2) (T[ψ;g] = Ω²T[ψ̂;ĝ] en forme cinétique) est cohérente avec mon calcul : les termes de connexion de spin et de dérivée de Ω^{3/2} sont réels avant antisymétrisation et disparaissent. Les points 2(2) à 2(4) relèvent de la note compagnon et ne sont pas vérifiés au-delà.

**R3.** Le paragraphe de la §5 ne revendique rien au-delà de règles conditionnelles. La phrase « ne démontre pas que toute règle échoue » est conforme.

## V9. Ordres de grandeur

Confirmé. Pour H₀ = 67.4 km/s/Mpc et Ω_Λ = 0.685 : H∞ = 1.19e-33 eV et m_e/H∞ = 4.29e38 (4.0e38 à 4.3e38 selon H₀ ∈ [67, 73]). Le poids d'antiparticule est exp(−2.7e39), bien inférieur à e^{−10^{39}}. La rotation de m/H radians par facteur e de Ω est correcte.

## Autres remarques

- **R4.** §3 (scalaire) : correct. On a (□̂ − R̂/6)φ̂ = Ω^{−3}(m² + (ξ − 1/6)R)φ = [(m² + (ξ − 1/6)R)/Ω²]φ̂ ; sur de Sitter, m² = 2H² ; pour m² > 9H²/4, φ̂ ~ |η|^{1/2 ± iν}.
- **R5.** Lemme 1 : correct (H hermitien).
- **R6.** Les §2 et 4.1 (conventions, covariance conforme de poids 3/2, équation (2)) ont été vérifiés.
- **R7.** La section « Verification » cite des scripts que je n'ai pas consultés (isolement). Mes propres scripts reproduisent indépendamment les points numériques annoncés.
- **R8.** Le résumé (iii) parle de « solutions qui contiennent les deux exposants » pour l'interférence. Il hérite de la réserve E1 / R1 (k = 0, et X = 1).
- **R9.** Le nom « Proposition 5 » n'apparaît pas dans le texte (environnement sans titre, étiquette prop:ccc). Purement formel.
- **R10.** Dans la Prop. 2, l'extension à λ(η, x) « à x fixé » est correcte pour la composante A_η. La régularité des A_i n'intervient pas dans l'obstruction.

## Correctifs prioritaires (résumé)

1. E1 : « présent seulement si » (contre-exemple X = 1).
2. E2 : aligner la §5 sur la Remarque 2(4) (exception k = 0).
3. E3 / C2 : exiger la lissité en Ω dans la Déf. 1(c), et préciser la variable de lissité.
4. C9 : m_eff² = (m² + m₅²)/(Z₁² − Z₂²), avec la remise à l'échelle chirale explicite.
5. C8 : ajouter les termes ∇ψ̄ σ ∇ψ (et γ₅σ) à l'annexe, avec leur réduction à une masse constante.
6. C6 : remplacer « f à support compact dans ran(1−P) » par f = (1−P)g.
7. C11 : restreindre la Prop. 5(b) à la masse constante sur de Sitter (version quantique), ou à ‖χ₀⁺‖ ≠ ‖χ₀⁻‖ (version classique) ; restreindre la Prop. 5(c) à de Sitter exact.
8. C1, C5, C10 : définir « pôle simple », préciser le repère des composantes, situer les exemples sur de Sitter.
