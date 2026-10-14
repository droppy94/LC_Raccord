"""Q3 : R_{rho nu lambda} avec T = X^M seul. L = (kappa/2)(T - 1/3 g tr_g T),
R_{rho nu lambda} = Omega^-1 (nabla_nu L_{lambda rho} - nabla_lambda L_{nu rho}), Omega = s.
Mode A_y = u(s) cos kx, u = U0 + beta u1, (I2 u')' + k^2 I2 u = 0, I2 = e^-2 [1 + 2 beta (lam - ln s)].
"""
import sympy as sp

s, x, y, z, k, beta, e, lam, kap, u0, c, L = sp.symbols('s x y z k beta e lambda kappa u0 c L')
X = [s, x, y, z]
N = 8  # ordre de troncature en s

# --- solution u1 en serie : u1 = sum (a_n + b_n ln s) s^n
a = sp.symbols('a0:%d' % (N+1)); bb = sp.symbols('b0:%d' % (N+1))
U0 = sp.series(u0*sp.cos(k*s) + c/k*sp.sin(k*s), s, 0, N+2).removeO()
u1 = sum((a[n] + bb[n]*sp.log(s))*s**n for n in range(N+1))
I2 = (1 + 2*beta*(lam - sp.log(s)))/e**2
uu = U0 + beta*u1
eq = sp.expand(sp.diff(I2*sp.diff(uu, s), s) + k**2*I2*uu)
eq1 = sp.expand(sp.diff(eq, beta).subs(beta, 0)*e**2)  # ordre beta
eq1 = sp.expand(eq1.subs(sp.log(s), L))
conds = []
for p in range(-2, N-1):
    for q in (0, 1):
        cf = eq1.coeff(L, q).coeff(s, p) if p != 0 else eq1.coeff(L, q).subs(s, 0) if False else sp.expand(eq1.coeff(L, q)*s**2).coeff(s, p+2)
        if cf != 0:
            conds.append(cf)
sol = sp.solve(conds, list(a[2:]) + list(bb), dict=True)
assert len(sol) == 1
sol = sol[0]
u1s = sp.expand(u1.subs(sol))
print('[calcule] u1 (serie, a0,a1 libres = homogene) =', sp.collect(sp.expand(u1s.subs(sp.log(s), L)), L))
free = [v for v in u1s.free_symbols if v in a or v in bb]
print('[calcule] parametres libres restants dans u1 :', free)
uu = U0 + beta*u1s

# --- tenseur de Maxwell
eta = sp.diag(-1, 1, 1, 1); g = eta/s**2; gi = eta*s**2
A = [0, 0, uu*sp.cos(k*x), 0]
F = sp.Matrix(4, 4, lambda m, n: sp.diff(A[n], X[m]) - sp.diff(A[m], X[n]))
F2 = sum(F[m, n]*F[m, n]*gi[m, m]*gi[n, n] for m in range(4) for n in range(4))
XM = sp.Matrix(4, 4, lambda m, n: I2*(sum(F[m, al]*F[n, al]*gi[al, al] for al in range(4)) - g[m, n]*F2/4))
trT = sum(gi[m, m]*XM[m, m] for m in range(4))
print('[calcule] tr_g X^M =', sp.simplify(trT))
Lh = sp.Matrix(4, 4, lambda m, n: kap/2*(XM[m, n] - g[m, n]*trT/3))

Gam = [[[sum(gi[l, al]*(sp.diff(g[al, m], X[n]) + sp.diff(g[al, n], X[m]) - sp.diff(g[m, n], X[al])) for al in range(4))/2
         for n in range(4)] for m in range(4)] for l in range(4)]
def nab(n, l, r):  # nabla_n L_{l r}
    return sp.diff(Lh[l, r], X[n]) - sum(Gam[al][n][l]*Lh[al, r] + Gam[al][n][r]*Lh[l, al] for al in range(4))
def Rc(r, n, l):
    return (nab(n, l, r) - nab(l, n, r))/s

def logstruct(expr):
    """renvoie dict {(puissance s, puissance L): coeff} a l'ordre beta^1, apres log(s)->L"""
    ex = sp.expand(sp.diff(expr, beta).subs(beta, 0))
    ex = sp.expand(ex.subs(sp.log(s), L))
    out = {}
    for q in range(0, 3):
        cq = ex.coeff(L, q)
        if cq == 0:
            continue
        cq = sp.expand(cq)
        for p in range(-4, 4):
            cp = sp.expand(cq*s**4).coeff(s, p+4)
            cp = sp.simplify(cp)
            if cp != 0:
                out[(p, q)] = cp
    return out

idx = {1: 'x', 2: 'y', 3: 'z'}
# Champs a I+ (ordre beta^0) : E_y = U0'(0) = c cos kx ; B_z = d_x A_y = -k u0 sin kx
Ey = c*sp.cos(k*x); Bz = -k*u0*sp.sin(k*x)
Bv = [0, 0, Bz]; Ev = [0, Ey, 0]
Q = sp.Matrix(3, 3, lambda i, j: Bv[i]*Bv[j] - Ev[i]*Ev[j])
Qtf = Q - sp.eye(3)*Q.trace()/3
target = 3*kap/e**2*Qtf

print('\n=== R_{i s j} : structure en (puissance de s, puissance de ln s) a l ordre beta^1 ===')
for i in (1, 2, 3):
    for j in (1, 2, 3):
        st = logstruct(Rc(i, 0, j))
        lg = {kk: v for kk, v in st.items() if kk[1] >= 1 and kk[0] <= 2}
        c00 = st.get((0, 1), 0)
        print('R_%ss%s : termes en ln s (s^p ln^q s, p<=2) :' % (idx[i], idx[j]), lg)
        print('     coeff beta ln s a s^0 =', sp.simplify(c00), ' ; cible =', sp.simplify(target[i-1, j-1]),
              ' ; ecart =', sp.simplify(sp.expand(sp.expand_trig(c00 - target[i-1, j-1]))))

print('\n=== Autres composantes R_{rho nu lambda} : presence de ln s aux ordres s^p, p<=1 ===')
for r in range(4):
    for n in range(4):
        for l in range(n+1, 4):
            if n == 0 and r != 0:
                continue  # R_{i s j} deja traite
            st = logstruct(Rc(r, n, l))
            lg = {kk: v for kk, v in st.items() if kk[1] >= 1 and kk[0] <= 1}
            if lg:
                print('R_%s%s%s :' % ('sxyz'[r], 'sxyz'[n], 'sxyz'[l]), lg)
print('[fin]')
