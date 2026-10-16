"""RJ2 : operateurs derives symboliquement (FW-1) : Einstein linearise autour de de Sitter (H=1, Lambda=3, kappa=1),
et operateur de Dirac conforme perturbe. Conventions de rj2_lemmes.py."""
import sympy as sp
I=sp.I
s1=sp.Matrix([[0,1],[1,0]]); s2=sp.Matrix([[0,-I],[I,0]]); s3=sp.Matrix([[1,0],[0,-1]])
Z2=sp.zeros(2); E2=sp.eye(2)
def blk(a,b,c,d): return sp.Matrix(sp.BlockMatrix([[a,b],[c,d]]))
g0=blk(E2,Z2,Z2,-E2); gu=[g0]+[blk(Z2,s,-s,Z2) for s in (s1,s2,s3)]
eta=sp.diag(-1,1,1,1)
gl=[eta[a,a]*gu[a] for a in range(4)]
beta=g0; alpha=[g0*gu[j] for j in (1,2,3)]
SGN=-1          # signe du tenseur cinetique (lu dans rj2_lemmes_sortie.txt)
CSPIN=sp.Rational(-1,4)   # coefficient de spin (idem)
X=sp.symbols('eta x y z',real=True); et=X[0]
LAM=3

def christoffel(g):
    gi=g.inv()
    return [[[sp.simplify(sum(gi[l,s]*(sp.diff(g[s,m],X[n])+sp.diff(g[s,n],X[m])-sp.diff(g[m,n],X[s])) for s in range(4))/2) for n in range(4)] for m in range(4)] for l in range(4)]

def lin_einstein(hfun):
    """delta(G + Lambda g)_{mu nu} pour g = a^2 (eta + eps h), a = -1/eta ; hfun : matrice 4x4 symetrique d'expressions."""
    a=-1/et
    gb=a**2*eta; gbi=gb.inv()
    Gb=christoffel(gb)
    dg=a**2*hfun
    # delta Gamma^l_{mn}
    dG=[[[sum(gbi[l,s]*(sp.diff(dg[s,n],X[m])+sp.diff(dg[s,m],X[n])-sp.diff(dg[m,n],X[s])) for s in range(4))/2
          -sum(gbi[l,s]*dg[s,r]*Gb[r][m][n] for s in range(4) for r in range(4)) for n in range(4)] for m in range(4)] for l in range(4)]
    def Ric_b():
        R=sp.zeros(4)
        for m in range(4):
            for n in range(4):
                R[m,n]=sum(sp.diff(Gb[l][m][n],X[l]) for l in range(4))-sum(sp.diff(Gb[l][m][l],X[n]) for l in range(4))\
                    +sum(Gb[l][l][s]*Gb[s][m][n]-Gb[l][n][s]*Gb[s][m][l] for l in range(4) for s in range(4))
        return R.applyfunc(sp.simplify)
    Rb=Ric_b(); Rsb=sp.simplify(sum(gbi[m,n]*Rb[m,n] for m in range(4) for n in range(4)))
    dR=sp.zeros(4)
    for m in range(4):
        for n in range(4):
            dR[m,n]=sum(sp.diff(dG[l][m][n],X[l]) for l in range(4))-sum(sp.diff(dG[l][m][l],X[n]) for l in range(4))\
                +sum(dG[l][l][s]*Gb[s][m][n]+Gb[l][l][s]*dG[s][m][n]-dG[l][n][s]*Gb[s][m][l]-Gb[l][n][s]*dG[s][m][l] for l in range(4) for s in range(4))
    dRs=-sum(gbi[m,a_]*gbi[n,b_]*dg[a_,b_]*Rb[m,n] for m in range(4) for n in range(4) for a_ in range(4) for b_ in range(4))\
        +sum(gbi[m,n]*dR[m,n] for m in range(4) for n in range(4))
    dE=dR-dRs*gb/2-Rsb*dg/2+LAM*dg
    Eb=Rb-Rsb*gb/2+LAM*gb
    return dE, Eb.applyfunc(sp.simplify)

def dirac_op(h,eps,psi,massterm):
    """D psi = i g^a e_a^mu nabla_mu psi - massterm*psi pour g_c = eta + eps h (vierbein symetrique)."""
    hu=eta*h        # h^mu_nu = eta^{mu rho} h_{rho nu} (eta = sa propre inverse)
    E=sp.eye(4)-eps*hu/2           # E[mu,a] = e_a^mu
    Ed=sp.eye(4)+eps*(h*eta)/2     # Ed[a,mu] = e^a_mu = delta + eps/2 h_mu^a
    g=eta+eps*h
    G=christoffel(g)
    out=sp.zeros(4,1)
    nab=[]
    for mu in range(4):
        M=sp.zeros(4)
        for a in range(4):
            for b in range(4):
                w=sum(Ed[a,nu]*(sp.diff(E[nu,b],X[mu])+sum(G[nu][mu][lm]*E[lm,b] for lm in range(4))) for nu in range(4))
                M+=CSPIN*eta[a,a]*w*gu[a]*gu[b]
        nab.append(sp.diff(psi,X[mu])+M*psi)
    for a in range(4):
        out+=I*gu[a]*sum((E[mu,a]*nab[mu] for mu in range(4)),sp.zeros(4,1))
    return out-massterm*psi

def dirac_lin(h,psi):
    """delta D psi au premier ordre pour g_c = eta + eps h (vierbein symetrique), derive directement :
    delta e_a^mu = -1/2 h^mu_a ; delta omega_mu^c_d = d_mu(delta e_d^c) + delta Gamma^c_{mu d} (fond plat, e = delta) ;
    delta D psi = i g^a delta e_a^mu d_mu psi + i g^mu CSPIN eta_cc delta omega_mu^c_d g^c g^d psi."""
    hu=eta*h
    dE=-hu/2
    dG=[[[sum(eta[l,s]*(sp.diff(h[s,n],X[m])+sp.diff(h[s,m],X[n])-sp.diff(h[m,n],X[s])) for s in range(4))/2 for n in range(4)] for m in range(4)] for l in range(4)]
    out=sp.zeros(4,1)
    for a in range(4):
        out+=I*gu[a]*sum((dE[mu,a]*sp.diff(psi,X[mu]) for mu in range(4)),sp.zeros(4,1))
    for mu in range(4):
        M=sp.zeros(4)
        for c in range(4):
            for d in range(4):
                w=sp.diff(dE[c,d],X[mu])+dG[c][mu][d]
                M+=CSPIN*eta[c,c]*w*gu[c]*gu[d]
        out+=I*gu[mu]*M*psi
    return out
