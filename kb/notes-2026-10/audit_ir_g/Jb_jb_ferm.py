"""jb_ferm.py -- (1) deformation du coefficient de T^ dans C-iso ; (2) logs d'ordre s^3 dans X^M (hors G1)."""
import sympy as sp, jb_indep as J
dl=sp.symbols('delta')
src=open('jb_indep.py').read()
# (1) deformation : T^ -> (1+delta) T^
J2={}
code=src.replace("That=trunc(-(beta/(2*e**2))","That=trunc(-(1+delta)*(beta/(2*e**2))").replace("e,beta,kap,lam,Cr=sp.symbols('e beta kappa lambda C_r',positive=True)","e,beta,kap,lam,Cr=sp.symbols('e beta kappa lambda C_r',positive=True); delta=sp.symbols('delta')").replace('if __name__=="__main__":','if False:')
exec(compile(code,'jb_indep_def','exec'),J2)
u0,c=sp.symbols('u0 c',real=True)
J2['analyse']('T1_deforme',[((1,0,0),(0,1,0),u0,c,(0,0,0),0,0)])
J2['analyse']('T2_deforme',[((1,1,0),(1,-1,1),u0,c,(0,0,0),0,0)],verbose=False)
# (2) logs d'ordre s^3 dans X^M non moyenne (mode du script)
A,A0,AB,AE=J.build([((1,0,0),(0,1,0),u0,c,(0,0,0),0,0)])
I2=(1+2*J.beta*(J.lam-J.L))/J.e**2
XM=J.Tmax(J.Fmat(A),I2).applyfunc(lambda v: J.trunc(v))
print("\nlogs d'ordre s^3 (coef de beta L) dans X^M, mode T1 :")
for (i,j) in [(0,0),(0,1),(1,1),(2,2),(3,3)]:
    v=sp.expand(sp.diff(sp.diff(XM[i,j],J.beta),J.L)).coeff(J.s,3)
    print("  ",(i,j),sp.factor(J.const_term(v) if False else v))
print("EXIT 0")
