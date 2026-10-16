"""RB-3 : les solutions j = +-2 des jauges longitudinale et B (meme donnees, mu = 13/10, vecteurs gen)
sont-elles reliees par h^B - h^L = L_xi eta + 2 (xi^eta/Omega) eta ? Ordre de xi^eta, de sigma = xi^eta/Omega,
et controle Delta L = -dd sigma, composante par composante."""
import sys, pickle
import sympy as sp
from rj2_series import Ser, dOm
I=sp.I; MU=sp.Rational(13,10); NG=6
tag=sys.argv[1] if len(sys.argv)>1 else 'gen_generique'
A=pickle.load(open(f"rb3_geo_long_{tag}.pkl","rb")); B=pickle.load(open(f"rb3_geo_B_{tag}.pkl","rb"))
NS=dict(sp.__dict__)
def ser(d,N=NG): return Ser({k:eval(v,NS) for k,v in d.items()},N)
eta=sp.diag(-1,1,1,1)
def hmat(G,q):
    g=G['geo'][q]; s={nm:ser(g[nm]) for nm in g}
    h=[[None]*4 for _ in range(4)]
    h[0][0]=s['Phi'].scale(-2)
    for i in range(1,4):
        h[0][i]=h[i][0]=s['S%d'%i]
        for k in range(1,4):
            H=s['H%d%d'%(min(i,k),max(i,k))]
            h[i][k]=(H+s['Psi'].scale(-2)) if i==k else H
    return h
def dser(s_,a,q): return dOm(s_,MU).scale(-1) if a==0 else s_.scale(I*q[a-1])
def onlyj(s_,js): return Ser({k:v for k,v in s_.d.items() if k[1] in js},s_.N)
def osc(s_):
    o=[n for (n,j) in s_.d if j!=0]; return min(o) if o else None
def Lsch(h,q):
    dd={}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4): dd[(a,b,c,d)]=dser(dser(h[a][b],c,q),d,q)
    Rm=lambda a,b,c,d:(dd[(a,d,b,c)]+dd[(b,c,a,d)]-dd[(b,d,a,c)]-dd[(a,c,b,d)]).scale(sp.Rational(1,2))
    Ric={(b,d):sum((Rm(a,b,a,d).scale(eta[a,a]) for a in range(4)),Ser({},50)) for b in range(4) for d in range(4)}
    Rs=sum((Ric[(b,b)].scale(eta[b,b]) for b in range(4)),Ser({},50))
    return {(a,b):(Ric[(a,b)]-Rs.scale(eta[a,b]/6)).scale(sp.Rational(1,2)) for a in range(4) for b in range(4)},Rs
for q in sorted(A['geo']):
    if q==(0,0,0): continue
    hL=hmat(A,q); hB=hmat(B,q)
    if not any(k[1]!=0 for a in range(4) for b in range(4) for k in hL[a][b].d): continue
    LL,RL=Lsch(hL,q); LB,RB=Lsch(hB,q)
    print(f"secteur {q}")
    print("   L_00 : osc min long =",osc(LL[(0,0)]),"; B =",osc(LB[(0,0)]),
          "| L_0i long :",min(x for x in [osc(LL[(0,i)]) for i in (1,2,3)] if x is not None),
          "| L_ij long :",min(x for x in [osc(LL[(i,k)]) for i in (1,2,3) for k in (1,2,3)] if x is not None))
    for j in (2,-2):
        nlo,nhi=-1,NG+2
        cs=[[sp.Symbol(f'x{c}_{n}') for n in range(nlo,nhi+1)] for c in range(4)]
        xi=[Ser({(n,j):cs[c][n-nlo] for n in range(nlo,nhi+1)},nhi) for c in range(4)]
        eqs=[]
        for m in range(4):
            for n_ in range(m,4):
                rhs=Ser({},50)
                for c in range(4):
                    rhs=rhs+dser(xi[c],m,q).scale(eta[c,n_])+dser(xi[c],n_,q).scale(eta[m,c])
                rhs=rhs+xi[0].shift(-1).scale(2*eta[m,n_])
                diff=onlyj(hB[m][n_],[j])-onlyj(hL[m][n_],[j])-rhs
                eqs+=[v for (n,jj),v in diff.d.items() if jj==j and n<=NG-1]
        S=sp.linsolve(eqs,[c for row in cs for c in row])
        if S==sp.EmptySet: print(f"   j={j:+d} : AUCUN xi (non equivalents)"); continue
        s=list(S)[0]; free=set().union(*[e.free_symbols for e in s])
        x0={n:s[n-nlo].subs({f:0 for f in free}) for n in range(nlo,nhi+1)}
        nz=[n for n,v in x0.items() if sp.simplify(v)!=0 and n<=NG-1]
        print("      libres :",sorted(str(f) for f in free)); print(f"   j={j:+d} : xi existe ; xi^eta premier ordre non nul = Omega^{min(nz) if nz else None} ; sigma = xi^eta/Omega commence a Omega^{(min(nz)-1) if nz else None} ; parametres libres : {len(free)}")
        # Delta L = -dd sigma (j fixe), ordres <= NG-3
        sig=Ser({(n-1,j):x0[n] for n in range(nlo,nhi+1)},NG-1)
        ok=True
        for a in range(4):
            for b in range(4):
                r=onlyj(LB[(a,b)],[j])-onlyj(LL[(a,b)],[j])+dser(dser(sig,a,q),b,q)
                if any(n<=NG-4 for (n,jj) in r.clean().d): ok=False
        print(f"   j={j:+d} : Delta L = -dd sigma (ordres <= {NG-4}) : {ok}")
