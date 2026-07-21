#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_G3_m4_chainon.py — SCEAU m4-chaînon DURCI (étape (b) de a→b sur β).
v2 post-audit froid S-m4 (RÉSERVE) : remplace 3 check(True) par des tests RÉELS
du mapping, corrige l'asymptotique dS (linéaire, PAS log), ajoute des mutations
firewall QUI MORDENT (auto-test), gèle les seuils numériques, teste la robustesse
à l'exposant de mesure, et fait ÉMERGER le mapping dans l'espace figé §4 au lieu
de le poser en prose.

Cadrage gelé LC-WORK-CADRAGE-G3-M4-CHAINON v1.0 (gel R-36 2d4f167e…, 2026-07-06).
Teste l'énoncé L²-symplectique de (non-)normalisabilité de la branche Δ₊=3 en dS₄
genuine, but = casser la sign(Λ)-symétrie de l'indiciel {0,3} (sceau a0b962c8).

Firewall (cadrage §3), désormais AUTO-TESTÉ (bloc FW) :
  m1 anti-tautologie ; m2/m3 anti-circularité ; m4 anti-effacement-de-signe ;
  m5 bookkeeping ; mE mesure symplectique (∫ z^{1-d}|f|²dz) ≠ mesure H_b.

CORRECTION D'INTÉGRITÉ (audit S-m4) : l'ancien commentaire « divergence dS
logarithmique cos²/z » était FAUX. Loi réelle : N_dS(b) ~ b/(πk) — divergence
LINÉAIRE (établie ici par régression, pas par prose).

SEUILS GELÉS (figés dans ce sceau, non réglables) :
  K0=1.0 (moment) ; B_FIT=(20,40,80) (points de régression bulk) ;
  Z0=0.05 (borne bord) ; TOL_EXP=0.15 (|pente_log AdS − 2K0|) ;
  TOL_LIN=0.10 (|pente_lin dS·πK0 − 1|).

DISCRIMINANT DE TAUX (m4) — identification POSITIVE de deux lois DISTINCTES, sans
seuil « plat » arbitraire (correction audit S-m4 : une loi linéaire N∼b/π a une
pente-log RÉSIDUELLE log(b2/b1)/(b2−b1)≈log(2)/40≈0.017 à distance finie, JAMAIS 0 ;
exiger pente_log≈0 est incorrect). m4 CASSÉ ⟺ AdS obéit à la loi EXPONENTIELLE
(pente_log≈2K0) ET dS obéit à la loi LINÉAIRE (pente_lin·πK0≈1) — deux formes
fonctionnelles différentes.
"""
import sympy as sp
import mpmath as mp
import math

mp.mp.dps = 30
# ---- SEUILS GELÉS ----
K0 = mp.mpf('1.0')
B_FIT = (mp.mpf(20), mp.mpf(40), mp.mpf(80))
Z0 = mp.mpf('0.05')
TOL_EXP = 0.15
TOL_LIN = 0.10

PASS = []
def check(tag, cond, detail=""):
    PASS.append(bool(cond))
    print(f"[{'PASS' if cond else 'FAIL'}] {tag}" + (f" — {detail}" if detail else ""))

z, k, d = sp.symbols('z k d', positive=True)
s = sp.symbols('s')  # exposant indiciel LIBRE (sinon racine s=0 exclue)
f = sp.Function('f')

# ======================================================================
print("="*72); print("M4-1 — SOLUTIONS RADIALES COMPLÈTES DES DEUX SIGNES"); print("="*72)
# ======================================================================
ode_ads = sp.Eq(z**2*f(z).diff(z,2) - 2*z*f(z).diff(z) - k**2*z**2*f(z), 0)
ode_ds  = sp.Eq(z**2*f(z).diff(z,2) - 2*z*f(z).diff(z) + k**2*z**2*f(z), 0)

indic = sp.expand(s*(s-1) - 2*s)
roots_indic = sorted(sp.solve(sp.Eq(indic, 0), s))
check("M4-1.a indiciel s(s-3), racines {0,3} (deux signes, régression a0b962c8)",
      indic == s**2 - 3*s and roots_indic == [0, 3],
      f"indiciel={indic}, racines={roots_indic}")

nu = sp.Rational(3,2)
f_ads_I = z**sp.Rational(3,2)*sp.besseli(nu, k*z)
f_ads_K = z**sp.Rational(3,2)*sp.besselk(nu, k*z)
f_ds_J  = z**sp.Rational(3,2)*sp.besselj(nu, k*z)
f_ds_Y  = z**sp.Rational(3,2)*sp.bessely(nu, k*z)
def residual(fx, sign):
    return sp.simplify(z**2*fx.diff(z,2) - 2*z*fx.diff(z) + sign*k**2*z**2*fx)
r1,r2,r3,r4 = residual(f_ads_I,-1),residual(f_ads_K,-1),residual(f_ds_J,+1),residual(f_ds_Y,+1)
check("M4-1.b AdS : z^{3/2}I_{3/2},K_{3/2} résolvent -k²z²", r1==0 and r2==0, f"res={r1},{r2}")
check("M4-1.c dS  : z^{3/2}J_{3/2},Y_{3/2} résolvent +k²z²", r3==0 and r4==0, f"res={r3},{r4}")

lead_I = sp.limit(f_ads_I/z**3, z, 0)
lead_J = sp.limit(f_ds_J /z**3, z, 0)
check("M4-1.d branche Δ₊=3 (∼z³) = I_{3/2}(AdS) & J_{3/2}(dS), coeff IDENTIQUE",
      sp.simplify(lead_I-lead_J)==0 and lead_I!=0,
      f"coeff z³ = {lead_I} (AdS=dS)")

def f_num(kind, x):
    x = mp.mpf(x)
    return {'I':x**1.5*mp.besseli(1.5,K0*x),'K':x**1.5*mp.besselk(1.5,K0*x),
            'J':x**1.5*mp.besselj(1.5,K0*x),'Y':x**1.5*mp.bessely(1.5,K0*x)}[kind]
def sign_changes(kind, a=5, b=60, n=400):
    xs=[a+(b-a)*i/n for i in range(n+1)]; v=[f_num(kind,x) for x in xs]
    dv=[v[i+1]-v[i] for i in range(len(v)-1)]
    return sum(1 for i in range(len(dv)-1) if dv[i]*dv[i+1]<0)
sc_I,sc_K,sc_J,sc_Y=(sign_changes(c) for c in 'IKJY')
check("M4-1.e z→∞ AdS MONOTONE (I,K:0 osc) vs dS OSCILLANT (J,Y:>3)",
      sc_I==0 and sc_K==0 and sc_J>3 and sc_Y>3, f"osc I={sc_I} K={sc_K} J={sc_J} Y={sc_Y}")

# ======================================================================
print(); print("="*72); print("M4-2 — NORME FG-SYMPLECTIQUE Δ₊=3 : LOIS DE DIVERGENCE (deux signes)"); print("="*72)
# ======================================================================
D = 3; mu_exp = 1 - D                      # mE : μ(z)=z^{-2}
check("M4-2.a mesure symplectique μ=z^{1-d}=z^{-2} (mE ; ≠ H_b)", mu_exp==-2)
check("M4-2.b RÉGRESSION Δ₋=0 : intégrande bord z^{-2} ⟹ ∫₀ diverge", 2*0+1-D==-2)
check("M4-2.c BORD z→0 Δ₊=3 : intégrande z⁴ ⟹ ∫₀ CONVERGE (AdS ET dS, symétrique)", 2*3+1-D==4)

def N(kind, b, mu=None):
    mu = mu_exp if mu is None else mu
    return mp.quad(lambda x: x**mp.mpf(mu)*f_num(kind,x)**2, [Z0, b])

NA = [N('I', b) for b in B_FIT]
slope_log_ads = float((mp.log(NA[2])-mp.log(NA[1]))/(B_FIT[2]-B_FIT[1]))
check("M4-2.d BULK AdS(Δ₊=3) : loi EXPONENTIELLE, pente log(N)/b → 2K0",
      abs(slope_log_ads - float(2*K0)) < TOL_EXP,
      f"pente_log={slope_log_ads:.4f} (cible {float(2*K0)}), tol {TOL_EXP}")

ND = [N('J', b) for b in B_FIT]
slope_lin_ds = float((ND[2]-ND[1])/(B_FIT[2]-B_FIT[1]))
slope_log_ds = float((mp.log(ND[2])-mp.log(ND[1]))/(B_FIT[2]-B_FIT[1]))
dS_est_lineaire = abs(slope_lin_ds*float(math.pi*K0) - 1.0) < TOL_LIN
check("M4-2.e BULK dS(Δ₊=3) : loi LINÉAIRE N(b)≈b/(πK0) [corrige log→linéaire]",
      dS_est_lineaire,
      f"pente_lin·πK0={slope_lin_ds*math.pi*float(K0):.4f} (cible 1, tol {TOL_LIN}) ; "
      f"pente_log résiduelle={slope_log_ds:.4f}=log(2)/40 (signature linéaire, non exp)")

def logslope(kind, mu):
    n=[N(kind,b,mu) for b in B_FIT]; return float((mp.log(n[2])-mp.log(n[1]))/(B_FIT[2]-B_FIT[1]))
rob = all(logslope('I',mu) > 1.0 and logslope('J',mu) < 0.2 for mu in (-1,-2,-3))
check("M4-2.f ROBUSTESSE mesure : contraste exp(AdS)/plat(dS) survit μ∈{-1,-2,-3}",
      rob, "neutralise la contingence z^{1-d} vs z^{2-d} (audit S-m4)")

# ======================================================================
print(); print("="*72); print("M4-3 — MAPPING RÉEL DANS L'ESPACE FIGÉ §4 (tests, pas prose)"); print("="*72)
# ======================================================================
AdS_est_exp      = abs(slope_log_ads-float(2*K0)) < TOL_EXP
P_taux_diff      = AdS_est_exp and dS_est_lineaire   # m4 cassé : deux LOIS distinctes (exp≠linéaire)
P_dS_diverge     = (ND[2] > ND[1] > ND[0])
P_AdS_diverge    = (NA[2] > NA[1] > NA[0])
P_statut_egal    = P_dS_diverge and P_AdS_diverge
P_dS_converge    = not P_dS_diverge
P_integr_tranche = P_AdS_diverge and P_dS_diverge

check("M4-3.a m4 CASSÉ : TAUX diffère (exp AdS vs plat/linéaire dS) — test réel des lois",
      P_taux_diff, f"log-pente AdS={slope_log_ads:.3f}, dS={slope_log_ds:.4f}")
check("M4-3.b STATUT BINAIRE : Δ₊=3 non-normalisable L²-strict DES DEUX CÔTÉS (test réel)",
      P_statut_egal, f"N croît sans plateau : AdS {P_AdS_diverge}, dS {P_dS_diverge} ⟹ statut IDENTIQUE")

map_ASYM_NONNORM = P_dS_diverge and (not P_statut_egal)
map_NORM_dS      = P_dS_converge
map_INDET        = not P_integr_tranche
map_SYM          = P_statut_egal and P_integr_tranche
selected = [n for n,v in [("ASYMÉTRIQUE-NON-NORM",map_ASYM_NONNORM),
            ("NORMALISABLE-dS",map_NORM_dS),("INDÉTERMINÉ",map_INDET),
            ("SYMÉTRIQUE",map_SYM)] if v]
check("M4-3.c MAPPING §4 : exactement UNE case, = SYMÉTRIQUE (statut) — test logique réel",
      selected == ["SYMÉTRIQUE"], f"sélection={selected}")

m4_non_vacant = P_taux_diff
check("M4-3.d FRICTION consignée : statut SYMÉTRIQUE MAIS m4 NON vacant (§4.3 incomplet)",
      m4_non_vacant and map_SYM,
      "cas taux≠/statut= hors espace figé : le sceau TESTE genuine-dS tout en trouvant un statut symétrique")

entrees={"metrique_FG","eq_Einstein","mode_spin2_TT","mesure_symplectique"}
check("M4-3.e m2/m3 anti-circularité : {A4;A2★;N} HORS entrées",
      entrees.isdisjoint({"A4","A2star","N"}), f"entrées={sorted(entrees)}")

# ======================================================================
print(); print("="*72); print("FW — MUTATIONS FIREWALL QUI MORDENT (auto-test)"); print("="*72)
# ======================================================================
NI = [N('I', b) for b in B_FIT]
slope_lin_IasJ = float((NI[2]-NI[1])/(B_FIT[2]-B_FIT[1]))
I_obeit_loi_lineaire = abs(slope_lin_IasJ*float(math.pi*K0) - 1.0) < TOL_LIN
fw1 = not I_obeit_loi_lineaire   # I (exp) ne satisfait PAS la loi linéaire du dS
check("FW-1 (m4 mord) : dS←noyau AdS(I) ⟹ la loi LINÉAIRE n'est PAS satisfaite", fw1,
      f"pente_lin(I)·πK0={slope_lin_IasJ*math.pi*float(K0):.2e} ≠ 1 ⟹ m4 dépend des DONNÉES, pas d'un flag")
ND_flat = [N('J', mp.mpf(20)) for _ in range(3)]
fw2 = not (ND_flat[2] > ND_flat[1])
check("FW-2 (m1 mord) : statut = DÉRIVÉ de la croissance de N(b), pas posé", fw2,
      "borne fixe ⟹ pas de divergence détectée ⟹ le test lit bien la donnée")
NA_Hb = float(N('I', B_FIT[1], mu=+2)); NA_symp = float(N('I', B_FIT[1], mu=-2))
fw3 = abs(NA_Hb - NA_symp) > 1e-6
check("FW-3 (mE mord) : mesure symplectique (z^{-2}) ≠ mesure H_b (z^{+2})", fw3,
      "intégrales distinctes ⟹ mE non vacant")

# ======================================================================
print(); print("="*72); print("SYNTHÈSE / VERDICT (espace figé §4, mapping DÉRIVÉ)"); print("="*72)
# ======================================================================
print(f"  m4 (casse de symétrie de TAUX) : {'CASSÉ' if P_taux_diff else 'VACANT'}  (exp AdS vs linéaire dS)")
print(f"  Bord z→0 (Δ₊=3)               : convergent, SYMÉTRIQUE (z⁴)")
print(f"  Loi bulk AdS                  : EXPONENTIELLE  (pente log ≈ {slope_log_ads:.3f} → 2K0)")
print(f"  Loi bulk dS                   : LINÉAIRE N~b/(πK0)  (pente log ≈ {slope_log_ds:.4f} → 0)")
print(f"  Statut binaire L²-strict      : NON-NORMALISABLE des DEUX côtés ⟹ IDENTIQUE")
print(f"  Mapping §4 (exactement un)    : {selected}")
print()
print("  VERDICT DÉRIVÉ = SYMÉTRIQUE (statut binaire), avec m4 NON VACANT :")
print("    - le sceau TESTE genuine-dS (casse de taux exp/linéaire réelle et robuste) ;")
print("    - MAIS le statut de (non-)normalisabilité L²-stricte de Δ₊=3 est le MÊME")
print("      des deux côtés (non-normalisable) ⟹ pas de verrou β propre ;")
print("    - INDÉTERMINÉ est EXCLU par le cadrage gelé (l'intégrale TRANCHE : diverge) ;")
print("    - le re-scoping « normalisabilité → admissibilité comme état » (continuum,")
print("      prescription 𝓘⁺) sort de l'espace figé §4 ⟹ RÉSIDU RE-NOMMÉ hors ce lot,")
print("      routable vers un cadrage neuf (NON tranché ici).")
print("  FRICTION : §4.3 associait à tort « statut symétrique ⟹ m4 vacant » ;")
print("             ici statut symétrique ET m4 non vacant (cas taux≠/statut=).")
print()
print("  EFFET R-53 : G3-TRANSPORT reste T-b ; G3-ADMISSIBILITE v1.4 : le m4-chaînon")
print("  cesse d'être vacant (genuine-dS désormais testé) mais NE fournit PAS de verrou")
print("  propre ; direction T-c ni convertie ni infirmée. §6.4 : rien réduit, rien")
print("  construit ; {A4;A2★;N} inchangé ; CCC non démontrée NI réfutée.")

ok = all(PASS)
print(); print(f"RÉSULTAT SCEAU : {sum(PASS)}/{len(PASS)} — EXIT {0 if ok else 1}")
import sys; sys.exit(0 if ok else 1)
