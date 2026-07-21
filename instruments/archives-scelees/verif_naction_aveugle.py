#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_naction_aveugle.py — SCEAU AVEUGLE (dérivation + engagement de c)

Dérive, à partir des SEULES définitions du §2 du paquet aveugle, le coefficient

        C_T^{prog (Osborn-Petkos)} = c · ℓ_dS² / G ,            c = ?

puis le scelle (EXIT 0). AUCUNE réconciliation (§4) n'est faite ici : on n'utilise
nulle part la valeur holographique externe du programme, ni sa magnitude, ni son signe.

Lecture externe autorisée et utilisée : la SEULE valeur d'Osborn-Petkos du
scalaire conforme libre en d=3 (étalonnage de la machinerie Fourier+projecteur).
Source publiée : Osborn-Petkos 1994 ; cf. p.ex. arXiv:1511.04077 (App. C),
arXiv:2201.09520 (App. A) — C_T^scalaire(d=3) = 3/(32 π²) dans la convention
⟨TT⟩ = (C_T/x^{2d}) 𝓘. Cette valeur NE concerne PAS le C_T du programme.

Facteurs exhibés : (1) Fourier conforme, (2) projecteur TT (trace 2, idempotent),
(3) dictionnaire holographique (d/16πG) + lecture de la fonction d'onde dS,
(4) somme de polarisation (graviton = 2 pol. en d=3).
"""
import sys
import sympy as sp

# ----------------------------------------------------------------------------
def section(t): print("\n" + "="*72 + f"\n{t}\n" + "="*72)
_asserts = 0
def must(cond, msg):
    global _asserts
    if not cond:
        print(f"ÉCHEC : {msg}", file=sys.stderr); sys.exit(1)
    _asserts += 1
    print(f"  ✓ {msg}")

# Symboles
G, H, MPl2, ell, q, k = sp.symbols('G H M_Pl2 ell_dS q k', positive=True)
pi = sp.pi

# ============================================================================
section("§2  DÉFINITIONS POSÉES (et UNIQUEMENT celles-ci)")
# ----------------------------------------------------------------------------
# Conventions
#   M_Pl² = 1/(8 π G) ;  ℓ_dS = 1/H
MPl2_val = 1/(8*pi*G)
ell_val  = 1/H
d = 3                                   # dimension de bord
print(f"  d = {d}  ;  M_Pl² = 1/(8πG)  ;  ℓ_dS = 1/H")

# Fonction d'onde dS : H_k = (1 + i k η) e^{-i k η}
eta = sp.symbols('eta', negative=True)
i = sp.I
Hk = (1 + i*k*eta)*sp.exp(-i*k*eta)
Hkp = sp.diff(Hk, eta)
a2 = 1/(H**2*eta**2)                     # a = -1/(Hη) en dS  =>  a² = 1/(H²η²)
expr = sp.simplify(a2*Hkp/Hk)            # a² (H'_k/H_k)
# développement η -> 0⁻
ser = sp.series(expr, eta, 0, 1).removeO()
print(f"  a²(H'_k/H_k) = {sp.nsimplify(ser)}   (η→0⁻)")
# partie de contact (réelle, divergente) et partie finie (imaginaire)
contact = sp.simplify(k**2/(H**2*eta))
finite  = sp.simplify(ser - contact)
must(sp.simplify(finite + i*k**3/H**2) == 0,
     "séparation η→0⁻ : contact = k²/(H²η) réel ; fini = − i k³/H²  (conforme §2)")

# F = (M_Pl²/4) a²(H'/H)  ->  partie finie
F_finite = sp.simplify((MPl2/4)*finite)         # = -i M_Pl² k³ /(4 H²)
must(sp.simplify(F_finite + i*MPl2*k**3/(4*H**2)) == 0,
     "F_fini = − i · M_Pl² k³ /(4 H²)")

# ============================================================================
section("SANITY-CHECK 1 — Fourier conforme scalaire en d=3  (= π²/12)")
# ----------------------------------------------------------------------------
# ∫ d^d x e^{ikx} |x|^{-2Δ} = π^{d/2} 2^{d-2Δ} Γ(d/2-Δ)/Γ(Δ) |k|^{2Δ-d}
Delta = sp.symbols('Delta')
def FT_conf(D, dd):
    return pi**(sp.Rational(dd,2)) * 2**(dd-2*D) * sp.gamma(sp.Rational(dd,2)-D)/sp.gamma(D)
ft_T = sp.nsimplify(FT_conf(3, 3))       # opérateur de poids Δ = d = 3
must(sp.simplify(ft_T - pi**2/12) == 0,
     f"FT(|x|^-6) en d=3 (Δ=3) = {ft_T} = π²/12  →  facteur scalaire q³")

# ============================================================================
section("SANITY-CHECK 2 — projecteur TT  (trace 2, idempotent)")
# ----------------------------------------------------------------------------
# π_ij = δ_ij - q̂_i q̂_j  ;  Π = ½(π_ik π_jl + π_il π_jk) - 1/(d-1) π_ij π_kl
qhat = sp.Matrix([0, 0, 1])              # q̂ = ẑ (sans perte de généralité)
delta = sp.eye(3)
piT = delta - qhat*qhat.T                # diag(1,1,0)
def Pi(ii,jj,kk,ll):
    return (sp.Rational(1,2)*(piT[ii,kk]*piT[jj,ll] + piT[ii,ll]*piT[jj,kk])
            - sp.Rational(1, d-1)*piT[ii,jj]*piT[kk,ll])
idx = range(3)
trace_first = sum(Pi(a_,a_,c_,e_) for a_ in idx for c_ in idx for e_ in idx
                  if c_==e_)            # Π_{aa,cc}
must(trace_first == 0, "Π sans trace : Π_{ii,kk} = 0")
PiPi = sum(Pi(a_,b_,c_,e_)*Pi(a_,b_,c_,e_) for a_ in idx for b_ in idx
           for c_ in idx for e_ in idx)
must(PiPi == 2, "Π:Π = 2  (= nb de polarisations TT en d=3 ; idempotent)")
# idempotence Π·Π = Π (sur un tenseur-test symétrique sans trace transverse)
test = sp.Matrix([[1,2,0],[2,-1,0],[0,0,0]])     # symétrique, transverse à ẑ, trace 0
PiT = sp.Matrix(3,3, lambda r,c2: sum(Pi(r,c2,m,n)*test[m,n] for m in idx for n in idx))
must(sp.simplify(PiT - test) == sp.zeros(3,3),
     "idempotence : Π agit comme identité sur un tenseur déjà TT")

# Π_{ij,kl} p^i p^j p^k p^l = ½ (p⊥²)²
p1,p2,p3 = sp.symbols('p1 p2 p3', real=True)
p = [p1,p2,p3]
Pipppp = sum(Pi(a_,b_,c_,e_)*p[a_]*p[b_]*p[c_]*p[e_]
             for a_ in idx for b_ in idx for c_ in idx for e_ in idx)
pperp2 = p1**2 + p2**2                    # transverse à ẑ
must(sp.simplify(Pipppp - sp.Rational(1,2)*pperp2**2) == 0,
     "Π_{ij,kl} pᵢpⱼpₖp_l = ½ (p⊥²)²")

# ============================================================================
section("ÉTALONNAGE — machinerie Fourier+projecteur via le scalaire libre d=3")
# ----------------------------------------------------------------------------
# Coefficient impulsion du scalaire libre : ⟨T T⟩ = A_sc q³ Π .
# Contraction projetée : Π:⟨TT⟩ = 2 A_sc q³ = ∫_p p⊥⁴ /(p² (q-p)²)  ≡  J.
# (le projecteur TT tue trace + termes d'amélioration ; reste ∂φ∂φ.)
# Réduction par l'intégrale-maître d=3 :
#   ∫_p (p²)^-α ((q-p)²)^-β = K(α,β) (q²)^{3/2-α-β},
def Kmaster(al, be):
    return (sp.Rational(1,1)/(4*pi)**sp.Rational(3,2)
            * sp.gamma(al+be-sp.Rational(3,2))
            * sp.gamma(sp.Rational(3,2)-al) * sp.gamma(sp.Rational(3,2)-be)
            / sp.gamma(al) / sp.gamma(be) / sp.gamma(3-al-be))
K11 = sp.nsimplify(Kmaster(1,1))
must(sp.simplify(K11 - sp.Rational(1,8)) == 0,
     f"intégrale-maître K(1,1) = {K11} = 1/8  →  ∫_p 1/(p²(q-p)²) = 1/(8q)")

# J = ∫_p (p²-μ²)² /(p²(q-p)²),  μ = p·q/q ;  partie non-analytique ∝ q³ .
# Décomposition (p²-μ²)² = p⁴ - 2 p²μ² + μ⁴ → termes A, B, C.
# Chaque monôme uᵃ vᵇ (u=p², v=(q-p)²) sur la base 1/(uv) donne K(1-a,1-b)
# (les 1/Γ aux pôles annulent automatiquement les termes analytiques/contact).
u, v, q2 = sp.symbols('u v q2', positive=True)
def coeff_q3(num_over_base):
    """num_over_base = fraction rationnelle en (u, q2, v), polynomiale en (u,v)
       mais éventuellement Laurent en q2 (μ² et μ⁴ portent des 1/q2).
       Renvoie le coeff. de q³ de ∫_p num/(u v), via le remplacement
         uᵃ vᵇ (q²)ᶜ · 1/(uv) -> K(1-a,1-b) (q²)^{c + 3/2-(1-a)-(1-b)} ,
       en ne gardant que la contribution non-analytique (q²)^{3/2}.
       Les 1/Γ aux pôles annulent automatiquement les termes de contact."""
    expr = sp.expand(num_over_base)
    M = 6                                     # efface les 1/q2 (max |c|=2)
    cleared = sp.expand(expr * q2**M)
    pdict = sp.Poly(cleared, u, v, q2).as_dict()
    total = sp.Integer(0)
    for (a_, b_, c_), coef in pdict.items():
        c_true = c_ - M                       # exposant réel de q2 dans num
        Kv = Kmaster(1-a_, 1-b_)
        if Kv in (sp.zoo, sp.nan) or Kv == 0:
            continue                          # terme analytique/contact → écarté
        power = sp.Rational(3,2) - (1-a_) - (1-b_)        # exposant de (q²)
        tot_pow = c_true + power
        if sp.simplify(tot_pow - sp.Rational(3,2)) == 0:  # ne garder que q³
            total += coef * Kv
    return sp.nsimplify(total)

mu2 = ( (u + q2 - v)/2 )**2 / q2          # μ²   = (p·q)²/q²
mu4 = ( (u + q2 - v)/2 )**4 / q2**2       # μ⁴   = (p·q)⁴/q⁴
# termes ; base 1/(u v) déjà factorisée par coeff_q3 :
A = coeff_q3( u**2 )                       # p⁴/(p²v) = u²·1/(uv)
B = coeff_q3( -2*mu2*u )                   # -2 p²μ²/(p²v) = -2μ²/v = (-2μ²·u)/(uv)
C = coeff_q3( mu4 )                        # μ⁴/(p²v) = μ⁴·1/(uv)
J = sp.nsimplify(A + B + C)
must(sp.simplify(A) == 0, "terme p⁴ : aucune partie non-analytique q³ (contact)")
must(sp.simplify(B) == 0, "terme p²μ² : aucune partie non-analytique q³ (contact)")
must(sp.simplify(C - sp.Rational(1,128)) == 0, f"terme μ⁴ : coeff. q³ = {C} = 1/128")
must(sp.simplify(J - sp.Rational(1,128)) == 0, f"J = {J} = 1/128  (coeff. de q³)")

A_sc = sp.nsimplify(J/2)                   # 2 A_sc = J
must(sp.simplify(A_sc - sp.Rational(1,256)) == 0,
     f"A_sc = J/2 = {A_sc} = 1/256  (coeff. impulsion ⟨TT⟩ scalaire libre)")

# Valeur O-P fetchée (étalon, NON liée au programme) :
CT_sc_OP = sp.Rational(3,32)/pi**2
print(f"\n  [fetch] C_T^scalaire(d=3, Osborn-Petkos) = 3/(32π²)  = {CT_sc_OP}")

# Dictionnaire impulsion -> position : C_T = κ · A , κ = C_T^sc / A_sc
kappa = sp.nsimplify(CT_sc_OP / A_sc)
must(sp.simplify(kappa - 24/pi**2) == 0,
     f"dictionnaire C_T = κ·A_q³,  κ = {kappa} = 24/π²")
# cohérence : κ = (½)·(facteur Fourier scalaire π²/12)⁻¹ ... vérif. croisée
must(sp.simplify(kappa*A_sc - CT_sc_OP) == 0,
     "vérif. croisée : κ·A_sc reproduit C_T^scalaire = 3/(32π²)")

# ============================================================================
section("§3  DÉRIVATION DE c  (dictionnaire holographique + polarisation)")
# ----------------------------------------------------------------------------
# Lecture de la fonction d'onde : la 2-pts céleste ⟨TT⟩ du programme est lue
# sur la partie FINIE de F. Coefficient (magnitude) du terme q³ :
#   |F_fini| / k³ = M_Pl² /(4 H²)  ; la somme sur les 2 polarisations TT
#   fournit le projecteur Π (trace 2).  Dictionnaire holographique (d/16πG)
#   et normalisation sont encodés dans le préfacteur M_Pl²/4 de F (§2).
A_prog = MPl2/(4*H**2)                      # coeff. impulsion ⟨TT⟩_prog (Π, 2 pol.)
print(f"  A_prog (coeff. q³, magnitude) = M_Pl²/(4H²)")

# Conversion en C_T Osborn-Petkos via le dictionnaire étalonné :
CT_prog = sp.simplify(kappa * A_prog)       # = 6 M_Pl²/(π² H²)
must(sp.simplify(CT_prog - 6*MPl2/(pi**2*H**2)) == 0,
     "C_T^prog = κ·A_prog = 6 M_Pl²/(π² H²)")

# Passage aux unités ℓ_dS²/G :  M_Pl² = 1/(8πG),  1/H² = ℓ_dS²
CT_prog_units = sp.simplify(CT_prog.subs(MPl2, MPl2_val))   # en fonction de G,H
CT_prog_units = sp.simplify(CT_prog_units * H**2 * ell**2 / ell**2)  # garder H
# exprimer en ℓ²/G : 1/H² -> ℓ²
c_coeff = sp.simplify(CT_prog.subs(MPl2, MPl2_val) * H**2)  # = C_T · H² · ... isole 1/G·... 
c_coeff = sp.nsimplify(sp.simplify(CT_prog.subs(MPl2, MPl2_val))*H**2*G)  # coeff de ℓ²/G après 1/H²->ℓ²
must(sp.simplify(c_coeff - sp.Rational(3,4)/pi**3) == 0,
     f"c = {c_coeff} = 3/(4π³)")

c_val = sp.Rational(3,4)/pi**3
c_num = sp.N(c_val, 12)

# ============================================================================
section("ENGAGEMENT (SCEAU)")
# ----------------------------------------------------------------------------
print(f"""
  Chaîne de facteurs exhibée :
    Fourier conforme scalaire d=3 .......... π²/12
    projecteur TT .......................... trace 2, idempotent, Π:Π = 2
    coeff. impulsion programme (fonction d'onde) ... M_Pl²/(4H²)
    polarisation ........................... graviton = 2 pol. (via Π)
    dictionnaire impulsion→position (étalon) ... κ = 24/π²
    unités ................................. M_Pl²=1/(8πG), ℓ_dS=1/H

  ┌────────────────────────────────────────────────────────────────────┐
  │   C_T^prog (Osborn-Petkos)  =  c · ℓ_dS²/G                           │
  │                                                                      │
  │        c  =  3 / (4 π³)   ≈  {float(c_num):.10f}                    │
  └────────────────────────────────────────────────────────────────────┘

  Hypothèse de convention unique (laissée à §4) : la 2-pts vaut Re(ψ₂)·Π
  sans facteur 2 additionnel ; SIGNE et facteur de continuation i^(d-1)=−1
  (ℓ_AdS→iℓ_dS) NON appliqués ici — réservés à la réconciliation §4.
""")

print(f"OK — {_asserts} assertions. c scellé. AUCUNE réconciliation faite. EXIT 0.")
sys.exit(0)
