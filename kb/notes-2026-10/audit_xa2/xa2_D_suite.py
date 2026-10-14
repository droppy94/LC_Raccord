"""XA-2 / D : suite de B (meme machinerie, parametres numeriques k=1, A=1/3, B=1/2, kappa=b=1).
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

sig = x**2 + y**2 + z**2 - s**2
print("== (1) ordre dominant en s hors cone (x-2 : est-ce O(1) ou mieux ?) ==")
orders_at(sp.log(sig), {x: 1, y: sp.Rational(1, 2), z: sp.Rational(2, 3)}, label="ln sigma, pt (1,1/2,2/3)")
print("  t =", round(time.time()-t0, 1))
s0 = 1
sigp = x**2 + y**2 + z**2 - (s+s0)**2
nh = (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3))
print("== (2) contre-exemple (a), s0 = 1 ==")
orders_at(sp.log(sigp), {x: 2, y: sp.Rational(1, 2), z: 0}, label="(a) r>s0, ordre en s")
# chemin dans le plan (s, r) : r = s0 + lam*s, s -> 0, pour lam = 3 (hors cone : sigma' ~ 2 s0 (lam-1) s > 0) et lam = 0 (sur la sphere)
for lam in (3, 0, sp.Rational(1, 2)):
    phi = sp.log(sigp) if lam > 1 else sp.log(-sigp)
    pt = {x: (s0+lam*s)*nh[0], y: (s0+lam*s)*nh[1], z: (s0+lam*s)*nh[2]}
    orders_at(phi, pt, label=f"(a) r = s0 + {lam} s, s -> 0")
    print("  t =", round(time.time()-t0, 1))
# a s fixe = 1/4 pres du cone r = s0 + s + e
orders_at(sp.log(sigp), {s: sp.Rational(1, 4), x: (s0+sp.Rational(1, 4)+e)*nh[0], y: (s0+sp.Rational(1, 4)+e)*nh[1], z: (s0+sp.Rational(1, 4)+e)*nh[2]},
          var=e, N=0, label="(a) s=1/4, r = s0+s+e, ordre en e")
print("  t =", round(time.time()-t0, 1))
print("EXIT 0 (contre-exemple (c) dans xa2_E)")
