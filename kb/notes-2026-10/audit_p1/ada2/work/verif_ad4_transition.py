# ad-4 : B = (d^2+k^2)^2 [S u0] avec S transition C^inf en e^{-1/t} sur [-6, -4] ; k = 1, mode A.
# (1) B symbolique exact (sympy) evalue en multiprecision vs differences finies imbriquees (methode du script).
# (2) R(tau) = Int_{-6}^{-4} K(tau - tau') B(tau') dtau' avec le B exact, quadrature a haute precision, et
#     par une seconde methode (integration par parties : derivees reportees sur le noyau, avec termes de bord).
# (3) Lissite en tau = 0 : derivees numeriques de R, et controle R(0) par les deux methodes.
import sympy as sp
from mpmath import mp, mpf, quad, cos, sin, exp, diff as mdiff, nstr, ci, si, pi

t = sp.symbols('tau', real=True)
k = 1
tau0, delta = -6, 2
s = (t - tau0)/sp.Integer(delta)
S = sp.exp(-1/s)/(sp.exp(-1/s) + sp.exp(-1/(1-s)))
u0 = sp.cos(k*t) + k*t*sp.sin(k*t)
P2 = lambda f: sp.diff(f, t, 2) + k**2*f
Su = S*u0
B_sym = P2(P2(Su))
mp.dps = 30
fB = sp.lambdify(t, B_sym, 'mpmath')
fSu = sp.lambdify(t, Su, 'mpmath')
fSu1 = sp.lambdify(t, sp.diff(Su, t), 'mpmath')
fSu2 = sp.lambdify(t, sp.diff(Su, t, 2), 'mpmath')
fSu3 = sp.lambdify(t, sp.diff(Su, t, 3), 'mpmath')

def B_exact(tv):
    tv = mpf(tv)
    if tv <= tau0 or tv >= tau0 + delta:
        return mpf(0)
    return fB(tv)

# methode du script (differences finies imbriquees, dps 15)
def S_num(tt):
    if tt <= tau0: return mpf(0)
    if tt >= tau0 + delta: return mpf(1)
    ss = (tt - tau0)/delta
    f1 = exp(-1/ss); f2 = exp(-1/(1-ss))
    return f1/(f1+f2)
def uA_num(tt): return cos(tt) + tt*sin(tt)
def B_fd(tt, dps=15):
    with mp.workdps(dps):
        fsu = lambda s_: S_num(s_)*uA_num(s_)
        d2 = lambda s_: mdiff(fsu, s_, 2) + fsu(s_)
        return mdiff(d2, tt, 2) + d2(tt)

print("(1) B aux 7 points du script : exact (sympy, 30 chiffres) vs differences finies imbriquees (dps 15) vs mdiff ordre 4 direct")
pts = [mpf(tau0) + mpf(delta)*mpf(i)/8 for i in range(1, 8)]
for p in pts:
    be = B_exact(p)
    bf = B_fd(p)
    with mp.workdps(30):
        # derivee 4e directe de S u (une seule differentiation numerique, haute precision)
        f4 = mdiff(lambda s_: S_num(s_)*uA_num(s_), p, 4) + 2*mdiff(lambda s_: S_num(s_)*uA_num(s_), p, 2) + S_num(p)*uA_num(p)
    print(f"  tau = {nstr(p,5)} : exact = {nstr(be, 12)} ; FD script = {nstr(bf, 12)} ; ecart rel = {nstr(abs(bf-be)/abs(be), 3)} ; mdiff ordre 4 (dps30) = {nstr(f4, 12)}")

# Points supplementaires proches des bords (ou e^{-1/s} rend tout plat)
print("  Bords :")
for p in (mpf('-5.95'), mpf('-5.9'), mpf('-4.1'), mpf('-4.05')):
    print(f"  tau = {p} : exact = {nstr(B_exact(p), 10)} ; FD script = {nstr(B_fd(p), 10)}")

# Controle integral : Int_{-6}^{-4} B dtau = [ (Su)''' + 2 (Su)' ]_{-6}^{-4} + Int Su dtau
print("(2) Controle integral de B exact")
IB = quad(B_exact, [tau0, -5.5, -5, -4.5, tau0 + delta])
bord = fSu3(mpf(-4) - mpf('1e-25')) + 2*fSu1(mpf(-4) - mpf('1e-25'))
# en -4 : S = 1 a tous ordres, donc (Su)''' = u0''' etc.
u0n = lambda tt: cos(tt) + tt*sin(tt)
u0_1 = lambda tt: tt*cos(tt)
u0_3 = lambda tt: -2*sin(tt) - tt*cos(tt)   # u0''' : u0'' = cos - t sin ; u0''' = -2 sin - t cos
ISu = quad(lambda tt: fSu(tt), [tau0, -5.5, -5, -4.5, tau0 + delta])
print(f"  Int B = {nstr(IB, 15)} ; u0'''(-4) + 2 u0'(-4) + Int S u0 = {nstr(u0_3(mpf(-4)) + 2*u0_1(mpf(-4)) + ISu, 15)}")

# (3) R(tau), methode directe avec B exact, haute precision, intervalle decoupe
def K(T): return -2*cos(T)/T
def R_direct(tv, dps=30):
    with mp.workdps(dps):
        return quad(lambda tp: K(tv - tp)*B_exact(tp), [tau0, -5.75, -5.5, -5.25, -5, -4.75, -4.5, -4.25, tau0 + delta])

# methode 2 : integration par parties. R = Int K(tau-tau') (d^2+1)^2 (Su)(tau') dtau'.
# (d^2+1)^2 (Su) = (Su)'''' + 2 (Su)'' + Su. On reporte les derivees sur K (en tau'), avec les termes de bord en -4 (en -6 tout est nul).
# Int_a^b K g'''' = [K g''' - K' g'' + K'' g' - K''' g]_a^b + Int K'''' g ; Int K g'' = [K g' - K' g]_a^b + Int K'' g.
def R_parts(tv, dps=30):
    with mp.workdps(dps):
        Kf = lambda tp: -2*cos(tv - tp)/(tv - tp)
        K1 = lambda tp: mdiff(Kf, tp, 1); K2 = lambda tp: mdiff(Kf, tp, 2); K3 = lambda tp: mdiff(Kf, tp, 3); K4 = lambda tp: mdiff(Kf, tp, 4)
        b = mpf(-4)
        g0, g1, g2, g3 = u0n(b), u0_1(b), cos(b) - b*sin(b), u0_3(b)
        bord = (Kf(b)*g3 - K1(b)*g2 + K2(b)*g1 - K3(b)*g0) + 2*(Kf(b)*g1 - K1(b)*g0)
        integ = quad(lambda tp: (K4(tp) + 2*K2(tp) + Kf(tp))*fSu(tp), [tau0, -5.5, -5, -4.5, tau0 + delta])
        return bord + integ

print("(3) R(tau) : script (FD) vs direct (B exact) vs integration par parties")
for tv in (mpf(-2), mpf(-1), mpf('-0.5'), mpf('-0.1'), mpf('-0.01'), mpf(0), mpf('0.5'), mpf(1)):
    rd = R_direct(tv); rp = R_parts(tv)
    print(f"  tau = {tv} : R direct = {nstr(rd, 14)} ; par parties = {nstr(rp, 14)} ; ecart = {nstr(rd - rp, 3)}")

print("(4) Derivees de R en tau = 0 (lissite) : R^(n)(tau) = Int K^(n)(tau - tau') B(tau') dtau', K^(n) symbolique")
Ts = sp.symbols('T', real=True)
Ksym = -2*sp.cos(Ts)/Ts
for n in (1, 2, 3, 4):
    Kn = sp.lambdify(Ts, sp.diff(Ksym, Ts, n), 'mpmath')
    val = quad(lambda tp: Kn(mpf(0) - tp)*B_exact(tp), [tau0, -5.75, -5.5, -5.25, -5, -4.75, -4.5, -4.25, tau0 + delta])
    print(f"  R^({n})(0) = {nstr(val, 12)}")
# controle par difference finie centree grossiere sur R_direct : (R(h)-R(-h))/2h, h = 1e-3
h = mpf('1e-3')
print("  controle (R(h)-R(-h))/(2h), h=1e-3 :", nstr((R_direct(h) - R_direct(-h))/(2*h), 10))
print("  s^2 R(-s) = R(0) s^2 - R'(0) s^3 + ... : aucun terme s^0 ni s^1 par construction (R bornee), R(0) =", nstr(R_direct(mpf(0)), 12))
