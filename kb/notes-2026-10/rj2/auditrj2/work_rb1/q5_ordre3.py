# Q5/Q6 : source d'ordre eps^3 de l'equation du spineur et test de resonance
#   i Dslash_0 psi3 - (m/Omega) psi3 = S := -i deltaD[h] psi1
#   resonance <=> coefficient de Omega^{-1 + i mu} projete sur P+ (ou de Omega^{-1 - i mu} sur P-) non nul
import sympy as sp, pickle, sys
from conv import gu, gl, eta, E4, I, g0
from deltaD import deltaD
from spinors import mode, mu, Om

t, x, y, z = sp.symbols('t x y z', real=True); X = (t, x, y, z)
sh, sp_ = sp.symbols('s_h s_psi')
q = sp.symbols('q1:4', real=True); p = sp.symbols('p1:4', real=True)
Hs = sp.Matrix(4, 4, lambda a, b: sp.Symbol('H%d%d' % (min(a, b), max(a, b))))
C = sp.Matrix(sp.symbols('C0:4'))
Pp = (E4 + g0)/2; Pm = (E4 - g0)/2

# forme generique : S = -i deltaD[h] psi pour h = H Omega^{s_h} e^{iqx}, psi = C Omega^{s_psi} e^{ipx}
ph = (-t)**sh*sp.exp(I*(q[0]*x + q[1]*y + q[2]*z)); pp = (-t)**sp_*sp.exp(I*(p[0]*x + p[1]*y + p[2]*z))
S = -I*deltaD(Hs*ph, C*pp, X)
S = (S/((-t)**(sh + sp_ - 1)*sp.exp(I*((q[0]+p[0])*x + (q[1]+p[1])*y + (q[2]+p[2])*z)))).applyfunc(lambda e: sp.expand(sp.simplify(e)))
S = S.subs(t, -Om).applyfunc(sp.expand)
A = S.applyfunc(lambda e: e.coeff(Om, 0))     # partie Omega^{s_h+s_psi-1}  (seule capable de resonner)
B = S.applyfunc(lambda e: e.coeff(Om, 1))
print("S = Omega^{s_h+s_psi-1} [A + Omega B] :", sp.simplify(S - A - Om*B) == sp.zeros(4, 1))
print("A(s_h, s_psi) (coefficient pouvant resonner) =")
for i in range(4):
    print("   ", sp.factor(A[i]))
# A ne depend que de s_h * H (derivee temporelle de h) et de H_{0 mu} s_psi : verification
A_s0 = A.subs(sh, 0)
print("A a s_h = 0 ne depend que de H00, H0i :", (A_s0.free_symbols & set(Hs[1:, 1:])) == set())

if __name__ == "__main__":
    fn = sys.argv[1]
    results, NH, MUNUM = pickle.load(open(fn, 'rb'))
    m = mu if MUNUM is None else sp.Rational(MUNUM)
    print("\n=== Coefficients d'ordre Omega^0 de h dans la solution calculee (", fn, ")")
    for lab, (qv, T, sols) in results.items():
        for j, Sx in sols.items():
            unk, d, free = Sx
            H0 = {(a, b): sp.simplify(sp.sympify(d[unk[(0, a, b)]])) for (n, a, b) in unk if n == 0}
            print("  secteur", lab, "j =", j, ": h^(0) =", {k: v for k, v in H0.items() if v != 0}, "(h_0i = 0 par jauge)")
            # resonance : psi j_psi = +-1, ordre 0 ; h ordre 0 j ; exposant total -1 + i(j + j_psi) mu
            for jpsi, P, lab2 in ((1, Pp, 'P+'), (-1, Pm, 'P-')):
                if j + jpsi not in (1, -1):
                    continue
                Pres = Pp if j + jpsi == 1 else Pm
                Hsub = {Hs[a, b]: 0 for a in range(4) for b in range(4)}
                for (a, b), v in H0.items():
                    Hsub[sp.Symbol('H%d%d' % (a, b))] = v
                Hsub[sp.Symbol('H33')] = -H0[(1, 1)] - H0[(2, 2)]
                for i_ in (1, 2, 3):
                    Hsub[sp.Symbol('H0%d' % i_)] = 0
                Cgen = P*C   # composante d'ordre 0 du spineur, dans le bon sous-espace
                val = (Pres*A.subs(Hsub).subs({sh: I*j*m, sp_: I*jpsi*m}).subs(dict(zip(C, Cgen)))).applyfunc(sp.simplify)
                print("     resonance Omega^{-1%+di mu} : projection = %s" % (j + jpsi, list(val)))
    # contre-test de sensibilite : si h avait un lapse Omega^0 (j=0) ou un terme Omega^{0 + 2 i mu}, la projection serait non nulle
    print("\n=== Contre-tests (sensibilite du critere)")
    sub0 = {Hs[a, b]: 0 for a in range(4) for b in range(4)}
    v1 = (Pp*A.subs({**sub0, Hs[0, 0]: sp.Symbol('L')}).subs({sh: 0, sp_: I*m}).subs(dict(zip(C, Pp*C)))).applyfunc(sp.simplify)
    print("  lapse h_00 = L Omega^0 (j=0), psi ~ Omega^{i mu} P+ C : P+ S_{-1+i mu} =", list(v1))
    v2 = (Pp*A.subs({**sub0, Hs[1, 1]: sp.Symbol('W'), Hs[2, 2]: -sp.Symbol('W')}).subs({sh: 2*I*m, sp_: -I*m}).subs(dict(zip(C, Pm*C)))).applyfunc(sp.simplify)
    print("  h_11 = -h_22 = W Omega^{0+2i mu}, psi ~ Omega^{-i mu} P- C : P+ S_{-1+i mu} =", list(v2))
    v3 = (Pp*A.subs({**sub0, Hs[0, 0]: sp.Symbol('L2')}).subs({sh: 2*I*m, sp_: -I*m}).subs(dict(zip(C, Pm*C)))).applyfunc(sp.simplify)
    print("  h_00 = L2 Omega^{0+2i mu}, psi ~ Omega^{-i mu} P- C : P+ S_{-1+i mu} =", list(v3))
    v4 = (Pp*A.subs({**sub0, Hs[1, 1]: sp.Symbol('W'), Hs[2, 2]: sp.Symbol('W'), Hs[3, 3]: sp.Symbol('W')}).subs({sh: 2*I*m, sp_: -I*m}).subs(dict(zip(C, Pm*C)))).applyfunc(sp.simplify)
    print("  h_ij = W delta_ij Omega^{0+2i mu} (trace), psi ~ Omega^{-i mu} P- C : P+ S_{-1+i mu} =", list(v4))
    v5 = (Pp*A.subs({**sub0, Hs[0, 1]: sp.Symbol('V')}).subs({sh: 2*I*m, sp_: -I*m}).subs(dict(zip(C, Pm*C)))).applyfunc(sp.simplify)
    print("  decalage h_01 = V Omega^{0+2i mu} (hors de notre jauge), psi ~ Omega^{-i mu} P- C : P+ S_{-1+i mu} =", list(v5))
    v6 = (Pp*A.subs({**sub0, Hs[0, 1]: sp.Symbol('V0')}).subs({sh: 0, sp_: I*m}).subs(dict(zip(C, Pp*C)))).applyfunc(sp.simplify)
    print("  decalage h_01 = V0 Omega^0 (j=0), psi ~ Omega^{i mu} P+ C : P+ S_{-1+i mu} =", list(v6))
