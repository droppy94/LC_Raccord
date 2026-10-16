# Variante E3 (b) : W remplace par un tenseur sans les symetries de Weyl.
#   mode 'trace'  : W + (eta_ac S_bd - eta_ad S_bc - eta_bc S_ad + eta_bd S_ac), S symetrique (symetries de Riemann, trace non nulle)
#   mode 'nopair' : tenseur generique seulement antisymetrique en (ab) et en (cd) (36 fonctions), sans symetrie de paires ni cyclicite
# Test au niveau de T (la partie ln de (2.17) en derive) : partie ln Omega de T, puis residu sur D = 0, dD = 0 (D_abc = d^d W_abcd),
# compare au residu predit par l'identite : -LOG c0 b [ s eta^cd W_acbd + n^d (d^c W_acbd - D_bda) ].
import sys, itertools, sympy as sp
mode = sys.argv[1]
txt = open('af_check_copie.py').read()
head = txt.split('# ---------------------------------------------------------------- AF-1')[0]
exec(head)
if mode == 'trace':
    Sf = {}
    for a in idx:
        for b_ in idx:
            Sf[(a, b_)] = Sf.get((b_, a)) or sp.Function('ES%d%d' % (a, b_))(*X)   # prefixe E pour jetify
    for a, b_, c, d in itertools.product(idx, repeat=4):
        Wt[(a, b_, c, d)] = Wt[(a, b_, c, d)] + eta[a, c]*Sf[(b_, d)] - eta[a, d]*Sf[(b_, c)] - eta[b_, c]*Sf[(a, d)] + eta[b_, d]*Sf[(a, c)]
elif mode == 'nopair':
    pairs = [(a, b_) for a in idx for b_ in idx if a < b_]
    G = {(p, q): sp.Function('EG%d%d%d%d' % (p + q))(*X) for p in pairs for q in pairs}
    for a, b_, c, d in itertools.product(idx, repeat=4):
        if a == b_ or c == d: Wt[(a, b_, c, d)] = 0; continue
        sg = 1; p = (a, b_); q = (c, d)
        if a > b_: p = (b_, a); sg = -sg
        if c > d: q = (d, c); sg = -sg
        Wt[(a, b_, c, d)] = sg*G[(p, q)]
pair_ok = all(sp.expand(Wt[(a, b_, c, d)] - Wt[(c, d, a, b_)]) == 0 for a, b_, c, d in itertools.product(idx, repeat=4))
tr_ok = all(sp.expand(sum(eta[a, a]*Wt[(a, b_, a, d)] for a in idx)) == 0 for b_ in idx for d in idx)
print("=== variante E3(b), mode", mode, "=== symetrie de paires :", pair_ok, "; sans trace :", tr_ok)
sigma = -sp.log(Om_f)
def D_div(a, bb, c): return sum(up(d)*sp.diff(Wt[(a, bb, c, d)], X[d]) for d in idx)
def jetify(expr):
    expr = sp.sympify(expr); reps = {}
    for dv in expr.atoms(sp.Derivative):
        if dv.expr != Om_f:
            reps[dv] = sp.Symbol('d' + str(dv.expr.func) + '_' + ''.join(str(X.index(v)) for v, k in dv.variable_count for _ in range(k)), real=True)
    expr = expr.xreplace(reps)
    return expr.xreplace({f: sp.Symbol(str(f.func), real=True) for f in expr.atoms(sp.Function) if f.func.__name__[0] in 'EB'})
Tln = {}
for a in idx:
    for b_ in idx:
        T = c0*b*sum(up(c)*up(d)*sp.diff(sigma*Om_f*Wt[(a, c, b_, d)], X[c], X[d]) for c in idx for d in idx)
        Tln[(a, b_)] = sp.expand(jetify(subs_omega(T))).coeff(LOG, 1)
Dj = [z for z in (jetify(D_div(a, bb, c)) for a in idx for bb in idx for c in idx) if z != 0]
dDj = [z for z in (jetify(sp.diff(D_div(a, bb, c), X[e])) for a in idx for bb in idx for c in idx for e in idx) if z != 0]
v1 = sorted({z for q in Dj for z in q.free_symbols}, key=str)
s1 = sp.solve(Dj, v1, dict=True)[0]
v2 = sorted({z for q in dDj for z in q.free_symbols if len(str(z).split('_')[-1]) == 2 and str(z).startswith('d')}, key=str)
dDj2 = [sp.expand(q.subs(s1)) for q in dDj]
s2 = sp.solve([q for q in dDj2 if q != 0], v2, dict=True)[0]
on = lambda z: sp.expand(sp.expand(z.subs(s1)).subs(s2))
print("  contraintes resolues :", len(s1), len(s2))
nz = {k: on(v) for k, v in Tln.items() if on(v) != 0}
print("  composantes de la partie ln de T non nulles sur D = dD = 0 :", len(nz), "/ 16")
# residu predit
ok = True
for (a, b_), v in Tln.items():
    trterm = s*sum(up(c)*Wt[(a, c, b_, c)] for c in idx)
    pairterm = sum(up(d)*sp.diff(Om_f, X[d])*(sum(up(c)*sp.diff(Wt[(a, c, b_, d)], X[c]) for c in idx) - D_div(b_, d, a)) for d in idx)
    pred = on(sp.expand(jetify(subs_omega(-c0*b*(trterm + pairterm)))))
    if sp.expand(on(v) - pred) != 0: ok = False
print("  residu == -LOG c0 b [ s eta^cd W_acbd + n^d (d^c W_acbd - D_bda) ] sur toutes les composantes :", ok)
ex = next(iter(nz.items()), None)
print("  exemple :", ex[0] if ex else None, sp.factor(ex[1]) if ex else None)
if mode == 'trace':
    print("  avec s = 0 :", sum(1 for v in nz.values() if sp.expand(v.subs(s, 0)) != 0), "composantes non nulles")
