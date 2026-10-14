# Audit M-a1, question 1 : loi locale, mode inhomogene A_y = u(s) cos(kx), fermeture H-loc.
# Cadre : ghat = s^-2 eta, eta = diag(-1,1,1,1) en (s,x,y,z). Premier ordre en beta.
import sympy as sp, itertools, sys, time, functools
print = functools.partial(print, flush=True)
T0=time.time()

s, x = sp.symbols('s x', positive=True)
k, u0, c, beta, lam, e, kap = sp.symbols('k u0 c beta lambda e kappa', positive=True)
al0, al1 = sp.symbols('alpha0 alpha1')          # constantes homogenes libres de u1
Lg = sp.log(s)
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 6   # ordre de troncature en s
EP, EM = sp.exp(sp.I*k*x), sp.exp(-sp.I*k*x)
X = [s, x, sp.Symbol('y'), sp.Symbol('z')]
eta = sp.diag(-1, 1, 1, 1)
g = eta / s**2
gi = eta * s**2

# ---- mode u = u0 cos ks + (c/k) sin ks + beta u1, serie tronquee
U0 = sp.series(u0*sp.cos(k*s) + c/k*sp.sin(k*s), s, 0, NS+3).removeO()
a = sp.symbols('a0:%d' % (NS+4)); b = sp.symbols('b0:%d' % (NS+4))
U1 = al0 + al1*s + b[1]*Lg*s + sum((a[n] + b[n]*Lg)*s**n for n in range(2, NS+3))
I2 = (1 + 2*beta*(lam - Lg))/e**2
u = U0 + beta*U1
eqm = sp.expand(sp.diff(I2*sp.diff(u, s), s) + k**2*I2*u)
eqm1 = sp.expand(eqm.coeff(beta, 1)*s)          # ordre beta, multiplie par s
eqs = []
P = sp.Poly(sp.expand(eqm1.subs(Lg, sp.Symbol('L'))), s, sp.Symbol('L'))
for (ps, pl), cf in P.terms():
    if ps <= NS+1:
        eqs.append(cf)
print('t',time.time()-T0); sol_u1 = sp.solve(eqs, list(a[2:NS+3]) + list(b[1:NS+3]), dict=True)[0]
res = sp.expand(eqm1.subs(sol_u1).subs(Lg, sp.Symbol('L'))); print('[calcule] residu equation de mode, ordre min :', min(t.as_coeff_exponent(s)[1] for t in sp.Add.make_args(res)) if res!=0 else 'nul')
U1s = U1.subs(sol_u1)
for n in range(NS+3):
    pass
print('[calcule] u1 (debut) =', sp.series(U1s, s, 0, 4))
u = U0 + beta*U1s

# ---- champ
A = [0, 0, u*(EP+EM)/2, 0]
F = sp.zeros(4, 4)
for m_ in range(4):
    for n_ in range(4):
        F[m_, n_] = sp.diff(A[n_], X[m_]) - sp.diff(A[m_], X[n_])
Fup_eta = eta*F*eta
F2eta = sp.expand(sum(F[i, j]*Fup_eta[i, j] for i in range(4) for j in range(4)))
F2g = s**4*F2eta
XM = sp.zeros(4, 4)
for m_ in range(4):
    for n_ in range(4):
        XM[m_, n_] = I2*(sum(F[m_, al]*F[n_, bb]*gi[al, bb] for al in range(4) for bb in range(4))
                         - sp.Rational(1, 4)*g[m_, n_]*F2g)
That = -beta/(2*e**2)*F2eta*s**4

# ---- ansatz fermeture H-loc : diag(r0,r1,r1,r1) + q en (s,x)
basis = [1, sp.exp(2*sp.I*k*x), sp.exp(-2*sp.I*k*x)]
unk = []
def ansatz(name, nmin, nmax):
    expr = 0
    for n in range(nmin, nmax+1):
        for m in range(3):
            for ib, bf in enumerate(basis):
                for bo in range(2):
                    sym = sp.Symbol('%s_%d_%d_%d_%d' % (name, n, m, ib, bo))
                    unk.append(sym)
                    expr += sym*beta**bo*s**n*Lg**m*bf
    return expr
NMIN = 0
r1 = ansatz('r', NMIN, NS)
q = ansatz('q', NMIN, NS)
# trace imposee : ghat^{mn}(XM+XR) = That  ->  r0
trXM = sp.simplify(sp.expand(sum(gi[i, j]*XM[i, j] for i in range(4) for j in range(4))))
print('[calcule] trace ghat de XM =', trXM)
r0 = sp.expand(3*r1 - (That - trXM)/s**2)
XR = sp.Matrix([[r0, q, 0, 0], [q, r1, 0, 0], [0, 0, r1, 0], [0, 0, 0, r1]])

# Christoffel de ghat
Gam = [[[sp.simplify(sum(gi[a_, d]*(sp.diff(g[d, b_], X[c_]) + sp.diff(g[d, c_], X[b_]) - sp.diff(g[b_, c_], X[d]))
                         for d in range(4))/2) for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]
def cov(T):  # nabla_a T_bc
    return [[[sp.diff(T[b_, c_], X[a_]) - sum(Gam[d][a_][b_]*T[d, c_] + Gam[d][a_][c_]*T[b_, d] for d in range(4))
              for c_ in range(4)] for b_ in range(4)] for a_ in range(4)]

def trunc(expr, nmax, keep_beta=1):
    """1er ordre en beta ; dict (n, m, b) -> coef(x) pour s^n ln^m s beta^b, n<=nmax"""
    ex = sp.expand(expr)
    ex = sp.expand(ex.subs(Lg, sp.Symbol('L')))
    out = {}
    for term in sp.Add.make_args(ex):
        if term == 0: continue
        cs, ns = term.as_coeff_exponent(s)
        assert not cs.has(s), term
        if ns > nmax: continue
        cb, bo = cs.as_coeff_exponent(beta)
        if bo > 1: continue
        cl, mL = cb.as_coeff_exponent(sp.Symbol('L'))
        key = (int(ns), int(mL), int(bo))
        out[key] = out.get(key, 0) + cl
    return out

T = XM + XR
TT = sp.Matrix(4, 4, lambda i, j: sp.expand(T[i, j]))
cT = cov(TT)
div = [sp.expand(sum(gi[a_, b_]*cT[a_][b_][nu] for a_ in range(4) for b_ in range(4))) for nu in range(4)]
print('[calcule] div composantes y,z nulles :', sp.simplify(div[2]) == 0, sp.simplify(div[3]) == 0)

# equations de conservation : ordres s^n, n <= NS+1 (div ~ s^2 * d T ~ s^{n+1})
cons = []
for nu in (0, 1):
    dd = trunc(div[nu]*s**0, NS+1)
    for key, cf in dd.items():
        cfe = sp.expand(cf)
        for ib, bf in enumerate([sp.exp(2*sp.I*k*x), sp.exp(-2*sp.I*k*x)]):
            cfe_ = cfe
        # projeter sur la base exp(0), exp(+-2ikx)
        cfe = sp.expand(cfe)
        proj = {0: 0, 2: 0, -2: 0}
        for t in sp.Add.make_args(cfe):
            if t == 0: continue
            ph = 0
            for p in (2, -2):
                if t.has(sp.exp(p*sp.I*k*x)):
                    ph = p
            proj[ph] += t.subs(sp.exp(ph*sp.I*k*x), 1) if ph else t
        for v in proj.values():
            v = sp.expand(v)
            if v != 0:
                cons.append(v)
print('[calcule] nombre d equations de conservation :', len(cons))
print('t avant solve',time.time()-T0); Am, bm = sp.linear_eq_to_matrix(cons, unk)
solset = sp.linsolve((Am, bm), unk)
assert solset != sp.S.EmptySet
sol = list(solset)[0]
solX = {u_: v for u_, v in zip(unk, sol) if v != u_}
free = [u_ for u_ in unk if u_ not in solX]
print('[calcule] inconnues libres restantes (fonctions d integration + troncature) :', len(free), free)
for u_ in free:
    pass
XRs = {nm: sp.expand(ex.subs(solX)) for nm, ex in (('r1', r1), ('q', q))}
for nm, ex in XRs.items():
    d = trunc(ex, 3)
    print('[calcule] X^R %s : ordres (n, m_log, beta) presents jusqu a s^3 :' % nm, sorted(kk for kk, v in d.items() if sp.expand(v) != 0))
    for kk in sorted(d):
        if sp.expand(d[kk]) != 0 and kk[0] <= 2: print('     ', kk, sp.simplify(sp.expand(d[kk]).rewrite(sp.cos)))

# ---- L et R
TS = sp.Matrix(4, 4, lambda i, j: sp.expand(TT[i, j].subs(solX)))
print('t apres subs', time.time()-T0)
trT = sp.expand(sum(gi[i, j]*TS[i, j] for i in range(4) for j in range(4)))
Lh = sp.Matrix(4, 4, lambda i, j: sp.expand(kap/2*(TS[i, j] - g[i, j]*trT/3)))
cL_ = cov(Lh)
names = 'sxyz'
Rres = {}
for rho in range(4):
    for nu in range(4):
        for la in range(nu+1, 4):
            Rres[(rho, nu, la)] = sp.expand((cL_[nu][la][rho] - cL_[la][nu][rho])/s)
print('t apres R', time.time()-T0)
for nu in (0, 1):
    dchk = trunc(sp.expand(div[nu].subs(solX)), NS+1)
    print('[calcule] conservation nu=%s apres solution, ordres <= s^%d nuls :' % (names[nu], NS+1), all(sp.expand(v) == 0 for v in dchk.values()))
# Q local a scri (beta^0, s=0)
Ey = sp.expand(sp.diff(u, s).subs(beta, 0).subs(s, 0)*(EP+EM)/2)
Bz = sp.expand(sp.diff(u*(EP+EM)/2, x).subs(beta, 0).subs(s, 0))
Bv = [0, 0, Bz]; Ev = [0, Ey, 0]
Q = sp.Matrix(3, 3, lambda i, j: sp.expand(Bv[i]*Bv[j] - Ev[i]*Ev[j]))
Qtf = sp.expand(Q - sp.eye(3)*Q.trace()/3)

Ls = sp.Symbol('L')
def coef(R, ns, mL, bo):
    return sp.simplify(sp.expand(trunc(R, 1).get((ns, mL, bo), 0)))

print('\n==== (a) coefficient de beta*ln s a l ordre s^0, toutes composantes R_{rho nu lambda} ====')
allok = True
for (rho, nu, la), R in Rres.items():
    d = trunc(R, 1)
    lab = 'R_%s%s%s' % (names[rho], names[nu], names[la])
    c10 = sp.simplify(sp.expand(d.get((0, 1, 1), 0)).rewrite(sp.cos))
    c20 = sp.simplify(sp.expand(d.get((0, 2, 1), 0)).rewrite(sp.cos))
    c1b0 = sp.simplify(sp.expand(d.get((0, 1, 0), 0)))
    neg = [kk for kk in d if kk[0] < 0 and sp.simplify(d[kk]) != 0]
    if nu == 0 and rho >= 1 and la >= 1:
        target = 3*kap/e**2*Qtf[rho-1, la-1]
        diff_ = sp.simplify(sp.expand((c10 - target).rewrite(sp.exp)))
        print('[calcule] %s : coef(beta ln s, s^0) = %s ; - (3k/e^2)Qtf = %s ; ln^2 : %s ; beta^0 ln : %s ; ordres <0 : %s'
              % (lab, c10, diff_, c20, c1b0, neg))
        allok &= (diff_ == 0)
    else:
        print('[calcule] %s : coef(beta ln s, s^0) = %s ; ln^2 : %s ; ordres <0 : %s' % (lab, c10, c20, neg))
print('[calcule] loi locale R_isj|_{beta ln s, s^0} = (3 kappa/e^2) Qtf_ij(x) :', allok)
print('[calcule] Qtf(x) =', sp.simplify(Qtf.applyfunc(lambda t: t.rewrite(sp.cos))))

print('\n==== (b) ordre s^1 : coefficient de beta ln s ====')
for (rho, nu, la), R in Rres.items():
    d = trunc(R, 1)
    c11 = sp.simplify(sp.expand(d.get((1, 1, 1), 0)).rewrite(sp.cos))
    c21 = sp.simplify(sp.expand(d.get((1, 2, 1), 0)).rewrite(sp.cos))
    if c11 != 0 or c21 != 0:
        print('[calcule] R_%s%s%s : s^1 beta ln s : %s ; s^1 beta ln^2 s : %s' % (names[rho], names[nu], names[la], c11, c21))

print('\n==== (c) dependance des coefficients de log (s^0 et s^1) envers les constantes libres ====')
fs = set(free) | {al0, al1, lam}
for (rho, nu, la), R in Rres.items():
    d = trunc(R, 1)
    for key in [(0, 1, 1), (0, 2, 1), (1, 1, 1), (1, 2, 1), (0, 1, 0), (1, 1, 0), (0, 0, 0), (0, 0, 1)]:
        cf = sp.expand(d.get(key, 0))
        dep = sorted(str(f) for f in fs if cf.has(f))
        if dep:
            print('[calcule] R_%s%s%s %s depend de %s' % (names[rho], names[nu], names[la], key, dep))
print('[calcule] fin (NS=%d)' % NS)
