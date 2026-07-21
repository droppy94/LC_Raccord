#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D1_stabilite.py — Candidat-sélecteur #5 de D1 (stabilité inter-éons) et son
rapport à l'hypothèse de Weyl (D3). LC-RACCORD, module A. Dépendance : sympy.
  [A] Carte de stabilité (classe Penrose-cohérente, Markwell-Stevens eq.14) :
      invariant mλ ; droite fixe mλ=9k²/4 ; Jacobien non-hyperbolique (val.propre 1
      double) ; emballement géométrique hors de la droite ; dégénérescence à k=0.
  [B] Weyl : C≡0 en FLRW (indépendant de m,λ) ; C≠0 en Kasner (sourcé par
      l'anisotropie, sans matière ni Λ). => stabilité (fond) ⊥ Weyl (marée) en symétrie.
Conclusion : #5 ne FERME PAS D1 (relation, pas facteur unique ; vacant à k=0 ;
indépendant de D3 en FLRW). La fermeture exige le secteur inhomogène (g₃), où D3 agit.
"""
import sympy as sp
m,l,k,P = sp.symbols('m lambda k P', positive=True)
mp, lp = 9*k**2/(4*l), 4*l**2*m/(9*k**2)
print("="*70); print("[A] Carte T:(m,λ)->(m',λ')  (Markwell-Stevens eq.14)")
print("  invariant m'λ' =", sp.simplify(mp*lp), " => mλ conservé")
print("  droite fixe : m'=m <=> mλ = 9k²/4")
J = sp.Matrix([[sp.diff(mp,m),sp.diff(mp,l)],[sp.diff(lp,m),sp.diff(lp,l)]])
Jf = sp.simplify(J.subs(m, 9*k**2/(4*l)))
print("  Jacobien|fixe =", Jf.tolist(), " trace=",sp.simplify(Jf.trace()),
      " det=",sp.simplify(Jf.det())," val.propres=",list(Jf.eigenvals().keys()),"(1 double)")
print("  ratio m'/m sur niveau mλ=P :", sp.simplify(9*k**2/(4*P)),
      " (=1 ssi P=9k²/4 ; sinon emballement géométrique)")
print("  k=0 : droite fixe -> mλ=0 (dégénère) ; 55d c1²=2λ̂/3k diverge => #5 inapplicable")
print("="*70); print("[B] Tenseur de Weyl C_txtx : FLRW vs Kasner")
t,x,y,z=sp.symbols('t x y z'); X=[t,x,y,z]
def weyl_txtx(g):
    n=4; gi=g.inv()
    Ga=[[[sp.simplify(sum(gi[s,a]*(sp.diff(g[a,i],X[j])+sp.diff(g[a,j],X[i])-sp.diff(g[i,j],X[a]))for a in range(n))/2)for j in range(n)]for i in range(n)]for s in range(n)]
    Ru=lambda a,b,c,d:(sp.diff(Ga[a][b][d],X[c])-sp.diff(Ga[a][b][c],X[d])+sum(Ga[a][c][e]*Ga[e][b][d]-Ga[a][d][e]*Ga[e][b][c]for e in range(n)))
    Rl=lambda a,b,c,d:sp.simplify(sum(g[a,e]*Ru(e,b,c,d)for e in range(n)))
    Ric=[[sp.simplify(sum(Ru(a,i,a,j)for a in range(n)))for j in range(n)]for i in range(n)]
    R=sp.simplify(sum(gi[i,j]*Ric[i][j]for i in range(n)for j in range(n)))
    return sp.simplify(Rl(0,1,0,1)-sp.Rational(1,2)*(g[0,0]*Ric[1][1]-g[0,1]*Ric[1][0]-g[1,0]*Ric[0][1]+g[1,1]*Ric[0][0])+sp.Rational(1,6)*R*(g[0,0]*g[1,1]-g[0,1]*g[1,0]))
gF=sp.diag(-t**2,t**2,t**2,t**2)
gK=sp.diag(-1,t**sp.Rational(4,3),t**sp.Rational(4,3),t**sp.Rational(-2,3))  # Kasner (2/3,2/3,-1/3)
print("  FLRW radiation : C_txtx =", weyl_txtx(gF), "  (=0 : Weyl nul, indép. de m,λ)")
print("  Kasner aniso.  : C_txtx =", weyl_txtx(gK), "  (≠0 : Weyl sourcé par l'anisotropie)")
print("="*70)
print("VERDICT : #5 contraint (relation mλ=9k²/4, k≠0) mais ne FERME PAS D1 ;")
print("  Weyl≡0 en FLRW => D3 vacant dans le secteur symétrique ; pont #5->D3 non tenu ici.")
print("  Fermeture de D1 => secteur inhomogène (g₃), domaine propre de D3 (Weyl).")
print("="*70)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
# Encode [A] invariant conserve + Jacobien (vp 1 double) ; [B] Weyl FLRW=0, Kasner!=0.
assert sp.simplify(mp*lp - m*l) == 0, "A: invariant mλ doit etre conserve par T"
assert Jf.eigenvals() == {sp.Integer(1): 2}, "A: Jacobien|fixe doit avoir vp 1 (double, non-hyperbolique)"
assert sp.simplify(weyl_txtx(gF)) == 0, "B: Weyl C_txtx doit etre nul en FLRW"
assert sp.simplify(weyl_txtx(gK)) != 0, "B: Weyl C_txtx doit etre non nul en Kasner (anisotropie)"
print("EXIT 0 (F1: 4 assertions stabilite/Weyl verifiees)")
