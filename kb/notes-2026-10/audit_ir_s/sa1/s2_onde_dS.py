# S-a1 script 2 : onde tensorielle de dS, T^, trace, conservation, R_{rho nu lambda}, Weyl rescale.
import sympy as sp
s,x,y,z = sp.symbols('s x y z', positive=True)
k,A,B,b,kap,eps = sp.symbols('k A B b kappa epsilon')
X = [s,x,y,z]; N=4
eta = sp.diag(-1,1,1,1)
u = A*(sp.cos(k*s)+k*s*sp.sin(k*s)) + B*(sp.sin(k*s)-k*s*sp.cos(k*s))
out = []
def P(*a):
    t=' '.join(str(v) for v in a); print(t); out.append(t)
# 0. equation du mode : ghat = s^-2(eta+eps h), a=1/s ; u_ss - (2/s)u_s + k^2 u = 0
P('[calcule] mode eq u_ss-(2/s)u_s+k^2u =', sp.simplify(sp.diff(u,s,2)-2/s*sp.diff(u,s)+k**2*u))
h = sp.zeros(4,4); h[2,2]=u*sp.cos(k*x); h[3,3]=-u*sp.cos(k*x)
# 0b. verification independante : ghat lineairement Einstein avec Lambda=3 (R_ab = 3 g_ab, H=1)
def geom(g):
    gi = g.inv()
    Gam = [[[sum(gi[a,e]*(sp.diff(g[e,b_],X[c])+sp.diff(g[e,c],X[b_])-sp.diff(g[b_,c],X[e])) for e in range(N))/2
             for c in range(N)] for b_ in range(N)] for a in range(N)]
    def Riem(a,b_,c,e):  # R^a_{bce}
        r = sp.diff(Gam[a][b_][e],X[c]) - sp.diff(Gam[a][b_][c],X[e])
        r += sum(Gam[a][c][f]*Gam[f][b_][e]-Gam[a][e][f]*Gam[f][b_][c] for f in range(N))
        return r
    return gi,Gam,Riem
def ser1(e):  # ordre eps^1 (eps^0 + eps^1)
    e = sp.series(e, eps, 0, 2).removeO()
    return sp.simplify(e)
ghat = (eta+eps*h)/s**2
gi,Gam,Riem = geom(ghat)
Ric = sp.Matrix(4,4,lambda a,b_: ser1(sum(Riem(c,a,c,b_) for c in range(N))))
P('[calcule] Ric[ghat]-3 ghat (ordre eps) =', sp.simplify(Ric - (3*ghat).applyfunc(ser1)))
# 1. Weyl non lineaire de g=eta+eps h a l'ordre eps (indices bas)
g = eta+eps*h
gi,Gam,Riem = geom(g)
Rl = {}
for a in range(N):
    for b_ in range(N):
        for c in range(N):
            for e in range(N):
                Rl[(a,b_,c,e)] = ser1(sum(g[a,f]*Riem(f,b_,c,e) for f in range(N)))
Ricg = sp.Matrix(4,4,lambda a,b_: ser1(sum(gi[c,f]*Rl[(f,a,c,b_)] for c in range(N) for f in range(N))))
Rsg = ser1(sum(gi[a,b_]*Ricg[a,b_] for a in range(N) for b_ in range(N)))
Cw = {}
for a in range(N):
    for b_ in range(N):
        for c in range(N):
            for e in range(N):
                Cw[(a,b_,c,e)] = ser1(Rl[(a,b_,c,e)] - sp.Rational(1,2)*(g[a,c]*Ricg[b_,e]-g[a,e]*Ricg[b_,c]-g[b_,c]*Ricg[a,e]+g[b_,e]*Ricg[a,c])
                                      + Rsg/6*(g[a,c]*g[b_,e]-g[a,e]*g[b_,c]))
P('[calcule] C[g] nul a eps^0 :', all(Cw[q].subs(eps,0)==0 for q in Cw))
C1 = {q: sp.simplify(Cw[q].coeff(eps,1)) for q in Cw}   # coefficient de eps
# 2. Bach linearise de g : d^c d^d C_acbd
Bach = sp.Matrix(4,4,lambda a,b_: sp.simplify(sum(eta[c,c]*eta[e,e]*sp.diff(C1[(a,c,b_,e)],X[c],X[e]) for c in range(N) for e in range(N))))
P('[calcule] Bach lineaire de g (doit etre 0 : ghat Einstein, Bach conformement covariant) =', Bach)
# 3. T_ab[g] = 8 b d^c d^d(phi C_acbd) (constante 8 fixee par variation brute, script 1), phi=-ln s
phi = -sp.log(s)
T = sp.Matrix(4,4,lambda a,b_: sp.simplify(8*b*sum(eta[c,c]*eta[e,e]*sp.diff(phi*C1[(a,c,b_,e)],X[c],X[e]) for c in range(N) for e in range(N))))
That = (s**2*T).applyfunc(sp.simplify)   # coefficient de eps de T^_ab
P('[calcule] T^_ab / eps, composantes non nulles :')
for a in range(N):
    for b_ in range(a,N):
        if That[a,b_]!=0:
            P(f'  T^_{a}{b_} =', That[a,b_])
            P(f'     serie s->0 :', sp.series(That[a,b_], s, 0, 4))
P('[calcule] contient log(s) :', any(That[a,b_].has(sp.log) for a in range(N) for b_ in range(N)))
# trace : g^ab T_ab (fond suffisant a cet ordre)
P('[calcule] trace eta^ab T^_ab =', sp.simplify(sum(eta[a,a]*That[a,a] for a in range(N))))
# 4. connexion du fond ghat0 = s^-2 eta
g0 = eta/s**2
g0i,G0,_ = geom(g0)
def nab_cov2(Tm, c, a, b_):  # nabla_c T_ab
    return sp.diff(Tm[a,b_],X[c]) - sum(G0[f][c][a]*Tm[f,b_] + G0[f][c][b_]*Tm[a,f] for f in range(N))
div = [sp.simplify(sum(g0i[a,c]*nab_cov2(That,c,a,b_) for a in range(N) for c in range(N))) for b_ in range(N)]
P('[calcule] conservation nabla^a T^_ab =', div)
# 5. L^ = (kappa/2)(T^ - 1/3 g tr T) ; R_{rho nu lambda} = s^-1 (nabla_nu L_{lambda rho} - nabla_lambda L_{nu rho})
trT = sp.simplify(sum(g0i[a,b_]*That[a,b_] for a in range(N) for b_ in range(N)))
Lh = (kap/2*(That - g0*trT/3)).applyfunc(sp.simplify)
Rr = {}
P('[calcule] R_{rho nu lambda} (coefficient de eps), nu<lambda, non nuls :')
for r in range(N):
    for n in range(N):
        for l in range(n+1,N):
            v = sp.simplify((nab_cov2(Lh,n,l,r) - nab_cov2(Lh,l,n,r))/s)
            if v!=0:
                Rr[(r,n,l)] = v
                P(f'  R_{r}{n}{l} =', v)
                P(f'     serie :', sp.series(v, s, 0, 2))
# 6. Weyl rescale W = C/s, partie electrique E_ij = C_sisj/s
P('[calcule] composantes electriques C_sisj / eps et W = C/s :')
for i in range(1,N):
    for j in range(i,N):
        c = C1[(0,i,0,j)]
        if c!=0:
            P(f'  C_s{i}s{j} =', c, ' ; serie :', sp.series(c,s,0,4))
            P(f'  W_s{i}s{j}=C/s serie :', sp.series(c/s,s,0,3))
P('[calcule] composantes magnetiques (C_sijk) non nulles :')
for i in range(1,N):
    for j in range(1,N):
        for l in range(j+1,N):
            c = C1[(0,i,j,l)]
            if c!=0: P(f'  C_s{i}{j}{l} =', c, ' ; serie :', sp.series(c/s,s,0,2))
# 7. Relation R dominant <-> W electrique
P('[calcule] rapports R / (W electrique) au premier ordre en s :')
E = {(i,j): sp.simplify(C1[(0,i,0,j)]/s) for i in range(1,N) for j in range(1,N)}
for key,v in Rr.items():
    lead = sp.series(v, s, 0, 0).removeO()
    P(f'  R_{key} terme singulier :', sp.simplify(lead))
# W electrique a scri
E0 = {key: sp.limit(val, s, 0) for key,val in E.items() if val!=0}
P('[calcule] W_sisj a scri :', E0)
open('s2_sortie.txt','w').write('\n'.join(out)+'\n')
