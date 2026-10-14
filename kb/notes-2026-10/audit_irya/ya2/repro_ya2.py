#!/usr/bin/env python3
# repro_ya2.py : reproduction independante pour l'audit YA-2 (code de l'auditeur).
# Partie A : integrales I_m(eta) = int_0^inf dk k^m f(k) e^{-2 i k eta}, f gaussienne et f = k^{-N}.
# Partie B : forme fermee de int d^3k/(2k(2pi)^3) e^{-ik(eta+eta')} e^{ik.(x-x')}.
# Partie C : comportement de T^w (partie alpha beta*) pour N = 2..6, cos- et sin-parties, avec coupure IR.
# Partie D : tenseur energie-impulsion complet du scalaire a couplage xi : le terme alpha beta* en etat homogene isotrope.
import sympy as sp
import mpmath as mp
mp.mp.dps = 30
out = []
def P(*a):
    line = ' '.join(str(z) for z in a); print(line); out.append(line)

k, eta, r, T, a = sp.symbols('k eta r T a', real=True)
L, apos, k0 = sp.symbols('L a_+ k_0', positive=True)
etan = sp.symbols('eta_n', negative=True)

P("######## A. Integrales I_m, f gaussienne : f = exp(-k^2/L^2), parties cos(2 k eta) et sin(2 k eta)")
for m in (1, 3):
    Ic = sp.integrate(k**m*sp.exp(-k**2/L**2)*sp.cos(2*k*eta), (k, 0, sp.oo))
    Is = sp.integrate(k**m*sp.exp(-k**2/L**2)*sp.sin(2*k*eta), (k, 0, sp.oo))
    Ic = sp.simplify(Ic.rewrite(sp.erfi)); Is = sp.simplify(Is.rewrite(sp.erfi))
    P(f"  m={m} : cos-partie =", Ic)
    P(f"  m={m} : sin-partie =", Is)
    # developpement en eta = 0 : serie entiere ?
    P(f"      serie en eta (cos) :", sp.series(Ic, eta, 0, 5).removeO())
    P(f"      serie en eta (sin) :", sp.series(Is, eta, 0, 6).removeO())
    # controle numerique
    for e_ in (-0.3, -0.05):
        num_c = mp.quad(lambda kk: kk**m*mp.exp(-kk**2/4)*mp.cos(2*kk*e_), [0, mp.inf])
        sym_c = Ic.subs({L: 2, eta: e_}).evalf(20)
        P(f"      controle L=2, eta={e_} : cos num={mp.nstr(num_c,12)} sympy={sp.N(sym_c,12)}")
P("  [calcule] cos- et sin-parties sont des combinaisons de exp(-L^2 eta^2), eta*erfi(L eta) : fonctions entieres de eta ; le developpement est une serie entiere (pas de |eta|, pas de log).")
P("")

P("######## A'. Integrales I_m, f = k^{-N}, regularisation UV e^{-a k} (a -> 0+) quand m-N+1 > 0")
P("  Forme generale : int_0^inf dk k^{s-1} e^{-ak} e^{2 i k eta} = Gamma(s) / (a - 2 i eta)^s,  s = m - N + 1 > 0.")
P("  Limite a -> 0, eta < 0 : (a - 2 i eta)^{-s} -> (2|eta|)^{-s} e^{-i pi s/2 sgn(eta)}  ->  pour eta<0 : (2|eta|)^{-s} e^{+ i pi s/2}.")
P("  Donc int k^{s-1} cos(2 k eta) dk -> Gamma(s) cos(pi s/2)/(2|eta|)^s   et   int k^{s-1} sin(2 k eta) dk -> Gamma(s) sin(pi s/2) sgn(eta)/(2|eta|)^s.")
s = sp.symbols('s', positive=True)
expr = sp.gamma(s)/(apos - 2*sp.I*eta)**s
for s_ in (1, 2, 3):
    lim = sp.limit(expr.subs(s, s_).subs(eta, etan), apos, 0)
    P(f"   s={s_} : lim_a->0 Gamma(s)/(a-2i eta)^s (eta<0) =", sp.simplify(lim), " ; Re =", sp.simplify(sp.re(lim)), " ; Im =", sp.simplify(sp.im(lim)))
P("   [calcule] s=1 (m=3, N=3) : Re = 0, Im = 1/(2 eta) : la sin-partie vaut +1/(2 eta) (= -1/(2|eta|) pour eta<0), PAS -1/(2 eta).")
# controle numerique explicite de la sin partie, comme dans le script
for e_ in (-0.1, -0.05, -0.02):
    v = mp.quadosc(lambda kk: mp.sin(2*kk*e_)*mp.exp(-kk*1e-3), [0, mp.inf], omega=2*abs(e_))
    P(f"   controle numerique : eta * int sin(2k eta) e^(-k/1000) dk, eta={e_} : {mp.nstr(e_*v, 8)}  (exact a->0 : eta * 1/(2 eta) = +1/2 ; avec a : 2 eta^2/(4 eta^2 + a^2))")
P("")
P("  Avec phase : alpha beta* = k^{-N} e^{i phi} ; Re(alpha beta* e^{-2 i k eta}) = k^{-N} cos(2 k eta - phi).")
P("  => I_m^{phi}(eta) = Gamma(s) cos(pi s/2 + phi)/(2|eta|)^s   (eta<0, s = m-N+1 > 0).  [derive]")
P("  Coefficient nul ssi cos(pi s/2 + phi) = 0 : pour phi = 0, ssi s IMPAIR (s=1,3,...) ; pour phi = pi/2, ssi s PAIR.")
P("  (le script ecrit 'puissance entiere paire' pour s = 1 et s = 3 : annotation fausse, c'est s impair.)")
P("")

P("######## A''. f = k^{-N}, cas m-N+1 <= 0 : l'integrale DIVERGE en k -> 0 ; coupure IR k0 obligatoire.")
P("  int_{k0}^inf dk k^{s-1} cos(2 k eta - phi), s <= 0 : = [continuation analytique Gamma(s) cos(pi s/2+phi)/(2|eta|)^s] - int_0^{k0} dk k^{s-1} cos(2k eta - phi) (serie de Taylor en eta, regularisee en s).")
P("  Les poles de Gamma(s) en s = 0, -1, -2, ... sont compenses ou non par cos(pi s/2 + phi) :")
for s_ in (0, -1, -2, -3):
    for phi_ in (0, sp.pi/2):
        eps = sp.symbols('epsilon')
        coef = sp.series(sp.gamma(s_+eps)*sp.cos(sp.pi*(s_+eps)/2 + phi_), eps, 0, 1).removeO()
        P(f"   s={s_}, phi={phi_} : Gamma(s+eps) cos(pi(s+eps)/2+phi) = {sp.simplify(coef)}  -> " + ("POLE en 1/eps : terme |eta|^{-s} ln|eta|" if coef.has(1/eps) or sp.limit(coef, eps, 0) in (sp.oo, -sp.oo, sp.zoo) else "fini : terme |eta|^{-s} pur"))
P("  [calcule] s=0 (m=3,N=4) : phi=0 -> pole -> ln|eta| ; phi=pi/2 -> fini -> pas de log, terme regulier (sgn(eta) x const).")
P("            s=-1 (m=3,N=5) : phi=0 -> fini -> |eta|^1 (C^0) ; phi=pi/2 -> pole -> eta ln|eta| (C^0).")
P("            s=-2 (m=3,N=6) : phi=0 -> pole -> eta^2 ln|eta| (C^1) ; phi=pi/2 -> fini -> |eta|^2 sgn ~ eta|eta| (C^1).")
P("")

P("######## C. Comportement de J_N(eta) = int_{k0}^inf dk k^{3-N} cos(2 k eta - phi), k0 = 1, eta -> 0- (coupure IR explicite)")
P("  N <= 3 : integrale oscillante, definie au sens d'Abel (facteur e^{-ak}, a->0+). Formes fermees exactes (sympy) :")
kp = sp.symbols('kp', positive=True)
for N_ in (2, 3):
    for phi_ in (0, sp.pi/2):
        full = sp.integrate(k**(3-N_)*sp.cos(2*k*etan - phi_)*sp.exp(-apos*k), (k, 0, sp.oo), conds='none')
        full0 = sp.simplify(sp.limit(sp.simplify(full), apos, 0))
        low = sp.integrate(k**(3-N_)*sp.cos(2*k*etan - phi_), (k, 0, k0))
        Jex = sp.simplify(full0 - low)
        ser = sp.series(Jex.subs(k0, 1), etan, 0, 3).removeO()
        P(f"   N={N_}, phi={phi_} : J = {Jex}  ;  serie en eta->0 : {ser}")
P("   [calcule] N=2, phi=0 : J ~ -1/(4 eta^2) ; N=2, phi=pi/2 : J regulier (pas de singularite !) ; N=3, phi=0 : J -> -k0 regulier (PAS de 1/eta) ; N=3, phi=pi/2 : J ~ 1/(2 eta).")
P("   (Remarque : avec un facteur e^{-ak} a a fixe, des termes parasites a/(4 eta^2), a/(4|eta|^3) apparaissent pres de eta=0 : ce sont des deltas naissants en eta = 0, nuls pour eta<0 a a->0.)")
P("  N >= 4 : integrale absolument convergente ; controle mpmath.")
def J(N_, phi_, e_):
    return mp.quadosc(lambda kk: kk**(3-N_)*mp.cos(2*kk*e_ - phi_), [1, mp.inf], omega=2*abs(e_))
etas = [mp.mpf(x) for x in ('-0.08', '-0.04', '-0.02', '-0.01')]
h = mp.mpf('1e-4')
for N_ in (4, 5, 6):
    for phi_ in (0, mp.pi/2):
        vals = [J(N_, phi_, e_) for e_ in etas]
        d1 = [(J(N_,phi_,e_+h) - J(N_,phi_,e_-h))/(2*h) for e_ in etas]
        d2 = [(J(N_,phi_,e_+h) - 2*J(N_,phi_,e_) + J(N_,phi_,e_-h))/h**2 for e_ in etas]
        P(f"   N={N_}, phi={'0' if phi_==0 else 'pi/2'} : J = {[mp.nstr(v,6) for v in vals]} ; J' = {[mp.nstr(v,6) for v in d1]} ; J'' = {[mp.nstr(v,6) for v in d2]}")
P("   Lecture [calcule] : N=4,phi=0 : J ~ -ln|eta| (ecarts de ln 2 = 0.693 entre points) ; N=4,phi=pi/2 : J borne, J' ~ 1/eta (donc J ~ sgn x const + eta ln|eta|... C^0).")
P("            N=5,phi=0 : J' -> +pi = 3.1416 en 0- (kink |eta|, C^0) ; N=5,phi=pi/2 : J'' ~ -2/eta (eta ln|eta|, C^0).")
P("            N=6,phi=0 : J'' ~ 2 c ln|eta| (eta^2 ln|eta|, C^1) ; N=6,phi=pi/2 : J'' -> const avec saut en 0 (eta|eta|, C^1).")
P("  Bilan y-1 corrige : T^w(alpha beta*) ~ Gamma(4-N) cos(pi(4-N)/2 + phi) (2|eta|)^{N-4} + regulier ; 1/eta ssi N = 3 ET sin(phi) != 0 ; pour N=3 et phi=0 : aucune singularite.")
P("")

P("######## B. Forme fermee de W_r(T, r) = int d^3k/(2k (2pi)^3) e^{-ikT} e^{ik.r}, T = eta + eta'")
P("  Integration angulaire : int dOmega e^{ik.r} = 4 pi sin(kr)/(kr)  =>  W_r = (1/(4 pi^2 r)) int_0^inf dk sin(kr) e^{-ikT}  (mesure dk, pas k dk).")
I1 = sp.integrate(sp.sin(k*r)*sp.exp(-sp.I*k*T)*sp.exp(-apos*k), (k, 0, sp.oo), conds='none')
I1 = sp.simplify(I1)
P("  int_0^inf dk sin(kr) e^{-ikT} e^{-ak} =", I1)
re_lim = sp.simplify(sp.limit(sp.re(I1.subs({r: sp.Symbol('rp', positive=True), T: sp.Symbol('Tn', negative=True)})), apos, 0))
P("  Re, a->0 (hors cone) :", re_lim, "  => Re W_r = 1/(4 pi^2 (r^2 - T^2)) (valeur principale) [calcule]")
P("  Im, a->0 : -(pi/2)[delta(r-T) - delta(r+T)]/ (4 pi^2 r) : distribution portee par le cone reflechi r = |T|. [derive]")
P("  Avec prescription : W_r = 1/(4 pi^2) 1/( r^2 - (T - i0)^2 ). Singulier sur r = |T| = |eta + eta'| : pour eta, eta' < 0, p.ex. eta=eta'=-1, r=2. [calcule]")
P("  Terme alpha beta* = k^{-N} : w_N = (1/(4 pi^2 r)) 2 Re[ e^{i phi} int dk k^{-N} sin(kr) e^{-ikT} ] ; int dk k^{-N} e^{i k (r - T)} ~ Gamma(1-N) (-i(r-T))^{N-1} :")
P("  singularite en (r - |T|)^{N-1} (avec ln ou sgn selon la phase, N entier >= 1) : classe C^{N-2} sur le cone reflechi, jamais C^inf. (Le script ecrit |.|^{N-4} dans le message et r^{N-3} en commentaire : l'exposant pertinent est N-1 transversalement au cone.) [derive]")
# controle numerique de l'ordre de la singularite sur le cone reflechi : F_N(r) = int_1^inf dk k^{-N} sin(kr) cos(kT), T = -2, r -> 2
def F(N_, r_, T_=-2):
    return mp.quadosc(lambda kk: kk**(-N_)*mp.sin(kk*r_)*mp.cos(kk*T_), [1, mp.inf], omega=abs(r_)+abs(T_))
rows = []
for d in ('1e-1', '1e-2', '1e-3', '1e-4'):
    d = mp.mpf(d); hh = d/10
    rows.append((mp.nstr(d,2), mp.nstr((F(2, 2+d+hh) - F(2, 2+d-hh))/(2*hh),7)))
P(f"  N=2 : F_2'(r) en r = 2 + d : {rows}  -> croissance en ln(1/d) (0.5 ln 10 = 1.15 par decade) : F_2 est C^0 mais pas C^1 sur le cone. [calcule]")
rows = []
for d in ('2e-1', '1e-1', '5e-2', '2e-2'):
    d = mp.mpf(d); hh = mp.mpf('2e-3')
    fpp = lambda rr: (F(3, rr+hh) - 2*F(3, rr) + F(3, rr-hh))/hh**2
    rows.append((mp.nstr(d,2), mp.nstr(fpp(2+d),6), mp.nstr(fpp(2-d),6)))
P(f"  N=3 : F_3''(r) en r = 2 + d et 2 - d : {rows}  -> F_3'' tend vers deux limites differentes (saut, terme b|b|/2 ... ) : F_3 est C^1 mais pas C^2 sur le cone. [calcule]")
P("  (Precision : avec alpha beta* reel la singularite transverse est de type sgn(b)|b|^{N-1} ; avec une phase, de type b^{N-1} ln|b| ; dans les deux cas classe C^{N-2} exactement.) [derive]")
P("")

P("######## D. Tenseur energie-impulsion du scalaire sans masse, couplage xi, etat homogene isotrope de Bogoliubov sur Minkowski")
P("  T_{mu nu} = d_mu phi d_nu phi - (1/2) g_{mu nu} (d phi)^2 + xi (g_{mu nu} Box - d_mu d_nu) phi^2, signature (-+++), coordonnees (eta, x).")
P("  Mode : v_k = alpha u_k + beta u_k*, u_k = e^{-ik eta}/sqrt(2k) (x e^{ik.x}). Termes croises alpha beta* dans <T_{mu nu}> : angulairement moyennes.")
xi = sp.symbols('xi', real=True)
kk, th = sp.symbols('kk theta', positive=True)
al, be = sp.symbols('alpha beta')
u = sp.exp(-sp.I*kk*eta)/sp.sqrt(2*kk)
v = al*u + be*sp.conjugate(u)
vc = sp.conjugate(v)
# on garde seulement les termes en alpha*conj(beta) et conj(alpha)*beta
def cross(expr):
    expr = sp.expand(expr)
    ab = sp.Symbol('AB'); ba = sp.Symbol('BA')
    e2 = expr.subs({al*sp.conjugate(be): ab, sp.conjugate(al)*be: ba})
    e2 = e2.subs({al*sp.conjugate(al): 0, be*sp.conjugate(be): 0})
    return sp.simplify(sp.expand(e2))
# <phi'^2> -> |v'|^2 ; <(d_i phi)(d_j phi)> -> k_i k_j |v|^2 ; <phi^2> -> |v|^2
dv = sp.diff(v, eta); dvc = sp.conjugate(dv)
phidot2 = cross(dv*dvc)
phi2 = cross(v*vc)
grad2 = cross(kk**2*v*vc)
# isotropie : <k_i k_j> -> k^2/3 delta_ij
# T_00 = (1/2)(phi'^2 + grad^2) + xi(g_00 Box - d_0 d_0) phi^2 ; g_00=-1, Box = -d_0^2 + lap ; homogene : lap -> 0
T00 = sp.Rational(1,2)*(phidot2 + grad2) + xi*(-(-sp.diff(phi2, eta, 2)) - sp.diff(phi2, eta, 2))
# T_ij (trace par delta_ij) : <d_i phi d_j phi> -> grad2/3 ; -(1/2)(-phi'^2 + grad2) ; xi (Box phi2) delta_ij avec Box -> -d_eta^2 ; -xi d_i d_j -> 0
Tii = grad2/3 - sp.Rational(1,2)*(-phidot2 + grad2) + xi*(-sp.diff(phi2, eta, 2))
P("  terme croise de <T_00> (par mode, apres moyenne angulaire) :", sp.simplify(T00))
P("  terme croise de <T_ij>/delta_ij (par mode, apres moyenne angulaire) :", sp.factor(sp.simplify(Tii)))
P("  terme croise de <phi^2> (par mode) :", sp.simplify(phi2))
P("  [calcule] <T_00>^{alpha beta*} = 0 pour tout xi ; <T_ij>^{alpha beta*} proportionnel a (xi - 1/6) : pour le scalaire CONFORME (xi = 1/6), le terme alpha beta* du tenseur est IDENTIQUEMENT NUL en etat homogene isotrope.")
P("  [calcule] Le tenseur d'etat du scalaire conforme se reduit au terme |beta|^2 : rho = int d^3k/(2pi)^3 k |beta_k|^2, p = rho/3, INDEPENDANT de eta.")
# anisotrope : partie sans trace
P("  Etat anisotrope (alpha beta* dependant de la direction) : terme croise de <T_ij> = 2 Re(alpha beta* u^2) [k_i k_j - k^2 delta_ij/3] + 8 (xi-1/6)... : seule la partie sans trace survit a xi = 1/6. [derive]")
P("")

P("######## E. Contre-exemples cherches : T^w ~ 1/eta sans singularite de w dans le domaine eta, eta' < 0 ?")
P("  Cadre : terme alpha beta* en coincidence : C(eta) = Re int_0^inf dk g(k) e^{-2 i k eta}, g = k^3 alpha beta* (pour xi != 1/6). Abel-regularise.")
e0 = sp.symbols('eta_0', real=True); ell, K = sp.symbols('ell K', positive=True)
A1 = sp.limit(sp.integrate(sp.exp(2*sp.I*k*e0)*sp.exp(-2*sp.I*k*eta)*sp.exp(-apos*k), (k, 0, sp.oo), conds='none'), apos, 0)
P("  (i) phase lineaire alpha beta* = k^{-3} e^{2 i k eta_0} (etat translate en temps) : int dk e^{2ik(eta_0-eta)} =", sp.simplify(A1), " : pole en eta = eta_0, pas en 0. Pour eta_0 < 0 la singularite de T^w est DANS le domaine ; pour eta_0 > 0 T^w est lisse en 0- mais w est singulier sur le cone r = |eta+eta' - 2 eta_0| qui coupe le domaine. [calcule]")
A2 = sp.limit(sp.integrate(sp.cos(k*ell)*sp.exp(-2*sp.I*k*eta)*sp.exp(-apos*k), (k, 0, sp.oo), conds='none'), apos, 0)
P("  (ii) oscillant alpha beta* = k^{-3} cos(k ell) : int dk cos(k ell) e^{-2ik eta} =", sp.simplify(A2), " : poles en eta = +-ell/2, rien en eta = 0 : pas de 1/eta ; w singulier sur les cones r = |T +- ell| (dans le domaine). [calcule]")
A3 = sp.integrate(sp.exp(-2*sp.I*k*eta), (k, 0, K))
P("  (iii) support compact alpha beta* = k^{-3} 1_{k<K} : int_0^K dk e^{-2ik eta} =", sp.simplify(A3), " : fonction ENTIERE de eta (singularite apparente en 0 levable) ; w entiere en (T, x) : ni 1/eta, ni cone. [calcule]")
P("  (iv) argument general [derive] : w_ab(T, x) := int d^3k/(2k(2pi)^3) 2Re(alpha beta* e^{-ikT}) e^{ik.x} est une solution distributionnelle de l'equation des ondes en (T, x) sur R^4 (chaque mode e^{-ikT+ik.x} avec |k| = k l'est).")
P("      Si T^w ~ 1/eta en eta -> 0-, alors w_ab n'est pas C^inf au point (T=0, x=0) (sinon la limite de coincidence et ses derivees seraient lisses en eta = 0).")
P("      Par propagation des singularites (Hormander : WF(u) invariant par le flot bicaracteristique nul pour Box u = 0), la singularite en (0,0) se propage le long d'un rayon nul T = -|x| vers T < 0,")
P("      c'est-a-dire sur des points (eta+eta' = T < 0, |x-x'| = |T|) : par exemple eta = eta' = T/2 < 0. Donc w est singulier dans le domaine eta, eta' < 0.")
P("      Conclusion : AUCUNE famille alpha beta* (temperee, homogene) ne donne T^w ~ 1/eta sans singularite de w dans le domaine. Les familles oscillantes deplacent la singularite, les supports compacts la suppriment avec le 1/eta. [derive]")
P("      (Pour le scalaire conforme la question est vide : le terme alpha beta* de T^w est identiquement nul, cf. D.)")
P("")
open('repro_ya2_sortie.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
