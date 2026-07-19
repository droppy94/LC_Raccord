#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnostic d'architecture : l'intégration directe profonde capture-t-elle la
cascade Mixmaster (plusieurs rebonds) ou le germe de radiation la halte-t-il ?
On dump la trajectoire w(N), |³S|(N), et on compte les rebonds par DEUX méthodes :
(i) pics de |³S| ; (ii) renversements de la vitesse de forme dw/dN (signe de v·v_prev<0)."""
import numpy as np
from scipy.integrate import solve_ivp

def ricci3(A1,A2,A3):
    l1,l2,l3=A1/(A2*A3),A2/(A3*A1),A3/(A1*A2)
    s=0.5*(l1+l2+l3); return np.array([2*(s-l2)*(s-l3),2*(s-l3)*(s-l1),2*(s-l1)*(s-l2)])
def rhs(N,y,Lam):
    w1,w2,s1,s2,H,rho=y; w3=-w1-w2
    a=np.exp(N); R3c=ricci3(*(a*np.exp(np.array([w1,w2,w3])))); R3s=R3c.sum(); S=R3c-R3s/3
    sig2=0.5*(s1**2+s2**2+(s1+s2)**2)
    return [s1/H,s2/H,-3*s1-S[0]/H,-3*s2-S[1]/H,(-H**2-(2/3)*sig2-rho/3+Lam/3)/H,-4*rho]
def kasner_p(u):
    d=1+u+u*u; return np.array([-u,1+u,u*(1+u)])/d
def build(eps,Om,u=2.0,rho0=100.0,Lam=1.0):
    w0=np.array([eps,-eps,0.0]); F=ricci3(*np.exp(w0)).sum()
    H=np.sqrt((rho0+Lam-0.5*F)/(1-Om)/3); p=kasner_p(u); sig=H*np.sqrt(Om)*(3*p-1)
    return [w0[0],w0[1],sig[0],sig[1],H,rho0]

def analyze(Om,u=2.0,rho0=100.0,Nmax=60.0,ng=20000):
    y0=build(0.05,Om,u,rho0=rho0)
    s=solve_ivp(rhs,[0,Nmax],y0,args=(1.0,),method='Radau',rtol=1e-11,atol=1e-13,dense_output=True)
    Ng=np.linspace(0,Nmax,ng); Y=s.sol(Ng); w1,w2,s1,s2,H,rho=Y; w3=-w1-w2; s3=-s1-s2
    a=np.exp(Ng)
    R3=np.array([ricci3(*(a[k]*np.exp(np.array([w1[k],w2[k],w3[k]])))) for k in range(ng)])
    R3s=R3.sum(axis=1); S=R3-(R3s/3)[:,None]; Smag=np.sqrt((S**2).sum(axis=1))
    sig2=0.5*(s1**2+s2**2+s3**2); Omsig=sig2/(3*H**2)
    # (i) pics de |³S|
    peaks_S=[]
    for k in range(5,ng-5):
        if Smag[k]==max(Smag[k-5:k+6]) and Smag[k]>10*np.median(Smag[max(0,k-500):k+500]):
            peaks_S.append(Ng[k])
    # (ii) renversements de la direction de vitesse de forme (produit scalaire v_k·v_{k-1}<0)
    V=np.vstack([s1/H,s2/H,s3/H]).T  # dw/dN
    rev=0; last=None
    for k in range(1,ng):
        nv=np.linalg.norm(V[k])
        if nv>1e-8:
            if last is not None and float(V[k]@last)<0: rev+=1
            last=V[k]/nv
    # eps et gel
    eps_out=np.sqrt(w1[-1]**2+w2[-1]**2+w3[-1]**2)/np.sqrt(2)
    # N où Ω_σ tombe sous 0.5 (fin de domination cisaillement)
    idx=np.where(Omsig<0.5)[0]; N_halt=Ng[idx[0]] if len(idx) else Nmax
    return dict(peaks=len(peaks_S),peakN=peaks_S[:12],revers=rev,eps_out=float(eps_out),
                Omsig0=float(Omsig[0]),Omsig_end=float(Omsig[-1]),N_halt=float(N_halt),
                Smax=float(Smag.max()),Sbase=float(np.median(Smag)))

print("="*80)
print(" DIAGNOSTIC : rebonds dans l'intégration directe profonde (Radau, ng=20000)")
print("="*80)
print(f"{'1−Ω_σ':>8} {'N_halt':>7} {'pics|³S|':>9} {'révers.v':>9} {'eps_out':>9} {'Ω_σ_end':>10}  premiers N de rebond")
for Om in [0.9,0.99,0.999,0.9999,0.99999,0.999999]:
    d=analyze(Om)
    pN=" ".join(f"{x:.2f}" for x in d['peakN'])
    print(f"{1-Om:>8.0e} {d['N_halt']:>7.2f} {d['peaks']:>9d} {d['revers']:>9d} "
          f"{d['eps_out']:>9.4f} {d['Omsig_end']:>10.1e}  {pN}")

print("\nLecture :")
print(" - Si pics|³S| et révers.v CROISSENT avec la profondeur ⟹ la cascade EST capturée")
print("   par l'intégration directe ⟹ on peut faire l'ensemble en direct (Radau).")
print(" - Si ça reste ~1 ⟹ le germe de radiation halte avant la cascade ⟹ il FAUT l'oracle")
print("   BKL/Gauss (jump analytique à travers les rebonds, germe→0).")
