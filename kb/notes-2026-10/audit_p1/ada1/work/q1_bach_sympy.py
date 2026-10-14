#!/usr/bin/env python3
# ADA-1, question 1 : tenseur de Bach linearise sur une perturbation TT de Minkowski,
# solutions u_A, u_B de u'' - (2/tau) u' + k^2 u = 0, et (d^2+k^2)^2 u.
# Conventions :
#   eta = diag(-1,1,1,1), coordonnees (tau,x,y,z)
#   Riemann linearise : R_abcd = 1/2 (d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac)
#   Ricci R_bd = eta^{ac} R_abcd, R = eta^{bd} R_bd
#   Weyl (n=4) : C_abcd = R_abcd - 1/2 (g_ac R_bd - g_ad R_bc - g_bc R_ad + g_bd R_ac) + R/6 (g_ac g_bd - g_ad g_bc)
#   Bach linearise sur fond plat : B_ab = d^c d^d C_acbd
import sympy as sp
import itertools

tau, x, y, z = sp.symbols('tau x y z', real=True)
k = sp.symbols('k', positive=True)
X = [tau, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
etainv = eta.inv()

def d(f, a):
    return sp.diff(f, X[a])

def bach_of_h(h):
    """h : Matrix 4x4 symetrique de fonctions des coordonnees. Retourne (B_ab, box^2 h_ab, R_ab, R)."""
    R4 = {}
    for a, b, c, dd in itertools.product(range(4), repeat=4):
        R4[(a, b, c, dd)] = sp.Rational(1, 2) * (d(d(h[a, dd], b), c) + d(d(h[b, c], a), dd)
                                                 - d(d(h[b, dd], a), c) - d(d(h[a, c], b), dd))
    Ric = sp.zeros(4, 4)
    for b, dd in itertools.product(range(4), repeat=2):
        Ric[b, dd] = sum(etainv[a, c] * R4[(a, b, c, dd)] for a in range(4) for c in range(4))
    Rs = sum(etainv[b, dd] * Ric[b, dd] for b in range(4) for dd in range(4))
    C = {}
    for a, b, c, dd in itertools.product(range(4), repeat=4):
        C[(a, b, c, dd)] = (R4[(a, b, c, dd)]
                            - sp.Rational(1, 2) * (eta[a, c] * Ric[b, dd] - eta[a, dd] * Ric[b, c]
                                                   - eta[b, c] * Ric[a, dd] + eta[b, dd] * Ric[a, c])
                            + Rs / 6 * (eta[a, c] * eta[b, dd] - eta[a, dd] * eta[b, c]))
    B = sp.zeros(4, 4)
    for a, b in itertools.product(range(4), repeat=2):
        B[a, b] = sum(etainv[c, e] * etainv[dd, f] * d(d(C[(a, c, b, dd)], e), f)
                      for c in range(4) for dd in range(4) for e in range(4) for f in range(4))
    def box(f):
        return sum(etainv[a, a] * d(d(f, a), a) for a in range(4))
    box2h = sp.zeros(4, 4)
    for a, b in itertools.product(range(4), repeat=2):
        box2h[a, b] = box(box(h[a, b]))
    return sp.simplify(B), sp.simplify(box2h), sp.simplify(Ric), sp.simplify(Rs)

out = []
# --- (a) perturbation de l'enonce : h_yy = -h_zz = u(tau) cos(k x)
u = sp.Function('u')(tau)
h = sp.zeros(4, 4)
h[2, 2] = u * sp.cos(k * x)
h[3, 3] = -u * sp.cos(k * x)
div = [sp.simplify(sum(etainv[b, b] * d(h[a, b], b) for b in range(4))) for a in range(4)]
tr = sp.simplify(sum(etainv[a, a] * h[a, a] for a in range(4)))
out.append("(a) h_yy = -h_zz = u(tau) cos(kx) : divergence d^b h_ab = %s ; trace = %s" % (div, tr))
B, box2h, Ric, Rs = bach_of_h(h)
ratio = sp.simplify(B + sp.Rational(1, 4) * box2h)
boxh = sp.Matrix(4, 4, lambda a, b: sum(etainv[c, c] * d(d(h[a, b], c), c) for c in range(4)))
out.append("    R_ab + (1/2) box h_ab = %s ; R = %s" % (sp.simplify(Ric + sp.Rational(1, 2) * boxh), Rs))
out.append("    B_ab + (1/4) box^2 h_ab = %s  (doit etre la matrice nulle)" % ratio)
out.append("    B_yy = %s" % sp.simplify(B[2, 2]))
out.append("    box^2 h_yy = %s" % sp.factor(box2h[2, 2]))
Dop = lambda f: sp.diff(f, tau, 2) + k**2 * f
out.append("    (d_tau^2+k^2)^2 u * cos(kx) - box^2 h_yy = %s" % sp.simplify(Dop(Dop(u)) * sp.cos(k * x) - box2h[2, 2]))

# --- (b) verification generale sur une onde plane TT : h_ab = e_ab exp(i p.x), p = (w, kx, ky, kz)
w, p1, p2, p3 = sp.symbols('omega p1 p2 p3', real=True)
e = sp.Matrix(4, 4, lambda a, b: sp.Symbol('e%d%d' % (min(a, b), max(a, b)), real=True))
phase = sp.exp(sp.I * (-w * tau + p1 * x + p2 * y + p3 * z))
hp = e * phase
Bp, box2hp, _, _ = bach_of_h(hp)
# conditions TT : p^a e_ab = 0 (4 eq.), eta^{ab} e_ab = 0 (1 eq.) -> 5 contraintes sur 10 composantes
pvec = sp.Matrix([w, p1, p2, p3])  # composantes covariantes p_a = (-w? ) : on utilise p^a = eta^{ab} p_b avec p_b = (-w,p1,p2,p3) de la phase
pcov = sp.Matrix([-w, p1, p2, p3])
pup = etainv * pcov
constraints = [sum(pup[a] * e[a, b] for a in range(4)) for b in range(4)]
constraints.append(sum(etainv[a, a] * e[a, a] for a in range(4)))
sol = sp.solve(constraints, [e[0, 0], e[0, 1], e[0, 2], e[0, 3], e[1, 1]], dict=True)
out.append("(b) onde plane TT generique : solution des contraintes TT = %s" % sol)
p2sq = sp.simplify(sum(etainv[a, a] * pcov[a]**2 for a in range(4)))
diff_mat = (Bp + sp.Rational(1, 4) * box2hp).subs(sol[0])
diff_mat = sp.simplify(diff_mat / phase)
out.append("    (B_ab + (1/4) box^2 h_ab)/phase apres contraintes TT = %s (doit etre nul)" % diff_mat)
out.append("    box^2 h_ab = (p^2)^2 h_ab avec p^2 = %s" % p2sq)

# --- (c) solutions de u'' - (2/tau) u' + k^2 u = 0
ode = sp.Eq(sp.diff(u, tau, 2) - 2 / tau * sp.diff(u, tau) + k**2 * u, 0)
gen = sp.dsolve(ode, u)
out.append("(c) dsolve : %s" % gen)
uA = sp.cos(k * tau) + k * tau * sp.sin(k * tau)
uB = sp.sin(k * tau) - k * tau * sp.cos(k * tau)
for name, uu in [('u_A', uA), ('u_B', uB)]:
    res = sp.simplify(sp.diff(uu, tau, 2) - 2 / tau * sp.diff(uu, tau) + k**2 * uu)
    out.append("    %s = %s ; residu de l'EDO = %s" % (name, uu, res))
    out.append("    (d^2+k^2) %s = %s" % (name, sp.simplify(Dop(uu))))
    out.append("    (d^2+k^2)^2 %s = %s" % (name, sp.simplify(Dop(Dop(uu)))))
W = sp.simplify(uA * sp.diff(uB, tau) - uB * sp.diff(uA, tau))
out.append("    Wronskien W(u_A,u_B) = %s (non nul pour tau != 0 : solutions independantes)" % sp.factor(W))
# forme complexe equivalente
uc = (1 - sp.I * k * tau) * sp.exp(sp.I * k * tau)
out.append("    (1 - i k tau) e^{i k tau} = %s" % sp.simplify(sp.expand(uc, complex=True)))
out.append("    comportement tau -> 0 : u_A -> %s, u_B -> %s" % (sp.series(uA, tau, 0, 4), sp.series(uB, tau, 0, 5)))

# --- (d) question 3 : B_eps = (d^2+k^2)^2 [e^{eps tau} u_A], developpement en eps
eps = sp.symbols('epsilon', positive=True)
ue = sp.exp(eps * tau) * uA
Be = sp.simplify(Dop(Dop(ue)) * sp.exp(-eps * tau))
Be_poly = sp.collect(sp.expand(Be), eps)
out.append("(d) B_eps(tau) e^{-eps tau} = %s" % Be_poly)
for n in range(0, 5):
    out.append("    coefficient de eps^%d : %s" % (n, sp.simplify(Be_poly.coeff(eps, n))))

txt = "\n".join(out)
print(txt)
open('/home/claude/audit_p1/ada1/work/q1_bach_sympy.out', 'w').write(txt + "\n")
