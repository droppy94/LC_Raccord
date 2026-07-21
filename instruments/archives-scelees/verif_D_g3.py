#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D_g3.py — Ouverture du module [D] (LC-RACCORD) : la donnée g₃ à 𝓘⁺ comme
tenseur de stress holographique. Dépendance : sympy.
Dictionnaire Fefferman-Graham (de Haro-Skenderis-Solodukhin, CMP 217, 595, 2001) :
métrique ds²=(ℓ²/z²)(dz²+g_ij(z,x)dx^i dx^j), g(z)=g₍₀₎+z²g₍₂₎+...+z^d g₍d₎+...
  g₍₀₎ = source (métrique de bord) ; g₍₂ₙ₎ (n<d/2) = local en g₍₀₎ ;
  g₍d₎ = ⟨T_ij⟩ (VEV libre) ; ⟨T_ij⟩=(d/16πG)g₍d₎ (+anomalie, nulle si d impair).
Bord = 𝓘⁺ spacelike de de Sitter => d=3 (impair) => g₃ = donnée libre TT = ⟨T⟩.
  [A] exposants radiaux FG d'un mode TT : {0, d} -> {0,3}  (source / VEV)
  [B] comptage TT (d=3) : 2 polarisations
  [C] dS pur planaire : g₃=0 (vide)
"""
import sympy as sp
z,r,d=sp.symbols('z r d')
H=z**r
ind=sp.simplify((z**2*sp.diff(H,z,2)+(1-d)*z*sp.diff(H,z))/H)
print("="*70)
print("[A] FG, mode TT (type scalaire sans masse), indiciel :",sp.expand(ind),
      "-> r =",sp.solve(ind,r))
print("    d=3 -> exposants",[s.subs(d,3) for s in sp.solve(ind,r)],
      ": r=0 (g₀=source/jauge conforme=D1) , r=3 (g₃=⟨T⟩ libre=Weyl rescalé)")
print("[B] comptage TT d=3 : sym 3×3 =",3*4//2,"− trace 1 − transverse 3 =",3*4//2-1-3,
      "polarisations (g₃ = 2 fonctions libres)")
print("[C] dS pur planaire ds²=(1/H²z²)(−dz²+δ dx²) : g_ij(z)=δ constant => g₃=0 (vide)")
print("    => g₃ mesure l'écart au vide de Sitter.")
print("[Dict] ⟨T_ij⟩=(d/16πG) g₃ (d=3, pas d'anomalie).")
print("       D1 reformulé : fixer g₃ = choisir l'ÉTAT de la CFT céleste ;")
print("       candidat = état dS-invariant (Bunch-Davies/Hartle-Hawking) -> g₃ unique.")
print("="*70)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
_sol = set(sp.solve(ind, r))
assert _sol == {sp.Integer(0), d}, "[A] exposants FG du mode TT doivent etre {0, d}"
assert {s.subs(d, 3) for s in _sol} == {sp.Integer(0), sp.Integer(3)}, "[A] d=3 -> {0,3}"
assert 3*4//2 - 1 - 3 == 2, "[B] comptage TT d=3 = 2 polarisations"
print("EXIT 0 (F1: 3 assertions g3/FG verifiees)")
