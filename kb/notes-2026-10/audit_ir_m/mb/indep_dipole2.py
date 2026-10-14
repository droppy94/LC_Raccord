"""indep_dipole2.py -- audit M-b, bloc I-B : integrales radiales avec derivees analytiques de m(u) et quadrature a points de rupture.
m(u) = (1 - tanh v)/2, v = (u + D)/w : m' = -sech^2 v/(2w), m'' = sech^2 v tanh v / w^2 ; int m''^2 du = 4/(15 w^3) exactement."""
import mpmath as mp
mp.mp.dps=30
D=mp.mpf(10); w=mp.mpf(1)/2
cA,cG,cAG,cE=mp.mpf(1)/5,mp.mpf(7)/15,mp.mpf(2)/15,-mp.mpf(1)/3
def mm(u):
    v=(u+D)/w; sh=mp.sech(v)**2; th=mp.tanh(v)
    return (1-th)/2, -sh/(2*w), sh*th/w**2
def q(r,mode='full'):
    m,md,mdd=mm(-r)
    al=m/r**3+md/r**2; ga=mdd/r; ep=md/r**2+mdd/r
    if mode=='rad': al=0; ep=ga
    if mode=='stat': ga=0; ep=0; al=m/r**3
    return cA*al**2+cG*ga**2+cAG*al*ga-cE*ep**2
def I(a,b,mode='full'):
    pts=[a]+[p for p in mp.linspace(a,b,25)[1:-1]]+[b] if b!=mp.inf else [a,a+1,a+3,a+10,a+100,mp.inf]
    return mp.quad(lambda r: 4*mp.pi*r**2*q(r,mode),pts)
Iin=I(mp.mpf('0.05'),D-3*w); Ish=I(D-3*w,D+3*w); Iout=I(D+3*w,mp.inf)
print("boule r in [0.05, 7] :",mp.nstr(Iin,8)," ; coquille [7,13] :",mp.nstr(Ish,10)," ; reliquat [13, inf) :",mp.nstr(Iout,8))
print("reliquat statique pur (1/5)(4 pi/3)/13^3 :",mp.nstr(cA*4*mp.pi/(3*13**3),8))
print("coquille, partie rayonnee seule :",mp.nstr(I(D-3*w,D+3*w,'rad'),10))
print("prediction exacte (4/5) 4 pi * 4/(15 w^3) =",mp.nstr(mp.mpf(4)/5*4*mp.pi*4/(15*w**3),10))
print("int m''^2 : quadrature sans point de rupture (comme ir_i.py, dps=20) :",end=' ')
mp.mp.dps=20
print(mp.nstr(mp.quad(lambda u: mm(u)[2]**2,[-mp.inf,mp.inf]),8)," ; avec rupture en u=-D :",mp.nstr(mp.quad(lambda u: mm(u)[2]**2,[-mp.inf,-D,mp.inf]),8)," ; exact 32/15 =",mp.nstr(mp.mpf(32)/15,8))
