"""check_r31.py -- audit M-b : un coefficient laisse libre par ir_i.py (r31 : terme s^3 ln s de r0) entre-t-il dans un coefficient de ln de R ?"""
import sympy as sp
exec(open('/home/claude/audit_mb/work/indep_I_ferm.py').read().split('r0=sp.Function')[0])
a,b=sp.symbols('a b')
r0=s**3*sp.log(s)*a; q=s**2*b*0; r1=r0/3
XR=sp.diag(r0,r1,r1,r1)
print("div (r31 seul) :",[sp.factor(w) for w in div(XR)])
Lh=kap/2*(XR-sp.Rational(1,3)*sum(gi[i,i]*XR[i,i] for i in range(n))*gh); DL=cov(Lh)
for c in ((1,0,1),(2,0,2),(0,0,1)):
    rho_,nu,la=c; w=sp.expand(((DL[(nu,la,rho_)]-DL[(la,nu,rho_)])/s).subs(sp.log(s),L)); print(c,":",sp.collect(w,L))
# meme chose avec series sympy, comme ir_i.py : ser(expr,1)
w=sp.expand((DL[(0,1,1)]-DL[(1,0,1)])/s)
print("series(.,s,0,1) de R_(1,0,1) :",sp.series(w,s,0,1))
print("series(.,s,0,3) :",sp.series(w,s,0,3))
