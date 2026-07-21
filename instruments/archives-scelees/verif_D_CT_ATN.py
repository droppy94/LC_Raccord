#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_CT_ATN.py — LC-RACCORD. Sceau du cadrage LC-WORK-CT-CADRAGE (chantier différé
M1 de LC-WORK-REPRISE-POST-D1-E). Teste le FINDING A_T·N = 16 par DEUX routes
indépendantes qui doivent CONVERGER, et identifie la charge centrale C_T ~ N.

Position. Le cadrage C_T a établi (tri des 4 mécanismes) que C_T n'est PAS libre :
holographiquement VERROUILLÉE à N (anomalie indisponible en d=3 impair ; unitarité borne
le signe ; normalisation conforme fixe la forme seule). Reste à VÉRIFIER que le candidat-
égalité A_T = 16/N (convention standard) tient — i.e. que la route dS/CFT reproduit
l'amplitude QFT standard.

Extension de :
    verif_E_planck.py       — N = S_dS = π/(G H^2) = (ℓ_dS/ℓ_P)^2 (entropie de de Sitter).
    verif_D3_spectre_k3.py  — forme <TT> ∝ k^3 (Δ=d=3) scellée ; A_T laissé décision ouverte.
    verif_D_g3.py           — dictionnaire <T> = (d/16πG) g3 ; d=3 impair (pas d'anomalie).

Blocs (= critère de réfutation §5 de LC-WORK-CT-CADRAGE) :
    [A] ROUTE CANONIQUE (QFT-sur-dS, symbolique). Mode tensoriel BD, variable canonique
        μ=(M_Pl/2)a h. Late-time |h_k|^2 = 2H^2/(M_Pl^2 k^3) par polarisation =>
        𝒫_T (2 pol) = (2/π^2)(H/M_Pl)^2 = A_T. Vérifie le coefficient 2/π^2.
    [B] ENTROPIE N (symbolique). N = S_dS = Aire/(4G) = π/(G H^2) = 8π^2 (M_Pl/H)^2.
    [C] PRODUIT & ROBUSTESSE (symbolique). A_T·N = 16 (M_Pl réduit) ; cancellation H,G
        (free_symbols vide) ; sensibilité de convention (convention lâche -> π). Robuste :
        A_T·N est un NOMBRE PUR ; la valeur (16) dépend de la convention, la cancellation non.
    [D] ROUTE HOLOGRAPHIQUE dS/CFT (le vrai test, symbolique). Mode bulk-to-boundary
        H_k=(1+ikη)e^{-ikη}, H_k(0)=1. Coefficient de fonction d'onde
        F=(M_Pl^2/4) a^2 (H'/H), développé en η->0 :
            a^2 (H'/H) = k^2/(H^2 η)  [réel, divergent : CONTACT/PHASE]
                         - i k^3/H^2  [fini : PHYSIQUE].
        Prescription dS/CFT (Maldacena) : 𝒫 = 1/(2|Im F|_fini) => ⟨|h|^2⟩ = 2H^2/(M_Pl^2 k^3)
        = IDENTIQUE à [A]. Identification C_T ~ coeff de ⟨TT⟩∝C_T k^3 ~ M_Pl^2/H^2 ~ N
        (VERROUILLAGE). Deux nombres purs : A_T·N = 16 ET A_T·(coeff ⟨TT⟩) = 1/(2π^2).
        Le terme divergent RÉEL = phase (drop de |Ψ|^2) = la signature « C_T imaginaire »
        non-unitaire de dS/CFT [À INVENTER : valeur/réalité exacte de C_T].

Cibles (LC-WORK-CT-CADRAGE, papier ; ce sceau doit les reproduire) :
    amplitude            A_T = (2/π^2)(H/M_Pl)^2 = 16 G H^2 / π   (M_Pl^2 = 1/(8πG))
    entropie             N = S_dS = π/(G H^2) = 8π^2 (M_Pl/H)^2
    produit              A_T·N = 16            (nombre pur ; cancellation H,G)
    convention lâche     A_T·N = π             (M_P^2=1/G, A_T≡(H/M_P)^2 sans préfacteur)
    convergence routes   [A] et [D] donnent le MÊME ⟨|h|^2⟩ = 2H^2/(M_Pl^2 k^3)
    verrouillage         coeff ⟨TT⟩ ∝ M_Pl^2/H^2 ∝ N  ;  A_T·(coeff ⟨TT⟩) = 1/(2π^2)
    signature dS/CFT     terme divergent RÉEL (phase) ; le 'i' du terme fini = non-unitarité

Dépendances : sympy. Re-exécutable, sans réseau.
Discipline (LC-AUDIT-VERDICT §6.4) : un `établi` de sceau = « l'algèbre est correcte ET
les cibles reproduites » ; JAMAIS « la physique de la CCC est établie ». Restent
décision ouverte / à inventer : la valeur/réalité exacte de C_T en dS (continuation,
non-unitarité) ; la survie de la relation au crossover CCC ; la fixation de N
(circularité LC-E, NON brisée). Ne ferme PAS D1.
"""

import sympy as sp


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


print("=" * 72)
print(" verif_D_CT_ATN.py — test dS/CFT du candidat-égalité A_T·N = 16, C_T ~ N")
print("=" * 72)

# Symboles communs.
eta, k, H, G, pi = sp.symbols('eta k H G pi', positive=True)
I = sp.I
MPl2 = 1 / (8 * pi * G)          # masse de Planck RÉDUITE : M_Pl^2 = 1/(8πG)

# ======================================================================
# [A] ROUTE CANONIQUE (QFT-sur-dS) : A_T = (2/π^2)(H/M_Pl)^2
# ======================================================================
banner("[A] ROUTE CANONIQUE  —  mode BD, μ=(M_Pl/2)a h  =>  A_T = (2/π^2)(H/M_Pl)^2")

a = -1 / (H * eta)                                   # facteur d'échelle dS, η ∈ (-∞,0)
# Mode canonique de Bunch-Davies pour μ (équation μ'' + (k^2 - a''/a)μ = 0, a''/a = 2/η^2) :
mu = (1 / sp.sqrt(2 * k)) * sp.exp(-I * k * eta) * (1 - I / (k * eta))
# Vérif EOM : a''/a = 2/η^2.
app_a = sp.simplify(sp.diff(a, eta, 2) / a)
assert sp.simplify(app_a - 2 / eta**2) == 0
EOM_mu = sp.simplify(sp.diff(mu, eta, 2) + (k**2 - app_a) * mu)
assert EOM_mu == 0
print("  a''/a =", app_a, " ; mode μ_BD vérifie μ'' + (k^2 - a''/a)μ = 0  [EOM =", EOM_mu, "]")

# h = 2μ/(M_Pl a). |h_k|^2 late-time (η->0).
MPl = sp.sqrt(MPl2)
h = 2 * mu / (MPl * a)
h2 = sp.simplify(sp.Abs(h)**2)
h2_lim = sp.simplify(sp.limit(h2, eta, 0, dir='-'))
print("  |h_k|^2 (η->0, par polarisation) =", h2_lim, "   (cible 2H^2/(M_Pl^2 k^3))")
assert sp.simplify(h2_lim - 2 * H**2 / (MPl2 * k**3)) == 0

# 𝒫_h = (k^3/2π^2)|h_k|^2 par pol ; ×2 polarisations.
P_per_pol = sp.simplify(k**3 / (2 * pi**2) * h2_lim)
A_T = sp.simplify(2 * P_per_pol)                     # 2 polarisations
print("  𝒫_h (par pol) =", P_per_pol, " ; A_T (2 pol) =", A_T)
A_T_target = sp.simplify(2 / pi**2 * H**2 / MPl2)
assert sp.simplify(A_T - A_T_target) == 0
print("  >>> A_T = (2/π^2)(H/M_Pl)^2 =", sp.simplify(A_T), "  [= 16 G H^2/π]")
assert sp.simplify(A_T - 16 * G * H**2 / pi) == 0

# ======================================================================
# [B] ENTROPIE N = S_dS = π/(G H^2) = 8π^2 (M_Pl/H)^2
# ======================================================================
banner("[B] ENTROPIE N  —  N = S_dS = Aire/(4G) = π/(G H^2)")

r_dS = 1 / H
Area = 4 * pi * r_dS**2
N = sp.simplify(Area / (4 * G))
print("  r_dS = 1/H ; Aire = 4π/H^2 ; N = S_dS =", N, "  (cible π/(G H^2))")
assert sp.simplify(N - pi / (G * H**2)) == 0
N_MPl = sp.simplify(N - 8 * pi**2 * MPl2 / H**2)
print("  N = 8π^2 (M_Pl/H)^2 ?  vérif =", N_MPl)
assert N_MPl == 0

# ======================================================================
# [C] PRODUIT & ROBUSTESSE : A_T·N = 16 ; cancellation H,G ; convention lâche -> π
# ======================================================================
banner("[C] PRODUIT  —  A_T·N = 16 (nombre pur ; cancellation H,G) ; lâche -> π")

prod = sp.simplify(A_T * N)
print("  A_T·N =", prod, "   (cible 16)")
assert prod == 16
print("  dépendance résiduelle (free_symbols) :", prod.free_symbols, "  (doit être vide)")
assert prod.free_symbols == set()

# Sensibilité de convention : M_P^2 = 1/G (NON réduit), A_T écrit lâchement = (H/M_P)^2.
A_T_loose = H**2 * G
prod_loose = sp.simplify(A_T_loose * N)
print("  convention lâche : A_T≡(H/M_P)^2, M_P^2=1/G  =>  A_T·N =", prod_loose, "  (cible π)")
assert sp.simplify(prod_loose - pi) == 0
print("  >>> la cancellation H,G est ROBUSTE (structurelle) ; le coefficient (16/π) ne l'est pas.")

# ======================================================================
# [D] ROUTE HOLOGRAPHIQUE dS/CFT (le vrai test) : convergence, C_T ~ N, signature i
# ======================================================================
banner("[D] ROUTE HOLOGRAPHIQUE dS/CFT  —  convergence [A]=[D], C_T ~ N, signature non-unitaire")

# (a) Mode bulk-to-boundary normalisé : H_k(η)=(1+ikη)e^{-ikη}, H_k(0)=1.
Hk = (1 + I * k * eta) * sp.exp(-I * k * eta)
EOM_H = sp.simplify(sp.diff(Hk, eta, 2) - (2 / eta) * sp.diff(Hk, eta) + k**2 * Hk)
assert EOM_H == 0 and sp.limit(Hk, eta, 0) == 1
print("  (a) mode bulk-to-boundary H_k=(1+ikη)e^{-ikη} : EOM =", EOM_H, " ; H_k(0) =",
      sp.limit(Hk, eta, 0))

# (b) Coefficient de fonction d'onde F = (M_Pl^2/4) a^2 (H'/H), développé en η->0.
a2 = a**2
ratio = sp.simplify(a2 * sp.diff(Hk, eta) / Hk)
laurent = sp.series(ratio, eta, 0, 1).removeO()
print("  (b) a^2 (H'/H) =", sp.series(ratio, eta, 0, 1))
div_term = sp.simplify(laurent.coeff(eta, -1))       # terme ∝ 1/η (divergent)
fin_term = sp.simplify(laurent.coeff(eta, 0))        # terme η^0 (fini)
print("      terme divergent (∝1/η) =", div_term, "   [RÉEL -> contact/phase]")
print("      terme fini (η^0)        =", fin_term, "   [le 'i' = signature dS/CFT]")
assert sp.simplify(div_term - k**2 / H**2) == 0       # réel
assert sp.simplify(fin_term - (-I * k**3 / H**2)) == 0  # imaginaire pur (le i explicite)

# (c) Prescription dS/CFT : 𝒫 = 1/(2 |Im F|_fini). F_fini = (M_Pl^2/4)·fin_term (imag. pur).
F_fin = sp.simplify(MPl2 / 4 * fin_term)             # = -i M_Pl^2 k^3/(4H^2)
ImF_abs = sp.simplify(MPl2 / 4 * sp.Abs(fin_term))   # |Im F|_fini = M_Pl^2 k^3/(4H^2)
hh_holo = sp.simplify(1 / (2 * ImF_abs))
print("  (c) F_fini =", F_fin, " ; |Im F|_fini =", ImF_abs)
print("      ⟨|h|^2⟩ = 1/(2|Im F|) =", hh_holo)
print("      route [A] donnait |h_k|^2 =", h2_lim)
assert sp.simplify(hh_holo - h2_lim) == 0
print("      >>> CONVERGENCE : routes canonique [A] et holographique [D] COÏNCIDENT.")

# (d) Identification C_T ~ coeff de ⟨TT⟩ ∝ C_T k^3 (réponse holographique ~ |Im F|-coeff).
#     coeff = M_Pl^2/(4H^2) ; C_T ∝ M_Pl^2/H^2 ∝ N (VERROUILLAGE). Nombres purs.
CT_coeff = sp.simplify(ImF_abs / k**3)               # = M_Pl^2/(4H^2)
print("\n  (d) coeff de ⟨TT⟩∝C_T k^3 (= |Im F|_fini/k^3) =", CT_coeff, "  (∝ M_Pl^2/H^2)")
ratio_CT_N = sp.simplify(CT_coeff / N)
print("      coeff/N =", ratio_CT_N, "  (constant ∝ 1/π^2 => C_T ∝ N : VERROUILLAGE)")
assert {H, G, k}.isdisjoint(ratio_CT_N.free_symbols)   # rapport sans H,G,k => C_T ∝ N
AT_CT = sp.simplify(A_T * CT_coeff)
print("      A_T·(coeff ⟨TT⟩) =", AT_CT, "   (cible 1/(2π^2)) — nombre pur")
assert sp.simplify(AT_CT - 1 / (2 * pi**2)) == 0
AT_N_holo = sp.simplify(A_T * N)
print("      A_T·N (via route holographique, cohérent [C]) =", AT_N_holo, "  (= 16)")
assert AT_N_holo == 16

# (e) Signature non-unitaire : le terme divergent est RÉEL (=> i·réel = phase, drop de |Ψ|^2)
#     et le terme fini porte un 'i' explicite. C'est la signature « C_T complexe » de dS/CFT.
print("\n  (e) divergent =", div_term, "(RÉEL) -> i·réel = PHASE, drop de |Ψ|^2 [contact local]")
print("      fini      =", fin_term, "(IMAGINAIRE) -> le 'i' = non-unitarité dS/CFT")
print("      => 'C_T imaginaire/négatif' (Strominger) : valeur/réalité exacte [À INVENTER].")
assert sp.im(div_term) == 0 and sp.re(fin_term) == 0  # divergent réel ; fini imaginaire pur

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-" * 72)
print(" VERDICT (établi : algèbre ; cibles reproduites) :")
print("   [A] CANONIQUE   : A_T = (2/π^2)(H/M_Pl)^2 = 16 G H^2/π  (mode BD, canonique).")
print("   [B] ENTROPIE    : N = S_dS = π/(G H^2) = 8π^2 (M_Pl/H)^2.")
print("   [C] PRODUIT     : A_T·N = 16 (nombre pur ; H,G se simplifient) ; lâche -> π.")
print("   [D] HOLOGRAPHIE : route dS/CFT CONVERGE avec [A] (même ⟨|h|^2⟩) ; C_T ∝ N")
print("                     (verrouillage) ; A_T·(coeff⟨TT⟩)=1/(2π^2) ; A_T·N=16.")
print("   ==> CANDIDAT-ÉGALITÉ A_T = 16/N CONFIRMÉ par les deux routes (convention standard).")
print("   À INVENTER : valeur/réalité exacte de C_T en dS (terme divergent réel = phase ;")
print("     'i' du terme fini = non-unitarité) ; survie au crossover CCC ; fixation de N")
print("     (circularité LC-E, NON brisée). NE ferme PAS D1.")
print("   Discipline §6.4 : 'A_T·N=16 reproduit (algèbre)' != 'D1 fermé / CCC établie'.")
print("-" * 72)
print("\nTOUS LES ASSERT PASSENT.")
