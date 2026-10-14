---
id: RAPPORT-IR-m-AUDIT-AVEUGLE
date: 2026-10-11
objet: rapports des sous-agents M-a1, M-a2, M-a3 et M-b (audit froid aveugle conjoint de NOTE-111, NOTE-116, NOTE-118), substance reproduite fidelement
gel: NOTE-BORD-EON-119-ARMEMENT-AUDIT-IR-m (sha256 220717a01d612de6…, sceau 2026-10-11T16:58:02Z)
scripts: copies dans D:\temporaire\audit_ir_m\ (sous-dossiers ma1, ma2, ma3, mb)
---

# Rapport M-a1 (re-derivation independante du bloc I, cecite stricte)
Scripts : q1_loi_locale.py (fae5f6a7…), q2_dipole.py (bc315077…), q3_compensation.py (6cee6500…) ; sorties q1_out_NS4.txt (305a474d…), q1_out_NS5.txt (35e45fa1…), q2_out.txt (a3968cde…), q2_out_D80_w2.txt (3ca3f4c2…), q3_out.txt (c5149ee4…), figure q2_profil_a_r.png (a6d51daf…).

1. Loi locale, mode A_y = u cos kx, fermeture H-loc. u₁ = α₀ + s(α₁ + 2c ln s) + … ; E porte le log 2βc ln s, B non. tr X^M = 0. Conservation satisfaite jusqu'a s^{NS+1} (NS = 4 et 5). 12 constantes libres, X^R sans log jusqu'a s³.
   - (a) Coefficient de β ln s a s⁰ : R_xsx = (κ/e²)(c²cos²kx − k²u₀²sin²kx) ; R_ysy = (κ/e²)(−2c²cos²kx − k²u₀²sin²kx) ; R_zsz = (κ/e²)(c²cos²kx + 2k²u₀²sin²kx) ; toutes les autres composantes nulles ; pas de ln², pas de puissance negative. **R_isj|ln = (3κ/e²) Q_tf,ij(x) point par point**, harmoniques comprises, identique en NS = 4 et NS = 5. Mecanisme : partie sans trace de T_ij a l'ordre s² ln s = (2β/e²) Q_tf ; une contrainte s²(σ ln s + τ) sans trace donne (κ/2)(3 ln s + 1)σ + (3κ/2)τ dans R_isj.
   - (b) Gradients a l'ordre s ln s seulement, coefficient κ/e² : R_ssx = −(κ/e²)∂_x tr Q ; R_yxy = (κ/e²)∂_x Q_yy ; R_zxz = (κ/e²)∂_x Q_zz.
   - (c) Coefficients de log a s⁰ et s¹ independants des 12 constantes, de α₀, α₁, λ.
2. Dipole eteint (f = ½(1 − tanh((t + D)/w)), D = 40, w = 1, puis D = 80, w = 2). Maxwell verifie pour f arbitraire ; forme fermee B = m₀[(3n n_z − ẑ)(f/r³ + f′/r²) + (n n_z − ẑ) f″/r], E = −m₀(ẑ × n)(f′/r² + f″/r).
   - r < D : champ nul aux queues exponentielles pres (1e-55 a D/4, 1e-13 a D − 6w) ; pas de log.
   - Coquille r ≈ D : epaisseur ~w, Q_tf ~ m₀² f″²/D².
   - r > D : statique pur, Q_tf ∝ r⁻⁶.
   - Moyenne angulaire exacte ⟨Q_tf⟩ = a(r)(m̂m̂ − ⅓𝟙), a = m₀²[2α²/15 − 2αβ/3 + β² + S²/3] ; statique a = m₀²/(5r⁶) (1/5) ; rayonne a = (4/5)m₀² m̈²/r² (4/5) ; meme signe.
   - Integrales J = ∫a r² dr : coquille 0,2133328 contre 16/(75w³) = 0,2133333 (w = 1) ; 0,0266666 contre 0,0266667 (w = 2) ; reliquat 1/(15 r³_min) ; boule ~1e-17.
3. Compensation sans H-loc : oui, formellement. δX_ij = s² ln s σ_ij sans trace et conservee donne (3κ/2)σ_ij ln s dans R_isj ; σ = −(2/e²)Q_tf annule le log ; pour σ(x) la conservation se referme ordre par ordre. Le contenu predictif de la loi locale repose sur H-loc.

# Rapport M-a2 (re-derivation independante du bloc L, cecite stricte)
Scripts : ma2_q1_q3.py (e5283a66…), ma2_q4_q6.py (b55a8578…) ; sorties ma2_q1_q3.out (206a7074…), ma2_q4_q6.out (d7f579a5…).

1. a = i(J₊ − J₋)/(2k), b = −(J₊ + J₋)/2 ; controle numerique a 1e-11.
2. **Q_k = −½ L[J₊J₊† + J₋J₋†] − ½ Re(J₋†J₊) P_⊥** (identite symbolique exacte). Partie diagonale : polarisation lineaire seule (intensite compensee, V eliminee par la partie reelle). Partie d'interference proportionnelle a P_⊥, de partie sans trace non nulle mode par mode.
3. Interference ∝ e^{2ik t₀}, tend vers 0 apres moyenne de bande (Riemann-Lebesgue) ; bande lisse : decroissance rapide ; bande a bords francs : O(1/(|t₀|Δk)).
4. **Seule la composante E, ℓ = 2 survit** (E pur ℓ = 2 : (8π/5)T ; B ℓ = 2, E et B ℓ = 3, 4 : 0). Application de rang 5 : **5 conditions reelles**.
5. Lois : dipole electrique +c STF Re(pp†) ; magnetique −c STF Re(mm†) ; terme croise E1 × M1 nul. Lineaire m : ≠ 0 ; p : ≠ 0, signe oppose ; tournant : +c STF(ẑẑ) ≠ 0 ; chiral : L = 0 en chaque direction ; **p = m colineaires en phase (helicite nulle) : ∫L = 0 (motif B pur) alors que L ≠ 0 localement** ; isotrope : 0 en moyenne d'ensemble ; E ℓ = 2 : cT ; B ℓ = 2 : 0 ; generique : ≠ 0. Condition pour des dipoles : STF Re(pp†) = STF Re(mm†). L'helicite partielle ne suffit pas ; l'helicite n'est pas necessaire.
6. ⟨ε_Bε_B − ε_Eε_E⟩ = (4/5)(mm − ⅓m²𝟙) ; ε_Bε_B − ε_Eε_E = −2L point par point ; ⟨L⟩ = −(2/5)(mm − ⅓m²𝟙).
7. Classe Q_tf = 0 exceptionnelle (codimension 5) : isotropie, helicite pure, motifs B purs, equilibre E1/M1.

# Rapport M-a3 (re-derivation independante du bloc K, cecite stricte)
Scripts : q1_divergence.py (51e78428…), q2_riegert.py (5baf8937…), q3_cotton_maxwell.py (c6ad34ab…), q4_psi_regularite.py (71a133a8…) ; sorties q1_output.txt (6a5f8fe9…), q2_output.txt (43408024…), q3_output.txt (c2efcec2…), q4_output.txt (5b9713ff…).

1. ∇^μ X^M_μν + ¼ ∂_ν(I²)F² = 0 exactement sur couche, pour I²(s) quelconque, mode non moyenne ; seule la composante s non nulle ; **pas de log au premier ordre en β**.
2. Δ₄ = □² + 2R^{μν}∇_μ∇_ν − ⅔R□ + ⅓∇^μR∇_μ ; F₄ = E − ⅔□R + bC² ; fond : Δ₄(−ln s) = 6, F₄ = 24. Densite d'ordre ε independante de b, sans ln s, egale a (1/6)□_η R^(1)[h] ; par covariance de Weyl (σ = φ), **φ disparait identiquement**. δS_b/δh₁ = (1/6)(∂_x²□ψ − □²ψ) ; δS_b/δh₂ = δS_b/δh₃ = −(1/6)□²ψ. Pas de log, pas de φ ni de ses derivees ; T^(b)_ii ~ s² pour ψ lisse ; T_yy = T_zz, T_yz = 0.
3. R avec T = X^M seul : **loi (3κ/e²)Q_tf reproduite exactement** sur les 9 composantes R_isj ; autres logs seulement sous-dominants (s ln s, s² ln s).
4. T^(b) ne peut pas compenser (pas de log ; T_yy = T_zz alors que Q_tf distingue y et z). ψ analytique. T^W sans log si W est exactement invariant de Weyl et regulier. Hypotheses : H1 ψ lisse (automatique) ; H2 famille diagonale (hors diagonale par covariance) ; **H3 regularite de W : un facteur de forme non local F ln(□/μ²)F est singulier sur des ondes a impulsion nulle, cas des ondes planes du mode** ; H4 premier ordre, auxiliaires sur couche, J fixe.

# Rapport M-b (audit des scripts, reproduction, contre-exemples)
Empreintes des cinq scripts conformes. Scripts : indep_I.py (7f438197…), indep_I_ferm.py (0b53ea3f…), check_r31.py (381ee85f…), inspect_i.py (feddbe9d…), ir_i_flag.py (be9b815d…), indep_dipole2.py (8839cee7…), indep_dipole3.py (4c6be7ee…), indep_L.py (8c57fda6…), indep_K.py (08c49234…), indep_K_weyl.py (02d51b4d…) et sorties ; indep_dipole.py (ed122f58…) est un premier essai defectueux conserve (R-55).

**Bloc I**
- I-A confirmee et generalisee : deux polarisations (A_y = u cos kx, A_z = v sin kx), Q_yz ≠ 0 ; loi tensorielle hors diagonale exacte ; aucun gradient a s⁰. Preuve structurelle : div X^M|₀ + T̂/s = 0, X^R obeit a un systeme hyperbolique a coefficients constants, **X^R sans log a tous les ordres sous H-loc**.
- DEFAUT 1 : le test « coefficients libres hors des logs » de ir_i.py est aveugle (d/dβ pris avant la recherche des symboles libres). 6 des 60 libres sont des donnees de Cauchy, 54 des artefacts de troncature. Mis a l'ordre β, r31 entre a l'ordre s ln s (κa/6). A s⁰, aucun libre n'entre. Affirmation vraie a s⁰, non demontree a s ln s.
- I-A' confirmee : drapeau corrige True ; test diagonal accepte ±ref (defaut mineur).
- I-B : moyennes 1/5 et 4/5 confirmees (7/15 + 1/3) ; boule sans champ aux queues tanh pres. DEFAUT 2 : bornes reelles D ∓ 6w, etiquetees D ∓ 3w. **DEFAUT 3 : la prediction 21,36 est un artefact de quadrature (∫m″² = 2,1243 au lieu de 32/15) ; vraie prediction 21,44661 ; ecart reel −1,8e-5, pas 0,4 % ; l'explication par le melange statique-rayonne est sans objet.** Integrale totale = prediction rayonnee a 1e-9 (reliquat statique compense par les termes croises d'induction dans la coquille).

**Bloc L**
- L-A, L-B confirmees (200 tirages, 3e-15). L-D confirmee par quadrature spherique independante (1e-15).
- L-C : condition E ℓ = 2 et codimension 5 correctes (dipoles : 5 conditions sur ℝ¹²). **L'enumeration des trois classes est tautologique** : sources physiques a Q_tf = 0 hors helicite pure et hors ensemble isotrope : p ∥ m, |p| = |m|, phase quelconque (⟨L⟩ = 0, L local jusqu'a 0,996) ; p = x + iy, m = x − iy. Correction : « Q_tf = 0 ssi E₂ = 0 (codimension 5) ; helicite pure et ensemble isotrope en sont deux cas particuliers ».
- Interference : rapport ≈ e^{−2t₀²/σ²} pour une enveloppe gaussienne ; 0,13 pour σ = 10, t₀ = −10 : la moyenne est asymptotique (|t₀| ≫ duree de la source) et globale ; aimant eteint (cas du bloc I) : 4e-5 a t₀ = −2, bruit numerique des |t₀| ≥ 5.

**Bloc K**
- K-A confirmee (identite exacte ; residu nul de s⁰ a s⁵).
- K-B confirmee et generalisee : par covariance de Weyl, √g(Δ₄φ − F₄/4) = −¼√ḡ F̄₄, φ disparait ; controle brut sur une famille **non diagonale dependant de (s, x, y)** (H_sx, H_xy, H_zz) : aucun log. T_2 = T_3 decoule de la symetrie y ↔ z (pas un controle). ψ lisse est automatique.
- K-C confirmee (indep_I, X^M seul, deux polarisations) ; elle suppose que le reste de T est sans log (c'est K-B).
- K-D valide sous hypotheses : (1) tenseur plat du secteur invariant de Weyl lisse en s = 0 (sinon contre-exemple X′ = s² ln s diag(0,0,f,−f)(x), conserve et sans trace, donnant (3κ/2) f ln s) ; (2) **T evalue sur le fond** : le terme de Riegert en charge de Weyl ∫√g φ C² (φ nu) est nul sur le fond mais donne ln s × ∂⁴h (type Bach) a l'ordre lineaire en h (indep_K_weyl) ; si la reponse metrique h est d'ordre β, logs possibles d'ordre b·β ; (3) premier ordre en β, forme de I². Qualifications inutiles : famille diagonale (vaut pour tout H) ; « ψ causal et lisse » (decoule de l'equation).
