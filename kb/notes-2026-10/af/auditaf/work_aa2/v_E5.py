# Variante E5 : robustesse de la condition AF-2 a une completion de S2 (Omega[g] fonctionnelle de la metrique).
# On ajoute a That des termes construits sur (eta, n) et les scalaires F^2, F.Ftilde :
#   Omega^2 [a1 eta_ab + a2 n_a n_b] beta F^2  (sans log, cas d'une variation de sigma)  +  Omega^2 ln Omega [a3 eta_ab + a4 n_a n_b] beta F^2
#   + Omega^2 ln Omega a5 eta_ab beta F.Ftilde ; Lhat = kappa/2 (That - 1/3 ghat tr That). Puis conditions d'annulation de Omega^0 ln Omega.
import sympy as sp, itertools
txt = open('af_check_copie.py').read()
exec(txt.split('# ---------------------------------------------------------------- AF-1')[0])
sigma = -sp.log(Om_f)
exec('\n'.join(txt.split('\n')[124:144]))
nS = list(n); nupS = [up(a)*n[a] for a in idx]
R_ = lambda nm: sp.Symbol(nm, real=True)
cal = {n[0]: 1, n[1]: 0, n[2]: 0, n[3]: 0, s: 0, lam: 3}
Ff = {(a, bb): sp.Function(f'F{a}{bb}')(*X) for a in idx for bb in idx if a < bb}
F = lambda a, bb: 0 if a == bb else (Ff[(a, bb)] if a < bb else -Ff[(bb, a)])
coup = 1/e2 - 4*betas*sigma
F2 = sum(up(a)*up(bb)*F(a, bb)**2 for a in idx for bb in idx)
FFd = sum(sp.LeviCivita(a, bb, c, d)*F(a, bb)*F(c, d) for a, bb, c, d in itertools.product(idx, repeat=4))
M = sp.Matrix(4, 4, lambda a, bb: sum(up(c)*F(a, c)*F(bb, c) for c in idx) - eta[a, bb]*F2/4)
al = sp.symbols('a1:6', real=True)
nf_ = [sp.diff(Om_f, X[a]) for a in idx]
extra = sp.Matrix(4, 4, lambda a, bb: Om_f**2*betas*((al[0]*eta[a, bb] + al[1]*nf_[a]*nf_[bb])*F2
                   + sp.log(Om_f)*((al[2]*eta[a, bb] + al[3]*nf_[a]*nf_[bb])*F2 + al[4]*eta[a, bb]*FFd)))
Th = (coup*Om_f**2*M + extra).applyfunc(sp.expand)
trg = Om_f**2*sum(up(a)*Th[a, a] for a in idx)                     # ghat^ab That_ab
Lh2 = sp.Matrix(4, 4, lambda a, bb: kap/2*(Th[a, bb] - sp.Rational(1, 3)*eta[a, bb]/Om_f**2*trg))
calEB = None
Ei = sp.symbols('Ex Ey Ez', real=True); Bi = sp.symbols('Bx By Bz', real=True)
calEB = {R_('F01'): Ei[0], R_('F02'): Ei[1], R_('F03'): Ei[2], R_('F23'): Bi[0], R_('F13'): -Bi[1], R_('F12'): Bi[2]}
print("=== E5 : completion isotrope / (eta, n) ===")
logc = {}
for rho in idx:
    for nu in idx:
        for la in range(nu + 1, 4):
            r = jetify(subs_omega(R217(Lh2, rho, nu, la)))
            r = sp.expand(r.subs(cal))
            logc[(rho, nu, la)] = sp.expand(sp.expand(r).coeff(LOG, 1).coeff(W, 0).subs(calEB))
for k_ in [(1, 0, 2), (2, 0, 3), (1, 0, 1), (2, 0, 2), (0, 0, 1), (1, 1, 2), (2, 1, 2)]:
    print("  ln Omega coeff", k_, ":", sp.factor(logc[k_]))
Stf_off = [Ei[0]*Ei[1] + Bi[0]*Bi[1], Ei[0]*Ei[2] + Bi[0]*Bi[2], Ei[1]*Ei[2] + Bi[1]*Bi[2]]
print("  composantes hors diagonale (i,0,j), i != j, independantes de a1..a5 :",
      all(not (logc[k_].free_symbols & set(al)) for k_ in [(1, 0, 2), (1, 0, 3), (2, 0, 3), (2, 0, 1), (3, 0, 1), (3, 0, 2)]))
d12 = sp.expand(logc[(1, 0, 1)] - logc[(2, 0, 2)]); d23 = sp.expand(logc[(2, 0, 2)] - logc[(3, 0, 3)])
print("  differences diagonales R(1,0,1)-R(2,0,2), R(2,0,2)-R(3,0,3) :", sp.factor(d12), ";", sp.factor(d23))
print("  => (E_iE_j + B_iB_j)_tf = 0 reste impose quelle que soit la completion de cette forme ; pour E, B reels : E = B = 0")
