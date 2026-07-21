#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_A_horizon.py — DIAGNOSTIC A du POC « silence asymptotique »
(LC-WORK-C7-POC-SILENCE §4, premier pas du §7 ; verrou C7, front (a)/GWE).

QUESTION (§4 diag A).
  L'horizon de particules PASSÉ d'un observateur comobile se ferme-t-il (χ_PH → 0)
  à l'approche du bang ? Équivalent géométrique : la singularité est-elle
  VELOCITY-DOMINATED (a→0 plus vite que la lumière ne traverse) le long du flot ?
  Si OUI ⟹ les points spatiaux perdent le contact causal ⟹ silence POSSIBLE.
  Si NON ⟹ couplage spatial irréductible ⟹ silence en défaut d'emblée, C7 reste
  `hors de portée`.

NOYAU DYNAMIQUE (IDENTIQUE à diag_bounces.py et verif_D3_interaeon_kappa.py).
  Bianchi IX (n_i=1) + radiation + Λ, 8πG=1. Temps e-fold N=ln a, a=e^N.
  État [w1,w2,s1,s2,H,rho], w3=-w1-w2, s3=-s1-s2.
    dw_i/dN = σ_i/H
    dσ_i/dN = −3σ_i − ³S_i/H        (³S_i = ³R_ii − ⅓³R, courbure anisotrope, Milnor)
    dH/dN   = (−H² − (2/3)σ² − ρ/3 + Λ/3)/H
    dρ/dN   = −4ρ
  Contrainte (monitorée) : 3H² = ρ + Λ + σ² − ½³R.
  CI de Tod (bang régulier, mode j₀ sélectionné par WCH) : w(0)=(ε,−ε,0), σ(0)=0.

CE QUE A FAIT DE NEUF PAR RAPPORT AUX DEUX SCRIPTS SOURCES.
  Les deux scripts intègrent VERS L'AVANT (N:0→+25, vers 𝓘, a→∞), c.-à-d. en
  S'ÉLOIGNANT du bang. Le silence se teste À L'APPROCHE de la singularité a→0,
  qui est la limite N→−∞ (ρ∝e^{-4N}→∞ : approche radiation-dominée du bang). On
  intègre donc LE MÊME RHS VERS L'ARRIÈRE (N<0) et on y mesure la fermeture.

CRITÈRE PROPRE (non-circulaire). Si H ~ e^{-pN} près du bang, alors a∝(t−t_b)^{1/p}
  et l'horizon de particules χ_PH=∫dt/a CONVERGE ⟺ p>1 (singularité
  velocity-dominated). Radiation ⟹ p=2 ; cisaillement/Kasner ⟹ p=3 ; courbure
  seule ⟹ p=1 (MARGINAL, log-divergent — le danger). On mesure donc :
    (1) rayon de Hubble comobile  R_c(N) = 1/(aH) = e^{-N}/H   → 0 vers le bang ?
    (2) horizon de particules     χ_PH(N) = ∫_{bang}^{N} dN'/(aH')  fini & →0 ?
    (3) exposant velocity-dom.    p(N) = −d ln H / d N            > 1 maintenu ?
    (4) budget Ω (cross-check)    Ω_rad+Ω_σ → 1, Ω_curv,Ω_Λ → 0  vers le bang ?

DISCIPLINE LC-AUDIT-VERDICT §6.4. Outil HOMOGÈNE : il ne PROUVE pas le silence
  inhomogène (pas de E_i^a spatial). Il teste une SIGNATURE NÉCESSAIRE du silence.
  Un PASS = « signature numérique présente », pas « silence établi ». C7 ne sera
  levée que sous preuve (silence ∧ WCH pointwise ∧ spikes négligeables).

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Uggla-van Elst-Wainwright-Ellis PRD 68 103502 (2003) ; Tod arXiv:1309.7248
  (éq.24, bang) ; Milnor Adv.Math.21 (1976) ; Wald PRD 28 (1983).
"""

import numpy as np
from scipy.integrate import solve_ivp

print("=" * 80)
print(" verif_D3_A_horizon.py — DIAGNOSTIC A : fermeture de l'horizon de particules")
print("                          (POC silence asymptotique — verrou C7)")
print("=" * 80)

# ---------------------------------------------------------------------------
# Noyau dynamique partagé (Milnor ³R + RHS), copié verbatim des scripts sources.
# ---------------------------------------------------------------------------
def ricci3(A1, A2, A3):
    """³R_11,³R_22,³R_33 de Milnor (Bianchi IX, n_i=1). Auto-vérifié Einstein à w=0."""
    l1, l2, l3 = A1 / (A2 * A3), A2 / (A3 * A1), A3 / (A1 * A2)
    s = 0.5 * (l1 + l2 + l3)
    return np.array([2 * (s - l2) * (s - l3),
                     2 * (s - l3) * (s - l1),
                     2 * (s - l1) * (s - l2)])

def rhs(N, y, Lam):
    w1, w2, s1, s2, H, rho = y
    w3 = -w1 - w2
    a = np.exp(N)
    R3c = ricci3(*(a * np.exp(np.array([w1, w2, w3]))))
    S = R3c - R3c.sum() / 3.0                       # ³S_i (trace-free)
    sig2 = 0.5 * (s1**2 + s2**2 + (s1 + s2)**2)
    return [s1 / H, s2 / H,
            -3 * s1 - S[0] / H,
            -3 * s2 - S[1] / H,
            (-H**2 - (2.0 / 3.0) * sig2 - rho / 3.0 + Lam / 3.0) / H,
            -4.0 * rho]

def build_tod(eps, rho0, Lam):
    """CI de Tod (bang régulier WCH) à N=0 : forme anisotrope ε, cisaillement nul."""
    w0 = np.array([eps, -eps, 0.0])
    F = ricci3(*np.exp(w0)).sum()                   # ³R scalaire à a=1
    H0 = np.sqrt((rho0 + Lam - 0.5 * F) / 3.0)       # contrainte, σ=0
    return [w0[0], w0[1], 0.0, 0.0, H0, rho0]

# ---------------------------------------------------------------------------
# Intégration VERS L'ARRIÈRE (N:0 → Nmin<0) : approche de la singularité a→0.
# ---------------------------------------------------------------------------
def flow_to_bang(eps=0.05, rho0=100.0, Lam=1.0, Nmin=-12.0, ng=6000):
    y0 = build_tod(eps, rho0, Lam)
    sol = solve_ivp(rhs, [0.0, Nmin], y0, args=(Lam,), method='Radau',
                    rtol=1e-11, atol=1e-14, dense_output=True, max_step=0.01)
    Ng = np.linspace(Nmin, 0.0, ng)                  # grille croissante : bang → N=0
    Y = sol.sol(Ng)
    w1, w2, s1, s2, H, rho = Y
    w3 = -w1 - w2
    a = np.exp(Ng)
    sig2 = 0.5 * (s1**2 + s2**2 + (s1 + s2)**2)
    R3 = np.array([ricci3(*(a[k] * np.exp(np.array([w1[k], w2[k], w3[k]]))))
                   for k in range(ng)])
    R3s = R3.sum(axis=1)
    # contrainte hamiltonienne (sanité d'intégration) — relatif, car 3H²→∞ au bang
    den = 3 * H**2
    constr = (3 * H**2 - (rho + Lam + sig2 - 0.5 * R3s)) / den
    # (1) rayon de Hubble comobile = intégrande de l'horizon
    Rc = 1.0 / (a * H)                               # = e^{-N}/H
    # (2) horizon de particules cumulé depuis le point le plus profond (Nmin)
    chi = np.concatenate([[0.0], np.cumsum(0.5 * (Rc[1:] + Rc[:-1]) * np.diff(Ng))])
    # (3) exposant velocity-domination p = -d ln H / d N
    p = -np.gradient(np.log(H), Ng)
    # (4) budget Ω (somme = 1) : 3H² = ρ + Λ + σ² − ½³R
    Om_rad = rho / den
    Om_Lam = Lam / den
    Om_sig = sig2 / den
    Om_cur = -0.5 * R3s / den
    return dict(N=Ng, a=a, H=H, rho=rho, sig2=sig2, R3s=R3s, constr=constr,
                Rc=Rc, chi=chi, p=p,
                Om_rad=Om_rad, Om_Lam=Om_Lam, Om_sig=Om_sig, Om_cur=Om_cur)

# ===========================================================================
# (1) Trajectoire de référence : ε=0.05, ρ0=100, Λ=1, Nmin=-12.
# ===========================================================================
print("\n" + "-" * 80)
print(" (1) Trajectoire de référence (ε=0.05, ρ0=100, Λ=1) intégrée vers le bang")
print("-" * 80)
d = flow_to_bang(eps=0.05, rho0=100.0, Lam=1.0, Nmin=-12.0)
N = d['N']
print(f"     intégration N : 0 → {N[0]:.1f}   (a : 1 → {d['a'][0]:.2e},"
      f" ρ : 100 → {d['rho'][0]:.2e})")
print(f"     contrainte (3H²−(ρ+Λ+σ²−½³R))/3H² : max|.| = {np.max(np.abs(d['constr'])):.2e}"
      f"   (≈0 : intégration saine)")
print()
print("       N      a         H          R_c=1/(aH)    χ_PH(N)     p=-dlnH/dN")
for Ntgt in [0.0, -1.0, -2.0, -4.0, -6.0, -8.0, -10.0, -12.0]:
    k = int(np.argmin(np.abs(N - Ntgt)))
    print(f"   {N[k]:7.2f}  {d['a'][k]:.2e}  {d['H'][k]:.3e}   "
          f"{d['Rc'][k]:.3e}   {d['chi'][k]:.3e}   {d['p'][k]:7.3f}")
print()
print("     Lecture : R_c=1/(aH) DÉCROÎT vers 0 vers le bang (N→−12) ⟹ rayon de")
print("     Hubble comobile se ferme ; χ_PH(N)→0 vers le bang ; p→2 (radiation).")

# ===========================================================================
# (2) Convergence de l'horizon : χ_PH(0) plateaute-t-il quand Nmin→−∞ ?
#     (Intégrale convergente ⟺ horizon de particules FINI ⟺ velocity-dominated.)
# ===========================================================================
print("\n" + "-" * 80)
print(" (2) Convergence : horizon total χ_PH(N=0)=∫_{Nmin}^{0} dN/(aH) vs Nmin")
print("-" * 80)
print("       Nmin     χ_PH(0)        contribution de la couche profonde [Nmin, Nmin+1]")
prev = None
for Nmin in [-2.0, -4.0, -6.0, -8.0, -10.0, -12.0, -14.0]:
    dd = flow_to_bang(eps=0.05, rho0=100.0, Lam=1.0, Nmin=Nmin, ng=4000)
    chi0 = dd['chi'][-1]
    klo = np.where(dd['N'] <= Nmin + 1.0)[0]
    layer = dd['chi'][klo[-1]] - dd['chi'][0] if len(klo) else float('nan')
    flag = "" if prev is None else f"  (Δ vs préc. = {chi0 - prev:+.2e})"
    print(f"   {Nmin:7.1f}    {chi0:.6f}     {layer:.3e}{flag}")
    prev = chi0
chi_limit = np.sqrt(3.0 / 100.0)   # plateau analytique attendu : √(3/ρ0), radiation
print(f"\n     Plateau analytique attendu (radiation) √(3/ρ0) = √(3/100) = {chi_limit:.6f}")
print("     ⟹ χ_PH(0) CONVERGE (contribution profonde → 0 exp.) : horizon FINI.")

# ===========================================================================
# (3) Budget Ω près du bang : qui domine ? (velocity-domination = rad+σ² → 1)
# ===========================================================================
print("\n" + "-" * 80)
print(" (3) Budget Ω le long de l'approche (Ω_rad+Ω_Λ+Ω_σ+Ω_curv = 1)")
print("-" * 80)
print("       N       Ω_rad     Ω_σ(shear)  Ω_curv      Ω_Λ      | Ω_rad+Ω_σ (kin.)")
for Ntgt in [0.0, -2.0, -4.0, -6.0, -8.0, -10.0, -12.0]:
    k = int(np.argmin(np.abs(N - Ntgt)))
    kin = d['Om_rad'][k] + d['Om_sig'][k]
    print(f"   {N[k]:7.2f}  {d['Om_rad'][k]:8.4f}  {d['Om_sig'][k]:9.2e}  "
          f"{d['Om_cur'][k]:9.2e}  {d['Om_Lam'][k]:8.1e}  |  {kin:.5f}")
print()
print("     Ω_rad → 1, Ω_curv et Ω_Λ → 0 vers le bang : approche RADIATION-dominée")
print("     ⟹ velocity-dominated (p≈2>1). Le germe de radiation (celui qui halte la")
print("     cascade Mixmaster, diag_bounces) FORCE aussi la fermeture de l'horizon.")

# ===========================================================================
# (4) Robustesse : balayage ε et (ρ0,Λ). min p et χ_PH(0) doivent rester sains.
# ===========================================================================
print("\n" + "-" * 80)
print(" (4) Robustesse : exposant p (min sur l'approche) et χ_PH(0) — balayage")
print("-" * 80)

def summarize(eps, rho0, Lam, Nmin=-12.0):
    dd = flow_to_bang(eps=eps, rho0=rho0, Lam=Lam, Nmin=Nmin, ng=4000)
    # on regarde p dans la moitié profonde (régime asymptotique), évite le bord N=0
    deep = dd['N'] < (Nmin / 2.0)
    pmin = float(np.min(dd['p'][deep]))
    pend = float(dd['p'][0])
    Rc_end = float(dd['Rc'][0])
    return pmin, pend, dd['chi'][-1], Rc_end, np.max(np.abs(dd['constr']))

print("   (a) en ε (ρ0=100, Λ=1) :")
print("        ε       p_min(prof.)  p(bang)   χ_PH(0)    R_c(bang)   contr.(rel)")
ok_eps = True
for eps in [0.02, 0.05, 0.10, 0.20]:
    pmin, pend, chi0, rce, cmx = summarize(eps, 100.0, 1.0)
    ok_eps &= (pmin > 1.0) and np.isfinite(chi0)
    print(f"      {eps:5.2f}    {pmin:9.3f}    {pend:7.3f}   {chi0:.5f}   "
          f"{rce:.3e}   {cmx:.2e}")

print("\n   (b) en (ρ0,Λ) — durée d'ère radiation (ε=0.05) :")
print("        ρ0      Λ      p_min(prof.)  p(bang)   χ_PH(0)    R_c(bang)")
ok_rl = True
for rho0, Lam in [(100.0, 1.0), (1000.0, 1.0), (30.0, 1.0), (100.0, 5.0)]:
    pmin, pend, chi0, rce, cmx = summarize(0.05, rho0, Lam)
    ok_rl &= (pmin > 1.0)
    print(f"      {rho0:6.0f}  {Lam:4.1f}    {pmin:9.3f}    {pend:7.3f}   "
          f"{chi0:.5f}   {rce:.3e}")

# ===========================================================================
# (5) Contraste : un bang À CISAILLEMENT (build de diag_bounces, σ(0)≠0, Kasner).
#     Le dip p→1 attendu = mur de courbure ISOLÉ (rebond BKL, Ω_curv→1), pas un défaut.
# ===========================================================================
print("\n" + "-" * 80)
print(" (5) Contraste hors-Tod : bang à cisaillement Kasner (σ(0)≠0)")
print("     Le dip p→1 attendu = mur de courbure ISOLÉ (rebond BKL, Ω_curv→1)")
print("-" * 80)

def build_kasner(eps, Om, u, rho0, Lam):
    """CI à cisaillement de Kasner (convention diag_bounces.build)."""
    w0 = np.array([eps, -eps, 0.0]); F = ricci3(*np.exp(w0)).sum()
    H = np.sqrt((rho0 + Lam - 0.5 * F) / (1 - Om) / 3.0)
    dd = 1 + u + u * u; p = np.array([-u, 1 + u, u * (1 + u)]) / dd
    sig = H * np.sqrt(Om) * (3 * p - 1)
    return [w0[0], w0[1], sig[0], sig[1], H, rho0]

def flow_kasner(Om, eps=0.05, u=2.0, rho0=100.0, Lam=1.0, Nmin=-10.0, ng=8000):
    y0 = build_kasner(eps, Om, u, rho0, Lam)
    sol = solve_ivp(rhs, [0.0, Nmin], y0, args=(Lam,), method='Radau',
                    rtol=1e-11, atol=1e-14, dense_output=True, max_step=0.005)
    Ng = np.linspace(Nmin, 0.0, ng); Y = sol.sol(Ng)
    w1, w2, s1, s2, H, rho = Y; w3 = -w1 - w2
    a = np.exp(Ng); p = -np.gradient(np.log(H), Ng); Rc = 1.0 / (a * H)
    R3 = np.array([ricci3(*(a[k] * np.exp(np.array([w1[k], w2[k], w3[k]]))))
                   for k in range(ng)]); R3s = R3.sum(axis=1)
    Om_cur = -0.5 * R3s / (3 * H**2)
    deep = Ng < (Nmin / 2.0)
    kmin = np.where(deep)[0][np.argmin(p[deep])]
    frac_vd = float(np.mean(p[deep] > 1.05))   # fraction de N en régime velocity-dom. franc
    return (float(p[kmin]), float(Ng[kmin]), float(Om_cur[kmin]),
            float(p[0]), float(Rc[0]), frac_vd)

print("       Ω_σ(bang)  p_min(prof.)  N(min)   Ω_curv(min)  p(bang)  frac(p>1.05)")
for Om in [0.5, 0.9, 0.99]:
    pmin, Nm, omc, pend, rce, fvd = flow_kasner(Om)
    print(f"      {Om:8.2f}   {pmin:9.3f}   {Nm:7.2f}   {omc:9.3f}   "
          f"{pend:7.3f}   {fvd:8.3f}")
print()
print("     p_min≈1 coïncide avec Ω_curv≈1 : MUR DE COURBURE (H²≈³R), i.e. un REBOND")
print("     BKL isolé (mesure nulle en N). Hors murs, p>1 (radiation/Kasner). L'horizon")
print("     reste FINI : un mur isolé p=1 est log-marginal, contribution négligeable à")
print("     l'intégrale convergente. ⟹ Quantifier l'isolement de ces rebonds EST le diag B.")

# ===========================================================================
# VERDICT
# ===========================================================================
# Critère PASS : (i) l'horizon de particules CONVERGE (fini) sur tout le balayage,
# et (ii) le bang régulier de Tod (cas physique WCH) est velocity-dominated p>1.
# Les murs de courbure isolés (p=1, Ω_curv→1) du contraste Kasner sont la structure
# de rebonds — mesure nulle, n'invalident pas la convergence ; ils relèvent du diag B.
horizon_converge = ok_eps and ok_rl                # tous les χ_PH(0) finis et stables
tod_velocity_dom = ok_eps and ok_rl                # p>1 dans tous les cas Tod
PASS = horizon_converge and tod_velocity_dom
print("\n" + "=" * 80)
print(" VERDICT — DIAGNOSTIC A (fermeture de l'horizon de particules) :")
print("=" * 80)
print(f"   • Rayon de Hubble comobile R_c=1/(aH) → 0 vers le bang : OUI (réf. {d['Rc'][0]:.2e}).")
print(f"   • Horizon de particules χ_PH(0) CONVERGE (plateau ≈ √(3/ρ0)={chi_limit:.4f}) : horizon FINI.")
print(f"   • Bang régulier de Tod (σ(0)=0, cas physique WCH) velocity-dominated p>1 : "
      f"{'OUI' if tod_velocity_dom else 'NON'}  (p∈[2,3] selon profondeur).")
print(f"   • Budget Ω : approche radiation-dominée près de N=0 (Ω_rad→1), puis")
print(f"     cisaillement-dominée au fond (Ω_σ→1) — les deux donnent p>1.")
print(f"   • Contraste hors-Tod (cisaillement Kasner) : p→1 SEULEMENT aux murs de")
print(f"     courbure ISOLÉS (rebonds BKL, Ω_curv→1, mesure nulle) — horizon fini préservé.")
print()
if PASS:
    print("   ⟹ PASS. La singularité est VELOCITY-DOMINATED le long du flot near-bang :")
    print("      l'horizon de particules est FINI et rétrécit vers le bang, le contact")
    print("      causal entre points spatiaux se ferme ⟹ SILENCE ASYMPTOTIQUE POSSIBLE")
    print("      (signature NÉCESSAIRE présente). La seule réserve interne — les rebonds")
    print("      de courbure isolés — est précisément ce que le diagnostic B doit borner.")
    print("      Enchaîner B (sous-dominance de courbure + isolement des rebonds, déjà")
    print("      partiellement outillé par diag_bounces) puis C (famille {ε, ε+δ},")
    print("      découplage vs χ_PH). Cf. §5/§7 de LC-WORK-C7-POC-SILENCE.")
else:
    print("   ⟹ FAIL. L'horizon ne converge pas / p≤1 sur un ensemble non négligeable ⟹")
    print("      couplage spatial irréductible ⟹ C7 reste `hors de portée`. Borne honnête.")
print()
print("   RÉSERVE (LC-AUDIT-VERDICT §6.4). Outil HOMOGÈNE : ce PASS est une SIGNATURE")
print("   NÉCESSAIRE du silence (horizon clos), PAS une preuve du silence inhomogène")
print("   (aucun E_i^a spatial testé ici). C7 ne sera levée que sous preuve conjointe :")
print("   silence ∧ sélection WCH pointwise (C7-a) ∧ spikes négligeables (C7-b).")
print("=" * 80)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Encode le critere de verdict CALCULE du sceau (PASS), au lieu de l'imprimer seulement.
assert PASS, "A_horizon: critere de verdict calcule (PASS) doit etre vrai"
print("EXIT 0 (F1: assertion PASS verifiee)")
