# Controle independant de la tache 3-5 : solution exacte par variation des constantes,
# puis Weyl electrique exact et extraction de Gamma (tous ordres en s pour le log).
import sympy as sp
s = sp.Symbol('s', positive=True)
k, b, G = sp.symbols('k b G', positive=True)
A, B = sp.symbols('A B', real=True)
y1 = sp.cos(k*s) + k*s*sp.sin(k*s)
y2 = sp.sin(k*s) - k*s*sp.cos(k*s)
W = sp.simplify(y1*sp.diff(y2, s) - y2*sp.diff(y1, s))
F = 64*sp.pi*b*k**3*s*(A*sp.sin(k*s) - B*sp.cos(k*s))   # issu de t3 (u1''-2u1'/s+k^2u1=F)
# forme y'' + P y' + Q y = F : variation des constantes standard
t = sp.Symbol('t', positive=True)
I1 = sp.integrate(sp.simplify((y2*F/W).subs(s, t)), t)
I2 = sp.integrate(sp.simplify((y1*F/W).subs(s, t)), t)
u1 = sp.simplify(-y1*I1.subs(t, s) + y2*I2.subs(t, s))
print('u1 exact =', u1)
res = sp.simplify(sp.diff(u1, s, 2) - 2*sp.diff(u1, s)/s + k**2*u1 - F)
print('residu exact :', res)
u0 = A*y1 + B*y2
Csysy = lambda u: (k**2*u - sp.diff(u, s, 2))/4    # issu de t2
WE0 = sp.simplify(Csysy(u0)/s)
WE1 = sp.simplify(Csysy(u1)/s)
print('W_E0 exact =', WE0)
print('W_E1 exact =', WE1)
# extraction du log, donnees separees (A=1,B=0) et (A=0,B=1)
L = sp.Symbol('L')   # L = ln s
def logcoef(expr):
    e = sp.expand_log(sp.expand(expr), force=True)
    e = e.rewrite(sp.log)
    ser = sp.series(e, s, 0, 4).removeO()
    ser = sp.expand(ser.subs(sp.log(s), L))
    return sp.collect(ser, L)
for (Av, Bv) in [(1, 0), (0, 1)]:
    print('A=%d,B=%d : W_E0 serie =' % (Av, Bv), sp.series(WE0.subs({A: Av, B: Bv}), s, 0, 4))
    print('           W_E1 serie (L=ln s) =', logcoef(WE1.subs({A: Av, B: Bv})))
# controle exact a tous ordres : partie en ln s de W_E1 = -64 pi b ln s * W_E0|_{A=0}
Creg = sp.Symbol('Creg')                # Creg = Ci(2ks) - ln s, analytique en s (gamma + ln 2k + serie entiere)
WE1_split = WE1.subs(sp.Ci(2*k*s), Creg + L)
WE1_split = sp.expand(sp.expand_log(WE1_split, force=True).subs(sp.log(s), L))
coefL = sp.simplify(WE1_split.coeff(L, 1))
print('coefficient exact de ln s dans W_E1 =', coefL)
print('coefL / W_E0|_{A=0} =', sp.simplify(coefL / WE0.subs(A, 0)))
W0 = sp.limit(WE0.subs(A, 0), s, 0)
Gam = sp.simplify(-G*coefL.subs(s, 0)/W0)
print('W0 =', W0, ' ; Gamma =', Gam)
bsc = sp.Rational(1, 120)/(4*sp.pi)**2
print('Gamma (scalaire conforme) =', sp.simplify(Gam.subs(b, bsc)), '=', sp.N(Gam.subs(b, bsc)/G, 12), 'G')
