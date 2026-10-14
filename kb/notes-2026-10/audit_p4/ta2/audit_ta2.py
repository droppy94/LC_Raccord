#!/usr/bin/env python3
# Audit TA-2 : relevé numérique indépendant. Unités hbar = c = 1.
# Fractions exactes : on travaille en coefficients rationnels sur une base
# monomiale {pi^a, G^b, H^c}, en manipulant pi symboliquement (exposant entier).
from fractions import Fraction as F
import math

# ---------- Représentation : coefficient rationnel * pi^p * G^g * H^h ----------
class Mono:
    def __init__(self, c, p=0, g=0, h=0):
        self.c, self.p, self.g, self.h = F(c), p, g, h
    def __mul__(self, o):
        return Mono(self.c*o.c, self.p+o.p, self.g+o.g, self.h+o.h)
    def __truediv__(self, o):
        return Mono(self.c/o.c, self.p-o.p, self.g-o.g, self.h-o.h)
    def __repr__(self):
        s = f"({self.c})"
        for name, e in (("pi", self.p), ("G", self.g), ("H", self.h)):
            if e: s += f"*{name}^{e}"
        return s
    def value(self, G, H):
        return float(self.c) * math.pi**self.p * G**self.g * H**self.h

PI = Mono(1, p=1)
G  = Mono(1, g=1)
H  = Mono(1, h=1)

def b_of(NS, NF, NV):
    n = NS + 6*NF + 12*NV
    # b = n / (120 (4 pi)^2) = n / (1920 pi^2)
    return Mono(F(n, 120*16), p=-2), n

kappa = Mono(8) * PI * G            # 8 pi G
A     = Mono(4) * PI / (H*H)        # 4 pi / H^2
S_dS  = A / (Mono(4) * G)           # A/(4G) = pi/(G H^2)

print("=== Données dérivées ===")
print("kappa =", kappa)
print("S_dS  =", S_dS)

print("\n=== P1 : epsilon = 8 b kappa H^2 ===")
cases = {"(i)  N_S=1": (1,0,0), "(ii) N_F=1": (0,1,0), "(iii) N_V=1": (0,0,1)}
for lab, (NS,NF,NV) in cases.items():
    b, n = b_of(NS,NF,NV)
    eps = Mono(8) * b * kappa * H*H
    prod = eps * S_dS
    assert prod.p == 0 and prod.g == 0 and prod.h == 0
    print(f"{lab}: n={n:2d}  b = {b}   epsilon = {eps}   epsilon*S_dS = {prod.c}")

print("\n=== P2 : unités 8 pi G = 1 ===")
# G = 1/(8 pi) ; Lambda = 3 H^2  =>  H^2 = Lambda/3
G_val = Mono(F(1,8), p=-1)
S_sub = (PI / (G_val * H*H))        # pi/(G H^2) avec G substitué -> coefficient * pi^2 * H^-2
print("S_dS (8piG=1) =", S_sub, "  i.e. 8 pi^2 / H^2")
# remplacer H^-2 par 3/Lambda : coefficient *3, exposant en Lambda -1
coef_Lambda = S_sub.c * 3
print(f"S_dS = {coef_Lambda} * pi^2 / Lambda   (pi exposant = {S_sub.p})")
ratio = F(12) / coef_Lambda
print("(12 pi^2/Lambda) / S_dS =", ratio)

print("\n=== P3 : ordres de grandeur ===")
H_eV  = 1.5e-33
H_GeV = H_eV * 1e-9
MP    = 1.22e19          # GeV
Gn    = 1.0 / MP**2      # GeV^-2
GH2   = Gn * H_GeV**2
inv_S = 1.0 / S_dS.value(Gn, H_GeV)
b12, n12 = b_of(0,0,1)
eps12 = (Mono(8) * b12 * kappa * H*H).value(Gn, H_GeV)
print(f"H = {H_GeV:.3e} GeV ; G = {Gn:.3e} GeV^-2")
print(f"G H^2        = {GH2:.3e}")
print(f"1/S_dS       = {inv_S:.3e}   (S_dS = {1/inv_S:.3e})")
print(f"epsilon(N_V=1) = {eps12:.3e}")
print(f"epsilon * S_dS (num.) = {eps12/inv_S:.6f}")

print("\n=== P4 : contrôle numérique indépendant de epsilon*S_dS = n/30 ===")
# Membre gauche : évaluation flottante directe des définitions brutes,
# sans passer par la classe Mono ni par la forme simplifiée.
import random
random.seed(2026)
ok = True
for trial in range(2000):
    NS, NF, NV = random.randint(0,7), random.randint(0,7), random.randint(0,7)
    n = NS + 6*NF + 12*NV
    if n == 0: continue
    Gf = 10.0**random.uniform(-125, 3)
    Hf = 10.0**random.uniform(-45, 3)
    bf = (NS + 6*NF + 12*NV) / (120.0 * (4*math.pi)**2)
    kf = 8*math.pi*Gf
    epsf = 8*bf*kf*Hf**2
    Af = 4*math.pi/Hf**2
    Sf = Af/(4*Gf)
    lhs = epsf*Sf
    rhs = n/30.0
    rel = abs(lhs-rhs)/rhs
    if rel > 1e-12:
        ok = False
        print("ECART", NS,NF,NV,Gf,Hf,lhs,rhs,rel)
print("2000 tirages aléatoires (N_S,N_F,N_V in 0..7, G,H log-uniformes) :",
      "IDENTITE VERIFIEE (ecart relatif < 1e-12)" if ok else "ECHEC")
# et sur les valeurs physiques de P3 pour n = 1, 6, 12
for n in (1,6,12):
    bf = n/(120.0*(4*math.pi)**2)
    epsf = 8*bf*(8*math.pi*Gn)*H_GeV**2
    Sf = (4*math.pi/H_GeV**2)/(4*Gn)
    print(f"n={n:2d}: eps*S (flottant) = {epsf*Sf:.15f}   n/30 = {n/30:.15f}")
