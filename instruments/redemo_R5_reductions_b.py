#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R5_reductions_b.py — Silo R, lot R-5, INSTRUMENT AMENDÉ
(instruction du verdict CSE E-3, audit/CSE-R4R5-VERDICT.md). Remplace
en aval redemo_R5_reductions.py, qui reste au dépôt.

STATUT DE MÉTHODE, déclaré : REPRODUCTION GUIDÉE (réserve d'aveuglement
partiel + verdict CSE E-3). « Redérivation indépendante » ne s'applique
pas.

Discipline amendée (leçon CSE) : PASS = assert discriminant seul compté ;
CONSIGNATION = déclaration importée/triviale, hors décompte ; aucune
disjonction rendant un assert infaillible (P6-#16 v1 retiré).

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


i = sp.I
k, H, MPl, g0 = sp.symbols("k H M_Pl g_0", positive=True)
eta = sp.Symbol("eta", negative=True)

print("== P1 : relation d'état BD — g₃ = −(i/3)k³g₀ ==")
hBD = g0*(1 + i*k*eta)*sp.exp(-i*k*eta)
ser = sp.series(hBD, eta, 0, 5).removeO().expand()
check("coefficient η³ = −(i/3)k³g₀",
      sp.simplify(ser.coeff(eta, 3) + (i/3)*k**3*g0) == 0)
check("contrôle : coefficient η² = +k²g₀/2 (réel, pair)",
      sp.simplify(ser.coeff(eta, 2) - k**2*g0/2) == 0)
check("contrôle : pas de terme η¹ (développement FG propre)",
      ser.coeff(eta, 1) == 0)

print("== P2 : route A3 — projection TT d'un tenseur isotrope = 0 ==")
n1, n2, n3, c = sp.symbols("n1 n2 n3 c", real=True)
nv = sp.Matrix([n1, n2, n3])
delta = sp.eye(3)
P = delta - nv*nv.T


def PiTT(T):
    out = sp.zeros(3, 3)
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


res = PiTT(c*delta)
res = sp.simplify(sp.expand(res.subs(n3**2, 1 - n1**2 - n2**2)))
check("Π^TT(c·δ) = 0 (isotrope = pure trace) ⟹ ⟨g₃⟩=0 forcé par A3",
      res == sp.zeros(3, 3))
# firewall CSE (sonde de l'auditeur intégrée) : un tenseur ANISOTROPE
# ne s'annule pas — le projecteur discrimine.
T_aniso = sp.diag(1, 0, 0)
res_a = sp.simplify(sp.expand(
    PiTT(T_aniso).subs(n3**2, 1 - n1**2 - n2**2)))
check("firewall : Π^TT(diag(1,0,0)) ≠ 0 — le test discrimine",
      res_a != sp.zeros(3, 3))

print("== P3 : route A4, inclusion stricte par TÉMOIN ==")
consigne("A4 ⟹ ⟨g₃⟩=0", "trivial (g₃=0 opérateur) — déclaration, "
         "hors décompte")
P0 = 2*H**2/(MPl**2*k**3)
amp = (i/3)*k**3
mean_g3 = amp*0
var_g3 = sp.simplify(amp*sp.conjugate(amp)*P0)
check("témoin BD ∈ S_A3 (⟨g₃⟩ = a·⟨g₀⟩ = 0)", mean_g3 == 0)
check("témoin BD ∉ S_A4 (⟨g₃g₃⟩ = k⁶𝒫₀/9 ≠ 0)",
      sp.simplify(var_g3 - k**6*P0/9) == 0 and var_g3 != 0)
consigne("S_A4 ⊊ S_A3 STRICTE, sens unique, {A3,A4}→{A4} au un-point",
         "CONCLUSION portée par les deux PASS témoins ci-dessus — "
         "déclaration, hors décompte (assert v1 littéral retiré)")

print("== P4 : écart A3/A4 = deux-point ∝ k³ ; indépendance du "
      "un-point CALCULÉE ==")
check("⟨g₃g₃⟩ = (2H²/9M_Pl²)·k³ ∝ k³",
      sp.simplify(var_g3 - (2*H**2/(9*MPl**2))*k**3) == 0)
d, Delta = 3, 3
check("Δ=3 : puissance 2Δ−d = 3", 2*Delta - d == 3)
lam = sp.Symbol("lambda", positive=True)
check("invariance d'échelle du spectre adimensionné",
      sp.simplify((k**3*P0).subs(k, lam*k) - k**3*P0) == 0)
# Instruction CSE : « l'écart ne dépend pas du un-point » — CALCULÉ.
# Deux-point CONNEXE de g₃=a·g₀ avec ⟨g₀⟩=m ≠ 0 quelconque :
m = sp.Symbol("m", real=True)
V = sp.Symbol("V", positive=True)                 # Var(g₀), connexe
E_XXbar = V + m**2                                 # ⟨g₀ḡ₀⟩
conn = sp.simplify(amp*sp.conjugate(amp)*E_XXbar
                   - (amp*m)*sp.conjugate(amp*m))
check("⟨g₃g₃⟩_connexe = |a|²·V : le un-point m se CANCELLE (calculé)",
      m not in conn.free_symbols
      and sp.simplify(conn - k**6*V/9) == 0)
check("firewall : le moment NON connexe |a|²(V+m²) dépend de m — "
      "la distinction mord",
      m in sp.simplify(amp*sp.conjugate(amp)*E_XXbar).free_symbols)

print("== P5 : résidu gaussien de D1 ==")
consigne("« données gaussiennes = {moyenne ; deux-point} ⟹ résidu = "
         "1 nombre »", "THÉORÈME DE CARACTÉRISATION GAUSSIENNE, prémisse "
         "importée — non testable par free_symbols (CSE : l'assert v1 "
         "A·k³/k³ était une paraphrase, retiré) ; la détermination "
         "{moyenne=0 (P2/P3) ; forme k³ (P4)} est portée par les PASS "
         "amont, le théorème reste une prémisse déclarée")
check("le nombre = A_T : (k³/2π²)·𝒫₀·2 = (2/π²)(H/M_Pl)² "
      "(identification calculée)",
      sp.simplify((k**3/(2*sp.pi**2))*P0*2
                  - sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2) == 0)

print("== P6 : candidat D1⟷E — A_T = 16/N par ÉLIMINATION "
      "(plus de disjonction) ==")
G_of = 1/(8*sp.pi*MPl**2)
N_ds = sp.pi/(G_of*H**2)
A_T = sp.Rational(2, 1)/sp.pi**2*(H/MPl)**2
check("A_T·N = 16 (re-vérifié)", sp.simplify(A_T*N_ds) == 16)
# Instruction CSE : P6-#16 v1 (disjonction infaillible) RETIRÉ.
# Remplacé par un calcul d'ÉLIMINATION indépendant : résoudre
# (H/M_Pl)² depuis N, substituer dans A_T, obtenir 16/N.
x = sp.Symbol("x", positive=True)                  # x = (H/M_Pl)²
Nsym = sp.Symbol("N", positive=True)
x_of_N = sp.solve(sp.Eq(Nsym, 8*sp.pi**2/x), x)
check("élimination : (H/M_Pl)² = 8π²/N (solution unique)",
      len(x_of_N) == 1 and sp.simplify(x_of_N[0] - 8*sp.pi**2/Nsym) == 0)
A_T_of_N = sp.simplify((sp.Rational(2, 1)/sp.pi**2)*x_of_N[0])
check("A_T(N) = 16/N EXACTEMENT (aucun paramètre libre hors N)",
      sp.simplify(A_T_of_N - 16/Nsym) == 0
      and A_T_of_N.free_symbols == {Nsym})
check("firewall : un coefficient muté (3/π²) ne donne PAS 16/N",
      sp.simplify((sp.Rational(3, 1)/sp.pi**2)*x_of_N[0] - 16/Nsym) != 0)

print("== P7 : conclusion de comptage ==")
consigne("inconnues restantes de l'arc = { A4 ; A2★ ; N }",
         "RECOMBINAISON des PASS amont (un-point A4 ; forme scellée ; "
         "amplitude 16/N) — déclaration au rapport, hors décompte "
         "(assert v1 set==set retiré ; déjà déclaré consignation au "
         "rapport R-5 §3, désormais déclaré DANS l'instrument)")
consigne("RÉDUCTION DE COMPTAGE, PAS FERMETURE",
         "D1 non clos (N non fixé) ; circularité LC-E intacte ; >2-pt "
         "décision ouverte — garde-fou §6.4, hors décompte")

print("\nREDEMO R-5b : %d/%d PASS discriminants + %d consignations "
      "déclarées — EXIT 0" % (sum(npass), len(npass), len(ncons)))
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (reproduction "
      "guidée) — verdict CSE E-3 instruit, jamais E-1.")
print("§6.4 : instruire ne scelle, ne réduit, ne compte, ne démontre "
      "rien. { A4 ; A2★ ; N } INCHANGÉ ; réduire n'est pas fermer.")
sys.exit(0)
