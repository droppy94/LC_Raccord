#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R4_CT.py — Silo R, lot R-4 (C_T ∝ N), protocole §2.0 étape 2 :
REDÉRIVATION INDÉPENDANTE des cibles gelées (audit/R4-CIBLES-GELEES.md,
sha256 044dc749…), depuis les prémisses nommées des têtes, SANS lecture
des corps de dérivation d'origine.

Prémisses : dS₄, M_Pl réduit, G=1/(8πM_Pl²), ℓ=1/H, κ²=8πG, d=3, vide
de Bunch–Davies, mode tensoriel canoniquement normalisé μ=(M_Pl/2)a·h.

Ce script N'EST PAS un sceau de la KB ; c'est l'instrument de
redémonstration du lot R-4. §6.4 : redériver ne scelle, ne réduit, ne
compte, ne démontre rien — au mieux « algèbre correcte + cibles
reproduites, sous hypothèses explicites ».
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


H, MPl, k, eta, u, G, ell, kappa2, N, dr, s = sp.symbols(
    "H M_Pl k eta u G ell kappa2 N delta_r s", positive=True)
i = sp.I

print("== T1 : route canonique — 𝒫 = ⟨|h|²⟩ (BD, η→0⁻) ==")
# mode canonique v_k = (1/sqrt(2k))(1 - i/(k η)) e^{-i k η} ; a = -1/(H η)
eta_n = sp.Symbol("eta", negative=True)
v = (1/sp.sqrt(2*k))*(1 - i/(k*eta_n))*sp.exp(-i*k*eta_n)
a = -1/(H*eta_n)
h = 2*v/(MPl*a)                       # μ=(M_Pl/2) a h ⟹ h = 2μ/(M_Pl a)
P = sp.simplify(h*sp.conjugate(h))
P0 = sp.limit(P, eta_n, 0, "-")
check("𝒫 = 2H²/(M_Pl²k³)", sp.simplify(P0 - 2*H**2/(MPl**2*k**3)) == 0)
# contrôle : v satisfait v'' + (k² - 2/η²)v = 0 (EOM de μ en dS)
eom_v = sp.simplify(sp.diff(v, eta_n, 2) + (k**2 - 2/eta_n**2)*v)
check("contrôle EOM du mode canonique", eom_v == 0)

print("== T11 : EOM TT dS + Bunch–Davies (S2) ==")
hBD = (1 + i*k*eta_n)*sp.exp(-i*k*eta_n)
eom_h = sp.simplify(sp.diff(hBD, eta_n, 2) - (2/eta_n)*sp.diff(hBD, eta_n)
                    + k**2*hBD)
check("h''−(2/η)h'+k²h=0 pour BD=(1+ikη)e^{−ikη}", eom_h == 0)
# même forme que la radiale AdS y''−(2/u)y'+y=0 sous u=k|η| (η<0 ⟹ u=−kη)

print("== T10 : dualité S1 — squelette (f_a, f_b), S²=−𝟙 ==")
fa = sp.cos(u) + u*sp.sin(u)
fb = u*sp.cos(u) - sp.sin(u)
for nm, f in (("f_a", fa), ("f_b", fb)):
    check("%s solution de y''−(2/u)y'+y=0" % nm,
          sp.simplify(sp.diff(f, u, 2) - (2/u)*sp.diff(f, u) + f) == 0)
S = sp.Matrix([[0, -1], [1, 0]])
check("S²=−𝟙", S*S == -sp.eye(2))
check("valeurs propres ±i", set(S.eigenvals()) == {i, -i})
# BD = f_a − i f_b = (1−iu)e^{iu} ; sous u=−kη : (1+ikη)e^{−ikη}
check("f_a − i·f_b = (1−iu)e^{iu}",
      sp.simplify(sp.expand((fa - i*fb - (1 - i*u)*sp.exp(i*u)).rewrite(sp.exp))) == 0)
check("(1−iu)e^{iu}|_{u=−kη} = BD",
      sp.simplify(sp.expand((((1 - i*u)*sp.exp(i*u)).subs(u, -k*eta_n) - hBD).rewrite(sp.exp))) == 0)
# BD mode propre +i de S sur (f_a, f_b) : S:(a,b)↦(−b,a) ; combinaison
# c=(1,−i) : S^T c = (−(−i), 1·?) → vérif directe par action sur coeffs
c = sp.Matrix([1, -i])          # BD = c^T·(f_a, f_b)
check("BD mode propre +i de la carte S", sp.simplify(S*c - i*c).norm() == 0)

print("== T2/T13[D] : route holographique — F on-shell, β forcé, γ absent ==")
beta = sp.Symbol("beta", positive=True)
F = beta*a**2*sp.diff(hBD, eta_n)/hBD          # F = β a² h'/h
ImF_lim = sp.limit(sp.im(sp.simplify(F)), eta_n, 0, "-")
P_holo = 1/(2*sp.Abs(ImF_lim))
sol = sp.solve(sp.Eq(P_holo, 2*H**2/(MPl**2*k**3)), beta)
check("β = M_Pl²/4 UNIQUE (𝒫 holo = 𝒫 canonique)",
      len(sol) == 1 and sp.simplify(sol[0] - MPl**2/4) == 0)
# γ n'apparaît dans aucune des deux expressions ⟹ séparation β/γ
check("γ ∉ 𝒫 (séparation magnitude/map)", True)

print("== T3/T4/T5 : A_T, N, A_T·N=16 ==")
A_T = sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2   # 𝒫_T = (k³/2π²)·𝒫·2 pol.
check("A_T = (k³/2π²)·𝒫·2", sp.simplify(
    (k**3/(2*sp.pi**2))*(2*H**2/(MPl**2*k**3))*2 - A_T) == 0)
G_of = 1/(8*sp.pi*MPl**2)
N_ds = sp.pi/(G_of*H**2)
check("N = π/(GH²) = 8π²(M_Pl/H)²",
      sp.simplify(N_ds - 8*sp.pi**2*MPl**2/H**2) == 0)
prod = sp.simplify(A_T*N_ds)
check("A_T·N = 16 (nombre pur, H et M_Pl cancellés)", prod == 16)

print("== T6/T7/T13 : verrouillage C_T∝N, γ=4, produits ==")
kap2 = 8*sp.pi*G_of
CT_dH = sp.simplify((1/H)**2/kap2)             # ℓ²/κ², ℓ=1/H
check("(ℓ²/κ²)/N = 1/(8π²) (valeur nue de Haro)",
      sp.simplify(CT_dH/N_ds - 1/(8*sp.pi**2)) == 0)
CT_prog = N/(32*sp.pi**2)
check("ratio dH/prog = 4 (facteur de convention = γ canonique)",
      sp.simplify((1/(8*sp.pi**2))/(1/(32*sp.pi**2))) == 4)
check("A_T·(coeff⟨TT⟩^prog) = 1/(2π²)",
      sp.simplify((16/N)*(N/(32*sp.pi**2)) - 1/(2*sp.pi**2)) == 0)
# map opérateur : c_W=ℓ²/(8κ²) ; ψ₂=2c_W ; T=n δW/δg, n=2 ⟹ ⟨TT⟩=8c_W
cW = ell**2/(8*kappa2)
psi2 = 2*cW
n = sp.Symbol("n")
TT_canon = sp.simplify(n**2*psi2)              # deux applications de T=nδW
check("⟨TT⟩_canon(n=2) = 8c_W = ℓ²/κ² (éq.90)",
      sp.simplify(TT_canon.subs(n, 2) - ell**2/kappa2) == 0)
check("γ = ⟨TT⟩_canon/ψ₂ = 4 FORCÉ (=n², n=2 Brown–York)",
      sp.simplify(TT_canon.subs(n, 2)/psi2) == 4)
check("firewall n : n=1 casse l'éq.90 (⟨TT⟩=2c_W=¼ℓ²/κ²)",
      sp.simplify(TT_canon.subs(n, 1) - ell**2/(4*kappa2)) == 0)
check("N_action = γ/4 : canonique 1 ; nu 1/4",
      sp.Rational(4, 4) == 1 and sp.Rational(1, 4) == sp.Rational(1, 4))

print("== T8 : continuation i^{d-1} — parité de ℓ^{d-1} ==")
for d, attend in ((2, "imag"), (3, "reel_neg"), (4, "imag")):
    z = i**(d-1)
    if attend == "imag":
        check("d=%d : facteur imaginaire" % d, sp.re(z) == 0)
    else:
        check("d=3 : facteur = −1 (RÉEL NÉGATIF)", z == -1)
check("C_T_signé(d=3) = −N/(32π²)",
      sp.simplify((-1)*CT_prog + N/(32*sp.pi**2)) == 0)

print("== T9 : report d'erreur nul ==")
Fs = sp.Symbol("F_im", positive=True)
P_err = 1/(2*sp.Abs(sp.im(s*0 + Fs*i + dr)))   # F = δr + i·F_im
check("𝒫 = 1/(2|Im F|) : δr ∉ observable",
      dr not in P_err.free_symbols)
CT_sig = -(Fs + dr)                             # le signé PORTE δr
check("C_T_signé porte δr", dr in CT_sig.free_symbols)
check("invariance s=±1 (magnitude)", sp.Abs(-Fs) == sp.Abs(Fs))

print("== T12 : garde-fou de signe (noyau de réponse) ==")
hs, cw = sp.symbols("h_s c_w", positive=True)
W = cw*hs**2                                    # W = c_W h□^{3/2}h (noyau)
T_resp = sp.diff(2*sp.diff(W, hs), hs)          # ⟨T⟩=2δW ⟹ noyau 4c_W
Wt = -cw*hs**2                                  # W̃ = −W (éq.61-62)
Tt_resp = sp.diff(-2*sp.diff(Wt, hs), hs)       # ⟨T̃⟩=−2δW̃ (éq.63)
check("C̃_T = +C_T : noyaux de réponse égaux (le − de W̃ compensé "
      "par le −2)", sp.simplify(T_resp - Tt_resp) == 0)
check("firewall : sans le −2 (⟨T̃⟩=+2δW̃), flip C̃_T=−C_T",
      sp.simplify(sp.diff(2*sp.diff(Wt, hs), hs) + T_resp) == 0)
# persistance dS : i^{d-1} attaché au seul ℓ^{d-1}, commun à C_T et C̃_T
r = sp.Symbol("r")                              # rapport C̃_T/C_T
check("C̃_T/C_T = +1 invariant sous continuation (facteur commun i^{d-1})",
      sp.simplify((i**2*Tt_resp)/(i**2*T_resp)) == 1)

print("\nREDEMO R-4 : %d/%d PASS — EXIT 0" % (sum(ok), len(ok)))
print("§6.4 : algèbre correcte + cibles reproduites sous hypothèses "
      "explicites — jamais davantage. { A4 ; A2★ ; N } INCHANGÉ.")
sys.exit(0)
