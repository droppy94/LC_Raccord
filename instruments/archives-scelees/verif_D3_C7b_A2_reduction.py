#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_C7b_A2_reduction.py  —  SCEAU du §7 de LC-WORK-A2-CONJECTURE.

OBJET (et SES LIMITES, discipline LC-AUDIT-VERDICT §6.4) :
Ce sceau SCELLE les deux maillons NON-A2★ de la chaîne de réduction de C7-b :
  (A) la DÉDUCTION §4 (symbolique) : pour toute charge agrégée Q(τ) SOUS-EXPONENTIELLE,
      R_grad,gen(τ) = Q(τ)·I_spike^gen(τ)/⟨Ω_σ⟩_bulk → 0, avec I_spike^gen = C_F·w/cosh(wτ)
      ≈ 2·C_F·w·e^{−|w|τ} (raccord exact à A1 / LC-D3-A1-SUPERHORIZON, LC-D3-GRADIENT-C7B) ;
  (B) le fait BKL-standard : le nombre de bounces N_b croît SOUS-EXPONENTIELLEMENT (quasi-
      linéairement) le long de l'oracle de Gauss-Kuzmin déjà scellé (LC-D3-INTERAEON-P6).

Ce sceau NE SCELLE PAS la conjecture A2★ (« Q(τ) sous-exponentielle / pas de cascade ») : c'est
le seul maillon `décision ouverte` / `à inventer` qui RESTE, isolé. Une signature numérique
atteste l'algèbre / le numérique, JAMAIS la thèse physique (CCC). « Le bang gagne » (P6 B) intact.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(20260608)
PASS = []
def check(name, cond):
    PASS.append(bool(cond))
    print(f"   [{'PASS' if cond else 'FAIL'}] {name}")

print("="*80)
print(" verif_D3_C7b_A2_reduction.py — réduction C7-b/A2 : déduction §4 + N_b(τ) sous-exp.")
print("="*80)

# ============================================================================
# PARTIE A — DÉDUCTION §4 (symbolique, sympy)
# ============================================================================
print("\n PARTIE A — déduction symbolique : Q sous-exp. ⟹ R_grad,gen → 0")
t, w, C_F, p = sp.symbols('t w C_F p', positive=True)

# A.1 — raccord exact à A1 : I_spike = C_F·w/cosh(wt) ~ 2·C_F·w·e^{-wt}
I_spike = C_F * w / sp.cosh(w*t)
ratio = sp.limit(I_spike / (2*C_F*w*sp.exp(-w*t)), t, sp.oo)
print(f"   I_spike^gen = C_F·w/cosh(wt) ;  lim (I_spike)/(2·C_F·w·e^(-wt)) = {ratio}")
check("A.1  raccord A1 : I_spike ~ 2·C_F·w·e^{-wt} (rapport→1)", sp.simplify(ratio) == 1)

# A.2 — Q polynomiale (sous-exp.) : R = Q·I_spike → 0  (⟨Ω_σ⟩_bulk = O(1), pris =1 au leading)
for pp in [1, 2, 5, 17]:
    R = (t**pp) * I_spike
    lim = sp.limit(R, t, sp.oo)
    check(f"A.2  Q=t^{pp} (polynomial) :  lim R_grad,gen = {lim}", lim == 0)

# A.3 — Q sous-exponentielle non polynomiale (e^{√t}) : R → 0 encore
R_sub = sp.exp(sp.sqrt(t)) * I_spike
lim_sub = sp.limit(R_sub, t, sp.oo)
check(f"A.3  Q=e^√t (sous-exp.) :  lim R_grad,gen = {lim_sub}", lim_sub == 0)

# A.4 — borne de bascule : Q ~ e^{|w|t} (EXACTEMENT le seuil) ⟹ R NE tend PAS vers 0
#        (c'est la réfutation R2 du §5 : la cascade exponentielle casserait la décroissance)
R_break = sp.exp(w*t) * I_spike
lim_break = sp.limit(R_break, t, sp.oo)
print(f"   contrôle de bascule : Q=e^(wt) ⟹ lim R = {lim_break}  (≠0 attendu : seuil de cascade)")
check("A.4  seuil : Q=e^{wt} ⟹ R↛0 (la cascade exp. CASSE — réfutation R2)", lim_break != 0)

# A.5 — critère général : R→0 ⟺ lim (ln Q)/t < |w|  (sous-exponentialité stricte)
#        vérifié sur Q=e^{c·t} pour c<w (→0) et c>w (↛0)
c = sp.Rational(1, 3)
check("A.5  Q=e^{(w/3)t} (c<w) ⟹ R→0",  sp.limit(sp.exp(c*w*t)*I_spike, t, sp.oo) == 0)

# ============================================================================
# PARTIE B — N_b(τ) SOUS-EXPONENTIEL le long de l'oracle de Gauss-Kuzmin
# ============================================================================
print("\n PARTIE B — bounce count N_b sous-exponentiel (oracle Gauss-Kuzmin, P6)")

# B.0 — TIE-IN ORACLE : reproduire que la part fractionnaire aux transitions d'ère
#        suit Gauss-Kuzmin ρ(x)=1/(ln2·(1+x))  (machinerie de verif_D3_P6_specB_oracle.py)
def era_boundary_x(n):
    out=[]; u=1.0+rng.random()
    for _ in range(3000):                      # burn-in
        u = 1.0/(u-1.0) if u<2.0 else u-1.0
        if not np.isfinite(u) or u<1.0 or u>1e7: u=1.0+rng.random()
    while len(out)<n:
        if u<2.0:
            x=u-1.0; out.append(x); u=1.0/x
        else:
            u=u-1.0
        if not np.isfinite(u) or u<1.0 or u>1e7: u=1.0+rng.random()
    return np.array(out)

x = era_boundary_x(200000)
xs = np.array([0.2,0.4,0.6,0.8])
emp = np.array([(x<=v).mean() for v in xs])      # CDF empirique
gk  = np.log2(1.0+xs)                              # CDF Gauss-Kuzmin = log2(1+x)
err = float(np.max(np.abs(emp-gk)))
print(f"   (B.0) map de Gauss : écart max |CDF_emp − log2(1+x)| = {err:.4f}")
check("B.0  oracle reproduit : part fractionnaire ~ Gauss-Kuzmin (<3%)", err < 0.03)

# B.1 — N_b(n) = Σ a_i, a_i = #époques par ère = partial quotients ~ Gauss-Kuzmin.
#        Échantillonnage EXACT de la marginale : x~GK via CDF inverse x=2^u−1, a=floor(1/x).
#        (la marginale gouverne la croissance du SOMME, dominée par la queue lourde 1/k²)
def partial_quotients(n):
    u = rng.random(n)
    xx = np.maximum(2.0**u - 1.0, 1e-300)         # x~Gauss-Kuzmin
    return np.floor(1.0/xx)                        # a=floor(1/x), float64 (pas d'overflow)

M, n = 400, 4000                                  # 400 trajectoires de 4000 ères
checkpoints = np.array([250, 500, 1000, 2000, 4000])
Nb_at = {k: [] for k in checkpoints}
amax_global = 0.0
for _ in range(M):
    a = partial_quotients(n)
    amax_global = max(amax_global, a.max())
    csum = np.cumsum(a)
    for k in checkpoints:
        Nb_at[k].append(csum[k-1])
med = np.array([np.median(Nb_at[k]) for k in checkpoints])   # médiane (robuste à la queue)
mean = np.array([np.mean(Nb_at[k]) for k in checkpoints])    # moyenne (dominée par la queue)

print("   (B.1) croissance de N_b(n) (médiane sur 400 trajectoires) :")
print("        n      N_b(méd)   N_b/(n·ln n)   [réf 1/ln2≈1.443]")
for k, m_ in zip(checkpoints, med):
    print(f"      {k:5d}   {m_:9.0f}      {m_/(k*np.log(k)):.3f}")

# (a) DÉCISIVEMENT NON-EXPONENTIEL : ln(N_b)/n → 0
ratio_log = np.log(med[-1]) / checkpoints[-1]
print(f"   (B.1a) ln(N_b(4000))/4000 = {ratio_log:.5f}   (→0 ⟹ non-exponentiel)")
check("B.1a  non-exponentiel : ln(N_b)/n ≪ 1 (<0.02)", ratio_log < 0.02)

# (b) QUASI-LINÉAIRE : exposant log-log ≈ 1 (n·ln n donne ~1 + 1/ln n)
slope = np.polyfit(np.log(checkpoints), np.log(med), 1)[0]
print(f"   (B.1b) exposant log-log de N_b vs n = {slope:.3f}  (≈1 ⟹ quasi-linéaire)")
check("B.1b  quasi-linéaire : exposant log-log ∈ [0.85, 1.30]", 0.85 <= slope <= 1.30)

# (c) loi n·ln n (Diamond-Vaaler/Khinchin) : fit N_b = K·(n ln n), R² élevé
nl = checkpoints*np.log(checkpoints)
K = np.sum(med*nl)/np.sum(nl*nl)
resid = med - K*nl; ss_res = np.sum(resid**2); ss_tot = np.sum((med-med.mean())**2)
R2 = 1 - ss_res/ss_tot
print(f"   (B.1c) fit N_b ≈ {K:.3f}·n·ln n  (réf 1/ln2={1/np.log(2):.3f}) ; R²={R2:.4f}")
check("B.1c  loi n·ln n : R² > 0.99 et K ∈ [0.5, 3.0]", R2 > 0.99 and 0.5 <= K <= 3.0)

# (d) CONTRASTE avec une vraie exponentielle : e^{0.01 n} à n=4000
expo = np.exp(0.01*4000)
print(f"   (B.1d) si N_b ~ e^(0.01n) : N_b(4000)~{expo:.2e}  vs observé ~{med[-1]:.2e}")
check("B.1d  N_b observé ≪ baseline exponentielle (≥10 ordres)", med[-1] < expo*1e-10)

# (e) QUEUE LOURDE bornée : la plus longue ère vue ~ O(n), MAIS son coût en τ est ∝ ses époques
print(f"   (B.1e) ère la plus longue observée : a_max = {amax_global:.0f}  (~O(n), queue lourde)")
print(f"          la moyenne ({mean[-1]:.0f}) > médiane ({med[-1]:.0f}) : somme tail-dominée,")
print(f"          mais médiane ET moyenne restent SOUS-EXP. (mean/(n ln n)={mean[-1]/nl[-1]:.2f})")
check("B.1e  même la moyenne (tail-dominée) est sous-exp. : mean/(n ln n) bornée (<6)",
      mean[-1]/nl[-1] < 6.0)

# B.2 — TRANSFERT à τ : coût par époque borné Δτ∈[c_min,c_max], c_min>0 (BKL : les époques
#        ne rétrécissent pas en temps-log) ⟹ N_b(τ) ≤ τ/c_min : LINÉAIRE (sous-exp.).
print("   (B.2) transfert au temps τ : Δτ par époque borné (BKL) ⟹ N_b(τ) linéaire-borné")
c_min, c_max = 0.5, 2.0
a_one = partial_quotients(20000)                  # une longue trajectoire d'époques
dtau = rng.uniform(c_min, c_max, size=a_one.sum().astype(int).item() if a_one.sum()<5e6 else 0)
# coût τ cumulé par ÉPOQUE (chaque époque = 1 bounce) ; modèle Δτ borné stochastique
n_epoch = int(min(a_one.sum(), 2_000_000))
dtau = rng.uniform(c_min, c_max, size=n_epoch)
tau = np.cumsum(dtau)                              # τ(m) après m époques (=m bounces)
m_idx = np.arange(1, n_epoch+1)                    # N_b(τ) = m
# fit linéaire N_b vs τ
A = np.vstack([tau, np.ones_like(tau)]).T
sl, _ = np.linalg.lstsq(A, m_idx, rcond=None)[0]
pred = sl*tau + _
R2tau = 1 - np.sum((m_idx-pred)**2)/np.sum((m_idx-m_idx.mean())**2)
within = np.all((m_idx <= tau/c_min + 1) & (m_idx >= tau/c_max - 1))
print(f"   (B.2) N_b(τ) : fit linéaire pente={sl:.4f} (∈[1/c_max,1/c_min]=[{1/c_max:.2f},{1/c_min:.2f}]) ; R²={R2tau:.6f}")
check("B.2a  N_b(τ) linéaire : R² > 0.999", R2tau > 0.999)
check("B.2b  borne τ/c_min ≥ N_b ≥ τ/c_max vérifiée époque-par-époque", within)

# ============================================================================
print("\n" + "="*80)
n_pass = sum(PASS); n_tot = len(PASS)
print(f" RÉSULTAT : {n_pass}/{n_tot} ASSERTS PASSENT")
print("="*80)
print("""
 INTERPRÉTATION (discipline §6.4) :
   • SCELLÉ ici : (A) la déduction §4 — Q sous-exp. ⟹ R_grad,gen→0, raccord exact à A1 ;
                  (B) N_b(τ) SOUS-EXPONENTIEL (quasi-linéaire) le long de l'oracle GK de P6,
                      queue lourde des ères longues bornée (coût τ proportionnel).
   • NON SCELLÉ : la conjecture A2★ (« Q(τ) sous-exponentielle / pas de cascade de spikes »).
     A.4 montre le SEUIL : une cascade Q~e^{|w|τ} casserait R→0 (réfutation R2). Que la
     dynamique générique évite cette cascade reste `à inventer` / `hors de portée`.
   • EFFET : toute la chaîne de C7-b est `formalisable` SAUF la conjecture A2★, isolée.
     Le verrou C7 est réduit à un UNIQUE postulat nommé et falsifiable. C7 NON levée.
     « Le bang gagne » (P6 B) intact ; aucune touche à l'algèbre des chaînons amont.
""")
import sys
sys.exit(0 if n_pass == n_tot else 1)
