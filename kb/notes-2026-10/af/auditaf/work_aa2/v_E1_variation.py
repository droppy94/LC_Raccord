# Variante E1 bis : forme fermee. Au premier ordre autour de eta, delta Int sigma C^2 = 2 Int sigma C^abcd delta R_abcd[h]
# avec R_abcd[h] = 1/2 (d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac). On verifie C^abcd R_abcd[h] = -2 C^abcd d_a d_c h_bd
# (pour C de Weyl), d'ou, par deux integrations par parties, T_bd = 2 dS/dg_bd = -8 b d^a d^c (sigma C_abcd) = -8 b d^c d^d (sigma C_acbd) (lettres renommees).
import itertools, sympy as sp
src = open('af_check_copie.py').read()
exec(src.split('# ---------------------------------------------------------------- AF-1')[0])
Wc = {k: v.subs({f: sp.Symbol(str(f.func)) for f in sp.sympify(v).atoms(sp.Function)}) if v != 0 else 0 for k, v in Wt.items()}
h = {}
for a in idx:
    for b_ in idx:
        h[(a,b_)] = h.get((b_,a)) or sp.Function('h%d%d' % (a,b_))(*X)
dd = lambda f, a, c: sp.diff(f, X[a], X[c])
up4 = lambda a,b_,c,d: up(a)*up(b_)*up(c)*up(d)
lhs = sum(up4(a,b_,c,d)*Wc[(a,b_,c,d)]*sp.Rational(1,2)*(dd(h[(a,d)],b_,c)+dd(h[(b_,c)],a,d)-dd(h[(b_,d)],a,c)-dd(h[(a,c)],b_,d))
          for a,b_,c,d in itertools.product(idx, repeat=4))
rhs = -2*sum(up4(a,b_,c,d)*Wc[(a,b_,c,d)]*dd(h[(b_,d)],a,c) for a,b_,c,d in itertools.product(idx, repeat=4))
print("C.R[h] = -2 C^abcd d_a d_c h_bd :", sp.expand(lhs-rhs)==0)
print("donc S = b Int sigma C^2 -> delta S = -4 b Int d_a d_c(sigma C^abcd) h_bd, T_ab = -2 dS/dg^ab = +2 dS/dg_ab = -8 b d^c d^d(sigma C_acbd) : c0 = -8 (convention T = -2/sqrt(g) dS/dg^ab)")
