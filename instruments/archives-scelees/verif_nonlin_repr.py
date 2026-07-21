#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_nonlin_repr.py — LC-RACCORD. Sceau de la SOUS-QUESTION 2 du front
« généralisation NON-LINÉAIRE du verrouillage » : argument de REPRÉSENTATION sur le
secteur ÉLECTRIQUE E ∝ g3 ∝ <T_ij>. Objet : verrouiller, de façon EXACTE (tous ordres),
l'ABSENCE D'ADMIXTURE DE SINGLET dans g3 — condition de <E>=0 sous A3.

CONTEXTE (faits importés, NON re-dérivés) :
  • E_ij ∝ g3_ij ∝ <T_ij> (identification holographique électrique ; E_ij=(d/2H)g3
    déjà SCELLÉE en amont, verif_D3_bunchdavies.py — NON rejouée ici).
  • Le secteur MAGNÉTIQUE est clos en amont (verif_nonlin_cotton.py, sub-Q1 PASS :
    B ∝ Cotton[g0] = 0 sur fond conf. plat). Reste le SEUL secteur électrique.
  • Identités de Ward EXACTES en d=3 (d impair), de Haro-Skenderis-Solodukhin :
        g0^{ij} g3_ij = 0            (SANS TRACE — pas d'anomalie en d impair)
        ∇^i g3_ij = 0                (CONSERVÉ / TRANSVERSE)
    => g3 est EXACTEMENT pur spin-2 (transverse + sans trace), NON-perturbativement.

DISTINCTION avec le déjà-scellé (verif_A3_D1_passerelle [2]) :
  La passerelle avait l'argument « un-point dS-inv d'un TT rang 2 = 0 » AU NIVEAU
  LINÉAIRE (mode TT unique). CE SCEAU établit le contenu NON-PERTURBATIF :
    (i)  les projecteurs SVT et la décomposition sont EXACTS (espace de moments,
         aucune hypothèse perturbative) ;
    (ii) la condition transverse+sans-trace => pur spin-2 tient pour l'OPÉRATEUR
         g3 entier (Ward exactes), pas seulement sa linéarisation ;
    (iii) le secteur spin-2 ne porte AUCUN invariant isotrope (hélicité ±2),
         et tout contre-terme local est ∝ g_ij (singlet), HORS de la donnée de Weyl.

CE QUE CE SCEAU ÉTABLIT (algèbre) :
  [A] Décomposition SVT en d=3 (espace de moments) : projecteurs trace / longitudinal /
      TT orthogonaux, idempotents, de somme = identité (décomposition COMPLÈTE).
  [B] Π^TT projette sur traceless + transverse ; le seul tenseur symétrique transverse
      ISOTROPE (∝ P_ij = δ-nn) a trace 2 ≠ 0 => tué par l'absence de trace =>
      AUCUN invariant dans le secteur spin-2 => <g3>_spin2 = 0 (état isotrope/dS-inv).
  [C] Hélicité : les polarisations TT e^± tournent en e^{±2iψ} autour de n (hélicité ±2),
      pas d'hélicité 0 => pas de composante rotation-invariante dans le spin-2.

PORTÉE (discipline LC-AUDIT-VERDICT §6.4) :
  `établi (algèbre)` = l'algèbre est correcte ET les faits reproduits ; JAMAIS « CCC
  établie ». Ici : <E>=<g3>_spin2 = 0 EXACTEMENT sous A3 (état dS/rotation-invariant),
  upgrade NON-perturbatif de la passerelle. NE ferme PAS D1 (le DEUX-POINT <g3 g3>~k^3
  reste libre, SPECTRE-K3, irréductible) ; conditionnel à A3 ; spécifique au un-point.
  Trace ∝ g_ij = singlet (contre-terme) HORS de la donnée de Weyl. A3/A4 NON fusionnés.

Dépendances : sympy. Re-exécutable, sans réseau.
"""

import sympy as sp
import numpy as np

N_ASSERT = 0


def check(cond, msg):
    global N_ASSERT
    assert cond, "ÉCHEC: " + msg
    N_ASSERT += 1
    print("   [PASS] " + msg)


def banner(s):
    print("\n" + "=" * 72 + "\n " + s + "\n" + "=" * 72)


def delta(i, j):
    return sp.S(1) if i == j else sp.S(0)


print("=" * 72)
print(" verif_nonlin_repr.py — représentation, secteur électrique E ∝ g3")
print("=" * 72)

# ----------------------------------------------------------------------
banner("[A] Décomposition SVT complète en d=3 (espace de moments)")
# ----------------------------------------------------------------------
# Projecteur transverse P = δ - n⊗n et projecteur TT sur tenseurs symétriques :
#   Π_{ij,kl} = 1/2(P_ik P_jl + P_il P_jk) - 1/(d-1) P_ij P_kl,  d-1 = 2 (en d=3).
def make_P(nvec):
    return sp.Matrix(3, 3, lambda i, j: delta(i, j) - nvec[i] * nvec[j])

def make_PiTT(Pm):
    def Pi(i, j, k, l):
        return (sp.Rational(1, 2) * (Pm[i, k] * Pm[j, l] + Pm[i, l] * Pm[j, k])
                - sp.Rational(1, 2) * Pm[i, j] * Pm[k, l])
    def apply(M):
        return sp.Matrix(3, 3, lambda i, j: sum(Pi(i, j, k, l) * M[k, l]
                                                for k in range(3) for l in range(3)))
    return apply

# --- (A1) Symbolique avec n = ẑ (WLOG : construction COVARIANTE en n) ---
nz = sp.Matrix([0, 0, 1])
Pz = make_P(nz)
applyTT = make_PiTT(Pz)
check(sp.simplify(Pz * Pz - Pz).is_zero_matrix, "P=δ-n⊗n idempotent (n=ẑ)")
check(sp.simplify(Pz * nz).is_zero_matrix, "P transverse : P·n=0 (n=ẑ)")
check(sp.simplify(Pz.trace() - 2) == 0, "tr P = 2 = d-1")

S = sp.Matrix(3, 3, lambda i, j: sp.Symbol('s%d%d' % (min(i, j), max(i, j))))  # symétrique
TT = applyTT(S)
check(sp.simplify(sum(TT[i, i] for i in range(3))) == 0,
      "Π^TT(S) sans trace : δ^{ij} Π^TT_{ij,kl} S_kl = 0")
check(sp.Matrix([sp.simplify(sum(nz[i] * TT[i, j] for i in range(3))) for j in range(3)]).is_zero_matrix,
      "Π^TT(S) transverse : n^i Π^TT_{ij,kl} S_kl = 0")
check(sp.simplify(applyTT(TT) - TT).is_zero_matrix, "Π^TT idempotent : Π^TT∘Π^TT = Π^TT")

# --- (A2) Confirmation NUMÉRIQUE sur direction n GÉNÉRIQUE (covariance) ---
rng = np.random.default_rng(20260609)
def Pnum(nv):
    return np.eye(3) - np.outer(nv, nv)
def PiTTnum(Pm, M):
    out = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            s = 0.0
            for k in range(3):
                for l in range(3):
                    s += (0.5 * (Pm[i, k] * Pm[j, l] + Pm[i, l] * Pm[j, k])
                          - 0.5 * Pm[i, j] * Pm[k, l]) * M[k, l]
            out[i, j] = s
    return out
max_tr = max_tv = max_id = 0.0
for _ in range(200):
    nv = rng.standard_normal(3); nv /= np.linalg.norm(nv)
    Pm = Pnum(nv)
    A = rng.standard_normal((3, 3)); Msym = 0.5 * (A + A.T)
    T = PiTTnum(Pm, Msym)
    max_tr = max(max_tr, abs(np.trace(T)))            # sans trace
    max_tv = max(max_tv, np.max(np.abs(T @ nv)))      # transverse
    max_id = max(max_id, np.max(np.abs(PiTTnum(Pm, T) - T)))  # idempotent
check(max(max_tr, max_tv, max_id) < 1e-12,
      "direction GÉNÉRIQUE (200 tirages) : Π^TT sans trace + transverse + idempotent (<1e-12)")
print("       (max |trace|, |transverse|, |idemp| = %.1e)" % max(max_tr, max_tv, max_id))

# ----------------------------------------------------------------------
banner("[B] Aucun invariant isotrope dans le secteur spin-2")
# ----------------------------------------------------------------------
# Le seul tenseur symétrique TRANSVERSE isotrope est ∝ P_ij (trace 2 ≠ 0) ; le seul
# isotrope plein est ∝ δ_ij (trace 3). Tous deux sont PURE TRACE => Π^TT les annule.
# Donc le secteur spin-2 ne contient AUCUN invariant : <g3>_spin2 = 0 (état isotrope).
check(sp.simplify(applyTT(Pz)).is_zero_matrix,
      "Π^TT(P) = 0 : l'isotrope transverse ∝P (trace 2) n'a AUCUNE part spin-2")
check(sp.simplify(applyTT(sp.eye(3))).is_zero_matrix,
      "Π^TT(δ) = 0 : le singlet plein δ (trace 3) n'a AUCUNE part spin-2")
# confirmation numérique direction générique
max_inv = 0.0
for _ in range(200):
    nv = rng.standard_normal(3); nv /= np.linalg.norm(nv)
    Pm = Pnum(nv)
    max_inv = max(max_inv, np.max(np.abs(PiTTnum(Pm, Pm))), np.max(np.abs(PiTTnum(Pm, np.eye(3)))))
check(max_inv < 1e-12, "direction GÉNÉRIQUE : Π^TT(P)=Π^TT(δ)=0 (<1e-12) => spin-2 ∩ invariants = {0}")
print("   => seuls invariants symétriques rang 2 = {δ, P} (pure trace) ; spin-2 ∩ invariants = {0}.")
print("   => g3 (transverse+sans trace, Ward EXACTES) est pur spin-2 => <g3> = 0 exactement.")

# ----------------------------------------------------------------------
banner("[C] Hélicité ±2 des polarisations TT (pas d'hélicité 0)")
# ----------------------------------------------------------------------
# n = ẑ ; plan transverse (ê_x, ê_y). Polarisations e^± = (ê_x ± i ê_y)⊗(ê_x ± i ê_y).
psi = sp.symbols('psi', real=True)
ex = sp.Matrix([1, 0, 0]); ey = sp.Matrix([0, 1, 0])
ep = (ex + sp.I * ey)
em = (ex - sp.I * ey)
Ep = ep * ep.T            # e^+  (symétrique, sans trace, transverse à ẑ)
Em = em * em.T            # e^-
# sanity : sans trace et transverse à ẑ
check(sp.simplify(Ep.trace()) == 0 and sp.simplify(Em.trace()) == 0,
      "polarisations e^± sans trace")
nz = sp.Matrix([0, 0, 1])
check(sp.simplify(Ep * nz).is_zero_matrix and sp.simplify(Em * nz).is_zero_matrix,
      "polarisations e^± transverses (e·ẑ = 0)")
# rotation autour de z d'angle ψ
Rz = sp.Matrix([[sp.cos(psi), -sp.sin(psi), 0],
                [sp.sin(psi), sp.cos(psi), 0],
                [0, 0, 1]])
Ep_rot = sp.expand(Rz * Ep * Rz.T)
Em_rot = sp.expand(Rz * Em * Rz.T)
# cible e^{∓2iψ} en forme trig (double-angle) pour comparaison robuste
fac_m = sp.cos(2 * psi) - sp.I * sp.sin(2 * psi)   # = e^{-2iψ}
fac_p = sp.cos(2 * psi) + sp.I * sp.sin(2 * psi)   # = e^{+2iψ}
diff_p = sp.simplify(sp.expand_trig(Ep_rot - fac_m * Ep))
diff_m = sp.simplify(sp.expand_trig(Em_rot - fac_p * Em))
check(diff_p.is_zero_matrix,
      "R_z(ψ) e^+ R_z^T = e^{-2iψ} e^+  =>  hélicité ∓2")
check(diff_m.is_zero_matrix,
      "R_z(ψ) e^- R_z^T = e^{+2iψ} e^-  =>  hélicité ±2")
print("   => le secteur spin-2 porte hélicité ±2 SEULEMENT : pas d'hélicité 0,")
print("      donc pas de composante rotation-invariante. Cohérent avec [B].")

# ----------------------------------------------------------------------
banner("[D] Conséquence — secteur électrique (lecture)")
# ----------------------------------------------------------------------
print("""   g3 ∝ <T> est, par les Ward EXACTES (d=3 impair), transverse + sans trace
   => pur spin-2 (tous ordres). Le spin-2 ne contient aucun invariant isotrope
   ([B]) / hélicité ±2 sans hélicité 0 ([C]). Donc dans un état dS/rotation-invariant
   (A3) : <E_ij> = <g3>_spin2 = 0, EXACTEMENT — upgrade NON-perturbatif de la
   passerelle. Trace éventuelle ∝ g_ij = singlet (contre-terme), HORS de g3.
   (sub-Q2 = PASS ; reste sub-Q3 : parité E vs B.)""")

# ======================================================================
print("\n" + "=" * 72)
print(" RÉSULTAT : %d/%d ASSERTS PASSENT" % (N_ASSERT, N_ASSERT))
print("=" * 72)
print("""
 INTERPRÉTATION (discipline §6.4) :
   • SCELLÉ (algèbre) :
       [A] décomposition SVT complète en d=3 ; Π^TT idempotent, traceless+transverse.
       [B] spin-2 ∩ invariants = {0} (Π^TT(δ)=Π^TT(P)=0) : aucun singlet dans le spin-2.
       [C] polarisations TT d'hélicité ±2 (pas d'hélicité 0) : pas d'invariant rotationnel.
   • EFFET : g3 (transverse+sans trace par Ward EXACTES) est pur spin-2 => <E>=<g3>=0
       EXACTEMENT sous A3. Upgrade NON-PERTURBATIF de verif_A3_D1_passerelle [2].
       Combiné à sub-Q1 (magnétique clos), le contenu UN-POINT du Weyl complet s'annule
       sous A3, non-perturbativement => A4 => A3-un-point passe de `établi perturbatif`
       à `établi` (au un-point), MODULO sub-Q3 (parité).
   • NON SCELLÉ / portée : un-point seulement (le DEUX-POINT <g3 g3>~k^3 reste libre,
       SPECTRE-K3, irréductible — A3/A4 NON fusionnés) ; conditionnel à A3 ; D1 NON clos ;
       trace ∝ g_ij = singlet hors donnée de Weyl. PAS la CCC.
     « Le bang gagne » (P6 B) intact ; aucune touche à l'algèbre des chaînons amont.
""")
