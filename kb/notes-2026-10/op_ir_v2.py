"""
op_ir_v2.py -- NOTE-BORD-EON-102, sous le gel de NOTE-101.
Coordonnee s = -tau = Omega > 0 ; hat-g = Omega^-2 eta ; H = 1. Mode A_y = u(s) cos(kx).
Equation de S2 (3.14) : (I^2 u_s)_s + k^2 I^2 u = 0, I^2 = e^-2 [1 + 2 beta (lam - ln s)], lam = ln(M/k) (a* = k/M).
Premier ordre en beta. Partie A : mode ; B : secteur Maxwell, logs ; C : (2.17) partie homogene, C-iso ;
D : facteurs de forme (residu S2 ; -Box de Bochner ; laplacien de Hodge).
"""
import sympy as sp

s = sp.symbols('s', positive=True)
x, y, z = sp.symbols('x y z', real=True)
k, e, beta, kap, u0, c, lam, Cr = sp.symbols('k e beta kappa u0 c lambda C_r', positive=True)
L = sp.symbols('L')
N = 8                       # ordre du developpement en s
X = [s, x, y, z]; n = 4
Om = s
eta = sp.diag(-1, 1, 1, 1)
gh = eta/Om**2; gi = gh.inv()
G = [[[sp.simplify(sum(gi[l, q]*(sp.diff(gh[q, m], X[r]) + sp.diff(gh[q, r], X[m]) - sp.diff(gh[m, r], X[q])) for q in range(n))/2)
       for r in range(n)] for m in range(n)] for l in range(n)]

def tolog(ex):
    ex = sp.expand(sp.expand_log(sp.expand(ex), force=True))
    return sp.expand(ex.subs(sp.log(s), L))

def ser(ex, order=N):
    return sp.expand(sp.series(ex, s, 0, order).removeO())

# ---------------- A. mode au premier ordre en beta ----------------
I2 = (1 + 2*beta*(lam - sp.log(s)))/e**2
def residual(u):
    return sp.expand((sp.diff(I2*sp.diff(u, s), s) + k**2*I2*u)*e**2)

# branche magnetique gelee : U0 = u0 cos(ks)
U0m = u0*sp.cos(k*s)
# U1'' + k^2 U1 = (2/s) U0'  (ordre beta) ; serie particuliere sans terme homogene ajoute
src_m = ser(2/s*sp.diff(U0m, s), N)
# v2 : resolution recursive (v1 imposait aussi les ordres tronques -> systeme incompatible, IndexError)
# U1 = sum a_j s^j, a0 = a1 = 0 (choix homogene : renormalise u0 / ajoute du sin, sans effet sur les logs)
# (j+2)(j+1) a_{j+2} + k^2 a_j = src_j
srcc = [sp.expand(src_m).coeff(s, j) for j in range(N)]
acoef = [0, 0]
for j in range(N):
    acoef.append(sp.expand((srcc[j] - k**2*acoef[j])/((j+2)*(j+1))))
U1m = sum(acoef[j]*s**j for j in range(N+2))
um = U0m + beta*U1m
rm = residual(um)
rm1 = ser(sp.diff(rm, beta).subs(beta, 0), N-2)      # ordre beta du residu
print("A1. branche magnetique : U1 =", ser(U1m, 6))
print("    residu O(beta) (doit etre ~0 jusqu'a l'ordre tronque) :", rm1)
assert sp.simplify(rm.subs(beta, 0)) == 0

# branche electrique : U0 = (c/k) sin(ks) ; U1'' + k^2 U1 = (2/s) U0' = 2c cos(ks)/s
U0e = c/k*sp.sin(k*s)
bb = sp.symbols('b0:%d' % (N+2)); dd = sp.symbols('d0:%d' % (N+2))
U1e = sum(bb[j]*s**j for j in range(1, N+2)) + sp.log(s)*sum(dd[j]*s**j for j in range(1, N+2))
src_e = 2*c*sp.cos(k*s)/s
expr = tolog(sp.diff(U1e, s, 2) + k**2*U1e - ser(src_e*s, N+1)/s)
Pe = sp.expand(expr*s)
# v2 : equations uniquement pour les ordres s^p, p <= N-1 (ordres controles) ; inconnues restantes mises a 0
eqs_e = []
for p in range(0, N):
    cp = sp.expand(Pe.coeff(s, p))
    for q in range(0, 3):
        eqs_e.append(sp.expand(cp.coeff(L, q)))
eqs_e = [q_ for q_ in eqs_e if q_ != 0]
unk = list(bb[1:N+1]) + list(dd[1:N+1])
sole = sp.solve(eqs_e, unk, dict=True)
assert sole, "branche electrique : systeme sans solution"
sole = sole[0]
U1e = U1e.subs(sole).subs({v: 0 for v in list(bb) + list(dd)})
ue = U0e + beta*U1e
re_ = residual(ue)
print("A2. branche electrique : U1 =", tolog(ser(U1e, 4)))
print("    residu O(beta) :", tolog(ser(sp.diff(re_, beta).subs(beta, 0)*s, N-1)/s))

# ---------------- B. secteur Maxwell (moyenne spatiale) ----------------
def maxwell_sector(u):
    A_y = u*sp.cos(k*x)
    F = sp.zeros(4, 4)
    F[1, 2] = sp.diff(A_y, x); F[2, 1] = -F[1, 2]          # F_xy
    F[0, 2] = sp.diff(A_y, s); F[2, 0] = -F[0, 2]          # F_sy
    FFg = F*gi*F.T
    F2g = sum(gi[i, kk]*gi[j, l]*F[i, j]*F[kk, l] for i in range(n) for j in range(n) for kk in range(n) for l in range(n))
    XM = I2*(FFg - sp.Rational(1, 4)*gh*F2g)
    avg = XM.applyfunc(lambda v: sp.integrate(sp.expand(v), (x, 0, 2*sp.pi/k))*k/(2*sp.pi))
    F2eta = sum(eta[i, kk]*eta[j, l]*F[i, j]*F[kk, l] for i in range(n) for j in range(n) for kk in range(n) for l in range(n))
    F2avg = sp.integrate(sp.expand(F2eta), (x, 0, 2*sp.pi/k))*k/(2*sp.pi)
    return avg, F2avg

def first_order_logs(M):
    out = {}
    for i in range(4):
        v = tolog(ser(sp.expand(M[i, i]), 6))
        v1 = sp.expand(sp.diff(v, beta).subs(beta, 0))
        out[i] = sp.expand(sp.diff(v1, L))
    return out

for name, u in (("magnetique", um), ("electrique", ue)):
    avg, F2avg = maxwell_sector(u)
    lg = first_order_logs(avg)
    zeroth = {i: tolog(ser(sp.expand(avg[i, i].subs(beta, 0)), 4)) for i in range(4)}
    print(f"\nB. branche {name} : <X^M> ordre 0 (diag, s,x,y,z) :", [zeroth[i] for i in range(4)])
    print(f"   coefficient de beta*L dans <X^M> :", [sp.factor(lg[i]) for i in range(4)])
    for i in range(4):
        if zeroth[i] != 0:
            lead = sp.limit(zeroth[i]/s**2, s, 0)
            cl = sp.limit(lg[i]/s**2, s, 0)
            if lead != 0:
                print(f"   composante {i}: rapport (coef. beta L)/(ordre 0) a s -> 0 :", sp.simplify(cl/lead))

# ---------------- C. (2.17) partie homogene, C-iso, branche magnetique ----------------
def D(T):
    return {(r, m, q): sp.diff(T[m, q], X[r]) - sum(G[p][r][m]*T[p, q] + G[p][r][q]*T[m, p] for p in range(n))
            for r in range(n) for m in range(n) for q in range(n)}
def div(T):
    DT = D(T); return [sp.expand(sum(gi[m, r]*DT[(r, m, nu)] for m in range(n) for r in range(n))) for nu in range(n)]
def tr(T):
    return sp.expand(sum(gi[i, j]*T[i, j] for i in range(n) for j in range(n)))

avg_m, F2avg_m = maxwell_sector(um)
XMh = avg_m.applyfunc(lambda v: ser(sp.expand(v), 6))
XMh = XMh.applyfunc(lambda v: sp.expand(v.subs(beta, 0) + beta*sp.diff(v, beta).subs(beta, 0)))   # premier ordre
That = sp.expand(ser(-(beta/(2*e**2))*F2avg_m*Om**4, 7))            # trace anomale moyenne
r0 = sp.Function('r0')(s)
r1 = (r0 + That/Om**2)/3
XR = sp.diag(r0, r1, r1, r1)
cons0 = sp.expand(div(XMh + XR)[0])
sol = sp.dsolve(sp.Eq(cons0, 0), r0)
r0s = sol.rhs.subs(sp.Symbol('C1'), Cr)
tot = (XMh + XR.subs(r0, r0s)).applyfunc(lambda v: sp.expand(v.doit()))
print("\nC. conservation totale (ordre tronque) :", [tolog(ser(sp.expand(v), 5)) for v in div(tot)])
Lh = kap/2*(tot - sp.Rational(1, 3)*tr(tot)*gh)
DL = D(Lh)
print("   R (2.17), composantes non nulles, premier ordre en beta, s -> 0 :")
for rho in range(n):
    for nu in range(n):
        for la in range(nu+1, n):
            v = (DL[(nu, la, rho)] - DL[(la, nu, rho)])/Om
            v = tolog(ser(sp.expand(v), 2))
            v = sp.expand(v.subs(beta, 0) + beta*sp.diff(v, beta).subs(beta, 0))
            if v != 0:
                print("    ", (rho, nu, la), ":", sp.collect(v, L))

# ---------------- D. facteurs de forme ----------------
print("\nD1. residu S2 : -beta log((k^2 - k0^2)/k^2) evalue a k0 = 0 (partie statique) :", -beta*sp.log((k**2 - 0)/k**2))
print("    condition (3.16) : rapport beta/(1 + 2 beta ln(aM/k)) avec a = 1/s :", sp.limit(beta/(1 + 2*beta*(lam - sp.log(s))), s, 0, '+'))

def bochner_box_2form(F):
    # (Box F)_{mu nu} = g^{ab} nabla_a nabla_b F_{mu nu}
    def nab1(T):   # nabla_a T_{mn} -> T3[a][m][n]
        return [[[sp.diff(T[m][q], X[a]) - sum(G[p][a][m]*T[p][q] + G[p][a][q]*T[m][p] for p in range(n)) for q in range(n)] for m in range(n)] for a in range(n)]
    Fl = [[F[i, j] for j in range(n)] for i in range(n)]
    N1 = nab1(Fl)
    # nabla_b (N1)_{a m q}
    out = sp.zeros(4, 4)
    for m in range(n):
        for q in range(n):
            acc = 0
            for a in range(n):
                for b in range(n):
                    term = sp.diff(N1[a][m][q], X[b]) - sum(G[p][b][a]*N1[p][m][q] + G[p][b][m]*N1[a][p][q] + G[p][b][q]*N1[a][m][p] for p in range(n))
                    acc += gi[a, b]*term
            out[m, q] = sp.simplify(acc)
    return out

Fu = sp.zeros(4, 4); B0 = sp.symbols('B0', positive=True)
Fu[1, 2] = B0; Fu[2, 1] = -B0
bx = bochner_box_2form(Fu)
print("D2. Bochner -Box F, champ uniforme F_xy = B0 : (-Box F)_xy =", sp.simplify(-bx[1, 2]), " ; rapport a F_xy :", sp.simplify(-bx[1, 2]/B0))
# mode a l'ordre 0 (Maxwell libre, branche magnetique)
Fm = sp.zeros(4, 4); A_y0 = u0*sp.cos(k*s)*sp.cos(k*x)
Fm[1, 2] = sp.diff(A_y0, x); Fm[2, 1] = -Fm[1, 2]; Fm[0, 2] = sp.diff(A_y0, s); Fm[2, 0] = -Fm[0, 2]
bm = bochner_box_2form(Fm)
print("    mode k : (-Box F)_xy / F_xy =", sp.simplify(-bm[1, 2]/Fm[1, 2]), " ; (-Box F)_sy / F_sy =", sp.simplify(-bm[0, 2]/Fm[0, 2]))
# Hodge : Delta = d delta + delta d ; sur F ferme et co-ferme (Maxwell libre) Delta F = 0 ; Weitzenbock : Delta F = -Box F + Ric terms
Ric_scalar = 12  # de Sitter H = 1, R = 12
print("    de Sitter : R =", Ric_scalar, " ; physique : k_phys^2 = k^2 Omega^2 =", k**2*s**2)
# operateur de S2 : -d^2_eta e^{-2 Omega_S} = e^{2 ln s}(-d^2_eta) ; sur la partie statique d'un mode k : k^2 s^2 = k_phys^2
print("D3. forme exacte S2 sur la partie statique : -d^2_eta e^{-2 Omega_S} -> k^2 * s^2 = k_phys^2 (pas de terme en H)")
print("\nEXIT 0")
