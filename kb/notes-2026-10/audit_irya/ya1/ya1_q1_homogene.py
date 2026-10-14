#!/usr/bin/env python3
# YA-1, question 1 : classe homogene (Bogoliubov), comportement en eta -> 0^- de
#   w(x,x) et de T^w ~ dd w |_coinc, pour alpha beta* ~ k^{-N} e^{i phi} (classe b)
#   et alpha beta* a decroissance rapide (classe a).
#
# Conventions (derivees a la main, verifiees ci-dessous) :
#   omega_2(x,x') = int d^3k/(2pi)^3 v_k(x) v_k^*(x'),  v_k = alpha u_k + beta u_k^*
#   w = omega_2 - H, et apres integration angulaire (alpha,beta isotropes) :
#   w(x,x') = (1/4pi^2) int_0^inf k dk [sin(kr)/(kr)] { 2|beta|^2 cos(k(eta-eta'))
#                                              + 2 Re[alpha beta^* e^{-ik(eta+eta')}] }
#   Coincidence : w(x,x)      = (1/2pi^2) int k   dk { |beta|^2 + Re[ab* e^{-2ik eta}] }
#                 d_eta d_eta' w|c = (1/2pi^2) int k^3 dk { |beta|^2 - Re[ab* e^{-2ik eta}] }
#                 sum_i d_i d_i' w|c = (1/2pi^2) int k^3 dk { |beta|^2 + Re[ab* e^{-2ik eta}] }
#   La partie oscillante (dependante de eta) est J(eta) = (1/2pi^2) int k^3 Re[ab* e^{-2ik eta}] dk.
#
# Modele UV de la classe (b) : alpha beta^* = e^{i phi} k^{-N} pour k >= 1 (coupure IR a k=1,
# sans effet sur le comportement UV / eta -> 0). Alors
#   int_1^inf k^{3-N} e^{-2 i k eta} dk = E_{N-3}(2 i eta)   (exponentielle integrale generalisee)
#   int_1^inf k^{1-N} e^{-2 i k eta} dk = E_{N-1}(2 i eta)

import sympy as sp
import mpmath as mp

mp.mp.dps = 30
out = []
def P(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

P("=== YA1 Q1 : classe homogene ===")

# ---------- 0. Verification symbolique de la structure de w ----------
eta, etap, k, phi = sp.symbols('eta etap k phi', real=True)
r = sp.symbols('r', positive=True)
A2, B2 = sp.symbols('A2 B2', positive=True)          # |alpha|^2, |beta|^2
AB = sp.symbols('AB')                                 # alpha beta^*
ABc = sp.symbols('ABc')                               # alpha^* beta
Ph, Phinv = sp.symbols('Ph Phinv')                    # e^{ik.(x-x')} et son inverse
u, up = sp.exp(-sp.I*k*eta), sp.exp(-sp.I*k*etap)
# v(x) v^*(x') = |a|^2 u u'^* + |b|^2 u^* u' + a b^* u u' + a^* b u^* u'^* (phases spatiales : Ph pour u u'^*, u u' ; Phinv pour les conjugues)
expr = (A2*u*sp.conjugate(up)*Ph + B2*sp.conjugate(u)*up*Phinv + AB*u*up*Ph + ABc*sp.conjugate(u)*sp.conjugate(up)*Phinv)
vac = u*sp.conjugate(up)*Ph
wint = sp.expand((expr - vac).subs(A2, 1 + B2))
P("[derive] integrand de w (par mode, facteur 1/(2k) omis), avec |alpha|^2 = 1 + |beta|^2 :")
P("   ", wint)
P("   -> termes |beta|^2 (dependent de eta-eta') et alpha beta^* e^{-ik(eta+eta')} Ph + c.c. (dependent de eta+eta')")

# Derivatives at coincidence of the alpha beta* term : d_eta d_eta' e^{-ik(eta+eta')} = -k^2 ; spatial d_i d_i' e^{ik.(x-x')} = +k_i^2
P("[derive] d_eta d_eta' e^{-ik(eta+eta')} =", sp.simplify(sp.diff(sp.exp(-sp.I*k*(eta+etap)), eta, etap)/sp.exp(-sp.I*k*(eta+etap))))
P("[derive] d_eta d_eta' e^{-ik(eta-eta')} =", sp.simplify(sp.diff(sp.exp(-sp.I*k*(eta-etap)), eta, etap)/sp.exp(-sp.I*k*(eta-etap))))
P("   => la densite d'energie rho^w = (1/2)(d_eta d_eta' + sum_i d_i d_i') w|c ne contient PAS le terme alpha beta^* (champ sans masse),")
P("      la pression p^w = (1/2 d_eta d_eta' - 1/6 sum_i d_i d_i') w|c en contient -2/3 J(eta).")

# ---------- 1. Classe (b) : formes fermees et developpements en eta -> 0 ----------
z = sp.symbols('z')
P("")
P("[calcule] Classe (b) : J_N(eta) := int_1^inf k^{3-N} e^{-2 i k eta} dk = E_{N-3}(2 i eta) ; developpement en eta -> 0")
for N in [3, 4, 5, 6, 7]:
    n = N - 3
    if n == 0:
        EN = sp.exp(-z)/z
    else:
        EN = sp.expint(n, z)
    ser = sp.series(EN, z, 0, 3).removeO()
    P(f"  N={N} : E_{n}(z) = {ser} + O(z^3),  z = 2 i eta")
P("  Lecture : N=3 -> 1/z ~ 1/eta ; N=4 -> -log z ; N=5 -> fini, derivee ~ log ; N=6 -> C^1, derivee seconde ~ log ; N=7 -> C^2 ...")
P("  Terme reel : Re[e^{i phi} E_0(2 i eta)] = Re[e^{i phi} e^{-2 i eta}/(2 i eta)] = sin(phi - 2 eta)/(2 eta)")
expr0 = sp.re(sp.exp(sp.I*phi)*sp.exp(-2*sp.I*eta)/(2*sp.I*eta))
P("  [calcule] sympy :", sp.simplify(sp.expand_complex(expr0)))

# Coincidence w(x,x) : int_1^inf k^{1-N} e^{-2 i k eta} dk = E_{N-1}(2 i eta)
P("")
P("[calcule] w(x,x) oscillant : int_1^inf k^{1-N} e^{-2 i k eta} dk = E_{N-1}(2 i eta)")
for N in [1, 2, 3, 4]:
    n = N - 1
    EN = sp.exp(-z)/z if n == 0 else sp.expint(n, z)
    P(f"  N={N} : {sp.series(EN, z, 0, 3).removeO()} + O(z^3)")
P("  Lecture : w(x,x) ~ 1/eta pour N=1, log pour N=2, fini (C^0, terme eta log eta) pour N=3.")

# ---------- 2. Verification numerique independante (quadosc) et exposant local ----------
P("")
P("[calcule] Verification numerique : J_N(eta) par quadrature oscillante vs forme fermee, phi = pi/2 (sin phi = 1)")
phi_v = mp.pi/2
def J_closed(N, et):
    zz = 2j*et
    En = mp.exp(-zz)/zz if N == 3 else mp.expint(N-3, zz)
    return mp.re(mp.exp(1j*phi_v)*En)
def J_quad(N, et):
    f = lambda kk: kk**(3-N)*mp.cos(phi_v - 2*kk*et)
    return mp.quadosc(f, [1, mp.inf], omega=2*abs(et))
for N in [3, 4, 5, 6]:
    P(f"  N = {N}")
    prev = None
    for e in [mp.mpf('-0.1'), mp.mpf('-0.01'), mp.mpf('-0.001'), mp.mpf('-0.0001')]:
        jc = J_closed(N, e)
        jq = J_quad(N, e) if N <= 5 else None
        line = f"    eta={mp.nstr(e,5):>8}  J_closed={mp.nstr(jc,12):>18}"
        if jq is not None:
            line += f"  J_quadosc={mp.nstr(jq,12):>18}  diff={mp.nstr(jc-jq,3)}"
        if N == 3:
            line += f"   eta*J={mp.nstr(e*jc,8)}  (attendu -> sin(phi)/2 = 0.5)"
        if N == 4:
            line += f"   J/ln|eta|={mp.nstr(jc/mp.log(abs(e)),8)}  (attendu -> -cos(phi) = 0)  J-(-ln(2|eta|)*cos phi + (pi/2)sgn... )"
        P(line)
# For N=4 use phi=0 to show the log clearly
P("  N = 4, phi = 0 (cos phi = 1) : J ~ -ln(2|eta|) - gamma")
for e in [mp.mpf('-0.1'), mp.mpf('-0.01'), mp.mpf('-0.001')]:
    zz = 2j*e
    jc = mp.re(mp.expint(1, zz))
    P(f"    eta={mp.nstr(e,5):>8}  Re E_1(2i eta)={mp.nstr(jc,10)}   -ln(2|eta|)-gamma={mp.nstr(-mp.log(2*abs(e))-mp.euler,10)}")

# Regularity in eta=0 for N>=5 : m-th derivative of J_N ~ int k^{3-N+m} : finite iff m <= N-5 (log at m=N-4)
P("")
P("[derive] Regularite en eta=0 (classe b) : d^m J_N / d eta^m = (-2i)^m int_1^inf k^{3-N+m} e^{-2ik eta} dk")
P("         fini et continu en 0 ssi 3-N+m < -1, i.e. m <= N-5 ; divergence logarithmique pour m = N-4 ; puissance |eta|^{N-4-m} pour m > N-4.")
P("         => J_N est C^{N-5} mais pas C^{N-4} : lisse (C^inf) pour AUCUN N fini.")
# numeric check: N=6, second derivative diverges like log
P("[calcule] Exemple N=6 : J''(eta) numerique (phi=0) vs ln :")
for e in [mp.mpf('-0.1'), mp.mpf('-0.01'), mp.mpf('-0.001')]:
    f = lambda t: mp.re(mp.expint(3, 2j*t))
    d2 = mp.diff(f, e, 2)
    P(f"    eta={mp.nstr(e,5):>8}  J''={mp.nstr(d2,10)}   4*ln(2|eta|) = {mp.nstr(4*mp.log(2*abs(e)),10)}  (pente attendue : J''(eta/10)-J''(eta) -> 4 ln(1/10) = {mp.nstr(4*mp.log(mp.mpf(1)/10),8)})")

# ---------- 3. Classe (a) : decroissance rapide -> lisse a travers eta = 0 ----------
P("")
P("[calcule] Classe (a) : alpha beta^* = e^{i phi} e^{-k/kc}. J(eta) = Re[e^{i phi} int_0^inf k^3 e^{-k(1/kc + 2 i eta)} dk]")
kc = sp.symbols('k_c', positive=True)
Ja = sp.integrate(k**3*sp.exp(-k*(1/kc + 2*sp.I*eta)), (k, 0, sp.oo), conds='none')
P("   int = ", sp.simplify(Ja), " : fonction analytique (reelle-analytique) de eta sur tout R, poles en eta = +- i/(2 kc) seulement.")
P("   Gaussienne alpha beta^* = e^{i phi} e^{-k^2/kc^2} : int_0^inf k^3 e^{-k^2/kc^2 - 2 i k eta} dk est une fonction entiere de eta (transformee de Fourier d'une gaussienne tronquee, tous les moments finis).")
P("   [derive] Argument general : si int_0^inf k^{3+m} |alpha_k beta_k^*| dk < inf pour tout m, la derivation sous le signe somme est licite a tout ordre et J est C^inf sur R, y compris a travers eta = 0.")

# ---------- 4. Resume Q1 ----------
P("")
P("[derive] RESUME Q1 :")
P("  * terme dependant de l'etat : w = w_{|beta|^2}(eta-eta', x-x') + w_{ab*}(eta+eta', x-x') ; w_{ab*} = int d^3k/((2pi)^3 2k) alpha beta^* e^{-ik(eta+eta') + ik.(x-x')} + c.c.")
P("  * (a) decroissance rapide : w(x,x) et T^w lisses en eta=0 (prolongement C^inf, voire analytique).")
P("  * (b) alpha beta^* ~ k^{-N} e^{i phi} : T^w_osc ~ Re[e^{i phi} Gamma(4-N) (2 i eta)^{N-4}] ; 1/eta  <=>  N = 3 (coefficient sin(phi)/(4 pi^2 eta) dans d_eta d_eta' w) ; N=4 : log ; N>=5 : fini mais seulement C^{N-5} ; lisse pour aucun N fini.")
P("  * w(x,x) : 1/eta pour N=1, log pour N=2, C^0 (terme eta ln|eta|) pour N=3.")

with open('/home/claude/audit_ya1/work/ya1_q1_homogene.out', 'w') as fh:
    fh.write("\n".join(out) + "\n")
