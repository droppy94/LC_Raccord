#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_interaeon_poc.py — DÉMONSTRATEUR DE FAISABILITÉ (pas le calcul complet).
Question de cadrage (LC-WORK-AUDIT-FROID suite ; frontière de LC-D3-CROSSOVER-EINSTEIN3D §4) :
propager â à travers l'éon futur jusqu'à SON 𝓘 pour obtenir la carte ε_n ↦ ε_{n+1}
est-il `formalisable` (extension de machinerie connue) ou `à inventer` ?

CE QUE CE FICHIER MONTRE (et CE QU'IL NE MONTRE PAS).
  • MONTRE : la PARTIE TARDIVE de l'évolution (radiation -> Λ-domination -> 𝓘) se réduit à
    des ODE qu'on sait écrire et intégrer, et que l'anisotropie GELÉE de 𝓘 (qui définit
    ε_{n+1}) est une quantité bien définie et numériquement extractible. -> argument pour
    `formalisable`.
  • NE MONTRE PAS : (i) le couplage de COURBURE (Bianchi IX, terme de structure) ; (ii) la
    back-réaction du cisaillement/courbure sur le fond ; (iii) la dynamique près du bang
    (Mixmaster pour IX) ; (iv) la matière CCC exacte (σ̌, champ phantom, matière noire) au-
    delà des deux ordres de Tod. Ces quatre points sont le `à inventer`/extension lourde.

NIVEAU DU DÉMONSTRATEUR : cisaillement en CHAMP-TEST sur un fond FRW radiation+Λ (pas de
back-réaction, directions plates). Suffit à établir : (1) ODE intégrables ; (2) isotropi-
sation CINÉTIQUE Σ=σ/θ→0 (Wald) ; (3) l'anisotropie gelée Δβ=∫σ dt CONVERGE (intégrale
finie) -> ε_{n+1} est un nombre fini, donc la CARTE EXISTE et est calculable.

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Wald PRD 28 (1983) (no-hair) ; Wainwright-Ellis, Dynamical Systems in Cosmology
(1997) (ODE de Bianchi) ; Tod arXiv:1309.7248 (données de bang, éq.28-33).
"""

import numpy as np
from scipy.integrate import solve_ivp

print("="*78)
print(" verif_D3_interaeon_poc.py — DÉMONSTRATEUR : la carte ε_n↦ε_{n+1} est-elle calculable ?")
print("="*78)

# ----------------------------------------------------------------------
# Fond FRW radiation + Λ (unités 8πG/3 = 1). H² = ρ_r0 a^{-4} + Λ/3.
# Cisaillement champ-test : σ̇ + 3Hσ = 0  ->  σ = σ0 a^{-3}  (sans source anisotrope).
# Variables : y = [a, σ1, σ2] (σ3 = -σ1-σ2, sans trace) ; on suit aussi β_i = ∫(H+σ_i)dt.
# ----------------------------------------------------------------------
rho_r0 = 1.0        # densité de radiation initiale (a=1)
Lam    = 3.0        # Λ (=> H_inf = 1)
def Hubble(a):
    return np.sqrt(rho_r0*a**-4 + Lam/3.0)

# anisotropie initiale du bang : σ_i^0 (sans trace). On la prend ∝ ε_n (petit).
def run(eps_n):
    s0 = np.array([eps_n, -0.5*eps_n])   # σ1,σ2 ; σ3=-(σ1+σ2)=-0.5 eps  (sans trace)
    def rhs(t, y):
        a, s1, s2, b1, b2, b3 = y
        H = Hubble(a)
        # σ̇_i + 3H σ_i = 0
        ds1 = -3*H*s1; ds2 = -3*H*s2
        s3 = -s1 - s2
        # β̇_i = H + σ_i  (log des facteurs d'échelle directionnels)
        return [a*H, ds1, ds2, H+s1, H+s2, H+s3]
    y0 = [1.0, s0[0], s0[1], 0.0, 0.0, 0.0]
    sol = solve_ivp(rhs, [0, 30], y0, rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.01)
    a, s1, s2, b1, b2, b3 = sol.y
    H = Hubble(a)
    s3 = -s1 - s2
    sigma = np.sqrt(0.5*(s1**2 + s2**2 + s3**2))     # scalaire de cisaillement
    Sigma = sigma/(3*H)                               # Σ = σ/θ  (paramètre d'anisotropie)
    return sol.t, a, Sigma, np.array([b1,b2,b3])

# ----------------------------------------------------------------------
# (1) Les ODE s'intègrent ; (2) isotropisation cinétique Σ -> 0.
# ----------------------------------------------------------------------
t, a, Sigma, beta = run(eps_n=0.3)
print("\n (1)-(2) Intégration radiation->Λ, cisaillement champ-test (ε_n=0.3) :")
print(f"     a : {a[0]:.2f} -> {a[-1]:.3e}   (expansion : radiation puis de Sitter)")
print(f"     Σ=σ/θ : {Sigma[0]:.4f} (début) -> {Sigma[-1]:.3e} (𝓘)   -> ISOTROPISATION CINÉTIQUE (Wald)")
assert Sigma[-1] < 1e-6 and Sigma[-1] < Sigma[0]

# ----------------------------------------------------------------------
# (3) Anisotropie GELÉE : Δβ_ij = β_i - β_j -> CONVERGE (intégrale finie) => ε_{n+1} fini.
# ----------------------------------------------------------------------
dbeta = beta - beta.mean(axis=0)        # part sans-trace des log-facteurs (anisotropie)
frozen = dbeta[:, -1]                    # valeurs gelées à 𝓘
# vérif de convergence : la dérivée de l'anisotropie -> 0 (plus rien ne bouge)
tail_drift = np.abs(dbeta[:, -1] - dbeta[:, -200]).max()
print("\n (3) Anisotropie gelée du 𝓘 futur (part sans-trace des log-facteurs) :")
print(f"     Δβ_i gelés = {np.round(frozen,5)}   (dérive sur la queue : {tail_drift:.2e} -> CONVERGE)")
print(f"     => ε_{{n+1}} := |Δβ gelé| = {np.linalg.norm(frozen):.5f}  : un NOMBRE FINI, bien défini.")
assert tail_drift < 1e-6

# ----------------------------------------------------------------------
# (bonus) La carte ε_n -> ε_{n+1} est, à ce niveau, LINÉAIRE : on en lit la pente κ.
# ----------------------------------------------------------------------
print("\n (bonus) Carte ε_n ↦ ε_{n+1} (champ-test, directions plates) :")
print("     ε_n      ε_{n+1}=|Δβ gelé|")
slopes=[]
for en in [0.05, 0.10, 0.20, 0.30]:
    _,_,_,b = run(en)
    db = b - b.mean(axis=0)
    en1 = np.linalg.norm(db[:,-1])
    slopes.append(en1/en)
    print(f"     {en:.2f}     {en1:.5f}")
kappa = np.mean(slopes)
print(f"     -> carte LINÉAIRE, pente κ ≈ {kappa:.4f}  (à CE niveau : champ-test, sans courbure)")
print("        |κ|<1 -> isotropisation inter-éon ; >1 -> runaway ; =1 -> marginal.")
print("        [valeur NON physique en l'état : ignore courbure IX + back-réaction + bang.]")

# ======================================================================
# VERDICT DE FAISABILITÉ
# ======================================================================
print("\n" + "="*78)
print(" VERDICT DE FAISABILITÉ (ce démonstrateur) :")
print("="*78)
print("   ÉTABLI ICI : la partie TARDIVE (radiation->Λ->𝓘) se réduit à des ODE intégrables ;")
print("   l'isotropisation cinétique Σ→0 marche (Wald) ; l'anisotropie gelée de 𝓘 CONVERGE")
print("   vers un nombre fini ; la carte ε_n↦ε_{n+1} EXISTE, est LINÉAIRE (petit ε) et sa")
print("   pente κ est extractible. -> la STRUCTURE du calcul est `formalisable`.")
print("")
print("   RESTE À AJOUTER (l'écart vers le vrai κ) :")
print("     (i)  couplage de COURBURE (Bianchi IX : terme de structure n_i) — ODE, formalisable ;")
print("     (ii) BACK-RÉACTION cisaillement+courbure sur le fond — ODE couplées, formalisable ;")
print("     (iii) dynamique près du BANG (Mixmaster IX) — formalisable mais lourd/chaotique ;")
print("     (iv) matière CCC EXACTE (σ̌, phantom, DM) au-delà des 2 ordres de Tod — `à inventer`.")
print("")
print("   => CADRAGE : (i)-(iii) = `formalisable` (extension Wainwright-Ellis + Tod) ;")
print("      seul (iv) est `à inventer`. La carte κ est ACCESSIBLE en approx. (i)-(iii),")
print("      ce qui SUFFIT à trancher qualitativement l'isotropisation inter-éon.")
print("="*78)
