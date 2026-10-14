#!/usr/bin/env python3
# YA-1, question 2 : support singulier du terme alpha beta^* de w(x,x') pour alpha beta^* ~ k^{-N} e^{i phi}.
#
#  w_{ab*}(x,x') = int d^3k/((2pi)^3 2k) alpha_k beta_k^* e^{i Phi} + c.c.,  Phi(k) = k.(x-x') - |k| (eta+eta').
#  (i)  Phase stationnaire : grad_k Phi = 0  <=>  (x-x') = khat (eta+eta')  =>  |x-x'| = |eta+eta'|  (cone "reflechi").
#  (ii) Forme fermee isotrope (coupure IR k>=1), s = eta+eta', r = |x-x'| :
#       w_{ab*}(s,r) = (1/(4 pi^2 r)) * int_1^inf k^{-N} [ sin(k(r+s) - phi) + sin(k(r-s) + phi) ] dk
#                    = (1/(4 pi^2 r)) * Im[ e^{-i phi} E_N(-i(r+s)) + e^{+i phi} E_N(-i(r-s)) ]
#       avec E_N(z) = int_1^inf e^{-z t} t^{-N} dt. Dans le domaine s<0, la singularite est en r = -s = |s| (r+s = 0).

import sympy as sp
import mpmath as mp
mp.mp.dps = 30
out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

P("=== YA1 Q2 : support singulier du terme alpha beta^* ===")

# ---------- (i) phase stationnaire ----------
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
r1, r2, r3, s = sp.symbols('r1 r2 r3 s', real=True)
kn = sp.sqrt(k1**2 + k2**2 + k3**2)
Phi = k1*r1 + k2*r2 + k3*r3 - kn*s
grad = [sp.diff(Phi, v) for v in (k1, k2, k3)]
P("[calcule] grad_k Phi =", [sp.simplify(g) for g in grad])
# norm of (r) at stationary point : r_i = s k_i/|k|  => |r|^2 = s^2
rsq = sum((s*ki/kn)**2 for ki in (k1, k2, k3))
P("[calcule] au point stationnaire r = s khat : |r|^2 =", sp.simplify(rsq), " => |x-x'| = |eta+eta'|")
P("[derive] Pour eta,eta' < 0 : |eta+eta'| = |eta|+|eta'| > 0, atteint dans le domaine (ex. eta=eta'=-1, |x-x'|=2).")
P("         Ce lieu est le cone de lumiere entre x et le point image R x' = (-eta', x') : singularite de type 'charge image'.")
P("         Il ne coincide avec le cone de lumiere entre x et x' (|x-x'| = |eta-eta'|) que si eta eta' = 0.")

# ---------- (ii) nature de la singularite : developpement de E_N(z) en z = 0 ----------
z = sp.symbols('z')
P("")
P("[calcule] Partie singuliere de E_N(z) en z=0 (terme en z^{N-1} log z) :")
for N in [3, 4, 5]:
    ser = sp.series(sp.expint(N, z), z, 0, N+1).removeO()
    P(f"   N={N} : E_N(z) = {ser}")
P("[derive] Avec z = -i t, t = r+s : w_{ab*} contient un terme ~ t^{N-1} ln|t| : w_{ab*} est C^{N-2} mais pas C^{N-1} a travers le cone reflechi.")
P("         N=3 : C^1, derivees secondes a divergence logarithmique sur le cone reflechi ; aucun N fini ne donne C^inf.")
P("         Homogeneite : alpha beta^* = c k^{-N} => w_{ab*}(lambda s, lambda r) = lambda^{N-2} w_{ab*}(s,r) ; dd w a le degre N-4 ; au sommet (s=0,r=0) : |eta|^{N-4} => 1/eta pour N=3.")

# ---------- (iii) verification numerique, N = 3, phi = pi/2, s = -1 : singularite en r = 1 ----------
phi = mp.pi/2
N = 3
def w_ab(sv, rv):
    E = lambda t: mp.expint(N, -1j*t)
    return mp.im(mp.exp(-1j*phi)*E(rv+sv) + mp.exp(1j*phi)*E(rv-sv))/(4*mp.pi**2*rv)
def w_ab_quad(sv, rv):
    f = lambda kk: kk**(-N)*(mp.sin(kk*(rv+sv)-phi) + mp.sin(kk*(rv-sv)+phi))
    return mp.quadosc(f, [1, mp.inf], omega=max(abs(rv+sv), abs(rv-sv)))/(4*mp.pi**2*rv)
sv = mp.mpf(-1)
P("")
P("[calcule] N=3, phi=pi/2, s=eta+eta'=-1 : w_{ab*}(s,r), forme fermee vs quadrature oscillante")
for rv in [mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('1.1'), mp.mpf('2.0')]:
    P(f"   r={mp.nstr(rv,3)}  closed={mp.nstr(w_ab(sv,rv),12)}  quad={mp.nstr(w_ab_quad(sv,rv),12)}")
P("[calcule] derivee seconde d^2_r w_{ab*}(s=-1, r) au voisinage de r = 1 (cone reflechi) : divergence logarithmique attendue")
for d in [mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3'), mp.mpf('1e-4')]:
    f = lambda rr: w_ab(sv, rr)
    d2p = mp.diff(f, 1+d, 2); d2m = mp.diff(f, 1-d, 2)
    P(f"   delta={mp.nstr(d,3)} : d2w(1+delta)={mp.nstr(d2p,8)}  d2w(1-delta)={mp.nstr(d2m,8)}  ln(1/delta)/(4 pi^2)={mp.nstr(mp.log(1/d)/(4*mp.pi**2),8)}")
P("[calcule] la meme derivee seconde loin du cone reflechi (r = 0.5, 2, 3) : finie")
for rv in [mp.mpf('0.5'), mp.mpf(2), mp.mpf(3)]:
    P(f"   r={mp.nstr(rv,3)} : d2w={mp.nstr(mp.diff(lambda rr: w_ab(sv, rr), rv, 2),10)}")
P("[calcule] premiere derivee d_r w en r=1+-delta : continue (C^1)")
for d in [mp.mpf('1e-2'), mp.mpf('1e-4')]:
    P(f"   delta={mp.nstr(d,3)} : d1w(1+delta)={mp.nstr(mp.diff(lambda rr: w_ab(sv, rr), 1+d, 1),10)}  d1w(1-delta)={mp.nstr(mp.diff(lambda rr: w_ab(sv, rr), 1-d, 1),10)}")

# ---------- (iv) le vrai cone de lumiere entre x et x' n'est pas singulier pour w_{ab*} ----------
P("")
P("[calcule] Au cone de lumiere veritable |x-x'| = |eta-eta'| (ex. eta=-0.3, eta'=-0.7 : s=-1, r=0.4) : w_{ab*} y est lisse")
for d in [mp.mpf('1e-2'), mp.mpf('1e-4')]:
    P(f"   delta={mp.nstr(d,3)} : d2w(0.4+delta)={mp.nstr(mp.diff(lambda rr: w_ab(sv, rr), mp.mpf('0.4')+d, 2),10)}  d2w(0.4-delta)={mp.nstr(mp.diff(lambda rr: w_ab(sv, rr), mp.mpf('0.4')-d, 2),10)}")

# ---------- (v) le terme |beta|^2 ~ k^{-2N} : singulier sur le vrai cone, a frequence negative ----------
P("")
P("[derive] Terme |beta|^2 : w_{bb}(t=eta-eta', r) = (1/(2 pi^2 r)) int k^{-2N} sin(kr) cos(kt) dk, N=3 : k^{-6} => terme ~ (r-|t|)^5 ln|r-|t|| :")
P("         C^4 mais pas C^5 sur le cone de lumiere veritable |x-x'| = |eta-eta'| ; la partie u^*(x) u(x') est a frequence NEGATIVE (covecteur k dans V^- au premier point).")
Nb = 6
def w_bb(tv, rv):
    E = lambda t: mp.expint(Nb, -1j*t)
    return mp.im(E(rv+tv) + E(rv-tv))/(4*mp.pi**2*rv)
tv = mp.mpf(-1)
P("[calcule] d^5_r w_{bb}(t=-1, r) pres de r=1 (|beta|^2 = k^{-6}, k>=1) : divergence logarithmique")
for d in [mp.mpf('1e-1'), mp.mpf('1e-2'), mp.mpf('1e-3')]:
    P(f"   delta={mp.nstr(d,3)} : d5w(1+delta)={mp.nstr(mp.diff(lambda rr: w_bb(tv, rr), 1+d, 5),8)}  d5w(1-delta)={mp.nstr(mp.diff(lambda rr: w_bb(tv, rr), 1-d, 5),8)}")

# ---------- (vi) classe a decroissance rapide : singularite repoussee dans le plan complexe ----------
P("")
P("[calcule] Classe (a) alpha beta^* = e^{i phi} e^{-k/kc} : w_{ab*}(s,r) en forme fermee")
kk, kc, rr, ss, ph = sp.symbols('k k_c r s phi', positive=True)
I1 = sp.integrate(sp.exp(-kk*(1/kc + sp.I*ss))*sp.sin(kk*rr), (kk, 0, sp.oo), conds='none')
P("   int_0^inf e^{-k(1/kc + i s)} sin(kr) dk =", sp.simplify(I1))
P("   => w_{ab*} = (1/(2 pi^2 r)) Re[e^{i phi} * (ci-dessus)] : fonction reelle-analytique de (s,r) sur R^2 ;")
P("      singularites seulement en (1/kc + i s)^2 + r^2 = 0, i.e. s = +- r + i/kc : hors de l'axe reel. Le cone reflechi est 'repousse' a distance imaginaire 1/kc.")

P("")
P("[derive] RESUME Q2 : supp sing(w_{ab*}) = {|x-x'| = |eta+eta'|} (cone de lumiere de l'image miroir R x' = (-eta',x')), qui rencontre le domaine eta,eta'<0 ;")
P("   ces etats (N fini) ne sont pas Hadamard sur le domaine : (1) le terme alpha beta^* porte une singularite hors du cone de lumiere entre x et x' ;")
P("   (2) le terme |beta|^2 ~ k^{-2N} porte une singularite de frequence negative sur le cone de lumiere lui-meme, ce qui viole deja la forme locale pres de la diagonale.")
P("   Hadamard <=> beta_k (donc alpha beta^*) a decroissance rapide (tous les moments UV finis) ; alors w est C^inf sur R^4 x R^4, donc lisse a travers eta = 0.")

with open('/home/claude/audit_ya1/work/ya1_q2_support_singulier.out', 'w') as fh:
    fh.write("\n".join(out) + "\n")
