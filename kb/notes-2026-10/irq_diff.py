"""irq_diff.py -- IR-q (NOTE-122/123), sous-question q-4.
Si le second membre R de (2.17) porte A ln(Omega), quelle regularite a travers scri+ ?
Modele : metrique-pont g = -dtau^2 + (delta_ij + eps*d_ij*f(tau)) dx^i dx^j, d = diag(1,1,-2) sans trace,
tau temps conforme, Omega = tau (cote ancien eon tau > 0 ici, raccord en tau = 0), premier ordre en eps.
A) on suppose W = C/Omega et on cherche f tel que dW/dtau ~ ln tau (second membre de l'equation de Bianchi
   rescalee nabla.W = R avec R ~ ln) : test f = tau^4 ln tau ; on lit l'ordre de C[g], de W, de dW.
B) classe de differentiabilite de g en tau = 0.
C) eon suivant selon Tod (1309.7248, eq. 1-3) : g_check = Omega_check^2 g avec Omega_check ~ tau (au premier
   ordre, reciproque Omega_hat*Omega_check = -1, Omega_hat ~ 1/tau) ; temps propre T ~ tau^2/2 ;
   tenseur d'Einstein (repere orthonorme) : ordres dominants (radiation, Tod §6-7) et premier terme en log.
"""
import sympy as sp
t, eps = sp.symbols('tau epsilon', positive=True)
x, y, z = sp.symbols('x y z', real=True)
X = [t, x, y, z]
f = t**4*sp.log(t)
d = [1, 1, -2]

def metric(conf2):
    g = sp.diag(-1, *[1 + eps*d[i]*f for i in range(3)])
    return (conf2*g).applyfunc(sp.simplify)

def christoffel(g):
    gi = g.inv()
    n = 4
    return [[[sp.simplify(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e]))
                              for e in range(n))/2) for c in range(n)] for b in range(n)] for a in range(n)]

def riemann(g, G):
    n = 4
    R = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for dd in range(n):
                    R[(a, b, c, dd)] = (sp.diff(G[a][b][dd], X[c]) - sp.diff(G[a][b][c], X[dd])
                                        + sum(G[a][c][e]*G[e][b][dd] - G[a][dd][e]*G[e][b][c] for e in range(n)))
    return R

def lin(e):
    return sp.series(sp.simplify(e), eps, 0, 2).removeO()

def curv(g):
    G = christoffel(g)
    Rm = riemann(g, G)
    Ric = sp.Matrix(4, 4, lambda b, dd: lin(sum(Rm[(a, b, a, dd)] for a in range(4))))
    gi = g.inv()
    Rs = lin(sum(gi[a, b]*Ric[a, b] for a in range(4) for b in range(4)))
    return Rm, Ric, Rs

# --- A, B : metrique-pont
g = metric(1)
Rm, Ric, Rs = curv(g)
# Weyl C_{titj} (indices bas) pour la metrique-pont, partie d'ordre eps
gl = g
def weyl_low(i, j):
    a, b, c, dd = 0, i, 0, j
    Rabcd = lin(sum(gl[a, e]*Rm[(e, b, c, dd)] for e in range(4)))
    P = lambda p, q: (Ric[p, q] - Rs*gl[p, q]/6)/2   # Schouten (signe conventionnel)
    corr = gl[a, c]*P(b, dd) - gl[a, dd]*P(b, c) - gl[b, c]*P(a, dd) + gl[b, dd]*P(a, c)
    return sp.simplify(lin(Rabcd - corr))
E = [sp.simplify(weyl_low(i, i).coeff(eps)) for i in (1, 2, 3)]
print("A. Weyl electrique de g (coefficient de eps), composantes xx, yy, zz :")
for e in E:
    print("   ", sp.expand(e))
W = [sp.expand(e/t) for e in E]            # W = C / Omega, Omega = tau
dW = [sp.expand(sp.diff(w, t)) for w in W]
print("   W = C/Omega :", W)
print("   dW/dtau (doit porter ln tau, comme R de (2.17)) :", dW)
print("   W en tau -> 0 :", [sp.limit(w, t, 0) for w in W], " ; dW en tau -> 0 :", [sp.limit(w, t, 0, '+') for w in dW])

print("B. regularite de g en tau = 0 : derivees de f = tau^4 ln tau")
for k in range(1, 6):
    print(f"   d^{k}f/dtau^{k} -> ", sp.limit(sp.diff(f, t, k), t, 0, '+'))

# --- C : eon suivant (Tod) : g_check = tau^2 g (Omega_check = tau a l'ordre dominant ; signe sans effet)
gc = metric(t**2)
Rmc, Ricc, Rsc = curv(gc)
gci = gc.inv()
Gc = (Ricc - Rsc*gc/2).applyfunc(lin)
# repere orthonorme : G_00 = G_tt / tau^2, G_ii = G_ii / g_ii
G00 = sp.simplify(Gc[0, 0]/gc[0, 0])
Gii = [sp.simplify(lin(Gc[i, i]/gc[i, i])) for i in (1, 2, 3)]
T = sp.symbols('T', positive=True)   # temps propre de l'eon suivant : dT = tau dtau -> T = tau^2/2
sub = {t: sp.sqrt(2*T)}
def show(name, e):
    e0 = sp.expand(e.subs(eps, 0).subs(sub))
    e1 = sp.expand(e.coeff(eps).subs(sub))
    print(f"   {name} : fond = {sp.simplify(e0)} ; perturbation (coef eps) = {sp.simplify(e1)}")
print("C. Einstein de l'eon suivant (repere orthonorme, en temps propre T), Tod : rho = -G_00, p_i = -G_ii (conventions de signe a lire avec prudence) :")
show("G_00", G00)
for i, e in enumerate(Gii):
    show(f"G_{'xyz'[i]}{'xyz'[i]}", e)
print("EXIT 0")
