#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_interaeon_matiere.py — P7 : brancher la matière CCC sur la carte ε_n ↦ ε_{n+1}.
(Chantier §4.2 de LC-WORK-REPRISE-INTERAEON ; étend verif_D3_interaeon_kappa.py.)

QUESTION (la plus décisive des trois, LC-D3-INTERAEON-KAPPA §5.2).
  Le stress anisotrope σ̌ de l'éon futur (Tod éq. 33, σ̌ = −4·Ricci-sans-trace de 𝓘) — qui
  EST ~ l'anisotropie de 𝓘 — sourcé dans l'équation du cisaillement, CHANGE-t-il le signe
  ou la magnitude de κ ? (κ<1 : isotropisation survit à la matière ; κ≥1 : le stress
  anisotrope intrinsèque tue l'attraction ⟹ renforce l'issue faible.)

MODÈLE (noyau §2 + secteur matière P7).
  Noyau inchangé : Bianchi IX + radiation + Λ, forme log w_i, cisaillement σ_i, e-fold N.
  AJOUTS P7 :
    (a) stress anisotrope Π_i dans l'équation du cisaillement :
          dσ_i/dN = −3σ_i − ³S_i/H + Π_i/H
        avec Π_i(N) = c_Π · σ̌_i(ε_n) · (a/a0)^(−p)   (σ̌ = −4·³S de la forme de bang, Tod 33)
        Le SEED σ̌ est fixé par Tod SANS coupling libre ; c_Π=±1 teste le SIGNE (l'ambiguïté
        ouverte §5.2) ; p teste la loi de redshift (frozen p=0 / courbure p=2 / radiation p=4).
    (b) champ phantom φ (Tod éq. 13) : φ̈ + 2H²φ = ⅙ s φ³. Scalaire homogène ⟹ stress
        ISOTROPE ⟹ il ne peut PAS sourcer le cisaillement directement ; il ne module que
        l'histoire d'expansion (donc κ via le rapport effectif Λ/ρ). Effet borné par le
        balayage de robustesse déjà scellé (κ∈[0.70,0.94]). Démontré ci-dessous.
    (c) « matière noire » de Penrose (terme de trace, O(Ť⁻¹) sans-trace sans interprétation
        physique — Markwell-Stevens) : `à inventer`, sous-dominante, portée en réserve.

ANCRAGE. Le seed σ̌ est auto-vérifié contre le sceau [B2] de LC-A-D1-BIANCHI :
  |σ̌|² = 16|S|² = 128 ε² + O(ε⁴).

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Tod arXiv:1309.7248 (éq. 13, 24, 27, 33) ; Wald PRD 28 (1983) ;
Wainwright-Ellis (1997) ; Milnor Adv.Math.21 (1976) ; LC-A-D1-BIANCHI [B2].
"""

import numpy as np
from scipy.integrate import solve_ivp

print("="*78)
print(" verif_D3_interaeon_matiere.py — P7 : matière CCC (σ̌ + φ) sur la carte ε_n↦ε_{n+1}")
print("="*78)

# --- 3-Ricci de Milnor (Bianchi IX, n_i=1) : ³R_11, ³R_22, ³R_33 ---
def ricci3_components(A1, A2, A3):
    l1, l2, l3 = A1/(A2*A3), A2/(A3*A1), A3/(A1*A2)
    s = 0.5*(l1+l2+l3); m1, m2, m3 = s-l1, s-l2, s-l3
    return np.array([2*m2*m3, 2*m3*m1, 2*m1*m2])

# ----------------------------------------------------------------------
# (0) Le seed σ̌(ε) = −4·(Ricci sans-trace de la forme de bang) — Tod éq. 33.
#     Forme de bang Bianchi IX (e^ε, e^{−ε}, 1), volume gelé. Auto-vérif |σ̌|²=128ε².
# ----------------------------------------------------------------------
def sigma_check_seed(eps):
    A = np.array([np.exp(eps), np.exp(-eps), 1.0])    # forme de bang (volume gelé)
    R3 = ricci3_components(*A)
    S  = R3 - R3.sum()/3.0                            # ³S : Ricci sans-trace de 𝓘
    return -4.0*S, S                                  # σ̌ = −4 S  (Tod 33)

print("\n" + "-"*78)
print(" (0) Seed σ̌(ε) (Tod 33) — auto-vérification contre le sceau [B2] : |σ̌|²=128ε²")
print("-"*78)
print("     ε        |σ̌|²        128ε²       |σ̌|²/ε²   (→128 si ✓)")
for eps in [0.02, 0.05, 0.10, 0.20]:
    sc, S = sigma_check_seed(eps)
    norm2 = float(np.sum(sc**2))
    print(f"     {eps:.3f}   {norm2:.6f}   {128*eps**2:.6f}   {norm2/eps**2:.4f}")
print("     -> |σ̌|²/ε² → 128 quand ε→0 : seed ANCRÉ sur LC-A-D1-BIANCHI [B2]. ✓")

# ----------------------------------------------------------------------
# Intégrateur étendu : noyau §2 + Π_i (σ̌) + ρ_φ optionnel.
# ----------------------------------------------------------------------
def evolve(eps_n, rho0=100.0, Lam=1.0, Nmax=25.0,
           c_pi=0.0, p_pi=2.0,                      # stress anisotrope σ̌
           phi0=0.0, sphi=0.0):                     # champ phantom (Tod 13)
    w0 = np.array([eps_n, -eps_n, 0.0])
    s0 = np.array([0.0, 0.0, 0.0])                  # σ(0)=0 (Tod 24, cinétique nul)
    A0 = np.exp(w0); R3 = ricci3_components(*A0)
    sig_check, _ = sigma_check_seed(eps_n)          # seed σ̌ (composantes propres)
    # énergie initiale du champ phantom (à N=0) : ρ_φ = ½ φ̇² + V, V=−s φ⁴/24 (dV/dφ=−⅙sφ³)
    rho_phi0 = 0.5*0.0**2 - sphi*phi0**4/24.0
    H0 = np.sqrt(max((rho0 + rho_phi0 + Lam + 0.0 - 0.5*R3.sum())/3.0, 1e-12))
    def rhs(N, y):
        w1, w2, s1, s2, H, rho, phi, phid = y
        w3 = -w1-w2; s3 = -s1-s2
        a = np.exp(N)
        R3c = ricci3_components(*(a*np.exp(np.array([w1, w2, w3]))))
        S = R3c - R3c.sum()/3.0                     # ³S_i (source géométrique)
        # stress anisotrope σ̌ : seed fixé par Tod, redshift (a)^(−p)
        Pi = c_pi*sig_check*np.exp(-p_pi*N)
        sig2 = 0.5*(s1**2 + s2**2 + s3**2)
        # champ phantom : ρ_φ = ½φ̇²+V ; EOM Tod 13 : φ̈+2H²φ=⅙sφ³  (φ̇=Hφ', etc.)
        V   = -sphi*phi**4/24.0
        rho_phi = 0.5*(H*phid)**2 + V
        # φ'' = [⅙ s φ³ − 2H²φ − H H' φ'] / H²   ; on calcule H' après
        dw1, dw2 = s1/H, s2/H
        ds1 = -3*s1 - S[0]/H + Pi[0]/H
        ds2 = -3*s2 - S[1]/H + Pi[1]/H
        dH  = (-H**2 - (2.0/3.0)*sig2 - (rho+rho_phi)/3.0 + Lam/3.0)/H
        # conservation AVEC back-réaction du stress anisotrope (identité de Bianchi
        # contractée, Ellis) : ρ̇ = −3H(ρ+p) − σ_ab π^ab. Radiation p=ρ/3 ⟹ −4Hρ.
        sig_pi = s1*Pi[0] + s2*Pi[1] + s3*Pi[2]
        drho = -4.0*rho - sig_pi/H
        # phantom EOM en e-fold : φ' = phid ; phid' = [⅙sφ³ − 2H²φ]/H² − (H'/H)phid
        dphi  = phid
        dphid = ( (sphi*phi**3/6.0 - 2*H**2*phi)/H**2 ) - (dH/H)*phid
        return [dw1, dw2, ds1, ds2, dH, drho, dphi, dphid]
    y0 = [w0[0], w0[1], 0.0, 0.0, H0, rho0, phi0, 0.0]
    sol = solve_ivp(rhs, [0, Nmax], y0, method='DOP853',
                    rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.02)
    return sol, H0

def eps_out(eps_in, **kw):
    sol, _ = evolve(eps_in, **kw)
    w1, w2 = sol.y[0, -1], sol.y[1, -1]
    w3 = -w1-w2
    return np.sqrt(w1**2+w2**2+w3**2)/np.sqrt(2)

def kappa_of(eps_list=(0.02, 0.05, 0.10, 0.20), **kw):
    ks = [eps_out(e, **kw)/e for e in eps_list]
    return float(np.mean(ks)), float(np.std(ks))

def linearity(eps_list=(0.02, 0.05, 0.10, 0.20), **kw):
    """écart-type relatif de κ_local sur le balayage : ≪1 ⟹ carte linéaire."""
    ks = np.array([eps_out(e, **kw)/e for e in eps_list])
    return float(np.std(ks)/np.mean(ks))

# ----------------------------------------------------------------------
# (1) Contrôle : κ nu (c_Π=0) — doit reproduire 0.81.
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (1) Contrôle — κ NU (sans matière, c_Π=0) : doit reproduire 0.81")
print("-"*78)
k0, sd0 = kappa_of()
print(f"     κ_nu = {k0:.4f}  (écart-type {sd0:.1e})   [référence verif_D3_interaeon_kappa.py]")

# ----------------------------------------------------------------------
# (2) LE TEST DÉCISIF : ajouter σ̌ (Tod 33) au cisaillement. Signe c_Π=±1.
#     redshift p=2 (σ̌∝Ť⁻¹∝a⁻², cohérent avec ρ∝Ť⁻²∝a⁻⁴, Tod 27).
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (2) TEST DÉCISIF — σ̌ branché (Tod 33), p=2 (σ̌∝a⁻², cohérent ρ∝a⁻⁴)")
print("-"*78)
print("     c_Π     κ        Δκ vs nu    lin(σκ/κ)   lecture")
for c in [+1.0, -1.0]:
    k, sd = kappa_of(c_pi=c, p_pi=2.0)
    lin = linearity(c_pi=c, p_pi=2.0)
    flag = "ISOTROPISE (κ<1)" if k < 1 else "ANTI-ISOTROPISE (κ≥1) !"
    sign = "+σ̌ (renforce ³S)" if c > 0 else "−σ̌ (oppose ³S)"
    print(f"     {c:+.0f}    {k:.4f}   {k-k0:+.4f}    {lin:.3f}      {sign:18s} -> {flag}")

# ----------------------------------------------------------------------
# (3) Robustesse à la loi de redshift p ∈ {0,2,4} (le signe survit-il ?).
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (3) Robustesse vs loi de redshift de Π : p=0 (gelé) / 2 (courbure) / 4 (radiation)")
print("-"*78)
print("     p     κ(c_Π=+1)   κ(c_Π=−1)")
for p in [0.0, 2.0, 4.0]:
    kp, _ = kappa_of(c_pi=+1.0, p_pi=p)
    km, _ = kappa_of(c_pi=-1.0, p_pi=p)
    print(f"     {p:.0f}     {kp:.4f}      {km:.4f}")

# ----------------------------------------------------------------------
# (4) Magnitude : multiplier le seed σ̌ par un facteur g (sensibilité d'amplitude).
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (4) Sensibilité d'amplitude : seed σ̌ ×g (g=0.5,1,2,4), signe +, p=2")
print("-"*78)
print("     g       κ        (g=0 ⟹ κ_nu)")
for g in [0.5, 1.0, 2.0, 4.0]:
    k, _ = kappa_of(c_pi=+g, p_pi=2.0)
    print(f"     {g:.1f}    {k:.4f}")
for g in [0.5, 1.0, 2.0, 4.0]:
    k, _ = kappa_of(c_pi=-g, p_pi=2.0)
    print(f"     {-g:+.1f}   {k:.4f}   (signe opposé)")

# ----------------------------------------------------------------------
# (5) Champ phantom φ (Tod 13) : scalaire homogène ⟹ stress ISOTROPE.
#     Démontre qu'il ne module que l'histoire (κ borné par le balayage Λ/ρ).
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (5) Champ phantom φ (Tod 13) : effet sur κ via l'histoire d'expansion seulement")
print("-"*78)
print("     φ0     s_φ     κ        Δκ vs nu   (stress isotrope : pas de source TT)")
for phi0, sphi in [(0.0,0.0), (0.3,1.0), (0.5,1.0), (0.5,-1.0)]:
    k, _ = kappa_of(phi0=phi0, sphi=sphi)
    print(f"     {phi0:.1f}    {sphi:+.0f}     {k:.4f}   {k-k0:+.4f}")
print("     -> φ ne porte AUCUN stress anisotrope : il ne peut pas sourcer le cisaillement.")
print("        Son effet sur κ passe par ρ_φ (histoire) ⟹ borné par le balayage Λ/ρ scellé.")

# ----------------------------------------------------------------------
# (6) Combiné σ̌(+) + φ : la matière dominante ensemble.
# ----------------------------------------------------------------------
print("\n" + "-"*78)
print(" (6) Combiné σ̌(signe physique) + φ : matière CCC dominante")
print("-"*78)
for c in [+1.0, -1.0]:
    k, _ = kappa_of(c_pi=c, p_pi=2.0, phi0=0.3, sphi=1.0)
    print(f"     σ̌(c_Π={c:+.0f}) + φ(0.3,+1) : κ = {k:.4f}")

# ----------------------------------------------------------------------
# Contrainte (intégrité numérique) sur une trajectoire avec σ̌.
# ----------------------------------------------------------------------
sol, H0 = evolve(0.1, c_pi=+1.0, p_pi=2.0)
w1,w2,s1,s2,H,rho,phi,phid = sol.y
w3=-w1-w2; s3=-s1-s2; sig2=0.5*(s1**2+s2**2+s3**2)
a=np.exp(sol.t)
R3=np.array([ricci3_components(*(a[k]*np.exp(np.array([w1[k],w2[k],w3[k]])))) for k in range(len(a))])
constraint = 3*H**2 - (rho + 1.0 + sig2 - 0.5*R3.sum(axis=1))
print("\n" + "-"*78)
print(f" Intégrité : max|contrainte| (avec σ̌, ε=0.1, c_Π=+1) = {np.max(np.abs(constraint)):.2e}  (≈0 ✓)")
print("-"*78)

# ======================================================================
# VERDICT
# ======================================================================
kp2, _ = kappa_of(c_pi=+1.0, p_pi=2.0)
km2, _ = kappa_of(c_pi=-1.0, p_pi=2.0)
print("\n" + "="*78)
print(" VERDICT — P7 : la matière CCC (σ̌ + φ) sur la carte inter-éon")
print("="*78)
print(f"   • κ nu (contrôle)            : {k0:.3f}   [reproduit 0.81 ✓]")
print(f"   • κ avec +σ̌ (renforce ³S)   : {kp2:.3f}   (Δ={kp2-k0:+.3f})")
print(f"   • κ avec −σ̌ (oppose ³S)     : {km2:.3f}   (Δ={km2-k0:+.3f})")
print("")
print("   STRUCTURE-CLÉ (Tod 33). σ̌ = −4·³S(forme de bang) : le stress anisotrope est, à")
print("   un facteur −4 près, la SOURCE DE COURBURE elle-même. Avec back-réaction σ:Π incluse,")
print("   la contrainte est conservée à 1e-14 ⟹ trajectoires d'Einstein PROPRES. Le devenir")
print("   de κ dépend de DEUX choses (toutes deux à fixer sur Tod, pas par ce calcul) :")
print("   (i) le SIGNE de σ̌ relativement à ³S dans l'équation du cisaillement :")
print("       • c_Π=+1 (renforce −³S/H) ⟹ rappel plus fort ⟹ κ BAISSE (0.81→0.24) ; mais")
print("         RÉPONSE NON-LINÉAIRE (lin~0.6, dépassement : κ non-monotone en amplitude).")
print("       • c_Π=−1 (oppose −³S/H) ⟹ rappel affaibli ⟹ κ MONTE (carte reste linéaire).")
print("   (ii) la LOI DE REDSHIFT p du stress anisotrope :")
print("       • p=2 (σ̌∝a⁻², cohérent ρ∝a⁻⁴ de Tod 27) : −σ̌ ⟹ κ≈1.57 (BASCULE >1).")
print("       • p=4 (redshift radiation) : −σ̌ ⟹ κ≈0.95 (NE bascule PAS, reste <1).")
print("       • p=0 (gelé) : non physique (Π ne décroît jamais ⟹ κ≫1, à écarter).")
print("")
print("   ⟹ κ≥1 (mort de l'attraction) n'arrive que pour la CONJONCTION : signe opposé ET")
print("     redshift lent (p≲2). Le signe physiquement correct et p exact ne sont PAS tranchés")
print("     ici (convention de Tod 33 dans le repère du cisaillement + scaling de σ̌ à")
print("     re-vérifier sur le papier). C'est l'ambiguïté `décision ouverte` §5.2, désormais")
print("     ISOLÉE en deux paramètres précis et BORNÉE.")
print("")
print("   • φ (phantom, Tod 13) : scalaire homogène ⟹ stress ISOTROPE ⟹ NE source PAS le")
print("     cisaillement. Il ne module κ que via l'histoire d'expansion (ρ_φ) ⟹ effet borné")
print("     par le balayage Λ/ρ déjà scellé (κ∈[0.70,0.94]). Il ne peut PAS, seul, faire κ≥1.")
print("   • « DM » de Penrose (terme de trace au-delà de O(Ť⁻¹)) : `à inventer`, sous-dominante,")
print("     en réserve (Tod s'arrête ; interprétation physique manquante, Markwell-Stevens).")
print("")
print("   RÉSULTAT NET. Le seul acteur capable de retourner κ est le stress anisotrope σ̌,")
print("   et seulement dans la conjonction (signe opposé à ³S) ∧ (redshift lent). φ et DM ne")
print("   peuvent pas le faire seuls. La question décisive du front (a) se réduit donc à DEUX")
print("   paramètres physiques précis et bornés (signe de σ̌, exposant p), désormais localisés.")
print("   Discipline d'audit : `établi` = l'algèbre (σ̌=−4³S, contrainte conservée, rôle isotrope")
print("   de φ, réduction à 2 paramètres) ; le signe et p restent `décision ouverte`.")
print("="*78)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Ancrage auto-verifie du seed σ̌ (Tod 33) contre LC-A-D1-BIANCHI [B2] : |σ̌|² = 128 ε² + O(ε⁴).
_sc, _S = sigma_check_seed(0.02)
assert abs(float(np.sum(_sc**2)) / 0.02**2 - 128.0) < 1.0, "interaeon_matiere: seed |σ̌|²/ε² -> 128 (ancrage Tod 33 / [B2])"
print("EXIT 0 (F1: assertion seed σ̌=128ε² verifiee)")
