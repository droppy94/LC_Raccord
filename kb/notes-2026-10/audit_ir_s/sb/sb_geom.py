import sympy as sp
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
X = [s, x, y, z]; n = 4
def geom(g, trunc=lambda e: e):
    gi = trunc_mat(g.inv() if trunc is None else g.inv(), trunc)
    G = [[[trunc(sum(gi[a, e]*(sp.diff(g[e, b], X[c]) + sp.diff(g[e, c], X[b]) - sp.diff(g[b, c], X[e])) for e in range(n))/2)
           for c in range(n)] for b in range(n)] for a in range(n)]
    Rup = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(c+1, n):
                    v = trunc(sp.diff(G[a][b][d], X[c]) - sp.diff(G[a][b][c], X[d]) + sum(G[a][c][e]*G[e][b][d] - G[a][d][e]*G[e][b][c] for e in range(n)))
                    Rup[(a, b, c, d)] = v; Rup[(a, b, d, c)] = -v
                Rup[(a, b, c, c)] = 0
    Ric = sp.Matrix(n, n, lambda b, d: trunc(sum(Rup[(a, b, a, d)] for a in range(n))))
    Rs = trunc(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
    return gi, G, Rup, Ric, Rs
def trunc_mat(M, tr): return M.applyfunc(tr)
def invariants(g, gi, Rup, Ric, Rs, trunc=lambda e: e):
    # Riem^2 = R^a_bcd R_a^bcd ; metriques diagonales seulement (pour la vitesse)
    diag = all(g[i, j] == 0 for i in range(n) for j in range(n) if i != j)
    assert diag
    Riem2 = trunc(sum(Rup[(a, b, c, d)]**2*g[a, a]*gi[b, b]*gi[c, c]*gi[d, d] for a in range(n) for b in range(n) for c in range(n) for d in range(n)))
    Ric2 = trunc(sum(Ric[a, b]**2*gi[a, a]*gi[b, b] for a in range(n) for b in range(n)))
    E = trunc(Riem2 - 4*Ric2 + Rs**2)
    C2 = trunc(Riem2 - 2*Ric2 + Rs**2/3)
    return E, C2, Ric2
def box(f, g, gi, sqrtg, trunc=lambda e: e):
    return trunc(sum(sp.diff(trunc(sqrtg*gi[a, a]*sp.diff(f, X[a])), X[a]) for a in range(n))/sqrtg)

def EL(L, f, vars_):
    """delta/delta f de Int L : somme_alpha (-D)^alpha dL/d(D^alpha f)."""
    atoms = [a for a in L.atoms(sp.Derivative) if a.expr == f] + [f]
    atoms = sorted(set(atoms), key=lambda a: -len(a.variables) if isinstance(a, sp.Derivative) else 0)
    dums = {a: sp.Dummy() for a in atoms}
    Ld = L.subs(dums)   # derivees d'ordre eleve d'abord
    out = 0
    for a, dm in dums.items():
        dL = sp.diff(Ld, dm).subs({v: k for k, v in dums.items()})
        if isinstance(a, sp.Derivative):
            out += (-1)**len(a.variables)*sp.diff(dL, *a.variables)
        else:
            out += dL
    return sp.expand(out)
