"""XA-1 Q1(a) : ansatz formel u = sum_{n=0}^N (a_n + c_n ln s) s^n, box^2 u = 0.
box = -d_s^2 + d_x^2 + d_y^2 + d_z^2.
On calcule s^4 * box^2 u, on remplace ln s par un symbole L, et on lit les
coefficients de s^j L^e. Les equations sont exigees pour s^j, j <= N (ie ordre
s^{j-4} <= s^{N-4} dans box^2 u) : ce sont celles non polluees par la troncature.
"""
import sympy as sp

N = 8
s, x, y, z, L = sp.symbols('s x y z L', positive=True)
a = [sp.Function(f'a{n}')(x, y, z) for n in range(N + 1)]
c = [sp.Function(f'c{n}')(x, y, z) for n in range(N + 1)]

def box(f):
    return -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)

u = sum((a[n] + c[n] * sp.log(s)) * s**n for n in range(N + 1))
B2 = box(box(u))
E = sp.expand(sp.expand(B2 * s**4).subs(sp.log(s), L))
P = sp.Poly(E, s, L)
coeffs = {}
for (j, e), co in zip(P.monoms(), P.coeffs()):
    coeffs[(j, e)] = sp.simplify(co)

print(f"N = {N}; degre max en L dans s^4 box^2 u :", max(e for (_, e) in coeffs))
print("\n--- Equations sur les termes en ln s (coefficient de s^j L), j <= N ---")
sol = {}
for j in range(0, N + 1):
    eq = coeffs.get((j, 1), 0)
    eq_s = sp.simplify(eq.subs(sol)) if eq != 0 else 0
    print(f"s^{j-4} ln s :", eq)
    # inconnue nouvelle : c_j (coefficient j(j-1)(j-2)(j-3) c_j)
    if eq_s != 0:
        r = sp.solve(eq_s, c[j], dict=True)
        if r:
            sol[c[j]] = sp.simplify(r[0][c[j]])
print("\n--- Equations sur les termes sans ln (coefficient de s^j L^0), j <= 3 ---")
for j in range(0, 4):
    print(f"s^{j-4} :", coeffs.get((j, 0), 0))

# Resolution sequentielle complete : on impose tous les coefficients j<=N
unk = []
eqs = []
for j in range(0, N + 1):
    for e in (0, 1):
        co = coeffs.get((j, e), 0)
        if co != 0:
            eqs.append(co)
# on resout etape par etape en c_j puis a_j
sol = {}
for j in range(0, N + 1):
    for e in (1, 0):
        co = coeffs.get((j, e), 0)
        if co == 0:
            continue
        co = sp.simplify(sp.expand(co.subs(sol).doit()))
        if co == 0:
            continue
        target = c[j] if e == 1 else (c[j] if (j < 4) else a[j])
        if co.has(target):
            r = sp.solve(co, target, dict=True)
            sol[target] = sp.simplify(r[0][target])
        else:
            print("Equation residuelle (non resoluble pour la cible) :", j, e, co)
print("\n--- Solution sequentielle (j <= N) ---")
for k, v in sol.items():
    print(k, "=", v)
print("\nTous les c_n (n<=N) nuls :", all(sp.simplify(sol.get(cn, None) if cn in sol else 1) == 0 for cn in c))
print("c_n determines :", [str(cn) for cn in c if cn in sol])
print("c_n non contraints par les equations j<=N :", [str(cn) for cn in c if cn not in sol])
