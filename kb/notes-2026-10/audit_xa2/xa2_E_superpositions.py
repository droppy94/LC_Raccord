"""XA-2 / E : contre-exemple (c), meme machinerie que B/D (meme machinerie, parametres numeriques k=1, A=1/3, B=1/2, kappa=b=1).
(1) ordre dominant de R en s au voisinage de s = 0 hors cone (x-2 et (a)) ; (2) (a) structure pres de la sphere ;
(3) contre-exemple (c) : superpositions ligne / plan de sommets."""
import sympy as sp, time
src = open('xa2_B_x2.py').read()
exec(src.split("# --- Lemme")[0])
exec("def T_of_phi" + src.split("def T_of_phi")[1].split("names = 'sxyz'")[0])
t0 = time.time()
names = 'sxyz'
num = {k: 1, A: sp.Rational(1, 3), B: sp.Rational(1, 2), kap: 1, b: 1}
for i in range(4):
    for j in range(4):
        for m in range(4):
            Gh[i][j][m] = sp.sympify(Gh[i][j][m])
CWn = {kk: sp.simplify(v.subs(num)) for kk, v in CW.items()}
CW.clear(); CW.update(CWn)
e = sp.symbols('e', positive=True)

def lead_order(expr, var, N=8):
    ser = sp.series(expr, var, 0, N).removeO()
    if ser == 0: return None, 0
    terms = sp.Add.make_args(sp.expand(ser))
    o = min(t.as_coeff_exponent(var)[1] for t in terms)
    c = sum(t for t in terms if t.as_coeff_exponent(var)[1] == o)
    return o, c

def orders_at(phi, pt, var=s, N=4, label=""):
    RR = R_of_T(T_of_phi(phi))
    res = {}
    for key, v in RR.items():
        vp = sp.simplify(v.subs(num).subs(pt))
        if vp == 0: continue
        o, c = lead_order(vp, var, N)
        if o is not None: res[''.join(names[i] for i in key)] = o
    print(f"   {label} : ordres dominants {res} ; min = {min(res.values()) if res else None}")
    return res

box = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
print("== (3) contre-exemple (c) ==")
rp2 = y**2 + z**2
xi = sp.symbols('xi', real=True); q = sp.symbols('q', positive=True)
print("   int dxi /((x-xi)^2+q) =", sp.integrate(1/(xi**2+q), (xi, -sp.oo, sp.oo)), " => ligne de ln sigma : 2 pi sqrt(rho^2-s^2) + const ; ligne de 1/sigma : pi/sqrt(rho^2-s^2)")
print("   plan de 1/sigma (PV, coupure Lambda) : pi ln(Lambda^2+q) - pi ln|q|, q = z^2 - s^2")
print("   box^2 sqrt(rho^2-s^2) =", sp.simplify(box(box(sp.sqrt(rp2 - s**2)))),
      "; box (1/sqrt(rho^2-s^2)) =", sp.simplify(box(1/sp.sqrt(rp2 - s**2))),
      "; box ln(z^2-s^2) =", sp.simplify(box(sp.log(z**2 - s**2))))
Fneg = sp.pi*sp.exp(-e**2)*sp.erfc(sp.I*e)/(sp.I*e)
print("   ligne 1/sigma poids exp(-xi^2), controle q=7/10 :", sp.N(sp.Integral(sp.exp(-xi**2)/(xi**2+sp.Rational(7, 10)), (xi, -sp.oo, sp.oo))),
      sp.N(sp.pi*sp.exp(q)*sp.erfc(sp.sqrt(q))/sp.sqrt(q)).subs(q, sp.Rational(7, 10)))
print("   sur l'axe rho = 0 (q = -s^2, ici e = s) : Re =", sp.series(sp.re(sp.expand_complex(Fneg)), e, 0, 2), " ; Im =", sp.series(sp.im(sp.expand_complex(Fneg)), e, 0, 1))
# plan, poids gaussien : int d^2xi exp(-xi^2)/(xi^2+q) = pi e^q E1(q) ~ -pi ln q
print("   plan poids exp(-xi^2) : pi e^q E1(q), developpement q->0+ :", sp.series(sp.pi*sp.exp(q)*sp.expint(1, q), q, 0, 1))
print("   R pour phi = ln(s^2 - z^2) (plan des sommets z=0) :")
orders_at(sp.log(s**2 - z**2), {x: sp.Rational(1, 3), y: sp.Rational(1, 5), z: 0}, label="(c) plan, sur z=0, ordre en s")
orders_at(sp.log(z**2 - s**2), {x: sp.Rational(1, 3), y: sp.Rational(1, 5), z: sp.Rational(1, 2)}, label="(c) plan, z=1/2, ordre en s")
print("  t =", round(time.time()-t0, 1))
orders_at(sp.sqrt(rp2 - s**2), {x: sp.Rational(1, 3), y: sp.Rational(1, 5), z: sp.Rational(1, 2)}, label="(c) ligne ln-sigma, rho>0, ordre en s")
orders_at(1/sp.sqrt(s**2 - y**2 - z**2), {x: sp.Rational(1, 3), y: 0, z: 0}, label="(c) ligne 1/sigma (partie Im, 1/s), sur l'axe, ordre en s")
print("  t =", round(time.time()-t0, 1))
print("EXIT 0")
