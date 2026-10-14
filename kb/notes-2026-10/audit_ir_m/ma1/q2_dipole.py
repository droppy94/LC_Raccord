# Audit M-a1, question 2 : dipole magnetique eteint, repere conforme plat (c = 1, gaussien).
import sympy as sp, numpy as np, functools, sys
np.seterr(over="ignore")
print = functools.partial(print, flush=True)

# ---------- (a) verification symbolique de Maxwell sans source hors origine
t, x, y, z = sp.symbols('t x y z', real=True)
m0 = sp.symbols('m0', positive=True)
f = sp.Function('f')
r = sp.sqrt(x**2 + y**2 + z**2)
g = m0*f(t - r)/r
# A = rot(zhat g), phi = 0  (jauge de Lorenz : div A = 0 et phi = 0)
A = sp.Matrix([sp.diff(g, y), -sp.diff(g, x), 0])
def curl(V): return sp.Matrix([sp.diff(V[2], y)-sp.diff(V[1], z), sp.diff(V[0], z)-sp.diff(V[2], x), sp.diff(V[1], x)-sp.diff(V[0], y)])
def div(V): return sp.diff(V[0], x)+sp.diff(V[1], y)+sp.diff(V[2], z)
B = curl(A); E = -sp.diff(A, t)
chk = {
 'div B': sp.simplify(div(B)),
 'div E': sp.simplify(div(E)),
 'rot E + dB/dt': sp.simplify(curl(E) + sp.diff(B, t)),
 'rot B - dE/dt': sp.simplify(curl(B) - sp.diff(E, t)),
}
for kk, v in chk.items():
    print('[calcule] (a) %s = %s' % (kk, v))
# forme fermee : B = m0[(3 n nz - z)(f/r^3 + f'/r^2) + (n nz - z) f''/r],  E = -m0 (z x n)(f'/r^2 + f''/r)
n = sp.Matrix([x, y, z])/r; zh = sp.Matrix([0, 0, 1])
tr_ = t - r
F0, F1, F2 = f(tr_), sp.diff(f(t), t, 1).subs(t, tr_), sp.diff(f(t), t, 2).subs(t, tr_)
Bc = m0*((3*n*n[2] - zh)*(F0/r**3 + F1/r**2) + (n*n[2] - zh)*F2/r)
Ec = -m0*zh.cross(n)*(F1/r**2 + F2/r)
print('[calcule] (a) B - forme fermee =', sp.simplify(B - Bc).T, '; E - forme fermee =', sp.simplify(E - Ec).T)

# ---------- (b,c) numerique a t = 0
D = float(sys.argv[1]) if len(sys.argv) > 1 else 40.0
w = float(sys.argv[2]) if len(sys.argv) > 2 else 1.0
M0 = 1.0
def fs(tt):  # marche 1 -> 0 autour de t = -D
    u = (tt + D)/w; return 0.5*(1 - np.tanh(u))
def f1(tt):
    u = (tt + D)/w; return -0.5/w/np.cosh(u)**2
def f2(tt):
    u = (tt + D)/w; return np.tanh(u)/np.cosh(u)**2/w**2

def fields(rv):  # rv : (...,3), t = 0
    rr = np.linalg.norm(rv, axis=-1)[..., None]; nn = rv/rr; tr = -rr
    a0, a1, a2 = fs(tr), f1(tr), f2(tr)
    zz = np.array([0, 0, 1.0]); nz = nn[..., 2:3]
    Bv = M0*((3*nn*nz - zz)*(a0/rr**3 + a1/rr**2) + (nn*nz - zz)*a2/rr)
    Ev = -M0*np.cross(zz, nn)*(a1/rr**2 + a2/rr)
    return Bv, Ev

# quadrature angulaire : Gauss-Legendre en mu x uniforme en phi
mu, wmu = np.polynomial.legendre.leggauss(24)
nph = 24; ph = 2*np.pi*np.arange(nph)/nph
MU, PH = np.meshgrid(mu, ph, indexing='ij'); W = np.outer(wmu, np.ones(nph))/(2*nph)
ST = np.sqrt(1 - MU**2)
NV = np.stack([ST*np.cos(PH), ST*np.sin(PH), MU], -1)

def Qtf_avg(rad):
    Bv, Ev = fields(rad*NV)
    Q = Bv[..., :, None]*Bv[..., None, :] - Ev[..., :, None]*Ev[..., None, :]
    Q = Q - np.eye(3)*np.trace(Q, axis1=-2, axis2=-1)[..., None, None]/3
    return np.einsum('ij,ijab->ab', W, Q)

# analytique (moyenne exacte) : a = 2 al^2/15 - 2 al be/3 + be^2 + S^2/3
def a_analytic(rr):
    tr = -rr; P = fs(tr)/rr**3 + f1(tr)/rr**2; Rr = f2(tr)/rr; S = f1(tr)/rr**2 + f2(tr)/rr
    al, be = 3*P + Rr, P + Rr
    return M0**2*(2*al**2/15 - 2*al*be/3 + be**2 + S**2/3)

# carte locale : quelques points (theta = 0, pi/4, pi/2)
print('\n[calcule] (b) carte de Qtf(x) a t=0, D=%g, w=%g (composantes zz, xx, xz) ; |Qtf| = norme de Frobenius' % (D, w))
for rad in [0.25*D, 0.5*D, D - 6*w, D - 2*w, D, D + 2*w, D + 6*w, 1.5*D, 3*D]:
    row = []
    for th in [0, np.pi/4, np.pi/2]:
        Bv, Ev = fields(rad*np.array([np.sin(th), 0, np.cos(th)]))
        Q = np.outer(Bv, Bv) - np.outer(Ev, Ev); Q -= np.eye(3)*np.trace(Q)/3
        row.append('th=%4.2f: zz=% .3e xz=% .3e |Q|=%.3e' % (th, Q[2, 2], Q[0, 2], np.linalg.norm(Q)))
    print('  r=%7.2f  ' % rad + ' | '.join(row))

# moyenne angulaire : verifie la structure (mhat mhat - 1/3) et compare a l'analytique
print('\n[calcule] (c) moyennes angulaires : <Qtf> = a(r) (zz - 1/3 Id) ; controle structure et analytique')
for rad in [D + 10*w, 2*D, D, D - 0.5*w, D + 0.5*w]:
    Qa = Qtf_avg(rad); a = 1.5*Qa[2, 2]
    struct = np.max(np.abs(Qa - a*(np.diag([0, 0, 1.0]) - np.eye(3)/3)))
    print('  r=%7.2f  a_num=% .6e  a_analytique=% .6e  ecart_structure=%.1e' % (rad, a, a_analytic(rad), struct))
rr = 2*D; print('  statique r=2D : a*r^6/m0^2 = %.6f (attendu 1/5 = 0.2)' % (a_analytic(rr)*rr**6))
# rayonnement pur : a / (m0^2 f''^2 / r^2)
print('  rayonne r=D : a/(m0^2 f\'\'(t_r)^2/r^2) a r=D+w = %.6f (attendu 4/5 a O(w/D))' % (1.5*Qtf_avg(D + w)[2, 2]/(f2(-(D + w))**2/(D + w)**2)))

# integrales radiales par region : J = int a(r) r^2 dr  ;  int d^3x <Qtf> = 4 pi J (mhat mhat - 1/3)
from scipy.integrate import quad
h = 10*w
regs = {'r < D-10w': (1e-3*D, D - h), '|r-D| <= 10w': (D - h, D + h), 'r > D+10w': (D + h, np.inf)}
print('\n[calcule] (c) integrales radiales J = int a(r) r^2 dr (unites m0 = 1)')
Jtot = 0
for kk, (lo, hi) in regs.items():
    J, err = quad(lambda q: a_analytic(q)*q**2, lo, hi, limit=800, points=None if hi == np.inf else [D] if lo < D < hi else None)
    Jtot += J
    print('  %-14s J = %.6e  (err %.1e)' % (kk, J, err))
# controle de la quadrature angulaire contre a_analytic sur la coquille
Jnum = quad(lambda q: 1.5*Qtf_avg(q)[2, 2]*q**2, D - h, D + h, limit=400, points=[D])[0]
print('  coquille, J avec moyenne angulaire numerique = %.6e' % Jnum)
print('[calcule] attendus analytiques :')
print('  statique  r > D+10w : m0^2/(15 (D+10w)^3) = %.6e' % (1/(15*(D + h)**3)))
print('  rayonne   coquille  : (4/5) m0^2 int f\'\'^2 dt = (4/5)(4/15) m0^2/w^3 = 16/(75 w^3) = %.6e' % (16/(75*w**3)))
print('  interieur r < D-10w : ~ exp(-20) x (puissances), nul a precision machine pres pour une marche a support compact')
Jrad_only = quad(lambda q: 0.8*f2(-q)**2, D - h, D + h, points=[D])[0]
print('  controle : (4/5) int f\'\'(t_r)^2 dr sur la coquille = %.6e' % Jrad_only)

# figure
try:
    import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
    R_ = np.linspace(0.05*D, 3*D, 6000)
    A_ = np.array([a_analytic(q) for q in R_])
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.semilogy(R_/D, np.abs(A_)*R_**2 + 1e-300, lw=1.2, color='#2b6cb0')
    ax.axvline(1, color='0.6', ls=':', lw=1)
    ax.set_ylim(1e-14, 1); ax.set_xlabel('r / D'); ax.set_ylabel('|a(r)| r^2  (m0=1)')
    ax.set_title('Dipole eteint, t=0 : <Qtf> = a(r)(zz-1/3), D=%g, w=%g' % (D, w), fontsize=9)
    ax.text(0.3, 1e-12, 'r<D : vide (pas de champ, pas de log)', fontsize=8)
    ax.text(1.05, 1e-2, 'coquille rayonnee', fontsize=8); ax.text(1.6, 1e-8, 'dipole statique ~ r^-4', fontsize=8)
    fig.tight_layout(); fig.savefig('/home/claude/audit_ma1/q2_profil_a_r.png', dpi=130)
    print('[calcule] figure : /home/claude/audit_ma1/q2_profil_a_r.png')
except Exception as ex:
    print('figure non produite :', ex)
