#!/usr/bin/env python3
"""var_E4_poids_conforme.py -- audit FA-2, point E4 : un poids conforme w != 1 pour H (H = Omega^w H_r) peut-il
retirer le terme Omega^-2 de l'equation de Higgs rescalee sans en creer d'autre ?
On calcule Omega^-(w+2) [ boxhat_D (Omega^w H_r) - (m^2 + xi Rhat) Omega^w H_r ] avec Rhat = 4 lambda - kappa Omega^2 Str,
d d Omega par (2.14), n.n par (3.8), et on lit les coefficients de Omega^-2 et Omega^-1.
Aussi : jauge singuliere A -> A + c n/Omega (chi = c ln Omega) : effet sur l'equation rescalee.
"""
import sympy as sp
from fw3_fa2_lib import *
w = sp.Symbol('w', real=True)
c = sp.Symbol('c', real=True)

J = Jet('friedrich')
p = Field(*jets3('p')); q = Field(*jets3('q')); J.add_field(p); J.add_field(q)
A = [sp.Symbol(f'A{a}', real=True) for a in idx]
dA = [[sp.Symbol(f'dA{b}_{a}', real=True) for a in idx] for b in idx]
ddA = [[[sp.Symbol(f'ddA{min(cc,b)}{max(cc,b)}_{a}', real=True) for a in idx] for b in idx] for cc in idx]
J.add_A(A, dA, ddA)
Hr = (p.v + I*q.v)/sp.sqrt(2)

def higgs_rescaled(wv, Ashift=None):
    Av = [A[a] + (Ashift[a] if Ashift else 0) for a in idx]
    H = W**wv*Hr
    DH = [J.D(H, a) - I*e*Av[a]*H for a in idx]
    def Dhat2(a, b):
        return J.D(DH[b], a) - I*e*Av[a]*DH[b] - sum(Gh(cc, a, b)*DH[cc] for cc in idx)
    boxhatH = sum(ghatinv[a, b]*Dhat2(a, b) for a in idx for b in idx)
    Rhat_sub = 4*lam - kap*W**2*Str
    expr = sp.expand(W**(-wv-2)*(boxhatH - (m**2 + xi*Rhat_sub)*H))
    return reduce_nn(expr)

for wv in (1, 2, 0, sp.Rational(1, 2)):
    ex = higgs_rescaled(wv)
    lv = laurent(ex)
    print(f"\nw = {wv} : puissances de Omega presentes : {sorted(lv)}")
    for k in (-2, -1):
        if k in lv: print(f"   coefficient Omega^{k} : {sp.factor(sp.collect(lv[k], [p.v, q.v]))}")
# poids symbolique : coefficient de Omega^-1 et Omega^-2 en fonction de w (sans reduction, W^w non polynomial : on factorise a la main)
H = W**w*Hr
DH = [J.D(H, a) - I*e*A[a]*H for a in idx]
def Dhat2(a, b):
    return J.D(DH[b], a) - I*e*A[a]*DH[b] - sum(Gh(cc, a, b)*DH[cc] for cc in idx)
boxhatH = sum(ghatinv[a, b]*Dhat2(a, b) for a in idx for b in idx)
expr = sp.expand(sp.powsimp(sp.expand(W**(-w-2)*(boxhatH - (m**2 + 4*lam*xi)*H)), force=True))
expr = reduce_nn(expr)
lv = laurent(expr)
print("\nw symbolique : coefficient Omega^-1 =", sp.factor(lv.get(-1, 0)))
print("w symbolique : coefficient Omega^-2 =", sp.factor(sp.collect(lv.get(-2, 0), [p.v, q.v])))
# jauge singuliere : A -> A + c n_a/Omega
ex = higgs_rescaled(1, Ashift=[c*n[a]/W for a in idx])
lv = laurent(ex)
print("\njauge singuliere chi = c ln Omega (w = 1) : puissances presentes :", sorted(lv), "; coefficient Omega^-2 :", sp.factor(lv.get(-2, 0)), "; coefficient Omega^-1 :", sp.factor(lv.get(-1, 0)))
