"""XA-2 / A : reproduction independante de x-1, x-3 (recurrence explicite, toutes puissances), x-4,
et contre-exemple (b) (correcteurs s^mu, ln^2 s). Auditeur aveugle."""
import sympy as sp
s = sp.symbols('s', positive=True); x, y, z = sp.symbols('x y z', real=True)
box = lambda f: -sp.diff(f, s, 2) + sp.diff(f, x, 2) + sp.diff(f, y, 2) + sp.diff(f, z, 2)
sig = x**2 + y**2 + z**2 - s**2

print("== x-1 : box^2 hors cone ==")
for nom, f in (("ln sigma", sp.log(sig)), ("1/sigma", 1/sig), ("s/sigma", s/sig)):
    b1 = sp.simplify(box(f)); b2 = sp.simplify(box(b1))
    print(f"  box({nom}) = {b1} ; box^2 = {b2}")
p = sp.symbols('p')
print("  formule box sigma^p / sigma^(p-1) :", sp.simplify(box(sig**p)/sig**(p-1)))

print("== verif. comportement de .coeff(s,0) en presence de log(s) (point technique du script audite) ==")
ex = 3 + 5*sp.log(s) + 7*s
print("  (3+5 ln s+7 s).coeff(s,0) =", ex.coeff(s, 0))

print("== x-3 : recurrence exacte pour tout n (implementation differente : action terme a terme) ==")
# box^2 = d_s^4 - 2 Delta d_s^2 + Delta^2 ; on calcule l'action sur s^n ln^j s symboliquement en n
n = sp.symbols('n', integer=True)
def ds_k(expr, kk):
    return sp.diff(expr, s, kk)
# coefficients : d_s^4 (s^n ln s) = s^(n-4) [P(n) ln s + P'(n)]
P = sp.expand(n*(n-1)*(n-2)*(n-3))
t4 = sp.simplify(sp.expand(ds_k(s**n*sp.log(s), 4)/s**(n-4)))
t2 = sp.simplify(sp.expand(ds_k(s**n*sp.log(s), 2)/s**(n-2)))
print("  d_s^4(s^n ln s)/s^(n-4) =", sp.collect(sp.expand(t4), sp.log(s)))
print("  P(n) =", sp.factor(P), "; P'(n) =", sp.factor(sp.diff(P, n)), "; P'(0..3) =", [sp.diff(P, n).subs(n, i) for i in range(4)])
print("  d_s^2(s^n ln s)/s^(n-2) =", sp.collect(sp.expand(t2), sp.log(s)))
print("  Ordre s^(m-4) ln s : P(m) c_m - 2 (m-2)(m-3) Delta c_(m-2) + Delta^2 c_(m-4) = 0 (les a_n ne produisent jamais ln s)")
print("  Ordre s^(m-4)     : P'(m) c_m - 2 (2m-5) Delta c_(m-2) + [termes a_n, presents seulement pour m>=4] = 0")
# verification directe de cette structure par un ansatz numerote jusqu'a N = 12
N = 12
a_ = [sp.Function(f'a{i}')(x, y, z) for i in range(N)]
c_ = [sp.Function(f'c{i}')(x, y, z) for i in range(N)]
L = sp.Symbol('L')  # ln s remplace par un symbole APRES derivation
phi = sum(a_[i]*s**i + c_[i]*s**i*sp.log(s) for i in range(N))
eq = sp.expand((box(box(phi))*s**4).subs(sp.log(s), L))
poly = sp.Poly(eq, s, L)
dic = poly.as_dict()
sol = {}
ok = True
for m in range(N):                      # ordres s^(m-4), m <= N-1 entierement resolus (ne font intervenir que c_m, c_(m-2), c_(m-4))
    cl = dic.get((m, 1), 0); c0 = dic.get((m, 0), 0)
    cl = sp.simplify(sp.sympify(cl).subs(sol).doit()); c0 = sp.simplify(sp.sympify(c0).subs(sol).doit())
    if m < 4:
        assert cl == 0
        r = sp.solve(c0, c_[m]); sol[c_[m]] = r[0]
        print(f"  m={m} (s^{m-4})      : eq = {sp.factor(c0)} -> c{m} = {r[0]}")
    else:
        r = sp.solve(cl, c_[m]); sol[c_[m]] = r[0]
        print(f"  m={m} (s^{m-4} ln s) : eq = {sp.factor(cl)} -> c{m} = {r[0]}")
    ok = ok and sol[c_[m]] == 0
print("  c_0..c_%d tous nuls :" % (N-1), ok)
# exhaustivite : aucune puissance de L >= 2, aucune puissance non entiere
print("  degres en L presents :", sorted({kk[1] for kk in dic}))

print("== contre-exemple (b) : alpha(x) ln s + correcteurs s^mu ln^j s ==")
mu = sp.symbols('mu')
for j in (1, 2, 3):
    lead = sp.expand(sp.diff(s**mu*sp.log(s)**j, s, 4)/s**(mu-4))
    lead = sp.collect(sp.expand(lead.subs(sp.log(s), L)), L)
    print(f"  d_s^4(s^mu ln^{j} s)/s^(mu-4) =", lead)
print("  => terme dominant (Re mu minimal, puissance de log J maximale) : coefficient de s^(mu-4) ln^J = P(mu)a ; puis ln^(J-1) : J P'(mu) a.")
print("     Les termes Delta d_s^2 et Delta^2 deplacent l'exposant de +2, +4 : ils ne peuvent pas compenser l'ordre dominant.")
print("     P(mu)=0 impose mu in {0,1,2,3} ; racines simples => J P'(mu) != 0 => J = 0. Recurrence sur les reseaux mu0 + 2N.")
# test explicite : alpha ln s + beta ln^2 s + somme s^mu
al, be, ga = [sp.Function(nm)(x) for nm in ('alpha', 'beta', 'gamma')]
phi_b = al*sp.log(s) + be*sp.log(s)**2 + ga*s**2*sp.log(s)**2
eb = sp.expand((box(box(phi_b))*s**4).subs(sp.log(s), L))
print("  alpha ln s + beta ln^2 s + gamma s^2 ln^2 s : coefficients s^0 L^j :",
      {kk: sp.factor(v) for kk, v in sp.Poly(eb, s, L).as_dict().items() if kk[0] == 0})

print("== x-4 ==")
f = sp.Function('f')
print("  box^2 f(s) - f'''' =", sp.simplify(box(box(f(s))) - sp.diff(f(s), s, 4)), ";", sp.dsolve(sp.diff(f(s), s, 4), f(s)))
print("EXIT 0")
