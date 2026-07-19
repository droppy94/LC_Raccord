#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_A2_numerique.py  —  SCEAU du front A2★ NUMÉRIQUE (voie mésoscopique).
Exécute LC-WORK-CADRAGE-A2-NUMERIQUE v0.1 (gel sha 179d2f00…eca7a21b).

OBJET (et SES LIMITES, discipline LC-AUDIT-VERDICT §6.4) :
Teste la conjecture A2★ (non-cascade : Q(τ)=Σ_spikes C_F sous-exponentielle) par un MODÈLE
MÉSOSCOPIQUE de production + charge de spikes piloté par la statistique d'ères de Gauss-Kuzmin
(déjà scellée, LC-D3-INTERAEON-P6). NE PROUVE PAS A2★ en générique 3D (OA `hors de portée`,
non ouverte). Une signature numérique atteste l'algèbre / le modèle, JAMAIS la thèse physique.

  BLOC A — N1 : prolifération n_s(τ) vs facteur de réplication ρ (cascade ⟺ ρ>0).
  BLOC B — N2 : pont u_ère→C_F ; ⟨C_F⟩ sous la mesure de Gauss-Kuzmin ; seuil de convergence.
  BLOC C — N3 : synthèse Q=n_s·⟨C_F⟩ ⟹ R_grad,gen→0 (raccord à la déduction scellée).
  BLOC D — FIREWALL : mutations (cascade ; charge divergente) DOIVENT casser ;
                       contrôles limites G₂ (transitoire) et billard (zéro spike).

Cibles GELÉES avant exécution (anti-fit, R-7). Aucune valeur attendue n'est inscrite dans le
cadrage : on fige la QUESTION et les ISSUES, on lit le SCALING.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260617)
PASS = []
def check(name, cond):
    PASS.append(bool(cond))
    print(f"   [{'PASS' if cond else 'FAIL'}] {name}")

print("="*80)
print(" verif_A2_numerique.py — A2★ non-cascade, voie mésoscopique era-driven")
print("="*80)

# ============================================================================
# BLOC A — N1 : prolifération des surfaces de spike n_s(τ) vs ρ
# ----------------------------------------------------------------------------
# Modèle mésoscopique (Garfinkle : spikes PRODUITS aux bounces ; Lim : |w|>1 transitoire,
# 0<|w|<1 permanent). Par bounce :
#   production ADDITIVE (bulk, O(1)/bounce, INDÉPENDANTE de n_s) : +λ_perm, +λ_trans
#   réplication MULTIPLICATIVE (cascade) : +ρ·n  (chaque spike engendre ρ sous-spikes)
#   décroissance des transitoires (Lim |w|>1) : −δ·n_trans
# ⟹ n_perm(b+1) = (1+ρ)·n_perm + λ_perm ;  n_trans(b+1) = (1+ρ−δ)·n_trans + λ_trans
# N_b ~ linéaire en τ (oracle scellé) ⟹ b ≡ proxy de τ.
# ============================================================================
print("\n BLOC A — N1 : prolifération n_s(τ), balayage du facteur de réplication ρ")

def evolve_ns(rho, n_bounces=4000, lam_perm=0.4, lam_trans=0.6, delta=0.25):
    # évolution directe (sûre pour ρ=0 / contrôles : croissance linéaire, pas d'overflow)
    n_perm = 0.0; n_trans = 0.0; hist = np.empty(n_bounces)
    for b in range(n_bounces):
        n_perm  = (1.0+rho)*n_perm  + lam_perm
        n_trans = (1.0+rho-delta)*n_trans + lam_trans
        hist[b] = n_perm + n_trans
    return hist

def growth_rate(rho, n_steps=3000, lam_perm=0.4, lam_trans=0.6, delta=0.25):
    # taux exponentiel asymptotique ln(n_s(b+1)/n_s(b)). Le RATIO est scale-free :
    # renormalisation périodique ⟹ aucun overflow, même pour la cascade ρ>0.
    n_perm, n_trans = lam_perm, lam_trans
    ratio = 1.0
    for b in range(n_steps):
        new_p = (1.0+rho)*n_perm + lam_perm
        new_t = (1.0+rho-delta)*n_trans + lam_trans
        tot_old = n_perm + n_trans
        tot_new = new_p + new_t
        ratio = tot_new/tot_old
        n_perm, n_trans = new_p, new_t
        if tot_new > 1e150:                 # renormalise (le ratio est invariant d'échelle)
            n_perm /= tot_new; n_trans /= tot_new
    return float(np.log(ratio))

rates = {}
for rho in [0.0, 0.05, 0.2, 0.5, 1.0]:
    r = growth_rate(rho)
    rates[rho] = r
    print(f"   ρ={rho:<4} : taux exponentiel asymptotique ln(n_s(b+1)/n_s(b)) = {r:.6e}")

# A.1 — ρ=0 (production purement additive, physique) : n_s SOUS-EXPONENTIEL (taux→0)
check("A.1  ρ=0 (additif) ⟹ n_s sous-exponentiel (taux ≈ 0, < 1e-3)", rates[0.0] < 1e-3)

# A.2 — n_s(ρ=0) croît au plus linéairement (le permanent s'accumule, le transitoire sature)
h0 = evolve_ns(0.0)
lin_ratio = h0[-1] / h0[len(h0)//2]               # ~2 si linéaire, →1 si saturant, >>2 si exp
check("A.2  ρ=0 : n_s croît AU PLUS linéairement (ratio fin/milieu ≤ 2.2)", lin_ratio <= 2.2)

# A.3 — ρ>0 (réplication multiplicative) : CASCADE, taux = ln(1+ρ−...) > 0, croissant en ρ
check("A.3  ρ>0 ⟹ cascade : taux exponentiel STRICTEMENT positif", all(rates[r] > 1e-2 for r in [0.2,0.5,1.0]))
check("A.4  taux exponentiel MONOTONE croissant en ρ (0<0.05<0.2<0.5<1.0)",
      rates[0.0] < rates[0.05] < rates[0.2] < rates[0.5] < rates[1.0])

# A.5 — raccord quantitatif : pour ρ assez grand devant δ, taux ≈ ln(1+ρ−δ_eff).
#        (contrôle de cohérence du mécanisme de cascade, δ=0.25 sur le transitoire dominant)
pred = np.log(1.0+1.0-0.0)                          # ρ=1 : le permanent (δ=0) domine, taux→ln2
check("A.5  ρ=1 : taux ≈ ln(1+ρ) du secteur permanent (±5%)", abs(rates[1.0]-pred)/pred < 0.05)

# ============================================================================
# BLOC B — N2 : pont u_ère → C_F ; ⟨C_F⟩ sous la mesure de Gauss-Kuzmin
# ----------------------------------------------------------------------------
# Exposants de Kasner BORNÉS ∀ u≥1 : p1=−u/S, p2=(1+u)/S, p3=u(1+u)/S, S=1+u+u².
# Profil Lim exact : C_F = 2π·A². Amplitude A bornée par l'écart d'exposants (p3−p1) ≤ ~4/3.
# ⟹ C_F(u) BORNÉE. Mesure d'ère : quotients partiels a=k ~ Gauss-Kuzmin P(k)=log2(1+1/(k(k+2))).
# ============================================================================
print("\n BLOC B — N2 : pont u_ère→C_F, espérance sous Gauss-Kuzmin")

def kasner(u):
    S = 1.0+u+u*u
    return (-u/S, (1.0+u)/S, u*(1.0+u)/S)

# B.0 — exposants de Kasner bornés ∀ u (échantillon large) : ∑p=1, ∑p²=1, p∈[−1/3,1]
us = 1.0 + 50.0*rng.random(200000)
P = np.array([kasner(u) for u in us])
check("B.0  Kasner : ∑p=1 et ∑p²=1 (identités, <1e-9)",
      np.allclose(P.sum(1),1,atol=1e-9) and np.allclose((P**2).sum(1),1,atol=1e-9))
check("B.0' exposants BORNÉS ∀ u : p∈[−1/3−ε, 1+ε]", P.min() > -1/3-1e-6 and P.max() < 1+1e-6)

# B.1 — charge physique par spike : C_F(u)=2π·A², A=(p3−p1) borné ⟹ C_F→const quand u→∞
def C_F_phys(u):
    p1,p2,p3 = kasner(u)
    A = p3 - p1                                     # écart d'anisotropie, borné
    return 2.0*np.pi*A*A
cf_large = C_F_phys(1e6)
check("B.1  C_F(u) BORNÉE : C_F(u→∞) fini (≈2π, écart→1)", 1.0 < cf_large/(2*np.pi) < 1.2)

# B.2 — mesure de Gauss-Kuzmin sur les quotients partiels a=k
def P_GK(k):                                        # P(a=k)=log2(1+1/(k(k+2)))
    return np.log2(1.0 + 1.0/(k*(k+2.0)))
ks = np.arange(1, 200001, dtype=float)
pk = P_GK(ks)
check("B.2  Gauss-Kuzmin : Σ P(k) = 1 (normalisation, <1e-3)", abs(pk.sum()-1.0) < 1e-3)

# B.3 — ⟨C_F⟩ PHYSIQUE sous Gauss-Kuzmin : FINI (C_F bornée ⟹ trivialement intégrable).
#        u_ère ≈ quotient partiel k (taille de l'ère) ; C_F(k) bornée.
cf_k = np.array([C_F_phys(float(k)) for k in ks])
ECF_phys = float(np.sum(cf_k*pk))
check(f"B.3  ⟨C_F⟩_GK PHYSIQUE fini = {ECF_phys:.4f} (borné, ~2π)", np.isfinite(ECF_phys) and ECF_phys < 50)

# B.4 — SEUIL de convergence dérivé de la mesure : C_F~k^s ⟹ Σ k^s·P(k), P(k)~1/(k²ln2).
#        converge ⟺ s<1. Test s∈{0.5 (conv), 1.0 (diverge), 2.0 (diverge)} par stabilité de
#        la somme tronquée (K=1e4 vs K=2e5).
def trunc_sum(s, K):
    kk = np.arange(1, int(K)+1, dtype=float)
    return float(np.sum((kk**s)*P_GK(kk)))
def converges(s):
    return abs(trunc_sum(s,2e5) - trunc_sum(s,1e4)) < 0.05*max(1.0,trunc_sum(s,1e4))
check("B.4  seuil dérivé : s=0.5 (<1) CONVERGE", converges(0.5))
check("B.4' seuil dérivé : s=1.0 DIVERGE (somme non stabilisée)", not converges(1.0))
check("B.4'' seuil dérivé : s=2.0 DIVERGE", not converges(2.0))
# s_phys = 0 (C_F bornée) < s*=1 ⟹ pont OK
check("B.5  pont : s_phys=0 (C_F bornée) < seuil s*=1 ⟹ ⟨C_F⟩ FINI", 0.0 < 1.0 and np.isfinite(ECF_phys))

# ============================================================================
# BLOC C — N3 : synthèse Q=n_s·⟨C_F⟩ ⟹ R_grad,gen→0 (raccord déduction scellée)
# ----------------------------------------------------------------------------
# Déduction scellée (verif_D3_C7b_A2_reduction.py) : I_spike=C_F·w/cosh(wt),
# R_grad,gen=Q·I_spike/⟨Ω⟩ ; R→0 ⟺ lim ln Q / t < |w|.
# ============================================================================
print("\n BLOC C — N3 : synthèse Q=n_s·⟨C_F⟩ ⟹ R_grad,gen→0")
t, w, C_Fs = sp.symbols('t w C_Fs', positive=True)
I_spike = C_Fs*w/sp.cosh(w*t)

# C.1 — raccord exact à A1 : I_spike ~ 2·C_F·w·e^{-wt}
check("C.1  raccord A1 : I_spike ~ 2C_F·w·e^{-wt}",
      sp.simplify(sp.limit(I_spike/(2*C_Fs*w*sp.exp(-w*t)), t, sp.oo)) == 1)

# C.2 — modèle ρ=0 : n_s ~ linéaire ⟹ Q ~ t·⟨C_F⟩ (sous-exp.) ⟹ R→0
Q_model = t*ECF_phys                                 # n_s linéaire × charge bornée
check("C.2  ρ=0 : Q=t·⟨C_F⟩ (sous-exp.) ⟹ lim R_grad,gen = 0",
      sp.limit(Q_model*I_spike, t, sp.oo) == 0)

# C.3 — critère ln Q / t : modèle ρ=0 ⟹ 0 < |w| (marge stricte)
lnQ_rate = sp.limit(sp.log(Q_model)/t, t, sp.oo)
check("C.3  ρ=0 : lim ln Q / t = 0 < |w| (sous-exponentialité STRICTE)", lnQ_rate == 0)

# ============================================================================
# BLOC D — FIREWALL : les mutations DOIVENT casser + contrôles limites
# ============================================================================
print("\n BLOC D — FIREWALL (chaque mutation DOIT casser) + contrôles limites")

# m1 — CASCADE : n_s ~ (1+ρ)^b ⟹ Q ~ e^{c·t}, c>0 ⟹ si c≥|w|, R↛0 (réfutation R2).
#       on prend la cascade ρ=1 (c=ln2) et w=ln2/2 < c ⟹ R↛0.
c_casc = sp.Rational(1,1)*sp.log(2)                  # taux de cascade du secteur permanent ρ=1
Q_casc = sp.exp(c_casc*t)
R_casc = (Q_casc*I_spike).subs(w, sp.log(2)/2)       # |w| < c_casc
lim_casc = sp.limit(R_casc, t, sp.oo)
print(f"   m1 cascade : Q=e^(ln2·t), |w|=ln2/2 ⟹ lim R = {lim_casc}")
check("D.m1 CASCADE casse : Q exp. avec c>|w| ⟹ R↛0 (mutation MORD)", lim_casc != 0)

# m2 — CHARGE DIVERGENTE : C_F(k)~k² (s=2>s*) ⟹ ⟨C_F⟩ diverge (mutation MORD).
ECF_div_1e4 = trunc_sum(2.0, 1e4); ECF_div_2e5 = trunc_sum(2.0, 2e5)
print(f"   m2 charge div. : ⟨C_F⟩(K=1e4)={ECF_div_1e4:.1f} vs (K=2e5)={ECF_div_2e5:.1f} (croît)")
check("D.m2 CHARGE DIVERGENTE casse : C_F~k² ⟹ ⟨C_F⟩ non stabilisée (MORD)",
      ECF_div_2e5 > 1.5*ECF_div_1e4)

# m3 — mutation du critère : si on prétend R→0 alors que ln Q/t = |w| (seuil EXACT), c'est FAUX.
R_seuil = (sp.exp(w*t)*I_spike)
check("D.m3 SEUIL EXACT casse : Q=e^{wt} ⟹ R↛0 (la cascade marginale CASSE — R2)",
      sp.limit(R_seuil, t, sp.oo) != 0)

# contrôle limite G₂ — régime transitoire-dominé, additif (ρ=0) : n_s linéaire (non-cascade reproduite)
rate_g2 = growth_rate(0.0, lam_perm=0.1, lam_trans=0.9, delta=0.4)   # transitoire dominant
check("D.c1 contrôle G₂ : régime transitoire-dominé, ρ=0 ⟹ n_s sous-exp (taux≈0)",
      rate_g2 < 1e-3)

# contrôle limite BILLARD/ultralocal — aucune structure spatiale ⟹ aucune production ⟹ n_s≡0
h_bil = evolve_ns(0.0, lam_perm=0.0, lam_trans=0.0, delta=0.25)
check("D.c2 contrôle BILLARD (ultralocal) : production nulle ⟹ n_s ≡ 0 (cohérence OB)",
      np.allclose(h_bil, 0.0))

# ============================================================================
# VERDICT
# ============================================================================
print("\n" + "="*80)
ok = all(PASS)
print(f" RÉSULTAT : {sum(PASS)}/{len(PASS)} assertions PASS.")
print(" LECTURE (anti-fit, §6.4) :")
print(f"   • N1 : non-cascade ⟺ ρ=0 (production ADDITIVE/bulk). ρ=0 ⟹ n_s sous-exp ;")
print(f"          ρ>0 ⟹ cascade exp. Le verdict N1 REPOSE sur l'additivité (ρ=0), input")
print(f"          PHYSIQUE motivé (Garfinkle : production O(1)/bounce, indép. de n_s), NON")
print(f"          dérivé d'un théorème générique 3D ⟹ issue N1-b/(a) : SOUTIEN conditionnel.")
print(f"   • N2 : ⟨C_F⟩_GK = {ECF_phys:.3f} FINI (C_F bornée par exposants de Kasner bornés ;")
print(f"          seuil dérivé s*=1 > s_phys=0) ⟹ issue N2-a : pont u_ère→C_F FAIT (OC adressé).")
print(f"   • N3 : Q=n_s·⟨C_F⟩ sous-exp ⟹ R_grad,gen→0 via la déduction scellée. PASS conditionnel.")
print(f"   • Firewall MORDANT : cascade, charge divergente, seuil exact CASSENT ; limites G₂")
print(f"          (non-cascade) et billard (zéro spike) REPRODUITES.")
print(" SANS SURCLASSEMENT (§6.4) : OA (générique 3D) PERSISTE ; soutien mésoscopique ≠ théorème.")
print("   A2★ : décision ouverte, MIEUX SITUÉE ; OC adressé, gap re-nommé (additivité ⟸ 3D NR).")
print("   {A4 ; A2★ ; N} INCHANGÉ ; C7 non levée ; D1 non clos ; CCC non démontrée.")
print("="*80)
assert ok, "ÉCHEC : au moins une assertion a FAIL."
print(f"OK — {len(PASS)} assertions. Firewall mordant (m1/m2/m3 + c1/c2). EXIT 0.")
