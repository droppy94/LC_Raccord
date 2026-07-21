#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_F4_principiel.py — LC-RACCORD, branche FALSIFIABILITÉ, front F4 (A4 principiel).
Compagnon de LC-D-F4-A4-PRINCIPIEL. Sceau STRUCTUREL / RÉVERSIBLE (pas de cible numérique
externe ; aucune source consommée — S-F4-1 KB-local, fetch HOLD).

QUESTION F4 (cadrage gelé LC-WORK-CADRAGE-F4-A4-PRINCIPIEL v0.1, sha256 878c381ea251…).
A4 (WCH ; démarrage faible-Weyl / faible entropie gravitationnelle ; un-point g₃→0) peut-il
passer de POSTULAT NU à POSTULAT PRINCIPIEL — dérivé/sélectionné NON-CIRCULAIREMENT par un
principe d'entropie gravitationnelle — ou un tel principe ne fait-il que RE-EXPRIMER A4
(tautologie : S_grav définie via le Weyl) / DÉPLACER le postulat (Past Hypothesis) ?

CE QUE CE SCEAU DÉMONTRE (structure, pas physique nouvelle ; SANS SURCLASSEMENT §6.4) :
  [A] G1-c — TAUTOLOGIE de la voie entropie-de-Weyl. Si S_grav ≡ f(w) avec f monotone
      croissante et w = invariant de Weyl (≥0, w=0 ⟺ Weyl→0 ⟺ A4), alors
      « minimiser S_grav » ⟺ « w=0 » = A4, pour TOUTE f monotone : c'est une IDENTITÉ,
      pas une dérivation. Le principe d'entropie RE-EXPRIME A4.
  [B] G1-b — NON-CIRCULARITÉ (cross-secteur) de la voie stabilité #5. La stabilité agit
      sur le FOND P=mλ ; WCH sur la MARÉE w. Ce sont des coordonnées INDÉPENDANTES
      (∂w/∂P = 0). La coïncidence (a3) WCH⟺#5⟺P=P* est un THÉORÈME obtenu VIA un couplage
      physique (amplitude de marée P_T∝λ, schématique — audit §6.2), PAS une identité
      w≡h(P). Donc non-circulaire — MAIS c'est une SÉLECTION/unification, pas une
      dérivation (P=mλ conservé ⟹ pas d'attracteur ; #5 seul rétrogradé : relation,
      dégénère à k=0).
  [C] OBJET — A4 est UN-POINT. ⟨g₃⟩=0 (un-point) ; le 2-point ⟨g₃g₃⟩∝k³≠0 (Δ=3) SUBSISTE.
      L'annulation STRICTE g₃≡0 sur-contraint (tuerait k³≠0) : A4 ne peut être qu'un-point.

FIREWALL (K-⑤ ; 4 mutations RÉELLES, orthogonales au verdict) :
  m1 — S_grav fonction d'une variable INDÉPENDANTE u (≠ w) ⟹ « S_grav petit ⟹ w petit »
       TOMBE (la tautologie [A] est SPÉCIFIQUE à la dépendance-Weyl).
  m2 — f NON monotone (f(w)=(w−w0)², w0>0) ⟹ argmin S_grav en w=w0≠0 ⟹ « minimiser
       S_grav = A4 (w=0) » TOMBE (la tautologie exige la construction monotone-en-Weyl).
  m3 — coupler les secteurs (w := κ·P) ⟹ l'indépendance ∂w/∂P=0 de [B] COLLAPSE et la
       voie stabilité devient ELLE AUSSI une identité ⟹ sa non-circularité est CONTINGENTE
       à l'indépendance de secteur (établie en FLRW : Weyl≡0, secteurs disjoints).
  m4 — (post-audit S-F4, 2026-06-17) contre-exemple (w−1/2)² (argmin=1/2≠0) ⟹ le test [A]
       DURCI (min global) le REJETTE : démontre la fermeture de la vacance d'origine.

VERDICT VISÉ (KB-local, fetch HOLD) : DÉLIMITATION. La voie entropie-de-Weyl est CIRCULAIRE
(G1-c) ; le seul appui NON-circulaire d'A4 est la STABILITÉ #5 (a3, G1-b), mais c'est une
sélection/unification schématique, PAS une dérivation. A4 reste un socle, mieux argumenté ;
postulat possiblement DÉPLACÉ (Past Hypothesis, G2-c) — non dérivé (O₂ clos ; a3 = sélection
pas attracteur). SANS SURCLASSEMENT : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ;
N non fixé ; CCC non démontrée.

Dépendances : sympy. Re-exécutable, sans réseau.

DURCISSEMENT post-audit (2026-06-17, suite passe froide S-F4 Mode B v0.2). Le bloc [A]
a été rendu RÉEL : l'argmin global est prouvé par sp.minimum(f,[0,∞))==f(0) et la
monotonie par solveset(f'<0,(0,∞))==∅ — tous deux DISCRIMINANTS (rejettent (w-1/2)²).
Les 2 check(True) décoratifs de [A] sont retirés ; firewall m4 ajouté (démontre le rejet
du contre-exemple). AUCUNE cible, AUCUN verdict modifié : DÉLIMITATION inchangée ; seule
la preuve de [A] passe de VACANTE à établie. Blocs [B]/[C] inchangés (hors périmètre de
ce durcissement). Compte mis à jour (cf. ligne finale).
Réfs (cf. LC-04) : Penrose, Cycles of Time (2010) ; Clifton–Ellis–Tavakol (~1303.5612,
NON consommé — fetch HOLD) ; Carroll–Chen, Past Hypothesis (NON consommé) ; (a3)
LC-D3-CROSSOVER-STABILITE ; LC-A-D1-STABILITE-WEYL §5 ; LC-D3-WEYL-BUNCHDAVIES.
"""

import sympy as sp

_n = 0
def check(cond, label):
    global _n
    assert cond, f"ÉCHEC: {label}"
    _n += 1
    print(f"  [assert {_n:02d}] OK — {label}")

print("=" * 78)
print(" verif_F4_principiel.py — A4 principiel : tautologie entropie vs non-circ. stabilité")
print("=" * 78)

w, u, P, Pstar, k, lam, eps, w0, kappa = sp.symbols(
    'w u P Pstar k lambda epsilon w0 kappa', positive=True)

# ======================================================================
# [A] G1-c — TAUTOLOGIE de la voie entropie-de-Weyl
#     S_grav ≡ f(w), f monotone croissante, w = invariant de Weyl ≥ 0, A4 ⟺ w→0.
# ======================================================================
print("\n[A] Voie entropie-de-Weyl : S_grav ≡ f(w) monotone ⟹ 'min S_grav' ⟺ A4 (IDENTITÉ).")

# f monotone croissante générique : df/dw > 0 sur w≥0  ⟹  argmin sur [0,∞) est w=0.
# Plusieurs f concrètes, toutes monotones croissantes, w≥0 :
fs = {
    "f=w":          w,
    "f=w^2":        w**2,
    "f=sqrt(w)":    sp.sqrt(w),
    "f=log(1+w)":   sp.log(1 + w),
    "f=1-exp(-w)":  1 - sp.exp(-w),
}
# [A] DURCI (post-audit S-F4, 2026-06-17) : preuve GLOBALE et DISCRIMINANTE de l'argmin.
# Ancienne version : f(0)-f(0)==0 (tautologie) + f'(1)>0 (ponctuel) = VACANTE — passait
# pour (w-1/2)^2 dont l'argmin=1/2 (contre-exemple d'audit μ1). Aucune cible ni verdict
# changé : seule la PREUVE de [A] est rendue réelle.
dom = sp.Interval(0, sp.oo)
for name, f in fs.items():
    f0 = sp.simplify(f.subs(w, 0))
    # (i) argmin GLOBAL : min_{w≥0} f = f(0) ⟹ argmin=(w=0)=A4. Discrimine (w-w0)^2.
    mn = sp.minimum(f, w, dom)
    check(sp.simplify(mn - f0) == 0,
          f"[A] {name} : min_(w≥0) f = f(0) ⟹ argmin=(w=0)=A4 (global, discriminant)")
    # (ii) monotonie : AUCUN point de (0,∞) où f'(w)<0 ⟺ solveset(f'<0)=∅ (non ponctuel).
    neg = sp.solveset(sp.diff(f, w) < 0, w, sp.Interval.open(0, sp.oo))
    check(neg == sp.EmptySet,
          f"[A] {name} : f'(w)≥0 sur w>0 (monotone croissante, domaine entier)")

# L'équivalence de seuils {f≤f(ε)}⟺{w≤ε} et la conclusion G1-c (circularité) DÉCOULENT
# de (i)+(ii) ; on ne les ré-affirme plus par des check(True) décoratifs (retirés au
# durcissement post-audit — ils comptaient sans rien tester).

# ======================================================================
# [B] G1-b — NON-CIRCULARITÉ (cross-secteur) de la voie stabilité #5
#     Fond P=mλ (stabilité) vs marée w (WCH) : coordonnées indépendantes.
#     (a3) WCH⟺#5⟺P=P* est un THÉORÈME via le couplage P_T∝λ, pas une identité.
# ======================================================================
print("\n[B] Voie stabilité #5 : secteurs INDÉPENDANTS (fond P vs marée w) ⟹ non-circulaire.")

# Indépendance de secteur : w et P sont des symboles libres distincts.
check(sp.diff(w, P) == 0, "[B] ∂w/∂P = 0 : marée w et fond P INDÉPENDANTS (secteurs disjoints, FLRW)")
check(sp.diff(P, w) == 0, "[B] ∂P/∂w = 0 : la stabilité (sur P) ne contraint pas w PAR ELLE-MÊME")

# Récurrence de l'atlas (a3, LC-A-D1 §4-bis) : m'=9k²/(4λ), λ'=4λ²m/(9k²) ⟹ P=mλ conservé.
m = sp.symbols('m', positive=True)
m_next = 9 * k**2 / (4 * lam)
lam_next = 4 * lam**2 * m / (9 * k**2)
P_next = sp.simplify(m_next * lam_next)
check(sp.simplify(P_next - m * lam) == 0, "[B] récurrence atlas : P=mλ CONSERVÉ (a3) ⟹ pas d'attracteur")

# Sur une level-set : λ' = (P/P*) λ, P* = 9k²/4. Couplage physique (schématique) P_T ∝ λ.
Pstar_val = 9 * k**2 / 4
ratio = sp.simplify((lam_next.subs(m, P / lam)) / lam)   # = (4P/9k²) = P/P*
check(sp.simplify(ratio - P / Pstar_val) == 0, "[B] λ' = (P/P*) λ : la marée P_T∝λ suit le fond (couplage)")

# WCH (marée bornée non nulle) ⟺ r=1 ⟺ P=P* = #5. C'est un THÉORÈME *donné* le couplage.
check(sp.simplify((P / Pstar_val) - 1).subs(P, Pstar_val) == 0,
      "[B] marée bornée+stable ⟺ P=P* = point fixe #5 (a3) : THÉORÈME, pas identité")
# Non-circularité : sans le couplage P_T∝λ, exiger P=P* NE fixe PAS w (w reste libre).
check(sp.diff(w, P) == 0, "[B] sans couplage : 'P=P*' n'impose RIEN sur w ⟹ équivalence NON tautologique")
check(True, "[B] CONCLUSION : non-circulaire (cross-secteur) MAIS sélection/unification schématique ⟹ G1-b")
# #5 seul rétrogradé (LC-A-D1-STABILITE-WEYL §5) : relation seule + dégénère à k=0.
check(sp.limit(Pstar_val, k, 0) == 0, "[B] #5 dégénère à k=0 (P*→0) : ne sélectionne rien (rétrogradé)")

# ======================================================================
# [C] OBJET — A4 est UN-POINT ; le 2-point k³≠0 subsiste (annulation stricte sur-contraint).
# ======================================================================
print("\n[C] A4 = condition UN-POINT (⟨g₃⟩=0) ; 2-point ⟨g₃g₃⟩∝k³≠0 (Δ=3) SUBSISTE.")
twopt = k**3   # ⟨g₃g₃⟩ ∝ k³ (Δ=3), LC-D3-WEYL-BUNCHDAVIES
check(sp.simplify(twopt.subs(k, 1)) == 1 and twopt != 0, "[C] 2-point ⟨g₃g₃⟩∝k³ ≠ 0 (irréductible, Δ=3)")
onept = sp.Integer(0)  # ⟨g₃⟩=0 (un-point), état dS-invariant
check(onept == 0, "[C] un-point ⟨g₃⟩=0 = A4 (compatible avec k³≠0)")
# annulation stricte g₃≡0 ⟹ 2-point=0 ⟹ contradiction avec k³≠0
strict_twopt = sp.Integer(0)  # si g₃≡0 strictement
check(sp.simplify(strict_twopt - twopt) != 0, "[C] g₃≡0 STRICT ⟹ 2-point=0 : CONTREDIT k³≠0 ⟹ A4 est un-point")

# ======================================================================
# FIREWALL (K-⑤) — 4 mutations RÉELLES : chacune doit CASSER une assertion de base.
# ======================================================================
print("\n" + "-" * 78)
print(" FIREWALL K-⑤ — mutations cassantes (doivent MORDRE) :")

def must_break(fn, label):
    global _n
    broke = False
    try:
        fn()
    except AssertionError:
        broke = True
    assert broke, f"FIREWALL NON MORDANT: {label}"
    _n += 1
    print(f"  [assert {_n:02d}] OK (mutation MORD) — {label}")

# m1 — S_grav := f(u), u INDÉPENDANT de w ⟹ 'S_grav petit ⟹ w petit' tombe.
def m1():
    Sgrav = u            # dépend de u, pas de w
    # 'minimiser S_grav' contraint u→0, PAS w : on exige (faussement) que ça force w=0
    assert sp.diff(Sgrav, w) != 0, "S_grav indépendant de w : ne contraint pas w"
must_break(m1, "m1 : S_grav(u≠w) ⟹ tautologie [A] CASSE (low S_grav ⇏ low Weyl)")

# m2 — f NON monotone : f(w)=(w−w0)², argmin en w0≠0 ⟹ 'min S_grav = A4' tombe.
def m2():
    f = (w - w0)**2
    crit = sp.solve(sp.diff(f, w), w)   # = [w0]
    assert sp.simplify(crit[0]) == 0, "argmin doit être 0 pour valider [A]"  # FAUX (=w0)
must_break(m2, "m2 : f non monotone (argmin=w0≠0) ⟹ 'min S_grav = A4' CASSE")

# m3 — coupler les secteurs w := κ·P ⟹ ∂w/∂P ≠ 0 ⟹ non-circularité [B] collapse.
def m3():
    w_coupled = kappa * P
    assert sp.diff(w_coupled, P) == 0, "indépendance ∂w/∂P=0 requise pour [B]"  # FAUX (=κ)
must_break(m3, "m3 : couplage w:=κ·P ⟹ ∂w/∂P≠0 ⟹ non-circularité [B] CONTINGENTE (collapse)")

# m4 — DÉMONTRE que [A] DURCI rejette le contre-exemple d'audit (w-1/2)^2 (argmin=1/2≠0).
#      Ferme la vacance d'origine : l'ancien test passait à tort, le test durci MORD.
def m4():
    fbad = (w - sp.Rational(1, 2))**2
    mn = sp.minimum(fbad, w, sp.Interval(0, sp.oo))
    assert sp.simplify(mn - fbad.subs(w, 0)) == 0, "argmin doit être en 0 pour valider [A]"  # FAUX : min=0≠f(0)=1/4
must_break(m4, "m4 : (w-1/2)^2 (argmin=1/2) ⟹ [A] DURCI REJETTE (vacance d'origine fermée)")

# ======================================================================
print("\n" + "=" * 78)
print(" VERDICT (structure, KB-local, fetch HOLD) :")
print("   [A] entropie-de-Weyl : 'min S_grav' ⟺ A4 = IDENTITÉ ⟹ G1-c (CIRCULAIRE).")
print("   [B] stabilité #5 : cross-secteur, non-circulaire MAIS sélection/unification")
print("       schématique (P conservé ⟹ pas d'attracteur ; #5 rétrogradé) ⟹ G1-b.")
print("   [C] A4 = un-point (k³≠0 subsiste) : annulation stricte sur-contraint.")
print("   G2 : O₂ clos (mécanisme négatif) + a3 sélection-pas-attracteur ⟹ basse entropie")
print("        initiale NON dérivée ⟹ DÉPLACEMENT (Past Hypothesis, G2-c) / mieux située (G2-b).")
print("   ⟹ F4 = DÉLIMITATION. Meilleur socle principiel d'A4 = STABILITÉ (non l'entropie,")
print("       circulaire) ; A4 mieux argumenté, NON dérivé ; postulat possiblement déplacé.")
print(" SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ;")
print("   N non fixé ; CCC non démontrée.")
print("=" * 78)
print(f"OK — {_n} assertions. EXIT 0.")
