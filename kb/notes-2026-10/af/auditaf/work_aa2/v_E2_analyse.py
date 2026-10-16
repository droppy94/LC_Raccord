# Variante E2 : (a) structure en jets du second membre de (2.17) : ordre de derivation maximal de W et puissance minimale de Omega associee
# (b) composantes du pole dans le repere n=(1,0,0,0) et equation de transport homogene (lien avec la "divergence en ln" de W)
# (c) les logs sont-ils lineaires dans les seules combinaisons de divergence (residu apres reduction = 0) et a quel ordre de jets
import sympy as sp
src_txt = open('af_check_copie.py').read()
exec(src_txt.split('# ---------------- AF-3 (i)')[0])
print("\n=== analyse AA-2 ===")
def jet_order(sym):
    s_ = str(sym)
    if s_.startswith('d') and '_' in s_: return len(s_.split('_')[1])
    return 0
maxord = {}
for k_, v in src.items():
    L_ = laurent_log(v)
    for kk, c in L_.items():
        for t in sp.Add.make_args(c):
            o = max([jet_order(z) for z in t.free_symbols] + [0])
            maxord.setdefault(o, set()).add(kk)
for o in sorted(maxord):
    print("  jets d'ordre", o, "de W apparaissent aux (puissance, log) :", sorted(maxord[o]))
# (b) repere n = (1,0,0,0), lambda = 3, s = 0
cal = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0, s: 0, lam: 3}
print("  pole dans le repere de n (c0 symbolique), composantes non nulles :")
for k_ in sorted(pole):
    v = sp.factor(pole[k_].subs(cal))
    if v != 0: print("    R", k_, ":", v, "/Omega")
# cote gauche de (2.17) pour (rho, nu, lambda) = (j, 0, i) : d^mu W_mu j 0 i
for (j, i) in [(1, 1), (2, 2), (1, 2)]:
    lhs = sum(up(m)*sp.diff(Wt[(m, j, 0, i)], X[m]) for m in idx)
    print("    LHS (2.17) (%d,0,%d) :" % (j, i), lhs)
# (c) residu des logs hors divergence : deja on_shell == 0 ; on verifie que chaque coefficient log est nul sur s1,s2,s3 et non nul hors couche
nz = sum(1 for v in logs.values() for vv in v.values() if vv != 0)
print("  coefficients log non nuls hors couche :", nz, "; nuls sur couche :", all(on_shell(vv) == 0 for v in logs.values() for vv in v.values()))
# ordre maximal de jets dans les logs
mo = max(jet_order(z) for v in logs.values() for vv in v.values() for z in vv.free_symbols)
print("  ordre maximal de jets de W dans les coefficients log :", mo)
