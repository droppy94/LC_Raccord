#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_moduleA_scri.py — Sceau du module A (LC-RACCORD) : structure conforme de
de Sitter et caractère causal de 𝓘. Re-exécutable. Dépendance : sympy.
  [A.dS.1]  c'est bien dS : R = 4Λ = 12H² ; R_ab = Λ g_ab (vide + Λ), Λ = 3H²
  [A.dS.2]  caractère causal de 𝓘 : signe(N=g̃^{ab}∂_aΩ∂_bΩ)|_𝓘 = -signe(Λ)
            => Λ>0 : 𝓘 spacelike ; Λ=0 : null ; Λ<0 : timelike. N|_𝓘⁺ = -Λ/3.
            g̃ non dégénérée en 𝓘 => extension conforme lisse (Friedrich 1986).
"""
import sympy as sp
eta,chi,th,ph,H = sp.symbols('eta chi theta phi H', positive=True)
x=[eta,chi,th,ph]; n=4
a=sp.sec(eta)/H                            # η=gd(Ht) sans dim ; a(η)=H^{-1}sec(η)
g=sp.diag(-a**2, a**2, a**2*sp.sin(chi)**2, a**2*sp.sin(chi)**2*sp.sin(th)**2)
gi=g.inv()
Gam=[[[sp.simplify(sum(gi[l,m]*(sp.diff(g[m,i],x[j])+sp.diff(g[m,j],x[i])-sp.diff(g[i,j],x[m]))
      for m in range(n))/2) for j in range(n)] for i in range(n)] for l in range(n)]
def Ric(i,j):
    return sp.simplify(sum(sp.diff(Gam[l][i][j],x[l]) for l in range(n))
        -sum(sp.diff(Gam[l][i][l],x[j]) for l in range(n))
        +sum(Gam[l][i][j]*Gam[m][l][m] for l in range(n) for m in range(n))
        -sum(Gam[l][i][m]*Gam[m][l][j] for l in range(n) for m in range(n)))
R=sp.simplify(sum(gi[i,j]*Ric(i,j) for i in range(n) for j in range(n)))
print("="*70); print("[A.dS.1] de Sitter (tranchage fermé)")
print("   R =",R," (= 12H² = 4Λ)")
print("   R_ab = 3H² g_ab :", all(sp.simplify(Ric(i,i)-3*H**2*g[i,i])==0 for i in range(n)),
      " => Λ = 3H²")
print("="*70); print("[A.dS.2] caractère causal de 𝓘")
Om=sp.cos(eta); gt_ee=-1/H**2
N=sp.simplify((1/gt_ee)*sp.diff(Om,eta)**2)
print("   Ω=cos(η) ; g̃=Ω²g=H^{-2}(-dη²+dΩ₃²) régulière en η=±π/2")
print("   N(η)=g̃^{ηη}(∂_ηΩ)² =",N,"  ;  N|_𝓘⁺ =",sp.simplify(N.subs(eta,sp.pi/2)),"= -Λ/3 < 0")
print("   => normale temporelle => 𝓘⁺ SPACELIKE ; signe(N)|_𝓘 = -signe(Λ)")
print("="*70)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
assert sp.simplify(R - 12*H**2) == 0, "[A.dS.1] R doit valoir 12H^2 = 4Lambda"
assert all(sp.simplify(Ric(i,i) - 3*H**2*g[i,i]) == 0 for i in range(n)), "[A.dS.1] R_ab = 3H^2 g_ab"
assert sp.simplify(N.subs(eta, sp.pi/2) + H**2) == 0, "[A.dS.2] N|scri+ = -H^2 = -Lambda/3 < 0 (spacelike)"
print("EXIT 0 (F1: 3 assertions dS/scri verifiees)")
