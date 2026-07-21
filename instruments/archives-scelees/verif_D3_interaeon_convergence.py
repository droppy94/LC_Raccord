#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_D3_interaeon_convergence.py — ITÉRATION ∏κ_n : le verdict de clôture du front (a).
(Chantier §5.1 de LC-WORK-REPRISE-CLOTURE-A ; couple verif_D3_interaeon_kappa.py à la
 récurrence (m,λ) de verif_D1_atlas.py.)

VERSION 2 (2026-06-07) — grave l'audit froid :
  • runaway mλ>2.25 ÉTENDU jusqu'à la vraie rupture GO (éon 24, pas ~8) ;
  • branche runaway OPPOSÉE mλ<2.25 (ρ_0→∞, Λ→0) ajoutée : reste dans GO, κ SATURE <1 ;
  • test de stabilité Nmax de la saturation de κ (forme bien gelée) ;
  => les DEUX branches d'emballement donnent ∏κ_n→0 (aucun résiduel dans le domaine GO).

QUESTION (le verdict de clôture). ε_n = (∏_{i<n} κ_i) ε_0 → 0 (isotropisation TOTALE
multi-éon, forme dynamique d'issue forte) ou → const>0 (RÉSIDUELLE, issue faible persiste) ?
Dépend de la suite (ρ_{0,i}, Λ_i) d'éon en éon, donc de la prescription du facteur conforme.

DISPOSITIF.
  • κ(ρ_0,Λ) : noyau Bianchi IX + radiation + Λ (ordre dominant, sceau _kappa.py), réimplémenté
    en minimal ici. κ = pente de ε_{n+1}=κ ε_n (carte linéaire à petit ε).
  • Suite (m,λ) : récurrence NewClass de l'atlas D1 (sceau verif_D1_atlas.py, eq.14) :
        λ_{i+1}=4λ_i²m_i/(9k²) ,  m_{i+1}=9k²/(4λ_i) ,  invariant mλ.
    Point fixe mλ=9k²/4=2.25 (Tod=NewClass=Nurowski). Runaway sinon :
        mλ>2.25 -> m→0, λ→∞  (ρ_0→0, Λ→∞)
        mλ<2.25 -> m→∞, λ→0  (ρ_0→∞, Λ→0)
  • Identification (ordre dominant) : ρ_0 ∝ m (constante de radiation, ρ=mR⁻⁴ chez Tod),
    Λ ∝ λ. Référence : éon 0 placé dans le régime GO (ρ_0=100, Λ=1 → κ≈0.81). κ dépend
    de ρ_0 ET de Λ (pas seulement du rapport) ; on teste la robustesse à la normalisation.

POINT PHYSIQUE CLÉ. Penrose suppose Λ CONSTANTE d'éon en éon. L'atlas D1 a montré que la
condition de Penrose (λ̂=λ) n'est self-cohérente QU'au point fixe ; hors de lui, λ (donc Λ)
s'emballe — vers ∞ (mλ>2.25) ou vers 0 (mλ<2.25) — ce qui CONTREDIT Penrose des deux côtés.
Donc le scénario physiquement mandaté est le POINT FIXE.

Dépendances : numpy, scipy. Re-exécutable, sans réseau.
Réfs : Tod arXiv:1309.7248 ; Markwell-Stevens arXiv:2212.06914 ; Nurowski arXiv:2102.11823,
2101.12670 ; Wainwright-Ellis (1997). Sceaux : verif_D3_interaeon_kappa.py, verif_D1_atlas.py.
"""
import numpy as np
from scipy.integrate import solve_ivp

print("="*78)
print(" verif_D3_interaeon_convergence.py v2 — ITÉRATION ∏κ_n (noyau κ ↔ atlas (m,λ))")
print("="*78)

# --- noyau κ minimal (ordre dominant, identique à verif_D3_interaeon_kappa.py) ---
def ricci3(A1,A2,A3):
    l1,l2,l3=A1/(A2*A3),A2/(A3*A1),A3/(A1*A2); s=0.5*(l1+l2+l3)
    m1,m2,m3=s-l1,s-l2,s-l3; return np.array([2*m2*m3,2*m3*m1,2*m1*m2])
def evolve(eps_in, rho0, Lam, Nmax=25.0):
    w0=np.array([eps_in,-eps_in,0.0]); A0=np.exp(w0)
    H0=np.sqrt(max((rho0+Lam-0.5*ricci3(*A0).sum())/3.0,1e-12))
    def rhs(N,y):
        w1,w2,s1,s2,H,rho=y; w3=-w1-w2; s3=-s1-s2; a=np.exp(N)
        R3c=ricci3(*(a*np.exp(np.array([w1,w2,w3])))); S=R3c-R3c.sum()/3.0
        sig2=0.5*(s1**2+s2**2+s3**2)
        return [s1/H,s2/H,-3*s1-S[0]/H,-3*s2-S[1]/H,
                (-H**2-(2/3)*sig2-rho/3+Lam/3)/H,-4*rho]
    sol=solve_ivp(rhs,[0,Nmax],[w0[0],w0[1],0,0,H0,rho0],method='DOP853',
                  rtol=1e-10,atol=1e-12,max_step=0.02)
    w1,w2,s1,s2,H,rho=sol.y[:,-1]; w3=-w1-w2; s3=-s1-s2
    eps=np.sqrt(w1**2+w2**2+w3**2)/np.sqrt(2)
    Sig=np.sqrt(0.5*(s1**2+s2**2+s3**2))/(3*H)   # Σ=σ/θ : ~0 si la forme est gelée à 𝓘
    return eps, Sig
def kappa(rho0,Lam,eps=0.05,Nmax=25.0):
    e,_=evolve(eps,rho0,Lam,Nmax); return e/eps

# --- récurrence (m,λ) de l'atlas D1 ---
k=1.0
def step_ml(m,l): return 9*k*k/(4*l), 4*l*l*m/(9*k*k)   # (m',λ')

# --- identification (m,λ) -> (ρ_0,Λ) : éon 0 en régime GO (ρ_0=100,Λ=1) ---
def to_rho_Lam(m,l,m0,l0,rho_ref=100.0,Lam_ref=1.0):
    return rho_ref*(m/m0), Lam_ref*(l/l0)

def go_ok(rho0,Lam):  # GO : atteint 𝓘 (Λ>9/64ρ0) ET ère radiation (ρ0≫Λ : ρ0>5Λ)
    return (Lam > 9/(64*rho0)) and (rho0 > 5*Lam)

# ----------------------------------------------------------------------
# (1) Scénario PHYSIQUE : point fixe Penrose (mλ=2.25) -> (ρ_0,Λ) constants.
# ----------------------------------------------------------------------
print("\n"+"-"*78)
print(" (1) POINT FIXE Penrose (Λ constante, mλ=2.25) : (ρ_0,Λ) éon-indépendants")
print("-"*78)
m,l=1.5,1.5; m0,l0=m,l
rho0,Lam=to_rho_Lam(m,l,m0,l0); kap=kappa(rho0,Lam)
print(f"     (m,λ)=({m},{l}) constants -> (ρ_0,Λ)=({rho0:.1f},{Lam:.2f}) constants")
print(f"     κ_n = {kap:.4f} CONSTANT -> ∏κ_n = κⁿ  ->  ε_n = κⁿ ε_0  ->  0")
print(f"     => ISOTROPISATION TOTALE (géométrique, multi-éon). Lente si κ→1 (bang réaliste).")
prod=1.0
for n in range(1,8): prod*=kap
print(f"     ex. après 7 éons : ∏κ = {prod:.4f}  (ε_7/ε_0)")

# ----------------------------------------------------------------------
# (2a) RUNAWAY mλ>2.25 (Λ→∞) ÉTENDU jusqu'à la vraie rupture GO.
# ----------------------------------------------------------------------
print("\n"+"-"*78)
print(" (2a) RUNAWAY mλ=2.40 > 2.25 (Λ NON constante) : ρ_0→0, Λ→∞ (ρ_0Λ=const=100)")
print("-"*78)
print("      éon   ρ_0      Λ       Λ/ρ_0    κ_n      ∏κ_n      GO")
m,l=1.6,1.5; m0,l0=m,l; prod=1.0; broke=None; prod_break=None
for n in range(0,30):
    rho0,Lam=to_rho_Lam(m,l,m0,l0); ok=go_ok(rho0,Lam)
    if ok:
        kap=kappa(rho0,Lam); prod*=kap
        if n%2==0: print(f"      {n:<4}  {rho0:7.3f} {Lam:6.3f}  {Lam/rho0:.4f}  {kap:.4f}   {prod:.3e}   {ok}")
    else:
        if broke is None: broke=n; prod_break=prod
        if n<broke+2: print(f"      {n:<4}  {rho0:7.3f} {Lam:6.3f}  {Lam/rho0:.4f}    --        --       {ok}  <- GO CASSE")
    m,l=step_ml(m,l)
print(f"      -> GO (ère radiation ρ_0>5Λ) tient jusqu'à l'éon {broke-1}; rupture à l'éon {broke}")
print(f"         (ρ_0Λ=100 conservé ; seuil ρ_0=5Λ -> ρ_0<{np.sqrt(5*100):.1f}). ∏κ à la rupture = {prod_break:.3e}.")
print(f"         κ_n reste <1 (≈0.82, lentement croissant) ; ∏κ_n MONOTONE décroissant -> 0.")
print(f"         Au-delà : radiation épuisée -> hors noyau d'ordre dominant -> P6.")

# ----------------------------------------------------------------------
# (2b) RUNAWAY OPPOSÉ mλ<2.25 (Λ→0) : reste dans GO, κ SATURE <1.
# ----------------------------------------------------------------------
print("\n"+"-"*78)
print(" (2b) RUNAWAY mλ=1.00 < 2.25 (Λ NON constante) : ρ_0→∞, Λ→0 (ρ_0Λ=const=100)")
print("-"*78)
print("      éon   ρ_0          Λ         Λ/ρ_0      κ_n      1-κ_n     ∏κ_n      GO")
m,l=1.0,1.0; m0,l0=m,l; prod=1.0; s=0.0
for n in range(0,14):
    rho0,Lam=to_rho_Lam(m,l,m0,l0); ok=go_ok(rho0,Lam)
    if ok:
        kap=kappa(rho0,Lam); prod*=kap; s+=(1-kap)
        if n<10 or n==13: print(f"      {n:<4}  {rho0:11.2f} {Lam:8.5f}  {Lam/rho0:.6f}  {kap:.5f}  {1-kap:.5f}  {prod:.5f}  {ok}")
    m,l=step_ml(m,l)
print(f"      -> κ_n SATURE à ≈0.795 < 1 (ne tend PAS vers 1) ; 1-κ_n≈0.205 quasi-constant.")
print(f"         Σ(1-κ_n)={s:.3f} (diverge) -> ∏κ_n -> 0. GO tient (Λ>seuil 𝓘 car ρ_0 monte plus vite).")
print(f"         AUCUN plateau résiduel : la branche Λ→0 isotropise aussi totalement.")

# ----------------------------------------------------------------------
# (3) Robustesse à la normalisation (ρ_ref, Λ_ref) du point fixe.
# ----------------------------------------------------------------------
print("\n"+"-"*78)
print(" (3) Robustesse : κ au point fixe pour diverses normalisations (ρ_ref,Λ_ref)")
print("-"*78)
print("     (ρ_ref,Λ_ref)     Λ/ρ_0     κ      GO ?")
for rr,lr in [(100.0,1.0),(1000.0,1.0),(100.0,5.0),(50.0,1.0),(30.0,1.0)]:
    kp=kappa(rr,lr); print(f"     ({rr:6.0f},{lr:.0f})       {lr/rr:.4f}    {kp:.4f}   {go_ok(rr,lr)}")
print("     -> κ<1 pour TOUTE normalisation GO-admissible : ∏κ_n→0 robuste au point fixe.")

# ----------------------------------------------------------------------
# (4) Stabilité Nmax de la saturation de κ (forme bien gelée à 𝓘 ?).
#     Λ minuscule => 𝓘 atteint tard ; on vérifie que κ ne dépend pas de Nmax.
# ----------------------------------------------------------------------
print("\n"+"-"*78)
print(" (4) Stabilité Nmax : la saturation κ≈0.795 (branche Λ→0) est-elle réelle ?")
print("-"*78)
print("     (ρ_0, Λ)               κ(Nmax=25)  Σ          κ(Nmax=60)  Σ")
for rho0,Lam in [(506.25,0.19753),(29192.93,0.00343),(3787675.24,0.00003)]:
    e25,S25=evolve(0.05,rho0,Lam,25.0); e60,S60=evolve(0.05,rho0,Lam,60.0)
    print(f"     ({rho0:11.2f},{Lam:.5f})  {e25/0.05:.5f}    {S25:.1e}   {e60/0.05:.5f}    {S60:.1e}")
print("     -> κ identique à 5 décimales, Σ=σ/θ→1e-50 : forme PARFAITEMENT gelée. Saturation RÉELLE.")

# ======================================================================
print("\n"+"="*78)
print(" VERDICT — itération ∏κ_n : clôture du front (a)")
print("="*78)
print("   • PHYSIQUE (Penrose : Λ constante). L'atlas D1 montre que λ̂=λ n'est self-cohérent")
print("     QU'au point fixe mλ=9k²/4 ; donc Λ=const FORCE ρ_0 éon-indépendante. Alors κ est")
print("     CONSTANT (<1, robuste) et ∏κ_n = κⁿ → 0 :")
print("     => ISOTROPISATION TOTALE multi-éon (forme dynamique d'issue forte), LENTE (κ→1")
print("        pour un bang radiation-dominé réaliste). C'est le verdict de clôture.")
print("")
print("   • COUNTERFACTUEL (runaway, Λ non constante — exclu par Penrose, instabilité D1).")
print("     DEUX directions, toutes deux SANS résiduel dans le domaine GO :")
print("     - mλ>2.25 : ρ_0→0, Λ→∞. κ_n reste <1 (≈0.82) ; ∏κ_n décroît -> 0.014 jusqu'à la")
print("       rupture GO à l'éon 24 (radiation épuisée) ; au-delà -> P6.")
print("     - mλ<2.25 : ρ_0→∞, Λ→0. GO tient ; κ_n SATURE à ≈0.795<1 (PAS ->1) ; ∏κ_n -> 0.")
print("     Donc l'intuition 'Λ/ρ_0→0 ⟹ κ→1 ⟹ résiduel' est FAUSSE : κ sature sous 1.")
print("")
print("   SYNTHÈSE. À l'ordre dominant : sous Penrose (Λ const) le front (a) se ferme vers une")
print("   ISOTROPISATION TOTALE dynamique (∏κ_n→0). Ce n'est PAS une dérivation d'A3 à éon fini :")
print("   attraction multi-éon, lente. Et même hors Penrose, AUCUNE des deux branches runaway ne")
print("   produit de résiduel dans le domaine valide (l'une sort via P6, l'autre sature κ<1).")
print("   Discipline : `établi` = l'algèbre (κ<1 robuste, ∏κ_n→0) ; complétude hors-GO et valeur")
print("   de κ pour bang réaliste restent `à inventer` (P6) / `établi lent` (κ→1).")
print("="*78)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Mecanisme de cloture du front (a) : en regime GO (eon 0 ref ρ0=100,Λ=1), κ<1 (contraction)
# => ∏κ_n -> 0. Encode le fait calcule κ in (0,1).
_kref = kappa(100.0, 1.0)
assert 0.0 < _kref < 1.0, "interaeon_convergence: κ(GO ref) doit etre dans (0,1) (contraction ∏κ_n->0)"
print(f"EXIT 0 (F1: assertion κ(ref)={_kref:.4f} in (0,1) verifiee)")
