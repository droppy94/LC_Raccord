# Prompt S-b : audit des scripts et des affirmations, recherche de contre-exemples (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail qui a produit les fichiers ci-dessous. Lis uniquement les fichiers de /home/claude/audit_sb/ ; ne cherche pas d'autres notes ou fichiers sur le disque (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/ ni dans d'autres dossiers audit_*). Travaille avec sympy (python3) dans /home/claude/audit_sb/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

Verifie d'abord les empreintes sha256 :
- irq_diff.py 750ccc53430be3eaafb8d07ac963d5f740cc27774159c948de25e2988aa10a21
- irr_c.py ef0c3f4fac14d233652deafaf931348b47736596f9ff33aa3fc678de7019cde9
- irr_c_ctrl.py 8035a342d686d4f2a760f5469d960812e8a03f659ba9c439c40c77303bb548ed

## Affirmations soumises a l'audit
**Bloc Q (irq_diff.py, irq_diff_sortie.txt)**
- Q-A : dans le modele g = −dτ² + (δ + ε d f) dx dx, d = diag(1,1,−2), f = τ⁴ ln τ, la courbure de Weyl electrique de g vaut (−3, −3, 6)·ε(τ² ln τ + (7/12)τ²) ; W = C/Ω (Ω = τ) est continue en 0 et dW/dτ porte ln τ (signature d'un second membre en ln Ω dans l'equation de Bianchi rescalee).
- Q-B : g est C³ et non C⁴ en τ = 0.
- Q-C : pour l'eon suivant ǧ = τ² g, en temps propre Ť = τ²/2, le fond est une radiation (G_00 = −3/(4Ť²), G_ii = 1/(4Ť²)) et la perturbation est une contrainte spatiale sans trace ∝ d (5 ln Ť + ln 32 + 9/2), sans terme en G_00.

**Bloc R (irr_c.py, irr_c_ctrl.py et sorties)**
- R-A : la forme fermee T_ab = c0 ∂^c∂^d(φ C_acbd[h]), φ = −ln s, coincide avec la variation brute d'Euler-Lagrange de φC² (facteur λ = −1/4, c0 = −8 retenu).
- R-B : pour ĝ = s⁻²(η + εh), h_yy = −h_zz = u cos kx, u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks), le tenseur physique T̂ = s² T est sans trace, conserve, sans ln s, avec T̂_yy = −T̂_zz = b(−4Bk³ s + 4Ak⁴ s²) cos kx + O(s³).
- R-C : le second membre R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), L̂ = (κ/2)(T̂ − ⅓ĝ trT̂), porte un pole : R_ysy = −R_zsz = −4bκBk³ cos kx/s + regulier.
- R-D : la partie electrique du Weyl rescale a 𝓘⁺ vaut W_E,yy = −Bk³ cos kx/2, d'ou R_isj|pole = (8bκ/Ω) w_ij.
- R-E (affirmation derivee) : le coefficient du terme en ln s de T^(C), proportionnel au tenseur de Bach de g, s'annule sur couche pour une onde du vide.

## Mission
1. Audite chaque script point par point (OK / DEFAUT), avec des controles independants la ou un controle serait tautologique. En particulier : la normalisation c0 (relation entre la variation brute et T_ab = (2/√g)δS/δg^{ab}), le passage T̂ = s² T, les Christoffel du fond, les conventions de signe de R.
2. Reproduis independamment R-B, R-C, R-D, Q-A, Q-B, Q-C.
3. **Cherche activement des contre-exemples** :
   - polarisation « croix » (h_yz), k oblique, superposition de deux modes ;
   - le pole est-il un artefact de jauge (diffeomorphisme lineaire) ou de choix de facteur conforme (Ω → θΩ, θ lisse) ?
   - le pole subsiste-t-il si l'on ajoute au terme φC² la contribution a l'ordre ε de la partie de l'action anomale associee a la densite d'Euler (de la forme ∫√g [φ(E − ⅔□R) − ½ φΔ₄φ] a un coefficient pres) ? Si c'est faisable, calcule-la sur le meme mode ; sinon, dis ce qui manque ;
   - l'absence de ln s (R-E) tient-elle pour un h non solution du vide (h source par une matiere) ?
4. Juge chaque affirmation : valide, valide sous hypotheses (nomme-les), ou invalide.
5. Liste reserves et corrections.

Rends un rapport structure (blocs Q et R) avec les empreintes de tes scripts et sorties.
