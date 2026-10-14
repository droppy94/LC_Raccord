# Q4 : source eteinte ; Q5 : dipole magnetique coherent
import sympy as sp

s, k, a, D, ks, xx = sp.symbols('s k a D k_star x', positive=True)
kx, th, ph = sp.symbols('kx theta phi', real=True)

print('== Q4 ==')
# libre pour s < D (tau > -D) : u_ss + k^2 u = 0, u(D)=a, du/dtau(-D)=0 <=> u_s(D)=0
u = sp.Function('u')
sol = sp.dsolve(sp.Eq(u(s).diff(s, 2) + k**2*u(s), 0), u(s), ics={u(D): a, u(s).diff(s).subs(s, D): 0}).rhs
sol = sp.simplify(sol)
print(' u(s) =', sol)
u0 = sp.simplify(sol.subs(s, 0)); c = sp.simplify(sol.diff(s).subs(s, 0))
print(' u0 = u(0) =', u0, ' ; c = u_s(0) =', c)
print(' mode k||x eps||y : B_z = -k u0 sin kx =', sp.simplify(-k*u0), '* sin(kx) ; E_y = c cos kx =', c, '* cos(kx)')
Q = sp.diag(0, -c**2/2, (k*u0)**2/2)
Qe = Q.applyfunc(lambda t: sp.expand(sp.expand_trig(sp.simplify(sp.fu(t)))))
Qe = Q.applyfunc(lambda t: sp.expand(sp.expand(t).subs({sp.sin(D*k)**2: (1-sp.cos(2*D*k))/2, sp.cos(D*k)**2: (1+sp.cos(2*D*k))/2})))
print(' Q =', Qe.tolist())
cz = sp.Symbol('C2')
Qc = Qe.applyfunc(lambda t: sp.expand(sp.expand(t).subs(sp.cos(2*D*k), cz)))
Q_indep = Qc.applyfunc(lambda t: t.coeff(cz, 0)); Q_dep = Qc.applyfunc(lambda t: t.coeff(cz, 1))
print(' partie independante de D :', Q_indep.tolist(), ' trace =', Q_indep.trace())
print(' partie en cos(2kD) (coefficient) :', Q_dep.tolist(), ' trace =', Q_dep.trace())
print('  -> partie independante = (k^2 a^2/4) (eB eB - eE eE), eB = k^ x eps = z, eE = y')
# moyenne spectrale
n = 2
w = k**n*sp.exp(-k/ks)
num = sp.integrate(w*sp.cos(2*k*D), (k, 0, sp.oo), conds='none')
den = sp.integrate(w, (k, 0, sp.oo))
avg = sp.simplify((num/den).subs(D, xx/(2*ks)))
print(' <cos 2kD>_{n=2} =', sp.factor(avg), ' ; x = 2 k* D')
print('  verif Re (1 - i x)^-3 :', sp.simplify(avg - sp.re(sp.expand_complex((1 - sp.I*xx)**-3))))
print('  developpement x grand :', sp.series(avg, xx, sp.oo, 8))
for xv in (1, 3, 10, 30, 100):
    print('   x=%s : %s' % (xv, sp.N(avg.subs(xx, xv), 6)))
# variante : poids incluant k^2 a^2 (ponderation de Q par le spectre) -> n effectif 4
for nn in (4,):
    w2 = k**nn*sp.exp(-k/ks)
    av2 = sp.simplify((sp.integrate(w2*sp.cos(2*k*D), (k, 0, sp.oo), conds='none')/sp.integrate(w2, (k, 0, sp.oo))).subs(D, xx/(2*ks)))
    print(' (variante n=%d, si le facteur k^2 de Q est inclus dans le poids) <cos 2kD> =' % nn, sp.factor(av2), '~', sp.series(av2, xx, sp.oo, 8).removeO().as_ordered_terms()[-1])

print('\n== Q5 ==')
m1, m2, m3, M = sp.symbols('m1 m2 m3 M', real=True)
m = sp.Matrix([m1, m2, m3])
kh = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
eE = kh.cross(m)
eB = kh.cross(eE)
G = eB*eB.T - eE*eE.T
avgk = G.applyfunc(lambda t: sp.simplify(sp.integrate(sp.integrate(sp.expand(t)*sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi))/(4*sp.pi)))
print(' < eB eB - eE eE >_k =', avgk.tolist())
target = sp.Rational(4, 15)*(3*m*m.T - (m.T*m)[0]*sp.eye(3))
print('  - (4/15)(3 m m - |m|^2 delta) =', sp.simplify(avgk - target).tolist(), ' ; trace =', sp.simplify(avgk.trace()))
print('  verif |eB|^2 = |eE|^2 :', sp.simplify((eB.T*eB)[0] - (eE.T*eE)[0]))
# moyenne isotrope sur m = M (sin a cos b, sin a sin b, cos a)
al, be = sp.symbols('alpha_m beta_m', real=True)
msub = {m1: M*sp.sin(al)*sp.cos(be), m2: M*sp.sin(al)*sp.sin(be), m3: M*sp.cos(al)}
avgm = avgk.applyfunc(lambda t: sp.simplify(sp.integrate(sp.integrate(sp.expand(t.subs(msub))*sp.sin(al), (be, 0, 2*sp.pi)), (al, 0, sp.pi))/(4*sp.pi)))
print(' < . >_{k, m isotrope} =', avgm.tolist())
print(' separement <eB eB>_k =', eB.__class__ and sp.Matrix(3, 3, lambda i, j: sp.simplify(sp.integrate(sp.integrate(sp.expand((eB*eB.T)[i, j])*sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi))/(4*sp.pi))).tolist())
