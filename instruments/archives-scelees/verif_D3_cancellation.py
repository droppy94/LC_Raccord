#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_cancellation.py — LC-RACCORD. Pourquoi les ondes « disparaissent » à 𝓘 :
TROIS mécanismes distincts, à ne pas confondre. (Compagnon de LC-D3-WCH-CANCELLATION.
Consolide verif_D3_bunchdavies, verif_D3_backreaction, verif_D1_bianchiA/einstein3d.)

QUESTION. « À la frontière de Sitter, les ondes ont-elles perdu leur amplitude, ou
s'annulent-elles entre elles ? » — la réponse exige de SÉPARER trois objets que l'image
naïve « les ondes s'éteignent » confond :

  [C1] Le mode tensoriel inhomogène GÈLE (f→1), il ne décroît PAS ; la marée rescalée
       par mode g₃ est FINIE. -> « perte d'amplitude » FAUSSE pour le datum qui compte.
  [C2] Perte d'amplitude RÉELLE, mais d'un AUTRE objet : le cisaillement HOMOGÈNE du
       fond σ_bg décroît (no-hair de Wald/Starobinsky en Λ-domination : σ∝a^{-3}→0).
  [C3] CANCELLATION un-point : ⟨g₃⟩=0 parce que les contributions SIGNÉES des modes de
       toutes directions se compensent (∫k̂k̂=⅓δ tue la part sans-trace). C'EST la WCH
       un-point, et elle est CONTINGENTE à l'isotropie (A3) : un état anisotrope la casse.
  [C4] VARIANCE deux-points IRRÉDUCTIBLE : ⟨g₃g₃⟩~k³ est une somme de CARRÉS, rien ne s'y
       compense -> empreinte durable (spectre primordial ; contact [E]/CMB).

VERDICT. La « disparition des ondes à 𝓘 » au sens de la WCH est une CANCELLATION [C3]
(symétrie), pas une perte d'amplitude [C1 faux ; C2 concerne le fond]. La variance [C4]
survit. Conséquence : la WCH un-point a besoin d'une SYMÉTRIE pour avoir lieu -> elle est
exactement le contenu du pivot A3 (cf. LC-D3-CROSSOVER-ANISOTROPE, -EINSTEIN3D).
Analogie BAO↔horizon : moyenne qui se lave [C3] = ⟨δ⟩=0 ; empreinte deux-points [C4] =
bosse BAO. `[résonance structurelle, non dérivée]`.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs : Bunch-Davies Proc.R.Soc.A 360 (1978) ; Wald PRD 28 (1983) / Starobinsky JETP Lett.
37 (1983) (no-hair) ; de Haro-Skenderis-Solodukhin CMP 217 (2001) ; Gurzadyan-Penrose
EPJP 128 (2013) (cercles CMB = empreinte inter-éon candidate, contestée).
"""

import sympy as sp

print("="*78)
print(" verif_D3_cancellation.py — perte d'amplitude ? cancellation ? variance ?")
print("   les TROIS mécanismes de la 'disparition' des ondes à 𝓘, séparés")
print("="*78)

eta, k, H, t = sp.symbols('eta k H t', positive=True)
I = sp.I
th, ph, eps = sp.symbols('theta phi epsilon', real=True)

# ======================================================================
# [C1] Le mode inhomogène GÈLE (ne décroît pas) ; g₃ par mode FINI.
# ======================================================================
print("\n" + "-"*78)
print(" [C1] Le mode tensoriel GÈLE à 𝓘 (η→0), il ne perd PAS son amplitude")
print("-"*78)
f = (1 + I*k*eta)*sp.exp(-I*k*eta)
flim = sp.limit(f, eta, 0)
g3 = sp.expand(sp.series(f, eta, 0, 5).removeO()).coeff(eta, 3)
print("   mode Bunch-Davies f(η→0) =", flim, "  -> GÈLE à une constante (≠ 0 : pas de décroissance)")
print("   marée rescalée par mode g₃ =", sp.simplify(g3), "  -> FINIE, non nulle")
assert flim == 1 and sp.simplify(g3) != 0
print("   => « les ondes perdent leur amplitude » est FAUX pour le datum rescalé (g₃ fini).")

# ======================================================================
# [C2] Perte d'amplitude RÉELLE, mais du CISAILLEMENT HOMOGÈNE du fond (no-hair).
# ======================================================================
print("\n" + "-"*78)
print(" [C2] Perte d'amplitude RÉELLE, mais d'un AUTRE objet : le fond (no-hair)")
print("-"*78)
# Équation du cisaillement de fond en Λ-domination : σ̇ + 3Hσ = 0 (sans source), a∝e^{Ht}.
sig = sp.Function('sigma')
ode = sp.Eq(sp.diff(sig(t), t) + 3*H*sig(t), 0)
sol = sp.dsolve(ode, sig(t))
print("   cisaillement de fond :", ode, " -> ", sol)
sig_t = sol.rhs
print("   σ_bg(t→∞) =", sp.limit(sig_t.subs(sp.Symbol('C1'), 1), t, sp.oo),
      "  -> DÉCROÎT vers 0 (no-hair de Wald/Starobinsky : σ∝a^{-3}∝e^{-3Ht}).")
assert sp.limit(sig_t.subs(sp.Symbol('C1'), 1), t, sp.oo) == 0
print("   => CECI est une vraie perte d'amplitude — mais du cisaillement CINÉTIQUE du FOND,")
print("      pas des ondes inhomogènes [C1], ni de l'anisotropie GELÉE de â (cf. EINSTEIN3D).")

# ======================================================================
# [C3] CANCELLATION un-point : ⟨g₃⟩=0 par symétrie ; CASSÉE si anisotrope.
# ======================================================================
print("\n" + "-"*78)
print(" [C3] CANCELLATION un-point : ⟨g₃⟩=0 par isotropie (= WCH), CONTINGENTE à A3")
print("-"*78)
nhat = sp.Matrix([sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)])
def avg(e, w=1):
    num = sp.integrate(sp.integrate(e*w*sp.sin(th), (ph,0,2*sp.pi)), (th,0,sp.pi))
    den = sp.integrate(sp.integrate(w*sp.sin(th),   (ph,0,2*sp.pi)), (th,0,sp.pi))
    return sp.simplify(num/den)
# isotrope : part sans-trace de ⟨k̂k̂⟩ = 0 (les contributions signées se compensent)
M_iso = sp.Matrix(3,3, lambda i,j: avg(nhat[i]*nhat[j]))
TF_iso = sp.simplify(M_iso - sp.trace(M_iso)/3*sp.eye(3))
print("   état ISOTROPE   : ⟨k̂k̂⟩ sans-trace =", TF_iso.tolist(), " -> ANNULATION (⟨g₃⟩=0 = WCH)")
assert TF_iso == sp.zeros(3,3)
# anisotrope (poids quadrupolaire ε) : la cancellation ÉCHOUE
w = 1 + eps*(3*sp.cos(th)**2 - 1)/2
M_ani = sp.Matrix(3,3, lambda i,j: avg(nhat[i]*nhat[j], w))
TF_ani = sp.simplify(M_ani - sp.trace(M_ani)/3*sp.eye(3))
print("   état ANISOTROPE : ⟨k̂k̂⟩ sans-trace =", [sp.simplify(TF_ani[i,i]) for i in range(3)],
      " -> ⟨g₃⟩≠0 ([B3])")
assert sp.simplify(TF_ani.subs(eps, sp.Rational(1,2))) != sp.zeros(3,3)
print("   => la WCH un-point N'EST PAS une perte d'amplitude : c'est une CANCELLATION de")
print("      contributions signées, qui EXIGE la symétrie. Casser l'isotropie la détruit.")
print("      C'est, mot pour mot, le contenu physique du pivot A3.")

# ======================================================================
# [C4] VARIANCE deux-points : somme de CARRÉS, ne s'annule pas (empreinte).
# ======================================================================
print("\n" + "-"*78)
print(" [C4] VARIANCE deux-points : irréductible (empreinte durable)")
print("-"*78)
kz2 = avg(nhat[2]**2)
print("   ⟨k̂_z²⟩ =", kz2, " (>0)   ;   |g₃|² par mode =", sp.simplify(sp.Abs(g3)**2), " (>0)")
print("   ⟨g₃g₃⟩ ~ k³ (conforme Δ=3) : somme de CARRÉS -> aucune compensation possible.")
assert kz2 > 0 and sp.simplify(sp.Abs(g3)**2) != 0
print("   => la VARIANCE survit : c'est l'empreinte (spectre primordial ; contact [E]/CMB).")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "="*78)
print(" VERDICT — trois mécanismes, à ne pas confondre :")
print("="*78)
print("   [C1] mode inhomogène : GÈLE (g₃ fini)        -> PAS de perte d'amplitude.")
print("   [C2] cisaillement de FOND : décroît (no-hair) -> perte d'amplitude RÉELLE (autre objet).")
print("   [C3] moyenne ⟨g₃⟩=0 : CANCELLATION par symétrie -> = WCH un-point = contenu de A3.")
print("   [C4] variance ⟨g₃g₃⟩~k³ : somme de carrés       -> empreinte durable irréductible.")
print("")
print("   ==> La 'disparition des ondes à 𝓘' au sens WCH est [C3] (CANCELLATION), pas une")
print("       perte d'amplitude. Une cancellation a besoin d'une symétrie : d'où A3 pivot.")
print("")
print(" ANALOGIE BAO ↔ horizon `[résonance structurelle, non dérivée]` :")
print("   moyenne qui se lave (⟨δ⟩=0)         ↔  [C3] ⟨g₃⟩=0 (cancellation) ;")
print("   bosse BAO dans le deux-points       ↔  [C4] ⟨g₃g₃⟩~k³ (empreinte) ;")
print("   surface de dernière diffusion       ↔  crossover 𝒞 / 𝓘 ;")
print("   empreinte inter-éon candidate       ↔  cercles de Gurzadyan-Penrose (réel, CONTESTÉ).")
print("   [Garde-fou audit §6.5 : pont de VOCABULAIRE, non une dérivation.]")
print("="*78)
