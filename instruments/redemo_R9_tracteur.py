#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R9_tracteur.py — Silo R, lot R-9 (module [B] : tracteur sur S²,
verdict B-PAUVRE, résidu = Weyl rescalé), protocole §2.0 étape 2 :
REDÉRIVATION depuis les prémisses nommées, cibles gelées
audit/R9-CIBLES-GELEES.md (sha256 7018b47e…91d1), corps des têtes
JAMAIS ouverts, REIMPORT.txt non lu à l'écriture du présent instrument.

PLAFOND ANNONCÉ AU GEL : E-2 (verdict révélé par deux canaux).

Prémisses : S² = section conforme 2D (sphère céleste / section de ℐ⁺,
module [A] : ℐ⁺ de genre espace, LC-A-SURVIE-CONFORME) ; géométrie de
Cartan conforme normale / calcul tracteur standard ; d ambiant = 4.

Ce script N'EST PAS un sceau de la KB. §6.4 : redériver ne scelle, ne
réduit, ne compte, ne démontre rien.
"""
import sys
import sympy as sp

ok = []
ncons = [0]


def check(name, cond):
    cond = bool(cond)
    ok.append(cond)
    print("  [PASS] %s" % name if cond else "  [FAIL] %s" % name)
    if not cond:
        sys.exit("ÉCHEC : " + name)


def consigne(txt):
    ncons[0] += 1
    print("  [CONSIGNATION] %s" % txt)


x, y, z = sp.symbols("x y z", real=True)
a, b, c = sp.symbols("a b c", real=True)

print("== A1[B1] : fibré tracteur standard — rang n+2 ==")
n = sp.Symbol("n", integer=True, positive=True)
rang = n + 2
check("rang(𝒯) = n+2 ; sur S² (n=2) : rang 4", rang.subs(n, 2) == 4)
consigne("série de composition 𝒯 ≃ ℰ[1] ⊕ TM[-1] ⊕ ℰ[-1] : IMPORT "
         "(tracteur standard, Bailey-Eastwood-Gover) — le rang seul est "
         "arithmétique ici")

print("== A2[B2] : 2D — Riemann à UNE composante, identité de section ==")
# métrique 2D GÉNÉRIQUE : trois fonctions arbitraires E,F,G de (x,y)
E = sp.Function("E")(x, y)
F = sp.Function("F")(x, y)
G = sp.Function("G")(x, y)
g = sp.Matrix([[E, F], [F, G]])
gi = g.inv()
co = (x, y)


def christoffel(g, gi, co):
    N = len(co)
    Gam = [[[0]*N for _ in range(N)] for _ in range(N)]
    for i_ in range(N):
        for j_ in range(N):
            for k_ in range(N):
                s = 0
                for l_ in range(N):
                    s += gi[i_, l_]*(sp.diff(g[l_, j_], co[k_])
                                     + sp.diff(g[l_, k_], co[j_])
                                     - sp.diff(g[j_, k_], co[l_]))
                Gam[i_][j_][k_] = sp.together(s/2)
    return Gam


def riemann_down(g, gi, co):
    N = len(co)
    Gam = christoffel(g, gi, co)
    Rup = [[[[0]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for r_ in range(N):
        for s_ in range(N):
            for m_ in range(N):
                for nu in range(N):
                    t = (sp.diff(Gam[r_][s_][nu], co[m_])
                         - sp.diff(Gam[r_][s_][m_], co[nu]))
                    for l_ in range(N):
                        t += (Gam[r_][m_][l_]*Gam[l_][s_][nu]
                              - Gam[r_][nu][l_]*Gam[l_][s_][m_])
                    Rup[r_][s_][m_][nu] = t
    Rd = [[[[0]*N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for a_ in range(N):
        for b_ in range(N):
            for m_ in range(N):
                for nu in range(N):
                    t = 0
                    for r_ in range(N):
                        t += g[a_, r_]*Rup[r_][b_][m_][nu]
                    Rd[a_][b_][m_][nu] = t
    return Rd


Rd = riemann_down(g, gi, co)
K = sp.simplify(Rd[0][1][0][1]/g.det())          # courbure sectionnelle
resid_max = 0
for a_ in range(2):
    for b_ in range(2):
        for m_ in range(2):
            for nu in range(2):
                cible = K*(g[a_, m_]*g[b_, nu] - g[a_, nu]*g[b_, m_])
                r_ = sp.simplify(Rd[a_][b_][m_][nu] - cible)
                if r_ != 0:
                    resid_max += 1
check("métrique 2D GÉNÉRIQUE (E,F,G libres) : R_abcd = K(g_ac g_bd − "
      "g_ad g_bc) IDENTIQUEMENT (16/16 composantes)", resid_max == 0)
check("⟹ une seule composante indépendante ; n²(n²−1)/12 = 1 à n=2",
      sp.Rational(2**2*(2**2 - 1), 12) == 1)
# tout le Riemann 2D est pure courbure scalaire ⟹ partie sans trace
# (Weyl) IDENTIQUEMENT NULLE : aucun invariant conforme local ne survit.

print("== A3[B3-support] : comptage du Weyl — le Weyl est AMBIANT ==")
f = n*(n + 1)*(n + 2)*(n - 3)/12
check("composantes du Weyl : f(3)=0 (nul en 3D)", f.subs(n, 3) == 0)
check("f(4)=10 (le Weyl n'existe qu'à partir de n=4)", f.subs(n, 4) == 10)
check("f(2) sans objet — couvert par A2 (2D : Riemann pure trace)", True
      if resid_max == 0 else False)
# ⟹ tout « Weyl » évalué sur S² est une donnée AMBIANTE (4D restreinte),
# jamais un invariant intrinsèque de la section — support de B3.

print("== A4[B1] : la ronde S² est conformément plate EXPLICITE ==")
r2 = x**2 + y**2
Om2 = 4/(1 + r2)**2                               # stéréographique
gS = Om2*sp.eye(2)
giS = gS.inv()
RdS = riemann_down(gS, giS, co)
KS = sp.simplify(RdS[0][1][0][1]/gS.det())
check("K[4/(1+r²)² δ] = 1 EXACT (métrique ronde en carte "
      "stéréographique, conforme à δ par construction)", KS == 1)
check("facteur conforme 4/(1+r²)² > 0 partout (classe conforme = "
      "classe plate)", Om2.subs({x: 0, y: 0}) == 4)

print("== A5[B6-jambe C] : Cotton 3D conformément plat = 0 ==")
phi = a*x*y + b*y*z**2 + c*x**2*z                 # 3e dérivées non triviales
co3 = (x, y, z)
g3 = sp.exp(2*phi)*sp.eye(3)
gi3 = g3.inv()
Rd3 = riemann_down(g3, gi3, co3)
Ric = sp.zeros(3, 3)
for a_ in range(3):
    for b_ in range(3):
        t = 0
        for m_ in range(3):
            for nu in range(3):
                t += gi3[m_, nu]*Rd3[m_][a_][nu][b_]
        Ric[a_, b_] = t
Rsc = sp.trace(gi3*Ric)
P3 = Ric - Rsc/4*g3                               # Schouten n=3 : Ric − (R/4)g
Gam3 = christoffel(g3, gi3, co3)


def covd_P(P, Gam, co, c_, a_, b_):
    t = sp.diff(P[a_, b_], co[c_])
    for l_ in range(3):
        t -= Gam[l_][c_][a_]*P[l_, b_] + Gam[l_][c_][b_]*P[a_, l_]
    return t


cot_res = 0
for a_ in range(3):
    for b_ in range(3):
        for c_ in range(3):
            Cabc = sp.simplify(covd_P(P3, Gam3, co3, a_, b_, c_)
                               - covd_P(P3, Gam3, co3, b_, a_, c_))
            if Cabc != 0:
                cot_res += 1
check("Cotton[e^{2φ}δ₃] = 0 (27/27 composantes) sur la famille "
      "φ = a·xy + b·yz² + c·x²z (3es dérivées non triviales)",
      cot_res == 0)
consigne("famille polynomiale à 3 paramètres, PAS le φ générique "
         "fonctionnel — évidence de famille, mordue par le firewall A6")

print("== A6 : FIREWALL Cotton — Nil (recoupe R-7/Q6) ==")
gN = sp.Matrix([[1, 0, 0], [0, 1 + x**2, -x], [0, -x, 1]])  # dx²+dy²+(dz−xdy)²
giN = gN.inv()
RdN = riemann_down(gN, giN, co3)
RicN = sp.zeros(3, 3)
for a_ in range(3):
    for b_ in range(3):
        t = 0
        for m_ in range(3):
            for nu in range(3):
                t += giN[m_, nu]*RdN[m_][a_][nu][b_]
        RicN[a_, b_] = sp.simplify(t)
RscN = sp.simplify(sp.trace(giN*RicN))
PN = RicN - RscN/4*gN
GamN = christoffel(gN, giN, co3)
nz = 0
sample = None
for a_ in range(3):
    for b_ in range(3):
        for c_ in range(3):
            Cabc = sp.simplify(covd_P(PN, GamN, co3, a_, b_, c_)
                               - covd_P(PN, GamN, co3, b_, a_, c_))
            if sp.simplify(Cabc.subs(x, 0)) != 0 or Cabc != 0:
                nz += 1
                if sample is None:
                    sample = Cabc
check("R[Nil] = −1/2 CONSTANT", RscN == sp.Rational(-1, 2))
check("Cotton[Nil] ≠ 0 (le test A5 n'est PAS vacant ; verrou porté "
      "par la non-platitude conforme)", nz > 0)
consigne("recoupement R-7/Q6 : même témoin Nil, R constant mais Cotton "
         "non nul — concordant, redérivé ici indépendamment")

print("== A7[B2,B6] : Ω^𝒯 = Weyl ⊕ Cotton ⟹ Cartan-plat sur S² ==")
consigne("décomposition Ω^𝒯 = W ⊕ C (courbure tracteur normale) : "
         "IMPORT (BEG/Čap-Gover) — non redérivée ; ses DEUX jambes le "
         "sont : W ≡ 0 en 2D/3D (A2/A3), C = 0 en conformément plat "
         "(A5, firewall A6)")
check("classe conforme de S² = classe plate (A4) ⟹ W-jambe nulle (A2) "
      "ET C-jambe nulle (A5) ⟹ Ω^𝒯 = 0 : géométrie de Cartan PLATE",
      resid_max == 0 and cot_res == 0 and KS == 1)
check("⟹ B-PAUVRE au sens « zéro invariant conforme local "
      "intrinsèque » : tout l'objet est le modèle plat (Möbius)", True
      if (resid_max == 0 and cot_res == 0) else False)
consigne("« au sens strict du critère » : le critère lui-même vit au "
         "corps NON OUVERT — lu ici comme « aucun invariant local » ; "
         "l'adéquation exacte au critère de la tête reste NON confrontée")

print("== A8[B7] : durcissement — le verdict ne tient qu'à dim 2 ==")
# A2 est GÉNÉRIQUE (E,F,G libres) : aucune rondeur, aucune symétrie
# n'est utilisée ⟹ toute perturbation de la section S² (dS perturbé
# compris) reste une métrique 2D ⟹ même conclusion.
check("A2 couvre la section PERTURBÉE (E,F,G arbitraires ⊃ ronde+δg) "
      "⟹ verdict stable par construction", resid_max == 0)
check("firewall dimensionnel : en 4D f(4)=10 ⟹ le même argument "
      "CASSE (les perturbations portent du Weyl)", f.subs(n, 4) != 0)
consigne("« durci sur dS perturbé (V98) » : la robustesse redérivée "
         "est celle de la SECTION 2D ; le contenu V98 exact (quel "
         "perturbé, quel ordre) vit au corps non ouvert — non confronté")

print("== A9[B3] : résidu localisé = Weyl RESCALÉ (ambiant) ==")
check("cohérence : intrinsèque nul (A2/A5) ∧ Weyl ambiant existant "
      "(f(4)=10) ⟹ tout contenu non trivial est AMBIANT-restreint, "
      "conforme à « résidu localisé »", resid_max == 0
      and f.subs(n, 4) == 10)
consigne("valeur du résidu : NON dérivée ici — recoupement R-7/Q4 "
         "(résidu rescalé fini non nul, témoin type I, 𝓔_i = 6q_i/H) ; "
         "B3 est cohérent, pas redémontré en substance")
consigne("B4 (depend_de [A]) : consigné — ℐ⁺ de genre espace et sa "
         "section S² présupposent LC-A-SURVIE-CONFORME (lot R-1, E-2)")

print("\nREDEMO R-9 : %d/%d PASS + %d consignations — EXIT 0"
      % (sum(ok), len(ok), ncons[0]))
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE (E-2, plafond annoncé "
      "AU GEL : verdict révélé par deux canaux).")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre "
      "rien. { A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.")
sys.exit(0)
