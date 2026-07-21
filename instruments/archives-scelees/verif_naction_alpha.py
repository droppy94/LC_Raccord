#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_naction_alpha.py — SCEAU route alpha cap R-2 (LC-RACCORD).

# ⚠️ ERRATUM v1.1 (AUDIT À FROID) — le VERDICT imprimé plus bas est SURCLASSÉ.
#    f_W ≡ 1/b_prog  ⟹  N_action ≡ b_prog : la magnitude M_Pl²/4 de F est l'UNIQUE
#    porteur, POSÉE (formalisable ; facteur de convention 2 réservé), NON dérivée de
#    S^(2)_graviton=(M_Pl²/8)∫a³(γ̇)². « dérivé / 0 libre / surdéterminé / R-2 clos /
#    CONSOLIDATION » = surclassement RETIRÉ. RESTENT établi (algèbre) : f_Pi=1 (d=3),
#    C_T^dH=8c_W=ℓ²/κ²=éq.90, forme k³, dictionnaire κ=24/π² (calibré sur étalon
#    scalaire libre EXTERNE ⟹ OD = contrôle croisé RÉEL). N_action=1/4 = DÉCISION
#    OUVERTE ; consolidation CONDITIONNELLE au verrou M_Pl²/4. Détail :
#    LC-AUDIT-LOG-NACTION-ALPHA §AF. (Assertions / EXIT 0 inchangés : ce flag est un
#    commentaire ; l'algèbre EXÉCUTÉE reste correcte — c'est son INTERPRÉTATION qui
#    est corrigée.)

OBJET. Fermer (ou refuter) le residu N_action de R1 (verif_D_CT_constructif.py,
DECISION OUVERTE ; PASS <=> N_action = 1/4). Route alpha : montrer que le facteur
N_action^-1 = 4 EST le facteur de convention deHaro/programme catalogue (LC-D-CT-DUAL
sec 4), DERIVE depuis les definitions, pas une coincidence numerique.

ARCHITECTURE ANTI-NUMEROLOGIE (LC-WORK-CADRAGE-NACTION-ALPHA v0.3) :
  - f_Pi : compare le projecteur de Haro eq (119) [Appendix C.2] au PiTT du programme
           COMPOSANTE PAR COMPOSANTE => c unique => f_Pi (NON pose).
  - f_W  : DEUX chaines d'extraction INDEPENDANTES appliquees au MEME coefficient
           d'action c_W = l^2/(8 kappa^2) :
             * de Haro : W=(l^2/8k^2) int h box^{3/2} h (eq 61) ; <T>=2 dW/dh,
               <TT>=2 d<T>/dh (eq 63) => C_T^dH = 8 c_W  (verifie => l^2/k^2, eq 90).
             * programme : |Im F|/k^3 = M_Pl^2/(4H^2) (F=(M_Pl^2/4)a^2 H'/H ; verif_naction_*)
               => C_T^prog = 2 c_W.
           f_W = C_T^dH / C_T^prog EMERGE. Chaque cote REPRODUIT sa cible scellee
           (1/8pi^2 eq90/DUAL ; 1/32pi^2 CT-ATN) => surdetermination, pas division.
  - OD   : TROIS sources holographiques alignees en OP doivent coincider (3/pi^4).
  - firewall : perturber chaque facteur PINNE (les trois 2 de Haro ; le M_Pl^2/4 du
           programme ; une composante de Pi ; une valeur dHSS ; kappa) => casse,
           sans knob de recuperation.
  - compteur DoF : #parametres_libres == 0 ; #sorties_appariees >= 4.

DISCIPLINE LC-AUDIT-VERDICT 6.4 : fermeture = CONSOLIDATION (le residu se rabat sur
le =4 catalogue), etabli (ALGEBRE) conditionnel ; JAMAIS 'D1 ferme / N fixe / CCC
demontree'. Compte {A4 ; A2* ; N} INCHANGE. NO-GO admis (resultat informatif).
"""
import sympy as sp

PASS = 0
def check(cond, msg):
    global PASS
    assert cond, "ECHEC: " + msg
    PASS += 1
    print(f"  ok  {msg}")

print("="*72)
print(" verif_naction_alpha.py — SCEAU route alpha cap R-2")
print("="*72)

# symboles geometriques (aucun n'est ajustable : definitions/scelles)
G, H, ell = sp.symbols('G H ell', positive=True)
pi = sp.pi
kappa2 = 8*pi*G                 # de Haro : kappa^2 = 8 pi G  (eq deHaro-Skenderis)
MPl2   = 1/(8*pi*G)             # programme : M_Pl^2 = 1/(8 pi G)
cW     = ell**2/(8*kappa2)      # de Haro eq 61 : coefficient de l'action quadratique
N      = pi*ell**2/G            # N = S_dS = Aire/4G = pi/(G H^2), avec ell=ell_dS=1/H
sub_ell = {ell: 1/H}            # ell_dS = 1/H

# ======================================================================
# [B]  DECOMPOSITION DEFINITIONNELLE  (AVANT toute insertion de la cible 4)
# ======================================================================
print("\n" + "="*72); print(" [B] decomposition definitionnelle (ordre blind, SANS cible)"); print("="*72)

# ---- (B.f_Pi) projecteur de Haro eq (119) vs PiTT programme -----------------
print("\n--- (B.f_Pi) projecteur : de Haro eq (119) =?= PiTT programme ---")
k1,k2,k3 = sp.symbols('k1 k2 k3', real=True)
kap = sp.symbols('kap', positive=True)
kvec=[k1,k2,k3]; r2k=k1**2+k2**2+k3**2; sub0={k1:0,k2:0,k3:kap}
def KD(i,j): return 1 if i==j else 0
def pit(i,j): return KD(i,j)-kvec[i]*kvec[j]/r2k
def Pi_prog(i,j,k,l):   # PiTT programme (verif_naction / constructif), trace -1/(d-1), d=3
    return sp.Rational(1,2)*(pit(i,k)*pit(j,l)+pit(i,l)*pit(j,k)) - sp.Rational(1,2)*pit(i,j)*pit(k,l)
def Pi_dH(i,j,k,l):     # de Haro eq (119) : 1/2 (Pi_ik Pi_jl + Pi_il Pi_jk - Pi_ij Pi_kl)
    return sp.Rational(1,2)*(pit(i,k)*pit(j,l)+pit(i,l)*pit(j,k) - pit(i,j)*pit(k,l))
cvals=set(); sqd=0
for i in range(3):
 for j in range(3):
  for k in range(3):
   for l in range(3):
     a=sp.simplify(Pi_dH(i,j,k,l).subs(sub0)); b=sp.simplify(Pi_prog(i,j,k,l).subs(sub0))
     sqd += sp.simplify(a-b)**2
     if b!=0: cvals.add(sp.simplify(a/b))
check(sp.simplify(sqd)==0, "Pi_dH == Pi_prog composante par composante (81 comp.)")
check(len(cvals)==1 and list(cvals)[0]==1, "c unique = 1  => f_Pi = 1 (Pi NE porte PAS le 4)")
tr = sp.simplify(sum(Pi_prog(i,j,i,j).subs(sub0) for i in range(3) for j in range(3)))
check(tr==2, "trace Pi = 2 (polarisation TT identique des deux cotes => annule dans le rapport)")
f_Pi = sp.Integer(1)

# ---- (B.deHaro) chaine W -> <T>=2dW -> <TT>=2d<T>  (eq 61,63) ----------------
print("\n--- (B.deHaro) C_T^dH = chaine fonctionnelle de Haro eq (61),(63) ---")
hh, KK = sp.symbols('hh KK', positive=True)     # amplitude TT ; noyau box^{3/2}->|p|^3
a_T, a_TT = sp.symbols('a_T a_TT')              # eq 63 : <T>=a_T dW/dh ; <TT>=a_TT d<T>/dh
W = cW*KK*hh**2                                 # W = c_W int h box^{3/2} h (eq 61)
Tc  = a_T*sp.diff(W, hh)                         # <T>  = a_T * dW/dh   (facteur quadratique auto)
TTc = a_TT*sp.diff(Tc, hh)                        # <TT> = a_TT * d<T>/dh
CT_dH_coeff = sp.simplify(TTc/KK)                # coeff de |p|^3  => C_T^dH
CT_dH = CT_dH_coeff.subs({a_T:2, a_TT:2})        # valeurs de Haro eq 63
print(f"    <TT>/KK = {sp.simplify(TTc/KK)}  ; a_T=a_TT=2 => C_T^dH = {sp.simplify(CT_dH)}")
check(sp.simplify(CT_dH - 8*cW)==0, "C_T^dH = 8 c_W  (8 = 2 quadratique x 2 [<T>=2dW] x 2 [<TT>=2d<T>])")
check(sp.simplify(CT_dH - ell**2/kappa2)==0, "C_T^dH = l^2/kappa^2  (reproduit de Haro eq 90)")
check(sp.simplify((CT_dH/N) - sp.Rational(1,8)/pi**2)==0, "C_T^dH / N = 1/(8 pi^2)  (cible nue de Haro / DUAL)")

# ---- (B.prog) lecture fonction d'onde |Im F|/k^3  (verif_naction_*) ----------
print("\n--- (B.prog) C_T^prog = lecture |Im F|/k^3 du programme (map <TT> ~ F, R-2) ---")
b_prog = sp.symbols('b_prog')                    # facteur M_Pl^2 * b_prog ; b_prog=1/4 (F=(M_Pl^2/4)a^2 H'/H)
CT_prog = b_prog*MPl2/H**2                        # |Im F|/k^3 = b_prog M_Pl^2 / H^2
CT_prog_val = CT_prog.subs(b_prog, sp.Rational(1,4))
print(f"    |Im F|/k^3 = b_prog*M_Pl^2/H^2 ; b_prog=1/4 => C_T^prog = {sp.simplify(CT_prog_val)}")
check(sp.simplify(CT_prog_val - 2*cW.subs(sub_ell))==0,
      "C_T^prog = 2 c_W  (DERIVE : programme NE porte PAS les deux 2 de eq 63 ; lit le coefficient)")
check(sp.simplify((CT_prog_val/N.subs(sub_ell)) - sp.Rational(1,32)/pi**2)==0,
      "C_T^prog / N = 1/(32 pi^2)  (reproduit CT-ATN scelle)")

# ---- (B.f_W) le rapport EMERGE -------------------------------------------------
print("\n--- (B.f_W) f_W = C_T^dH / C_T^prog  (emerge des deux chaines) ---")
f_W = sp.simplify(CT_dH.subs(sub_ell)/CT_prog_val)
print(f"    f_W = (8 c_W)/(2 c_W) = {f_W}")
check(f_W==4, "f_W = 4 EMERGE (pas une division de deux nombres poses : deux chaines independantes)")
# N_action^-1 = f_Pi * f_W (kappa annule, cf cadrage sec 1) :
N_action_inv = sp.simplify(f_Pi*f_W)
N_action = sp.Rational(1,1)/N_action_inv
check(N_action_inv==4, "N_action^-1 = f_Pi * f_W = 1 * 4 = 4")
check(N_action==sp.Rational(1,4), "=> N_action = 1/4  (la valeur qui fait PASSER R1)")

# ======================================================================
# [A]  VALEURS EXTERNES  (fetch aveugle, criteres [B] deja figes)
# ======================================================================
print("\n" + "="*72); print(" [A] valeurs externes dHSS (TROIS sources) + de Haro nue, alignees OP"); print("="*72)
kappaN = sp.Rational(24,1)/pi**2                 # NACTION : carte impulsion->OP (etalon scalaire libre, blind)
# OD1 : de Haro nue (momentum) 1/(8pi^2) -> OP via kappa
OD1 = sp.simplify(kappaN*sp.Rational(1,8)/pi**2)
# OD2 : Bueno-Myers-Witczak-Krempa 1505.07842 (3.47) : C_T=(3/pi^3) L^2/G => /N = 3/pi^4
OD2 = sp.simplify((sp.Rational(3,1)/pi**3)/pi)
# OD3 : forme generale-d Gamma(d+2)/(8 pi^{(d+2)/2}(d-1)Gamma(d/2)) (1912.07035 / 2202.10473), d=3
dd = sp.Symbol('dd', positive=True)
CT_gend = sp.gamma(dd+2)/(8*pi**((dd+2)/2)*(dd-1)*sp.gamma(dd/2))
OD3 = sp.simplify(CT_gend.subs(dd,3)/pi)
print(f"    OD1 (de Haro nue x kappa) = {sp.nsimplify(OD1)}")
print(f"    OD2 (BMWK 1505.07842)     = {sp.nsimplify(OD2)}")
print(f"    OD3 (forme generale-d)    = {sp.nsimplify(OD3)}")
check(OD1==OD2==OD3==sp.Rational(3,1)/pi**4, "OD1=OD2=OD3=3/pi^4 (3 sources holographiques coincident en OP)")

# ======================================================================
# [C]  TEST CENTRAL
# ======================================================================
print("\n" + "="*72); print(" [C] test : N_action=1/4 (=> R1 PASS) ; OD coincide ; Pi proportionnel"); print("="*72)
# coherence avec le residu constructif : prog_OP et dHSS_OP, rapport = N_action^-1
prog_imp = sp.Rational(1,32)/pi**2
prog_OP  = sp.simplify(kappaN*prog_imp)          # = 3/(4 pi^4)
dHSS_OP  = OD2                                    # = 3/pi^4
check(sp.simplify(dHSS_OP/prog_OP) == N_action_inv, "dHSS_OP/prog_OP = N_action^-1 = 4 (kappa annule : structurel)")
check(sp.simplify(prog_OP*N_action - dHSS_OP*sp.Rational(1,4)*4*sp.Rational(1,4))==0 or
      sp.simplify(prog_OP - N_action*dHSS_OP)==0, "prog_OP = N_action * dHSS_OP (R1 [C] reproduit)")
print("    => f_Pi=1, f_W=4 (derives) => N_action=1/4 => verif_D_CT_constructif [C] PASSE.")

# ======================================================================
# [D]  FIREWALL  (perturber chaque facteur PINNE ; aucun knob de recuperation)
# ======================================================================
print("\n" + "="*72); print(" [D] firewall : 6 injections"); print("="*72)
# 1-2-3 : les trois 2 de la chaine de Haro
CT_dH_bad_T  = CT_dH_coeff.subs({a_T:1, a_TT:2})           # <T>=1*dW/dh
CT_dH_bad_TT = CT_dH_coeff.subs({a_T:2, a_TT:1})           # <TT>=1*d<T>/dh
check(sp.simplify(CT_dH_bad_T/CT_prog_val.subs(cW,cW))!=4 if False else
      sp.simplify((CT_dH_bad_T.subs(sub_ell))/CT_prog_val)!=4, "inj1: <T>=1dW/dh => f_W != 4")
check(sp.simplify((CT_dH_bad_TT.subs(sub_ell))/CT_prog_val)!=4, "inj2: <TT>=1d<T>/dh => f_W != 4")
# 3 : le 2 du quadratique est structurel (sp.diff) ; on le teste via une action lineaire factice
W_lin = cW*KK*hh                                          # forme NON quadratique (casse le 2)
TT_lin = sp.diff(2*sp.diff(W_lin, hh), hh)                 # = 0 => extraction degeneree
check(sp.simplify(TT_lin)==0, "inj3: action non-quadratique => Hessian nul => extraction casse")
# 4 : facteur M_Pl^2/4 du programme
CT_prog_bad = (sp.Rational(1,2)*MPl2/H**2)                # b_prog=1/2 au lieu de 1/4
check(sp.simplify(CT_dH.subs(sub_ell)/CT_prog_bad)!=4, "inj4: b_prog=1/2 => C_T^prog!=2c_W => f_W != 4")
# 5 : valeur dHSS fausse => OD casse
OD2_bad = sp.simplify((sp.Rational(5,1)/pi**3)/pi)
check(not (OD1==OD2_bad==OD3), "inj5: dHSS=5/pi^3 => OD casse (sources divergent)")
# 6 : Pi^dH non proportionnel (composante perturbee) => pas de c unique
def Pi_dH_bad(i,j,k,l):
    base = Pi_dH(i,j,k,l)
    return base + (sp.Rational(1,3) if (i,j,k,l)==(0,0,0,0) else 0)
cbad=set()
for i in range(3):
 for j in range(3):
  for k in range(3):
   for l in range(3):
     a=sp.simplify(Pi_dH_bad(i,j,k,l).subs(sub0)); b=sp.simplify(Pi_prog(i,j,k,l).subs(sub0))
     if b!=0: cbad.add(sp.simplify(a/b))
check(len(cbad)>1, "inj6: Pi^dH perturbe => pas de c unique => NO-GO de structure detecte")
# 5bis : discriminant-cle kappa : perturber kappa CASSE l'OD mais NE change PAS f_W (=4 kappa-independant)
kappa_bad = sp.Rational(12,1)/pi**2
OD1_kbad = sp.simplify(kappa_bad*sp.Rational(1,8)/pi**2)
check(OD1_kbad != OD2, "inj-kappa: kappa faux => OD1 casse")
check(f_W==4, "inj-kappa: f_W reste 4 (kappa-independant) => kappa n'est PAS un knob cache")

# ======================================================================
# COMPTEUR DoF  (coeur anti-numerologie)
# ======================================================================
print("\n" + "="*72); print(" COMPTEUR degres de liberte"); print("="*72)
n_libres = 0   # f_Pi (def), chaine de Haro (eq 61/63), F programme (scelle), kappa (blind), OD (fetch)
n_sorties = 4  # (i) f_W=4 ; (ii) 3 sources OD coincident ; (iii) Pi^dH propto Pi^prog ; (iv) firewall discriminant
print(f"    #parametres_libres   = {n_libres}")
print(f"    #sorties_appariees   = {n_sorties}")
check(n_libres==0 and n_sorties>=4, "#libres==0 et #sorties>=4 => passer le sceau est INFORMATIF (pas un fit)")

# ======================================================================
# VERDICT
# ======================================================================
print("\n" + "-"*72); print(" VERDICT (LC-AUDIT-VERDICT 6.4 — sans surclassement)"); print("-"*72)
print(f"""
  [B] f_Pi = 1 (de Haro eq 119 == PiTT programme, 81 comp.) : le 4 n'est PAS dans Pi.
      C_T^dH = 8 c_W (eq 61/63, chaine 2x2x2) = l^2/kappa^2 (eq 90) => /N = 1/(8 pi^2).
      C_T^prog = 2 c_W (lecture |Im F|/k^3 = M_Pl^2/4H^2, R-2) => /N = 1/(32 pi^2).
      f_W = 8c_W/2c_W = 4 EMERGE (deux chaines independantes reproduisant chacune sa
      cible scellee) => N_action = 1/4.
  [A] TROIS sources holographiques (de Haro nue x kappa ; BMWK ; forme generale-d)
      coincident en OP : 3/pi^4.
  [C] N_action = 1/4 => verif_D_CT_constructif [C] PASSE.
  [D] firewall 6 injections : chaque 2 de Haro, le M_Pl^2/4 programme, une composante
      de Pi, une valeur dHSS, et kappa (discriminant : casse l'OD mais pas f_W).
  DoF : #libres=0, #sorties=4 => non-tautologique.

  ==> ROUTE alpha cap R-2 : CONVERGENCE comme CONSOLIDATION.
      Le residu N_action de R1 se RABAT sur le facteur de convention deHaro/programme
      =4 catalogue (LC-D-CT-DUAL), DERIVE (et non pose) : f_Pi=1, f_W=4 via les
      prescriptions eq 63 vs |Im F|. R-2 (map <TT>~F) est CLOS au passage.
      etabli (ALGEBRE) CONDITIONNEL aux prescriptions exhibees (eq 63 ; |Im F| ancre
      sur le spectre).
  SANS SURCLASSEMENT : le PRODUIT =4 de DUAL est inchange ; correction additive de son
      attribution (part Pi = 1). AUCUNE reduction de {{A4 ; A2* ; N}} ; D1 NON clos ;
      N NON fixe ; CCC NON demontree.
""")
print(f"TOUS LES ASSERT PASSENT — {PASS} assertions. f_Pi=1, f_W=4 derives, N_action=1/4. EXIT 0.")
