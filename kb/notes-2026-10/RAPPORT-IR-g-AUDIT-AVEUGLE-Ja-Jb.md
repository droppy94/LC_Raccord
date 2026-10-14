---
id: RAPPORT-IR-g-AUDIT-AVEUGLE-Ja-Jb
date: 2026-10-11
objet: rapports des sous-agents J-a et J-b (audit froid aveugle de NOTE-108), substance reproduite fidelement
gel: NOTE-BORD-EON-112-ARMEMENT-AUDIT-IR-g (2026-10-11T15:23:12Z)
---

# Rapport J-a (re-derivation independante, cecite stricte, sans source)
Scripts dans /home/claude/audit_ja/ : ja_core.py (378a9175…), ja_q1.py (9ce52baa…), ja_q2.py (c54e4fad…), ja_q3.py (d159ba16…), ja_q45.py (ef24c39d…) et sorties (ja_q1.out e20470dc…, ja_q2.out 23bb9bda…, ja_q3.out 5fb1bead…, ja_q45.out e9809e0e…).

1. u₁ = 2c s ln s − k²u₀s² + … ; E porte un log (E = c(1 + 2β ln s) cos kx), B non. Log de X^M a l'ordre s² : X_ij|ln = e⁻²(2Q̃_ij − δ_ij tr Q̃), X_ss|ln = −e⁻² tr Q̃, X_si|ln = 0 (Q̃ = B_iB_j − E_iE_j local). Poynting sans log.
2. C-iso : trace et conservation verifiees ; constantes libres (C_rad, constante en β s²) et λ absentes des logs. **Loi trouvee par ajustement : R_isj|ln = −R_ijs = 3(κ/e²)(Q_ij − ⅓δ_ij tr Q), α = 3, γ = 0 ; la trace ne contribue pas.**
3. Quatre configurations non diagonales (polarisation oblique ; deux modes de k differents ; meme k, deux polarisations ; k₂ oblique) : loi exacte, composantes hors diagonale comprises. Termes croises entre k distincts nuls apres moyenne (verifie par integration directe) ; entre modes de meme k, a garder dans Q.
4. Source eteinte : B = −ak cos kD sin kx, E = ak sin kD cos kx ; Q = (a²k²/4)(ε_Bε_B − ε_Eε_E) + (a²k²/4) cos 2kD (δ − k̂k̂) ; partie independante de D sans trace. ⟨cos 2kD⟩ = (1 − 3x²)/(1 + x²)³ (n = 2), ~ −3/x⁴.
5. Dipole : ⟨ε_Bε_B − ε_Eε_E⟩ = (4/15)(3mm − m²δ) = (4/5)(mm − ⅓m²δ) ; orientations isotropes : 0.
6. Objet decisif : Q^TF = ⟨B_iB_j − E_iE_j⟩ − ⅓δ⟨B² − E²⟩ ; la dichotomie « magnetique / E = B » porte sur tr Q, qui n'entre pas.

# Rapport J-b (audit de ir_g.py et contre-exemples)
Empreinte conforme. Chaine independante (polynomes de Laurent en z_x, z_y, z_z ; Frobenius ; Christoffel conformes). Scripts dans /home/claude/audit_jb/work/ : jb_indep.py (f5fa52a2…), jb_g5.py (87a1fe1a…), jb_g34.py (c8b7de15…), jb_ferm.py (5e3bb32e…) et sorties.

| Point de ir_g.py | Verdict |
|---|---|
| Equation de mode, resolution, T_B, T_E, logs, moyenne, C-iso, R | OK |
| Reference Q codee a la main en diagonale, un seul mode | DEFAUT mineur (covariance et hors diagonale non testes) |
| Controle de trace (ligne 67) | DEFAUT mineur (tautologique) |
| Partie C | OK ; pour n pair la vraie decroissance est x^−(n+2) |
| Partie D | OK ; ligne 94 (Smiso) code mort |

- G1 confirme a l'ordre s² sur 11 configurations ; a l'ordre s³, X_sx porte un β ln s oscillant (sin 2kx), de moyenne nulle : ecrire « a l'ordre s² ».
- G2 confirme ; **loi tensorielle** R_isj|ln = (3βκ/e²)(Q_ij − ⅓δ_ij tr Q), hors diagonale comprise ; R_ssi, R_sij, R_kij sans log ; λ, C_r absents ; robuste a une deformation de T̂ (δ). Aucun contre-exemple.
- G3 confirme a la normalisation pres : avec Q moyenne spatiale, facteurs ¼ (non ½) ; le terme dependant de D alimente aussi Q_tf via (⅓𝟙 − k̂k̂) sauf distribution isotrope des k̂ ; le poids spectral doit etre celui de a²k².
- G4 confirme ((4/5)(mm − ⅓m²) ; isotrope nul ; ⟨ε_Bε_B + ε_Eε_E⟩_tf = (2/15)(mm − ⅓m²)).
- **G5 : premiere moitie valide, seconde moitie invalide.** Contre-exemples calcules a Q = 0, donc sans log : T7 onde progressive **circulaire** (coherente, polarisee) ; T9 onde stationnaire helicoidale ; T11 faisceau non polarise anisotrope a E = B. Q_tf d'une onde progressive mesure sa seule polarisation lineaire (elliptique : Q = diag(0, −3/2, 3/2), non nul). Condition exacte : ⟨B_iB_j⟩_tf = ⟨E_iE_j⟩_tf.
- Convention : en τ, R_iτj = −R_isj (coefficient −3βκ/e²).
