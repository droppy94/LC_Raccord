#!/usr/bin/env python3
# Verification : contribution de la constante d'integration (fluide de rayonnement) a R_rho nu lambda
import sympy as sp
s=sp.symbols('s',positive=True); C,kap=sp.symbols('C kappa')
co=[s]+list(sp.symbols('x y z')); eta=sp.diag(-1,1,1,1); g=eta/s**2; gi=eta*s**2
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],co[c])+sp.diff(g[d,c],co[b])-sp.diff(g[b,c],co[d])) for d in range(4))/2) for c in range(4)] for b in range(4)] for a in range(4)]
T=sp.diag(C*s**2,C*s**2/3,C*s**2/3,C*s**2/3)
div=[sp.simplify(sum(gi[m,a]*(sp.diff(T[m,n],co[a])-sum(Gam[l][a][m]*T[l,n]+Gam[l][a][n]*T[m,l] for l in range(4))) for m in range(4) for a in range(4))) for n in range(4)]
tr=sp.simplify(sum(gi[m,n]*T[m,n] for m in range(4) for n in range(4)))
Lh=kap/2*(T-g*tr/3)
nab=lambda nu,la,rho: sp.diff(Lh[la,rho],co[nu])-sum(Gam[sg][nu][la]*Lh[sg,rho]+Gam[sg][nu][rho]*Lh[la,sg] for sg in range(4))
R=[sp.simplify((nab(n,l,r)-nab(l,n,r))/s) for r in range(4) for n in range(4) for l in range(4)]
print("divergence:",div,"trace:",tr,"R tous nuls:",all(v==0 for v in R))
