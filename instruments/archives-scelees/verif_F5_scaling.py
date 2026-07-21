#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_F5_scaling.py  —  SCEAU CONDITIONNEL / RÉVERSIBLE  (front F5, étape (c))
                        VERSION DURCIE (R-28, audit froid passe 4)
================================================================================
Objet : vérifier, au niveau de l'ALGÈBRE D'EXPOSANTS seulement, la forme gelée
au cadrage (F5-G3)

        A_T  ~  1/C_T  ~  1/N ,   C_T ~ N = S_dS ~ (ell_dS/ell_P)^(d-1)

par DEUX routes :
  (R1) invariance dS / dimensionnel : l'état BD n'admet qu'une échelle, H ;
       en dimension de bord d (bulk d+1), G_N ~ M_P^-(d-1) et A_T ~ G_N H^(d-1)
       = (H/M_P)^(d-1).
  (R2) dictionnaire holographique (fonction d'onde) : A_T ~ 1/C_T (amplitude =
       inverse de la raideur du stress), avec C_T ~ N.

DURCISSEMENT R-28 (corollaire de l'audit froid, passe 4) : on garde d SYMBOLIQUE.
On démontre alors que A_T·N est INDÉPENDANT de ell ET de d — donc A_T ~ 1/N est une
IDENTITÉ POUR TOUT d, non une coïncidence évaluée à d=3 — parce que N, C_T et
(M_P/H)^(d-1) sont LE MÊME comptage de degrés de liberté en loi d'aire ell^(d-1).
Conséquence épistémique explicitement scellée : l'accord des deux routes sur
l'exposant N^-1 est ADOSSÉ À CE SOCLE PARTAGÉ (loi d'aire). Les routes sont donc
indépendantes EN CONTENU (R2 porte le dictionnaire holographique 1/raideur, absent
de R1) mais NON indépendantes AU NIVEAU DE L'EXPOSANT.

Le sceau N'ÉTABLIT PAS le coefficient O(1) : il reste un symbole LIBRE (requiert O₂,
la CFT de raccordement, non construite). Vérifié explicitement (garde-fou §6.4).

Statut : SCALING `formalisable` ; coefficient `à inventer` ; N NON fixé.
N'établit PAS « D1 clos / N fixé / W³ fixé / CCC démontrée ». {A4 ; A2★ ; N} INCHANGÉ.
Réversible (précédent S-CB-3a) ; remplace la version d=3 figé (R-28 sanctionné).
"""
import sympy as sp

A = 0  # compteur d'assertions

# --- Symboles -----------------------------------------------------------------
# d : dimension de bord SYMBOLIQUE (bulk d+1). ell_P : echelle de Planck (coeff.).
d, ell_dS, ell_P = sp.symbols('d ell_dS ell_P', positive=True)
c_dim, c_wf, c_CT = sp.symbols('c_dim c_wf c_CT', positive=True)  # O(1) LIBRES

p = d - 1  # exposant de loi d'aire (d-1) : c'est LUI le squelette partage

# --- Definitions geometriques (d SYMBOLIQUE) ----------------------------------
# N = S_dS = (ell_dS/ell_P)^(d-1) = aire d'horizon en unites de Planck
N = (ell_dS / ell_P)**p
H   = 1 / ell_dS         # Hubble ~ 1/rayon dS
M_P = 1 / ell_P          # masse de Planck ~ 1/longueur de Planck

# --- Route R1 : dimensionnel / dS  --------------------------------------------
# A_T ~ G_N H^(d-1) = (H/M_P)^(d-1)  (G_N ~ M_P^-(d-1))
A_T_R1 = c_dim * (H / M_P)**p
res_R1 = sp.simplify(A_T_R1 * N)
# IDENTITE pour tout d : A_T*N ne depend NI de ell NI de d -> vaut c_dim
assert ell_dS not in res_R1.free_symbols and ell_P not in res_R1.free_symbols, \
    "R1 : A_T*N doit etre sans echelle"
A += 1
assert d not in res_R1.free_symbols, \
    "R1 : A_T*N doit etre INDEPENDANT de d (identite pour tout d, pas coincidence d=3)"
A += 1
assert sp.simplify(res_R1 - c_dim) == 0, "R1 : A_T*N doit valoir exactement c_dim"
A += 1

# --- Route R2 : holographique / fonction d'onde -------------------------------
C_T    = c_CT * N
A_T_R2 = sp.simplify(c_wf / C_T)
res_R2 = sp.simplify(A_T_R2 * N)
assert ell_dS not in res_R2.free_symbols and ell_P not in res_R2.free_symbols, \
    "R2 : A_T*N doit etre sans echelle"
A += 1
assert d not in res_R2.free_symbols, "R2 : A_T*N doit etre INDEPENDANT de d"
A += 1

# --- SOCLE PARTAGE (le coeur de R-28) -----------------------------------------
# N, C_T/c_CT et (M_P/H)^(d-1) sont LE MEME facteur de loi d'aire (ell_dS/ell_P)^(d-1).
aire = (ell_dS / ell_P)**p
assert sp.simplify(N - aire) == 0, "N doit etre la loi d'aire (ell_dS/ell_P)^(d-1)"
A += 1
assert sp.simplify(C_T / c_CT - aire) == 0, "C_T/c_CT doit etre la MEME loi d'aire"
A += 1
assert sp.simplify((M_P / H)**p - aire) == 0, "(M_P/H)^(d-1) doit etre la MEME loi d'aire"
A += 1
# Consequence : l'accord d'exposant des deux routes est ADOSSE a ce socle commun
# (non independant au niveau de l'exposant). Le rapport des deux amplitudes est
# SANS N et SANS d (pur rapport de coefficients).
ratio = sp.simplify(A_T_R1 / A_T_R2)
assert N not in ratio.free_symbols and ell_dS not in ratio.free_symbols, \
    "le rapport R1/R2 doit etre un pur coefficient (meme exposant, socle partage)"
A += 1

# --- Produit A_T * C_T : N-INDEPENDANT, jamais un nombre -----------------------
prod_R1 = sp.simplify(A_T_R1 * C_T)
prod_R2 = sp.simplify(A_T_R2 * C_T)
assert ell_dS not in prod_R1.free_symbols and d not in prod_R1.free_symbols, \
    "A_T*C_T (R1) doit etre sans echelle ni d"
A += 1
assert ell_dS not in prod_R2.free_symbols, "A_T*C_T (R2) doit etre sans echelle"
A += 1

# --- GARDE-FOU anti-surclassement : COEFFICIENT O(1) LIBRE --------------------
assert {c_dim} & res_R1.free_symbols, "R1 : coefficient O(1) fixe a tort"
A += 1
assert {c_wf, c_CT} & res_R2.free_symbols, "R2 : coefficient O(1) fixe a tort"
A += 1
assert not prod_R1.is_number, "A_T*C_T (R1) ne doit pas etre un nombre"
A += 1
assert not prod_R2.is_number, "A_T*C_T (R2) ne doit pas etre un nombre"
A += 1

# --- RECUPERATION d=3 (le cas physique du programme) --------------------------
exp_d3 = p.subs(d, 3)
assert exp_d3 == 2, "a d=3, l'exposant de loi d'aire (d-1) vaut 2"
A += 1
A_T_R1_d3 = sp.simplify(A_T_R1.subs(d, 3))
assert sp.simplify(A_T_R1_d3 - c_dim * (H / M_P)**2) == 0, \
    "a d=3, A_T(R1) = c_dim (H/M_P)^2"
A += 1

# --- Coherence momentum : <TT> ~ k^(2 Delta_T - d), Delta_T = d ----------------
Delta_T = d
k_power = 2 * Delta_T - d            # = d  (symbolique)
assert sp.simplify(k_power - d) == 0, "k_power doit valoir d (Delta_T=d)"
A += 1
assert k_power.subs(d, 3) == 3, "a d=3 : <TT> ~ k^3, raccord avec <g3 g3> ~ k^3 (SPECTRE-K3)"
A += 1

print("=" * 72)
print("verif_F5_scaling.py  —  sceau de scaling DURCI (F5-c, R-28, d symbolique)")
print("-" * 72)
print("  exposant de loi d'aire  p = d-1   (= 2 a d=3)")
print(f"  A_T (R1) = {sp.simplify(A_T_R1)}")
print(f"  A_T (R2) = {A_T_R2}     ;   C_T = {C_T}")
print(f"  A_T*N (R1) = {res_R1}   (= c_dim : IDENTITE, sans ell NI d)")
print(f"  A_T*N (R2) = {res_R2}   (sans ell ni d)")
print("  N = C_T/c_CT = (M_P/H)^(d-1) = (ell_dS/ell_P)^(d-1)  <-- socle d'aire PARTAGE")
print(f"  A_T*C_T (R1) = {prod_R1}  (sans echelle, coeff. indetermine)")
print("-" * 72)
print(f"OK — {A} assertions. A_T ~ N^-1 : IDENTITE pour TOUT d (socle loi d'aire partage).")
print("    Routes independantes EN CONTENU (R2 = 1/raideur holographique) mais")
print("    NON independantes au niveau de l'EXPOSANT (accord adosse au socle d'aire).")
print("    COEFFICIENT O(1) NON fixe (a inventer, requiert O2). N NON fixe.")
print("    Sans surclassement : {A4 ; A2*  ; N} INCHANGÉ ; D1 non clos. EXIT 0.")
print("=" * 72)
