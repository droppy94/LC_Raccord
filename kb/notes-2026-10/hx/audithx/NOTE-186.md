---
id: NOTE-BORD-EON-186-HX-EXECUTION
numero: 186
serie: I
branche: CCC + M (croisement S27 x Prop. 4, chantier HX)
reservation: 2026-10-15T16:25:17Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 186)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-185-ARMEMENT-HX.md, sha256 12dcfa433b5df18e, sceau NOTE-185-SCEAU.txt 2026-10-15T16:25:17Z"
script: "hx_check.py et hx_check_sortie.txt (empreintes au sceau de cloture)"
---

# HX, execution : le Higgs et les trois conditions sur la masse des fermions

## VERDICT : HX-V1. Prediction (informee) realisee.
Le secteur fermionique, et celui des bosons W, Z, n'ajoutent **aucune condition** a celle du Higgs. Les couplages de Yukawa et de masse de jauge sont conformement invariants ; le coefficient de masse de l'equation de Dirac rescalee est exactement y H_r = m_f/Omega. La condition de regularite formelle des fermions (Prop. 4(c), chantier ED) equivaut a la lissite du Higgs rescale, donc, par le theoreme 3.1 de Friedrich, a M2 = m_h^2 + 12 xi H^2 = 2H^2 = 2 lambda/3. Les conditions plus faibles (a) et (b) donnent un classement en M2.

## 1. HX-1 : classement (Higgs homogene pres du point symetrique, donnees generiques c1 != 0)
Equation indicielle (verifiee) : alpha(alpha - 3) + M2 = 0, h = c1 Omega^{3/2 - mu} + c2 Omega^{3/2 + mu}, mu = sqrt(9/4 - M2), M2 = (m_h^2 + 12 xi H^2)/H^2.

| M2 (unites H^2) | (a) champ de Dirac continu | (b) densite d'energie rescalee bornee | (c) coefficient lisse, critere formel |
|---|---|---|---|
| M2 <= 0 (dont le Higgs actuel, tachyonique au point symetrique, et M2 = 0 : masse constante) | non | non | non |
| 0 < M2 < 2 | **oui** | non | non |
| M2 = 2 (Friedrich ; ou couplage conforme xi = 1/6, m_h = 0) | oui | oui | **oui** (alpha = 1, 2) |
| 2 < M2 < 9/4 | oui | oui | non (exposants non entiers) |
| M2 = 9/4 | oui | oui | non (racine double, logarithme) |
| M2 > 9/4 (mu complexe) | oui | oui | non (oscillation Omega^{1/2 -+ i nu}) |

Seuils : (a) ssi M2 > 0 ; (b) ssi M2 >= 2 ; (c) ssi M2 = 2. **Concorde avec S27 A.1** (« borne ssi m_h^2 >= 2H^2 », « lisse ssi = 2H^2 ») et le **complete** : S27 jugeait m_f/Omega borne, qui est exactement (b) ; (a) ajoute une zone 0 < M2 < 2 ou le champ de Dirac rescale converge alors que sa densite d'energie rescalee diverge. Avec un couplage non minimal, seule la combinaison M2 compte (sur dS, R = 12H^2).

## 2. HX-2 : doublet complet, sans homogeneite
Poids conformes (ghat = Omega^-2 g, H = Omega H_r, psi = Omega^{3/2} psi_r) : sqrt(-ghat) y H psibar psi a un poids **0** ; le terme de Yukawa y psibar_L H psi_R + h.c. est donc conformement invariant, et l'equation de Dirac rescalee porte le coefficient y H_r (sans homogeneite ni hypothese sur la direction du doublet). La regularite formelle du secteur fermionique equivaut a la lissite de H_r. Par contraste, sqrt(-ghat) m_h^2 abs(H)^2 a un poids -2 : c'est le terme Omega^-2 m^2 abs(H_r)^2 de Friedrich, compense par le terme de courbure R/6 exactement a m_h^2 = 2 lambda/3. Le potentiel du doublet ne contient que abs(H)^2 et abs(H)^4 (pas de terme cubique) : la condition annexe de Friedrich (mu = 0 dans (3.3)) est satisfaite ; l'application du theoreme 3.1, enonce pour un scalaire reel, aux quatre composantes reelles d'un potentiel O(4)-invariant est une extension, plausible, non verifiee ici (FW-3).

## 3. HX-3 : bosons W, Z
sqrt(-ghat) ghat^{mn} abs(H)^2 A_m A_n a un poids **0** (A de poids 0) : le terme de masse de jauge est conformement invariant ; la masse rescalee des W, Z est g abs(H_r), reguliere ssi H_r l'est. Meme reduction que pour les fermions.

## 4. HX-4 : bilan
- Pour tout le secteur dont la masse vient du Higgs (leptons charges, quarks, W, Z ; neutrinos si operateur de Weinberg, masse ~ v^2, donc ~ Omega^2), la condition de bord se reduit a **une seule condition sur le Higgs** : M2 = 2 lambda/3 pour la regularite formelle (c), M2 >= 2H^2 pour (b), M2 > 0 pour (a).
- Hors reduction, inchange depuis S27 : baryons (Lambda_QCD, C-M2), neutrinos de Majorana non issus de H, matiere noire (C-M4).
- La tension Q-M3 (electron sans masse, anomalie de trace QED) reste ouverte et hors chantier.

## 5. Limites
Classement HX-1 sur solutions homogenes, donnees generiques (c1 != 0 ; des donnees fines c1 = 0 changent l'exposant dominant) ; quartique et couplages de jauge sous-dominants pres du point symetrique (S27 D.1, non re-demontre) ; extension du theoreme 3.1 au doublet non verifiee ; aucun mecanisme qui amenerait le Higgs a M2 = 2 n'est propose (le cout, S27 A.2, hors chantier).

## 6. Propositions (non entees ; audit d'abord)
- **S27-02 v2** : greffe G-M1 sur §A.1 : tableau du §1, invariance conforme des couplages de Yukawa et de masse de jauge, reduction exacte du secteur fermionique et W, Z a la condition de Higgs ; zone 0 < M2 < 2 (champ continu, energie divergente).

## 7. Non-surclassement
Rien de grave. CCC + M hypothese ouverte (condition unique sur le Higgs confirmee, plus precise). p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
