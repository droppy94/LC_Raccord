#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_WCH_GWE.py — LC-RACCORD. Sceau du chaînon LC-D3-WCH-GWE v0.3.

  v0.3 (2026-06-08, HOUSEKEEPING post-audit LC-AUDIT-LOG-WCH-GWE §4.5) :
    AJOUT bloc [6bis] MODE EXACT. Le scan [7] v0.2 utilisait la formule LEADING
    (k.eta)^4/27, dont le seuil (A)/(B) a 1.917 est un ARTEFACT de troncature
    (usage hors domaine k.eta~O(1)). Le mode regulier EXACT donne
        Omega_sigma/eps^2 = (x cos x - sin x)^2 / (3 x^2) ,  x = k.eta ,
    DERIVE symboliquement ici (sans tronquer h'), qui PLAFONNE a 0.377 (atteint a
    x~2.74) et ne croise JAMAIS 0.5 => REGIME (A) a TOUTE echelle, AUCUNE bascule.
    Le verrou de (A) n'est donc PAS le spectre/la coupure (moot) mais la
    RETRO-ACTION INHOMOGENE (C7, hors de portee). Le bloc [6] leading et son
    assert (k.eta)^4/27 sont CONSERVES intacts (algebre correcte dans son domaine).

But (LC-WORK-REPRISE-WCH-GWE-SCEAU).
    TRANCHER le verdict (A) que LC-D3-WCH-GWE a posé en `formalisable` :
    « le Omega_sigma imposé par la GW-Epoch (Meissner-Penrose 2503.24263) tombe-t-il
      sous la frontiere du regime (A), Omega_sigma <~ 0.5 eps^2 ? »
    L'etape PAPIER est faite (en KB). Ce sceau fait le NUMERIQUE/SYMBOLIQUE.

Methode. Extension de verif_D3_bunchdavies.py (sceau parent). Etat des blocs :
    [1]    REECRIT  : fond dS (a=-1/H.eta) -> radiation a=H.eta ; EOM TT
                      h'' + (2/eta) h' + k^2 h = 0 ; mode regulier j0 = sin(k.eta)/(k.eta).
    [1bis] AJOUTE   : controle conforme. v = a.h (poids -1) satisfait l'equation PLATE
                      v'' + k^2 v = 0 : le frottement (2/eta) disparait (a'' = 0).
    [2-4]  ADAPTE   : expansion FG sur a=H.eta ; g0,g2 locaux ; dichotomie regulier j0 /
                      singulier y0 (= mode Y de M-P, exclu par WCH/Friedrich) ;
                      residu deux-points <g3 g3> ~ k^3 (importe de LC-D3-WEYL-BUNCHDAVIES)
                      => P_h = k^3 <h0^2> ~ const (A_T tensoriel invariant d'echelle).
    [5]    ACQUIS   : E_ij = (d/2H) g3_ij (derive dans le sceau parent, bloc [5]) ; reutilise.
    [6]    NEUF     : le PONT forme->cisaillement. sigma = (1/2)|h'|/a, h' = -(k^2 eta/3) h0
                      super-horizon, Omega_sigma = sigma^2/(3 H_phys^2), eps = h0/2.
                      VERIFIE SYMBOLIQUEMENT :  Omega_sigma = (k.eta)^4 eps^2 / 27.
    [7]    NEUF     : intégrale spectrale / SENSIBILITE a la coupure k_UV.eta_*.
                      verdict (A) ssi (k.eta_*)^4 <~ 13.5  <=>  k.eta_* <~ 1.9.
                      Mode M-P dominant : k.eta_* ~ 2e-7 (CGB) => Omega_sigma/eps^2 ~ 1e-30.

CIBLES (LC-D3-WCH-GWE, etablies au papier ; ce sceau doit les reproduire) :
    pont mode-a-mode     Omega_sigma/eps^2 = (k.eta)^4 / 27
    seuil regime (A)     k.eta <~ 1.9
    borne raccord        eta_* = 1/H ,  H_* = H  (atlas D1, a=1)
    mode M-P dominant    k.eta_* ~ 2e-7   (M-P eq.85 h~1e-16,k~1e-8 Hz ; eq.89 onset<10s)
    verdict attendu      Omega_sigma/eps^2 ~ (2e-7)^4/27 ~ 1e-30 << 0.5  => (A), marge ~1e29

Entrees M-P verifiees contre la source (OCR de l'archive arXiv 2503.24263) :
    eq.85  h ~ 1e-16, k ~ 1e-8 Hz   (« CGB has presumably the parameters »)
    eq.89  (eta_inf - eta_GW) < 10 s
    p.15   « GWE has large local fluctuations of the Weyl tensor (and small averaged
            Weyl tensor) »  <- la distinction un-point/deux-points du verdict.

Dependances : sympy. Re-executable, sans reseau.
Discipline (LC-AUDIT-VERDICT 6.4) : un `etabli` de sceau = « l'algebre est correcte »,
jamais « la physique de la CCC est etablie ».
"""

import sympy as sp

eta, k, H, h0, eps = sp.symbols('eta k H h0 epsilon', positive=True)
d = 3

def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)

banner("verif_D3_WCH_GWE.py — sceau du pont forme->cisaillement (regime A)")

# ----------------------------------------------------------------------
# [1] EOM cote RADIATION (REECRIT). Atlas D1 : a = H.eta (lineaire),
#     H = a'/a = 1/eta (script-H), H_phys = H/a = 1/(H eta^2).
#     EOM du mode TT (metrique) sur fond radiation : h'' + (2/eta) h' + k^2 h = 0.
#     (cf. dS du parent : h'' - (2/eta) h' + k^2 h = 0 ; le signe du frottement bascule.)
# ----------------------------------------------------------------------
a = H * eta
calH = sp.simplify(sp.diff(a, eta) / a)            # script-H = a'/a
Hphys = sp.simplify(calH / a)                      # H_phys = H/a
print("\n[1] Fond radiation (atlas D1) : a = H.eta")
print("    script-H = a'/a =", calH, "   H_phys = H/a =", Hphys, "  (= 1/(H eta^2))")
assert sp.simplify(calH - 1/eta) == 0
assert sp.simplify(Hphys - 1/(H*eta**2)) == 0

# Mode regulier : j0(k.eta) = sin(k.eta)/(k.eta)  (Bessel spherique, ordre 1/2).
h = h0 * sp.sin(k*eta) / (k*eta)
EOM = sp.simplify(sp.diff(h, eta, 2) + (2/eta)*sp.diff(h, eta) + k**2 * h)
print("    Mode regulier  h = h0 sin(k.eta)/(k.eta) = h0 j0(k.eta)")
print("    EOM  h'' + (2/eta) h' + k^2 h =", EOM, " -> j0 est bien solution.")
assert EOM == 0

# Mode singulier y0 = -cos(k.eta)/(k.eta) : diverge en eta->0 (pole 1/eta).
y0 = -h0 * sp.cos(k*eta) / (k*eta)
EOM_y = sp.simplify(sp.diff(y0, eta, 2) + (2/eta)*sp.diff(y0, eta) + k**2 * y0)
pole = sp.limit(eta * y0, eta, 0)
print("    Mode singulier y0 = -h0 cos(k.eta)/(k.eta) : EOM =", EOM_y,
      "; residu eta->0 (eta*y0) =", sp.simplify(pole), " != 0  -> DIVERGENT.")
assert EOM_y == 0 and sp.simplify(pole) != 0

# Comportement super-horizon du mode regulier : h' = -(k^2 eta/3) h0 + O(eta^3).
hp = sp.diff(h, eta)
hp_lead = sp.series(hp, eta, 0, 2).removeO()
print("    Super-horizon : h'(eta) =", sp.simplify(hp_lead), " = -(k^2 eta/3) h0 + O(eta^3)")
assert sp.simplify(hp_lead - (-(k**2*eta/3)*h0)) == 0

# ----------------------------------------------------------------------
# [1bis] CONTROLE CONFORME (AJOUTE).
#     Variable de poids -1 : v = a.h. Sur a lineaire (a''=0), v satisfait
#     l'equation PLATE v'' + k^2 v = 0 : le frottement (2/eta) a disparu.
#     C'est l'invariance conforme du champ sans masse (M-P : d'Alembertien plat).
# ----------------------------------------------------------------------
app = sp.diff(a, eta, 2)
v = sp.simplify(a * h)
flat = sp.simplify(sp.diff(v, eta, 2) + k**2 * v)
print("\n[1bis] Controle conforme : v = a.h (poids -1), a = H.eta")
print("    a'' =", app, " (=> pas de terme a''/a)")
print("    v =", v, "   v'' + k^2 v =", flat, " -> equation PLATE : frottement absorbe.")
assert app == 0 and flat == 0

# ----------------------------------------------------------------------
# [2-4] FG sur radiation (ADAPTE) + dichotomie regulier/singulier + spectre.
# ----------------------------------------------------------------------
ser = sp.expand(sp.series(h, eta, 0, 5).removeO())
g0 = ser.coeff(eta, 0); g1 = ser.coeff(eta, 1)
g2 = ser.coeff(eta, 2); g3 = ser.coeff(eta, 3)
print("\n[2-4] Expansion FG du mode regulier  h =", ser)
print("    g0 (forme/source) =", g0, " | g1 =", g1, " | g2 (local) =", g2,
      " | g3 (un-point) =", g3)
assert g0 == h0 and g1 == 0
assert sp.simplify(g2 - (-h0*k**2/6)) == 0       # g2 polynomial en k^2 => LOCAL (Schouten)
assert g3 == 0                                   # mode regulier pair => g3 un-point = 0
print("    g2/g0 =", sp.simplify(g2/g0), " (polynome en k^2 => LOCAL).")
print("    g3 = 0 : le mode REGULIER j0 a un g3 un-point NUL (consistant avec WCH).")
print("    => le g3 un-point != 0 viendrait du mode SINGULIER y0 = mode Y de M-P,")
print("       que la WCH/Friedrich (Psi-tilde->0 a I+) EXCLUT. Identification cardinale.")
print("    Deux-points (importe de LC-D3-WEYL-BUNCHDAVIES) : <g3 g3> ~ k^3")
print("       => <h0^2> ~ k^-3 => P_h = k^3 <h0^2> ~ const  (strain invariant d'echelle A_T).")
print("    [dS/CFT bord d=3] Delta=3 => <T T> ~ k^(2Delta-d) = k^3 (coherent).")

# ----------------------------------------------------------------------
# [5] WEYL -> g3 (ACQUIS du sceau parent, bloc [5]). On ne re-derive pas.
# ----------------------------------------------------------------------
print("\n[5] Acquis (verif_D3_bunchdavies.py bloc [5], non re-derive) :")
print("    E_ij (Weyl electrique rescale a I+) = (d/2H) g3_ij ,  d =", d, ".")
print("    Donc « C->0 au crossover » <=> « g3->0 » ; et psi-tilde|_I = g3.")

# ----------------------------------------------------------------------
# [6] LE PONT forme->cisaillement (NEUF) — coeur du sceau.
#     ADM (LC-D3-WCH-GWE 2, etabli) : sigma = (1/2)|h'|/a, norm. « + » e_ij e^ij = 2.
#     => sigma^2 = (1/4)(h'/a)^2 ;  Omega_sigma = sigma^2/(3 H_phys^2).
#     Super-horizon h' = -(k^2 eta/3) h0 ; conversion forme eps = h0/2 (Misner H_ii=2w_i).
# ----------------------------------------------------------------------
banner("[6] PONT forme->cisaillement : Omega_sigma = (k.eta)^4 eps^2 / 27")

sigma2 = sp.Rational(1, 4) * (hp_lead / a)**2          # (1/4)(h'/a)^2, super-horizon
Omega_sigma = sp.simplify(sigma2 / (3 * Hphys**2))     # sigma^2 / (3 H_phys^2)
print("\n  sigma^2 = (1/4)(h'/a)^2 =", sp.simplify(sigma2))
print("  Omega_sigma = sigma^2/(3 H_phys^2) =", Omega_sigma)

target_h0 = (k*eta)**4 * h0**2 / 108
print("  cible (en h0) : (k.eta)^4 h0^2 / 108 =", sp.simplify(target_h0))
assert sp.simplify(Omega_sigma - target_h0) == 0
print("  [check] Omega_sigma == (k.eta)^4 h0^2 / 108  : OK")

# Conversion forme : eps = h0/2  =>  h0 = 2 eps.
Omega_eps = sp.simplify(Omega_sigma.subs(h0, 2*eps))
target_eps = (k*eta)**4 * eps**2 / 27
print("\n  Conversion forme  eps = h0/2  (Misner H_ii = 2 w_i) :")
print("  Omega_sigma =", Omega_eps)
assert sp.simplify(Omega_eps - target_eps) == 0
ratio = sp.simplify(Omega_eps / eps**2)
print("  >>> Omega_sigma / eps^2 =", ratio, "  ===  (k.eta)^4 / 27   [CIBLE REPRODUITE]")
assert sp.simplify(ratio - (k*eta)**4/27) == 0

# Le 27 = 108/4, sans glissement.
assert sp.Rational(108, 4) == 27
print("  [check] 27 = 108/4 (facteur 1/4 = conversion eps=h0/2) : OK")

# ----------------------------------------------------------------------
# [6bis] MODE EXACT (AJOUTE v0.3) — sans tronquer h'.
#     Le bloc [6] utilise h' LEADING = -(k^2 eta/3) h0 (super-horizon), d'ou
#     (k.eta)^4/27. Ici on garde le h' EXACT du mode regulier j0 :
#         h = h0 sin(k.eta)/(k.eta) ,  h'(eta) = h0 k j0'(k.eta) ,
#     et on derive le rapport EXACT, valide a TOUTE echelle k.eta.
#         Omega_sigma/eps^2 = (x cos x - sin x)^2 / (3 x^2) ,  x = k.eta.
#     -> plafonne a 0.377 (x~2.74), ne croise JAMAIS 0.5 : (A) partout.
#     Audit C5 : le « seuil 1.917 » du leading est un artefact (hors domaine).
# ----------------------------------------------------------------------
banner("[6bis] MODE EXACT : Omega_sigma/eps^2 = (x cos x - sin x)^2/(3 x^2), x=k.eta")

hp_exact = sp.diff(h, eta)                                  # h' EXACT (pas de troncature)
sigma2_exact = sp.Rational(1, 4) * (hp_exact / a)**2        # (1/4)(h'/a)^2
Omega_exact = sp.simplify(sigma2_exact / (3 * Hphys**2))    # sigma^2/(3 H_phys^2)
Omega_exact_eps = sp.simplify(Omega_exact.subs(h0, 2*eps))  # conversion eps=h0/2
ratio_exact = sp.simplify(Omega_exact_eps / eps**2)         # = f(k.eta)

x = sp.symbols('x', positive=True)                          # x = k.eta
target_exact = (x*sp.cos(x) - sp.sin(x))**2 / (3*x**2)
# ratio_exact est fonction de (k,eta) via x=k.eta ; on compare apres subs k.eta->x.
ratio_exact_x = sp.simplify(ratio_exact.subs(eta, x/k))
diff_exact = sp.simplify(ratio_exact_x - target_exact)
print("\n  Omega_sigma/eps^2 (exact, simplifie) =", ratio_exact_x)
print("  cible (x cos x - sin x)^2/(3 x^2)     =", target_exact)
print("  difference symbolique                 =", diff_exact)
assert diff_exact == 0
print("  [check] le mode exact reproduit (x cos x - sin x)^2/(3 x^2) : OK")

# Limite leading : a x->0, doit redonner le bloc [6] = x^4/27.
lead = sp.series(target_exact, x, 0, 6).removeO()
print("\n  Limite super-horizon (x->0) :", sp.simplify(lead), " (= x^4/27 + O(x^6))")
assert sp.simplify(lead - x**4/27) == 0
print("  [check] limite leading == (k.eta)^4/27 (coherent avec [6]) : OK")

# Plafond numerique : balayage de R(x) sur (0, 60]. Max ~ 0.377 < 0.5, jamais croise.
import math
def R_exact(xx):
    return (xx*math.cos(xx) - math.sin(xx))**2 / (3.0*xx**2)
N = 600000
xmax_scan = 60.0
rmax, xstar = 0.0, 0.0
for i in range(1, N+1):
    xx = xmax_scan * i / N
    r = R_exact(xx)
    if r > rmax:
        rmax, xstar = r, xx
print("\n  Balayage R(x) sur (0, %.0f] (%d points) :" % (xmax_scan, N))
print("    max R(x) = %.5f  a x = %.4f" % (rmax, xstar))
print("    sup asymptotique cos^2(x)/3 = %.5f (enveloppe)" % (1.0/3.0))
assert rmax < 0.5                       # ne croise JAMAIS le seuil (A)/(B)
assert abs(rmax - 0.3767) < 1e-3        # plafond ~ 0.377 (atteint x~2.74)
assert abs(xstar - 2.744) < 1e-2
print("  [check] max < 0.5 (REGIME (A) a TOUTE echelle, AUCUNE bascule) : OK")
print("  [check] plafond ~ 0.377 a x ~ 2.74 : OK")
print("\n  >>> Le mode regulier EXACT est en REGIME (A) pour TOUT k.eta.")
print("      Le « seuil k.eta~1.917 » du scan leading [7] est un ARTEFACT de troncature")
print("      (formule (k.eta)^4/27 employee hors de son domaine k.eta~O(1)).")

# ----------------------------------------------------------------------
# [7] INTEGRALE SPECTRALE / SENSIBILITE A LA COUPURE (NEUF) — le verrou.
# ----------------------------------------------------------------------
banner("[7] Scan LEADING (conserve) & sensibilite a la coupure k_UV.eta_*")

# Borne raccord (atlas D1) : eta_* = 1/H, H_* = H, a=1.
print("\n  Borne raccord (atlas D1, a=1) : eta_* = 1/H, script-H_* = H.")
print("  NB (v0.3) : ce bloc utilise la formule LEADING (k.eta)^4/27. Son « seuil » est un")
print("  ARTEFACT (cf. [6bis] : le mode EXACT ne croise jamais 0.5). Conserve pour trace.")
print("  Critere leading : Omega_sigma <~ 0.5 eps^2  <=>  (k.eta_*)^4 <~ 13.5.")
x_seuil = (13.5) ** sp.Rational(1, 4)
print("  Seuil LEADING (artefact) : k.eta_* <~ 13.5^(1/4) =", sp.N(x_seuil, 6), " (~ 1.9).")
assert abs(float(x_seuil) - 1.917) < 1e-2     # vrai pour la formule leading (algebre OK)

# Pont numerique mode-a-mode : f(x) = x^4/27, x = k.eta_*.
def ratio_mode(x):
    return x**4 / 27.0

# --- Mode M-P dominant : CGB (eq.85 + eq.89, verifie contre l'OCR de 2503.24263). ---
k_MP = 1e-8           # Hz   (eq.85)
dt_MP = 10.0          # s    (eq.89, onset (eta_inf - eta_GW) < 10 s)
x_raw = k_MP * dt_MP                 # ~ 1e-7
x_MP = 2e-7                          # valeur documentee LC-D3-WCH-GWE (O(1) ang. freq.)
print("\n  Mode M-P dominant (CGB) : k.eta_* = k.(eta_inf - eta_GW)")
print("    k ~ %.0e Hz, (eta_inf-eta_GW) ~ %.0f s  =>  k.eta_* ~ %.0e (brut), ~2e-7 (doc)."
      % (k_MP, dt_MP, x_raw))
for x, lab in [(x_raw, "brut 1e-7"), (x_MP, "doc 2e-7")]:
    r = ratio_mode(x)
    print("    k.eta_* = %-9s -> Omega_sigma/eps^2 = (k.eta_*)^4/27 = %.2e" % (lab, r))
r_MP = ratio_mode(x_MP)
print("  >>> verdict M-P : Omega_sigma/eps^2 ~ %.1e  <<  0.5  => REGIME (A), marge ~%.0e."
      % (r_MP, 0.5 / r_MP))
assert r_MP < 0.5 and r_MP < 1e-28          # ~1e-30, marge ~1e29 (cible)

# --- SENSIBILITE : scan de la coupure effective k_UV.eta_*, LEADING vs EXACT --------
print("\n  Scan k_UV.eta_* : formule LEADING (k.eta)^4/27 vs mode EXACT [6bis] :")
print("    %-12s | %-13s | %-7s | %-13s | regime" %
      ("k_UV.eta_*", "leading", "(lead)", "EXACT"))
print("    " + "-"*60)
scan = [2e-7, 1e-3, 1e-1, 1.0, float(x_seuil), 2.744, 5.0]
for x in scan:
    rl = ratio_mode(x)
    rx = R_exact(x)
    reg_l = "(A)" if rl <= 0.5 else "(B)"
    reg_x = "(A)" if rx <= 0.5 else "(B)"
    mark = "  <- artefact leading" if abs(x - float(x_seuil)) < 1e-2 else \
           ("  <- max exact" if abs(x - 2.744) < 1e-2 else "")
    print("    %-12.4g | %-13.3e | %-7s | %-13.3e | %s%s"
          % (x, rl, reg_l, rx, reg_x, mark))
print("    => colonne EXACT : (A) PARTOUT. La « bascule (B) » leading n'a pas de realite.")

# Variance integree (spectre plat) : la dependance (k.eta)^4 est celle du LEADING.
#   Le mode EXACT bornant le rapport a 0.377, l'integrale par octave reste O(A_T), bornee.
A_T_sym = sp.symbols('A_T', positive=True)
kUV_eta = sp.symbols('kUV_eta', positive=True)
Omega_tot = kUV_eta**4 / 108 * A_T_sym
print("\n  Variance (spectre plat A_T), forme LEADING : Omega_sigma^tot ~ (k_UV.eta_*)^4/108 . A_T")
print("    =", Omega_tot, "  (NB : c'est la croissance LEADING ; le mode exact plafonne, [6bis]).")

print("\n  LECTURE (v0.3, post-audit) :")
print("   - Mode regulier EXACT [6bis] : (A) a TOUTE echelle (max 0.377). La coupure spectrale")
print("     NE decide PAS (A) : la reserve « spectre M-P presumably » est MOOT (audit C5).")
print("   - Au pic CGB (k_UV.eta_* ~ 2e-7, super-horizon ~7 ordres), Omega_sigma/eps^2 ~ 6e-29")
print("     (illustration mono-mode ; PAS une 'marge de robustesse').")
print("   - Le VERROU primaire de (A) physique est la RETRO-ACTION INHOMOGENE (C7, hors de")
print("     portee) : (a) la selection WCH du mode regulier tient-elle POINTWISE en bang")
print("     inhomogene ? (b) les spikes (mesure nulle en localisation mais dynamiquement NON")
print("     negligeables -- la petitesse spatiale ne borne PAS la retro-action) retro-agissent-ils")
print("     sur <Omega_sigma> ? Renvoi Heinzle-Uggla (P6 4.5/4bis) : MARQUE cette reserve ouverte.")

# ----------------------------------------------------------------------
# VERDICT
# ----------------------------------------------------------------------
banner("VERDICT DU SCEAU")
print("""
  [1]    EOM radiation a=H.eta, mode regulier j0 = sin(k.eta)/(k.eta)        : OK
  [1bis] controle conforme : v=a.h satisfait v''+k^2v=0 (frottement absorbe) : OK
  [2-4]  FG : g0,g2 locaux ; g3 un-point = 0 (regulier) ; y0 singulier (meme  : OK
         Bessel que le mecanisme M-P, ordres differents) exclu par WCH ;
         residu deux-points <g3 g3>~k^3 => P_h~const (importe)
  [5]    E ~ g3 (proportionnalite transportee par raccord conforme ;  : ACQUIS (parent)
         facteur (d/2H) derive cote dS uniquement, non utilise ici)
  [6]    PONT leading : Omega_sigma/eps^2 = (k.eta)^4/27 (symbolique)  : CIBLE REPRODUITE
  [6bis] MODE EXACT : Omega_sigma/eps^2 = (x cos x - sin x)^2/(3 x^2)  : (A) a TOUTE echelle
         plafond 0.377 < 0.5 (x~2.74), ne croise jamais 0.5 -> AUCUNE bascule
  [7]    scan leading conserve ; son « seuil 1.9 » = ARTEFACT (cf [6bis])  : REGIME (A)

  >>> Le pont forme->cisaillement est VERIFIE SYMBOLIQUEMENT (leading [6] ET exact [6bis]).
      Le mode regulier WCH-selectionne est en REGIME (A) pour TOUT k.eta (max 0.377). Au pic
      CGB de M-P, Omega_sigma/eps^2 ~ 6e-29 (illustration mono-mode).

  >>> ALGEBRE ETABLIE. Le verdict (A) de LC-D3-WCH-GWE est `etabli (algebre)`. La WCH a un
      CONTENU DYNAMIQUE : l'exclusion du mode Y (Friedrich/A3-A4) + la dispersion super-horizon
      delivrent Omega_sigma << eps^2 A L'ORDRE DOMINANT.

  VERROU RESTANT (decision ouverte, non tranchee par l'algebre) -- DEPLACE par l'audit C5 :
      ce n'est PLUS le spectre M-P (rendu moot par le mode exact [6bis]), mais la
      RETRO-ACTION INHOMOGENE (C7, hors de portee) : selection WCH pointwise + retro-action
      des spikes sur le budget de cisaillement homogene. Renvoi Heinzle-Uggla = MARQUEUR de
      cette reserve, pas un appui.

  DISCIPLINE (LC-AUDIT-VERDICT 6.4) : `etabli` ici = l'algebre du pont et la reproduction
  des cibles. Ce n'est PAS « la physique de la CCC est etablie ».
""")
print("Tous les assert sont passes.")
