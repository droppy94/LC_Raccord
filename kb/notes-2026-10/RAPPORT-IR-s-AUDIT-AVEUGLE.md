---
id: RAPPORT-IR-s-AUDIT-AVEUGLE
date: 2026-10-12
objet: rapports des sous-agents S-a1, S-a2, S-b, S-c (audit froid aveugle de NOTE-123 et NOTE-125), substance reproduite fidelement
gel: NOTE-BORD-EON-127-ARMEMENT-AUDIT-IR-s (sha256 b1bc0714c415e2de…, sceau 2026-10-12T11:51:18Z)
scripts: copies dans D:\temporaire\audit_ir_s\ (sous-dossiers sa1, sa2, sb)
---

# S-a1 (re-derivation aveugle du bloc R)
Scripts : s1_variation_generale.py (3aa1365e…), s2_onde_dS.py (049bbc1b…) ; sorties s1_sortie.txt (6fcf560c…), s2_sortie.txt (2fd7042a…). Convention de Riemann MTW.
- u solution du mode tensoriel ; Ric[ĝ] − 3ĝ = 0 a l'ordre ε. Invariance de Weyl : S_C[ĝ] = b∫√g φ C²[g] ; T̂_ab = s² T_ab[g].
- Variation brute (10 fonctions h_μν et φ generiques) : **T_ab = 8b ∂^c∂^d(φ C_acbd)** au premier ordre (convention T_ab = (2/√g)δS/δg^{ab}).
- T̂_yy = −T̂_zz = 4bk³ s (B cos ks − A sin ks) cos kx ; sans trace, conserve, **aucun ln s** (Bach linearise nul : ĝ d'Einstein). Forme exacte T̂_ij = −8b C_sisj = −8b Ω W_sisj.
- **R_ysy = −R_zsz = 4Bbk³κ cos kx/s − 6Abk⁴κ cos kx + …** ; R_yxy regulier. Pole simple porte par B seul. Origine : L̂_ij = −4bκ s W_ij ; ∇̂_s L̂ donne −12bκW, ∇̂_j L̂_si donne +4bκW par les Christoffel ; total −8bκW/s.
- W_sysy → −½Bk³ cos kx a 𝓘⁺ (partie electrique, donnee B) ; W_syxy → ½Ak³ sin kx (partie magnetique, donnee A).
- **R_isj = −(8bκ/Ω) W_sisj|𝓘⁺ + O(1).**
- Non-artefact : C₁ invariant de jauge (Stewart-Walker, C[η] = 0) ; Ω → θΩ ne modifie φ que d'un terme lisse ; le pole ne disparait que si W_E|𝓘⁺ = 0.
- Transport qualitatif : au premier ordre, δW ≈ −α bκ W₀ ln s (divergence logarithmique) ; resomme, W ∝ s^{−αbκ} ; la regularite de W exige W_E|𝓘⁺ = 0.

# S-a2 (re-derivation aveugle du calcul q-4)
Script sa2_calc.py (a0b958a1…), sortie sa2_out.txt (9ec67316…).
- C_0i0j = −(ε/4) d_ij f″ ; Bianchi : ∇^μW_μi0j = −∂_τ W_0i0j. dW/dτ = A ln τ ⇒ W = W₀ + A(τ ln τ − τ) ⇒ **f = c₀ + c₁τ − (2/3)W₀τ³ − (A/3)τ⁴ ln τ + (19/36)Aτ⁴**.
- f⁗ ~ −8A ln τ : **g est C³ (C^{3,α}) non C⁴ ; W continue non C¹** ; C[g] C¹ non C².
- ǧ = τ²g : fond **radiation** (ρ = 3/(4Ť²), w = 1/3) ; ordre ε : δĜ_00 = δĜ_0i = 0, δĜ_ij = (εd_ij/2τ³)(τf″ + 2f′) **sans trace ∝ d** ; terme A τ⁴ ln τ : **5 ln Ť** + cste, rapport a ρ ~ Ť² ln Ť.
- Pas de casse, perte de regularite. Reserve : le terme c₁τ (jauge pour g) devient physique dans ǧ (Ť^{−3/2}) ; il depend de la prescription reciproque, pas du log.

# S-b (audit des scripts, reproduction, contre-exemples)
Empreintes conformes. Scripts dans work/ (sb_lib, sb_geom, sb_conf_bianchi, sb_RA, sb_modes, sb_gauge_RE, sb_paneitz_check, sb_euler, sb_euler_R, sb_Q, sb_EL_test et sorties).
**Bloc Q**
- Q-A valide comme illustration (la reciproque, source en ln ⇒ f ~ τ⁴ ln τ, n'est pas demontree par le script) ; Q-B valide sous prolongement a τ < 0 (τ⁴ ln|τ|) ; Q-C valide (5 ln Ť + ln 32 + 9/2, sans G⁰₀).
- DEFAUT d'etiquette : « G_00 » est la composante mixte G⁰₀ = −ρ.
- Coherence Q/R : avec une source en 1/Ω (bloc R), le modele adequat est f = τ³ ln τ : W ~ ln τ diverge, g seulement C², perturbation de l'eon suivant ∝ Ť^{−1/2}(ln 64Ť⁶ + 7).
**Bloc R**
- R-A valide sur les 10 composantes (λ = −1/4). **DEFAUT de convention** : c0 = −8 correspond a T^{ab} = (2/√−g)δS/δg_ab (Carroll, Wald), c0 = +8 a T_ab = (2/√g)δS/δg^{ab} (convention ecrite au gel). Le signe de R-D en depend, pas l'existence du pole. c0 = −8 est coherent si b est le coefficient de C² dans ⟨T^a_a⟩ = bC² + … avec l'action +b∫σC².
- T̂ = s² T valide meme hors invariance de Weyl. Signe de R controle (∇_a(Ω⁻¹C^a_bcd) = Ω⁻¹∇̂_aĈ^a_bcd).
- R-B, R-C, R-D reproduits exactement. Formule generale : si Bach[g] = 0, **R_isj|pole = −c0 bκ W_E,ij/Ω** ; R_ijk et R_sij sans pole.
- Contre-exemples : polarisation croix, k oblique (3,4,0), superposition de modes : pole present, relation exacte, lineaire en W_E. Diffeomorphisme lineaire : invariant. Ω → θΩ : R → R/θ, le pole subsiste. Reference g → θ²g : residu polaire nul.
- **Partie a (Euler)** : action de Wess-Zumino integrable ∫√g{bσC² + a[σ(E − ⅔□R) + 2σΔ₄σ]} (coefficient +2, et non « −½ » comme ecrit dans la mission). Fond T̂ = 6a ĝ (trace 24a correcte). A l'ordre ε, la partie non proportionnelle a g vaut 4k²(w_D − w_E)u cos kx/s², **identiquement nulle pour la combinaison integrable (1, 1, 1)** : la partie a se reduit a 6a ĝ_ab, covariantement constante, **sans contribution a R ; pole inchange**. Une combinaison non integrable donne un fond incoherent (non ∝ ĝ). Contre-termes locaux ∫R², ∫C² : nuls (⁽¹⁾H et Bach nuls pour une metrique d'Einstein).
- Manque : la partie non locale Γ[g] de la reference, b∫C ln(□/μ²)C sur η + εh, d'ordre ε et dependante de l'etat.
- R-E valide sous Bach[g] = 0 (vide Einstein-Λ) ; **invalide hors couche** : u = mode B + γs⁴ donne T̂_yy ∋ −48bγ s² ln s cos kx et R_ysy ∋ −72bκγ ln s cos kx ; pole en B inchange.
- Corrections : commentaire ligne 59 de irr_c.py ; etiquette G⁰₀ ; prolongement τ < 0 ; ne pas presenter le modele Q comme consequence de R-C ; pole porte par la seule partie electrique (mode B) ; hypotheses : φ fixe, premier ordre, sans retroaction, partie non locale absente, modes TT.

# S-c (audit de lecture)
Aucune contradiction frontale de T1 a F5, I1, I2. Verdicts : T1, T2, T4, T5, MP1, MP2, MP5, F2, F3, F4, F5 FIDELES ; nuances :
- T3 : ǧ = Ω̂⁻⁴ĝ est une consequence (« necessarily ») de (1) et (2) ; la clause « non obtenue en prolongeant les equations conformes » est [derive] (compatible avec l.104-105 et l.119-120 de Tod) ; Ω̂ est fixe par l'equation de champ fantome (13) avec φ₂ = 0 et Yamabe.
- T5 : developpement en puissances de r = e^{−Ht} ; Tod mentionne l'analyticite en r² du cadre de Fefferman et Graham (que cij viole).
- T6 : les demi-entiers n'apparaissent que dans les restes O(·) de la §7, en Ť (coordonnee, egale au temps propre a l'ordre dominant seulement).
- MP1 : le resume dit aussi « joins essentially smoothly » et « Accordingly ». MP3 : citation a completer par « – except at Hawking points such as H – ».
- MP4 : « fini a 𝓘⁺ » est [derive] ; la quantite conservee est l'integrale M = ∮ψ̃κ̃ (eq. 47) ; cote eon A, la conservation repose sur une isotropie locale « normally assumed ».
- MP5 : l'epoque GW est **proposee** ; MP evoquent des particules massives (matiere noire, « erebons ») qui se desintegrent en gravitons avant le raccord.
- F1 : FIDELE mais incomplet ; la these de l'article est qu'un champ **massif** (m² = 2λ/3) traverse aussi ; Friedrich juge « strong » l'exigence de Penrose de seuls champs sans masse pres du raccord.
- I1 : FIDELE a la lettre ; nuances : Friedrich envisage des pertes de lissite sans fixer de classe (et identifie les termes (m² − 2λ/3)Ω^{−k}) ; exposants non entiers chez Tod (en Ť) et chez MP (eq. 88-89 : F(η) ~ (η∞ − η)^{1/2 − √33/2}, exposant irrationnel au raccord ; MP concluent que l'ansatz « is no longer appropriate »).
- I2 : FIDELE pour le corps des textes ; reserve : le resume de MP presente la lissite comme decoulant de l'epoque GW (« Accordingly »), sans derivation dans le corps ; chez Friedrich, la lissite du prolongement est un resultat demontre (cas couverts), mais ce prolongement ne produit pas de Big Bang.
- Passages omis signales : Tod l.244 (φ₂ = 0, « Delayed Rest Mass Hypothesis »), l.121-122 (« element of risk »), l.481-482 (trace non nulle au troisieme ordre), l.248 (Yamabe pour I non compact) ; MP l.46 (« none actually contracts »), l.944-947, l.1023-1026 ; Friedrich l.128-142 (blow-up sans equations hyperboliques, instabilite), l.432-437 (« waist » etroit).
