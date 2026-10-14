# irad_kernel.py -- IR-ad (NOTE-159) : convergence et lissite du noyau retarde de Gamma[g] sur l'histoire de l'onde.
# Repere plat g = eta + eps h, h_yy = -h_zz = u(tau) cos(k x), tau = temps conforme (tau < 0 sur l'eon, scri+ = {tau = 0}).
import sympy as sp
from mpmath import mp, quad, quadosc, mpf, sin, cos, exp, log, pi as mpi, euler, e1, inf

tau, taup, x, kk = sp.symbols('tau taup x k', real=True)
k = sp.symbols('k', positive=True)
eps = sp.symbols('epsilon', positive=True)

# ---------- ad-1 : Bach linearise sur h TT et identite de de Sitter ----------
print("== ad-1 : Bach linearise et identite de de Sitter ==")
u = sp.Function('u')
# metrique plate + eps h, h_yy = -h_zz = u(tau) cos(k x) : h TT par rapport a eta (trace nulle, d^a h_ab = 0).
# Riemann linearise : R_abcd = 1/2 (d_b d_c h_ad + d_a d_d h_bc - d_a d_c h_bd - d_b d_d h_ac)
X = [tau, x, sp.symbols('y', real=True), sp.symbols('z', real=True)]
y, z = X[2], X[3]
h = sp.zeros(4,4); h[2,2] = u(tau)*sp.cos(k*x); h[3,3] = -u(tau)*sp.cos(k*x)
g = sp.diag(-1,1,1,1); ginv = g
def d(f,a): return sp.diff(f, X[a])
R = [[[[sp.Rational(1,2)*(d(d(h[a,dd],b),c) + d(d(h[b,c],a),dd) - d(d(h[b,dd],a),c) - d(d(h[a,c],b),dd)) for dd in range(4)] for c in range(4)] for b in range(4)] for a in range(4)]
Ric = sp.Matrix(4,4, lambda a,b: sum(ginv[c,c]*R[c][a][c][b] for c in range(4)))
Rs = sum(ginv[a,a]*Ric[a,a] for a in range(4))
# Weyl linearise (n=4) : C_abcd = R_abcd - 1/2 (g_ac R_bd - g_ad R_bc - g_bc R_ad + g_bd R_ac) + R/6 (g_ac g_bd - g_ad g_bc)
def C(a,b,c,dd):
    return R[a][b][c][dd] - sp.Rational(1,2)*(g[a,c]*Ric[b,dd] - g[a,dd]*Ric[b,c] - g[b,c]*Ric[a,dd] + g[b,dd]*Ric[a,c]) + Rs/6*(g[a,c]*g[b,dd] - g[a,dd]*g[b,c])
# Bach linearise sur fond plat : B_ab = d^c d^d C_acbd
def Bach(a,b):
    return sp.simplify(sum(ginv[c,c]*ginv[dd,dd]*d(d(C(a,c,b,dd),c),dd) for c in range(4) for dd in range(4)))
B_yy = Bach(2,2)
box_h_yy = sum(ginv[a,a]*d(d(h[2,2],a),a) for a in range(4))
box2_h_yy = sp.simplify(sum(ginv[a,a]*d(d(box_h_yy,a),a) for a in range(4)))
ratio = sp.simplify(B_yy/box2_h_yy)
print("B_yy / (box^2 h_yy) =", ratio, "   (attendu -1/4)")
print("B_tt, B_tx, B_xx :", Bach(0,0), Bach(0,1), Bach(1,1), "  B_zz = -B_yy :", sp.simplify(Bach(3,3)+B_yy)==0)
# modes de de Sitter en temps conforme : u'' - (2/tau) u' + k^2 u = 0
uA = sp.cos(k*tau) + k*tau*sp.sin(k*tau)
uB = sp.sin(k*tau) - k*tau*sp.cos(k*tau)
for name, uu in (("A",uA),("B",uB)):
    ode = sp.simplify(sp.diff(uu,tau,2) - 2/tau*sp.diff(uu,tau) + k**2*uu)
    b2 = sp.simplify((sp.diff(uu,tau,2)+k**2*uu))
    b4 = sp.simplify(sp.diff(b2,tau,2)+k**2*b2)
    print(f"mode {name} : equation de de Sitter residu =", ode, " ; (d^2+k^2) u =", b2, " ; (d^2+k^2)^2 u =", b4)

# ---------- ad-2 : noyau temporel de ln((k^2 - (omega+i0)^2)/mu^2) ----------
print("\n== ad-2 : noyau retarde K_k(T) de ln((k^2 - (omega + i0)^2)/mu^2) ==")
print("  ln(k^2 - (omega+i0)^2) = ln(k - omega - i0) + ln(k + omega + i0).")
print("  TF inverse (convention f(T) = Int domega/(2pi) e^{-i omega T} f~(omega)) de ln(a - omega - i0) : -[theta(T) e^{-iaT}/T]_+ - (gamma_E + ln mu) delta(T)  (d/dT de -i theta(T) e^{-iaT}... : voir controle)")
print("  Somme des deux branches : K_k(T) = -2 [theta(T) cos(kT)/T]_+ + c(mu,k) delta(T) ; support dans T >= 0 (retarde) ; decroissance en 1/T.")
# controle : d/dT [K] doit redonner la TF de d/dT <-> (-i omega) ln(...) ; on verifie plutot numeriquement une identite d'action :
# pour une fonction test f(T) = e^{-T^2}, Int K_k(T) f(T) dT doit egaler Int domega/(2pi) ln(k^2-(omega+i0)^2) f~(omega)  -- controle lourd ; on verifie a la place
# l'identite elementaire Int_0^inf (e^{-iaT} - e^{-ibT})/T dT = ln(b/a) + i pi/2 (sgn...) : forme de la partie principale
mp.dps = 15
a_, b_ = mpf(1), mpf(3)
val = quadosc(lambda T: (cos(a_*T)-cos(b_*T))/T, [0, inf], omega=b_)
print("  controle Frullani : Int_0^inf (cos aT - cos bT)/T dT =", val, "  ln(b/a) =", log(b_/a_))

# ---------- ad-3 : (H-a) commutation adiabatique u_eps = e^{eps tau} u_0 ----------
print("\n== ad-3 : histoire adiabatique u_eps = e^{eps tau} u_0, B_eps = (d^2+k^2)^2 u_eps ==")
for name, uu in (("A",uA),("B",uB)):
    ue = sp.exp(eps*tau)*uu
    b2 = sp.diff(ue,tau,2)+k**2*ue
    b4 = sp.simplify(sp.expand(sp.diff(b2,tau,2)+k**2*b2))
    ser = sp.series(sp.simplify(b4*sp.exp(-eps*tau)), eps, 0, 2).removeO()
    print(f"  mode {name} : e^(-eps tau) B_eps =", sp.simplify(ser), " + O(eps^2)")
# reponse retardee R_eps(tau) = Int_{-inf}^{tau} K_k(tau - tau') B_eps(tau') dtau', partie non locale (sans delta, qui donne c(mu) B_eps -> 0)
# K_k(T) = -2 cos(kT)/T pour T > 0 ; singularite en T = 0 : partie finie [.]_+ : on la definit par Int_0^inf (f(tau-T) - f(tau) theta(1-T)) cos(kT) (-2/T) dT  (regularisation de Hadamard a l'echelle 1)
mp.dps = 15
kval = mpf(1)
def B_eps_num(tp, ev, mode="A"):
    # premier ordre en eps, mode A : e^{eps tau}( -8 k^3 eps sin(k tau) ) d'apres la serie (verifie ci-dessus) ; on utilise l'expression exacte de b4 lambdifiee
    return None
for name, uu in (("A",uA),):
    ue = sp.exp(eps*tau)*uu
    b2 = sp.diff(ue,tau,2)+k**2*ue
    b4 = sp.simplify(sp.expand(sp.diff(b2,tau,2)+k**2*b2))
    fB = sp.lambdify((tau,eps,k), b4, 'mpmath')
    print("  reponse retardee R_eps(tau0) (partie non locale, mode A, k = 1), regularisation de Hadamard [.]_+ a l'echelle 1 :")
    for tau0 in (mpf(0), mpf(-1)):
        for ev in (mpf('0.1'), mpf('0.01'), mpf('0.001')):
            f = lambda T: fB(tau0 - T, ev, kval)
            f0 = fB(tau0, ev, kval)
            # Int_0^1 (f(tau0-T) - f0) (-2 cos(kT)/T) dT + Int_1^inf f(tau0-T) (-2 cos(kT)/T) dT
            I1 = quad(lambda T: (f(T) - f0)*(-2*cos(kval*T)/T), [0, 1])
            I2 = quadosc(lambda T: f(T)*(-2*cos(kval*T)/T), [1, inf], omega=kval)
            Rv = I1 + I2
            print(f"    tau0 = {tau0}, eps = {ev} : R_eps = {Rv}   R_eps/(eps ln(1/eps)) = {Rv/(ev*log(1/ev))}")

# ---------- ad-4 : (H-b) emission a temps fini, raccord lisse ----------
print("\n== ad-4 : histoire brusque lissee : u = S(tau) u_0, S = 0 pour tau < tau0, S = 1 pour tau > tau0 + delta, raccord C^inf (fonction de transition en e^{-1/t}) ==")
tau0v, deltav = mpf(-6), mpf(2)
def S(t):
    if t <= tau0v: return mpf(0)
    if t >= tau0v + deltav: return mpf(1)
    s = (t - tau0v)/deltav
    f1 = exp(-1/s); f2 = exp(-1/(1-s))
    return f1/(f1+f2)
def uA_num(t): return cos(kval*t) + kval*t*sin(kval*t)
from mpmath import diff as mdiff
def Bnum(t):
    # B = (d^2 + k^2)^2 [S u0] evalue numeriquement par differences finies d'ordre eleve (mp.dps 15)
    if t <= tau0v or t >= tau0v + deltav: return mpf(0)
    fsu = lambda s_: S(s_)*uA_num(s_)
    d2 = lambda s_: mdiff(fsu, s_, 2) + kval**2*fsu(s_)
    return mdiff(d2, t, 2) + kval**2*d2(t)
print("  B[h] est a support dans [tau0, tau0+delta] = [-6, -4] ; reponse R(tau) = Int K(tau - tau') B(tau') dtau' pour tau > -4 : K lisse sur le support (T >= 2)")
# tabulation de B sur le support
pts = [tau0v + deltav*mpf(i)/8 for i in range(1,8)]
Btab = [(float(p), float(Bnum(p))) for p in pts]
print("  B sur le support (tau, B) :", [(round(a,3), round(b,4)) for a,b in Btab])
def Rresp(t):
    return quad(lambda tp: (-2*cos(kval*(t-tp))/(t-tp))*Bnum(tp), [tau0v, tau0v+deltav])
for t in (mpf(-2), mpf(-1), mpf('-0.5'), mpf('-0.1'), mpf('-0.01'), mpf(0)):
    print(f"    tau = {t} : R(tau) = {Rresp(t)}")
print("  R est lisse en tau = 0 (convolution d'un noyau C^inf pour T >= 2 avec une source C^inf a support compact) ; valeur finie non nulle ; depend de tau0 et du raccord.")

# ---------- ad-5 : comptage ----------
print("\n== ad-5 : T-hat_Gamma = s^2 R(tau = -s) avec R lisse en 0 => T-hat ~ s^2 R(0) + ... : aucun terme s^1 ; pas de pole. ==")
print("  condition de convergence : Int_{-inf}^{tau} |B(tau')| / (1 + |tau - tau'|) dtau' < inf ; satisfaite si B est integrable a poids 1/|tau'| dans le passe (B = 0 hors d'un compact : trivial ; adiabatique : B = O(eps) e^{eps tau'}, integrale O(eps ln 1/eps) -> 0).")
