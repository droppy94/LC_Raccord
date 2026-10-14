"""XA-2 / C : le Weyl lineaire du mode h s'annule-t-il en s = 0 ? (explique l'ordre s^-1 sur la sphere, contre-ex. (a))"""
import sympy as sp
s = sp.symbols('s', positive=True); x = sp.symbols('x', real=True); y, z = sp.symbols('y z', real=True)
k, A, B = sp.symbols('k A B', positive=True)
X = [s, x, y, z]; n = 4; eta = sp.diag(-1, 1, 1, 1)
u = A*(sp.cos(k*s) + k*s*sp.sin(k*s)) + B*(sp.sin(k*s) - k*s*sp.cos(k*s))
print("equation du mode : u'' - (2/s) u' + k^2 u =", sp.simplify(sp.diff(u, s, 2) - 2/s*sp.diff(u, s) + k**2*u))
H = sp.zeros(4, 4); H[2, 2] = u*sp.cos(k*x); H[3, 3] = -u*sp.cos(k*x)
d = lambda f, i, j: sp.diff(f, X[i], X[j])
R4 = {(a, b, c, q): (d(H[a, q], b, c) + d(H[b, c], a, q) - d(H[b, q], a, c) - d(H[a, c], b, q))/2
      for a in range(n) for b in range(n) for c in range(n) for q in range(n)}
Ric = sp.Matrix(n, n, lambda b, q: sum(eta[a, a]*R4[(a, b, a, q)] for a in range(n)))
Rs = sum(eta[a, a]*Ric[a, a] for a in range(n))
C = {kk: v - (eta[kk[0], kk[2]]*Ric[kk[1], kk[3]] - eta[kk[0], kk[3]]*Ric[kk[1], kk[2]] - eta[kk[1], kk[2]]*Ric[kk[0], kk[3]] + eta[kk[1], kk[3]]*Ric[kk[0], kk[2]])/2
     + Rs/6*(eta[kk[0], kk[2]]*eta[kk[1], kk[3]] - eta[kk[0], kk[3]]*eta[kk[1], kk[2]]) for kk, v in R4.items()}
lead = {}
for kk, v in C.items():
    ser = sp.series(sp.simplify(v), s, 0, 3).removeO()
    if ser != 0:
        lead[kk] = sp.factor(ser)
print("C(s=0) = 0 pour toutes composantes :", all(sp.simplify(v.subs(s, 0)) == 0 for v in C.values()))
for kk in [(0, 2, 0, 2), (0, 2, 1, 2), (1, 2, 1, 2), (2, 3, 2, 3)]:
    print("  C_%s ~" % ''.join('sxyz'[i] for i in kk), lead.get(kk, 0))
