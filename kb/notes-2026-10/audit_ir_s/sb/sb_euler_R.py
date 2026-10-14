import sympy as sp, pickle
from sb_lib import s, x, X, eta, christoffel_full, covd2, lin_curv
back, res = pickle.load(open('sb_euler.pkl', 'rb'))
k, A, B, b, a, kap, wE, wR, wD = sp.symbols('k A B b a kappa w_E w_R w_D')
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
ghat = s**-2*eta; Gam = christoffel_full(ghat)
# 1) partie C de la chaine non lineaire vs forme fermee de l'audite (c0 = -8)
H = sp.zeros(4, 4); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
_, _, _, _, C = lin_curv(H)
Tcl = -8*sp.expand(sum(eta[c,c]*eta[d,d]*sp.diff(-sp.log(s)*C[(2,c,2,d)], X[c], X[d]) for c in range(4) for d in range(4)))
print("1) T_yy[C] chaine non lineaire - forme fermee c0=-8 :", sp.simplify(res['C'] - Tcl))
# 2) partie a : T_yy^(1) = sum w_i T_i ; on retire la piece c*g_yy^(1) du fond (c = coefficient de eta dans T de fond)
for key in 'ERD':
    print(f"   T_yy^(1)[{key}] * s^4 / cos kx =", sp.factor(sp.simplify(res[key]*s**4/sp.cos(k*x))))
def Rpole(Tyy1, cback):
    # cback : T_ab(fond) = cback * s^-4 * eta_ab (si de cette forme) ; partie non ~ g :
    Tp = sp.simplify(Tyy1 - cback*s**-4*u*sp.cos(k*x))
    Th = sp.zeros(4, 4); Th[2, 2] = sp.expand(s**2*Tp); Th[3, 3] = -Th[2, 2]
    L = (kap/2*Th)
    R = sp.simplify((covd2(L, Gam, 2, 2, 0) - covd2(L, Gam, 0, 2, 2))/s)
    return Tp, sp.simplify(sp.limit(s*R, s, 0)), sp.expand(sp.series(R, s, 0, 1).removeO())
# fond par morceau : T^ss_i = -2dS/dN, T^yy_i ; ~ eta ssi T^ss = -T^yy
for key in 'ERD':
    print(f"   fond [{key}] : T^ss = {-back[key][0]}, T^yy = {back[key][1]}")
Tss = sum(w*(-back[kk][0]) for w, kk in zip((wE, wR, wD), 'ERD')); Tyy0 = sum(w*back[kk][1] for w, kk in zip((wE, wR, wD), 'ERD'))
print("2) combinaison w_E E + w_R(-2/3 sig boxR) + w_D(2 sig Delta4 sig) : fond T^ss + T^yy (nul ssi fond ~ eta) =", sp.simplify(Tss + Tyy0))
Tyy1 = sum(w*res[kk] for w, kk in zip((wE, wR, wD), 'ERD'))
# partie de T_yy^(1) non proportionnelle a g_yy^(1), avec c = T^yy de fond * s^4 (eta_yy = 1)
Tp, res_pole, Rser = Rpole(Tyy1, sp.simplify(Tyy0*s**4))
print("   T'_yy (partie non ~ g) =", sp.factor(Tp))
print("   residu polaire de R_ysy (partie a) :", sp.factor(res_pole))
for lab, sub in (("WZ integrable (1,1,1)", {wE: 1, wR: 1, wD: 1}), ("variante -1/2 phi Delta4 phi (1,1,-1/4)", {wE: 1, wR: 1, wD: sp.Rational(-1, 4)}),
                 ("E seul (1,0,0)", {wE: 1, wR: 0, wD: 0})):
    print(f"   {lab} : T'_yy = {sp.factor(Tp.subs(sub))} ; fond T^ss+T^yy = {sp.simplify((Tss+Tyy0).subs(sub))} ; residu polaire = {sp.factor(res_pole.subs(sub))}")
_, pC, RC = Rpole(b*res['C'], 0)
print("3) partie C : residu polaire R_ysy =", sp.factor(pC), " ; W_E,yy(scri) = -B k^3 cos(kx)/2 => residu/(8 b kappa W_E) =", sp.simplify(pC/(8*b*kap*(-B*k**3*sp.cos(k*x)/2))))
