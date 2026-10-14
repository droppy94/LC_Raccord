"""op_ir_v2_ctrl.py -- controles de D (NOTE-102) : (i) operateur plat de S2 sur le mode libre ; (ii) Maxwell libre covariant (delta F = 0) => Hodge Delta F = 0 ;
(iii) premier ordre en beta non uniforme pres de I+ : rapport du terme d'ordre 1 au terme d'ordre 0 dans I^2."""
import sympy as sp
s=sp.symbols('s',positive=True); x,y,z=sp.symbols('x y z',real=True); k,u0,beta,lam=sp.symbols('k u0 beta lambda',positive=True)
X=[s,x,y,z]; n=4; eta=sp.diag(-1,1,1,1); gh=eta/s**2; gi=gh.inv()
G=[[[sp.simplify(sum(gi[l,q]*(sp.diff(gh[q,m],X[r])+sp.diff(gh[q,r],X[m])-sp.diff(gh[m,r],X[q])) for q in range(n))/2) for r in range(n)] for m in range(n)] for l in range(n)]
A=u0*sp.cos(k*s)*sp.cos(k*x)
# (i) operateur plat -d^2 = d_s^2 - d_x^2 (eta = -s) sur la composante A_y du mode libre
print("(i) (-d^2_eta) A_y / A_y =", sp.simplify((sp.diff(A,s,2)-sp.diff(A,x,2))/A))
F=sp.zeros(4,4); F[1,2]=sp.diff(A,x); F[2,1]=-F[1,2]; F[0,2]=sp.diff(A,s); F[2,0]=-F[0,2]
# (ii) delta F_nu = -nabla^mu F_mu nu
def nabF(a,m,q): return sp.diff(F[m,q],X[a])-sum(G[p][a][m]*F[p,q]+G[p][a][q]*F[m,p] for p in range(n))
dF=[sp.simplify(-sum(gi[m,a]*nabF(a,m,nu) for m in range(n) for a in range(n))) for nu in range(n)]
print("(ii) delta F (Maxwell libre covariant) =", dF, " ; dF = 0 car F = dA => Hodge Delta F = (d delta + delta d) F =", "0" if all(v==0 for v in dF) else "NON NUL")
# (iii) I^2 e^2 = 1 + 2 beta (lam - ln s) : terme d'ordre 1 / ordre 0
r=sp.limit(2*beta*(lam-sp.log(s)),s,0,'+'); print("(iii) 2 beta (lam - ln s) quand s -> 0+ :", r, " (I^2 est lineaire en ln s exactement dans l'action simplifiee de S2)")
print("EXIT 0")
