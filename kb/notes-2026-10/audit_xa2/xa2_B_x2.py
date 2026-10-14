"""XA-2 / B : reproduction independante de x-2 et contre-exemples (a), (c).
Implementation differente : Weyl obtenu par linearisation en epsilon du Riemann complet de eta + eps h
(Christoffels explicites), Christoffels de g_hat calcules directement depuis g_hat, R de (2.17) recalcule.
Lemme structurel : pour T lisse quelconque, R est regulier en s = 0 (pas de 1/s)."""
import sympy as sp, time
t0 = time.time()
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
k, A, B, kap, b, eps = sp.symbols('k A B kappa b epsilon')
X = [s, x, y, z]; n = 4
eta = sp.diag(-1, 1, 1, 1)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
H = sp.zeros(4, 4); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)

# --- Weyl lineaire par Riemann complet de g = eta + eps H, puis d/d eps en 0
g = eta + eps*H; gi = g.inv()
Gm = [[[sum(gi[a, m]*(sp.diff(g[m, bb], X[c]) + sp.diff(g[m, c], X[bb]) - sp.diff(g[bb, c], X[m])) for m in range(n))/2
        for c in range(n)] for bb in range(n)] for a in range(n)]
def Rup(a, bb, c, d):   # R^a_{bcd} = d_c G^a_{db} - d_d G^a_{cb} + G^a_{ce} G^e_{db} - G^a_{de} G^e_{cb}
    return (sp.diff(Gm[a][d][bb], X[c]) - sp.diff(Gm[a][c][bb], X[d])
            + sum(Gm[a][c][e]*Gm[e][d][bb] - Gm[a][d][e]*Gm[e][c][bb] for e in range(n)))
Rl = {}
for a in range(n):
    for bb in range(n):
        for c in range(n):
            for d in range(n):
                full = sum(g[a, m]*Rup(m, bb, c, d) for m in range(n))
                Rl[(a, bb, c, d)] = sp.simplify(sp.diff(full, eps).subs(eps, 0))
Ric = sp.Matrix(4, 4, lambda bb, d: sum(eta[a, a]*Rl[(a, bb, a, d)] for a in range(n)))
Rsc = sum(eta[a, a]*Ric[a, a] for a in range(n))
def Cw(a, bb, c, d):
    return (Rl[(a, bb, c, d)] - (eta[a, c]*Ric[bb, d] - eta[a, d]*Ric[bb, c] - eta[bb, c]*Ric[a, d] + eta[bb, d]*Ric[a, c])/2
            + Rsc/6*(eta[a, c]*eta[bb, d] - eta[a, d]*eta[bb, c]))
CW = {(a, bb, c, d): sp.simplify(Cw(a, bb, c, d)) for a in range(n) for bb in range(n) for c in range(n) for d in range(n)}
# controle : trace de Weyl nulle
print("controle trace Weyl nulle :", all(sp.simplify(sum(eta[a, a]*CW[(a, bb, a, d)] for a in range(n))) == 0 for bb in range(n) for d in range(n)))
print("controle convention : signe R_{xyxy} de la courbure de h vs script audite (formule lineaire) ->",
      sp.simplify(Rl[(1, 2, 1, 2)] - (sp.diff(H[1, 2], X[2], X[1]) + sp.diff(H[2, 1], X[1], X[2]) - sp.diff(H[2, 2], X[1], X[1]) - sp.diff(H[1, 1], X[2], X[2]))/2))

# --- Christoffels de g_hat = s^-2 eta, calcules directement
gh = s**-2*eta; ghi = gh.inv()
Gh = [[[sp.simplify(sum(ghi[a, m]*(sp.diff(gh[m, bb], X[c]) + sp.diff(gh[m, c], X[bb]) - sp.diff(gh[bb, c], X[m])) for m in range(n))/2)
        for c in range(n)] for bb in range(n)] for a in range(n)]

def R_of_T(T):
    That = s**2*T
    tr = sum(ghi[a, bb]*That[a, bb] for a in range(n) for bb in range(n))
    Lh = kap/2*(That - gh*tr/3)
    def nab(c, a, bb):  # nabla_c L_ab
        return sp.diff(Lh[a, bb], X[c]) - sum(Gh[m][c][a]*Lh[m, bb] + Gh[m][c][bb]*Lh[a, m] for m in range(n))
    out = {}
    for r in range(n):
        for nu in range(n):
            for la in range(nu+1, n):
                out[(r, nu, la)] = (nab(nu, la, r) - nab(la, nu, r))/s
    return out

# --- Lemme : T lisse generique => s*R = O(s) (pas de pole)
Tg = sp.Matrix(4, 4, lambda i, j: sp.Function(f'T{min(i,j)}{max(i,j)}')(s, x, y, z))
Rg = R_of_T(Tg)
lem = all(sp.simplify(sp.expand(v*s).subs(s, 0)) == 0 for v in Rg.values())
print("LEMME : pour T_ab lisse arbitraire, (s*R).subs(s=0) = 0 pour toutes composantes :", lem)
print("   exemple R_sxy =", sp.factor(sp.expand(sp.simplify(Rg[(0, 1, 2)]))))

def T_of_phi(phi):
    T = sp.zeros(4, 4)
    for a in range(n):
        for bb in range(a, n):
            T[a, bb] = -8*b*sum(eta[c, c]*eta[d, d]*sp.diff(phi*CW[(a, c, bb, d)], X[c], X[d]) for c in range(n) for d in range(n))
            T[bb, a] = T[a, bb]
    return T

names = 'sxyz'
num = {k: 1, A: sp.Rational(1, 3), B: sp.Rational(1, 2), kap: 1, b: 1}

def pole_check(phi, pt, label, order=2):
    """coefficients des puissances negatives de s au point pt (phi lisse en s=0 attendu)."""
    T = T_of_phi(phi); RR = R_of_T(T)
    worst = None
    for key, v in RR.items():
        vp = sp.simplify(v.subs(pt))
        ser = sp.series(vp, s, 0, 1).removeO()
        neg = [t for t in sp.Add.make_args(sp.expand(ser)) if t.has(sp.log(s)) or t.as_coeff_exponent(s)[1] < 0]
        if neg:
            worst = (key, neg)
            print(f"   {label} R_{''.join(names[i] for i in key)} : termes singuliers {neg}")
    print(f"   {label} : aucune puissance negative ni ln s" if worst is None else f"   {label} : SINGULIER")
    return RR

sig = x**2 + y**2 + z**2 - s**2
print("== x-2 (i) : phi = ln sigma, k,A,B,kappa,b symboliques, point (1, 1/2, 2/3) (z != 0) ==")
pole_check(sp.log(sig), {x: 1, y: sp.Rational(1, 2), z: sp.Rational(2, 3)}, "pt(1,1/2,2/3)")
print("== x-2 (i bis) : point du script (3/2,1/2,0) ==")
pole_check(sp.log(sig), {x: sp.Rational(3, 2), y: sp.Rational(1, 2), z: 0}, "pt(3/2,1/2,0)")
print("  t =", round(time.time()-t0, 1), "s")

e = sp.symbols('e', positive=True)
def cone_order(phi, path, label, pars):
    T = T_of_phi(phi.subs(pars)) ; RR = R_of_T(T.subs(pars))
    res = {}
    for key, v in RR.items():
        ve = sp.simplify(v.subs(pars).subs(path))
        if ve == 0:
            continue
        ser = sp.series(ve, e, 0, 0).removeO()
        if ser == 0:
            res[key] = 0; continue
        lead = sp.Poly(sp.expand(ser*e**8), e)
        res[key] = min(m[0] for m in lead.monoms()) - 8
    mn = min(res.values()) if res else None
    print(f"   {label} : {len(res)} composantes non nulles ; ordres {dict((''.join(names[i] for i in kk), o) for kk, o in res.items())} ; plus singulier e^{mn}")
    return res

print("== x-2 (ii) : ordre pres du cone ==")
nh = (sp.Rational(2, 3), sp.Rational(1, 3), sp.Rational(2, 3))
sh = sp.Rational(1, 2)
cone_order(sp.log(sig), {s: sh, x: (sh+e)*nh[0], y: (sh+e)*nh[1], z: (sh+e)*nh[2]}, "direction generique n=(2,1,2)/3, s=1/2", num)
cone_order(sp.log(sig), {s: sh, x: sh+e, y: 0, z: 0}, "droite du script y=z=0, s=1/2", num)
print("  t =", round(time.time()-t0, 1), "s")

print("== contre-exemple (a) : sommet hors du bord, sigma' = r^2 - (s+s0)^2, s0 = 1 ==")
s0 = 1
sigp = x**2 + y**2 + z**2 - (s+s0)**2
# point de s=0 hors sphere : regulier ?
pole_check(sp.log(-sigp), {x: sp.Rational(1, 3), y: sp.Rational(1, 4), z: 0}, "(a) r<s0 hors sphere, ln(-sigma')")
pole_check(sp.log(sigp), {x: 2, y: sp.Rational(1, 2), z: 0}, "(a) r>s0 hors sphere, ln(sigma')")
# point SUR la sphere r = s0 : on approche s -> 0 a x fixe (alors sigma' = -2 s s0 - s^2 < 0)
pt = {x: nh[0]*s0, y: nh[1]*s0, z: nh[2]*s0}
T = T_of_phi(sp.log(-sigp).subs(num)); RR = R_of_T(T.subs(num))
ords = {}
for key, v in RR.items():
    vp = sp.simplify(v.subs(num).subs(pt))
    if vp == 0: continue
    ser = sp.series(vp, s, 0, 0).removeO()
    if ser == 0: ords[key] = 0; continue
    ords[key] = min(m[0] for m in sp.Poly(sp.expand(ser*s**8), s).monoms()) - 8
print("   (a) sur la sphere r = s0, s -> 0 : ordres en s", {''.join(names[i] for i in kk): o for kk, o in ords.items()})
print("  t =", round(time.time()-t0, 1), "s")
print("EXIT 0 (suite dans xa2_D)")
