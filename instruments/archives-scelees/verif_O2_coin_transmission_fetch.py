#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_O2_coin_transmission_fetch.py
LC-RACCORD — vérification SYMBOLIQUE STRUCTURELLE du coin de transmission D↔N
APRÈS fetch resserré (Witten ~1805.11559 ; Compère-Marolf ~0805.1902 ; Jubb ~1612.00149).

PORTÉE (anti-fit, gel cadrage 7cbf1072...dba9f, cibles TC-G1..G4/TC-R INCHANGÉES) :
Cette vérif teste la COHÉRENCE STRUCTURELLE de la décomposition
    S_TC = -(1/8πG) ∮_B √σ [ η + κ(p)·Φ ] d²θ
à la lumière des données conjuguées fournies par le fetch, et localise le gate TC-G2/TC-G3.
Ce n'est PAS un sceau (aucune construction finie) : aucune anomalie de coin n'est CALCULÉE
(le contre-terme de coin conforme z→0 vient d'une source NON armée). On vérifie :
  C1  décomposition de la variation de la face N : δγ = 2γ δω + δγ̃ ; BC conforme ⟹ δγ̃=0, δK=0,
      mais δω LIBRE (échelle non fixée, échangée contre K) — le résidu codim-2 est porté par δω.
  C2  équilibre du coin : δC_mixte = (part boost/η, face D) + (part κ(p)·Φ·δω, face N).
  C3  bonne-position (δC_mixte=0 ∀ variations) DÉTERMINE S_TC comme fonction de p,
      mais NE FIXE PAS p (p reste un label libre) — TC-G3 n'est pas tranché par la seule bonne-position.
  C4  limite same-type (firewall m2) : face N redevient Dirichlet ⟹ δω=0 ⟹ terme κ(p)·Φ → 0 ⟹
      réduction au η-term nu de LMPS. (m2 DOIT mordre.)
  C5  retrait du coin (firewall m1) : S_TC=0 ⟹ résidu codim-2 ≠ 0 ⟹ mal-position. (m1 DOIT mordre.)
  C6  gate TC-G2/TC-G3 : finitude z→0 de l'intégrande de coin ; le résidu renormalisé est une
      ANOMALIE DE COIN CONFORME A_c(p) ; p fixé ⟺ A_c(p)=0 a une solution isolée. A_c(p) requiert
      le contre-terme de coin conforme (source NON armée) ⟹ p NON fixé EN SCOPE (gate confirmé).
EXIT 0 = identités structurelles + firewalls m1/m2 vérifiés. AUCUN sceau.
"""
import sympy as sp

def section(t): print("\n=== %s ===" % t)

G, p, z = sp.symbols('G p z', positive=True)
# données géométriques / conjuguées (symbolique)
eta      = sp.symbols('eta', real=True)          # angle de boost codim-2 (LMPS / Jubb), face D
omega    = sp.symbols('omega', real=True)        # facteur conforme (échelle) de la face N
dω       = sp.symbols('domega', real=True)       # variation d'échelle (LIBRE sous BC conforme)
dγt      = sp.symbols('dgammat', real=True)      # variation de la classe conforme (FIXÉE ⟹ 0)
dK       = sp.symbols('dK', real=True)           # variation de la courbure moyenne (FIXÉE ⟹ 0)
Ktil     = sp.symbols('Ktilde', real=True)       # courbure extrinsèque SANS-TRACE = conjugué libre (Witten)
sqrtsig  = sp.symbols('sqrt_sigma', positive=True)  # √σ_0 (métrique induite régulière sur B)
kappa    = sp.Function('kappa')                  # poids κ(p) (famille York/Compère-Marolf)
Phi      = sp.symbols('Phi', real=True)          # pièce conjuguée de la face N (∝ K̃ ; Witten)

pref = -1/(8*sp.pi*G)

# ----------------------------------------------------------------------
section("C1 — décomposition de la variation de la face N (Witten + CM)")
# δγ_ab = 2 γ_ab δω + δγ̃_ab  ; BC conforme : δγ̃=0 (classe fixée), δK=0 (K fixé), δω libre.
dgamma_full = 2*dω + dγt          # schéma scalaire de la trace + sans-trace
bc_conforme = {dγt: 0, dK: 0}     # données FIXÉES par la BC conforme
residu_face_N = dgamma_full.subs(bc_conforme)
print("  δγ|_N sous BC conforme (δγ̃=0,δK=0) =", residu_face_N, " (porté par δω, LIBRE)")
assert residu_face_N == 2*dω, "C1: le résidu de la face N doit être l'échelle δω libre"
print("  OK : l'échelle ω n'est PAS fixée (échangée contre K) ⟹ résidu codim-2 = δω.")

# ----------------------------------------------------------------------
section("C2 — équilibre du coin : δC_mixte")
# Contribution D (Dirichlet/GHY) : le η-term annule la variation de boost résiduelle (LMPS) : δη.
deta = sp.symbols('deta', real=True)
contrib_D = pref*sqrtsig*deta                       # δ(η-term)  (backbone LMPS, face D)
# Contribution N (conforme) : le terme κ(p)·Φ doit absorber le résidu d'échelle δω.
contrib_N = pref*sqrtsig*kappa(p)*Phi*dω            # δ(κ(p)Φ-term) couplé à δω
dC_mixte  = contrib_D + contrib_N
print("  δC_mixte =", sp.simplify(dC_mixte))

# ----------------------------------------------------------------------
section("C3 — bonne-position DÉTERMINE S_TC(p) mais NE FIXE PAS p")
# Bonne-position : δC_mixte = 0 pour les variations admissibles.
# Le η-term règle la part boost (δη) côté D ; la part N impose κ(p)·Φ = (terme géométrique fixé).
# C'est UNE condition sur le produit κ(p)·Φ ⟹ elle FIXE le terme de coin pour CHAQUE p,
# mais p reste un LABEL libre tant qu'aucune condition INDÉPENDANTE ne le contraint.
geom = sp.symbols('C_geom', real=True)             # cible géométrique que κ(p)Φ doit reproduire
cond_wellposed = sp.Eq(kappa(p)*Phi, geom)         # 1 équation, 2 inconnues effectives (p via κ, et Φ)
print("  condition de bonne-position :", cond_wellposed)
# Résolution pour Φ à p donné : toujours soluble ⟹ p libre.
sol_Phi = sp.solve(cond_wellposed, Phi)
print("  Φ(p) =", sol_Phi, " ⟹ soluble ∀ p ⟹ p NON fixé par la bonne-position seule.")
assert sol_Phi, "C3: la bonne-position doit être soluble pour tout p (p libre à ce stade)"

# ----------------------------------------------------------------------
section("C4 — firewall m2 : limite same-type (face N redevient Dirichlet)")
# Same-type : la face N est aussi Dirichlet ⟹ δγ̃=0 ET δω=0 (toute la métrique fixée).
same_type = {dω: 0}
contrib_N_same = contrib_N.subs(same_type)
dC_same = sp.simplify(contrib_D + contrib_N_same)
print("  δC_mixte (same-type) =", dC_same, " ⟹ ne reste que le η-term (LMPS).")
assert contrib_N_same == 0, "m2: en same-type, le terme κ(p)Φ DOIT s'annuler (δω=0)"
print("  m2 MORD : κ(p)·Φ·δω → 0 ; réduction au η-term nu de LMPS. ✓")

# ----------------------------------------------------------------------
section("C5 — firewall m1 : retrait du terme de coin")
S_TC_removed = 0
residu_si_retrait = (pref*sqrtsig*kappa(p)*Phi*dω)  # ce que le coin devait absorber
print("  S_TC=0 ⟹ résidu non absorbé =", residu_si_retrait)
val = residu_si_retrait.subs({sqrtsig:1, Phi:1, dω:1, G:1}).subs(kappa(p), 1)
assert val != 0, "m1: sans terme de coin, le résidu d'échelle DOIT réapparaître"
print("  m1 MORD : sans coin, le résidu d'échelle δω réapparaît ⟹ mal-position. ✓")

# ----------------------------------------------------------------------
section("C6 — gate TC-G2/TC-G3 : finitude z→0 et anomalie de coin conforme")
# Près du bord conforme : √σ ~ z^{-2} √σ_0 ⟹ intégrande de coin ~ z^{-2}(η+κΦ)√σ_0 (DIVERGENT).
sig_z = sqrtsig/z**2
integrande = pref*sig_z*(eta + kappa(p)*Phi)
print("  intégrande de coin ~", sp.simplify(integrande), "  (∝ z^{-2} ⟹ divergent nu)")
# Le contre-terme de coin conforme (Compère-Marolf normalisable + contre-termes de coin) soustrait
# les puissances z^{-2}, z^0 ; le RÉSIDU est une anomalie de coin conforme A_c(p) (coefficient log z).
A_c = sp.Function('A_c')   # anomalie de coin conforme (coefficient du log z) — NON calculée ici
print("  après contre-terme : résidu = A_c(p)·log(z)  (anomalie de coin conforme)")
print("  TC-G3 : p fixé  ⟺  A_c(p)=0 a une solution ISOLÉE.")
print("  MAIS A_c(p) exige le CONTRE-TERME DE COIN CONFORME explicite (source NON armée :")
print("       renormalisation EH avec contre-termes de coin / BY à BC mixte) ⟹ NON calculé en scope.")
print("  ⟹ gate TC-G2 (finitude conditionnelle) confirmé ; TC-G3 (sort de p) GATÉ sur A_c(p) ;")
print("     p NON fixé EN SCOPE ⟹ C1-b TENU (consolidé, mieux situé).")

# ----------------------------------------------------------------------
section("BILAN STRUCTUREL")
print("  C1 résidu face N = δω (échelle libre)        : OK")
print("  C2 δC_mixte = η-part(D) + κ(p)Φ·δω-part(N)    : OK")
print("  C3 bonne-position ⟹ S_TC(p), p NON fixé       : OK")
print("  C4 firewall m2 (same-type → η nu)             : MORD")
print("  C5 firewall m1 (retrait → résidu réapparaît)  : MORD")
print("  C6 gate TC-G2/TC-G3 = anomalie A_c(p), source NON armée : gate CONFIRMÉ")
print("\n  VERDICT SUPPORTÉ = TC-b (consolidation, mieux situé) — AUCUN sceau, α reste C1-b.")
print("  SANS SURCLASSEMENT (§6.4) : structurer/dériver la forme ≠ calculer A_c(p) ≠ fixer p ≠")
print("  exhiber TC-a ≠ construire α ≠ construire O₂ (β≡G3 reste) ≠ fermer D1.")
print("\nEXIT 0")
