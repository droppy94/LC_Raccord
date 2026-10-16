#!/usr/bin/env python3
"""
af_check.py (v2 ; v1 conservee : af_check_v1_defectueux.py, signe de la partie spatiale du Weyl, symboles de calibration, jets de F) -- NOTE-197 (chantier AF). Formal regularity, in Friedrich's sense, of the local Wess-Zumino terms
  (AF-1) c-part   T_ab = c0 b d^c d^d (sigma C_acbd),  sigma = -ln Omega,  C = Omega W   (G-V3)
  (AF-2) sigma F^2 beta_* Int sqrt(g) sigma F^2  (running Maxwell coupling)                 (M-V3)
Conventions of Friedrich: signature (-,+,+,+), ghat = Omega^-2 g, g = eta at zeroth order (de Sitter is conformally flat).
First order in perturbations (linear in W, or quadratic-in-F Maxwell stress times beta_*): at this order
  d_a d_b Omega = s eta_ab,  d_c s = 0,  higher derivatives of Omega = 0,  n.n = -lambda/3 + 2 Omega s   ((2.14), (2.15), (3.8)).
Unknowns: Omega, n_a = d_a Omega, s, and generic jets of W (via E_ij, B_ij relative to the x0 axis: any Weyl tensor)
or of F. c0 = -8 as in irr_c.py (NOTE-125), the sign follows the convention for T (NOTE-128).
"""
import itertools
import sympy as sp

X = sp.symbols('x0:4', real=True)
idx = range(4)
eta = sp.diag(-1, 1, 1, 1)
Om_f = sp.Function('O')(*X)
W = sp.Symbol('Omega', positive=True)
n = sp.symbols('n0:4', real=True)
s, lam, kap, b, c0, betas, e2 = sp.symbols('s lambda kappa b c0 beta_* e2', real=True)
LOG = sp.Symbol('LOG', real=True)          # stands for ln Omega

def subs_omega(expr):
    """formal substitutions for derivatives of Omega (first order), then Omega -> symbol"""
    expr = sp.sympify(expr)
    reps = {}
    for dv in expr.atoms(sp.Derivative):
        if dv.expr == Om_f:
            vars_ = [v for v, k in dv.variable_count for _ in range(k)]
            if len(vars_) == 1:
                reps[dv] = n[X.index(vars_[0])]
            elif len(vars_) == 2:
                reps[dv] = s*eta[X.index(vars_[0]), X.index(vars_[1])]
            else:
                reps[dv] = 0
    expr = expr.xreplace(reps)
    expr = expr.xreplace({sp.log(Om_f): LOG}).xreplace({Om_f: W})
    return sp.expand(expr)

def reduce_nn(expr, K=8):
    """(3.8) at zeroth order: n0^2 = n1^2 + n2^2 + n3^2 + lambda/3 - 2 Omega s"""
    gen = n[0]**2 - (n[1]**2 + n[2]**2 + n[3]**2 + lam/3 - 2*W*s)
    P = sp.expand(expr*W**K)
    r = sp.rem(sp.Poly(P, n[0]), sp.Poly(gen, n[0]))
    return sp.expand(r.as_expr()/W**K)

def laurent_log(expr, lo=-4, hi=3):
    """dict (power, logpower) -> coefficient"""
    expr = sp.expand(expr)
    out = {}
    for lp in range(0, 3):
        el = expr.coeff(LOG, lp)
        for k in range(lo, hi + 1):
            c = sp.expand(el.coeff(W, k))
            if c != 0:
                out[(k, lp)] = c
    return out

# ---------------------------------------------------------------- generic Weyl tensor (E, B relative to x0)
def sym_traceless(name):
    f = {}
    for i, j in [(1, 1), (2, 2), (1, 2), (1, 3), (2, 3)]:
        f[(i, j)] = sp.Function(f'{name}{i}{j}')(*X)
    M = sp.zeros(4)
    for (i, j), v in f.items():
        M[i, j] = v; M[j, i] = v
    M[3, 3] = -f[(1, 1)] - f[(2, 2)]
    return M
Ef = sym_traceless('E'); Bf = sym_traceless('B')
eps3 = lambda i, j, k: sp.LeviCivita(i, j, k)
Wt = {}
for a, bb, c, d in itertools.product(idx, repeat=4):
    Wt[(a, bb, c, d)] = 0
def setW(a, bb, c, d, v):
    # Weyl symmetries
    for (p, q, r, t, sg) in [(a, bb, c, d, 1), (bb, a, c, d, -1), (a, bb, d, c, -1), (bb, a, d, c, 1),
                              (c, d, a, bb, 1), (d, c, a, bb, -1), (c, d, bb, a, -1), (d, c, bb, a, 1)]:
        Wt[(p, q, r, t)] = sg*v
for i in (1, 2, 3):
    for j in (1, 2, 3):
        setW(0, i, 0, j, Ef[i, j])
        for k in (1, 2, 3):
            setW(0, i, j, k, sum(eps3(j - 1, k - 1, l - 1)*Bf[l, i] for l in (1, 2, 3)))
for i, j, k, l in itertools.product((1, 2, 3), repeat=4):
    if (i, j) < (k, l) or (i, j) == (k, l):
        d_ = lambda p, q: 1 if p == q else 0
        setW(i, j, k, l, +(d_(i, k)*Ef[j, l] + d_(j, l)*Ef[i, k] - d_(i, l)*Ef[j, k] - d_(j, k)*Ef[i, l]))
# checks: tracelessness, cyclic identity
tr_ok = all(sp.simplify(sum(eta[a, a]*Wt[(a, bb, a, d)] for a in idx)) == 0 for bb in idx for d in idx)
cyc_ok = all(sp.simplify(Wt[(a, bb, c, d)] + Wt[(a, c, d, bb)] + Wt[(a, d, bb, c)]) == 0 for a, bb, c, d in itertools.product(idx, repeat=4))
print("(0) generic Weyl tensor from (E, B): traceless:", tr_ok, "; cyclic identity:", cyc_ok)

def up(i): return eta[i, i]
def D_div(a, bb, c):     # d^d W_abcd
    return sum(up(d)*sp.diff(Wt[(a, bb, c, d)], X[d]) for d in idx)

# ---------------------------------------------------------------- AF-1
sigma = -sp.log(Om_f)
C = {k: Om_f*v for k, v in Wt.items()}          # formal substitution C = Omega W
def T1(a, bb, use_sigma=True):
    f = sigma if use_sigma else sp.Integer(1)
    return c0*b*sum(up(c)*up(d)*sp.diff(f*C[(a, c, bb, d)], X[c], X[d]) for c in idx for d in idx)
print("\n(AF-1) c-part of Wess-Zumino")
# (a) log part of T is sigma * Lin(D, dD): identity d^c d^d (Omega W_acbd) = n^d D_bda + n^c D_acb + Omega d^c D_acb + (dd Omega).W
ok_id = True
for a in idx:
    for bb in idx:
        lhs = sum(up(c)*up(d)*sp.diff(C[(a, c, bb, d)], X[c], X[d]) for c in idx for d in idx)
        rhs = (sum(up(d)*sp.diff(Om_f, X[d])*D_div(bb, d, a) for d in idx) + sum(up(c)*sp.diff(Om_f, X[c])*D_div(a, c, bb) for c in idx)
               + Om_f*sum(up(c)*sp.diff(D_div(a, c, bb), X[c]) for c in idx)
               + sum(up(c)*up(d)*sp.diff(Om_f, X[c], X[d])*Wt[(a, c, bb, d)] for c in idx for d in idx))
        if sp.simplify(sp.expand(lhs - rhs)) != 0:
            ok_id = False
print("  identity  d^c d^d (Omega W_acbd) = n^d D_bda + n^c D_acb + Omega d^c D_acb + (d^c d^d Omega) W_acbd  (off shell):", ok_id)
print("  and (d^c d^d Omega) W_acbd = s eta^cd W_acbd = 0 (traceless) at first order: the ln Omega part of T is sigma x Lin(D, dD)")
That = sp.zeros(4)
for a in idx:
    for bb in idx:
        That[a, bb] = Om_f**2*T1(a, bb)
trT = sp.expand(sum(up(a)*That[a, a] for a in idx))
print("  eta-trace of That (off shell):", sp.simplify(subs_omega(trT)))
Lh = kap/2*That
# Christoffel of ghat = Omega^-2 eta, as functions
nf = [sp.diff(Om_f, X[a]) for a in idx]
nupf = [up(a)*nf[a] for a in idx]
def Gh(a, bb, c):
    return -((1 if a == bb else 0)*nf[c] + (1 if a == c else 0)*nf[bb] - eta[bb, c]*nupf[a])/Om_f
def cov(Tm, a, bb, c):
    return sp.diff(Tm[a, bb], X[c]) - sum(Gh(e, c, a)*Tm[e, bb] + Gh(e, c, bb)*Tm[a, e] for e in idx)
def R217(Lm, rho, nu, la):
    return (cov(Lm, la, rho, nu) - cov(Lm, nu, rho, la))/Om_f

# jets: replace derivatives of E, B by symbols; set divergence jets D aside by recording them
def jetify(expr):
    expr = sp.sympify(expr)
    reps = {}
    for dv in expr.atoms(sp.Derivative):
        if dv.expr != Om_f:
            name = str(dv.expr.func) + '_' + ''.join(str(X.index(v)) for v, k in dv.variable_count for _ in range(k))
            reps[dv] = sp.Symbol('d' + name, real=True)
    expr = expr.xreplace(reps)
    reps2 = {f: sp.Symbol(str(f.func), real=True) for f in expr.atoms(sp.Function) if f.func.__name__[0] in 'EBF'}
    return expr.xreplace(reps2)

Thj = That.applyfunc(lambda z: reduce_nn(jetify(subs_omega(z))))
lowT = min(min(laurent_log(Thj[a, bb]).keys(), default=(99, 0))[0] for a in idx for bb in idx)
print("  lowest power of Omega in That_ab:", lowT)
# Omega^1 coefficient of That: compare with -c0 b Omega E^n_ab, E^n_ab = n^c n^d W_acbd
Wsym = {k: jetify(v) for k, v in Wt.items()}
nupS = [up(a)*n[a] for a in idx]
En = sp.Matrix(4, 4, lambda a, bb: sp.expand(sum(nupS[c]*nupS[d]*Wsym[(a, c, bb, d)] for c in idx for d in idx)))
okE = all(laurent_log(reduce_nn(Thj[a, bb] + c0*b*W*En[a, bb])).get((1, 0), 0) == 0 for a in idx for bb in idx)
print("  Omega^1 coefficient of That (no log) == -c0 b E^n_ab, E^n_ab = n^c n^d W_acbd :", okE)
logT = {(a, bb): {k: v for k, v in laurent_log(Thj[a, bb]).items() if k[1] > 0} for a in idx for bb in idx}
print("  log terms of That: present only through divergence jets (checked below)")

src = {}
print("  computing (2.17) source ... ")
for rho in idx:
    for nu in idx:
        for la in range(nu + 1, 4):
            src[(rho, nu, la)] = reduce_nn(jetify(subs_omega(R217(Lh, rho, nu, la))))
low = 99; pole = {}; logs = {}
for k_, v in src.items():
    L_ = laurent_log(v)
    if L_:
        low = min(low, min(kk[0] for kk in L_))
    pole[k_] = L_.get((-1, 0), 0)
    logs[k_] = {kk: vv for kk, vv in L_.items() if kk[1] > 0}
print("  lowest power of Omega in (2.17) source:", low, "; terms of order Omega^-2 or below:",
      [k_ for k_, v in src.items() if any(kk[0] <= -2 for kk in laurent_log(v))])
# formal pole coefficient: compare with structure  P_rho nu la = alpha kappa c0 b (n_nu E_la rho - n_la E_nu rho) + beta' (eta...)
nS = list(n)
alpha_s = sp.Symbol('alpha')
cand = {k_: sp.expand(alpha_s*kap*c0*b*(nS[k_[1]]*En[k_[2], k_[0]] - nS[k_[2]]*En[k_[1], k_[0]])) for k_ in src}
diffs = [laurent_log(reduce_nn(src[k_] - cand[k_]/W)).get((-1, 0), 0) for k_ in src]
sol = sp.solve([d_ for d_ in diffs if d_ != 0][:6], alpha_s, dict=True)
print("  pole coefficient fitted to alpha kappa c0 b (n_nu E^n_lambda rho - n_lambda E^n_nu rho):", sol)
if sol:
    okP = all(sp.expand(d_.subs(sol[0])) == 0 for d_ in diffs)
    print("  fit exact on all 24 components:", okP)
syms_pole = set().union(*[sp.sympify(v).free_symbols for v in pole.values()])
print("  symbols in the pole coefficient:", sorted(str(z) for z in syms_pole))
# log terms vanish when the divergence of W vanishes: substitute divergence-free first and second jets by solving linear constraints
logsyms = set().union(*[sp.sympify(vv).free_symbols for v in logs.values() for vv in v.values()])
print("  number of log terms in (2.17) source:", sum(len(v) for v in logs.values()))
# divergence constraints in jets (orders 1 and 2 of W, i.e. D and dD)
Dj = [jetify(D_div(a, bb, c)) for a in idx for bb in idx for c in idx]
dDj = [jetify(sp.diff(D_div(a, bb, c), X[e])) for a in idx for bb in idx for c in idx for e in idx]
ddDj = [jetify(sp.diff(D_div(a, bb, c), X[e], X[f])) for a in idx for bb in idx for c in idx for e in idx for f in idx if e <= f]
Dj = [z for z in Dj if z != 0]; dDj = [z for z in dDj if z != 0]; ddDj = [z for z in ddDj if z != 0]
v1 = sorted({z for q in Dj for z in q.free_symbols}, key=str)
v2 = sorted({z for q in dDj for z in q.free_symbols if str(z).count('_') == 1 and len(str(z).split('_')[1]) == 2}, key=str)
s1 = sp.solve(Dj, v1, dict=True)[0]
dDj2 = [sp.expand(q.subs(s1)) for q in dDj]
s2 = sp.solve([q for q in dDj2 if q != 0], v2, dict=True)[0]
v3 = sorted({z for q in ddDj for z in q.free_symbols if str(z).count('_') == 1 and len(str(z).split('_')[1]) == 3}, key=str)
ddDj3 = [sp.expand(sp.expand(q.subs(s1)).subs(s2)) for q in ddDj]
s3 = sp.solve([q for q in ddDj3 if q != 0], v3, dict=True)[0]
print('  divergence constraints solved: orders 1, 2, 3 of W jets:', len(s1), len(s2), len(s3), 'variables eliminated')
def on_shell(z):
    return sp.expand(sp.expand(sp.expand(z.subs(s1)).subs(s2)).subs(s3))
log_vanish = all(on_shell(vv) == 0 for v in logs.values() for vv in v.values())
print("  all log Omega terms of the (2.17) source vanish when div W = 0 (and its first derivatives):", log_vanish)
pole_unchanged = all(sp.expand(on_shell(pole[k_]) - pole[k_]) == 0 for k_ in src)
log_orders = sorted({kk for v in logs.values() for kk in v})
print('  (power, log power) of the log terms before reduction:', log_orders)
# with classical matter, div W = J != 0: log terms are Lin(J) (identity above); example of a non-vanishing log term off the divergence-free jets:
ex_log = next(vv for v in logs.values() for vv in v.values())
print('  example log coefficient contains divergence jets only (non-zero off shell):', ex_log != 0)
print("  pole coefficient independent of the divergence jets:", pole_unchanged)

# ---------------- AF-3 (i) calibration on NOTE-125 mode: n = (1,0,0,0) (Omega = s coordinate x0), s_F = 0, lambda = 3, E_yy = -E_zz = e
e_ = sp.Symbol('e')
cal = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0, s: 0, lam: 3}
R_ = lambda nm: sp.Symbol(nm, real=True)
Ecal = {R_('E11'): 0, R_('E22'): e_, R_('E12'): 0, R_('E13'): 0, R_('E23'): 0,
        R_('B11'): 0, R_('B22'): 0, R_('B12'): 0, R_('B13'): 0, R_('B23'): 0}
# E^n relative to n_a=(1,0,0,0): n^0 = -1, E^n_ij = W_i0j0 = E_ij of the parametrisation (x0 axis): consistent
Ryy = sp.expand(pole[(2, 0, 2)].subs(cal).subs(Ecal).subs(c0, -8))
print("\n(AF-3 i) calibration: formal pole of R_{y s y} on n = (1,0,0,0), E_yy = e, c0 = -8 :", Ryy, "/Omega")
Bk = sp.Symbol('Bk3cos')
print("   with e = W_E,yy|scri = -B k^3 cos kx / 2 (irr_c_ctrl, NOTE-125):", sp.expand(Ryy.subs(e_, -Bk/2)),
      " ; NOTE-125: R_ysy|pole = -4 b kappa B k^3 cos kx / s  ->  match:", sp.simplify(Ryy.subs(e_, -Bk/2) + 4*b*kap*Bk) == 0)

# ---------------------------------------------------------------- AF-2 : sigma F^2
print("\n(AF-2) sigma F^2 term (running Maxwell coupling), coupling 1/e2_eff = 1/e2 - 4 beta_* sigma")
Ff = {}
for a in idx:
    for bb in idx:
        if a < bb:
            Ff[(a, bb)] = sp.Function(f'F{a}{bb}')(*X)
def F(a, bb):
    if a == bb: return 0
    return Ff[(a, bb)] if a < bb else -Ff[(bb, a)]
coup = 1/e2 - 4*betas*sigma
# Maxwell equation (conformal frame, F weight 0, sqrt(g) g g F^2 invariant): d_a [coup F^ab] = 0
maxw = [sp.expand(sum(up(a)*up(bb)*sp.diff(coup*F(a, bb), X[a]) for a in idx)) for bb in idx]
# solve for div F: d^a F_ab = - (d^a coup) F_ab / coup ; first order in beta_*
divF = [sum(up(a)*sp.diff(F(a, bb), X[a]) for a in idx) for bb in idx]
rhs_div = [sp.expand(sp.series(sp.expand(-(sum(up(a)*sp.diff(coup, X[a])*F(a, bb) for a in idx))/coup), betas, 0, 2).removeO()) for bb in idx]
rhs_div_j = [jetify(subs_omega(z)) for z in rhs_div]
print("  rescaled Maxwell equation d^a F_ab = RHS, RHS to first order in beta_*:", [sp.factor(z) for z in rhs_div_j])
# stress tensor: physical That_ab = coup * (F_ac F_bd ghat^cd - 1/4 ghat_ab F^2) = coup * Omega^2 M_ab[F; eta]
M = sp.zeros(4)
F2 = sum(up(a)*up(bb)*F(a, bb)**2 for a in idx for bb in idx)
for a in idx:
    for bb in idx:
        M[a, bb] = sum(up(c)*F(a, c)*F(bb, c) for c in idx) - eta[a, bb]*F2/4
That2 = (coup*Om_f**2*M).applyfunc(sp.expand)
print("  eta-trace of M:", sp.simplify(sum(up(a)*M[a, a] for a in idx)))
Lh2 = kap/2*That2
src2 = {}
for rho in idx:
    for nu in idx:
        for la in range(nu + 1, 4):
            src2[(rho, nu, la)] = reduce_nn(jetify(subs_omega(R217(Lh2, rho, nu, la))))
lo2 = min(min(laurent_log(v).keys(), default=(99, 0))[0] for v in src2.values())
print("  lowest power of Omega in (2.17) source:", lo2)
logc = {k_: laurent_log(v).get((0, 1), 0) for k_, v in src2.items()}
othl = {k_: {kk: vv for kk, vv in laurent_log(v).items() if kk[1] > 0 and kk != (0, 1)} for k_, v in src2.items()}
print("  log terms other than Omega^0 ln Omega:", sorted({kk for v in othl.values() for kk in v}))
syms2 = set().union(*[sp.sympify(v).free_symbols for v in logc.values()])
print("  symbols in the Omega^0 ln Omega coefficient:", sorted(str(z) for z in syms2))
Mj = M.applyfunc(jetify)
cand2 = {k_: sp.expand(sp.Symbol('gam')*kap*betas*(nS[k_[1]]*Mj[k_[2], k_[0]] - nS[k_[2]]*Mj[k_[1], k_[0]])
                       + sp.Symbol('gam2')*kap*betas*(eta[k_[2], k_[0]]*sum(nupS[c]*Mj[k_[1], c] for c in idx)
                                                      - eta[k_[1], k_[0]]*sum(nupS[c]*Mj[k_[2], c] for c in idx))) for k_ in src2}
eqs = [sp.expand(reduce_nn(logc[k_] - cand2[k_])) for k_ in src2]
eqs_coeffs = []
for q in eqs:
    if q != 0:
        eqs_coeffs += sp.Poly(q, *sorted(q.free_symbols - {sp.Symbol('gam'), sp.Symbol('gam2')}, key=str)).coeffs()
sol2 = sp.solve(eqs_coeffs, [sp.Symbol('gam'), sp.Symbol('gam2')], dict=True)
print("  Omega^0 ln Omega coefficient fitted to kappa beta_* [gam (n_nu M_lambda rho - n_lambda M_nu rho) + gam2 (eta_lambda rho (n.M)_nu - eta_nu rho (n.M)_lambda)]:", sol2)

# AF-3 (ii) calibration on uniform magnetic field of NOTE-98: F_12 = B0, n = (1,0,0,0), beta_* = -beta~/(2 e2)
B0, bt = sp.symbols('B0 beta_tilde', real=True)
calF = {R_(f'F{a}{bb}'): 0 for a in idx for bb in idx if a < bb}
calF[R_('F12')] = B0
for k_ in [(1, 0, 1), (2, 0, 2), (3, 0, 3)]:
    v = sp.expand(logc[k_].subs(cal).subs(calF).subs(betas, -bt/(2*e2)))
    print(f"   (ii) ln Omega coefficient of R_{k_}: {sp.factor(v)}  (NOTE-98, with 1/e^2 = 1/e2: -kappa beta~ B0^2/e^2 on (1,0,1),(2,0,2), +2 x on (3,0,3))")

# AF-3 (iii) algebraic vanishing condition in the frame n = (1,0,0,0): electric E_i = F_0i, magnetic B_i
Ei = sp.symbols('Ex Ey Ez', real=True); Bi = sp.symbols('Bx By Bz', real=True)
calEB = {R_('F01'): Ei[0], R_('F02'): Ei[1], R_('F03'): Ei[2],
         R_('F23'): Bi[0], R_('F13'): -Bi[1], R_('F12'): Bi[2]}
conds = sorted({sp.factor(sp.expand(v.subs(cal).subs(calEB))) for v in logc.values()} - {0}, key=str)
print("   (iii) distinct non-zero ln Omega coefficients in the frame of n, in terms of E_i, B_i:")
for q in conds:
    print("      ", q)
EE = sp.Matrix(3, 3, lambda i, j: Ei[i]*Ei[j]); BB = sp.Matrix(3, 3, lambda i, j: Bi[i]*Bi[j])
S_ = EE + BB; S_tf = S_ - sp.eye(3)*S_.trace()/3
Q_ = BB - EE; Q_tf = Q_ - sp.eye(3)*Q_.trace()/3
print("   compare: spatial traceless part of (E_iE_j + B_iB_j) (Maxwell stress) and of (B_iB_j - E_iE_j) (NOTE-113 criterion):")
print("      (EE+BB)_tf diagonal:", [sp.expand(S_tf[i, i]) for i in range(3)], " off-diagonal 12:", sp.expand(S_tf[0, 1]))
print("      Poynting (E x B):", [sp.expand(z) for z in sp.Matrix(Ei).cross(sp.Matrix(Bi))])
# solve the vanishing conditions of all ln Omega coefficients for real E, B
sol_EB = sp.solve(list(conds), list(Ei) + list(Bi), dict=True)
real_sols = [d_ for d_ in sol_EB if all(sp.im(v) == 0 for v in d_.values() if v.is_number)]
print("   all ln Omega coefficients vanish  <=>  solutions for (E, B):", sol_EB)
print("   argument: S = EE^T + BB^T is positive semidefinite of rank <= 2 ; S_tf = 0 forces S proportional to the identity (rank 3) unless S = 0 ; hence E = B = 0")
print("\nEXIT 0")
