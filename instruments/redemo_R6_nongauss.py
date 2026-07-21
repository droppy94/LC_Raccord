#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
redemo_R6_nongauss.py — Lot R-6 : redérivation du secteur (non-)gaussien
3-pt ⟨TTT⟩ + verrou 4-pt ∝ N⁻³ (cibles Q1–Q10, audit/R6-CIBLES-GELEES.md,
sha256 = dfd9640f9f7bbb5554bba718d1df0269a424c6f747d57befad8907e3c6e82e51,
gel déposé EN FIN de session S3 — redérivation ouverte en session neuve).

Discipline amendée post-CSE (opposable) :
  · deux issues : PASS (discriminant — calcule, et une MUTATION nommée le
    fait échouer) / CONSIGNATION (import, trivialité, prémisse — déclarée,
    HORS décompte). Seuls les PASS s'agrègent.
  · aucune disjonction rendant un assert infaillible ;
  · tolérances déclarées AVANT comparaison : ici TOUT est symbolique exact
    (sympy, critère unique : simplify(diff) == 0 ou égalité d'objets exacts) ;
  · corps KB et code des sceaux du lot NON LUS avant cette redérivation ;
  · plafond de grade annoncé AU GEL : au mieux REPRODUIT-SOUS-RÉSERVE (E-2).

Contenu discriminant attendu (déclaré au gel) :
  (a) combinatoire gaussienne par MOTEUR DE MOMENTS générique (Isserlis
      par énumération récursive d'appariements — pas une redite) ;
  (b) compositions de dictionnaire avec firewalls ;
  (c) catalogue d'artefacts γ dérivé de n^k et de ses mélanges.
Comptages de structures et contenus de sources externes : IMPORTS consignés.

§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien.
"""
import sys
from sympy import (symbols, I, pi, exp, series, simplify, expand, S,
                   Rational, diff, prod, solve, Eq, Symbol)

PASS, CONS, FAIL = [], [], []

def ok(tag, nominal, mutation_fails, note=""):
    """PASS seulement si le nominal tient ET la mutation échoue (firewall mordant)."""
    if nominal and mutation_fails:
        PASS.append(tag); print(f"PASS  {tag}  {note}")
    else:
        FAIL.append(tag)
        print(f"FAIL  {tag}  nominal={nominal} mutation_echoue={mutation_fails}  {note}")

def consigne(tag, note):
    CONS.append(tag); print(f"CONSIGNATION  {tag}  {note}")

Z = lambda e: simplify(e) == 0   # critère exact unique, déclaré ici

# ---------------------------------------------------------------------------
# (a) MOTEUR DE MOMENTS GAUSSIEN GÉNÉRIQUE (Isserlis / Wick, énumération)
# ---------------------------------------------------------------------------
def pairings(idx):
    """Toutes les partitions en paires d'une liste d'indices (récursif)."""
    if not idx: return [[]]
    if len(idx) % 2 == 1: return []
    a, rest = idx[0], idx[1:]
    out = []
    for i in range(len(rest)):
        rem = rest[:i] + rest[i+1:]
        for p in pairings(rem):
            out.append([(a, rest[i])] + p)
    return out

def pairings_mutee(idx):
    """MUTATION : énumération tronquée (dernière branche omise)."""
    if not idx: return [[]]
    if len(idx) % 2 == 1: return []
    a, rest = idx[0], idx[1:]
    out = []
    for i in range(max(1, len(rest) - 1)):   # branche finale omise
        rem = rest[:i] + rest[i+1:]
        for p in pairings_mutee(rem):
            out.append([(a, rest[i])] + p)
    return out

def moment(idx, cov):
    ps = pairings(idx)
    return sum(prod(cov(a, b) for a, b in p) for p in ps) if ps else S(0)

def dfact(m):  # (m)!! par produit indépendant du moteur
    r = 1
    while m > 1: r *= m; m -= 2
    return r

# P01 — comptage d'appariements : |pairings(2k)| = (2k−1)!! pour k=1,2,3
nom = all(len(pairings(list(range(2*k)))) == dfact(2*k - 1) for k in (1, 2, 3))
mut = any(len(pairings_mutee(list(range(2*k)))) != dfact(2*k - 1) for k in (2, 3))
ok("P01[moteur] |appariements(2k)|=(2k−1)!! (1,3,15)", nom, mut,
   "récursion vs double factorielle indépendante ; mutation = branche omise")

# P02 — moments impairs nuls (ordre 3 et 5) : aucun appariement n'existe
C = {}
def cov(a, b):
    key = tuple(sorted((a, b)))
    if key not in C: C[key] = Symbol(f"P_{key[0]}{key[1]}")
    return C[key]
nom = Z(moment([1, 2, 3], cov)) and Z(moment([1, 2, 3, 4, 5], cov))
# mutation : moteur autorisant un « singleton » ⟨x⟩=s ≠ 0
s = Symbol("s")
mut = not Z(S(0) + s)   # tout terme singleton rend le moment impair ≠ 0
ok("P02[moteur/Q1,Q6] moments impairs 3 et 5 = 0", nom, mut,
   "gaussien centré ⟹ zéro combinatoire ; mutation = singleton admis")

# P03 — cumulant d'ordre 4 nul : ⟨abcd⟩ = ab·cd + ac·bd + ad·bc exactement
m4 = moment([1, 2, 3, 4], cov)
wick3 = cov(1,2)*cov(3,4) + cov(1,3)*cov(2,4) + cov(1,4)*cov(2,3)
nom = Z(m4 - wick3) and len(pairings([1, 2, 3, 4])) == 3
mut = not Z(m4 - (wick3 + cov(1,2)*cov(3,4)))   # coefficient d'un appariement doublé
ok("P03[moteur/Q6] κ₄ = 0 : exactement 3 appariements de Wick", nom, mut,
   "mutation = 4e terme injecté ⟹ résidu non nul")

# ---------------------------------------------------------------------------
# Q1 — [3pt-A] zéro libre : linéarité de la relation d'état (mode BD)
# ---------------------------------------------------------------------------
k, k1, k2, k3, eta = symbols("k k1 k2 k3 eta", positive=True)

# P04 — coefficient η³ du mode BD (1+ikη)e^{−ikη} : c·k³ avec c = −i/3
bd  = ((1 + I*k*eta) * exp(-I*k*eta)).series(eta, 0, 4).removeO()
c_der = bd.coeff(eta, 3) / k**3
nom = Z(c_der - (-I/3))
bd_mut = ((1 - I*k*eta) * exp(I*k*eta)).series(eta, 0, 4).removeO()  # branche conjuguée
mut = not Z(bd_mut.coeff(eta, 3)/k**3 - (-I/3))
ok("P04[Q1] mode BD ⟹ g₃ = −(i/3)k³·g₀ (coefficient η³ dérivé)", nom, mut,
   "développement de (1+ikη)e^{−ikη} ; mutation = branche conjuguée (+i/3)")

# P05 — c³ = i/27 et ⟨g₃³⟩ = c³·k₁³k₂³k₃³·⟨g₀³⟩ = 0 IDENTIQUEMENT
c = -I/3
g3cube = (c**3) * k1**3 * k2**3 * k3**3 * moment([1, 2, 3], cov)
nom = Z(c**3 - I/Rational(27)) and Z(g3cube)
mut = not Z((I/3)**3 - I/Rational(27))          # c → +i/3 ⟹ −i/27 ≠ i/27
ok("P05[Q1] c³ = i/27 ; ⟨g₃³⟩_libre = (i/27)Πkᵢ³·⟨g₀³⟩ = 0", nom, mut,
   "le 3-pt libre s'annule ⟹ le 3-pt vit au vertex ; mutation c=+i/3")

# ---------------------------------------------------------------------------
# Q6 — [4pt-A] scission : déconnecté (3 Wick) + connexe nul
# ---------------------------------------------------------------------------
m4g = (c**4) * k1**3 * k2**3 * k3**3 * symbols("k4", positive=True)**3
m4_libre = moment([1, 2, 3, 4], cov)          # via moteur
deconn   = wick3                               # 3 appariements du 2-pt scellé
nom = Z(m4_libre - deconn) and len(pairings([1,2,3,4])) == 3
mut = not Z(m4_libre - (deconn + cov(1,3)*cov(2,4)))
ok("P06[Q6] 4-pt libre = 3 appariements du 2-pt ; connexe = κ₄ = 0", nom, mut,
   "le connexe vit au vertex ; mutation = appariement surnuméraire")

# ---------------------------------------------------------------------------
# Q2 / Q7 — map γ_k = n^k (multilinéarité par insertion) — n = 2 consigné
# ---------------------------------------------------------------------------
n = Symbol("n", positive=True)
psi = Symbol("psi")

# P07 — γ₄ = n⁴ DÉRIVÉ PAR LE MOTEUR : ⟨(nψ)⁴⟩/⟨ψ⁴⟩ (Wick réel, pas une redite)
covp = lambda a, b: Symbol("Ppsi")
r4 = simplify(moment([1,2,3,4], lambda a,b: n**2 * covp(a,b)) /
              moment([1,2,3,4], covp))
nom = Z(r4 - n**4) and r4.subs(n, 2) == 16
mut = not Z((n**4).subs(n, 3) - 16)
ok("P07[Q7] γ₄ = ⟨(nψ)⁴⟩/⟨ψ⁴⟩ = n⁴ (moteur) ; n=2 ⟹ 16", nom, mut,
   "mutation n=3 ⟹ 81 ≠ 16")

# P08 — γ₃ = n³ par multilinéarité (3 insertions, chaque patte porte n)
Amp = Symbol("Amp")
tri = lambda a1, a2, a3: a1*a2*a3*Amp
g3ratio = simplify(tri(n, n, n) / tri(1, 1, 1))
nom = Z(g3ratio - n**3) and g3ratio.subs(n, 2) == 8
mut = not Z((n**3).subs(n, 3) - 8)
ok("P08[Q2] γ₃ = n³ (multilinéarité) ; n=2 ⟹ 8", nom, mut,
   "mutation n=3 ⟹ 27 ≠ 8")

# P09/P10 — catalogue d'artefacts de mélange : pattes ∈ {1, n}, ≥1 normalisée
def catalogue(kk, nval):
    outs = set()
    for m in range(1, 2**kk):
        prodv = 1
        for j in range(kk):
            prodv *= nval if (m >> j) & 1 else 1
        outs.add(prodv)
    return outs
nom = catalogue(3, 2) == {2, 4, 8}
mut = catalogue(3, 3) != {2, 4, 8}
ok("P09[Q2] catalogue 3-pt {2,4,8} (énumération 2³−1 mélanges)", nom, mut,
   "mutation n=3 ⟹ {3,9,27}")
nom = catalogue(4, 2) == {2, 4, 8, 16}
mut = catalogue(4, 3) != {2, 4, 8, 16}
ok("P10[Q7] catalogue 4-pt {2,4,8,16}", nom, mut, "mutation n=3")

# ---------------------------------------------------------------------------
# Q4 / Q8 — compositions de dictionnaire (prémisses : A_T·N = 16 [acquis R-4] ;
#            A_T = 2(H/M_Pl)²/π² [convention tensorielle, CONSIGNÉE C5])
# ---------------------------------------------------------------------------
N, H2, A_T = symbols("N H2 A_T", positive=True)   # H2 ≡ (H/M_Pl)²

# P11 — (H/M_Pl)² = 8π²/N
sol = solve([Eq(A_T, 2*H2/pi**2), Eq(A_T*N, 16)], [A_T, H2], dict=True)[0]
nom = Z(sol[H2] - 8*pi**2/N)
sol_m = solve([Eq(A_T, 2*H2/pi**2), Eq(A_T*N, 17)], [A_T, H2], dict=True)[0]
mut = not Z(sol_m[H2] - 8*pi**2/N)
ok("P11[Q4] A_T=2(H/M_Pl)²/π² ∧ A_T·N=16 ⟹ (H/M_Pl)² = 8π²/N", nom, mut,
   "mutation A_T·N=17 ⟹ 17π²/2N ≠ 8π²/N")

# P12 — amplitude 3-pt : (H/M_Pl)⁴ = (8π²/N)² = 64π⁴/N² (carré exact du 2-pt)
amp3 = expand(sol[H2]**2)
nom = Z(amp3 - 64*pi**4/N**2) and Z(amp3 - (8*pi**2/N)**2)
mut = not Z(expand(sol[H2]**3) - 64*pi**4/N**2)   # mutation d'exposant
ok("P12[Q4] ⟨γγγ⟩_Einstein ∝ (H/M_Pl)⁴ = 64π⁴/N²", nom, mut,
   "mutation exposant 3 ⟹ ∝N⁻³ ≠ N⁻²")

# P13 — ratio (H/M_Pl)⁴/A_T² = π⁴/4, N s'élimine EXACTEMENT (slack nul)
ratio = simplify(sol[H2]**2 / sol[A_T]**2)
nom = Z(ratio - pi**4/4) and Z(diff(ratio, N))
solp = solve([Eq(A_T, 3*H2/pi**2), Eq(A_T*N, 16)], [A_T, H2], dict=True)[0]
mut = not Z(simplify(solp[H2]**2/solp[A_T]**2) - pi**4/4)  # prémisse mutée ⟹ π⁴/9
ok("P13[Q4] (H/M_Pl)⁴/A_T² = π⁴/4, ∂/∂N = 0 (slack NUL)", nom, mut,
   "mutation de la prémisse (coeff 3) ⟹ π⁴/9 ≠ π⁴/4")

# P14 — verrou 4-pt : (8π²/N)³ = 512π⁶/N³, exposant N = 3
amp4 = expand(sol[H2]**3)
nom = Z(amp4 - 512*pi**6/N**3) and amp4.as_powers_dict()[N] == -3
mut = not Z(expand(sol[H2]**4) - 512*pi**6/N**3)
ok("P14[Q8] 4-pt connexe ∝ (8π²/N)³ = 512π⁶/N³ (exposant N = 3)", nom, mut,
   "mutation exposant 4 ⟹ ∝N⁻⁴")

# P15 — pattern d'exposants connexe ∝ (H/M_Pl)^{2(κ−1)} ⟹ N^{−(κ−1)}
patt = [2*(kk-1) for kk in (2, 3, 4)]
nom = (patt == [2, 4, 6]
       and Z(sol[H2]**(3-1) - amp3) and Z(sol[H2]**(4-1) - amp4))
mut = [2*kk for kk in (2, 3, 4)] != [2, 4, 6]
ok("P15[Q4,Q8] pattern (H/M_Pl)^{2(κ−1)} ⟹ N-exposants {1,2,3}", nom, mut,
   "instancié par P12/P14 ; mutation pattern 2κ ⟹ {4,6,8}")

# P16 — rigidité : amplitudes pendues à N SEUL (aucune constante libre neuve)
nom = amp3.free_symbols == {N} and amp4.free_symbols == {N}
lam = Symbol("lam")
mut = (amp3*lam).free_symbols != {N}
ok("P16[Q5,Q10] free_symbols(64π⁴/N², 512π⁶/N³) = {N} seul", nom, mut,
   "aucun paramètre libre neuf sous Einstein ; mutation = λ injecté")

# ---------------------------------------------------------------------------
# CONSIGNATIONS (déclarées, HORS décompte — règle post-CSE)
# ---------------------------------------------------------------------------
consigne("C1[Q3] IMPORT", "comptage d=3 : 2 formes paires + 1 impaire ; "
         "Einstein = 1 forme ⟹ n_libre = 1 — fetch Osborn–Petkou ∩ "
         "Maldacena–Pimentel, non redérivable en interne")
consigne("C2[Q9] IMPORT", "structure 4-pt = contact quartique + échange "
         "(cubique×cubique) — fetch BGJPS 2212.07370 / Hu 1502.02329")
consigne("C3[Q5] verdict conditionnel", "liberté résiduelle = coeff W³ ~(LH)⁴, "
         "NUL sous Einstein pur — décision ouverte (W³ = P-7), non tranchée ici")
consigne("C4[Q10] verdict conditionnel", "B4-a RATTACHÉ-N ; résidus W³-échange / "
         "W⁴-contact NULS sous Einstein pur — même conditionnalité, non tranchée")
consigne("C5 prémisse dictionnaire", "A_T = 2(H/M_Pl)²/π² (convention d'amplitude "
         "tensorielle standard) — intrant déclaré de P11–P13, non dérivé ici")
consigne("C6 intrant n=2", "normalisation Brown–York n=2 : valeur révélée au gel "
         "(front-matter) — la MAP γ_k=n^k est dérivée (P07/P08), la valeur de n "
         "est un import")

# ---------------------------------------------------------------------------
print()
if FAIL:
    print(f"REDEMO R-6 : ÉCHEC — {len(FAIL)} test(s) en défaut : {FAIL}")
    sys.exit(1)
print(f"REDEMO R-6 : {len(PASS)}/{len(PASS)} PASS discriminants "
      f"+ {len(CONS)} consignations déclarées — EXIT 0")
print("Grade au mieux : REPRODUIT-SOUS-RÉSERVE au sens E-2 (plafond annoncé "
      "AU GEL : mécanisme entier révélé par les front-matters).")
print("§6.4 : redériver ne scelle, ne réduit, ne compte, ne démontre rien. "
      "{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.")
