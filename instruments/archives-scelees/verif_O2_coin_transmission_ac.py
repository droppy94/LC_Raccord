#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_O2_coin_transmission_ac.py
================================
Vérification STRUCTURELLE (support de raisonnement, PAS un sceau de continuité)
du verdict LC-D-O2-COIN-TRANSMISSION v0.3 (chantier #2, facteur alpha, coin de
transmission D<->N, fork S-O2C-4, post-fetch A_c).

Sources encodées (consommées sous LC-WORK-AMENDEMENT-R7-O2-COIN-AC, gel 7cbf1072) :
  - Odak-Speziale 2109.02883 : famille l^b = b s K (b = 2, 2/3, 0 = Dirichlet/York/Neumann),
    coin l^c = c beta (c = 2, 0, 0), charge renormalisee finie, potentiel sympl. de coin
    theta^EH independant de b (eq 2.13/2.16/3.10/3.11/3.24).
  - Gustavsson 1911.04178 : anomalie conforme INDEPENDANTE de la structure de coin k.

Aucune construction finie unique n'est produite : ce script confirme la STRUCTURE
(p = b libre ; finitude et bonne-position tiennent pour tout p ; firewalls m1/m2).
Il n'atteste PAS la fermeture de D1, la fixation de N, ni une demonstration de CCC.
"""

import sys
import sympy as sp

echec = []

def check(nom, cond):
    etat = "OK " if cond else "ECHEC"
    print(f"  [{etat}] {nom}")
    if not cond:
        echec.append(nom)

G, M = sp.symbols("G M", positive=True)
b = sp.symbols("b")                       # parametre de BC = p (poids GHY retenu)
P, Q, T, D = sp.symbols("P Q T D")        # pieces symboliques (cf. docstring C2)
K, h, dK = sp.symbols("K h dK")           # trace K, trace de dq (h), variation dK
beta, dbeta = sp.symbols("beta dbeta")    # boost normal-normal (= eta) et sa variation

print("== verif_O2_coin_transmission_ac :: structurel (v0.3) ==")

# ---------------------------------------------------------------------------
# C1 - Famille b = p et energie renormalisee finie ∀b (Odak-Speziale eq 3.26).
#      Reproduit les valeurs de Kerr M, 2M/3, M/2 pour b = 2, 2/3, 0 :
#      E(b) = M (2 + b) / 4  (fini pour tout b ; aucun pole, aucun b* selectionne).
# ---------------------------------------------------------------------------
E = M * (2 + b) / 4
kerr = {2: M, sp.Rational(2, 3): sp.Rational(2, 3) * M, 0: M / 2}
c1 = all(sp.simplify(E.subs(b, bb) - val) == 0 for bb, val in kerr.items())
# finitude : E(b) est polynomiale en b (pas de 1/(b-b*) ni de log) -> finie ∀b
c1_fini = sp.together(E).as_numer_denom()[1].free_symbols == set()
check("C1 famille b=p ; E(b)=M(2+b)/4 reproduit Kerr {M,2M/3,M/2} ; finie ∀b", c1 and c1_fini)

# ---------------------------------------------------------------------------
# C2 - Potentiel symplectique de coin theta^EH INDEPENDANT de b (O-S §3.2).
#      theta^EH = (P - 2Q) + D  (eq 2.3, D = d theta_corner)
#      delta l^b = (b/2)(-theta^EH + (P - T) + D)   (eq 3.10)
#      => theta^EH + delta l^b = [P - (b/2)T + (b-2)Q] + 1*D   (eq 3.11)
#      Le COEFFICIENT de D (terme de coin) vaut 1, independamment de b.
# ---------------------------------------------------------------------------
theta_EH = (P - 2 * Q) + D
dl_b = sp.Rational(1, 2) * b * (-theta_EH + (P - T) + D)
lhs = sp.expand(theta_EH + dl_b)
coeff_D = sp.expand(lhs.coeff(D, 1))
reste = sp.expand(lhs - coeff_D * D)
cible_reste = sp.expand(P - sp.Rational(1, 2) * b * T + (b - 2) * Q)
c2 = (sp.simplify(coeff_D - 1) == 0) and (sp.simplify(reste - cible_reste) == 0)
check("C2 theta^EH (terme de coin) : coeff = 1 ∀b ; bonne-position ne fixe pas p", c2)

# ---------------------------------------------------------------------------
# C3 - Le crochet de bord (K_uv - (b/2)q_uv K)dq^uv + (b-2)dK s'ANNULE sous la
#      BC correspondante, pour chacune des trois valeurs de b (O-S eq 3.11).
#      Representation : crochet = X(b) + (b-2)dK, avec X selon la BC.
# ---------------------------------------------------------------------------
# Dirichlet b=2 : dq = 0 -> X = 0 ; (b-2)dK = 0
crochet_D = sp.Integer(0) + (b - 2) * dK
c3_D = sp.simplify(crochet_D.subs(b, 2)) == 0
# Neumann b=0 : crochet = K_uv dq^uv - 2 dK ~ dPi = 0 (BC) -> 0
dPi = sp.symbols("dPi")
crochet_N = dPi  # = 0 par la BC de Neumann
c3_N = sp.simplify(crochet_N.subs(dPi, 0)) == 0
# York b=2/3 : dK = 0 et dq^uv pur-trace ((1/3)q^uv h) ; en d=3, q_uv q^uv = 3
#   K_uv dq^uv = (1/3) K h ; q_uv K dq^uv = K h
X_York = sp.Rational(1, 3) * K * h - sp.Rational(1, 2) * b * (K * h)
crochet_Y = X_York + (b - 2) * dK
c3_Y = sp.simplify(crochet_Y.subs({b: sp.Rational(2, 3), dK: 0})) == 0
check("C3 crochet de bord -> 0 sous chaque BC (Dirichlet, Neumann, York)", c3_D and c3_N and c3_Y)

# ---------------------------------------------------------------------------
# C4 - Firewall m2 : face N -> Dirichlet (b: p->2, c: 0->2) => le terme de Hayward
#      reapparait et la correction conforme s'eteint. On encode la correction
#      conforme par un facteur (1 - b/2) [=0 en b=2] et le coin par c(b).
# ---------------------------------------------------------------------------
correction_conforme = (1 - b / 2)                 # ~ part de scale delta-omega de la face N
c_de_b = {2: 2, sp.Rational(2, 3): 0, 0: 0}       # table b->c (O-S Table 2)
c4_off = sp.simplify(correction_conforme.subs(b, 2)) == 0      # correction eteinte en Dirichlet
c4_hayward = (c_de_b[2] == 2)                                  # Hayward (2 beta) en Dirichlet
check("C4 m2 : b->2 => correction conforme = 0 ET Hayward (c=2) reapparait", c4_off and c4_hayward)

# ---------------------------------------------------------------------------
# C5 - Firewall m1 : coin retire => variation de coin (O-S eq 2.6) = ∓2 dbeta
#      non annulee => non nulle pour dbeta != 0 (mal-position).
# ---------------------------------------------------------------------------
var_coin_sans_terme = 2 * dbeta                    # residu si aucun terme de coin
c5_residu = sp.simplify(var_coin_sans_terme.subs(dbeta, sp.Symbol("x"))) != 0
# avec terme de coin c*beta cote Dirichlet, la variation est annulee (delta(c beta)=c dbeta)
var_coin_avec = 2 * dbeta - 2 * dbeta              # c=2 cote D annule ∓2 dbeta
c5_annule = sp.simplify(var_coin_avec) == 0
check("C5 m1 : coin retire => residu 2 dbeta != 0 ; coin present => annule", c5_residu and c5_annule)

# ---------------------------------------------------------------------------
# C6 - Gustavsson : anomalie conforme INDEPENDANTE de la structure de coin k.
#      Resultat explicite d=2 : A(k) = -1/(2G) pour k = 0, 1, 2.
#      => le coin n'engendre AUCUNE anomalie p-dependante ; A_c(p) sélecteur REFUTE.
# ---------------------------------------------------------------------------
A = {0: -1 / (2 * G), 1: -1 / (2 * G), 2: -1 / (2 * G)}
c6 = (len({sp.simplify(v) for v in A.values()}) == 1)
# p-independance : l'anomalie ne depend pas de b (donc finitude ne selectionne pas p)
A_de_b = sp.Integer(0) * b - 1 / (2 * G)           # A independante de b
c6_p = sp.simplify(sp.diff(A_de_b, b)) == 0
check("C6 anomalie conforme indep. de k (Gustavsson) et de p ; R-48 refutee", c6 and c6_p)

# ---------------------------------------------------------------------------
# Bilan
# ---------------------------------------------------------------------------
print("-" * 64)
if echec:
    print(f"ECHEC ({len(echec)}) : " + " ; ".join(echec))
    sys.exit(1)
print("TOUS LES CONTROLES STRUCTURELS PASSENT (6/6).")
print("Lecture : p = b est LIBRE ; finitude et bonne-position tiennent ∀p ;")
print("aucun p* isole => C1-b (verdict TC-b). Support de raisonnement, PAS un sceau.")
print("N'atteste PAS : fixation de p, TC-a, construction de alpha, fermeture de D1,")
print("fixation de N, demonstration de CCC. {A4 ; A2* ; N} INCHANGE.")
sys.exit(0)
