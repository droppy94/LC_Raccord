#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R4_CT_b.py — Silo R, lot R-4, INSTRUMENT AMENDÉ (instruction du
verdict CSE E-3, audit/CSE-R4R5-VERDICT.md). Remplace en aval
redemo_R4_CT.py, qui reste au dépôt (historique jamais réécrit).

STATUT DE MÉTHODE, déclaré : ceci est une REPRODUCTION GUIDÉE (réserve
d'aveuglement partiel, audit/RESERVE-AVEUGLEMENT-R4-R5.md ; verdict CSE
E-3). Le mot « redérivation indépendante » ne s'applique pas.

Discipline amendée (leçon CSE, opposable) :
- deux issues : PASS (assert discriminant, calcule) et CONSIGNATION
  (déclaration importée/triviale, NE COMPTE PAS dans le décompte) ;
- aucune disjonction rendant un assert infaillible ;
- firewalls de mutation là où le CSE les a demandés.

§6.4 : instruire ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
import sympy as sp

npass, ncons = [], []


def check(name, cond):
    cond = bool(cond)
    npass.append(cond)
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        sys.exit("ÉCHEC : " + name)


def consigne(name, note):
    ncons.append(name)
    print("  [CONSIGNATION] %s — %s" % (name, note))


H, MPl, k, u, ell, kappa2, N, K = sp.symbols(
    "H M_Pl k u ell kappa2 N K", positive=True)
i = sp.I
eta_n = sp.Symbol("eta", negative=True)

print("== T1 : route canonique — 𝒫 = ⟨|h|²⟩ (BD, η→0⁻) ==")
v = (1/sp.sqrt(2*k))*(1 - i/(k*eta_n))*sp.exp(-i*k*eta_n)
a = -1/(H*eta_n)
h = 2*v/(MPl*a)
P0 = sp.limit(sp.simplify(h*sp.conjugate(h)), eta_n, 0, "-")
check("𝒫 = 2H²/(M_Pl²k³)", sp.simplify(P0 - 2*H**2/(MPl**2*k**3)) == 0)
check("contrôle EOM du mode canonique",
      sp.simplify(sp.diff(v, eta_n, 2) + (k**2 - 2/eta_n**2)*v) == 0)

print("== T11 : EOM TT dS + Bunch–Davies ==")
hBD = (1 + i*k*eta_n)*sp.exp(-i*k*eta_n)
check("h''−(2/η)h'+k²h=0 pour BD",
      sp.simplify(sp.diff(hBD, eta_n, 2) - (2/eta_n)*sp.diff(hBD, eta_n)
                  + k**2*hBD) == 0)

print("== T10 : dualité S1 — (f_a, f_b), carte S ==")
fa = sp.cos(u) + u*sp.sin(u)
fb = u*sp.cos(u) - sp.sin(u)
for nm, f in (("f_a", fa), ("f_b", fb)):
    check("%s solution de y''−(2/u)y'+y=0" % nm,
          sp.simplify(sp.diff(f, u, 2) - (2/u)*sp.diff(f, u) + f) == 0)
S = sp.Matrix([[0, -1], [1, 0]])
consigne("S²=−𝟙, vp ±i", "arithmétique triviale sur matrice donnée "
         "(CSE : contenu mince) — vérifiée hors décompte : %s" %
         (S*S == -sp.eye(2) and set(S.eigenvals()) == {i, -i}))
check("f_a − i·f_b = (1−iu)e^{iu}",
      sp.simplify(sp.expand(
          (fa - i*fb - (1 - i*u)*sp.exp(i*u)).rewrite(sp.exp))) == 0)
check("(1−iu)e^{iu}|_{u=−kη} = BD",
      sp.simplify(sp.expand(
          (((1 - i*u)*sp.exp(i*u)).subs(u, -k*eta_n)
           - hBD).rewrite(sp.exp))) == 0)
c = sp.Matrix([1, -i])
check("BD mode propre +i de la carte S", sp.simplify(S*c - i*c).norm() == 0)

print("== T2 : route holographique — β forcé ; γ ∉ 𝒫 (testé) ==")
beta = sp.Symbol("beta", positive=True)
gam = sp.Symbol("gamma", positive=True)
F_expr = beta*a**2*sp.diff(hBD, eta_n)/hBD
ImF_lim = sp.limit(sp.im(sp.simplify(F_expr)), eta_n, 0, "-")
P_holo = 1/(2*sp.Abs(ImF_lim))
sol = sp.solve(sp.Eq(P_holo, 2*H**2/(MPl**2*k**3)), beta)
check("β = M_Pl²/4 UNIQUE (𝒫 holo = 𝒫 canonique)",
      len(sol) == 1 and sp.simplify(sol[0] - MPl**2/4) == 0)
# Instruction CSE : « γ ∉ 𝒫 » testé sur les EXPRESSIONS, plus littéral.
check("γ ∉ free_symbols(𝒫_holo) ET γ ∉ free_symbols(𝒫_canon)",
      gam not in P_holo.free_symbols and gam not in P0.free_symbols)
check("firewall : une 𝒫 contaminée (γ·𝒫) échoue au même prédicat",
      gam in (gam*P_holo).free_symbols)

print("== T3/T4/T5 : A_T, N, A_T·N=16 ==")
A_T = sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2
check("A_T = (k³/2π²)·𝒫·2",
      sp.simplify((k**3/(2*sp.pi**2))*(2*H**2/(MPl**2*k**3))*2 - A_T) == 0)
G_of = 1/(8*sp.pi*MPl**2)
N_ds = sp.pi/(G_of*H**2)
check("N = π/(GH²) = 8π²(M_Pl/H)²",
      sp.simplify(N_ds - 8*sp.pi**2*MPl**2/H**2) == 0)
check("A_T·N = 16 (H, M_Pl cancellés)", sp.simplify(A_T*N_ds) == 16)
check("firewall : G non réduit (G→2G) casse A_T·N=16",
      sp.simplify(A_T*sp.pi/((2*G_of)*H**2)) != 16)

print("== T6/T13 : C_T^dH calculé, γ dérivé de la carte, "
      "C_T^prog DÉRIVÉ (plus de fiat) ==")
kap2 = 8*sp.pi*G_of
CT_dH = sp.simplify((1/H)**2/kap2)               # ℓ²/κ², ℓ=1/H
check("(ℓ²/κ²)/N = 1/(8π²)", sp.simplify(CT_dH/N_ds - 1/(8*sp.pi**2)) == 0)
cW = ell**2/(8*kappa2)
psi2 = 2*cW
n = sp.Symbol("n")
TT_canon = sp.simplify(n**2*psi2)
check("⟨TT⟩_canon(n=2) = 8c_W = ℓ²/κ² (éq.90)",
      sp.simplify(TT_canon.subs(n, 2) - ell**2/kappa2) == 0)
gamma_derived = sp.simplify(TT_canon.subs(n, 2)/psi2)
check("γ = ⟨TT⟩_canon/ψ₂ = n²|_{n=2} = 4", gamma_derived == 4)
consigne("n=2 « unique/FORCÉ » DÉGRADÉ", "n=2 = convention Brown–York, "
         "PRÉMISSE nommée, non démontrée ici (instruction CSE : "
         "démontrer ou dégrader — dégradé)")
check("firewall n : n=1 donne une autre valeur (γ=1, ⟨TT⟩=¼ℓ²/κ²)",
      sp.simplify(TT_canon.subs(n, 1)/psi2) == 1
      and sp.simplify(TT_canon.subs(n, 1) - ell**2/(4*kappa2)) == 0)
# C_T^prog DÉRIVÉ : C_T^dH / γ — plus de constante posée par fiat.
CT_prog_der = sp.simplify(CT_dH/gamma_derived)
check("C_T^prog = C_T^dH/γ = N/(32π²) (DÉRIVÉ, ratio 4 = γ)",
      sp.simplify(CT_prog_der - N_ds/(32*sp.pi**2)) == 0)
check("A_T·(coeff⟨TT⟩^prog) = 1/(2π²) (sur le C_T^prog dérivé)",
      sp.simplify(A_T*CT_prog_der - 1/(2*sp.pi**2)) == 0)
consigne("N_action := γ/4", "DÉFINITION importée du gel (T13) — "
         "l'objet n'est pas construit ici ; valeurs sur γ dérivé "
         "consignées : γ(n=2)/4 = 1 (canonique), γ(n=1)/4 = 1/4 (nu)")

print("== T8 : continuation i^{d-1} + C_T_signé DÉRIVÉ EN CHAÎNE ==")
for d, attend in ((2, "imag"), (3, "reel_neg"), (4, "imag")):
    z = i**(d-1)
    if attend == "imag":
        check("d=%d : facteur imaginaire" % d, sp.re(z) == 0)
    else:
        check("d=3 : facteur = −1 (RÉEL NÉGATIF)", z == -1)
# Instruction CSE : plus de −x+x=0. Chaîne : parité calculée × C_T^prog dérivé.
CT_signed = sp.simplify(i**(3-1)*CT_prog_der)
check("C_T_signé(d=3) = i²·C_T^prog(dérivé) = −N/(32π²)",
      sp.simplify(CT_signed + N_ds/(32*sp.pi**2)) == 0)
check("firewall : d=4 ne donne PAS un réel (i³·C_T^prog imaginaire)",
      sp.re(sp.simplify(i**(4-1)*CT_prog_der)) == 0
      and sp.im(sp.simplify(i**(4-1)*CT_prog_der)) != 0)

print("== T9 : report d'erreur — s VIVANT (instruction CSE) ==")
dr = sp.Symbol("delta_r", real=True)
Fim = sp.Symbol("F_im", positive=True)
s = sp.Symbol("s", real=True)
F_gen = dr + i*s*Fim                              # F = δr + i·s·F_im
P_of = 1/(2*sp.Abs(sp.im(F_gen)))
check("δr ∉ 𝒫 (extrait par im(F) sur l'expression, pas par "
      "construction)", dr not in P_of.free_symbols)
P_plus = P_of.subs(s, 1)
P_minus = P_of.subs(s, -1)
check("invariance s=±1 : 𝒫(s=+1) = 𝒫(s=−1) par SUBSTITUTION (s vivant)",
      sp.simplify(P_plus - P_minus) == 0)
P_bad = 1/(2*sp.im(F_gen))                        # mutation : sans |·|
check("firewall : sans le module, 𝒫(s=+1) ≠ 𝒫(s=−1) — la mutation mord",
      sp.simplify(P_bad.subs(s, 1) - P_bad.subs(s, -1)) != 0)
consigne("« C_T_signé porte δr »", "NON DÉRIVABLE depuis les prémisses "
         "de l'instrument (la construction du signé à partir de F "
         "relève du corps de la tête) — cible REQUALIFIÉE consignation "
         "reportée ; l'assert fabriqué de l'instrument v1 est retiré")

print("== T12 : garde-fou de signe + LOCALISATION i^{d-1} testée ==")
hs, cw = sp.symbols("h_s c_w", positive=True)
W = cw*hs**2
T_resp = sp.diff(2*sp.diff(W, hs), hs)
Wt = -cw*hs**2
Tt_resp = sp.diff(-2*sp.diff(Wt, hs), hs)
check("C̃_T = +C_T : noyaux de réponse égaux (le − de W̃ compensé "
      "par le −2)", sp.simplify(T_resp - Tt_resp) == 0)
check("firewall : sans le −2, flip C̃_T=−C_T",
      sp.simplify(sp.diff(2*sp.diff(Wt, hs), hs) + T_resp) == 0)
# Instruction CSE : tester la LOCALISATION de i^{d-1} sur ℓ^{d-1},
# plus un ratio à facteur commun. Structure importée (prémisse) :
# C_T(d) = K·ℓ^{d-1}/κ² (cohérente avec C_T^dH = ℓ²/κ² à d=3).
for d in (2, 3, 4):
    CT_model = K*ell**(d-1)/kappa2
    check("localisation d=%d : C_T(ℓ→iℓ)/C_T(ℓ) = i^{d-1} "
          "(par substitution)" % d,
          sp.simplify(CT_model.subs(ell, i*ell)/CT_model - i**(d-1)) == 0)
CT3 = K*ell**2/kappa2
check("firewall localisation : facteur attaché à κ² donnerait i^{-1}=−i "
      "≠ i² (d=3) — la mutation discrimine",
      sp.simplify(CT3.subs(kappa2, i*kappa2)/CT3 - (-i)) == 0
      and sp.simplify(-i - i**2) != 0)
consigne("C̃_T/C_T = +1 invariant sous continuation",
         "COROLLAIRE des deux PASS précédents (noyaux égaux + facteur "
         "localisé commun) — plus un assert autonome (l'assert v1 "
         "testait x/x=1, retiré)")

print("\nREDEMO R-4b : %d/%d PASS discriminants + %d consignations "
      "déclarées — EXIT 0" % (sum(npass), len(npass), len(ncons)))
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (reproduction "
      "guidée) — verdict CSE E-3 instruit, jamais E-1.")
print("§6.4 : instruire ne scelle, ne réduit, ne compte, ne démontre "
      "rien. { A4 ; A2★ ; N } INCHANGÉ.")
sys.exit(0)
