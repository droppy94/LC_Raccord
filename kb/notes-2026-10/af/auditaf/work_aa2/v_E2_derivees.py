# Variante E2 bis : apres reduction d'ordre (div W = 0 et derivees), le second membre non logarithmique de (2.17)
# contient-il encore des derivees de W (modification de la partie principale) ? A quelle puissance de Omega ?
import sympy as sp
src_txt = open('af_check_copie.py').read()
exec(src_txt.split('# ---------------- AF-3 (i)')[0])
print("\n=== analyse AA-2 (derivees residuelles) ===")
def jet_order(sym):
    s_ = str(sym)
    if s_.startswith('d') and '_' in s_: return len(s_.split('_')[1])
    return 0
res = {}
ex = None
for k_, v in src.items():
    for kk, c in laurent_log(v).items():
        if kk[1] > 0: continue
        cs = on_shell(c)
        for t in sp.Add.make_args(cs):
            o = max([jet_order(z) for z in t.free_symbols] + [0])
            if o > 0:
                res.setdefault((kk, o), 0); res[(kk, o)] += 1
                if ex is None and kk == (0, 0): ex = (k_, t)
print("  termes contenant des jets de W (ordre>=1) apres reduction, par ((puissance,log), ordre) :", res)
print("  exemple a Omega^0 :", ex)
cal = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0, s: 0, lam: 3}
c00 = on_shell(laurent_log(src[(1, 0, 1)]).get((0, 0), 0)).subs(cal)
print("  R(1,0,1) a Omega^0, repere n=(1,0,0,0), apres reduction :", sp.factor(c00))
