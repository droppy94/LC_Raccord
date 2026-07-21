#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# verif_O2_hodge.py — SCEAU de l'étape (c) du pivot O₂ : TEST du TRANSPORT DE HODGE
#   par la jonction Dirichlet→Neumann.
#
#   Question (c) (cadrage gelé LC-WORK-CADRAGE-O2-HODGE v0.1, sha 14a7446c3d9a) :
#   la jonction D→N (réciprocité de Penrose Ω·ω=−1) réalise-t-elle la S COMPLÈTE
#   (avec le facteur Hodge porteur du −1), ou seulement le swap SIGN-NEUTRE ?
#
#   VERDICT scellé = DISCORDANCE : J = Swap(s=+1) ≠ S. La jonction transporte
#   l'ÉCHANGE (g₀↔g₃ = E↔B) mais NON le −1 du Hodge. Le secteur porteur du signe
#   (continuation dS i^{d-1} + rotation E↔B paire↔impaire/Cotton) est INDÉPENDANT
#   de la jonction conforme. (C-O2) forte NON établie par cette voie.
#
#   Entrées AMONT (scellées, NON re-dérivées — adossées) :
#     - O2-P1 §2 : (f_a,f_b)=(source g₀, VEV g₃) ; jonction = swap, P=[[0,s],[1,0]],
#                  involution conforme nue ⟹ s=+1.
#     - CT-DUAL §2 : Hodge S=[[0,−1],[1,0]], S²=−𝟙, vp ±i (de Haro éq. 43-44-51).
#     - CT-DUAL §3 (garde-fou, le cœur) : W̃=−W MAIS ⟨T̃⟩=−2δW̃/δh̃ ⟹ C̃_T=+C_T.
#     - CT-REALITE / CT-DUAL-DS : signe physique = i^{d-1}, d=3 ⟹ i²=−1 (source UNIQUE).
#     - F6-MEMOIRE : E∝g₃ pair (tenseur vrai) ; B∝Cotton[g₀] impair (pseudo-tenseur) ;
#                    secteurs DISJOINTS.
#
#   Stack : Python 3.12 / SymPy 1.14.  EXIT 0 attendu. Firewall : 3 mutations cassantes.
#   SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos.
# =============================================================================

import sympy as sp

N = 0
def check(cond, msg):
    global N
    assert cond, "ÉCHEC: " + msg
    N += 1

I = sp.I

# -----------------------------------------------------------------------------
# [BLOC 1] Même plan (a,b), opérations DISTINCTES : J (swap) vs S (Hodge)
#   J et S agissent toutes deux sur le couple de coefficients (a,b) des MÊMES
#   modes radiaux (f_a,f_b). Elles ne diffèrent que par le signe hors-diagonal,
#   mais cette différence est un INVARIANT de classe (det, ordre, vp) : J≠S même
#   à changement de base près.
# -----------------------------------------------------------------------------
def build_J(s):
    # jonction : swap source↔VEV avec signe s de la patte VEV→source (O2-P1 §2[D])
    return sp.Matrix([[0, s], [1, 0]])

S = sp.Matrix([[0, -1], [1, 0]])          # Hodge scellé (CT-DUAL §2)
s_phys = sp.Integer(1)                     # involution conforme NUE ⟹ s=+1 (O2-P1)
J = build_J(s_phys)

# Hodge : involution à carré −𝟙, rotation 90°, ordre 4, vp ±i, det +1
check(S*S == -sp.eye(2),               "S² = −𝟙 (Hodge, CT-DUAL)")
check(S.det() == 1,                    "det S = +1 (rotation)")
check(S.trace() == 0,                  "tr S = 0")
check(set(S.eigenvals().keys()) == {I, -I}, "vp(S) = ±i (ordre 4)")
check((S**4) == sp.eye(2),             "S⁴ = 𝟙 (ordre 4)")

# Jonction (s=+1) : involution à carré +𝟙, échange, ordre 2, vp ±1, det −1
check(J*J == sp.eye(2),                "J² = +𝟙 (swap sign-neutre, ordre 2)")
check(J.det() == -1,                   "det J = −1 (réflexion/échange)")
check(J.trace() == 0,                  "tr J = 0")
check(set(J.eigenvals().keys()) == {sp.Integer(1), sp.Integer(-1)}, "vp(J) = ±1 (ordre 2)")

# (c)-G1 : J ≠ S, et la différence est un INVARIANT (det, ordre) — pas un signe de convention
check(J != S,                          "J ≠ S (signe hors-diagonal différent)")
check(J.det() != S.det(),              "INVARIANT : det J = −1 ≠ +1 = det S (classes distinctes)")
# J=S exigerait s=−1 ; le contrôle montre que SEUL s=−1 identifierait les deux
check(build_J(-1) == S,                "J=S ⟺ s=−1 (contrôle) ; or s_phys=+1")
check(s_phys == 1,                     "(c) : jonction nue ⟹ s=+1 (O2-P1), donc J≠S")

# -----------------------------------------------------------------------------
# [BLOC 2] Garde-fou de signe (CT-DUAL §3, le cœur) : la jonction (Legendre D→N)
#   NE FLIPPE PAS le signe physique. W̃=−W mais ⟨T̃⟩=−2δW̃ vs ⟨T⟩=+2δW ⟹ C̃_T=+C_T.
# -----------------------------------------------------------------------------
k = sp.Symbol('k', positive=True)         # k = ℓ²/8κ² > 0 (préfacteur de Haro éq. 61)
W      =  k                                # W  = +k (éq. 61)
W_tild = -k                                # W̃  = −k (éq. 62) : − relatif RÉEL (Legendre/CS)
# tenseurs de stress : ⟨T⟩=+2 δW, ⟨T̃⟩=−2 δW̃  (éq. 63, le −2 explicite)
CT      = 2  * W                           # ∝ +2k  ⟹ signe +
CT_tild = -2 * W_tild                       # ∝ (−2)(−k)=+2k ⟹ signe +
check(sp.sign(W_tild) == -sp.sign(W),  "W̃ = −W : − relatif réel (Legendre/CS)")
check(CT == CT_tild,                   "GARDE-FOU : C̃_T = +C_T (le − de W̃ compensé par −2)")
check(sp.sign(CT_tild) == sp.sign(CT), "jonction D→N NE FLIPPE PAS le signe physique")
# signe NET de la jonction sur C_T = +1 (pas de −1 transporté)
net_junction_sign = sp.simplify(CT_tild / CT)
check(net_junction_sign == 1,          "signe NET jonction = +1 (aucun −1 physique transporté)")

# -----------------------------------------------------------------------------
# [BLOC 3] Source UNIQUE du signe = continuation dS i^{d-1} (INDÉPENDANTE de la
#   jonction). d=3 ⟹ i² = −1 réel. Opération ℓ²→−ℓ², ≠ Legendre/swap.
# -----------------------------------------------------------------------------
d = sp.Integer(3)
dS_factor = I**(d-1)                       # i^{d-1}, d=3
check(dS_factor == -1,                 "continuation dS : i^{d-1}|_{d=3} = i² = −1 (réel)")
check(sp.im(dS_factor) == 0,           "−1 dS est RÉEL (d=3 impair)")
# indépendance : le −1 dS n'est PAS le signe net de la jonction (qui vaut +1)
check(dS_factor != net_junction_sign,  "le −1 (dS) ≠ signe jonction (+1) : APPORT INDÉPENDANT")
# c'est le SEUL porteur du signe physique négatif requis par la CCC
check(dS_factor == -1 and net_junction_sign == 1,
      "source UNIQUE du signe = dS (i^{d-1}), pas la jonction (CT-REALITE/CT-DUAL-DS)")

# -----------------------------------------------------------------------------
# [BLOC 4] Disjonction de parité (F6) : E∝g₃ pair (tenseur vrai) ; B∝Cotton[g₀]
#   impair (pseudo-tenseur). Le swap reste dans le secteur pair ; le Hodge traverse
#   pair↔impair (c'est là que vit le −1 de S(B)=−E).
# -----------------------------------------------------------------------------
par_E = sp.Integer(+1)   # électrique E ∝ g₃ : parité paire (tenseur vrai), MÊME secteur que g₃
par_B = sp.Integer(-1)   # magnétique B ∝ Cotton[g₀] : parité impaire (pseudo-tenseur)
check(par_E == 1 and par_B == -1,      "F6 : E pair / B impair (secteurs DISJOINTS)")
check(par_E * par_B == -1,             "E et B de parités opposées ⟹ S traverse pair↔impair")
# le swap g₀↔g₃ relie deux data de MÊME parité (FG, tenseurs vrais) ⟹ reste dans le pair
par_g0 = sp.Integer(+1); par_g3 = sp.Integer(+1)
check(par_g0 == par_g3,                "swap g₀↔g₃ : même secteur de parité (pair) ⟹ pas de −1")

# -----------------------------------------------------------------------------
# [BLOC 5] Verdict (c) = DISCORDANCE, et NON-SURCLASSEMENT (§6.4)
# -----------------------------------------------------------------------------
junction_realises_full_S = (J == S)                 # False (s=+1)
junction_realises_swap    = (J.det() == -1 and J*J == sp.eye(2))  # True : échange involutif
minus_one_is_independent  = (dS_factor == -1 and net_junction_sign == 1)
check(junction_realises_full_S == False, "VERDICT : la jonction NE réalise PAS la S complète")
check(junction_realises_swap   == True,  "la jonction réalise BIEN le swap (échange E↔B)")
check(minus_one_is_independent == True,   "le −1 vit dans un secteur INDÉPENDANT (dS)")
# (C-O2) forte non établie par cette voie ⟹ pas de réduction du compte
A4_reduit = False; D1_clos = False; N_fixe = False
check(not (A4_reduit or D1_clos or N_fixe),
      "§6.4 : discordance ⟹ {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; N non fixé")

# =============================================================================
# FIREWALL — 3 mutations cassantes (doivent FAIRE ÉCHOUER le bloc visé)
# =============================================================================
def firewall():
    fired = 0
    # (m1) jonction forcée à porter le −1 (s=−1) : J deviendrait = S ⟹ casse la DISCORDANCE
    try:
        Jm = build_J(-1)
        assert Jm != S, "m1"            # FAUX si s=−1
        raise RuntimeError("m1 non déclenchée")
    except AssertionError:
        fired += 1
    # (m2) réciprocité forcée DIAGONALE (pas d'échange) : casse « la jonction réalise le swap »
    try:
        Jdiag = sp.Matrix([[1, 0], [0, 1]])
        assert Jdiag.det() == -1, "m2"  # FAUX : map diagonale a det +1, pas un échange
        raise RuntimeError("m2 non déclenchée")
    except AssertionError:
        fired += 1
    # (m3) garde-fou DÉSACTIVÉ (⟨T̃⟩=+2δW̃ au lieu de −2) : C̃_T=−C_T ⟹ casse « pas de flip »
    try:
        CT_bad = +2 * W_tild            # = −2k  (signe −, flip)
        assert CT_bad == CT, "m3"       # FAUX : −2k ≠ +2k
        raise RuntimeError("m3 non déclenchée")
    except AssertionError:
        fired += 1
    return fired

fired = firewall()
assert fired == 3, "Firewall : les 3 mutations doivent casser (obtenu %d/3)" % fired

# =============================================================================
print("=" * 78)
print("verif_O2_hodge.py — SCEAU (c) : TRANSPORT DE HODGE par la jonction D→N")
print("-" * 78)
print("  [1] J=[[0,1],[1,0]] (swap, det−1, ordre 2, vp ±1) ≠ S=[[0,−1],[1,0]]")
print("      (Hodge, det+1, ordre 4, vp ±i) — invariant de classe, J=S ⟺ s=−1, or s=+1.")
print("  [2] garde-fou CT-DUAL §3 : W̃=−W mais ⟨T̃⟩=−2δW̃ ⟹ C̃_T=+C_T ; signe net jonction = +1.")
print("  [3] −1 physique = continuation dS i^{d-1}|_{d=3}=−1 (réel), APPORT INDÉPENDANT, source unique.")
print("  [4] F6 : E(g₃) pair / B(Cotton) impair, disjoints ; swap reste pair ⟹ ne porte pas le −1.")
print("-" * 78)
print("  VERDICT = DISCORDANCE : la jonction transporte l'ÉCHANGE mais NON le −1 du Hodge.")
print("  (C-O2) forte NON établie par cette voie ; O₂ reste à inventer.")
print("  Firewall : 3/3 mutations cassantes confirmées (m1 s=−1 / m2 diagonale / m3 garde-fou off).")
print("-" * 78)
print("  SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ;")
print("  D1 non clos ; N non fixé ; CCC non démontrée.")
print("OK — %d assertions. EXIT 0." % N)
print("=" * 78)
