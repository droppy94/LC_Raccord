#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_O2_bprime_AUDIT.py — COPIE D'AUDIT (positif seul, SANS firewall).

But : permettre une VÉRIFICATION INDÉPENDANTE de la chaîne de dérivation
seule. Les mutations cassantes du pilote NE SONT PAS incluses (discipline :
les mutations-pilote ne sont pas jointes au paquet d'audit). L'auditeur est
invité à concevoir SES PROPRES tests de réfutation après replay.

Claim à vérifier (algèbre symbolique) :
  Données (à tenir pour acquises, sourcées) :
    * Équation indicielle d'un mode TT près d'un bord conforme de dimension d :
        z² H'' + (1−d) z H' = 0   ⟹   exposants {0, d}.
      ⟹ Δ_- = 0 (mode "source"), Δ_+ = d (mode "VEV"/sous-dominant).
    * Une matrice de référence S = [[0,−1],[1,0]] (S² = −I, valeurs propres ±i).
    * Une "réciprocité négative" agissant sur le facteur conforme : Ω ↦ −1/Ω.
    * Un résultat amont : l'opération échange les deux modes, induisant
        P = [[0, s],[1, 0]],  P² = s·I,  et  P = S ⟺ s = −1.
  Affirmation à auditer :
    (1) le poids pertinent est le GAP w = Δ_+ − Δ_- = d ;
    (2) sous Ω ↦ −1/Ω, une branche Ω^Δ prend le facteur (−1)^Δ ;
    (3) s étant le signe RELATIF entre branches, tout poids GLOBAL se simplifie,
        d'où s = (−1)^{Δ_+−Δ_-} = (−1)^d ;
    (4) en d=3 : s = −1 ⟹ P = S, P² = −I.
"""

import sympy as sp

n = 0
def check(c, m):
    global n
    assert c, "ÉCHEC : " + m
    n += 1

dd, r = sp.symbols('dd r')
zz = sp.symbols('zz', positive=True)

# (A) exposants FG
Hz = zz**r
indic = sp.simplify((zz**2*sp.diff(Hz, zz, 2) + (1 - dd)*zz*sp.diff(Hz, zz)) / Hz)
racines = sp.solve(sp.Eq(indic, 0), r)
check(set(racines) == {0, dd}, "exposants FG = {0, d}")
Dm, Dp = 0, dd

# (B) facteur de signe par branche sous Ω ↦ −1/Ω
def branch_sign(D, recip=-1):
    return sp.Integer(recip)**D
sig_m = branch_sign(Dm, -1)
sig_p = branch_sign(Dp, -1)

# (C) signe relatif = s ; (3) poids global se simplifie
s_rel = sp.simplify(sig_p / sig_m)
check(sp.simplify(s_rel - (-1)**(Dp - Dm)) == 0, "s = (−1)^{Δ+−Δ-}")
check(sp.simplify(s_rel - (-1)**dd) == 0, "s = (−1)^d")
cpos = sp.symbols('cpos', positive=True)
check(sp.simplify((cpos*sig_p)/(cpos*sig_m) - s_rel) == 0, "poids global simplifié")

# (D) matrices
s = sp.symbols('s')
P = sp.Matrix([[0, s], [1, 0]])
S = sp.Matrix([[0, -1], [1, 0]])
check(sp.simplify(P*P - s*sp.eye(2)) == sp.zeros(2), "P² = s·I")
check(sp.simplify(S*S + sp.eye(2)) == sp.zeros(2), "S² = −I")
check(sp.simplify((P - S).subs(s, -1)) == sp.zeros(2), "P = S ⟺ s = −1")

# (E) branchement parité + d=3
for dv in [2, 3, 4, 5]:
    sval = int((-1)**dv)
    eq = (sp.simplify(P.subs(s, sval) - S) == sp.zeros(2))
    check(eq == (dv % 2 == 1), f"d={dv} : P=S ⟺ d impair")
check(int((-1)**3) == -1, "d=3 ⟹ s=−1")

print(f"OK (copie d'audit, positif seul) — {n} assertions. s=(−1)^d ; d=3 ⟹ s=−1 ⟹ P=S.")
print("AUDITEUR : replayez, vérifiez chaque pas indépendamment, PUIS concevez vos propres")
print("mutations cassantes (le firewall du pilote n'est pas fourni).")
