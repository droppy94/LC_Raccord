---
id: NOTE-BORD-EON-153-IR-ab-LECTURE-2412.11022-2405.01024
numero: 153
serie: I
branche: Q-M3 suite (IR-ab, lecture)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 153)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-152-ARMEMENT-IR-ab-LECTURE-2412.11022-2405.01024 (sha256 aaf4a492046ad3253968b48780118653c292d2f89a5ac6c66db8188a9b6417f1, sceau 2026-10-13T11:02:23Z)
sources:
  - "[8] A. J. Foraci, R. P. Woodard, Resumming Photon Loops for Inflationary Gravity, arXiv:2412.11022v1 [gr-qc], 15 decembre 2024, UFIFT-QG-24-08, prepublication (aucune reference de revue dans l'en-tete) ; texte integral (17 pages) lu via alphaXiv le 2026-10-13 ; extraits src/SOURCE-2412.11022v1-extraits.txt, sha256 12b9a99d285f7598b0ea2accbc49864352824ec62bacb005a000ee7db3496418"
  - "[27] S. P. Miao, N. C. Tsamis, R. P. Woodard, Summing Gravitational Effects from Loops of Inflationary Scalars, arXiv:2405.01024v2 [gr-qc], 7 octobre 2024, publie Class. Quant. Grav. 41, 215007 (2024) ; texte integral (27 pages) lu via alphaXiv le 2026-10-13 ; extraits src/SOURCE-2405.01024v2-extraits.txt, sha256 9b461ee307597753f0e0a78d3077339836ced216527309afd4f1347e80dcfdd6"
instruments:
  - "irab_conv.py, sha256 84295061b1c38f05a229ee592e6b07e95d1d7a2eba4fc15d25a9dd8cf8b855c5 (version avec controle de convention ajoute apres une premiere execution, empreinte initiale 9356db0ec611ab34), EXIT 0, sortie irab_conv_sortie.txt (3e1ed753819232ed)"
depend: [NOTE-BORD-EON-152-ARMEMENT-IR-ab-LECTURE-2412.11022-2405.01024, NOTE-BORD-EON-148-IR-z-LECTURE-2501.01972 (v2), NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-133-IR-u-EXECUTION]
verdict: "AB-V1 qualifie AB-V4 (deux limitations declarees par les sources : course de G ignoree ; attribution du contre-terme a Z par commodite)"
prediction_realisee: "oui pour l'essentiel ; la composante AB-V4 est un peu plus forte que prevue (course de G, non la jauge)"
rouvre_si:
  - "audit froid"
  - "lecture de 2110.08715 (origine du procede, modeles sigma) ou de 2307.09386 (variante electromagnetique) si l'on veut remonter plus haut"
  - "source ulterieure verifiant la resommation a deux boucles pour gravite + matiere"
---

# NOTE-153 : IR-ab. Les deux sources amont confirment le coefficient et l'exposant ; le procede repose sur l'appariement ln μ / ln a de la regularisation dimensionnelle, sans verification d'ordre superieur, et les sources declarent elles-memes deux limitations (course de G ignoree, attribution par commodite). Verdict **AB-V1 qualifie AB-V4**

## 0. Resume
- **ab-1** [extrait, calcule] : [8] eq. (53) : C_0i0j → C^tree{1 + κ_W²H²/(40π²) ln a}, soit **2GH²/(5π) = 8bκH²** pour N_V = 1 (irab_conv.py) ; eq. (60) : 2ℏGH²/(5πc⁵), resomme [a]^(2ℏGH²/5πc⁵). C'est bien le double de Dirac (NOTE-148 v2), et [8] est la source de la lecture par proportionnalite. Le photon ne porte pas d'obstacle a la conservation (eq. 30, ∝ D − 4) ni de tenseur induit (eq. 34) ; « correlated to the absence of an Eddington (R²) counterterm » : c₁ = 0.
- **ab-2** [extrait] : le procede est **anterieur aux deux sources** : [8] et [27] renvoient tous deux a Miao-Tsamis-Woodard JHEP 03 (2022) 069, arXiv:2110.08715 (modeles sigma non lineaires), et [27] cite en outre Glavan-Miao-Prokopec-Woodard arXiv:2307.09386 pour la variante electromagnetique (δZ = −4[C − (3D−8)C₄]H²). [27] eq. (91) definit δZ = D[2(D−1)c₁ − c₂]κ_W²H² en **dissequant** le contre-terme R² (eq. 89 : (R − DΛ)² + 2DΛ[R − (D−2)Λ] + D(D−4)Λ², dont seul le terme median est retenu comme renormalisation de champ) et en retenant du contre-terme de Weyl le terme en ∂₀²h_ij C̃_0i0j (eq. 90). [8] eq. (57) reprend la formule a l'identique (« the analysis is identical »). Conversions verifiees : γ_photon = −κ_W²H²/(80π²), −2γ = coefficient de (53) ; γ_MMC = 3GH²/(20π), −2γ = −3GH²/(10π) = eq. (93) [calcule].
- **ab-3** [extrait] : justification **structurelle** et explicite : eq. (5) de [8] et (6) de [27], (2H)^(D−4)/(D−4) − (aμ)^(D−4)/(D−4) = −ln(μa/2H) + O(D−4) : les divergences primitives ne portent pas de facteur a^(D−4), les contre-termes si ; « The close relation between μ and a(t) in relation (5) suggests that this second source of secular logarithms can be resummed by a variant of the renormalization group ». Les deux sources distinguent les logarithmes de **queue** (propagateur MMC, formalisme stochastique) des logarithmes de **renormalisation** (groupe de renormalisation) ; les champs conformes (« Passive fields », [27] §1 : scalaires conformes, fermions, photons) n'ont pas de queue : « Because the photon propagator has no tail term, the only secular logarithms from photon loops derive from renormalization (5). This means that factors of ln(μ) always come in the form ln(μa) ». Pour les champs conformes, le cas est donc classe **purement ultraviolet**, conformement a la prediction.
- **ab-4** [extrait] : **aucune verification a deux boucles** pour gravite + matiere ; aucun cas exactement soluble pour le graviton. Le seul controle est celui de [27] §2 sur le modele sigma AB : la γ_{B²} tiree des contre-termes reproduit le coefficient du logarithme de ⟨B²⟩ de la Table 1 (« non-trivial agreement ») ; c'est un controle de l'**explication** (le coefficient du log a l'ordre calcule = −2γ), non de la **resommation** (ordres superieurs). [27] rappelle que le formalisme stochastique, lui, « can be proven to reproduce each order's leading logarithms [19] » ; rien de tel n'est affirme pour la variante du groupe de renormalisation. Statut selon les mots des sources : « explained » / « explanation » pour le logarithme a une boucle ; « can be resummed » / « it is even possible to sum up the effects » pour la puissance.
- **ab-5** [extrait] : **jauge gravitationnelle non discutee** dans les deux sources pour les boucles de matiere ; [27] §2 nomme « the gauge issue » comme ce que les modeles sigma evitent, et note 10 attribue un contre-terme non covariant ΔC a la brisure de de Sitter du propagateur du graviton (boucles de gravitons, hors cadre). [8] ne discute que l'invariance U(1). Etat : vide conforme du repere plat (propagateur de Minkowski rescale, [8] §2 ; NOTE-148 v2). Prescription in-in de Schwinger-Keldysh, equation (35) de [8] avec l'operateur de Lichnerowicz sans fixation de jauge.
- **ab-6** [extrait] : [8] §6 : « "late time" here means during an endless phase of de Sitter expansion. More work needs to be done to infer what would happen in the current universe after a long phase of primordial expansion » ; [27] §6 : « Over a prolonged period of inflation these factors must overwhelm even the smallest coupling constant. At this point perturbation theory breaks down ». **Rien** sur a → ∞ en tant que limite, ni sur un seuil. Deux limitations **declarees par les sources** : (L1) « If we ignore possible running of Newton's constant it is even possible to sum up the effects » ([27] §5 et §6 ; β_G « vanishes at the order we are working ») ; (L2) l'attribution du terme median de (89) a une renormalisation de champ plutot qu'a une renormalisation de G est adoptee « because we have no information about higher order couplings it is convenient to adopt the latter interpretation ».
- **Point hors questions, consigne pour IR-ad** [extrait] : [8] eq. (37)-(39) ecrit le noyau non local f_B = ∂⁴{θ(Δη − Δr)(ln[μ²(Δη² − Δr²)] − 1)} (noyau retarde de ln(−□/μ²)) et montre, eq. (49)-(50), que **« the nonlocal contribution vanishes »** sur le mode de de Sitter u₀ = (1 + ikη)e^(−ikη), par l'identite (∂₀ + ik)²∂₀u₀ = 0 ; le logarithme seculaire provient entierement du terme **local** 8π ln(aa′)δ⁴(x − x′). C'est la structure que le programme a adoptee (log dans WZ, NOTE-131/133 ; Γ[g] sans contribution) et la prediction ad-3 de NOTE-158. Lecture faite sous le gel de NOTE-152, non sous celui de NOTE-158 ; elle sera citee dans NOTE-159 comme lecture hors gel declaree (precedent NOTE-138).

## 1. Table de concordance [calcule] (irab_conv.py, EXIT 0)
| Grandeur | Source | Programme | Egal |
|---|---|---|---|
| Coefficient du log, photon ([8] eq. 53, 60) | κ_W²H²/(40π²) = 2GH²/(5π) | 8bκH², N_V = 1 | oui |
| Rapport photon / Dirac | 2 | 2 (NOTE-148 v2) | oui |
| γ photon depuis c₂ (eq. 56), c₁ = 0 | −κ_W²H²/(80π²) | recalcule | oui |
| Exposant −2γ = coefficient du log | oui ([8] eq. 58 → 53) | | oui |
| γ MMC depuis c₁, c₂ ([27] eq. 85-86, 91) | 3GH²/(20π) | recalcule | oui |
| Exposant MMC ([27] eq. 93) | −3GH²/(10π) | −2γ | oui |
| ∂c₂/∂ln μ (photon) | 1/(160π²) | b_V | oui (la lecture « c₂ = b » de NOTE-137 vaut pour la derivee en ln μ ; en ln μ² c'est b/2) |

## 2. Lecture [derive]
1. **Chaine des sources de la clause resommee.** 2110.08715 (modeles sigma, procede formule) → 2307.09386 (electromagnetisme sous boucles de gravitons, δZ) → 2405.01024 [27] (scalaire MMC sous gravite, δZ = D[2(D−1)c₁ − c₂]κ²H², eq. 91) → 2412.11022 [8] (photon, eq. 57-58, c₁ = 0) → 2501.01972 (Dirac, par proportionnalite 1/2, NOTE-148 v2) → 2501.05077 (revue, NOTE-135). A chaque maillon, l'exposant est −2γ avec γ tire des contre-termes BPHZ a une boucle ; pour les champs conformes, c₁ = 0 et l'exposant est fixe par le seul contre-terme de Weyl, dont le residu en ln μ est b (NOTE-137 retrouve a la source, table §1).
2. **Nature du procede.** Trois ingredients, tous explicites dans les sources : (i) l'appariement ln μ ↔ ln a (eq. 5/6), fait de regularisation dimensionnelle et non conjecture ; (ii) l'absence de queue pour les champs conformes, qui assure que **tous** les logarithmes seculaires sont de type (i) ; (iii) l'equation de Callan-Symanzik d'une theorie renormalisable appliquee a un calcul BPHZ d'une theorie non renormalisable, avec un choix d'attribution des contre-termes (L2) et β_G = 0 a l'ordre calcule (L1). (i) et (ii) sont solides ; (iii) est le pas non demontre. Les sources le disent : « explained » pour le logarithme, « can be resummed » pour la puissance, « if we ignore possible running of Newton's constant » pour la sommation.
3. **Ce que cela change pour G-V3.** Rien au coefficient γ = 8 (confirme une troisieme fois a la source, pour le photon directement). La clause resommee de NOTE-138 v3 (« procede de groupe de renormalisation, non verifie a l'ordre superieur, valable tant que de Sitter persiste, limite Ω → 0 = extrapolation du programme ») est **exacte** et peut etre precisee par les deux limitations declarees (L1, L2) et par l'origine du procede (2110.08715). Elle n'a pas a etre adoucie (pas de controle d'ordre superieur) ni durcie au-dela de L1 et L2 (aucun enonce de restriction excluant le regime utile ; la jauge n'est simplement pas discutee).
4. **Remarque sur l'extrapolation Ω → 0.** Les sources parlent d'« endless phase of de Sitter expansion » comme domaine du « late time » ; l'eon de la CCC est exactement cela (de Sitter asymptotique jusqu'a 𝓘⁺). L'extrapolation du programme n'est donc pas une sortie du domaine declare par les sources, mais une lecture de leur « endless » comme Ω → 0 ; elle reste du programme, puisque les sources ne traitent pas de 𝓘⁺ ni de quantites rescalees.

```
   clause resommee de G-V3 : ce qui est ancre et ce qui ne l'est pas (apres IR-ab)
   ----------------------------------------------------------------------------------------
   coefficient du log (gamma = 8)           : calcule (133), aveugle (137), source Dirac (148), source photon (153)
   appariement ln mu <-> ln a               : fait de regularisation dimensionnelle ([8] eq. 5, [27] eq. 6)
   absence de queue (champs conformes)      : [27] §1 (Passive fields), [8] §5
   exposant = -2 gamma, gamma des contre-termes : [27] eq. 91, [8] eq. 57-58 ; retrouve (irab_conv.py)
   puissance a^p (sommation)                : Callan-Symanzik, beta_G = 0 a l'ordre calcule, "if we ignore possible
                                              running of Newton's constant" ; attribution des contre-termes "convenient"
   ordre superieur                          : non verifie (aucune source) ; stochastique prouve, RG non
   jauge gravitationnelle                   : non discutee (boucles de matiere)
   limite Omega -> 0                        : "endless phase" chez les sources ; lecture du programme
```

## 3. Verdict
**AB-V1 qualifie AB-V4.**
- **AB-V1** : coefficient confirme a la source pour le photon (ab-1) ; procede fonde sur l'appariement structurel ln μ / ln a et l'absence de queue des champs conformes (ab-3) ; aucune verification d'ordre superieur ni calcul independant pour gravite + matiere (ab-4) ; la clause de NOTE-138 v3 est maintenue.
- **AB-V4** (qualification, faible) : deux limitations declarees par [27] a porter dans une revision du libelle : (L1) la sommation en puissance suppose β_G = 0 au-dela de l'ordre calcule (« if we ignore possible running of Newton's constant ») ; (L2) l'identification du contre-terme a une renormalisation de champ plutot que de G est un choix « convenient ». L'independance de jauge gravitationnelle n'est pas discutee (pas une limitation declaree : un silence).

## 4. Confrontation a la prediction
Prediction (NOTE-152 §4) : ab-1 [**realise**] ; ab-2 [**realise**, avec une precision : le procede remonte a 2110.08715, en amont des deux sources] ; ab-3 [**realise**] ; ab-4 [**realise** : pas de deux boucles ; le controle du modele sigma porte sur l'explication, non sur la resommation] ; ab-5 [**realise** : jauge non discutee, Bunch-Davies / vide conforme] ; ab-6 [**realise**, et la composante AB-V4 vient de la course de G (L1) et de l'attribution (L2), non de la jauge comme prevu]. Prediction realisee ; composante AB-V4 un peu plus forte que prevue.

## 5. Consequences (rien n'est grave)
- Libelle de G-V3 (NOTE-138 v3 §1.3), clause resommee : revision proposee, non entee : « ... procede de groupe de renormalisation (Callan-Symanzik, γ de la renormalisation de champ du graviton par le seul contre-terme de Weyl, β_G = 0 a l'ordre calcule ; origine Miao-Tsamis-Woodard 2110.08715 ; appariement ln μ / ln a de la regularisation dimensionnelle, [8] eq. 5), introduit par « suggests », **sans verification a l'ordre superieur, sous l'hypothese declaree d'absence de course de G et d'attribution du contre-terme a la renormalisation de champ** ([27] §5-6), valable « tant que la phase de Sitter persiste » ... ».
- Chaine 133/135/137/148 : aucune correction. La lecture « c₂ = b » de NOTE-137 est precisee : derivee en ln μ.
- IR-ad (NOTE-158/159) : [8] eq. (49)-(50) fournit un appui de source a la prediction ad-3 (contribution non locale nulle sur le mode de de Sitter) ; a citer comme lecture hors gel declaree.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 6. Pistes
- Audit froid de NOTE-153 (lecture aveugle des eq. 53, 56-58 de [8] et 89-93 de [27] ; conversion).
- Lecture de 2110.08715 et 2307.09386 si l'on veut l'origine du procede (priorite basse : les deux sources lues en contiennent la substance).
- Revision du libelle de G-V3 (NOTE-138 v4) apres audit, integrant IR-ab, IR-ac, IR-aa, IR-ad.

## 7. Non-surclassement
[conv], non audite. Lecture d'une prepublication ([8]) et d'un article publie ([27]). Les conversions sont [calcule] ; les enonces de statut sont les mots des sources. G-V3 reste un candidat non grave ; la clause resommee reste un procede, non un theoreme.
