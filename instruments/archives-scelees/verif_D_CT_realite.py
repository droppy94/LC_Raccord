#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_CT_realite.py — LC-RACCORD. Sceau de la question « RÉALITÉ de C_T en dS »
(dernier `à inventer` connexe du verrouillage C_T~N). Successeur de verif_D_CT_ATN.py :
ce dernier a scellé A_T·N=16, le verrouillage C_T∝N (en MAGNITUDE) et la convergence
des deux routes, en ISOLANT la signature non-unitaire mais SANS trancher la réalité de
C_T continué. Ce sceau formalise la continuation et, surtout, fait un VRAI TEST DE
REPORT D'ERREUR : une indétermination du signe/réalité de C_T se propage-t-elle, ou non,
vers l'observable ?

Position. La continuation dS/CFT est ℓ_AdS -> iℓ_dS (Λ -> -Λ). La charge centrale de la
CFT de bord scale comme C_T ∝ ℓ^{d-1}/G ; la continuation attache donc un facteur i^{d-1}.
Le verif_D_CT_ATN calcule une MAGNITUDE |C_T| = N/(32π²) (prescription |Im F|, positive) ;
la continuation fournit le SIGNE/la phase. Ce sont deux objets distincts du graphe de
dépendances — pas une valeur contradictoire.

Extension de :
    verif_D_CT_ATN.py       — A_T·N=16 ; |C_T| (magnitude) ∝ N ; |C_T|/N = 1/(32π²) ;
                              prescription dS/CFT 𝒫 = 1/(2|Im F|_fini) ; signature isolée.
    verif_E_planck.py       — N = S_dS = π/(G H^2) (entropie de de Sitter).

Blocs :
    [A] CONTINUATION i^{d-1} (parité de la puissance de ℓ). Sur C_T ∝ c0·ℓ^{d-1}/G, la
        continuation ℓ_AdS = i·ℓ_dS donne C_T_signé = i^{d-1}·|C_T|. Classement d∈{2,3,4} :
            d=2 (ℓ^1) -> i        -> IMAGINAIRE   (cas Strominger, c∝ℓ)
            d=3 (ℓ^2) -> -1       -> RÉEL NÉGATIF  (le cas qui nous concerne)
            d=4 (ℓ^3) -> -i       -> IMAGINAIRE
        => en d=3 (puissance PAIRE d-1=2), C_T continué est RÉEL NÉGATIF, PAS imaginaire.
        Le facteur i^{d-1} est INDÉPENDANT de la normalisation c0 (parité structurelle).
    [B] MAGNITUDE vs SIGNÉ (pas de contradiction). |C_T| = N/(32π²) > 0 (sceau ATN) ;
        C_T_signé(d=3) = -|C_T| = -N/(32π²) < 0. Le sceau ATN calcule la magnitude ; la
        continuation attache le signe. Aucune valeur n'est contradictoire.
    [C] TEST DE REPORT D'ERREUR (le coeur). L'observable 𝒫 = 1/(2|Im F|_fini) ne dépend
        que de la MAGNITUDE de Im F. On INJECTE une erreur sur la réalité/le signe de C_T :
        une partie réelle arbitraire δr (réalité fausse) ET un signe s∈{+1,-1} (ambiguïté de
        signe). L'observable est INVARIANT (δr ∉ ses free_symbols ; identique pour s=±1),
        alors que C_T_signé, lui, PORTE l'erreur (δr ∈ ses free_symbols). => PARE-FEU :
        l'erreur de réalité ne remonte pas vers l'observable.
    [D] LECTURE (structurel ; NON scellé comme physique). C_T_signé(d=3) < 0 n'est pas une
        charge centrale unitaire (l'unitarité exige C_T>0). « C_T déterminé en magnitude »
        != « C_T unitaire propre ». L'obstruction « C_T<0 » coïncide avec l'item déjà
        catalogué « CFT de raccordement non construite » : ce n'est PAS une obstruction
        indépendante neuve. [à inventer / décision ouverte — pas un acquis algébrique.]

Cibles (paper LC-WORK-REPRISE-POST-NONLIN-VERROU §4 ; ce sceau les reproduit) :
    facteur de continuation   i^{d-1} : d=2 imag, d=3 réel<0, d=4 imag (parité, c0-libre)
    magnitude                 |C_T| = N/(32π²) > 0
    signé d=3                 C_T_signé = -N/(32π²) < 0  (réel négatif)
    observable                𝒫 = 2H^2/(M_Pl^2 k^3) — INVARIANT sous (δr, s) [report nul]
    pare-feu                  δr ∈ free_symbols(C_T_signé)  ET  δr ∉ free_symbols(𝒫)

Dépendances : sympy. Re-exécutable, sans réseau.
Discipline (LC-AUDIT-VERDICT §6.4) : un `établi` de sceau = « l'algèbre est correcte ET
les cibles reproduites ». Ici : la parité i^{d-1}, la non-contradiction magnitude/signe et
l'invariance de l'observable (report nul) sont `établi (algèbre)`. La LECTURE [D] (réalité ≡
item raccordement) est `décision ouverte` argumentée, NON scellée comme physique. Ne ferme
PAS D1 ; (A) physique conditionnel au seul A2★ inchangé ; la CCC n'est pas démontrée.
"""

import sympy as sp


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


print("=" * 72)
print(" verif_D_CT_realite.py — continuation i^(d-1), magnitude/signe, report d'erreur")
print("=" * 72)

# Symboles communs.
k, H, G, pi, ell_dS, c0 = sp.symbols('k H G pi ell_dS c0', positive=True)
I = sp.I
MPl2 = 1 / (8 * pi * G)              # M_Pl^2 réduite = 1/(8πG)
N = sp.simplify(pi / (G * H**2))     # N = S_dS (verif_E_planck)

# ======================================================================
# [A] CONTINUATION i^{d-1} : parité de la puissance de ℓ (c0-indépendante)
# ======================================================================
banner("[A] CONTINUATION ℓ_AdS -> iℓ_dS  sur  C_T ∝ c0·ℓ^(d-1)/G  =>  facteur i^(d-1)")

# C_T^AdS(ℓ) = c0 ℓ^{d-1}/G ; continuation ℓ_AdS = i ℓ_dS.
def C_T_AdS(ell, d):
    return c0 * ell**(d - 1) / G

attendu = {2: "IMAGINAIRE", 3: "RÉEL<0", 4: "IMAGINAIRE"}
for d in (2, 3, 4):
    C_signed = sp.simplify(C_T_AdS(I * ell_dS, d))          # C_T continué (signé)
    C_mag = sp.simplify(C_T_AdS(ell_dS, d))                 # magnitude (>0)
    facteur = sp.simplify(C_signed / C_mag)                 # = i^{d-1}, doit être c0-libre
    if sp.im(facteur) != 0 and sp.re(facteur) == 0:
        nature = "IMAGINAIRE"
    elif sp.re(facteur) > 0:
        nature = "RÉEL>0"
    else:
        nature = "RÉEL<0"
    print(f"  d={d} : C_T ∝ ℓ^{d-1}  ->  facteur = i^{d-1} = {str(facteur):>3}  =>  {nature}")
    assert sp.simplify(facteur - I**(d - 1)) == 0           # facteur = i^{d-1}
    assert {c0, ell_dS, G, H, k}.isdisjoint(facteur.free_symbols)  # parité c0-indépendante
    assert nature == attendu[d]
print("  >>> parité : d-1 PAIR (d=3) -> réel ; d-1 IMPAIR (d=2,4) -> imaginaire.")
print("      'imaginaire' (KB) = importation du cas d=2 ; en d=3 c'est RÉEL NÉGATIF.")

# ======================================================================
# [B] MAGNITUDE (sceau ATN) vs SIGNÉ (continuation) : pas de contradiction
# ======================================================================
banner("[B] MAGNITUDE |C_T| = N/(32π²) > 0  vs  SIGNÉ C_T(d=3) = -N/(32π²) < 0")

# Magnitude issue de verif_D_CT_ATN : coeff de <TT> = |Im F|_fini/k^3 = M_Pl^2/(4H^2).
CT_mag = sp.simplify(MPl2 / (4 * H**2))                     # = 1/(32π G H^2)
ratio_mag_N = sp.simplify(CT_mag / N)
print("  |C_T| (magnitude, sceau ATN) =", CT_mag, "  ;  |C_T|/N =", ratio_mag_N)
assert sp.simplify(ratio_mag_N - 1 / (32 * pi**2)) == 0     # |C_T| = N/(32π²)
assert CT_mag > 0                                           # magnitude positive
# Signé en d=3 : facteur i^2 = -1.
CT_signed_d3 = sp.simplify(I**(3 - 1) * CT_mag)             # = -|C_T|
print("  C_T signé (d=3) = i^2·|C_T| =", CT_signed_d3, "  (réel négatif)")
assert sp.im(CT_signed_d3) == 0 and CT_signed_d3 < 0        # réel ET négatif
assert sp.simplify(CT_signed_d3 + N / (32 * pi**2)) == 0    # = -N/(32π²)
print("  >>> magnitude (>0) et signé (<0) sont DEUX objets : le sceau ATN calcule |C_T|,")
print("      la continuation attache le signe. AUCUNE valeur contradictoire.")

# ======================================================================
# [C] TEST DE REPORT D'ERREUR : l'observable est-il insensible au signe/réalité de C_T ?
# ======================================================================
banner("[C] REPORT D'ERREUR  —  perturber la réalité/le signe de C_T ; l'observable bouge-t-il ?")

target = sp.simplify(2 * H**2 / (MPl2 * k**3))             # ⟨|h|^2⟩ canonique (cible)

# Coefficient fini VRAI de la fonction d'onde : F_fin = (M_Pl^2/4)(-i k^3/H^2).
F_fin_true = sp.simplify(MPl2 / 4 * (-I * k**3 / H**2))
P_true = sp.simplify(1 / (2 * sp.Abs(sp.im(F_fin_true))))
print("  observable VRAI 𝒫 = 1/(2|Im F|) =", P_true, "  (cible", target, ")")
assert sp.simplify(P_true - target) == 0

# INJECTION D'ERREUR : partie réelle arbitraire δr (réalité fausse de C_T) + signe s=±1.
dr = sp.symbols('delta_r', real=True)                      # erreur sur la PARTIE RÉELLE de C_T
print("  injection : F_fin -> (M_Pl^2/4)[ s·(-i k^3/H^2) + δr ]  avec δr réel arbitraire, s=±1")
for s in (1, -1):
    F_fin_err = sp.simplify(MPl2 / 4 * (s * (-I * k**3 / H**2) + dr))
    P_err = sp.simplify(1 / (2 * sp.Abs(sp.im(F_fin_err))))
    print(f"    s={s:+d} : 𝒫(perturbé) =", P_err, " ; δr présent ? ", dr in P_err.free_symbols)
    assert sp.simplify(P_err - target) == 0                # observable INCHANGÉ
    assert dr not in P_err.free_symbols                    # δr n'entre PAS dans l'observable

# Le C_T signé, lui, PORTE l'erreur (partie réelle δr + signe).
CT_signed_err = sp.simplify(dr + I**(3 - 1) * CT_mag)      # = δr - |C_T|
print("  C_T signé (perturbé) = δr + i^2|C_T| =", CT_signed_err, " ; δr présent ? ",
      dr in CT_signed_err.free_symbols)
assert dr in CT_signed_err.free_symbols                    # l'erreur VIT dans C_T signé
print("  >>> PARE-FEU : δr ∈ free_symbols(C_T signé)  MAIS  δr ∉ free_symbols(observable).")
print("      => une erreur de réalité/signe de C_T NE SE REPORTE PAS vers l'observable.")
print("      (l'observable est alimenté par la MAGNITUDE |Im F|, en amont du signe.)")

# ======================================================================
# [D] LECTURE (structurel ; NON scellé comme physique)
# ======================================================================
banner("[D] LECTURE  —  C_T<0 n'est pas unitaire ; réduction sur l'item « CFT de raccordement »")

# L'unitarité d'une CFT exige C_T>0 ; le signé d=3 est <0.
print("  unitarité d'une CFT : exige C_T > 0.   C_T signé(d=3) =", CT_signed_d3, "< 0.")
assert not (CT_signed_d3 > 0)                              # viole la borne d'unitarité
print("  => 'C_T déterminé en magnitude' != 'C_T charge centrale unitaire propre'.")
print("  NOTE [à inventer / décision ouverte — NON scellé] : que C_T<0 soit une obstruction")
print("       DE FOND dépend de savoir si le raccordement CCC exige une VRAIE CFT unitaire")
print("       (alors obstruction) ou un simple GÉNÉRATEUR de fonctions (alors bénin, vue de")
print("       Maldacena : Ψ = fonction d'onde, pas théorie duale physique). Or 'vraie CFT")
print("       unitaire' EST l'item déjà catalogué 'CFT de raccordement non construite'.")
print("       => la réalité de C_T ne crée PAS d'obstruction indépendante : elle se RABAT")
print("          sur cet item. Consolidation (moins de `à inventer` distincts), pas réduction")
print("          du compte {A4 ; A2★ ; N}. D1 NON clos.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-" * 72)
print(" VERDICT (établi : algèbre ; cibles reproduites) :")
print("   [A] CONTINUATION : facteur i^(d-1), c0-indépendant. d=2 imag, d=3 RÉEL<0, d=4 imag.")
print("                      => en d=3, C_T continué est RÉEL NÉGATIF (pas imaginaire).")
print("   [B] MAGNITUDE/SIGNE : |C_T|=N/(32π²)>0 (sceau ATN) ; C_T signé(d=3)=-N/(32π²)<0.")
print("                      Deux objets distincts — AUCUNE contradiction.")
print("   [C] REPORT D'ERREUR : observable 𝒫=2H^2/(M_Pl^2 k^3) INVARIANT sous (δr, s) ;")
print("                      δr ∈ C_T signé mais ∉ observable. PARE-FEU : report NUL.")
print("   [D] LECTURE [décision ouverte, NON scellé] : C_T<0 non unitaire ; la réalité de")
print("                      C_T se RABAT sur l'item 'CFT de raccordement' (consolidation).")
print("   ==> Les `établi (algèbre)` amont (A_T·N=16, verrouillage en magnitude, convergence")
print("       des routes) sont ROBUSTES au verdict de réalité, quel qu'il soit.")
print("   À INVENTER : nature (obstruction de fond vs bénin) du C_T<0 = item raccordement ;")
print("       survie au crossover ; fixation de N (circularité LC-E, NON brisée). Ne ferme PAS D1.")
print("   Discipline §6.4 : 'report nul + C_T<0 (algèbre)' != 'D1 fermé / CCC établie'.")
print("-" * 72)
print("\nTOUS LES ASSERT PASSENT.")
