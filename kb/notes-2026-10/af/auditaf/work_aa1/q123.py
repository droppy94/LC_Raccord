"""AA-1, Q1 Q2 Q3 : terme sigma C^2 au premier ordre autour de eta."""
import sympy as sp, itertools as it, pickle, time
from common import *

t0 = time.time()
B = weyl_basis()
print("rang base de Weyl :", len(B), "| symetries/trace verifiees :", all(check_weyl(C) for C in B))

# W(x) = sum_k w_k(x) B^k, jets generiques jusqu'a l'ordre 3
wk, wsyms = [], []
for k in range(10):
    p, sy = jet_poly(f"w{k}", 3); wk.append(p); wsyms.append(sy)
W = lambda idx, x0=True: sum(wk[k] * B[k][idx] for k in range(10))
Om = Omega_x()
sig = -sp.log(Om)

# g_k = sigma * Omega * w_k  (sigma C = sigma Omega W)
G2 = [[[None]*4 for _ in range(4)] for _ in range(10)]
G3 = [[[[None]*4 for _ in range(4)] for _ in range(4)] for _ in range(10)]
for k in range(10):
    g = sig * Om * wk[k]
    for c, d in it.product(range(4), repeat=2):
        gcd = sp.diff(g, X[c], X[d])
        G2[k][c][d] = logsub(at0(gcd))
        for e in range(4):
            G3[k][e][c][d] = logsub(at0(sp.diff(gcd, X[e])))

ei = [etainv[a, a] for a in range(4)]
T0 = sp.zeros(4, 4); T1 = [sp.zeros(4, 4) for _ in range(4)]
for a, bb in it.product(range(4), repeat=2):
    T0[a, bb] = sp.expand(c0 * b * sum(ei[c] * ei[d] * B[k][a, c, bb, d] * G2[k][c][d]
                                       for k in range(10) for c in range(4) for d in range(4)))
    for e in range(4):
        T1[e][a, bb] = sp.expand(c0 * b * sum(ei[c] * ei[d] * B[k][a, c, bb, d] * G3[k][e][c][d]
                                              for k in range(10) for c in range(4) for d in range(4)))
print("T symetrique :", all(sp.expand(T0[a, c] - T0[c, a]) == 0 for a in range(4) for c in range(4)))
print("trace eta^{ab} T_ab = 0 :", sp.expand(sum(ei[a] * T0[a, a] for a in range(4))) == 0)

# jets de W et de sa divergence au point 0
nu_up = [ei[a] * n[a] for a in range(4)]
def Wjet(idx, al):
    return sum(wsyms[k][tuple(sorted(al))] * B[k][idx] for k in range(10))
def Djet(a, bb, c, al):  # d_al D_abc(0), D_abc = d^d W_abcd
    return sum(ei[d] * Wjet((a, bb, c, d), al + (d,)) for d in range(4))
E = sp.Matrix(4, 4, lambda a, bb: sum(nu_up[c] * nu_up[d] * Wjet((a, c, bb, d), ()) for c in range(4) for d in range(4)))

# ---------- Q1 : decomposition de T ----------
print("\n=== Q1 ===")
ok_struct = True; ok_formula = True
for a, bb in it.product(range(4), repeat=2):
    P = sp.Poly(T0[a, bb], ell, Om0, 1/Om0) if False else None
    expr = T0[a, bb]
    # termes presents : puissances de Om0 et de ell
    terms = sp.Add.make_args(expr)
    for t in terms:
        pe = sp.degree(t, ell); po = sp.Poly(t * Om0**2, Om0).degree() - 2 if t.has(Om0) else 0
        if (pe, po) not in [(0, -1), (0, 0), (1, 0), (1, 1)]:
            ok_struct = False; print("terme inattendu", a, bb, t)
    Y = sum(nu_up[d] * Djet(bb, d, a, ()) for d in range(4)) + sum(nu_up[c] * Djet(a, c, bb, ()) for c in range(4))
    dD = sum(ei[c] * Djet(a, c, bb, (c,)) for c in range(4))
    hand = c0 * b * (-E[a, bb] / Om0 - (ell + 1) * Y - Om0 * ell * dD)
    ok_formula &= sp.expand(expr - hand) == 0
print("puissances presentes dans T : seulement Om^-1, Om^0, ln Om, Om ln Om :", ok_struct)
print("T = c0 b [ -E^n/Om - (lnOm+1)(n^d D_bda + n^c D_acb) - Om lnOm d^c D_acb ] :", ok_formula)
That0 = (Om0**2 * T0).applyfunc(sp.expand)
coefO1 = That0.applyfunc(lambda v: sp.expand(v).coeff(ell, 0).coeff(Om0, 1))
print("coef de Om^1 (sans log) dans That = -c0 b E^n :", (coefO1 + c0 * b * E).applyfunc(sp.expand) == sp.zeros(4, 4))
logpart = T0.applyfunc(lambda v: sp.expand(v).coeff(ell, 1))
print("partie ln Om de T ne contient que des jets de D (verif en Q3)")

# ---------- Q2 ----------
print("\n=== Q2 ===")
R = R_from_T(T0, T1)
minpow = 10; ok_lead = True; dep_deriv = False
first_order_syms = set()
for al in multi_indices(3):
    if len(al) >= 1:
        for k in range(10): first_order_syms.add(wsyms[k][al])
for rho, nu, la in it.product(range(4), repeat=3):
    e = R[rho, nu, la]
    for t in sp.Add.make_args(e):
        if t == 0: continue
        po = sp.Poly(t * Om0**5, Om0).degree() - 5
        minpow = min(minpow, po)
    lead = sp.expand(e * Om0).subs(Om0, 0)  # coefficient de Om^-1 (les autres termes s'annulent)
    target = -kap * c0 * b * (n[nu] * E[la, rho] - n[la] * E[nu, rho])
    ok_lead &= sp.expand(lead - target) == 0
    dep_deriv |= bool(lead.free_symbols & first_order_syms)
print("plus basse puissance de Om dans R :", minpow)
print("coef Om^-1 de R = -kappa c0 b (n_nu E_lam rho - n_lam E_nu rho) :", ok_lead)
print("le coefficient depend de derivees de W :", dep_deriv)
print("le coefficient depend de lambda ou s :", any(R[i].has(lam) for i in it.product(range(4), repeat=3)))

# ---------- Q3 ----------
print("\n=== Q3 ===")
Rlog = {i: sp.expand(R[i]).coeff(ell, 1) for i in it.product(range(4), repeat=3)}
print("R contient ln^2 :", any(sp.expand(R[i]).coeff(ell, 2) != 0 for i in Rlog))
cons = {0: [], 1: [], 2: []}
for a, bb, c in it.product(range(4), repeat=3):
    cons[0].append(Djet(a, bb, c, ()))
    for e in range(4):
        cons[1].append(Djet(a, bb, c, (e,)))
        for f in range(e, 4):
            cons[2].append(Djet(a, bb, c, (e, f)))
allsyms = sorted(set().union(*[wsyms[k].values() for k in range(10)]), key=str)
def solve_and_test(levels):
    eqs = [sp.expand(q) for L in levels for q in cons[L] if sp.expand(q) != 0]
    unknowns = sorted(set().union(*[q.free_symbols for q in eqs]) & set(allsyms), key=str)
    sol = sp.solve(eqs, unknowns, dict=True)
    assert len(sol) == 1
    sol = sol[0]
    rank = len(sol)
    nz = [i for i in Rlog if sp.expand(Rlog[i].subs(sol)) != 0]
    return rank, len(eqs), nz, sol
for levels in ([0], [0, 1], [0, 1, 2]):
    rank, neq, nz, sol = solve_and_test(levels)
    print(f"contraintes d^k D = 0 pour k in {levels} : {neq} equations, {rank} jets elimines ; "
          f"composantes de R avec ln Om restant : {len(nz)}")
    if levels == [0, 1, 2]:
        sol_full = sol
# verification de la forme fermee pour D = J != 0
Y = lambda a, bb, al=(): None
def Yfun(a, bb):
    # Y_ab(x) au premier ordre en x autour de 0 : valeur et derivee
    val = sum(nu_up[d] * Djet(bb, d, a, ()) for d in range(4)) + sum(nu_up[c] * Djet(a, c, bb, ()) for c in range(4)) \
        + Om0 * sum(ei[c] * Djet(a, c, bb, (c,)) for c in range(4))
    der = []
    for e in range(4):
        # d_e de n^d D_bda : s eta^{de}... n^d = eta^{dd} n_d, d_e n_d = s eta_de
        dv = sum(ei[d] * s * eta[d, e] * Djet(bb, d, a, ()) + nu_up[d] * Djet(bb, d, a, (e,)) for d in range(4)) \
           + sum(ei[c] * s * eta[c, e] * Djet(a, c, bb, ()) + nu_up[c] * Djet(a, c, bb, (e,)) for c in range(4)) \
           + n[e] * sum(ei[c] * Djet(a, c, bb, (c,)) for c in range(4)) \
           + Om0 * sum(ei[c] * Djet(a, c, bb, (c, e)) for c in range(4))
        der.append(dv)
    return val, der
Yv = {}; Yd = {}
for a, bb in it.product(range(4), repeat=2):
    Yv[(a, bb)], Yd[(a, bb)] = Yfun(a, bb)
nY = lambda nu_, la: sum(nu_up[m] * Yv[(m, la)] for m in range(4))
ok_closed = True
for rho, nu, la in it.product(range(4), repeat=3):
    hand = (kap / 2) * (-c0 * b) * (3 * (n[nu] * Yv[(la, rho)] - n[la] * Yv[(nu, rho)])
                                   + eta[la, rho] * nY(0, nu) - eta[nu, rho] * nY(0, la)
                                   + Om0 * (Yd[(la, rho)][nu] - Yd[(nu, rho)][la]))
    ok_closed &= sp.expand(Rlog[(rho, nu, la)] - hand) == 0
print("forme fermee de la partie ln Om de R en fonction de D=J (Y_ab = n^d J_bda + n^c J_acb + Om d^c J_acb) :", ok_closed)
# exemple : D != 0 avec D(0)=0 mais dD(0) != 0 -> log residuel ?
pickle.dump({'T0': T0, 'T1': T1, 'R': R}, open('/home/claude/AF/auditaf/work_aa1/q123.pkl', 'wb'))
print("temps %.1fs" % (time.time() - t0))
