"""indep_K_weyl.py -- audit M-b : le terme d'anomalie de Weyl de Riegert, int sqrt(g) phi C^2, hors du calcul de ir_k.py.
Par invariance de Weyl de sqrt(g) C^2 : int sqrt(g) phi C^2 [s^-2(eta+eps H)] = eps^2 int phi C1.C1 (plat).
Contribution a T : nulle sur le fond (ordre 0 en H), lineaire en H ensuite. Contient-elle ln s ?"""
import sympy as sp
from sympy.calculus.euler import euler_equations
s=sp.symbols('s',positive=True); x=sp.symbols('x',real=True); X=[s,x,sp.Symbol('y'),sp.Symbol('z')]; n=4; eta=sp.diag(-1,1,1,1)
h=[sp.Function(f'h{i}')(s,x) for i in (1,2,3)]
H=sp.diag(0,*h)
d=lambda f,*ix: sp.diff(f,*[X[i] for i in ix])
Rl=lambda a,b,c,dd: (d(H[a,dd],b,c)+d(H[b,c],a,dd)-d(H[b,dd],a,c)-d(H[a,c],b,dd))/2
R4={(a,b,c,dd):Rl(a,b,c,dd) for a in range(n) for b in range(n) for c in range(n) for dd in range(n)}
Ric=sp.Matrix(n,n,lambda b,dd: sum(eta[a,a]*R4[(a,b,a,dd)] for a in range(n)))
Rs=sum(eta[a,a]*Ric[a,a] for a in range(n))
C={k:sp.expand(v-(eta[k[0],k[2]]*Ric[k[1],k[3]]-eta[k[0],k[3]]*Ric[k[1],k[2]]-eta[k[1],k[2]]*Ric[k[0],k[3]]+eta[k[1],k[3]]*Ric[k[0],k[2]])/2
          +Rs/6*(eta[k[0],k[2]]*eta[k[1],k[3]]-eta[k[0],k[3]]*eta[k[1],k[2]])) for k,v in R4.items()}
C2=sp.expand(sum(eta[a,a]*eta[b,b]*eta[c,c]*eta[dd,dd]*C[(a,b,c,dd)]**2 for a in range(n) for b in range(n) for c in range(n) for dd in range(n)))
phi=-sp.log(s)
EL=euler_equations(phi*C2,h,[s,x])
for i,e in enumerate(EL):
    Ti=sp.expand(e.lhs); lg=sp.expand(Ti).coeff(sp.log(s))
    print(f"T^(C)_{i+1} contient log(s) : {Ti.has(sp.log)} ; coefficient de ln s : {sp.simplify(lg)}")
print("EXIT 0")
