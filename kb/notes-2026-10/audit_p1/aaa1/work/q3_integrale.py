#!/usr/bin/env python3
"""Q3 : I_N(eta) = int_0^inf dk k^{3-N} e^{-2 i k eta}, eta -> 0^-  (s = -eta > 0).
Formes fermees (avec coupure IR mu si necessaire), developpements en s, controle numerique N=3.
"""
import sympy as sp
import mpmath as mp

s, mu, Lam = sp.symbols('s mu Lambda', positive=True)
k = sp.symbols('k', positive=True)
a = -2 * sp.I * s  # a = 2 i eta = -2 i s ; convergence : Re a -> 0+ (prescription d'Abel)
eps = sp.symbols('epsilon', positive=True)

print('=' * 70)
print('Formule generale : int_mu^inf k^{3-N} e^{-a k} dk = a^{N-4} Gamma(4-N, a mu),  a = 2 i eta = -2 i s')
print('Pour mu -> 0 et N < 4 : a^{N-4} Gamma(4-N) ; definie par continuation analytique (Abel : a -> a + epsilon).')

# N = 3 : forme fermee exacte, sans coupure IR
I3 = sp.integrate(sp.exp(-(eps + a) * k), (k, 0, sp.oo), conds='none')
I3 = sp.limit(sp.simplify(I3), eps, 0)
print('\nN = 3 : I_3 = ', sp.simplify(I3), '  = i/(2 s) : |I_3| ~ s^{-1}')
# avec coupure IR mu
I3mu = sp.exp(-a * mu) / a
print('N = 3 avec coupure mu : I_3 = e^{-a mu}/a =', sp.series(sp.simplify(I3mu), s, 0, 2))

# N = 4 : Gamma(0, a mu) = E_1(a mu)
I4 = sp.expint(1, a * mu)
ser4 = sp.series(I4, s, 0, 2)
print('\nN = 4 : I_4 = E_1(a mu), developpement :', ser4)
print('   -> terme dominant : -ln(s) (log(a mu) = ln(2 s mu) - i pi/2)')

# N = 5 : a Gamma(-1, a mu) = a [ e^{-a mu}/(a mu) - E_1(a mu) ]
I5 = a * (sp.exp(-a * mu) / (a * mu) - sp.expint(1, a * mu))
ser5 = sp.series(I5, s, 0, 2)
print('\nN = 5 : I_5 = a Gamma(-1, a mu), developpement :', sp.simplify(ser5))
print('   -> constante IR 1/mu, puis terme en s ln s et terme lineaire en s ; pas de terme singulier.')

# cas gaussien : alpha beta* = Y e^{-k^2/Lambda^2} : I_G = int_0^inf k^3 e^{-k^2/Lambda^2} e^{-2 i k eta} dk
IG = sp.integrate(k**3 * sp.exp(-k**2 / Lam**2) * sp.exp(2 * sp.I * k * s), (k, 0, sp.oo), conds='none')
IG = sp.simplify(IG)
print('\nGaussien : I_G =', IG)
print('  developpement en s :', sp.series(IG, s, 0, 3))
print('  valeur en s=0 (limite) :', sp.limit(IG, s, 0), '  (= Lambda^4/2)')
print('  => fonction entiere de s : regulier, pas de singularite en s -> 0.')

# Developpement general non entier : I_N ~ Gamma(4-N) (2 i eta)^{N-4} = Gamma(4-N) (-2 i s)^{N-4} ~ s^{N-4}
print('\nLoi generale (mu -> 0, N < 4 non entier, ou partie singuliere pour N >= 4) : I_N ~ Gamma(4-N) (-2 i s)^{N-4}')
print('  N=3 : s^{-1} ; N=4 : ln s ; N=5 : s ln s (apres soustraction de la constante IR 1/mu).')

# ---------------- controle numerique N = 3 ----------------
print('\n' + '=' * 70)
print('Controle numerique N = 3 : int_0^inf e^{2 i k s} dk  (eta = -s)')
mp.mp.dps = 30
for sval in (mp.mpf('0.1'), mp.mpf('0.01'), mp.mpf('0.001')):
    exact = 1j / (2 * sval)
    # (a) quadosc sur partie reelle et imaginaire
    re = mp.quadosc(lambda kk: mp.cos(2 * sval * kk), [0, mp.inf], omega=2 * sval)
    im = mp.quadosc(lambda kk: mp.sin(2 * sval * kk), [0, mp.inf], omega=2 * sval)
    # (b) regularisation d'Abel e^{-eps k}, eps -> 0
    abel = []
    for e in (mp.mpf('1e-2') * sval, mp.mpf('1e-4') * sval):
        vr = mp.quadosc(lambda kk: mp.cos(2 * sval * kk) * mp.exp(-e * kk), [0, mp.inf], omega=2 * sval)
        vi = mp.quadosc(lambda kk: mp.sin(2 * sval * kk) * mp.exp(-e * kk), [0, mp.inf], omega=2 * sval)
        abel.append(mp.mpc(vr, vi))
    print(f's = {sval}: exact i/(2s) = {exact}')
    print(f'   quadosc : Re = {mp.nstr(re, 12)}, Im = {mp.nstr(im, 12)}')
    print(f'   Abel eps=1e-2 s : {mp.nstr(abel[0], 12)} ; eps=1e-4 s : {mp.nstr(abel[1], 12)}')
    print(f'   s * Im(I_3) = {mp.nstr(sval * im, 12)}  (attendu 0.5)')

# controle numerique N=4 et N=5 avec coupure mu : comparaison forme fermee / quadrature Abel
print('\nControle numerique N = 4, 5 avec coupure IR mu = 1 (quadosc)')
for N in (4, 5):
    for sval in (mp.mpf('0.1'), mp.mpf('0.01')):
        av = -2j * sval
        if N == 4:
            ff = mp.expint(1, av)
        else:
            ff = av * (mp.exp(-av) / av - mp.expint(1, av))
        nr = mp.quadosc(lambda kk: kk**(3 - N) * mp.cos(2 * sval * kk), [1, mp.inf], omega=2 * sval)
        ni = mp.quadosc(lambda kk: kk**(3 - N) * mp.sin(2 * sval * kk), [1, mp.inf], omega=2 * sval)
        num = mp.mpc(nr, ni)
        print(f'  N={N}, s={sval}: forme fermee {mp.nstr(ff, 10)} ; quadrature {mp.nstr(num, 10)}')

# controle numerique gaussien Lambda = 1
print('\nControle numerique gaussien (Lambda = 1)')
IGf = sp.lambdify(s, IG.subs(Lam, 1), 'mpmath')
for sval in (mp.mpf('0.5'), mp.mpf('0.05')):
    num = mp.quad(lambda kk: kk**3 * mp.exp(-kk**2) * mp.exp(2j * sval * kk), [0, mp.inf])
    print(f'  s={sval}: forme fermee {mp.nstr(mp.mpc(IGf(sval)), 12)} ; quadrature {mp.nstr(num, 12)}')
