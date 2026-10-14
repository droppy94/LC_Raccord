# Audit J-a : noyau de calcul (re-derivation independante)
# de Sitter H=1, s=-tau>0, Omega=s, ghat = s^-2 eta, eta=diag(-1,1,1,1) en (s,x,y,z)
import sympy as sp

s = sp.symbols('s', positive=True)
x, y, z = sp.symbols('x y z', real=True)
beta, lam, e, kap = sp.symbols('beta lambda e kappa', positive=True)
LS = sp.Symbol('LS')  # stand-in pour ln s dans les extractions
X = [s, x, y, z]
eta = sp.diag(-1, 1, 1, 1)
gh = eta / s**2
ghi = gh.inv()
I2 = e**-2 * (1 + 2*beta*(lam - sp.log(s)))
NORD = 7  # ordre de troncature en s pour u1

# Christoffel de ghat
Gam = [[[sp.simplify(sum(ghi[l, m]*(sp.diff(gh[m, a], X[b]) + sp.diff(gh[m, b], X[a]) - sp.diff(gh[a, b], X[m]))
                         for m in range(4))/2) for b in range(4)] for a in range(4)] for l in range(4)]


def u1_particular(u0, c, k, N=NORD):
    """u1'' + k^2 u1 = (2/s) d_s u^(0), solution particuliere serie en s, ln s, sans s^0 ni s^1 pur."""
    u0f = u0*sp.cos(k*s) + c/k*sp.sin(k*s)
    rhs = sp.series(2/s*sp.diff(u0f, s), s, 0, N).removeO()
    a = sp.symbols('a0:%d' % (N+2)); b = sp.symbols('b0:%d' % (N+2))
    ans = sum(a[n]*s**n + b[n]*s**n*sp.log(s) for n in range(N+2))
    res = sp.expand(sp.diff(ans, s, 2) + k**2*ans - rhs)
    eqs = []
    resL = sp.expand(res.subs(sp.log(s), LS))
    P = sp.Poly(sp.expand(resL*s**2), s, LS)  # multiplie par s^2 pour eliminer 1/s, 1/s^2
    for (ps, pl), cf in P.terms():
        if ps <= N+1:  # ordres fiables
            eqs.append(cf)
    eqs += [a[0], a[1]]
    sol = sp.solve(eqs, list(a)+list(b), dict=True)[0]
    u1 = ans.subs(sol)
    # coefficients non determines (ordres hauts) -> 0
    u1 = u1.subs({v: 0 for v in list(a)+list(b)})
    return sp.expand(u1)


def mode_u(u0, c, k):
    u0f = u0*sp.cos(k*s) + c/k*sp.sin(k*s)
    u0s = sp.series(u0f, s, 0, NORD+1).removeO()
    return sp.expand(u0s + beta*u1_particular(u0, c, k))


def mode_F(u, kvec, eps):
    """F_{mu nu} decompose en (P cos(k.x), Q sin(k.x)). Renvoie (P,Q) matrices 4x4."""
    us = sp.diff(u, s)
    P = sp.zeros(4); Q = sp.zeros(4)
    for i in range(3):
        P[0, i+1] = us*eps[i]; P[i+1, 0] = -us*eps[i]
        for j in range(3):
            Q[i+1, j+1] = -u*(kvec[i]*eps[j] - kvec[j]*eps[i])
    return P, Q


def XM_from_Fpair(FA, FB):
    """partie bilineaire sym. : X_mn = s^2 I2 (F_ma F_nb eta^ab - 1/4 eta_mn F.F), (FA,FB) -> forme bilineaire"""
    etai = eta
    T = sp.zeros(4)
    FF = sum(FA[a, b]*FB[c, d]*etai[a, c]*etai[b, d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
    for m in range(4):
        for n in range(4):
            T[m, n] = sum(FA[m, a]*FB[n, b]*etai[a, b] for a in range(4) for b in range(4)) - sp.Rational(1, 4)*eta[m, n]*FF
    T = (T + T.T)/2
    return s**2*I2*T, FF


def first_order(expr):
    ex = sp.expand(expr)
    return sp.expand(ex.coeff(beta, 0)), sp.expand(ex.coeff(beta, 1))


def averaged_XM(modes, cross=True):
    """modes: liste (u, kvec, eps). Moyenne spatiale exacte : <cos ka cos kb> = 1/2 delta(ka=kb), idem sin, <cos sin>=0
    (k vecteurs non nuls, pas de paire ka=-kb)."""
    Fs = [mode_F(u, kv, ep) for (u, kv, ep) in modes]
    XM = sp.zeros(4); FF = 0
    for i, (Pi, Qi) in enumerate(Fs):
        for j, (Pj, Qj) in enumerate(Fs):
            same = list(modes[i][1]) == list(modes[j][1])
            if not same or (i != j and not cross):
                continue
            Xa, Fa = XM_from_Fpair(Pi, Pj)
            Xb, Fb = XM_from_Fpair(Qi, Qj)
            XM += (Xa + Xb)/2
            FF += (Fa + Fb)/2
    return XM.applyfunc(lambda t: sp.expand(t)), sp.expand(FF)


def trunc(expr, n):
    """garde les termes s^p (ln s)^q avec p<=n (expr polynome en s, ln s, eventuellement 1/s)."""
    ex = sp.expand(sp.expand(expr).subs(sp.log(s), LS))
    out = sp.S(0)
    for t in sp.Add.make_args(ex):
        d =t.as_powers_dict().get(s, 0)
        if d <= n:
            out += t
    return sp.expand(out.subs(LS, sp.log(s)))


def closure_Ciso(XM, FFbar, N=6):
    """X^R = diag(r0,r1,r1,r1): trace ghat^{mn}(XM+XR) = That, div. cov. totale = 0. Retourne XR, eqs check."""
    That = -(beta/(2*e**2))*FFbar*s**4
    C = sp.Symbol('C_rad')
    cs = sp.symbols('q0:%d' % (3*(N+3)))
    r0 = C*s**2 + beta*sum(cs[3*n+m]*s**n*sp.log(s)**m for n in range(N+1) for m in range(3))
    trM = sp.expand(sum(ghi[m, n]*XM[m, n] for m in range(4) for n in range(4)))
    # trace: ghat^mn XR_mn = s^2(-r0+3r1)
    r1 = sp.expand((That - trM)/s**2/3 + r0/3)
    XR = sp.diag(r0, r1, r1, r1)
    T = XM + XR
    div = []
    for nu in range(4):
        d = 0
        for m in range(4):
            for a in range(4):
                if ghi[m, a] == 0:
                    continue
                cov = sp.diff(T[m, nu], X[a]) - sum(Gam[l][a][m]*T[l, nu] + Gam[l][a][nu]*T[m, l] for l in range(4))
                d += ghi[m, a]*cov
        div.append(sp.expand(d))
    # ordre beta^0 et beta^1 de div_s, resoudre par coefficients
    eqs = []
    for order in (0, 1):
        ex = sp.expand(div[0].coeff(beta, order).subs(sp.log(s), LS))
        if ex == 0:
            continue
        P = sp.Poly(sp.expand(ex*s**2), s, LS)
        for (ps, pl), cf in P.terms():
            if ps <= N+1:
                eqs.append(cf)
    sol = sp.solve(eqs, cs, dict=True)
    sol = sol[0] if sol else {}
    XR = XR.applyfunc(lambda t: sp.expand(t.subs(sol)))
    free = set().union(*[XR[i, i].free_symbols for i in range(4)]) & set(cs)
    return XR, [sp.expand(dd.subs(sol)) for dd in div], free, C


def Rtensor(T):
    trT = sp.expand(sum(ghi[m, n]*T[m, n] for m in range(4) for n in range(4)))
    L = (kap/2)*(T - gh*trT/3)
    L = L.applyfunc(sp.expand)

    def nab(nu, lam_, rho):
        return sp.diff(L[lam_, rho], X[nu]) - sum(Gam[sg][nu][lam_]*L[sg, rho] + Gam[sg][nu][rho]*L[lam_, sg] for sg in range(4))
    R = {}
    for rho in range(4):
        for nu in range(4):
            for la in range(nu+1, 4):
                R[(rho, nu, la)] = sp.expand((nab(nu, la, rho) - nab(la, nu, rho))/s)
    return R, L


def coeff_sp_ln(expr, p, q=1):
    """coefficient de s^p (ln s)^q"""
    ex = sp.expand(sp.expand(expr).subs(sp.log(s), LS))
    ex = sp.expand(ex*s**20)
    P = sp.Poly(ex, s, LS)
    return sp.simplify(P.coeff_monomial(s**(p+20)*LS**q))
