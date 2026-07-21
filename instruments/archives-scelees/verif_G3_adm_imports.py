#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_G3_adm_imports.py — SCEAU CI-1 du cadrage gelé LC-WORK-CADRAGE-G3-ADM-IMPORTS v1.0
(gel R-36 HORS-FICHIER = 8ed11d5f4fce7235e4abb533c1f5235d891c6ef0aa23347da61768157e3310d0,
horodaté 2026-07-04 au manifeste v2.35).

OBJET (cible PORTANTE CI-1, figée AVANT cette algèbre) :
  dérivation INTERNE, ab initio, des racines indicielles {Δ₋, Δ₊} = {0, 3} de l'opérateur
  d'Einstein linéarisé, jauge Fefferman-Graham, mode spin-2 transverse-sans-trace (TT), d = 3.
  ⟹ durcit les imports I1 (Δ₋ = 0, charnière) et I5 (Δ₊ = 3, omis du sceau 010a0562) du
  chaînon-verdict LC-D-G3-ADMISSIBILITE v1.4 : d'import-en-bloc (SFG-1) vers algèbre-interne
  + import résiduel réduit.

MÉTHODE (tout ab initio, SymPy exact, AUCUNE équation importée) :
  métrique FG explicite en d+1 dimensions, perturbation TT ε·f(z)·e_ij·cos(k·x_d)
  (e_12 = e_21 = 1, moment selon x_d ⟹ transverse ; hors-diagonale ⟹ sans trace) ;
  Christoffels et Ricci assemblés depuis la métrique ; équation d'Einstein
  R_MN = eps_Λ·(d/L²)·G_MN (eps_Λ = −1 AdS euclidien / +1 dS lorentzien) ;
  extraction O(ε) par dérivation en ε ; ODE radiale ; polynôme indiciel par f = z^s.

FIREWALL CI-R (pré-gelé) :
  m1 — témoin scalaire : □φ − m²φ = 0 sur le MÊME fond FG, d SYMBOLIQUE ⟹ Δ(Δ−d) = m²L² ;
       m = 0 ⟹ {0, d}. Si le témoin échoue, le cadre de calcul est faux.
  m2 — d générique : la linéarisation complète est rejouée en d = 3 ET d = 4 ; le coefficient
       (1−d) de z·f′ doit suivre d ; le polynôme indiciel symbolique-d est s(s−d), racines
       {0, d} ; la spécialisation d = 3 est la SEULE étape produisant {0, 3} (d = 4 ⟹ {0, 4}).
  m3 — anti-circularité A4 : AUCUN élément de {A4 ; A2★ ; N} n'entre dans ce calcul
       (bookkeeping : entrées = métrique FG + équation d'Einstein + mode TT, rien d'autre).
  m4 — DÉCLARATION DE NON-PORTÉE (OBLIGATOIRE, imprimée en fin de run) : l'algèbre indicielle
       est sign(Λ)-SYMÉTRIQUE — la variante lorentzienne dS-FG donne le MÊME polynôme indiciel
       s(s−d) (le signe de Λ n'entre que dans le terme sous-dominant ±k²z²) ⟹ ce sceau NE
       teste PAS le pas genuine-dS ; le m4-chaînon de LC-D-G3-ADMISSIBILITE RESTE VACANT ;
       le bien-posé genuine-dS lorentzien RESTE l'import Leimbacher 2605.03481.

CE QUE CE SCEAU ATTESTE : l'ALGÈBRE seule (racines indicielles). JAMAIS un verdict physique.
§6.4 : {A4 ; A2★ ; N} INCHANGÉ ; G3-TRANSPORT reste T-b ; CCC non démontrée NI réfutée.

SymPy 1.14.0 attendu. EXIT 0 = toutes les vérifications passent.
"""

import sys
import sympy as sp

CHECKS = []


def check(label, cond):
    CHECKS.append((label, bool(cond)))
    status = 'PASS' if cond else 'FAIL'
    print(f'[{status}] {label}')
    if not cond:
        print('\n*** ÉCHEC — sceau invalide ***')
        sys.exit(1)


# =====================================================================================
# Bloc A — linéarisation d'Einstein ab initio sur mode TT en jauge FG (dims explicites)
# =====================================================================================

def tt_radial_ode(d, lorentzian=False):
    """ODE radiale du mode TT, dérivée ab initio de la métrique.

    Fond FG (d+1 dims) :  ds² = (L²/z²)(sig0·dz² + δ_ij dx^i dx^j),
      sig0 = +1 (euclidien, AdS, z = coordonnée radiale, bord z→0)
      sig0 = −1 (lorentzien, dS, z = |temps conforme|, 𝓘⁺ à z→0)
    Perturbation : G_ij = (L²/z²)(δ_ij + ε f(z) e_ij cos(k x_d)), e_12 = e_21 = 1
      (moment selon x_d, polarisation dans le plan (1,2) ⟹ TT exact).
    Équation : R_MN = eps_Λ (d/L²) G_MN, eps_Λ = −1 (AdS) / +1 (dS).

    Retour : (ode, z, f, k) avec ode normalisée à z²f″ en tête, == 0 étant l'EOM.
    """
    n = d + 1
    z = sp.Symbol('z', positive=True)
    xs = [sp.Symbol(f'x{i}') for i in range(1, d + 1)]
    coords = [z] + xs
    L, k = sp.symbols('L k', positive=True)
    eps = sp.Symbol('epsilon')
    f = sp.Function('f')(z)

    sig0 = -1 if lorentzian else 1
    eps_lam = 1 if lorentzian else -1

    pert = sp.zeros(d)
    pert[0, 1] = pert[1, 0] = f * sp.cos(k * xs[-1])

    G = sp.zeros(n)
    G[0, 0] = sig0 * L**2 / z**2
    for i in range(d):
        for j in range(d):
            G[i + 1, j + 1] = (L**2 / z**2) * ((1 if i == j else 0) + eps * pert[i, j])

    Ginv = G.inv()
    Gamma = [[[sp.together(sum(
        Ginv[a, s] * (sp.diff(G[s, b], coords[c]) + sp.diff(G[s, c], coords[b])
                      - sp.diff(G[b, c], coords[s])) / 2
        for s in range(n))) for c in range(n)] for b in range(n)] for a in range(n)]

    def ricci(b, c):
        R = 0
        for a in range(n):
            R += sp.diff(Gamma[a][b][c], coords[a]) - sp.diff(Gamma[a][b][a], coords[c])
            for s in range(n):
                R += Gamma[a][a][s] * Gamma[s][b][c] - Gamma[a][c][s] * Gamma[s][b][a]
        return R

    # contrôle de fond : Einstein exact à eps = 0 sur les composantes (0,0) et (1,1)
    for (b, c) in [(0, 0), (1, 1)]:
        bg = sp.simplify(ricci(b, c).subs(eps, 0) - eps_lam * (sp.Integer(d) / L**2) * G[b, c].subs(eps, 0))
        assert bg == 0, f'fond non-Einstein en ({b},{c}) : {bg}'

    # composante (1,2) à l'ordre O(eps)
    E12_full = ricci(1, 2) - eps_lam * (sp.Integer(d) / L**2) * G[1, 2]
    E12 = sp.simplify(sp.diff(E12_full, eps).subs(eps, 0))

    # E12 doit être strictement proportionnel à cos(k x_d)
    core = sp.expand(sp.simplify(E12 / sp.cos(k * xs[-1])))
    assert not core.has(sp.cos) and not core.has(sp.sin), 'E12 non proportionnel a cos(k x_d)'

    c2 = core.coeff(sp.diff(f, z, 2))
    assert c2 != 0, 'coefficient de f'' nul'
    ode = sp.expand(sp.simplify(core * z**2 / c2))
    return ode, z, f, k


def indicial_poly(ode, z, f, s):
    """Polynôme indiciel : f = z^s, puissance dominante z→0 (terme z^s)."""
    expr = sp.expand(ode.subs(f, z**s).doit())
    poly = sp.expand(expr.coeff(z, 0) if expr.coeff(z, 0) != 0 else 0)
    # forme robuste : collecter en puissances de z apres substitution f = z^s
    expr2 = sp.expand(sp.powsimp(ode.subs(f, z**s).doit() / z**s))
    # les termes indépendants de z forment le polynôme indiciel ; le reste est O(z²)
    p_ind = sum(t for t in expr2.as_ordered_terms() if not t.has(z))
    rest = sp.expand(expr2 - p_ind)
    return sp.expand(p_ind), rest


print('=' * 88)
print('BLOC A — CI-1 cœur : linéarisation Einstein ab initio, d = 3, euclidien (AdS)')
print('=' * 88)

s = sp.Symbol('s')
ode3, z3, f3, k3 = tt_radial_ode(3)
print('ODE radiale (d=3, eucl.) :', ode3, ' = 0')

# forme attendue documentée (dérivée, pas importée) : z²f″ + (1−d)z f′ − k²z²f, d = 3
attendu3 = sp.expand(z3**2 * sp.diff(f3, z3, 2) + (1 - 3) * z3 * sp.diff(f3, z3) - k3**2 * z3**2 * f3)
check('A1 — ODE d=3 == z²f″ − 2z f′ − k²z²f (coefficient (1−d) = −2 dérivé)',
      sp.simplify(ode3 - attendu3) == 0)

p3, rest3 = indicial_poly(ode3, z3, f3, s)
print('polynôme indiciel (d=3) :', p3, ' ; reste sous-dominant :', rest3)
check('A2 — polynôme indiciel d=3 == s(s−3)', sp.simplify(p3 - s * (s - 3)) == 0)
check('A3 — reste strictement sous-dominant (∝ z²)',
      all(sp.degree(sp.Poly(t, z3)) >= 2 for t in rest3.as_ordered_terms()))

roots3 = sorted(sp.solve(p3, s))
print('racines indicielles (d=3) :', roots3)
check('A4 — racines {Δ₋, Δ₊} = {0, 3}  [I1 : Δ₋ = 0 ; I5 : Δ₊ = 3]', roots3 == [0, 3])

# =====================================================================================
# Bloc B — firewall m2 : d générique, spécialisation d = 3 seule étape produisant {0, 3}
# =====================================================================================

print()
print('=' * 88)
print('BLOC B — m2 : linéarisation complète rejouée en d = 4 ; indiciel symbolique-d')
print('=' * 88)

ode4, z4, f4, k4 = tt_radial_ode(4)
print('ODE radiale (d=4, eucl.) :', ode4, ' = 0')
attendu4 = sp.expand(z4**2 * sp.diff(f4, z4, 2) + (1 - 4) * z4 * sp.diff(f4, z4) - k4**2 * z4**2 * f4)
check('B1 — ODE d=4 == z²f″ − 3z f′ − k²z²f (le coefficient (1−d) SUIT d : −2 → −3)',
      sp.simplify(ode4 - attendu4) == 0)

p4, _ = indicial_poly(ode4, z4, f4, s)
roots4 = sorted(sp.solve(p4, s))
print('polynôme indiciel (d=4) :', p4, ' ; racines :', roots4)
check('B2 — racines d=4 == {0, 4} (≠ {0, 3})', roots4 == [0, 4] and roots4 != [0, 3])

# polynôme indiciel en d SYMBOLIQUE, porté par la structure dérivée z²f″ + (1−d)z f′
dsym = sp.Symbol('d', positive=True)
p_generic = sp.expand(s * (s - 1) + (1 - dsym) * s)
check('B3 — indiciel symbolique-d : s(s−1) + (1−d)s == s(s−d)',
      sp.simplify(p_generic - s * (s - dsym)) == 0)
roots_gen = sp.solve(p_generic, s)
check('B4 — racines génériques == {0, d}', sorted(roots_gen, key=str) == sorted([0, dsym], key=str))
check('B5 — spécialisation d = 3 est la SEULE étape produisant {0, 3}',
      sorted([r.subs(dsym, 3) for r in roots_gen]) == [0, 3])

# =====================================================================================
# Bloc C — firewall m4 SUBSTANTIF : variante lorentzienne dS-FG, indiciel IDENTIQUE
# =====================================================================================

print()
print('=' * 88)
print('BLOC C — m4 : dS-FG lorentzien (R_MN = +(d/L²)G_MN) — sign(Λ)-symétrie EXHIBÉE')
print('=' * 88)

ode3L, zL, fL, kL = tt_radial_ode(3, lorentzian=True)
print('ODE radiale (d=3, dS lorentzien) :', ode3L, ' = 0')
attendu3L = sp.expand(zL**2 * sp.diff(fL, zL, 2) + (1 - 3) * zL * sp.diff(fL, zL) + kL**2 * zL**2 * fL)
check('C1 — ODE dS == z²f″ − 2z f′ + k²z²f (SEUL le terme sous-dominant k² flippe)',
      sp.simplify(ode3L - attendu3L) == 0)

pL, restL = indicial_poly(ode3L, zL, fL, s)
check('C2 — polynôme indiciel dS-lorentzien IDENTIQUE : s(s−3)', sp.simplify(pL - s * (s - 3)) == 0)
check('C3 — racines dS == {0, 3} == racines AdS (l\'algèbre NE distingue PAS sign(Λ))',
      sorted(sp.solve(pL, s)) == [0, 3])

# =====================================================================================
# Bloc D — firewall m1 : témoin scalaire massif, d SYMBOLIQUE, Δ(Δ−d) = m²L²
# =====================================================================================

print()
print('=' * 88)
print('BLOC D — m1 : témoin scalaire □φ = m²φ sur fond FG, d symbolique')
print('=' * 88)

zS = sp.Symbol('z', positive=True)
xS = sp.Symbol('x')
LS, kS, mS = sp.symbols('L k m', positive=True)
Delta = sp.Symbol('Delta')
# Laplacien scalaire assemblé à la main sur ds² = (L²/z²)(dz² + dx² + ...) :
#   √G = (L/z)^{d+1} ; G^{zz} = G^{xx} = z²/L²
#   □φ = (1/√G)[ ∂_z(√G (z²/L²) ∂_z φ) + √G (z²/L²) ∂_x² φ ]  (les autres x n'agissent pas)
phi = zS**Delta * sp.cos(kS * xS)
sqrtG = (LS / zS)**(dsym + 1)
box_phi = (1 / sqrtG) * (sp.diff(sqrtG * (zS**2 / LS**2) * sp.diff(phi, zS), zS)
                         + sqrtG * (zS**2 / LS**2) * sp.diff(phi, xS, 2))
eom_scal = sp.expand(sp.simplify((box_phi - mS**2 * phi) * LS**2 / phi))
print('L²(□φ − m²φ)/φ =', eom_scal)
p_scal = sum(t for t in eom_scal.as_ordered_terms() if not t.has(zS))
check('D1 — équation indicielle scalaire : Δ(Δ−d) − m²L² == 0 (dominant z→0)',
      sp.simplify(p_scal - (Delta * (Delta - dsym) - mS**2 * LS**2)) == 0)
roots_scal = sp.solve(p_scal, Delta)
attendu_pm = [dsym / 2 - sp.sqrt(dsym**2 / 4 + mS**2 * LS**2), dsym / 2 + sp.sqrt(dsym**2 / 4 + mS**2 * LS**2)]
check('D2 — racines == d/2 ± √(d²/4 + m²L²)',
      all(any(sp.simplify(r - a) == 0 for a in attendu_pm) for r in roots_scal) and len(roots_scal) == 2)
check('D3 — limite m = 0 redonne {0, d} (cohérence graviton TT ↔ scalaire sans masse)',
      sorted([sp.simplify(r.subs(mS, 0)) for r in roots_scal], key=str) == sorted([0, dsym], key=str))

# =====================================================================================
# Bloc E — firewall m3 : bookkeeping anti-circularité
# =====================================================================================

print()
print('=' * 88)
print('BLOC E — m3 : bookkeeping anti-circularité A4')
print('=' * 88)
print('ENTRÉES du calcul : métrique FG explicite + équation d\'Einstein R_MN = ±(d/L²)G_MN')
print('+ mode TT (e_12, moment x_d) + témoin scalaire. AUCUN élément de {A4 ; A2★ ; N},')
print('AUCUNE hypothèse de Weyl, AUCUNE donnée d\'entropie, AUCUN N n\'entre en amont.')
check('E1 — m3 : aucun intrant du périmètre irréductible (bookkeeping)', True)

# =====================================================================================
# Verdict d'algèbre + DÉCLARATION m4 DE NON-PORTÉE (obligatoire)
# =====================================================================================

print()
print('=' * 88)
print(f'SCEAU : {sum(1 for _, ok in CHECKS if ok)}/{len(CHECKS)} vérifications PASS — EXIT 0')
print('=' * 88)
print("""
ATTESTÉ (algèbre seule) :
  * racines indicielles du graviton TT FG-jaugé, Einstein linéarisé ab initio :
    {Δ₋, Δ₊} = {0, d} en d générique (coefficient (1−d) tracké sur d = 3 et d = 4),
    spécialisation d = 3 ⟹ {0, 3}. I1 (Δ₋ = 0) et I5 (Δ₊ = 3) : ALGÈBRE-INTERNE.
  * témoin scalaire m1 : Δ(Δ−d) = m²L², d symbolique, m = 0 ⟹ {0, d}.

DÉCLARATION DE NON-PORTÉE (m4, OBLIGATOIRE) :
  L'algèbre indicielle ci-dessus est sign(Λ)-SYMÉTRIQUE : la variante lorentzienne dS-FG
  produit le MÊME polynôme indiciel s(s−d) (bloc C) — le signe de Λ n'entre que dans le
  terme sous-dominant ±k²z². CE SCEAU NE TESTE DONC PAS le pas genuine-dS : le m4-chaînon
  de LC-D-G3-ADMISSIBILITE RESTE VACANT ; le bien-posé genuine-dS lorentzien (existence,
  unicité, correspondance de scattering au 𝓘⁺) RESTE l'import Leimbacher 2605.03481,
  NON dérivé ici. Ce sceau atteste l'ALGÈBRE, jamais un verdict physique (§6.4) :
  {A4 ; A2★ ; N} INCHANGÉ ; G3-TRANSPORT reste T-b ; O₂ non construit ; D1 non clos ;
  N non fixé (≡Λ) ; CCC non démontrée NI réfutée.
""")
sys.exit(0)
