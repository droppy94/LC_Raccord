#!/usr/bin/env python3
"""var_E1_conventions.py -- audit FA-2 (reprise), point E1. Verification INDEPENDANTE (sans le code de la note) des
relations conformes, a partir d'une fonction Omega(x) generique et de la metrique ghat = Omega^-2 eta en dimension 4.
 (1) Christoffel de ghat ; (2) Rhat_ab et Rhat (formules (2.3)-(2.4) de la consigne) ; (3) de Sitter : signe de la
 convention d'Einstein de Friedrich ; (4) en DEFINISSANT kappa That par Einstein (That := (Ghat + lambda ghat)/kappa) et
 s := (1/4) box Omega (g plat, L = 0) : verification identique de (2.14), (3.8) et (2.15), cette derniere avec un facteur
 Omega^k devant nablahat_c That (trace physique ghat^{ab} That_ab), k = -1 et k = +1 testes.
"""
import sympy as sp
x = sp.symbols('x0:4', real=True)
lam, kap = sp.symbols('lambda kappa', positive=True)
O = sp.Function('Omega')(*x)
eta = sp.diag(-1, 1, 1, 1); idx = range(4)
g = O**-2*eta; gi = O**2*eta
def Gam(a, b, c):
    return sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b]) - sp.diff(g[b, c], x[d])) for d in idx)/2)
G = [[[Gam(a, b, c) for c in idx] for b in idx] for a in idx]
n = [sp.diff(O, x[a]) for a in idx]; nup = [sum(eta[a, b]*n[b] for b in idx) for a in idx]
okG = all(sp.simplify(G[a][b][c] + ((1 if a == b else 0)*n[c] + (1 if a == c else 0)*n[b] - eta[b, c]*nup[a])/O) == 0
          for a in idx for b in idx for c in idx)
print("(1) Gammahat^a_bc = -(delta^a_b n_c + delta^a_c n_b - eta_bc n^a)/Omega :", okG)
# Ricci : R_bd = d_a G^a_bd - d_d G^a_ba + G^a_ae G^e_bd - G^a_de G^e_ba  (convention usuelle, sphere/dS de courbure scalaire > 0)
def Ric(b, d):
    return sp.simplify(sum(sp.diff(G[a][b][d], x[a]) - sp.diff(G[a][b][a], x[d]) for a in idx)
                       + sum(G[a][a][e]*G[e][b][d] - G[a][d][e]*G[e][b][a] for a in idx for e in idx))
Rab = sp.Matrix(4, 4, lambda b, d: Ric(b, d))
ddO = sp.Matrix(4, 4, lambda a, b: sp.diff(O, x[a], x[b]))
boxO = sum(eta[a, b]*ddO[a, b] for a in idx for b in idx)
nn = sum(eta[a, b]*n[a]*n[b] for a in idx for b in idx)
form = 2*ddO/O + (boxO/O - 3*nn/O**2)*eta
print("(2) Rhat_ab = 2 Omega^-1 dd Omega + (Omega^-1 box Omega - 3 Omega^-2 |dOmega|^2) eta :", sp.simplify(Rab - form) == sp.zeros(4))
Rs = sp.simplify(sum(gi[a, b]*Rab[a, b] for a in idx for b in idx))
print("    Rhat = Omega^2 (6 Omega^-1 box Omega - 12 Omega^-2 |dOmega|^2) :", sp.simplify(Rs - O**2*(6*boxO/O - 12*nn/O**2)) == 0)
# (3) de Sitter : Omega = -H t (t < 0), H^2 = lambda/3
H = sp.sqrt(lam/3); t = x[0]
sub = {O: -H*t}
Gh = (Rab - Rs*g/2 + lam*g)
Gh_dS = sp.simplify(Gh.subs(O, -H*t).doit())
print("(3) de Sitter Omega = -sqrt(lambda/3) t : Rhat_ab - Rhat ghat/2 + lambda ghat = 0 (That = 0) :", Gh_dS == sp.zeros(4),
      "; Rhat =", sp.simplify(Rs.subs(O, -H*t).doit()), " ; |dOmega|^2 =", sp.simplify(nn.subs(O, -H*t).doit()), "(= -lambda/3 : scri du genre espace)")
# (4) That defini par Einstein ; s = box Omega / 4 (g plat : L = 0, (2.14) trace)
That = (Gh)/kap
trT = sp.simplify(sum(gi[a, b]*That[a, b] for a in idx for b in idx))   # trace physique
print("    -Rhat + 4 lambda = kappa That (trace) :", sp.simplify(-Rs + 4*lam - kap*trT) == 0)
Tstar = That - trT*g/4
s = boxO/4
ok214 = sp.simplify(ddO - (s*eta + kap/2*O*Tstar)) == sp.zeros(4)
print("(4a) (2.14) dd Omega = s eta - Omega L + (kappa/2) Omega T*  (L = 0) : identite :", ok214)
ok38 = sp.simplify(nn - (-lam/3 + 2*O*s + kap/12*trT)) == 0
print("(4b) (3.8) |dOmega|^2 = -lambda/3 + 2 Omega s + (kappa/12) That (trace physique = Omega^2 Str) : identite :", ok38)
for k in (-1, 1):
    res = [sp.simplify(sp.diff(s, x[c]) - (kap/2*sum(nup[b]*Tstar[b, c] for b in idx) - kap/24*O**k*sp.diff(trT, x[c]))) for c in idx]
    print(f"(4c) (2.15) d_c s = (kappa/2) n^b T*_bc - (kappa/24) Omega^({k}) d_c That (L = 0) : identite :", all(r == 0 for r in res))
