#!/usr/bin/env python3
"""var_E4b_poids_general.py -- audit FA-2 (reprise), point E4. La partie « w symbolique » de var_E4 ne termine pas
(> 10 min, powsimp sur Omega^w) ; on la remplace par :
 (1) une formule fermee derivee a la main : avec H = Omega^w h, boxhat u = Omega^2 box u - 2 Omega n.du (ghat = Omega^-2 eta, dim 4),
     Omega^-(w+2) [boxhat_D - m^2 - xi Rhat](Omega^w h) = box_D h - Omega^-2 [m^2 + 4 lambda xi - (lambda/3) w (3-w)] h
                                                     + Omega^-1 2 (w-1) [n^a D_a h + w s h] + O(1)
     (box Omega = 4 s + O(Omega), n.n = -lambda/3 + 2 Omega s + O(Omega^2)) ;
 (2) la verification de cette formule contre le calcul en jets de la bibliotheque pour w = 0, 1/2, 1, 2, 3, 5/2 ;
 (3) l'argument de jauge : invariance du coefficient de (2.17) par H_r -> e^{i e chi} H_r.
"""
import sympy as sp
from fw3_fa2_lib import *
J = Jet('friedrich')
p = Field(*jets3('p')); q = Field(*jets3('q')); J.add_field(p); J.add_field(q)
A = [sp.Symbol(f'A{a}', real=True) for a in idx]
dA = [[sp.Symbol(f'dA{b}_{a}', real=True) for a in idx] for b in idx]
ddA = [[[sp.Symbol(f'ddA{min(cc,b)}{max(cc,b)}_{a}', real=True) for a in idx] for b in idx] for cc in idx]
J.add_A(A, dA, ddA)
h = (p.v + I*q.v)/sp.sqrt(2)
Dh = [J.D(h, a) - I*e*A[a]*h for a in idx]
nDh = sum(nup[a]*Dh[a] for a in idx)
def lib(wv):
    H = W**wv*h
    DH = [J.D(H, a) - I*e*A[a]*H for a in idx]
    def Dhat2(a, b):
        return J.D(DH[b], a) - I*e*A[a]*DH[b] - sum(Gh(cc, a, b)*DH[cc] for cc in idx)
    boxhatH = sum(ghatinv[a, b]*Dhat2(a, b) for a in idx for b in idx)
    expr = sp.expand(W**(-wv-2)*(boxhatH - (m**2 + xi*(4*lam - kap*W**2*Str))*H))
    return laurent(reduce_nn(expr))
allok = True
for wv in (0, R(1, 2), 1, 2, 3, R(5, 2)):
    lv = lib(wv)
    c2 = -(m**2 + 4*lam*xi - lam/3*wv*(3 - wv))*h
    c1 = 2*(wv - 1)*(nDh + wv*s*h)
    ok2 = sp.simplify(sp.expand(lv.get(-2, 0) - c2)) == 0
    ok1 = sp.simplify(sp.expand(reduce_nn(lv.get(-1, 0) - c1))) == 0
    lowest = min(lv)
    allok &= ok2 and ok1 and lowest >= -2
    print(f"w = {wv}: plus basse puissance {lowest} ; Omega^-2 == -(m^2+4 lambda xi-(lambda/3) w(3-w)) h : {ok2} ; Omega^-1 == 2(w-1)(n.Dh + w s h) : {ok1}")
print("formule fermee confirmee pour tous les w testes :", allok)
print("=> Omega^-1 identiquement nul (n.Dh jet independant) <=> w = 1 ; alors Omega^-2 nul <=> m^2 + 4 lambda xi = 2 lambda/3.")
print("   Choisir w racine de (lambda/3) w(3-w) = m^2 + 4 lambda xi (w != 1) retire Omega^-2 mais laisse 2(w-1) n.Dh Omega^-1.")
# (3) jauge : le coefficient Omega^-2 de (2.17) ne depend que de p^2 + q^2 = 2|H_r|^2, invariant par rotation de phase
th = sp.Symbol('theta', real=True)
expr = p.v**2 + q.v**2
rot = {p.v: sp.cos(th)*p.v - sp.sin(th)*q.v, q.v: sp.sin(th)*p.v + sp.cos(th)*q.v}
print("(3) p^2 + q^2 invariant par H_r -> e^{i theta} H_r :", sp.simplify(expr.subs(rot, simultaneous=True) - expr) == 0)
