# Variante E3 (a) : sigma remplace par une fonction lisse de Omega (f = Omega, f = 1, f = Omega^2) dans T_ab = c0 b d d (f C).
# Attendu : ni pole ni log dans le second membre de (2.17).
import sys, sympy as sp
mode = sys.argv[1]
txt = open('af_check_copie.py').read()
part = txt.split('# divergence constraints in jets')[0]
repl = {'omega': 'sigma = Om_f', 'un': 'sigma = sp.Integer(1)', 'omega2': 'sigma = Om_f**2'}[mode]
assert 'sigma = -sp.log(Om_f)' in part
part = part.replace('sigma = -sp.log(Om_f)', repl)
part = part.replace('sol = sp.solve([d_ for d_ in diffs if d_ != 0][:6], alpha_s, dict=True)', 'sol = []')
exec(part)
print("\n=== variante E3(a), mode", mode, ":", repl, "===")
allk = sorted({kk for v in src.values() for kk in laurent_log(v)})
print("  (puissance, log) presents dans le second membre de (2.17) :", allk)
print("  pole (Omega^-1) present :", any(kk[0] < 0 for kk in allk), "; log present :", any(kk[1] > 0 for kk in allk))
allT = sorted({kk for a in idx for bb in idx for kk in laurent_log(Thj[a, bb])})
print("  (puissance, log) presents dans That :", allT)
