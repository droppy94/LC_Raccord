import sympy as sp
t, eps, T = sp.symbols('tau epsilon T', positive=True)
x, y, z = sp.symbols('x y z', real=True); X = [t, x, y, z]; n = 4
dd = [1, 1, -2]
def curv(g):
    gi = g.inv()
    G = [[[sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) for e in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    Rup = lambda a, b, c, d: sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d]) + sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(n))
    return G, Rup
def lin(e): return sp.expand(sp.series(sp.simplify(e), eps, 0, 2).removeO())
def run(f, label):
    g = sp.diag(-1, *[1 + eps*dd[i]*f for i in range(3)])
    G, Rup = curv(g)
    Ric = sp.Matrix(n, n, lambda b, d: lin(sum(Rup(a, b, a, d) for a in range(n))))
    Rs = lin(sum(g.inv()[a, a]*Ric[a, a] for a in range(n)))
    P = (Ric - Rs*g/6)/2
    E = []
    for i in (1, 2, 3):
        Rl = lin(sum(g[0, e]*Rup(e, i, 0, i) for e in range(n)))
        Cl = lin(Rl - (g[0, 0]*P[i, i] - g[0, i]*P[i, 0] - g[i, 0]*P[0, i] + g[i, i]*P[0, 0]))
        E.append(sp.expand(Cl.coeff(eps)))
    print(f"[{label}] f = {f}")
    print("   C_titi (coef eps) :", E, " ; attendu -f''/4 * d :", [sp.simplify(E[i] + sp.diff(f, t, 2)*dd[i]/4) == 0 for i in range(3)])
    W = [sp.expand(e/t) for e in E]; dW = [sp.expand(sp.diff(w, t)) for w in W]
    print("   W =", W, "\n   dW/dtau =", dW)
    print("   limites W, dW en 0+ :", [sp.limit(w, t, 0, '+') for w in W], [sp.limit(w, t, 0, '+') for w in dW])
    print("   limites f^(k)(0+), k=1..5 :", [sp.limit(sp.diff(f, t, kk), t, 0, '+') for kk in range(1, 6)])
    # eon suivant, g_check = tau^2 g
    gc = t**2*g
    G, Rup = curv(gc)
    Ric = sp.Matrix(n, n, lambda b, d: lin(sum(Rup(a, b, a, d) for a in range(n))))
    gci = gc.inv(); Rs = lin(sum(gci[a, a]*Ric[a, a] for a in range(n)))
    Gt = (Ric - Rs*gc/2).applyfunc(lin)
    mixed = [lin(gci[a, a]*Gt[a, a]) for a in range(n)]        # G^a_a
    frame = [lin(Gt[a, a]/(t**2*(1 if a == 0 else (1 + eps*dd[a-1]*f)))) for a in range(n)]  # G_(aa) repere orthonorme
    sub = {t: sp.sqrt(2*T)}
    for nm, arr in (("G^a_a (mixte)", mixed), ("G_(aa) (repere orthonorme)", frame)):
        print(f"   {nm} : fond =", [sp.simplify(e.subs(eps, 0).subs(sub)) for e in arr],
              "; coef eps =", [sp.simplify(sp.expand_log(e.coeff(eps).subs(sub), force=True)) for e in arr])
    off = [lin(Gt[a, b]) for a in range(n) for b in range(n) if a != b]
    print("   composantes hors diagonale nulles :", all(o == 0 for o in off))
run(t**4*sp.log(t), "Q, modele de l'audite")
run(t**3*sp.log(t), "variante : source R ~ 1/Omega (cf. R-C)")
