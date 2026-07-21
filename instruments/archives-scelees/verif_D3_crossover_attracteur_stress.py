#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_crossover_attracteur_stress.py — STRESS-TEST (RoB 2) du verdict de la porte (ii).

Teste la ROBUSTESSE du verdict 'jamais attracteur' contre :
  (S1) l'invariant structurel det J*=1 sur une grille (c0, λ*, k) et toutes closures ;
  (S2) le balayage (c0, λ*, k) des trois closures (douce/dure/balance) ;
  (S3) ~7 FORMES différentes de closure 'balance' (zéro en λ*) ;
  (S4) le théorème : det=1 ⟹ |μ₁||μ₂|=1 ⟹ attracteur impossible (le numérique confirme l'algèbre).

Map (établi a3 + canal a2) :  m'=P*/λ , λ'=mλ²/P*+δλ(λ) , P*=9k²/4.
"""
import numpy as np

def Pstar(k): return 9*k**2/4

def jacobian(m, lam, k, dlam, h=1e-6):
    Ps = Pstar(k)
    dprime = (dlam(lam+h) - dlam(lam-h))/(2*h)        # δλ'(λ), diff. centrée (scalaire lisse)
    return np.array([[0.0,           -Ps/lam**2],
                     [lam**2/Ps,      2*m*lam/Ps + dprime]])

def eig(J):
    tr, dt = np.trace(J), np.linalg.det(J)
    disc = tr*tr - 4*dt
    if abs(disc) < 1e-9: disc = 0.0
    if disc >= 0:
        s = np.sqrt(disc); return np.array([(tr+s)/2,(tr-s)/2]), dt, tr
    s = np.sqrt(-disc);    return np.array([(tr+1j*s)/2,(tr-1j*s)/2]), dt, tr

def verdict(m, lam, k, dlam):
    # P* est-il un point fixe ? (exige δλ(λ*)=0)
    if abs(dlam(lam)) > 1e-12:
        return "RÉPULSEUR (P* non fixe)", None, None, None
    mu, dt, tr = eig(jacobian(m, lam, k, dlam))
    a = np.max(np.abs(mu))
    lab = "ATTRACTEUR" if a < 1-1e-6 else ("RÉPULSEUR" if a > 1+1e-6 else "NEUTRE")
    return lab, a, dt, tr

def banner(t): print("\n"+"="*86+"\n "+t+"\n"+"="*86)

# =====================================================================================
banner("[S1] INVARIANT STRUCTUREL det J*=1 — grille (c0, λ*, k) × {douce, dure, balance}")
print("    Si det J*=1 PARTOUT, alors |μ₁||μ₂|=1 partout ⟹ attracteur (|μ|<1 pour les deux) IMPOSSIBLE.")
dets = []
for k in [0.5, 1.0, 2.0, 3.0]:
    for lam_s in [0.4, 1.0, 1.5, 4.0]:
        for c0 in [0.001, 0.05, 0.5, 2.0]:
            m_s = Pstar(k)/lam_s
            for dl in [lambda l,c=c0: c*l**2,
                       lambda l,c=c0,L=lam_s: c*(l/L)*l**2,
                       lambda l,c=c0,L=lam_s: c*(1-l/L)*l**2]:
                dets.append(np.linalg.det(jacobian(m_s, lam_s, k, dl)))
dets = np.array(dets)
print(f"    {len(dets)} configurations testées.  det J* : min={dets.min():.6f}, max={dets.max():.6f}, "
      f"écart-max-à-1 = {np.max(np.abs(dets-1)):.2e}")
print("    ⟹ det J* ≡ 1 (à la précision machine) INDÉPENDAMMENT de (c0,λ*,k) et de la closure. CONFIRMÉ.")

# =====================================================================================
banner("[S2] BALAYAGE (c0, λ*, k) — verdict des trois closures")
print(f"    {'k':>4} {'λ*':>5} {'c0':>6} | {'douce':>22} | {'dure':>22} | {'balance (|μ|, det, tr)':>30}")
print("    " + "-"*94)
any_attr = False
for k in [0.5, 1.0, 2.0]:
    for lam_s in [0.4, 1.0, 1.5, 4.0]:
        for c0 in [0.01, 0.05, 0.5, 2.0, 10.0]:
            m_s = Pstar(k)/lam_s
            dl_douce   = lambda l,c=c0: c*l**2
            dl_dure    = lambda l,c=c0,L=lam_s: c*(l/L)*l**2
            dl_balance = lambda l,c=c0,L=lam_s: c*(1-l/L)*l**2
            vd,_,_,_       = verdict(m_s, lam_s, k, dl_douce)
            vu,_,_,_       = verdict(m_s, lam_s, k, dl_dure)
            vb,ab,db,tb    = verdict(m_s, lam_s, k, dl_balance)
            if "ATTRACTEUR" in (vd,vu,vb): any_attr = True
            # n'imprime qu'un échantillon lisible
            if c0 in (0.05, 2.0, 10.0) and lam_s in (0.4, 1.5, 4.0):
                bstr = f"{vb} (|μ|={ab:.3f}, det={db:.2f}, tr={tb:.2f})" if ab else vb
                print(f"    {k:>4} {lam_s:>5} {c0:>6} | {vd.split('(')[0]:>22} | {vu.split('(')[0]:>22} | {bstr:>30}")
print(f"\n    AUCUN attracteur rencontré sur tout le balayage ? {'OUI ✓' if not any_attr else 'NON ✗'}")
print("    (balance bascule NEUTRE→RÉPULSEUR quand c0·λ* franchit ~4 ; jamais ATTRACTEUR.)")

# =====================================================================================
banner("[S3] FORMES de closure 'balance' (toutes s'annulent en λ*) — verdict + s=δλ'(λ*)")
k, lam_s, c0 = 1.0, 1.5, 0.05
m_s = Pstar(k)/lam_s
formes = [
    ("(1−λ/λ*)·λ²        [zéro simple, réf]", lambda l: c0*(1-l/lam_s)*l**2),
    ("(1−λ/λ*)·λ³        [puissance +1]",     lambda l: c0*(1-l/lam_s)*l**3),
    ("(1−λ/λ*)·λ         [puissance −1]",     lambda l: c0*(1-l/lam_s)*l),
    ("(1−λ/λ*)²·λ²       [zéro DOUBLE]",      lambda l: c0*(1-l/lam_s)**2*l**2),
    ("sin(π(λ*−λ)/λ*)·λ² [zéro oscillant]",   lambda l: c0*np.sin(np.pi*(lam_s-l)/lam_s)*l**2),
    ("tanh((λ*−λ)/λ*)·λ² [saturant]",          lambda l: c0*np.tanh((lam_s-l)/lam_s)*l**2),
    ("(λ/λ*−1)·λ²        [balance INVERSÉE]", lambda l: c0*(l/lam_s-1)*l**2),
    ("c0·(λ*−λ)·(λ−2λ*)/λ* [zéro + courbure]", lambda l: c0*(lam_s-l)*(l-2*lam_s)/lam_s),
]
print(f"    {'forme':<42} {'s=δλ′(λ*)':>11}  {'det':>5}  {'tr':>7}  {'|μ|max':>7}  verdict")
print("    " + "-"*96)
attr_S3 = False
for name, dl in formes:
    h=1e-6; s = (dl(lam_s+h)-dl(lam_s-h))/(2*h)
    lab, a, dt, tr = verdict(m_s, lam_s, k, dl)
    if "ATTRACTEUR" in lab: attr_S3 = True
    astr = f"{a:.4f}" if a is not None else "  —  "
    dstr = f"{dt:.3f}" if dt is not None else "  —"
    tstr = f"{tr:.3f}" if tr is not None else "   —"
    print(f"    {name:<42} {s:>+11.4f}  {dstr:>5}  {tstr:>7}  {astr:>7}  {lab}")
print(f"\n    AUCUN attracteur parmi les formes balance ? {'OUI ✓' if not attr_S3 else 'NON ✗'}")

# =====================================================================================
banner("[S4] THÉORÈME (le numérique ne fait que confirmer l'algèbre)")
print("""    m' = P*/λ ne dépend PAS de m  ⟹  ∂m'/∂m = 0.
       det J* = (∂m'/∂m)(∂λ'/∂λ) − (∂m'/∂λ)(∂λ'/∂m)
              = 0 − (−P*/λ²)(λ²/P*) = 1,   POUR TOUTE back-réaction δλ(λ) sur λ seul.
       μ₁μ₂ = det = 1  ⟹  |μ₁||μ₂| = 1  ⟹  on NE PEUT PAS avoir |μ₁|<1 ET |μ₂|<1.
       ⟹  ATTRACTEUR (linéaire) IMPOSSIBLE.  Le verdict ne dépend que de s = δλ′(λ*) :
            s = 0        → μ=1 double défective         → NEUTRE (drift séculaire)
            −4 < s < 0   → μ complexes, |μ|=1 (centre)  → NEUTRE
            s > 0  ou  s ≤ −4 → μ réels, un |μ|>1       → RÉPULSEUR
       JAMAIS attracteur. CQFD.""")

banner("VERDICT DU STRESS-TEST")
robuste = (not any_attr) and (not attr_S3) and (np.max(np.abs(dets-1)) < 1e-6)
print(f"    det J*≡1 sur grille : {'✓' if np.max(np.abs(dets-1))<1e-6 else '✗'}")
print(f"    aucun attracteur (S2 balayage) : {'✓' if not any_attr else '✗'}")
print(f"    aucun attracteur (S3 formes)   : {'✓' if not attr_S3 else '✗'}")
print(f"\n    ⟹ VERDICT 'jamais attracteur' ROBUSTE : {'CONFIRMÉ ✓' if robuste else 'NON CONFIRMÉ ✗'}")
print("    Le verdict neutre/répulseur de la porte (ii) minimale tient sur tout l'espace des")
print("    paramètres ET des formes de closure : c'est une obstruction STRUCTURELLE (det=1),")
print("    pas un accident de paramétrage. (Discipline §6.4 : signature numérique, pas preuve.)")
print("="*86)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
assert robuste, "crossover_attracteur_stress: verdict calcule (robuste) doit etre vrai"
print("EXIT 0 (F1: assertion robuste verifiee)")
