# RAPPORT AL-2 : audit adverse de NOTE-BORD-EON-202-LB-EXECUTION

Auditeur isolé (IA). Pièces lues : la consigne, NOTE-BORD-EON-202-LB-EXECUTION.md, EXTRAIT-ARTICLE-v2.4-props.tex. Outils : base alphaXiv (lecture des PDF), WebSearch. Journal des requêtes : work_al2/journal_requetes.txt. Aucune référence citée de mémoire : chaque titre ci-dessous a été lu dans la source ou dans une bibliographie lue.

Classement : **[E]** erreur (renverse une attribution ou un verdict), **[C]** correction (précise), **[K]** complément (référence à ajouter).

## Synthèse

| Point | Constat principal | Classe |
|---|---|---|
| LB-2, LB-3, §3.4 | Ibison, arXiv:1105.3767 (« The Dirac Field at the Future Conformal Singularity ») traite le Dirac massif au bord futur conforme de de Sitter, dans le repère conforme, avec la masse effective m a(t) = m/Ω et l'énergie de repos E = a(t) m ∫ψ†γ⁰ψ qui croît comme 1/Ω : c'est un équivalent partiel (classique, intégré) de la Prop. 3 | E |
| LB-3, §3.4 | Bachelot, arXiv:2003.03356 donne, dans le cadre CCC, des conditions quantitatives de décroissance de la masse pour qu'un champ massif (scalaire) traverse le raccord : analogue scalaire direct de la Prop. 4 | E |
| LB-4(c), écart à la prédiction | S3 ne laisse pas ouverte l'identification « Bunch-Davies global restreint = état défini à ℑ⁻ » : il l'affirme en renvoyant à S5. Ce qui reste ouvert dans S3, c'est le statut de l'état du projecteur fermionique. S5, que la note n'a pas lu, construit des états Hadamard pour Dirac sur la carte plate à partir de ℑ⁻ | E |
| LB-2 | Contradiction interne : LB-1 attribue à S3 (Lemme 3.1) l'asymptotique du Dirac massif à scri de de Sitter, alors que LB-2 affirme qu'aucun travail lu ne la traite | E |
| S6 | Hollands ne montre la propriété Hadamard que pour les états adiabatiques **d'ordre infini**. À ordre fini n, la différence avec un état Hadamard est seulement de classe C^(n−N+1) | C |
| E2 | Exact sur le fond, à H = 1 et par secteur d'hélicité. Mais la borne (3.10) de S3, prise à la lettre, ne tend pas vers 0 (coquille). « ‖E‖ contrôlé par e^(−t) » n'est donc pas écrit dans S3 | C |
| Prop. 3, quantique | La positivité m tanh(πm/H)‖f‖² vaut pour l'énergie intégrée en espace (Plancherel), pas point par point. Il faut de plus un paquet d'ondes normalisable, pas un mode de Fourier | C (article et note) |
| S16, S11, S12 | S16 a un seul auteur (pas « et al. »). Il manque l'auteur de S11 (Pham Truong Xuan). Le niveau de S12 est contradictoire (« [texte, introduction] ») | C |
| Verdict global | LB-V2 maintenu, mais LB-2 et LB-3 doivent être révisés et la revendication de nouveauté (§3.4) réécrite | E |

## E1. Sources S1 à S16

| # | Identifiant et titre vérifiés | Attribution de la note | Niveau déclaré | Constat |
|---|---|---|---|---|
| S1 | hep-th/0109199, « Polarized Dirac fermions in de Sitter spacetime », I. I. Cotăescu. Phys. Rev. D 65 (2002) 084008, référence confirmée dans la bibliographie de 1804.02842 | Exacte. Éq. (34)-(35) : f⁺ = C t_c² e^(πk/2) H^(1)_(ν−)(−p t_c), ν± = 1/2 ± i m/ω. La déduction des poids t_c^(3/2 ± i m/ω) est correcte (terme dominant z^(−ν)) | [texte] plausible (article court) | RAS. La note dit que la référence de publication a été lue dans la bibliographie de S2. Je ne l'ai pas retrouvée dans les pages lues de S2, mais elle est confirmée ailleurs |
| S2 | arXiv:2610.00410, « Fermionic Particle Creation in Curved Spacetime: Physical Bloch-Vector Dynamics and Exact de Sitter Scaling », S. Boonpan | Exacte : éq. (2.11) H = kσ₃ + m a σ₁, (5.38), (A.36), (5.57), §5.5, « recover the standard Gibbons–Hawking Fermi–Dirac plateau », §7.1 (aucune revendication de nouveauté) | [texte] plausible | [K] S2 cite Kanno–Sasaki–Tanaka, JHEP 03 (2017) 068, « Vacuum state of the Dirac field in de Sitter space and entanglement entropy » (non lu). C'est une référence plus établie qu'un preprint de 2026 pour le facteur de paires |
| S3 | arXiv:1902.09144, « The Fermionic Signature Operator in De Sitter Spacetime », Dappiaggi, Finster, Murro, Radici | Lemme 3.1 : exact, voir E2. Prop. 4.5 et définition de Bunch-Davies via Allen–Lütken : exactes. Lecture de §3.3 : **erronée**, voir ci-dessous | [texte] : la lecture de §3.3 est fautive | **[E]** Voir LB-4(c) |
| S4 | Allen, Lütken, « Spinor two point functions in maximally symmetric spaces », Commun. Math. Phys. 106 (1986) 201, confirmé par la bibliographie de S3 | Exacte | [titre] | RAS |
| S5 | arXiv:1009.5179, « Approximate KMS states for scalar and spinor fields in Friedmann-Robertson-Walker spacetimes », Dappiaggi, Hack, Pinamonti | « Non lu » | [titre] | **[E/K]** Le contenu de S5 tranche la réserve de LB-4(c). Le cas d) a(t) = e^(t/γ) (de Sitter, carte plate) est inclus. Thm 4.2 : l'état de bord à ℑ⁻ induit sur le bulk Dirac un état quasi-libre de forme Hadamard. Les modes vérifient lim e^(ikτ) χ_k = 1/√(2k) quand τ → −∞, c'est-à-dire la condition de Bunch-Davies des calculs de modes. Réserve : le Thm 4.2 est énoncé pour Λ_β. Le cas β = ∞ (fondamental) n'est pas explicitement couvert dans les pages lues (une remarque le « présume » comme limite). À vérifier avant de citer |
| S6 | gr-qc/9906076, « The Hadamard Condition for Dirac Fields and Adiabatic States on Robertson-Walker Spacetimes », S. Hollands, CMP 216 (2001) 635 | « États adiabatiques ... ce sont des états Hadamard » | [texte] douteux | **[C]** Trop fort. Résumé et Thm VI.1 : « adiabatic states of infinite order are Hadamard ». Prop. VI.1 et Comment VII.1 : à ordre fini n, ils ne sont « not Hadamard in general » (différence de classe C^(n−N+1)). Titre : « Spacetimes » et non « space-times » |
| S7 | arXiv:0904.0612, « The extended algebra of observables for Dirac fields and the trace anomaly of their stress-energy tensor », Dappiaggi, Hack, Pinamonti | Voir E3(a) | [sections 3-4] plausible | [C] Mineur, voir E3(a) |
| S8 | arXiv:1711.04011, « Conformal extension of the Bunch-Davies state across the de Sitter boundary », M. Wrochna | Exacte : Klein-Gordon massif seulement | [texte] plausible | RAS |
| S9 | arXiv:2108.11630, « Hadamard states for quantized Dirac fields on Lorentzian manifolds of bounded geometry » ; arXiv:2108.11955, « Hadamard property of the in and out states for Dirac fields on asymptotically static spacetimes », Gérard, Stoskopf | Exacte | [résumé] | RAS. 2108.11630 §3.5 énonce aussi : « the Hadamard condition is preserved by conformal transformations » (utile pour l'article) |
| S10 | Mason, Nicolas : JHDE 1 (2004) 197 ; J. Inst. Math. Jussieu 8 (2009) 179 ; J. Geom. Phys. 62 (2012) 867, tous confirmés par la bibliographie de S11 | Exacte | [titre] | RAS |
| S11 | arXiv:2107.06521, « Conformal scattering theory for the Dirac field on Kerr spacetime », **Pham Truong Xuan** | Exacte (Dirac sans masse) | [résumé] | [C] Ajouter l'auteur |
| S12 | arXiv:1311.0700, « Smooth non-zero rest-mass evolution across time-like infinity », H. Friedrich (Ann. Henri Poincaré 16 (2015) 2215, d'après la bibliographie de Bachelot) | Exacte, citations conformes : « each of them will need a special analysis » ; « restricted to the scalar field only for the purpose of illustration, other fields could be considered as well » | « [texte, introduction] » est contradictoire | [C] Écrire [sections 1, 3] ou [texte] |
| S13 | arXiv:1309.7248, « The equations of Conformal Cyclic Cosmology », K. P. Tod | Exacte (fluide de radiation, Maxwell) | [texte] plausible | [K] Tod mentionne la « Delayed Rest Mass Hypothesis » (φ₂ = 0). C'est un usage du mot « masse au repos » sans rapport avec un champ massif, à ne pas confondre |
| S14 | arXiv:2212.06914, « Toward fixing a framework for conformal cyclic cosmology », O. Markwell, C. Stevens | Exacte : « asymptotic decay of rest-mass » ; Π_aΠ^a = 1 + Q Ω̌² + O(Ω̌³), Q « relating to a Higgs-type mechanism », d'après Gurzadyan–Penrose, Eur. Phys. J. Plus 128 (2013) | [texte] plausible | RAS |
| S15 | arXiv:2503.24263, « The Physics of Conformal Cyclic Cosmology », K. A. Meissner, R. Penrose | Exacte | [sections] | [C] Mineur : le passage sur les erebons et la GWE en fin d'éon se trouve dans un sous-titre « A. GWE at the end of an aeon » qui précède la section VII. Le renvoi « V.A » est à vérifier. Coquille de titre confirmée (« The Physics of ... ») |
| S16 | arXiv:1804.02842, « Propagators of the Dirac fermions in the de Sitter expanding universe » ; arXiv:1809.00670, « Integral representation of the Feynman propagators of the Dirac fermions on the de Sitter expanding universe » | « vide de Bunch-Davies » exact (« fixed vacuum of Bunch-Davies type ») | [titre] | [C] **Un seul auteur** (I. I. Cotăescu), pas « et al. ». [K] Ces deux articles renvoient à Candelas–Raine, PRD 12 (1975) 965 et à Koksma–Prokopec, CQG 26 (2009) 125003 pour le propagateur de Dirac en de Sitter (non lus) |

**[E] LB-4(c), lecture fautive de S3.** S3, §3.3 : « the procedure of [9] is based on the observation that the two-point function of the spinorial Bunch-Davies state selects only negative frequencies on the conformal boundary ℑ⁻ ». Il en conclut que l'état du projecteur fermionique « cannot coincide » avec Bunch-Davies. Ce que S3 laisse ouvert (intro, p. 3), c'est que l'**état FP** soit Hadamard ou soit la restriction de Bunch-Davies. S3 ne laisse pas ouverte l'identification de Bunch-Davies restreint avec l'état de fréquences à ℑ⁻ : il l'affirme en citant [9] = S5. La note confond les deux énoncés.

## E2. Lemme 3.1 de S3 et Prop. 1 de l'article

S3 travaille avec R(t) = e^t, donc H = 1, en signature (+,−,−,−) et avec γ⁰ = diag(1,1,−1,−1). Pour chaque hélicité, avec λ = ±|k| et ψ = R^(−3/2)(u₁φ, u₂φ), le système de mode est i u' = [[m, −λe^(−t)], [−λe^(−t), −m]] u.

Changement de variables :

```
tau = -e^{-t} = eta   (H=1),   Omega = 1/a = e^{-t} = |eta|
d/dt = |eta| d/deta   =>   i du/deta = ( m a sigma_3  - lambda sigma_1 ) u
                          = ( beta m a + alpha.k ) u     (eq. hk, bloc d'helicite)
e^{-i m t} = e^{+i m ln Omega} = exp( i beta (m/H) ln Omega )  sur beta=+1
R^{-3/2} = Omega^{3/2}   <->   psi = Omega^{3/2} u
lambda e^{-t} = k|eta|
```

Le Lemme 3.1 dit : u = (e^(−imt) f₁^∞, e^(imt) f₂^∞) + E(t). C'est exactement u = U₀ χ₀ + U₀(χ − χ₀), avec f^∞ ↔ χ₀ et les phases ↔ U₀. L'attribution est donc **exacte sur le fond**, avec quatre précisions.

1. **[C] Borne d'erreur.** (3.10) écrit ‖E‖ ≤ ‖f^∞‖ exp(|λ|e^(−t)). Prise à la lettre, cette borne tend vers ‖f^∞‖ et non vers 0. La preuve aboutit à la même expression ; c'est une coquille pour exp(|λ|e^(−t)) − 1. Corrigée, elle donne ‖χ − χ₀‖ ≤ (e^(k|η|) − 1)‖χ₀‖. La borne de la Prop. 1, k|η|‖χ₀‖, est plus forte (e^x − 1 ≥ x) et vaut pour tout η. « ‖E‖ contrôlé par e^(−t) » est donc une lecture corrigée, pas un énoncé de S3. L'article ne doit pas citer (3.10) tel quel.
2. **[C] Portée.** S3 est écrit à H = 1, par secteur d'hélicité 2×2. L'article est 4×4 avec H général. L'équivalence passe par la décomposition en hélicité et un changement d'échelle.
3. **[C] Ce que S3 ne dit pas.** La non-existence de la limite (« u has no limit ») et la phase relative e^(2i(m/H) ln Ω) entre les secteurs β = ±1 (Prop. 2(b)) sont des conséquences immédiates mais ne sont pas écrites. La note le reconnaît.
4. **[K] Antériorité.** S3 précise « This can be made precise following [20, Lemma 6.3] », où [20] est Finster–Reintjes, arXiv:1312.7209 (non lu). Il faut aussi citer Ibison, 1105.3767, §6-8 : dans le repère conforme de de Sitter, l'équation devient celle de Minkowski avec m → f(x) m (éq. 49) ; près du bord, ψ → e^(iφ(z,z₀,λ)) P(k) ψ (éq. 94) ; « the phase oscillates rapidly, infinitely quickly so at the boundary ». C'est le contenu qualitatif de la Prop. 1, en repère conforme et au bord futur. L'affirmation d'Ibison que seule une composante β survit est valable à l'ordre dominant en e^(−πm/H) : il néglige ces termes. Elle est donc cohérente avec le poids 1/(e^(2πm/H) + 1).

Verdict E2 : **exact quant au contenu, légèrement trop fort quant à la forme** (borne d'erreur). Prop. 1 = « Lemme 3.1 de S3, repassé à H général et lu à scri, avec une borne uniforme meilleure ».

## E3. Argument quantique (LB-4)

**(a) Axiome 1 de S7.** Texte de S7 (Def. 4.1, « strong version of Wald's axioms ») : « Given two quasifree states ω₁ and ω₂, such that ω₁⁻(x,y) − ω₂⁻(x,y) is a smooth bispinor, ω₁(:T_μν(x):) − ω₂(:T_μν(x):) is equal to Tr[D̃^can_μν(ω₁⁻ − ω₂⁻)] ». La note est fidèle. **[C]** Deux nuances. L'opérateur est D̃^can (avec tilde, D^can = −D̃^can D'_y), pas D^can. Et S7 vérifie l'axiome 1 pour sa prescription « for our regularisation scheme and two Hadamard states » (preuve du Thm 4.1, D^(−1/6), version réduite des axiomes). L'article doit donc exiger des états Hadamard, pas seulement quasi-libres.

**(b) État de Slater.** Dérivation correcte, avec ces réserves :
- **Pureté.** Si ω est quasi-libre pur de projecteur P et f ∈ Ran(1−P) avec ‖f‖ = 1, alors a*(f)Ω est l'état quasi-libre pur de projecteur P + |f⟩⟨f|. C'est correct. L'hypothèse f ∈ Ran(1−P) n'est pas restrictive : a*(Pf)Ω = 0, il suffit donc de remplacer f par (1−P)f/‖(1−P)f‖. Sans pureté, le calcul de Wick pour un état quasi-libre invariant de jauge donne encore une différence de rang un (|g⟩⟨g|/⟨f,(1−S)f⟩ avec g = (1−S)f). En revanche, ω_f n'est plus quasi-libre en général, et l'axiome 1 (énoncé pour des états quasi-libres) ne s'applique plus à la lettre.
- **Normalisation.** Avec ‖f‖ = 1, le facteur ‖f‖² de l'article vaut 1. Pour un f non normalisé, l'état normalisé ne dépend pas de ‖f‖ : écrire ‖f‖² n'a de sens que pour f normalisé.
- **Lissité.** La différence est F(x)F(y)† (au signe de la convention ω⁻ près), où F est la solution associée à f. Elle est lisse si f a des données de Cauchy lisses. **[C] Un mode de Fourier n'est pas dans l'espace à une particule** : il faut un paquet d'ondes. L'article parle de « a mode f » et doit le préciser.
- **Signe.** Pour un ajout de particule, ω_f⁻ − ω⁻ = +F F† (avec ω⁻(f,h) = ω(ψ†(f)ψ(h))). « Au signe de convention près » est acceptable.
- **[C] Positivité du pôle (non relevée par la note).** Pour un paquet F = ∫ f̂(k) u_k e^(ikx), on a Ω ρ̂(x) → m(|g₊(x)|² − |g₋(x)|²), avec g± = ∫ f̂(k) χ₀^±(k) e^(ikx). Le rapport |χ₀⁻|²/|χ₀⁺|² = e^(−2πm/H) est indépendant de k, mais les spineurs χ₀^±(k) dépendent de k̂ (hélicité). La positivité stricte m tanh(πm/H)‖f‖² vaut donc pour **l'énergie intégrée** ∫ρ̂ d³x (par Plancherel), pas point par point. Le « pôle de la densité » de l'article doit être énoncé pour l'énergie intégrée sur un domaine comobile, ou démontré pointwise.

**(c) Restriction Hadamard.** L'argument est correct. La condition de Hadamard porte sur le front d'onde, elle est locale. La carte plate I⁻(p) est un ouvert causalement convexe de de Sitter. La relation bicaractéristique y est la restriction de celle de de Sitter, donc la restriction d'un état Hadamard est Hadamard (même structure de spin). **[C]** Deux limites. Cet argument ne donne pas la **pureté** de la restriction, qui est requise en (b) ; elle provient de l'identification avec le vide de Fock des modes de carte plate. Et l'identification elle-même n'est pas « non établie » : S3 l'affirme via S5, et S5 Thm 4.2 donne directement la propriété Hadamard pour les états construits à ℑ⁻ (réserve β = ∞, voir E1). La phrase de la note « dont la nature Hadamard est admise via son identification (non démontrée ici) » est trop pessimiste et mal attribuée.

**(d) « Pas besoin de Bunch-Davies, seul le chiffre tanh en dépend ».** Partiellement juste.
- Vrai pour l'**existence** d'un pôle générique : tout état quasi-libre pur Hadamard et tout paquet tel que ∫|f̂|²(‖χ₀⁺‖² − ‖χ₀⁻‖²) ≠ 0.
- Faux tel quel pour le **signe** et pour l'interprétation « un électron ». Ce qui compte comme particule dépend de l'état. Pour un état dont les modes de particule ont une limite à β = +1 (état « out », par exemple l'état FP de S3 qui retient u₁ quand t → ∞, de statut Hadamard inconnu), le résidu vaut m‖f‖². Pour un état mal choisi, il peut s'annuler ou changer de signe.
- L'article ne dit d'ailleurs pas autre chose : il attribue tanh à Bunch-Davies. La reformulation proposée par la note (« la positivité vaut dès que le mode ajouté a une composante particule dominante ») est correcte. Il faut seulement ajouter que cette condition porte sur l'intégrale en k et en x.

## E4. Recherche de nouveauté (9 requêtes, journal dans work_al2/)

Requêtes : (Q1) CCC et particules massives, masse au repos, Dirac au raccord ; (Q2) asymptotique du Dirac massif au bord conforme futur de de Sitter et diffusion conforme ; (Q3) équations conformes de Friedrich couplées à Dirac avec Λ > 0 ; (Q4) masse dépendant du temps, VEV de Higgs tendant vers 0, CCC ; (Q5, web) Bachelot, Dirac, CCC ; (Q6, web) Dirac massif asymptotiquement de Sitter ; (Q7, web) Penrose, CCC, électrons, extinction de la masse, Higgs ; (Q8) Nurowski, Meissner–Nurowski, Poincaré–Einstein ; plus la lecture de Lübbe 1312.2059, Tod 2102.02701 et Tod 2202.10864.

Résultats qui modifient le verdict :

1. **[E] Ibison, arXiv:1105.3767, « The Dirac Field at the Future Conformal Singularity »** (chapitre InTech « Cosmology », 2011). Repère conforme de FRW et de de Sitter, Dirac massif, bord futur conforme, avec continuation au-delà et renvoi à Penrose et Friedrich.
   - Éq. (45)-(49) : masse effective f(x) m, c'est-à-dire le coefficient m/Ω de l'éq. (dirachat).
   - §8 : oscillation de phase infiniment rapide au bord (Prop. 1).
   - Éq. (33) : énergie de repos dans le repère conforme E = a(t) m ∫ψ†γ⁰ψ d³x, « not in general time-independent » ; l'introduction précise que dans ce repère « (−g)^(1/2) times the energy density of matter increases in proportion to the scale, giving rise, effectively, to an increase in the rest mass of a free electron ». C'est le terme (m/Ω) u†βu de ρ̂, éq. (rho), donc **le noyau classique de la Prop. 3** : énergie rescalée ∝ m/Ω pour une particule. Il manque chez Ibison la limite exacte m(‖χ₀⁺‖² − ‖χ₀⁻‖²), l'invariance de jauge, l'état quantique et le critère CCC.
   - Rien sur la jauge (Prop. 2) ni sur la masse variable (Prop. 4).
2. **[E] Bachelot, arXiv:2003.03356, « Propagation of Massive Scalar Fields in Pre-Big Bang Cosmologies »** (A. Bachelot). Cadre CCC explicite, Klein-Gordon massif, masse fonction du temps, champ renormalisé Ω^((n−1)/2) u. Il énonce des conditions suffisantes de décroissance de la masse pour que le champ traverse la surface de raccord : ∫ m²Ω² dτ < ∞ (III.18), qui en de Sitter impose une décroissance exponentielle de la masse (III.26), puis la condition plus faible ∫ m²Ω²|τ| dτ < ∞ (IV.39). Le calcul de l'auditeur indique qu'en de Sitter cette dernière revient à ∫^∞ m(t)² dt < ∞ (à confirmer). C'est l'**analogue scalaire direct de la Prop. 4(a)** (condition intégrale ∫ m dt < ∞ pour Dirac) et de la conclusion « quantitative » du §ccc. Pas de Dirac.
3. **[K] Szabados, arXiv:1603.06997**, « Gravity, as a classical regulator for the Higgs field, and the origin of rest masses and electric charge ». Il conclut que, dans un univers asymptotiquement exponentiel, le mécanisme « reverse-BEH » cosmologique ne peut pas faire perdre leur masse aux champs « (as it would be desirable in the CCC model) ». C'est pertinent pour la phrase de l'article sur une VEV de Higgs qui tendrait vers 0.
4. **[K] Tod, arXiv:2202.10864, « Some questions about Conformal Cyclic Cosmology »**, §3 : « Can one implement mass fade-out? » est posé comme question ouverte. Tod, arXiv:2102.02701, §3.5 : le « reverse Higgs mechanism » de Penrose « needs new physics », sans taux. Ces deux textes soutiennent la nouveauté de la **forme quantitative** (1/a, condition intégrale) pour Dirac.
5. **[K]** Loran, hep-th/0404135, « Massive Spinors and dS/CFT Correspondence » : poids de bord des spineurs massifs en dS (citable pour « boundary weights ... are known »). Quiros, arXiv:2510.09957 : masses de poids conforme −1 (m → Ω⁻¹m) rendant l'action de Dirac invariante de Weyl, parenté formelle avec la Prop. 4(c) (m = Ωμ), hors CCC.
6. Négatifs (lus) : Lübbe 1312.2059 (scalaire conforme, Maxwell, Yang-Mills, radiation ; pas de champ massif), Marosek–Balcerzak 2608.27014 (constantes variables, pas de fermion), Markwell–Stevens S14, Meissner–Penrose S15. Aucun équivalent de la **Prop. 2 (jauge)** trouvé.

Conclusion E4 : **la Prop. 2 n'est pas trouvée. La Prop. 3 a un précurseur partiel (Ibison 2011). La Prop. 4 a un analogue scalaire en CCC (Bachelot 2020).** La nouveauté résiduelle se réduit à : la Prop. 2 ; la forme exacte et quantique de la Prop. 3 ; la version Dirac des Prop. 4(a)-(c), avec l'ordre strict (c) ⇒ (b) ⇒ (a) ; la Remarque Friedrich.

## E5. Verdicts

- **LB-1 : LB-V2, justifié et renforcé.** Ajouter Ibison et l'origine Finster–Reintjes. Corriger la citation de la borne de S3 (E2).
- **LB-2 : LB-V1 non justifié tel que rédigé [E].** La note se contredit (S3 Lemme 3.1 traite le Dirac massif à scri de de Sitter), et Ibison le traite au bord conforme futur dans le repère conforme. LB-V1 ne survit que sous la formulation étroite « par diffusion conforme ou par les équations conformes de Friedrich ». Correction proposée : **LB-V2** (asymptotique connue : S3, Ibison, Loran). La formulation par équations conformes avec matière Dirac (Remarque Friedrich) reste non trouvée.
- **LB-3 : LB-V1 à réviser [E].** La Prop. 2 n'est pas trouvée (V1). La Prop. 3 a un précurseur classique partiel (Ibison) : V2 partiel. La Prop. 4 a un analogue scalaire en CCC (Bachelot) : la version Dirac n'est pas trouvée, mais l'idée « conditions quantitatives de décroissance de la masse pour traverser le raccord » est publiée. La prédiction faible « Prop. 2-4 absentes » est donc **partiellement infirmée**.
- **LB-4 : LB-V2, justifié sur le fond.** Corriger (c) : l'identification et le statut Hadamard sont dans S3 et S5 (sous réserve β = ∞), pas « ouverts ». Corriger S6 (ordre infini). Ajouter la réserve de positivité intégrée (E3b).
- **Global : LB-V2 maintenu, pas LB-V3.** Aucun énoncé mathématique de l'extrait n'est contredit. Mais l'« écart à la prédiction » écrit par la note repose sur la lecture fautive de S3, et la nouveauté des Prop. 3 et 4 est surévaluée.

## E6. Propositions §3 de la note pour l'article v2.5

1. **Prop. 1 [C/K]** : ajouter Ibison (1105.3767) et le renvoi [20, Lemme 6.3] de S3. Préciser que S3 travaille à H = 1, par hélicité. Ne pas reprendre la borne (3.10).
2. **Facteur de paires [C]** : la proposition est juste. Préférer, ou ajouter, une source publiée (Kanno–Sasaki–Tanaka 2017, cité par S2, à lire) au seul preprint S2.
3. **Argument quantique [C]** : reformulation à amender.
   - Paquet d'ondes normalisé, pas un mode.
   - Positivité pour l'énergie intégrée.
   - S6 : seulement à ordre adiabatique infini.
   - S7 : D̃^can, états Hadamard.
   - Statut de Bunch-Davies en carte plate : S5 Thm 4.2 avec S3 §3.3, à la place de « non démontrée ».
4. **Nouveauté [E]** : la phrase proposée (« Prop. 2 à 4 non trouvées ... ») est **fausse au vu d'E4**. Proposition : « La Prop. 2 n'a pas été trouvée. Le noyau classique de la Prop. 3 apparaît chez Ibison [1105.3767]. Un analogue scalaire de la Prop. 4 en CCC est donné par Bachelot [2003.03356] ; nous en donnons la version Dirac et la hiérarchie (c) ⇒ (b) ⇒ (a). »
5. **Contexte [K]** : ajouter Bachelot (méthode de renormalisation conforme avec masse variable en CCC).
6. **CCC et masse [K]** : ajouter Tod 2202.10864 (« Can one implement mass fade-out? ») et Szabados 1603.06997 (pas de reverse-BEH cosmologique), à placer en regard de la phrase de l'article sur la VEV de Higgs.
7. **Coquille S15** : correcte.
8. **Manquante [C]** : corriger les fiches S16 (auteur unique), S11 (auteur) et S6 (titre, ordre infini).

## Réserves de l'auditeur

- Ibison, Bachelot, Szabados et Tod ont été lus par extraits ciblés, pas intégralement.
- La réduction en de Sitter de la condition (IV.39) de Bachelot à ∫ m(t)² dt < ∞ est un calcul de l'auditeur, à vérifier.
- Le cas β = ∞ de S5 n'est pas confirmé.
- Finster–Reintjes 1312.7209, Kanno–Sasaki–Tanaka, Candelas–Raine et Koksma–Prokopec n'ont pas été lus.
- Audit fait par une IA, non relu par un humain.
