#!/usr/bin/env python3
"""Q1 : separation de points pour un mode, structures de phase P2 et P3.
T_{mu nu} = d_mu phi d_nu phi - 1/2 g (d phi)^2 - (1/6)(d_mu d_nu - g box) phi^2
Point-splitting bilineaire :
  d_mu phi d_nu phi  -> 1/2 (d_mu d'_nu + d_nu d'_mu) w
  (d phi)^2          -> g^{ab} d_a d'_b w
  phi^2              -> w ;  d_mu d_nu phi^2 -> (d_mu + d'_mu)(d_nu + d'_nu) w
puis coincidence x' -> x.
"""
import sympy as sp

eta, etap = sp.symbols('eta etap', real=True)
x = sp.symbols('x1:4', real=True)
xp = sp.symbols('xp1:4', real=True)
k = sp.symbols('k', positive=True)
kv = sp.symbols('k1:4', real=True)
X = [eta] + list(x)
Xp = [etap] + list(xp)
g = sp.diag(-1, 1, 1, 1)
ginv = g.inv()

def tenseur(w):
    """applique D_{mu nu} a w(x,x') et prend la coincidence."""
    T = sp.zeros(4, 4)
    d = lambda f, mu: sp.diff(f, X[mu])
    dp = lambda f, mu: sp.diff(f, Xp[mu])
    # (d phi)^2 -> g^{ab} d_a d'_b w
    kin = sum(ginv[a, b] * d(dp(w, b), a) for a in range(4) for b in range(4))
    # box phi^2 -> g^{ab}(d_a + d'_a)(d_b + d'_b) w
    def D(f, mu):
        return d(f, mu) + dp(f, mu)
    box2 = sum(ginv[a, b] * D(D(w, b), a) for a in range(4) for b in range(4))
    for mu in range(4):
        for nu in range(4):
            t = sp.Rational(1, 2) * (d(dp(w, nu), mu) + d(dp(w, mu), nu))
            t -= sp.Rational(1, 2) * g[mu, nu] * kin
            t -= sp.Rational(1, 6) * (D(D(w, nu), mu) - g[mu, nu] * box2)
            T[mu, nu] = t
    sub = {etap: eta, xp[0]: x[0], xp[1]: x[1], xp[2]: x[2]}
    T = T.subs(sub)
    return sp.simplify(T)

kdotx = sum(kv[i] * (x[i] - xp[i]) for i in range(3))
norm = 1 / (2 * k * (2 * sp.pi) ** 3)
# contrainte k^2 = |kvec|^2 appliquee a la fin
ksq = {kv[0]**2: k**2 - kv[1]**2 - kv[2]**2}

def report(nom, w):
    T = tenseur(w)
    T = T.applyfunc(lambda e: sp.simplify(sp.expand(e).subs(ksq)))
    trace = sp.simplify(sum(ginv[a, b] * T[a, b] for a in range(4) for b in range(4)).subs(ksq))
    print('=' * 70)
    print(nom)
    print('T_00 =', sp.simplify(T[0, 0]))
    print('T_0i =', [sp.simplify(T[0, i]) for i in (1, 2, 3)])
    print('T_ij =')
    sp.pprint(T[1:, 1:])
    print('trace g^{mu nu} T_{mu nu} =', trace)
    return T

# P2 : |beta|^2 e^{+ik(eta-eta')}
b2 = sp.symbols('b2', positive=True)
w_P2 = b2 * sp.exp(sp.I * k * (eta - etap)) * sp.exp(sp.I * kdotx) * norm
T_P2 = report('P2 : |beta|^2 e^{+ik(eta-eta\')}', w_P2)
# conjugue
w_P2c = b2 * sp.exp(-sp.I * k * (eta - etap)) * sp.exp(sp.I * kdotx) * norm
T_P2c = report('P2 conj : |beta|^2 e^{-ik(eta-eta\')}', w_P2c)

# P3 : alpha beta* e^{-ik(eta+eta')}
ab = sp.symbols('ab')  # alpha beta* (complexe)
w_P3 = ab * sp.exp(-sp.I * k * (eta + etap)) * sp.exp(sp.I * kdotx) * norm
T_P3 = report('P3 : alpha beta* e^{-ik(eta+eta\')}', w_P3)

# decomposition T_ij = A k_i k_j + B delta_ij pour P3
Tij = T_P3[1:, 1:]
A, B = sp.symbols('A B')
eqs = []
for i in range(3):
    for j in range(3):
        eqs.append(sp.expand((Tij[i, j] - (A * kv[i] * kv[j] + B * (1 if i == j else 0))).subs(ksq)))
sol = sp.solve([eqs[1], eqs[4]], [A, B], dict=True)  # T_12 et T_22
print('residus de toutes les composantes avec cette solution :',
      [sp.simplify(e.subs(sol[0]).subs(ksq)) for e in eqs])
print('=' * 70)
print('P3 : decomposition T_ij = A k_i k_j + B delta_ij')
print('solution :', sol)
Asol = sp.simplify(sol[0][A]); Bsol = sp.simplify(sol[0][B])
# verification
chk = sp.simplify((Tij - (Asol * sp.Matrix(kv) * sp.Matrix(kv).T + Bsol * sp.eye(3))).applyfunc(lambda e: sp.expand(e).subs(ksq)))
print('verification residu :', chk)
# partie isotrope (moyenne angulaire : <k_i k_j> = k^2/3 delta_ij) et partie sans trace
iso = sp.simplify(Asol * k**2 / 3 + Bsol)
print('partie isotrope (moyenne angulaire) : (A k^2/3 + B) delta_ij, coefficient =', iso)
print('partie sans trace : A (k_i k_j - k^2/3 delta_ij), A =', Asol)
print('trace spatiale T_ii =', sp.simplify(Asol * k**2 + 3 * Bsol))
print('T_00 (P3) =', sp.simplify(T_P3[0, 0]))
print('trace -T_00 + T_ii =', sp.simplify(-T_P3[0, 0] + Asol * k**2 + 3 * Bsol))

# Verification de la forme ab-bb, forme generale : somme des quatre termes pour |beta|^2 et ab
print('=' * 70)
print('Controle : somme P2 + P2conj (terme |beta|^2 complet)')
Tsum = (T_P2 + T_P2c).applyfunc(lambda e: sp.simplify(sp.expand(e).subs(ksq)))
sp.pprint(Tsum)
