# NOTE-166, T-4 : releve numerique de la coincidence entre l'exposant du pole G-V3
# epsilon = 8 b kappa H^2 et l'inverse de l'entropie de de Sitter 1/S_dS.
# Aucun verdict : simple releve (gel NOTE-165 §2, FW-T5). Unites hbar = c = 1.
# Conventions du programme (NOTE-138 v4, NOTE-153) : kappa = 8 pi G ;
# b = (N_S + 6 N_F + 12 N_V) / (120 (4 pi)^2)  (coefficient de l'anomalie sur C^2).
# S_dS = A/(4G) = pi/(G H^2) [M, Gibbons-Hawking 1977] ; avec Lambda = 3 H^2 : S_dS = 3 pi/(G Lambda).
from fractions import Fraction as F
import math
pi = math.pi
def b_coeff(NS, NF, NV):           # fraction de 1/(120 (4pi)^2)
    return F(NS + 6*NF + 12*NV, 120)
print("espece       n=N_S+6N_F+12N_V   8 b kappa H^2 / (G H^2)      1/S_dS / (G H^2)    rapport epsilon*S_dS")
for nom, (NS, NF, NV) in {"scalaire (N_S=1)": (1,0,0), "Dirac (N_F=1)": (0,1,0), "photon (N_V=1)": (0,0,1)}.items():
    n = NS + 6*NF + 12*NV
    # 8 b kappa H^2 = 8 * n/(120 * 16 pi^2) * 8 pi G H^2 = n G H^2 /(30 pi)
    eps_over_GH2 = F(n, 30)          # en unites de G H^2 / pi
    inv_S_over_GH2 = F(1, 1)         # 1/S_dS = G H^2 / pi
    ratio = eps_over_GH2 / inv_S_over_GH2
    print(f"{nom:18s} {n:3d}            {str(eps_over_GH2):>6s} x GH^2/pi           GH^2/pi              {str(ratio)}")
# controle symbolique de l'identite 8 b kappa H^2 = n G H^2/(30 pi)
n = 1
lhs = 8 * (n/(120*(4*pi)**2)) * 8*pi
rhs = n/(30*pi)
print("controle 8*b*kappa (n=1) =", lhs, " n/(30 pi) =", rhs, " ecart relatif", abs(lhs-rhs)/rhs)
# recoupement avec les sources lues : FLT 1703.02076 (8 pi G = 1) donnent |exp(iS)| = exp(-+ 12 pi^2/Lambda).
# Avec 8 pi G = 1 : S_dS = 3 pi/(G Lambda) = 24 pi^2 / Lambda, donc 12 pi^2/Lambda = S_dS / 2.
G = 1/(8*pi); Lam = 1.0
S_dS = 3*pi/(G*Lam); print("8piG=1 : S_dS =", S_dS, " 24 pi^2 =", 24*pi**2, " 12 pi^2/Lambda / S_dS =", (12*pi**2/Lam)/S_dS)
# ordre de grandeur avec H_0 ~ 1.5e-33 eV, G = 1/M_P^2, M_P = 1.22e19 GeV (valeurs [M], declarees)
H = 1.5e-33; MP = 1.22e28  # eV
GH2 = (H/MP)**2
print("G H^2 (sans dimension) ~", GH2, " ; 1/S_dS = G H^2/pi ~", GH2/pi, " ; epsilon photon = 2 G H^2/(5 pi) ~", 2*GH2/(5*pi))
