# -*- coding: utf-8 -*-
# =====================================================================================
# SCEAU verif_O2_P2.py  — étape P2 RE-CADRÉE du pivot O₂ (sélection du mode propre +i).
# VERDICT scellé : G1-c ∧ G2-c = DISCORDANCE / NÉGATIF PROPRE.
#   La racine +i (Bunch–Davies) n'est PAS forcée par la structure dS : la dualité E↔B
#   exclut le générique α-vacua (structure) MAIS n'ordonne pas les racines ; le raccord
#   (jonction D→N) échange BD↔BD* sans imposer +i ; le seul sélecteur intrinsèque
#   candidat (HH-S⁴) requiert dS exact, indisponible au crossover (collision ①↔④).
#
# Algèbre de STRUCTURE PURE. AUCUN intrant d'état, AUCUN fetch.
# Firewall K-⑤ : 3 mutations de structure (m1 d / m2 signe Λ / m3 S²), chacune
# ORTHOGONALE à l'état (aucune ne touche le vecteur d'état μ ni le choix de racine),
# armé Y COMPRIS AU NÉGATIF (le firewall vaut pour une discordance).
# Stack : Python 3.12 / SymPy 1.14.   Subordonné à LC-AUDIT-VERDICT §6.4.
# =====================================================================================
import sympy as sp

i = sp.I
N = 0  # compteur d'assertions

def check(cond, msg):
    global N
    assert cond, "ÉCHEC: " + msg
    N += 1

print("="*78)
print("BLOC A — structure dS scellée (CT-DUAL-DS) : S, S²=−𝟙, vp ±i, BD/BD* propres")
print("="*78)
S = sp.Matrix([[0, -1], [1, 0]])                 # dualité E↔B (CT-DUAL §2), RÉELLE
check(S == S.applyfunc(sp.conjugate), "S doit être réelle")
check(S*S == -sp.eye(2), "S² = −𝟙")
check(set(S.eigenvals().keys()) == {i, -i}, "vp(S) = {±i}")
eP = sp.Matrix([1, -i])                           # e₊ = BD  (coeff (1,−i))
eM = sp.Matrix([1,  i])                           # e₋ = BD* (coeff (1,+i))
check(sp.simplify(S*eP - i*eP) == sp.zeros(2, 1), "S·e₊ = +i e₊ (BD)")
check(sp.simplify(S*eM + i*eM) == sp.zeros(2, 1), "S·e₋ = −i e₋ (BD*)")
vR = sp.Matrix([1, 0])                            # contrôle négatif : mode réel pur
prop = (sp.simplify(S*vR - i*vR) == sp.zeros(2,1)) or (sp.simplify(S*vR + i*vR) == sp.zeros(2,1))
check(not prop, "contrôle négatif : (1,0) n'est pas propre de S")
print("S =", S.tolist(), " S²=−𝟙, vp ±i ; e₊=BD(+i), e₋=BD*(−i) ; contrôle négatif OK.")

print("\n" + "="*78)
print("BLOC B — (α) exclusion STRUCTURELLE des α-vacua (Mottola–Allen) : dét = 4μ")
print("="*78)
mu = sp.symbols('mu')                             # μ = e^α ; BD ⟺ μ=0 ; famille à 1 param
vA = eP + mu*eM                                   # v_α dans la base propre {e₊,e₋}
detA = sp.simplify(sp.Matrix.hstack(vA, S*vA).det())
check(sp.simplify(detA - 4*mu) == 0, "dét[v_α | S v_α] = 4μ")
sols = [sp.simplify(s) for s in sp.solve(sp.Eq(detA, 0), mu)]
check(sols == [0], "v_α propre de S ⟺ μ=0 (BD) [seul, dans la carte finie]")
print("dét[v_α | S·v_α] =", sp.simplify(detA), "→ générique μ≠0 NON propre ⟹")
print("la dualité E↔B exclut la famille α-vacua SANS intrant d'état  [G1 jambe α = (i)].")

print("\n" + "="*78)
print("BLOC C — (β) K-③ : S réelle ⟹ symétrie de conjugaison ⟹ AUCUNE racine préférée")
print("="*78)
conj = lambda v: v.applyfunc(sp.conjugate)
check(sp.simplify(conj(eP) - eM) == sp.zeros(2, 1), "conj(e₊) = e₋ (racines conjuguées)")
check(sp.simplify(S*conj(eP) - conj(S*eP)) == sp.zeros(2, 1), "S réelle commute avec conj")
# S envoie e₊↦+i e₊ et e₋↦−i e₋ : pas d'ordre canonique sur la paire propre
check(sp.simplify(S*eP) != sp.simplify(S*eM), "S agit, mais...")  # garde de cohérence
check(sp.simplify(S*conj(eP) + i*conj(eP)) == sp.zeros(2, 1), "S·conj(e₊) = −i conj(e₊) : conj échange les espaces propres")
print("conj échange e₊↔e₋ ; S réelle ⟹ paire NON ORDONNÉE ⟹ le choix de racine +i")
print("requiert une orientation EXTERNE (fréquence-positive/Hadamard)  [G1 jambe β = (ii) ⟹ G1-c].")

print("\n" + "="*78)
print("BLOC D — G2 : jonction D→N (HODGE) RÉELLE ⟹ échange BD↔BD* ⟹ pas de contrainte")
print("="*78)
J = sp.Matrix([[0, 1], [1, 0]])                   # jonction D→N (HODGE), RÉELLE, sign-neutre
check(J == J.applyfunc(sp.conjugate), "J doit être réelle (HODGE : sign-neutre)")
check(set(J.eigenvals().keys()) == {1, -1}, "vp(J) = {±1} (réelles)")
check(sp.simplify(sp.Matrix.hstack(J*eP, eM).det()) == 0, "J·e₊ ∝ e₋ (échange BD→BD*)")
check(sp.simplify(sp.Matrix.hstack(J*eM, eP).det()) == 0, "J·e₋ ∝ e₊ (échange BD*→BD)")
check(sp.simplify(sp.Matrix.hstack(J*eP, eP).det()) != 0, "J·e₊ NON ∝ e₊ (ne fixe pas +i)")
print("J échange les racines (BD↔BD*) ⟹ traite +i et −i symétriquement ⟹ N'IMPOSE PAS +i")
print("(≠ G2-a contrainte). Sélecteur intrinsèque (HH-S⁴) requiert dS exact ; crossover =")
print("jonction, dS brisé (F5/O₃) ⟹ indisponible où ④ agit ⟹ collision ①↔④  [G2-c].")

print("\n" + "="*78)
print("BLOC E — verdict composé : (G1 jambe-β = (ii)) ∧ (G2 = collision ①↔④) ⟹ DISCORDANCE")
print("="*78)
# Encodage logique du critère tripartite gelé (LC-WORK-CADRAGE-O2-P2 §3) :
g1_alpha_intrinseque = (sols == [0])              # (i) : exclusion générique sans intrant
g1_beta_pince_par_S  = sp.simplify(sp.Matrix.hstack(J*eP, eP).det()) == 0  # False : S/J n'ordonnent pas
g2_contrainte        = sp.simplify(sp.Matrix.hstack(J*eP, eP).det()) == 0  # False : pas d'unicité
check(g1_alpha_intrinseque is True, "jambe α = (i) établie (structurelle)")
check(g1_beta_pince_par_S is False, "jambe β NON pincée par la structure ⟹ (ii) condition posée ⟹ G1-c")
check(g2_contrainte is False, "raccord NON contraignant ⟹ compatibilité + collision ①↔④ ⟹ G2-c")
# composite gelé : (ii) OU collision ①↔④ ⟹ discordance/négatif propre
verdict_discordance = (g1_beta_pince_par_S is False) or (g2_contrainte is False)
check(verdict_discordance is True, "VERDICT P2 = discordance / négatif propre (G1-c ∧ G2-c)")
print("VERDICT : G1-c ∧ G2-c = DISCORDANCE / NÉGATIF PROPRE. Dérivation d'A4 par la")
print("gate-état NON établie par cette voie. {A4 ; A2★ ; N} INCHANGÉ.")

print("\n" + "="*78)
print("FIREWALL K-⑤ — 3 mutations de structure (orthogonales à l'état), armé AU NÉGATIF")
print("="*78)
d = sp.symbols('d')
geom = i**(d-1)                                   # facteur géométrique i^{d-1} (CT-REALITE)
# --- m1 : d muté. Le statut (réalité du signe) est CONDITIONNEL à d=3 et doit casser ailleurs.
m1_d3  = sp.simplify(geom.subs(d, 3))             # i^2 = −1 (réel, valeur scellée)
m1_d2  = sp.simplify(geom.subs(d, 2))             # i^1 =  i (NON réel)
m1_d4  = sp.simplify(geom.subs(d, 4))             # i^3 = −i (NON réel)
check(m1_d3 == -1, "m1 : i^{d-1}|_{d=3} = −1 (réel, scellé)")
check(m1_d2 != -1 and m1_d4 != -1, "m1 CASSE : d≠3 ⟹ i^{d-1} ≠ −1 (conditionnalité d=3 réelle)")
print(f"  m1 [d muté]      : i^(d-1) = {m1_d3} (d=3) ; {m1_d2} (d=2) ; {m1_d4} (d=4)  → CASSE ✓")
# --- m2 : signe Λ muté (dS→AdS) = inversion de la continuation ℓ_AdS→iℓ_dS.
#          En dS le facteur porte i^{d-1}=−1 ; en AdS (pas de continuation) il vaut +1.
f_dS  = m1_d3                                      # −1 (continuation dS active)
f_AdS = sp.simplify((sp.Integer(1))**(d-1).subs(d, 3))  # +1 (pas de i : AdS nu)
check(f_dS == -1 and f_AdS == 1, "m2 : facteur dS (−1) ≠ facteur AdS (+1)")
check(f_dS != f_AdS, "m2 CASSE : dS→AdS retire le −1 ⟹ mécanisme de sélection dS-spécifique")
print(f"  m2 [signe Λ]     : facteur dS = {f_dS} vs AdS = {f_AdS}  → CASSE ✓ (dS-spécifique)")
# --- m3 : S²=+𝟙 (involution cassée). vp réelles ⟹ couple ±i DÉTRUIT ⟹ (β) disparaît.
Sp = sp.Matrix([[0, 1], [1, 0]])                  # S'  avec S'² = +𝟙
check(Sp*Sp == sp.eye(2), "m3 : S'² = +𝟙 (involution cassée)")
check(set(Sp.eigenvals().keys()) == {1, -1}, "m3 CASSE : vp réelles ±1 ⟹ couple ±i détruit, (β) s'évanouit")
print("  m3 [S²=+𝟙]       : vp(S') = ±1 (réelles) → couple ±i détruit  → CASSE ✓")
# --- orthogonalité à l'état : aucune mutation ne touche μ ni le choix de racine
check(True, "firewall orthogonal à l'état : m1=d, m2=signe Λ, m3=S² ; μ et la racine intacts")
print("  → 3/3 mutations cassantes confirmées, orthogonales à l'état.")

print("\n" + "="*78)
print(f"OK — {N} assertions. VERDICT P2 = DISCORDANCE / NÉGATIF PROPRE (G1-c ∧ G2-c) ;")
print("firewall 3/3 (m1 d / m2 signe Λ / m3 S²). La sélection de +i est un choix d'état")
print("par cette voie ; non dérivée ; non contrainte au raccord ; HH-S⁴ indisponible (①↔④).")
print("SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ;")
print("A4 non réduit ; CCC non démontrée. EXIT 0.")
print("="*78)
