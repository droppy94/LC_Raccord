---
id: NOTE-BORD-EON-185-ARMEMENT-HX
numero: 185
serie: I
branche: CCC + M (croisement S27 x Prop. 4 ; chantier HX)
reservation: 2026-10-15 (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 185)
date: 2026-10-15
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant calcul : conditions sur le secteur de Higgs pour que les masses de Yukawa satisfassent la Prop. 4 (a), (b), (c) de l'article et le critere formel de Friedrich (chantier ED), y compris m_h^2 != 2 lambda/3 et le doublet complet"
decision: "operateur (Thierry), 2026-10-15 18:24 heure de Paris : « accord donne pour armer le croisement entre S27 et la Prop. 4 »"
---

# Gel HX : le Higgs pres du point symetrique et les trois conditions sur la masse des fermions

## 0. Acquis repris (non rejoues)
- S27-02 A.1 : pres du point symetrique, en dS, h ~ Omega^{3/2 - mu}, mu = sqrt(9/4 - m_h^2/H^2), m_f = y h ; m_f/Omega borne ssi m_h^2 >= 2H^2 ; tout lisse ssi m_h^2 = 2H^2 (= 2 lambda/3).
- Article v2.3, Prop. 4 : (a) continuite du champ de Dirac ssi int m dt fini ; (b) densite d'energie rescalee bornee ssi m a borne ; (c) coefficient lisse ssi m = Omega mu lisse ; ordre strict.
- ED (NOTE-181/183/184) : le systeme couple Einstein-Dirac est formellement regulier ssi (c), a inconnues fixees.

## 1. Questions figees
- **HX-1 (classement)** : pour le Higgs homogene minimalement couple (eventuellement non minimal, xi R |H|^2), avec les deux branches h = c1 Omega^{3/2 - mu} + c2 Omega^{3/2 + mu}, donnees generiques (c1 != 0), pour quelles valeurs de m_h^2/H^2 (reelles, y compris negatives, et mu complexe) la masse m_f = y h satisfait-elle (a), (b), (c) ? Comparaison avec le classement de S27 (borne / lisse).
- **HX-2 (doublet, sans homogeneite)** : le couplage de Yukawa y psibar_L H psi_R + h.c. est-il conformement invariant avec les poids standard (H poids 1, psi poids 3/2) ? En deduire que le coefficient de masse de l'equation de Dirac rescalee est y H_rescale, et que la regularite formelle du secteur fermionique equivaut a la regularite (lissite) du Higgs rescale, independamment de l'homogeneite.
- **HX-3 (jauge)** : meme question pour les masses des bosons W, Z (terme g^2 abs(H)^2 A^2).
- **HX-4 (bilan)** : le secteur fermionique (et de jauge) ajoute-t-il une condition a celle du Higgs ? Quelles masses du Modele standard restent hors de cette reduction (C-M2 baryons, Lambda_QCD ; neutrinos selon leur origine ; matiere noire) ?

## 2. Espace de verdicts
- **HX-V0** : non concluant.
- **HX-V1** : reduction exacte : (c) et le critere formel pour les fermions et W, Z equivalent a la lissite du Higgs rescale, donc (Friedrich, theoreme 3.1, potentiel sans terme cubique) a m_h^2 = 2 lambda/3 ; (a) et (b) donnent des conditions plus faibles, classees en m_h^2 ; aucune condition supplementaire venant des fermions.
- **HX-V2** : reduction partielle : une condition supplementaire apparait (par exemple via la partie non homogene, le doublet, la jauge, ou le terme quartique).
- **HX-V3** : incompatibilite : la condition de Higgs ne peut etre satisfaite sans violer une autre condition du secteur (contredirait S27 C-M1).

## 3. Prediction (informee, precedent ix)
**HX-V1.** Classement attendu (c1 != 0) : (a) ssi m_h^2 > 0 ; (b) ssi m_h^2 >= 2H^2 ; (c) et critere formel ssi m_h^2 = 2H^2 ; avec xi : remplacer m_h^2 par m_h^2 + 12 xi H^2 (sur dS, R = 12H^2). Yukawa et terme de masse de jauge conformement invariants ; secteur fermionique et W, Z sans condition supplementaire. Hors reduction : Lambda_QCD (C-M2), neutrinos de Majorana non issus de H, matiere noire (inchanges depuis S27).

## 4. Firewall
- FW-1 : critere formel (precedent xii) pour HX-2 et HX-3 ; le classement HX-1 sur solutions homogenes est un classement de solutions, nomme comme tel.
- FW-2 : verification symbolique des exposants et de l'invariance conforme (script scelle avec sortie).
- FW-3 : la condition de Higgs de Friedrich est citee (theoreme 3.1), pas re-demontree ; le doublet complexe a quatre composantes reelles, chacune scalaire : le theoreme s'applique composante par composante sous reserve que le potentiel n'ait pas de terme cubique (verifie : |H|^2 et |H|^4).
- FW-4 : ne pas rouvrir le cout (87 ordres de grandeur, S27 A.2) ; hors chantier.
- FW-5 : audit froid aveugle avant toute greffe.

## 5. Non-surclassement
Rien de grave. CCC + M reste une hypothese ouverte ; p_Q non fixe, N non chiffre, noyau {A4 ; A2* ; N} inchange.
