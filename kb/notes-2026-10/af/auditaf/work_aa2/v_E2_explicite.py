# Variante E2 ter : test independant de la procedure formelle (substitutions d d Omega = s eta, d s = 0, reduction par (3.8), jetify).
# On prend un Omega EXPLICITE quadratique, Omega = c + k.x + (s/2) eta(x,x), pour lequel d d Omega = s eta, d s = 0 et
# n.n = -lambda/3 + 2 Omega s sont EXACTS, et des champs E, B polynomiaux arbitraires (non a divergence nulle).
# On recalcule (2.17) directement (implementation propre : log reel, Christoffel de Omega^-2 eta) et on compare, en des points,
# au second membre formel src du script (n -> d Omega(x), Omega -> Omega(x), LOG -> ln Omega(x), jets -> derivees).
import sympy as sp, random, itertools
src_txt = open('af_check_copie.py').read()
exec(src_txt.split('# ---------------- AF-3 (i)')[0])
print("\n=== test explicite AA-2 ===")
random.seed(7)
xs = X
sv = sp.Rational(1, 5); kv = [sp.Rational(1), sp.Rational(1, 5), sp.Rational(-1, 10), sp.Rational(3, 10)]; cv = sp.Rational(2)
Om_ex = cv + sum(kv[a]*xs[a] for a in idx) + sv/2*sum(eta[a, a]*xs[a]**2 for a in idx)
lam_v = -3*(sum(eta[a, a]*kv[a]**2 for a in idx) - 2*sv*cv)
c0v, bv, kapv = sp.Integer(-8), sp.Rational(3, 7), sp.Rational(5, 3)
mons = [sp.Integer(1)] + list(xs) + [xs[a]*xs[b_] for a in idx for b_ in idx if a <= b_] + [xs[0]*xs[1]*xs[2], xs[1]**3, xs[0]**2*xs[3], xs[2]*xs[3]**2]
polys = {}
for nm in ['E11', 'E22', 'E12', 'E13', 'E23', 'B11', 'B22', 'B12', 'B13', 'B23']:
    polys[nm] = sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4))*m for m in random.sample(mons, 6))
fsub = {}
for f in set().union(*[sp.sympify(v).atoms(sp.Function) for v in Wt.values() if v != 0]):
    fsub[f] = polys[str(f.func)]
Wex = {k: sp.sympify(v).xreplace(fsub) for k, v in Wt.items()}
sig = -sp.log(Om_ex)
Tex = sp.Matrix(4, 4, lambda a, b_: c0v*bv*sum(up(c)*up(d)*sp.diff(sig*Om_ex*Wex[(a, c, b_, d)], xs[c], xs[d]) for c in idx for d in idx))
Lex = kapv/2*Om_ex**2*Tex
nex = [sp.diff(Om_ex, xs[a]) for a in idx]
def G(a, b_, c):
    return -((1 if a == b_ else 0)*nex[c] + (1 if a == c else 0)*nex[b_] - eta[b_, c]*up(a)*nex[a])/Om_ex
def cv_(a, b_, c):
    return sp.diff(Lex[a, b_], xs[c]) - sum(G(e, c, a)*Lex[e, b_] + G(e, c, b_)*Lex[a, e] for e in idx)
pts = [(sp.Rational(1, 3), sp.Rational(-1, 2), sp.Rational(1, 4), sp.Rational(2, 5)), (sp.Rational(-1, 7), sp.Rational(1, 3), sp.Rational(0), sp.Rational(1, 2))]
comps = [(1, 0, 1), (2, 0, 3), (0, 1, 2), (3, 1, 2), (1, 2, 3), (0, 0, 3)]
allok = True
for pt in pts:
    ptd = dict(zip(xs, pt))
    Om0 = Om_ex.subs(ptd)
    assert Om0 > 0
    jets = {}
    def jetval(sym):
        s_ = str(sym)
        if s_.startswith('d') and '_' in s_:
            nm, dd_ = s_[1:].split('_')
            e_ = polys[nm]
            for ch in dd_: e_ = sp.diff(e_, xs[int(ch)])
            return e_.subs(ptd)
        if s_ in polys: return polys[s_].subs(ptd)
        return None
    for k_ in comps:
        direct = sp.expand(sp.expand_log(((cv_(k_[2], k_[0], k_[1]) - cv_(k_[1], k_[0], k_[2]))/Om_ex).subs(ptd), force=True))
        form = src[k_]
        rep = {z: jetval(z) for z in form.free_symbols if jetval(z) is not None}
        rep.update({n[a]: nex[a].subs(ptd) for a in idx})
        rep.update({W: Om0, LOG: sp.log(Om0), s: sv, lam: lam_v, c0: c0v, b: bv, kap: kapv})
        fv = sp.expand(sp.expand_log(form.xreplace(rep), force=True))
        d_ = sp.nsimplify(sp.expand(direct - fv))
        ok = sp.simplify(d_) == 0
        allok &= ok
        print("  point", pt, "composante", k_, ": direct =", sp.N(direct, 12), "; formel =", sp.N(fv, 12), "; egal :", ok)
print("  procedure formelle exacte sur Omega quadratique explicite (s != 0) :", allok)
