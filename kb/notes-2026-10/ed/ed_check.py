#!/usr/bin/env python3
"""
ed_check.py -- NOTE-181 (chantier ED). Jet algebra at a point, signature (+,-,-,-).
Unphysical metric g = eta (flat), physical ghat = Omega^-2 eta, tetrad ehat^a_mu = Omega^-1 delta.
psi = Omega^{3/2} psihat. psihat and its first derivatives are independent complex symbols (jets);
Omega and its first derivatives are independent real symbols.
 (A) fix the spin connection Gamma_mu = c [gamma_mu, gamma^nu] d_nu sigma, sigma = -ln Omega,
     by requiring i gammahat^mu nablahat_mu psi = Omega^{5/2} i gamma^mu d_mu psihat (off shell);
 (B) kinetic symmetrised Dirac tensor: That_{mu nu}[psi; ghat] - Omega^2 T_{mu nu}[psihat; eta] = 0 (off shell)?
 (C) Lagrangian term: Lag[psi; ghat] = Omega^4 * psihatbar (i gamma.d - m/Omega) psihat (off shell);
 (D) Omega-power count of 2 Omega^-1 nablahat_[nu Lhat_lambda] rho for Lhat = Omega^2 Y (Y generic smooth):
     no negative power of Omega (symbolic, generic Omega(x), Y(x));
 (E) scalar control: m^2 phi^2 ghat = m^2 psi^2 eta is O(Omega^0) (the source of Friedrich's terms).
"""
import sympy as sp
I = sp.I
eta = sp.diag(1, -1, -1, -1)
# Dirac representation
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
Z = sp.zeros(2); E2 = sp.eye(2)
def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(E2, Z, Z, -E2)
gs = [blk(Z, s, -s, Z) for s in (s1, s2, s3)]
gup = [g0] + gs                                   # gamma^a
glo = [sum((eta[a, b]*gup[b] for b in range(4)), sp.zeros(4)) for a in range(4)]   # gamma_a
for a in range(4):
    for b in range(4):
        assert sp.simplify(gup[a]*gup[b] + gup[b]*gup[a] - 2*eta[a, b]*sp.eye(4)) == sp.zeros(4)

Om = sp.symbols('Omega', positive=True)
dOm = sp.symbols('dO0:4', real=True)
ar = sp.symbols('a0:4', real=True); br = sp.symbols('b0:4', real=True)
dar = [sp.symbols(f'da{m}_0:4', real=True) for m in range(4)]   # d_m psihat_i real parts
dbr = [sp.symbols(f'db{m}_0:4', real=True) for m in range(4)]
ph = sp.Matrix([ar[i] + I*br[i] for i in range(4)])
dph = [sp.Matrix([dar[m][i] + I*dbr[m][i] for i in range(4)]) for m in range(4)]
m, c = sp.symbols('m c', real=True)

def bar(v): return (v.H)*g0                        # row vector psibar
psi = Om**sp.Rational(3, 2)*ph
dpsi = [Om**sp.Rational(3, 2)*dph[mu] + sp.Rational(3, 2)*Om**sp.Rational(1, 2)*dOm[mu]*ph for mu in range(4)]
dsig = [-dOm[mu]/Om for mu in range(4)]
ghat_lo = [Om**-1*glo[mu] for mu in range(4)]       # curved gamma_mu
ghat_up = [Om*gup[mu] for mu in range(4)]
def Gam(cc):
    return [cc*sum(((glo[mu]*gup[nu] - gup[nu]*glo[mu])*dsig[nu] for nu in range(4)), sp.zeros(4)) for mu in range(4)]

# (A) fix c
G = Gam(c)
lhs = sum((I*ghat_up[mu]*(dpsi[mu] + G[mu]*psi) for mu in range(4)), sp.zeros(4, 1))
rhs = Om**sp.Rational(5, 2)*sum((I*gup[mu]*dph[mu] for mu in range(4)), sp.zeros(4, 1))
diff = sp.expand(lhs - rhs)
cval = None
for cand in [sp.Rational(1,4), -sp.Rational(1,4), sp.Rational(1,8), -sp.Rational(1,8), sp.Rational(1,2), -sp.Rational(1,2)]:
    if sp.simplify(diff.subs(c, cand)) == sp.zeros(4, 1):
        cval = cand; break
G = Gam(cval)
chkA = sp.simplify(sp.expand(sum((I*ghat_up[mu]*(dpsi[mu] + G[mu]*psi) for mu in range(4)), sp.zeros(4, 1)) - rhs))
print("(A) spin connection coefficient c =", cval, "; Dirac operator covariance residual = 0 :", chkA == sp.zeros(4, 1))

# (B) kinetic tensor
def Tkin(psi_, dpsi_, gl, Gm):
    pb = bar(psi_)
    nab = [dpsi_[mu] + Gm[mu]*psi_ for mu in range(4)]
    nabb = [bar(dpsi_[mu]) - pb*Gm[mu] for mu in range(4)]
    T = sp.zeros(4)
    for mu in range(4):
        for nu in range(4):
            T[mu, nu] = (I/4)*((pb*gl[mu]*nab[nu])[0] + (pb*gl[nu]*nab[mu])[0]
                               - (nabb[nu]*gl[mu]*psi_)[0] - (nabb[mu]*gl[nu]*psi_)[0])
    return T
That = Tkin(psi, dpsi, ghat_lo, G)
Tflat = Tkin(ph, dph, glo, [sp.zeros(4)]*4)
resB = (That - Om**2*Tflat).applyfunc(lambda e: sp.simplify(sp.expand(e)))
print("(B) That[psi;ghat] - Omega^2 T[psihat;eta] = 0 off shell :", resB == sp.zeros(4))
print("    That real (Hermitian combination) :", all(sp.simplify(sp.im(sp.expand(Tflat[i, j]))) == 0 for i in range(4) for j in range(4)))

# (C) Lagrangian
Lag = (bar(psi)*(lhs.subs(c, cval) if False else sum((I*ghat_up[mu]*(dpsi[mu] + G[mu]*psi) for mu in range(4)), sp.zeros(4, 1))))[0] - m*(bar(psi)*psi)[0]
Lflat = (bar(ph)*sum((I*gup[mu]*dph[mu] for mu in range(4)), sp.zeros(4, 1)))[0] - (m/Om)*(bar(ph)*ph)[0]
print("(C) Lag[psi;ghat] - Omega^4 psihatbar(i gamma.d - m/Omega)psihat = 0 :", sp.simplify(sp.expand(Lag - Om**4*Lflat)) == 0)

# (D) Omega-power count in (2.17) source for Lhat = Omega^2 Y
X = sp.symbols('x0:4', real=True)
Of = sp.Function('O')(*X)
Y = sp.Matrix(4, 4, lambda i, j: sp.Function(f'Y{min(i,j)}{max(i,j)}')(*X))
gh = Of**-2*eta; ghi = Of**2*eta
Ch = [[[sum(ghi[a, e]*(sp.diff(gh[e, b], X[cc]) + sp.diff(gh[e, cc], X[b]) - sp.diff(gh[b, cc], X[e])) for e in range(4))/2
        for cc in range(4)] for b in range(4)] for a in range(4)]
import sys
PW = int(sys.argv[1]) if len(sys.argv) > 1 else 2
Lh = Of**PW*Y
def cov(T, a, b, cc): return sp.diff(T[a, b], X[cc]) - sum(Ch[e][cc][a]*T[e, b] + Ch[e][cc][b]*T[a, e] for e in range(4))
worst = sp.oo
for r in range(4):
    for nu in range(4):
        for la in range(nu+1, 4):
            S = sp.expand(2*(cov(Lh, la, r, nu) - cov(Lh, nu, r, la))/(2*Of))
            W = sp.Symbol('W', positive=True)
            reps = {}
            for dv in S.atoms(sp.Derivative):
                if dv.expr == Of:
                    reps[dv] = sp.Symbol('d' + '_'.join(str(v) for v, k in dv.variable_count for _ in range(k)) + '_Omega', real=True)
                else:
                    reps[dv] = sp.Symbol('D' + str(abs(hash(dv)) % 10**8), real=True)
            S = sp.expand(S.xreplace(reps).xreplace({Of: W}))
            Ysub = {f: sp.Symbol(str(f.func), real=True) for f in S.atoms(sp.Function)}
            S = sp.expand(S.xreplace(Ysub))
            p = sp.Poly(sp.expand(S*W**6), W)
            low = min(mon[0] for mon in p.monoms()) - 6 if not p.is_zero else sp.oo
            worst = min(worst, low)
print(f"(D) Lhat = Omega^{PW} Y : lowest power of Omega in 2 Omega^-1 nablahat_[nu Lhat_lambda] rho :", worst, "(>= 0 means formally regular)")

# (E) scalar control
psis, ms = sp.symbols('psi_s m_s', real=True)
print("(E) scalar: m^2 phi^2 ghat with phi = Omega psi :", sp.simplify(ms**2*(Om*psis)**2*Om**-2), "* eta  (order Omega^0)")
