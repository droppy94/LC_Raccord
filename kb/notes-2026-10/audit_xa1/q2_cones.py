"""XA-1 Q2 : ln sigma, 1/sigma, s/sigma ; regularisations sigma+i eps ;
lissite D'-valuee de ln|sigma| en s=0 ; cone decale ; solution fondamentale de box^2."""
import sympy as sp

s, x, y, z = sp.symbols('s x y z', real=True)
eps, s0, R = sp.symbols('epsilon s_0 R', positive=True)
r = sp.sqrt(x**2 + y**2 + z**2)

def box(f):
    return -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)

sig = x**2 + y**2 + z**2 - s**2
print("box sigma =", sp.simplify(box(sig)))
print("eta(dsigma,dsigma) - 4 sigma =",
      sp.simplify(-sp.diff(sig, s)**2 + sp.diff(sig, x)**2 + sp.diff(sig, y)**2 + sp.diff(sig, z)**2 - 4*sig))
for name, f in [("ln sigma", sp.log(sig)), ("1/sigma", 1/sig), ("s/sigma", s/sig)]:
    b1 = sp.simplify(box(f))
    b2 = sp.simplify(box(b1))
    print(f"{name}: box = {sp.factor(b1)} ; box^2 = {b2}")

print("\n--- Regularisation sigma -> sigma + i eps (identites exactes en eps) ---")
S = sig + sp.I*eps
for name, f in [("ln(sigma+ie)", sp.log(S)), ("1/(sigma+ie)", 1/S), ("s/(sigma+ie)", s/S)]:
    b1 = sp.simplify(box(f))
    b2 = sp.simplify(box(b1))
    print(f"{name}: box = {sp.factor(b1)} ; box^2 = {sp.factor(b2)}")

print("\n--- Cone de sommet (0,0): restriction a la droite r=0 ---")
print("ln|sigma| sur r=0 :", sp.simplify(sp.log(sp.Abs(sig.subs({x: 0, y: 0, z: 0})))), "(= 2 ln s pour s>0)")

print("\n--- Lissite D'-valuee : F(s) = int_0^R r^2 ln|r^2-s^2| dr, 0<s<R ---")
rr = sp.symbols('r', positive=True)
sp_ = sp.symbols('s', positive=True)
I1 = sp.integrate(rr**2*sp.log(sp_**2 - rr**2), (rr, 0, sp_))
I2 = sp.integrate(rr**2*sp.log(rr**2 - sp_**2), (rr, sp_, R))
F = sp.simplify(I1 + I2)
print("F(s) =", F)
ser = sp.series(F, sp_, 0, 8).removeO()
print("serie de F en s=0 (ordre 8) :", sp.simplify(ser))
print("contient log(s) ? ", sp.simplify(sp.expand_log(ser, force=True)).has(sp.log(sp_)))
# poids polynomial type fonction test radiale (R^2-r^2)^2 r^2
w = rr**2*(R**2 - rr**2)**2
J = sp.simplify(sp.integrate(w*sp.log(sp_**2 - rr**2), (rr, 0, sp_)) + sp.integrate(w*sp.log(rr**2 - sp_**2), (rr, sp_, R)))
serJ = sp.series(J, sp_, 0, 10).removeO()
print("poids (R^2-r^2)^2 : serie contient log(s) ?", sp.expand_log(serJ, force=True).has(sp.log(sp_)))
# partie imaginaire de ln(sigma+i0) : i*pi * indicatrice(r<s) -> i pi s^3/3 * 4pi apres angles
print("partie imaginaire (r<s) : int_0^s r^2 dr =", sp.integrate(rr**2, (rr, 0, sp_)))

print("\n--- Cone decale : sigma' = r^2 - (s+s0)^2, sommet s=-s0 ---")
rad = sp.symbols('rho', positive=True)
sigp = rad**2 - (sp_ + s0)**2
print("sigma' a s=0 :", sp.factor(sigp.subs(sp_, 0)), " -> zero sur la sphere rho = s0")
print("ln|sigma'| sur rho=s0 :", sp.factor(sigp.subs(rad, s0)), " = -s(s+2 s0)")
print("donc ln|sigma'| = ln s + ln(s+2 s0) sur la sphere (comportement ponctuel en ln s)")
print("hors sphere, rho != s0 : sigma'(0) =", sp.factor(sigp.subs(sp_, 0)), "!= 0 -> analytique en s pres de 0")
print("normale : d sigma' en (s=0, rho=s0) = (d_s, d_rho) =",
      (sp.diff(sigp, sp_).subs({sp_: 0, rad: s0}), sp.diff(sigp, rad).subs({sp_: 0, rad: s0})),
      " (covecteur nul, transverse a {s=0} car composante d_rho non nulle)")
# lissite D'-valuee du cone decale : G(s) = int r^2 ln|r^2-(s+s0)^2| dr sur [0,R], R>s0+s
t = sp.symbols('t', positive=True)
G = sp.simplify(sp.integrate(rr**2*sp.log(t**2 - rr**2), (rr, 0, t)) + sp.integrate(rr**2*sp.log(rr**2 - t**2), (rr, t, R)))
print("G(t), t = s+s0 :", G, " -> analytique en t pour 0<t<R, donc en s pres de 0")

print("\n--- Solution fondamentale retardee de box^2 (convention P = d_s^2 - Delta, box^2 = P^2) ---")
H = sp.Heaviside
r_ = sp.symbols('r', positive=True)
f = H(s - r_)/(8*sp.pi)
Pf = sp.diff(f, s, 2) - sp.diff(f, r_, 2) - 2/r_*sp.diff(f, r_)
print("P[theta(s-r)/(8 pi)] =", sp.simplify(Pf), " (attendu delta(s-r)/(4 pi r), noyau retarde de P)")
