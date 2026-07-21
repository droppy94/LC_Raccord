#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_facteur.py — Sceau du verrou D1 (LC-RACCORD, module A) : facteur conforme
au crossover CCC. Dépendance : sympy. Re-exécutable.
  [D1.bg]  réciprocité de Penrose Ω̂Ω̌=-1 : passé dS (Λ) -> futur FRW radiation (R=0)
           => le BACKGROUND de la transition est fixé ; la donnée dynamique (g₃) ne l'est pas.
"""
import sympy as sp
eta,x,y,z,H = sp.symbols('eta x y z H', positive=True)
X=[eta,x,y,z]; n=4
# bridging conformément plat g=-dη²+dx²+dy²+dz² ; ĝ=Ω̂²g = dS (Ω̂=-1/(Hη)) ;
# réciprocité Ω̌=-1/Ω̂=Hη ; ǧ=Ω̌²g => a(η)=Hη
a=H*eta
g=sp.diag(-a**2,a**2,a**2,a**2); gi=g.inv()
Gam=[[[sp.simplify(sum(gi[l,m]*(sp.diff(g[m,i],X[j])+sp.diff(g[m,j],X[i])-sp.diff(g[i,j],X[m]))
      for m in range(n))/2) for j in range(n)] for i in range(n)] for l in range(n)]
def Ric(i,j):
    return sp.simplify(sum(sp.diff(Gam[l][i][j],X[l]) for l in range(n))
        -sum(sp.diff(Gam[l][i][l],X[j]) for l in range(n))
        +sum(Gam[l][i][j]*Gam[m][l][m] for l in range(n) for m in range(n))
        -sum(Gam[l][i][m]*Gam[m][l][j] for l in range(n) for m in range(n)))
Rc=[[Ric(i,j) for j in range(n)] for i in range(n)]
R=sp.simplify(sum(gi[i,j]*Rc[i][j] for i in range(n) for j in range(n)))
G00=sp.simplify(Rc[0][0]-sp.Rational(1,2)*R*g[0,0])
tr=sp.simplify(sum(gi[i,j]*(Rc[i][j]-sp.Rational(1,2)*R*g[i,j]) for i in range(n) for j in range(n)))
print("="*70); print("[D1.bg] réciprocité Ω̂Ω̌=-1 : dS (passé, Λ) -> ǧ=H²η²(-dη²+dx²+dy²+dz²)")
print("   R(ǧ) =",R," (=0 => trace nulle => radiation)")
print("   G_00 =",G00," (>0 => densité positive) ; trace G^a_a =",tr)
print("   => BACKGROUND : Λ-dominé -> radiation-dominé (Big Bang). FIXÉ par la réciprocité.")
print("   MAIS : la donnée dynamique (g₃ = Weyl rescalé, cf. LC-A) n'est PAS fixée par")
print("          la réciprocité (1 relation scalaire) => verrou D1 (prescription requise).")
print("="*70)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutées (additif) ---
# Encode la conclusion imprimée [D1.bg] : fond ǧ trace-free (radiation) + densité > 0.
assert sp.simplify(R) == 0, "D1.bg: R(g_check) doit etre nul (radiation, trace nulle)"
assert sp.simplify(tr) == 0, "D1.bg: trace G^a_a nulle (radiation)"
assert float(G00.subs({H: 1, eta: 1})) > 0, "D1.bg: G_00 > 0 (densite positive)"
print("EXIT 0 (F1: 3 assertions D1.bg verifiees)")
