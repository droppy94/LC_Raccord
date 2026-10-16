"""AA-1, Q4 (sigma F^2) et Q5 (controles)."""
import sympy as sp, itertools as it, pickle
from sympy.calculus.euler import euler_equations
from common import *

e2, beta, bt, B0, ee = sp.symbols('e2 beta_star betatilde B0 e', real=True)  # e2 = e^2
ei = [etainv[a, a] for a in range(4)]
Om = Omega_x()

print("=== Q4.1 : equation de Maxwell ===")
A = [sp.Function(f'A{a}')(*X) for a in range(4)]
F = sp.Matrix(4, 4, lambda a, c: sp.diff(A[c], X[a]) - sp.diff(A[a], X[c]))
f = 1 / e2 - 4 * beta * (-sp.log(Om))          # couplage effectif 1/e^2 - 4 beta sigma
Lag = -sp.Rational(1, 4) * f * sum(ei[a] * ei[c] * F[a, c] ** 2 for a in range(4) for c in range(4))
EL = euler_equations(Lag, A, X)
# forme attendue : d^a (f F_ab) = 0 ; on verifie puis on isole d^a F_ab
divF = [sum(ei[a] * sp.diff(F[a, c], X[a]) for a in range(4)) for c in range(4)]
nF = [sum(ei[a] * sp.diff(Om, X[a]) * F[a, c] for a in range(4)) for c in range(4)]
for c in range(4):
    lhs = EL[c].lhs
    target = sum(ei[a] * sp.diff(f * F[a, c], X[a]) for a in range(4))
    prop = sp.simplify(lhs / target) if target != 0 else None
    print(f" EL[{c}] / d^a(f F_a{c}) =", prop)
    # d^a F_ab = -(d^a f) F_ab / f
    sol = -sum(ei[a] * sp.diff(f, X[a]) * F[a, c] for a in range(4)) / f
    ser = sp.series(sol, beta, 0, 2).removeO()
    claimed_minus = -4 * e2 * beta * nF[c] / Om
    print(f"   d^a F_a{c} - (-4 e^2 beta n^a F_a{c}/Omega) = O(beta^2) :", sp.simplify(ser - claimed_minus) == 0,
          "| avec signe + (K-4) :", sp.simplify(ser + claimed_minus) == 0)

print("\n=== Q4.2 : termes ln Omega de R ===")
M0 = sp.Matrix(4, 4, lambda a, c: sp.Symbol(f'M{min(a,c)}{max(a,c)}'))
M0 = M0.subs(sp.Symbol('M00'), sum(sp.Symbol(f'M{i}{i}') for i in range(1, 4)))  # trace eta^ab M_ab = 0
M1 = [sp.Matrix(4, 4, lambda a, c: sp.Symbol(f'dM{e}_{min(a,c)}{max(a,c)}')) for e in range(4)]
for e in range(4):
    M1[e] = M1[e].subs(sp.Symbol(f'dM{e}_00'), sum(sp.Symbol(f'dM{e}_{i}{i}') for i in range(1, 4)))
fT = 1 / e2 + 4 * beta * sp.log(Om)
Tx = fT * (M0 + sum((X[e] * M1[e] for e in range(4)), sp.zeros(4, 4)))
T0 = Tx.applyfunc(lambda v: logsub(at0(v)))
T1 = [Tx.applyfunc(lambda v: logsub(at0(sp.diff(v, X[e])))) for e in range(4)]
R = R_from_T(T0, T1)
nup = [ei[a] * n[a] for a in range(4)]
nM = lambda c: sum(nup[a] * M0[a, c] for a in range(4))
ok = True; struct = set()
for rho, nu, la in it.product(range(4), repeat=3):
    r = sp.expand(R[rho, nu, la])
    for t in sp.Add.make_args(r):
        if t != 0:
            struct.add((sp.degree(t, ell), sp.Poly(t * Om0 ** 5, Om0).degree() - 5))
    c00 = r.coeff(ell, 1).coeff(Om0, 0)
    claim = kap * beta * (6 * (n[nu] * M0[la, rho] - n[la] * M0[nu, rho])
                          + 2 * (eta[la, rho] * nM(nu) - eta[nu, rho] * nM(la)))
    ok &= sp.expand(c00 - claim) == 0
print(" (degre en ln Omega, puissance de Omega) presents dans R :", sorted(struct))
print(" coef Omega^0 ln Omega = kappa beta [6(n_nu M_lam rho - n_lam M_nu rho) + 2(eta_lam rho n^c M_c nu - eta_nu rho n^c M_c lam)] :", ok)

print("\n=== Q4.3 : condition algebrique, n_a = (1,0,0,0) ===")
Ev = sp.symbols('E1:4', real=True); Bv = sp.symbols('B1:4', real=True)
Fm = sp.zeros(4, 4)
for i in range(3):
    Fm[0, i + 1] = Ev[i]; Fm[i + 1, 0] = -Ev[i]
eps = sp.LeviCivita
for i, j in it.product(range(3), repeat=2):
    Fm[i + 1, j + 1] = sum(eps(i, j, k) * Bv[k] for k in range(3))
F2 = sum(ei[a] * ei[c] * Fm[a, c] ** 2 for a in range(4) for c in range(4))
Mx = sp.Matrix(4, 4, lambda a, c: sum(ei[d] * Fm[a, d] * Fm[c, d] for d in range(4)) - eta[a, c] * F2 / 4)
print(" M sans trace :", sp.expand(sum(ei[a] * Mx[a, a] for a in range(4))) == 0, "| M_00 =", sp.factor(Mx[0, 0]))
nsub = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0}
Xc = []
for rho, nu, la in it.product(range(4), repeat=3):
    v = (6 * (n[nu] * M0[la, rho] - n[la] * M0[nu, rho]) + 2 * (eta[la, rho] * nM(nu) - eta[nu, rho] * nM(la)))
    Xc.append(sp.expand(v.subs(nsub)))
Msub = {sp.Symbol(f'M{a}{c}'): Mx[a, c] for a in range(4) for c in range(a, 4) if (a, c) != (0, 0)}
eqs = [sp.expand(x.subs(Msub)) for x in Xc if sp.expand(x.subs(Msub)) != 0]
EB = sp.Matrix(3, 3, lambda i, j: Ev[i] * Ev[j] + Bv[i] * Bv[j])
EBtf = EB - EB.trace() / 3 * sp.eye(3)
cross = sp.Matrix(Ev).cross(sp.Matrix(Bv))
# l'ideal engendre par eqs = ideal engendre par {EBtf_ij, (ExB)_i} (combinaisons lineaires a coefficients constants)
gens = [EBtf[i, j] for i in range(3) for j in range(i, 3)] + list(cross)
Ms = sp.Matrix([[sp.Poly(q, *Ev, *Bv).as_expr().coeff(1) for q in []]]) if False else None
def lin_span_equal(A_, B_):
    mons = sorted(set().union(*[sp.Poly(q, *Ev, *Bv).monoms() for q in A_ + B_]))
    mat = lambda L: sp.Matrix([[sp.Poly(q, *Ev, *Bv).coeff_monomial(m) for m in mons] for q in L])
    ra, rb, rab = mat(A_).rank(), mat(B_).rank(), mat(A_ + B_).rank()
    return ra, rb, rab
print(" rangs (equations, {(EE+BB)_tf, ExB}, union) :", lin_span_equal(eqs, gens), "-> egalite des espaces si les trois sont egaux")
# M_0i et (ExB)
print(" M_0i =", [sp.expand(Mx[0, i]) for i in range(1, 4)], " ; (E x B) =", list(cross))
# champs reels : la matrice EE^T + BB^T est de rang <= 2, donc (.)_tf = 0 impose (.) = mu I de rang 3 ou nul
print(" det(E E^T + B B^T) =", sp.expand(EB.det()), " (rang <= 2) ; trace =", sp.expand(EB.trace()))
mu = sp.Symbol('mu')
print(" EE^T+BB^T = mu I avec det = 0  =>  mu^3 = 0  =>  mu = 0  =>  |E|^2+|B|^2 = 3 mu = 0")
# controle complexe : existe-t-il une solution non nulle ?
Ez = sp.Matrix([1, sp.I, 0]); Bz = sp.Matrix([0, 0, 0])
EBz = Ez * Ez.T + Bz * Bz.T
print(" exemple complexe E=(1,i,0), B=0 : (EE)_tf =", list(EBz - EBz.trace()/3*sp.eye(3)), " ExB =", list(Ez.cross(Bz)))

print("\n=== Q5 (b) : F_12 = B0 ===")
for sgn, lab in [(1, "n_a = (1,0,0,0) (indice bas)"), (-1, "n^a = (1,0,0,0) (indice haut, donc n_0 = -1)")]:
    sub = {n[0]: sgn, n[1]: 0, n[2]: 0, n[3]: 0, lam: 3, s: 0}
    Fb = {Ev[0]: 0, Ev[1]: 0, Ev[2]: 0, Bv[0]: 0, Bv[1]: 0, Bv[2]: B0}  # B_3 = F_12
    Msb = {k: v.subs(Fb) for k, v in Msub.items()}
    out = []
    for i in (1, 2, 3):
        r = sp.expand(R[i, 0, i]).coeff(ell, 1)
        r = r.subs(sub).subs({sp.Symbol(f'dM{e}_{a}{c}'): 0 for e in range(4) for a in range(4) for c in range(4)})
        r = sp.expand(r.subs(Msb).subs(beta, -bt / (2 * e2)))
        out.append(sp.factor(r))
    print(" ", lab, ": coef ln Omega de R_101, R_202, R_303 =", out)
print("   (M dans eta pour ce F :", [Mx[i, i].subs({Ev[0]:0,Ev[1]:0,Ev[2]:0,Bv[0]:0,Bv[1]:0,Bv[2]:B0}) for i in range(4)], ")")

print("\n=== Q5 (a) : W purement electrique, E_yy = -E_zz = e ===")
d = pickle.load(open('/home/claude/AF/auditaf/work_aa1/q123.pkl', 'rb'))
Rw = d['R']
Bw = weyl_basis()
wk0 = [sp.Symbol(f'w{k}_') for k in range(10)]
W0 = lambda idx: sum(wk0[k] * Bw[k][idx] for k in range(10))
# electrique : W_0i0j = E_ij (independant du signe de n^0) ; magnetique nul : W_0ijk = 0
conds = []
Etarget = {(1, 1): 0, (2, 2): ee, (3, 3): -ee, (1, 2): 0, (1, 3): 0, (2, 3): 0}
for (i, j), v in Etarget.items():
    conds.append(W0((0, i, 0, j)) - v)
for i, j, k in it.product(range(1, 4), repeat=3):
    conds.append(W0((0, i, j, k)))
solw = sp.solve(conds, wk0, dict=True)
print(" solution unique pour W(0) :", len(solw) == 1 and len(solw[0]) == 10)
for sgn, lab in [(1, "n_a = (1,0,0,0)"), (-1, "n^a = (1,0,0,0)")]:
    sub = {n[0]: sgn, n[1]: 0, n[2]: 0, n[3]: 0, lam: 3, s: 0, c0: -8}
    r = sp.expand(Rw[2, 0, 2])
    pole = sp.expand(r * Om0).subs(Om0, 0)
    pole = sp.factor(pole.subs(solw[0]).subs(sub))
    print(f"  {lab} : residu du pole de R_y0y (coef de 1/Omega) =", pole)
