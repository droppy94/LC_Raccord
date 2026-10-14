"""audit_db_etat.py -- contre-exemple d'etat : branche electrique seule, et superposition de poids egaux
(type Bunch-Davies hors horizon : k^2|u0|^2 = |c|^2), premier ordre en beta, ordre dominant en s."""
import sympy as sp, itertools as it
exec(open('audit_db_indep.py').read().split('# ---------- (b) mode ----------')[0])
k, e, beta, kap, u0, c, lam, Cr = sp.symbols('k e beta kappa u0 c lambda C_r', positive=True)
b1 = sp.symbols('b1')
I2ex = (1 + 2*beta*(lam - sp.log(s)))/e**2
src = open('audit_db_indep.py').read()
ns = {}
for name in ('def XM_avg', 'def cov_D', 'def R_from', 'def closure'):
    pass
code = src.split('# ---------- (c) X^M mixte et moyenne ----------')[1].split('Tm, F2m = XM_avg')[0]
code2 = src.split('# ---------- (d) fermeture C-iso et (e) R ----------')[1].split('# cas uniforme exact')[0]
exec(code); exec(code2)
def first(v, order):
    v = sp.expand(sp.series(sp.expand(v), s, 0, order).removeO())
    return sp.expand(v.coeff(beta, 0) + beta*v.coeff(beta, 1))
def R_branch(ufun):
    T, F2 = XM_avg(ufun, I2ex)
    T = T.applyfunc(lambda v: first(v, 4))
    Th = sp.expand(-(beta/(2*e**2))*sp.series(F2, s, 0, 2).removeO().subs(beta, 0)*s**4)
    Tt, r0s, divs = closure(T, Th)
    R = R_from(Tt)
    out = {}
    for key, v in R.items():
        v = first(v, 1)
        out[key] = sp.collect(v, sp.log(s))
    return T, out
U1e = 2*c*s*sp.log(s) + b1*c*s - c*k**2*s**3*sp.log(s)/3
ue = c/k*sp.sin(k*s) + beta*U1e
Te, Re = R_branch(ue)
print("electrique <X^M> diag :", [sp.factor(Te[i, i]) for i in range(4)])
for kk, v in Re.items(): print("  R elec", kk, ":", v)
um = u0*sp.cos(k*s) + beta*(-u0*k**2*s**2 + u0*k**4*s**4/9)
Tm, Rm = R_branch(um)
print("somme de poids egaux (c = k u0) :")
for kk in Rm:
    tot = sp.collect(sp.expand(Rm[kk] + Re.get(kk, 0).subs(c, k*u0)), sp.log(s))
    print("  R tot", kk, ":", tot)
Ttot = (Tm + Te.subs(c, k*u0)).applyfunc(sp.expand)
print("  <X^M> tot diag :", [sp.collect(Ttot[i, i], sp.log(s)) for i in range(4)])
# moyenne isotrope (direction de k et polarisation) : partie spatiale -> (1/3) trace spatiale
sp_tr = sp.expand(sum(Ttot[i, i] for i in (1, 2, 3)))
print("  apres isotropisation : T_ss =", sp.collect(Ttot[0, 0], sp.log(s)), "; T_ii (chaque) =", sp.collect(sp_tr/3, sp.log(s)))
print("EXIT 0")
