#!/usr/bin/env python3
"""
fw3_check.py -- NOTE-191 (chantier FW3). Formal regularity, in Friedrich's sense (arXiv:1311.0700),
of the conformal field equations coupled to Yang-Mills (abelian suffices for weights) + Higgs
(complex, potential m^2|H|^2 + lambda_h|H|^4, non-minimal coupling xi) + Dirac (Yukawa mass).

Conventions of Friedrich: signature (-,+,+,+), physical metric ghat = Omega^-2 g, g = eta (flat, jets at a point),
Einstein eqs Rhat_ab - 1/2 Rhat ghat + lambda ghat = kappa That, so -Rhat + 4 lambda = kappa That (2.2).
Unknowns substituted for second/third derivatives of Omega (formal procedure of Friedrich):
  (2.14)  d_a d_b Omega = s eta_ab - Omega L_ab + (kappa/2) Omega S_ab        (S = T*_ab, regular, generic symbol)
  (2.15)  d_c s        = -n^r L_rc + (kappa/2) n^r S_rc - (kappa/24) Omega d_c(Omega^2 Str)   (Str = Omega^-2 That, regular)
  (3.8)   n.n          = -lambda/3 + 2 Omega s + (kappa/12) Omega^2 Str        (used as a polynomial reduction in n0)
Jets: Omega (W), n_a = d_a Omega ; H_r = p + i q with jets up to third order ; A_a with jets up to second order ;
s, L_ab, d_c L_ab, S_ab, d_c S_ab, Str, d_c Str generic.

Parts:
 (A) Yang-Mills: sqrt(-ghat) ghat^{ma} ghat^{nb} = sqrt(-g) g^{ma} g^{nb} ; That_YM = Omega^2 T_YM[A; eta] ; current weights.
 (B) Higgs equation: Omega^-3 (boxhat_D - Rhat/6)[Omega H_r] = (box_D - R/6)[H_r] (R = 0 here) off shell, with gauge A;
     rescaled Higgs equation: coefficient of Omega^-2 is m^2 + (xi - 1/6) Rhat -> m^2 + 4 lambda xi - 2 lambda/3 + regular.
 (C) Geometric sector: That_ab regular, Omega^-2 That regular, and the Laurent coefficients of Omega^-2, Omega^-1 in
     2 Omega^-1 nablahat_[nu Lhat_lambda] rho, after substitutions (2.14), (2.15), (3.8).
     Calibration 1: real scalar, xi = 0, A = 0 (Friedrich) ; calibration 2: xi = 1/6, m = 0.
 (D) Dirac (signature (+,-,-,-) as in ED, weights are signature independent): Dirac equation with A and Yukawa mass,
     kinetic tensor with A, Lagrangian with Yukawa mass: orders in Omega.
"""
import sys, itertools
import sympy as sp
I = sp.I
R = sp.Rational

# ---------------------------------------------------------------- symbols
W = sp.symbols('Omega', positive=True)
n = sp.symbols('n0:4', real=True)
s = sp.symbols('s', real=True)
lam, kap, m, xi, lamh, e = sp.symbols('lambda kappa m xi lambda_h e', real=True)
eta = sp.diag(-1, 1, 1, 1)
idx = range(4)
def sym2(name):
    M = sp.zeros(4)
    for a in idx:
        for b in idx:
            M[a, b] = sp.Symbol(f'{name}{min(a,b)}{max(a,b)}', real=True)
    return M
L = sym2('L'); S = sym2('S')
dL = [sym2(f'dL{c}_') for c in idx]; dS = [sym2(f'dS{c}_') for c in idx]
Str = sp.Symbol('Str', real=True); dStr = sp.symbols('dStr0:4', real=True)

def jets3(name):
    """value, first, second (sym), third (sym) derivative symbols"""
    v = sp.Symbol(name, real=True)
    d1 = [sp.Symbol(f'd{name}_{a}', real=True) for a in idx]
    d2 = [[sp.Symbol(f'd{name}_{min(a,b)}{max(a,b)}', real=True) for b in idx] for a in idx]
    d3 = [[[sp.Symbol(f'd{name}_' + ''.join(str(k) for k in sorted((a, b, c))), real=True) for c in idx] for b in idx] for a in idx]
    return v, d1, d2, d3

# derivatives of Omega: first = n ; second, third substituted (formal procedure)
def dds(c):  # d_c s by (2.15)
    nup = [sum(eta[r, t]*n[t] for t in idx) for r in idx]   # n^r
    return (-sum(nup[r]*L[r, c] for r in idx) + kap/2*sum(nup[r]*S[r, c] for r in idx)
            - kap/24/W*(2*W*n[c]*Str + W**2*dStr[c]))
def ddO(a, b):   # (2.14)
    return s*eta[a, b] - W*L[a, b] + kap/2*W*S[a, b]
def dddO(c, a, b):   # d_c of (2.14)
    return dds(c)*eta[a, b] - n[c]*L[a, b] - W*dL[c][a, b] + kap/2*(n[c]*S[a, b] + W*dS[c][a, b])

# Christoffel of ghat = Omega^-2 eta : Gamhat^a_bc = -(delta^a_b n_c + delta^a_c n_b - eta_bc n^a)/Omega
nup = [sum(eta[r, t]*n[t] for t in idx) for r in idx]
def Gh(a, b, c):
    return -((1 if a == b else 0)*n[c] + (1 if a == c else 0)*n[b] - eta[b, c]*nup[a])/W
ghat = W**-2*eta; ghatinv = W**2*eta

# ---------------------------------------------------------------- field content
class Field:
    """a function of x represented by jets; .v value, .d(a), .dd(a,b), .ddd(a,b,c)"""
    def __init__(self, v, d1, d2, d3):
        self.v, self.d1, self.d2, self.d3 = v, d1, d2, d3
    def d(self, a): return self.d1[a]
    def dd(self, a, b): return self.d2[a][b]
    def ddd(self, a, b, c): return self.d3[a][b][c]

# generic differentiation of polynomial expressions in jets: build a derivation D_c on the jet variables
class Jet:
    def __init__(self):
        self.rules = {}   # symbol -> list of 4 expressions (its partial derivatives)
    def add_field(self, f):
        self.rules[f.v] = [f.d1[a] for a in idx]
        for a in idx:
            self.rules[f.d1[a]] = [f.d2[a][b] for b in idx]
            for b in idx:
                self.rules[f.d2[a][b]] = [f.d3[a][b][c] for c in idx]
    def add_omega(self):
        self.rules[W] = [n[a] for a in idx]
        for a in idx:
            self.rules[n[a]] = [ddO(a, b) for b in idx]
        self.rules[s] = [dds(c) for c in idx]
        for a in idx:
            for b in idx:
                self.rules[L[a, b]] = [dL[c][a, b] for c in idx]
                self.rules[S[a, b]] = [dS[c][a, b] for c in idx]
        self.rules[Str] = [dStr[c] for c in idx]
    def add_A(self, A, dA, ddA):
        for a in idx:
            self.rules[A[a]] = [dA[b][a] for b in idx]
            for b in idx:
                self.rules[dA[b][a]] = [ddA[c][b][a] for c in idx]
    def D(self, expr, c):
        expr = sp.sympify(expr)
        out = 0
        for sym in expr.free_symbols:
            if sym in self.rules:
                out += sp.diff(expr, sym)*self.rules[sym][c]
        return out

J = Jet(); J.add_omega()

def build_matter(xi_val, complex_H=True, gauge=True, ym=True, real_scalar=False):
    """returns That_ab (lower indices, physical) as expression in jets, and the jet object"""
    fields = []
    if real_scalar:
        p = Field(*jets3('p')); fields = [p]; comps = [(p, None)]
    else:
        p = Field(*jets3('p')); q = Field(*jets3('q')); fields = [p, q]; comps = [(p, q)]
    for f in fields: J.add_field(f)
    if gauge:
        A = [sp.Symbol(f'A{a}', real=True) for a in idx]
        dA = [[sp.Symbol(f'dA{b}_{a}', real=True) for a in idx] for b in idx]
        ddA = [[[sp.Symbol(f'ddA{min(c,b)}{max(c,b)}_{a}', real=True) for a in idx] for b in idx] for c in idx]
        J.add_A(A, dA, ddA)
    else:
        A = [0]*4; dA = [[0]*4 for _ in idx]; ddA = None
    # physical field H = Omega * H_r, H_r = (p + i q)/sqrt(2)  (real scalar: phi = Omega p)
    if real_scalar:
        Hr = p.v; dHr = [p.d(a) for a in idx]
        H = W*Hr
        DH = [W*dHr[a] + n[a]*Hr for a in idx]             # d_a H
        DHc = DH
        absH2 = H**2
        kin = sum(eta[a, b]*DH[a]*DH[b] for a in idx for b in idx)*W**2   # ghat^{ab} d_a phi d_b phi (ghat^{ab} = W^2 eta^{ab})
        # Friedrich (3.2): T = dphi dphi - ghat (1/2 (dphi.dphi + m^2 phi^2) + V), V = lambda_h phi^4 (U const)
        def T_ab(a, b):
            return DH[a]*DH[b] - ghat[a, b]*(R(1, 2)*(kin + m**2*absH2) + lamh*absH2**2)
        Vxi_base = absH2  # phi^2
    else:
        Hr = (p.v + I*q.v)/sp.sqrt(2)
        dHr = [(p.d(a) + I*q.d(a))/sp.sqrt(2) for a in idx]
        H = W*Hr
        DH = [W*dHr[a] + n[a]*Hr - I*e*A[a]*H for a in idx]          # D_a H = d_a H - i e A_a H
        DHc = [sp.conjugate(x) for x in DH]
        absH2 = sp.expand(H*sp.conjugate(H))
        kin = sum(eta[a, b]*DHc[a]*DH[b] for a in idx for b in idx)*W**2  # ghat^{ab} (D_a H)^* D_b H
        def T_ab(a, b):
            return DHc[a]*DH[b] + DHc[b]*DH[a] - ghat[a, b]*(kin + m**2*absH2 + lamh*absH2**2)
        Vxi_base = 2*absH2  # sum phi_i^2
    That = sp.zeros(4)
    for a in idx:
        for b in idx:
            That[a, b] = T_ab(a, b)
    # non-minimal coupling: T^xi = xi (Ghat_ab + ghat_ab boxhat - nablahat_a nablahat_b) (sum phi_i^2)
    if xi_val != 0:
        f = sp.expand(Vxi_base)
        def nabhat2(a, b):   # nablahat_a nablahat_b f
            return J.D(J.D(f, b), a) - sum(Gh(c, a, b)*J.D(f, c) for c in idx)
        N2 = sp.zeros(4)
        for a in idx:
            for b in idx:
                N2[a, b] = nabhat2(a, b)
        boxf = sum(ghatinv[a, b]*N2[a, b] for a in idx for b in idx)
        # Ghat_ab from (2.3), (2.4) with g flat: Rhat_ab = 2 W^-1 ddO + (W^-1 boxO - 3 W^-2 n.n) eta ; Rhat = W^2 (6 W^-1 boxO - 12 W^-2 n.n)
        nn = sum(eta[a, b]*n[a]*n[b] for a in idx for b in idx)
        boxO = sum(eta[a, b]*ddO(a, b) for a in idx for b in idx)
        Rhat = W**2*(6*boxO/W - 12*nn/W**2)
        Ghat = sp.zeros(4)
        for a in idx:
            for b in idx:
                Rab = 2*ddO(a, b)/W + (boxO/W - 3*nn/W**2)*eta[a, b]
                Ghat[a, b] = Rab - R(1, 2)*Rhat*ghat[a, b]
        for a in idx:
            for b in idx:
                That[a, b] += xi_val*(Ghat[a, b]*f + ghat[a, b]*boxf - N2[a, b])
    # Yang-Mills
    if ym and gauge:
        F = [[dA[a][b] - dA[b][a] for b in idx] for a in idx]
        F2 = sum(ghatinv[a, c]*ghatinv[b, d]*F[a][b]*F[c][d] for a in idx for b in idx for c in idx for d in idx)
        for a in idx:
            for b in idx:
                That[a, b] += sum(ghatinv[c, d]*F[a][c]*F[b][d] for c in idx for d in idx) - R(1, 4)*ghat[a, b]*F2
    That = That.applyfunc(sp.expand)
    extra = dict(Hr=Hr, absH2=absH2, A=A, dA=dA, DH=DH)
    return That, extra

def laurent(expr, lo=-4, hi=6):
    """dict power -> coefficient in W"""
    expr = sp.expand(expr)
    out = {}
    for k in range(lo, hi+1):
        c = expr.coeff(W, k)
        if c != 0: out[k] = c
    return out

def reduce_nn(expr):
    """polynomial reduction modulo (3.8): n0^2 = n1^2+n2^2+n3^2 + lambda/3 - 2 W s - kappa/12 W^2 Str"""
    gen = n[0]**2 - (n[1]**2 + n[2]**2 + n[3]**2 + lam/3 - 2*W*s - kap/12*W**2*Str)
    expr = sp.expand(expr)
    # make polynomial in W
    K = 4
    P = sp.expand(expr*W**K)
    r = sp.rem(sp.Poly(P, n[0]), sp.Poly(gen, n[0]))
    return sp.expand(r.as_expr()/W**K)

def cotton_source(That):
    """2 Omega^-1 nablahat_[nu Lhat_lambda] rho with Lhat = kappa/2 (That - 1/3 Thathat ghat) + lambda/6 ghat"""
    tr = sum(ghatinv[a, b]*That[a, b] for a in idx for b in idx)
    Lh = sp.zeros(4)
    for a in idx:
        for b in idx:
            Lh[a, b] = kap/2*(That[a, b] - R(1, 3)*tr*ghat[a, b]) + lam/6*ghat[a, b]
    def nabL(c, a, b):   # nablahat_c Lhat_ab
        return J.D(Lh[a, b], c) - sum(Gh(d, c, a)*Lh[d, b] + Gh(d, c, b)*Lh[a, d] for d in idx)
    out = {}
    for rho in idx:
        for nu in idx:
            for la in range(nu+1, 4):
                out[(rho, nu, la)] = sp.expand((nabL(nu, la, rho) - nabL(la, nu, rho))/W)   # 2 W^-1 * (1/2)(...)
    return out, tr

def report_sector(label, xi_val, **kw):
    print(f"\n=== {label} ===")
    That, ex = build_matter(xi_val, **kw)
    tr = sum(ghatinv[a, b]*That[a, b] for a in idx for b in idx)
    lowT = min(min(laurent(reduce_nn(That[a, b])).keys(), default=99) for a in idx for b in idx)
    lowtr = min(laurent(reduce_nn(tr/W**2)).keys(), default=99)
    print(f"  lowest power of Omega in That_ab (lower indices): {lowT}  (>= 0 regular)")
    print(f"  lowest power of Omega in Omega^-2 That (trace, Friedrich's T*): {lowtr}  (>= 0 regular)")
    src, _ = cotton_source(That)
    coef = {-3: {}, -2: {}, -1: {}}
    lowest = 99
    for key, val in src.items():
        red = reduce_nn(val)
        lv = laurent(red)
        if lv: lowest = min(lowest, min(lv.keys()))
        for k in coef:
            if k in lv: coef[k][key] = sp.factor(lv[k])
    print(f"  lowest power of Omega in (2.17) source after substitutions (2.14),(2.15),(3.8): {lowest}")
    return That, ex, src, coef

if __name__ == '__main__':
    sp.init_printing(wrap_line=False)
    # ---------------- (A) Yang-Mills weights
    print("(A) Yang-Mills: sqrt(-ghat) ghat^{ma} ghat^{nb} / (sqrt(-g) g^{ma} g^{nb}) =",
          sp.simplify((W**-4)*(W**2)*(W**2)), "(1 means conformal invariance of the YM equation in 4D; "
          "YM equation rescaled: nabla_mu F^{mu nu} = j_r^nu with J^nu = Omega^4 j_r^nu)")
    # Higgs current: J_a = i e (H^* D_a H - (D_a H)^* H)
    Th0, ex0 = build_matter(0, complex_H=True, gauge=True, ym=False)
    H = W*ex0['Hr']; DH = ex0['DH']
    Jlow = [sp.expand(I*e*(sp.conjugate(H)*DH[a] - sp.conjugate(DH[a])*H)) for a in idx]
    print("    Higgs current J_a (lower) lowest Omega power:", min(min(laurent(x).keys()) for x in Jlow),
          "; J_a / Omega^2 free of n_a (dOmega):", all(sp.expand(x/W**2).has(*n) is False for x in Jlow),
          "-> J^nu = ghat^{nu a} J_a = Omega^4 j_r^nu")
    print("    Dirac current: psibar gammahat_a psi = Omega^{3/2} Omega^{-1} Omega^{3/2} psibar_r gamma_a psi_r = Omega^2 j_r,a -> J^nu = Omega^4 j_r^nu (weights, see (D))")

    # ---------------- (B) Higgs equation
    print("\n(B) Higgs equation: conformal covariance of boxhat_D - Rhat/6 with gauge field, off shell")
    Hr = ex0['Hr']
    DHc = [W*J.D(Hr, a) + n[a]*Hr - I*e*ex0['A'][a]*H for a in idx]   # D_a H
    def Dhat2(a, b):   # nablahat_a D_b H - i e A_a D_b H  (gauge-covariant second derivative on hat metric)
        return J.D(DHc[b], a) - I*e*ex0['A'][a]*DHc[b] - sum(Gh(c, a, b)*DHc[c] for c in idx)
    boxhatH = sum(ghatinv[a, b]*Dhat2(a, b) for a in idx for b in idx)
    nn = sum(eta[a, b]*n[a]*n[b] for a in idx for b in idx)
    boxO = sum(eta[a, b]*ddO(a, b) for a in idx for b in idx)
    Rhat = W**2*(6*boxO/W - 12*nn/W**2)
    lhs = sp.expand(W**-3*(boxhatH - Rhat/6*H))
    DHr = [J.D(Hr, a) - I*e*ex0['A'][a]*Hr for a in idx]
    boxHr = sum(eta[a, b]*(J.D(DHr[b], a) - I*e*ex0['A'][a]*DHr[b]) for a in idx for b in idx)
    print("    Omega^-3 (boxhat_D - Rhat/6)[Omega H_r] - box_D[H_r] = 0 (R = 0 for flat g):", sp.simplify(sp.expand(lhs - boxHr)) == 0)
    # rescaled Higgs equation: boxhat_D H - m^2 H - 2 lambda_h |H|^2 H - xi Rhat H + Yuk = 0
    # => box_D H_r = Omega^-3 [ (m^2 + (xi - 1/6) Rhat) H + 2 lambda_h |H|^2 H - Yuk ]
    Rhat_sub = 4*lam - kap*W**2*Str     # (2.2) with That = Omega^2 Str
    coefm2 = sp.expand(W**-3*(m**2 + (xi - R(1, 6))*Rhat_sub)*H)
    print("    coefficient structure: Omega^-3 (m^2 + (xi-1/6) Rhat) H =", sp.collect(sp.expand(coefm2/Hr), W))
    print("    -> singular part Omega^-2 (m^2 + 4 lambda xi - 2 lambda/3) H_r ; regular part -(xi-1/6) kappa Str H_r")
    print("    quartic: Omega^-3 2 lambda_h |H|^2 H = ", sp.expand(W**-3*2*lamh*ex0['absH2']*H/Hr), "* H_r (order 0) ; Yukawa: Omega^-3 y psibar psi = y psibar_r psi_r (order 0)")

    # ---------------- (C) geometric sector
    # calibration 1: Friedrich's real scalar, xi = 0
    T1, ex1, src1, c1 = report_sector("(C1) calibration: real scalar, xi = 0, no gauge (Friedrich th. 3.1)", 0, complex_H=False, gauge=False, ym=False, real_scalar=True)
    p = sp.Symbol('p', real=True)
    pred = {}
    for (rho, nu, la), v in src1.items():
        pred[(rho, nu, la)] = sp.expand(kap/3*(m**2 - 2*lam/3)*p**2*R(1, 2)*(n[nu]*eta[la, rho] - n[la]*eta[nu, rho]))
    ok2 = all(sp.simplify(c1[-2].get(k, 0) - pred[k]) == 0 for k in src1)
    print("  Omega^-2 coefficient == (kappa/3)(m^2 - 2 lambda/3) p^2 n_[nu eta_lambda]rho :", ok2)
    msp = {m: sp.sqrt(2*lam/3)}
    print("  Omega^-2 coefficient vanishes at m^2 = 2 lambda/3 :", all(sp.simplify(v.subs(msp)) == 0 for v in c1[-2].values()))
    print("  Omega^-1 coefficient vanishes at m^2 = 2 lambda/3 :", all(sp.simplify(v.subs(msp)) == 0 for v in c1[-1].values()))
    print("  Omega^-1 coefficient non-zero for generic m (example component):", [sp.factor(v) for v in list(c1[-1].values())[:1]])
    print("  Omega^-3 terms:", len(c1[-3]))

    # full system: complex Higgs + gauge + YM + xi
    T2, ex2, src2, c2 = report_sector("(C2) full: complex Higgs doublet component, gauge field, Yang-Mills, non-minimal xi", xi, complex_H=True, gauge=True, ym=True)
    pq2 = sp.expand(ex2['absH2']/W**2)   # |H_r|^2
    pred2 = {}
    for (rho, nu, la), v in src2.items():
        pred2[(rho, nu, la)] = sp.expand(kap/3*(m**2 + 4*lam*xi - 2*lam/3)*pq2*(n[nu]*eta[la, rho] - n[la]*eta[nu, rho]))
    ok2b = all(sp.simplify(c2[-2].get(k, 0) - pred2[k]) == 0 for k in src2)
    print("  Omega^-2 coefficient == (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) 2|H_r|^2 n_[nu eta_lambda]rho :", ok2b)
    msub = {m: sp.sqrt(2*lam/3 - 4*lam*xi)}
    v2 = all(sp.simplify(v.subs(msub)) == 0 for v in c2[-2].values())
    v1 = all(sp.simplify(v.subs(msub)) == 0 for v in c2[-1].values())
    print("  at m^2 + 4 lambda xi = 2 lambda/3 : Omega^-2 coefficient vanishes :", v2, "; Omega^-1 coefficient vanishes :", v1)
    print("  Omega^-3 terms:", len(c2[-3]))
    # which symbols appear in the singular coefficients (gauge field? YM? Yukawa?)
    syms = set()
    for k in (-2, -1):
        for v in c2[k].values(): syms |= v.free_symbols
    print("  symbols in the singular coefficients:", sorted(str(x) for x in syms))
    print("  gauge potential A, dA or lambda_h present in singular coefficients:", any(str(x).startswith(('A', 'dA', 'ddA', 'lambda_h')) for x in syms))
    # calibration 2: xi = 1/6, m = 0
    print("  calibration 2 (xi = 1/6, m = 0): all singular coefficients vanish :",
          all(sp.simplify(v.subs({xi: R(1, 6), m: 0})) == 0 for k in (-3, -2, -1) for v in c2[k].values()))
    # iff: generic non-vanishing
    print("  generic (xi, m): Omega^-2 coefficient non-zero (example):", sp.factor(list(c2[-2].values())[0]))

    # ---------------- (D) Dirac sector, signature (+,-,-,-), as in ED (ed_check.py), with gauge field and Yukawa mass
    print("\n(D) Dirac sector (+,-,-,-), jets, gauge field A (weight 0), Yukawa mass y H = y Omega H_r")
    etaD = sp.diag(1, -1, -1, -1)
    s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
    Z = sp.zeros(2); E2 = sp.eye(2)
    def blk(a, b, c, d): return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
    g0 = blk(E2, Z, Z, -E2); gs = [blk(Z, t, -t, Z) for t in (s1, s2, s3)]
    gup = [g0] + gs; glo = [sum((etaD[a, b]*gup[b] for b in idx), sp.zeros(4)) for a in idx]
    Om = W
    dOm = n
    ar = sp.symbols('a0:4', real=True); br = sp.symbols('b0:4', real=True)
    dar = [sp.symbols(f'da{mu}_0:4', real=True) for mu in idx]; dbr = [sp.symbols(f'db{mu}_0:4', real=True) for mu in idx]
    ph = sp.Matrix([ar[i] + I*br[i] for i in range(4)])
    dph = [sp.Matrix([dar[mu][i] + I*dbr[mu][i] for i in range(4)]) for mu in idx]
    AD = sp.symbols('A0:4', real=True); y = sp.Symbol('y', real=True); hr = sp.Symbol('h_r', real=True)
    def bar(v): return (v.H)*g0
    psi = Om**R(3, 2)*ph
    dpsi = [Om**R(3, 2)*dph[mu] + R(3, 2)*Om**R(1, 2)*dOm[mu]*ph for mu in idx]
    dsig = [-dOm[mu]/Om for mu in idx]
    Gam = [R(1, 4)*sum(((glo[mu]*gup[nu] - gup[nu]*glo[mu])*dsig[nu] for nu in idx), sp.zeros(4)) for mu in idx]
    ghat_lo = [Om**-1*glo[mu] for mu in idx]; ghat_up = [Om*gup[mu] for mu in idx]
    nabla = [dpsi[mu] + Gam[mu]*psi - I*e*AD[mu]*psi for mu in idx]
    dirac_hat = sum((I*ghat_up[mu]*nabla[mu] for mu in idx), sp.zeros(4, 1)) - y*Om*hr*psi
    dirac_r = sum((I*gup[mu]*(dph[mu] - I*e*AD[mu]*ph) for mu in idx), sp.zeros(4, 1)) - y*hr*ph
    print("    (i gammahat.Dhat - y Omega h_r) psi - Omega^{5/2} (i gamma.D - y h_r) psi_r = 0 off shell:",
          sp.simplify(sp.expand(dirac_hat - Om**R(5, 2)*dirac_r)) == sp.zeros(4, 1), "-> rescaled Dirac coefficient y h_r, regular")
    def Tkin(psi_, nab_, nabb_, gl):
        pb = bar(psi_); T = sp.zeros(4)
        for mu in idx:
            for nu in idx:
                T[mu, nu] = (I/4)*((pb*gl[mu]*nab_[nu])[0] + (pb*gl[nu]*nab_[mu])[0] - (nabb_[nu]*gl[mu]*psi_)[0] - (nabb_[mu]*gl[nu]*psi_)[0])
        return T
    nabb = [bar(dpsi[mu]) - bar(psi)*Gam[mu] + I*e*AD[mu]*bar(psi) for mu in idx]
    That_D = Tkin(psi, nabla, nabb, ghat_lo)
    nab_r = [dph[mu] - I*e*AD[mu]*ph for mu in idx]; nabb_r = [bar(dph[mu]) + I*e*AD[mu]*bar(ph) for mu in idx]
    T_r = Tkin(ph, nab_r, nabb_r, glo)
    print("    kinetic tensor with gauge field: That[psi; ghat, A] - Omega^2 T[psi_r; eta, A] = 0 off shell:",
          (That_D - Om**2*T_r).applyfunc(lambda z: sp.simplify(sp.expand(z))) == sp.zeros(4))
    Lag = (bar(psi)*sum((I*ghat_up[mu]*nabla[mu] for mu in idx), sp.zeros(4, 1)))[0] - y*Om*hr*(bar(psi)*psi)[0]
    Lag_r = (bar(ph)*sum((I*gup[mu]*nab_r[mu] for mu in idx), sp.zeros(4, 1)))[0] - y*hr*(bar(ph)*ph)[0]
    print("    Lagrangian: Lag[psi; ghat, A, yH] - Omega^4 psibar_r (i gamma.D - y h_r) psi_r = 0 off shell:",
          sp.simplify(sp.expand(Lag - Om**4*Lag_r)) == 0,
          "-> ghat Lag = Omega^2 (...) eta : order Omega^2 in Lhat, (2.17) regular (ED part D, power 2 -> lowest 0);"
          " with constant mass instead (y h_r -> m/Omega) the mass term of ghat Lag is order Omega^1 (ED-3)")
    print("    constant-mass control: Omega^-2 * Omega^4 * (m/Omega) psibar_r psi_r = order", sp.Poly(sp.expand(Om**-2*Om**4*(1/Om)*Om**3), Om).monoms()[0][0] - 3, "(Omega^1)")
