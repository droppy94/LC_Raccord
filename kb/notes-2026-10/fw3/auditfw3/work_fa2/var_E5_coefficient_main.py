#!/usr/bin/env python3
"""var_E5_coefficient_main.py -- audit FA-2, point E5 : coefficient de Omega^-2 de (2.17) recalcule de facon INDEPENDANTE
du mecanisme de jets du script (pas de classe Jet, pas de derivation symbolique generale).

Principe (ordre dominant seulement) :
  * L̂_ab - (lambda/6) ĝ_ab = (kappa/2)(T̂_ab - (1/3) T̂ ĝ_ab) est O(1) en Omega (T̂_ab O(1), T̂ ĝ = Omega^2 Str Omega^-2 eta O(1)).
  * nablahat_[nu L̂_lambda]rho = d_[nu L̂_lambda]rho - Γ̂ termes ; d L̂^(0) = O(1), Γ̂ = O(Omega^-1).
    Donc le coefficient de Omega^-2 de 2 Omega^-1 nablahat_[nu L̂_lambda]rho est
      C_{rho nu lambda} = 2 x [ -Γ̂ termes antisymetrises ] appliques a L̂^(0), avec Omega Γ̂ = -(delta n + delta n - eta n^.).
  * L̂^(0) : partie O(1) de L̂ avec n.n -> -lambda/3 (3.8 a l'ordre 0).
  * T̂^(0) : (i) partie minimale : D_a H -> n_a H_r ; (ii) partie xi : Ĝ^(0) f + (ĝ box - nabla nabla)^(0) f, avec
      Ĝ^(0) obtenu de (2.3), (2.4) et d d Omega -> s eta (2.14 a l'ordre 0), n.n -> -lambda/3 + 2 Omega s (3.8),
      f = 2 |H|^2 = 2 Omega^2 |H_r|^2.
"""
import sympy as sp
I = sp.I; R = sp.Rational
W = sp.symbols('Omega', positive=True)
n = sp.symbols('n0:4', real=True); s = sp.Symbol('s', real=True)
lam, kap, m, xi = sp.symbols('lambda kappa m xi', real=True)
p, q = sp.symbols('p q', real=True)
eta = sp.diag(-1, 1, 1, 1); idx = range(4)
nup = [sum(eta[r, t]*n[t] for t in idx) for r in idx]
nn = sum(eta[a, b]*n[a]*n[b] for a in idx for b in idx)
Hr2 = (p**2 + q**2)/2                       # |H_r|^2

def red(expr):
    """n.n -> -lambda/3 a l'ordre dominant : elimination de n0^2"""
    gen = n[0]**2 - (n[1]**2 + n[2]**2 + n[3]**2 + lam/3)
    return sp.expand(sp.rem(sp.Poly(sp.expand(expr), n[0]), sp.Poly(gen, n[0])).as_expr())

# ---- (1) Ĝ a l'ordre dominant par (2.3), (2.4) : verification de Ĝ^(0) = -lambda ĝ
ddO = lambda a, b: s*eta[a, b]                 # (2.14) a l'ordre 0 (termes Omega L, Omega S d'ordre superieur)
boxO = sum(eta[a, b]*ddO(a, b) for a in idx for b in idx)
nn38 = -lam/3 + 2*W*s                           # (3.8) sans le terme Omega^2
Rhat = sp.expand(W**2*(6*boxO/W - 12*nn38/W**2))
Rab = lambda a, b: sp.expand(2*ddO(a, b)/W + (boxO/W - 3*nn38/W**2)*eta[a, b])
Ghat = sp.Matrix(4, 4, lambda a, b: sp.expand(Rab(a, b) - R(1, 2)*Rhat*W**-2*eta[a, b]))
print("Rhat a l'ordre dominant :", Rhat, " ; Rhat_ab :", sp.factor(Rab(0, 0)), ",", sp.factor(Rab(1, 1)))
print("Ghat_ab + lambda ghat_ab = 0 a l'ordre Omega^-2 et Omega^-1 :", (Ghat + lam*W**-2*eta).applyfunc(sp.expand) == sp.zeros(4))

# ---- (2) (ĝ box - nabla nabla) f a l'ordre O(1), f = 2 Omega^2 |H_r|^2 (|H_r|^2 traite comme constant a l'ordre dominant :
#      ses derivees sont multipliees par Omega et ne contribuent pas a O(1))
fr = sp.Symbol('f_r', real=True)              # = 2 |H_r|^2
f = W**2*fr
df = [2*W*n[a]*fr for a in idx]
ddf = lambda a, b: 2*n[a]*n[b]*fr + 2*W*ddO(a, b)*fr
Gh = lambda a, b, c: -((1 if a == b else 0)*n[c] + (1 if a == c else 0)*n[b] - eta[b, c]*nup[a])/W
N2 = sp.Matrix(4, 4, lambda a, b: sp.expand(ddf(a, b) - sum(Gh(c, a, b)*df[c] for c in idx)))
boxf = sp.expand(sum(W**2*eta[a, b]*N2[a, b] for a in idx for b in idx))
Timp = sp.Matrix(4, 4, lambda a, b: sp.expand(W**-2*eta[a, b]*boxf - N2[a, b]))
print("(ghat box - nabla nabla) f a l'ordre 0 : composante (0,0) =", sp.factor(Timp[0, 0].coeff(W, 0)), "; (0,1) =", sp.factor(Timp[0, 1].coeff(W, 0)), " (attendu -6 n_a n_b f_r)")
Timp0 = Timp.applyfunc(lambda z: z.coeff(W, 0))

# ---- (3) T̂^(0) complet et L̂^(0)
T0 = sp.zeros(4)
for a in idx:
    for b in idx:
        Tmin = 2*n[a]*n[b]*Hr2 - eta[a, b]*(nn + m**2)*Hr2            # D_a H -> n_a H_r ; ghat (ghat^{cd} D_c H* D_d H + m^2 |H|^2) -> eta (n.n + m^2)|H_r|^2
        Txi = xi*(-lam*eta[a, b]*2*Hr2 + Timp0[a, b].subs(fr, 2*Hr2))   # Ĝ^(0) f = -lambda Omega^-2 eta 2 Omega^2 |H_r|^2
        T0[a, b] = sp.expand(Tmin + Txi)
tr0 = sp.expand(sum(eta[a, b]*T0[a, b] for a in idx for b in idx))    # Str a l'ordre 0 = eta^{ab} T̂^(0)_ab
print("Omega^-2 That a l'ordre 0 (Str^(0)) =", sp.factor(red(tr0)))
L0 = sp.Matrix(4, 4, lambda a, b: sp.expand(kap/2*(T0[a, b] - R(1, 3)*tr0*eta[a, b])))

# ---- (4) coefficient de Omega^-2 de 2 Omega^-1 nablahat_[nu L̂_lambda]rho = 2 x (-Γ̂ termes)_[nu lambda], Omega Γ̂ explicite
def OmGam(a, b, c):   # Omega * Gammahat^a_bc
    return -((1 if a == b else 0)*n[c] + (1 if a == c else 0)*n[b] - eta[b, c]*nup[a])
def gam_term(nu, la, rho):   # -(Omega Γ̂) termes de nablahat_nu L_{la rho}
    return -sum(OmGam(d, nu, la)*L0[d, rho] + OmGam(d, nu, rho)*L0[la, d] for d in idx)
ok = True
for rho in idx:
    for nu in idx:
        for la in range(nu+1, 4):
            C = red(gam_term(nu, la, rho) - gam_term(la, nu, rho))      # 2 Omega^-1 x (1/2)(...) -> facteur 1
            pred = red(kap/3*(m**2 + 4*lam*xi - 2*lam/3)*(p**2 + q**2)*R(1, 2)*(n[nu]*eta[la, rho] - n[la]*eta[nu, rho]))
            if sp.simplify(C - pred) != 0:
                ok = False; print("  ecart composante", (rho, nu, la), sp.factor(C - pred))
print("Coefficient Omega^-2 de (2.17) == (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3)(p^2 + q^2) n_[nu eta_lambda]rho :", ok)
# decomposition de la part en xi : trois origines
ex = (0, 0, 1)
Cx = red(gam_term(0, 1, 0) - gam_term(1, 0, 0))
print("Composante (rho,nu,lambda) = (0,0,1) :", sp.factor(Cx))
print("  part en xi :", sp.factor(Cx.coeff(xi)), " ; attendu (4/3) kappa lambda xi (p^2+q^2) n_[0 eta_1]0 = (2/3) kappa lambda xi (p^2+q^2) n_1 ... signe selon eta_00 = -1")
