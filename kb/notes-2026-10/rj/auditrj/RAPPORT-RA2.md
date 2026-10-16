# RAPPORT RA-2 : audit adverse isolé du chantier RJ (NOTE-207)

Pièces lues : consigne PROMPT-AVEUGLE-RA2.md ; NOTE-BORD-EON-207-RJ-EXECUTION.md ; rj_check.py ; rj_check_sortie.txt ; gel NOTE-BORD-EON-206-ARMEMENT-RJ.md ; Friedrich arXiv:1601.04506 (texte intégral récupéré, lu pour le §3 en entier, le §4 autour de (4.16) à (4.18), et l'hypothèse de signe sur ρ̂). Aucun autre fichier ouvert.

Fichiers de travail (tous dans /home/claude/RJ/auditrj/work_ra2/) : rj_check_copie.py et sortie_reproduite.txt (reproduction) ; ra2_A_P0.py et sortie_A.txt (identité P0, lien avec Z) ; ra2_B_dirac_T.py et sortie_B.txt (tenseur de Dirac avec connexion de spin) ; ra2_C_numerique.py et sortie_C.txt (conservation complète, particule pure, terme dérivée, paquets, sensibilité) ; friedrich1601.04506.txt (texte de l'article).

Conventions : n_a = d_a Ω (indice bas), signature (-,+,+,+), signes pris dans la sortie du script.

## Synthèse

| # | Classe | Constat |
|---|---|---|
| 1 | **erreur** | Pour une solution « particule pure à la limite », le tenseur τ n'oscille à **aucun** ordre : c'est une série entière en Ω (solution de Frobenius u₊ = Ω^{i m/H} × série entière). L'affirmation de la note (« oscillation d'amplitude O(Ω) : C⁰, pas C¹ ») est fausse pour τ ; elle n'est vraie que pour l'inconnue χ. Idem pour « P3 porte sur toute solution avec k non nul, quelle que soit sa limite ». |
| 2 | correction | Signe de τ_0a : le tenseur physique donne τ_0a = **−** Ω k_a N (convention e^{+ik·x} du script), non + Ω k_a N. Sans effet sur max\|S/Ω\| ni sur le verdict, mais le test de conservation du script ne pouvait pas le voir. |
| 3 | correction | « Plus aucun pôle » vaut pour les seconds membres du secteur Einstein et pour l'équation de matière écrite en χ ; en inconnue u l'équation de Dirac garde le pôle (i m/H) β / Ω. Pôle ou phase est un choix d'inconnue ; l'invariant est la paire d'exposants de Fuchs ± i m/H. |
| 4 | correction | « Aucun choix d'inconnue spinorielle ne la retire » : vrai pour toute V indépendante de k (même non régulière) et pour toute V régulière (même non diagonale et dépendant de k) ; faux pour une V dépendant de k et elle-même non régulière (la matrice fondamentale rend χ constant). Il faut énoncer la version invariante. |
| 5 | correction | Le verdict RJ-V2 est justifié, mais pour une raison que la note n'établit pas et contredit en partie : la « classe exceptionnelle explicite » exigée par la définition de RJ-V2 au gel existe (particule pure ou antiparticule pure à la limite, paquets de même type compris, et k = 0) ; la note ne l'énonce pas et la décrit à tort comme seulement C⁰. |
| 6 | correction | FW-4 n'est pas respecté à la lettre : le gel prévoyait, en cas de V1 ou V2, le passage au couplage formel complet ; la note conclut au verdict global sur le seul premier étage. Le verdict doit être marqué « premier étage ». |
| 7 | complément | P0 est exacte en toute généralité (Ω et T̂ fonctions arbitraires ; métrique conforme courbe non diagonale) ; et S(ρUU, n) = ρ Z_Friedrich **exactement**, pour U et n quelconques : la lacune déclarée au §2 est comblée. |
| 8 | complément | Le second membre de (3.7) contient aussi le terme dérivée (1/2)(∇τ' − ∇τ') : pour une solution générique il est borné et oscille sans limite (étendue 0,51), pour une particule pure il est régulier. La note ne l'a pas examiné. |
| 9 | complément | Équations (3.3) à (3.6) : en poids poussière, tous les seconds membres sont des polynômes en Ω, τ, ∂τ sans puissance négative de Ω. Le point « non calculé » du §5 se ferme : pas de pôle, phases à des ordres supérieurs pour une solution générique, analytiques pour une particule pure. |
| 10 | complément | Le courant de Dirac n'est **pas** asymptotiquement au repos pour une solution générique (vitesse J/N d'ordre 1, oscillante) : l'option « flot = courant de Dirac normalisé » du gel (RJ-3) et la prémisse du gel §3 (Ibison) ne valent que pour la classe pure. La note a remplacé ce flot par la normale de Hubble sans le dire. |
| 11 | complément | La limite de la densité, m(\|χ0+\|² − \|χ0−\|²), n'a pas de signe fixé et peut s'annuler (sorties : −0,036 ; −0,022). Friedrich utilise ρ̂ ≥ 0 (et ρ > 0 sur 𝓘⁺ pour la simplification des contraintes). Le gel demandait le signe de ρ dans RJ-1 : non traité. |
| 12 | complément | §5 incomplet : manquent FLRW tendant vers de Sitter (exigé par RJ-2 au gel), le terme dérivée de (3.7), la transposition de la jauge par géodésiques conformes à un flot non géodésique, et le signe de la densité limite. |
| 13 | complément | Sensibilité (E7) : conclusions inchangées pour m/H de 0,05 à 5, \|k\| de 0,1 à 10, rtol 1e-9 et 1e-12. Mais pour m/H petit la période d'oscillation dépasse la fenêtre (27 décades pour m/H = 0,05) : « sans limite » repose alors sur l'expression analytique, pas sur le chiffre. |

Bilan : aucun constat ne renverse le verdict RJ-V2. Le constat 1 renverse en revanche un résultat énoncé (le comportement de la classe pure) et change le contenu du verdict dans un sens qui **renforce** RJ-V2 tel que défini au gel, tout en affaiblissant la formulation de RJ-4 (§7) qui fait de la phase une obstruction « pour toute solution ».

## E1. Reproduction, P0, P1

**Reproduction.** Les empreintes sha256 des trois pièces concordent avec l'en-tête de la note (6f2aae275fb256b6, e0e0589b81772307, 44f184af4568e3ed). Le script relancé (16 s) donne une sortie **identique octet pour octet** à rj_check_sortie.txt.

**P0, généralité.** Le script ne teste qu'une instance : un Ω polynomial fixé, un T̂ polynomial tiré avec une graine fixe, g de Minkowski. J'ai refait le test :
- A1 : Ω et les dix T̂_ab **fonctions arbitraires** de (t, x, y, z), g = η : 24 composantes (j, k<l), 0 résidu, symbolique exact. Les composantes k>l s'en déduisent par antisymétrie des deux membres : la vérification couvre toutes les composantes.
- A2 : g **courbe, non diagonale**, polynomiale, ∇ la connexion de Levi-Civita de g ; 72 tests exacts en points rationnels : 0 résidu. L'identité est donc tensorielle, pas un artefact de la platitude de g.
- A3 : pour τ = ρ U U, U unitaire quelconque et n quelconque, S − ρ Z = 0 identiquement, avec Z = ∇_[kΩ g_l]j + 2 ∇_[kΩ U_l] U_j + U_[k g_l]j U^q ∇_qΩ, lu dans l'article (3.20). En outre le membre de gauche du script est exactement le second membre de (3.7) de l'article, 2 Ω⁻¹ ∇̂_[ν L̂_λ]η, et L̂ du script coïncide avec (3.10) pour la poussière. **P0 est la généralisation exacte de (3.20) de Friedrich à un tenseur quelconque.** La phrase « la proportionnalité exacte entre S et le Z de Friedrich hors alignement n'est pas vérifiée » peut être remplacée par « S = ρ Z, vérifié ».

**P1.** Exact : pour n = −ν e0, l'application τ ↦ S est de rang 9, noyau engendré par e0 e0. L'énoncé « toute composante τ_0a ou τ_ab d'ordre 1 laisse un pôle » est correct (injectivité sur un supplémentaire du noyau). Remarque : la trace pure τ = c g n'est pas dans le noyau, ce qui est cohérent.

## E2. Tenseur de Dirac

Vérification indépendante (ra2_B_dirac_T.py) : tétrade e^a_μ = a δ, connexion de spin construite à partir de ω_μ^a_b, contrôlée par ∇γ = 0 (16 composantes, 0 échec) ; formule covariante symétrisée T_μν = (i/4)[ψ̄ γ_(μ ∇_ν) ψ − h.c.] ×2.

- **Termes de connexion de spin et poids.** Pour ψ = a^{−3/2} u, **u arbitraire, hors couche** : T̂_μν = a⁻² T^plat_μν[u], 10 composantes sur 10, 0 résidu. Les termes de connexion de spin s'annulent exactement dans la partie symétrisée. Donc τ = Ω⁻¹ T̂_coord = Ω T^plat[u].
- **τ_00 = Ω k·J + m B** : exact.
- **τ_ab = (Ω/2)(k_a J_b + k_b J_a)** : exact (6 composantes).
- **τ_0a** : le calcul donne T^plat_0i = **− k_i N** (c'est −T^{0i}, la densité d'impulsion étant + k_i N pour la convention e^{+ik·x} du script, qui intègre i u' = (α·k + β m a) u). Le script code + Ω k N. **Correction de signe.**
- **Conséquence du signe.** S est linéaire et chaque composante de S qui contient τ_0a ne contient que lui (n n'a qu'une composante temporelle) : le signe faux retourne quelques composantes de S sans changer max\|S/Ω\| = 0,40, ni aucune conclusion.
- **Le test de conservation du script est insuffisant.** Il ne teste que la composante ν = 0 pour un mode homogène, qui ne fait intervenir que τ_00 et la trace spatiale Σ τ_aa : il est aveugle au signe de τ_0a et à la partie sans trace de τ_ab. Test complet (C1) : superposition de deux modes (champ non homogène), divergence covariante ∇̂^μ T̂_μν, ν = 0..3 :

| η | résidus relatifs, signe physique | résidus relatifs, signe du script |
|---|---|---|
| −3 | 1e-10 sur les 4 composantes | 0,8 ; 1,4 ; 0,2 ; 2,4 |
| −0,5 | ≤ 1e-10 | 0,2 ; 0,1 ; 0,1 ; 0,2 |

Avec un mode unique, le signe du script passe (1e-10) : c'est exactement l'angle mort. Le tenseur corrigé est conservé dans toutes ses composantes ; la mention « conservation vérifiée numériquement, résidu 7e-9 » de la note surestime ce que le script a validé.

- **Point structurel utile** (vaut aussi pour les paquets) : dans T^plat_0i et T^plat_ij, le terme de masse s'élimine **ponctuellement**, parce qu'il apparaît sous la forme ψ†{α_i, β}ψ = 0. D'où τ_0a, τ_ab = O(Ω) pour toute solution, pas seulement pour un mode.

## E3. « Plus aucun pôle » : choix cachés

1. **Jauge U = normale de Hubble.** S(τ, n) est un tenseur qui ne dépend que de τ et de n = dΩ, pas du repère. Le choix de U n'intervient donc pas dans l'absence de pôle ; ce qui intervient est le **facteur conforme** Ω = −Hη, dont le gradient est la normale de Hubble. La phrase « absorbés par le poids poussière et le choix U = normale de Hubble » attribue le mécanisme au mauvais objet. Dans le problème couplé, Ω devient une inconnue et c'est là que la question de jauge (relation régularisante (4.16)) se poserait ; elle n'est pas traitée.

2. **Le flot de Dirac n'est pas un flot de Friedrich.** La vitesse du courant de Dirac par rapport au repère de Hubble est J/N (invariante par changement conforme). Pour une solution générique J = 2 Re(e^{−2iθ} χ+† σ χ−) est d'ordre 1 et oscillant : sur les sorties, \|τ_ab\|/Ω = \|k\|·O(\|J\|) va de 0,34 à 0,73 avec N = 1. Le courant n'est donc **pas** asymptotiquement au repos, contrairement à la prémisse du gel (§3, Ibison) ; il ne l'est que pour la classe pure (J = O(Ω)). L'option « flot = courant de Dirac normalisé » du gel (RJ-3) donnerait un flot non aligné avec dΩ à 𝓘⁺ : la condition géométrique de Friedrich (« les géodésiques du flot atteignent 𝓘⁺ orthogonalement », fin du §3) échoue génériquement. La note substitue la normale de Hubble sans le signaler. L'absence de pôle dans S ne vient pas d'un alignement du flot, mais de la domination de la masse (τ_0a, τ_ab = O(Ω)).

3. **Homogénéité, un seul mode.** Un mode complexe unique donne des bilinéaires indépendants de x : le calcul de la note est homogène par construction. Paquets (C4, deux modes, point x fixé) :

| superposition | τ_00 (étendue, Ω < 1e-5) | \|τ_ab\|/Ω (étendue) | verdict |
|---|---|---|---|
| deux particules pures | 5e-11 | 1,3e-5 (décroît comme Ω) | régulier |
| particule pure + antiparticule pure | 6,5e-6 | 1,07 | borné, sans limite |

Aucun pôle dans les deux cas (point structurel de E2). La séparation régulier / irrégulier suit le **type** des modes (exposant + i m/H ou − i m/H), pas le nombre de modes.

4. **Terme dérivée de (3.7).** Le script ne rapporte que S/Ω. Le second membre complet est (1/2)(∇_k τ'_lj − ∇_l τ'_kj) + S/Ω. Calcul (C3) sur Ω ∈ [1e-8, 1e-3] :

| solution | terme dérivée : max | étendue | S/Ω : étendue |
|---|---|---|---|
| générique | 0,40 | **0,51** (oscille) | 0,60 |
| particule pure | 0,40 | 0,002 (variation lisse en Ω) | 5e-4 |

Le terme dérivée est borné (d/dη de Ω e^{2iθ} reste borné), donc pas de pôle, mais il porte lui aussi la phase pour une solution générique.

5. **Autres équations conformes** (lues dans l'article, (3.3) à (3.6)). En posant T̂(e_j, e_k) = Ω τ_jk dans un repère g-orthonormé et T̂ = Ω³ tr τ, j'obtiens :
   - (3.3) : −T̂/4 = −(1/4) Ω³ tr τ = (m/4) Ω³ B ;
   - (3.4) : (1/2) Ω T*_jk = (1/2) Ω² (τ_jk − (1/4) tr τ g_jk) ;
   - (3.5) : (1/2) Ω n^i (τ_ik − (1/4) tr τ g_ik) − (1/8) Ω n_k tr τ − (1/24) Ω² ∇_k tr τ ;
   - (3.6) : Ω × (second membre de (3.7)).

   Pour τ = ρUU on retrouve exactement (3.16) à (3.19) de l'article (contrôle de transcription). Aucune puissance négative de Ω : seuls (3.7) (via S/Ω) et l'équation de matière peuvent être singuliers. Pour une solution générique les phases réapparaissent à des ordres supérieurs (B a une composante O(Ω) oscillante), ce qui est une irrégularité au sens FW-3 ; pour la classe pure tout est analytique.

6. **Injection linéaire.** Le calcul est un champ test sur de Sitter exact ; rien n'est dit sur la rétroaction ni sur un Ω dynamique. La note le dit (§0, §8), mais le §7 tire des conclusions au niveau du système couplé.

## E4. Prop. 3 et poids

- **Énoncé de la note : correct sur le fond.** La densité physique vaut ρ̂ = a⁻⁴(k·J + m a B) ≈ m B Ω³. En poids radiatif Ω⁻⁴ elle donne k·J + m B/Ω (pôle) ; en poids Ω⁻³, m B + Ω k·J (régulier, limite m(\|χ0+\|² − \|χ0−\|²)).
- **Quel poids est imposé ?** Les équations (3.3) à (3.7) sont écrites en fonction du tenseur physique T̂ avec des facteurs de Ω fixés : leurs seconds membres sont **indépendants** du poids choisi pour l'inconnue de matière. Le poids est un choix de variable, mais il n'est pas libre si l'on exige (i) une inconnue à limite finie non nulle et (ii) des seconds membres polynomiaux en Ω : pour une matière massive (ρ̂ ~ a⁻³) seul le poids Ω⁻³ satisfait les deux (poids 4 : inconnue à pôle ; poids 2 : inconnue nulle à 𝓘⁺ et facteurs Ω⁻² explicites dans (3.7)). Le poids radiatif est, lui, celui que donne naturellement le spineur rescalé de poids 3/2 (bilinéaires de u = T^plat[u]) : la tension entre les deux poids vaut un facteur Ω, c'est exactement le pôle de la Prop. 3.
- **Formulation proposée pour la v2.5** : « le pôle m/Ω est celui de la variable radiative ; les seconds membres des équations conformes, qui ne dépendent pas de ce choix, n'ont pas de pôle ». Ajouter : la limite m(\|χ0+\|² − \|χ0−\|²) **n'a pas de signe fixé** et peut s'annuler (constat 11) ; si l'article dit « signe fixe », il faut préciser « fixé pour une solution donnée, non positif en général ».

## E5. Équation pour χ et transformations u = V χ

- **Identité P3** : U0† α_i U0 = α_i e^{2iβθ} est correcte (bloc supérieur droit σ e^{−2iθ}), et le coefficient est de module 1, sans limite.
- **Structure invariante.** En variable Ω l'équation est du/dΩ = (A0/Ω + A1) u, A0 = (i m/H) β, A1 = (i/H) α·k : point singulier **régulier** (Fuchs), exposants ± i m/H, de différence 2i m/H non entière. Il existe deux solutions de Frobenius u_± = Ω^{± i m/H} × (série entière, même entière en Ω, car A1 est constant ; récurrence (ρ + n − A0) c_n = A1 c_{n−1} inversible pour n ≥ 1).
- **V indépendante de k (quelconque, même non régulière).** Si le coefficient à k = 0 doit être régulier, V = Ω^{A0} Y avec Y régulière inversible ; le coefficient en k devient Y⁻¹ α_i Ω^{2A0} Y, régulier si et seulement si α_i Ω^{2A0} l'est : impossible. **Aucune V indépendante de k ne convient.**
- **V régulière, dépendant de k, non diagonale.** Les exposants modulo Z sont invariants par transformation méromorphe (y compris les cisaillements Ω^{diag(entiers)}) ; ± i m/H ne sont pas entiers : **impossible**.
- **V dépendant de k et non régulière.** La matrice fondamentale V_k = Φ_k(Ω) donne χ' = 0 : coefficients nuls, donc réguliers. La phase est alors entièrement dans V. L'affirmation de la note n'est donc vraie qu'avec la clause « V régulière, ou V indépendante de k ».
- **« Donc sur toute solution » : faux pour les quantités invariantes.** La particule pure u₊ a tous ses bilinéaires analytiques en Ω ; seule l'inconnue χ porte e^{2iθ} à l'ordre Ω. Vérification numérique (C2, m/H = 0,7) :

| Ω | \|τ_ab\|/Ω² | (τ_00 − m)/Ω | \|χ−\|/Ω | phase de χ− |
|---|---|---|---|---|
| 1e-1 | 0,98632 | 0,0473 | 0,5804 | −2,60 |
| 1e-2 | 0,98841 | 0,0047 | 0,5812 | +0,46 |
| 1e-3 | 0,98843 | 0,0005 | 0,5812 | −2,77 |
| 1e-4 | 0,98843 | 0,00005 | 0,5812 | +0,29 |
| 1e-5 | 0,98844 | 0,000005 | 0,5812 | −2,93 |

τ_ab/Ω² converge sans oscillation ; τ_00 = m + O(Ω²) ; seule la phase de χ− tourne. Le coefficient de Frobenius d'ordre dominant prédit J/Ω = (0,567568 ; 0,405405 ; 0,756757), le calcul donne (0,567501 ; 0,405385 ; 0,756668) (l'écart de 1e-4 vient de la donnée imposée en Ω = 1e-10 avec χ− = 0). En dessous de Ω = 1e-6 les petites dérives sont numériques.

Schéma de la structure :

```
   solution u = c+ u+  +  c- u-          u± = Ω^{± i m/H} (série entière)

   bilinéaires (τ)  :  |c+|² (série)  +  |c-|² (série)  +  c+* c- Ω^{-2 i m/H} (série)
                       \___________ analytiques ___________/   \___ phase log-périodique ___/
   classe pure (c- = 0 ou c+ = 0, paquets de même type, k = 0) : τ analytique
   générique : τ borné, sans limite (ordre 1 dans τ_ab/Ω, ordre Ω dans τ_00)
```

## E6. Verdict, FW-3, §5

- **RJ-V2 est le bon verdict**, et même plus nettement que ne le dit la note : la définition du gel exige « régularisation seulement pour les solutions purement particule (ou purement antiparticule) à la limite ... avec une classe exceptionnelle explicite ». Cette classe existe et est explicite (exposant unique de Fuchs ; paquets de même type ; k = 0). La note, elle, la décrit comme seulement C⁰ et écrit au §4 que l'irrégularité touche « toute solution avec k non nul » : avec ces phrases, le verdict n'aurait plus de classe exceptionnelle et ressemblerait plutôt à un V2 dégénéré. Il faut corriger le texte, pas l'étiquette.
- **Application de FW-3.** Honnête pour la classe générique (phase multipliant un coefficient non nul à l'ordre 1 de S/Ω et du terme dérivée). Deux précisions : (a) au sens strict de FW-3, la classe pure est **régulière** au niveau des seconds membres (séries entières) ; (b) l'équation de matière reste singulière pour toute inconnue régulière (pôle de Fuchs en u, phase en χ), y compris pour la classe pure. Le verdict doit dire à quel niveau (sources ou équation) la régularité est obtenue.
- **« Plus aucun pôle » (§6, §7).** À restreindre aux seconds membres du secteur Einstein ((3.3) à (3.7)) et à l'équation de matière écrite dans l'inconnue non régulière χ. En u, le pôle (i m/H)β/Ω demeure. « Pôle contre phase » est un échange d'inconnue ; l'invariant est la paire d'exposants ± i m/H.
- **§7, RG-4.** « L'obstruction ... n'empêche ni la bornitude ni la continuité pour une particule pure » sous-estime : pour la classe pure, les sources sont analytiques. La formulation invariante correcte de l'obstruction est : **interférence entre les deux exposants de Fuchs** (phase relative de la Prop. 2(b)), présente si et seulement si les deux composantes limites sont non nulles. La phrase « aucun choix d'inconnue spinorielle ne la retire » doit porter la clause de E5.
- **FW-4.** Le gel prévoyait le couplage formel complet en cas de V1 ou V2 ; il n'est pas fait. L'argument « il ne peut pas donner RJ-V1 » est valable pour V1 (l'équation de matière reste singulière), mais le couplage pourrait réintroduire des pôles et donc toucher la classe exceptionnelle elle-même. Le verdict global doit être étiqueté « premier étage (champ test) ».
- **FW-1.** Lecture déclarée « §§ 5 début, 7 début », alors que FW-1 demandait la lecture des §§ 4, 5, 7 avant toute affirmation sur le mécanisme. Les affirmations sur le §5 (« système symétrique hyperbolique valable des deux côtés ») reposent sur une lecture partielle : conformité partielle.
- **RJ-1 incomplet.** Le gel demandait les hypothèses sur le signe de ρ. Friedrich utilise ρ̂ ≥ 0 le long des géodésiques et ρ > 0 sur 𝓘⁺ pour la simplification des contraintes ; pour Dirac la limite m B peut être négative ou nulle (sorties : −0,0365 pour la solution générique du script ; −0,0217 pour m/H = 0,05, \|k\| = 10). Quand m B → 0, le rapport inclinaison/densité (τ_0a/(Ω τ_00)) diverge : l'analogie « poussière + inclinaison régulière f » cesse.
- **§5 incomplet.** À ajouter : FLRW tendant vers de Sitter (demandé explicitement par RJ-2 au gel, ni fait ni listé) ; le terme dérivée de (3.7) (fait ici) ; la transposition de la jauge par géodésiques conformes à un flot non géodésique (courant de Dirac) ; le signe et l'annulation possible de la densité limite ; la fermeture de (3.3) à (3.6) (faite ici, E3 point 5).

## E7. Sensibilité

Solution générique, Ω ∈ [1e-8, 1e-2], 600 points (C5) :

| m/H | \|k\| | \|τ_ab\|/Ω (min, max) | \|τ_0a\|/Ω max | τ_00 final | période (décades de Ω) |
|---|---|---|---|---|---|
| 0,05 | 1 | 0,50 ; 0,57 | 0,80 | +0,033 | 27,3 |
| 0,05 | 10 | 5,44 ; 6,77 | 8,0 | −0,022 | 27,3 |
| 0,3 | 1 | 0,29 ; 0,45 | 0,80 | +0,245 | 4,5 |
| 0,7 | 0,1 | 0,046 ; 0,061 | 0,08 | +0,492 | 1,9 |
| 0,7 | 10 | 6,26 ; 7,70 | 8,0 | +0,314 | 1,9 |
| 2 | 1 | 0,57 ; 0,69 | 0,80 | +1,163 | 0,7 |
| 5 | 1 | 0,59 ; 0,74 | 0,80 | +2,716 | 0,3 |

Résultats identiques à rtol = 1e-9 et 1e-12. La conclusion qualitative (aucun pôle ; τ_ab/Ω borné, d'ordre \|k\|, sans limite) ne change pas. Trois réserves :
- pour m/H petit la période d'oscillation (π H/m en ln Ω, soit 1,36/(m/H) décades) dépasse largement la fenêtre : la non-existence de limite n'est pas démontrée par le chiffre mais par la forme analytique J = 2 Re(e^{−2iθ} χ+† σ χ−) ;
- dans la sortie du script, « dernière décade (Ω < 1e-5) » couvre en fait trois décades ; pour m/H = 0,7 cela fait environ 1,5 période ;
- max\|S/Ω\| = 0,40 est constant parce qu'il est dominé par la composante non oscillante τ_0a (\|k_3\| N / 2 = 0,4) : ce maximum masque l'oscillation, seule l'étendue la montre.

## Ce que je recommande de reporter dans l'acte RJ

1. Corriger le signe de τ_0a dans rj_check.py et remplacer le test de conservation par un test complet sur une superposition (sans effet sur les chiffres de S/Ω).
2. Remplacer la ligne « particule pure » du tableau par : τ analytique en Ω (solution de Frobenius), aucune oscillation ; retirer « C⁰, pas C¹ » (valable pour χ seulement).
3. Énoncer explicitement la classe exceptionnelle de RJ-V2 : solutions à un seul exposant de Fuchs (particule pure ou antiparticule pure à la limite, paquets de même type compris), et k = 0.
4. Restreindre « plus aucun pôle » aux seconds membres de (3.3) à (3.7) ; dire que l'équation de matière reste singulière (pôle en u, phase en χ) pour toute inconnue régulière, et donner l'énoncé invariant (exposants ± i m/H).
5. Étiqueter le verdict « premier étage (FW-4) » ; compléter le §5 (FLRW, flot de Dirac non géodésique, signe de la densité limite).
6. Ajouter dans RJ-1 l'hypothèse ρ̂ ≥ 0 de Friedrich et le fait que la limite m(\|χ0+\|² − \|χ0−\|²) n'a pas de signe fixé.
7. Remplacer au §2 « proportionnalité non vérifiée » par « S(ρUU, n) = ρ Z, vérifié (RA-2, A3) ».

## Non-surclassement

Audit par IA, non relu par un humain. Les points 1 et 5 du tableau reposent sur la théorie de Fuchs standard et sur un contrôle numérique à un seul jeu de paramètres pour la classe pure (m/H = 0,7, k = (0,6 ; 0 ; 0,8)) ; le couplage formel complet n'a pas été examiné ici non plus.
