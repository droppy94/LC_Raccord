---
id: LC-04-REFERENCES
titre: "Repères bibliographiques (orientation, par module)"
codename: LC-RACCORD
tags: [references, bibliographie, orientation]
statut: support
version: 1.31
langue: fr
maj: "2026-07-26 — v1.31 : APURATION DU FRONT-MATTER. Le journal des versions antérieures (v1.30 et avant, 24 entrées) est retiré de cet en-tête et déposé dans `audit/CHANGELOG-ARCHIVE-04-REFERENCES.md`. Aucune ligne du corps n'est touchée. Motif : le champ `maj:` portait une part majeure du fichier et se rechargeait à chaque ouverture de session ; git porte déjà cette histoire nativement."
avertissement: >
  Repères d'orientation pour localiser la littérature, non une bibliographie
  vérifiée ni exhaustive. À confirmer (auteur, titre exact, année) avant tout
  usage formel ou citation.
---

# Repères bibliographiques (à vérifier avant citation)

> Ces entrées servent à **orienter la recherche documentaire** par module. Les
> intitulés sont donnés de mémoire et doivent être recontrôlés (le moteur de
> recherche / les bases comme arXiv, INSPIRE-HEP sont les sources à interroger).

## Module [A] — Survie conforme / CCC

> Chaînon `LC-A-SURVIE-CONFORME` : extension conforme régulière à `Λ>0` (cœur
> géométrique `établi`), facteur conforme (verrou D1), Weyl (D3).

- H. Friedrich, « On the existence of n-geodesically complete or future complete
  solutions of Einstein's field equations with smooth asymptotic structure »,
  Comm. Math. Phys. **107**, 587–609 (1986). `[confirmé]` — équations d'Einstein
  conformes régulières ; extension non dégénérée à `𝓘⁺` spacelike ; stabilité non
  linéaire de de Sitter. **Pierre angulaire du module A.** [LC-A]
- R. Penrose, *Cycles of Time*, 2010. `[confirmé]` — CCC. [LC-A]
- R. Penrose, exposés fondateurs de la CCC (« Before the Big Bang… »), ~2006.
- K. P. Tod, « Penrose's Weyl curvature hypothesis and conformally-cyclic
  cosmology », J. Phys. Conf. Ser. **229**, 012013 (2010) ; et *Gen. Rel. Grav.*
  (2015) — crossover, facteur conforme, hypothèse de Weyl. `[confirmé]` [LC-A, D1, D3]
- E. T. Newman, « A fundamental solution to the CCC equations », Gen. Rel. Grav.
  **46**(5), 1717 (2014) `[confirmé]` ; P. Nurowski, « Poincaré–Einstein approach to
  Penrose's conformal cyclic cosmology », Class. Quantum Grav. **38**(14), 145004
  (2021) `[confirmé]` — prescriptions (divergentes) du facteur conforme au crossover. [D1]
- C. Lübbe & J. A. Valiente Kroon (2013) — stabilité non linéaire de FRW (fluide de
  radiation) par équations conformes ; extension de Friedrich à la matière. `[confirmé]` [LC-A]
- O. Markwell & C. Stevens, « Toward fixing a framework for conformal cyclic
  cosmology », Gen. Rel. Grav. **55**, 93 (2023) ; arXiv:2212.06914v2. `[confirmé — en
  KB]` — met les trois prescriptions côte à côte en FLRW radiation ; réduction à
  `Ω̂=c₁â` ; bifurcation instable inter-éons ; seule la condition de Penrose (55d)
  satisfiable. **Source des équations de l'atlas `LC-A-D1` §4-bis.** [D1]
- A. Ashtekar, B. Bonga & A. Kesavan, asymptotique à `Λ>0` (`g̃^{ab}∂_aΩ∂_bΩ|_𝓘 = −Λ/3`) —
  *Asymptotics with a positive cosmological constant* II & III, Phys. Rev. D **92**, 044011 &
  104032 (2015) ; arXiv:1506.06152 & 1510.05593. `[confirmé]` [LC-A]
- K. Anguige & K. P. Tod — singularités isotropes ; Weyl nul initial ⟹ conformément
  plat (fluide parfait) ; *Isotropic cosmological singularities I & II*, Ann. Phys. **276**,
  257 & 294 (1999). `[confirmé]` [D3]
- Gurzadyan & Penrose, recherche de cercles concentriques dans le CMB, ~2010 ;
  réfutations / discussions (Wehus–Eriksen et al.). — prise empirique CCC.

### Front (a) / F3 — singularités génériques & statistique des spikes (substantiation d'A2★)

> Références consommées par `LC-D-F3-A2STAR` v0.1 (confrontation de la non-cascade
> d'A2★ à la statistique rigoureuse des spikes). **Verdict F3 = délimitation à lean
> positif** : SOUTIEN en réduction **G₂**, OBSTRUCTION en générique 3D. (La source
> KB-locale du verdict, Garfinkle gr-qc/0312117 `0312117v4.pdf`, et Lim arXiv:0710.0628
> déjà en KB, sont citées dans le chaînon ; non redupliquées ici.)
>
> **[NOTE HYGIÈNE — 2026-06-14]** Le PDF KB-locale `0312117v4_1.pdf` (Garfinkle,
> gr-qc/0312117v4, « Numerical simulations of generic singularities ») est servi par le
> mount comme **archive ZIP re-zippée à sha256 VOLATIL** (varie entre rafraîchissements du
> mount : observé `1cdf15db…c0a08aed`, puis `78bfad79…6f2b2a54`). Le **contenu est
> vérifié-bon** (en-tête PK, pages JPEG + OCR du bon papier). **Règle pour ce PDF :
> vérifier le CONTENU** (OCR / titre / auteur), **pas le hash** — un sha discordant à
> l'ouverture est **attendu** et ne constitue **pas** une alerte d'intégrité. (Les sha
> figés dans `LC-AUDIT-LOG-F3` et les notes de reprise archivées sont des instantanés
> historiques, non des invariants.)

- J. M. Heinzle, C. Uggla & W. C. Lim, « Spike oscillations », Phys. Rev. D **86**,
  104049 (2012) ; arXiv:1206.0932. `[confirmé]` — cadre BKL **modifié** : spikes =
  oscillations spatiales récurrentes brisant la localité asymptotique. **SOUTIEN (G₂)**
  de la non-cascade. [front (a) / A2★]
- J. M. Heinzle & C. Uggla, « Spike statistics », Gen. Rel. Grav. **45**, 939–957
  (2013) ; arXiv:1212.5500. `[confirmé]` — distribution rigoureuse des séquences de
  Kasner à spikes récurrents + scalaire de Weyl Hubble-normalisé, **en réduction G₂**.
  **SOUTIEN (G₂)** ; n'établit PAS le générique 3D (= gap nommé). [front (a) / A2★]
- T. Damour, M. Henneaux & H. Nicolai, « Cosmological billiards », Class. Quantum Grav.
  **20**, R145 (2003) ; arXiv:hep-th/0212256. `[confirmé]` — formalisme billard
  **ultralocal** (réflexions de Kasner par point) : **exclut les spikes par
  construction** (obstacle **OB** de F3). [front (a) / A2★]
- M. Henneaux, D. Persson & P. Spindel, « Spacelike singularities and hidden
  symmetries of gravity », Living Rev. Relativity **11**, 1 (2008) ; arXiv:0710.1818.
  `[confirmé]` — revue du programme billard / symétries cachées. [front (a) / A2★]
- C. Uggla, « Recent developments concerning generic spacelike singularities », Gen.
  Rel. Grav. **45**, 1669 (2013) ; arXiv:1304.6905. `[confirmé]` `[R-15 — ID corrigé]`
  — revue de la statistique des singularités génériques. **⚠ NE PAS confondre** avec
  arXiv:1306.6527 (« Spacetime Singularities: Recent Developments », actes) : version
  **sœur, même message**, titre/ID/journal distincts. [front (a) / A2★]
- W. C. Lim, L. Andersson, D. Garfinkle & F. Pretorius, « Spikes in the Mixmaster
  regime of G₂ cosmologies », Phys. Rev. D **79**, 123526 (2009) ; arXiv:0904.1546.
  `[confirmé]` `[R-20]` — spikes récurrents **transitoires** en modèles G₂ (attribution
  du caractère transitoire) ; confirmation tierce arXiv:2503.02684 (décrit Heinzle-Uggla
  comme « analyse statistique des spikes en modèles G₂ »). [front (a) / A2★]

## Module [B] — Géométrie de Cartan conforme

- Bailey, Eastwood, Gover, calcul tracteur pour structures conformes/projectives
  (« Thomas's structure bundle… »), ~1994.
- Littérature sur géométrie de Cartan et géométries paraboliques (Čap–Slovák).

## Module [C] — Structure modulaire / intrication

- Tomita–Takesaki, théorie modulaire (exposés de référence en TQC algébrique).
- Bisognano–Wichmann, hamiltonien modulaire = boost, ~1975–1976.
- Haag, *Local Quantum Physics* (type des algèbres locales, type III₁).
- E. Witten, « Notes on Some Entanglement Properties of QFT », ~2018 ; travaux
  sur algèbres de von Neumann et gravité / produit croisé (avec
  Chandrasekaran, Longo, Penington), ~2021–2023.
- Van Raamsdonk, « Building up spacetime with quantum entanglement », ~2010 ;
  Ryu–Takayanagi ~2006 ; Maldacena–Susskind (ER=EPR) ~2013 ; Swingle
  (réseaux de tenseurs / MERA) ~2012.
- A. Connes & C. Rovelli, « Von Neumann algebra automorphisms and
  time–thermodynamics relation in generally covariant quantum theories »,
  Class. Quantum Grav. 11 (1994) — temps thermique (support de LC-05 §5 et
  LC-08 §6 : voie de dérivation de la sérialité d'agent).

## Module [D] — Holographie céleste / AdS-CFT

- Maldacena, AdS/CFT, 1997–1998 (comptage `d`/`d+1`).
- A. Strominger, « Lectures on the Infrared Structure of Gravity and Asymptotic
  Symmetries », ~2017.
- Pasterski, Shao, Strominger ; revues d'holographie céleste (Pasterski ;
  Raclariu) ; correspondance théorèmes mous ↔ identités de Ward ; groupe BMS.

> Chaînon `LC-D-HOLOGRAPHIE-G3` : la donnée `g₍₃₎` à `𝓘⁺` = `⟨T⟩` d'une CFT céleste
> (dictionnaire de Fefferman–Graham) ; D1 reformulé en choix d'état. Références
> vérifiées sur le web (2026-06-07).

- S. de Haro, K. Skenderis & S. N. Solodukhin, « Holographic reconstruction of
  spacetime and renormalization in the AdS/CFT correspondence », Commun. Math. Phys.
  **217**, 595–622 (2001) ; arXiv:hep-th/0002230. `[confirmé]` — dictionnaire FG :
  connaître les sources `g₍₀₎` fixe l'expansion ; la donnée CFT nouvelle est la VEV de
  l'opérateur dual (`g₍d₎`) ; `⟨T_ij⟩ = (d/16πG) g₍d₎`. **Source du dictionnaire
  holographique de `LC-D`.** [D]

> Chaînon `LC-D-NONLIN-VERROU` : dualité électrique/magnétique du Weyl rescalé au bord
> (`E∝g₍₃₎∝⟨T⟩` ; `B∝Cotton[g₍₀₎]`) en `d=3`. Références vérifiées sur le web (2026-06-09).

- S. de Haro, « Dual gravitons in AdS₄/CFT₃ and the holographic Cotton tensor », JHEP
  **01** (2009) 042 ; arXiv:0808.2054. `[confirmé]` — le tenseur de stress renormalisé = champ
  **électrique** du Weyl, le tenseur de **Cotton** = champ **magnétique** ; dualité valable à tout
  rayon et **au-delà du linéaire**. **Source de `B∝Cotton`.** [D]
  **Renvois d'équations (LC-D-NONLIN-2PT, 2026-06-12, absence vérifiée avant ajout)** :
  éq. **(43)-(53)** — dualité des EOM, Cotton `(i/2)k³` ≡ éq. (47), équipartition
  `⟨𝓑𝓑⟩=⟨𝓔𝓔⟩` ≡ éq. (49)/(50) **en unités de dualité** (scoping R-11 ; 2e convention
  p.14 `𝓑=2C`) ; **+ éq. (90)** — exhibe **dans la source même** le couple pair `k³Π`
  radiatif + impair Chern-Simons **contact** (= C1+C2 du chaînon, corroboration
  excédentaire de l'audit) ; **+ éq. (121)** (App. C.2) — recoupe **indépendamment** le
  Cotton `(i/2)k³`. Extrait d'audit `EXTRAIT_0808_2054v1_dH.pdf` (sha au manifeste
  `LC-WORK-AUDIT-EXTRAITS-MANIFESTE-2PT`). [D]
- S. de Haro & A. C. Petkou, « Holographic aspects of electric–magnetic dualities », J. Phys.
  Conf. Ser. **110** (2008) 102003 ; arXiv:0710.0965. `[confirmé]` — `⟨T_ij⟩ = (ℓ²/8πG) C_ij`
  pour le Weyl self-dual ; Cotton **symétrique, sans trace, conservé** ; = condition de bord sur
  `g₍₃₎`. [D]
- D. S. Mansi, A. C. Petkou & G. Tagliabue, « Gravity in the 3+1-split formalism I & II »,
  Class. Quant. Grav. **26** (2009) 045008 & 045009 ; arXiv:0808.1212 & 0808.1213. `[confirmé]`
  — `8πT_ab = −lim_{r→∞} r³ C_arbr` (électrique) et `C_ab = lim_{r→∞} r³ C̃_arbr` (magnétique) ;
  valable en régime **non-linéaire** ; le Cotton mesure l'écart à la **platitude conforme**. [D]
- I. Bakas, « Energy–momentum/Cotton tensor duality for AdS₄ black holes », JHEP **01** (2009)
  003 ; arXiv:0809.4852. `[confirmé]` — réalisation explicite de la dualité énergie-moment/Cotton
  (secteurs axial/polaire). [D]
- A. Strominger, « The dS/CFT correspondence », JHEP **10** (2001) 034 ;
  arXiv:hep-th/0106113. `[confirmé]` — holographie à `Λ>0`, CFT euclidienne à `𝓘⁺`
  spacelike. [D]
- J. M. Maldacena, « Non-Gaussian features of primordial fluctuations in single field
  inflationary models », JHEP **05** (2003) 013 ; arXiv:astro-ph/0210603 (2002).
  `[confirmé]` — fonction d'onde de Sitter, `⟨T⟩` de bord, dS/CFT en cosmologie. [D]
- T. S. Bunch & P. C. W. Davies, « Quantum field theory in de Sitter space:
  renormalization by point splitting », Proc. R. Soc. Lond. A **360**, 117–134 (1978) ;
  DOI 10.1098/rspa.1978.0060. `[confirmé]` — vide de Bunch–Davies (état dS-invariant /
  euclidien, condition de Hadamard) ; candidat-sélecteur de D1 sur `g₃`. (Antériorités :
  Chernikov–Tagirov 1968 ; Schomblond–Spindel 1976.) [D]

> Chaînon `LC-D-NONGAUSS-TTT` (trois-point `⟨g₃g₃g₃⟩`, passage léger) + audit
> `LC-AUDIT-LOG-NONGAUSS` : sources du comptage 2+1, de la map `γ₃` et des recoupements
> Ward. Références vérifiées sur le web (2026-06-11).

- J. M. Maldacena & G. L. Pimentel, « On graviton non-gaussianities during inflation »,
  JHEP **09** (2011) 045 ; arXiv:1104.2846. `[confirmé]` — bispectre tensoriel en dS exact :
  les isométries dS contraignent les formes à **2 paires + 1 impaire** ; éq. 2.6 (`ε·ε*` —
  R-4 : facteur 4 **cohérent**, énoncé explicite à vérifier p.6 au passage lourd) ;
  éq. 2.18-2.20 (**2.20** porteuse littérale de `(H/M_Pl)⁴(LH)⁴`, 2.18 équivalente via
  2.19 — R-3). **Source « MP » du comptage [D].** Archive ZIP de pages JPEG+OCR en KB ;
  extrait d'audit `EXTRAIT_1104_2846v2_MP.pdf` (p.6 hors extrait, résidu gelé). [D]
  **`[SOLDE R-4 — passage lourd, 2026-06-12, audit 4/4]`** La **p.6 est désormais
  extraite** (`EXTRAIT_1104_2846v2_P6.pdf`, p.6-7, sha au manifeste
  `LC-WORK-AUDIT-EXTRAITS-MANIFESTE-LOURD`) : l'énoncé est **VERBATIM** — « The
  helicities can be normalized by ε^A_ij ε^{*B}_ij = 4δ^{AB} » — vérifié par les
  4 passes ET jusqu'à la **version publiée** (passe 3, Temps 3 ; l'extrait est la
  **v2**, post-correction de parité, note added). **R-4 SOLDÉE par exhibition ;
  le résidu p.6 est levé.** Renvois consommés par le sceau lourd : p.6 — mode BD
  `γ_cl=(H/√(2k³))e^{ikη}(1−ikη)` ; p.7 — éq. **(2.6)** avec le 4 explicite,
  re-refermant `𝒫=2H²/(M_Pl²k³)` slack nul (PL-B). [D]
- H. Osborn & A. Petkos (« A. C. Petkou » dans la version publiée), « Implications of
  conformal invariance in field theories for general dimensions », Ann. Phys. **231**
  (1994) 311 ; arXiv:hep-th/9307010. `[confirmé]` — construction groupe-théorique du
  trois-point pour spins arbitraires ; `d=3` : **2 structures indépendantes** pour `⟨TTT⟩`
  (recoupe MP, comptage 2+1) ; coefficients Ward `(d−2)(d+3)=6`, `d(d+2)=15` consignés
  [E4] (étalon **numérique** = passage lourd, exigence telle-qu'écrite). **Source « OP ».**
  Archive ZIP JPEG+OCR en KB ; extrait `EXTRAIT_hepth9307010v2_OP.pdf`. [D]
  **Renvois d'équations (LC-D-NONLIN-2PT, 2026-06-12, absence vérifiée avant ajout)** :
  éq. **(2.23)-(2.24)** — formes du deux-point `⟨TT⟩` : (2.23) recoupe le secteur
  **pair** `k³·Π^TT` (C1) ; (2.24) tenseur **impair**, C2 **cohérente** avec OP à
  points séparés (un seul tenseur impair admissible — jamais « confirmée », R-13).
  Pages consommées : **p.3 et p.7** (erratum R-9 du chaînon §5). Extrait d'audit
  `EXTRAIT_hepth9307010v2_2PT.pdf` (sha au manifeste
  `LC-WORK-AUDIT-EXTRAITS-MANIFESTE-2PT`). [D]
  **Renvois d'équations (LC-D-NONGAUSS-TTT-LOURD, 2026-06-12, audit 4/4 — absence
  vérifiée avant ajout)** : éq. **(5.5)/(5.6)** — `C_T` du scalaire et du fermion
  libres en `d` général (étalons de refermeture, p. imprimée 18) ; éq.
  **(5.12)/(5.13)** — coefficients `(t=a, b, c)` des trois-points libres
  (p. imprimée 19) ; éq. **(6.42)** — identité de Ward
  `4S_d[(d−2)(d+3)a − 2b − (d+1)c]/[d(d+2)] = C_T` (p. imprimée 26) ⟹ `(6,2,4,15)`
  en `d=3` : **la consignation [E4] est vérifiée à la source, l'exigence « étalon
  numérique telle-qu'écrite » ci-dessus est SOLDÉE** (PL-A tenue telle qu'écrite,
  refermeture sur les DEUX étalons en `d` général, slack nul) ; renvoi croisé
  interne p. imprimée 27 (« in agreement with the results for free field
  theories… »). **Convention de pagination (R-15)** : pages imprimées 18/19/26/27
  = pages **scan** 19/20/27/28 (décalage +1, page de garde de l'archive).
  Extrait d'audit `EXTRAIT_hepth9307010v2_WARD.pdf` (4 pages, sha par fichier et
  par page au manifeste `LC-WORK-AUDIT-EXTRAITS-MANIFESTE-LOURD`). [D]
- D. M. Hofman, D. Li, D. Meltzer, D. Poland & F. Rejon-Barrera, « A proof of the
  conformal collider bounds », JHEP **06** (2016) 111 ; arXiv:1603.03771. `[confirmé]` —
  éq. **C.24** : premier recoupement de la formule Ward chapeautée (attribution **R-2** :
  la formule est portée par 1603.03771 + 1511.04077, **recoupant** OP — pas « OP »
  directement). Archive ZIP JPEG+OCR en KB ; extrait `EXTRAIT_1603_03771v2_C24.pdf`. [D]
- P. Bueno & W. Witczak-Krempa, « Bounds on corner entanglement in quantum critical
  states », Phys. Rev. B **93**, 045131 (2016) ; arXiv:1511.04077. `[confirmé]` —
  App. **C** : conventions `C_T` et structures `⟨TT⟩`/`⟨TTT⟩` en `d=3`, second recoupement
  Ward (R-2). Archive ZIP JPEG+OCR en KB ; extrait `EXTRAIT_1511_04077v2_AppC.pdf`. [D]
- J. Soda, H. Kodama & M. Nozawa, « Parity violation in graviton non-gaussianity »,
  JHEP **08** (2011) 067 ; arXiv:1106.3228. `[confirmé]` — en dS **exact**, aucune violation
  de parité dans le bispectre (la forme impaire, présente en fonction d'onde, est
  **absente du bispectre** — résolution du bloc [D] du chaînon, cohérente avec le scoping
  S2) ; la violation de parité réapparaît `∝` slow-roll. [D]
- M. Shiraishi, D. Nitta & S. Yokoyama, « Parity violation of gravitons in the CMB
  bispectrum », Prog. Theor. Phys. **126** (2011) 937 ; arXiv:1108.0175. `[confirmé]` —
  pendant observationnel (CMB) de la forme impaire ; complète la résolution du bloc [D]. [D]

> Chaînon `LC-D-W3-GPY` (consolidation rang 3, route externe) — intrant du régime (a),
> 2026-06-12. Références vérifiées sur le web (2026-06-12) ; UNE consommée, TROIS en
> attente (sous-fronts (b)/(c) non ouverts).

- S. Giombi, S. Prakash & X. Yin, « A Note on CFT Correlators in Three Dimensions »,
  JHEP **07** (2013) 105 ; arXiv:1104.4317 (v4 en KB, PDF natif `1104_4317v4.pdf`,
  24 p.). `[confirmé — CONSOMMÉE]` — classification par invariants conformes 3d :
  §3.2 éq. (3.10)-(3.11) (ansatz 6 coefficients, 3 relations de conservation ⟹
  **2 paires + 1 impaire** pour `⟨TTT⟩`, paires = scalaire ⊕ fermion libres) ;
  éq. (3.12) (impaire à points séparés, théories CS-matière violant la parité —
  hors périmètre S2, nuance consignée au chaînon §2) ; §3.1 éq. (3.4) (unicité de
  l'impaire sous inégalité triangulaire) ; abstract (paires libres / impaire non
  libre). **TROISIÈME route du comptage 2+1** (indépendante de MP∩OP et des orbites
  S₃×P). [D]
- D. Anninos, T. Hartman & A. Strominger, « Higher Spin Realization of the dS/CFT
  Correspondence », Class. Quant. Grav. **34** (2017) 015009 ; arXiv:1108.5735 (v1 en
  KB, `1108_5735v1.pdf`, 18 p.). `[CONSOMMÉ — sous-front (b), 2026-06-13]` — candidat de CFT
  de raccordement (modèle Sp(N) euclidien, dual conjecturé de la gravité higher-spin
  de Vasiliev en dS₄). Consommée au sous-front **(b)** (OUVERT ET CLOS 2026-06-13 ;
  cf. `LC-D-SPN`, sceau `verif_spn.py` EXIT 0/23) — relevé : règle de signe éq. (2.4)
  `⟨…⟩_Sp(N) = −⟨…⟩_O(N)` (un (−1) par boucle ≡ N→−N) ; verdict CONSOLIDATION → décision
  ouverte documentée ; caveat consigné MAINTENU : higher-spin ≠ Einstein ⟹ `(a,b,c)`
  propres NON fixés. [D]
  `[NOTE F1 — 2026-06-13]` Re-consommée par F1 (`LC-D-F1-SPN`, sceau `verif_F1_spn.py` EXIT 0/20) pour le COEFFICIENT : (A.10)/(A.11) `⟨J^(s)J^(s)⟩_dS=−(ℓ²_dS/G_N)f` (∀ spin pair, dont s=2) ; `C2=1/(2N)`, `C2∼−G_NΛ∼1/N` ⟹ `ℓ²/G_N∼N` dans Vasiliev. Caveat higher-spin ≠ Einstein **confirmé PAR LE COEFFICIENT** : `|C_T^Sp(N)|/N=3/(32π²)` (OP) vs cible programme `3/(4π⁴)`, écart `π²/8` = O1 ⟹ **CFT de raccordement ≠ Sp(N)**. Aucun fetch neuf (même source v1). [D]
- O. H. E. Philcox & M. Shiraishi, « Non-Gaussianity Beyond the Scalar Sector… »,
  Phys. Rev. D **111**, 123502 (2025) ; arXiv:2409.10595 (v2 en KB,
  `2409_10595v2.pdf`). `[confirmé — CONSOMMÉ — front F2, 2026-06-14]` — bornes Planck PR4 sur
  onze gabarits de bispectres tensoriels et mixtes (aucune détection, max 2σ).
  Réservé au sous-front **(c)** (non ouvert) ; caveat consigné : map
  programme→gabarits f_NL = décision ouverte préalable ; acquis négatif en vigueur. [D]
  `[NOTE F2 — 2026-06-14]` Sous-front **(c)** OUVERT et CONSOMMÉ par F2
  (`LC-D-F2-TTT-PLANCK` v0.1, audité 3/3) — supersede « (non ouvert) » ci-dessus.
  COMMIT : 11 templates PR4, aucune évidence, max 2σ ; énoncé pivot §I/§II (TTT
  single-field slow-roll einsteinien d'amplitude INDÉTECTABLE, suppression slow-roll).
  **Table III** = bornes appariées en forme sur `W³(n_NL)`, **INCONFRONTABLES** faute de
  valeur programme (OB) ⟹ **R-23**, renvoi-avant F5 (extraction différée, sous garde-fou
  « borne appariée inconfrontable »). Équivalence `f^ttt_NL` à O(1) près (R-24, note 2). [D]
  `[NOTE F5 — 2026-06-14]` Ré-consommée par F5 (`LC-D-F5-ETAT-RACCORD` §4ter) : extraction de la **Table III** (`W³(n_NL)`, SEVEM T+E+B) classée L1 **`inconfrontable`** (borne appariée en forme sur W³, pas de valeur programme — OB) ⟹ dépôt comme intrant futur, **aucune** conversion en contrainte ; **R-23 suspendue à OB**. Coefficient « 0,53 » (note 6) = F2-hérité (R-27). AUCUN fetch neuf.
- O. H. E. Philcox & M. Shiraishi, « Testing Graviton Parity and Gaussianity with
  Planck T-, E- and B-mode Bispectra », Phys. Rev. D **109**, 063522 (2024) ; arXiv:2312.12498 (v2 en KB,
  `2312_12498v2.pdf`). `[confirmé — CONSOMMÉ — front F2, 2026-06-14]` — pendant parité-impaire/parité-paire des
  bornes PR4. Réservé au sous-front **(c)** (non ouvert). [D]
  `[NOTE F2 — 2026-06-14]` Sous-front **(c)** OUVERT et CONSOMMÉ par F2
  (`LC-D-F2-TTT-PLANCK` v0.1, audité 3/3) — supersede « (non ouvert) » ci-dessus.
  COMMIT : template équilatéral sourcé par champs de jauge (= au-delà d'Einstein),
  `f^ttt_NL = 900 ± 700` (Table II) vs 1300 ± 1200 Planck 2018, aucune détection, parité
  paire ET impaire ⟹ borne sur l'enrichissement au-delà d'Einstein, au mieux borne sup.
  lâche sur W³ (D3c, ne ferme pas). Renvoi journal résolu (web-check 2026-06-14 :
  PRD 109, 063522, publié 14 mars 2024 ; relevé par la passe d'audit 2). [D]

### Front (a) / F6 — BMS / mémoire gravitationnelle (cœur G1/G2 ; sources G3 NON consommées)

`[NOTE F6 — 2026-06-15]` Le cœur interne **G1/G2** de F6 (`LC-D-F6-BMS-MEMOIRE` v0.1) est **KB-only** et **ne consomme AUCUNE référence neuve** : il s'appuie sur des relations amont **déjà scellées** (de Haro–Skenderis–Solodukhin `⟨T⟩=(d/16πG)g₃`, déjà confirmée ; `WEYL-BUNCHDAVIES`, `NONLIN-VERROU`, `HOLOGRAPHIE-G3`, `CT-ATN` — internes).

`[ANTI-FETCH — G3 non ouvert]` Les sources du **volet G3** (flux-balance Λ-BMS, `décision ouverte`, différée) sont **listées mais NON consommées** tant que G3 n'est pas explicitement ouvert (gel des cibles AVANT lecture, anti-fit) : **triangle IR de Strominger** (lectures sur Strominger, *Lectures on the Infrared Structure of Gravity* ; soft theorems ⟺ BMS ⟺ memory) ; **Λ-BMS / BMS en dS** (Compère–Fiorucci–Ruzziconi et al.) ; **mémoire gravitationnelle** (Christodoulou ; Thorne) ; **Meissner–Penrose `2503.24263`** (KB-locale, ZIP/JPEG — crossover/CCC). Toute ouverture de G3 fera l'objet d'un **cadrage dédié** (cibles gelées AVANT fetch), avec consommation explicite.

### Front (a) / O₂ — CFT de raccordement / jonction inter-éons (PIVOT ; étape (a) KB-only)

`[NOTE O₂ — 2026-06-15]` L'étape **(a)** d'O₂ (`LC-D-O2-JONCTION` v0.1, cartographie de la jonction) est **interne (S-O2-1)** et **ne consomme AUCUNE référence neuve** : elle s'appuie sur la **dualité graviton-dual de de Haro déjà scellée** (`0808.2054`, KB-locale ; S1 AdS + S2 dS) et sur des relations amont scellées (`HOLOGRAPHIE-G3`, `CT-DUAL`, `CT-GAMMA` — internes). Résultat : le crossover `𝒞` se lit comme une **transition Dirichlet→Neumann** ; la conjecture **(C-O2)** [réciprocité de Penrose ≟ S-map] est **étayée structurellement, non prouvée** ; la réduction de A4 est conditionnée à deux gates `à inventer` **P1/P2**.

`[ANTI-FETCH — P1 / étape (b)]` Le test de **P1** (la réciprocité conforme de Penrose au `𝒞` **est** la S-map de de Haro — facteurs compris : signe, `S²=−1`, induction `g₀↔g₃`) requerra, en sus de l'algèbre KB-locale, une lecture **gelée AVANT fetch** de la **réciprocité conforme de Penrose** dans la CCC (l'« hypothèse réciproque » / inversion du facteur conforme `Ω↦−1/Ω` au crossover) : **R. Penrose, _Cycles of Time_, 2010, DÉJÀ en KB [LC-A]** (+ exposés fondateurs CCC) ; de Haro `0808.2054` (S-map) reste KB-locale. **Listée, NON consommée** tant que l'étape (b) n'est pas explicitement ouverte (anti-fit) ; toute ouverture fera l'objet d'un **cadrage dédié** (cibles gelées AVANT fetch), avec consommation explicite. **Aucune référence bibliographique neuve** n'est ajoutée par ce lot (renvoi à l'existant).

`[NOTE O₂ (b) — 2026-06-15]` L'étape **(b)** (test de P1, `LC-D-O2-P1` v0.1, sceau `verif_O2_P1.py`
EXIT 0/20) est **interne / KB-local** (S-O2-b-1) et **ne consomme AUCUNE référence neuve** : algèbre
sur les modes de Haro `(f_a,f_b)` + S-map scellée. **Résultat** : l'inversion de Penrose `Ω·ω=−1`
induit le **swap** `g₀↔g₃` mais **pas** le `−𝟙` de la dualité (elle est une **involution conforme**)
⟹ P1 **réduite au signe** `s=(−1)^w`.

`[ANTI-FETCH — b′ : parité du poids conforme w]` Trancher `s=(−1)^w` (prochain pas **(b′)**) requiert
un fetch **ciblé** sur la **parité du poids conforme `w`** du mode TT sous le facteur conforme
**négatif** `ω<0` (loi de réciprocité **tensorielle** de Penrose) : **R. Penrose, _Cycles of Time_**
(2010, **déjà en KB [LC-A]**) + lois de transformation FG de de Haro (`0808.2054`, KB-locale).
**Listé, NON consommé** tant que (b′) n'est pas explicitement ouvert (anti-fit) ; ouverture sous
**cadrage gelé dédié** (cible = parité de `w`, gelée AVANT fetch). **Aucune référence neuve** par ce lot.

`[ANTI-FETCH — c : transport de Hodge — NON CONSOMMÉ]` La tentative (b′) ayant été **réfutée**, le
résidu **structurel** de P1 a été tranché en **(c)** (`LC-D-O2-HODGE` v0.1, verdict `discordance`) par
**croisement KB-local** (`CT-DUAL` §2-§3, `CT-REALITE`, `F6`, `O2-P1`). Le fetch **ciblé** prévu par le
cadrage gelé `LC-WORK-CADRAGE-O2-HODGE` (loi de **dualité gravitationnelle TT linéarisée** `E↔B` du
Weyl en FG, rapport au facteur conforme `ω<0`) est resté **NON CONSOMMÉ** : la structure s'est
**pincée KB-local** (la jonction réalise le swap mais non le `−1` du Hodge ; le signe vient de la
continuation dS `i^{d-1}`, source unique). **Aucune référence neuve** par ce lot.

`[ANTI-FETCH — P2 : critère d'exclusion intrinsèque des α-vacua — NON CONSOMMÉ (HOLD)]` L'exécution de
**P2** (gate ÉTAT, `LC-D-O2-P2` v0.1, verdict `discordance / négatif propre`) s'est faite **KB-local**
(`CT-DUAL-DS`, `WEYL-BUNCHDAVIES`, `F5-ETAT-RACCORD`, `O2-HODGE`). Le fetch **ciblé** prévu par le
cadrage gelé `LC-WORK-CADRAGE-O2-P2` (S-O2-P2-1 ii — **critère d'exclusion intrinsèque des α-vacua en
dS** : régularité euclidienne `S⁴` / Hadamard, statut avec/sans choix) est resté **NON CONSOMMÉ** :
décision **fetch = HOLD** — le statut est **pinçable KB-local** (`F5/O₁` : la dS-invariance seule ne
sélectionne pas BD, l'argument standard « état régulier le plus bas » tombe par non-unitarité ; le
sélecteur s'effondre sur {Hadamard-posé ; A4}), et le résidu (argument Hartle–Hawking `S⁴` *sans choix*
en dS exact) est **non décisif** (borné à l'éon idéalisé, capé par la collision ①↔④). **Aucune
référence neuve** par ce lot.

`[ANTI-FETCH — F4 : entropie gravitationnelle (Clifton–Ellis–Tavakol) / Past Hypothesis (Carroll–Chen) — NON CONSOMMÉ (HOLD)]` L'exécution de
**F4** (A4 principiel, `LC-D-F4-A4-PRINCIPIEL` v0.1, verdict `délimitation`) s'est faite **KB-local**
(`CROSSOVER-STABILITE`, `D1-STABILITE-WEYL §5`, `D1-FACTEUR-CONFORME §5`, `WEYL-BUNCHDAVIES`,
`AUDIT-VERDICT`, `O2-P2`). Le fetch **ciblé** prévu par le cadrage gelé
`LC-WORK-CADRAGE-F4-A4-PRINCIPIEL` (S-F4-2 — **forme du functional `S_grav` et son indépendance au
Weyl** : Clifton–Ellis–Tavakol « a gravitational entropy proposal » ~`1303.5612` ; Carroll–Chen
*Past Hypothesis*) est resté **NON CONSOMMÉ** : décision **fetch = HOLD** — la **circularité** de la
voie entropie-de-Weyl est **structurelle/définitionnelle** (toute `S_grav` au sens de Weyl est monotone
en l'invariant `w` ⟹ « basse `S_grav` ⟺ faible Weyl » = identité), le verdict est **pinçable KB-local** ;
un fetch ne confirmerait que la forme du functional (circularité inchangée) ou, à bas prior, exigerait un
functional **Weyl-indépendant** sélectionnant `g₃→0` — inaccessible à un principe de fond (« la fermeture
vient de la **marée**, hors symétrie », `D1-STABILITE-WEYL §5`). **Aucune référence neuve** par ce lot.

`[ANTI-FETCH — F6-G3 : Λ-BMS — NON CONSOMMÉ (HOLD) ; 2026-06-16]` L'exécution du volet **F6-G3** (flux-balance Λ-BMS à `𝓘⁺` dS spacelike, `LC-D-F6-G3-LAMBDA-BMS` v0.1, verdict `délimitation`) s'est faite **KB-local** (S-G3-1 : parité E/B + Hessien G1 scellé ; garde-fou `C̃_T=+C_T` `CT-DUAL-DS` ; 4 obstructions F5→`O₂` ; BD dS `+i` ; `⟨g₃g₃⟩∝k³`). Les sources du volet G3 **listées dès v1.23** (triangle IR de **Strominger** ~`1703.05448` ; **Λ-BMS** Compère–Fiorucci–Ruzziconi ; **mémoire** Christodoulou / Thorne ; **Meissner–Penrose `2503.24263`** KB-locale) restent **NON CONSOMMÉES** : le repli **S-G3-2** (fetch conditionnel pré-autorisé) **n'a pas été déclenché** — décision **fetch = HOLD** : la délimitation (gap nommé pointant `O₂`) est **robuste sans corroboration de la littérature** ; un fetch n'aurait fait que **documenter** le caractère « Λ-BMS non standard / débattu », sans changer le verdict. **Aucune référence neuve** par ce lot.

## Module [E] — Anomalie de trace / champ d'échelle

- Riegert, action non locale pour l'anomalie de trace, ~1984.
- Programmes de gravité invariante d'échelle (Wetterich ; 't Hooft, « Local
  conformal symmetry… », ~2014–2015).
- *Note exploratoire `LC-E-PLANCK-RESIDUEL`* — G. W. Gibbons & S. W. Hawking,
  « Cosmological event horizons, thermodynamics, and particle creation », Phys. Rev. D
  **15**, 2738 (1977) `[confirmé]` (entropie/température de de Sitter) ; 't Hooft /
  Susskind, borne holographique `[à vérifier — module E, hors front (a)]` ; Padmanabhan, gravité entropique /
  comptage cosmique `[à vérifier — spéculatif, module E]`.

## Module [F] — Conforme UV / fantômes

- Stelle, gravité à dérivées supérieures renormalisable mais avec fantômes,
  ~1977.
- Mannheim, gravité conforme et tentatives PT-symétriques de traiter les
  fantômes.
- Reuter, Weinberg — sécurité asymptotique (point fixe UV).

## Transverse — Dynamique symbolique / formalisme thermodynamique (support du sous-programme φ : LC-05 à LC-08)

> Sélection variationnelle, dérivation cinématique et cartographie de la
> constante de croissance `φ` de l'ossature (LC-05 à LC-08, objets transverses
> appariés à LC-02-OSSATURE).

- W. Parry, « Intrinsic Markov chains », Trans. Amer. Math. Soc. 112 (1964) —
  mesure de Parry (entropie maximale). [LC-05]
- D. Ruelle, *Thermodynamic Formalism*, 1978 — principe variationnel, pression.
  [LC-05]
- R. Bowen, *Equilibrium States and the Ergodic Theory of Anosov
  Diffeomorphisms*, Lecture Notes in Math. 470, 1975. [LC-05]
- D. Lind & B. Marcus, *An Introduction to Symbolic Dynamics and Coding*, 1995 —
  sous-décalages de type fini, Perron–Frobenius. [LC-05, LC-07]
- R. Lyons, « Random walks and percolation on trees », Ann. Probab. 18 (1990) —
  branching number. [LC-05]
- H. Kesten, « Symmetric random walks on groups », Trans. Amer. Math. Soc. 92
  (1959) — mesure spectrale sur arbres réguliers. [LC-05]
- V. W. de Spinadel, « The metallic means family », Visual Mathematics 1 (1999) —
  moyennes métalliques (or, argent, bronze ; `x²=nx+1`). [LC-07]
- OEIS — A000045 (Fibonacci / or), A000129 (Pell / argent), A000931 (Padovan /
  plastique) : suites associées aux pinceaux réfractaire et métallique. [LC-07]
- *(Repères fondationnels, LC-08, à confirmer)* : R. D. Sorkin, exposés sur les
  ensembles causaux (« causal sets : discrete gravity », order + number ;
  croissance séquentielle classique Rideout–Sorkin) ; A. N. Whitehead, *Process
  and Reality* (1929) — le devenir comme procès sériel (repère culturel, non
  technique).

### Fermeture du verrou φ — régime & Trotterisation (LC-09, LC-10)

> Limites quantiques de vitesse (Lemme A) et déroulement en sauts quantiques
> (Lemme B). Toutes `à vérifier` avant citation.

- N. Margolus & L. B. Levitin, « The maximum speed of dynamical evolution »,
  Physica D 120 (1998) — borne `τ⊥ ≥ πℏ/2E` (moyenne). [LC-09, LC-10]
- S. Lloyd, « Ultimate physical limits to computation », Nature 406 (2000) —
  taux d'opérations, scaling extensif. [LC-09, LC-10]
- L. Mandelstam & I. Tamm, « The uncertainty relation between energy and time… »,
  J. Phys. USSR 9 (1945) — borne `τ⊥ ≥ πℏ/2ΔE` (variance) ; survit en III₁. [LC-10]
- L. B. Levitin & T. Toffoli, « Fundamental limit on the rate of quantum
  dynamics », Phys. Rev. Lett. 103 (2009) — borne combinée ML/MT. [LC-10]
- J. J. Bisognano & E. H. Wichmann, hamiltonien modulaire = boost (wedge),
  J. Math. Phys. ~1975–1976 — ancrage géométrique de la borne modulaire (Unruh).
  [LC-10] (déjà cité côté module [C].)
- S. Deffner & E. Lutz, « Quantum speed limit for non-Markovian dynamics »,
  Phys. Rev. Lett. 111 (2013) — bornes de vitesse par débit d'entropie relative ;
  base de la transposition modulaire (Lemme A). [LC-10]
- R. L. Hudson & K. R. Parthasarathy, « Quantum Itô's formula and stochastic
  evolutions », Comm. Math. Phys. 93 (1984) — calcul d'Itô quantique, table
  diagonale `dA_e dA_f† = δ_{ef} dt`. [LC-10]
- J. Dalibard, Y. Castin & K. Mølmer, « Wave-function approach to dissipative
  processes in quantum optics », Phys. Rev. Lett. 68 (1992) — Monte-Carlo
  wavefunction (déroulement en sauts). [LC-10]
- H. J. Carmichael, *An Open Systems Approach to Quantum Optics* (1993) ;
  H.-P. Breuer & F. Petruccione, *The Theory of Open Quantum Systems* (2002) —
  trajectoires quantiques, GKLS, unravelings. [LC-10]
- *(rappel, déjà côté LC-02)* E. A. Carlen & J. Maas — flux de gradient
  entropique, métrique BKM/KMB pour semi-groupes à bilan détaillé ; pertinent au
  résidu KMB du Lemme A. [LC-02, LC-10]
- D. Buchholz & E. H. Wichmann, « Causal independence and the energy-level
  density of states in local quantum field theory », Comm. Math. Phys. 106 (1986)
  — propriété de scission (split property). [LC-10 §1.4 bis]
- S. Doplicher & R. Longo, « Standard and split inclusions of von Neumann
  algebras », Invent. Math. 75 (1984) — inclusion scindée standard, facteur type I
  intermédiaire. [LC-10 §1.4 bis]
- H. Araki, « Relative entropy of states of von Neumann algebras », Publ. RIMS 11
  (1976) — entropie relative en type III (additivité sous produit). [LC-10 §1.4 bis]
- D. Petz, « Monotone metrics on matrix spaces » (1996) et travaux sur la métrique
  de Kubo–Mori–Bogoliubov (Hessienne de l'entropie relative). [LC-10 §1.4 bis]

## Bases à interroger pour vérification

- arXiv (gr-qc, hep-th), INSPIRE-HEP, Google Scholar.
- Pour chaque entrée : confirmer auteur·e·s, titre exact, année, et lien
  primaire avant toute insertion dans un livrable.
