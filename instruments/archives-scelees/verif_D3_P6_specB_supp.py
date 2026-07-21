#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compléments au POC spec B : (a) ε_out vs ε_in (discriminant Wald/bang),
(b) poussée Ω_σ→1 profonde (multiplication des rebonds, trend ε_out),
(c) compte de rebonds sur sortie DENSE (le détecteur grossier sous-comptait)."""
import numpy as np
from scipy.integrate import solve_ivp

def ricci3_components(A1,A2,A3):
    l1,l2,l3=A1/(A2*A3),A2/(A3*A1),A3/(A1*A2)
    s=0.5*(l1+l2+l3); m1,m2,m3=s-l1,s-l2,s-l3
    return np.array([2*m2*m3,2*m3*m1,2*m1*m2])
def rhs(N,y,Lam):
    w1,w2,s1,s2,H,rho=y; w3=-w1-w2; s3=-s1-s2
    A=np.exp(np.array([w1,w2,w3])); a=np.exp(N)
    R3c=ricci3_components(*(a*A)); R3s=R3c.sum(); S=R3c-R3s/3
    sig2=0.5*(s1**2+s2**2+s3**2)
    return [s1/H,s2/H,-3*s1-S[0]/H,-3*s2-S[1]/H,
            (-H**2-(2/3)*sig2-rho/3+Lam/3)/H,-4*rho]
def kasner_p(u):
    d=1+u+u*u; return np.array([-u,1+u,u*(1+u)])/d
def build(eps,Om,u=2.0,rho0=100.0,Lam=1.0,perm=(0,1,2)):
    w0=np.array([eps,-eps,0.0]); F=ricci3_components(*np.exp(w0)).sum()
    H=np.sqrt((rho0+Lam-0.5*F)/(1-Om)/3)
    p=kasner_p(u)[list(perm)]; sig=H*np.sqrt(Om)*(3*p-1)
    return [w0[0],w0[1],sig[0],sig[1],H,rho0],H
def eps_w(w1,w2): w3=-w1-w2; return np.sqrt(w1*w1+w2*w2+w3*w3)/np.sqrt(2)
def run(eps,Om,u=2.0,perm=(0,1,2),Nmax=50.0):
    y0,_=build(eps,Om,u,perm=perm)
    s=solve_ivp(rhs,[0,Nmax],y0,args=(1.0,),method='Radau',rtol=1e-10,atol=1e-12,
                dense_output=True)
    # sortie dense pour rebonds + gel
    Ng=np.linspace(0,Nmax,6000); Y=s.sol(Ng)
    w1,w2,s1,s2,H,rho=Y; w3=-w1-w2; s3=-s1-s2
    a=np.exp(Ng)
    R3=np.array([ricci3_components(*(a[k]*np.exp(np.array([w1[k],w2[k],w3[k]]))))
                 for k in range(len(Ng))])
    R3s=R3.sum(axis=1); S=R3-(R3s/3)[:,None]; Smag=np.sqrt((S**2).sum(axis=1))
    sig2=0.5*(s1**2+s2**2+s3**2); Omsig=sig2/(3*H**2)
    # rebonds : pics de |³S| au-dessus de 3× le fond local glissant
    peaks=0
    for k in range(3,len(Smag)-3):
        loc=np.median(Smag[max(0,k-200):k+200])+1e-30
        if Smag[k]>5*loc and Smag[k]>=Smag[k-1] and Smag[k]>Smag[k+1]:
            peaks+=1
    eps_out=eps_w(w1[-1],w2[-1])
    eps_mid=eps_w(w1[len(Ng)//2],w2[len(Ng)//2])
    return dict(eps_out=float(eps_out),eps_mid=float(eps_mid),
                Omsig_end=float(Omsig[-1]),bounces=peaks,
                frozen=abs(eps_out-eps_mid)<1e-6)

print("="*78)
print(" (a) DISCRIMINANT : ε_out dépend-il de ε_in ?  (Wald: ε_out∝ε_in ; bang: ⊥)")
print("="*78)
print("   À Ω_σ fixé, varier ε_in. Si ε_out ~ const ⟹ le bang fixe la forme (bang gagne).")
for Om in [0.5,0.9]:
    print(f"   --- Ω_σ={Om} ---")
    print("     ε_in      ε_out      ε_out/ε_in")
    base=None
    for ein in [0.01,0.02,0.05,0.10,0.20]:
        d=run(ein,Om); 
        print(f"     {ein:.3f}     {d['eps_out']:.5f}    {d['eps_out']/ein:7.2f}")

print("\n"+"="*78)
print(" (b) POUSSÉE PROFONDE Ω_σ→1 : rebonds se multiplient ? ε_out sature/diverge ?")
print("="*78)
print("     1−Ω_σ      ε_out      bounces   Ω_σ_end    frozen")
for Om in [0.9,0.99,0.999,0.9999,0.99999]:
    d=run(0.05,Om,Nmax=60.0)
    print(f"     {1-Om:.0e}    {d['eps_out']:.5f}     {d['bounces']:3d}     {d['Omsig_end']:.1e}   {d['frozen']}")

print("\n"+"="*78)
print(" (c) ε_out moyenné sur l'axe BKL u et permutations (à Ω_σ=0.99) — enveloppe")
print("="*78)
vals=[]
for u in [1.0,1.3,1.6,2.0,3.0,5.0,9.0]:
    for perm in [(0,1,2),(1,2,0),(2,0,1)]:
        d=run(0.05,0.99,u=u,perm=perm); vals.append(d['eps_out'])
vals=np.array(vals)
print(f"   ε_out sur {len(vals)} (u,axe) : min={vals.min():.3f}  médiane={np.median(vals):.3f}  "
      f"max={vals.max():.3f}  moy={vals.mean():.3f}")
print(f"   => même la plus FAVORABLE des orientations donne ε_out={vals.min():.3f} (ε_in=0.05).")

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertion machine ajoutee (additif) ---
# Discriminant Wald/bang : au deep-bang (Ω_σ=0.99) ε_out se FIGE (Kasner gele) entre mi-parcours et fin.
_d = run(0.05, 0.99, Nmax=60.0)
assert _d["frozen"], "P6_specB_supp: au deep-bang ε_out doit etre fige (|eps_out-eps_mid|<1e-6)"
print("EXIT 0 (F1: assertion eps_out fige verifiee)")
