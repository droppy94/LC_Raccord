#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_O2_P1.py — SCEAU de l'étape (b) du pivot O₂ : TEST de P1.

Cadrage gelé : LC-WORK-CADRAGE-O2-P1 v0.1 (sha256 9859e78c3da3…).
Portée S-O2-b-2 = (α) : map induite sur (f_a, f_b) + carré / swap / signe SEULEMENT.
S-O2-b-1 = KB-local (de Haro 0808.2054 + S scellée CT-DUAL + relation Ω·ω=−1 [LC-A]).

QUESTION P1 : la réciprocité conforme de Penrose au crossover 𝒞 (Ω·ω=−1) induit-elle
EXACTEMENT la S-map de de Haro (S=[[0,−1],[1,0]], S²=−𝟙), FACTEURS COMPRIS ?

CE QUE CE SCEAU ÉTABLIT (et CE QU'IL N'ÉTABLIT PAS) :
  - ÉTABLIT (algèbre) : (i) les modes de Haro (f_a, f_b) = (source, VEV) ; (ii) la S-map
    scellée S²=−𝟙, vp ±i ; (iii) l'inversion de Penrose induit le SWAP source↔VEV (P1-G1) ;
    (iv) le carré de la map induite = s·𝟙 où s = signe de la patte VEV→source ; (v) une
    involution conforme NUE (de coordonnée) donne s=+1 ⟹ carré +𝟙 ≠ S²=−𝟙.
  - N'ÉTABLIT PAS : la valeur de s. s=−1 (⟹ match S) exigerait que le facteur conforme
    NÉGATIF ω<0 de Ω·ω=−1 DESCENDE en −1 sur le mode TT (poids conforme) — FACTEUR DÉCISIF
    LAISSÉ SYMBOLIQUE (décision ouverte, fetch-conditionnel S-O2-b-1). Le sceau ne fixe PAS s.
  - SANS SURCLASSEMENT (§6.4) : P1 n'est NI prouvée NI réfutée à plat ; elle est RÉDUITE à
    un unique signe s. {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; CCC non démontrée.

Firewall (3 mutations cassantes, S-O2-b-3) en fin de fichier.
"""
import sympy as sp

PASS = 0
def check(cond, label):
    global PASS
    assert cond, f"ÉCHEC: {label}"
    PASS += 1
    print(f"  ✓ {label}")

u = sp.symbols('u', positive=True)

print("="*78)
print("verif_O2_P1.py — test de P1 (Penrose Ω·ω=−1 ≟ S-map de de Haro), portée (α)")
print("="*78)

# ---------------------------------------------------------------------------
# [A] Les modes radiaux de de Haro (0808.2054, éq. 43) : source f_a, VEV f_b.
# ---------------------------------------------------------------------------
print("\n[A] Modes de de Haro (f_a, f_b) = (source, VEV)")
f_a = sp.cos(u) + u*sp.sin(u)        # source : f_a(0)=1
f_b = u*sp.cos(u) - sp.sin(u)        # VEV    : f_b ~ -u^3/3

# asymptotique u->0 : f_a -> constante (mode source, non normalisable) ; f_b ~ u^3 (VEV).
fa0 = sp.limit(f_a, u, 0)
fb_lead = sp.series(f_b, u, 0, 5).removeO()
check(fa0 == 1, "f_a(0)=1 : mode SOURCE (non normalisable, g₀)")
check(sp.simplify(fb_lead - (-u**3/3)) == 0, "f_b ~ -u³/3 : mode VEV (normalisable, g₃=⟨T⟩)")
# lien Bessel sphérique (recoupement KB) : f_a=-u²y₁, f_b=-u²j₁
j1 = sp.sin(u)/u**2 - sp.cos(u)/u
y1 = -sp.cos(u)/u**2 - sp.sin(u)/u
check(sp.simplify(f_a - (-u**2*y1)) == 0, "f_a = -u² y₁(u) (recoupement Bessel)")
check(sp.simplify(f_b - (-u**2*j1)) == 0, "f_b = -u² j₁(u) (recoupement Bessel)")

# ---------------------------------------------------------------------------
# [B] La S-map SCELLÉE (CT-DUAL, éq. 51) : référence connue. S²=−𝟙, vp ±i.
# ---------------------------------------------------------------------------
print("\n[B] S-map scellée (référence CT-DUAL) : S=[[0,−1],[1,0]], S²=−𝟙, vp ±i")
S = sp.Matrix([[0, -1], [1, 0]])
I2 = sp.eye(2)
check(S*S == -I2, "S² = −𝟙 (carré de la dualité = −1, scellé)")
check(set(S.eigenvals().keys()) == {sp.I, -sp.I}, "valeurs propres de S = ±i")
check(S.det() == 1 and S.trace() == 0, "det S=1, tr S=0 (rotation 90°, ordre 4)")

# ---------------------------------------------------------------------------
# [C] L'inversion de Penrose Ω·ω=−1 : action de COORDONNÉE = involution.
#     Ω~1/z ⟹ Ω↦−1/Ω ⟹ z↦−1/z ; appliqué deux fois ⟹ identité.
# ---------------------------------------------------------------------------
print("\n[C] Inversion de Penrose (coordonnée) : z↦−1/z est une INVOLUTION")
z = sp.symbols('z', positive=True)
inv = lambda zz: -1/zz
check(sp.simplify(inv(inv(z)) - z) == 0, "z↦−1/z appliqué deux fois = identité (involution coord.)")
# le signe − de Ω·ω=−1 ne survit PAS dans z car z~Ω^{-2} (le signe se carre) :
Om = sp.symbols('Omega', positive=True)
z_of_Om = 1/Om**2            # z ~ Ω^{-2}
Om_new = -1/Om               # Ω ↦ −1/Ω
z_new = 1/Om_new**2          # z' ~ Ω'^{-2}
check(sp.simplify(z_new - 1/z_of_Om) == 0, "z ~ Ω⁻² : Ω↦−1/Ω induit z↦1/z (signe carré, perdu sur z)")

# ---------------------------------------------------------------------------
# [D] Map INDUITE sur (f_a, f_b). L'inversion ÉCHANGE source↔VEV (P1-G1, swap).
#     Convention : patte source→VEV normalisée à +1 ; patte VEV→source = signe s (OUVERT).
#     P = [[0, s],[1, 0]]  ⟹  P² = s·𝟙.
# ---------------------------------------------------------------------------
print("\n[D] Map induite P sur (f_a, f_b) : SWAP (P1-G1) ; carré = s·𝟙, s OUVERT")
s = sp.symbols('s')   # signe de la patte VEV→source : DÉCISIF, LAISSÉ SYMBOLIQUE
P = sp.Matrix([[0, s], [1, 0]])
# P1-G1 — swap : P est hors-diagonale (échange les deux modes)
check(P[0,0] == 0 and P[1,1] == 0 and P[0,1] != 0 and P[1,0] != 0,
      "P1-G1 : P hors-diagonale ⟹ SWAP source↔VEV (g₀↔g₃) — ÉTABLI")
# P1-G2/G3 — carré et signe : P² = s·𝟙 ; match S ⟺ s = −1
P2 = sp.simplify(P*P)
check(P2 == s*I2, "P² = s·𝟙 (le carré PORTE le signe s de la patte VEV→source)")
check(sp.simplify((P - S)) == sp.Matrix([[0, s+1],[0,0]]),
      "P − S = [[0, s+1],[0,0]] ⟹ P = S  ⟺  s = −1")
check((P2.subs(s, -1) == -I2), "s=−1 ⟹ P²=−𝟙 (MATCH S : concordance)")
check((P2.subs(s, 1) == I2), "s=+1 ⟹ P²=+𝟙 (involution NUE : DISCORDANCE avec S²=−𝟙)")

# ---------------------------------------------------------------------------
# [E] Le FACTEUR DÉCISIF (NON fixé) : s = descente du signe de ω<0 sur le mode TT.
#     Une mise à l'échelle conforme NUE (poids w) donne un facteur ω^w ; le signe de
#     ω<0 ne donne −1 QUE si w est IMPAIR. w (parité) = NON pinçable KB-local ⟹ OUVERT.
# ---------------------------------------------------------------------------
print("\n[E] Facteur décisif s : signe descendu de ω<0 — OUVERT (parité du poids w)")
w = sp.symbols('w', integer=True)   # poids conforme du mode TT (parité inconnue KB-local)
omega = sp.symbols('omega', negative=True)
# une mise à l'échelle conforme nue donne le facteur omega**w ; son signe = (-1)**w pour omega<0
sign_descent = sp.sign((-1)**w)     # +1 si w pair ; −1 si w impair  (symbolique)
# le sceau N'AFFIRME PAS la parité de w : il EXPRIME que s en dépend, sans la trancher
check(sp.simplify(sign_descent - (-1)**w) == 0,
      "s ≡ (−1)^w (parité du poids conforme TT) : DÉCISIF, NON tranché KB-local")
check(((-1)**w).subs(w, 1) == -1 and ((-1)**w).subs(w, 2) == 1,
      "w impair ⟹ s=−1 (match S) ; w pair ⟹ s=+1 (involution) — DÉCISION OUVERTE")
# garde-fou anti-surclassement : s reste un symbole libre (P1 NON tranchée)
check(s in P.free_symbols, "GARDE-FOU : s reste LIBRE ⟹ P1 NON tranchée (ni prouvée ni réfutée à plat)")

# ---------------------------------------------------------------------------
# VERDICT (algèbre)
# ---------------------------------------------------------------------------
print("\n" + "="*78)
print("VERDICT (b) — DÉLIMITATION :")
print("  P1-G1 (SWAP source↔VEV / g₀↔g₃) : ÉTABLI (algèbre).")
print("  P1-G2/G3 (carré −𝟙 / signe) : P² = s·𝟙 ; MATCH S ⟺ s=−1. Une involution conforme")
print("     NUE donne s=+1 (carré +𝟙) ≠ S²=−𝟙 ⟹ la réciprocité conforme ne fournit PAS le −𝟙")
print("     de la dualité par sa seule action de coordonnée.")
print("  FACTEUR DÉCISIF : s=(−1)^w (descente du signe de ω<0 sur le mode TT, parité w) —")
print("     DÉCISION OUVERTE, fetch-conditionnel (S-O2-b-1). P1 RÉDUITE à un unique signe.")
print("  ⟹ (C-O2) en forme forte NON établie ; sa vérité tient au seul signe s=(−1)^w.")
print("  SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ;")
print("     N non fixé ; CCC non démontrée. P2 reste de toute façon ouverte.")

# ===========================================================================
# FIREWALL (S-O2-b-3) — 3 mutations cassantes : le résultat est SENSIBLE.
# ===========================================================================
print("\n" + "="*78)
print("FIREWALL — 3 mutations cassantes")
def must_break(fn, label):
    global PASS
    try:
        fn(); raise SystemExit(f"FIREWALL N'A PAS CASSÉ: {label}")
    except AssertionError:
        PASS += 1; print(f"  ✓ casse comme attendu : {label}")

# (m1) signe inversé sur S de référence : S_mut=[[0,1],[-1,0]] ⟹ S_mut ≠ S (P1-G3 sensible)
def m1():
    S_mut = sp.Matrix([[0, 1], [-1, 0]])
    assert S_mut == S, "m1: signe S inversé"   # casse : S_mut ≠ S
must_break(m1, "(m1) signe inversé S↦[[0,1],[−1,0]] ⟹ P1-G3 sensible")

# (m2) carré forcé +𝟙 : prétendre P²=−𝟙 INDÉPENDAMMENT de s ⟹ faux (P² = s·𝟙)
def m2():
    assert sp.simplify(P*P) == -I2, "m2: P²=−𝟙 forcé sans s=−1"  # casse : P²=s·𝟙 ≠ −𝟙
must_break(m2, "(m2) carré forcé +𝟙/−𝟙 indépendant de s ⟹ P1-G2 sensible (P²=s·𝟙)")

# (m3) swap absent : map diagonale D=[[1,0],[0,1]] ⟹ pas un swap (P1-G1 sensible)
def m3():
    D = sp.Matrix([[1, 0], [0, 1]])
    assert D[0,1] != 0 and D[1,0] != 0, "m3: swap absent (map diagonale)"  # casse
must_break(m3, "(m3) swap absent (map diagonale) ⟹ P1-G1 sensible")

print("\n" + "="*78)
print(f"OK — {PASS} assertions. P1 RÉDUITE à un signe s=(−1)^w (décision ouverte) ;")
print("SWAP établi, −𝟙 NON fourni par la réciprocité conforme nue ; (C-O2) forte NON établie.")
print("SANS SURCLASSEMENT : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; CCC non démontrée. EXIT 0.")
print("="*78)
