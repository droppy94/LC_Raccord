"""indep_dipole3.py -- audit M-b, bloc I-B : integrales par region, bornes reelles du script (7, 13 = D -+ 6w) et bornes D -+ 3w (8.5, 11.5).
Quadrature : somme de sous-intervalles courts (mp.quad sur une longue liste de points s'est revele non fiable ici)."""
import mpmath as mp
exec(open('/home/claude/audit_mb/work/indep_dipole2.py').read().split('def I(')[0])
def Isum(a,b,mode='full',N=48):
    pts=mp.linspace(mp.mpf(a),mp.mpf(b),N+1); return mp.fsum(mp.quad(lambda r: 4*mp.pi*r**2*q(r,mode),[pts[i],pts[i+1]]) for i in range(N))
tail=lambda a: Isum(a,60)+mp.quad(lambda r: 4*mp.pi*r**2*q(r),[60,200,mp.inf])
pred=mp.mpf(4)/5*4*mp.pi*4/(15*w**3)
for lab,(a,b) in (("bornes du script (D -+ 6w)",(7,13)),("bornes D -+ 3w",(mp.mpf('8.5'),mp.mpf('11.5')))):
    Ib=Isum('0.05',a); Ic=Isum(a,b); Icr=Isum(a,b,'rad'); It=tail(b)
    print(f"{lab} : boule {mp.nstr(Ib,6)} ; coquille {mp.nstr(Ic,9)} (rayonne seul {mp.nstr(Icr,9)}) ; reliquat {mp.nstr(It,6)} (statique pur {mp.nstr(cA*4*mp.pi/(3*mp.mpf(b)**3),6)})")
print("prediction rayonnee exacte :",mp.nstr(pred,9)," ; ecart relatif coquille (bornes du script) :",mp.nstr((Isum(7,13)-pred)/pred,3))
print("total toutes regions :",mp.nstr(Isum('0.05',13)+tail(13),9))
