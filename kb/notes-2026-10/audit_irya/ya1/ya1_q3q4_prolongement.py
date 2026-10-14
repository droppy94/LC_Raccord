#!/usr/bin/env python3
# YA-1, questions 3 et 4 : illustrations calculatoires de l'argument de prolongement
#  (a) les termes w_{ab*}(s,r) sont des bisolutions de l'equation des ondes (verification symbolique),
#      lisses a travers s = eta+eta' = 0 dans la classe Hadamard, singulieres sur r = -s dans la classe (b) ;
#  (b) la formule de Kirchhoff (probleme de Cauchy, 3+1) : pour des donnees lisses sur eta = tau, la solution
#      est lisse pour eta de part et d'autre de tau, y compris a travers eta = 0 ;
#  (c) T^w(eta) a travers eta = 0 pour un etat Hadamard homogene explicite : fini et lisse.

import sympy as sp
import mpmath as mp
mp.mp.dps = 25
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

P("=== YA1 Q3/Q4 : prolongement de w a travers eta = 0 ===")

# ---------- (a) bisolution : operateur des ondes en variables (s, r) ----------
# Pour une fonction F(s, r), s = eta + eta', r = |x - x'| :
#   Box_x F = -d_eta^2 F + Delta_x F = -F_ss + F_rr + (2/r) F_r  (meme chose pour Box_{x'}).
s, r, phi = sp.symbols('s r phi', real=True)
kc = sp.symbols('k_c', positive=True)
def box(F):
    return sp.simplify(-sp.diff(F, s, 2) + sp.diff(F, r, 2) + 2*sp.diff(F, r)/r)

# Classe (a), alpha beta^* = e^{i phi} e^{-k/kc} : w_{ab*} = (1/(2 pi^2 r)) Re[ e^{i phi} kc^2 r / (kc^2 r^2 + (1 + i kc s)^2) ]
G = sp.exp(sp.I*phi)*kc**2*r/(kc**2*r**2 + (1 + sp.I*kc*s)**2)
w_a = sp.re(G)/(2*sp.pi**2*r)
w_a = sp.simplify(sp.expand_complex(w_a))
P("[calcule] classe (a) : w_{ab*}(s,r) =", w_a)
P("[calcule] Box w_{ab*} (classe a) =", box(w_a))
P("[calcule] w_{ab*}(s, r->0) (limite de coincidence spatiale), classe (a) :", sp.simplify(sp.limit(w_a, r, 0)))
# analyticite : denominateur reel
den = sp.denom(sp.together(w_a))
P("[calcule] denominateur de w_{ab*} (classe a) :", sp.factor(den))
P("[derive]  il ne s'annule pour aucun (s,r) reel (somme de carres), w_{ab*} est reelle-analytique sur R x R_+ et au sommet s=0, r=0.")

# Classe (b), N=3 : w = (1/(4 pi^2 r)) Im[ e^{-i phi} E_3(-i(r+s)) + e^{i phi} E_3(-i(r-s)) ] ; verification de l'equation des ondes
# via la representation integrale : chaque mode k^{-3} sin(kr) cos(ks - phi)/r est solution (on verifie sur le mode).
k = sp.symbols('k', positive=True)
mode = sp.sin(k*r)*sp.cos(k*s - phi)/r
P("[calcule] classe (b) : Box [sin(kr) cos(ks-phi)/r] =", box(mode), " (chaque mode est une bisolution, donc la superposition aussi)")

# ---------- (b) formule de Kirchhoff : donnees lisses sur eta = tau -> solution lisse globale ----------
x1, x2, x3, t, tau, eta = sp.symbols('x1 x2 x3 t tau eta', real=True)
th, ph = sp.symbols('theta varphi', real=True)
def sph_mean(f, tt):
    # moyenne de f sur la sphere de centre x, rayon |tt| (parametrage t -> signe sans importance pour la moyenne)
    sub = {x1: x1 + tt*sp.sin(th)*sp.cos(ph), x2: x2 + tt*sp.sin(th)*sp.sin(ph), x3: x3 + tt*sp.cos(th)}
    return sp.simplify(sp.integrate(sp.integrate(f.subs(sub)*sp.sin(th), (th, 0, sp.pi)), (ph, 0, 2*sp.pi))/(4*sp.pi))
f0 = x1**2 + x2**2 + x1*x3**3        # donnees de Cauchy lisses (polynomiales) en eta = tau
f1 = x3 + x1*x2
u = sp.diff(t*sph_mean(f0, t), t) + t*sph_mean(f1, t)
u = sp.expand(u)
P("[calcule] Kirchhoff : u(t,x) =", u, "  (t = eta - tau)")
boxu = sp.simplify(-sp.diff(u, t, 2) + sp.diff(u, x1, 2) + sp.diff(u, x2, 2) + sp.diff(u, x3, 2))
P("[calcule] Box u =", boxu, " ; u(0,x) - f0 =", sp.simplify(u.subs(t, 0) - f0), " ; u_t(0,x) - f1 =", sp.simplify(sp.diff(u, t).subs(t, 0) - f1))
P("[derive]  u est un polynome en (t,x) : lisse pour tout t, de part et d'autre de la surface de Cauchy, en particulier a travers eta = 0 lorsque tau < 0 < tau + t.")
P("          La formule de Kirchhoff u = d_t[t M_t f0] + t M_t f1 est valable pour t de signe quelconque et depend de maniere C^inf de tout parametre dont f0, f1 dependent de maniere C^inf.")

# ---------- (c) T^w a travers eta = 0 pour un etat Hadamard homogene explicite ----------
# beta_k = b e^{-k/kc} (reel), alpha_k = sqrt(1+beta^2) e^{-i phi} : alpha beta^* = b e^{-k/kc} sqrt(1+b^2 e^{-2k/kc}) e^{-i phi}
# J(eta) = (1/2pi^2) int k^3 Re[alpha beta^* e^{-2ik eta}] dk, et T^w_{eta eta'} = (1/2pi^2) int k^3 |beta|^2 dk - J(eta)
b, kcv, phiv = mp.mpf('0.5'), mp.mpf(1), mp.pi/3
def ab(kk):
    be = b*mp.exp(-kk/kcv)
    return be*mp.sqrt(1+be**2)*mp.exp(-1j*phiv)
stat = mp.quad(lambda kk: kk**3*(b*mp.exp(-kk/kcv))**2, [0, mp.inf])/(2*mp.pi**2)
P("")
P("[calcule] etat Hadamard homogene explicite (beta = 0.5 e^{-k}, phi = pi/3) : T^w_{eta eta'}(eta) = partie stationnaire - J(eta)")
P(f"   partie stationnaire (1/2pi^2) int k^3 |beta|^2 dk = {mp.nstr(stat, 10)}")
for e in ['-0.5', '-0.1', '-0.01', '-0.001', '0', '0.001', '0.01', '0.1', '0.5']:
    ev = mp.mpf(e)
    J = mp.quad(lambda kk: kk**3*mp.re(ab(kk)*mp.exp(-2j*kk*ev)), [0, mp.inf])/(2*mp.pi**2)
    P(f"   eta={e:>7} : J={mp.nstr(J, 10):>15}   T^w_eta eta' = {mp.nstr(stat - J, 10)}")
P("[derive]  T^w est continu, borne et C^inf a travers eta = 0 : aucune divergence pour un etat Hadamard (classe a decroissance rapide).")

# ---------- (d) contre-pied : etat N=3 : T^w_{eta eta'} ~ -sin(phi)/(4 pi^2 eta) ----------
P("")
P("[calcule] etat de classe (b), N=3, phi = pi/2 (alpha beta^* = i k^{-3} pour k >= 1) : -J(eta) = -sin(phi-2eta)/(4 pi^2 eta)")
for e in ['-0.1', '-0.01', '-0.001']:
    ev = mp.mpf(e)
    J = mp.re(mp.exp(1j*mp.pi/2)*mp.exp(-2j*ev)/(2j*ev))/(2*mp.pi**2)
    P(f"   eta={e:>7} : -J = {mp.nstr(-J, 10):>15}   eta*(-J) = {mp.nstr(-ev*J, 8)}  (-> -1/(4 pi^2) = {mp.nstr(-1/(4*mp.pi**2), 8)})")

with open('/home/claude/audit_ya1/work/ya1_q3q4_prolongement.out', 'w') as fh:
    fh.write("\n".join(out) + "\n")
