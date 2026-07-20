"""
Symbolic computation on the c=1 free-boson Fock space (sympy).
Companion to audit_neutral.py / anchor_neutral.py; identical machinery and the
same state Psi(beta, Q). This file adds five self-standing checks on scalar
quantities built from a real parameter Q.

Objects:
  v      = fixed two-term vector { (-1,-1): 1/2 , (-2): Q }  on the Fock space.
  c(Q)   = 2 * weight(v, v)        (weight = diagonal monomial weight below).
  Psi    = fixed linear combination of three Fock vectors (s111, s21, s3),
           coefficients g1,g2,g3 polynomial in (beta, Q); built exactly as in
           the companion files.
  P(b,Q) = herm(Psi, Psi)          (sesquilinear norm).
  prefac = w**2 / g                (w, g positive symbols).

Reported checks (please state your expectations BEFORE running, then compare):
  D0  c(Q): closed form; is c even in Q (c(-Q)-c(Q)=0)?; value c(0).
  D1  P: is its Q-odd part zero?; degree of P in Q.
  D2  For each candidate substitution s, do P and c change? (dP=0?, dc=0?)
        s in { Q->-Q ; Q->iQ ; beta->2Q-beta ; (beta,Q)->(-beta,-Q) }.
  D3  Reality of P under Q->iQ: is Im P(beta,iQ)=0?; is P(beta,iQ)=P?
  D4  Solve for Q' the equations c(Q')=-c(Q) and c(Q')=i*c(Q); report the
        roots and whether they are real.
  D5  prefac under w->i*w: report the multiplicative factor; does Q occur in
        prefac's free symbols?

No physical interpretation is asserted. The reader is invited to check, in
particular:
  (a) whether the diagonal weight used to define c(Q) is the right/only inner
      product, i.e. whether the parity of c is a genuine property or an artifact
      of that normalization;
  (b) whether "Q does not occur in prefac" is a fact of the given expression or
      an assumption imported by the way prefac is written;
  (c) whether "no real Q' solves c(Q')=-c(Q)" establishes anything beyond the
      stated polynomial identity -- e.g. whether some other continuation of Q
      (not tested here) could realize it;
  (d) which reported outcomes are forced purely by construction rather than
      genuine.
"""
import sympy as sp
from itertools import product as iproduct
from collections import defaultdict, Counter
beta, Q = sp.symbols('beta Q', real=True)
w, g = sp.symbols('w g', positive=True)
I = sp.I

# ---------- Fock-space machinery (identical to companion files) ----------
def pk(k, n):
    r = sp.Integer(1)
    for j in range(1, k): r *= (-n - j)
    return r

def field_state(klist, nmax=8):
    K = sum(klist); st = defaultdict(lambda: sp.Integer(0))
    for ns in iproduct(*[range(-nmax, 1) for _ in klist]):
        if sum(ns) != -K: continue
        coeff = sp.Integer(1)
        for k, n in zip(klist, ns):
            coeff *= (-I) * pk(k, n)
            if n == 0: coeff *= beta
        neg = tuple(sorted([n for n in ns if n < 0]))
        st[neg] += coeff
    return {m: sp.expand(c) for m, c in st.items() if sp.expand(c) != 0}

def add_states(lst):
    out = defaultdict(lambda: sp.Integer(0))
    for c, st in lst:
        for m, v_ in st.items(): out[m] += c * v_
    return {m: sp.expand(v_) for m, v_ in out.items() if sp.expand(v_) != 0}

def mono_norm2(modes):
    # diagonal weight of a monomial: prod_n |n|^mult(n) * mult(n)!
    c = Counter(modes); val = sp.Integer(1)
    for n, mult in c.items():
        val *= (abs(n))**mult * sp.factorial(mult)
    return val

def herm(A, B):   # sesquilinear form (conjugate on A)
    tot = sp.Integer(0)
    for m, ca in A.items():
        if m in B: tot += sp.conjugate(ca) * B[m] * mono_norm2(m)
    return sp.expand(tot)

# ---------- state Psi(beta, Q) : identical construction to companions ----------
s111 = field_state([1, 1, 1])
s21  = field_state([2, 1])
s3   = field_state([3])
m1 = sp.Rational(8,3)*Q**3*(-2) - sp.Rational(2,3)*Q*(-3)
m2 = sp.Rational(16,3)*Q**2*(-2) - sp.Rational(4,3)*(-3)
m3 = sp.Integer(-3); m4 = 4*Q*(-2); m5 = sp.Integer(-2)
a1 = m1*sp.Rational(1,6)*I     # imaginary
a2 = m2*sp.Rational(-1,2)
a3 = m3*(-1)
a4 = m4*(-I)                   # imaginary
a5 = m5
h1 = a1*beta**4 - a4*beta**2      # s111
h2 = a2*beta**3 - 4*a5*beta       # s111
h3 = -a2*beta**2 - 2*a3*beta**2   # s21
h4 = 3*a1*beta**3 - 2*a4*beta     # s21
h5 = -a1*beta**2                  # s3
h6 = -a2*beta                     # s3
g1 = h1*sp.Rational(1,2) + h2/(2*I)
g2 = h3*sp.Rational(1,2) + h4/(2*I)
g3 = h5*sp.Rational(1,2) + h6/(2*I)
Psi = add_states([(g1, s111), (g2, s21), (g3, s3)])

# ============================================================
# D0. scalar c(Q) = 2 * weight(v, v),  v = {(-1,-1):1/2, (-2):Q}
# ============================================================
print("="*64); print("D0.  c(Q) and its parity in Q"); print("="*64)
v = { (-1,-1): sp.Rational(1,2), (-2,): Q }
weight_v = sum(sp.conjugate(cc)*cc*mono_norm2(m) for m, cc in v.items())
c_scalar = sp.expand(2*weight_v)
print("  c(Q) =", c_scalar)
print("  c(-Q) - c(Q) =", sp.expand(c_scalar.subs(Q,-Q) - c_scalar), " (0 => even in Q)")
print("  c(0) =", c_scalar.subs(Q,0))

# ============================================================
# D1. norm P(beta,Q) = herm(Psi,Psi)
# ============================================================
print(); print("="*64); print("D1.  P(beta,Q) = herm(Psi,Psi)"); print("="*64)
P = sp.expand(herm(Psi, Psi))
Podd = sp.expand((P - P.subs(Q,-Q))/2)
print("  P_odd (Q-odd part) == 0 ?", Podd == 0)
print("  degree of P in Q =", sp.degree(sp.Poly(P, Q)))
print("  P(beta,0) =", sp.factor(P.subs(Q,0)))

# ============================================================
# D2. effect of candidate substitutions on P and on c
# ============================================================
print(); print("="*64); print("D2.  substitutions: dP=0 ?  dc=0 ?"); print("="*64)
tests = {
 "Q -> -Q"                    : {Q: -Q},
 "Q -> iQ"                    : {Q: I*Q},
 "beta -> 2Q - beta"          : {beta: 2*Q - beta},
 "(beta,Q) -> (-beta,-Q)"     : {beta: -beta, Q: -Q},
}
for name, sub in tests.items():
    dP = sp.simplify(P.subs(sub, simultaneous=True) - P)
    dc = sp.simplify(c_scalar.subs(sub, simultaneous=True) - c_scalar)
    print("  %-24s: dP=0? %-5s  dc=0? %s" % (name, dP == 0, dc == 0))

# ============================================================
# D3. reality of P under Q -> iQ
# ============================================================
print(); print("="*64); print("D3.  P(beta, iQ)"); print("="*64)
P_iQ = sp.expand(P.subs(Q, I*Q))
print("  Im P(beta,iQ) == 0 ?", sp.im(P_iQ) == 0)
print("  P(beta,iQ) - P == 0 ?", sp.simplify(P_iQ - P) == 0)

# ============================================================
# D4. can c(Q')=-c(Q) or c(Q')=i c(Q) be solved for Q' ? are roots real ?
# ============================================================
print(); print("="*64); print("D4.  solving c(Q')=-c(Q) and c(Q')=i c(Q)"); print("="*64)
Qp = sp.Symbol('Qp')
sol_neg = sp.solve(sp.Eq(c_scalar.subs(Q, Qp), -c_scalar), Qp)
sol_i   = sp.solve(sp.Eq(c_scalar.subs(Q, Qp),  I*c_scalar), Qp)
print("  c(Q') = -c(Q):  Q' =", sol_neg,
      " ; real ?", [s.is_real for s in sol_neg] if sol_neg else "none")
print("  c(Q') = i c(Q): Q' =", sol_i,
      " ; real ?", [s.is_real for s in sol_i] if sol_i else "none")

# ============================================================
# D5. prefactor w**2/g under w -> i w ; does Q occur in it ?
# ============================================================
print(); print("="*64); print("D5.  prefac = w**2/g under w -> i w"); print("="*64)
prefac = w**2 / g
prefac_t = (I*w)**2 / g
print("  prefac =", prefac, " ; after w->i w =", sp.simplify(prefac_t))
print("  multiplicative factor =", sp.simplify(prefac_t/prefac))
print("  does Q occur in prefac ? ", Q in prefac.free_symbols)
