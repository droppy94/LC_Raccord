# analyse symbolique en mu : denominateurs (poles eventuels), ordres minimaux, dependance aux parametres libres
import sympy as sp, pickle, sys
from spinors import mu
results, NH, MUNUM = pickle.load(open(sys.argv[1], 'rb'))
TRUST = NH - 2
print("NH =", NH, "; mu symbolique :", MUNUM is None, "; ordres fiables n <=", TRUST)
for lab, (qv, T, sols) in results.items():
    print("==== secteur", lab, "q =", qv)
    dens = set()
    for j, S in sols.items():
        unk, d, free = S
        firstnz = {}
        for (n, a, b), sym in sorted(unk.items()):
            if n > TRUST: continue
            v = sp.factor(sp.simplify(sp.sympify(d[sym])))
            if v != 0:
                firstnz.setdefault((a, b), n)
                num, den = sp.fraction(sp.together(v))
                for f, e in sp.factor_list(den)[1]:
                    if f.has(mu): dens.add(f)
            if (a, b) == (0, 0) and n <= 4:
                print("   j=%+d  h_00 coefficient de Omega^{%d%+di mu} = %s" % (j, n, j, str(v)[:200]))
        print("   j=%+d  ordre minimal non nul (avec parametres libres) :" % j, firstnz, "; libres :", sorted(map(str, free)))
    print("   facteurs de denominateurs dependant de mu :", dens)
    for f in dens:
        r = sp.solve(f, mu)
        print("      ", f, " -> racines en mu :", r, " (reelles positives :", [x for x in r if x.is_real and x.is_positive], ")")
