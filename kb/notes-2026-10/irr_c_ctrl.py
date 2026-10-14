"""irr_c_ctrl.py -- controle IR-r : partie electrique du Weyl rescale W = C[g]/Omega a scri+ pour le mode de de Sitter."""
import sympy as sp
s=sp.symbols('s',positive=True); x=sp.symbols('x',real=True); k,A,B=sp.symbols('k A B',positive=True)
X=[s,x,sp.Symbol('y'),sp.Symbol('z')]; n=4; eta=sp.diag(-1,1,1,1)
u=A*(sp.cos(k*s)+k*s*sp.sin(k*s))+B*(sp.sin(k*s)-k*s*sp.cos(k*s))
H=sp.zeros(n,n); H[2,2]=u*sp.cos(k*x); H[3,3]=-u*sp.cos(k*x)
d=lambda f,*ix: sp.diff(f,*[X[i] for i in ix])
R4=lambda a,b,c,dd:(d(H[a,dd],b,c)+d(H[b,c],a,dd)-d(H[b,dd],a,c)-d(H[a,c],b,dd))/2
Ric=sp.Matrix(n,n,lambda b,dd: sum(eta[a,a]*R4(a,b,a,dd) for a in range(n)))
Rs=sum(eta[a,a]*Ric[a,a] for a in range(n))
C=lambda a,b,c,dd: R4(a,b,c,dd)-(eta[a,c]*Ric[b,dd]-eta[a,dd]*Ric[b,c]-eta[b,c]*Ric[a,dd]+eta[b,dd]*Ric[a,c])/2+Rs/6*(eta[a,c]*eta[b,dd]-eta[a,dd]*eta[b,c])
for (i,nm) in [(2,'yy'),(3,'zz'),(1,'xx')]:
    WE=sp.series(sp.simplify(C(0,i,0,i)/s),s,0,2).removeO()
    print(f"W_E,{nm} = C_s{nm[0]}s{nm[0]}/s =", sp.expand(WE))
print("EXIT 0")
