#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_crossover_matching.py — LC-RACCORD, front (a) du raccord, étape (a1).
(Compagnon de LC-D3-CROSSOVER-MATCHING.)

QUESTION (a1). Au crossover 𝒞 (bandage region : ĝ=Ω̂²g, ǧ=Ω̌²g, MÊME pont régulier g,
réciprocité Ω̂Ω̌=-1), l'énoncé « le nouvel éon naît dans le vide » se traduit par la
donnée classique de marée ĝ₃ = 0 (= C->0 de LC-D3) du côté passé. Le matching
    ĝ₃ = 0   ↦   ǧ₃ = 0
est-il CONSISTANT (point fixe du raccordement) sous les prescriptions de l'atlas D1
(Tod / Newman / Nurowski), AU NIVEAU LINÉAIRE ? (Le non-linéaire = (a2)/(a3).)

MÉCANISME testé. La marée g₃ (= Weyl rescalé TT) est portée par le pont PARTAGÉ g.
Le Weyl (1,3) C^a_bcd est conformément invariant : ĝ, g, ǧ partagent le MÊME C^a_bcd.
Donc ĝ₃ et ǧ₃ sont deux rescalings d'un même datum radiatif du pont. La carte
ĝ₃ ↦ ǧ₃ induite par réciprocité est LINÉAIRE HOMOGÈNE (multiplicative) : 0 ↦ 0 forcé.
La liberté de prescription (le c₁ de l'atlas) n'affecte que le FACTEUR de proportion
(carte des tides NON nulles -> pertinent pour (a3)), pas l'existence du point fixe à 0.
Une source TT additive serait nécessaire pour casser 0↦0 ; or le fond FLRW (isotrope,
conformément plat) n'admet AUCUN tenseur TT local -> aucune prescription locale ne peut
en injecter.

Sceaux :
  [S1] Fond du crossover sans marée  : Weyl(dS planaire) = 0  ET  Weyl(radiation-FRW
       obtenue par réciprocité Ω̌=-1/Ω̂) = 0.  => ĝ₃ = ǧ₃ = 0 (point fixe trivial existe).
  [S2] Weyl (1,3) conformément invariant (lemme « la tide est partagée ») : vérifié
       sur une métrique-test à Weyl NON nul (diagonale, type Kasner), g vs Ω(t)²g.
  [S3] Réciprocité homogène : Ω̌=-1/Ω̂, perturbation Ω̂->Ω̂(1+φ) => δ(lnΩ̌)=-δ(lnΩ̂),
       purement multiplicatif, AUCUN terme additif -> 0 ↦ 0.
  [S4] Lemme « pas de source » : le fond FLRW/isotrope n'a pas de partie TT (la
       projection TT d'un tenseur isotrope c·δ_ij est nulle) -> g₂ (Schouten local) n'a
       pas de part TT, et le mode libre étant nul, g₃^TT = 0 des deux côtés.

Dépendances : sympy. Re-exécutable, sans réseau.
Réfs (cf. LC-04) : Penrose, Cycles of Time (2010) — réciprocité ; Friedrich CMP 107
(1986) — donnée (g₀,g₃) ; de Haro–Skenderis–Solodukhin CMP 217 (2001) — FG ;
Markwell–Stevens GRG 55, 93 (2023) — atlas des prescriptions.
"""

import sympy as sp

print("="*74)
print(" verif_D3_crossover_matching.py — (a1) consistance de ĝ₃=0 ↦ ǧ₃=0 au crossover")
print("="*74)

# ======================================================================
# Machinerie : Christoffel, Riemann (1,3), Ricci, Weyl (0,4) et (1,3), n=4.
# ======================================================================
def christoffel(g, X):
    n = len(X); gi = g.inv()
    return [[[sp.simplify(sum(sp.Rational(1,2)*gi[l,m]*(sp.diff(g[m,i],X[j])
              + sp.diff(g[m,j],X[i]) - sp.diff(g[i,j],X[m])) for m in range(n)))
              for j in range(n)] for i in range(n)] for l in range(n)]

def riemann_up(g, X):  # R^a_{bcd}
    n = len(X); G = christoffel(g, X)
    R = [[[[0]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    R[a][b][c][d] = sp.simplify(
                        sp.diff(G[a][d][b], X[c]) - sp.diff(G[a][c][b], X[d])
                        + sum(G[a][c][e]*G[e][d][b] - G[a][d][e]*G[e][c][b] for e in range(n)))
    return R

def weyl_tensors(g, X):
    n = len(X); gi = g.inv()
    Ru = riemann_up(g, X)
    # Riemann tout bas R_{abcd}=g_{ae}R^e_{bcd}
    Rl = [[[[sp.simplify(sum(g[a,e]*Ru[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Ru[a][b][a][d] for a in range(n))))
    Rs = sp.simplify(sum(gi[b,d]*Ric[b,d] for b in range(n) for d in range(n)))
    # Weyl (0,4), n=4
    def Cl(a,b,c,d):
        return sp.simplify(
            Rl[a][b][c][d]
            - sp.Rational(1,2)*(g[a,c]*Ric[b,d]-g[a,d]*Ric[b,c]-g[b,c]*Ric[a,d]+g[b,d]*Ric[a,c])
            + sp.Rational(1,6)*Rs*(g[a,c]*g[b,d]-g[a,d]*g[b,c]))
    C0 = [[[[Cl(a,b,c,d) for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    # Weyl (1,3) C^a_{bcd}=g^{ae}C_{ebcd}
    C1 = [[[[sp.simplify(sum(gi[a,e]*C0[e][b][c][d] for e in range(n)))
             for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
    return C0, C1, Ric, Rs

# ======================================================================
# [S1] Fond du crossover sans marée : Weyl(dS)=0 et Weyl(radiation)=0.
# ======================================================================
print("\n[S1] Fond du crossover (réciprocité dS->radiation) : marée de fond nulle ?")
eta, H = sp.symbols('eta H', positive=True)
Xb = [eta, sp.symbols('x1 x2 x3', real=True)[0],
      sp.symbols('x1 x2 x3', real=True)[1], sp.symbols('x1 x2 x3', real=True)[2]]
x1, x2, x3 = Xb[1], Xb[2], Xb[3]

# Passé : dS planaire, Ω̂ = -1/(Hη)  ->  ĝ = Ω̂² (Mink)
def all_zero(C):
    return all(sp.simplify(C[a][b][c][d]) == 0 for a in range(4) for b in range(4)
               for c in range(4) for d in range(4))
def any_nonzero(C):
    return any(sp.simplify(C[a][b][c][d]) != 0 for a in range(4) for b in range(4)
               for c in range(4) for d in range(4))

Omh = -1/(H*eta)
g_dS = sp.diag(-Omh**2, Omh**2, Omh**2, Omh**2)
_, C1_dS, _, Rs_dS = weyl_tensors(g_dS, Xb)
print("     passé  dS planaire : R =", sp.simplify(Rs_dS), "(=4Λ) ; tous C^a_bcd nuls :", all_zero(C1_dS))
assert all_zero(C1_dS)

# Futur par réciprocité : Ω̌ = -1/Ω̂ = Hη  ->  ǧ = Ω̌² (Mink)  (radiation : R=0)
Omc = -1/Omh
g_rad = sp.diag(-Omc**2, Omc**2, Omc**2, Omc**2)
_, C1_rad, Ric_rad, Rs_rad = weyl_tensors(g_rad, Xb)
print("     futur  réciprocité : a(η)=Hη, R =", sp.simplify(Rs_rad),
      "(radiation) ; tous C^a_bcd nuls :", all_zero(C1_rad))
assert all_zero(C1_rad)
print("     => ĝ₃ = ǧ₃ = 0 sur le fond : le point fixe ĝ₃=0↦ǧ₃=0 EXISTE (trivialement).")

# ======================================================================
# [S2] Weyl (1,3) conformément invariant — lemme « la tide est partagée ».
#      Métrique-test à Weyl NON nul (diagonale, exposants génériques) ; g vs Ω²g.
# ======================================================================
print("\n[S2] Lemme : C^a_bcd conformément invariant (=> tide portée par le pont partagé)")
t = sp.symbols('t', positive=True)
Xk = [t, x1, x2, x3]
g_test = sp.diag(-1, t**2, t**4, t**6)            # diagonale, Weyl non nul
_, C1_g, _, _ = weyl_tensors(g_test, Xk)
print("     métrique-test diag(-1, t², t⁴, t⁶) : Weyl non nul :", any_nonzero(C1_g))
assert any_nonzero(C1_g)

Om = t                                            # facteur conforme test Ω(t)=t
g_resc = (Om**2) * g_test
_, C1_resc, _, _ = weyl_tensors(g_resc, Xk)
same = all(sp.simplify(C1_g[a][b][c][d] - C1_resc[a][b][c][d]) == 0
           for a in range(4) for b in range(4) for c in range(4) for d in range(4))
print("     g  vs  Ω²g  :  C^a_bcd[g] == C^a_bcd[Ω²g] pour tout (a,b,c,d) :", same)
assert same
print("     => C^a_bcd INVARIANT : ĝ, g, ǧ (mutuellement conformes) partagent la marée.")

# ======================================================================
# [S3] Réciprocité homogène : Ω̌=-1/Ω̂, perturbation multiplicative -> 0↦0.
# ======================================================================
print("\n[S3] Réciprocité Ω̂Ω̌=-1 : la carte de perturbation est-elle homogène (sans source) ?")
eps, phi = sp.symbols('epsilon phi')
Omh_pert = Omh*(1 + eps*phi)                      # Ω̂ -> Ω̂(1+εφ)
Omc_pert = -1/Omh_pert                            # réciprocité exacte
ser = sp.series(Omc_pert, eps, 0, 3).removeO()
ser = sp.expand(ser)
c_const = ser.coeff(eps, 0)
c_lin   = sp.simplify(ser.coeff(eps, 1))
print("     Ω̌(ε) =", sp.simplify(ser))
print("     terme ε⁰ =", sp.simplify(c_const), " (= Ω̌ de fond, AUCUNE source ajoutée)")
print("     terme ε¹ =", c_lin, " = -φ·Ω̌_fond  => δ(lnΩ̌) = -δ(lnΩ̂) (linéaire)")
assert sp.simplify(c_const - Omc) == 0                       # fond intact
assert sp.simplify(c_lin - (-phi*Omc)) == 0                  # purement multiplicatif
print("     => perturbation passée nulle (φ=0) -> perturbation future nulle : 0 ↦ 0.")

# ======================================================================
# [S4] Lemme « pas de source » : le fond isotrope/FLRW n'a pas de partie TT.
#      Projecteur TT sur une 3-métrique plate (mode k le long de x3).
# ======================================================================
print("\n[S4] Lemme : un fond isotrope (FLRW) n'admet aucun tenseur TT local (pas de source)")
# Tenseur isotrope candidat-source : S_ij = c·δ_ij (Schouten/Ricci d'un fond FLRW plat).
c = sp.symbols('c')
S = sp.diag(c, c, c)                              # 3x3 isotrope
# Projecteur TT pour un mode k = (0,0,k) : transverse (P^z=0) + sans trace.
# P_ij = δ_ij - k_i k_j/k² ; ici annule la composante z.
P = sp.diag(1, 1, 0)
# part transverse : (P S P) ; puis retrait de la trace transverse (/dim transverse=2)
PSP = P*S*P
trT = sp.trace(PSP)
S_TT = sp.simplify(PSP - sp.Rational(1,2)*trT*P)
print("     S_ij = c·δ_ij (isotrope) ; projection transverse-sans-trace S^TT =")
sp.pprint(S_TT)
assert S_TT == sp.zeros(3, 3)
print("     => S^TT = 0 : aucune marée TT constructible localement sur un fond isotrope.")
print("        Donc g₂ (Schouten, local) n'a pas de part TT ; mode libre nul => g₃^TT = 0.")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-"*74)
print(" VERDICT (a1) — niveau LINÉAIRE, fond FLRW :")
print("   [S1] le point fixe ĝ₃=0↦ǧ₃=0 existe (fond du crossover sans marée).")
print("   [S2] C^a_bcd conformément invariant : ĝ₃ et ǧ₃ rescalent une marée PARTAGÉE.")
print("   [S3] la carte induite par réciprocité est homogène (multiplicative) : 0↦0.")
print("   [S4] aucune source TT n'existe sur un fond isotrope : nulle prescription")
print("        locale ne peut envoyer ĝ₃=0 vers ǧ₃≠0.")
print("   ==> MATCHING ĝ₃=0 ↦ ǧ₃=0 CONSISTANT ET FORCÉ pour Tod/Newman/Nurowski.")
print("       La liberté c₁ de l'atlas ne change que le FACTEUR (tides ≠0) -> (a3).")
print(" RÉSERVES (décision ouverte, NON couvert ici) :")
print("   - O(h²) : back-réaction des fluctuations k³ (peut briser l'homogénéité) -> (a2).")
print("   - stabilité/unicité du point fixe ; couplage au runaway (m,λ) atlas §4-bis -> (a3).")
print("   - fond ANISOTROPE (Bianchi A) : le cisaillement fournit une structure TT")
print("     -> la carte peut devenir inhomogène (source) -> atlas inhomogène.")
print("   - état de raccordement non-unitaire (dS/CFT) : source non-locale possible -> (a2).")
print("-"*74)
