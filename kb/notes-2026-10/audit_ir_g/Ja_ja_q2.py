# Q2 : mode unique, partie homogene, fermeture C-iso, coefficients de ln s a l'ordre s^0 dans R
import sympy as sp
from ja_core import *

u0, c, k = sp.symbols('u0 c k', positive=True)


def run(modes, label, cross=True, verbose=True):
    XM, FF = averaged_XM(modes, cross=cross)
    XR, div, free, C = closure_Ciso(XM, FF)
    T = (XM + XR).applyfunc(sp.expand)
    trT = sp.expand(sum(ghi[m, n]*T[m, n] for m in range(4) for n in range(4)))
    That = sp.expand(-(beta/(2*e**2))*FF*s**4)
    out = {}
    if verbose:
        print('==', label)
        print(' checks: trace-That (<=s^5) =', trunc(trT - That, 5), '; div O(beta^0,beta^1) (<=s^4) =', [(trunc(sp.expand(d).coeff(beta,0), 4), trunc(sp.expand(d).coeff(beta,1), 4)) for d in div],
              '; inconnues libres X^R :', free)
        print(' X^R_ss =', trunc(XR[0, 0], 3))
    R, L = Rtensor(T)
    for key, val in R.items():
        cf = coeff_sp_ln(sp.expand(val).coeff(beta, 1), 0, 1)
        cf2 = coeff_sp_ln(sp.expand(val).coeff(beta, 1), 0, 2)
        # termes plus singuliers que s^0 avec log ?
        sing = [coeff_sp_ln(sp.expand(val).coeff(beta, 1), p, 1) for p in (-3, -2, -1)]
        if cf != 0 or cf2 != 0 or any(t != 0 for t in sing):
            out[key] = sp.factor(cf)
            if verbose:
                print('  R_%s%s%s : [beta s^0 ln s] =' % tuple('sxyz'[i] for i in key), sp.factor(cf),
                      ('; ln^2 : %s' % cf2) if cf2 != 0 else '', ('; singulier : %s' % sing) if any(t != 0 for t in sing) else '')
    # ordre beta^0, verifier absence de ln
    l0 = [coeff_sp_ln(sp.expand(v).coeff(beta, 0), 0, 1) for v in R.values()]
    if verbose:
        print('  ln s a beta^0 dans R :', set(l0))
    # Q tenseur a scri
    return out, XM, R


def Qtensor(modes_data):
    """modes_data: liste (u0,c,kvec,eps) ; Q_ij = <B_iB_j - E_iE_j>, E = c eps cos, B = -u0 (k x eps) sin"""
    Q = sp.zeros(3)
    groups = {}
    for (a, cc, kv, ep) in modes_data:
        groups.setdefault(tuple(kv), []).append((a, cc, sp.Matrix(kv), sp.Matrix(ep)))
    for kv, lst in groups.items():
        Bv = sum((-a*kvv.cross(ep) for (a, cc, kvv, ep) in lst), sp.zeros(3, 1))
        Ev = sum((cc*ep for (a, cc, kvv, ep) in lst), sp.zeros(3, 1))
        Q += (Bv*Bv.T - Ev*Ev.T)/2
    return Q.applyfunc(sp.expand)


if __name__ == '__main__':
    modes = [(mode_u(u0, c, k), [k, 0, 0], [0, 1, 0])]
    out, XM, R = run(modes, 'mode unique k||x eps||y')
    Q = Qtensor([(u0, c, [k, 0, 0], [0, 1, 0])])
    trQ = Q.trace(); Qt = Q - sp.eye(3)*trQ/3
    print(' Q =', Q.tolist(), ' trQ =', trQ)
    print(' Q sans trace =', Qt.tolist())
    # moyenne de X^M ln : verifier 2Q - delta trQ
    for i in range(3):
        print('  <X^M_%s%s> [s^2 beta ln s] =' % ('xyz'[i], 'xyz'[i]), sp.factor(coeff_sp_ln(XM[i+1, i+1].coeff(beta, 1), 2, 1)),
              ' vs (2Q - d trQ)/e^2 =', sp.factor((2*Q[i, i] - trQ)/e**2))
    print('  <X^M_ss> [s^2 beta ln s] =', sp.factor(coeff_sp_ln(XM[0, 0].coeff(beta, 1), 2, 1)), ' vs -trQ/e^2 =', sp.factor(-trQ/e**2))
    # ajustement de la loi R_{i s j} = alpha * kappa/e^2 * Qt_ij + gamma * kappa/e^2 * trQ delta_ij
    al, ga = sp.symbols('alpha gamma')
    print(' Ajustement loi :')
    eqs = []
    for i in range(3):
        for j in range(3):
            key = (i+1, 0, j+1)
            val = out.get(key, 0)
            eqs.append(sp.expand(val - (al*Qt[i, j] + ga*trQ*(1 if i == j else 0))*kap/e**2))
    print('  R_{i s j}:', sp.solve(eqs, [al, ga], dict=True))
    print('  composantes non nulles :', list(out.keys()))
