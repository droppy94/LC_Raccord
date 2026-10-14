"""audit_db_indep.py -- controles independants (auditeur D-b).
Methodes volontairement differentes de op_ir_v2.py :
 (a) Christoffels par formule conforme fermee, comparee a la formule metrique ;
 (b) mode : equation exacte de S2 (3.14) avec I^2 exact, developpement en beta fait par sympy.series,
     et solution de Frobenius / resommee (I^2 u_s = const) pour juger l'uniformite ;
 (c) X^M en composantes mixtes, moyenne par orthogonalite (sin^2, cos^2 -> 1/2) faite a la main ;
 (d) conservation resolue a la main (ODE lineaire en r0), constante C_r conservee ;
 (e) R recalcule avec une derivee covariante ecrite a partir de la formule conforme ;
 (f) Bochner via Weitzenbock : -Box F = Delta_Hodge F - (Ric terms), Delta_Hodge par d et delta (etoile de Hodge),
     sans Christoffels.
"""
import sympy as sp, itertools as it

s = sp.symbols('s', positive=True)
x, y, z = sp.symbols('x y z', real=True)
k, e, beta, kap, u0, c, lam, Cr, B0 = sp.symbols('k e beta kappa u0 c lambda C_r B0', positive=True)
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1)
g = eta/s**2; gi = g.inv()

# ---------- (a) Christoffels ----------
# g = e^{2w} eta, w = -ln s : Gamma^a_bc = d_b w delta^a_c + d_c w delta^a_b - eta_bc eta^ad d_d w
w = -sp.log(s); dw = [sp.diff(w, v) for v in X]
Gc = [[[sp.simplify(dw[b]*int(a == cc) + dw[cc]*int(a == b) - eta[b, cc]*sum(eta.inv()[a, d]*dw[d] for d in range(n)))
        for cc in range(n)] for b in range(n)] for a in range(n)]
Gm = [[[sp.simplify(sum(gi[a, q]*(sp.diff(g[q, b], X[cc]) + sp.diff(g[q, cc], X[b]) - sp.diff(g[b, cc], X[q])) for q in range(n))/2)
        for cc in range(n)] for b in range(n)] for a in range(n)]
print("(a) Christoffels conforme == metrique :", all(sp.simplify(Gc[a][b][cc] - Gm[a][b][cc]) == 0 for a in range(n) for b in range(n) for cc in range(n)))
print("    non nuls :", {(a, b, cc): Gc[a][b][cc] for a in range(n) for b in range(n) for cc in range(n) if Gc[a][b][cc] != 0})
G = Gc

# ---------- (b) mode ----------
I2ex = (1 + 2*beta*(lam - sp.log(s)))/e**2
u = sp.Function('u')
# premier ordre : U1'' + k^2 U1 = (2/s) U0'  (verifie par developpement de l'equation exacte)
U0, U1 = sp.Function('U0')(s), sp.Function('U1')(s)
eqfull = sp.expand((sp.diff(I2ex*sp.diff(U0 + beta*U1, s), s) + k**2*I2ex*(U0 + beta*U1))*e**2)
eq1 = sp.expand(eqfull.coeff(beta, 1))
eq1 = eq1.subs(sp.diff(U0, s, 2), -k**2*U0)   # U0 libre
print("(b) equation d'ordre beta (coef. de 1 + 2 beta(lam - ln s) factorise) :", sp.simplify(eq1 - 2*(lam - sp.log(s))*0))
# magnetique : solution particuliere exacte en forme close (variation des constantes) puis serie
U0m = u0*sp.cos(k*s)
src = sp.simplify(2/s*sp.diff(U0m, s))
t = sp.symbols('t', positive=True)
# U1(s) = int_0^s sin(k(s-t))/k * src(t) dt  (U1(0) = U1'(0) = 0)
U1m_ser = sp.series(sp.integrate(sp.series(sp.sin(k*(s - t))/k*src.subs(s, t), t, 0, 9).removeO(), (t, 0, s)), s, 0, 9).removeO()
print("    magnetique U1 (Green) =", sp.expand(U1m_ser))
# electrique : U1 = int_0^s sin(k(s-t))/k * 2c cos(kt)/t dt : divergent en t->0 => borne inferieure s0 ; partie en ln s
U0e = c/k*sp.sin(k*s)
srce = sp.simplify(2/s*sp.diff(U0e, s))
print("    electrique : source (2/s)U0' =", srce, " ; ordre principal U1 ~ 2c s ln s : verif",
      sp.simplify(sp.diff(2*c*s*sp.log(s), s, 2) - 2*c/s))
# resomme (k->0, ordre dominant en ks) : (I^2 u_s)_s = 0 => u_s = C/I^2 (electrique) ; u = const (magnetique)
print("    resomme electrique : I^2 (u_s)^2 avec u_s = c e^2... /I^2 ->  proportionnel a 1/I^2 =", sp.simplify(1/I2ex))

# ---------- (c) X^M mixte et moyenne ----------
def XM_avg(uf, I2):
    Ay = uf*sp.cos(k*x)
    F = sp.zeros(4, 4)
    F[1, 2] = sp.diff(Ay, x); F[2, 1] = -F[1, 2]
    F[0, 2] = sp.diff(Ay, s); F[2, 0] = -F[0, 2]
    Fup = gi*F*gi
    F2 = sum(F[i, j]*Fup[i, j] for i in range(n) for j in range(n))
    T = sp.zeros(4, 4)
    for a_ in range(n):
        for b_ in range(n):
            T[a_, b_] = I2*(sum(F[a_, m]*F[b_, q]*gi[m, q] for m in range(n) for q in range(n)) - g[a_, b_]*F2/4)
    # moyenne : remplacer sin^2(kx), cos^2(kx) -> 1/2, sin*cos -> 0
    def av(v):
        v = sp.expand(sp.expand_trig(v))
        v = v.subs({sp.sin(k*x)**2: sp.Rational(1, 2), sp.cos(k*x)**2: sp.Rational(1, 2)})
        v = v.subs({sp.sin(k*x)*sp.cos(k*x): 0})
        return sp.expand(v)
    T = T.applyfunc(av)
    F2eta = av(sum(F[i, j]*(eta*F*eta)[i, j] for i in range(n) for j in range(n)))
    return T, F2eta

Tm, F2m = XM_avg(U0m, 1/e**2)
mixed = (gi*Tm).applyfunc(sp.simplify)
print("(c) magnetique ordre 0, T^mu_nu =", [sp.simplify(mixed[i, i]) for i in range(4)], " trace =", sp.simplify(mixed.trace()))
print("    covariant T_mu_nu =", [sp.simplify(Tm[i, i]) for i in range(4)])
# premier ordre complet, branche magnetique : u = U0 + beta U1
um = U0m + beta*U1m_ser
Tm1, _ = XM_avg(um, I2ex)
for i in range(4):
    v = sp.expand(sp.series(Tm1[i, i], s, 0, 4).removeO())
    v1 = sp.expand(v.coeff(beta, 1)); v0 = sp.expand(v.coeff(beta, 0))
    print(f"    comp {i}: ordre0 = {sp.factor(v0)} ; coef beta*ln s = {sp.factor(v1.coeff(sp.log(s)))} ; coef beta (hors ln) = {sp.factor(v1.subs(sp.log(s), 0))}")
# electrique, ordre dominant en s : u = c s (1 + beta(2 ln s + b1)) + O(s^3) ; b1 arbitraire
b1 = sp.symbols('b1')
ue = c/k*sp.sin(k*s) + beta*(2*c*s*sp.log(s) + b1*c*s)
Te1, _ = XM_avg(ue, I2ex)
for i in range(4):
    v = sp.expand(sp.series(Te1[i, i], s, 0, 3).removeO())
    v1 = sp.expand(v.coeff(beta, 1)); v0 = sp.expand(v.coeff(beta, 0))
    print(f"    elec comp {i}: ordre0 = {sp.factor(v0)} ; coef beta ln s = {sp.factor(v1.coeff(sp.log(s)))}")

# ---------- (d) fermeture C-iso et (e) R ----------
def cov_D(T):   # nabla_r T_mq
    return {(r, m, q): sp.diff(T[m, q], X[r]) - sum(G[p][r][m]*T[p, q] + G[p][r][q]*T[m, p] for p in range(n))
            for r in range(n) for m in range(n) for q in range(n)}

def R_from(Ttot):
    trT = sp.expand(sum(gi[i, j]*Ttot[i, j] for i in range(n) for j in range(n)))
    L = kap/2*(Ttot - trT*g/3)
    DL = cov_D(L)
    out = {}
    for rho, nu, la in it.product(range(n), repeat=3):
        if nu < la:
            v = sp.simplify((DL[(nu, la, rho)] - DL[(la, nu, rho)])/s)
            if v != 0:
                out[(rho, nu, la)] = v
    return out

def closure(TM, That):
    # X^R = diag(r0, r1, r1, r1), trace(X^R) = That, div(TM + XR) = 0 ; resolution a la main
    r0 = sp.Function('r0')(s)
    r1 = (r0 + That/s**2)/3
    XR = sp.diag(r0, r1, r1, r1)
    Tt = TM + XR
    DT = cov_D(Tt)
    div0 = sp.expand(sum(gi[m, r]*DT[(r, m, 0)] for m in range(n) for r in range(n)))
    sol = sp.dsolve(div0, r0)
    r0s = sol.rhs.subs(sp.Symbol('C1'), Cr)
    Tt = Tt.subs(r0, r0s).applyfunc(lambda v: sp.expand(v.doit()))
    DT = cov_D(Tt)
    divs = [sp.simplify(sum(gi[m, r]*DT[(r, m, nu)] for m in range(n) for r in range(n))) for nu in range(n)]
    return Tt, r0s, divs

# cas uniforme exact F_xy = B0 (solution exacte de (3.14) avec I^2 exact) : premier ordre en beta
Fu_T = sp.zeros(4, 4)
F = sp.zeros(4, 4); F[1, 2] = B0; F[2, 1] = -B0
Fup = gi*F*gi; F2 = sum(F[i, j]*Fup[i, j] for i in range(n) for j in range(n))
I2lin = (1 + 2*beta*(sp.Symbol('lamU') - sp.log(s)))/e**2
for a_ in range(n):
    for b_ in range(n):
        Fu_T[a_, b_] = sp.expand(I2lin*(sum(F[a_, m]*F[b_, q]*gi[m, q] for m in range(n) for q in range(n)) - g[a_, b_]*F2/4))
F2eta_u = 2*B0**2
Thu = -(beta/(2*e**2))*F2eta_u*s**4
Ttu, r0u, divu = closure(Fu_T, Thu)
print("\n(d) uniforme : r0 =", sp.simplify(r0u), " ; div =", divu)
Ru = R_from(Ttu)
for key, v in Ru.items():
    print("    R uniforme", key, ":", sp.collect(sp.expand(v), sp.log(s)))

# mode magnetique, homogene, premier ordre en beta, ordre dominant s^0
TMm = Tm1.applyfunc(lambda v: sp.expand(sp.series(v, s, 0, 6).removeO()))
TMm = TMm.applyfunc(lambda v: sp.expand(v.coeff(beta, 0) + beta*v.coeff(beta, 1)))
That_m = sp.expand(-(beta/(2*e**2))*F2m*s**4)   # F2eta d'ordre 0 suffit au premier ordre
Ttm, r0m, divm = closure(TMm, That_m)
print("(d) mode : div (tronque) =", [sp.expand(sp.series(v, s, 0, 4).removeO()) for v in divm])
Rm = R_from(Ttm)
for key, v in Rm.items():
    v = sp.expand(sp.series(sp.expand(v), s, 0, 2).removeO())
    v = sp.expand(v.coeff(beta, 0) + beta*v.coeff(beta, 1))
    # garder strictement s^0 (y compris s^0 ln s) : coefficient de s^0 apres separation
    v0 = sp.expand(sum(term for term in sp.Add.make_args(v) if sp.degree(term.subs(sp.log(s), 1), s) == 0))
    print("    R mode", key, ":", sp.collect(v0, sp.log(s)), " ; contient C_r ?", v.has(Cr))
print("    C_r dans R uniforme ?", any(v.has(Cr) for v in Ru.values()))

# ---------- (f) Bochner via Hodge + Weitzenbock ----------
sqrtg = s**-4
eps = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
for p in it.permutations(range(4)):
    eps[p] = sp.combinatorics.Permutation(list(p)).signature()
def hodge2(Fc):  # (*F)_ab = 1/2 sqrt|g| eps_abcd F^cd
    Fu_ = gi*Fc*gi
    return sp.Matrix(4, 4, lambda a, b: sp.simplify(sp.Rational(1, 2)*sqrtg*sum(eps[a, b, cc, d]*Fu_[cc, d] for cc in range(4) for d in range(4))))
def delta2(Fc):  # (delta F)_b = -nabla^a F_ab = -(1/sqrtg) g_bc d_a(sqrtg F^ac) for antisymmetric F
    Fu_ = gi*Fc*gi
    return [sp.simplify(-sum(g[b, cc]*sum(sp.diff(sqrtg*Fu_[a, cc], X[a]) for a in range(4)) for cc in range(4))/sqrtg) for b in range(4)]
def d1(A):
    return sp.Matrix(4, 4, lambda a, b: sp.diff(A[b], X[a]) - sp.diff(A[a], X[b]))
def dF3(Fc):
    return [[[sp.simplify(sp.diff(Fc[b, cc], X[a]) + sp.diff(Fc[cc, a], X[b]) + sp.diff(Fc[a, b], X[cc])) for cc in range(4)] for b in range(4)] for a in range(4)]
def hodge_laplacian_closed(Fc):
    # F ferme : Delta F = d delta F
    return d1(delta2(Fc))
for name, Fc in (("uniforme", sp.Matrix(4, 4, lambda a, b: B0*int((a, b) == (1, 2)) - B0*int((a, b) == (2, 1)))),
                 ("mode", None)):
    if Fc is None:
        Ay = u0*sp.cos(k*s)*sp.cos(k*x)
        Fc = d1([0, 0, Ay, 0])
    dd = dF3(Fc)
    closed = all(dd[a][b][cc] == 0 for a in range(4) for b in range(4) for cc in range(4))
    DH = hodge_laplacian_closed(Fc).applyfunc(sp.simplify)
    # Weitzenbock sur espace d'Einstein a courbure constante +1 : Delta F = -Box F + 4 F  =>  -Box F = Delta F - 4F
    mBox = (DH - 4*Fc).applyfunc(sp.simplify)
    nz = [(a, b) for a in range(4) for b in range(4) if Fc[a, b] != 0]
    print(f"(f) {name}: dF=0 ? {closed} ; Delta_Hodge F = 0 ? {all(v == 0 for v in DH)} ; (-Box F)/F =", {ab: sp.simplify(mBox[ab]/Fc[ab]) for ab in nz})

# controle direct de Weitzenbock (coefficient 4) avec Box calcule par Christoffels conformes, sur un 2-forme generique
f = [[sp.Function(f'f{a}{b}')(s, x, y, z) if a < b else 0 for b in range(4)] for a in range(4)]
Fg = sp.Matrix(4, 4, lambda a, b: f[a][b] if a < b else (-f[b][a] if a > b else 0))
N1 = {(a, m, q): sp.diff(Fg[m, q], X[a]) - sum(G[p][a][m]*Fg[p, q] + G[p][a][q]*Fg[m, p] for p in range(n)) for a in range(n) for m in range(n) for q in range(n)}
def boxc(m, q):
    acc = 0
    for a in range(n):
        for b in range(n):
            if gi[a, b] == 0: continue
            term = sp.diff(N1[(a, m, q)], X[b]) - sum(G[p][b][a]*N1[(p, m, q)] + G[p][b][m]*N1[(a, p, q)] + G[p][b][q]*N1[(a, m, p)] for p in range(n))
            acc += gi[a, b]*term
    return acc
# Delta_Hodge generique = d delta + delta d ; ici on teste seulement la composante (x,y) pour economiser
def delta3(H):  # (delta H)_bc = -nabla^a H_abc = -(1/sqrtg) g_b. g_c. d_a(sqrtg H^a..)
    Hup = [[[sum(gi[a, a2]*gi[b, b2]*gi[cc, c2]*H[a2][b2][c2] for a2 in range(4) for b2 in range(4) for c2 in range(4)) for cc in range(4)] for b in range(4)] for a in range(4)]
    return sp.Matrix(4, 4, lambda b, cc: -sum(g[b, b2]*g[cc, c2]*sum(sp.diff(sqrtg*Hup[a][b2][c2], X[a]) for a in range(4)) for b2 in range(4) for c2 in range(4))/sqrtg)
DHg = d1(delta2(Fg)) + delta3(dF3(Fg))
for (m, q) in ((1, 2), (0, 2)):
    wz = sp.simplify(DHg[m, q] - (-boxc(m, q) + 4*Fg[m, q]))
    print(f"    Weitzenbock generique composante {(m, q)} : Delta F - (-Box F + 4F) =", wz)
print("EXIT 0")
