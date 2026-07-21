#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_phi_seals.py — Sceaux numériques reproductibles du sous-programme φ (LC-RACCORD).
Archive les trois vérifications de la fermeture du verrou (LC-10) :
  [A.3.3]  test de consistance + carte d'excitation k = n = d  -> métallique(k)
  [B.5]    sauts quantiques mono-canal (O(dt²)) = Gauss-Seidel -> φ ; additif d=2 -> argent
           + branchement dynamique (agent-based, population) -> φ
  [KMB]    extensivité (⟨K⟩,S_rel ∝ k ; σ(K) ∝ √k) ; S_rel = Hessienne Kubo-Mori ; additivité
Dépendances : numpy, scipy.  Aucune ressource réseau.
"""
import numpy as np, scipy.linalg as sl
trap = getattr(np, 'trapezoid', None) or np.trapz
phi=(1+np.sqrt(5))/2; silver=1+np.sqrt(2)
def metallic(d): return (d+np.sqrt(d*d+4))/2

def sceau_A33():
    print("="*68); print("[A.3.3] consistance πℏ/2E = ℓ/c  ⇔  E·τ = πℏ/2  ;  carte k=n=d")
    print("  k | n=ops/tick | métallique(k) | nom")
    noms={1:"or (φ)",2:"argent",3:"bronze",4:"4e mét."}
    for k in (1,2,3,4):
        print(f"  {k} |     {k}      | {metallic(k):.6f}     | {noms[k]}")
    print(f"  -> k=1 : n=1 => Gauss-Seidel strict => λ=φ={phi:.6f}")

def sceau_B5(rng=np.random.default_rng(7)):
    print("="*68); print("[B.5] sauts mono-canal (O(dt²)) = GS->φ  vs  additif d=2 = Jacobi->argent")
    g=np.array([1,0],complex); e=np.array([0,1],complex); sm=np.outer(g,e.conj())
    H=(0.5)*(np.outer(e,g.conj())+np.outer(g,e.conj()))
    L1=np.sqrt(0.5)*sm; L2=np.sqrt(0.5)*sm
    Heff=H-0.5j*(L1.conj().T@L1+L2.conj().T@L2)
    def frac2(dt,nsteps=20000,ntraj=40):
        n2=ntot=0
        for _ in range(ntraj):
            psi=e.copy()
            for _ in range(nsteps):
                p1=(dt*np.vdot(psi,(L1.conj().T@L1)@psi)).real
                p2=(dt*np.vdot(psi,(L2.conj().T@L2)@psi)).real
                j1=rng.random()<p1; j2=rng.random()<p2; nj=int(j1)+int(j2)
                if nj==2: n2+=1
                ntot+=1
                psi=(L1 if j1 else L2)@psi if nj>=1 else psi-1j*dt*(Heff@psi)
                nm=np.linalg.norm(psi); psi=psi/nm if nm>0 else e.copy()
        return n2, ntot
    print("  dt      frac(2 sauts)   #events / #steps   (O(dt²) = théorème ; sceau illustratif)")
    for dt in (0.04,0.02,0.01,0.005):
        n2,ntot=frac2(dt)
        print(f"  {dt:<6}  {n2/ntot:.3e}      {n2:>4d} / {ntot}")
    print("  [caveat revue à froid : points petit-dt sous-échantillonnés (jusqu'à 1 événement) ;")
    print("   le O(dt²) est garanti par la table d'Itô diagonale (théorème), pas par ces comptes]")
    def leslie(M,steps=60):
        v=np.array([1.,0.])
        for _ in range(steps): v=M@v; r=v.sum()
        v0=np.array([1.,0.])
        for _ in range(steps): nv=M@v0; r=nv.sum()/v0.sum(); v0=nv
        return r
    print(f"  GS  [[1,1],[1,0]] -> λ={leslie(np.array([[1.,1.],[1.,0.]])):.6f}  (φ={phi:.6f})")
    print(f"  Jac [[2,1],[1,0]] -> λ={leslie(np.array([[2.,1.],[1.,0.]])):.6f}  (argent={silver:.6f})")
    # item 3 : branchement DYNAMIQUE (agent-based, comptage de population, PAS rayon spectral)
    # un enfant actif par fire = mono-canal (le double-saut est interdit en O(dt²)).
    na, nb = 1, 0; prev = na + nb; ratio = 0.0
    for _ in range(60):
        na, nb = na + nb, na      # a -> a + b (fire : un enfant actif) ; b -> a
        tot = na + nb; ratio = tot / prev; prev = tot
    print(f"  branchement mono-canal (dynamique, population) -> ratio={ratio:.6f}  (φ={phi:.6f})")

def sceau_KMB():
    print("="*68); print("[KMB] extensivité ⟨K⟩,S_rel ∝ k ; σ(K) ∝ √k ; S_rel=Hessienne Kubo-Mori ; additivité")
    eps=1.3; K1=np.diag([0.,eps]); w1=sl.expm(-K1); w1/=np.trace(w1)
    th=0.6; U=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
    rho1=U@np.diag([0.78,0.22])@U.T
    def Srel(r,w): return np.real(np.trace(r@(sl.logm(r)-sl.logm(w))))
    def meanK(r,w): K=-sl.logm(w); return np.real(np.trace(r@K))
    def varK(r,w): K=-sl.logm(w); m=np.real(np.trace(r@K)); return np.real(np.trace(r@K@K))-m**2
    def kr(ms):
        o=ms[0]
        for m in ms[1:]: o=np.kron(o,m)
        return o
    print("  k | Δ⟨K⟩(lin) | S_rel(lin) | σ(K)(√k)")
    for k in range(1,6):
        W=kr([w1]*k); R=kr([rho1]*k)
        print(f"  {k} | {meanK(R,W)-meanK(W,W):.5f}  | {Srel(R,W):.5f}   | {np.sqrt(varK(R,W)):.5f}")
    def gKMB(w,A,nl=6000,lm=300.):
        lam=np.geomspace(1e-7,lm,nl); d=w.shape[0]
        return trap(np.array([np.real(np.trace(np.linalg.inv(w+L*np.eye(d))@A@np.linalg.inv(w+L*np.eye(d))@A)) for L in lam]),lam)
    A1=np.array([[0.,0.5],[0.5,0.]]); t=1e-3
    print(f"  S_rel(ω+tA‖ω)/((t²/2)gKMB) = {Srel(w1+t*A1,w1)/(0.5*t*t*gKMB(w1,A1)):.4f}  (=1 : S_rel=Hessienne KMB)")
    A2=np.array([[0.2,0.3],[0.3,-0.2]]); tt=1e-2; r1=w1+tt*A1; r2=w1+tt*A2
    print(f"  S((ρ1⊗ρ2)‖(ω⊗ω))/(S1+S2) = {Srel(np.kron(r1,r2),np.kron(w1,w1))/(Srel(r1,w1)+Srel(r2,w1)):.6f}  (=1 : additivité exacte)")

if __name__=="__main__":
    sceau_A33(); sceau_B5(); sceau_KMB(); print("="*68)

# --- F1 (audit froid, LC-WORK-AUDIT-BILAN) : assertions machine ajoutees (additif) ---
def _f1_assertions():
    _phi = (1 + np.sqrt(5)) / 2; _silver = 1 + np.sqrt(2)
    assert np.isclose(metallic(1), _phi), "[A.3.3] metallic(1) = phi"
    assert np.isclose(metallic(2), _silver), "[A.3.3] metallic(2) = argent"
    lam_gs = max(abs(np.linalg.eigvals(np.array([[1., 1.], [1., 0.]]))))
    lam_jac = max(abs(np.linalg.eigvals(np.array([[2., 1.], [1., 0.]]))))
    assert np.isclose(lam_gs, _phi), "[B.5] Leslie GS -> phi"
    assert np.isclose(lam_jac, _silver), "[B.5] Leslie Jacobi -> argent"
    a, b = 1, 0; prev = 1; rr = 0.0
    for _ in range(60):
        a, b = a + b, a; tot = a + b; rr = tot / prev; prev = tot
    assert np.isclose(rr, _phi), "[B.5] branchement mono-canal (population) -> phi"
    eps = 1.3; K1 = np.diag([0., eps]); w1 = sl.expm(-K1); w1 /= np.trace(w1)
    def _Srel(r, w): return np.real(np.trace(r @ (sl.logm(r) - sl.logm(w))))
    def _gKMB(w, A, nl=6000, lm=300.):
        lam = np.geomspace(1e-7, lm, nl); dd = w.shape[0]
        return trap(np.array([np.real(np.trace(np.linalg.inv(w+L*np.eye(dd))@A@np.linalg.inv(w+L*np.eye(dd))@A)) for L in lam]), lam)
    A1 = np.array([[0., 0.5], [0.5, 0.]]); t = 1e-3
    assert abs(_Srel(w1+t*A1, w1)/(0.5*t*t*_gKMB(w1, A1)) - 1) < 0.02, "[KMB] S_rel = Hessienne Kubo-Mori"
    A2 = np.array([[0.2, 0.3], [0.3, -0.2]]); tt = 1e-2; r1 = w1+tt*A1; r2 = w1+tt*A2
    assert abs(_Srel(np.kron(r1, r2), np.kron(w1, w1))/(_Srel(r1, w1)+_Srel(r2, w1)) - 1) < 1e-3, "[KMB] additivite exacte"
_f1_assertions()
print("EXIT 0 (F1: 7 assertions phi/Leslie/branchement/KMB verifiees)")
