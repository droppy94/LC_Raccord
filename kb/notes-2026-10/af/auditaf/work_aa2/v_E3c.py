# Variante E3 (c) : AF-2 sans sigma. mode 'beta0' : beta_* = 0 ; mode 'omega' : sigma remplace par Omega (couplage 1/e2 - 4 beta_* Omega) ;
# mode 'ref' : couplage d'origine (controle). Attendu : ni pole dans l'equation de Maxwell, ni log dans (2.17), sauf 'ref'.
import sys, sympy as sp
mode = sys.argv[1]
txt = open('af_check_copie.py').read()
exec(txt.split('# ---------------------------------------------------------------- AF-1')[0])
sigma = -sp.log(Om_f)
lines = txt.split('\n')
blk = '\n'.join(lines[124:144])          # nf ... jetify (lignes 125-144 du script)
assert blk.startswith('nf = ') and 'def jetify' in blk
exec(blk)
nS = list(n); nupS = [up(a)*n[a] for a in idx]
af2 = txt.split('# ---------------------------------------------------------------- AF-2 : sigma F^2')[1].split('# AF-3 (ii)')[0]
newc = {'ref': 'coup = 1/e2 - 4*betas*sigma', 'beta0': 'coup = 1/e2', 'omega': 'coup = 1/e2 - 4*betas*Om_f'}[mode]
af2 = af2.replace('coup = 1/e2 - 4*betas*sigma', newc)
cut = af2.split('Mj = M.applyfunc(jetify)')[0]
print("=== variante E3(c), mode", mode, ":", newc, "===")
exec(cut)
allk = sorted({kk for v in src2.values() for kk in laurent_log(v)})
print("  (puissance, log) dans le second membre de (2.17) :", allk)
print("  pole dans Maxwell :", any(sp.expand(z*W).subs(W, 0) != 0 for z in rhs_div_j), "; log dans (2.17) :", any(kk[1] > 0 for kk in allk))
