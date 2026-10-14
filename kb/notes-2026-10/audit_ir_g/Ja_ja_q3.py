# Q3 : test de la loi R_{i s j}|_{beta s^0 ln s} = 3 (kappa/e^2) (Q_ij - delta_ij trQ/3) sur des Q non diagonaux
import sympy as sp
from ja_core import *
from ja_q2 import run, Qtensor

u0, c, k, v0, d, q, th = sp.symbols('u0 c k v0 d q theta', positive=True)


def check(modes_data, label, cross=True):
    modes = [(mode_u(a, cc, sp.sqrt(sum(t**2 for t in kv))), kv, ep) for (a, cc, kv, ep) in modes_data]
    out, XM, R = run(modes, label, cross=cross)
    Q = Qtensor(modes_data) if cross else sum((Qtensor([m]) for m in modes_data), sp.zeros(3))
    trQ = Q.trace(); Qt = Q - sp.eye(3)*trQ/3
    print(' Q =', sp.simplify(Q).tolist())
    bad = []
    for i in range(3):
        for j in range(3):
            diff = sp.simplify(out.get((i+1, 0, j+1), 0) - 3*kap/e**2*Qt[i, j])
            if diff != 0:
                bad.append(((i, j), diff))
    others = {kk: v for kk, v in out.items() if not (kk[1] == 0 and kk[0] > 0)}
    print(' ecart a la loi 3 kappa/e^2 Q^TF :', bad if bad else 'AUCUN', '; autres composantes avec ln :', others)
    # loi locale (avant moyenne) de X^M : verif <X^M_ij>_ln = (2Q_ij - delta trQ)/e^2, <X^M_si>_ln = 0
    bad2 = []
    for i in range(3):
        for j in range(3):
            dd = sp.simplify(coeff_sp_ln(XM[i+1, j+1].coeff(beta, 1), 2, 1) - (2*Q[i, j] - (trQ if i == j else 0))/e**2)
            if dd != 0:
                bad2.append(((i, j), dd))
        dd = sp.simplify(coeff_sp_ln(XM[0, i+1].coeff(beta, 1), 2, 1))
        if dd != 0:
            bad2.append((('s', i), dd))
    print(' ecart <X^M>_ln a (2Q - d trQ)/e^2 :', bad2 if bad2 else 'AUCUN')
    return Q


# (a) mode unique a polarisation oblique
check([(u0, c, [k, 0, 0], [0, sp.cos(th), sp.sin(th)])], '(a) un mode, k||x, eps oblique (0,cos th, sin th)')
# (b) deux modes de directions differentes, polarisation du second oblique
e2 = [1/sp.sqrt(2), 0, 1/sp.sqrt(2)]
check([(u0, c, [k, 0, 0], [0, 1, 0]), (v0, d, [0, q, 0], e2)], '(b) deux modes k1||x eps1||y, k2||y eps2=(1,0,1)/sqrt2')
# (c) deux modes de meme k, polarisations y et z (termes croises de meme k)
check([(u0, c, [k, 0, 0], [0, 1, 0]), (v0, d, [k, 0, 0], [0, sp.Rational(3, 5), sp.Rational(4, 5)])], '(c) deux modes meme k||x, eps y et (0,3/5,4/5), croises inclus')
# (d) deux modes k1 = (k,0,0), k2 = (k,k,0) obliques
check([(u0, c, [k, 0, 0], [0, 1, 0]), (v0, d, [k, k, 0], [0, 0, 1])], '(d) k1=(k,0,0) eps y ; k2=(k,k,0) eps z')

# Verification directe des termes croises par integration sur la boite (cas b, k=1, q=2), coefficient s^2 beta ln s de X^M
print('\n== Verification directe (cas b) par integration spatiale, k=1, q=2 ==')
sub = {k: 1, q: 2}
mod = [(u0, c, [1, 0, 0], [0, 1, 0]), (v0, d, [0, 2, 0], e2)]
A = sp.zeros(4, 1)
for (a, cc, kv, ep) in mod:
    uu = mode_u(a, cc, sp.sqrt(sum(t**2 for t in kv)))
    uu = trunc(uu, 3)
    ph = kv[0]*x + kv[1]*y + kv[2]*z
    for i in range(3):
        A[i+1] += uu*ep[i]*sp.cos(ph)
F = sp.zeros(4)
for m in range(4):
    for n in range(4):
        F[m, n] = sp.diff(A[n], X[m]) - sp.diff(A[m], X[n])
XMf, FFf = XM_from_Fpair(F, F)
XMf = XMf.applyfunc(sp.expand)
XMa, _ = averaged_XM([(mode_u(a, cc, sp.sqrt(sum(t**2 for t in kv))), kv, ep) for (a, cc, kv, ep) in mod])
for (m, n) in [(0, 0), (0, 1), (0, 3), (1, 1), (1, 3), (2, 2), (3, 3), (1, 2)]:
    cf = coeff_sp_ln(XMf[m, n].coeff(beta, 1), 2, 1)
    cf0 = coeff_sp_ln(XMf[m, n].coeff(beta, 0), 2, 0)
    av = sp.integrate(sp.integrate(cf, (x, 0, 2*sp.pi)), (y, 0, 2*sp.pi))/(4*sp.pi**2)
    av0 = sp.integrate(sp.integrate(cf0, (x, 0, 2*sp.pi)), (y, 0, 2*sp.pi))/(4*sp.pi**2)
    # part croisee = produit u0*v0, c*d, u0*d, c*v0
    cross = [sp.expand(cf).coeff(a1, 1).coeff(a2, 1) for (a1, a2) in [(u0, v0), (c, d), (u0, d), (c, v0)]]
    print(' X^M_%s%s : terme croise local non nul ? %s ; <.> integre = %s ; formule moyenne = %s ; <beta^0 s^2> = %s'
          % ('sxyz'[m], 'sxyz'[n], any(sp.simplify(t) != 0 for t in cross), sp.simplify(av),
             sp.simplify(coeff_sp_ln(XMa[m, n].coeff(beta, 1), 2, 1)), sp.simplify(av0)))
