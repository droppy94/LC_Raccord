# Canaux de resonance a l'ordre eps^3, h GENERIQUE (10 composantes, toute jauge), terme d'ordre Omega^0 de h :
# h ~ H Omega^{0 + i jh mu},  psi ~ Omega^{i jpsi mu} P C,  source Omega^{-1 + i(jh+jpsi) mu} ; resonance si P_res A != 0
import sympy as sp
import q5_ordre3 as Q
from conv import E4, g0
mu = sp.Symbol('mu', positive=True); I = sp.I
Pp = (E4 + g0)/2; Pm = (E4 - g0)/2
for jh in (-2, 0, 2):
    for jpsi, Ppsi in ((1, Pp), (-1, Pm)):
        tot = jh + jpsi
        if tot not in (1, -1):
            continue
        Pres = Pp if tot == 1 else Pm
        v = (Pres*Q.A.subs({Q.sh: I*jh*mu, Q.sp_: I*jpsi*mu}).subs(dict(zip(Q.C, Ppsi*Q.C)))).applyfunc(sp.factor)
        Hin = sorted(map(str, set().union(*[e.free_symbols for e in v]) & set(map(lambda s_: s_, Q.Hs))))
        print("jh=%+d jpsi=%+d -> Omega^{-1%+di mu} : projection resonante =" % (jh, jpsi, tot), list(v), " | composantes de h impliquees :", Hin)
