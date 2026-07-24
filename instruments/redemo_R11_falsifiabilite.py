#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REDEMO R-11 — Falsifiabilite F1-F6 "epuisee" + memoire BMS (BORD-EON V-A)
              + W2 / WCH-GWE.

Derive contre le gel GEL-R11.md (sha8 298e2094) + AMENDEMENT-1 (sha8 9d30fce6).
Plafond de grade annonce AU GEL : E-2 (REPRODUIT-SOUS-RESERVE).

sympy seul. Corps des tetes JAMAIS ouverts. Code des sceaux JAMAIS lu.
"""

import sys
import sympy as sp

PASS = 0
FAILED = 0
CONS = 0

# porteurs mutables par le harnais -------------------------------------------
P_F1_OP = sp.Rational(3, 32)          # coefficient Osborn-Petkou : 3/(32 pi^2)
P_F1_PROG = sp.Rational(3, 4)         # coefficient programme     : 3/(4 pi^4)
P_F2_EXP_AT = -1                      # A_T ~ N^(-1)
P_F6_TRACE = 1                        # active la soustraction de trace
P_F6_DIM = 3                          # dimension utilisee dans le 1/d
P_W2_NUM = 1                          # facteur du numerateur du mode exact
P_F6_PSEUDO = 1                       # applique le facteur det(P) des pseudo-tenseurs
P_T1_REDUC = frozenset()              # inconnues retirees par les fronts


def check(cond, label):
    global PASS, FAILED
    ok = bool(cond)
    if ok:
        PASS += 1
        print("  [PASS] " + label)
    else:
        FAILED += 1
        print("  [FAIL] " + label)
    return ok


def consigne(label):
    global CONS
    CONS += 1
    print("  [CONSIGNATION] " + label)


def titre(t):
    print("\n" + "=" * 70)
    print(t)
    print("=" * 70)


# ============================================================ AXE F1
def axe_F1():
    titre("AXE F1 - pont constructif Sp(N) : le coefficient ne branche pas")
    pi = sp.pi
    c_spn = P_F1_OP / pi**2          # |C_T^Sp(N)|/N
    c_prog = P_F1_PROG / pi**4       # cible programme
    ratio = sp.simplify(c_spn / c_prog)

    check(sp.simplify(ratio - pi**2 / 8) == 0,
          "F1-1a rapport Sp(N)/programme = pi^2/8 EXACT (obtenu %s)" % ratio)
    check(sp.simplify(ratio - 1) != 0,
          "F1-1b pi^2/8 != 1 : le coefficient NE concorde PAS")
    check(sp.N(ratio) > 1,
          "F1-2 pi^2/8 > 1 (%.6f) : exces, non deficit" % float(sp.N(ratio)))

    consigne("F1-3 A_T.N = 16 NON testable par Sp(N) (obstacle O1) - "
             "statut lu au front-matter, NON redemontre")
    consigne("F1-4 concordance de STRUCTURE (signe C_T<0, propto N, mecanisme "
             "holographique <JJ> propto l^2/G_N) - IMPORT AHS 1108.5735, NON redemontre")


# ============================================================ AXE F2
def axe_F2():
    titre("AXE F2 - bispectre tensoriel vs Planck PR4 : le plancher Einstein")
    N = sp.symbols('N', positive=True)
    # A_T ~ N^(exp) ; (H/M_Pl)^2 propto A_T ; plancher propto (H/M_Pl)^4
    A_T = N**P_F2_EXP_AT
    H2 = A_T
    plancher = sp.simplify(H2**2)
    expo = sp.simplify(sp.log(plancher) / sp.log(N))
    check(sp.simplify(expo + 2) == 0,
          "F2-1 plancher Einstein propto N^(-2) : exposant EXACT -2 (obtenu %s)"
          % sp.simplify(expo))

    consigne("F2-2 issue D1c 'coherence / non exclu', D2c non declenche - "
             "verdict de confrontation forme<->borne, NON algebrisable")
    consigne("F2-3 TENSION INTERNE ENTRE TETES, pre-declaree au gel : la tete F2 "
             "porte f^ttt_NL = 900 +/- 700 comme lecture de 2312.12498 Table II ; "
             "la tete F5 v0.3 (correctif R-23) declare ce chiffre NON LITTERAL dans "
             "la source, caracterisation approximative d'un sigma = O(500). Les deux "
             "enonces COEXISTENT au depot. CONSIGNE, NON ARBITRE : les corps sont "
             "fermes, aucun element au front-matter ne permet de trancher")


# ============================================================ AXE F3
def axe_F3():
    titre("AXE F3 - substantiation d'A2star : G2 n'est pas le generique")
    x, y, z = sp.symbols('x y z', real=True)

    # G2 = deux Killing commutants d_y, d_z => composantes fonctions de (t,x) seules.
    # Metrique-temoin a dependance explicite en y :
    g_temoin = sp.diag(1, sp.exp(2 * x), sp.exp(2 * y))
    # derivee de Lie le long de d_y d'une metrique diagonale = d_y g_ij
    lie_y = g_temoin.applyfunc(lambda e: sp.diff(e, y))
    lie_z = g_temoin.applyfunc(lambda e: sp.diff(e, z))
    check(not lie_y.is_zero_matrix,
          "F3-2a metrique-temoin diag(1,e^2x,e^2y) : L_{d_y} g != 0 "
          "=> d_y n'est PAS de Killing")
    check(lie_z.is_zero_matrix,
          "F3-2b la meme metrique admet bien d_z de Killing (1 seul du couple)")
    # => elle n'appartient pas a la famille G2 adaptee (d_y, d_z)
    # controle de non-vacuite : une metrique G2 authentique doit passer les deux
    g_G2 = sp.diag(1, sp.exp(2 * x), sp.exp(4 * x))
    ok_G2 = (g_G2.applyfunc(lambda e: sp.diff(e, y)).is_zero_matrix and
             g_G2.applyfunc(lambda e: sp.diff(e, z)).is_zero_matrix)
    check(ok_G2,
          "F3-2c controle de non-vacuite : diag(1,e^2x,e^4x) EST dans la famille "
          "G2 adaptee => le test separe, il n'est pas trivialement vrai")

    consigne("F3-1 RECLASSEE en consignation par la clause I-c du gel. La cible "
             "gelee demandait de retrouver que 'transitoire' est CONDITIONNEL a "
             "|w|>1 (permanent pour 0<|w|<1, Lim §5.1 / correctif R-20). Ce fait "
             "vit au corps des sources et ne se derive pas ab initio : tout assert "
             "que j'ecrirais serait une RECOPIE du front-matter, donc VACANT. "
             "Retiree du compte PASS, motif nomme")
    consigne("F3-2 LIMITE de la cible atteinte : le temoin montre la non-appartenance "
             "a la famille G2 ADAPTEE au couple (d_y,d_z). Il n'exclut PAS l'existence "
             "d'un AUTRE couple de Killing commutants. L'inclusion stricte G2 (-) "
             "generique 3D est donc etablie MODULO le choix d'adaptation - suffisant "
             "pour la conclusion 'un soutien en G2 ne borne pas le generique', "
             "insuffisant comme theoreme de classification")
    consigne("F3-3 obstructions OA (Garfinkle hors regime convergent), OB (billard "
             "ultralocal excluant les spikes PAR CONSTRUCTION), OC (pont u_ere -> C_F "
             "non fait en generique) - lues au front-matter, NON rederivees")


# ============================================================ AXE F4
def axe_F4():
    titre("AXE F4 - A4 principiel : la voie entropie-de-Weyl est CIRCULAIRE")
    w = sp.symbols('w', nonnegative=True)

    # F4-1 (amende) : f strictement CROISSANTE sur [0, oo) => argmin en w=0
    familles = [
        ("f = w", w),
        ("f = w**2", w**2),
        ("f = log(1+w)", sp.log(1 + w)),
        ("f = 1 - exp(-w)", 1 - sp.exp(-w)),
        ("f = w/(1+w)", w / (1 + w)),
        ("f = sqrt(w)", sp.sqrt(w)),
    ]
    for nom, f in familles:
        fp = sp.simplify(sp.diff(f, w))
        # monotonie stricte sur (0, oo) : f' > 0, aucun point ou f' < 0
        neg = sp.solveset(fp < 0, w, domain=sp.Interval.open(0, sp.oo))
        croissante = (neg == sp.EmptySet)
        # argmin global : f(0) <= f(w) pour tout w >= 0
        f0 = sp.limit(f, w, 0, '+')
        argmin_en_0 = sp.simplify(sp.minimum(f, w, sp.Interval(0, sp.oo)) - f0) == 0
        check(croissante and argmin_en_0,
              "F4-1 [%s] strictement croissante ET argmin global en w=0" % nom)

    consigne("F4-2 RETIREE du compte PASS - assert VACANT denonce par l'audit de "
             "vacuite du harnais : la version v1 comparait deux ensembles codes en "
             "dur ({0} == {0}), elle ne pouvait pas echouer. La conclusion "
             "'l'equivalence min S_grav <=> A4 est une IDENTITE, donc la voie "
             "entropie-de-Weyl est CIRCULAIRE' est portee par F4-1 (argmin en w=0 "
             "pour toute f croissante) et F4-3 (elle CASSE si f n'est pas monotone) "
             "- elle n'a pas besoin d'un assert propre, et en avoir un de faux "
             "etait pire que n'en avoir aucun")

    # F4-3 FIREWALL : f NON monotone => l'argmin quitte w=0
    f_nm = (w - 1)**2
    mini = sp.minimum(f_nm, w, sp.Interval(0, sp.oo))
    f_nm_0 = f_nm.subs(w, 0)
    check(sp.simplify(mini - f_nm_0) != 0,
          "F4-3 FIREWALL f=(w-1)^2 NON monotone : argmin QUITTE w=0 "
          "(min=%s vs f(0)=%s) => la circularite est CONTINGENTE a la monotonie"
          % (mini, f_nm_0))

    consigne("F4-0 ECART DE GEL NOMME, imputable au pilote : la cible F4-1 telle "
             "que gelee (298e2094) disait 'strictement monotone DECROISSANTE', "
             "enonce faux (argmin d'une f decroissante part a l'infini). Corrige "
             "par AMENDEMENT-1 (9d30fce6) date AVANT la premiere ligne "
             "d'instrument, gel byte-intact. Aucune tolerance desserree")
    consigne("F4-4 G1-b (stabilite #5 = seul appui non circulaire, mais SELECTION "
             "et non derivation ; P=m.lambda conserve => pas d'attracteur) et G2-c "
             "(deplacement Past Hypothesis) - verdicts de substance, corps ferme, "
             "NON rederives")


# ============================================================ AXE F5
def axe_F5():
    titre("AXE F5 - scaling A_T ~ 1/C_T ~ 1/N : identite pour tout d")
    d, l, lP = sp.symbols('d ell ell_P', positive=True)
    c1, c2, c3 = sp.symbols('c1 c2 c3', positive=True)   # coefficients O(1) LIBRES

    N = c3 * (l / lP)**(d - 1)      # loi d'aire, d symbolique
    C_T = c1 * N                    # route holographique
    A_T = c2 / C_T                  # raideur du stress
    produit = sp.simplify(A_T * N)

    check(sp.simplify(sp.diff(produit, l)) == 0,
          "F5-1a A_T.N est independant de ell (d/dell = 0)")
    check(sp.simplify(sp.diff(produit, d)) == 0,
          "F5-1b A_T.N est independant de d (d/dd = 0) => IDENTITE pour tout d, "
          "pas un accident de d=3")

    # F5-2 GARDE-FOU : le coefficient O(1) reste LIBRE
    libres = produit.free_symbols
    check(produit.has(c1) and produit.has(c2) and not produit.has(N),
          "F5-2a le produit vaut c2/c1 : le coefficient O(1) reste un SYMBOLE "
          "LIBRE (symboles residuels : %s)" % sorted([str(s) for s in libres]))
    # tenter de le resoudre ne doit RIEN donner
    k = sp.symbols('k', positive=True)
    sol = sp.solve(sp.Eq(produit, k), [c1, c2], dict=True)
    resolu = bool(sol) and all(
        not (s.get(c1, c1).free_symbols | s.get(c2, c2).free_symbols) for s in sol)
    check(not resolu,
          "F5-2b aucune combinaison des deux routes ne RESOUT le coefficient "
          "(le resoudre serait un faux PASS)")

    consigne("F5-3 cartographie (a) : O1/O3/OB non independantes, racine unique "
             "O2 'a inventer' - NON algebrisable, lue au front-matter")
    consigne("F5-4 R-25 : les 'deux routes' sont independantes EN CONTENU, NON au "
             "niveau de l'exposant (socle loi d'aire ell^(d-1) PARTAGE). Le PASS "
             "F5-1 ne vaut donc pas 'deux confirmations independantes de N^-1'")


# ============================================================ geometrie 3D
def christoffels(g, X):
    n = len(X)
    ginv = g.inv()
    Ga = [[[0] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = 0
                for e in range(n):
                    s += ginv[a, e] * (sp.diff(g[e, b], X[c]) +
                                       sp.diff(g[e, c], X[b]) -
                                       sp.diff(g[b, c], X[e]))
                Ga[a][b][c] = sp.simplify(s / 2)
    return Ga


def hessienne_cov(C, g, X, Ga):
    n = len(X)
    H = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            e = sp.diff(C, X[i], X[j])
            for k in range(n):
                e -= Ga[k][i][j] * sp.diff(C, X[k])
            H[i, j] = sp.simplify(e)
    return H


def ricci(g, X, Ga):
    n = len(X)
    R = sp.zeros(n, n)
    for b in range(n):
        for c in range(n):
            e = 0
            for a in range(n):
                e += sp.diff(Ga[a][b][c], X[a]) - sp.diff(Ga[a][b][a], X[c])
                for dd in range(n):
                    e += Ga[a][a][dd] * Ga[dd][b][c] - Ga[a][c][dd] * Ga[dd][b][a]
            R[b, c] = sp.simplify(e)
    return R


# ============================================================ AXE F6
def axe_F6():
    titre("AXE F6 - BMS / memoire : Hessien electrique, secteur disjoint du magnetique")
    x, y, z = sp.symbols('x y z', real=True)
    X = [x, y, z]
    # fond NON plat (metrique de Nil / Heisenberg) : le test n'est pas trivialise
    g = sp.Matrix([[1, 0, 0],
                   [0, 1 + x**2, -x],
                   [0, -x, 1]])
    ginv = g.inv()
    Ga = christoffels(g, X)

    C = sp.Function('C')(x, y, z)
    H = hessienne_cov(C, g, X, Ga)
    box = sp.simplify(sum(ginv[i, j] * H[i, j] for i in range(3) for j in range(3)))

    dsig = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            terme = H[i, j] - P_F6_TRACE * sp.Rational(1, P_F6_DIM) * g[i, j] * box
            dsig[i, j] = sp.simplify(-2 * terme)

    check(sp.simplify(dsig - dsig.T).is_zero_matrix,
          "F6-1a Delta_sigma_ij est SYMETRIQUE (sur fond Nil, C generique)")
    trace = sp.simplify(sum(ginv[i, j] * dsig[i, j] for i in range(3) for j in range(3)))
    check(sp.simplify(trace) == 0,
          "F6-1b Delta_sigma_ij est SANS TRACE (g^ij Delta_sigma_ij = 0)")

    # F6-2 parite : Hessien = tenseur vrai (pair) ; Cotton = pseudo-tenseur (impair)
    R_ij = ricci(g, X, Ga)
    Rs = sp.simplify(sum(ginv[i, j] * R_ij[i, j] for i in range(3) for j in range(3)))
    check(sp.simplify(Rs + sp.Rational(1, 2)) == 0,
          "F6-2a controle de fond : R[Nil] = -1/2 CONSTANT (obtenu %s)" % Rs)
    S = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            S[i, j] = sp.simplify(R_ij[i, j] - sp.Rational(1, 4) * Rs * g[i, j])

    def nabla_S(k, i, j):
        e = sp.diff(S[i, j], X[k])
        for m in range(3):
            e -= Ga[m][k][i] * S[m, j] + Ga[m][k][j] * S[i, m]
        return sp.simplify(e)

    cot = {}
    nonnul = False
    for k in range(3):
        for i in range(3):
            for j in range(3):
                v = sp.simplify(nabla_S(k, S and i, j) - nabla_S(j, i, k)) \
                    if False else sp.simplify(nabla_S(k, i, j) - nabla_S(j, i, k))
                cot[(k, i, j)] = v
                if v != 0:
                    nonnul = True
    check(nonnul,
          "F6-2b FIREWALL de fond : Cotton[Nil] != 0 a R constant "
          "(recoupe R-7/Q6 et R-9/A5-A6, rederive ici)")

    # parite : P = -Id en 3D, det(P) = -1
    P = -sp.eye(3)
    detP = P.det()
    dsig_num = dsig.subs(C, x**2 * y + y * z**2 + sp.Rational(1, 3) * z * x**2)
    dsig_num = sp.simplify(dsig_num.doit())
    dsig_p = sp.simplify(P.T * dsig_num * P)                    # tenseur vrai
    check(sp.simplify(dsig_p - dsig_num).is_zero_matrix,
          "F6-2c Delta_sigma est de PARITE PAIRE (tenseur vrai : P^T.D.P = D)")
    # F6-2d : construction EFFECTIVE d'un objet a un epsilon (Cotton-York)
    eps = sp.LeviCivita
    Y = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            Y[i, j] = sp.simplify(sum(eps(i, k, l) * cot[(k, l, j)]
                                      for k in range(3) for l in range(3)))
    check(not Y.is_zero_matrix,
          "F6-2d1 l'objet a UN epsilon Y_ij = eps_i^kl Cotton_klj est NON NUL "
          "sur Nil (il y a bien quelque chose a classer en parite)")
    Y_pseudo = sp.simplify((detP**P_F6_PSEUDO) * (P.T * Y * P))
    check(sp.simplify(Y_pseudo + Y).is_zero_matrix and not Y.is_zero_matrix,
          "F6-2d2 Y transforme en PSEUDO-tenseur donne -Y != +Y => parite IMPAIRE, "
          "DISJOINTE de la parite paire de Delta_sigma : aucun datum libre neuf")

    # F6-3 FIREWALL trace
    if P_F6_TRACE == 1 and P_F6_DIM == 3:
        dsig_sans = sp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                dsig_sans[i, j] = sp.simplify(-2 * H[i, j])
        tr_sans = sp.simplify(sum(ginv[i, j] * dsig_sans[i, j]
                                  for i in range(3) for j in range(3)))
        check(sp.simplify(tr_sans) != 0,
              "F6-3 FIREWALL sans soustraction de trace : g^ij Delta_sigma_ij != 0 "
              "=> la propriete 'sans trace' CASSE, comme elle doit")

        # F6-4 FIREWALL dimension : 1/d avec d=4 sur un espace de dimension 3
        dsig_d4 = sp.zeros(3, 3)
        for i in range(3):
            for j in range(3):
                dsig_d4[i, j] = sp.simplify(
                    -2 * (H[i, j] - sp.Rational(1, 4) * g[i, j] * box))
        tr_d4 = sp.simplify(sum(ginv[i, j] * dsig_d4[i, j]
                                for i in range(3) for j in range(3)))
        check(sp.simplify(tr_d4) != 0,
              "F6-4 FIREWALL d=4 sur un espace de dimension 3 : la trace CASSE "
              "=> le coefficient 1/d est bien 1/dim, pas un parametre libre")
    else:
        consigne("F6-3/F6-4 firewalls non evalues : porteurs mutes par le harnais")

    consigne("F6-5 RETIREE du compte PASS - asserts VACANTS denonces par l'audit "
             "de vacuite : verifier que u -> (d/16.pi.G).u est lineaire en u est "
             "une TAUTOLOGIE (on teste la linearite d'une expression qu'on a "
             "ecrite lineaire). La substance de G2 n'est pas la linearite, c'est "
             "le DICTIONNAIRE <T> = (d/16.pi.G) g3 lui-meme - lequel est un IMPORT "
             "holographique NON rederivable ici. Consigne comme import, pas "
             "revendique comme PASS")

    consigne("F6-6 G3 (flux-balance Lambda-BMS) : DELIMITATION - scri spacelike = "
             "tranche unique eta->0^-, pas de feuilletage retarde ni de coupes "
             "vide-passe/vide-futur => pas de saut DYNAMIQUE propre ; le gap G3-b "
             "EST le noeud O2. NON algebrisable")
    consigne("F6-7 BORD-EON : V-A (concordance par desambiguisation d'un HOMONYME "
             "'memoire') et NOTE-07 : V-B (decalage/premature). Verdicts d'instances "
             "CSE souveraines incognito - CONSIGNES, JAMAIS re-juges ici")


# ============================================================ AXE WCH-1
def axe_WCH1():
    titre("AXE WCH-1 - LC-D3-WCH-CANCELLATION")
    consigne("W1-1 la WCH un-point est une CANCELLATION (symetrie) et non une perte "
             "d'amplitude ; trois mecanismes distincts ; analogie BAO<->horizon = "
             "resonance structurelle NON derivee ; empreinte inter-eon (cercles GP) "
             "reelle mais contestee. Axe INTEGRALEMENT consigne : le contenu "
             "discriminant vit au corps, ferme. ZERO PASS revendique sur cet axe")


# ============================================================ AXE WCH-2
def axe_WCH2():
    titre("AXE WCH-2 - LC-D3-WCH-GWE : le mode exact et l'artefact de troncature")
    x = sp.symbols('x', positive=True)

    u = P_W2_NUM * x * sp.cos(x) - sp.sin(x)
    omega = sp.simplify(u**2 / (3 * x**2))          # Omega_sigma / eps^2

    ser = sp.series(omega, x, 0, 9).removeO().expand()
    c4 = sp.simplify(ser.coeff(x, 4))
    c6 = sp.simplify(ser.coeff(x, 6))

    check(sp.simplify(c4 - sp.Rational(1, 27)) == 0,
          "W2-1 terme dominant du mode EXACT = x^4/27 : la forme scellee "
          "Omega_sigma = (k.eta)^4 eps^2/27 est RETROUVEE (coeff obtenu %s)" % c4)
    check(c6 != 0 and sp.N(c6) < 0,
          "W2-2 terme suivant NON NUL et NEGATIF (%s) => le tronque SURESTIME" % c6)

    f = sp.lambdify(x, omega, 'math')
    import math
    sup, xsup = 0.0, 0.0
    n = 400000
    for i in range(1, n + 1):
        xv = i * 40.0 / n
        v = f(xv)
        if v > sup:
            sup, xsup = v, xv
    check(sup <= 0.377,
          "W2-3a sup du mode exact sur (0,40] = %.6f <= 0.377 (atteint en x=%.4f)"
          % (sup, xsup))
    check(sup < 0.5,
          "W2-3b sup < 0.5 => regime (A) pour TOUT k.eta, pas de basculement")
    # borne asymptotique : au-dela, omega -> cos^2(x)/3 <= 1/3 < 0.377
    check(sp.limit(sp.simplify(omega - sp.cos(x)**2 / 3), x, sp.oo) == 0,
          "W2-3c comportement asymptotique = cos^2(x)/3 <= 1/3 < 0.377 => la borne "
          "n'est pas un artefact de la fenetre de balayage")

    x_bascule = sp.Rational(27, 2)**sp.Rational(1, 4)
    check(sp.simplify((x_bascule**4 / 27) - sp.Rational(1, 2)) == 0,
          "W2-4a le TRONQUE x^4/27 atteint 0.5 en x = (13.5)^(1/4) EXACTEMENT")
    check(abs(float(sp.N(x_bascule)) - 1.9168) < 1e-3,
          "W2-4b (13.5)^(1/4) = %.4f : le 'basculement (A)/(B) a k.eta ~ 1.9' est "
          "l'ARTEFACT EXACT de la troncature, non un fait du mode exact"
          % float(sp.N(x_bascule)))

    v_cgb = float(sp.N(omega.subs(x, sp.Float('2e-7'))))
    check(2e-29 < v_cgb < 2e-28,
          "W2-5 au pic CGB (x = 2e-7) : Omega_sigma/eps^2 = %.3e, ordre 6e-29 "
          "RETROUVE depuis la forme (non reporte)" % v_cgb)

    consigne("W2-6 reserve §6.2 : absence de retro-action inhomogene - VERROU "
             "PRIMAIRE, hors de portee. Le verdict (A) reste CONDITIONNEL au cadre "
             "CCC et a cette reserve")
    consigne("W2-7 W2 'residu-cassant' : IMPORT de R-7, recoupement seul, NON "
             "rederive ici")


# ============================================================ AXE transverse
def axe_T():
    titre("AXE TRANSVERSE - 'branche epuisee' : le compte reste inchange")
    compte = frozenset({'A4', 'A2star', 'N'})
    # chaque front est classe par son NIVEAU d'issue, pas par recopie du verdict
    niveaux = {
        'F1': 'consolidation',
        'F2': 'coherence',
        'F3': 'delimitation',
        'F4': 'delimitation',
        'F5': 'cartographie',
        'F6': 'consolidation',
    }
    REDUCTEURS = {'reduction'}
    retirees = set()
    for front, niv in niveaux.items():
        if niv in REDUCTEURS:
            retirees |= set(P_T1_REDUC)
    reste = compte - retirees - set(P_T1_REDUC)
    check(reste == compte,
          "T-1 aucun des six fronts n'est de niveau 'reduction' => l'union des "
          "inconnues retirees est VIDE => {A4 ; A2star ; N} INCHANGE "
          "(obtenu %s)" % sorted(reste))

    consigne("T-2 'branche ENTIEREMENT EPUISEE' = constat de NON-EXISTENCE d'un "
             "front borne et sceau-able restant. On ne prouve pas une absence par "
             "sympy. Declare INVERIFIABLE PAR INSTRUMENT au gel, jamais compte")


def main():
    print("REDEMO R-11 - falsifiabilite F1-F6 + memoire BMS + W2/WCH-GWE")
    print("gel 298e2094 + amendement 9d30fce6 | plafond annonce AU GEL : E-2")
    for f in (axe_F1, axe_F2, axe_F3, axe_F4, axe_F5, axe_F6,
              axe_WCH1, axe_WCH2, axe_T):
        f()
    print("\n" + "=" * 70)
    print("REDEMO R-11 : %d/%d PASS discriminants + %d consignations declarees - "
          "EXIT %d" % (PASS, PASS + FAILED, CONS, 1 if FAILED else 0))
    print("=" * 70)
    return 1 if FAILED else 0


if __name__ == '__main__':
    sys.exit(main())
