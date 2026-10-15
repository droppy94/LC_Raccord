#!/usr/bin/env python3
"""
fw3_fa2_lib.py -- bibliotheque de l'audit FA-2. Copie modifiee et parametree de fw3_check.py (original non touche).
Modifications par rapport a l'original :
  * DDS_FACTOR : facteur devant le terme de trace de (2.15). Original : -(kappa/24) * Omega * d(Omega^2 Str).
    Friedrich (2.8)/(2.15) : -(kappa/24) * Omega^-1 * d(Omega^2 Str). Les deux sont testables (E2).
  * build_matter : n_comp composantes complexes (E3b), tenseur generique Omega^2 Y_ab ajoute (E3a),
    terme cubique mu |H|^3 ou mu phi^3 (E3c), terme « Majorana-like » M Omega eta_ab B (E3c).
  * reduce_nn : choix de la variable de reduction (n0 ou n1) pour (3.8) (E2).
  * NREDUCE : variable eliminee par (3.8).
"""
import sympy as sp
I = sp.I
R = sp.Rational

W = sp.symbols('Omega', positive=True)
n = sp.symbols('n0:4', real=True)
s = sp.symbols('s', real=True)
lam, kap, m, xi, lamh, e, mu, MM = sp.symbols('lambda kappa m xi lambda_h e mu M', real=True)
eta = sp.diag(-1, 1, 1, 1)
idx = range(4)

def sym2(name):
    Mx = sp.zeros(4)
    for a in idx:
        for b in idx:
            Mx[a, b] = sp.Symbol(f'{name}{min(a,b)}{max(a,b)}', real=True)
    return Mx
L = sym2('L'); S = sym2('S')
dL = [sym2(f'dL{c}_') for c in idx]; dS = [sym2(f'dS{c}_') for c in idx]
Str = sp.Symbol('Str', real=True); dStr = sp.symbols('dStr0:4', real=True)
# tenseur generique Y (E3a) et scalaire generique B (E3c)
Y = sym2('Y'); dY = [sym2(f'dY{c}_') for c in idx]
B = sp.Symbol('B', real=True); dB = sp.symbols('dB0:4', real=True)

DDS_FACTOR = {'orig': W, 'friedrich': 1/W}
NREDUCE = 0

def jets3(name):
    v = sp.Symbol(name, real=True)
    d1 = [sp.Symbol(f'd{name}_{a}', real=True) for a in idx]
    d2 = [[sp.Symbol(f'd{name}_{min(a,b)}{max(a,b)}', real=True) for b in idx] for a in idx]
    d3 = [[[sp.Symbol(f'd{name}_' + ''.join(str(k) for k in sorted((a, b, c))), real=True) for c in idx] for b in idx] for a in idx]
    return v, d1, d2, d3

nup = [sum(eta[r, t]*n[t] for t in idx) for r in idx]

def make_omega(dds_mode='orig'):
    fac = DDS_FACTOR[dds_mode]
    def dds(c):
        return (-sum(nup[r]*L[r, c] for r in idx) + kap/2*sum(nup[r]*S[r, c] for r in idx)
                - kap/24*fac*(2*W*n[c]*Str + W**2*dStr[c]))
    def ddO(a, b):
        return s*eta[a, b] - W*L[a, b] + kap/2*W*S[a, b]
    return dds, ddO

def Gh(a, b, c):
    return -((1 if a == b else 0)*n[c] + (1 if a == c else 0)*n[b] - eta[b, c]*nup[a])/W
ghat = W**-2*eta; ghatinv = W**2*eta

class Field:
    def __init__(self, v, d1, d2, d3):
        self.v, self.d1, self.d2, self.d3 = v, d1, d2, d3
    def d(self, a): return self.d1[a]

class Jet:
    def __init__(self, dds_mode='orig'):
        self.rules = {}
        self.dds, self.ddO = make_omega(dds_mode)
        self.rules[W] = [n[a] for a in idx]
        for a in idx:
            self.rules[n[a]] = [self.ddO(a, b) for b in idx]
        self.rules[s] = [self.dds(c) for c in idx]
        for a in idx:
            for b in idx:
                self.rules[L[a, b]] = [dL[c][a, b] for c in idx]
                self.rules[S[a, b]] = [dS[c][a, b] for c in idx]
                self.rules[Y[a, b]] = [dY[c][a, b] for c in idx]
        self.rules[Str] = [dStr[c] for c in idx]
        self.rules[B] = [dB[c] for c in idx]
    def add_field(self, f):
        self.rules[f.v] = [f.d1[a] for a in idx]
        for a in idx:
            self.rules[f.d1[a]] = [f.d2[a][b] for b in idx]
            for b in idx:
                self.rules[f.d2[a][b]] = [f.d3[a][b][c] for c in idx]
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

def build_matter(J, xi_val, gauge=True, ym=True, real_scalar=False, n_comp=1,
                 add_Y=False, cubic=False, majorana_like=False):
    """That_ab (indices bas, physique) en fonction des jets."""
    fields = []
    if gauge:
        A = [sp.Symbol(f'A{a}', real=True) for a in idx]
        dA = [[sp.Symbol(f'dA{b}_{a}', real=True) for a in idx] for b in idx]
        ddA = [[[sp.Symbol(f'ddA{min(c,b)}{max(c,b)}_{a}', real=True) for a in idx] for b in idx] for c in idx]
        J.add_A(A, dA, ddA)
    else:
        A = [0]*4; dA = [[0]*4 for _ in idx]; ddA = None
    That = sp.zeros(4)
    if real_scalar:
        p = Field(*jets3('p')); J.add_field(p)
        Hr = p.v; H = W*Hr
        DH = [W*p.d(a) + n[a]*Hr for a in idx]
        absH2 = H**2
        kin = sum(eta[a, b]*DH[a]*DH[b] for a in idx for b in idx)*W**2
        V = lamh*absH2**2 + (mu*H**3 if cubic else 0)
        for a in idx:
            for b in idx:
                That[a, b] = DH[a]*DH[b] - ghat[a, b]*(R(1, 2)*(kin + m**2*absH2) + V)
        Vxi_base = absH2
        extra = dict(Hr=Hr, absH2=absH2, A=A, dA=dA, DH=DH, comps=[(p.v, 0)])
    else:
        comps = []
        kin = 0; absH2 = 0; Hr_list = []; DH_list = []
        for i in range(n_comp):
            suf = '' if i == 0 else str(i + 1)
            p = Field(*jets3('p' + suf)); q = Field(*jets3('q' + suf)); J.add_field(p); J.add_field(q)
            Hr = (p.v + I*q.v)/sp.sqrt(2)
            dHr = [(p.d(a) + I*q.d(a))/sp.sqrt(2) for a in idx]
            H = W*Hr
            DH = [W*dHr[a] + n[a]*Hr - I*e*A[a]*H for a in idx]
            DHc = [sp.conjugate(x) for x in DH]
            absH2 += sp.expand(H*sp.conjugate(H))
            kin += sum(eta[a, b]*DHc[a]*DH[b] for a in idx for b in idx)*W**2
            for a in idx:
                for b in idx:
                    That[a, b] += DHc[a]*DH[b] + DHc[b]*DH[a]
            comps.append((p.v, q.v)); Hr_list.append(Hr); DH_list.append(DH)
        absH2 = sp.expand(absH2)
        # |H|^3 = Omega^3 (sum (p_i^2+q_i^2)/2)^{3/2}
        V = lamh*absH2**2 + (mu*W**3*sp.expand(absH2/W**2)**R(3, 2) if cubic else 0)
        for a in idx:
            for b in idx:
                That[a, b] += -ghat[a, b]*(kin + m**2*absH2 + V)
        Vxi_base = 2*absH2
        extra = dict(Hr=Hr_list[0], absH2=absH2, A=A, dA=dA, DH=DH_list[0], comps=comps)
    if xi_val != 0:
        f = sp.expand(Vxi_base)
        def nabhat2(a, b):
            return J.D(J.D(f, b), a) - sum(Gh(c, a, b)*J.D(f, c) for c in idx)
        N2 = sp.zeros(4)
        for a in idx:
            for b in idx:
                N2[a, b] = nabhat2(a, b)
        boxf = sum(ghatinv[a, b]*N2[a, b] for a in idx for b in idx)
        nn = sum(eta[a, b]*n[a]*n[b] for a in idx for b in idx)
        boxO = sum(eta[a, b]*J.ddO(a, b) for a in idx for b in idx)
        Rhat = W**2*(6*boxO/W - 12*nn/W**2)
        for a in idx:
            for b in idx:
                Rab = 2*J.ddO(a, b)/W + (boxO/W - 3*nn/W**2)*eta[a, b]
                Ghat_ab = Rab - R(1, 2)*Rhat*ghat[a, b]
                That[a, b] += xi_val*(Ghat_ab*f + ghat[a, b]*boxf - N2[a, b])
    if ym and gauge:
        F = [[dA[a][b] - dA[b][a] for b in idx] for a in idx]
        F2 = sum(ghatinv[a, c]*ghatinv[b, d]*F[a][b]*F[c][d] for a in idx for b in idx for c in idx for d in idx)
        for a in idx:
            for b in idx:
                That[a, b] += sum(ghatinv[c, d]*F[a][c]*F[b][d] for c in idx for d in idx) - R(1, 4)*ghat[a, b]*F2
    if add_Y:          # E3a : tenseur generique regulier Omega^2 Y_ab (ex. : tenseur cinetique de Dirac, partie D)
        for a in idx:
            for b in idx:
                That[a, b] += W**2*Y[a, b]
    if majorana_like:  # E3c : terme de type ghat_ab M psi^T C psi = M Omega eta_ab B, B = bilineaire rescale generique
        for a in idx:
            for b in idx:
                That[a, b] += MM*W*eta[a, b]*B
    That = That.applyfunc(sp.expand)
    return That, extra

def laurent(expr, lo=-6, hi=8):
    expr = sp.expand(expr)
    out = {}
    for k in range(lo, hi+1):
        c = expr.coeff(W, k)
        if c != 0: out[k] = c
    return out

def reduce_nn(expr, var=None):
    """reduction polynomiale modulo (3.8) ; var = indice de la composante de n eliminee (0 par defaut)"""
    if var is None: var = NREDUCE
    others = [n[i]**2*eta[i, i] for i in idx if i != var]
    # eta^{ab} n_a n_b = -n0^2 + n1^2 + n2^2 + n3^2 = -lambda/3 + 2 W s + kappa/12 W^2 Str
    rhs = -lam/3 + 2*W*s + kap/12*W**2*Str
    gen = sp.expand(eta[var, var]*n[var]**2 + sum(others) - rhs)   # = 0
    expr = sp.expand(expr)
    K = 6
    P = sp.expand(expr*W**K)
    r = sp.rem(sp.Poly(P, n[var]), sp.Poly(gen, n[var]))
    return sp.expand(r.as_expr()/W**K)

def cotton_source(J, That):
    tr = sum(ghatinv[a, b]*That[a, b] for a in idx for b in idx)
    Lh = sp.zeros(4)
    for a in idx:
        for b in idx:
            Lh[a, b] = kap/2*(That[a, b] - R(1, 3)*tr*ghat[a, b]) + lam/6*ghat[a, b]
    def nabL(c, a, b):
        return J.D(Lh[a, b], c) - sum(Gh(d, c, a)*Lh[d, b] + Gh(d, c, b)*Lh[a, d] for d in idx)
    out = {}
    for rho in idx:
        for nu in idx:
            for la in range(nu+1, 4):
                out[(rho, nu, la)] = sp.expand((nabL(nu, la, rho) - nabL(la, nu, rho))/W)
    return out, tr

def antisym(nu, la, rho):
    return R(1, 2)*(n[nu]*eta[la, rho] - n[la]*eta[nu, rho])

def sector(label, xi_val, dds_mode='orig', var=None, **kw):
    print(f"\n=== {label} ===")
    print(f"  options: xi={xi_val}, dds_mode={dds_mode}, reduction via n{NREDUCE if var is None else var}, {kw}")
    J = Jet(dds_mode)
    That, ex = build_matter(J, xi_val, **kw)
    tr = sum(ghatinv[a, b]*That[a, b] for a in idx for b in idx)
    lowT = min(min(laurent(reduce_nn(That[a, b], var)).keys(), default=99) for a in idx for b in idx)
    lowtr = min(laurent(reduce_nn(tr/W**2, var)).keys(), default=99)
    print(f"  plus basse puissance de Omega dans That_ab : {lowT} ; dans Omega^-2 That : {lowtr}")
    src, _ = cotton_source(J, That)
    raw_low = min(min(laurent(v).keys(), default=99) for v in src.values())
    print(f"  plus basse puissance AVANT reduction (3.8) : {raw_low}  (doit etre >= -K pour que la reduction soit polynomiale)")
    coef = {k: {} for k in range(-6, 0)}
    lowest = 99
    for key, val in src.items():
        red = reduce_nn(val, var)
        lv = laurent(red)
        if lv: lowest = min(lowest, min(lv.keys()))
        for k in coef:
            if k in lv: coef[k][key] = sp.factor(lv[k])
    print(f"  plus basse puissance de Omega dans la source de (2.17) apres (2.14),(2.15),(3.8) : {lowest}")
    for k in sorted(coef):
        if coef[k]: print(f"  nombre de composantes non nulles a l'ordre Omega^{k} : {len(coef[k])}")
    return That, ex, src, coef, J

def check_K6(coef, ex, src, label=''):
    """K-6 : Omega^-2 == (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) Sum_i phi_i^2 n_[nu eta_lambda]rho ; Omega^-1 nul a la condition"""
    sumphi2 = sum(p**2 + q**2 for p, q in ex['comps'])
    pred = {k: sp.expand(kap/3*(m**2 + 4*lam*xi - 2*lam/3)*sumphi2*antisym(k[1], k[2], k[0])) for k in src}
    ok = all(sp.simplify(coef[-2].get(k, 0) - pred[k]) == 0 for k in src)
    print(f"  {label} Omega^-2 == (kappa/3)(m^2 + 4 lambda xi - 2 lambda/3) ({sumphi2}) n_[nu eta_lambda]rho : {ok}")
    msub = {m: sp.sqrt(2*lam/3 - 4*lam*xi)}
    v2 = all(sp.simplify(v.subs(msub)) == 0 for v in coef[-2].values())
    v1 = all(sp.simplify(v.subs(msub)) == 0 for v in coef[-1].values())
    v3 = all(len(coef[k]) == 0 for k in coef if k <= -3)
    print(f"  {label} a m^2 + 4 lambda xi = 2 lambda/3 : Omega^-2 nul : {v2} ; Omega^-1 nul : {v1} ; aucun Omega^-3 ou moins : {v3}")
    syms = set()
    for k in (-2, -1):
        for v in coef[k].values(): syms |= v.free_symbols
    print(f"  {label} symboles dans les coefficients singuliers : {sorted(str(x) for x in syms)}")
    return ok and v2 and v1 and v3
