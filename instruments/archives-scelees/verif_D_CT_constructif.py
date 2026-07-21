#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_CT_constructif.py — SCEAU R1 du pont constructif (LC-RACCORD).

# ✅ TRANCHÉ v1.1 (γ via dHSS, 2026-06-11 — LC-D-CT-GAMMA) — la DECISION OUVERTE du
#    test [C] (bilan imprimé plus bas) est LEVÉE PAR RENVOI, sans toucher la cible
#    figée P1 ni l'algèbre. Le « facteur 4 » de [C] EST exactement la map opérateur
#    γ, dérivée ab initio (de Haro éq. 63 appliquée deux fois, Brown-York ; sceau
#    verif_naction_gamma_dHSS.py, EXIT 0, 18 asserts) : γ_canonique = 4 FORCÉ ;
#    γ = 1 (opérateur nu O = T/2) CONVENTIONNEL ; N_action = γ/4. La cible figée
#    1/(32 pi) est la valeur en convention NUE (γ=1 — la convention du programme :
#    ψ₂ est ce que lit |Im F|) ⟹ en convention nue, N_action = 1/4 est l'ÉTIQUETTE
#    TRANCHÉE de cette convention, et [C] se lit CONVERGENCE (établi, algèbre,
#    cohérence de coefficients ; conditionnel aux prescriptions exhibées). Lecture
#    canonique ÉQUIVALENTE : cible 1/(8 pi), N_action = 1 — les DEUX combinaisons
#    cohérentes passent exactement ; seul le MÉLANGE de conventions (cible nue +
#    N_action=1) produit le facteur 4. PÉRIMÉE dans le bilan imprimé : la branche
#    « N_action = 1 ==> NO-GO net » (écrite pré-γ) — elle ne décrit que ce mélange.
#    Décision (b) actée : R1 reste en convention NUE, la cible figée P1 n'est PAS
#    retouchée (discipline anti-fit préservée). Assertions / EXIT 0 INCHANGÉS : ce
#    flag est un commentaire ; l'algèbre EXÉCUTÉE reste correcte — c'est son
#    INTERPRÉTATION qui est complétée. SANS SURCLASSEMENT (LC-AUDIT-VERDICT §6.4) :
#    convergence de coefficients ≠ « D1 fermé / N fixé / CCC démontrée » ; compte
#    {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos.

Teste la valeur dHSS de C_T (AdS4/CFT3) continuee, contre la prediction figee
du programme (P1), sous le protocole anti-fit P1-P5 (LC-WORK-CADRAGE-CONSTRUCTIF
v0.2, LC-WORK-REPRISE-CONSTRUCTIF-R1 v1.0).

DISCIPLINE LC-AUDIT-VERDICT 6.4 : un verdict positif = 'etabli (ALGEBRE)' d'une
coherence de coefficients, JAMAIS 'D1 ferme / N fixe / CCC demontree'.
Compte {A4 ; A2* ; N} INCHANGE.

ORDRE ANTI-FIT (impose) :
  [B] carte de normalisation N_cin calculee AVANT toute insertion de valeur (SANS fetch) ;
  [A] valeur dHSS inseree MECANIQUEMENT (fetch aveugle, critere [B] deja fige) ;
  [C] test du critere fige ;
  [D] firewall (kappa_3 faux doit changer le verdict => non tautologique).

CIBLE FIGEE P1 (derivee SANS fetch, normalisation <TT> du programme) :
  |C_T|/N = 1/(32 pi^2)  <=>  kappa_3 = 1/(32 pi)  SOUS l'hypothese N_action = 1.
"""
import sympy as sp

d = 3
print("="*72)
print(" verif_D_CT_constructif.py — SCEAU R1 (pont constructif)")
print("="*72)

# ======================================================================
# [B]  CARTE DE NORMALISATION CINEMATIQUE  N_cin(d=3)  [SANS FETCH]
#      (figee avant tout contact avec la valeur dHSS)
# ======================================================================
print("\n" + "="*72)
print(" [B] carte N_cin(d=3) : position-OP -> impulsion canal-TT   [SANS FETCH]")
print("="*72)
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kap = sp.symbols('kappa', positive=True)
kvec = [k1, k2, k3]; r2k = k1**2 + k2**2 + k3**2; kmag = sp.sqrt(r2k)
sub0 = {k1: 0, k2: 0, k3: kap}

def KD(i, j): return 1 if i == j else 0
def pit(i, j): return KD(i, j) - kvec[i]*kvec[j]/r2k
def PiTT(i, j, k, l):
    return (sp.Rational(1, 2)*(pit(i, k)*pit(j, l) + pit(i, l)*pit(j, k))
            - sp.Rational(1, d-1)*pit(i, j)*pit(k, l))

# (S2) sanity SANS fetch : trace projecteur TT = (d-2)(d+1)/2 = 2 ; idempotence sur eps
trace = sp.simplify(sum(PiTT(i, j, i, j) for i in range(3) for j in range(3)))
assert trace == 2, "projecteur TT : trace != 2"
eps = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
proj_eps = sp.Matrix(3, 3, lambda i, j: sp.simplify(
    sum(PiTT(i, j, k, l).subs(sub0)*eps[k, l] for k in range(3) for l in range(3))))
assert proj_eps == eps, "projecteur TT non idempotent sur eps"
epsdoteps = sum(eps[i, j]**2 for i in range(3) for j in range(3))   # = 2
print(f"  [S2] trace PiTT = {trace} (cible 2) ; PiTT.eps=eps : {proj_eps==eps} ; eps:eps = {epsdoteps}")

# (S1) sanity SANS fetch : FT scalaire d=3 (Delta=3) = pi^2/12
def Fs(Delta):
    return sp.pi**sp.Rational(d, 2)*2**(d-2*Delta)*sp.gamma(sp.Rational(d, 2)-Delta)/sp.gamma(Delta)
Fs3 = sp.simplify(Fs(3))
assert sp.simplify(Fs3 - sp.pi**2/12) == 0, "FT scalaire d=3 != pi^2/12"
print(f"  [S1] FT scalaire Fs(3) = {sp.nsimplify(Fs3)} (cible pi^2/12)")

# FT tensoriel : structure OP contractee eps:eps (eps TT => -1/d term s'annule) :
#   eps:eps: I_ik I_jl = 2 - 4(x1^2+x2^2)/r^2 + 4(x1^2-x2^2)^2/r^4   (puis /r^6)
def ft_monomial(powers, sigma):
    expr = Fs(sigma)*kmag**(2*sigma-d)
    for axis, p in enumerate(powers):
        for _ in range(p):
            expr = sp.diff(expr, kvec[axis])
    return sp.simplify((((-sp.I)**sum(powers))*expr).subs(sub0))
T1 = 2*ft_monomial((0, 0, 0), 3)
T2 = -4*(ft_monomial((2, 0, 0), 4) + ft_monomial((0, 2, 0), 4))
T3 = 4*(ft_monomial((4, 0, 0), 5) - 2*ft_monomial((2, 2, 0), 5) + ft_monomial((0, 4, 0), 5))
coeff_k3 = sp.nsimplify(sp.simplify((T1+T2+T3)/kap**3))
N_FT = sp.nsimplify(sp.simplify(coeff_k3/epsdoteps))   # C_T^mom = N_FT * C_T^OP
print(f"  eps:FT[I/x^6]:eps = ({coeff_k3}) kappa^3   =>   N_FT = {N_FT}  ~ {float(N_FT):.6f}")

# N_action : facteur du dictionnaire programme <-> Osborn-Petkos.
#   P2.3 l'argumentait =1 (action FG partagee) MAIS le flagguait 'a confirmer par le sceau'.
#   On le laisse SYMBOLIQUE : le sceau ne le pose pas, il le RESOUT par le test.
N_action = sp.symbols('N_action', positive=True)
N_cin = N_FT*N_action
print(f"  N_cin = N_FT * N_action = {N_FT} * N_action   (N_action = dictionnaire prog<->OP, NON pose)")

# CRITERE FIGE (avant fetch) : prediction = 1/(32 pi) en normalisation <TT> du programme
target = sp.Rational(1, 32)/sp.pi
print(f"\n  CRITERE FIGE P1 : kappa_3^normalise =?= 1/(32 pi) = {sp.nsimplify(target)} (slack nul)")

# ======================================================================
# [A]  VALEUR dHSS  (fetch aveugle, INSEREE MECANIQUEMENT — critere [B] deja fige)
# ======================================================================
print("\n" + "="*72)
print(" [A] valeur dHSS C_T^AdS = kappa_3 ell^2/G  (AdS4/CFT3, gravite d'Einstein)")
print("="*72)
# Sourcee (P4, recoupee) en convention Osborn-Petkos <TT>=(C_T/x^{2d}) I_{ij,kl},
# I = 1/2(II+II) - (1/d) delta delta  (= P2.1, IDENTIQUE) :
#   Bueno-Myers-Witczak-Krempa, arXiv:1505.07842 eq (3.47) : C_{T,E} = (3/pi^3) L^2/G  (d=3)
#   formule gen. arXiv:2202.10473 (4.9) / 1912.07035 (9.6) : Gamma(d+2)/(8 pi^{(d+2)/2}(d-1)Gamma(d/2)) L^{d-1}/G  -> 3/pi^3 en d=3
#   Larsen-Strominger arXiv:1405.1762 : meme structure I (d=3, -1/3 delta delta)
kappa3_dHSS = sp.Rational(3, 1)/sp.pi**3       # = 3/pi^3, convention POSITION/Osborn-Petkos
branche = "POSITION / Osborn-Petkos"           # P2.7 : format reporte = C_T^OP position-espace
print(f"  kappa_3^dHSS = {sp.nsimplify(kappa3_dHSS)}  ~ {float(kappa3_dHSS):.6f}   [branche : {branche}]")
print(f"  => branche P2.7 = POSITION/OP  ==>  N_cin = N_FT * N_action  (FT tensoriel actif)")

# ======================================================================
# [C]  TEST CENTRAL
# ======================================================================
print("\n" + "="*72)
print(" [C] test : N_cin * kappa_3^dHSS =?= 1/(32 pi)")
print("="*72)
lhs = sp.nsimplify(sp.simplify(N_cin*kappa3_dHSS))            # = N_FT*N_action*3/pi^3
print(f"  N_cin * kappa_3 = {lhs}")
# resoudre N_action requis pour PASS :
N_action_req = sp.nsimplify(sp.solve(sp.Eq(N_FT*N_action*kappa3_dHSS, target), N_action)[0])
print(f"  PASS exigerait  N_action = {N_action_req}  ~ {float(N_action_req):.6f}")
# sous l'hypothese naive N_action = 1 :
lhs_naive = sp.nsimplify(sp.simplify((N_cin*kappa3_dHSS).subs(N_action, 1)))
ecart = sp.nsimplify(sp.simplify(lhs_naive/target))
print(f"  sous N_action=1 :  N_cin*kappa_3 = {lhs_naive} ~ {float(lhs_naive):.6f}  (cible {sp.nsimplify(target)} ~ {float(target):.6f})")
print(f"                     ECART = (valeur/cible) = {ecart}   [facteur PUR]")
passe_naif = sp.simplify(lhs_naive - target) == 0
print(f"  PASS sous N_action=1 ? {passe_naif}")

# ======================================================================
# [D]  FIREWALL  (kappa_3 faux doit CHANGER le verdict => non tautologique)
# ======================================================================
print("\n" + "="*72)
print(" [D] firewall : sensibilite du test a kappa_3")
print("="*72)
lhs_x2 = sp.nsimplify(sp.simplify((N_FT*2*kappa3_dHSS)))      # kappa_3 -> 2 kappa_3
print(f"  kappa_3 -> 2 kappa_3 : N_FT*kappa_3 = {sp.nsimplify(N_FT*kappa3_dHSS)} -> {lhs_x2}  (change : {sp.simplify(lhs_x2 - N_FT*kappa3_dHSS)!=0})")
# mauvaise puissance de ell : C_T^AdS ~ kappa_3 ell^3/G (au lieu de ell^2) casse la dimension
ell, G = sp.symbols('ell G', positive=True)
CT_bon = kappa3_dHSS*ell**2/G
CT_faux = kappa3_dHSS*ell**3/G
N_loc = sp.symbols('N_loc', positive=True)   # N = pi ell^2/G (identification P3)
rap_bon = sp.simplify(CT_bon/(sp.pi*ell**2/G))     # = C_T/N, sans ell,G
rap_faux = sp.simplify(CT_faux/(sp.pi*ell**2/G))   # garde ell => dimensionnellement casse
print(f"  C_T/N (puissance ell^2, correcte) = {sp.nsimplify(rap_bon)} (pur, sans ell,G)")
print(f"  C_T/N (puissance ell^3, FAUSSE)   = {sp.nsimplify(rap_faux)} (contient ell => casse)")
assert rap_faux.free_symbols, "firewall : la mauvaise puissance de ell devrait laisser ell"
assert not rap_bon.free_symbols, "le rapport correct devrait etre pur"
print("  => test DISCRIMINANT : depend de la valeur ET de la structure de kappa_3 (non tautologique).")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-"*72)
print(" VERDICT (LC-AUDIT-VERDICT 6.4 — sans surclassement)")
print("-"*72)
print(f"""
  [B] CINEMATIQUE [etabli, algebre, sans fetch] : N_FT = pi^2/24 (FT OP->impulsion-TT,
      sanity-checks S1=pi^2/12, S2=projecteur trace 2 idempotent). SOLIDE.
  [A] VALEUR dHSS [sourcee, recoupee] : kappa_3 = 3/pi^3 (Osborn-Petkos, AdS4/CFT3,
      Einstein) — 3 sources concordantes ; convention I IDENTIQUE a P2.1.
  [C] TEST : sous N_action=1, N_cin*kappa_3 = 1/(8 pi) ; cible 1/(32 pi) ;
      ECART = facteur PUR 4 (= 2^2). N_action=1 est donc REFUTE.
      La cinematique fait passer l'ecart brut de 96/pi^2 (~9.73, branche N=1)
      a un facteur PUR 4 (branche OP+FT) : le CADRE est bon ; le residu est une
      CONVENTION, pas un nombre physique irrationnel.
  [D] FIREWALL : test discriminant (sensible a valeur + puissance de ell).

  ==> R1 NE CLOT PAS en convergence propre, et N'EST PAS un NO-GO net.
      R1 REDUIT la question de convergence a UN facteur defini et calculable :
      le dictionnaire programme<->Osborn-Petkos N_action (relation <T>=(d/16piG)g_(d)
      + comptage de polarisation du graviton), qui doit valoir EXACTEMENT 1/4 pour PASS.
      Ce facteur a ete DIFFERE en P2.3 (flague 'a confirmer'). Verdict :
        - N_action = 1/4  ==>  CONVERGENCE (etabli, algebre, coherence de coefficients) ;
        - N_action = 1    ==>  NO-GO net (facteur 4 physique) ;
        - actuellement : DECISION OUVERTE (non resolu sans deriver N_action).
      AUCUN rattrapage par convention applique (le facteur 4 N'EST PAS pose a 1/4).

  SANS SURCLASSEMENT : aucune affirmation 'D1 ferme / N fixe / CCC demontree'.
  Compte {{A4 ; A2* ; N}} INCHANGE.
""")
print("Sceau R1 : asserts [B] (S1,S2) + [D] passent. Test [C] = DECISION OUVERTE (facteur 4).")
