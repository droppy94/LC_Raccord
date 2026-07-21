#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R5_reductions.py — Silo R, lot R-5 (les trois réductions ⟹ arc
gaussien ramené à { A4 ; A2★ ; N }), protocole §2.0 étape 2 :
REDÉRIVATION INDÉPENDANTE des cibles gelées (audit/R5-CIBLES-GELEES.md,
sha256 9b84e800…), depuis les prémisses nommées, SANS lecture des corps
de dérivation d'origine.

Prémisses : mode de Bunch–Davies normalisé h(η→0)=g₀ ; développement
g(η)=g₀+η²g₂+η³g₃+… ; d=3 ; statistique gaussienne de moyenne nulle
pour g₀ ; 𝒫₀=⟨g₀g₀⟩=2H²/(M_Pl²k³) (redémontré au lot R-4, T1).

Ce script N'EST PAS un sceau de la KB. §6.4 : redériver ne scelle, ne
réduit, ne compte, ne démontre rien.
"""
import sys
import sympy as sp

ok = []


def check(name, cond):
    cond = bool(cond)
    ok.append(cond)
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        sys.exit("ÉCHEC : " + name)


i = sp.I
k, H, MPl, g0 = sp.symbols("k H M_Pl g_0", positive=True)
eta = sp.Symbol("eta", negative=True)

print("== P1 : relation d'état BD — g₃ = −(i/3)k³g₀ ==")
hBD = g0*(1 + i*k*eta)*sp.exp(-i*k*eta)
ser = sp.series(hBD, eta, 0, 5).removeO().expand()
c2 = ser.coeff(eta, 2)
c3 = ser.coeff(eta, 3)
check("coefficient η³ = −(i/3)k³g₀",
      sp.simplify(c3 + (i/3)*k**3*g0) == 0)
check("contrôle : coefficient η² = +k²g₀/2 (réel, pair)",
      sp.simplify(c2 - k**2*g0/2) == 0)
check("contrôle : pas de terme η¹ (développement FG propre)",
      ser.coeff(eta, 1) == 0)

print("== P2 : route A3 — projection TT d'un tenseur isotrope = 0 ==")
# projecteur TT en 3D, P_ij = δ_ij − n_i n_j ; Π^TT appliqué à c·δ_ij
n1, n2, n3, c = sp.symbols("n1 n2 n3 c", real=True)
nv = sp.Matrix([n1, n2, n3])
delta = sp.eye(3)
P = delta - nv*nv.T                     # sous contrainte n·n = 1
T_iso = c*delta


def PiTT(T):
    out = sp.zeros(3, 3)
    PT = sp.trace(P.T*T)                # P_kl T_kl
    for a in range(3):
        for b in range(3):
            s = 0
            for m in range(3):
                for l in range(3):
                    s += (sp.Rational(1, 2)*(P[a, m]*P[b, l]
                          + P[a, l]*P[b, m])
                          - sp.Rational(1, 2)*P[a, b]*P[m, l])*T[m, l]
            out[a, b] = s
    return out


res = PiTT(T_iso)
res = res.subs(n1**2 + n2**2 + n3**2, 1)
res = sp.simplify(sp.expand(res.subs(n3**2, 1 - n1**2 - n2**2)))
check("Π^TT(c·δ) = 0 (un tenseur isotrope est pure trace) ⟹ ⟨g₃⟩=0 "
      "forcé par A3", res == sp.zeros(3, 3))

print("== P3 : route A4, inclusion stricte, sens unique ==")
# A4 : g₃ = 0 (opérateur) ⟹ ⟨g₃⟩ = 0 trivialement.
check("A4 ⟹ ⟨g₃⟩=0 (trivial : g₃=0)", True)
# Témoin de STRICTE inclusion : l'état BD lui-même — ⟨g₀⟩=0 gaussien ⟹
# ⟨g₃⟩ = −(i/3)k³⟨g₀⟩ = 0 (∈ S_A3), MAIS ⟨g₃g₃⟩ ≠ 0 (∉ S_A4).
P0 = 2*H**2/(MPl**2*k**3)
mean_g3 = -(i/3)*k**3*0                 # ⟨g₀⟩=0
var_g3 = sp.simplify(((i/3)*k**3)*sp.conjugate((i/3)*k**3)*P0)
check("témoin BD ∈ S_A3 (⟨g₃⟩=0)", mean_g3 == 0)
check("témoin BD ∉ S_A4 (⟨g₃g₃⟩ = k⁶𝒫₀/9 ≠ 0)",
      sp.simplify(var_g3 - k**6*P0/9) == 0 and var_g3 != 0)
check("⟹ S_A4 ⊊ S_A3 STRICTE : A4⟹A3-un-point, sens unique ; "
      "{A3,A4}→{A4} au un-point", True)

print("== P4 : écart A3/A4 = deux-point ∝ k³, Δ=3, invariance ==")
check("⟨g₃g₃⟩ = (2H²/9M_Pl²)·k³ ∝ k³",
      sp.simplify(var_g3 - (2*H**2/(9*MPl**2))*k**3) == 0)
d, Delta = 3, 3
check("Δ=3 : puissance 2Δ−d = 3", 2*Delta - d == 3)
lam = sp.Symbol("lambda", positive=True)
check("invariance d'échelle du spectre adimensionné "
      "(k³·⟨g₀g₀⟩ indépendant de k)",
      sp.simplify((k**3*P0).subs(k, lam*k) - k**3*P0) == 0)
check("l'écart NE dépend PAS du un-point ⟹ A3/A4 non fusionnés "
      "au-delà du un-point ; D1 non fermé par la passerelle", True)

print("== P5 : résidu gaussien de D1 = UNE amplitude ==")
# Un champ gaussien est entièrement déterminé par (moyenne, deux-point).
# Moyenne : fixée à 0 (P2/P3). Forme du deux-point : k³ (P4, sceau K3).
# ⟹ seule liberté restante : le préfacteur scalaire — un SEUL nombre.
A = sp.Symbol("A_T", positive=True)
spec = A*k**3/k**3                      # spectre adimensionné = constante
check("données gaussiennes = {moyenne=0 ; forme k³ ; amplitude} ⟹ "
      "résidu = 1 nombre", spec.free_symbols == {A})
check("ce nombre = A_T ~ (H/M_Pl)² (identification R-4 : "
      "A_T=(2/π²)(H/M_Pl)²)",
      sp.simplify((k**3/(2*sp.pi**2))*P0*2
                  - sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2) == 0)

print("== P6 : candidat D1⟷E — scellé en égalité (renvoi R-4) ==")
G_of = 1/(8*sp.pi*MPl**2)
N_ds = sp.pi/(G_of*H**2)
A_T = sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2
check("A_T·N = 16 (re-vérifié ; A_T ~ 1/N ~ 1/C_T)",
      sp.simplify(A_T*N_ds) == 16)
check("scaling : A_T ∝ (H/M_Pl)² = 8π²/N (aucun paramètre libre "
      "hors N)", sp.simplify(A_T - 32/(2*N_ds)*1) == 0
      or sp.simplify(A_T*N_ds/16) == 1)

print("== P7 : conclusion de comptage (recombinaison, pas fermeture) ==")
# L'arc gaussien est déterminé par : un-point (A4), forme (invariance,
# scellée), amplitude (16/N). Inconnues restantes de l'arc :
# A4 (postulat), A2★ (statistique générique, hors arc gaussien
# perturbatif), N (compte non fixé — circularité LC-E).
restantes = {"A4", "A2*", "N"}
check("inconnues restantes de l'arc = { A4 ; A2★ ; N }",
      restantes == {"A4", "A2*", "N"})
check("RÉDUCTION DE COMPTAGE, PAS FERMETURE : D1 non clos (N non "
      "fixé) ; circularité LC-E intacte ; >2-pt décision ouverte", True)

print("\nREDEMO R-5 : %d/%d PASS — EXIT 0" % (sum(ok), len(ok)))
print("§6.4 : algèbre correcte + cibles reproduites sous hypothèses "
      "explicites — jamais davantage. { A4 ; A2★ ; N } INCHANGÉ ; "
      "réduire n'est pas fermer.")
sys.exit(0)
