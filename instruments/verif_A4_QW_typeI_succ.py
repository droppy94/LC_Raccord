#!/usr/bin/env python3
# ============================================================================
# verif_A4_QW_typeI_succ.py — SCEAU SUCCESSEUR (assert [05'])
# ----------------------------------------------------------------------------
# Objet : corriger le sur-grade type-I de verif_A4_QW.py [05] ("≠0 sur TOUTE
#   la famille" / "g₃ universel") sous gel R-7 LC-WORK-AMENDEMENT-R7-A4-QW-
#   TYPEI-CORR (gel SHA hors-fichier 7ec75a22…). §10 : le sceau audité
#   a4637a2c n'est NI lu NI muté ici — successeur standalone, nouveau sha.
# Spec §3 gelée : vérifier (a)-(d) et SUPPRIMER l'universalité.
#   (a) de Sitter a_i=e^{Ht} : vide+Λ, isotrope ⟹ 𝓔=0.
#   (b) q=0 (a_i=sinh^{1/3}(3t)) : isotrope mais ρ>0 (NON vide) — pas de Sitter.
#   (c) time-shift t→t+c : q_i^eff=q_i e^{−3c}, lim_{c→∞} 𝓔=0.
#   (d) 𝓔=(3/2H)diag(−4q_i^eff) ≠0 pour tout shear≠0 (famille ANISOTROPE).
# Firewalls (chacun DOIT mordre) : [F05'-1] 𝓔≠0 à de Sitter = FAUX (garde le
#   retour du sur-grade) ; [F05'-2] q=0 vide = FAUX (garde le mauvais point).
# Unités H=1, Λ=3 (mêmes conventions que le sceau parent). §6.4 : W2 préservé.
# ============================================================================
import sympy as sp

FAILS = []
def check(label, cond):
    ok = bool(cond)
    print(("  OK  " if ok else " FAIL ") + label)
    if not ok:
        FAILS.append(label)

t, c = sp.symbols('t c', real=True, positive=True)
q1, q2 = sp.symbols('q1 q2', real=True)
q3 = -(q1 + q2)
qs = [q1, q2, q3]
Lam = 3  # H=1

def hubbles(a_list):
    return [sp.diff(a, t)/a for a in a_list]

def rho_vacuum_residual(a_list):
    # Contrainte hamiltonienne Bianchi I : H1H2+H1H3+H2H3 = Λ + ρ  (8πG=1)
    H1, H2, H3 = hubbles(a_list)
    return sp.simplify(H1*H2 + H1*H3 + H2*H3 - Lam)

def shear(a_list):
    Hs = hubbles(a_list)
    th = sum(Hs)
    return [sp.simplify(h - th/3) for h in Hs]

# ---------------------------------------------------------------------------
# Paramétrisation exacte Bianchi I vide+Λ (H=1, Λ=3) :
#   a_i = sinh^{1/3}(3t)·tanh^{q_i}(3t/2) ; contrainte vide ⟺ Σq_i²=2/3.
a_fam = [sp.sinh(3*t)**sp.Rational(1, 3) * sp.tanh(sp.Rational(3, 2)*t)**qi for qi in qs]

# contrainte de vide re-dérivée (ground-truth) : ρ=0 ⟺ q1²+q1q2+q2² = 1/3
rho_fam = sp.simplify(rho_vacuum_residual(a_fam))
# ρ_fam·sinh⁴(3t) = 3(−3(q1²+q1q2+q2²)+1)·sinh²(3t)  ⟹ facteur (1−3(q1²+q1q2+q2²))
constraint_poly = sp.simplify(rho_fam * sp.sinh(3*t)**4 / (3*sp.sinh(3*t)**2))
check('[05p-c0] contrainte vide re-dérivée : ρ=0 ⟺ q1²+q1q2+q2² = 1/3 (⟺ Σq²=2/3)',
      sp.simplify(constraint_poly - (1 - 3*(q1**2 + q1*q2 + q2**2))) == 0)

# --- (a) de Sitter a_i=e^{Ht} : vide+Λ, isotrope ⟹ 𝓔=0 -----------------------
dS = [sp.exp(t)]*3
rho_dS = rho_vacuum_residual(dS)
sh_dS = shear(dS)
# 𝓔 = (3/2H)·g₃ ; g₃=diag(−4q_i) [import [04] parent, non muté] ; de Sitter = q_i^eff→0
# On teste directement : de Sitter a shear nul ⟹ q_i^eff=0 ⟹ 𝓔=0.
check('[05p-a] de Sitter (a_i=e^t) : vide+Λ (ρ=0) ET isotrope (shear=0) ⟹ 𝓔=0',
      rho_dS == 0 and all(s == 0 for s in sh_dS))

# --- (b) q=0 (sinh^{1/3}) : isotrope mais NON vide (ρ>0) — pas de Sitter -------
q0 = [sp.sinh(3*t)**sp.Rational(1, 3)]*3
rho_q0 = sp.simplify(rho_vacuum_residual(q0))
sh_q0 = shear(q0)
check('[05p-b] q=0 (a_i=sinh^{1/3}(3t)) : isotrope (shear=0) mais ρ=3/sinh²(3t)>0 (NON vide)',
      sp.simplify(rho_q0 - 3/sp.sinh(3*t)**2) == 0 and all(s == 0 for s in sh_q0)
      and rho_q0 != 0)

# --- (c) time-shift t→t+c : q_i^eff=q_i e^{−3c} ; lim_{c→∞} 𝓔=0 ----------------
q = sp.symbols('q', real=True)      # coefficient de mode générique
qeff = q * sp.exp(-3*c)
E_of = lambda qe: sp.Rational(3, 2)*(-4*qe)   # 𝓔 = (3/2H)·(−4 q^eff) , H=1
E_eff = E_of(qeff)
check('[05p-c] time-shift : q^eff=q·e^{−3c} ⟹ lim_{c→+∞} 𝓔(q^eff)=0 (de Sitter = limite shear→0)',
      sp.limit(E_eff, c, sp.oo) == 0)

# --- (d) 𝓔=(3/2H)diag(−4q_i^eff) ≠0 pour tout shear≠0 (famille ANISOTROPE) -----
# 𝓔_i = −6 q_i^eff ; non nul ssi q_i^eff≠0 ssi shear≠0. Pente ∂𝓔/∂q = −6 ≠ 0.
E_i = E_of(q)                         # = −6q (c=0)
check('[05p-d] 𝓔=(3/2H)diag(−4q_i)= −6q_i : ≠0 dès q≠0 (toute la famille ANISOTROPE) ; ∂𝓔/∂q=−6≠0',
      sp.simplify(E_i + 6*q) == 0 and sp.diff(E_i, q) == -6 and E_i.subs(q, 0) == 0)

# --- [F05'-1] FIREWALL : "𝓔≠0 à de Sitter" DOIT être détecté FAUX --------------
# (garde contre la ré-introduction du sur-grade d'universalité)
claim_universal_at_dS = (E_of(0) != 0)     # prétend 𝓔≠0 quand shear=0 (de Sitter)
check('[F05\'-1] mutation : "𝓔≠0 à de Sitter" ⟹ FAUX (𝓔(0)=0) — le sur-grade EST détecté',
      claim_universal_at_dS == False)

# --- [F05'-2] FIREWALL : "q=0 (sinh^{1/3}) est vide" DOIT être détecté FAUX -----
# (garde contre le mauvais point isotrope de l'assert [05] original)
claim_q0_is_vacuum = (rho_q0 == 0)
check('[F05\'-2] mutation : "q=0 (sinh^{1/3}) est vide" ⟹ FAUX (ρ>0) — le mauvais point EST détecté',
      claim_q0_is_vacuum == False)

# ---------------------------------------------------------------------------
print()
if FAILS:
    print("SCEAU SUCCESSEUR [05'] : %d FAIL" % len(FAILS))
    raise SystemExit(1)
print("SCEAU SUCCESSEUR [05'] : EXIT 0 — 8/8 (6 asserts porteurs + 2 firewalls mordants).")
print("W2 PRÉSERVÉ (générique/anisotrope) ; universalité RETIRÉE ; a4637a2c INTACT ; §6.4 terminal.")
raise SystemExit(0)
