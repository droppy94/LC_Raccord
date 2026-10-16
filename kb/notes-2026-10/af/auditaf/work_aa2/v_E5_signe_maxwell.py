# Variante E5/E6 : signe du pole de l'equation de Maxwell. Comparaison du second membre du script avec +-4 e2 beta_* n^a F_ab / Omega
import sympy as sp
n = sp.symbols('n0:4', real=True); W = sp.Symbol('Omega', positive=True); betas, e2 = sp.symbols('beta_* e2', real=True)
eta = [-1, 1, 1, 1]
Fs = {(a, b): sp.Symbol('F%d%d' % (a, b), real=True) for a in range(4) for b in range(4) if a < b}
F = lambda a, b: 0 if a == b else (Fs[(a, b)] if a < b else -Fs[(b, a)])
script = [4*betas*e2*(Fs[(0,1)]*n[1] + Fs[(0,2)]*n[2] + Fs[(0,3)]*n[3])/W, 4*betas*e2*(Fs[(0,1)]*n[0] + Fs[(1,2)]*n[2] + Fs[(1,3)]*n[3])/W,
          4*betas*e2*(Fs[(0,2)]*n[0] - Fs[(1,2)]*n[1] + Fs[(2,3)]*n[3])/W, 4*betas*e2*(Fs[(0,3)]*n[0] - Fs[(1,3)]*n[1] - Fs[(2,3)]*n[2])/W]
nF = [sum(eta[a]*n[a]*F(a, b) for a in range(4)) for b in range(4)]     # n^a F_ab
print("script == +4 e2 beta n^a F_ab / Omega :", all(sp.expand(script[b] - 4*e2*betas*nF[b]/W) == 0 for b in range(4)))
print("script == -4 e2 beta n^a F_ab / Omega :", all(sp.expand(script[b] + 4*e2*betas*nF[b]/W) == 0 for b in range(4)))
# derivation directe : d^a[(1/e2 + 4 beta ln Omega) F_ab] = 0  =>  d^a F_ab = -4 e2 beta n^a F_ab / Omega + O(beta^2)
