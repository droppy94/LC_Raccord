# iraa_aniso_v2.py (v1 conservee : controle numerique aa-2 defectueux, quad non oscillante) -- IR-aa (NOTE-157) : partie sans trace de T^w pour un etat homogene ANISOTROPE
# du scalaire conforme (xi = 1/6) sur Minkowski (repere plat), ordre zero en eps.
# Signature -+++ ; eta = temps conforme ; scri+ = {eta = 0} ; eon = {eta < 0}.
import sympy as sp
from mpmath import mp, quad, mpf, sin, cos, exp, pi as mpi

eta, etap = sp.symbols('eta etap', real=True)
x1,x2,x3,y1,y2,y3 = sp.symbols('x1 x2 x3 y1 y2 y3', real=True)
k = sp.symbols('k', positive=True)
th, ph = sp.symbols('theta phi', real=True)
X = [eta,x1,x2,x3]; Y = [etap,y1,y2,y3]
g = sp.diag(-1,1,1,1)

# ---------- aa-1 : tenseur ameliore par point-splitting sur un mode ----------
# Fonction a deux points d'un etat de Bogoliubov homogene : pour chaque k-vecteur,
#   w_k(x,x') = |alpha|^2 e^{-ik(eta-eta')} + |beta|^2 e^{+ik(eta-eta')}
#             + alpha beta* e^{-ik(eta+eta')} + alpha* beta e^{+ik(eta+eta')}   (x) e^{i k.(x-x')} / (2k (2pi)^3)
# Le terme d'etat w = omega_2 - H retire la partie du vide (|alpha|^2 -> |alpha|^2 - 1 = |beta|^2).
# On traite separement les trois structures de phase : P1 = e^{-ik(eta-eta')} (vide, soustrait), P2 = e^{ik(eta-eta')} (|beta|^2), P3 = e^{-ik(eta+eta')} (alpha beta*).
# T_{mu nu} = D_{mu nu} w |coincidence, avec D l'operateur bilineaire du tenseur ameliore :
#   T_{mu nu} = d_mu phi d_nu phi - 1/2 g (d phi)^2 - xi (d_mu d_nu - g box)(phi^2), xi = 1/6, phi^2 -> w|coinc.
xi = sp.Rational(1,6)
kv = sp.Matrix([k*sp.sin(th)*sp.cos(ph), k*sp.sin(th)*sp.sin(ph), k*sp.cos(th)])
kx = kv[0]*(x1-y1)+kv[1]*(x2-y2)+kv[2]*(x3-y3)

def T_from_bimode(wfun):
    """wfun(x,y) symbolique ; renvoie T_{mu nu} a la coincidence x=y (sans le facteur 1/(2k(2pi)^3))."""
    sub = {etap:eta, y1:x1, y2:x2, y3:x3}
    T = sp.zeros(4,4)
    # (d_mu phi d_nu phi) -> sym_{mu nu} d_mu^x d_nu^y w
    for m in range(4):
        for n in range(4):
            T[m,n] = sp.Rational(1,2)*(sp.diff(wfun, X[m], Y[n]) + sp.diff(wfun, X[n], Y[m]))
    # - 1/2 g (d phi)^2
    dd = sum(g[a,a]*sp.diff(wfun, X[a], Y[a]) for a in range(4))
    T = T - sp.Rational(1,2)*g*dd
    # - xi (d_mu d_nu - g box) phi^2, phi^2 = w|coinc
    w0 = wfun.subs(sub)
    for m in range(4):
        for n in range(4):
            T[m,n] = T[m,n] - xi*sp.diff(w0, X[m], X[n])
    box = sum(g[a,a]*sp.diff(w0, X[a], X[a]) for a in range(4))
    T = T + xi*g*box
    return sp.simplify(T.subs(sub))

P2 = sp.exp(sp.I*k*(eta-etap))*sp.exp(sp.I*kx)    # |beta|^2
P3 = sp.exp(-sp.I*k*(eta+etap))*sp.exp(sp.I*kx)   # alpha beta*
T2 = T_from_bimode(P2); T3 = T_from_bimode(P3)
print("== aa-1 : structures tensorielles par mode (facteur 1/(2k(2pi)^3) omis) ==")
print("terme |beta|^2 (phase e^{ik(eta-eta')}) :"); sp.pprint(sp.simplify(T2))
print("terme alpha beta* (phase e^{-ik(eta+eta')}) :"); sp.pprint(sp.simplify(T3))
tr2 = sp.simplify(sum(g[a,a]*T2[a,a] for a in range(4))); tr3 = sp.simplify(sum(g[a,a]*T3[a,a] for a in range(4)))
print("traces (doivent etre 0, xi = 1/6) :", tr2, tr3)

# Decomposition spatiale du terme alpha beta* : T_ij = A k_i k_j + B delta_ij  (A, B en e^{-2ik eta})
Tij3 = T3[1:,1:]
A = sp.simplify(Tij3[0,1]/(kv[0]*kv[1]))
B = sp.simplify(Tij3[0,0] - A*kv[0]**2)
print("alpha beta* : T_ij = A k_i k_j + B delta_ij avec A =", A, " B =", B)
print("  trace spatiale A k^2 + 3B =", sp.simplify(A*k**2+3*B), " ; T_00 =", sp.simplify(T3[0,0]), " ; T_0i =", [sp.simplify(T3[0,i]) for i in (1,2,3)])
print("  partie sans trace = A (k_i k_j - k^2 delta_ij/3) ; moyenne angulaire isotrope => 0 (YA-2 retrouve) ; partie isotrope : A k^2/3 + B =", sp.simplify(A*k**2/3+B))
Tij2 = T2[1:,1:]
A2 = sp.simplify(Tij2[0,1]/(kv[0]*kv[1])); B2 = sp.simplify(Tij2[0,0]-A2*kv[0]**2)
print("|beta|^2 : A =", A2, " B =", B2, " T_00 =", sp.simplify(T2[0,0]), " (independant de eta)")

# ---------- aa-2 : comportement en eta -> 0 de la partie sans trace pour alpha beta* = k^-N Y_2(k^) e^{i phi} ----------
# T_ij^tf(eta) = Int d^3k /(2k (2pi)^3) * 2 Re[ A(k,eta) alpha beta*(k) ] (k_i k_j - k^2/3 delta_ij)
#             avec A proportionnel a e^{-2 i k eta} (coefficient ci-dessus) ; angulaire : Y_2 -> tenseur constant Q_ij.
# radial : Int dk k^2/(2k) * k^2 * k^{-N} * Re[c e^{-2ik eta}]  = Int dk k^{3-N} Re[c e^{-2 i k eta}]
N, m = sp.symbols('N m', positive=True)
print("\n== aa-2 : integrale radiale I(eta) = Int_0^inf dk k^{3-N} e^{-2 i k eta} (eta<0) ==")
print("  I(eta) = Gamma(4-N) (2 i eta)^{N-4}  pour N<4 (analytique) : module ~ |eta|^{N-4} ; N=3 : 1/(2 i eta) -> 1/eta ; N=4 : log ; N>=5 : coupure IR")
mp.dps = 20
print("  controle numerique N=3 (coupure e^{-k/1000}) : eta * Int dk sin(2 k eta) e^{-k/1000} ->")
from mpmath import quadosc
a = mpf(1)/1000
for e in (-0.1,-0.05,-0.02):
    ee = mpf(e)
    val = quadosc(lambda kk: sin(2*kk*ee)*exp(-a*kk), [0, mp.inf], omega=2*abs(ee))
    exact = 2*ee/(a**2+4*ee**2)
    print("    eta =", e, " eta*I (quadosc) =", ee*val, " forme fermee 2 eta/(a^2+4 eta^2) * eta =", ee*exact, " (attendu -1/2)")
# decroissance rapide : alpha beta* = e^{-k^2/L^2} : I(eta) entiere en eta
L = sp.symbols('L', positive=True)
I_gauss = sp.integrate(k**3*sp.exp(-k**2/L**2)*sp.exp(-2*sp.I*k*eta), (k,0,sp.oo))
print("  decroissance gaussienne : I(eta) =", sp.simplify(I_gauss), " -> entiere en eta (erf, exp)")

# ---------- aa-3 : terme alpha beta* = structure de charge image, anisotropie comprise ----------
print("\n== aa-3 : alpha beta* = f(k^) (independant de k) : w_{ab*}(x,x') = Int d^3k/(2k(2pi)^3) f(k^) e^{-ik(eta+eta')} e^{ik.(x-x')} ==")
print("  = [operateur angulaire f(-i grad / |grad|) ] applique a G_M(x, R x'), R x' = (-eta', x') : support singulier sur (eta+eta')^2 = |x-x'|^2 (cone reflechi)")
print("  Un multiplicateur de Fourier homogene de degre 0 (f(k^)) est un operateur pseudo-differentiel d'ordre 0 : il preserve le front d'onde (singularite sur le cone reflechi conservee).")
print("  Hadamard ssi alpha beta* a decroissance rapide dans TOUTES les directions (critere de NOTE-146 v2 y-2 inchange).")

# ---------- aa-4 : comptage ----------
print("\n== aa-4 : T-hat = s^2 T_plat ; T_plat^tf ~ |eta|^{N-4} Q_ij => T-hat ~ s^{N-2} Q_ij ; pole dans (2.17) ssi N = 3 (ordre eps^0, independant de l'onde) ==")
print("  etat Hadamard (rapide) : T_plat^tf entier en eta => T-hat ~ s^2 : rien.")
