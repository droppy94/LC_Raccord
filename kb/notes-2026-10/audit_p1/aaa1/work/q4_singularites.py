#!/usr/bin/env python3
"""Q4 : support singulier du terme alpha beta* de w(x,x') pour alpha beta* = f(k^) (direction seule).
w_3(x,x') = int d^3k/(2k(2pi)^3) f(k^) e^{-ik tau} e^{i k.Dx},  tau = eta + eta', Dx = x - x'.
Integrale radiale : int_0^inf k dk e^{i k u} = -1/(u + i0)^2, u = k^.Dx - tau.
Donc w_3 = -(1/(2(2pi)^3)) int dOmega f(k^) / (k^.Dx - tau + i0)^2.
On calcule l'integrale angulaire pour f = 1 (isotrope) et f = P_2(k^.n) (quadrupole axial),
et pour la loi de puissance k^{-N} on donne l'integrale radiale.
"""
import sympy as sp

c, r, tau = sp.symbols('c r tau', real=True)
u = sp.symbols('u', real=True)
k = sp.symbols('k', positive=True)
N = sp.symbols('N')

print('=' * 70)
print('Integrale radiale (f ne dependant que de la direction) : int_0^inf k e^{iku} dk')
Ir = sp.integrate(k * sp.exp(sp.I * k * u - sp.Symbol('eps', positive=True) * k), (k, 0, sp.oo), conds='none')
print('  avec amortissement eps :', sp.simplify(Ir), '  -> -1/(u+i0)^2 quand eps -> 0')

# integrale angulaire : dOmega = 2 pi dc sur c = k^.n, n = Dx/|Dx| ; k^.Dx = r c
def ang(f):
    return 2 * sp.pi * sp.integrate(f / (r * c - tau) ** 2, (c, -1, 1))

print('\nIntegrale angulaire pour |tau| > r (exterieur du cone reflechi), f = 1 :')
A1 = sp.simplify(ang(1))
print('  ', A1)
print('   -> singulier exactement sur tau^2 = r^2 ; w_3 isotrope = fonction de Wightman du vide au point image (-eta\', x\').')

print('\nIntegrale angulaire pour f = P_2(c) = (3c^2-1)/2 (quadrupole axial autour de n = Dx/|Dx|) :')
P2 = (3 * c ** 2 - 1) / 2
A2 = sp.simplify(ang(P2))
print('  ', A2)
print('   singularites : poles 1/(tau^2 - r^2) et log((tau - r)/(tau + r)) -> support singulier = {tau^2 = r^2}.')
print('   Pour |tau| < r : continuation analytique via tau -> tau - i0 : le log acquiert une partie i pi,')
print('   la fonction reste lisse a l\'interieur du cone ; seules les extremites c = +-1 (k^ parallele a Dx) produisent la singularite.')

# verification : developpement pres de tau = r (tau = r + d)
d = sp.symbols('d', positive=True)
print('\nComportement de l\'integrale f=P_2 pres de tau = r + d, d -> 0+ :')
print('  ', sp.series(A2.subs(tau, r + d), d, 0, 1))

# loi de puissance k^{-N} : integrale radiale int_0^inf k^{1-N} e^{iku} dk (UV convergente pour N>0 au sens d'Abel ; IR convergente ssi N<2)
print('\nLoi de puissance alpha beta* = k^{-N} f(k^) : integrale radiale int_mu^inf k^{1-N} e^{iku} dk = (-iu)^{N-2} Gamma(2-N, -iu mu)')
mu = sp.symbols('mu', positive=True)
for Nv in (3, 4, 5):
    a = -sp.I * u
    expr = a ** (Nv - 2) * sp.uppergamma(2 - Nv, a * mu)
    ser = sp.series(expr, u, 0, Nv - 1)
    print(f'  N = {Nv} : partie non analytique en u = 0 :', sp.simplify(ser))
print('  -> integrale radiale : singularite de type u^{N-2} ln|u| en u = 0 (N entier).')
print('     L\'integration angulaire (une primitive en c pres des extremites c = +-1) eleve l\'ordre d\'une unite :')
print('     en un point generique du cone reflechi, w_3 ~ (tau -+ r)^{N-1} ln|tau -+ r| :')
print('     N=3 : C^1 non C^2 ; N=4 : C^2 non C^3 ; N=5 : C^3 non C^4 (verifie ci-dessous pour f = 1, N = 3).')
print('     Au sommet du cone (Dx = 0, tau = 2 eta -> 0) pas de lissage angulaire : w_3 ~ tau^{N-2} ln|tau|, T ~ tau^{N-4}.')
# verification f = 1, N = 3 : int_{-1}^{1} (rc - tau) log(rc - tau) dc
chk = sp.integrate((r * c - tau) * sp.log(r * c - tau), (c, -1, 1))
print('  controle f=1, N=3, integrale angulaire de u ln u :', sp.simplify(chk))
print('     -> termes (tau - r)^2 ln(tau - r) et (tau + r)^2 ln(tau + r) : C^1 non C^2 sur tau = +-r.')
print('     Pour tout N fini, w_3 n\'est pas C^infini : singularite portee par le cone reflechi tau^2 = r^2,')
print('     et non par le cone de lumiere (eta - eta\')^2 = r^2. Les deux ne coincident que si eta eta\' = 0.')
