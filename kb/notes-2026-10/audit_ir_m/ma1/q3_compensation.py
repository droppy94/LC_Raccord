# Audit M-a1, question 3 : une contrainte anisotrope non Maxwell d'ordre s^2 ln s peut-elle annuler le log local de R ?
import sympy as sp, functools
print = functools.partial(print, flush=True)
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
kap = sp.symbols('kappa', positive=True)
X = [s, x, y, z]; Lg = sp.log(s)
eta = sp.diag(-1, 1, 1, 1); g = eta/s**2; gi = eta*s**2
Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d])) for d in range(4))/2
         for c in range(4)] for b in range(4)] for a in range(4)]
def cov(T):
    return [[[sp.diff(T[b, c], X[a]) - sum(Gam[d][a][b]*T[d, c] + Gam[d][a][c]*T[b, d] for d in range(4))
              for c in range(4)] for b in range(4)] for a in range(4)]
def divg(T):
    cT = cov(T); return [sp.expand(sum(gi[a, b]*cT[a][b][nu] for a in range(4) for b in range(4))) for nu in range(4)]
def Rof(T):
    trT = sp.expand(sum(gi[i, j]*T[i, j] for i in range(4) for j in range(4)))
    Lh = sp.Matrix(4, 4, lambda i, j: kap/2*(T[i, j] - g[i, j]*trT/3))
    cL = cov(Lh)
    return {(r, n, l): sp.expand((cL[n][l][r] - cL[l][n][r])/s) for r in range(4) for n in range(4) for l in range(4)}

# (i) sigma constant, sans trace : dX_ij = s^2 ln s sigma_ij, autres composantes nulles
sg = sp.symbols('sxx sxy sxz syy syz', real=True)
S = sp.Matrix([[sg[0], sg[1], sg[2]], [sg[1], sg[3], sg[4]], [sg[2], sg[4], -sg[0]-sg[3]]])
dX = sp.zeros(4, 4)
for i in range(3):
    for j in range(3):
        dX[i+1, j+1] = s**2*Lg*S[i, j]
print('[calcule] (i) sigma constant : trace ghat =', sp.simplify(sum(gi[i, j]*dX[i, j] for i in range(4) for j in range(4))),
      '; divergence =', [sp.simplify(d) for d in divg(dX)])
R = Rof(dX)
print('[calcule] (i) R_isj induit (i,j spatiaux) :')
for i in range(1, 4):
    print('   ', [sp.simplify(R[(i, 0, j)]) for j in range(1, 4)])
print('[calcule] (i) autres composantes non nulles :', sorted({(a, b, c) for (a, b, c), v in R.items() if v != 0 and not (b == 0 and a > 0 and c > 0) and not (c == 0 and a > 0 and b > 0)}))

# (ii) sigma(x) quelconque : dX_ij = s^2 ln s sigma_ij(x) + s^2 tau_ij(x) (tau sans trace, libre),
#      dX_si = s^3 (ln s v_i + w_i)(x), dX_ss = 0 (trace nulle). On resout la conservation.
sig = [[None]*3 for _ in range(3)]; tau = [[None]*3 for _ in range(3)]
fn = lambda nm: sp.Function(nm)(x, y, z)
for i in range(3):
    for j in range(i, 3):
        sig[i][j] = sig[j][i] = fn('sigma%d%d' % (i, j)); tau[i][j] = tau[j][i] = fn('tau%d%d' % (i, j))
sig[2][2] = -sig[0][0] - sig[1][1]; tau[2][2] = -tau[0][0] - tau[1][1]
v = [fn('v%d' % i) for i in range(3)]; wv = [fn('w%d' % i) for i in range(3)]
dX = sp.zeros(4, 4)
for i in range(3):
    for j in range(3):
        dX[i+1, j+1] = s**2*Lg*sig[i][j] + s**2*tau[i][j]
    dX[0, i+1] = dX[i+1, 0] = s**3*(Lg*v[i] + wv[i])
dv = divg(dX)
print('\n[calcule] (ii) sigma(x) : divergence (premiers ordres)')
for nu in range(4):
    print('   nu=%d :' % nu, sp.collect(sp.expand(dv[nu]), [s, Lg]))

# (iii) completion : on ajoute dX_ss = s^4 (ln s P + P2)(x) et une partie spatiale isotrope compensant la trace,
#       puis on resout la conservation ordre par ordre (v_i, w_i, P, P2).
P, P2 = fn('P'), fn('P2')
dX3 = dX.copy()
dX3[0, 0] = s**4*(Lg*P + P2)
for i in range(3):
    dX3[i+1, i+1] += s**4*(Lg*P + P2)/3
tr3 = sp.simplify(sum(gi[i, j]*dX3[i, j] for i in range(4) for j in range(4)))
dv3 = divg(dX3)
sol_v = {v[i]: sum(sp.diff(sig[i][j], X[j+1]) for j in range(3)) for i in range(3)}
sol_w = {wv[i]: sum(sp.diff(tau[i][j], X[j+1]) for j in range(3)) - sol_v[v[i]] for i in range(3)}
e0 = sp.expand(dv3[0].subs(sol_v).subs(sol_w).doit())
print('\n[calcule] (iii) trace ghat =', tr3)
print('[calcule] (iii) equation nu=s apres v,w : s^5 ln s *', sp.expand(e0/s**5).coeff(Lg,1), '; s^5 *', sp.expand(e0/s**5).coeff(Lg,0))
sp_ = sp.solve([sp.expand(e0/s**5).coeff(Lg, 1), sp.expand(e0/s**5).coeff(Lg, 0)], [P, P2], dict=True)
print('[calcule] (iii) P, P2 =', sp_)
e0f = sp.simplify(e0.subs(sp_[0]).doit()) if sp_ else None
print('[calcule] (iii) residu nu=s a s^5 :', e0f)
for nu in (1, 2, 3):
    rr = sp.expand(dv3[nu].subs(sol_v).subs(sol_w).doit())
    if sp_: rr = sp.expand(rr.subs(sp_[0]).doit())
    print('[calcule] (iii) nu=%d, ordre s^4 nul :' % nu, sp.simplify(sp.expand(rr).coeff(s, 4)) == 0, '; terme dominant restant :', sp.Order(rr, (s, 0)) if rr != 0 else 0)
R3 = Rof(dX3.subs(sol_v).subs(sol_w).subs(sp_[0] if sp_ else {}).doit())
LL = sp.Symbol('L')
for key in [(1, 0, 1), (1, 0, 2), (3, 0, 3), (0, 0, 1), (1, 2, 3), (0, 1, 2)]:
    ex = sp.expand(R3[key].subs(Lg, LL))
    c0 = sum(t for t in sp.Add.make_args(ex) if not t.has(s))
    print('[calcule] (iii) R%s, ordre s^0 :' % (key,), sp.simplify(c0))
