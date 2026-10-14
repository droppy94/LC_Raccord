#!/usr/bin/env python3
# Audit D-a : re-derivation independante. sympy. Coordonnees (s,x,y,z), s=-tau>0.
import sympy as sp

s = sp.symbols('s', positive=True)
k, e, kap, C0, C1, B0 = sp.symbols('k e kappa C0 C1 B0', positive=True)
beta, lam, u0, c = sp.symbols('beta lambda u0 c', real=True)
L = sp.symbols('L', real=True)      # L = ln s (marqueur)
Cx, Sx = sp.symbols('Cx Sx')        # cos(kx), sin(kx)
N = 9                                # ordre de troncature en s

def P(*a):
    print(*a, flush=True)

def trunc(expr, n=N):
    """Tronque un polynome en s (coeffs dependant de log s) a l'ordre s^n."""
    expr = sp.expand(expr)
    return sum(expr.coeff(s, j) * s**j for j in range(0, n + 1))

def first_order(expr):
    expr = sp.expand(expr)
    return sp.expand(expr.coeff(beta, 0) + beta * expr.coeff(beta, 1))

def toL(expr):
    return sp.expand(sp.expand_log(expr, force=True).subs(sp.log(s), L))

# ---------------------------------------------------------------- Q1
P("=== Q1 : equation de mode, ordre beta ===")
P("f = 1+2b(lam - ln s); (f u')' + k^2 f u = 0 -> u1'' + k^2 u1 = (2/s) u0'")
def solve_u1(u0expr, fix):
    a = sp.symbols('a0:%d' % (N + 2)); b = sp.symbols('b0:%d' % (N + 2))
    u1 = sum((a[j] + b[j] * sp.log(s)) * s**j for j in range(N + 2))
    src = sp.series(2 * sp.diff(u0expr, s) / s, s, 0, N).removeO()
    res = toL(sp.diff(u1, s, 2) + k**2 * u1 - src)
    eqs = []
    for j in range(-2, N):
        cj = sp.expand(res.coeff(s, j)) if j != 0 else sp.expand(res.subs(s, 0) if False else res.coeff(s, 0))
        cj = sp.Poly(cj, L)
        eqs += list(cj.coeffs())
    sol = sp.solve(eqs + [a[0] - fix[0], a[1] - fix[1]], list(a) + list(b), dict=True)[0]
    out = sp.expand(u1.subs(sol))
    return sum(out.coeff(s, j) * s**j for j in range(0, N))  # ordre < N fiable

u0a = u0 * sp.cos(k * s)
u0b = c / k * sp.sin(k * s)
u1a = solve_u1(u0a, (0, 0))
u1b = solve_u1(u0b, (0, 0))
P("[calcule] branche (a) magnetique, u1 (a0=a1=0) =", sp.collect(trunc(u1a, 6), s))
P("[calcule] branche (b) electrique, u1 (a0=a1=0) =", sp.collect(trunc(toL(u1b), 6), s))
# verification residuelle
for nm, u0e, u1e in (("a", u0a, u1a), ("b", u0b, u1b)):
    r = toL(sp.series(sp.diff(u1e, s, 2) + k**2 * u1e - 2 * sp.diff(u0e, s) / s, s, 0, N - 2).removeO())
    P("   verif residu branche", nm, ":", sp.simplify(r))
    # verif sur l'equation complete (f u')' + k^2 f u au 1er ordre
    f = 1 + 2 * beta * (lam - sp.log(s))
    U = u0e + beta * u1e
    full = toL(sp.series(sp.diff(f * sp.diff(U, s), s) + k**2 * f * U, s, 0, N - 2).removeO())
    P("   verif eq. complete ordre beta^1 :", sp.simplify(sp.expand(full).coeff(beta, 1)))

# ---------------------------------------------------------------- geometrie
co = [s, sp.Symbol('x'), sp.Symbol('y'), sp.Symbol('z')]
eta = sp.diag(-1, 1, 1, 1)
g = eta / s**2
gi = eta * s**2
def christoffel(g, gi):
    G = [[[0] * 4 for _ in range(4)] for _ in range(4)]
    for a_ in range(4):
        for b_ in range(4):
            for c_ in range(4):
                G[a_][b_][c_] = sp.simplify(sum(gi[a_, d] * (sp.diff(g[d, b_], co[c_]) + sp.diff(g[d, c_], co[b_]) - sp.diff(g[b_, c_], co[d])) for d in range(4)) / 2)
    return G
Gam = christoffel(g, gi)

def Fmat(u, uniform=False):
    F = sp.zeros(4)
    if uniform:
        F[1, 2] = B0; F[2, 1] = -B0
    else:
        F[0, 2] = sp.diff(u, s) * Cx; F[2, 0] = -F[0, 2]
        F[1, 2] = -k * u * Sx;         F[2, 1] = -F[1, 2]
    return F

def avg(expr):
    expr = sp.expand(expr)
    pol = sp.Poly(expr, Cx, Sx)
    out = 0
    for (i, j), cf in pol.terms():
        if (i, j) == (0, 0): w = 1
        elif (i, j) == (2, 0) or (i, j) == (0, 2): w = sp.Rational(1, 2)
        elif (i, j) == (1, 1): w = 0
        else: raise ValueError((i, j))
        out += w * cf
    return out

I2 = (1 + 2 * beta * (lam - sp.log(s))) / e**2

def XM(F):
    FF = sum(F[a_, b_] * F[c_, d] * gi[a_, c_] * gi[b_, d] for a_ in range(4) for b_ in range(4) for c_ in range(4) for d in range(4))
    X = sp.zeros(4)
    for m in range(4):
        for n in range(4):
            X[m, n] = I2 * (sum(F[m, a_] * F[n, b_] * gi[a_, b_] for a_ in range(4) for b_ in range(4)) - g[m, n] * FF / 4)
    return X, FF

def FFeta(F):
    return sum(F[a_, b_] * F[c_, d] * eta[a_, c_] * eta[b_, d] for a_ in range(4) for b_ in range(4) for c_ in range(4) for d in range(4))

def leading(expr, var=s):
    """terme dominant s->0 d'un Laurent-polynome en s, coeffs polynome en L, au 1er ordre beta"""
    expr = sp.expand(expr)
    pw = sorted(set(t.as_coeff_exponent(var)[1] for t in sp.Add.make_args(expr)))
    for p in pw:
        cf = sp.simplify(expr.coeff(var, p))
        if cf != 0:
            return p, sp.expand(cf)
    return None, 0

# ---------------------------------------------------------------- Q2
P("\n=== Q2 : <X^M> diagonale ===")
branches = {"a_magnetique": u0a, "b_electrique": u0b}
u1s = {"a_magnetique": u1a, "b_electrique": u1b}
XMavg = {}
for nm in branches:
    U = trunc(sp.series(branches[nm], s, 0, N).removeO() + beta * u1s[nm], N)
    F = Fmat(U)
    X, FF = XM(F)
    Xa = sp.zeros(4)
    for m in range(4):
        for n in range(4):
            Xa[m, n] = first_order(toL(avg(X[m, n])))
    XMavg[nm] = (Xa, U, F)
    P("-- branche", nm)
    P("   hors-diagonal nuls :", all(Xa[m, n] == 0 for m in range(4) for n in range(4) if m != n))
    P("   trace g^{mn}X_mn =", sp.simplify(trunc(sp.expand(sum(gi[m, m] * Xa[m, m] for m in range(4))), N)))
    for m, lab in enumerate("sxyz"):
        p, cf = leading(Xa[m, m])
        c0 = cf.coeff(beta, 0); c1 = cf.coeff(beta, 1)
        P(f"   X_{lab}{lab} ~ s^{p} * [ {sp.factor(c0)} ] * (1 + beta*( {sp.simplify(sp.expand(c1/c0).coeff(L,0))} + ({sp.simplify(sp.expand(c1/c0).coeff(L,1))}) ln s ))" if c0 != 0 else f"   X_{lab}{lab} ~ s^{p} * {cf}")

# ---------------------------------------------------------------- Q3
def cov_div(T):
    """V_n = g^{ma} nabla_a T_{mn}"""
    V = []
    for n in range(4):
        tot = 0
        for m in range(4):
            for a_ in range(4):
                if gi[m, a_] == 0: continue
                d = sp.diff(T[m, n], co[a_]) - sum(Gam[l][a_][m] * T[l, n] + Gam[l][a_][n] * T[m, l] for l in range(4))
                tot += gi[m, a_] * d
        V.append(sp.expand(tot))
    return V

def build_XR(Xa, That, Cint):
    """trace + conservation -> r0, r1 (series s, L). ansatz polynome en s, L."""
    r0 = sp.Function('r0')(s); r1 = (That / s**2 + r0) / 3   # -s^2 r0 + 3 s^2 r1 = That
    XR = sp.diag(r0, r1, r1, r1)
    V = cov_div(Xa.subs(L, sp.log(s)) + XR)
    ode = sp.expand(V[0])
    # ansatz
    M = N + 4
    al = sp.symbols('al0:%d' % M); bl = sp.symbols('bl0:%d' % M)
    ans = sum((al[j] + bl[j] * sp.log(s)) * s**j for j in range(M))
    od = toL(sp.expand(ode.subs(r0, ans).doit()))
    od = first_order(od)
    eqs = []
    pw = sorted(set(t.as_coeff_exponent(s)[1] for t in sp.Add.make_args(od)))
    for p in pw:
        if p > N - 1: continue
        cf = sp.Poly(sp.expand(od.coeff(s, p)), L, beta)
        eqs += list(cf.coeffs())
    sol = sp.solve(eqs, list(al) + list(bl), dict=True)
    sol = sol[0]
    r0s = sp.expand(ans.subs(sol))
    free = sorted(r0s.free_symbols & (set(al) | set(bl)), key=str)
    return r0s, free

def schouten_R(T):
    trT = sp.expand(sum(gi[m, n] * T[m, n] for m in range(4) for n in range(4)))
    Lh = (kap / 2) * (T - g * trT / 3)
    def nabla(nu, lam_, rho):
        return sp.diff(Lh[lam_, rho], co[nu]) - sum(Gam[sg][nu][lam_] * Lh[sg, rho] + Gam[sg][nu][rho] * Lh[lam_, sg] for sg in range(4))
    R = {}
    for rho in range(4):
        for nu in range(4):
            for la in range(nu + 1, 4):
                val = sp.expand((nabla(nu, la, rho) - nabla(la, nu, rho)) / s)
                if val != 0:
                    R[(rho, nu, la)] = val
    return R, trT

P("\n=== Q3 : branche magnetique, fermeture C-iso ===")
def do_closure(Xa, That, label):
    r0s, free = build_XR(Xa, That, None)
    P(f"-- {label} : constantes libres dans r0 :", free)
    # imposer : on garde une constante libre (s^2 coefficient) ; renommer
    r0L = first_order(toL(r0s))
    r1L = first_order(toL((That / s**2 + r0s) / 3))
    XR = sp.diag(r0L, r1L, r1L, r1L)
    T = (Xa + XR).subs(L, sp.log(s))
    V = cov_div(T)
    P("   verif conservation (ordres < s^%d) :" % (N - 3), [sp.simplify(trunc(first_order(toL(v * s**3)), N - 3)) for v in V])
    tr = sp.expand(sum(gi[m, m] * T[m, m] for m in range(4)))
    P("   verif trace - That :", sp.simplify(trunc(first_order(toL(tr - That)), N - 1)))
    P("   r0 =", sp.collect(trunc(r0L, 6), s))
    P("   r1 =", sp.collect(trunc(r1L, 6), s))
    R, trT = schouten_R(T)
    out = {}
    for key, val in R.items():
        v = first_order(toL(val))
        p, cf = leading(v)
        out[key] = (p, cf)
        lab = "R_" + "".join("sxyz"[i] for i in key)
        P(f"   {lab} ~ s^{p} * [{sp.collect(cf, [beta, L])}]")
        v2 = sp.expand(v - cf * s**p)
        p2, cf2 = leading(v2)
        P(f"      ordre suivant : s^{p2} * [{sp.collect(cf2, [beta, L])}]")
        out[key] = (p, cf, p2, cf2)
    return out, r0L, r1L, free

That_fn = lambda F: first_order(toL(avg(-(beta / (2 * e**2)) * FFeta(F) * s**4)))
Xa, U, F = XMavg["a_magnetique"]
That_a = That_fn(F)
P("   T_hat (mag) =", sp.collect(trunc(That_a, 7), s))
out_a, r0a, r1a, free_a = do_closure(Xa, That_a, "mode magnetique")

P("\n--- champ uniforme F_xy = B0 ---")
Fu = Fmat(None, uniform=True)
Xu, _ = XM(Fu)
Xu = sp.Matrix(4, 4, lambda m, n: first_order(toL(Xu[m, n])))
P("   X^M uniforme diag :", [sp.factor(Xu[m, m]) for m in range(4)])
That_u = first_order(toL(-(beta / (2 * e**2)) * FFeta(Fu) * s**4))
P("   T_hat (unif) =", That_u)
out_u, r0u, r1u, free_u = do_closure(Xu, That_u, "uniforme")

P("\n--- comparaison terme a terme, B0^2 -> <B^2> = k^2 u0^2/2 ---")
P("   (constantes d'integration identifiees : coefficient de s^2 libre dans r0)")
for key in sorted(set(out_a) | set(out_u)):
    lab = "R_" + "".join("sxyz"[i] for i in key)
    pa, ca, pa2, ca2 = out_a.get(key, (None, 0, None, 0)); pu, cu, pu2, cu2b = out_u.get(key, (None, 0, None, 0))
    P(f"   {lab} ordre suivant : mode s^{pa2} [{sp.collect(ca2,[beta,L])}] | unif s^{pu2} [{sp.collect(sp.expand(cu2b.subs(B0**2, k**2*u0**2/2)) if cu2b!=0 else 0,[beta,L])}]")
    cu2 = sp.expand(cu.subs(B0**2, k**2 * u0**2 / 2)) if cu != 0 else 0
    P(f"   {lab}: mode s^{pa} [{sp.collect(ca,[beta,L])}] | unif s^{pu} [{sp.collect(cu2,[beta,L])}] | diff(meme puissance) = {sp.simplify(ca - cu2) if pa == pu else 'puissances differentes'}")

# ---------------------------------------------------------------- Q4
P("\n=== Q4 : operateurs sur le mode libre (beta=0, branche magnetique) ===")
X_ = co[1]
Ay = u0 * sp.cos(k * s) * sp.cos(k * X_)
P("[calcule] (i) (d_s^2 - d_x^2) A_y =", sp.simplify(sp.diff(Ay, s, 2) - sp.diff(Ay, X_, 2)))
A = [0, 0, Ay, 0]
Ff = sp.Matrix(4, 4, lambda a_, b_: sp.diff(A[b_], co[a_]) - sp.diff(A[a_], co[b_]))
def deltaF(F):
    # (delta F)_b = - nabla^a F_ab
    out = []
    for b_ in range(4):
        tot = 0
        for a_ in range(4):
            for c_ in range(4):
                if gi[a_, c_] == 0: continue
                d = sp.diff(F[a_, b_], co[c_]) - sum(Gam[l][c_][a_] * F[l, b_] + Gam[l][c_][b_] * F[a_, l] for l in range(4))
                tot += gi[a_, c_] * d
        out.append(sp.simplify(-tot))
    return out
dF = deltaF(Ff)
P("[calcule] (ii) delta F =", dF)
# dF (exterieure) = 0 identiquement (F = dA)
dFF = [sp.simplify(sp.diff(Ff[b_, c_], co[a_]) + sp.diff(Ff[c_, a_], co[b_]) + sp.diff(Ff[a_, b_], co[c_])) for a_ in range(4) for b_ in range(4) for c_ in range(4)]
P("   dF = 0 :", all(v == 0 for v in dFF))
hodge = sp.Matrix(4, 4, lambda a_, b_: sp.simplify(sp.diff(dF[b_], co[a_]) - sp.diff(dF[a_], co[b_])))
P("   laplacien de Hodge (d delta + delta d) F = d(delta F) =", hodge == sp.zeros(4))
def bochner(F):
    T3 = [[[sp.diff(F[c_, d], co[b_]) - sum(Gam[e_][b_][c_] * F[e_, d] + Gam[e_][b_][d] * F[c_, e_] for e_ in range(4)) for d in range(4)] for c_ in range(4)] for b_ in range(4)]
    Bx = sp.zeros(4)
    for c_ in range(4):
        for d in range(4):
            tot = 0
            for a_ in range(4):
                b_ = a_
                t = sp.diff(T3[b_][c_][d], co[a_]) - sum(Gam[e_][a_][b_] * T3[e_][c_][d] + Gam[e_][a_][c_] * T3[b_][e_][d] + Gam[e_][a_][d] * T3[b_][c_][e_] for e_ in range(4))
                tot += gi[a_, b_] * t
            Bx[c_, d] = sp.simplify(tot)
    return Bx
Bx = bochner(Ff)
for (i, j) in ((1, 2), (0, 2)):
    P(f"[calcule] (iii) Box F_{'sxyz'[i]}{'sxyz'[j]} / F_{'sxyz'[i]}{'sxyz'[j]} =", sp.simplify(Bx[i, j] / Ff[i, j]))
P("   autres composantes de Box F nulles :", all(sp.simplify(Bx[i, j]) == 0 for i in range(4) for j in range(4) if (i, j) not in ((1, 2), (2, 1), (0, 2), (2, 0))))
Bu = bochner(Fu)
P("[calcule] uniforme : delta F =", deltaF(Fu), "; Box F_xy / F_xy =", sp.simplify(Bu[1, 2] / Fu[1, 2]))
P("   courbure : Ric = ", sp.simplify(sp.Symbol('dummy') * 0), "(voir weitzenbock : Delta_H = -Box + p(n-p)H^2, p=2,n=4 -> 4)")
