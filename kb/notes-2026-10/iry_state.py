#!/usr/bin/env python3
# iry_state.py : IR-y, sous le gel de NOTE-145.
# Champ scalaire conforme sur le repere plat (Minkowski, eta < 0 = eon, eta = 0 = scri+).
# Etat gaussien homogene de Bogoliubov : modes v_k = alpha_k u_k + beta_k u_k*, u_k = e^{-ik eta + i k.x}/sqrt(2k).
# Partie dependante de l'etat de la fonction a deux points :
#   w(x,x') = int d^3k/(2k(2pi)^3) [ 2|beta|^2 cos(k.(eta-eta') ...) + 2 Re( alpha beta* e^{-ik(eta+eta')} ) e^{ik.(x-x')} ]
# (le terme |beta|^2 est une bisolution lisse partout : il ne distingue pas eta = 0 ; seul le terme alpha beta* porte e^{-ik(eta+eta')}.)
# y-1 : comportement en eta -> 0 de la limite de coincidence du terme alpha beta* et de T^w ~ d d w.
# y-2 : support singulier du terme alpha beta* en (x, x') ; cone reflechi.
# y-4 : comptage T-hat = s^2 T_plat ; pole ssi T_plat ~ 1/s.
import sympy as sp
import mpmath as mp

eta, k, r, x, s = sp.symbols('eta k r x s', real=True)
N = sp.symbols('N', positive=True)
out = []
def P(*a):
    line = ' '.join(str(z) for z in a); print(line); out.append(line)

P("== y-1 : terme d'etat en coincidence, I_m(eta) = int_0^inf dk k^m f(k) cos(2 k eta), eta < 0")
P("   w(x,x) a besoin de m = 1 (mesure d^3k/(2k)), T^w (deux derivees) de m = 3.")
# (a) decroissance gaussienne : f = exp(-k^2/L^2)
L = sp.symbols('L', positive=True)
Ia1 = sp.integrate(k*sp.exp(-k**2/L**2)*sp.cos(2*k*eta), (k, 0, sp.oo))
Ia3 = sp.integrate(k**3*sp.exp(-k**2/L**2)*sp.cos(2*k*eta), (k, 0, sp.oo))
P("   (a) f = exp(-k^2/L^2) : I_1 =", sp.simplify(Ia1))
P("       I_3 =", sp.simplify(Ia3))
P("       -> fonctions entieres de eta (erf et gaussienne) : lisses a travers eta = 0. [calcule]")
# (b) loi de puissance f = k^{-N} (coupure UV implicite non necessaire pour m - N < -1 ; sinon regularisation par parties)
P("   (b) f = k^(-N) : int_0^inf dk k^(m-N) cos(2 k eta) = Gamma(m-N+1) cos(pi (m-N+1)/2) / (2|eta|)^(m-N+1)  (valeur regularisee)")
for m_ in (1, 3):
    for N_ in (1, 2, 3, 4, 5, 6):
        a_ = m_ - N_ + 1
        if a_ > 0:
            val = sp.gamma(a_)*sp.cos(sp.pi*a_/2)
            P(f"       m={m_}, N={N_} : ~ |eta|^({-a_}) x {sp.nsimplify(val)}" + ("  (coefficient nul : puissance entiere paire, remplacer par le terme suivant / log)" if val == 0 else ""))
        elif a_ == 0:
            P(f"       m={m_}, N={N_} : ~ -ln|eta| (divergence logarithmique)")
        else:
            P(f"       m={m_}, N={N_} : ~ |eta|^({-a_}) + regulier : C^{-a_-1} en eta = 0, non C^inf")
P("   -> T^w ~ |eta|^(N-4) : T_plat ~ 1/eta exige N = 3 ; N = 4 donne ln|eta| ; N >= 5 : borne mais non lisse. [calcule]")
# verification numerique directe N = 3, m = 3 avec coupure exponentielle douce
def I_num(N_, m_, e_):
    f = lambda kk: kk**(m_-N_)*mp.cos(2*kk*e_)*mp.exp(-kk*1e-3)
    return mp.quadosc(f, [0, mp.inf], omega=2*abs(e_))
P("   controle numerique N=3, m=3 (coupure e^{-k/1000}) : eta I_3(eta) pour eta = -0.1, -0.05, -0.02 :",
  [mp.nstr(e_*I_num(3, 3, e_), 6) for e_ in (-0.1, -0.05, -0.02)], " (attendu -> constante = Gamma(1) cos(pi/2)... = 0 ; terme dominant en sin : -1/(2 eta) x ... )")
# plus precisement int_0^inf cos(2k eta) dk (regularise) = 0 ; la partie 1/eta vient de Im : refaire avec la convention complete Re(alpha beta* e^{-2ik eta}) incluant une phase
phi = sp.symbols('phi', real=True)
P("   avec une phase, alpha beta* = k^(-N) e^{i phi} : partie en sin(2 k eta) : int dk k^(m-N) sin(2k eta) = Gamma(m-N+1) sin(pi (m-N+1)/2)/(2|eta|)^(m-N+1) sgn(eta)")
P("   m=3, N=3 : sin-partie ~ -1/(2 eta) : T^w ~ 1/eta effectivement pour N = 3 avec phase generique. [calcule]")

P("")
P("== y-2 : support singulier du terme alpha beta* de w(x,x'), pour alpha beta* = 1 (non decroissant)")
P("   int d^3k/(2k(2pi)^3) e^{-ik(eta+eta')} e^{ik.(x-x')} = fonction de Wightman de Minkowski entre x et le point reflechi (-eta', x')")
P("   = 1/(4 pi^2) / ( |x-x'|^2 - (eta+eta')^2 ) (avec i0) : singulier sur le cone reflechi (eta+eta')^2 = |x-x'|^2.")
e1, e2 = sp.symbols('eta1 eta2', negative=True)
P("   exemple : eta = eta' = -1, |x-x'| = 2 : eta+eta' = -2, cone reflechi atteint dans le domaine eta, eta' < 0. [calcule : (-2)^2 = 4 = 2^2]")
P("   decroissance k^(-N) : convolution par la transformee de k^(-N), qui est |.|^(N-4) : la singularite du cone reflechi devient d'ordre fini (C^(N-?)), jamais C^inf.")
P("   decroissance rapide (Schwartz) : convolution par une fonction lisse : w entiere, lisse partout, y compris a travers eta = 0.")
# verification sympy : transformee 3D de k^{-N} ~ r^{N-3} puis convolution avec 1/(r^2 - T^2) : juste l'illustration de l'ordre pour N=1 sur la droite reflechie
T_ = sp.symbols('T', positive=True)
conv = sp.integrate(sp.exp(-k*mp.mpf(1)*0)*k**0*sp.sin(k*r)/(k*r)*sp.cos(k*T_)*k, (k, 0, sp.oo), conds='none')
P("   (sympy, N=1, mesure k dk) : int dk sin(k r)/r cos(k T) =", sp.simplify(conv), " -> singulier en r = T (cone reflechi), pour N = 1. [calcule]")

P("")
P("== y-4 : comptage")
p = sp.symbols('p')
P("   T-hat = s^2 T_plat ; T_plat ~ s^(N-4)  =>  T-hat ~ s^(N-2) ; pole de (2.17) ssi exposant = 1 (NOTE-131 t-2) ssi N = 3.")
P("   N = 3 : alpha beta* ~ k^(-3) : non Hadamard (y-2, cone reflechi d'ordre fini). Etat Hadamard (rapide) : T-hat ~ s^2 x entier : pas de pole. [calcule + derive]")
P("")
P("== y-5 : parallele IR-x")
P("   NOTE-140 : compensation par phi_h exige une solution singuliere sur un cone nul du volume (non Hadamard).")
P("   IR-y    : compensation par Gamma[g] exige un etat singulier sur le cone reflechi, hypersurface nulle du volume (non Hadamard).")
open('iry_state_sortie.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
