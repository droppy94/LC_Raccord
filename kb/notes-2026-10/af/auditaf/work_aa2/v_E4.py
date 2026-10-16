# Variante E4 : le pole peut-il etre retire par un autre choix d'inconnues ?
# (i) poids conforme different : C = Omega^p W_p. Equation pour W_p : d^mu W_p = Omega^{1-p} R[C] + (1-p) Omega^-1 n^mu W_p,mu... 
#     on calcule le coefficient total de Omega^-1 dans le repere n = (1,0,0,0), s = 0, lambda = 3, et on cherche p qui l'annule.
# (ii) redefinition W' = W + ln(Omega) X : existence d'un X de Weyl annulant le pole, et log induit.
import sys, itertools, sympy as sp
txt = open('af_check_copie.py').read()
exec(txt.split('# ---------------------------------------------------------------- AF-1')[0])
exec('\n'.join(txt.split('\n')[124:144]))
p = sp.Symbol('p')
sigma = -sp.log(Om_f)
cal = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0, s: 0, lam: 3}
def frame(z): return sp.expand(z.subs(cal))
Cp = {k: Om_f**p*v for k, v in Wt.items()}
That = sp.Matrix(4, 4, lambda a, bb: Om_f**2*c0*b*sum(up(c)*up(d)*sp.diff(sigma*Cp[(a, c, bb, d)], X[c], X[d]) for c in idx for d in idx))
Lh = kap/2*That
print("=== E4 (i) poids p ===")
tot = {}
for rho in idx:
    for nu in idx:
        for la in range(nu + 1, 4):
            r = jetify(subs_omega(R217(Lh, rho, nu, la)))
            # equation pour W_p : d^mu W_p,mu rho nu la = Omega^{-p} [ Omega R ] ... on ecrit R[C] = Omega^{-1}(...) ; d^mu(Omega^{1-p} W1) etc.
            # W1 = Omega^{-1} C = Omega^{p-1} W_p ; d.W1 = R  =>  d.W_p = Omega^{1-p} R - (p-1) Omega^{-1} n^mu W_p,mu rho nu la
            rr = sp.expand(sp.powsimp(sp.expand(frame(r)*W**(1 - p)), force=True))
            rr = sp.expand(sp.powsimp(rr, force=True))
            nW = sum(up(m)*n[m]*jetify(Wt[(m, rho, nu, la)]) for m in idx)
            rr = rr - (p - 1)*frame(nW)/W
            tot[(rho, nu, la)] = sp.expand(rr.coeff(LOG, 0).coeff(W, -1))
            assert all(sp.expand(rr).coeff(W, k) == 0 for k in (-2, -3))
for k_ in [(1, 0, 1), (1, 0, 2), (1, 2, 3), (2, 1, 3), (0, 1, 2)]:
    print("  pole total pour W_p, composante", k_, ":", sp.factor(tot[k_]))
eqs = []
for v in tot.values():
    if v != 0:
        eqs += sp.Poly(v, *sorted(v.free_symbols - {p, b, c0, kap}, key=str)).coeffs()
print("  p annulant le pole pour E, B generiques (b != 0) :", sp.solve(eqs, p, dict=True))
eqsB0 = []
for v in tot.values():
    v0 = v.subs({sp.Symbol(nm, real=True): 0 for nm in ['B11', 'B22', 'B12', 'B13', 'B23']})
    if v0 != 0: eqsB0 += sp.Poly(v0, *sorted(v0.free_symbols - {p, b, c0, kap}, key=str)).coeffs()
print("  idem si W purement electrique relativement a n (B = 0) :", sp.solve(eqsB0, p, dict=True))
eqsb0 = [sp.expand(q.subs(b, 0)) for q in eqs]
print("  idem avec b = 0 (controle : seul p = 1 est regulier) :", sp.solve([q for q in eqsb0 if q != 0], p, dict=True))
print("=== E4 (ii) W' = W + ln(Omega) X ===")
xs_ = sp.symbols('xe11 xe22 xe12 xe13 xe23 xb11 xb22 xb12 xb13 xb23', real=True)
names = ['E11', 'E22', 'E12', 'E13', 'E23', 'B11', 'B22', 'B12', 'B13', 'B23']
rep = {f: xs_[names.index(str(f.func))] for v in Wt.values() for f in sp.sympify(v).atoms(sp.Function)}
Xt = {k: sp.sympify(v).xreplace(rep) for k, v in Wt.items()}
# pole de reference (p = 1) dans le repere : P = tot a p = 1
P1 = {k: sp.expand(v.subs(p, 1)) for k, v in tot.items()}
eqX = [sp.expand(sum(up(m)*n[m]*Xt[(m, k_[0], k_[1], k_[2])] for m in idx).subs(cal) + P1[k_]) for k_ in P1]
solX = sp.solve(eqX, xs_, dict=True)
print("  X de Weyl tel que n.X/Omega annule le pole :", solX)
# log induit : ln(Omega) d^mu X_mu rho nu la, X = partie electrique de W (fonctions), evalue sur div W = 0 (ordre 1)
Xel = {k: sp.sympify(v).subs({f: 0 for f in sp.sympify(v).atoms(sp.Function) if str(f.func)[0] == 'B'}) for k, v in Wt.items()}
Dj = [z for z in (jetify(sum(up(d)*sp.diff(Wt[(a, bb, c, d)], X[d]) for d in idx)) for a in idx for bb in idx for c in idx) if z != 0]
v1 = sorted({z for q in Dj for z in q.free_symbols}, key=str)
s1 = sp.solve(Dj, v1, dict=True)[0]
divX = [sp.expand(jetify(sum(up(m)*sp.diff(Xel[(m, r, nu, la)], X[m]) for m in idx)).subs(s1)) for r in idx for nu in idx for la in range(nu + 1, 4)]
print("  composantes non nulles de d.X_el sur div W = 0 (coefficient du ln Omega induit) :", sum(1 for z in divX if z != 0), "/ 24 ; exemple :", next(z for z in divX if z != 0))
