#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_F6_memoire_cisaillement.py — Sceau du COEUR INTERNE G1/G2 du front F6
(BMS / mémoire gravitationnelle), branche FALSIFIABILITÉ. KB-only, sympy.

Adossé aux relations SCELLÉES :
  - E_ij|_{I+} = (d/2H) g3        (LC-D3-WEYL-BUNCHDAVIES §3, d=3) : E et g3 = MÊME datum TT radiatif
  - E ∝ g3 ∝ <T>   parité PAIRE / tenseur vrai / spin-2 TT       (LC-D-NONLIN-VERROU sub-Q2)
  - B ∝ Cotton[g0] parité IMPAIRE / pseudo-tenseur               (LC-D-NONLIN-VERROU sub-Q1/Q3)
  - <T_ij> = (d/16πG) g3                                         (LC-D-HOLOGRAPHIE-G3)

ÉTABLIT (algèbre — niveau REPRÉSENTATION + DICTIONNAIRE) :
  G1  La mémoire de déplacement  Δσ_ij = -2 ( D_iD_j - (1/d) g0_ij D² ) C  est un HESSIEN :
      symétrique, sans trace, PARITÉ PAIRE (tenseur vrai, construit SANS ε) => même secteur
      que g3 ; DISJOINT du secteur magnétique (pseudo-tenseur, une ε, parité impaire = Cotton/B)
      => la mémoire est une fonctionnelle de {g3, g0}, AUCUN datum neuf.
  G2  L'aspect de charge de supertranslation = <T> = (d/16πG) g3 (d=3) => Q[f] fonctionnelle
      LINÉAIRE de g3 = secteur C_T (CONSOLIDATION).

NON tranché ici (= G3, différé / fetch-conditionnel) : le flux-balance Λ-BMS et le caractère
bien-défini du « saut net entre vides » en dS spacelike-I+. SANS SURCLASSEMENT (§6.4) :
réduction de datum + consolidation ≠ « D1 clos / N fixé / signature CCC établie / CCC démontrée » ;
{A4 ; A2★ ; N} INCHANGÉ.
"""
import sympy as sp

N_AS = 0
def check(cond, msg):
    global N_AS
    assert bool(cond), "ÉCHEC: " + msg
    N_AS += 1

def zeromat(Mx):
    Mx = sp.Matrix(Mx)
    return all(sp.simplify(e) == 0 for e in Mx)

x1, x2, x3 = sp.symbols('x1 x2 x3', real=True)
X = (x1, x2, x3)
d = 3
delta = sp.eye(3)
H, G, k = sp.symbols('H G k', positive=True)

def hess(f):
    return sp.Matrix(3, 3, lambda i, j: sp.diff(f, X[i], X[j]))

def lap(f):
    return sum(sp.diff(f, xi, xi) for xi in X)

def subst_neg(expr):
    return expr.subs({x1: -x1, x2: -x2, x3: -x3}, simultaneous=True)

# =====================================================================
# [A] MÉMOIRE = HESSIEN ÉLECTRIQUE : sym + sans trace + PARITÉ PAIRE
# =====================================================================
# Scalaire de supertranslation (Goldstone vivant dans la classe conforme g0) : choix générique lisse.
C = sp.cos(x1) * sp.sin(2 * x2) * sp.exp(x3)

def memoire(scal):
    return -2 * (hess(scal) - sp.Rational(1, d) * lap(scal) * delta)

M = memoire(C)

check(zeromat(M - M.T), "[A1] Δσ symétrique")
check(sp.simplify(M.trace()) == 0, "[A2] Δσ sans trace")

# Parité PAIRE : reconstruire la MÊME fonctionnelle à partir du scalaire parité-imagé C(-x).
# Pour un tenseur VRAI (zéro ε) : fonctionnelle[C(-x)](x) == fonctionnelle[C](-x).
M_from_Cneg = memoire(subst_neg(C))
M_at_negx = M.applyfunc(subst_neg)
check(zeromat(M_from_Cneg - M_at_negx), "[A3] Δσ PARITÉ PAIRE (tenseur vrai = secteur E/g3)")

# Contrôle MAGNÉTIQUE : tenseur symétrique construit avec UNE ε à partir d'un champ symétrique
# générique (NON-Hessien, sinon la curl s'annule). Une ε => pseudo-tenseur (parité impaire = Cotton/B).
h = sp.Matrix([[sp.sin(x2) * x3, sp.exp(x1),     x2**2],
               [sp.exp(x1),      sp.cos(x1) * x3, sp.sin(x3)],
               [x2**2,           sp.sin(x3),      x1 * x2]])  # symétrique, NON-Hessien

def magnetique(hmat):
    def ent(i, j):
        t1 = sum(sp.LeviCivita(i, kk, l) * sp.diff(hmat[l, j], X[kk]) for kk in range(3) for l in range(3))
        t2 = sum(sp.LeviCivita(j, kk, l) * sp.diff(hmat[l, i], X[kk]) for kk in range(3) for l in range(3))
        return sp.Rational(1, 2) * (t1 + t2)
    return sp.Matrix(3, 3, ent)

Nmag = magnetique(h)
check(zeromat(Nmag - Nmag.T), "[A4] contrôle magnétique symétrique")
check(not zeromat(Nmag), "[A5] contrôle magnétique NON identiquement nul")

# parité IMPAIRE : fonctionnelle[h(-x)](x) == -fonctionnelle[h](-x)  (une ε)
h_neg = h.applyfunc(subst_neg)
N_from_hneg = magnetique(h_neg)
N_at_negx = Nmag.applyfunc(subst_neg)
check(zeromat(N_from_hneg + N_at_negx), "[A6] magnétique PARITÉ IMPAIRE (pseudo-tenseur = secteur Cotton/B)")
# disjonction de parité : le magnétique NE satisfait PAS la loi paire (firewall [D-i])
check(not zeromat(N_from_hneg - N_at_negx), "[A7] DISJOINT : magnétique ≠ secteur pair (mémoire/g3)")

# =====================================================================
# [B] g3 = datum TT ; même secteur (pair) que la mémoire
# =====================================================================
coeff_E_g3 = sp.Rational(d, 1) / (2 * H)            # E_ij = (d/2H) g3, d=3
check(sp.simplify(coeff_E_g3 - sp.Rational(3, 2) / H) == 0, "[B1] E=(d/2H)g3, d=3 => 3/(2H)")

# polarisation TT pour k || z  (e_+ : 11=+1, 22=-1)
kvec = sp.Matrix([0, 0, k])
ep = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
check(zeromat((ep * kvec)), "[B2] g3 transverse (e·k = 0)")
check(sp.simplify(ep.trace()) == 0, "[B3] g3 sans trace")
check(zeromat(ep - ep.T), "[B4] g3 symétrique (tenseur vrai, secteur PAIR = celui de Δσ)")

# =====================================================================
# [C] CHARGE MOLLE ↔ STRESS CÉLESTE  <T> = (d/16πG) g3  (secteur C_T)
# =====================================================================
coeff_T_g3 = sp.Rational(d, 1) / (16 * sp.pi * G)   # <T_ij> = (d/16πG) g3, d=3
check(sp.simplify(coeff_T_g3 - 3 / (16 * sp.pi * G)) == 0, "[C1] <T>=(d/16πG)g3, d=3 => 3/(16πG)")

# Q[f] = ∮ f <T>  : densité de charge linéaire en g3 => fonctionnelle du SEUL secteur C_T
a, g3s, fs = sp.symbols('a g3s fs', real=True)
Qden = lambda g3v: fs * coeff_T_g3 * g3v
check(sp.simplify(Qden(a * g3s) - a * Qden(g3s)) == 0, "[C2] Q[f] linéaire en g3 (fonctionnelle de C_T)")
check(sp.simplify(sp.diff(Qden(g3s), g3s) - fs * coeff_T_g3) == 0, "[C3] aspect de charge ∝ g3 (aucun datum indépendant)")

# =====================================================================
# [D] FIREWALL
# =====================================================================
# (i) déjà posé en [A7] : une vraie part magnétique (ε) est de parité OPPOSÉE => ne peut pas
#     être la mémoire de déplacement (qui doit apparier la parité PAIRE de g3).
check(not zeromat(N_from_hneg - N_at_negx), "[D-i] firewall: magnétique hors du secteur mémoire/g3")
# (ii) mutation du coefficient d=4 : casse E=(d/2H)g3 (résidu non nul)
d_mut = 4
resid = sp.simplify(sp.Rational(d_mut, 1) / (2 * H) - sp.Rational(3, 2) / H)
check(sp.simplify(resid - 1 / (2 * H)) == 0 and resid != 0, "[D-ii] firewall: mutation d=4 casse E=(d/2H)g3")
# (iii) sans soustraction de trace, Δσ n'est PAS sans trace
M_notrace = -2 * hess(C)
check(sp.simplify(M_notrace.trace() + 2 * lap(C)) == 0, "[D-iii-a] trace(Δσ_sans-soustraction) = -2∇²C")
check(sp.simplify(lap(C)) != 0, "[D-iii-b] ∇²C ≠ 0 => la mutation rend la trace NON nulle")

# =====================================================================
print("=" * 78)
print("verif_F6_memoire_cisaillement — COEUR INTERNE G1/G2 (front F6 BMS/mémoire)")
print(f"OK — {N_AS} assertions.")
print("  G1 : Δσ (mémoire de déplacement) = HESSIEN électrique (sym/sans trace/PARITÉ PAIRE)")
print("       = MÊME secteur que g3 ; DISJOINT du magnétique (pseudo, Cotton/B) => AUCUN datum neuf.")
print("  G2 : aspect de charge de supertranslation = <T> = (3/16πG) g3 => Q[f] linéaire en g3")
print("       = secteur C_T (CONSOLIDATION).")
print("  NON tranché (= G3, différé) : flux-balance Λ-BMS / saut net entre vides en dS spacelike-I+.")
print("  COEFFICIENT / niveau : représentation + dictionnaire (relations amont scellées).")
print("  SANS SURCLASSEMENT (§6.4) : réduction de datum + consolidation ≠ D1 clos / N fixé /")
print("  signature CCC établie / CCC démontrée ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos. EXIT 0.")
print("=" * 78)
