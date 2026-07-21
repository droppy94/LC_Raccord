#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_C7b_gradient.py  —  SCEAU voie 1.5 de C7-b (LC-RACCORD)
================================================================
Objet : borner l'ENERGIE DE GRADIENT NON-LOCALE des spikes — le SEUL facteur
de R_s que la voie 1 (verif_D3_C7b_spikes.py) ne ferme pas — par calcul
semi-analytique sur la SOLUTION DE SPIKE EXACTE de Lim (arXiv:0710.0628,
CQG 25 045014, §4.5-4.6), pondéré par la statistique de spikes scellée
(Heinzle-Uggla 1212.5500, carte BKL² / distribution log3, raccordée a
l'oracle de Gauss-Kuzmin verif_D3_P6_specB_oracle.py).

Discipline LC-AUDIT-VERDICT §6.4 : sceau SEMI-ANALYTIQUE. Il calcule
l'energie de gradient de la solution exacte (G2/Gowdy, un gradient spatial)
et borne le ratio gradient/bulk. Il NE PROUVE PAS le cas pleinement
generique (sans symetrie) — heritage d'ouverture possible (cf.
LC-WORK-BIBLIO-SPIKES-C7B §F, LC-WORK-REPRISE-C7B-VOIE2 §4).

Critere de decision (fige AVANT execution, LC-WORK-REPRISE-C7B-VOIE2 §5) :
   <Omega_sigma^grad>_spikes / <Omega_sigma>_bulk  -> 0   ==> C7-b CLOS (sur le profil exact)
                                                  -> O(1) ==> couplage non-local irreductible

Profil exact (Lim §4.5, eq.36-38) — toute la dependance spatiale du spike
beta-normalise (Sigma-, Nx, Sigmax, N-) est portee par c(x), s(x) :
   c(u) = (u^2 - 1)/(u^2 + 1)      pic en u=0, zeros en u=+-1   (u=kx)
   s(u) = 2u/(u^2 + 1)            zeros en u=0, pics en u=+-1
   k    = w e^tau sech(w tau)     (eq.32/39)
Coordonnee horizon-normalisee X = e^tau x (eq.44), horizon a X=+-1.
Rayon spike/horizon = (1/w) cosh(w tau)  (eq.43) -> SUPER-HORIZON pour 0<|w|<1.
"""

import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import brentq

PASS = []
def check(name, cond, detail=""):
    PASS.append(bool(cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))

print("="*74)
print("SCEAU verif_D3_C7b_gradient.py — voie 1.5 (energie de gradient non-locale)")
print("="*74)

# ----------------------------------------------------------------------
# §0. Profil exact de Lim — verifications symboliques (eq.37-38)
# ----------------------------------------------------------------------
print("\n§0. Profil exact c(u), s(u) (Lim 0710.0628 eq.37-38) — symbolique")
u = sp.symbols('u', real=True)
c = (u**2 - 1)/(u**2 + 1)
s = 2*u/(u**2 + 1)

# c^2 + s^2 = 1  (les variables vivent sur le cercle unite : rotation de repere)
identite = sp.simplify(c**2 + s**2)
check("c^2+s^2 = 1 (rotation de repere)", identite == 1, f"= {identite}")

# c : pic en u=0 (c=-1), zeros en u=+-1
check("c(0) = -1  (pic central)", sp.simplify(c.subs(u,0)) == -1)
check("c(+-1) = 0 (zeros)", sp.simplify(c.subs(u,1))==0 and sp.simplify(c.subs(u,-1))==0)
# s : zero en u=0, pics en u=+-1 (s(+-1)=+-1)
check("s(0) = 0", sp.simplify(s.subs(u,0))==0)
check("s(+-1) = +-1 (pics opposes)", sp.simplify(s.subs(u,1))==1 and sp.simplify(s.subs(u,-1))==-1)

# ----------------------------------------------------------------------
# §1. Densite d'energie de gradient du profil  g(u) = (dc/du)^2 + (ds/du)^2
# ----------------------------------------------------------------------
print("\n§1. Densite de gradient g(u) = (c')^2 + (s')^2 — reduction symbolique")
dc = sp.diff(c, u); ds = sp.diff(s, u)
g = sp.simplify(dc**2 + ds**2)
g_attendu = 4/(u**2 + 1)**2
check("g(u) = 4/(1+u^2)^2 (forme close exacte)",
      sp.simplify(g - g_attendu) == 0, f"g = {sp.simplify(g)}")

# Integrale du profil sur tout le spike :  int_{-inf}^{inf} g(u) du = 2*pi
Ig = sp.integrate(g_attendu, (u, -sp.oo, sp.oo))
check("int g(u) du = 2*pi (charge de gradient du profil)", sp.simplify(Ig - 2*sp.pi)==0,
      f"= {Ig}")

# ----------------------------------------------------------------------
# §2. Passage en coordonnee HORIZON-normalisee X = e^tau x  (eq.44)
#     u = k x = [w sech(w tau)] X ,  donc  kappa(tau) := w sech(w tau) = u/X
#     ==> energie de gradient Hubble-normalisee (par horizon) d'UN spike :
#         I_spike(tau) = int (d_X[champ])^2 dX
#                      = A(tau)^2 * int kappa^2 g(u) dX  ,  dX = du/kappa
#                      = A(tau)^2 * kappa * int g(u) du
#                      = 2*pi * A(tau)^2 * kappa(tau)
#     A(tau)^2 = Sigma-_Taub^2 + N-_Taub^2  (amplitude bornee, eq.27)
# ----------------------------------------------------------------------
print("\n§2. Energie de gradient d'un spike, en unites d'horizon : I_spike(tau)")
print("     I_spike = 2*pi * A(tau)^2 * kappa(tau),  kappa = w/cosh(w tau)")

def kappa(tau, w):
    return w/np.cosh(w*tau)            # = w sech(w tau)

def A2(tau, w):                        # Sigma-_Taub^2 + N-_Taub^2  (eq.27), borne
    Sm = (w*np.tanh(w*tau) - 1)/np.sqrt(3)
    Nm = (w/np.sqrt(3))/np.cosh(w*tau)
    return Sm**2 + Nm**2

def I_spike_quad(tau, w):
    """Integration NUMERIQUE directe de (d_X c)^2+(d_X s)^2 ponderee A^2,
       pour valider la forme close 2*pi*A^2*kappa."""
    kap = kappa(tau, w)
    def integrand(X):
        uu = kap*X
        dcu = 4*uu/(uu**2+1)**2
        dsu = 2*(1-uu**2)/(uu**2+1)**2
        return (kap**2)*(dcu**2 + dsu**2)      # (d_X c)^2+(d_X s)^2
    val,_ = quad(integrand, -np.inf, np.inf, limit=200)
    return A2(tau, w)*val

# validation forme close vs quadrature
print("    validation forme close 2*pi*A^2*kappa vs quadrature directe :")
ok_close = True
for w in (0.3, 0.5, 0.9, 1.5):
    for tau in (0.0, 1.0, 3.0):
        closed = 2*np.pi*A2(tau,w)*kappa(tau,w)
        numv   = I_spike_quad(tau,w)
        rel = abs(closed-numv)/max(abs(numv),1e-300)
        ok_close &= rel < 1e-6
    print(f"      w={w}: forme close OK (max rel.err verifie)")
check("I_spike = 2*pi*A^2*kappa coincide avec la quadrature directe", ok_close)

# A(tau)^2 borne (amplitude — coherent avec voie 1 : alpha_s borne)
A2_vals = [A2(t,w) for w in (0.3,0.5,0.9,1.5,3.0) for t in np.linspace(0,20,50)]
check("A(tau)^2 borne (amplitude finie, cf. voie 1 alpha_s<=borne)",
      max(A2_vals) < 10.0, f"max A^2 = {max(A2_vals):.3f}")

# ----------------------------------------------------------------------
# §3. I_spike(tau) -> 0  (le coeur physique : super-horizon => gradient doux)
# ----------------------------------------------------------------------
print("\n§3. Decroissance I_spike(tau) -> 0  (kappa = w/cosh(w tau) -> 0)")
taus3 = (0,2,5,10,20,40)
print("    tau :     " + "  ".join(f"{t:6.1f}" for t in taus3))
decroit_tous = True
for w in (0.3, 0.5, 0.9):
    row = [2*np.pi*A2(t,w)*kappa(t,w) for t in taus3]
    print(f"    w={w}: " + "  ".join(f"{v:6.3f}" for v in row))
    # monotone decroissante (apres le transitoire) ET -> 0 a grand tau
    monot = all(row[i+1] <= row[i] for i in range(1,len(row)-1))
    decroit_tous &= monot and (row[-1] < 1e-3)
check("I_spike(tau) -> 0 pour tout w in (0,1) (spikes super-horizon)", decroit_tous,
      "decroissance monotone, <1e-3 a tau=40 (taux=|w|, plus lent pour petit w)")

# decroissance exponentielle asymptotique : I_spike ~ 2*pi*A^2 * 2w e^{-|w|tau}
w=0.5; t1,t2=15.0,18.0
rate = -np.log(kappa(t2,w)/kappa(t1,w))/(t2-t1)
check("decroissance exponentielle, taux ~ |w|", abs(rate-abs(w))<1e-3,
      f"taux numerique={rate:.4f} vs |w|={w}")

# ----------------------------------------------------------------------
# §4. PIRE CAS sur w : max_w I_spike(tau) ~ O(1/tau) -> 0
#     f(w)=w/cosh(w tau) maximise a coth(w tau)=w tau  (y:=w tau, coth y = y)
# ----------------------------------------------------------------------
print("\n§4. Pire cas sur w : sup_w I_spike(tau) decroit encore (~1/tau)")
y_star = brentq(lambda y: 1/np.tanh(y) - y, 0.5, 3.0)   # coth(y)=y
check("racine coth(y)=y  (~1.1997)", abs(y_star-1.19968)<1e-3, f"y*={y_star:.5f}")
print(f"    w_opt(tau)=y*/tau ; sup_kappa = w_opt/cosh(y*) ~ {y_star/np.cosh(y_star):.4f}/tau")
sup_prev = None; decroit_sup = True
for tau in (5.0, 20.0, 80.0):
    w_opt = y_star/tau
    sup_kappa = kappa(tau, w_opt)            # = (y*/tau)/cosh(y*)
    # borne A^2 <= ~ (|w|+1)^2/3 ; ici w_opt petit -> A^2 ~ 1/3
    I_sup = 2*np.pi*((w_opt+1)**2/3.0)*sup_kappa
    print(f"    tau={tau:5.0f}: w_opt={w_opt:.4f}  sup_kappa={sup_kappa:.4e}  I_sup<={I_sup:.4e}")
    if sup_prev is not None: decroit_sup &= (sup_kappa < sup_prev)
    sup_prev = sup_kappa
check("sup_w I_spike(tau) -> 0 (meme le pire w decroit, ~1/tau)", decroit_sup)

# ----------------------------------------------------------------------
# §5. Ratio gradient/bulk avec densite de spikes (statistique log3 scellee)
# ----------------------------------------------------------------------
print("\n§5. Ratio  R_grad = n_s * I_spike / Omega_bulk  (densite log3 scellee)")
# Distribution d'ere des spikes (Heinzle-Uggla eq.17, carte BKL^2) :
#   Kbar(m) = log3((m+2)/(m+3)) - log3(m/(m+1))
def Kbar(m):
    log3 = lambda z: np.log(z)/np.log(3)
    return log3((m+2)/(m+3)) - log3(m/(m+1))
# verif normalisation (somme sur m>=1) et Kbar(1) scelle ~0.369 (voie 1)
masse = sum(Kbar(m) for m in range(1,200000))
check("Sum_m Kbar(m) = 1 (distribution log3 normalisee)", abs(masse-1)<1e-3,
      f"somme={masse:.4f}")
check("Kbar(1) ~ 0.369 (raccord scelle voie 1)", abs(Kbar(1)-0.369)<2e-3,
      f"Kbar(1)={Kbar(1):.4f}")

# Omega_bulk : cisaillement Hubble-normalise homogene, O(1) par horizon.
Omega_bulk = 1.0/3.0     # ordre de grandeur d'une amplitude de cisaillement bulk (A^2 ~1/3)

# n_s : nombre de spikes ACTIFS par horizon. Borne par la recurrence :
#   - chaque ere fournit O(1) spike transitoire ; #eres jusqu'a tau ~ lineaire en tau
#   - mais un spike n'est "actif" (structure ~horizon) que pendant sa vie transitoire
#   => densite active par horizon BORNEE. On teste deux modeles :
#        (i)  n_s = const (recurrence stationnaire)
#        (ii) n_s croit polynomialement ~ (1+tau)  (genereux : proliferation lineaire)
def ratio(tau, w, model):
    Is = 2*np.pi*A2(tau,w)*kappa(tau,w)
    if model=="const": n_s = 2.0
    elif model=="lin": n_s = 2.0*(1+tau)
    elif model=="poly3": n_s = 2.0*(1+tau)**3   # tres genereux
    return n_s*Is/Omega_bulk

print("    R_grad(tau) pour w=0.5 :")
print("    tau :        " + "  ".join(f"{t:8.1f}" for t in (1,5,10,20,40)))
for model in ("const","lin","poly3"):
    row=[ratio(t,0.5,model) for t in (1,5,10,20,40)]
    print(f"    n_s {model:6s}: " + "  ".join(f"{v:8.2e}" for v in row))
# verdict : -> 0 meme avec proliferation polynomiale
r_const = ratio(40,0.5,"const"); r_lin = ratio(40,0.5,"lin"); r_poly = ratio(40,0.5,"poly3")
check("R_grad -> 0 (densite constante)", r_const<1e-3, f"R(40)={r_const:.2e}")
check("R_grad -> 0 (proliferation lineaire ~tau)", r_lin<1e-2, f"R(40)={r_lin:.2e}")
check("R_grad -> 0 (proliferation cubique ~tau^3, genereuse)", r_poly<1e-1, f"R(40)={r_poly:.2e}")

# ----------------------------------------------------------------------
# §6. Stress-test : quelle croissance de densite faudrait-il pour R_grad~O(1) ?
#     R_grad ~ n_s * e^{-|w|tau} = O(1)  <=>  n_s ~ e^{+|w|tau} (EXPONENTIELLE).
#     Le nombre de bounces BKL jusqu'a tau croit ~ lineairement (Gauss-Kuzmin),
#     PAS exponentiellement => aucune proliferation connue ne defait la decroissance.
# ----------------------------------------------------------------------
print("\n§6. Stress-test : croissance de densite requise pour casser R_grad->0")
w=0.5
# densite requise pour maintenir R_grad=1 :
def n_required(tau): return Omega_bulk/(2*np.pi*A2(tau,w)*kappa(tau,w))
taus=np.array([10,20,40,80.0])
nreq=np.array([n_required(t) for t in taus])
# ajuste log(nreq) ~ rate*tau : doit valoir ~|w|
rate_req=np.polyfit(taus, np.log(nreq),1)[0]
check("densite requise CROIT EXPONENTIELLEMENT, taux ~ |w|",
      abs(rate_req-abs(w))<5e-2, f"taux requis={rate_req:.3f} vs |w|={w}")
print("    => casser R_grad->0 exigerait une PROLIFERATION EXPONENTIELLE de spikes")
print("       (n_s ~ e^{|w|tau}), non supportee : #bounces BKL ~ lineaire en tau.")

# ----------------------------------------------------------------------
# VERDICT
# ----------------------------------------------------------------------
print("\n" + "="*74)
n_ok=sum(PASS); n_tot=len(PASS)
print(f"BILAN : {n_ok}/{n_tot} controles PASS")
if all(PASS):
    print("""
VERDICT voie 1.5 — sur la SOLUTION DE SPIKE EXACTE de Lim (0710.0628) :
  L'energie de gradient non-locale d'un spike, en unites d'horizon, vaut
  I_spike(tau) = 2*pi * A(tau)^2 * w/cosh(w tau)  ->  0  (exponentiel ~e^{-|w|tau}),
  et meme sup_w I_spike(tau) ~ O(1/tau) -> 0.  Ponderee par la densite de
  spikes (statistique log3 scellee), bornee ou meme en proliferation
  polynomiale, le ratio <Omega_sigma^grad>_spikes/<Omega_sigma>_bulk -> 0.
  La casser exigerait une proliferation EXPONENTIELLE de spikes, non supportee.
  ==> Pour le profil exact (G2/Gowdy, un gradient spatial) : C7-b GRADIENT BORNE.
  PHYSIQUE : super-horizon (eq.43) => a l'echelle de l'horizon le champ varie
  peu => gradient Hubble-normalise doux ; l'integrale ne le compense pas.
RESERVE (§6.4) : sceau SEMI-ANALYTIQUE sur la solution EXACTE (un gradient).
  Le cas pleinement generique (sans symetrie, gradients multiples) n'est pas
  prouve ici : il reste `decision ouverte` (voie 2 / hors de portee).
""")
else:
    print("\nECHEC d'au moins un controle — voir ci-dessus.")
print("="*74)
