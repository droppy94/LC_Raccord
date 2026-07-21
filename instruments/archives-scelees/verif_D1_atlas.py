#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_atlas.py — Atlas des prescriptions D1 (LC-RACCORD, module A).
Cas FLRW radiation + Λ, k=1. Les trois prescriptions (Tod 2015 ; Markwell-Stevens
/ Penrose-(55d) ; Nurowski 2021 corrigé) se ramènent à la MÊME famille Ω̂=c1·â
(pont à courbure scalaire constante R=6k c1²=4λ) ; la liberté résiduelle = le seul
c1. La divergence = quelle condition fixe c1. Réf. : Markwell & Stevens, GRG 55,93
(2023), eq. (11),(12),(13),(14). Dépendance : numpy.
  [D1.atlas]  Tod (m,λ const ; viole λ̂=λ) vs NewClass (λ̂=λ ; (m,λ) itèrent)
  [D1.runaway] itération inter-éons de NewClass : bifurcation instable (mλ conservé,
               m->0, λ->inf) sauf accord fin m̂λ̂=9k²/4 -> les deux coïncident.
"""
import numpy as np
k=1.0
def tod(mh,lh):
    c1=(lh/mh)**0.25; lam=6*k*c1**2/4
    return c1,lam,mh,lh,bool(np.isclose(lam,lh))
def newclass(mh,lh):
    c1=np.sqrt(2*lh/(3*k)); lam=6*k*c1**2/4
    mc=9*k**2/(4*lh); lc=4*lh**2*mh/(9*k**2)
    return c1,lam,mc,lc,bool(np.isclose(lam,lh))
print("="*72); print("[D1.atlas] FLRW radiation, k=1.  Famille Ω̂=c1·â ; liberté = c1.")
print("  point fixe m̂λ̂=9k²/4=2.25 => Tod = NewClass = Nurowski (coïncidence).")
print("  m̂   λ̂  | prescr.  | c1     λ_pont | (m̌,λ̌)         | Penrose λ̂=λ ?")
for mh,lh in [(1.5,1.5),(1.0,2.0),(0.9,1.6)]:
    for nm,f in [("Tod ",tod),("New ",newclass)]:
        c1,lam,mc,lc,pen=f(mh,lh)
        print(f"  {mh:<3} {lh:<3}| {nm}    | {c1:.4f} {lam:.4f} | ({mc:.3f},{lc:.3f}) | {pen}")
    print("  "+"-"*64)
print("="*72); print("[D1.runaway] itération inter-éons (NewClass, recurrence eq.14) :")
print("  λ_{i+1}=4λ_i²m_i/(9k²) , m_{i+1}=9k²/(4λ_i) ;  invariant : mλ")
def it(m,l,n=6):
    out=[(0,m,l)]
    for i in range(1,n+1):
        l,m=4*l*l*m/(9*k*k), 9*k*k/(4*l); out.append((i,m,l))
    return out
for tag,(m0,l0) in [("point fixe (mλ=2.25)",(1.5,1.5)),("perturbé (mλ=2.40)",(1.6,1.5))]:
    print(f"  {tag}:")
    for i,m,l in it(m0,l0): print(f"    éon {i}: m={m:.4f} λ={l:.4f}  mλ={m*l:.4f}")
print("  => hors accord fin : m->0, λ->inf (bifurcation instable). VERROU D1 a des dents.")
print("="*72)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
# Encode [D1.atlas]/[D1.runaway] : invariant mλ conserve ; point fixe mλ=9k²/4 ;
# emballement hors point fixe (m->0, λ->inf).
_fp = newclass(1.5, 1.5)              # point fixe mλ=2.25=9k²/4
assert np.isclose(_fp[2], 1.5) and np.isclose(_fp[3], 1.5), "D1.atlas: (1.5,1.5) doit etre point fixe NewClass"
_orb = it(1.6, 1.5, 6)               # orbite perturbee mλ=2.40
assert all(np.isclose(m*l, 1.6*1.5) for _, m, l in _orb), "D1.runaway: invariant mλ doit etre conserve"
_ms = [m for _, m, l in _orb]; _ls = [l for _, m, l in _orb]
assert _ms[-1] < _ms[0] and _ls[-1] > _ls[0], "D1.runaway: hors point fixe m->0, λ->inf (bifurcation)"
print("EXIT 0 (F1: 4 assertions D1.atlas/runaway verifiees)")
