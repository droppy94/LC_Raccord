"""iru_litt_check.py -- IR-u (NOTE-133), u-4 : comparaison numerique avec Foraci, Litos, Woodard (arXiv 2606.17963, eq. 27 et 31) :
C_0i0j = C_tree (1 + 3 kW^2 H^2 C_q ln(a) / pi^2), C_q = 32/(3q), kW^2 = 16 pi G, H = 1.
IR-u : W_E = W0 (1 + gamma b kappa ln s), gamma = 8 (c0 = +8) ; ln s = -ln a ; kappa = 8 pi G ; b = coefficient de C^2 dans <T^a_a>
(Hawking-Hertog-Reall eq. 2.7 : c = (N_S + 6 N_F + 12 N_V)/(120 (4 pi)^2)).
"""
import sympy as sp
G = sp.symbols('G', positive=True); pi = sp.pi
champs = {'scalaire MCC': (2**10*3*5, (1, 0, 0)), 'fermion de Dirac': (2**9*5, (0, 1, 0)), 'photon': (2**8*5, (0, 0, 1))}
for nom, (q, (NS, NF, NV)) in champs.items():
    woodard = sp.simplify(3*16*pi*G*sp.Rational(32, 3*q)/pi**2)          # coefficient de ln a
    b = sp.Rational(NS + 6*NF + 12*NV, 120)/(4*pi)**2
    iru_c0p8 = sp.simplify(-8*b*8*pi*G)                                # coefficient de ln a, convention c0 = +8
    print(f"{nom:18s} Woodard : {woodard} ; IR-u (c0=+8) : {iru_c0p8} ; IR-u (c0=-8) : {-iru_c0p8} ; rapport Woodard/IR-u(c0=-8) = {sp.simplify(woodard/(-iru_c0p8))}")
print("EXIT 0")
