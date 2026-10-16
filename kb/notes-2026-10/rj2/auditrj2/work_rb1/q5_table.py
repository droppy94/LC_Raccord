# Tableau des coefficients (mu symbolique), parametres libres -> 0, ordres n <= NH-2
import sympy as sp, pickle, sys
from spinors import mu
results, NH, MUNUM = pickle.load(open(sys.argv[1], 'rb'))
comps = sys.argv[2].split(',') if len(sys.argv) > 2 else ['00', '11', '12']
for lab, (qv, T, sols) in results.items():
    print("==== secteur", lab, "q =", qv)
    for j, S in sorted(sols.items()):
        unk, d, free = S
        z = {f: 0 for f in free}
        for c in comps:
            a, b = int(c[0]), int(c[1])
            for n in range(NH - 1):
                v = sp.factor(sp.simplify(sp.sympify(d[unk[(n, a, b)]]).subs(z)))
                print("  h_%s  Omega^{%d%+di mu} : %s" % (c, n, j, v))
