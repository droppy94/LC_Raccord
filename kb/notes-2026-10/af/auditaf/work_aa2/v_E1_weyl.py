# Variante E1 : (1) dimension de l'espace des tenseurs de Weyl en 4D (resolution lineaire des symetries)
# (2) rang de l'application (E,B) -> W de af_check.py ; (3) T_ab = c0 b d^c d^d(sigma C_acbd) est symetrique et sans trace
import itertools, sympy as sp, re
src = open('af_check_copie.py').read()
head = src.split('# ---------------------------------------------------------------- AF-1')[0]
exec(head)
# (1) espace de Weyl
comp = {k: sp.Symbol('w_%d%d%d%d' % k) for k in itertools.product(range(4), repeat=4)}
eqs = []
for a,b_,c,d in itertools.product(range(4), repeat=4):
    w = comp
    eqs += [w[(a,b_,c,d)]+w[(b_,a,c,d)], w[(a,b_,c,d)]+w[(a,b_,d,c)], w[(a,b_,c,d)]-w[(c,d,a,b_)],
            w[(a,b_,c,d)]+w[(a,c,d,b_)]+w[(a,d,b_,c)]]
for b_,d in itertools.product(range(4), repeat=2):
    eqs.append(sum(eta[a,a]*comp[(a,b_,a,d)] for a in range(4)))
A = sp.Matrix([[sp.diff(e, v) for v in comp.values()] for e in eqs])
print("dim espace de Weyl (256 - rang des contraintes):", 256 - A.rank())
# (2) rang de (E,B) -> W
pars = [Ef[1,1],Ef[2,2],Ef[1,2],Ef[1,3],Ef[2,3],Bf[1,1],Bf[2,2],Bf[1,2],Bf[1,3],Bf[2,3]]
J = sp.Matrix([[sp.diff(Wt[k], p) for p in pars] for k in sorted(Wt)])
print("rang de l'application (E,B) -> W :", J.rank())
# chaque tenseur W satisfait-il toutes les symetries (pas seulement trace et cyclique) ?
ok = all(sp.simplify(Wt[(a,b_,c,d)]+Wt[(b_,a,c,d)])==0 and sp.simplify(Wt[(a,b_,c,d)]-Wt[(c,d,a,b_)])==0
         for a,b_,c,d in itertools.product(range(4), repeat=4))
print("antisymetrie et symetrie de paires :", ok)
# toutes les traces
oktr = all(sp.simplify(sum(eta[a,a]*Wt[(a,b_,c,a)] for a in range(4)))==0 for b_ in range(4) for c in range(4))
print("trace sur (1,4) nulle :", oktr)
# W_0i0j = E_ij et dualite : *W (dual gauche) a pour partie electrique +-B
# (3) symetrie et trace de T
sigma = -sp.log(Om_f); C = {k: Om_f*v for k,v in Wt.items()}
T = sp.Matrix(4,4, lambda a,b_: sum(up(c)*up(d)*sp.diff(sigma*C[(a,c,b_,d)], X[c], X[d]) for c in range(4) for d in range(4)))
print("T symetrique :", all(sp.expand(T[a,b_]-T[b_,a])==0 for a in range(4) for b_ in range(4)))
print("T sans trace (eta) hors couche :", sp.expand(sum(up(a)*T[a,a] for a in range(4)))==0)
