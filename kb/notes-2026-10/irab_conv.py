# irab_conv.py -- IR-ab (NOTE-153) : conversions de normalisation entre [8] 2412.11022, [27] 2405.01024 et le programme.
# kappa_W^2 = 16 pi G (Woodard) ; kappa = 8 pi G (programme) ; b = (N_S + 6 N_F + 12 N_V)/(120 (4 pi)^2).
import sympy as sp
G, H, D, mu = sp.symbols('G H D mu', positive=True)
kW2 = 16*sp.pi*G
kappa = 8*sp.pi*G
def b(NS, NF, NV): return sp.Rational(NS + 6*NF + 12*NV, 120)/(4*sp.pi)**2

print("== ab-1 : coefficient du logarithme, photon, [8] eq. (53) ==")
c_photon_src = kW2*H**2/(40*sp.pi**2)
c_photon_prog = 8*b(0,0,1)*kappa*H**2
print("[8] eq.53 :", sp.simplify(c_photon_src), "   programme 8 b kappa H^2 (N_V=1) :", sp.simplify(c_photon_prog),
      "   egaux :", sp.simplify(c_photon_src - c_photon_prog) == 0)
print("[8] eq.60 (hbar=c=1) : 2 G H^2/(5 pi) =", sp.simplify(2*G*H**2/(5*sp.pi) - c_photon_src) == 0)
print("rapport photon/Dirac (Dirac = G H^2/(5 pi), NOTE-148) :", sp.simplify(c_photon_src/(G*H**2/(5*sp.pi))))

print("\n== ab-2 : gamma de [8] eq. (58) a partir de c_2 eq. (56), c_1 = 0 ==")
c2 = mu**(D-4)/(D-4) * sp.gamma(D/2)/(2**8*sp.pi**(D/2)) * (D-2)*D/((D+1)*(D-3)**2)
dZ = D*(2*(D-1)*0 - c2)*kW2*H**2
# d/d ln(mu^2) = (mu/2) d/dmu
gamma = sp.limit(sp.simplify((mu/2)*sp.diff(dZ, mu)), D, 4)
print("gamma (D->4) =", sp.simplify(gamma), "   source : -kappa_W^2 H^2/(80 pi^2) =", sp.simplify(-kW2*H**2/(80*sp.pi**2)),
      "   egaux :", sp.simplify(gamma + kW2*H**2/(80*sp.pi**2)) == 0)
print("exposant resomme = -2 gamma =", sp.simplify(-2*gamma), " = coefficient du log (53) :", sp.simplify(-2*gamma - c_photon_src) == 0)

print("\n== ab-2 bis : [27] eq. (91), scalaire MMC, c_1 et c_2 eq. (85)-(86) ==")
c1s = mu**(D-4)*sp.gamma(D/2)/(2**8*sp.pi**(D/2)) * (D-2)/((D-1)**2*(D-3)*(D-4))
c2s = mu**(D-4)*sp.gamma(D/2)/(2**8*sp.pi**(D/2)) * 2/((D+1)*(D-1)*(D-3)**2*(D-4))
dZs = D*(2*(D-1)*c1s - c2s)*kW2*H**2
gs = sp.limit(sp.simplify((mu/2)*sp.diff(dZs, mu)), D, 4)
print("gamma_MMC (D->4) =", sp.simplify(gs), "   source : 3 G H^2/(20 pi) ; egaux :", sp.simplify(gs - 3*G*H**2/(20*sp.pi)) == 0)
print("exposant -2 gamma_MMC =", sp.simplify(-2*gs), " ; [27] eq. (93) : -3 G H^2/(10 pi)")

print("\n== structure : champ conforme => c_1 = 0 => delta Z = -D c_2 kappa_W^2 H^2 ; exposant fixe par le seul contre-terme de Weyl (NOTE-137) ==")
# exposant = -2 gamma = D kappa_W^2 H^2 (dc2/dln mu^2)|D=4 = 4 kappa_W^2 H^2 * (residu de c2) ; residu = b (HHR) pour le photon ?
res_c2 = sp.limit(sp.simplify((mu/2)*sp.diff(c2, mu)), D, 4)   # = (D-4)/2 * c2 -> partie finie
print("residu de c_2 (photon) =", sp.simplify(res_c2), "   b_V (programme) =", b(0,0,1), "   egaux :", sp.simplify(res_c2 - b(0,0,1)) == 0)
print("8 b kappa = 4 kappa_W^2 b :", sp.simplify(8*b(0,0,1)*kappa - 4*kW2*b(0,0,1)) == 0)
res_c2_lnmu = sp.limit(sp.simplify(mu*sp.diff(c2, mu)), D, 4)   # d c_2 / d ln mu
print("d c_2/d ln mu (photon) =", sp.simplify(res_c2_lnmu), "   = b_V :", sp.simplify(res_c2_lnmu - b(0,0,1)) == 0,
      "   (la lecture 'c_2 = b' de NOTE-137 vaut pour la derivee en ln mu ; en ln mu^2 c'est b/2)")
