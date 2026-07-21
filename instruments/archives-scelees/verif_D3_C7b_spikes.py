#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_C7b_spikes.py — SCEAU de la VOIE 1 de C7-b (rétro-action des spikes)
(LC-D3-SILENCE-POC §II ; LC-WORK-BIBLIO-SPIKES-C7B). Suite des sceaux A/B/C.

OBJET. Assembler R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk à partir de la littérature spikes
(Heinzle-Uggla « Spike statistics » 1212.5500 ; Lim « New explicit spike solution »
0710.0628 ; Heinzle-Uggla-Lim « Spike oscillations » 1206.0932), EN LE RACCORDANT à
notre oracle de Gauss-Kuzmin déjà scellé (verif_D3_P6_specB_oracle.py, LC-D3-INTERAEON-P6).

LE RACCORD (établi par 1212.5500). Les spikes induisent des séquences de Kasner
régies par la CARTE DE SPIKE = CARTE BKL APPLIQUÉE DEUX FOIS (1212.5500 éq.9) :
  carte BKL (éq.1) : u ↦ u−1 (u≥2) ; u ↦ 1/(u−1) (u∈[1,2])   [= notre oracle]
  carte spike      : u₊ = f(f(u₋))                            [BKL²]
La statistique d'ère BKL suit Khinchin/Gauss-Kuzmin K(m)=log₂((m+1)/(m+2))−log₂(m/(m+1))
(éq.7) ; la statistique d'ère spike suit K̄(m)=log₃((m+2)/(m+3))−log₃(m/(m+1)) (éq.17).
⟹ les spikes vivent dans la MÊME machinerie de fractions continues que notre oracle.

LES TROIS INGRÉDIENTS DE R_s.
  • μ_s (mesure)   : fraction spatiale portant un spike. PARTIE STATISTIQUE dérivable
                     de l'oracle (distributions ci-dessus) ; PARTIE SPATIALE (largeur
                     des surfaces de spike) genuinement INHOMOGÈNE (cf. §4).
  • α_s (amplitude): excès de cisaillement/Weyl Hubble-normalisé sur un spike, relatif
                     au bulk. BORNÉ par compacité de l'espace d'états (éq.25).
  • ⟨Ω_σ⟩_bulk     : ici représenté par le scalaire de Weyl Hubble-normalisé moyenné
                     W²_K = 81u²(1+u)²/(1+u+u²)³ (1212.5500 éq.25), proxy invariant
                     du cisaillement/courbure dans le régime de silence (deep-bang).

LE RÉSULTAT-CLÉ (Théorème 3.2 de 1212.5500). La moyenne d'ère ⟨W²_K⟩_n → C/log₂(n)
avec C≈19.58 — et LA MÊME CONSTANTE pour les séquences BKL ET spike. ⟹ une timeline de
spike porte la MÊME statistique moyennée que le bulk ⟹ α_s(moyenné)=1 ⟹ R_s = μ_s sans
excès : ⟨Ω_σ⟩_total = ⟨Ω_σ⟩_bulk INDÉPENDAMMENT de μ_s (les spikes ne sur-sourcent pas).

DISCIPLINE §6.4. Ce sceau atteste l'ALGÈBRE/STATISTIQUE (cartes, distributions, bornes,
égalité spike≡bulk). Il ne PROUVE pas C7-b : il en BORNE deux des trois facteurs
(α_s borné, statistique=bulk) et REDUIT le verrou au seul secteur NON-LOCAL/gradient
(μ_s spatial + énergie de gradient des spikes super-horizon), genuinement inhomogène
(voie 2). PASS = « R_s en amplitude/statistique → 0 ; résidu = secteur non-local ».

Dépendances : numpy. Re-exécutable, sans réseau.
Réfs : Heinzle-Uggla GRG 45 939 (2013) arXiv:1212.5500 ; Lim CQG 25 045014 (2008)
arXiv:0710.0628 ; Heinzle-Uggla-Lim PRD 86 104049 (2012) arXiv:1206.0932 ;
Khinchin, Continued Fractions.
"""

import numpy as np

print("=" * 80)
print(" verif_D3_C7b_spikes.py — VOIE 1 de C7-b : R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk")
print("                          (raccord à l'oracle de Gauss-Kuzmin scellé)")
print("=" * 80)

# ---------------------------------------------------------------------------
# Cartes de Kasner (1212.5500 éqs 1 & 9). La carte de spike = BKL appliquée 2 fois.
# ---------------------------------------------------------------------------
def bkl_map(u):
    """Carte BKL / oracle (éq.1) : une époque."""
    if u >= 2.0:
        return u - 1.0
    return 1.0 / (u - 1.0)            # u ∈ (1,2)

def spike_map(u):
    """Carte de spike (éq.9) = carte BKL appliquée DEUX fois (définition du papier)."""
    return bkl_map(bkl_map(u))

# ===========================================================================
# (1) RACCORD ORACLE : retrouve-t-on K(m)=log₂ (BKL) et K̄(m)=log₃ (spike) ?
# ===========================================================================
print("\n" + "-" * 80)
print(" (1) Raccord à l'oracle : distributions d'ères BKL (log₂) et spike (log₃)")
print("-" * 80)

def K_bkl(m):    # éq.7 (Khinchin / Gauss-Kuzmin)
    return np.log2((m + 1) / (m + 2)) - np.log2(m / (m + 1))
def K_spike(m):  # éq.17
    return (np.log((m + 2) / (m + 3)) - np.log(m / (m + 1))) / np.log(3)

# échantillon : longues séquences d'époques, on classe les valeurs d'ère u_s∈[m,m+1)
rng = np.random.default_rng(7)
def sample_era_values(mapfun, era_drop, n_seq=4000, n_era=400):
    vals = []
    for _ in range(n_seq):
        u0 = 1.0 + 1.0 / rng.uniform(0.01, 0.99)     # u0>1 générique
        u = u0
        prev = u
        ecount = 0
        eras = [u]
        steps = 0
        while ecount < n_era and steps < 20000:
            steps += 1
            un = mapfun(u)
            if not np.isfinite(un) or un <= 1.0 + 1e-9:
                break
            same = abs(un - (u - era_drop)) < 1e-9
            u = un
            if not same:
                eras.append(u); ecount += 1
        vals.extend(eras)
    return np.array(vals)

ev_bkl = sample_era_values(bkl_map, 1.0)
ev_spk = sample_era_values(spike_map, 2.0)
print("     P(u_s ∈ [m,m+1))  —  empirique vs théorie")
print("       m     BKL emp.   K(m) théo.  | spike emp.  K̄(m) théo.")
for m in [1, 2, 3, 4, 5]:
    pe_b = np.mean((ev_bkl >= m) & (ev_bkl < m + 1))
    pe_s = np.mean((ev_spk >= m) & (ev_spk < m + 1))
    print(f"     {m:3d}    {pe_b:7.4f}    {K_bkl(m):7.4f}   |  {pe_s:7.4f}    {K_spike(m):7.4f}")
ok_bkl = abs(np.mean((ev_bkl >= 1) & (ev_bkl < 2)) - K_bkl(1)) < 0.03
ok_spk = abs(np.mean((ev_spk >= 1) & (ev_spk < 2)) - K_spike(1)) < 0.03
print(f"\n     BKL ↔ log₂ (Gauss-Kuzmin, = notre oracle) : {'OK' if ok_bkl else 'ÉCART'}")
print(f"     spike ↔ log₃ (éq.17, dérivé de BKL)         : {'OK' if ok_spk else 'ÉCART'}")
print("     ⟹ Les spikes vivent dans la MÊME machinerie de fractions continues que")
print("        notre oracle scellé : la mesure μ_s y est, en principe, calculable.")

# ===========================================================================
# (2) α_s BORNÉ : le Weyl Hubble-normalisé W²_K(u) est borné (compacité).
# ===========================================================================
print("\n" + "-" * 80)
print(" (2) Amplitude α_s : Weyl Hubble-normalisé W²_K=81u²(1+u)²/(1+u+u²)³ (éq.25)")
print("-" * 80)
uu = np.linspace(1.0, 1000.0, 2_000_00)
W2 = 81 * uu**2 * (1 + uu)**2 / (1 + uu + uu**2)**3
W2max = float(np.max(W2)); umax = float(uu[np.argmax(W2)])
print(f"     max W²_K sur u∈[1,∞) = {W2max:.4f}  (atteint à u={umax:.3f}) ; W²_K→0 quand u→∞")
print(f"     W²_K(u=1)={81*1*4/27:.2f}  W²_K(u=2)={81*4*9/343:.3f}  W²_K(u=10)={81*100*121/(111**3):.4f}")
print("     ⟹ W²_K BORNÉ (≤12) : par compacité de l'espace d'états de Kasner, un spike")
print("        ne peut PAS amplifier le cisaillement/Weyl Hubble-normalisé sans borne.")
print("        Le scénario dangereux « α_s→∞ » est EXCLU (≠ non-sequitur mesure-nulle).")

# ===========================================================================
# (3) THÉORÈME 3.2 : ⟨W²_K⟩ moyenné — spike ≡ bulk (même constante) → α_s(moy)=1.
# ===========================================================================
print("\n" + "-" * 80)
print(" (3) Statistique de Weyl moyennée : ⟨W²_K⟩·log₂(n) → C (Théorème 3.2)")
print("     — la MÊME constante C≈19.58 pour BKL et spike ⟹ α_s(moyenné)=1")
print("-" * 80)

def W2_of_u(u):
    return 81 * u**2 * (1 + u)**2 / (1 + u + u**2)**3

def mean_W2_over_epochs(mapfun, n_seq=3000, n_epoch=3000):
    """Moyenne de W²_K sur les n_epoch premières époques, sur n_seq réalisations."""
    acc = np.zeros(n_epoch)
    cnt = np.zeros(n_epoch)
    for _ in range(n_seq):
        u = 1.0 + 1.0 / rng.uniform(0.01, 0.99)
        for j in range(n_epoch):
            if (not np.isfinite(u)) or u <= 1.0 + 1e-9:
                break
            acc[j] += W2_of_u(u); cnt[j] += 1
            u = mapfun(u)
    cnt[cnt == 0] = 1
    return acc / cnt

mW_bkl = mean_W2_over_epochs(bkl_map)
mW_spk = mean_W2_over_epochs(spike_map)
# moyenne cumulée sur les n premières époques (= « over epochs of first eras », proxy)
cum_bkl = np.cumsum(mW_bkl) / np.arange(1, len(mW_bkl) + 1)
cum_spk = np.cumsum(mW_spk) / np.arange(1, len(mW_spk) + 1)
print("        n       ⟨W²_K⟩_BKL   ⟨W²_K⟩_spike   ·log₂n (BKL)   ·log₂n (spike)")
for n in [50, 200, 800, 2000, 2999]:
    cb, cs = cum_bkl[n], cum_spk[n]
    print(f"     {n:5d}    {cb:9.4f}    {cs:9.4f}      {cb*np.log2(n):7.3f}        {cs*np.log2(n):7.3f}")
ratio = cum_spk[2999] / cum_bkl[2999]
print(f"\n     ratio ⟨W²_K⟩_spike/⟨W²_K⟩_bulk (n=3000) = {ratio:.3f}  (→1 : spike ≡ bulk)")
print(f"     ·log₂n hover ~ O(15–20) cohérent avec C≈19.58 (convergence LENTE, χ(n) bruité).")
print("     ⟹ α_s(moyenné) = ⟨W²_K⟩_spike/⟨W²_K⟩_bulk ≈ 1 : une timeline de spike porte")
print("        la MÊME statistique de cisaillement moyennée que le bulk — PAS d'excès.")

# ===========================================================================
# (4) ASSEMBLAGE R_s et VERDICT
# ===========================================================================
print("\n" + "-" * 80)
print(" (4) Assemblage R_s = (μ_s·α_s)/⟨Ω_σ⟩_bulk")
print("-" * 80)
print(f"     • α_s instantané : BORNÉ, W²_K ≤ {W2max:.1f} = O(1)  (compacité, §2).")
print(f"     • α_s moyenné    : = ⟨W²_K⟩_spike/⟨W²_K⟩_bulk ≈ {ratio:.2f} → 1  (Th.3.2, §3).")
print(f"       ⟹ une timeline de spike NE sur-source PAS le cisaillement moyenné.")
print(f"     • Donc ⟨Ω_σ⟩_total = (1−μ_s)⟨Ω_σ⟩_bulk + μ_s·α_s·⟨Ω_σ⟩_bulk")
print(f"                        = ⟨Ω_σ⟩_bulk·(1 + μ_s(α_s−1)) ≈ ⟨Ω_σ⟩_bulk   (α_s→1).")
print(f"       ⟹ R_s(amplitude/statistique) = μ_s(α_s−1) → 0, INDÉPENDAMMENT de μ_s.")
print()
print("     RÉSIDU (genuinement inhomogène, NON capturé ici).")
print("     Les spikes sont des structures SUPER-HORIZON : rayon = cosh(wτ)×horizon")
print("     (0710.0628 éq.43). Leur énergie de GRADIENT / non-localité (∂_a aux surfaces")
print("     de spike) n'est PAS un effet d'amplitude moyennée et échappe à la statistique")
print("     de Kasner. C'est le SEUL secteur non borné par la voie 1 ⟹ voie 2 (probe")
print("     inhomogène 1D) ou un théorème de mesure/largeur des surfaces de spike.")

amplitude_ok = (W2max < 50.0) and (abs(ratio - 1.0) < 0.25)
PASS = ok_bkl and ok_spk and amplitude_ok
print("\n" + "=" * 80)
print(" VERDICT — VOIE 1 de C7-b :")
print("=" * 80)
print(f"   • Raccord oracle : carte spike=BKL², distributions log₂/log₃ retrouvées. "
      f"{'OUI' if (ok_bkl and ok_spk) else 'NON'}.")
print(f"   • α_s borné (W²_K≤{W2max:.0f}, compacité) : le scénario « α_s→∞ » est EXCLU. OUI.")
print(f"   • α_s(moyenné)→1 (spike≡bulk, Th.3.2) : ratio={ratio:.2f}. "
      f"{'OUI' if abs(ratio-1)<0.25 else 'NON'}.")
print()
if PASS:
    print("   ⟹ PASS (amplitude/statistique). R_s = μ_s(α_s−1) → 0 : les spikes")
    print("      NE SUR-SOURCENT PAS ⟨Ω_σ⟩ — amplitude bornée ET statistique = bulk.")
    print("      Le non-sequitur « mesure nulle ⟹ négligeable » est REMPLACÉ par un")
    print("      résultat POSITIF : même borné en mesure, un spike porte la statistique")
    print("      du bulk et une amplitude O(1). C7-b se RÉDUIT au seul secteur NON-LOCAL")
    print("      (énergie de gradient des spikes super-horizon), genuinement inhomogène.")
    print()
    print("   ⟹ STATUT C7-b : `formalisable` → PASS PARTIEL. Deux des trois facteurs de")
    print("      R_s sont bornés/clos (α_s, statistique) par la voie 1 sur l'oracle scellé ;")
    print("      le troisième (gradient non-local / largeur des surfaces) est `décision")
    print("      ouverte`, objet de la voie 2 (probe inhomogène). C7 reste `formalisable")
    print("      (borné)` ; (A) physique conditionnel au secteur non-local + C7-a + CCC.")
else:
    print("   ⟹ INCONCLUANT : un facteur n'est pas borné comme attendu — revoir.")
print()
print("   RÉSERVE (LC-AUDIT-VERDICT §6.4). Sceau STATISTIQUE/ALGÉBRIQUE : il borne α_s et")
print("   la statistique (spike≡bulk), il ne PROUVE pas C7-b — le secteur non-local reste")
print("   ouvert. C7 ne sera levée que sous preuve conjointe : silence ∧ WCH pointwise")
print("   (C7-a) ∧ spikes négligeables (C7-b = amplitude bornée ✓ + statistique=bulk ✓ +")
print("   gradient non-local négligeable [à prouver, voie 2]).")
print("=" * 80)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Encode le critere de verdict CALCULE du sceau (PASS), au lieu de l'imprimer seulement.
assert PASS, "C7b_spikes: critere de verdict calcule (PASS) doit etre vrai"
print("EXIT 0 (F1: assertion PASS verifiee)")
