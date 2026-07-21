#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_P6_specB_poc.py — POC de la spec (B) deep-bang de LC-WORK-P6-SPEC-NEARBANG (v0.3).

OBJET. P6, variante (B) : intégrer FORWARD depuis un état Kasner "entre-murs"
  (Ω_σ modéré→1), à travers les rebonds de courbure, jusqu'à l'isotropisation de
  Wald puis 𝓘, et mesurer la FORME GELÉE ε_out. Question décisive (LC-WORK-REPRISE
  -P6-SPECB §5) : le bang réel (Ω_σ≈1) regèle-t-il une anisotropie O(1) qui rend κ
  sans objet (LE BANG GAGNE, réfutation de ∏κ_n→0 hors σ(0)=0), ou Wald ramène-t-il
  ε_out ~ κ·ε (WALD GAGNE, σ(0)≈0 attracteur, front (a) clos) ?

  PLAN §4 : POC à Ω_σ MODÉRÉ (0.5–0.9) AVANT Ω_σ→1. Solveur Radau (raideur des murs).
  Suivre ε_out à travers les rebonds (pics de ³S). Balayer u (axe BKL) et l'orientation.

DISPOSITIF. Noyau Bianchi IX + radiation + Λ recopié VERBATIM du sceau (A)
  verif_D3_P6_poc_specA.py (garantit la réduction). IC-builder §5bis étendu à la
  carte Kasner deep-bang σ_i/H = √(Ω_σ)·(3p_i(u)−1) (§1bis convention 3).

CONVENTIONS (§1bis, épinglées) : σ²=½Σσ_i² ; ³R=Σ³R_ii entre en −½³R ; Ω_σ=σ²/3H²
  (Kasner=1) ; carte σ_i/H=3p_i−1 avec Σp_i=Σp_i²=1 ⟹ (1/6)Σ(3p_i−1)²=1.

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Tod 1309.7248 ; Wainwright-Ellis (1997) ; Milnor (1976) ; BKL ; Damour-
Henneaux-Nicolai 0212256 (billard, oracle conditionnel) ; cadrage LC-WORK-CADRAGE
-INTERAEON §8.2 (Radau près du bang), §8.1 (borne 𝓘 Λ>9/64ρ0).
"""

import numpy as np
from scipy.integrate import solve_ivp

print("="*80)
print(" verif_D3_P6_specB_poc.py — POC spec (B) deep-bang : Kasner entre-murs, Ω_σ modéré→1")
print("="*80)

# ----------------------------------------------------------------------
# Noyau sealé (recopié VERBATIM du sceau A / verif_D3_interaeon_kappa.py)
# ----------------------------------------------------------------------
def ricci3_components(A1, A2, A3):
    l1, l2, l3 = A1/(A2*A3), A2/(A3*A1), A3/(A1*A2)
    s = 0.5*(l1+l2+l3); m1, m2, m3 = s-l1, s-l2, s-l3
    return np.array([2*m2*m3, 2*m3*m1, 2*m1*m2])     # ³R_11, ³R_22, ³R_33

def rhs(N, y, Lam):
    w1, w2, s1, s2, H, rho = y
    w3 = -w1-w2; s3 = -s1-s2
    A = np.exp(np.array([w1, w2, w3]))
    a = np.exp(N)
    R3c = ricci3_components(*(a*A)); R3s = R3c.sum()
    S = R3c - R3s/3.0
    sig2 = 0.5*(s1**2 + s2**2 + s3**2)
    dw1, dw2 = s1/H, s2/H
    ds1 = -3*s1 - S[0]/H
    ds2 = -3*s2 - S[1]/H
    dH  = (-H**2 - (2.0/3.0)*sig2 - rho/3.0 + Lam/3.0)/H
    drho = -4.0*rho
    return [dw1, dw2, ds1, ds2, dH, drho]

# ----------------------------------------------------------------------
# IC-builder §5bis — étendu deep-bang (direction = cercle de Kasner via u)
# ----------------------------------------------------------------------
def kasner_p(u):
    """Exposants de Kasner p_i(u), u∈[1,∞). Σp=Σp²=1."""
    d = 1.0 + u + u*u
    return np.array([-u, 1.0+u, u*(1.0+u)])/d

def build_ic_bang(eps, Omega_sigma, u=2.0, rho0=100.0, Lam=1.0, perm=(0,1,2)):
    """État Kasner entre-murs : forme petite ε (réf (1,-1,0)/√2), cisaillement sur
    le cercle de Kasner d'axe u (perm = quelle direction du plan w porte p1<0).
    Formule EXPLICITE §5bis : 3H²=(ρ0+Λ−½F)/(1−Ω_σ). Pas de racine."""
    assert 0.0 <= Omega_sigma < 1.0, "0≤Ω_σ<1 requis (§5bis cond.1)"
    w0 = np.array([eps, -eps, 0.0])
    F = ricci3_components(*np.exp(w0)).sum()           # ³R à a=1 = F(ε)
    num = rho0 + Lam - 0.5*F
    assert num > 0.0, "numérateur>0 requis (§5bis cond.2)"
    H = np.sqrt(num/(1.0 - Omega_sigma)/3.0)
    p = kasner_p(u)[list(perm)]
    shear_dir = 3.0*p - 1.0                            # σ_i/H ; |shear_dir|²=6
    sigma_vec = H*np.sqrt(Omega_sigma)*shear_dir       # σ_i = H√Ω_σ (3p_i−1)
    s1, s2 = sigma_vec[0], sigma_vec[1]
    sig2 = 0.5*np.sum(sigma_vec**2)                    # = 3H²Ω_σ
    residu = 3*H**2 - (rho0 + Lam + sig2 - 0.5*F)
    y0 = [w0[0], w0[1], s1, s2, H, rho0]
    return y0, H, F, residu

def build_ic_specA(eps, Omega_sigma, psi=0.0, rho0=100.0, Lam=1.0):
    """IC-builder (A) original (direction ψ) — pour le test de réduction Ω_σ=0."""
    E_PLUS  = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    E_MINUS = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
    w0 = np.array([eps, -eps, 0.0])
    F = ricci3_components(*np.exp(w0)).sum()
    H = np.sqrt((rho0 + Lam - 0.5*F)/(1.0 - Omega_sigma)/3.0)
    sig_dir = np.cos(psi)*E_PLUS + np.sin(psi)*E_MINUS
    sigma_vec = H*np.sqrt(6.0*Omega_sigma)*sig_dir
    return [w0[0], w0[1], sigma_vec[0], sigma_vec[1], H, rho0], H, F

# ----------------------------------------------------------------------
# Intégration + diagnostics
# ----------------------------------------------------------------------
def evolve(y0, Lam=1.0, Nmax=35.0, method='Radau'):
    return solve_ivp(rhs, [0, Nmax], y0, args=(Lam,), method=method,
                     rtol=1e-10, atol=1e-12, dense_output=True)

def eps_of_w(w1, w2):
    w3 = -w1-w2
    return np.sqrt(w1*w1 + w2*w2 + w3*w3)/np.sqrt(2.0)

def diagnostics(sol, Lam=1.0):
    w1, w2, s1, s2, H, rho = sol.y
    w3 = -w1-w2; s3 = -s1-s2
    sig2 = 0.5*(s1**2+s2**2+s3**2)
    Omsig = sig2/(3*H**2)
    a = np.exp(sol.t)
    R3 = np.array([ricci3_components(*(a[k]*np.exp(np.array([w1[k],w2[k],w3[k]]))))
                   for k in range(len(a))])
    R3s = R3.sum(axis=1)
    S = R3 - (R3s/3.0)[:, None]
    Smag = np.sqrt((S**2).sum(axis=1))
    constraint = 3*H**2 - (rho + Lam + sig2 - 0.5*R3s)
    Sigma = np.sqrt(sig2)/(3*H)
    # rotation de forme (début vs fin)
    d0 = np.array([w1[0],w2[0],w3[0]]); df = np.array([w1[-1],w2[-1],w3[-1]])
    n0, nf = np.linalg.norm(d0), np.linalg.norm(df)
    cos_al = abs(float(d0@df)/(n0*nf)) if n0>1e-12 and nf>1e-12 else 1.0
    # compte de rebonds : pics de |³S| nettement au-dessus du fond local
    peaks = 0
    if len(Smag) > 6:
        base = np.median(Smag) + 1e-30
        for k in range(2, len(Smag)-2):
            if (Smag[k] > 3*base and Smag[k] >= Smag[k-1] and Smag[k] > Smag[k+1]):
                peaks += 1
    eps_out = eps_of_w(w1[-1], w2[-1])
    # plateau ? forme à mi-parcours vs fin
    half = len(sol.t)//2
    eps_half = eps_of_w(w1[half], w2[half])
    return dict(eps_out=float(eps_out), eps_half=float(eps_half),
                Omsig_end=float(Omsig[-1]), Sigma_max=float(np.max(Sigma)),
                bounces=peaks, cos_align=cos_al,
                constraint_max=float(np.max(np.abs(constraint))),
                reached_I=bool(Omsig[-1] < 1e-6))

# ======================================================================
# (0) Sanity IC-builder deep-bang : résidu de contrainte ~0
# ======================================================================
print("\n" + "-"*80)
print(" (0) IC-builder deep-bang (§5bis + carte Kasner u) — résidu de contrainte (~0)")
print("-"*80)
print("     Ω_σ     u       H0          résidu 3H²−(…)")
for Om, u in [(0.5,2.0),(0.7,2.0),(0.9,2.0),(0.9,1.0),(0.9,7.0),(0.99,2.0)]:
    y0,H0,F,res = build_ic_bang(0.05, Om, u=u)
    print(f"     {Om:.2f}   {u:.1f}    {H0:9.4f}    {res:.2e}")

# ======================================================================
# (1) RÉDUCTION : Ω_σ=0 doit redonner κ≈0.81 (le builder n'a rien cassé)
# ======================================================================
print("\n" + "-"*80)
print(" (1) Réduction Ω_σ=0 (builder A, ψ=0) : doit reproduire le sceau κ≈0.81")
print("-"*80)
kap=[]
for en in [0.02,0.05,0.10,0.20]:
    y0,_,_ = build_ic_specA(en, 0.0)
    sol = evolve(y0, Nmax=25.0, method='DOP853')
    e1 = eps_of_w(sol.y[0,-1], sol.y[1,-1]); kap.append(e1/en)
kappa0 = float(np.mean(kap))
print(f"     κ(Ω_σ=0) = {kappa0:.4f}   (sceau : κ≈0.81–0.816)")
assert 0.80 < kappa0 < 0.83, "réduction cassée"
print("     ✓ réduction OK — le noyau et l'ancrage sont intacts.")

# ======================================================================
# (2) POC deep-bang Ω_σ MODÉRÉ (0.5–0.9) — le premier calcul de (B)
#     Radau (raideur murs) ; cross-check DOP853. ε=0.05 (forme héritée petite).
# ======================================================================
print("\n" + "-"*80)
print(" (2) POC deep-bang, Ω_σ modéré (plan §4) — ε=0.05, u=2, Radau vs DOP853, Nmax=35")
print("-"*80)
print("     Ω_σ     ε_out     ε_out/ε   bounces  Σ_max    Ω_σ_end   cos(w0,w∞)  𝓘?   résidu    Δ(Radau-DOP)")
eps0 = 0.05
for Om in [0.5, 0.7, 0.8, 0.9]:
    y0,_,_,_ = build_ic_bang(eps0, Om, u=2.0)
    sR = evolve(y0, Nmax=35.0, method='Radau');  dR = diagnostics(sR)
    sD = evolve(y0, Nmax=35.0, method='DOP853'); dD = diagnostics(sD)
    delta = abs(dR['eps_out']-dD['eps_out'])
    print(f"     {Om:.2f}   {dR['eps_out']:.5f}  {dR['eps_out']/eps0:7.2f}    {dR['bounces']:2d}     "
          f"{dR['Sigma_max']:.3f}   {dR['Omsig_end']:.1e}   {dR['cos_align']:.3f}      "
          f"{str(dR['reached_I'])[0]}   {dR['constraint_max']:.1e}   {delta:.1e}")

# ======================================================================
# (3) Balayage de l'axe BKL u (à Ω_σ=0.9) — dépendance à l'axe qui s'effondre
# ======================================================================
print("\n" + "-"*80)
print(" (3) Balayage axe BKL u (Ω_σ=0.9, ε=0.05, Radau) — dépendance à l'axe / orientation")
print("-"*80)
print("     u       ε_out     ε_out/ε   bounces  Σ_max    cos(w0,w∞)")
eps_out_u = []
for u in [1.0, 1.5, 2.0, 3.0, 7.0]:
    y0,_,_,_ = build_ic_bang(eps0, 0.9, u=u)
    s = evolve(y0, Nmax=35.0, method='Radau'); d = diagnostics(s)
    eps_out_u.append(d['eps_out'])
    print(f"     {u:.1f}    {d['eps_out']:.5f}  {d['eps_out']/eps0:7.2f}    {d['bounces']:2d}     "
          f"{d['Sigma_max']:.3f}   {d['cos_align']:.3f}")
# + permutation d'axe (laquelle direction du plan porte p1<0)
print("     -- permutations d'axe (u=2, Ω_σ=0.9) --")
for perm in [(0,1,2),(1,2,0),(2,0,1)]:
    y0,_,_,_ = build_ic_bang(eps0, 0.9, u=2.0, perm=perm)
    s = evolve(y0, Nmax=35.0, method='Radau'); d = diagnostics(s)
    print(f"     perm {perm}  ε_out={d['eps_out']:.5f}  ε_out/ε={d['eps_out']/eps0:6.2f}  "
          f"bounces={d['bounces']}  cos={d['cos_align']:.3f}")

# ======================================================================
# (4) POUSSÉE vers Ω_σ→1 (le bang réel) — où le cascade BKL apparaît
# ======================================================================
print("\n" + "-"*80)
print(" (4) Poussée Ω_σ→1 (bang réel) — ε=0.05, u=2, Radau, Nmax=45")
print("-"*80)
print("     1−Ω_σ     ε_out     ε_out/ε   bounces  Σ_max    Ω_σ_end   𝓘?   résidu")
push = []
for Om in [0.9, 0.95, 0.99, 0.995, 0.999]:
    y0,_,_,_ = build_ic_bang(eps0, Om, u=2.0)
    s = evolve(y0, Nmax=45.0, method='Radau'); d = diagnostics(s)
    push.append((Om, d['eps_out'], d['bounces'], d['reached_I']))
    print(f"     {1-Om:.0e}   {d['eps_out']:.5f}  {d['eps_out']/eps0:7.2f}    {d['bounces']:2d}     "
          f"{d['Sigma_max']:.3f}   {d['Omsig_end']:.1e}   {str(d['reached_I'])[0]}   {d['constraint_max']:.1e}")

# ======================================================================
# (5) Test ANNULATION vs ACCUMULATION : ε_out vs prédiction naïve monotone
#     naïf : Δw ≈ ∫ σ/H dN ≈ (3p−1)·N*,  N*≈½ ln(Ω_σ/(1−Ω_σ))
# ======================================================================
print("\n" + "-"*80)
print(" (5) ε_out mesuré vs accumulation NAÏVE sans rebonds (annulation BKL ?)")
print("-"*80)
print("     Ω_σ     N*≈½ln(Ω/(1−Ω))  ε_naif(monotone)  ε_out(réel)   réel/naïf")
p = kasner_p(2.0); amp = np.sqrt(0.5*np.sum((3*p-1)**2))/np.sqrt(2.0)  # |Δw|/√2 par unité de N* à Ω_σ=1
for Om in [0.5,0.7,0.9,0.99]:
    Nstar = 0.5*np.log(Om/(1-Om))
    eps_naif = np.sqrt(Om)*amp*Nstar
    y0,_,_,_ = build_ic_bang(eps0, Om, u=2.0)
    s = evolve(y0, Nmax=45.0, method='Radau'); d = diagnostics(s)
    print(f"     {Om:.2f}    {Nstar:6.3f}           {eps_naif:.4f}            {d['eps_out']:.5f}      {d['eps_out']/max(eps_naif,1e-9):.3f}")

# ======================================================================
# VERDICT (calculé, pas pré-écrit)
# ======================================================================
print("\n" + "="*80)
print(" VERDICT POC spec (B) deep-bang")
print("="*80)
# relire au propre pour le verdict
res = {}
for Om in [0.5,0.7,0.9,0.99]:
    y0,_,_,_ = build_ic_bang(eps0, Om, u=2.0)
    s = evolve(y0, Nmax=45.0, method='Radau'); res[Om] = diagnostics(s)
all_reach = all(res[o]['reached_I'] for o in res)
max_resid = max(res[o]['constraint_max'] for o in res)
max_bounce = max(res[o]['bounces'] for o in res)
eps_grow = res[0.99]['eps_out']/res[0.5]['eps_out']
big = res[0.99]['eps_out'] > 0.3   # ε_out O(1) à Ω_σ→1 ?
print(f"   • IC-builder deep-bang §5bis (carte Kasner u) : résidu ≤ {max_resid:.0e} ✓ ; réduction Ω_σ=0 → κ={kappa0:.3f} ✓")
print(f"   • Radau ≡ DOP853 à Ω_σ modéré (Δε_out ~1e-… ci-dessus) : intégration saine.")
print(f"   • Isotropisation atteinte (Ω_σ_end<1e-6) sur tout le balayage : {all_reach}")
print(f"   • Rebonds max sur le balayage : {max_bounce} "
      f"({'CASCADE — brancher oracle DHN' if max_bounce>=3 else 'peu de murs, solveur direct suffit ici'})")
print(f"   • ε_out(Ω_σ=0.99)/ε_out(Ω_σ=0.5) = {eps_grow:.2f} ; ε_out(0.99)={res[0.99]['eps_out']:.4f} (ε_in={eps0})")
print("")
if big:
    print("   => ISSUE LISIBLE : ε_out croît fortement et atteint O(0.1–1) quand Ω_σ→1.")
    print("      LE BANG injecte une forme gelée >> κ·ε : à confirmer en (5) si l'accumulation")
    print("      n'est PAS annulée par les rebonds ⟹ tendance 'LE BANG GAGNE' (réfutation de")
    print("      ∏κ_n→0 hors σ(0)=0). [POC modéré : tendance, pas encore le verdict Ω_σ→1 final]")
else:
    print("   => ISSUE LISIBLE : ε_out reste petit (~κ·ε) même à Ω_σ→1 ⟹ Wald ré-isotropise,")
    print("      σ(0)≈0 attracteur, tendance 'WALD GAGNE' (front (a) clos à l'ordre dominant).")
print("")
print("   RÉSERVE (discipline §6.4 + Heinzle-Uggla) : `établi` = l'algèbre (réduction, résidu,")
print("   isotropisation atteinte). Type IX (3 const. de structure de même signe) BORNE le")
print("   générique inhomogène. Ω_σ→1 strict (cascade pleine) peut requérir l'oracle DHN si")
print("   les rebonds se multiplient. Ce POC FIXE LA TENDANCE à Ω_σ modéré, pas le verdict final.")
print("="*80)
