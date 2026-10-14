# Reproduction independante : (a) Bach linearise / box^2 h ; (b) (d^2+k^2)^2 u = 0 pour les modes de Sitter ; (c) serie en eps.
import sympy as sp

t, x, y, z = sp.symbols('tau x y z', real=True)
k = sp.symbols('k', positive=True)
eps = sp.symbols('epsilon', positive=True)
X = [t, x, y, z]
eta = sp.diag(-1, 1, 1, 1)

# (a) Route independante : on ecrit le Weyl linearise directement via R_abcd lin., Ricci et scalaire,
# avec une perturbation generale u(tau) cos(k x) sur yy / zz, et on calcule B_ab = d^c d^d C_acbd.
u = sp.Function('u')(t)
h = sp.zeros(4, 4)
h[2, 2] = u*sp.cos(k*x)
h[3, 3] = -u*sp.cos(k*x)

def D(f, a):
    return sp.diff(f, X[a])

def Rlin(a, b, c, d):
    # Riemann linearise, convention standard R_abcd = 1/2 (h_ad,bc + h_bc,ad - h_ac,bd - h_bd,ac)
    return sp.Rational(1, 2)*(D(D(h[a, d], b), c) + D(D(h[b, c], a), d) - D(D(h[a, c], b), d) - D(D(h[b, d], a), c))

Ric = sp.Matrix(4, 4, lambda a, b: sum(eta[c, c]*Rlin(c, a, c, b) for c in range(4)))
Rsc = sp.simplify(sum(eta[a, a]*Ric[a, a] for a in range(4)))
print("Ricci lin. trace =", Rsc)
# verification TT
print("trace h =", sp.simplify(sum(eta[a, a]*h[a, a] for a in range(4))),
      " ; div h =", [sp.simplify(sum(eta[a, a]*D(h[a, b], a) for a in range(4))) for b in range(4)])
# Ricci lin. pour h TT doit etre -1/2 box h
box = lambda f: sum(eta[a, a]*D(D(f, a), a) for a in range(4))
print("Ric_yy + 1/2 box h_yy =", sp.simplify(Ric[2, 2] + sp.Rational(1, 2)*box(h[2, 2])))

def Weyl(a, b, c, d):
    return (Rlin(a, b, c, d)
            - sp.Rational(1, 2)*(eta[a, c]*Ric[b, d] - eta[a, d]*Ric[b, c] - eta[b, c]*Ric[a, d] + eta[b, d]*Ric[a, c])
            + Rsc/6*(eta[a, c]*eta[b, d] - eta[a, d]*eta[b, c]))

def Bach(a, b):
    return sp.simplify(sum(eta[c, c]*eta[d, d]*D(D(Weyl(a, c, b, d), c), d) for c in range(4) for d in range(4)))

Byy = Bach(2, 2)
box2 = sp.simplify(box(box(h[2, 2])))
print("B_yy =", sp.factor(Byy))
print("box^2 h_yy =", sp.factor(box2))
print("rapport B_yy / box^2 h_yy =", sp.simplify(Byy/box2))
# tracelessness et symetrie du Weyl (controle de la formule utilisee)
print("trace Weyl C^a_bad (doit etre 0) :", sp.simplify(sum(eta[a, a]*Weyl(a, 1, a, 2) for a in range(4))),
      sp.simplify(sum(eta[a, a]*Weyl(a, 2, a, 2) for a in range(4))))
# forme explicite en u : box^2 h_yy = (d^2+k^2)^2 u * cos(kx)
print("box^2 h_yy / cos(kx) - (d^2+k^2)^2 u =",
      sp.simplify(box2/sp.cos(k*x) - (sp.diff(u, t, 4) + 2*k**2*sp.diff(u, t, 2) + k**4*u)))
# autres composantes
print("B_tt, B_tx, B_xx, B_yz, B_yy+B_zz :", Bach(0, 0), Bach(0, 1), Bach(1, 1), Bach(2, 3), sp.simplify(Bach(2, 2)+Bach(3, 3)))

# (b) solutions de u'' - (2/tau) u' + k^2 u = 0 : dsolve independante puis (d^2+k^2)^2
U = sp.Function('U')
ode = sp.Eq(sp.diff(U(t), t, 2) - 2/t*sp.diff(U(t), t) + k**2*U(t), 0)
sol = sp.dsolve(ode, U(t))
print("dsolve :", sol)
usol = sol.rhs
P2 = lambda f: sp.diff(f, t, 2) + k**2*f
print("(d^2+k^2) u_gen =", sp.simplify(P2(usol)))
print("(d^2+k^2)^2 u_gen =", sp.simplify(P2(P2(usol))))
# et les deux modes du script
uA = sp.cos(k*t) + k*t*sp.sin(k*t)
uB = sp.sin(k*t) - k*t*sp.cos(k*t)
for nm, uu in (("A", uA), ("B", uB)):
    print(f"mode {nm} : ODE residu =", sp.simplify(sp.diff(uu, t, 2) - 2/t*sp.diff(uu, t) + k**2*uu),
          " ; (d^2+k^2)u =", sp.simplify(P2(uu)), " ; (d^2+k^2)^2 u =", sp.simplify(P2(P2(uu))))

# (c) developpement en eps : methode operatorielle : (d^2+k^2)^2 e^{eps t} u = e^{eps t} [(d+eps)^2 + k^2]^2 u
#   = e^{eps t} [ (d^2+k^2)^2 u + 4 eps d (d^2+k^2) u + O(eps^2) ]
for nm, uu in (("A", uA), ("B", uB)):
    exact = sp.simplify(sp.exp(-eps*t)*P2(P2(sp.exp(eps*t)*uu)))
    op = sp.expand(P2(P2(uu)) + 4*eps*sp.diff(P2(uu), t))
    print(f"mode {nm} : [exact - (0 + 4 eps d(d^2+k^2)u)]/eps^2 =", sp.simplify((exact - op)/eps**2),
          " ; terme O(eps) =", sp.simplify(op))
    # developpement complet exact (polynome en eps)
    print(f"   e^(-eps t) B_eps exact (collect eps) =", sp.collect(sp.expand(exact), eps))
