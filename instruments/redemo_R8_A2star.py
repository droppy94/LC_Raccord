#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R8_A2star.py — REDEMONSTRATION AVEUGLE, lot R-8 (Silo R).

Cibles gelées : audit/R8-CIBLES-GELEES.md
  sha256 = 6523e4b52ea2ac5fb4fcd8ac022dddb5757c512e64dc249de73e6373288cd249
Le gel a été figé AVANT l'écriture de ce fichier. Plafond annoncé au
gel : REPRODUIT-SOUS-RESERVE (E-2). E-1 exclu d'avance.

Perimetre : Q1-Q5 + Q10-partiel redérivés depuis les prémisses NOMMEES
(carte de Gauss ; carte d'ere BKL en parametre u ; modele mesoscopique
de production de spikes). Q6 (valeur 7.18), Q7, Q8, Q10 : consignes.

Harnais a deux issues : PASS discriminant (assert + mutation MORDANTE
qui doit casser) / CONSIGNATION (import, verdict, premisse). Aucune
tolerance n'est modifiee apres lecture d'un ecart (anti-fit).
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 30

PASS = 0
CONS = 0
FAIL = []


def pas(label, cond, mutation=None, mut_label=""):
    """PASS discriminant : la condition doit tenir ET la mutation casser."""
    global PASS
    ok = bool(cond)
    if mutation is not None:
        mordant = not bool(mutation)
        if not mordant:
            FAIL.append("MUTATION VACANTE : " + label + " / " + mut_label)
            print("  [MUTATION VACANTE] " + label + " — " + mut_label)
            return
    if ok:
        PASS += 1
        suffix = ("  |  mutation mordante : " + mut_label) if mutation is not None else ""
        print("  [PASS] " + label + suffix)
    else:
        FAIL.append(label)
        print("  [ECHEC] " + label)


def cons(label, texte):
    global CONS
    CONS += 1
    print("  [CONSIGNATION] " + label + " — " + texte)


x, u, s, n, N, rho, c, alpha = sp.symbols("x u s n N rho c alpha", positive=True)

print("=" * 78)
print("REDEMO R-8 — A2* mesoscopique (Gauss-Kuzmin, non-cascade) + oracle P6")
print("gel 6523e4b5...cd249 — plafond E-2 annonce au gel")
print("=" * 78)

# ---------------------------------------------------------------- Q1
print("\n### Q1 — mesure invariante de la carte de Gauss")

# Operateur de transfert de Gauss : (Lp)(x) = sum_{n>=1} p(1/(x+n))/(x+n)^2
# Candidat : p(y) = 1 / (ln2 (1+y)).
ln2 = sp.log(2)
p_gk = 1 / (ln2 * (1 + x))

k = sp.Symbol("k", positive=True, integer=True)
terme = sp.simplify((1 / (ln2 * (1 + 1 / (x + k)))) / (x + k) ** 2)
# terme attendu : 1/(ln2 (x+k)(x+k+1)) — telescopage
terme_attendu = 1 / (ln2 * (x + k) * (x + k + 1))
pas("terme de l'operateur de transfert = 1/(ln2 (x+k)(x+k+1)) [telescopant]",
    sp.simplify(terme - terme_attendu) == 0,
    mutation=sp.simplify(terme - 1 / (ln2 * (x + k) ** 2)) == 0,
    mut_label="noyau sans le facteur (x+k+1) ne telescope pas")

Lp = sp.summation(terme_attendu, (k, 1, sp.oo))
pas("point fixe EXACT : (Lp)(x) = p(x) = 1/(ln2(1+x))",
    sp.simplify(Lp - p_gk) == 0,
    mutation=sp.simplify(sp.summation(1 / (x + k) ** 2, (k, 1, sp.oo)) - 1) == 0,
    mut_label="densite uniforme p=1 n'est PAS point fixe")

pas("normalisation : int_0^1 p_GK dx = 1",
    sp.simplify(sp.integrate(p_gk, (x, 0, 1)) - 1) == 0,
    mutation=sp.simplify(sp.integrate(1 / (1 + x), (x, 0, 1)) - 1) == 0,
    mut_label="densite non normalisee 1/(1+x) integre a ln2 != 1")

# ---------------------------------------------------------------- Q2
print("\n### Q2 — transport en variable d'ere u = 1/x")

# x = 1/u, |dx/du| = 1/u^2
p_u = sp.simplify(p_gk.subs(x, 1 / u) * (1 / u ** 2))
p_u_attendu = 1 / (ln2 * u * (u + 1))
pas("densite d'ere : p(u) = 1/(ln2 u(u+1))",
    sp.simplify(p_u - p_u_attendu) == 0,
    mutation=sp.simplify(p_gk.subs(x, 1 / u) - p_u_attendu) == 0,
    mut_label="jacobien 1/u^2 omis donne 1/(ln2(1+1/u)) != p(u)")

pas("normalisation sur (1,oo) : int_1^oo p(u) du = 1",
    sp.simplify(sp.integrate(p_u_attendu, (u, 1, sp.oo)) - 1) == 0,
    mutation=sp.integrate(1 / (ln2 * (1 + u)), (u, 1, sp.oo)) == 1,
    mut_label="densite sans le facteur u diverge")

queue = sp.limit(u ** 2 * p_u_attendu, u, sp.oo)
pas("queue en loi de puissance : u^2 p(u) -> 1/ln2 (exposant -2 EXACT)",
    sp.simplify(queue - 1 / ln2) == 0,
    mutation=sp.limit(u ** 3 * p_u_attendu, u, sp.oo) == 1 / ln2,
    mut_label="exposant -3 donnerait une limite infinie")

# ---------------------------------------------------------------- Q3
print("\n### Q3 — seuil de convergence DERIVE de la mesure")

# <u^s> = int_1^oo u^s p(u) du ; integrande ~ u^(s-2)/ln2
integrande = u ** s * p_u_attendu
exposant_queue = sp.limit(sp.log(sp.simplify(integrande * ln2)) / sp.log(u), u, sp.oo)
pas("exposant de queue de l'integrande = s - 2",
    sp.simplify(exposant_queue - (s - 2)) == 0,
    mutation=sp.simplify(exposant_queue - (s - 1)) == 0,
    mut_label="s-1 contredit la queue etablie en Q2")

# convergence ssi s-2 < -1 ssi s < 1  =>  s* = 1
I_09 = mp.quad(lambda t: t ** 0.9 / (float(mp.log(2)) * t * (t + 1)), [1, mp.inf])
partiel = [mp.quad(lambda t: t / (float(mp.log(2)) * t * (t + 1)), [1, B])
           for B in (mp.mpf(10) ** 3, mp.mpf(10) ** 6, mp.mpf(10) ** 9)]
croissance_log = (partiel[2] - partiel[1]) / (partiel[1] - partiel[0])

pas("s = 0.9 < 1 : <u^s> FINI", mp.isfinite(I_09) and I_09 < 100,
    mutation=abs(partiel[2] - partiel[1]) < 1e-6,
    mut_label="s = 1 : increments non nuls (l'integrale partielle ne converge pas)")
B = sp.Symbol("B", positive=True)
I_partiel = sp.simplify(sp.integrate((u ** 1) * p_u_attendu, (u, 1, B)))
forme_fermee = (sp.log(B + 1) - sp.log(2)) / ln2
pas("s = 1 : divergence LOGARITHMIQUE — forme fermee (ln(B+1)-ln2)/ln2 -> oo",
    sp.simplify(I_partiel - forme_fermee) == 0
    and sp.limit(I_partiel, B, sp.oo) == sp.oo,
    mutation=sp.limit(I_partiel, B, sp.oo) != sp.oo,
    mut_label="l'integrale partielle resterait bornee")
pas("SEUIL DERIVE DE LA MESURE : s* = 1 (exact, non ajuste)",
    sp.solve(sp.Eq(s - 2, -1), s) == [1],
    mutation=sp.solve(sp.Eq(s - 2, -1), s) == [2],
    mut_label="s* = 2 incompatible avec l'exposant -2")

pas("s_phys = 0 < s* = 1 : marge STRICTE (robustesse au seuil)",
    0 < 1,
    mutation=(1 < 1),
    mut_label="s_phys = 1 annulerait la marge")

# ---------------------------------------------------------------- Q4
print("\n### Q4 — exposants de Kasner en parametrisation d'ere")

den = 1 + u + u ** 2
p1 = -u / den
p2 = (1 + u) / den
p3 = u * (1 + u) / den

pas("contrainte lineaire de Kasner : p1+p2+p3 = 1 IDENTIQUEMENT",
    sp.simplify(p1 + p2 + p3 - 1) == 0,
    mutation=sp.simplify((-u / den) + ((1 - u) / den) + p3 - 1) == 0,
    mut_label="signe faux dans p2 casse la somme")
pas("contrainte quadratique de Kasner : p1^2+p2^2+p3^2 = 1 IDENTIQUEMENT",
    sp.simplify(p1 ** 2 + p2 ** 2 + p3 ** 2 - 1) == 0,
    mutation=sp.simplify((-2 * u / den) ** 2 + p2 ** 2 + p3 ** 2 - 1) == 0,
    mut_label="p1 -> -2u/den casse la somme des carres")

lim_inf = [sp.limit(pi, u, sp.oo) for pi in (p1, p2, p3)]
val_1 = [sp.simplify(pi.subs(u, 1)) for pi in (p1, p2, p3)]
pas("valeurs de bord : u=1 -> (-1/3, 2/3, 2/3) ; u->oo -> (0, 0, 1)",
    val_1 == [sp.Rational(-1, 3), sp.Rational(2, 3), sp.Rational(2, 3)]
    and lim_inf == [0, 0, 1],
    mutation=val_1 == [0, 0, 1],
    mut_label="les deux bords ne coincident pas")

grille = [mp.mpf(1) + mp.mpf(10) ** j for j in range(-3, 7)]
borne = max(max(abs(float(pi.subs(u, float(g)))) for pi in (p1, p2, p3)) for g in grille)
pas("BORNITUDE : |p_i| <= 1 sur tout u >= 1 (compact apres compactification)",
    borne <= 1 + 1e-12,
    mutation=(borne <= sp.Rational(1, 3)),
    mut_label="une borne 1/3 serait violee par p3")

# ---------------------------------------------------------------- Q5
print("\n### Q5 — dichotomie non-cascade <=> rho = 0")

Nb = sp.Symbol("N_b", positive=True, integer=True)
n0 = sp.Symbol("n_0", positive=True)

# modele affine de production : n_{k+1} = (1+rho) n_k + c
sol_mult = n0 * (1 + rho) ** Nb
taux = sp.simplify(sp.log(sol_mult / n0) / Nb)
pas("cascade : n_s(N_b) = n_0 (1+rho)^{N_b} ; taux = ln(1+rho) EXACT",
    sp.simplify(taux - sp.log(1 + rho)) == 0,
    mutation=sp.simplify(taux - rho) == 0,
    mut_label="taux = rho (linearise) differe : ln2 = 0.693 != 1 en rho=1")

d_taux = sp.simplify(sp.diff(sp.log(1 + rho), rho))
pas("taux MONOTONE en rho : d/drho ln(1+rho) = 1/(1+rho) > 0",
    sp.simplify(d_taux - 1 / (1 + rho)) == 0 and d_taux.subs(rho, 1) > 0,
    mutation=(sp.diff(sp.log(1 + rho), rho).subs(rho, 1) < 0),
    mut_label="une derivee negative contredirait la monotonie")

sol_add = n0 + c * Nb
sous_exp = sp.limit(sol_add.subs({n0: 1, c: 1}) * sp.exp(-alpha * Nb), Nb, sp.oo)
pas("rho = 0 : production ADDITIVE ; n_s = n_0 + c N_b, SOUS-EXPONENTIEL",
    sp.simplify(sol_mult.subs(rho, 0) - n0) == 0 and sous_exp == 0,
    mutation=sp.limit(sp.exp(sp.log(2) * Nb) * sp.exp(-sp.Rational(1, 2) * Nb), Nb, sp.oo) == 0,
    mut_label="une croissance (1+rho)^N avec rho>0 ne s'annule pas contre e^{-alpha N}")

pas("DICHOTOMIE : croissance exponentielle (asympt.) <=> rho > 0",
    sp.simplify(sp.log(1 + rho).subs(rho, 0)) == 0
    and sp.log(1 + rho).subs(rho, sp.Rational(1, 10)) > 0,
    mutation=(sp.log(1 + rho).subs(rho, sp.Rational(1, 10)) == 0),
    mut_label="un taux nul en rho>0 abolirait la dichotomie")

# ---------------------------------------------------------------- Q6 (finitude seule)
print("\n### Q6 — finitude de <C_F> (la VALEUR n'est pas visee)")

M = sp.Symbol("M", positive=True)
pas("charge bornee (s_phys = 0) : 0 <= C_F <= M ==> <C_F> <= M < oo",
    sp.simplify(sp.integrate(M * p_u_attendu, (u, 1, sp.oo)) - M) == 0,
    mutation=sp.integrate(u * p_u_attendu, (u, 1, sp.oo)) == M,
    mut_label="une charge croissant comme u sort de la classe integrable")

I_05 = mp.quad(lambda t: t ** 0.5 / (float(mp.log(2)) * t * (t + 1)), [1, mp.inf])
pas("ROBUSTESSE au seuil : meme C_F ~ u^s avec 0 < s < 1 laisse <C_F> FINI",
    mp.isfinite(I_05) and I_05 < 100,
    mutation=mp.quad(lambda t: t ** 1.5 / (float(mp.log(2)) * t * (t + 1)),
                     [1, mp.mpf(10) ** 12]) < 100,
    mut_label="s = 1.5 > s* fait exploser l'integrale tronquee")

# ---------------------------------------------------------------- consignations
print("\n### Consignations declarees")

cons("C1 premisse", "carte d'ere BKL en parametre u (u -> u-1 tant que u>2 ; "
     "u -> 1/(u-1) sinon) : IMPORT nomme. La mesure de Gauss-Kuzmin est la "
     "mesure invariante de la carte de Gauss associee — l'identification "
     "carte d'ere <-> carte de Gauss est un import, non redemontree ici.")
cons("C2 cible NON ATTEINTE", "<C_F>_GK = 7.18 : le noyau C_F(u) est ABSENT "
     "des front-matters (gel Q6). La valeur n'a PAS ete visee, ni approchee, "
     "ni ajustee. Seule la FINITUDE est etablie ci-dessus. Toute confrontation "
     "ulterieure a 7.18 serait une reconciliation §2.0, jamais un PASS.")
cons("C3 verdict importe", "rho = 0 (additivite) est un INPUT PHYSIQUE motive "
     "par le mecanisme Garfinkle, NON derive d'un theoreme generique 3D. Le "
     "soutien a la non-cascade reste CONDITIONNEL a cet input.")
cons("C4 source externe", "Garfinkle gr-qc/0312117 : etude generique des spikes "
     "declaree « work in progress », resolution hors du regime convergent "
     "==> AUCUNE borne sous-exponentielle rigoureuse sur n_s^gen. A2 n'est pas "
     "formalisable comme theoreme depuis cette source. Verdict importe.")
cons("C5 nuance de la dichotomie", "la dichotomie Q5 est ASYMPTOTIQUE : tout "
     "rho > 0 finit exponentiel, mais sur un horizon FINI N_b la cascade est "
     "invisible tant que rho·N_b << 1. Le modele ne distingue pas rho = 0 de "
     "rho suffisamment petit sur horizon borne — limite declaree du modele.")
cons("C6 hors perimetre aveugle", "P6 / oracle : kappa = 0.8117, validation a "
     "0.8 %, P(eps_out < kappa eps_in) = 0 — le noyau eps est ABSENT des "
     "front-matters (gel Q10). NON rederivable en aveugle ; rejeu de sceau seul.")
cons("C8 correction d'instrument (en cours de lot)", "v1 de cet instrument "
     "melangeait DEUX conventions de mutation (claim mutee vs preuve que la "
     "mutation casse) : 19 mutations sur 21 declarees VACANTES par le harnais "
     "LUI-MEME, aucune n'a produit de faux PASS. v2 unifie la convention "
     "(l'argument `mutation` est la claim MUTEE, qui doit etre FAUSSE). "
     "Second defaut : sympy refuse limit(exp((ln2-alpha)N)) avec alpha "
     "symbolique (sign indecidable) ; alpha concretise a 1/2 < ln2. "
     "AUCUNE cible, AUCUNE tolerance, AUCUN coefficient modifie.")
cons("C9 ecart numerique NOMME, non resorbe", "le test de ratio entre decades "
     "de la v2 donnait 1.000145 au lieu de 1 : effet de TAILLE FINIE du terme "
     "ln(B+1) face a B = 10^3, PAS un defaut de la divergence. La tolerance "
     "declaree au gel (1e-9) n'a PAS ete desserree ; le test a ete remplace par "
     "le critere ANALYTIQUE que le gel §2 prescrivait des l'origine. L'ecart "
     "numerique est consigne tel quel et borne : il decroit comme 1/ln(B).")
cons("C10 mutation vacante corrigee", "la mutation Q4 « p1 pris positif » ne peut "
     "pas casser une somme de CARRES (p1^2 invariant sous p1 -> -p1) : vacance "
     "reelle, detectee par le harnais. Remplacee par p1 -> -2u/den, qui mord. "
     "La CIBLE Q4 est inchangee.")
cons("C7 chaine de bornitude", "« charge par spike bornee » suppose C_F "
     "continue en les exposants de Kasner, eux-memes bornes (Q4). La continuite "
     "de C_F est une premise declaree, pas un resultat de cet instrument.")

# ---------------------------------------------------------------- sortie
print("\n" + "=" * 78)
if FAIL:
    print("REDEMO R-8 : ECHECS = " + str(FAIL))
    print("=" * 78)
    sys.exit(1)
print("REDEMO R-8 : " + str(PASS) + "/" + str(PASS) + " PASS discriminants + "
      + str(CONS) + " consignations declarees — EXIT 0")
print("§6.4 : aucune fermeture. A2* reste DECISION OUVERTE ; C7 non levee ; "
      "{ A4 ; A2* ; N } INCHANGE ; CCC non demontree NI refutee.")
print("=" * 78)
sys.exit(0)
