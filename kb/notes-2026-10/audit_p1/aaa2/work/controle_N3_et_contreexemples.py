# controle_N3_et_contreexemples.py : taches 4 et 5 de l'audit AAA-2
import sympy as sp
import mpmath as mpm

mpm.mp.dps = 25
print("== Tache 4 : Int_0^inf dk sin(2 k eta) e^{-a k} ==")
k, a = sp.symbols('k a', positive=True)
eta = sp.symbols('eta', real=True)
I_sin = sp.integrate(sp.sin(2*k*eta)*sp.exp(-a*k), (k, 0, sp.oo), conds='none')
I_cos = sp.integrate(sp.cos(2*k*eta)*sp.exp(-a*k), (k, 0, sp.oo), conds='none')
print("forme fermee sympy  Int sin(2k eta) e^{-ak} dk =", sp.simplify(I_sin))
print("forme fermee sympy  Int cos(2k eta) e^{-ak} dk =", sp.simplify(I_cos))
print("eta * Int sin : limite a -> 0+ (eta != 0) =", sp.limit(sp.simplify(eta*I_sin), a, 0, '+'))
print("Int e^{-2ik eta} e^{-ak} dk = Int cos - i Int sin =", sp.simplify(I_cos - sp.I*I_sin), " = 1/(a + 2 i eta)")
print("  => limite a->0 : 1/(2 i eta) = -i/(2 eta) ; partie imaginaire -1/(2 eta) = -Int sin ; eta * Int sin = +1/2")
# controle numerique direct (quadrature amortie, independante de quadosc)
aval = mpm.mpf(1)/1000
for e in ('-0.1', '-0.05', '-0.02', '0.05'):
    ee = mpm.mpf(e)
    val = mpm.quad(lambda kk: mpm.sin(2*kk*ee)*mpm.exp(-aval*kk), mpm.linspace(0, 20000, 4001))
    print("  eta =", e, " eta*Int (quad par morceaux) =", mpm.nstr(ee*val, 12),
          " forme fermee =", mpm.nstr(2*ee**2/(aval**2 + 4*ee**2), 12))
print("Conclusion : la quantite imprimee par le script tend vers +1/2 (quel que soit le signe de eta) ; l'annotation « attendu -1/2 » est fausse (signe).")

print("\n== Formule Gamma(4-N) (2 i eta)^{N-4} (regularisation d'Abel e^{-ak}, a->0+) ==")
N = sp.symbols('N', positive=True)
I_abel = sp.gamma(4 - N)*(a + 2*sp.I*eta)**(N - 4)   # Int_0^inf k^{3-N} e^{-(a+2 i eta) k} dk, Re(a)>0, N<4
print("Int_0^inf k^{3-N} e^{-(a + 2i eta)k} dk = Gamma(4-N) (a + 2 i eta)^{N-4}  [derive : transformee de Laplace, Re a > 0, N < 4]")
for Nv in (mpm.mpf('2.5'), mpm.mpf(3), mpm.mpf('3.5')):
    ee = mpm.mpf('-0.3'); aa = mpm.mpf('1e-4')
    num = mpm.quad(lambda kk: kk**(3 - Nv)*mpm.exp(-(aa + 2j*ee)*kk), mpm.linspace(0, 4000, 2001))
    theo = mpm.gamma(4 - Nv)*(2j*ee)**(Nv - 4)
    print("  N =", Nv, " quad (a=1e-4) =", mpm.nstr(num, 10), " Gamma(4-N)(2 i eta)^{N-4} =", mpm.nstr(theo, 10))
print("  N = 4 : Int_K0^inf dk k^{-1} e^{-2ik eta} = E_1(2 i eta K0) ~ -gamma_E - log(2 i eta K0) + ... : log|eta|, coupure IR K0 necessaire")
print("  N >= 5 : Int_0 dk k^{3-N} diverge en k -> 0 pour tout eta : coupure IR necessaire, pas de loi en eta sans elle")

print("\n== Gaussienne : I(eta) = Int_0^inf k^3 e^{-k^2/L^2} e^{-2ik eta} dk, controle numerique de l'expression sympy du script ==")
L = sp.symbols('L', positive=True)
expr = sp.I*sp.sqrt(sp.pi)*L**7*eta**3*sp.exp(-L**2*eta**2)*sp.erfc(sp.I*L*eta)/2 - L**6*eta**2/2 \
       - 3*sp.I*sp.sqrt(sp.pi)*L**5*eta*sp.exp(-L**2*eta**2)*sp.erfc(sp.I*L*eta)/4 + L**4/2
for ev in ('-0.7', '-0.05', '0.0'):
    Lv = mpm.mpf('1.3'); ee = mpm.mpf(ev)
    num = mpm.quad(lambda kk: kk**3*mpm.exp(-kk**2/Lv**2)*mpm.exp(-2j*kk*ee), [0, mpm.inf])
    sym = complex(expr.subs({L: sp.Float(1.3, 30), eta: sp.Float(ev, 30)}).evalf(25))
    print("  eta =", ev, " quad =", mpm.nstr(num, 12), " expression du script =", sym)
print("  borne uniforme : |I(eta)| <= Int k^3 e^{-k^2/L^2} dk = L^4/2 pour tout eta reel  [derive]")

print("\n== Tache 5 : borne generale ==")
print("  T^tf_ij(eta) = (2 pi)^{-3} Int dk k^3 Re[ e^{-2ik eta} M_ij(k) ],  M_ij(k) = Int dOmega F(k,Omega) (n_i n_j - delta_ij/3)")
print("  |M_ij(k)| <= (2/3) Int dOmega |F(k,Omega)|  =>  |T^tf_ij(eta)| <= (2/3)(2pi)^{-3} Int d^3k k |F(k)|  pour tout eta  [derive]")
print("  Si F decroit rapidement (uniformement en direction), le membre de droite est fini : T^tf borne, continu (Riemann-Lebesgue),")
print("  meme C^infini si tous les moments existent. Un comportement en 1/eta est donc impossible. La dependance angulaire n'y change rien.")
print("  Le 1/eta du cas N=3 provient de la queue k -> infini (k ~ 1/|eta|), pas de l'infrarouge.")

print("\n== Tache 5 : cas limite, decroissance rapide direction par direction mais NON uniforme ==")
print("  F(k,theta) = i exp(-k^2 theta^{4/3}) (theta = angle polaire) : gaussien pour chaque theta > 0, mais F = i sur l'axe theta = 0.")
# M_zz(k) = 2 pi Int_0^pi sin(th) (cos^2 th - 1/3) exp(-k^2 th^{4/3}) dth ; attendu ~ c k^{-3}, c = 2pi (2/3) Int_0^inf u e^{-u^{4/3}} du
c_th = 2*mpm.pi*(mpm.mpf(2)/3)*mpm.quad(lambda u: u*mpm.exp(-u**(mpm.mpf(4)/3)), [0, mpm.inf])
def Mzz(kk):
    return 2*mpm.pi*mpm.quad(lambda th: mpm.sin(th)*(mpm.cos(th)**2 - mpm.mpf(1)/3)*mpm.exp(-kk**2*th**(mpm.mpf(4)/3)), [0, mpm.pi])
for kv in (5, 20, 80, 320):
    print("  k =", kv, " k^3 M_zz(k) =", mpm.nstr(kv**3*Mzz(mpm.mpf(kv)), 8), "  (limite theorique c =", mpm.nstr(c_th, 8), ")")
print("  => k^3 M_zz(k) -> c != 0 : le moment angulaire se comporte comme k^{-3}, i.e. N = 3 effectif, donc")
print("     T^tf_zz(eta) = (2pi)^{-3} Int dk k^3 M_zz(k) sin(2 k eta) ~ c/(2 eta) (2pi)^{-3} quand eta -> 0 :")
# verification numerique de eta * Int dk k^3 M_zz(k) sin(2 k eta) -> c/2 (amortissement e^{-a k}, a petit)
# tabulation de k^3 M_zz sur une grille et interpolation lineaire pour la quadrature oscillante
grid = [mpm.mpf(0)] + [mpm.mpf(2)**(j/mpm.mpf(4)) for j in range(-16, 60)]
tab = [(kk, kk**3*Mzz(kk) if kk > 0 else mpm.mpf(0)) for kk in grid]
def k3M(kk):
    if kk >= tab[-1][0]:
        return c_th
    lo, hi = 0, len(tab) - 1
    while hi - lo > 1:
        mid = (lo + hi)//2
        if tab[mid][0] <= kk: lo = mid
        else: hi = mid
    (k0, v0), (k1, v1) = tab[lo], tab[hi]
    return v0 + (v1 - v0)*(kk - k0)/(k1 - k0)
aa = mpm.mpf('5e-4')
for ev in ('-0.2', '-0.1', '-0.05'):
    ee = mpm.mpf(ev)
    val = mpm.quad(lambda kk: k3M(kk)*mpm.sin(2*kk*ee)*mpm.exp(-aa*kk), mpm.linspace(0, 20000, 2001))
    print("  eta =", ev, " eta * Int dk k^3 M_zz sin(2k eta) e^{-ak} =", mpm.nstr(ee*val, 8), "  (c/2 =", mpm.nstr(c_th/2, 8), ")")
print("  Ce cas n'est PAS un contre-exemple au sens strict : F n'est pas a decroissance rapide sur R^3 (pas de decroissance sur l'axe),")
print("  donc l'etat n'est pas Hadamard (singularite du cone reflechi conservee dans la direction de l'axe).")
