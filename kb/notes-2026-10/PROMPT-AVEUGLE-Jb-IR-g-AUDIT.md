# Prompt J-b : audit du code et des affirmations (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail qui a produit les fichiers ci-dessous. Lis uniquement les fichiers de /home/claude/audit_jb/ (ir_g.py et ir_g_sortie.txt) ; ne cherche pas d'autres notes ou fichiers sur le disque. Travaille avec sympy (python3) dans /home/claude/audit_jb/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

Verifie d'abord l'empreinte : ir_g.py sha256 69496f141995e957fceeff25441fd499ce8c008bc224e5d412ea6ea1eb2208c4.

## Cadre (rappel)
de Sitter H = 1, s = −τ = Ω > 0, ĝ = Ω⁻²η ; action simplifiee I² = e⁻²[1 + 2β(λ − ln s)] ; premier ordre en β ; mode A_y = u(s)cos(kx), u = u₀cos(ks) + (c/k)sin(ks) + βU₁ ; X^M = I²(F F ĝ⁻¹ − ¼ĝ F·F) ; fermeture isotrope C-iso pour la partie homogene (X^R = diag(r0,r1,r1,r1), trace = T̂ = −(β/2e²)⟨F²⟩_η Ω⁴, conservation) ; L̂ = (κ/2)(T − ⅓ĝ trT) ; R_ρνλ = Ω⁻¹(∇̂_νL̂_λρ − ∇̂_λL̂_νρ).

## Affirmations soumises a l'audit
- G1 : le coefficient de β ln s dans X^M (non moyenne, ordre s²) vaut exactement −2(T_B − T_E), ou T_B, T_E sont les tenseurs de Maxwell (I² = 1/e²) de la seule partie magnetique (A_y = u₀cos kx) ou electrique (A_y = c s cos kx) ; la composante de Poynting (s, x) n'a pas de log.
- G2 : pour la partie homogene sous C-iso, le coefficient de ln s a l'ordre s⁰ dans R_{isi} vaut (3βκ/e²) × (Q − ⅓ tr Q)_ii, Q = ⟨B_iB_j − E_iE_j⟩ ; la partie isotrope de R n'a pas de log ; la trace de Q (⟨F²⟩/2) ne contribue donc pas.
- G3 : source eteinte a τ = −D depuis une configuration magnetostatique : amplitudes B = ak cos kD, E = ak sin kD ; par mode Q = ½a²k²(ε_Bε_B − ε_Eε_E) + ½a²k² cos(2kD)(ε_Bε_B + ε_Eε_E) ; le premier terme ne depend pas de D. Moyenne spectrale de cos 2kD (spectre kⁿ e^{−k/k⋆}) : (1 − 3x²)/(1 + x²)³ pour n = 2, decroissance en loi de puissance pour x = 2k⋆D grand.
- G4 : dipole magnetique : ⟨ε_Bε_B − ε_Eε_E⟩_angles = (4/5)(mm − ⅓m²𝟙) ; moyenne nulle sur des orientations isotropes de m.
- G5 : conclusion : le critere « dominante magnetique / E = B » n'est pas celui qui decide du ln de (2.17) ; l'objet decisif est la partie sans trace de Q ; elle survit pour tout champ coherent polarise et ne s'annule que pour un ensemble isotrope non polarise ; E = B en module ne suffit pas.

## Mission
1. Audite ir_g.py point par point (equation de mode et sa resolution, construction de T_B et T_E, extraction des logs, moyenne, fermeture C-iso, extraction des composantes de R et convention d'indices, partie C, partie D) : OK / DEFAUT, avec controles independants la ou un controle du script serait tautologique.
2. Reproduis G1 a G4 independamment.
3. **Cherche activement des contre-exemples a G2** : Q non diagonal (polarisation oblique, k oblique), superposition de deux modes de directions differentes (termes croises), polarisation circulaire, dependance a λ ou aux constantes de la fermeture, autres composantes de R que (i, s, i). La loi garde-t-elle son coefficient 3 ? Doit-elle etre ecrite comme une loi tensorielle (composantes hors diagonale de R) ?
4. Juge G5 : valide, valide sous hypotheses (nomme-les : partie homogene, C-iso, premier ordre, etat), ou invalide.
5. Liste reserves et corrections.

Rends un rapport structure avec les empreintes de tes scripts et sorties.
