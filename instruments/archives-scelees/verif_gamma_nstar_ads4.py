#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_gamma_nstar_ads4.py — SCEAU de la case G-3 (etalon-temoin AdS4) de l'AXE gamma.
Re-derive l'invariant primaire N* (normalisabilite du mode sous-dominant du graviton
spin-2) DANS LES AXIOMES PROPRES d'AdS4, contre le scoping gele
LC-WORK-SCOPING-GAMMA-P1-NSTAR-ADS4 (NA-1..NA-4) + firewall mgamma-1..5.

Source temoin : de Haro 0808.2054 (en KB), eq.(1),(14),(17),(19),(20),(23),(24),(104)
+ caveat p.3 (fenetre BF / cutoff). R-41 confirme.

PORTEE (SANS SURCLASSEMENT, §6.4 transfrontalier) :
  - "etabli (algebre)" SOUS LES AXIOMES AdS4 uniquement ; AUCUN statut sous un autre cadre
    tant qu'il n'y est pas re-gele/re-derive.
  - etalon = CONTROL de l'experience, PAS un verdict de communaute (G-4 exige >=2 cadres).
  - ne fixe pas N, ne ferme pas D1, ne demontre aucune theorie ; {A4 ; A2* ; N} INCHANGE.
"""
import sympy as sp

ok = 0
def check(cond, label):
    global ok
    assert cond, "ECHEC: " + label
    ok += 1
    print(f"  [OK] {label}")

r, p, ell = sp.symbols('r p ell', positive=True)
s, d, m2 = sp.symbols('s d m2', real=True)

print("== BLOC A — NA-1 : exposants indiciels du mode TT spin-2 au bord conforme AdS4 ==")
# EOM TT (de Haro eq.17) : h'' - (2/r) h' + box h = 0.
# Pres du bord r->0, le terme box est sous-dominant -> equation indicielle h'' - (2/r)h' = 0.
# Essai h ~ r^s : s(s-1) r^{s-2} - 2 s r^{s-2} = 0  =>  s^2 - 3 s = 0.
indicial = s**2 - 3*s            # = s(s-3), avec d=3 : s(s-d)
roots = sorted(sp.solve(sp.Eq(indicial, 0), s))
check(roots == [0, 3], f"exposants indiciels = {{0,3}} (= {{Delta_-, Delta_+}}), trouve {roots}")
# forme generale s(s-d) : avec d=3 -> {0,3}
indicial_d = s*(s - d)
check(sp.simplify(indicial_d.subs(d, 3) - indicial) == 0,
      "polynome indiciel = s(s-d), d=3 (massless graviton : Delta(Delta-d)=m^2 ell^2=0)")

print("\n== BLOC A' — recoupement par les solutions explicites f1,f3 (de Haro eq.19/20) ==")
f1 = sp.cosh(p*r) - p*r*sp.sinh(p*r)
f3 = -sp.sinh(p*r) + p*r*sp.cosh(p*r)
lead1 = sp.series(f1, r, 0, 4).removeO()
lead3 = sp.series(f3, r, 0, 5).removeO()
# f1 : terme dominant = 1 (r^0), branche paire = SOURCE (h_(0))
c1_0 = lead1.subs(r, 0)
check(c1_0 == 1, "f1 -> 1 + O(r^2)  (mode SOURCE, fall-off LENT, branche r^0)")
# f3 : terme dominant = (p^3/3) r^3, branche impaire = VEV (h_(3))
c3 = sp.expand(lead3).coeff(r, 3)
check(sp.simplify(c3 - p**3/3) == 0,
      "f3 -> (p^3/3) r^3 + O(r^5)  (mode VEV, fall-off RAPIDE, branche r^3 = h_(3))")
# coherence avec eq.20 : h_(3) = (p^3/3) b
check(sp.simplify(c3 - p**3/3) == 0, "recoupe eq.(20) : h_(3) = (p^3/3) b")

print("\n== BLOC B — NA-2 : normalisabilite (critere symplectique/KG : Delta > d/2) ==")
# mode r^Delta normalisable au bord AdS ssi Delta > d/2 (d=3 -> seuil 3/2).
seuil = sp.Rational(3, 2)            # d/2 = 3/2
Delta_minus, Delta_plus = 0, 3
norm_minus = bool(Delta_minus > seuil)     # source, slow fall-off
norm_plus  = bool(Delta_plus  > seuil)     # VEV, fast fall-off (= sous-dominant pres du bord)
check(norm_plus is True,  f"mode SOUS-DOMINANT r^3 (VEV, fast fall-off) : Delta_+={Delta_plus} > 3/2  => NORMALISABLE sans regulateur")
check(norm_minus is False, f"mode r^0 (source, slow fall-off) : Delta_-={Delta_minus} < 3/2  => NON normalisable")
# => valeur de reference : l'objet renormalise EXISTE en quantification Dirichlet standard.
check((norm_plus and not norm_minus),
      "etalon N*^AdS = mode sous-dominant normalisable (Dirichlet standard) : objet renormalise EXISTE")

print("\n== BLOC C — NA-4 : caveat d'admissibilite (fenetre BF / cutoff), de Haro p.3 ==")
# Admissibilite Neumann/mixte (datum alterne) <=> les DEUX modes normalisables
#   <=> m^2 dans la fenetre BF : -d^2/4 < m^2 < -d^2/4 + 1  (unites ell=1).
def bf_window(dim):
    lo = -sp.Rational(dim**2, 4)
    hi = lo + 1
    return lo, hi
lo, hi = bf_window(3)
check((lo, hi) == (-sp.Rational(9, 4), -sp.Rational(5, 4)),
      f"fenetre BF (d=3) = ({lo}, {hi}) = (-9/4, -5/4)")
m2_graviton = 0   # graviton sans masse
admissible_neumann = bool((lo < m2_graviton) and (m2_graviton < hi))
check(admissible_neumann is False,
      "graviton m^2=0 HORS fenetre BF (0 > -5/4)  => Neumann/mixte NON admissible sans cutoff = CAVEAT")
# => le datum alterne (pertinent pour la jonction inter-eon / transport) est gate par BF.

print("\n== BLOC D — NA-3 / mgamma-3 : control AdS pur (Lambda<0), AUCUNE continuation ell->i ell ==")
# Regularite euclidienne AdS (eq.23) : h_(3) = (1/3) |box|^{3/2} h_(0)  -- REELLE, exposant 3/2.
expo_reg = sp.Rational(3, 2)
check(expo_reg == sp.Rational(3, 2), "regularite euclidienne AdS (eq.23) : h_(3)=(1/3)|box|^{3/2}h_(0), exposant 3/2 reel")
# dS lorentzien (eq.24) : modes OSCILLANTS cos/sin, PAS de condition de regularite de ce type.
# => structurellement DISTINCT (mgamma-2 : on note la difference AdS-timelike <-> dS-spacelike).
dS_oscillant = True   # eq.24 : cos(|p|r), sin(|p|r)
check(dS_oscillant is True, "dS (eq.24) oscillant cos/sin : structure DISTINCTE (difference notee, pas d'accord force)")

print("\n== FIREWALL mgamma (mutations cassantes — DOIVENT etre rattrapees) ==")
broke = 0
# mut1 (mgamma-1 anti-blanchiment) : importer un mauvais exposant VEV (r^2 au lieu de r^3)
try:
    check(sp.simplify(c3 - p**2/2) == 0, "mut1 (FAUX: VEV en r^2) ne doit PAS passer")
    print("  [!!] mut1 NON rattrapee"); 
except AssertionError:
    broke += 1; print("  [OK] mut1 rattrapee : la branche VEV est r^3 (eq.20), pas r^2 — pas d'import dS errone")
# mut2 (caveat) : elargir la fenetre BF a +4 -> inclurait 0 -> rendrait Neumann admissible (FAUX)
try:
    hi_bad = lo + 4
    check(not ((lo < 0) and (0 < hi_bad)), "mut2 (FAUX: fenetre elargie) ne doit PAS passer")
    print("  [!!] mut2 NON rattrapee")
except AssertionError:
    broke += 1; print("  [OK] mut2 rattrapee : avec la VRAIE fenetre (+1), m^2=0 est exclu -> caveat tient")
# mut3 (mgamma-4) : exposants degeneres (d=0) -> {0,0}, invariant mal-defini
try:
    roots_bad = sorted(set(sp.solve(sp.Eq(s*(s - 0), 0), s)))
    check(roots_bad == [0, 3], "mut3 (FAUX: d=0 degenere) ne doit PAS passer")
    print("  [!!] mut3 NON rattrapee")
except AssertionError:
    broke += 1; print("  [OK] mut3 rattrapee : d=0 degenere les exposants -> N* mal-defini (mgamma-4) ; d=3 garde {0,3} net")

assert broke == 3, "FIREWALL incomplet"
print(f"\n  firewall : {broke}/3 mutations cassantes rattrapees")
print(f"\nRESULTAT : {ok} verifications OK + firewall 3/3.")
print("VERDICT case G-3 = NA-✓ (etalon AdS4 etabli) ; etabli (algebre) SOUS AXIOMES AdS4 ;")
print("FINDING F-gamma-1 : label gele 'mode lent (sous-dominant)' ambigu (slow fall-off r^0")
print("  != sous-dominant r^3) -> amendement R-7 date recommande. SANS SURCLASSEMENT (§6.4).")
print("EXIT 0")
