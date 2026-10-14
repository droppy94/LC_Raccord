# Verification du noyau retarde K_k(T) de ln(k^2 - (omega+i0)^2) par une identite d'action sur une fonction test.
# Convention du script : f(T) = Int domega/(2pi) e^{-i omega T} f~(omega), donc f~(omega) = Int dT e^{i omega T} f(T).
# Test : f(T) = e^{-T^2}  ->  f~(omega) = sqrt(pi) e^{-omega^2/4}.
# Cote frequence : Int domega/(2pi) f~(omega) ln(k^2 - (omega+i0)^2) ; parties imaginaires (+-i pi pour |omega|>k) s'annulent par parite.
# Cote temps : Int dT K(T) f(T) avec K = -2 [theta(T) cos(kT)/T]_+ (Hadamard echelle 1) + c delta(T).
# On extrait c(k) = (cote frequence) - (partie non locale), et on le compare a des candidats.
from mpmath import mp, mpf, quad, quadosc, exp, cos, log, sqrt, pi, euler, inf, ci, sin
mp.dps = 20
f = lambda T: exp(-T**2)
ft = lambda w: sqrt(pi)*exp(-w**2/4)
for kv in (mpf(1), mpf(2), mpf('0.5')):
    freq = (1/(2*pi))*(quad(lambda w: ft(w)*log(abs(kv**2 - w**2)), [-inf, -kv, 0, kv, inf]))
    # partie non locale Hadamard a l'echelle 1
    nl = quad(lambda T: (f(T) - 1)*(-2*cos(kv*T)/T), [0, 1]) + quadosc(lambda T: f(T)*(-2*cos(kv*T)/T), [1, inf], omega=kv)
    c = freq - nl
    # candidats : -2 gamma_E ; -2 gamma_E - 2 ln k ; -2 Ci(k) ; 2(Ci(k) - gamma - ln k)
    print(f"k = {kv} : cote frequence = {freq}, partie non locale = {nl}, c(k) = {c}")
    print(f"    candidats : -2 gamma_E = {-2*euler}, -2(gamma_E + ln k) = {-2*(euler+log(kv))}, -2 Ci(k) = {-2*ci(kv)}, 2(Ci(k)-gamma_E-ln k) = {2*(ci(kv)-euler-log(kv))}")
# Test de la dependance en l'echelle L de Hadamard : difference attendue 2 f(0) [Ci(kL) - Ci(k)]
kv = mpf(1)
for L in (mpf('0.1'), mpf(1), mpf(10)):
    nlL = quad(lambda T: (f(T) - 1)*(-2*cos(kv*T)/T), [0, L]) + quadosc(lambda T: f(T)*(-2*cos(kv*T)/T), [L, inf], omega=kv)
    print(f"L = {L} : partie non locale = {nlL} ; prediction nl(1) + 2 f(0)(Ci(kL)-Ci(k)) = {nl if False else None}")
nl1 = quad(lambda T: (f(T) - 1)*(-2*cos(kv*T)/T), [0, 1]) + quadosc(lambda T: f(T)*(-2*cos(kv*T)/T), [1, inf], omega=kv)
for L in (mpf('0.1'), mpf(10)):
    nlL = quad(lambda T: (f(T) - 1)*(-2*cos(kv*T)/T), [0, L]) + quadosc(lambda T: f(T)*(-2*cos(kv*T)/T), [L, inf], omega=kv)
    print(f"L = {L} : nl(L) - nl(1) = {nlL - nl1} ; 2 f(0)(Ci(kL) - Ci(k)) = {2*(ci(kv*L)-ci(kv))}")
# Controle de Frullani (reproduit)
print("Frullani Int_0^inf (cos T - cos 3T)/T dT =", quadosc(lambda T: (cos(T)-cos(3*T))/T, [0, inf], omega=3), " ln 3 =", log(3))
