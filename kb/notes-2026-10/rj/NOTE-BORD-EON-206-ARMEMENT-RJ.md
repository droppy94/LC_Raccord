---
id: NOTE-BORD-EON-206-ARMEMENT-RJ
numero: 206
serie: I
branche: Chantier D (chantier RJ : regularisation par jauge)
reservation: 2026-10-16T15:17:31Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 206)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
nature: "GEL R-7 avant tout calcul et toute lecture au-dela de ce qui est declare au §0"
decision: "operateur (Thierry), 2026-10-16 : chantier RJ « avant la v2.5 » (NOTE-205 §3)"
amont: "NOTE-204 §5 et D6 ; NOTE-202 v2 (S19) ; NOTE-199 D4 (« seulement si » pour les inconnues de Friedrich) ; FW3 (NOTE-191 v2), ED (NOTE-181), article v2.4 Prop. 2, 3, 5"
---

# Gel RJ : un choix d'inconnues ou de jauge rend-il regulier le systeme Einstein-Dirac a scri ?

## 0. Etat de connaissance declare avant le gel
- Friedrich, arXiv:1601.04506, lu [resume, 1, 3, 8] lors de la contre-lecture de NOTE-204 : pour Einstein-lambda-poussiere, les equations conformes portent des facteurs Omega^{-1} (equation du flot, equation du Weyl rescale) ; une jauge fondee sur des geodesiques conformes adaptees au flot fournit une « relation regularisante » qui rend le systeme regulier ; scri C-infini pour un ensemble ouvert de donnees ; rho = Omega^{-3} rho-hat regulier. Les sections 4, 5 et 7 (mecanisme detaille) **ne sont pas lues**.
- Cote Dirac (acquis audites) : le spineur rescale a une phase exp(+-i(m/H) ln Omega) sans limite (Prop. 1) ; la phase relative entre composantes beta = +-1 est invariante de jauge U(1) (Prop. 2(b)) ; la densite d'energie rescalee a un pole m/Omega de signe fixe (Prop. 3), comme une poussiere ; dans les inconnues de Friedrich, le systeme couple n'est formellement regulier pour aucune masse de Dirac constante non nulle (ED, FW3).

## 1. Questions figees
- **RJ-1 (mecanisme).** Lire Friedrich 2016 §§ 3 a 5 et 7 : quels termes en Omega^{-1}, quelle jauge, quelle relation regularisante, quelles hypotheses sur la matiere (geodesicite du flot, T de la forme rho U U, signe de rho) sont utilisees.
- **RJ-2 (transposition au tenseur de Dirac).** Ecrire le tenseur d'energie-impulsion rescale d'une solution de Dirac massive en de Sitter (puis en FLRW tendant vers de Sitter) au voisinage de scri : partie de type poussiere (rho U U, pole 1/Omega) et reste. Quelles composantes du reste portent des facteurs oscillants exp(+-2i(m/H) ln Omega) (interferences particule-antiparticule, Zitterbewegung), a quel ordre en Omega ?
- **RJ-3 (test formel).** Dans les equations conformes de Friedrich avec ce tenseur et une jauge du type RJ-1 (flot = courant de Dirac normalise, ou flot de la partie poussiere), les seconds membres sont-ils formellement reguliers (critere des chantiers ED et FW3 : ni Omega^{-k} ni ln Omega, et ajout ici : ni phase exp(i c ln Omega) non reguliere) ? Calcul symbolique, script scelle.
- **RJ-4 (portee).** Consequence pour l'enonce « RG-4 refutee a titre provisoire » et pour la Remarque Friedrich et la Prop. 5 de l'article.

## 2. Espace de verdicts
- **RJ-V0** : non concluant (mecanisme de Friedrich non transposable a ce niveau de calcul, ou calcul inacheve).
- **RJ-V1** : regularisation complete au sens formel pour une solution de Dirac generique (partie poussiere et reste) ; le statut de RG-4 doit etre revise (la singularite formelle d'ED et FW3 serait un artefact des inconnues).
- **RJ-V2** : la partie poussiere se regularise comme chez Friedrich, mais les termes d'interference particule-antiparticule laissent dans les seconds membres des facteurs sans limite (phases en ln Omega) ou des poles ; regularisation seulement pour les solutions purement particule (ou purement antiparticule) a la limite ; RG-4 maintenue sous une forme invariante de jauge, avec une classe exceptionnelle explicite.
- **RJ-V3** : le mecanisme ne s'applique pas meme a la partie poussiere (par exemple parce que le courant de Dirac n'est pas geodesique, ou parce que la pression oscillante change la structure) ; la reserve de NOTE-204 §5 est levee dans le sens de RG-4.

## 3. Prediction (informee, precedent ix)
**RJ-V2.** Raison : la densite d'energie a deja la forme poussiere (Prop. 3) et le courant de Dirac est asymptotiquement au repos dans le repere de Hubble (Ibison, S17), ce qui rend plausible la transposition pour la partie poussiere ; mais la Prop. 2(b) montre qu'une phase relative invariante de jauge survit, et elle doit apparaitre dans les composantes du tenseur qui melangent les deux sous-espaces de beta. Prediction faible sur la seconde moitie : ces termes peuvent etre d'ordre assez eleve en Omega pour etre inoffensifs, ce qui donnerait RJ-V1.

## 4. Firewall
- FW-1 : RJ-1 se fait par lecture, niveau declare par section ; aucune affirmation sur le mecanisme de Friedrich avant la lecture des §§ 4, 5, 7.
- FW-2 : le script de RJ-3 est ecrit et scelle avec l'execution ; les equations de Friedrich recopiees sont verifiees par script avant usage (precedent xiv) ; les positions d'indices (n_a ou n^a, U_a ou U^a) sont fixees par ecrit (precedent xv).
- FW-3 : critere de regularite elargi annonce **avant** calcul : un second membre est regulier s'il est, en Omega, une serie entiere a coefficients reguliers ; une phase exp(i c ln Omega), c reel non nul, multipliant un coefficient non nul, est une irregularite (pas de limite), au meme titre que ln Omega.
- FW-4 : le calcul porte d'abord sur de Sitter exact avec un champ de Dirac test (tenseur de Dirac injecte dans les equations conformes, sans retroaction au-dela de l'ordre lineaire en T), puis, si RJ-V1 ou RJ-V2, sur le couplage formel complet.
- FW-5 : audit froid (deux agents isoles) avant toute entee ; la redaction de la v2.5 attend l'acte RJ.

## 5. Non-surclassement
Rien de grave. RG-4 refutee a titre provisoire, reserve de NOTE-204 §5 ouverte ; noyau {A4 ; A2★ ; N} inchange.
