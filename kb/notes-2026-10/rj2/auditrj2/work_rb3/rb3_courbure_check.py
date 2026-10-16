"""RB-3 : controle independant des formules de courbure lineaire de rj2_test_v2.py (l.276-284).
Reproduit le schema d'indices du script sur un h generique et le compare a une derivation directe
(Christoffel lineaire, R^a_bcd = d_c G^a_bd - d_d G^a_bc), puis teste Schouten et Weyl sur h = 2 sigma eta."""
import sympy as sp
X=sp.symbols('t x y z'); eta=sp.diag(-1,1,1,1)
h=sp.Matrix(4,4,lambda i,j: sp.Function('h%d%d'%(min(i,j),max(i,j)))(*X))
def D(f,c,d): return sp.diff(f,X[c],X[d])
# --- schema du script
def dd(a,b,c,d): return D(h[a,b],c,d)
def Riem_s(a,b,c,d): return sp.Rational(1,2)*(dd(a,d,b,c)+dd(b,c,a,d)-dd(b,d,a,c)-dd(a,c,b,d))
# --- derivation directe
G=[[[sum(eta[l,s]*(sp.diff(h[s,n],X[m])+sp.diff(h[s,m],X[n])-sp.diff(h[m,n],X[s])) for s in range(4))/2 for n in range(4)] for m in range(4)] for l in range(4)]
def Rup(a,b,c,d): return sp.diff(G[a][b][d],X[c])-sp.diff(G[a][b][c],X[d])
def Riem_d(a,b,c,d): return sum(eta[a,e]*Rup(e,b,c,d) for e in range(4))
bad=[(a,b,c,d) for a in range(4) for b in range(4) for c in range(4) for d in range(4) if sp.expand(Riem_s(a,b,c,d)-Riem_d(a,b,c,d))!=0]
print("Riemann lineaire : schema du script = derivation directe :", not bad, bad[:3])
# --- Ricci, R, Schouten, Weyl avec le schema du script, pour h quelconque
def curv(hm):
    def dd2(a,b,c,d): return D(hm[a,b],c,d)
    Rm={(a,b,c,d):sp.Rational(1,2)*(dd2(a,d,b,c)+dd2(b,c,a,d)-dd2(b,d,a,c)-dd2(a,c,b,d)) for a in range(4) for b in range(4) for c in range(4) for d in range(4)}
    Ric={(b,d):sum(Rm[(a,b,a,d)]*eta[a,a] for a in range(4)) for b in range(4) for d in range(4)}
    Rs=sum(Ric[(b,b)]*eta[b,b] for b in range(4))
    L={(a,b):(Ric[(a,b)]-Rs*eta[a,b]/6)/2 for a in range(4) for b in range(4)}
    C={(a,b,c,d):Rm[(a,b,c,d)]-(L[(b,d)]*eta[a,c]-L[(b,c)]*eta[a,d]+L[(a,c)]*eta[b,d]-L[(a,d)]*eta[b,c]) for a in range(4) for b in range(4) for c in range(4) for d in range(4)}
    return Rm,Ric,Rs,L,C
sig=sp.Function('sigma')(*X)
Rm,Ric,Rs,L,C=curv(2*sig*eta)
box=sum(eta[a,a]*sp.diff(sig,X[a],2) for a in range(4))
print("h = 2 sigma eta : C = 0 :", all(sp.expand(v)==0 for v in C.values()))
print("                  L_ab = -d_a d_b sigma :", all(sp.expand(L[(a,b)]+D(sig,a,b))==0 for a in range(4) for b in range(4)))
print("                  R = -6 box sigma :", sp.expand(Rs+6*box)==0)
Rm,Ric,Rs,L,C=curv(h)
print("h generique : Weyl sans trace :", all(sp.expand(sum(eta[a,a]*C[(a,b,a,d)] for a in range(4)))==0 for b in range(4) for d in range(4)))
print("              symetries de C (antisym ab, cd ; paires) :", all(sp.expand(C[(a,b,c,d)]+C[(b,a,c,d)])==0 and sp.expand(C[(a,b,c,d)]-C[(c,d,a,b)])==0 for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
# Bianchi algebrique
print("              Bianchi cyclique :", all(sp.expand(Rm[(a,b,c,d)]+Rm[(a,c,d,b)]+Rm[(a,d,b,c)])==0 for a in range(4) for b in range(4) for c in range(4) for d in range(4)))
# formules de RB-2 en jauge longitudinale, secteur e^{iqx} (q selon x)
t=X[0]; q=sp.Symbol('q',positive=True); Phi=sp.Function('Phi')(t); Psi=sp.Function('Psi')(t)
E=sp.exp(sp.I*q*X[1])
hl=sp.diag(-2*Phi,-2*Psi,-2*Psi,-2*Psi)*E
Rm,Ric,Rs,L,C=curv(hl)
print("jauge longitudinale : R = 2q^2 Phi - 4 q^2 Psi - 6 Psi'' :", sp.simplify(Rs/E-(2*q**2*Phi-4*q**2*Psi-6*sp.diff(Psi,t,2)))==0)
print("                      L_00 = Psi'' - (q^2/3)(Phi+Psi) :", sp.simplify(L[(0,0)]/E-(sp.diff(Psi,t,2)-q**2/3*(Phi+Psi)))==0)
print("                      L_11 =", sp.simplify(L[(1,1)]/E), "; L_22 =", sp.simplify(L[(2,2)]/E))
