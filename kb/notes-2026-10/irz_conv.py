# irz_conv.py : conversion des coefficients de Foraci-Woodard 2501.01972 (kappa_W^2 = 16 pi G) vers 8 b kappa du programme (kappa = 8 pi G, b = (N_S + 6 N_F + 12 N_V)/(120 (4 pi)^2)), H = 1.
import sympy as sp
G = sp.symbols('G', positive=True); pi = sp.pi
kW2 = 16*pi*G; kappa = 8*pi*G
def b(NS, NF, NV): return sp.Rational(NS + 6*NF + 12*NV, 120)/(4*pi)**2
rows = [("Dirac (eq. 35/42)", kW2/(80*pi**2), 8*b(0,1,0)*kappa),
        ("scalaire conforme (eq. 46)", kW2/(480*pi**2), 8*b(1,0,0)*kappa),
        ("photon (= 2 x Dirac, p. 6)", 2*kW2/(80*pi**2), 8*b(0,0,1)*kappa)]
for name, fw, prog in rows:
    print(f"{name:30s} FW = {sp.simplify(fw)}   8 b kappa = {sp.simplify(prog)}   egal : {sp.simplify(fw-prog)==0}")
# gamma de l'eq. 40 et exposant : 2 gamma en ln mu -> exposant en ln a : -2 gamma x (d ln mu^2 / d ln a = ... ) ; verification : -2 x (-kW2/(160 pi^2)) = kW2/(80 pi^2)
print("exposant (42) = -2 gamma(40) :", sp.simplify(-2*(-kW2/(160*pi**2)) - kW2/(80*pi**2)) == 0)
