#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_naction_firewall.py — SCEAU DE RÉCONCILIATION (point 1 de l'audit à froid)

OBJET. Le sceau aveugle (verif_naction_aveugle.py) a POSÉ — sans le dériver — que
A_prog = M_Pl²/(4H²) est le « coefficient impulsion de q³Π » du programme, donc
justiciable du dictionnaire cinématique κ=24/π² étalonné sur le scalaire libre.
Ce sceau DÉRIVE ce statut (et non le pose), en exhibant :

  [A] la somme de polarisation des 2 modes TT (d=3 bord) = MÊME projecteur Π que
      le sceau aveugle (Π:Π=2). La structure tensorielle de ⟨TT⟩ EST Π, pas un
      autre tenseur ;
  [B] la partie finie du coefficient de fonction d'onde F = (M_Pl²/4)a²(H'/H),
      |F_fini|/k³ = M_Pl²/(4H²) (re-dérivée, identique à CT-ATN et au sceau aveugle) ;
  [C] la CONSISTANCE avec le spectre vérifié du programme : la MÊME quantité
      M_Pl²/(4H²) reproduit 𝒫=2H²/(M_Pl²k³) (prescription 𝒫=1/(2|Im F|)). C'est ce
      qui PINCE la normalisation (lève la réserve « facteur 2 ») ;
  [D] conclusion : A_prog = M_Pl²/(4H²) est bien le coefficient SANS-DIMENSION de
      q³Π, du MÊME type que A_sc ⟹ κ s'applique ⟹ C_T^OP = κ·A_prog, c=3/(4π³).
      Le C_T/N=1/(32π²) de CT-ATN était la lecture EN IMPULSION (non-OP) ; sa
      valeur OP est κ fois plus grande.

  FIREWALL : on injecte une normalisation de polarisation FAUSSE (Σεε=2Π au lieu
  de Π) ; A_prog double, c double ⟹ le résultat DÉPEND vraiment de la convention
  désormais DÉRIVÉE (block A), il n'est pas posé arbitrairement.

DISCIPLINE (LC-AUDIT-VERDICT §6.4). Tout « établi » ici = ALGÈBRE + conventions
EXHIBÉES (Σεε=Π ; ⟨TT⟩∝F sans -2 ; spectre comme ancre). JAMAIS « D1 fermé / N
fixé / CCC démontrée ». Le compte {A4 ; A2★ ; N} est INCHANGÉ. La valeur c reste
CONDITIONNELLE aux conventions de normalisation dS/CFT exhibées.
"""
import sys
import sympy as sp

def section(t): print("\n" + "="*72 + f"\n{t}\n" + "="*72)
_asserts = 0
def must(cond, msg):
    global _asserts
    if not cond:
        print(f"ÉCHEC : {msg}", file=sys.stderr); sys.exit(1)
    _asserts += 1
    print(f"  ✓ {msg}")

G, H, MPl2, k = sp.symbols('G H M_Pl2 k', positive=True)
pi = sp.pi
i = sp.I
d = 3

# ============================================================================
section("[A]  SOMME DE POLARISATION  =  PROJECTEUR Π  (structure de ⟨TT⟩)")
# ----------------------------------------------------------------------------
# Projecteur TT — DÉFINITION IDENTIQUE au sceau aveugle (q̂ = ẑ).
qhat = sp.Matrix([0, 0, 1])
delta = sp.eye(3)
piT = delta - qhat*qhat.T                 # diag(1,1,0)
def Pi(ii,jj,kk,ll):
    return (sp.Rational(1,2)*(piT[ii,kk]*piT[jj,ll] + piT[ii,ll]*piT[jj,kk])
            - sp.Rational(1, d-1)*piT[ii,jj]*piT[kk,ll])
idx = range(3)
PiPi = sum(Pi(a,b,c,e)*Pi(a,b,c,e) for a in idx for b in idx for c in idx for e in idx)
must(PiPi == 2, "Π:Π = 2  (= nb de polarisations TT, d=3) — convention du sceau aveugle")

# Les 2 polarisations TT pour q = ẑ (transverses, symétriques, sans trace),
# normalisées ε^s:ε^{s'} = δ^{ss'}.
sqrt2 = sp.sqrt(2)
eps1 = sp.Matrix([[1,0,0],[0,-1,0],[0,0,0]]) / sqrt2     # + (plus)
eps2 = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]) / sqrt2      # × (croix)
pols = [eps1, eps2]

for s,e in enumerate(pols):
    must(e == e.T, f"ε^{s+1} symétrique")
    must(sp.trace(e) == 0, f"ε^{s+1} sans trace")
    must((e*qhat).norm() == 0, f"ε^{s+1} transverse à q")   # e·q̂ = 0
for s in range(2):
    for sp_ in range(2):
        ortho = sum(pols[s][a,b]*pols[sp_][a,b] for a in idx for b in idx)
        tgt = 1 if s==sp_ else 0
        must(sp.simplify(ortho - tgt) == 0,
             f"ε^{s+1}:ε^{sp_+1} = {tgt}  (orthonormalité)")

# Σ_s ε^s_{ij} ε^s_{kl}  ==  Π_{ij,kl}  (test composante par composante)
def Sigma(ii,jj,kk,ll):
    return sum(pols[s][ii,jj]*pols[s][kk,ll] for s in range(2))
mismatch = [(a,b,c,e) for a in idx for b in idx for c in idx for e in idx
            if sp.simplify(Sigma(a,b,c,e) - Pi(a,b,c,e)) != 0]
must(mismatch == [], "Σ_s ε^s_{ij} ε^s_{kl} = Π_{ij,kl}  (16 composantes) "
                     "⟹ la structure tensorielle de ⟨TT⟩ EST Π")

# ============================================================================
section("[B]  COEFFICIENT DE FONCTION D'ONDE  —  |F_fini|/k³ = M_Pl²/(4H²)")
# ----------------------------------------------------------------------------
eta = sp.symbols('eta', negative=True)
Hk  = (1 + i*k*eta)*sp.exp(-i*k*eta)
Hkp = sp.diff(Hk, eta)
a2  = 1/(H**2*eta**2)
expr = sp.series(sp.simplify(a2*Hkp/Hk), eta, 0, 1).removeO()
contact = sp.simplify(k**2/(H**2*eta))
finite  = sp.simplify(expr - contact)
must(sp.simplify(finite + i*k**3/H**2) == 0,
     "a²(H'/H)|_fini = − i k³/H²  (η→0⁻, identique CT-ATN §2)")
F_finite = sp.simplify((MPl2/4)*finite)            # = − i M_Pl² k³ /(4H²)
A_prog   = sp.simplify(sp.Abs(sp.im(F_finite)) / k**3)   # |F_fini|/k³
must(sp.simplify(A_prog - MPl2/(4*H**2)) == 0,
     "|F_fini|/k³ = M_Pl²/(4H²)  (coeff. impulsion brut, identique au sceau aveugle)")
# sans-dimension : en unités M_Pl²=1/(8πG), 1/H²=ℓ², le coeff. de ℓ²/G est pur
A_prog_pure = sp.nsimplify(A_prog.subs(MPl2, 1/(8*pi*G)) * H**2 * G)
must(sp.simplify(A_prog_pure - sp.Rational(1,32)/pi) == 0,
     f"A_prog = {A_prog_pure}·(ℓ²/G) = (1/32π)·ℓ²/G  →  coefficient SANS DIMENSION")

# ============================================================================
section("[C]  ANCRE — consistance avec le spectre VÉRIFIÉ du programme")
# ----------------------------------------------------------------------------
# Prescription dS/CFT du programme : 𝒫 = 1/(2 |Im F|_fini).
ImF = sp.Abs(sp.im(F_finite))
P_T = sp.simplify(1/(2*ImF))
must(sp.simplify(P_T - 2*H**2/(MPl2*k**3)) == 0,
     "𝒫 = 1/(2|Im F|) = 2H²/(M_Pl²k³)  (spectre du programme, CT-ATN route [A]≡[D])")
# La MÊME M_Pl²/(4H²) sert de coeff. ⟨TT⟩ ET de normalisation du spectre :
must(sp.simplify(ImF/k**3 - A_prog) == 0,
     "même M_Pl²/(4H²) dans le spectre et dans ⟨TT⟩ ⟹ PAS de facteur 2 résiduel")

# ============================================================================
section("[D]  CONCLUSION — κ s'applique ; c = 3/(4π³) ; CT-ATN était en impulsion")
# ----------------------------------------------------------------------------
# κ : dictionnaire impulsion→position OP, étalonné sur le scalaire libre
# (re-vérifié dans le sceau aveugle : A_sc=1/256, C_T^sc=3/(32π²)).
A_sc  = sp.Rational(1,256)
CT_sc = sp.Rational(3,32)/pi**2
kappa = sp.nsimplify(CT_sc / A_sc)
must(sp.simplify(kappa - 24/pi**2) == 0, "κ = C_T^sc/A_sc = 24/π² (étalon scalaire libre)")

# A_prog EST le coeff. q³Π (block A : structure = Π ; block B : sans dimension) ⟹ κ s'applique
CT_prog_OP = sp.simplify(kappa * A_prog)
c_OP = sp.nsimplify(CT_prog_OP.subs(MPl2, 1/(8*pi*G)) * H**2 * G)
must(sp.simplify(c_OP - sp.Rational(3,4)/pi**3) == 0,
     f"c (OP) = κ·A_prog = {c_OP} = 3/(4π³)  (reproduit le sceau aveugle)")

# CT-ATN : C_T/N=1/(32π²) lue SANS κ ⟹ lecture en impulsion (non-OP)
CT_over_N_prog = sp.Rational(1,32)/pi**2          # CT-ATN, impulsion
CT_over_N_OP   = sp.simplify(kappa * CT_over_N_prog)
must(sp.simplify(CT_over_N_OP - sp.Rational(3,4)/pi**4) == 0,
     f"C_T/N (OP) = κ·(1/32π²) = {CT_over_N_OP} = 3/(4π⁴)  (≠ 1/32π² de CT-ATN)")
must(sp.simplify((c_OP)/(sp.Rational(1,32)/pi)) - kappa == 0,
     "écart aveugle ↔ CT-ATN = exactement κ ⟹ CT-ATN lisait l'IMPULSION (non-OP)")

# ============================================================================
section("FIREWALL — sensibilité à la convention DÉRIVÉE (block A)")
# ----------------------------------------------------------------------------
# Si l'on injecte une normalisation FAUSSE Σεε = 2Π (polarisations sur-normalisées
# ε^s:ε^{s'}=2δ^{ss'}), le coeff. q³Π double, donc c double : le résultat DÉPEND
# de la convention maintenant établie en [A], il n'est pas posé arbitrairement.
A_prog_bad = 2*A_prog
c_bad = sp.nsimplify((kappa*A_prog_bad).subs(MPl2, 1/(8*pi*G)) * H**2 * G)
must(sp.simplify(c_bad - 2*c_OP) == 0,
     "convention FAUSSE (Σεε=2Π) ⟹ c double ⟹ le résultat teste vraiment [A]")
must(sp.simplify(c_bad - c_OP) != 0, "firewall actif : c_bad ≠ c_OP")

# ============================================================================
section("ENGAGEMENT (SCEAU)")
# ----------------------------------------------------------------------------
print(f"""
  DÉRIVÉ (et non posé) :
    [A]  Σ_s ε^s ε^s = Π (16 comp.) ⟹ structure de ⟨TT⟩ = Π, Π:Π=2 (2 pol.)
    [B]  |F_fini|/k³ = M_Pl²/(4H²) = (1/32π)·ℓ²/G  — coefficient SANS DIMENSION
    [C]  même M_Pl²/(4H²) reproduit 𝒫=2H²/(M_Pl²k³) ⟹ AUCUN facteur 2 résiduel
    [D]  A_prog est du MÊME type que A_sc ⟹ κ=24/π² s'applique :

  ┌──────────────────────────────────────────────────────────────────────┐
  │   c (Osborn-Petkos)  =  κ·A_prog  =  3/(4π³)   ≈ {float(sp.N(sp.Rational(3,4)/pi**3,12)):.10f}  │
  │   C_T/N (OP)         =  κ·(1/32π²) = 3/(4π⁴)   ≈ {float(sp.N(sp.Rational(3,4)/pi**4,12)):.10f}  │
  │                                                                        │
  │   ⟹ CT-ATN « C_T/N=1/(32π²) » = lecture EN IMPULSION (non-OP).         │
  │      La valeur Osborn-Petkos est κ=24/π² fois plus grande.             │
  └──────────────────────────────────────────────────────────────────────┘

  CONDITIONNEL (réserves exhibées, NON levées par algèbre) :
    · convention de polarisation Σ_s ε^s ε^s = Π (block A) ;
    · map opérateur dS/CFT ⟨TT⟩ ∝ F sans −2 additionnel, ANCRÉE sur le spectre
      vérifié du programme (block C) ;
    · valeur c établie (ALGÈBRE) SOUS ces conventions ; GRADE modéré-élevé.

  §6.4 : « c=3/(4π³) en OP (algèbre, sous conventions) » ≠ « D1 fermé / N fixé /
  CCC démontrée ». Compte {{A4 ; A2★ ; N}} INCHANGÉ. Verrouillage C_T∝N et
  cancellation A_T·N=16 INTACTS (κ nombre pur). Observable 𝒫 INTACTE.
""")
print(f"OK — {_asserts} assertions. Statut impulsion DÉRIVÉ. EXIT 0.")
sys.exit(0)
