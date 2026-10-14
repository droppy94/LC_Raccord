---
id: NOTE-BORD-EON-120-AUDIT-IR-m-CONCORDANCE
numero: 120
serie: I
branche: Q-M3 suite (audit IR-m)
reservation: 2026-10-11T16:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 120)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-119-ARMEMENT-AUDIT-IR-m (sha256 220717a01d612de64e01429d825f3ea068c2a0451abb9380c004391d6b5daa3f, sceau 2026-10-11T16:58:02Z)
rapport: RAPPORT-IR-m-AUDIT-AVEUGLE.md
depend: [NOTE-BORD-EON-119-ARMEMENT-AUDIT-IR-m, NOTE-BORD-EON-111-IR-i-EXECUTION, NOTE-BORD-EON-116-IR-l-EXECUTION, NOTE-BORD-EON-118-IR-k-EXECUTION]
verdict: "AU-V2 (blocs I, L, K) ; tous les resultats porteurs confirmes, dont trois retrouves en cecite stricte ; corrections mineures ; qualifications de K-D completees"
prediction_realisee: "oui (AU-V2), avec des corrections plus nombreuses que prevu (§5)"
rouvre_si:
  - "retroaction metrique : terme gravitationnel de l'anomalie en φC² sur fond perturbe (§3, K-D2)"
  - "facteur de forme non local de la partie invariante de Weyl singulier sur les modes a impulsion nulle (§3, K-D3)"
---

# NOTE-120 : audit froid aveugle conjoint de NOTE-111, NOTE-116, NOTE-118. Verdict **AU-V2**

## 0. Resume
Les trois maillons qui portent le renforcement de M-V3 tiennent. Les six resultats porteurs sont confirmes :
- **I-A** : la loi locale R_ln(x) = (3βκ/e²)Q_tf(x) a l'ordre s⁰.
- **L-A** : la formule exacte de Q_k.
- **L-C** : seule la composante E ℓ = 2 compte (codimension 5).
- **K-B** : T^(b) sans log et sans φ.
- **K-C** : la loi est retrouvee avec X^M seul.

Trois d'entre eux ont ete **retrouves en cecite stricte**, sans etre donnes : la loi locale et ses coefficients (M-a1), la formule de Q_k et la codimension 5 (M-a2), les tenseurs T^(b) et la loi par X^M seul (M-a3). M-b les reproduit tous par d'autres chaines et en etend deux : la loi s'ecrit hors diagonale, et l'absence de log dans T^(b) vaut pour des familles non diagonales.

L'audit releve aussi des defauts reels mais localises :
- une prediction numerique fausse et une explication sans objet dans NOTE-111 ;
- un test de script aveugle (ir_i.py) ;
- une enumeration tautologique dans NOTE-116 ;
- dans NOTE-118, deux hypotheses de K-D a ajouter, dont le fond fixe, et une qualification a retirer.

Aucun ne touche un resultat porteur.

## 1. Concordance par resultat

| Resultat | M-a (aveugle) | M-b | Etat |
|---|---|---|---|
| I-A loi locale a s⁰ | M-a1 : identique, composante par composante, NS = 4 et 5 | confirme, hors diagonale (Q_yz) | **concordant, renforce** |
| I-A gradients en s ln s | M-a1 : oui, coefficients explicites | oui | concordant |
| I-A fermeture libre hors des logs | M-a1 : vrai a s⁰ et s¹ (12 constantes) | test du script aveugle ; vrai a s⁰ ; X^R sans log a tous ordres sous H-loc (preuve structurelle) | **concordant a s⁰ ; enonce a restreindre et a fonder autrement** |
| I-A' defaut d'etiquette | (non pose) | confirme (drapeau corrige True) | concordant |
| I-B boule vide, 1/5, 4/5 | M-a1 : identique ; formule exacte de a(r) | identique | concordant |
| I-B integrales, ecart 0,4 % | M-a1 : coquille = 16/(75w³) a 2e-6 pres | prediction 21,36 fausse (quadrature) ; vraie 21,4466 ; ecart 2e-5 | **discordance avec NOTE-111 sur un point non porteur** |
| I-C compensation sans H-loc | M-a1 : oui | oui (contre-exemple explicite) | concordant |
| L-A formule de Q_k | M-a2 : identique | identique (3e-15) | **concordant** |
| L-B lineaire seule | M-a2 : oui | oui | concordant |
| L-C E ℓ = 2, codimension 5 | M-a2 : oui (rang 5) | oui | **concordant** |
| L-C trois classes d'exception | M-a2 : ajoute motifs B purs et equilibre E1/M1 ; helicite non necessaire | enumeration tautologique ; deux sources physiques hors helicite et isotropie | **a reformuler** |
| L-C interference | M-a2 : bande lisse rapide, bords francs O(1/(t₀Δk)) | asymptotique (\|t₀\| ≫ duree), globale | concordant, precise |
| L-D valeurs | M-a2 : identiques | identiques (1e-15) | concordant |
| K-A divergence de X^M sans log | M-a3 : identique, I² quelconque | identique | concordant |
| K-B T^(b) sans log ni φ | M-a3 : identique ; φ disparait par covariance de Weyl | identique ; familles non diagonales en (s, x, y) | **concordant, generalise** |
| K-C loi par X^M seul | M-a3 : exacte, 9 composantes | exacte, deux polarisations | **concordant** |
| K-D H-loc inutile, sous qualifications | M-a3 : valide ; hypothese H3 (regularite de W sur modes a impulsion nulle) | valide sous hypotheses (1) lissite du tenseur plat de W, (2) fond fixe ; « famille diagonale » inutile | **concordant, qualifications a remplacer** |

## 2. Corrections a porter (non entees)
**NOTE-111**
1. §2A : « Coefficients libres de la fermeture : aucun dans un coefficient de log » vaut a l'ordre s⁰. Le test de ir_i.py ne le prouve pas : il derive en β avant de chercher les symboles libres. Il faut le fonder sur la preuve structurelle de M-b (div X^M|₀ + T̂/s = 0 ; X^R solution d'un systeme hyperbolique a source lisse, donc sans log a tous les ordres sous H-loc). Les 54 libres d'ordre j ≥ 3 sont des artefacts de troncature.
2. §2B : les bornes sont D ∓ 6w, pas D ∓ 3w. La prediction de la coquille est 21,4466 ((4/5) · 4π · 4/(15w³) avec w = 1/2) et non 21,36 (artefact de quadrature de mp.quad). L'ecart est de −1,8e-5, pas 0,4 %. L'explication par le melange statique-rayonne est retiree.
3. Ajouter : les structures statique et rayonnee sont de meme signe. L'integrale sur toutes les regions egale la prediction rayonnee a 1e-9 pres : le reliquat statique est compense par les termes croises d'induction dans la coquille.

**NOTE-116**
4. §0, §4, §6 : remplacer « seules y echappent une source a helicite pure, un motif sans E ℓ = 2, ou un ensemble isotrope » par : « Q_tf = 0 si et seulement si la composante E ℓ = 2 du motif de polarisation lineaire, ponderee en k, s'annule (5 conditions reelles). L'helicite pure et l'ensemble isotrope en sont deux cas. D'autres cas physiques existent : p ∥ m de meme amplitude en phase (motif B pur, helicite nulle), p = x̂ + iŷ avec m = x̂ − iŷ ; pour des dipoles, la condition s'ecrit STF Re(pp†) = STF Re(mm†). L'helicite n'est ni necessaire, ni suffisante quand elle est partielle. »
5. §2D : la moyenne de l'interference est asymptotique (\|t₀\| grand devant la duree de la source) et globale ; une bande a bords francs ne decroit qu'en O(1/(\|t₀\|Δk)).

**NOTE-118**
6. §3 et §6, qualifications de K-V3 :
   - **ajouter K-D1** : le tenseur plat du secteur invariant de Weyl est lisse en s = 0. Sans cela, X′ = s² ln s diag(0, 0, f, −f)(x), conserve et sans trace, donnerait un log anisotrope.
   - **ajouter K-D2 (fond fixe)** : T est evalue sur le fond. Le terme gravitationnel de l'action anomale en charge de Weyl, ∫√g φ C², est nul sur le fond mais donne ln s × ∂⁴h a l'ordre lineaire en h (calcul M-b, indep_K_weyl). Il n'appartient pas a S_b tel que gele en NOTE-117. Il n'intervient qu'en presence d'une retroaction metrique, donc a un ordre superieur en κ [derive].
   - **ajouter K-D3** : regularite de W sur les modes a impulsion nulle, l'objection de M-a3 contre un facteur de forme F ln(□/μ²)F.
   - **retirer** « famille de metriques diagonale » pour T^(b) (M-b l'a verifie sur des familles non diagonales en (s, x, y)) et « etat de ψ causal et lisse » (consequence de l'equation).
   - **reformuler** « W hors orbite » : M-a3 montre que T^W[g] = s²T^W[η] vaut pour toute variation si W est exactement invariant de Weyl ; la vraie hypothese est la regularite de W (K-D3).

**Scripts** (R-55, conserves tels quels)
7. ir_i.py :
   - drapeau final a lire True ;
   - variable « neg » a renommer « termes en s ln s » ;
   - test diagonal a signe impose ;
   - test des libres aveugle (point 1) ;
   - etiquettes des bornes (point 2).
8. ir_k.py : T_2 = T_3 decoule de la symetrie de la famille et n'est pas un controle.

## 3. Ce qui change pour M-V3
- **Le renforcement de M-V3 est maintenu.** Les trois maillons sont audites (AU-V2).
- Conditions du candidat, mises a jour :
  - cadre S2 + [21] (champs charges conformes, vide conforme, in-in) ;
  - premier ordre en β ;
  - **fond fixe, sans retroaction** (K-D2, nouvelle formulation explicite) ;
  - lissite et regularite de la partie invariante de Weyl (K-D1, K-D3) ;
  - source causale avec E ℓ = 2 non nul (generique) ;
  - (2.17) comme critere pertinent (IR-q).
- La condition « famille de metriques diagonale » disparait pour T^(b).
- Reformulation de la condition de reglage fin : il ne s'agit pas d'helicite mais de l'annulation de 5 nombres, la composante E ℓ = 2 ponderee.
- Rien n'est grave. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 4. Verdict
**AU-V2** sur les trois blocs. Concordance sur tous les resultats porteurs (I-A ; L-A, L-C ; K-B, K-C), corrections mineures (normalisations, etiquettes, test aveugle, enumeration), qualifications nommees et completees.

## 5. Confrontation a la prediction
Prediction (NOTE-119 §5) : AU-V2 avec quatre corrections attendues.
- Normalisation des integrales de NOTE-111 : **realisee**, plus grave que prevu (prediction fausse, explication retiree).
- I-A' pur defaut d'etiquette : **realisee**.
- Precision de la codimension 5 : **realisee**, sous une autre forme (codimension exacte, enumeration tautologique).
- Qualification de K-D : **realisee**, avec deux hypotheses nouvelles (fond fixe et terme φC² ; regularite de W) et deux qualifications retirees.
- Non anticipe : le test aveugle des coefficients libres dans ir_i.py.
- Le risque principal nomme (hypothese cachee dans ir_k_ctrl.py) ne s'est pas materialise. Ce qu'il y avait de cache (K-C suppose le reste de T sans log) est couvert par K-B.

## 6. Consequences sur les pistes (proposees, non engagees)
- **IR-n** (Riegert hors diagonale) : levee pour T^(b) par l'audit (M-b, [calcule], familles en (s, x, y)) ; a acter par la greffe IR-m-c.
- **IR-o** : a reformuler en « regularite de la partie invariante de Weyl sur les modes a impulsion nulle (facteurs de forme non locaux) ».
- **IR-r** (nouvelle) : retroaction metrique. Le terme gravitationnel en φC² et la reponse h d'ordre κ peuvent-ils produire un log d'ordre κβ dans (2.17) ?
- IR-e, IR-h, IR-p, IR-q inchangees.

## 7. Greffes proposees (non entees)
- **IR-m-a** : NOTE-111 v2 (corrections 1 a 3, 7).
- **IR-m-b** : NOTE-116 v2 (corrections 4 et 5).
- **IR-m-c** : NOTE-118 v2 (corrections 6 et 8 ; IR-n levee pour T^(b)).

## 8. Non-surclassement
[conv]. Audit froid conduit (AU-V2). Les notes auditees restent [conv]. M-V3 reste un candidat non grave. Aucune promotion sans lecture exterieure.
