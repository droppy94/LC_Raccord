"""RJ2 : arithmetique de la classe K = { sum c_{n,j} Omega^{n + i j mu} } (NOTE-216, RJ2-2/3).
Serie = dict {(n,j): coefficient sympy (scalaire ou Matrix)} ; mu reel (rationnel dans les tests)."""
import sympy as sp
I=sp.I
class Ser:
    def __init__(self,d=None,N=None): self.d={k:v for k,v in (d or {}).items()}; self.N=N  # N : ordre de troncature (n <= N valide)
    def copy(self): return Ser(dict(self.d),self.N)
    def clean(self):
        out={}
        for k,v in self.d.items():
            if self.N is not None and k[0]>self.N: continue
            vv=sp.expand(v) if not isinstance(v,sp.MatrixBase) else v.applyfunc(sp.expand)   # coefficients exacts (mu rationnel)
            if (isinstance(vv,sp.MatrixBase) and vv.is_zero_matrix) or (not isinstance(vv,sp.MatrixBase) and vv==0): continue
            out[k]=vv
        self.d=out; return self
    def __add__(self,o):
        d=dict(self.d)
        for k,v in o.d.items(): d[k]=d[k]+v if k in d else v
        N=min(x for x in (self.N,o.N) if x is not None) if (self.N is not None or o.N is not None) else None
        return Ser(d,N).clean()
    def __neg__(self): return Ser({k:-v for k,v in self.d.items()},self.N)
    def __sub__(self,o): return self+(-o)
    def scale(self,c): return Ser({k:c*v for k,v in self.d.items()},self.N).clean()
    def shift(self,p): return Ser({(k[0]+p,k[1]):v for k,v in self.d.items()},None if self.N is None else self.N+p)
    def nmin(self): return min((k[0] for k in self.d),default=None)
def mul(A,B,op=lambda a,b:a*b):
    """produit de deux series ; troncature : N = min(NA + nminB, NB + nminA)"""
    d={}
    for (n1,j1),a in A.d.items():
        for (n2,j2),b in B.d.items():
            k=(n1+n2,j1+j2); v=op(a,b); d[k]=d[k]+v if k in d else v
    NA,NB=A.N,B.N; mA,mB=A.nmin(),B.nmin()
    N=None
    if NA is not None and mB is not None: N=NA+mB
    if NB is not None and mA is not None: N=min(N,NB+mA) if N is not None else NB+mA
    return Ser(d,N).clean()
def dOm(A,mu):
    return Ser({(n-1,j):(n+I*j*mu)*v for (n,j),v in A.d.items() if not (n==0 and j==0)},None if A.N is None else A.N-1).clean()
def conjS(A):
    return Ser({(n,-j):(sp.conjugate(v) if not isinstance(v,sp.MatrixBase) else v.conjugate()) for (n,j),v in A.d.items()},A.N)
def dag(A):
    return Ser({(n,-j):v.H for (n,j),v in A.d.items()},A.N)
def show(A,maxterms=12):
    ks=sorted(A.d.keys())
    return ", ".join(f"O^({n}{'+' if j>=0 else '-'}{abs(j)}i mu)" for n,j in ks[:maxterms])+(" ..." if len(ks)>maxterms else "")
