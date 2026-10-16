# analyse des solutions d'ordre eps^2
import sympy as sp, pickle, sys
from spinors import mu
fn = sys.argv[1]
results, NH, MUNUM = pickle.load(open(fn, 'rb'))
TRUST = NH - 2
for lab, (qv, T, sols) in results.items():
    print("==== secteur", lab, "q =", qv)
    nz = sorted(k for k, v in T.items() if sp.simplify(v) != sp.zeros(4))
    print("  termes source T_phys non nuls (n,j) [Omega^{n+ij mu}] :", nz)
    for k in sorted(T):
        if k[0] == 1:
            print("   T_phys", k, "composantes non nulles :", [(a, b) for a in range(4) for b in range(a, 4) if sp.simplify(T[k][a, b]) != 0])
    for j, S in sols.items():
        if S is None:
            print("  j =", j, ": INCOMPATIBLE"); continue
        unk, d, free = S
        z = {f: 0 for f in free}
        print("  j = %d  (solution particuliere, parametres libres -> 0 ; fiable jusqu'a n = %d)" % (j, TRUST))
        first = {}
        for (n, a, b), sym in sorted(unk.items()):
            if n > TRUST: continue
            v = sp.simplify(sp.sympify(d[sym]).subs(z))
            if v != 0:
                first.setdefault((a, b), n)
                if n <= TRUST:
                    vs = str(sp.nsimplify(v) if MUNUM else sp.factor(v))
                    print("     h_%d%d  Omega^{%d%+d i mu} : %s" % (a, b, n, j, vs[:300]))
        print("   -> ordre minimal non nul par composante :", first)
        # h00 a l'ordre 0
        print("   -> h_00 coefficient Omega^{0%+di mu} :" % j, sp.simplify(sp.sympify(d[unk[(0, 0, 0)]])))
