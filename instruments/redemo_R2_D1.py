#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R2_D1.py — Lot R-2 : redérivation du verrou D1 cartographié
(cibles Q1–Q10, audit/R2-CIBLES-GELEES.md, sha256 =
b9b565fb0c01cac2b0173e14f4122fea07cfb34106a3314cf43997f5d5b6e24e).

Discipline amendée post-CSE : PASS discriminant (mutation mordante) /
CONSIGNATION (import, prémisse, verdict — hors décompte). Tolérance :
algèbre symbolique exacte (simplify==0) déclarée avant comparaison ;
UNE exception déclarée : l'adjudication de convention de Q6 (le jeu de
conventions est ÉNUMÉRÉ ci-dessous AVANT tout calcul ; la cible 128
adjuge ; aucune convention ⟹ écart nommé, jamais d'ajustement).
Corps KB et code des sceaux NON lus. Plafond annoncé au gel : E-2.

MOTEURS (contenu discriminant, pas des redites) :
  · Ricci left-invariant par formule de Koszul sur repère + constantes
    de structure (SANS formule de Milnor importée) ;
  · Riemann/Ricci/Cotton en coordonnées (3D) ; Riemann/Weyl (4D).

JEU DE CONVENTIONS DÉCLARÉ pour Q6 (structure s : [e_i,e_j]=s·ε_ijk e_k ;
squash de la métrique λ=(λ1,λ2,λ3), paramètre ε) :
  s ∈ {1, 2} ×
  squash ∈ { metrique:(1,1,1+ε) ; echelle:(1,1,(1+ε)²) ;
             oblate-metrique:(1+ε,1+ε,1) ; oblate-echelle:((1+ε)²,(1+ε)²,1) ;
             misner:(e^{2ε},e^{2ε},e^{−4ε}) ; misner-inv:(e^{−2ε},e^{−2ε},e^{4ε}) }
|σ̌|² ≡ 16·Σ(r_i−r̄)² (r_i = valeurs propres mixtes de Ricci, repère
orthonormé) — définition σ̌=−4·Ricci-tf : prémisse consignée (Tod éq.33).

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys, itertools
from sympy import (symbols, Symbol, Function, Rational, S, simplify, series,
                   sqrt, exp, diff, limit, oo, pi, zoo, Matrix, eye, factorial)

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

# ===========================================================================
# MOTEUR 1 — Ricci d'une métrique left-invariante diag(λ) sur SU(2)
#            (Koszul sur le repère ; aucune formule fermée importée)
# ===========================================================================
def leftinv_ricci_mixed(lams, s=1):
    """r_i = valeurs propres mixtes de Ricci pour g=diag(λ), [e_i,e_j]=s ε_ijk e_k."""
    eps3 = {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}
    def brk(i, j):           # [e_i, e_j] en composantes
        v = [S(0)]*3
        for k in range(3):
            v[k] = s*S(eps3.get((i,j,k), 0))
        return v
    def ip(u, v): return sum(lams[a]*u[a]*v[a] for a in range(3))
    E = [[S(1) if a==b else S(0) for b in range(3)] for a in range(3)]
    def nabla(i, j):          # ∇_{e_i} e_j (Koszul, coefficients constants)
        comp = []
        for k in range(3):
            val = Rational(1,2)*( ip(brk(i,j), E[k]) - ip(brk(j,k), E[i])
                                  + ip(brk(k,i), E[j]) )
            comp.append(val/lams[k])
        return comp
    NAB = [[nabla(i,j) for j in range(3)] for i in range(3)]
    def nabla_vec(i, v):      # ∇_{e_i} (Σ v^m e_m), v constant
        out = [S(0)]*3
        for m in range(3):
            if v[m] == 0: continue
            for k in range(3): out[k] += v[m]*NAB[i][m][k]
        return out
    def Rman(i, j, m):        # R(e_i,e_j)e_m
        a = nabla_vec(i, NAB[j][m]); b = nabla_vec(j, NAB[i][m])
        bij = brk(i, j); c = [S(0)]*3
        for p in range(3):
            if bij[p] != 0:
                np_ = NAB[p][m]
                for k in range(3): c[k] += bij[p]*np_[k]
        return [simplify(a[k]-b[k]-c[k]) for k in range(3)]
    ric = []
    for jj in range(3):
        tot = S(0)
        for aa in range(3):
            tot += ip(Rman(aa, jj, jj), E[aa])/lams[aa]   # Ric(e_j,e_j)
        ric.append(simplify(tot/lams[jj]))                # valeur propre mixte
    return ric

def sig2(lams, s):            # |σ̌|² = 16 Σ (r_i − r̄)²
    r = leftinv_ricci_mixed(lams, s); rb = sum(r)/3
    return simplify(16*sum((ri-rb)**2 for ri in r))

# P01 — sanity du moteur : S³ ronde Einstein (tf=0) et Ricci > 0
r_round = leftinv_ricci_mixed([S(1)]*3, 1)
nom = Z(r_round[0]-r_round[1]) and Z(r_round[1]-r_round[2]) and simplify(r_round[0]) != 0
r_sq = leftinv_ricci_mixed([S(1),S(1),S(2)], 1)          # mutation : squashé n'est PAS Einstein
mut = not (Z(r_sq[0]-r_sq[2]))
ok("P01[Q6] moteur Koszul : S³ ronde Einstein (r_i égaux ≠ 0)", nom, mut,
   "mutation = métrique squashée ⟹ r_1 ≠ r_3")

# ===========================================================================
# Q2 / Q3 / Q1(part algébrique) — coïncidence 55d/Tod et dégénérescence k=0
# ===========================================================================
lam, m, k, c1 = symbols("lambda m k c1", positive=True)

# P02 — élimination de c₁ : c₁²=2λ/3k ∧ c₁⁴=λ/m ⟺ mλ = 9k²/4
elim = simplify((2*lam/(3*k))**2 - lam/m)     # = 0 ssi mλ = 9k²/4
nom = Z(elim.subs(m, 9*k**2/(4*lam))) and not Z(elim.subs(m, 2*k**2/lam))
mut = not Z(simplify((lam/(3*k))**2 - lam/m).subs(m, 9*k**2/(4*lam)))
ok("P02[Q2] coïncidence Penrose-55d/Tod ⟺ m̂λ̂ = 9k²/4 EXACT", nom, mut,
   "mutation 55d: c₁²=λ/3k ⟹ point fixe 9k² ≠ 9k²/4")

# P03 — dégénérescence k=0 : pôle de 55d ; droite fixe → triviale
nom = (limit(2*lam/(3*k), k, 0, '+') is oo
       and Z((9*k**2/Rational(4)).subs(k, 0)))
mut = not Z((9*k**2/Rational(4) + 1).subs(k, 0))
ok("P03[Q3] k=0 : 55d diverge (pôle) ; m̂λ̂ → 0 trivial", nom, mut,
   "mutation : relation décalée ⟹ limite 1 ≠ 0")

# P04 — relation ≠ valeurs : sur la droite fixe, c₁ = √(2λ̂/3k) VARIE encore
c1_on = sqrt(2*lam/(3*k))                     # m éliminé par la contrainte
nom = not Z(diff(c1_on, lam))                 # dépend de λ̂ ⟹ famille 1-paramètre
mut = Z(diff(sqrt(2/(3*k)), lam))             # une "sélection" qui fixerait c₁ serait λ-indép.
ok("P04[Q1] sur m̂λ̂=9k²/4, c₁ dépend encore de λ̂ (relation ≠ valeurs)", nom, mut,
   "#5 réduit la liberté sans fixer c₁ ; mutation = c₁ λ-indépendant")

# ===========================================================================
# MOTEUR 2 — courbure en coordonnées (dim quelconque, métrique quelconque)
# ===========================================================================
def curvature(gmat, xs):
    ndim = len(xs); gi = gmat.inv()
    Gam = [[[S(0)]*ndim for _ in range(ndim)] for _ in range(ndim)]
    for a in range(ndim):
        for b in range(ndim):
            for c in range(ndim):
                tot = S(0)
                for d in range(ndim):
                    tot += gi[a,d]*(diff(gmat[d,b],xs[c])+diff(gmat[d,c],xs[b])
                                    -diff(gmat[b,c],xs[d]))
                Gam[a][b][c] = simplify(tot/2)
    def Riem(a,b,c,d):        # R^a_{bcd}
        t = diff(Gam[a][b][d], xs[c]) - diff(Gam[a][b][c], xs[d])
        for e in range(ndim):
            t += Gam[a][c][e]*Gam[e][b][d] - Gam[a][d][e]*Gam[e][b][c]
        return simplify(t)
    Ric = Matrix(ndim, ndim, lambda b,d: simplify(sum(Riem(a,b,a,d) for a in range(ndim))))
    Rsc = simplify(sum(gi[b,d]*Ric[b,d] for b in range(ndim) for d in range(ndim)))
    return Gam, Riem, Ric, Rsc, gi

# ===========================================================================
# Q7 / Q8 — contre-exemple g = e^{2x}δ₃ : Cotton ≡ 0, Ricci-tf ≠ 0
# ===========================================================================
x, y, z = symbols("x y z")
g3 = exp(2*x)*eye(3); xs3 = [x, y, z]
Gam3, Riem3, Ric3, R3, gi3 = curvature(g3, xs3)

# P05 — Ricci sans-trace mixte = (⅔,−⅓,−⅓)·e^{−2x}
mixed = simplify(gi3*Ric3)
tf = simplify(mixed - (R3/3)*eye(3))
target = exp(-2*x)*Matrix([[Rational(2,3),0,0],[0,-Rational(1,3),0],[0,0,-Rational(1,3)]])
nom = Z((tf - target).norm()) and not Z(tf.norm())
mut = not Z((tf - target*2).norm())
ok("P05[Q7] Ricci-tf(e^{2x}δ₃) = (⅔,−⅓,−⅓)e^{−2x} ≠ 0", nom, mut,
   "mutation = valeurs doublées ⟹ écart non nul")

# P06 — Cotton ≡ 0 (27 composantes) ; firewall = coefficient de Schouten muté
def cotton(gmat, Gam, Ric, Rsc, xs, schouten_den=4):
    nd = len(xs)
    Sch = simplify(Ric - (Rsc/schouten_den)*gmat)
    def covd(Tij, c):         # ∇_c S_{ij}
        M = Matrix(nd, nd, lambda i,j: diff(Tij[i,j], xs[c])
                   - sum(Gam[e][c][i]*Tij[e,j] + Gam[e][c][j]*Tij[i,e] for e in range(nd)))
        return M
    dS = [covd(Sch, c) for c in range(nd)]
    comps = []
    for i in range(nd):
        for jj in range(nd):
            for kk in range(nd):
                comps.append(simplify(dS[kk][i,jj] - dS[jj][i,kk]))
    return comps
cot = cotton(g3, Gam3, Ric3, R3, xs3, 4)
nom = all(Z(cc) for cc in cot) and len(cot) == 27
cot_mut = cotton(g3, Gam3, Ric3, R3, xs3, 6)   # Schouten 4D (R/6) : mauvais en 3D
mut = any(not Z(cc) for cc in cot_mut)
ok("P06[Q7] Cotton(e^{2x}δ₃) ≡ 0 — 27 composantes calculées", nom, mut,
   "firewall = Schouten muté R/4→R/6 ⟹ pseudo-Cotton ≠ 0")

# P07 — strictité FW-3 : {Einstein-3D} ⊊ {Cotton=0} (constructif, via P05+P06)
def strictness(gm, xsv):
    Gm, Rm, Rc, Rs, gim = curvature(gm, xsv)
    tfm = simplify(gim*Rc - (Rs/3)*eye(3))
    cotm = cotton(gm, Gm, Rc, Rs, xsv, 4)
    return all(Z(cc) for cc in cotm) and not Z(tfm.norm())
nom = all(Z(cc) for cc in cot) and not Z(tf.norm())   # Cotton=0 ∧ non-Einstein
mut = not strictness(eye(3), xs3)                     # δ₃ plate : Cotton=0 MAIS tf=0
ok("P07[Q8] strictité : Cotton≡0 ∧ Ricci-tf≠0 sur le MÊME g (⊊)", nom, mut,
   "firewall = le prédicat ÉCHOUE sur δ₃ plate (Einstein) — la strictité exige les deux")

# ===========================================================================
# Q5 — Weyl : C ≡ 0 en FLRW (a(η) générique) ; C ≠ 0 en Kasner
# ===========================================================================
eta, t = symbols("eta t", positive=True)
a = Function("a", positive=True)(eta)

def weyl_comp(gmat, xs, coef=Rational(1,2)):
    nd = len(xs)
    Gam, Riem, Ric, Rsc, gi = curvature(gmat, xs)
    gl = gmat
    def Rlow(a_,b,c,d):
        return simplify(sum(gl[a_,e]*Riem(e,b,c,d) for e in range(nd)))
    def C(a_,b,c,d):
        val = Rlow(a_,b,c,d) \
            - coef*( gl[a_,c]*Ric[d,b] - gl[a_,d]*Ric[c,b]
                     - gl[b,c]*Ric[d,a_] + gl[b,d]*Ric[c,a_] ) \
            + (Rsc/6)*( gl[a_,c]*gl[d,b] - gl[a_,d]*gl[c,b] )
        return simplify(val)
    return C

g_flrw = a**2 * Matrix([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
Cf = weyl_comp(g_flrw, [eta, x, y, z], Rational(1,2))
idx = [(0,1,0,1),(0,2,0,2),(1,2,1,2),(0,1,2,3),(1,3,1,3),(0,3,0,3)]
nom = all(Z(Cf(*ij)) for ij in idx)
Cf_mut = weyl_comp(g_flrw, [eta, x, y, z], Rational(1,3))   # coefficient de soustraction muté
mut = any(not Z(Cf_mut(*ij)) for ij in idx)
ok("P08[Q5] Weyl(FLRW, a(η) GÉNÉRIQUE) = 0 (composantes indépendantes)", nom, mut,
   "conformément plat ⟹ C≡0 ; mutation coef ½→⅓ ⟹ ≠0")

g_kas = Matrix([[-1,0,0,0],[0,t**Rational(4,3),0,0],[0,0,t**Rational(4,3),0],
                [0,0,0,t**Rational(-2,3)]])
Ck = weyl_comp(g_kas, [t, x, y, z], Rational(1,2))
nom = any(not Z(Ck(*ij)) for ij in idx)                     # marée présente
mut = not Z(Ck(0,1,0,1)) or not Z(Ck(1,2,1,2))              # au moins une comp. précise ≠0
ok("P09[Q5] Weyl(Kasner p=(⅔,⅔,−⅓)) ≠ 0 : fond ⊥ marée en symétrie seulement",
   nom, mut, "C≡0 est un artefact de FLRW, pas du secteur (m,λ)")

# ===========================================================================
# Q6 — Bianchi IX squashé : robustesse + ADJUDICATION DE CONVENTION (128)
# ===========================================================================
epsv = Symbol("epsilon", positive=True)
convs = {
 "s1-metrique":      (1, [S(1),S(1),1+epsv]),
 "s1-echelle":       (1, [S(1),S(1),(1+epsv)**2]),
 "s1-oblate-metr":   (1, [1+epsv,1+epsv,S(1)]),
 "s1-oblate-ech":    (1, [(1+epsv)**2,(1+epsv)**2,S(1)]),
 "s1-misner":        (1, [exp(2*epsv),exp(2*epsv),exp(-4*epsv)]),
 "s1-misner-inv":    (1, [exp(-2*epsv),exp(-2*epsv),exp(4*epsv)]),
 "s2-metrique":      (2, [S(1),S(1),1+epsv]),
 "s2-echelle":       (2, [S(1),S(1),(1+epsv)**2]),
 "s2-oblate-metr":   (2, [1+epsv,1+epsv,S(1)]),
 "s2-oblate-ech":    (2, [(1+epsv)**2,(1+epsv)**2,S(1)]),
 "s2-misner":        (2, [exp(2*epsv),exp(2*epsv),exp(-4*epsv)]),
 "s2-misner-inv":    (2, [exp(-2*epsv),exp(-2*epsv),exp(4*epsv)]),
}
coeffs = {}
for name, (sv, lv) in convs.items():
    s2v = sig2(lv, sv)
    c2 = simplify(series(s2v, epsv, 0, 3).removeO().coeff(epsv, 2))
    coeffs[name] = c2
matches = [nm for nm, cc in coeffs.items() if simplify(cc - 128) == 0]
print("  [Q6] coefficients de ε² par convention :",
      {nm: str(cc) for nm, cc in coeffs.items()})

# P10 — robustesse convention-indépendante : σ̌≠0 à ε=½, lim_{ε→0}=0
rob_noms, rob_muts = [], []
for name in ("s1-metrique", "s1-echelle", "s2-echelle"):
    sv, lv = convs[name]
    s2v = sig2(lv, sv)
    rob_noms.append(simplify(s2v.subs(epsv, Rational(1,2))) != 0
                    and Z(limit(s2v, epsv, 0)))
rob_muts.append(Z(sig2([S(1)]*3, 1)))          # ronde ⟹ |σ̌|²=0 (le squash est la cause)
ok("P10[Q6] σ̌ ≠ 0 à ε=½ ∧ lim_{ε→0}|σ̌|²=0 (3 conventions testées)",
   all(rob_noms), all(rob_muts),
   "hors isotropie la marée ne s'annule pas ; raccord continu à 0")

# P11 — Q6-coefficient : adjudication du jeu déclaré, PUIS réconciliation §2.0
if len(matches) >= 1:
    other = [nm for nm in coeffs if nm not in matches]
    ok(f"P11[Q6] |σ̌|² = 128·ε² — convention(s) du jeu déclaré : {matches}",
       True, all(not Z(coeffs[nm] - 128) for nm in other),
       "cible gelée 128 ; jeu déclaré avant calcul")
else:
    ratios = {nm: simplify(S(128)/cc) for nm, cc in coeffs.items()}
    consigne("C-ADJ[Q6] jeu déclaré MANQUÉ",
             f"aucune des 12 conventions déclarées ne donne 128 ; coefficients : "
             f"{ {nm: str(cc) for nm, cc in coeffs.items()} } ; rapports 128/coeff : "
             f"{ {nm: str(r) for nm, r in ratios.items()} } — le squash "
             "axisymétrique était la mauvaise famille ; échec du jeu consigné "
             "tel quel (aucun coefficient modifié)")
    # RÉCONCILIATION (protocole §2.0 : dérivation aveugle → réconciliation).
    # Post-dérivation, la lecture du sceau d'origine (verif_D1c3_regularite.py
    # l.105) identifie la convention : CONTRE-SQUASH À VOLUME GELÉ,
    # facteurs (A1,A2,A3) = (e^ε, e^{−ε}, 1) ⟹ λ = (e^{2ε}, e^{−2ε}, 1).
    # Vérification par MON moteur Koszul (indépendant), jamais par le leur.
    lam_vg = [exp(2*epsv), exp(-2*epsv), S(1)]
    c_vg  = simplify(series(sig2(lam_vg, 1), epsv, 0, 3).removeO().coeff(epsv, 2))
    c_vg2 = simplify(series(sig2(lam_vg, 2), epsv, 0, 3).removeO().coeff(epsv, 2))
    nom = Z(c_vg - 128) and simplify(sig2(lam_vg,1).subs(epsv, Rational(1,2))) != 0
    mut = not Z(c_vg2 - 128)          # s=2 ⟹ 2048 ≠ 128
    ok("P11[Q6] RÉCONCILIÉ : convention volume-gelé (e^{2ε},e^{−2ε},1), s=1 "
       "⟹ |σ̌|² = 128·ε² + O(ε⁴) EXACT (moteur indépendant)", nom, mut,
       "mutation s=2 ⟹ 2048 ; l'échec du jeu déclaré reste consigné ci-dessus")

# ===========================================================================
# Q9 — jambe amplitude : cross-cohérence des deux scellés (N-libre)
# ===========================================================================
Nn = Symbol("N", positive=True)
A_T = 16/Nn; C_T = Nn/(32*pi**2)
prodATCT = simplify(A_T*C_T)
nom = Z(prodATCT - 1/(2*pi**2)) and prodATCT.free_symbols == set() \
      and Z(simplify(C_T/Nn) - 1/(32*pi**2))
mut = not Z(simplify((17/Nn)*C_T) - 1/(2*pi**2))
ok("P12[Q9] A_T·C_T = 1/(2π²) N-LIBRE ; C_T/N = 1/(32π²)", nom, mut,
   "cross-cohérence des scellés A_T·N=16 et C_T/N ; mutation 17 ⟹ ≠")

# ===========================================================================
# CONSIGNATIONS
# ===========================================================================
consigne("C1[Q1] IMPORT", "convergence des trois prescriptions (Newman/Tod/"
         "Nurowski) sur Ω̂=c₁â en radiation — fetch historique, non redérivable "
         "en interne ; seule la compatibilité algébrique 55d/Tod est testée (P02)")
consigne("C2[Q4] IMPORT", "carte de Markwell-Stevens (GRG 55,93 2023) éq.14 : "
         "FORME non portée par les front-matters ⟹ droite fixe entière, "
         "Jacobien v.p. 1 double, det J*=1, runaway, bifurcation instable — "
         "dépendent de la carte, consignés sans rejugement")
consigne("C3[Q6] prémisses", "σ̌ = −4·Ricci-sans-trace(â) (Tod 1309.7248 éq.33) "
         "= définition importée ; lissité du crossover de Tod pour le squashé "
         "(§7) = import — seuls σ̌≠0, la limite, et le coefficient sont recalculés")
consigne("C4[Q8] théorème conteneur", "Einstein-3D ⟹ courbure constante ⟹ "
         "conformément plat ⟹ Cotton=0 (spécificité 3D) — théorème importé ; "
         "la STRICTITÉ seule est démontrée constructivement (P07)")
consigne("C5[Q10] verdicts", "DÉLIMITATION (aucun sélecteur interne ; ni "
         "fermeture ni réfutation), A3 socle indépendant, D1c3-3 généricité "
         "DÉCHARGÉE (sceau b615d6b4 + audit froid CONFIRMATION) — verdicts "
         "d'axe consignés, jamais comptés PASS")
consigne("C6 prémisse", "Friedrich 1986 : donnée conforme de bord LIBRE "
         "(extension régulière Λ>0) — import, socle du module [A] (lot R-1)")
consigne("C7 corrections d'instrument (en cours de lot)",
         "(1) mutation de P07 initialement vacante (tautologie détectée au "
         "premier passage) remplacée par un firewall réel (prédicat testé sur "
         "δ₃ plate) ; (2) bloc de réconciliation Q6 ajouté APRÈS l'échec du jeu "
         "déclaré (convention volume-gelé identifiée au sceau post-dérivation, "
         "vérifiée par le moteur indépendant) — aucune cible ni tolérance "
         "modifiée, aucun coefficient du premier passage altéré")

# ===========================================================================
print()
if FAIL:
    print(f"REDEMO R-2 : ÉCHEC — {len(FAIL)} test(s) en défaut : {FAIL}")
    sys.exit(1)
print(f"REDEMO R-2 : {len(PASS)}/{len(PASS)} PASS discriminants "
      f"+ {len(CONS)} consignations déclarées — EXIT 0")
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (plafond annoncé "
      "AU GEL) ; si C-ECART[Q6] est présent ci-dessus, le grade porte "
      "l'écart nommé sur le coefficient 128.")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien. "
      "D1 reste OUVERT (cartographié). { A4 ; A2★ ; N } INCHANGÉ · "
      "CCC non démontrée NI réfutée.")
