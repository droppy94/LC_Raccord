# -*- coding: utf-8 -*-
# Calcul de dictionnaire Q <-> N/ell : Q porte-t-il une puissance de ell
# qui le ferait basculer sous ell_AdS -> i*ell_dS (mecanisme i^{d-1}, CT-REALITE) ?
import sympy as sp
from itertools import product as iproduct
from collections import defaultdict, Counter
beta, Q = sp.symbols('beta Q', real=True)
I = sp.I

# ============================================================
# [1] charge centrale c(Q) du Virasoro charge (gaz de Coulomb)
#     L_n = 1/2 sum :a_{n-k}a_k: - Q(n+1) a_n   (k3_Qsplit)
#     c/2 = || L_{-2}|0> ||^2   (car [L2,L-2]|0> = c/2 |0>)
#     L_{-2}|0> = 1/2 a_{-1}^2 + Q a_{-2}
# ============================================================
def mono(m):
    c=Counter(m); val=sp.Integer(1)
    for n,mu in c.items(): val*=(abs(n))**mu*sp.factorial(mu)
    return val
# etat L_{-2}|0> sous forme {modes: coeff}
Lm2 = { (-1,-1): sp.Rational(1,2), (-2,): Q }
normLm2 = sum(sp.conjugate(c)*c*mono(m) for m,c in Lm2.items())
c_central = sp.expand(2*normLm2)
print("charge centrale c(Q) =", c_central)
print("  c est-il PAIR en Q ? c(-Q)-c(Q) =", sp.expand(c_central.subs(Q,-Q)-c_central))
print("  c(Q=0) =", c_central.subs(Q,0), " (attendu 1 : boson libre)")

# ============================================================
# [2] norme P(beta,Q) = ||K3(Q)^+||^2  (reprise de k3_Qexplicit)
# ============================================================
def pk(k,n):
    r=sp.Integer(1)
    for j in range(1,k): r*=(-n-j)
    return r
def field_state(klist,nmax=8):
    K=sum(klist); st=defaultdict(lambda:sp.Integer(0))
    for ns in iproduct(*[range(-nmax,1) for _ in klist]):
        if sum(ns)!=-K: continue
        coeff=sp.Integer(1)
        for k,n in zip(klist,ns):
            coeff*=(-I)*pk(k,n)
            if n==0: coeff*=beta
        neg=tuple(sorted([n for n in ns if n<0]))
        st[neg]+=coeff
    return {m:sp.expand(c) for m,c in st.items() if sp.expand(c)!=0}
def add_states(lst):
    out=defaultdict(lambda:sp.Integer(0))
    for c,st in lst:
        for m,v in st.items(): out[m]+=c*v
    return {m:sp.expand(v) for m,v in out.items() if sp.expand(v)!=0}
def inner(A,B):
    tot=sp.Integer(0)
    for m,ca in A.items():
        if m in B: tot+=sp.conjugate(ca)*B[m]*mono(m)
    return sp.expand(tot)
c1s=sp.Rational(8,3)*Q**3*(-2)-sp.Rational(2,3)*Q*(-3)
c2s=sp.Rational(16,3)*Q**2*(-2)-sp.Rational(4,3)*(-3)
c3s=sp.Integer(-3); c4s=4*Q*(-2); c5s=sp.Integer(-2)
A4=c1s*sp.Rational(1,6)*I; A31=c2s*sp.Rational(-1,2); A22=c3s*(-1)
A211=c4s*(-I); A1111=c5s
cCos3=A4*beta**4-A211*beta**2; cSin3=A31*beta**3-4*A1111*beta
cCos21=-A31*beta**2-2*A22*beta**2; cSin21=3*A4*beta**3-2*A211*beta
cCos3d=-A4*beta**2; cSin3d=-A31*beta
s111=field_state([1,1,1]); s21=field_state([2,1]); s3=field_state([3])
K3p=add_states([(cCos3*sp.Rational(1,2),s111),(cSin3/(2*I),s111),
                (cCos21*sp.Rational(1,2),s21),(cSin21/(2*I),s21),
                (cCos3d*sp.Rational(1,2),s3),(cSin3d/(2*I),s3)])
P=sp.expand(inner(K3p,K3p))
Peven=sp.expand((P+P.subs(Q,-Q))/2); Podd=sp.expand((P-P.subs(Q,-Q))/2)
print("\n||K3(Q)||^2 = P : parties")
print("  P_odd (impair en Q) == 0 ?", Podd==0)
print("  deg_Q(P) =", sp.degree(sp.Poly(P,Q)))

# ============================================================
# [3] LE TEST : que fait chaque transformation candidate ?
#     A  : Q fixe (screening beta->2Q-beta)      -> reflexion sur beta seul
#     B  : Q -> -Q     (phi->-phi complet)
#     iQ : Q -> iQ     (charge de fond imaginaire = timelike/dS Liouville)
#     AU : (beta,Q)->(-beta,-Q)  (audit : seule sym. de P)
# ============================================================
print("\n=== ce que chaque transfo fait a P et a c ===")
tests = {
 "Q->-Q  (branche B)"       : {Q:-Q},
 "Q->iQ  (dict. dS/timelike)": {Q:I*Q},
 "beta->2Q-beta (screening A, Q fixe)": {beta:2*Q-beta},
 "(beta,Q)->(-beta,-Q) (audit)": {beta:-beta, Q:-Q},
}
for name,sub in tests.items():
    dP = sp.simplify(P.subs(sub,simultaneous=True)-P)
    dc = sp.simplify(c_central.subs(sub,simultaneous=True)-c_central)
    print("  %-38s: dP=0? %-5s  dc=0? %s" % (name, dP==0, dc==0))

# test realite de P sous Q->iQ
P_iQ = sp.expand(P.subs(Q,I*Q))
print("\nP(beta,iQ) est-il reel (=> partie imaginaire nulle) ?",
      sp.im(P_iQ)==0, "  ; egal a P ?", sp.simplify(P_iQ-P)==0)

# ============================================================
# [4] canal indirect : le retournement dimensionnel c -> -c (dS/CFT, i^{d-1})
#     est-il realisable par une transfo REELLE de Q ?  c=1+4Q^2.
# ============================================================
print("\n=== canal indirect Q <-> c : peut-on realiser c -> -c par Q reel ? ===")
qsol_flip = sp.solve(sp.Eq(c_central.subs(Q,sp.Symbol('Qp')), -c_central), sp.Symbol('Qp'))
print("  Q' tel que c(Q')=-c(Q) :", qsol_flip, " (reel ? ", 
      [s.is_real for s in qsol_flip] if qsol_flip else "aucun", ")")
qsol_iflip = sp.solve(sp.Eq(c_central.subs(Q,sp.Symbol('Qp')), I*c_central), sp.Symbol('Qp'))
print("  Q' tel que c(Q')=i*c(Q) (cas d=2) :", qsol_iflip)

# ============================================================
# [5] structure ASH/F1_spn : <JJ> = +/-(ell^2/G) f(x). Q est DANS f(x),
#     le +/- est DANS le prefacteur. Decouplage : Q n'apparait pas dans le prefacteur.
# ============================================================
ell,G = sp.symbols('ell G', positive=True)
prefac_AdS = +ell**2/G
prefac_dS  = (I*ell)**2/G          # ell_AdS -> i ell_dS
print("\n=== prefacteur ASH (F1_spn) : ell^2/G sous ell->i*ell ===")
print("  prefac_AdS =", prefac_AdS, " ; prefac_dS =", sp.simplify(prefac_dS),
      " => facteur", sp.simplify(prefac_dS/prefac_AdS), "(= N->-N)")
print("  Q apparait-il dans le prefacteur ? ", Q in prefac_dS.free_symbols)
