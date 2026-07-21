# verif_O2_P1b_soperation.py — LC-RACCORD
# Sceau algébrique du chaînon LC-D-O2-P1B-SOPERATION.
# Vérifie, en algèbre exacte (SymPy), trois faits utilisés au verdict :
#   (V1) La carte S de Leigh-Petkou (éq. 2.4 spin-1 ; éq. 2.18 spin-2),
#        S : (C, W) -> ( C/(C^2+W^2), -W/(C^2+W^2) ),
#        satisfait S∘S = IDENTITÉ sur les coefficients du deux-points.
#        => le -1 central de SL(2,Z) est INVISIBLE au niveau deux-points
#        (l'action effective est PSL(2,Z)) : aucun S^2=-1 gravitonique
#        n'est extractible de ce niveau.
#   (V2) La carte S préserve le signe de C (C>0 => S(C)>0) — cohérence
#        avec le garde-fou scellé C~_T = +C_T (LC-D-CT-DUAL §3, m4).
#   (V3) Sur tau = W + i C, la carte S coïncide avec tau -> -1/tau
#        (générateur S de SL(2,Z) au niveau projectif), et T : W -> W+1
#        avec tau -> tau+1. S^2 agit sur tau comme l'identité alors que
#        la matrice S de SL(2,Z) satisfait S_mat^2 = -Id : l'écart est
#        exactement le noyau {±Id} de SL(2,Z) -> PSL(2,Z).
# AUCUNE conclusion physique : établi (algèbre) uniquement.

import sympy as sp

C, W = sp.symbols('C W', real=True, positive=False)

def S_map(c, w):
    d = c**2 + w**2
    return sp.simplify(c/d), sp.simplify(-w/d)

# ---------- V1 : involution au niveau deux-points ----------
C1, W1 = S_map(C, W)
C2, W2 = S_map(C1, W1)
assert sp.simplify(C2 - C) == 0, "V1 FAIL: S^2(C) != C"
assert sp.simplify(W2 - W) == 0, "V1 FAIL: S^2(W) != W"
print("V1 PASS  S∘S = Id sur (C,W)  [spin-1 éq.2.4 et spin-2 éq.2.18 : même carte]")

# ---------- V2 : préservation du signe de C ----------
Cpos = sp.symbols('Cpos', positive=True)
Wany = sp.symbols('Wany', real=True)
SC, _ = S_map(Cpos, Wany)
assert sp.ask(sp.Q.positive(SC), sp.Q.positive(Cpos) & sp.Q.real(Wany)) is True, \
    "V2 FAIL: signe de C non préservé"
print("V2 PASS  C>0 ⟹ S(C)>0  [garde-fou m4 : C~_T=+C_T, zéro friction]")

# ---------- V3 : équivalence tau -> -1/tau et écart PSL/SL ----------
tau = W + sp.I*C
Stau = -1/tau
# parties réelle/imaginaire de -1/tau : Re = -W/(C^2+W^2), Im = C/(C^2+W^2)
ReS = sp.simplify(sp.re(Stau, evaluate=True))
ImS = sp.simplify(sp.im(Stau, evaluate=True))
assert sp.simplify(ReS - W1) == 0, "V3 FAIL: Re(-1/tau) != S(W)"
assert sp.simplify(ImS - C1) == 0, "V3 FAIL: Im(-1/tau) != S(C)"
# matrice S de SL(2,Z) : action de Möbius (a tau + b)/(c tau + d)
Smat = sp.Matrix([[0, -1], [1, 0]])
assert (Smat**2) == -sp.eye(2), "V3 FAIL: S_mat^2 != -Id"
# Möbius de S_mat^2 = -Id : tau -> (-tau+0)/(0-1) = tau  (identité projective)
a, b, c, d = (Smat**2)[0, 0], (Smat**2)[0, 1], (Smat**2)[1, 0], (Smat**2)[1, 1]
assert sp.simplify((a*tau + b)/(c*tau + d) - tau) == 0, "V3 FAIL: Möbius(-Id) != Id"
print("V3 PASS  S:(C,W) ≡ tau→-1/tau ; S_mat²=-Id ⟹ Möbius(=deux-points) = Id")
print("         [le -1 central vit dans ker(SL(2,Z)→PSL(2,Z)) : indétectable au 2-pt]")

print("\nSCEAU: 3/3 PASS — établi (algèbre). Aucune conclusion physique.")
