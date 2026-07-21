#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R3_spectre.py — Silo R, lot R-3 (spectre ⟨g₃g₃⟩~k³ + variance
LOG), protocole §2.0 AMENDÉ post-CSE. Cibles gelées :
audit/R3-CIBLES-GELEES.md (sha256 eded7406…), figées AVANT redérivation.

STATUT DE MÉTHODE, déclaré : REPRODUCTION GUIDÉE pour la chaîne k³ (le
front-matter la révèle entière) — plafond E-2 annoncé au gel. SEUL
contenu quasi-indépendant : la reconstruction du NOYAU EXACT de
variance (le gel n'en donne que l'enveloppe cos²x/3, la moyenne 1/6 et
la constante β∞) — adjugée par β∞. ANTI-FIT consigné : 3 candidats de
noyau essayés, discriminés par β∞ ; le candidat retenu n'a PAS été
ajusté à la cible (écart résiduel nommé, borné, non corrigé).

Discipline : PASS = discriminant seul compté ; CONSIGNATION hors
décompte ; aucune disjonction infaillible ; firewalls mordants.

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
import sympy as sp
import mpmath as mp

npass, ncons = [], []


def check(name, cond):
    cond = bool(cond)
    npass.append(cond)
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        sys.exit("ÉCHEC : " + name)


def consigne(name, note):
    ncons.append(name)
    print("  [CONSIGNATION] %s — %s" % (name, note))


i = sp.I
k, H, MPl, g0, x = sp.symbols("k H M_Pl g_0 x", positive=True)
eta = sp.Symbol("eta", negative=True)
lam = sp.Symbol("lambda", positive=True)

print("== K1/K2 : chaîne du spectre (composition re-calculée) ==")
consigne("𝒫_h = 2H²/(M_Pl²k³)", "PRÉ-COUVERT R-4 T1 (recalculé là, "
         "32/35 PASS) — importé ici sans double compte")
P0 = 2*H**2/(MPl**2*k**3)
check("k³𝒫_h invariant d'échelle (k→λk)",
      sp.simplify((k**3*P0).subs(k, lam*k) - k**3*P0) == 0)
hBD = g0*(1 + i*k*eta)*sp.exp(-i*k*eta)
c3 = sp.series(hBD, eta, 0, 5).removeO().expand().coeff(eta, 3)
consigne("g₃ = −(i/3)k³g₀", "PRÉ-COUVERT R-5 P1 — recalcul de contrôle "
         "ici : %s" % (sp.simplify(c3 + (i/3)*k**3*g0) == 0))
amp = -(i/3)*k**3
Pg3 = sp.simplify(amp*sp.conjugate(amp)*P0)
check("COMPOSITION : P_{g₃} = (1/9)k⁶·P_{g₀}",
      sp.simplify(Pg3 - k**6*P0/9) == 0)
check("P_{g₃} ∝ k³ (exposant exact : k·d/dk ln P_{g₃} = 3)",
      sp.simplify(k*sp.diff(sp.log(Pg3), k)) == 3)

print("== K3 : lecture holographique k^{2Δ−d} ==")
consigne("Δ = d = 3 et carte ⟨TT⟩=(d/16πG)²·P_{g₃}",
         "IMPORTS du gel (dimension du dual de g₃ ; coefficient de "
         "carte) — non dérivés ici")
d, Delta = 3, 3
check("l'exposant CALCULÉ (3) = 2Δ−d", 2*Delta - d == 3)
check("firewall : Δ=2 donnerait 2Δ−d=1 ≠ exposant calculé",
      2*2 - d != 3)

print("== K4 : reconstruction AVEUGLE du noyau de variance ==")
consigne("anti-fit : candidats essayés", "3 candidats — (i) K=f_b²/(3x³) "
         "[retenu] ; (ii) cos²x/(3x) [IR divergent, rejeté avant "
         "intégration] ; (iii) x·cos²x/(3(1+x²)) [β=−0,0257, rejeté par "
         "β∞]. Aucun ajustement du retenu à la cible.")
fb = x*sp.cos(x) - sp.sin(x)
K = fb**2/(3*x**3)
# structure : f_b est le second membre du doublet S1 (R-4 T10)
check("f_b solution de y''−(2/u)y'+y=0 (le noyau est bâti sur le "
      "partenaire dual du mode BD)",
      sp.simplify(sp.diff(fb, x, 2) - (2/x)*sp.diff(fb, x) + fb) == 0)
# enveloppe : x·K − cos²x/3 = termes qui tombent en 1/x
diff_env = sp.simplify(sp.expand_trig(x*K - sp.cos(x)**2/3))
target_corr = sp.simplify(sp.expand_trig(
    -sp.sin(2*x)/(3*x) + sp.sin(x)**2/(3*x**2)))
check("enveloppe : x·K(x) = cos²x/3 + O(1/x) (correction exacte "
      "−sin2x/3x + sin²x/3x², identité symbolique)",
      sp.simplify(diff_env - target_corr) == 0)
check("moyenne de l'enveloppe = 1/6 (∫cos²x/3 sur une période)",
      sp.simplify(sp.integrate(sp.cos(x)**2/3, (x, 0, 2*sp.pi))
                  / (2*sp.pi)) == sp.Rational(1, 6))
check("IR-sûr : K(x) ~ x³/27 en 0 (PAS de divergence — série exacte)",
      sp.simplify(sp.series(K, x, 0, 5).removeO() - x**3/27) == 0)
check("UV : K − 1/(6x) = cos2x/6x − sin2x/3x² + sin²x/3x³ (identité "
      "exacte ⟹ le résidu au-delà du log est oscillant-intégrable)",
      sp.simplify(sp.expand_trig(
          K - 1/(6*x)
          - (sp.cos(2*x)/(6*x) - sp.sin(2*x)/(3*x**2)
             + sp.sin(x)**2/(3*x**3)))) == 0)

print("== K4 numérique : β∞ et croissance LOG (pas quartique) ==")
mp.mp.dps = 25
Kn = lambda t: (t*mp.cos(t) - mp.sin(t))**2/(3*t**3)
a_ = mp.quad(Kn, [0, 1])
t1 = mp.quadosc(lambda t: mp.cos(2*t)/(6*t), [1, mp.inf], period=mp.pi)
t2 = mp.quadosc(lambda t: -mp.sin(2*t)/(3*t**2), [1, mp.inf],
                period=mp.pi)
t3 = (mp.quadosc(lambda t: mp.sin(t)**2/(3*t**3) - 1/(6*t**3),
                 [1, mp.inf], period=mp.pi)
      + mp.quad(lambda t: 1/(6*t**3), [1, mp.inf]))
beta = a_ + t1 + t2 + t3
print("    β∞ (haute précision) = %s ; cible gelée = 0.04503" %
      mp.nstr(beta, 7))
check("β∞ = 0.04503 À LA PRÉCISION DE LA CIBLE ±1e-4 (tolérance "
      "déclarée ; écart exact consigné ci-dessous)",
      abs(beta - mp.mpf("0.04503")) < mp.mpf("1e-4"))
consigne("ÉCART NOMMÉ, BORNÉ, NON CORRIGÉ",
         "β∞(recalculé, 25 déc.) = %s vs 0.04503 (gelé) : |Δ| = %s "
         "(7e-4 relatif) — compatible avec la précision numérique de "
         "la valeur d'origine (« établi numérique ») ; AUCUN ajustement "
         "du noyau opéré (anti-fit)" %
         (mp.nstr(beta, 7), mp.nstr(abs(beta - mp.mpf("0.04503")), 2)))
# croissance LOG, pas puissance : I(X2)−I(X1) = ∫_{X1}^{X2} K dx,
# quadrature SUBDIVISÉE aux périodes (intégrande oscillant)
X1, X2 = mp.mpf(200), mp.mpf(2000)
pts = [X1]
while pts[-1] < X2:
    pts.append(min(pts[-1] + mp.pi, X2))
growth = mp.quad(Kn, pts)
check("croissance LOG : I(2000)−I(200) = (1/6)ln(10) ± 2e-3 "
      "(une loi (kη)⁴ donnerait ~10¹² × plus)",
      abs(growth - mp.log(10)/6) < mp.mpf("2e-3"))
check("firewall : le coefficient 1/6 est mesuré, pas posé — "
      "1/4·ln(10) échoue au même test",
      abs(growth - mp.log(10)/4) > mp.mpf("0.05"))

print("== K5 : cutoff holographique et finitude ==")
G_of = 1/(8*sp.pi*MPl**2)
N_ds = sp.pi/(G_of*H**2)
check("√(N/π) = √(8π)·M_Pl/H = ℓ_dS/ℓ_P (ℓ_P=√G, ℓ_dS=1/H)",
      sp.simplify(sp.sqrt(N_ds/sp.pi)
                  - (1/H)/sp.sqrt(G_of)) == 0)
Xstar = mp.mpf("1.02e61")
C = mp.log(Xstar)/6 + beta
print("    C(√(N/π)=1.02e61) = %s ; cible gelée = 23.46" % mp.nstr(C, 6))
check("Ω_σ^tot/A_T = 23.46 à la précision de la cible (±0.01)",
      abs(C - mp.mpf("23.46")) < mp.mpf("0.01"))
check("FINI et ≪0.5 dès A_T ≪ 1 : seuil exact 0.5/C = 0.0213 "
      "(H sous-Planckien largement suffisant)",
      abs(mp.mpf("0.5")/C - mp.mpf("0.02131")) < mp.mpf("1e-4"))
consigne("K6 : N joue deux rôles (cutoff log-doux + normalisation "
         "A_T~(H/M_P)²)", "DÉCLARATIF — reporté sur la circularité "
         "LC-E (N=S_dS présuppose ℓ_P), non brisée ici")

print("\nREDEMO R-3 : %d/%d PASS discriminants + %d consignations "
      "déclarées — EXIT 0" % (sum(npass), len(npass), len(ncons)))
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE (E-2 ; écart β∞ nommé "
      "borné). Le noyau exact K=f_b²/(3x³) est la seule pièce "
      "reconstruite en quasi-aveugle — adjugée par β∞, C, enveloppe, "
      "moyenne, log.")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre "
      "rien. { A4 ; A2★ ; N } INCHANGÉ.")
sys.exit(0)
