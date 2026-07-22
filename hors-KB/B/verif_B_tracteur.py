#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_B_tracteur.py  —  compagnon de LC-RESULTAT-B-TRACTEUR (module [B]).
Vérifie symboliquement (sympy, sans réseau) les faits qui portent le verdict :

  (A) de Sitter (tranchage fermé) est CONFORMÉMENT PLAT  : Weyl ≡ 0.
  (B) de Sitter est Einstein, Schouten P_ab = λ g_ab avec λ constant
      ⟹ tenseur de Cotton A_abc ≡ 0.
  (A)+(B) ⟹ la courbure de tracteur (= Weyl ⊕ Cotton) s'annule sur le fond dS
           ⟹ connexion de tracteur PLATE sur le fond ⟹ aucune information
           locale transportable sur le fond (face B-PAUVRE).
  (C) Schwarzschild–de Sitter a un Weyl NON nul (porté par la masse M)
      ⟹ courbure de tracteur ≠ 0 : le résidu transportable EST exactement
         le Weyl (rescalé) — ni toujours nul, ni générique. (face « résidu »)
  (D) En dimension ≤ 3 le Weyl est identiquement nul : la fibre S² (2D) ne
      porte AUCUN invariant conforme local ⟹ pas de dynamique intrinsèque
      sur la fibre (face B-PAUVRE, restreinte à S²).

EXIT 0 attendu si toutes les assertions passent.
"""
import sys
import sympy as sp

echecs = []

def check(nom, cond):
    tag = "OK " if cond else "ECHEC"
    print(f"  [{tag}] {nom}")
    if not cond:
        echecs.append(nom)

# ----------------------------------------------------------------------
# Outillage géométrique minimal (conventions standard, indices bas pour R).
# ----------------------------------------------------------------------
def christoffel(g, x):
    n = len(x); gi = g.inv()
    G = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
            - sp.diff(g[b, c], x[d])) for d in range(n))/2)
           for c in range(n)] for b in range(n)] for a in range(n)]
    return G

def riemann_low(g, x):
    n = len(x); G = christoffel(g, x)
    # R^a_{bcd}
    Rup = [[[[sp.simplify(sp.diff(G[a][b][d], x[c]) - sp.diff(G[a][b][c], x[d])
             + sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    R = [[[[sp.simplify(sum(g[a, e]*Rup[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    return R, Rup

def ricci_scalar(g, x):
    n = len(x); R, Rup = riemann_low(g, x)
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rup[a][b][a][d] for a in range(n))))
    gi = g.inv()
    Rs = sp.simplify(sum(gi[b, d]*Ric[b, d] for b in range(n) for d in range(n)))
    return R, Ric, Rs

def weyl_low(g, x):
    """C_abcd = R_abcd - (g KN P)_abcd, Schouten P = 1/(n-2)(Ric - R/(2(n-1)) g)."""
    n = len(x)
    R, Ric, Rs = ricci_scalar(g, x)
    P = sp.Matrix(n, n, lambda a, b: sp.simplify((Ric[a, b] - Rs/(2*(n-1))*g[a, b])/(n-2)))
    def KN(a, b, c, d):   # produit de Kulkarni–Nomizu (g ∧ P)
        return (g[a, c]*P[b, d] - g[a, d]*P[b, c] + g[b, d]*P[a, c] - g[b, c]*P[a, d])
    C = [[[[sp.simplify(R[a][b][c][d] - KN(a, b, c, d))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    return C, P, Ric, Rs

def weyl_is_zero(g, x):
    C, P, Ric, Rs = weyl_low(g, x)
    n = len(x)
    z = all(sp.simplify(C[a][b][c][d]) == 0
            for a in range(n) for b in range(n) for c in range(n) for d in range(n))
    return z, C, P, Ric, Rs

# ----------------------------------------------------------------------
print("verif_B_tracteur — vérification symbolique du fond du module [B]\n")

# (A)+(B) de Sitter, tranchage fermé conforme-statique :
#   ds^2 = 1/(H^2 cos^2 η) ( -dη^2 + dχ^2 + sin^2χ dθ^2 + sin^2χ sin^2θ dφ^2 )
H = sp.symbols('H', positive=True)
eta, chi, th, ph = sp.symbols('eta chi theta phi', real=True)
x4 = [eta, chi, th, ph]
Om = 1/(H**2*sp.cos(eta)**2)
gdS = sp.diag(-Om, Om, Om*sp.sin(chi)**2, Om*sp.sin(chi)**2*sp.sin(th)**2)

print("(A)+(B) de Sitter (Λ = 3H^2) :")
zdS, CdS, PdS, RicdS, RsdS = weyl_is_zero(gdS, x4)
check("Weyl(dS) ≡ 0  (conformément plat ⟹ tracteur plat sur le fond)", zdS)
# Einstein : Ric = Λ g avec Λ = 3H^2
Lam = 3*H**2
einstein = all(sp.simplify(RicdS[a, b] - Lam*gdS[a, b]) == 0 for a in range(4) for b in range(4))
check("Ric(dS) = Λ g,  Λ = 3H^2  (Einstein)", einstein)
check("R(dS) = 4Λ = 12H^2", sp.simplify(RsdS - 12*H**2) == 0)
# Schouten proportionnel à la métrique, coefficient CONSTANT ⟹ ∇P = 0 ⟹ Cotton = 0
lam0 = sp.simplify(PdS[0, 0]/gdS[0, 0])
prop = all(sp.simplify(PdS[a, b] - lam0*gdS[a, b]) == 0 for a in range(4) for b in range(4))
cst = all(sp.simplify(sp.diff(lam0, x4[k])) == 0 for k in range(4))
check("Schouten(dS) = λ g avec λ constant ⟹ Cotton ≡ 0", prop and cst)
print(f"        λ = {sp.simplify(lam0)}  (= Λ/6 = H^2/2)\n")

# (C) Schwarzschild–de Sitter : Weyl porté par la masse ⟹ tracteur ≠ 0
M, r, t = sp.symbols('M r t', positive=True)
th2, ph2 = sp.symbols('vartheta varphi', real=True)
f = 1 - 2*M/r - (H**2)*r**2            # Λ/3 = H^2
xS = [t, r, th2, ph2]
gS = sp.diag(-f, 1/f, r**2, r**2*sp.sin(th2)**2)
print("(C) Schwarzschild–de Sitter (masse M, Λ = 3H^2) :")
zS, CS, PS, RicS, RsS = weyl_is_zero(gS, xS)
# composante radiale-temporelle typique du Weyl (Coulombien, ∝ M/r^3)
C_trtr = sp.simplify(CS[0][1][0][1])
check("Weyl(SdS) ≠ 0  (résidu transportable = Weyl rescalé)", (not zS) and C_trtr != 0)
check("le Weyl s'annule si M → 0  (retour au fond dS conformément plat)",
      sp.simplify(C_trtr.subs(M, 0)) == 0)
print(f"        C_{{trtr}} = {C_trtr}   (∝ M : porté par la masse)\n")

# (D) dimension 2 : la fibre S² ne porte aucun invariant conforme local.
#   Weyl est défini pour n≥3 et identiquement nul pour n≤3 (comptage d'indices).
#   Démonstration explicite sur S² (métrique ronde) : Riemann ∝ (g∧g),
#   entièrement reconstruit par Ric/R ⟹ partie sans-trace (Weyl) vide.
a2 = sp.symbols('a', positive=True)
x2 = [th, ph]
gS2 = sp.diag(a2**2, a2**2*sp.sin(th)**2)
R2, Ric2, Rs2 = ricci_scalar(gS2, x2)
# en 2D : R_{abcd} = (Rs/2)(g_ac g_bd - g_ad g_bc) ; on le vérifie composante à composante
n2 = 2
maxwell2 = all(sp.simplify(R2[a][b][c][d]
              - (Rs2/2)*(gS2[a, c]*gS2[b, d] - gS2[a, d]*gS2[b, c])) == 0
              for a in range(n2) for b in range(n2) for c in range(n2) for d in range(n2))
check("fibre 2D (S²) : Riemann entièrement fixé par R (Weyl ≡ 0, pas d'invariant local)",
      maxwell2)
check("courbure de Gauss de S²(rayon a) = 1/a^2  (K = R/2)",
      sp.simplify(Rs2/2 - 1/a2**2) == 0)

print("\n" + "="*64)
if echecs:
    print("RÉSULTAT : ECHEC —", ", ".join(echecs)); sys.exit(1)
print("RÉSULTAT : toutes les assertions passent.")
print("Chaîne portée : Weyl(dS)=0 & Cotton(dS)=0 ⟹ tracteur PLAT sur le fond ;")
print("               Weyl(SdS)≠0 ⟹ résidu transportable = Weyl rescalé ;")
print("               fibre 2D ⟹ aucun invariant conforme intrinsèque sur S².")
sys.exit(0)
