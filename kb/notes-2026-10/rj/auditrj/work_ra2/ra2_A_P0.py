# RA-2, partie A : identite P0 en toute generalite + lien exact S = rho Z (Friedrich (3.20))
import sympy as sp
t,x,y,z = sp.symbols('t x y z', real=True); X=[t,x,y,z]
lam = sp.Symbol('lambda')

def check_P0(g, Om, That, label, simplify=True):
    gi = g.inv()
    gh = g/Om**2; ghi = gi*Om**2
    def chris(G, Gi):
        return [[[sp.together(sum(Gi[a,d]*(sp.diff(G[d,b],X[c])+sp.diff(G[d,c],X[b])-sp.diff(G[b,c],X[d])) for d in range(4))/2)
                  for c in range(4)] for b in range(4)] for a in range(4)]
    Gh = chris(gh, ghi); G = chris(g, gi)
    trT = sum(ghi[a,b]*That[a,b] for a in range(4) for b in range(4))
    Lh = (That - trT*gh/3)/2 + lam*gh/6
    def covd(Gam, Tm,k,l,j):
        return sp.diff(Tm[l,j],X[k]) - sum(Gam[m][k][l]*Tm[m,j] for m in range(4)) - sum(Gam[m][k][j]*Tm[l,m] for m in range(4))
    # tau en coordonnees : tau_jk = Omega^-3 T-hat(e-hat_j,e-hat_k) en repere ; en coordonnees tau_{mu nu} = That_{mu nu}/Omega
    tau = That/Om
    trtau = sum(gi[a,b]*tau[a,b] for a in range(4) for b in range(4))
    taup = tau - trtau*g/3
    n = [sp.diff(Om,v) for v in X]
    nup = [sum(gi[m,q]*n[q] for q in range(4)) for m in range(4)]
    bad = 0
    for j in range(4):
        for k in range(4):
            for l in range(k+1,4):
                lhs = (covd(Gh,Lh,k,l,j)-covd(Gh,Lh,l,k,j))/Om
                S = sp.Rational(1,2)*(2*(n[k]*taup[l,j]-n[l]*taup[k,j]) - g[k,j]*sum(nup[m]*taup[l,m] for m in range(4))
                                      + g[l,j]*sum(nup[m]*taup[k,m] for m in range(4)))
                rhs = sp.Rational(1,2)*(covd(G,taup,k,l,j)-covd(G,taup,l,k,j)) + S/Om
                d = sp.together(sp.expand(lhs-rhs))
                if simplify: d = sp.simplify(d)
                if d != 0: bad += 1
    print(label, ": composantes testees 24, residus non nuls :", bad)

# A1 : Omega et T-hat fonctions ARBITRAIRES, g Minkowski
Om = sp.Function('W')(*X)
That = sp.zeros(4,4)
for a in range(4):
    for b in range(a,4):
        f = sp.Function(f'T{a}{b}')(*X); That[a,b]=f; That[b,a]=f
check_P0(sp.diag(-1,1,1,1), Om, That, "A1 (Omega, T-hat fonctions arbitraires, g = eta)")

# A2 : g courbe (polynomiale non plate, non diagonale), Omega et T-hat polynomiaux
g = sp.Matrix([[-1-x**2/7, t*y/5, 0, z/9],[t*y/5, 1+t**2/3, x*z/11, 0],[0, x*z/11, 1+y**2/5, 0],[z/9,0,0,1+x*t/13]])
Om2 = 2 - t + x*y/3 + z**2/5
import random; random.seed(7)
T2 = sp.zeros(4,4)
for a in range(4):
    for b in range(a,4):
        e = sum(sp.Rational(random.randint(-3,3),random.randint(1,4))*m for m in [1,t,x,y,z,t*x,y**2])
        T2[a,b]=e; T2[b,a]=e
# verification numerique aleatoire (sympy exact rationnel en points) pour eviter un simplify tres long
def check_points(g, Om, That, npts=4):
    gi = g.inv(); gh = g/Om**2; ghi = gi*Om**2
    def chris(G, Gi):
        return [[[sum(Gi[a,d]*(sp.diff(G[d,b],X[c])+sp.diff(G[d,c],X[b])-sp.diff(G[b,c],X[d])) for d in range(4))/2
                  for c in range(4)] for b in range(4)] for a in range(4)]
    Gh = chris(gh, ghi); G = chris(g, gi)
    trT = sum(ghi[a,b]*That[a,b] for a in range(4) for b in range(4))
    Lh = (That - trT*gh/3)/2 + lam*gh/6
    tau = That/Om; trtau = sum(gi[a,b]*tau[a,b] for a in range(4) for b in range(4)); taup = tau - trtau*g/3
    n = [sp.diff(Om,v) for v in X]; nup = [sum(gi[m,q]*n[q] for q in range(4)) for m in range(4)]
    def covd(Gam, Tm,k,l,j):
        return sp.diff(Tm[l,j],X[k]) - sum(Gam[m][k][l]*Tm[m,j] for m in range(4)) - sum(Gam[m][k][j]*Tm[l,m] for m in range(4))
    pts = [{t:sp.Rational(1,3),x:sp.Rational(1,2),y:sp.Rational(-1,5),z:sp.Rational(2,7),lam:3},
           {t:sp.Rational(-2,3),x:sp.Rational(3,4),y:sp.Rational(1,6),z:sp.Rational(-1,3),lam:sp.Rational(1,2)},
           {t:sp.Rational(1,9),x:sp.Rational(-1,4),y:sp.Rational(5,6),z:sp.Rational(1,2),lam:-1}]
    worst = 0
    for p in pts:
        for j in range(4):
            for k in range(4):
                for l in range(k+1,4):
                    lhs = (covd(Gh,Lh,k,l,j)-covd(Gh,Lh,l,k,j))/Om
                    S = sp.Rational(1,2)*(2*(n[k]*taup[l,j]-n[l]*taup[k,j]) - g[k,j]*sum(nup[m]*taup[l,m] for m in range(4))
                                          + g[l,j]*sum(nup[m]*taup[k,m] for m in range(4)))
                    rhs = sp.Rational(1,2)*(covd(G,taup,k,l,j)-covd(G,taup,l,k,j)) + S/Om
                    v = sp.nsimplify((lhs-rhs).subs(p))
                    if v != 0: worst += 1
    return worst
print("A2 (g courbe non diagonale, 3 points rationnels exacts, 72 tests) : residus non nuls :", check_points(g, Om2, T2))

# A3 : pour tau = rho U U (U unitaire QUELCONQUE, n quelconque), S = rho Z  avec Z de Friedrich (3.20)
r = sp.Symbol('rho'); n0,n1,n2,n3 = sp.symbols('n0:4'); v1,v2,v3 = sp.symbols('v1:4', real=True)
eta = sp.diag(-1,1,1,1)
gam = 1/sp.sqrt(1-v1**2-v2**2-v3**2)
Uup = [gam, gam*v1, gam*v2, gam*v3]; U = [eta[i,i]*Uup[i] for i in range(4)]
nn = [n0,n1,n2,n3]; nnu=[eta[i,i]*nn[i] for i in range(4)]
tau = sp.Matrix(4,4,lambda i,j: r*U[i]*U[j]); trt = sum(eta[i,i]*tau[i,i] for i in range(4)); tp = tau - trt*eta/3
Un = sum(Uup[i]*nn[i] for i in range(4))
bad=0
for j in range(4):
    for k in range(4):
        for l in range(k+1,4):
            S = sp.Rational(1,2)*(2*(nn[k]*tp[l,j]-nn[l]*tp[k,j]) - eta[k,j]*sum(nnu[m]*tp[l,m] for m in range(4)) + eta[l,j]*sum(nnu[m]*tp[k,m] for m in range(4)))
            Zf = (nn[k]*eta[l,j]-nn[l]*eta[k,j])/2 + (nn[k]*U[l]-nn[l]*U[k])*U[j] + (U[k]*eta[l,j]-U[l]*eta[k,j])/2*Un
            if sp.simplify(S - r*Zf) != 0: bad+=1
print("A3 : S(rho U U, n) - rho Z_Friedrich, U et n quelconques : residus non nuls :", bad)
