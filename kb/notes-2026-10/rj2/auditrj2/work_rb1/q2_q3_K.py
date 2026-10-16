# Q2/Q3 : matrice de Fuchs K, valeurs propres, partie 1/Omega de T_c, termes croises de psibar psi
import sympy as sp
from conv import gu, gl, eta, E4, I, g0, dbar

n = sp.symbols('n0:4', real=True)          # n_a = nabla_a Omega (indice bas), composantes de repere quelconques
m = sp.Symbol('m', positive=True)
ns = sum((gu[a]*n[a] for a in range(4)), sp.zeros(4))      # n-slash = gamma^a n_a
nn = sum(eta[a, a]*n[a]**2 for a in range(4))                # n.n = eta^{ab} n_a n_b
print("nslash^2 = -(n.n) Id :", sp.simplify(ns*ns + nn*E4) == sp.zeros(4))
# equation conforme : i gamma^a nabla_a psi - (m/Omega) psi = 0 ; avec nabla_a psi = (n_a/Omega) K psi + reg :
# ordre 1/Omega : (i nslash K - m) psi = 0 pour tout P  =>  K = -i m nslash^{-1} = i m nslash/(n.n)
K = I*m*ns/nn
print("i nslash K - m = 0 :", sp.simplify(I*ns*K - m*E4) == sp.zeros(4))
print("K^2 =", sp.simplify((K*K)[0, 0]), "* Id ; K^2 diagonal scalaire :", sp.simplify(K*K - (K*K)[0, 0]*E4) == sp.zeros(4))
# valeurs propres pour n de genre temps : n.n = -N^2
Nn = sp.Symbol('N', positive=True)
print("  => valeurs propres de K : +/- sqrt(m^2/(n.n)) = +/- i m / sqrt(-n.n)")
# adjoint de Dirac de K
Kb = sp.simplify(dbar(K))
print("Kbar = gamma^0 K^dag gamma^0 = -K :", sp.simplify(Kb + K) == sp.zeros(4))
# spineur generique
a = sp.symbols('a0:4', real=True); b = sp.symbols('b0:4', real=True)
psi = sp.Matrix([a[i] + I*b[i] for i in range(4)])
pb = psi.H*g0
pbp = sp.expand((pb*psi)[0, 0])
# partie 1/Omega de T_c : T_ab = -(i/2) sym[ psibar gamma_a nabla_b psi - nabla_a psibar gamma_b psi ]
T1 = sp.zeros(4)
for A_ in range(4):
    for B_ in range(4):
        v = (pb*gl[A_]*n[B_]*K*psi + pb*gl[B_]*n[A_]*K*psi - n[A_]*pb*Kb*gl[B_]*psi - n[B_]*pb*Kb*gl[A_]*psi)[0, 0]
        T1[A_, B_] = sp.expand(-I/4*v)
coef = sp.Symbol('C')
R = sp.simplify(T1 - (-m/nn)*sp.Matrix(4, 4, lambda A_, B_: n[A_]*n[B_])*pbp)
print("Omega * T_c|_{1/Omega} = (m/(-n.n)) psibar psi n_a n_b  (identite exacte) :", R == sp.zeros(4))
print("  verification n.n=-1 : coefficient = m psibar psi ; trace(-m psibar psi) coherente avec T^ = -m psibar psi")
# Q3 : sous-espaces propres de K pour n de genre temps : P_pm = (1 pm nslash/N)/2, N = sqrt(-n.n)
Nsym = sp.sqrt(-nn)
Pp = (E4 + ns/Nsym)/2; Pm = (E4 - ns/Nsym)/2
print("P+ P- = 0, P+ + P- = 1 :", sp.simplify(Pp*Pm) == sp.zeros(4), sp.simplify(Pp + Pm - E4) == sp.zeros(4))
print("K P+ = (i m/N)... : K P+ - (-i m/N) P+ = 0 :", sp.simplify(K*Pp - (-I*m/Nsym)*Pp) == sp.zeros(4),
      "; K P- - (+i m/N) P- = 0 :", sp.simplify(K*Pm - (I*m/Nsym)*Pm) == sp.zeros(4))
print("adjoints de Dirac : bar(P+) = P+ :", sp.simplify(dbar(Pp) - Pp) == sp.zeros(4))
cross = sp.simplify(dbar(Pp)*Pm)
print("croise psibar_+ psi_- = psibar Pbar_+ P_- psi = 0 identiquement :", cross == sp.zeros(4))
# mais les termes croises d'autres bilineaires ne s'annulent pas :
crossv = [sp.simplify(dbar(Pp)*gu[c_]*Pm) != sp.zeros(4) for c_ in range(4)]
print("termes croises de psibar gamma^c psi (P+ gamma^c P-) non nuls pour c=0..3 :", crossv)
# cas de Sitter : n_a = (-1,0,0,0)
sub = {n[0]: -1, n[1]: 0, n[2]: 0, n[3]: 0}
print("de Sitter (n_a = d_a Omega = (-1,0,0,0)) : K =", sp.simplify(K.subs(sub)) == I*m*g0, "(K = i m gamma^0)")
print("   P+ (valeur propre -i m) =", sp.simplify(Pp.subs(sub)) == (E4 - g0)/2, " ; donc Omega^{+i mu} <-> gamma^0=+1 :",
      sp.simplify((K.subs(sub))*(E4 + g0)/2 - I*m*(E4 + g0)/2) == sp.zeros(4))
