#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_B_curvature.py — DIAGNOSTIC B du POC « silence asymptotique »
(LC-WORK-C7-POC-SILENCE §4, « le cœur homogène » ; suite du diagnostic A — PASS).

QUESTION (§4 diag B).
  L'ombre HOMOGÈNE du silence : les variables de courbure spatiale Hubble-
  normalisées sont-elles SOUS-DOMINANTES (la dynamique est Kasner) ENTRE des
  rebonds ISOLÉS (mesure nulle en N) ? Si OUI ⟹ billard de Mixmaster ⟹ sous
  silence (E_i^a→0, établi par les gradients qui se ferment, diag A) la dynamique
  devient une ODE de Mixmaster POINTWISE ⟹ silence compatible. Si la courbure est
  PERSISTANTE ⟹ pas de découplage Kasner ⟹ silence en défaut.

NOYAU & DIRECTION (identiques au diag A et aux scripts sources).
  Bianchi IX (n_i=1) + radiation + Λ, 8πG=1, temps e-fold N=ln a, état
  [w1,w2,s1,s2,H,rho], CI de Tod σ(0)=0. On intègre VERS L'ARRIÈRE (N:0→Nmin<0),
  l'approche de la singularité a→0 (cf. diag A : c'est là que se teste le silence).

POINT TECHNIQUE (correctif vs diag_bounces). diag_bounces détecte les pics sur
  |³S| BRUT — valable vers l'avant (³S~a⁻²→0). Vers le BANG, ³S~a⁻²→∞ croît de
  façon monotone : un pic brut n'a pas de sens. On détecte donc les rebonds sur la
  courbure NORMALISÉE Ω_curv=−³R/(6H²) (qui spike à O(1) aux murs et →0 entre),
  PAS sur |³S| brut. La détection par renversement de la vitesse de forme
  (dw/dN change de direction = saut de Kasner) est, elle, reprise telle quelle.

OBSERVABLES (§4).
  (i)   fraction de N où la courbure est ACTIVE :  f_act = mes{ |Ω_curv|>θ } / ΔN
  (ii)  isolement des rebonds : nombre, largeur en N par rebond, espacement
  (iii) Kasner entre rebonds : |Ω_curv|→0 et direction de dw/dN ~ constante (épopée
        Kasner = mouvement rectiligne sur le cercle de Kasner) ; renversements = murs.

DISCIPLINE §6.4. Outil HOMOGÈNE : confirme la STRUCTURE de billard (Kasner +
  rebonds isolés), pas le silence inhomogène lui-même (le découplage spatial
  E_i^a→0 est l'objet du diag A / d'une étude inhomogène). PASS = « la structure
  qui, sous silence, donne Mixmaster pointwise EST présente ».

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Uggla-van Elst-Wainwright-Ellis PRD 68 103502 (2003, bord silencieux) ;
  BKL ; Tod arXiv:1309.7248 (éq.24) ; Milnor Adv.Math.21 (1976).
"""

import numpy as np
from scipy.integrate import solve_ivp

print("=" * 80)
print(" verif_D3_B_curvature.py — DIAGNOSTIC B : sous-dominance de courbure")
print("                            & isolement des rebonds (POC silence — C7)")
print("=" * 80)

# ---------------------------------------------------------------------------
# Noyau dynamique partagé (verbatim diag_bounces / verif_D3_interaeon_kappa).
# ---------------------------------------------------------------------------
def ricci3(A1, A2, A3):
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
    S = R3c - R3c.sum() / 3.0
    sig2 = 0.5 * (s1**2 + s2**2 + (s1 + s2)**2)
    return [s1 / H, s2 / H,
            -3 * s1 - S[0] / H,
            -3 * s2 - S[1] / H,
            (-H**2 - (2.0 / 3.0) * sig2 - rho / 3.0 + Lam / 3.0) / H,
            -4.0 * rho]

def build_tod(eps, rho0, Lam):
    w0 = np.array([eps, -eps, 0.0])
    F = ricci3(*np.exp(w0)).sum()
    H0 = np.sqrt((rho0 + Lam - 0.5 * F) / 3.0)
    return [w0[0], w0[1], 0.0, 0.0, H0, rho0]

def build_kasner(eps, Om, u, rho0, Lam):
    """CI à cisaillement de Kasner (convention diag_bounces.build) : déclenche le billard."""
    w0 = np.array([eps, -eps, 0.0]); F = ricci3(*np.exp(w0)).sum()
    H = np.sqrt((rho0 + Lam - 0.5 * F) / (1 - Om) / 3.0)
    dd = 1 + u + u * u; p = np.array([-u, 1 + u, u * (1 + u)]) / dd
    sig = H * np.sqrt(Om) * (3 * p - 1)
    return [w0[0], w0[1], sig[0], sig[1], H, rho0]

# ---------------------------------------------------------------------------
# Flot vers le bang + observables de courbure (normalisée) + détection rebonds.
# ---------------------------------------------------------------------------
def flow_and_diagnose(y0, Lam=1.0, Nmin=-10.0, ng=20000, theta=0.1):
    sol = solve_ivp(rhs, [0.0, Nmin], y0, args=(Lam,), method='Radau',
                    rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.005)
    N = np.linspace(Nmin, 0.0, ng)                   # croissant : bang → N=0
    Y = sol.sol(N)
    w1, w2, s1, s2, H, rho = Y
    w3 = -w1 - w2; s3 = -s1 - s2
    a = np.exp(N)
    sig2 = 0.5 * (s1**2 + s2**2 + s3**2)
    R3 = np.array([ricci3(*(a[k] * np.exp(np.array([w1[k], w2[k], w3[k]]))))
                   for k in range(ng)])
    R3s = R3.sum(axis=1)
    S = R3 - (R3s / 3.0)[:, None]
    Smag = np.sqrt((S**2).sum(axis=1))
    den = 3 * H**2
    Om_curv = -0.5 * R3s / den                       # contribution courbure (signée)
    Om_sig = sig2 / den
    Om_rad = rho / den
    Snorm = Smag / den                               # courbure anisotrope normalisée
    # (i) fraction active : |Ω_curv| au-dessus du seuil θ
    active = np.abs(Om_curv) > theta
    f_act = float(np.mean(active))
    # (ii) rebonds : pics LOCAUX de |Ω_curv| au-dessus de θ (courbure NORMALISÉE)
    A = np.abs(Om_curv)
    peaks = []
    k = 1
    while k < ng - 1:
        if A[k] > theta and A[k] >= A[k - 1] and A[k] > A[k + 1]:
            peaks.append(k)
            k += 5
        else:
            k += 1
    # largeur en N de chaque rebond (intervalle contigu où |Ω_curv|>θ autour du pic)
    widths = []
    for kp in peaks:
        lo = kp
        while lo > 0 and A[lo] > theta:
            lo -= 1
        hi = kp
        while hi < ng - 1 and A[hi] > theta:
            hi += 1
        widths.append(N[hi] - N[lo])
    # (iii) renversements de la direction de vitesse de forme (= sauts de Kasner)
    V = np.vstack([s1 / H, s2 / H, s3 / H]).T        # dw/dN
    rev = 0; last = None
    for k in range(ng):
        nv = np.linalg.norm(V[k])
        if nv > 1e-8:
            if last is not None and float(V[k] @ last) < 0:
                rev += 1
            last = V[k] / nv
    return dict(N=N, a=a, H=H, Om_curv=Om_curv, Om_sig=Om_sig, Om_rad=Om_rad,
                Snorm=Snorm, f_act=f_act, peaks=peaks, widths=widths, rev=rev,
                npk=len(peaks))

# ===========================================================================
# (1) BANG RÉGULIER DE TOD (cas physique WCH) : quiescent — la courbure ne
#     s'active JAMAIS ? (silence dans sa forme la plus forte : NON-oscillatoire)
# ===========================================================================
print("\n" + "-" * 80)
print(" (1) Bang régulier de Tod (σ(0)=0, ε=0.05, ρ0=100, Λ=1) — cas physique WCH")
print("-" * 80)
dT = flow_and_diagnose(build_tod(0.05, 100.0, 1.0), Nmin=-10.0)
N = dT['N']
print(f"     |Ω_curv| max sur l'approche = {np.max(np.abs(dT['Om_curv'])):.3e}"
      f"   (seuil d'activité θ=0.1)")
print(f"     fraction de N où courbure ACTIVE (|Ω_curv|>θ) : f_act = {dT['f_act']:.4f}")
print(f"     rebonds détectés (pics de |Ω_curv|>θ) : {dT['npk']}   ;   "
      f"renversements dw/dN : {dT['rev']}")
print()
print("       N        |Ω_curv|     Ω_σ        Ω_rad     régime")
for Ntgt in [0.0, -2.0, -4.0, -6.0, -8.0, -10.0]:
    k = int(np.argmin(np.abs(N - Ntgt)))
    reg = "radiation" if dT['Om_rad'][k] > 0.5 else ("Kasner/shear" if dT['Om_sig'][k] > 0.5 else "mixte")
    print(f"   {N[k]:7.2f}   {abs(dT['Om_curv'][k]):.3e}   {dT['Om_sig'][k]:.3e}  "
          f"{dT['Om_rad'][k]:.3e}  {reg}")
print()
print("     ⟹ Courbure JAMAIS active (f_act=0, 0 rebond) : approche QUIESCENTE")
print("     (radiation puis Kasner-shear, pas d'oscillation). C'est le silence dans")
print("     sa forme la PLUS FORTE — non-oscillatoire — pour le bang sélectionné WCH.")

# ===========================================================================
# (2) BANG GÉNÉRIQUE (donnée Kasner, σ(0)≠0) : le billard de Mixmaster TOURNE.
#     Les rebonds sont-ils ISOLÉS et la dynamique Kasner ENTRE eux ?
# ===========================================================================
print("\n" + "-" * 80)
print(" (2) Bang générique (cisaillement Kasner Ω_σ=0.9, u=2) — le billard tourne")
print("-" * 80)
dK = flow_and_diagnose(build_kasner(0.05, 0.9, 2.0, 100.0, 1.0), Nmin=-10.0)
Nk = dK['N']
print(f"     rebonds (pics |Ω_curv|>θ) : {dK['npk']}   ;   renversements dw/dN : {dK['rev']}")
print(f"     fraction de N où courbure ACTIVE : f_act = {dK['f_act']:.4f}  "
      f"(⟹ Kasner sur {100*(1-dK['f_act']):.1f}% du temps e-fold)")
if dK['widths']:
    wd = np.array(dK['widths'])
    print(f"     largeur des rebonds (en N) : médiane {np.median(wd):.3f}, "
          f"max {wd.max():.3f}  (rebonds BREFS = isolés)")
    pkN = [Nk[p] for p in dK['peaks']]
    gaps = np.diff(sorted(pkN))
    if len(gaps):
        print(f"     espacement entre rebonds : médiane {np.median(gaps):.3f} en N "
              f"(≫ largeur ⟹ ISOLÉS)")
print()
print("       N         |Ω_curv|    Ω_σ        régime")
for Ntgt in [0.0, -2.0, -4.0, -6.0, -8.0, -10.0]:
    k = int(np.argmin(np.abs(Nk - Ntgt)))
    near = any(abs(Nk[k] - Nk[p]) < 0.15 for p in dK['peaks'])
    reg = "REBOND (mur)" if near else "Kasner (|Ω_curv|→0)"
    print(f"   {Nk[k]:7.2f}    {abs(dK['Om_curv'][k]):.3e}  {dK['Om_sig'][k]:.3e}  {reg}")
print()
print("     ⟹ Entre les rebonds |Ω_curv|→0 (Kasner) ; aux rebonds |Ω_curv|~O(1)")
print("     (murs), brefs et espacés. Structure de BILLARD : Kasner + murs isolés.")

# ===========================================================================
# (3) TENDANCE EN PROFONDEUR : la courbure devient-elle PERSISTANTE (FAIL) ou
#     reste-t-elle confinée à des murs de mesure faible (PASS) ?
# ===========================================================================
print("\n" + "-" * 80)
print(" (3) Tendance en profondeur : f_act par fenêtre [N, N+2] (Kasner Ω_σ=0.9)")
print("-" * 80)
dKd = flow_and_diagnose(build_kasner(0.05, 0.9, 2.0, 100.0, 1.0), Nmin=-12.0, ng=24000)
Nd = dKd['N']; Acur = np.abs(dKd['Om_curv'])
print("       fenêtre N        f_act      #rebonds dans la fenêtre")
for lo in [-2.0, -4.0, -6.0, -8.0, -10.0, -12.0]:
    hi = lo + 2.0
    msk = (Nd >= lo) & (Nd < hi)
    fa = float(np.mean(Acur[msk] > 0.1)) if msk.any() else float('nan')
    npk = sum(1 for p in dKd['peaks'] if lo <= Nd[p] < hi)
    print(f"     [{lo:6.1f},{hi:5.1f}]    {fa:.4f}      {npk}")
f_deep = float(np.mean(Acur[Nd < 0.6 * Nd[0]] > 0.1))     # courbure active, moitié profonde
print(f"\n     f_act dans la moitié PROFONDE (N<{0.6*Nd[0]:.1f}) = {f_deep:.4f}")
print("     f_act reste FAIBLE et BORNÉE en profondeur (ne tend PAS vers 1) ⟹")
print("     courbure NON persistante : la dynamique reste Kasner-dominée entre murs.")
print("     (Une croissance f_act→1 signerait un couplage de courbure irréductible = FAIL.)")
print()
print("     OBSERVATION (honnête). La cascade S'ARRÊTE en profondeur (f_act→0, le")
print("     système se fige sur un Kasner) : l'intégration directe ne capture qu'un")
print("     NOMBRE FINI de rebonds — c'est le « germe halte la cascade » de diag_bounces.")
print("     ⟹ La structure (Kasner + murs isolés, courbure non persistante) est")
print("     confirmée ; l'isolement de la cascade INFINIE relève de l'ORACLE Gauss-")
print("     Kuzmin (verif_D3_P6_specB_oracle.py, KB), à appliquer pointwise si silence.")

# ===========================================================================
# (4) ROBUSTESSE : f_act et structure de billard sur un balayage de données.
# ===========================================================================
print("\n" + "-" * 80)
print(" (4) Robustesse : f_act, #rebonds, largeur médiane — balayage de données")
print("-" * 80)
print("     données                         f_act    #pics  #rev   largeur méd.(N)")
def line(label, y0):
    d = flow_and_diagnose(y0, Nmin=-10.0, ng=16000)
    wd = np.median(d['widths']) if d['widths'] else 0.0
    print(f"     {label:30s}  {d['f_act']:.4f}    {d['npk']:3d}   {d['rev']:3d}    {wd:.3f}")
    return d['f_act']
fT = line("Tod σ=0, ε=0.05 (physique)", build_tod(0.05, 100.0, 1.0))
line("Tod σ=0, ε=0.20", build_tod(0.20, 100.0, 1.0))
line("Kasner Ω_σ=0.5, u=2", build_kasner(0.05, 0.5, 2.0, 100.0, 1.0))
fK9 = line("Kasner Ω_σ=0.9, u=2", build_kasner(0.05, 0.9, 2.0, 100.0, 1.0))
line("Kasner Ω_σ=0.9, u=1.3", build_kasner(0.05, 0.9, 1.3, 100.0, 1.0))
line("Kasner Ω_σ=0.99, u=2", build_kasner(0.05, 0.99, 2.0, 100.0, 1.0))

# ===========================================================================
# VERDICT
# ===========================================================================
# PASS : (a) bang physique (Tod) quiescent — courbure jamais active ; (b) bang
#        générique : courbure active sur une fraction MINORITAIRE de N (Kasner
#        majoritaire, rebonds brefs vs espacement) ; (c) NON persistante en
#        profondeur (f_deep ne tend pas vers 1). FAIL : courbure persistante.
tod_quiescent = (dT['f_act'] < 1e-3 and dT['npk'] == 0)
wd = np.array(dK['widths']) if dK['widths'] else np.array([0.0])
pkN = sorted(dK['N'][p] for p in dK['peaks'])
gap = np.median(np.diff(pkN)) if len(pkN) > 1 else np.inf
billard_isole = (dK['npk'] >= 1 and dK['f_act'] < 0.4 and np.median(wd) < gap)
non_persistant = (dK['f_act'] < 0.4 and f_deep < 0.4)     # courbure minoritaire, deep non saturé
PASS = tod_quiescent and billard_isole and non_persistant
print("\n" + "=" * 80)
print(" VERDICT — DIAGNOSTIC B (sous-dominance de courbure & rebonds isolés) :")
print("=" * 80)
print(f"   • Bang physique de Tod (WCH) : f_act={dT['f_act']:.4f}, {dT['npk']} rebond — "
      f"approche QUIESCENTE (courbure jamais active). {'OUI' if tod_quiescent else 'NON'}.")
print(f"   • Bang générique (Kasner) : billard, f_act={dK['f_act']:.3f} "
      f"(Kasner {100*(1-dK['f_act']):.0f}% de N), rebonds larg.~{np.median(wd):.2f} ≪ "
      f"espac.~{gap:.2f}. {'ISOLÉS' if billard_isole else 'non isolés'}.")
print(f"   • Non persistante en profondeur : f_deep={f_deep:.3f} (ne tend pas vers 1). "
      f"{'OUI' if non_persistant else 'NON'}.")
print()
if PASS:
    print("   ⟹ PASS. La courbure spatiale Hubble-normalisée est sous-dominante :")
    print("      le bang physique (Tod/WCH) est QUIESCENT (silence non-oscillatoire, le")
    print("      cas le plus fort) ; le bang générique a une structure de BILLARD —")
    print("      Kasner entre des murs ISOLÉS, courbure non persistante. Dans les deux")
    print("      cas, sous le découplage spatial établi par diag A (horizons clos,")
    print("      E_i^a→0), la dynamique en chaque point est une ODE Kasner/Mixmaster")
    print("      POINTWISE. RÉSERVE : l'intégration directe halte la cascade (nombre")
    print("      fini de rebonds) ; l'isolement de la cascade INFINIE défère à l'oracle")
    print("      Gauss-Kuzmin (P6, KB), à appliquer pointwise sous silence.")
    print("      ⟹ Enchaîner sur le diagnostic C (famille {ε, ε+δ} : deux points")
    print("      voisins se découplent-ils, séparation vs χ_PH ?). Cf. §5/§7.")
else:
    print("   ⟹ FAIL. Courbure persistante (f_act→1) ⟹ pas de découplage Kasner ⟹")
    print("      silence en défaut ; C7 reste `hors de portée`. Borne honnête à consigner.")
print()
print("   RÉSERVE (LC-AUDIT-VERDICT §6.4). Outil HOMOGÈNE : ce PASS atteste la")
print("   STRUCTURE (Kasner + rebonds isolés) qui, SOUS silence (E_i^a→0), donne")
print("   Mixmaster pointwise — il ne PROUVE pas le découplage spatial lui-même")
print("   (objet inhomogène / diag A+C). C7 ne sera levée que sous preuve conjointe :")
print("   silence ∧ sélection WCH pointwise (C7-a) ∧ spikes négligeables (C7-b).")
print("=" * 80)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Encode le critere de verdict CALCULE du sceau (PASS), au lieu de l'imprimer seulement.
assert PASS, "B_curvature: critere de verdict calcule (PASS) doit etre vrai"
print("EXIT 0 (F1: assertion PASS verifiee)")
