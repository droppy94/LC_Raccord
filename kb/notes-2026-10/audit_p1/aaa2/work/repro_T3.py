# repro_T3.py : reproduction independante du resultat central (terme alpha beta*)
# Formulation differente du script audite : produit de deux fonctions d'un point,
# composantes cartesiennes k1,k2,k3 (pas d'angles), k = |k| explicite.
import sympy as sp
import mpmath as mpm
import random

t, tp = sp.symbols('t tp', real=True)          # temps conformes eta, eta'
x = sp.symbols('x1:4', real=True)
y = sp.symbols('y1:4', real=True)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kvec = [k1, k2, k3]
knorm = sp.sqrt(k1**2 + k2**2 + k3**2)
xi = sp.Rational(1, 6)
g = sp.diag(-1, 1, 1, 1)            # signature -+++ ; g^{-1} = g
ginv = g.inv()

def T_bilin(f, h, Xc, Yc):
    """T_{mu nu}[f,h] = sym(d_mu f d_nu h) - 1/2 g g^{ab} d_a f d_b h - xi (d_mu d_nu - g box)(f h), a la coincidence."""
    coinc = {tp: t, y[0]: x[0], y[1]: x[1], y[2]: x[2]}
    df = [sp.diff(f, c) for c in Xc]
    dh = [sp.diff(h, c) for c in Yc]
    kin = sum(ginv[a, a]*df[a]*dh[a] for a in range(4))
    fh = (f*h).subs(coinc)                      # phi^2 a la coincidence, fonction de x seulement
    box = sum(ginv[a, a]*sp.diff(fh, Xc[a], Xc[a]) for a in range(4))
    T = sp.zeros(4, 4)
    for m in range(4):
        for n in range(4):
            T[m, n] = (sp.Rational(1, 2)*(df[m]*dh[n] + df[n]*dh[m]) - sp.Rational(1, 2)*g[m, n]*kin).subs(coinc) \
                      - xi*(sp.diff(fh, Xc[m], Xc[n]) - g[m, n]*box)
    return sp.simplify(T)

Xc = [t, x[0], x[1], x[2]]
Yc = [tp, y[0], y[1], y[2]]
kx = sum(kvec[i]*x[i] for i in range(3))
ky = sum(kvec[i]*y[i] for i in range(3))

# terme alpha beta* : e^{-ik(eta+eta')} e^{ik.(x-x')} = [e^{-ik eta + ik.x}] [e^{-ik eta' - ik.x'}]
f3 = sp.exp(-sp.I*knorm*t + sp.I*kx)
h3 = sp.exp(-sp.I*knorm*tp - sp.I*ky)
T3 = T_bilin(f3, h3, Xc, Yc)

print("== terme alpha beta* ==")
print("T_00 =", sp.simplify(T3[0, 0]))
print("T_0i =", [sp.simplify(T3[0, i]) for i in (1, 2, 3)])
attendu = sp.Matrix(3, 3, lambda i, j: (kvec[i]*kvec[j] - sp.KroneckerDelta(i, j)*knorm**2/3)*sp.exp(-2*sp.I*knorm*t))
diffTij = sp.simplify(T3[1:, 1:] - attendu)
print("T_ij - (k_i k_j - k^2 delta_ij/3) e^{-2ik eta} =", diffTij)
trace = sp.simplify(sum(ginv[a, a]*T3[a, a] for a in range(4)))
trace_sp = sp.simplify(sum(T3[i, i] for i in (1, 2, 3)))
print("trace 4D g^{mn} T_mn =", trace, " ; trace spatiale T_ii =", trace_sp)
print("partie isotrope de T_ij (T_ii/3) =", sp.simplify(trace_sp/3))

# terme |beta|^2 (structure P2) pour comparaison
f2 = sp.exp(sp.I*knorm*t + sp.I*kx)
h2 = sp.exp(-sp.I*knorm*tp - sp.I*ky)
T2 = T_bilin(f2, h2, Xc, Yc)
print("\n== terme |beta|^2 (phase e^{ik(eta-eta')}) ==")
print("T_00 =", sp.simplify(T2[0, 0]), " T_0i =", [sp.simplify(T2[0, i]) for i in (1, 2, 3)])
print("T_ij - k_i k_j =", sp.simplify(T2[1:, 1:] - sp.Matrix(3, 3, lambda i, j: kvec[i]*kvec[j])))
print("trace 4D =", sp.simplify(sum(ginv[a, a]*T2[a, a] for a in range(4))))

# structure P1 (e^{-ik(eta-eta')}) : porte aussi |beta|^2 apres soustraction du vide
f1 = sp.exp(-sp.I*knorm*t + sp.I*kx)
h1 = sp.exp(sp.I*knorm*tp - sp.I*ky)
T1 = T_bilin(f1, h1, Xc, Yc)
print("\n== structure P1 (e^{-ik(eta-eta')}), coefficient |alpha|^2 - 1 = |beta|^2 ==")
print("T_00 =", sp.simplify(T1[0, 0]), " T_0i =", [sp.simplify(T1[0, i]) for i in (1, 2, 3)])
print("T_ij - k_i k_j =", sp.simplify(T1[1:, 1:] - sp.Matrix(3, 3, lambda i, j: kvec[i]*kvec[j])))

# ---- controle numerique independant de la differentiation symbolique : differences finies (mpmath) ----
mpm.mp.dps = 30
def w3_num(X, Y, kk):
    kn = mpm.sqrt(sum(c**2 for c in kk))
    return mpm.exp(-1j*kn*(X[0] + Y[0]) + 1j*sum(kk[i]*(X[i+1] - Y[i+1]) for i in range(3)))

def fd2(fun, X, Y, m, n, h=mpm.mpf('1e-6')):
    """d^x_m d^y_n fun au point (X,Y) par differences finies centrees."""
    def shift(P, idx, s):
        Q = list(P); Q[idx] = Q[idx] + s; return Q
    return (fun(shift(X, m, h), shift(Y, n, h)) - fun(shift(X, m, h), shift(Y, n, -h))
            - fun(shift(X, m, -h), shift(Y, n, h)) + fun(shift(X, m, -h), shift(Y, n, -h)))/(4*h*h)

def fdxx(fun0, X, m, n, h=mpm.mpf('1e-6')):
    def shift(P, idx, s):
        Q = list(P); Q[idx] = Q[idx] + s; return Q
    if m == n:
        return (fun0(shift(X, m, h)) - 2*fun0(X) + fun0(shift(X, m, -h)))/(h*h)
    return (fun0(shift(shift(X, m, h), n, h)) - fun0(shift(shift(X, m, h), n, -h))
            - fun0(shift(shift(X, m, -h), n, h)) + fun0(shift(shift(X, m, -h), n, -h)))/(4*h*h)

random.seed(7)
gd = [-1, 1, 1, 1]
maxerr = mpm.mpf(0)
for trial in range(3):
    kk = [mpm.mpf(random.uniform(-2, 2)) for _ in range(3)]
    X0 = [mpm.mpf(random.uniform(-1, -0.1))] + [mpm.mpf(random.uniform(-1, 1)) for _ in range(3)]
    fun = lambda X, Y: w3_num(X, Y, kk)
    fun0 = lambda X: w3_num(X, X, kk)
    D = [[fd2(fun, X0, X0, m, n) for n in range(4)] for m in range(4)]
    kin = sum(gd[a]*D[a][a] for a in range(4))
    H = [[fdxx(fun0, X0, m, n) for n in range(4)] for m in range(4)]
    box = sum(gd[a]*H[a][a] for a in range(4))
    Tn = [[(D[m][n] + D[n][m])/2 - (gd[m] if m == n else 0)*kin/2 - (H[m][n] - (gd[m] if m == n else 0)*box)/6
           for n in range(4)] for m in range(4)]
    kn = mpm.sqrt(sum(c**2 for c in kk))
    ph = mpm.exp(-2j*kn*X0[0])
    Tth = [[0]*4 for _ in range(4)]
    for i in range(3):
        for j in range(3):
            Tth[i+1][j+1] = (kk[i]*kk[j] - (kn**2/3 if i == j else 0))*ph
    err = max(abs(Tn[m][n] - Tth[m][n]) for m in range(4) for n in range(4))
    maxerr = max(maxerr, err)
    print("essai", trial, " k =", [mpm.nstr(c, 6) for c in kk], " eta =", mpm.nstr(X0[0], 6),
          " ecart max |T_num - T_theorique| =", mpm.nstr(err, 5))
print("ecart max global (differences finies, h=1e-6) :", mpm.nstr(maxerr, 5))
