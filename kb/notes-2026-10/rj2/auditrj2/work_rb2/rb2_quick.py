"""RB-2 controles rapides.
(1) dirac_op : Ed est-il l'inverse de E au premier ordre (h_0i non nul) ?
(2) secteurs q = +-2k : pourquoi seulement j = 0 ? (structure ou donnees)
"""
import sys, itertools
import sympy as sp
sys.path.insert(0,'.')
from rj2_ops import eta, gu, g0, beta, alpha, gl, SGN
from rj2_series import Ser, mul, dOm, conjS, dag
I=sp.I
eps=sp.symbols('eps')
hs=sp.Matrix(4,4,lambda i,j: sp.Symbol('h%d%d'%(min(i,j),max(i,j))))
hu=eta*hs
E=sp.eye(4)-eps*hu/2
Ed_code=sp.eye(4)+eps*(hs*eta)/2
Ed_true=sp.eye(4)+eps*(eta*hs)/2
P=(E*Ed_code).applyfunc(sp.expand)
print("(1) E*Ed (code) - Id a l'ordre eps :", (P-sp.eye(4)).applyfunc(lambda e: sp.expand(e).coeff(eps,1)))
print("    E*Ed (corrige) - Id a l'ordre eps :", ((E*Ed_true).applyfunc(sp.expand)-sp.eye(4)).applyfunc(lambda e: sp.expand(e).coeff(eps,1)).is_zero_matrix)

# (2) secteurs +-2k, NU reduit
MU=sp.Rational(13,10); NU=3
def ak(k): return sum((alpha[j]*k[j] for j in range(3)),sp.zeros(4))
def mode_series(k,cp,cm):
    out={}
    for j,c in ((1,sp.Matrix([cp[0],cp[1],0,0])),(-1,sp.Matrix([0,0,cm[0],cm[1]]))):
        w=c; out[(0,j)]=w
        for n in range(1,NU+1):
            w=(((n+I*j*MU)*sp.eye(4)-I*MU*beta).inv())*(I*ak(k)*w); out[(n,j)]=w.applyfunc(sp.expand)
    return Ser(out,NU).clean()
def Dser(u,k,b):
    if b==0: return dOm(u,MU).scale(-1)
    return u.scale(I*k[b-1])
def sector_T(k,datap,datam):
    # modes +k (donnees datap) et -k (datam), secteur q = 2k : paires (m=+k, mp=-k)
    Up=mode_series(k,*datap); Um=mode_series(-k,*datam)
    js=set()
    for a in range(4):
        for b in range(a,4):
            X1=mul(dag(Um),Dser(Up,k,b),lambda A,B:(A*g0*gl[a]*B)[0])
            X2=mul(dag(Um),Dser(Up,k,a),lambda A,B:(A*g0*gl[b]*B)[0])
            Y1=mul(dag(Up),Dser(Um,-k,b),lambda A,B:(A*g0*gl[a]*B)[0])
            Y2=mul(dag(Up),Dser(Um,-k,a),lambda A,B:(A*g0*gl[b]*B)[0])
            T=(X1+X2-conjS(Y1)-conjS(Y2)).scale(SGN*I/4)
            js|={kk[1] for kk in T.d}
    return sorted(js)
k1=sp.Matrix([1,0,1])
print("(2) donnees du script :", sector_T(k1,([1,I],[sp.Rational(1,2),-1]),([I,1],[1,sp.Rational(1,2)])))
print("    donnees aleatoires 1 :", sector_T(k1,([1,2],[3,-1]),([2,-1],[1,5])))
print("    donnees aleatoires 2 :", sector_T(k1,([1+I,2],[3,-I]),([2*I,-1],[1,5+I])))
