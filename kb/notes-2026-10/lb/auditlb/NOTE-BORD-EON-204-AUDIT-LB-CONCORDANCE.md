---
id: NOTE-BORD-EON-204-AUDIT-LB-CONCORDANCE
numero: 204
serie: I
branche: Chantier D (audit LB)
reservation: 2026-10-16T15:02:11Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 204)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
gel: "NOTE-BORD-EON-203-ARMEMENT-AUDIT-LB.md sha256 3eae1e78da1647e4 (sceau NOTE-202-203-SCEAU.txt, 2026-10-16T15:03:08Z, pose avant lancement)"
rapports: "RAPPORT-AL1.md sha256 47e2b6d5112b1b3a ; RAPPORT-AL2.md sha256 3b40320fd67787ce ; work_al1/checks.py ; work_al2/journal_requetes.txt"
---

# Concordance de l'audit LB

## 0. Deroulement
Deux auditeurs isoles (Opus), sans interruption. AL-1 : cecite stricte (n'a pas vu NOTE-202), 9 requetes documentees, verifications numeriques (borne de la Prop. 1, etat de Slater par Jordan-Wigner sur 4 modes). AL-2 : adverse, 9 requetes documentees. Apres reception, contre-lecture par l'executant des quatre sources nouvelles qui portent les constats (niveau declare au §2).

## 1. Criteres
| Critere | AL-1 | AL-2 | Concordance |
|---|---|---|---|
| K-1 Lemme 3.1 de 1902.09144 et Prop. 1 | meme contenu analytique ; coquille de la borne (3.10) : lire exp(.) - 1 ; borne de l'article legerement meilleure | idem, independamment ; « \|\|E\|\| controle par e^{-t} » est une lecture corrigee, pas un enonce de S3 ; ajouter Ibison et Finster-Reintjes | **oui**, avec correction |
| K-2 Hadamard, carte plate (1902.09144) | Hadamard etabli sur de Sitter global (Prop. 4.5) ; ce qui reste ouvert est le statut de l'**etat FP** en carte plate ; S3 §3.3 affirme, via 1009.5179, que Bunch-Davies selectionne les frequences negatives a scri moins | meme lecture : **la note a confondu** l'etat FP et l'etat de Bunch-Davies restreint | **oui : attribution de la note infirmee** (D2) |
| K-3 facteur de paires (2610.00410) | standard, non revendique | exact ; ajouter Kanno-Sasaki-Tanaka (non lu) | **oui** |
| K-4 axiome 1 (0904.0612) | exact ; operateur D-tilde^can ; verifie pour des etats **Hadamard** | idem | **oui**, avec precision |
| K-5 etat de Slater | oui : quasi-libre pur de projecteur P + \|f><f\|, difference de rang un ; preuve et verification numerique | correct ; paquet d'ondes et non mode de Fourier ; sans purete, rang un mais plus quasi-libre ; **positivite seulement pour l'energie integree** (Plancherel), pas point par point | **oui**, avec deux reserves nouvelles (D4) |
| K-6 nouveaute Prop. 2 a 4 | Prop. 2 non trouvee ; **Bachelot 2003.03356** : analogue scalaire de la Prop. 4 ; **Friedrich 1601.04506** : poussiere avec pole 1/Omega de la densite rescalee et scri C-infini | Prop. 2 non trouvee ; **Bachelot** (meme constat) ; **Ibison 1105.3767** : noyau classique de la Prop. 3 (energie de repos en repere conforme croissant comme a(t) m) et oscillation infinie de phase au bord | **oui : verdict LB-3 (LB-V1) infirme** (D1) |
| K-7 titres et niveaux | (non demande) | S6 trop fort (Hadamard a ordre adiabatique **infini** seulement) ; S16 un seul auteur ; S11 auteur Pham Truong Xuan ; niveau de S12 contradictoire ; contradiction interne LB-1 / LB-2 | **retenu** (D3, D5) |

## 2. Contre-lecture des sources nouvelles (executant, apres les rapports)
- Ibison, « The Dirac Field at the Future Conformal Singularity », arXiv:1105.3767 (chapitre InTech « Cosmology », 2011) [sections 1, 5.2, 6.4, 8.3, 10] : eq. (33) E = a(t) m integrale de psi-dagger gamma0 psi, non constante ; introduction : en repere conforme, la densite d'energie croit comme l'echelle (« increase in the rest mass ») ; §8.3 : « the phase oscillates rapidly, infinitely quickly so at the boundary » ; seule une paire de composantes survit au bord (a l'ordre dominant). **Confirme.**
- Friedrich, « Sharp asymptotics for Einstein-lambda-dust flows », arXiv:1601.04506 (Comm. Math. Phys. 350 (2017) 803, reference lue dans la bibliographie de Bachelot) [resume, 1, 3, 8] : rho = Omega^{-3} rho-hat regulier, Thm 1.1 : ensemble ouvert de donnees a scri C-infini ; les equations conformes ont des facteurs Omega^{-1} (equation du flot, equation du Weyl rescale) **rendus reguliers par un choix de jauge** (geodesiques conformes adaptees au flot). Dans la convention de l'article (T-hat = Omega^{-2} T), la densite rescalee vaut rho/Omega : **pole simple compatible avec un scri lisse**. **Confirme.**
- Bachelot, « Propagation of Massive Scalar Fields in Pre-Big Bang Cosmologies », arXiv:2003.03356 [resume, I, III, IV.1-IV.4] : champ scalaire conformement couple, masse dependant du temps, cadre CCC explicite ; (III.26) en de Sitter : integrale de m^2 e^{Ht} dt finie (decroissance exponentielle) ; (IV.4), condition faible : **integrale de m^2 dt finie**, avec conditions de transmission a un parametre (Riccati). **Confirme** ; la reduction de AL-2 « a verifier » est ecrite telle quelle en (IV.4).
- Dappiaggi, Hack, Pinamonti, arXiv:1009.5179 [resume, 4.2] : Thm 4.2 : etats de Dirac construits a scri moins, quasi-libres, de forme Hadamard, pour beta fini (KMS) ; l'etat fondamental (beta infini) n'est que « presume » limite (remarque apres Prop. 4.2). Les deux auditeurs divergent sur ce point (AL-1 : resolu ; AL-2 : reserve beta infini) ; la lecture de l'executant donne raison a AL-2.

## 3. Corrections
- **D1 (nouveaute)** : LB-3 passe de LB-V1 a **LB-V2**. Prop. 2 : non trouvee. Prop. 3 : noyau classique chez Ibison (2011) ; la limite exacte, l'invariance de jauge, la version quantique et le critere CCC ne s'y trouvent pas. Prop. 4 : analogue scalaire en CCC chez Bachelot (2020), conditions integrales sur la masse ; la version Dirac (integrale de m dt finie, decroissance en 1/a, hierarchie (c) => (b) => (a)) non trouvee.
- **D2 (lecture de S3)** : ce que S3 laisse ouvert est le statut de l'etat FP, pas l'identification de Bunch-Davies. Statut corrige : la restriction de Bunch-Davies global a la carte plate est Hadamard (argument local, valide par AL-1 et AL-2) ; son identification avec le vide de modes de carte plate est affirmee par S3 via S5 ; S5 prouve le caractere Hadamard pour beta fini, l'etat fondamental est presume.
- **D3 (LB-2)** : contradiction interne. LB-2 passe a **LB-V2** : l'asymptotique du Dirac massif a scri de de Sitter est connue (S3 Lemme 3.1, Ibison, Loran hep-th/0404135 [titre, via AL-2], Roy 2609.34073 [via AL-1]) ; le traitement par equations conformes avec matiere de Dirac (Remarque de l'article) reste non trouve.
- **D4 (argument quantique)** : paquet d'ondes normalise (pas un mode) ; etats Hadamard exiges (pas seulement quasi-libres) ; operateur D-tilde^can ; **positivite du pole pour l'energie integree sur une tranche comobile**, pas pour la densite point par point ; S6 : ordre adiabatique infini.
- **D5 (fiches)** : S6 titre « Spacetimes », ordre infini ; S11 auteur Pham Truong Xuan ; S16 auteur unique Cotaescu ; S12 niveau [sections 1, 3] ; S15 renvoi de section a verifier ; publication de 1311.0700 : Ann. Henri Poincare 16 (2015) 2215.
- **D6 (Prop. 5(b) de l'article, nouveau et de fond)** : Friedrich 1601.04506 montre, pour la poussiere couplee a Einstein-lambda, qu'un pole 1/Omega de la densite d'energie rescalee (convention de l'article) coexiste avec un scri C-infini, et que des facteurs Omega^{-1} des equations conformes peuvent etre retires par un choix de jauge. Aucun enonce de l'article n'est contredit (5(b) est conditionnel et dit « not established here »), mais la motivation de 5(b) est affaiblie et la v2.5 doit le dire.

## 4. Verdict
**AU-V3 (partiel).** Deux criteres sont infirmes et confirmes a la concordance par les deux auditeurs independamment : K-6 (travail anterieur : analogue scalaire de la Prop. 4, Bachelot ; noyau classique de la Prop. 3, Ibison) et K-2 (attribution fausse de la note sur S3). Aucun enonce mathematique de l'article n'est contredit. **Prediction AU-V2 non realisee.** Conformement au gel : entee de NOTE-202 v1 suspendue ; NOTE-202 v2 integre D1 a D6.

## 5. Portee pour le programme (hors article)
D6 touche le critere de regularite formelle des chantiers ED, HX, FW3, AF (pas de Omega^{-k} au second membre dans les inconnues de Friedrich). Le cas de la poussiere montre que ce critere depend du choix des inconnues et de la jauge (reserve deja notee en NOTE-199 D4 : « seulement si » pour les inconnues de Friedrich). Le statut « RG-4 refutee a titre provisoire (sous le critere retenu) » reste exact mais la reserve doit etre renforcee : une regularisation par jauge, du type de celle de Friedrich pour la poussiere, n'a pas ete cherchee pour Dirac. A ouvrir comme piste (proposition : chantier RJ, regularisation par jauge), sous gel propre.

## 6. Non-surclassement
Audit par IA : ne vaut pas lecture humaine. RG-4 refutee a titre provisoire, reserve renforcee (§5) ; noyau {A4 ; A2★ ; N} inchange.
