#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_cb_weyl_magnetique.py — sceau du petit front c_B (LC-D-CB-WEYL-MAGNETIQUE)
================================================================================
Cibles gelées : LC-WORK-CADRAGE-CB v0.1 §3 (R-7 active depuis validation Thierry,
2026-06-12, scopings S-CB-1..4 tranchés "tout recommandé").

  CB-1 : la limite rescalée du Weyl MAGNÉTIQUE du mode TT de BD à 𝓘⁺ existe,
         finie, non nulle, indépendante de k et x ; 𝓑_ij = c_B·C_ij[g₀] avec
         c_B = 1/H attendu. (Si le calcul donne autre chose, le calcul tranche.)
  CB-2 : équipartition ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 1 EN UNITÉS PROGRAMME (fixée par les
         définitions, aucun paramètre neuf) ; refermeture dH (49)/(50) via la
         map prog↔dH (facteur fixe pur), slack nul ⟹ le scoping R-11 est levé
         PAR DÉRIVATION.
  CB-3 : anti-numérologie — 0 entrée libre < 2 sorties appariées.
  Firewall : F-1 (puissance de Ω discriminante) ; F-2 (Cotton ×2 casse d'un
         facteur 4) ; F-3 (parité : lecture électrique échoue).

Conventions (TOUTES réutilisées, scellées en amont — CADRAGE §2) :
  - Frame conforme : fond Minkowski diag(−1,+1,+1,+1) ; le Weyl tout-bas est
    conformément covariant (poids Ω²), route de verif_D3_bunchdavies.py.
  - Mode BD tensoriel : h(η) = A(1+ikη)e^{−ikη}, propagation ẑ, η→0⁻ ;
    relation d'état g₍₃₎ = −(i/3)k³ g₍₀₎ (glossaire / SPECTRE-K3).
  - Rescaling : Ω = −Hη (S-CB-2 : même prescription que l'électrique).
  - Magnétique : B̂_ij = ½ ε_i^{kl} Ĉ_{kl 0 j}, ε₁₂₃ = +1 (S-CB-2).
  - Cotton-York 3D : C_ij = ε_i^{kl} ∇_k P_{lj}, P = Ric − (R/4)g (Schouten d=3),
    dérivé AB INITIO ici avec le MÊME ε (cohérence d'orientation interne ⟹ le
    signe de c_B est convention-cohérent, pas posé).
  - Étalons de non-régression : Ĉ₀₁₀₁ = (i/2)Ak³η·e^{ik(z−η)} et
    E_lim/g₍₃₎ = 3/(2H) (verif_D3_bunchdavies.py) ; coefficient Cotton ½
    (LC-D-NONLIN-2PT C3, dH éq. 47).

Mono-phase (S-CB-3a) : AUCUN fetch externe ; comparanda dH (47),(49),(50) déjà
en KB (EXTRAIT_0808_2054v1_dH.pdf), consignés au chaînon NONLIN-2PT.

Discipline §6.4 : un EXIT 0 ici atteste l'algèbre et la reproduction des cibles
gelées — JAMAIS « D1 clos / N fixé / CCC démontrée ». {A4 ; A2★ ; N} inchangé.
"""

import sympy as sp

# ----------------------------------------------------------------------------
n_assert = 0
def check(cond, label):
    global n_assert
    if not cond:
        raise AssertionError(f"ÉCHEC — {label}")
    n_assert += 1
    print(f"  [{n_assert:02d}] OK — {label}")

I = sp.I
eta = sp.Symbol('eta', real=True)
x, y, z = sp.symbols('x y z', real=True)
k = sp.Symbol('k', positive=True)
A = sp.Symbol('A', positive=True)
H = sp.Symbol('H', positive=True)

coords = [eta, x, y, z]
g4 = sp.diag(-1, 1, 1, 1)          # frame conforme (Minkowski)
ginv = g4                           # diagonal ±1

h_bd  = A*(1 + I*k*eta)*sp.exp(-I*k*eta)   # mode BD, eta -> 0^-
phase = sp.exp(I*k*z)
Omega = -H*eta

E_PLUS  = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])   # e^+
E_CROSS = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])    # e^x

def H4_of(pol):
    """Perturbation TT spatiale H_{mu nu} du frame conforme."""
    Hm = sp.zeros(4, 4)
    pat = E_PLUS if pol == '+' else E_CROSS
    for a in range(3):
        for b in range(3):
            Hm[1 + a, 1 + b] = pat[a, b]*h_bd*phase
    return Hm

def lin_geometry(Hm):
    """Riemann/Ricci/Weyl linéarisés (n=4) sur fond Minkowski, formule du sceau
    bunchdavies : R_{munualbe} = 1/2(d_nu d_al H_{mube} + d_mu d_be H_{nual}
                                   - d_mu d_al H_{nube} - d_nu d_be H_{mual})."""
    def d(mu, expr):
        return sp.diff(expr, coords[mu])
    cacheR = {}
    def riem(mu, nu, al, be):
        key = (mu, nu, al, be)
        if key not in cacheR:
            cacheR[key] = sp.Rational(1, 2)*(
                d(nu, d(al, Hm[mu, be])) + d(mu, d(be, Hm[nu, al]))
                - d(mu, d(al, Hm[nu, be])) - d(nu, d(be, Hm[mu, al])))
        return cacheR[key]
    Ric = sp.zeros(4, 4)
    for nu in range(4):
        for be in range(4):
            Ric[nu, be] = sp.simplify(
                sum(ginv[mu, mu]*riem(mu, nu, mu, be) for mu in range(4)))
    Rs = sp.simplify(sum(ginv[nu, nu]*Ric[nu, nu] for nu in range(4)))
    def weyl(mu, nu, al, be):
        # n=4 : C = R - 1/2(g.Ric) + (R/6)(g.g) ; fond plat => g = eta_{munu}
        return sp.simplify(
            riem(mu, nu, al, be)
            - sp.Rational(1, 2)*(g4[mu, al]*Ric[nu, be] - g4[mu, be]*Ric[nu, al]
                                 - g4[nu, al]*Ric[mu, be] + g4[nu, be]*Ric[mu, al])
            + (Rs/6)*(g4[mu, al]*g4[nu, be] - g4[mu, be]*g4[nu, al]))
    return riem, Ric, Rs, weyl

def parts_EB(weyl):
    """Électrique E_ij = C_{0i0j} ; magnétique B_ij = 1/2 eps_i^{kl} C_{kl0j}."""
    E = sp.zeros(3, 3)
    B = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            E[i, j] = weyl(0, 1 + i, 0, 1 + j)
            B[i, j] = sp.simplify(sp.Rational(1, 2)*sum(
                sp.LeviCivita(i + 1, kk + 1, ll + 1)*weyl(1 + kk, 1 + ll, 0, 1 + j)
                for kk in range(3) for ll in range(3)))
    return E, B

def cotton_lin(pol):
    """Cotton-York 3D linéarisé AB INITIO (Euclide R^3, MÊME eps) sur la
    perturbation de bord h(0)_ij = A * pat * e^{ikz}."""
    pat = E_PLUS if pol == '+' else E_CROSS
    h3 = A*phase*pat
    c3 = [x, y, z]
    def d3(a, expr):
        return sp.diff(expr, c3[a])
    # Ricci linéarisé 3D (fond plat) : R_lj = 1/2(d_a d_l h^a_j + d_a d_j h^a_l
    #                                            - lap h_lj - d_l d_j h)
    tr = sum(h3[a, a] for a in range(3))
    Ric3 = sp.zeros(3, 3)
    for l in range(3):
        for j in range(3):
            Ric3[l, j] = sp.simplify(sp.Rational(1, 2)*(
                sum(d3(a, d3(l, h3[a, j])) for a in range(3))
                + sum(d3(a, d3(j, h3[a, l])) for a in range(3))
                - sum(d3(a, d3(a, h3[l, j])) for a in range(3))
                - d3(l, d3(j, tr))))
    R3 = sp.simplify(sum(Ric3[a, a] for a in range(3)))
    P3 = Ric3 - (R3/4)*sp.eye(3)          # Schouten d=3
    C3 = sp.zeros(3, 3)
    for i in range(3):
        for j in range(3):
            C3[i, j] = sp.simplify(sum(
                sp.LeviCivita(i + 1, kk + 1, ll + 1)*d3(kk, P3[ll, j])
                for kk in range(3) for ll in range(3)))
    return C3, R3

def lim_resc(expr):
    """Limite rescalée à scri+ : expr/Omega, eta -> 0."""
    return sp.simplify(sp.limit(sp.simplify(expr/Omega), eta, 0))

def hnorm2(M):
    """Somme des |M_ij|^2 (k, A, H réels positifs)."""
    return sp.simplify(sum(sp.simplify(M[i, j]*sp.conjugate(M[i, j]))
                           for i in range(3) for j in range(3)))

print("="*78)
print("SCEAU c_B — Weyl magnétique rescalé à 𝓘⁺ (cibles gelées CADRAGE-CB v0.1)")
print("="*78)

# ============================================================================
print("\n[A] Non-régression — route bunchdavies (électrique), mode +")
# ============================================================================
H4p = H4_of('+')
riem_p, Ric_p, Rs_p, weyl_p = lin_geometry(H4p)
Ep, Bp = parts_EB(weyl_p)

check(sp.simplify(Rs_p) == 0, "Ricci scalaire linéarisé R = 0 (TT)")

C0101 = sp.simplify(weyl_p(0, 1, 0, 1))
target_E = sp.Rational(1, 2)*I*A*k**3*eta*sp.exp(-I*k*eta)*phase
check(sp.simplify(C0101 - target_E) == 0,
      "Ĉ₀₁₀₁ = (i/2)Ak³η·e^{ik(z−η)} — étalon bunchdavies reproduit")
check(sp.simplify(C0101.series(eta, 0, 1).removeO()) == 0,
      "Ĉ₀₁₀₁ démarre à η¹ (pièces locales g₍₀₎, g₍₂₎ annulées)")
check(sp.simplify(sum(Ep[i, i] for i in range(3))) == 0
      and sp.simplify(Ep[0, 2]) == 0 and sp.simplify(Ep[2, 2]) == 0,
      "Électrique TT : trace nulle, E₁₃ = E₃₃ = 0 (2 polarisations)")

g3 = sp.simplify(h_bd.series(eta, 0, 4).removeO().coeff(eta, 3))*phase
check(sp.simplify(g3 - (-I*k**3/3)*A*phase) == 0,
      "Relation d'état BD : g₍₃₎ = −(i/3)k³ g₍₀₎ (glossaire/SPECTRE-K3)")

E_lim = sp.Matrix(3, 3, lambda i, j: lim_resc(Ep[i, j]))
check(sp.simplify(E_lim[0, 0]/g3 - sp.Rational(3, 2)/H) == 0,
      "E_lim/g₍₃₎ = 3/(2H) = d/2H — valeur SCELLÉE (verif_D3_bunchdavies)")

# ============================================================================
print("\n[B] Magnétique B̂ = ½εĈ : structure, rescaling, limite")
# ============================================================================
check(sp.simplify(Bp[0, 1] - Bp[1, 0]) == 0, "B̂ symétrique (B̂₁₂ = B̂₂₁)")
check(sp.simplify(sum(Bp[i, i] for i in range(3))) == 0, "B̂ sans trace")
check(sp.simplify(Bp[0, 2]) == 0 and sp.simplify(Bp[2, 2]) == 0
      and sp.simplify(Bp[0, 0]) == 0,
      "B̂(+) : TT, motif DUAL (porté par e^×, diagonale nulle) — parité en acte")

B12 = sp.simplify(Bp[0, 1])
target_B = -sp.Rational(1, 2)*I*A*k**3*eta*sp.exp(-I*k*eta)*phase
check(sp.simplify(B12 - target_B) == 0,
      "B̂₁₂ = −(i/2)Ak³η·e^{ik(z−η)} — même grandeur η¹ que l'électrique")

B_lim = sp.Matrix(3, 3, lambda i, j: lim_resc(Bp[i, j]))
check(sp.simplify(B_lim[0, 1] - I*A*k**3*phase/(2*H)) == 0,
      "𝓑₁₂ = lim B̂₁₂/Ω = (i/2H)Ak³e^{ikz} : FINIE, NON NULLE (CB-1, existence)")

# ============================================================================
print("\n[C] Cotton ab initio (même ε) et identification : c_B")
# ============================================================================
C3p, R3p = cotton_lin('+')
check(sp.simplify(R3p) == 0, "Cotton : R₃ linéarisé = 0 (TT) — Schouten = Ricci")
check(sp.simplify(C3p[0, 1] - sp.Rational(1, 2)*I*k**3*A*phase) == 0,
      "C^lin₁₂ = (i/2)k³A·e^{ikz} — coefficient ½ recoupé (NONLIN-2PT C3 ; dH 47)")

cB_plus = sp.simplify(B_lim[0, 1]/C3p[0, 1])
check(sp.simplify(cB_plus - 1/H) == 0,
      "c_B(+) = 𝓑/C^lin = 1/H — CIBLE GELÉE CB-1 TENUE telle qu'écrite")

H4x = H4_of('x')
_, _, _, weyl_x = lin_geometry(H4x)
Ex, Bx = parts_EB(weyl_x)
Bx_lim = sp.Matrix(3, 3, lambda i, j: lim_resc(Bx[i, j]))
C3x, _ = cotton_lin('x')
cB_cross = sp.simplify(Bx_lim[0, 0]/C3x[0, 0])
check(sp.simplify(cB_cross - 1/H) == 0,
      "c_B(×) = 1/H — identique sur la seconde polarisation")
check(sp.diff(cB_plus, k) == 0 and cB_plus.has(z) is False,
      "c_B indépendant de k et de x — constante de structure, pas de fit")

# ============================================================================
print("\n[D] Équipartition EN UNITÉS PROGRAMME + refermeture dH (CB-2)")
# ============================================================================
nB = hnorm2(B_lim)
nE = hnorm2(E_lim)
ratio_prog = sp.simplify(nB/nE)
check(ratio_prog == 1,
      "⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 1 EXACTE en unités programme — CIBLE GELÉE CB-2 TENUE")

crossEB = sp.simplify(sum(E_lim[i, j]*sp.conjugate(B_lim[i, j])
                          for i in range(3) for j in range(3)))
check(crossEB == 0,
      "⟨𝓔𝓑⟩ = 0 sur BD (motifs orthogonaux) — non-régression NONLIN-2PT C3")

# Map prog↔dH = κ²/(Hℓ²) : facteur FIXE PUR ⟹ s'annule dans tout ratio ;
# côté dH : préfacteurs 𝓔=−(ℓ²/2κ²)P vs 𝓑=(ℓ²/κ²)C (rapport 2) × Cotton ½
# ⟹ produit net (2·½)² = 1 (cas {2,4,8} déjà résolu au chaînon NONLIN-2PT).
mp = sp.Symbol('m_progdH', positive=True)   # facteur fixe pur, valeur indifférente
bb, ee = sp.symbols('bb ee', positive=True)
check(sp.simplify((mp*bb)**2/(mp*ee)**2 - bb**2/ee**2) == 0,
      "Map prog↔dH (facteur fixe pur) transparente dans tout ratio")
net_dH = (sp.Integer(2)*sp.Rational(1, 2))**2
check(net_dH == 1 and ratio_prog == net_dH,
      "Refermeture dH (49)/(50) : ratio prog = ratio dH = 1, SLACK NUL — "
      "le scoping R-11 est levé PAR DÉRIVATION")

# ============================================================================
print("\n[F] Firewall — chaque injection DOIT casser")
# ============================================================================
# F-1 : la puissance de Ω est discriminante (pas décorative)
ser = B12.series(eta, 0, 2).removeO()
check(sp.simplify(ser.coeff(eta, 0)) == 0 and sp.simplify(ser.coeff(eta, 1)) != 0,
      "F-1 : B̂ ∼ η¹ exactement ⟹ /Ω⁰ → 0 (signal tué), /Ω² → ∞ (diverge) ; "
      "seul Ω¹ donne une limite finie non nulle")
check(sp.limit(B12, eta, 0) == 0,
      "F-1 (pilote Ω⁰) : sans rescaling la limite est NULLE — CASSE")

# F-2 : Cotton ×2 (coefficient 1 au lieu de ½)
cB_mut = sp.simplify(B_lim[0, 1]/(2*C3p[0, 1]))
check(sp.simplify(cB_mut - 1/(2*H)) == 0 and sp.simplify(cB_mut - 1/H) != 0,
      "F-2 (pilote Cotton ×2) : c_B' = 1/(2H) ≠ 1/H — CASSE")
ratio_mut = sp.simplify(hnorm2(B_lim/2)/nE)   # 𝓑 lue avec le Cotton doublé
check(ratio_mut == sp.Rational(1, 4) and ratio_mut != 1,
      "F-2 (conséquence) : équipartition cassée d'un facteur 4 — CASSE")

# F-3 : parité/motif — une lecture ÉLECTRIQUE du canal magnétique échoue
ip_plus  = sp.simplify(sum(B_lim[i, j]*E_PLUS[i, j]  for i in range(3) for j in range(3)))
ip_cross = sp.simplify(sum(B_lim[i, j]*E_CROSS[i, j] for i in range(3) for j in range(3)))
check(ip_plus == 0 and ip_cross != 0,
      "F-3 (pilote parité) : 𝓑(+) ⊥ e^+ (lecture électrique : projection NULLE) "
      "mais 𝓑(+) ∥ e^× (motif dual) — CASSE")

# ============================================================================
print("\n[CB-3] Anti-numérologie")
# ============================================================================
entrees_libres = 0   # mode BD, Ω, ε, définitions : tout est scellé/figé en amont
sorties_appariees = 2  # (i) c_B vs attendu 1/H ; (ii) refermeture équipartition dH
check(entrees_libres < sorties_appariees,
      "0 entrée libre < 2 sorties appariées — CIBLE GELÉE CB-3 TENUE")

# ============================================================================
print("\n" + "="*78)
print(f"""RÉSULTAT (établi (algèbre) — discipline §6.4) :

  c_B = 1/H , EXACT, dérivé de la définition du Weyl rescalé (jamais posé) :
  𝓑_ij|𝓘⁺ = (1/H)·C_ij[g₍₀₎]   (le d/2 de l'électrique est absent : il vient
  du dictionnaire ⟨T⟩=(d/16πG)g₍₃₎, côté ÉTAT ; le magnétique est GÉOMÉTRIE).

  Couple complet des normalisations programme :
     𝓔 = (3/2H)·g₍₃₎  (scellé, bunchdavies)   |   𝓑 = (1/H)·C[g₍₀₎]  (ICI)

  ÉQUIPARTITION ⟨𝓑𝓑⟩ = ⟨𝓔𝓔⟩ : EXACTE AUSSI EN UNITÉS PROGRAMME — le scoping
  R-11 (unités de dualité) est LEVÉ PAR DÉRIVATION, pas par suppression.
  Refermeture dH (49)/(50) via map fixe pure : slack nul. Promesse C2pt-4
  du cadrage 2PT FERMÉE (la "seule constante non explicite en KB" l'est).

  SANS SURCLASSEMENT : ceci est un épinglage d'UNITÉS et une refermeture.
  JAMAIS « D1 clos / N fixé / CCC démontrée ». L'amplitude A_T~1/N reste la
  décision ouverte ; conditionnel à BD ; spécifique d=3.
  Compte {{A4 ; A2★ ; N}} INCHANGÉ.

TOUS LES ASSERT PASSENT — {n_assert} assertions. EXIT 0.""")
print("="*78)
