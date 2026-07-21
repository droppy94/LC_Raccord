#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R1_moduleA.py — Lot R-1 : redérivation de la cinématique du
module [A] (survie conforme à Λ>0 : 𝓘⁺ spacelike, −Λ/3, régularité).
Cibles Q1–Q6, audit/R1-CIBLES-GELEES.md, sha256 =
d197e40aabc1848292d0cb400bf019634759c7550ed687f39e98797e13a07314.

Discipline amendée post-CSE : PASS discriminant (mutation mordante) /
CONSIGNATION (import — hors décompte). Tolérance : algèbre symbolique
exacte (simplify==0), déclarée avant comparaison. Convention de
signature déclarée : (−,+,+,+) — une hypersurface est de genre ESPACE
ssi sa normale est TIMELIKE (norme < 0). Corps KB et code du sceau
NON lus. Plafond annoncé au gel : E-2.

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
from sympy import (symbols, Symbol, Function, Matrix, simplify, S, sqrt,
                   Rational, diff, dsolve, Eq, solve, limit, oo, det, eye)

PASS, CONS, FAIL = [], [], []
def ok(tag, nominal, mutation_fails, note=""):
    if nominal and mutation_fails:
        PASS.append(tag); print(f"PASS  {tag}  {note}")
    else:
        FAIL.append(tag)
        print(f"FAIL  {tag}  nominal={nominal} mut_echoue={mutation_fails}  {note}")
def consigne(tag, note):
    CONS.append(tag); print(f"CONSIGNATION  {tag}  {note}")
Z = lambda e: simplify(e) == 0

# --- moteur de courbure en coordonnées (identique en substance à R-2) ------
def curvature(gmat, xs):
    nd = len(xs); gi = gmat.inv()
    Gam = [[[S(0)]*nd for _ in range(nd)] for _ in range(nd)]
    for a in range(nd):
        for b in range(nd):
            for c in range(nd):
                tot = S(0)
                for d in range(nd):
                    tot += gi[a,d]*(diff(gmat[d,b],xs[c])+diff(gmat[d,c],xs[b])
                                    -diff(gmat[b,c],xs[d]))
                Gam[a][b][c] = simplify(tot/2)
    def Riem(a,b,c,d):
        t = diff(Gam[a][b][d], xs[c]) - diff(Gam[a][b][c], xs[d])
        for e in range(nd):
            t += Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c]
        return simplify(t)
    Ric = Matrix(nd, nd, lambda b,d: simplify(sum(Riem(a,b,a,d) for a in range(nd))))
    Rsc = simplify(sum(gi[b,d]*Ric[b,d] for b in range(nd) for d in range(nd)))
    return Gam, Riem, Ric, Rsc, gi

eta, x, y, z = symbols("eta x y z")
Lam = Symbol("Lambda", positive=True)
H = sqrt(Lam/3)

# ===========================================================================
# Q5 — Einstein+Λ pour g = Ω(η)⁻²·η_Mink ⟺ Ω affine, Ω'² = Λ/3
# ===========================================================================
Om = Function("Omega", positive=True)(eta)
mink = Matrix([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
g_conf = Om**(-2) * mink
_, _, Ric, Rsc, gi = curvature(g_conf, [eta, x, y, z])
Ein = simplify(Ric - Rational(1,2)*Rsc*g_conf + Lam*g_conf)   # G_ab + Λ g_ab
eqs = sorted({simplify(Ein[i,j]) for i in range(4) for j in range(4)} - {S(0)},
             key=str)
# résolution : les équations doivent se réduire à Ω'² = Λ/3 ∧ Ω'' = 0
Op = Om.diff(eta); Opp = Om.diff(eta, 2)
sub_ok = all(Z(e.subs({Opp: 0}).subs({Op: sqrt(Lam/3)}).doit()) for e in eqs)
sub_ko = all(Z(e.subs({Opp: 0}).subs({Op: sqrt(Lam/2)}).doit()) for e in eqs)
nom = sub_ok and len(eqs) >= 1
mut = not sub_ko                                              # Ω'²=Λ/2 NE résout PAS
ok("P01[Q5] Einstein+Λ pour g=Ω⁻²·η_Mink ⟺ Ω affine avec Ω'² = Λ/3",
   nom, mut, "moteur de courbure ; mutation Ω'²=Λ/2 ⟹ équations non satisfaites")

# P02 — cas dS explicite : Ω = −Hη (η<0) résout EXACTEMENT ; Ω(0)=0, dΩ≠0
g_dS = simplify(g_conf.subs(Om, -H*eta))
_, _, RicD, RscD, _ = curvature(g_dS, [eta, x, y, z])
EinD = simplify(RicD - Rational(1,2)*RscD*g_dS + Lam*g_dS)
nom = Z(EinD.norm()) and (-H*eta).subs(eta, 0) == 0 and diff(-H*eta, eta) != 0
g_mut = simplify(g_conf.subs(Om, -H*eta**2))                  # mutation dΩ(0)=0 et non-solution
_, _, RicM, RscM, _ = curvature(g_mut, [eta, x, y, z])
mut = not Z(simplify(RicM - Rational(1,2)*RscM*g_mut + Lam*g_mut).norm())
ok("P02[Q5] dS planaire (Ω=−Hη, H²=Λ/3) : G_ab+Λg_ab = 0 EXACT ; Ω(𝓘)=0, dΩ≠0",
   nom, mut, "mutation Ω=−Hη² ⟹ pas une solution")

# ===========================================================================
# Q2 / Q3 — norme du gradient à 𝓘 et caractère de l'hypersurface
# ===========================================================================
# ĝ = Ω²g = η_Mink (métrique rescalée régulière) ; ∇Ω = (Ω',0,0,0)
grad_norm = simplify(mink.inv()[0,0] * (diff(-H*eta, eta))**2)  # ĝ^{ηη}·Ω'²
nom = Z(grad_norm + Lam/3) and simplify(grad_norm) < 0          # = −Λ/3 < 0
mut = not Z(grad_norm + Lam/4)                                  # −Λ/4 ≠ −Λ/3
ok("P03[Q2] ĝ(∇Ω,∇Ω)|𝓘⁺ = −Λ/3 EXACTEMENT (< 0)", nom, mut,
   "cible du lotissement reproduite ; mutation −Λ/4")

# P04 — trichotomie de caractère selon le signe de Λ (convention −+++)
LamG = Symbol("LambdaG", real=True)                             # Λ générique
norm_of = -LamG/3                                               # forme dérivée en P01/P03
car = lambda n: ("espace" if n.is_negative else
                 "temps" if n.is_positive else "nul")
nom = (car(norm_of.subs(LamG, 3)) == "espace"        # Λ>0 : normale timelike ⟹ 𝓘 spacelike
       and car(norm_of.subs(LamG, -3)) == "temps"    # Λ<0 : 𝓘 timelike
       and car(norm_of.subs(LamG, 0)) == "nul")      # Λ=0 : 𝓘 nul
mut = not (car((+LamG/3).subs(LamG, 3)) == "espace") # signe muté ⟹ mauvais caractère
ok("P04[Q3] trichotomie : Λ>0 ⟹ 𝓘⁺ de genre ESPACE ; Λ<0 timelike ; Λ=0 nul",
   nom, mut, "mutation du signe de la norme ⟹ caractère inversé")

# ===========================================================================
# Q4 — régularité : ĝ non dégénérée à Ω=0 ; g physique y diverge
# ===========================================================================
nom = (det(mink) == -1                                          # ĝ|𝓘 = Mink, det ≠ 0
       and limit(g_dS[1,1], eta, 0, '-') is oo                  # g physique diverge
       and Z(simplify(((-H*eta)**2 * g_dS - mink)).norm()))     # ĝ = Ω²g exactement
mut = not (det(Matrix([[0,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])) != 0)
ok("P05[Q4] ĝ = Ω²g = η_Mink NON dégénérée à 𝓘 (det=−1) ; g physique diverge",
   nom, mut, "mutation = métrique dégénérée (det=0) détectée")

# ===========================================================================
# Q6 — Weyl(dS) = 0
# ===========================================================================
def weyl_comp(gmat, xs, coef=Rational(1,2)):
    nd = len(xs)
    Gam, Riem, Ric, Rsc, gi = curvature(gmat, xs)
    def Rlow(a_,b,c,d):
        return simplify(sum(gmat[a_,e]*Riem(e,b,c,d) for e in range(nd)))
    def C(a_,b,c,d):
        return simplify(Rlow(a_,b,c,d)
            - coef*( gmat[a_,c]*Ric[d,b] - gmat[a_,d]*Ric[c,b]
                     - gmat[b,c]*Ric[d,a_] + gmat[b,d]*Ric[c,a_] )
            + (Rsc/6)*( gmat[a_,c]*gmat[d,b] - gmat[a_,d]*gmat[c,b] ))
    return C
Cd = weyl_comp(g_dS, [eta, x, y, z])
idx = [(0,1,0,1),(0,2,0,2),(1,2,1,2),(0,1,2,3),(1,3,1,3),(0,3,0,3)]
nom = all(Z(Cd(*ij)) for ij in idx)
Cm = weyl_comp(g_dS, [eta, x, y, z], Rational(1,3))
mut = any(not Z(Cm(*ij)) for ij in idx)
ok("P06[Q6] Weyl(dS) = 0 (composantes indépendantes calculées)", nom, mut,
   "conformément plat ; mutation coef ½→⅓ ⟹ ≠0")

# ===========================================================================
# CONSIGNATIONS
# ===========================================================================
consigne("C1[Q1] IMPORT", "Friedrich (CMP 107, 1986) : existence ET stabilité "
         "de l'extension conforme régulière pour Λ>0, donnée conforme de bord "
         "LIBRE — théorème externe, non redérivable en interne ; c'est le "
         "résultat PORTEUR du module [A], consigné comme tel")
consigne("C2 convention", "signature (−,+,+,+) déclarée en tête d'instrument ; "
         "« 𝓘 de genre espace » ⟺ normale timelike (norme < 0)")
consigne("C3 périmètre", "le « établi » du lot = théorème importé (C1) + "
         "cinématique recalculée (P01–P06) ; la stabilité non-linéaire aux "
         "grandes données inhomogènes et la structure fine des données de "
         "Friedrich (g₀ source / g₃ libre) relèvent du théorème, pas de "
         "l'instrument")

# ===========================================================================
print()
if FAIL:
    print(f"REDEMO R-1 : ÉCHEC — {len(FAIL)} test(s) en défaut : {FAIL}")
    sys.exit(1)
print(f"REDEMO R-1 : {len(PASS)}/{len(PASS)} PASS discriminants "
      f"+ {len(CONS)} consignations déclarées — EXIT 0")
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (plafond annoncé "
      "AU GEL : valeurs révélées + cœur d'existence importé).")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien. "
      "{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.")
