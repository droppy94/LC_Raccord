# RAPPORT VA-2 : audit adverse de l'article v2.5 et de la note compagnon

Auditeur isolé VA-2, 2026-10-16. Pièces lues : ARTICLE-v2.5.tex, ARTICLE-v2.4.tex, COMPANION.tex, NOTE-BORD-EON-211 (gel), NOTE-BORD-EON-212 (rédaction), NOTE-202 v2 (LB), NOTE-207 v2 (RJ). Aucun autre fichier de /home/claude n'a été ouvert. Sources externes : 21 références vérifiées par alphaXiv (texte des articles) et recherche web. Environnement : Python 3.13.16, NumPy 2.5.3, SciPy 1.18.1, soit exactement les versions déclarées en section Verification (les scripts eux-mêmes ne sont pas dans le périmètre et n'ont pas été relancés).

Classement : **E** = erreur (énoncé faux tel qu'écrit, ou attribution fausse ou au-delà du niveau déclaré) ; **C** = correction (imprécision, surclassement léger, incohérence de notation) ; **K** = complément (manque utile).

## 0. Synthèse

| Axe | Résultat |
|---|---|
| E1 gel | Les 12 points du gel sont implémentés. Deux écarts non déclarés : « croissant à terme » (R1.2) remplacé par a → ∞ ; FW-2 (explicitations « signalées comme telles ») seulement en partie respecté. Un retrait de fond non déclaré : la remarque ΛCDM de la v2.4 sur le couplage ajusté (voir E6). |
| E2 références | Les 25 entrées existent. Titres, auteurs, revues et identifiants sont exacts pour les 24 références externes (la note compagnon n'est pas vérifiable). Quatre attributions dépassent le niveau de lecture déclaré ou le déforment : Gurzadyan-Penrose, Birrell-Davies, Markwell-Stevens, Meissner-Penrose. |
| E3 surclassement | **Une erreur de fond au §5** : « une règle exigeant la régularité formelle distingue ces deux classes ». C'est faux au sens de la Déf. 1(c) et contredit la Rem. 2(1) ainsi que NOTE-207 §6. La conclusion CCC reste conditionnelle ; le « premier étage, champ test » est respecté. |
| E4 cohérence | Les numéros et les renvois sont justes. Deux glissements de la convention du chapeau dans la Rem. 2 de l'article (T̂ et R̂). Il y a un conflit de notation λ (jauge) / λ (constante cosmologique) dans l'article, et un conflit H (Higgs) / H (Hubble) dans la note compagnon. |
| E5 compagnon | **Une erreur** : le résumé affirme « exactly when » pour W,Z, contre la restriction d'audit « suffisance ». Un surclassement : « flow-adapted gauge does not transpose » (NOTE-207 dit seulement « non fait »). Les numéros d'équations RJ sont transposés sans le dire. |
| E6 pertes | Pertes utiles : remarque ΛCDM, « Majorana restent singulières », plusieurs items de la liste « non établi », réserves de la section Verification. |
| E7 lisibilité | Six points obscurs : P « one-particle projector », fréquences positives et négatives à scri moins, double notation du poids radiatif, Rem. 2 titrée « coupled » mais contenant un champ test, entre autres. |

Verdict proposé au sens du gel (§3 de NOTE-211) : **V25-V3 au sens strict**, puisque l'audit trouve plusieurs énoncés faux tels qu'écrits (E3.1, E3.2, E1.3, E2.4, E5.1). Toutes ces erreurs se corrigent localement par une ou deux phrases. Aucune ne touche les preuves des Prop. 1 à 4, ni le Lemme 2, ni le noyau {A4 ; A2★ ; N}. Une fois les corrections faites, le verdict attendu est V25-V2, ce qui rejoint la prédiction du gel.

---

## E1. Implémentation du gel

| Point | Où | État | Constat |
|---|---|---|---|
| R1.1 | Déf. 1 (a)(b)(c) | fait | Les exemples sont justes (sin ln\|η\| ; \|η\|^{-1/2} ; \|η\|^{1/2}). Voir C1.1 et C1.2. |
| R1.2 | §2 | fait, avec écart | **C1.1** : le gel demande « a croissant à terme » ; l'article écrit a(t) → ∞. Aucune preuve n'utilise la monotonie, donc l'écart est bénin, mais il n'est pas déclaré dans NOTE-212. En revanche, le cadre FLRW général rend fausses deux affirmations qui étaient vraies sur de Sitter (E1.3, E1.4). |
| R1.3 | §4.2, 1er paragraphe | fait | **K1.1** : l'hypothèse « fond A = 0 et champ chargé test (pas de rétroaction de Maxwell) » reste implicite. Il suffit de l'ajouter. |
| R1.4 | Prop. 3 | fait | **C1.2** : « pôle simple si et seulement si le coefficient est non nul » est vrai, mais laisse croire que ρ̂ est borné quand le coefficient s'annule. Sur de Sitter c'est le cas (terme O(mk/H), borné sans limite). Sur FLRW général, Ω peut décroître plus vite que \|η\| (a ∝ t^p, p > 1 donne Ω ∝ \|η\|^{p/(p-1)}), et (m/Ω)·O(k\|η\|) peut alors diverger. Il faut le préciser ou restreindre à de Sitter. |
| R1.5 | preuve Prop. 4(a) | fait | La preuve est correcte (θ continue, non décroissante, divergente : e^{-iθ} parcourt le cercle). |
| R1.6 | Annexe A | fait | La base est correcte (invariants de rang 0 à 3 ; σ^{ab} g_{ab} = 0 ; pas d'invariant de rang 3). |
| R1.7 | §5, fin | fait | Le gel situe la phrase au « §6 v2.4 », mais elle était au §5 de la v2.4. C'est une coquille du gel ; NOTE-212 la corrige. |
| R1.8 | Verification | fait | Les versions sont exactes et correspondent à l'environnement. **C1.3** : le script de la v2.4 s'appelait `dirac_scri_check_v2.py` et celui de la v2.5 s'appelle `dirac_scri_check_v2_1.py`. Le changement de nom n'est pas expliqué, alors que la v2.5 affirme « outputs reproduced byte for byte ». Il faut dire s'il s'agit du même fichier renommé ou d'une version 2.1. |
| R2 | §4.3 | fait | Voir **C1.4** sur le support compact et E2 sur les attributions. |
| R3 | Rem. 2 (4 points) et compagnon | fait | |
| R4 | bibliographie | fait | NOTE-212 dit « 25 références, toutes dans la liste du gel ». C'est inexact : Penrose 2010, Birrell-Davies et Parker-Toms viennent de la v2.4 et ne figurent pas dans S1 à S19. Leur maintien est légitime (FW-1 interdit l'ajout, pas le maintien), mais Birrell-Davies reçoit dans la v2.5 une **nouvelle** attribution (E2.2). |
| RJ | Rem. 1, « Dependence on the weight », Rem. 2(4), Prop. 5(b) et suite | fait | Voir E3. |

**E1.1 (C), FW-2.** Les explicitations ajoutées (preuve de la Prop. 4(a), base de l'Annexe A, état de Slater) ne sont pas marquées « standard ; explicitation, pas un résultat nouveau ». La section Provenance dit « adds ». Il faut ajouter une demi-phrase.

**E1.2 (K), changements de fond hors gel.** On en trouve trois :
- le paragraphe ΛCDM du Lemme 2 a été retiré (voir E6.1) ;
- l'hypothèse « smooth Cauchy data of compact support » a été ajoutée au §4.3 (voir C1.4) ;
- la Déf. 1(c) compte comme irréguliers le ln Ω et le facteur exp(ic ln Ω). C'est un choix définitionnel couvert par R1.1, déclaré « we also count ».

Aucun nouveau résultat mathématique hors des chantiers n'a été trouvé.

**E1.3 (E), exemple de la Prop. 4 faux sur FLRW général.** « m ∝ Ω^{1/2} gives a convergent field » demande ∫ a^{-1/2} dt < ∞. Les hypothèses du §2 ne le garantissent pas. Pour a = t^{3/2}, on a bien ∫ dt/a < ∞, mais ∫ t^{-3/4} dt diverge. La v2.4 précisait « (i.e. m ∝ e^{-Ht/2}) », ce qui plaçait l'exemple sur de Sitter ; cette précision a disparu. Correction : écrire « on de Sitter space, m ∝ Ω^{1/2} ... ». Le second exemple, m ∝ Ω(1+Ω^{1/2}), reste vrai en général.

**E1.4 (E), résumé (i) : « In conformal time the mode equation has a regular singular point at scri with exponents ± i m/H ».** C'est vrai sur de Sitter seulement (la Rem. 1 le dit). Sur FLRW de loi de puissance, m a ∝ \|η\|^{-p/(p-1)} avec p/(p-1) > 1, ce qui donne un point singulier irrégulier. Même pour H → H∞, la régularité de Fuchs exige un développement analytique de a. Correction : « On de Sitter space, ... ».

**C1.4 (support compact, §4.3).** L'article demande « f in the range of 1 − P, ... smooth Cauchy data of compact support ». Pour un projecteur P de type vide (spectral, non local), cet ensemble peut être réduit à {0}. En Minkowski, aucune fonction d'onde de Dirac d'énergie positive n'est à support compact (théorème de type Hegerfeldt ; Thaller, *The Dirac Equation*). Le même obstacle est plausible pour les modes de fréquence positive de Bunch-Davies en carte plate. L'argument n'a besoin que de f lisse, à décroissance rapide et normalisée : la différence de rang un reste lisse et Plancherel s'applique. Il faut remplacer « compact support » par « Schwartz ». NOTE-202 et le gel ne demandaient pas le support compact.

**C1.5 (Prop. 1, preuve).** « it takes the values χ0+ and −χ0+ arbitrarily close to η = 0 » est inexact : la composante *s'approche* de ±χ0+, elle ne prend pas exactement ces valeurs. La v2.4 donnait les suites explicites. Il faut reprendre la v2.4 ou écrire « comes arbitrarily close to ».

**C1.6 (Rem. 1).** « P±(0) = χ0± » ne tient qu'à une phase constante près, puisque θ n'est défini qu'à une constante près (« up to a constant », Prop. 1). Il faut écrire « P±(0) = e^{∓ic}χ0± » ou fixer la constante de θ. De plus, « the interference term is present iff both χ0± ≠ 0 » doit s'entendre comme « peut être présent ». Pour X = β, le terme d'interférence d'ordre 0 s'annule identiquement (χ0+†βχ0− = 0) et n'apparaît qu'à l'ordre Ω, ce que NOTE-207 dit explicitement pour τ_00.

---

## E2. Références et niveaux de lecture

### E2.a Vérification par outil (21 références)

| Réf. | Vérifié | Résultat |
|---|---|---|
| Tod2022, arXiv:2202.10864 | texte | Titre « Some questions about Conformal Cyclic Cosmology », P. Tod. §2 : « Without some explicit mechanism to make the dust contribution fade away, its density is proportional ... to R^{-3} so it comes to dominate the radiation » ; §3 : « Can one implement mass fade-out? ». Attribution exacte. |
| Tod2015 | biblio de Tod 2022 et de Bachelot | GRG 47 (2015), no. 3, Art. 17. Exact. |
| MeissnerPenrose2025, 2503.24263 | texte | « The Physics of Conformal Cyclic Cosmology ». Exact (titre corrigé). |
| MarkwellStevens2022, 2212.06914 | texte | Titre et auteurs exacts. Voir E2.3. |
| GurzadyanPenrose2013 | biblios de Tod 2022, M-S et M-P | « On CCC-predicted concentric low-variance circles in the CMB sky », EPJ Plus 128 (2013) 22, arXiv:1302.5162. Exact. |
| Friedrich2015 | biblio de Bachelot | AHP 16 (2015) 2215–2238. Exact. |
| Friedrich2017 | biblio de Bachelot | CMP 350 (2017) 803–844. Exact. |
| Bachelot2020, 2003.03356 | texte | Titre exact, scalaire conformément couplé. (IV.4) : sur la métrique de type de Sitter, ∫ m² dτ/\|τ\| ∼ ∫ m²(t) dt < ∞, qualifiée de « much weaker ». La phrase de l'article « Bachelot's weak condition is, on de Sitter space, ∫ m² dt < ∞ » est exacte. |
| Ibison2011, 1105.3767 | texte | Titre exact, « To appear in 'Cosmology', InTech ». On y lit « increase in the rest mass of a free electron » et « the phase oscillates rapidly, infinitely quickly so at the boundary » (§8.3). Voir K2.1. |
| Cotaescu2002, hep-th/0109199 | texte et biblio de Boonpan | Titre exact, PRD 65 (2002) 084008. Hankel d'ordre ν± = 1/2 ± i m/ω. Exact. |
| DFMR2019, 1902.09144 | texte | Titre et auteurs exacts. Lemme 3.1 « following [20, Lemma 6.3] ». Prop. 4.5 : coïncide avec Bunch-Davies spinoriel. §3.3 : BD « selects only negative frequencies on ... I^- » via [9] = DHP2010. Exact. |
| FinsterReintjes2016 | biblio de DFMR | « A non-perturbative construction of the fermionic projector on globally hyperbolic manifolds II – Space-times of infinite lifetime », ATMP 20 (2016) 1007–1048, arXiv:1312.7209. Exact. |
| AllenLutken1986 | biblio de DFMR | CMP 106 (1986) 201. Exact (le titre original écrit « two point » sans trait d'union). |
| Boonpan2026, 2610.00410 | texte | Titre et auteur exacts. (A.36) 1/(e^{2πm/H}+1), « independent of the comoving momentum », « standard Gibbons–Hawking Fermi–Dirac plateau ». Exact. |
| Hollands2001 | biblios de DHP2010 et DFMR | CMP 216 (2001) 635, gr-qc/9906076. Exact. |
| DHP2009 | biblio de DHP2010 | Rev. Math. Phys. 21 (2009) 1241, 0904.0612. Exact. |
| DHP2010, 1009.5179 | texte et biblio de DFMR | Titre et auteurs exacts ; AHP 12 (2011) 1449. Remarque après la Prop. 4.2 : « Although we do not prove it explicitly, we presume that ... weakly converging to the unique (and pure) ground state ... β → ∞ ». Le « that they presume » de l'article est exact. |
| Wrochna2017, 1711.04011 | texte | Titre exact ; Klein-Gordon seulement. Exact. |
| MasonNicolas2004 | biblio de Pham | JHDE 1 (2004) 197–233. Exact. |
| MasonNicolas2012 | biblio de Pham | JGP 62 (2012) 867–889 (arXiv:1101.4333, non cité). Exact. |
| Pham2021, 2107.06521 | texte | Dirac **sans masse** sur Kerr. Exact. |

Birrell-Davies (1982), Parker-Toms (2009) et Penrose (Bodley Head 2010) sont confirmés par les bibliographies de Boonpan et de Tod. Seule la note compagnon n'est pas vérifiable.

### E2.b Attributions au-delà du niveau déclaré (FW-1) ou inexactes

**E2.1 (E, FW-1) : Gurzadyan-Penrose.** L'article écrit « Penrose's 'suppressed rest-mass hypothesis' is a condition on the conformal factor [GurzadyanPenrose2013, MarkwellStevens2022] ». NOTE-202 déclare GP au niveau [titre, via S14 et S12]. Attribuer un contenu à GP dépasse donc le niveau de lecture. Le contenu se trouve chez Markwell-Stevens (Π_aΠ^a = 1 + QΩ̌² + O(Ω̌³), « supressed rest-mass hypothesis », qu'ils attribuent à leur réf. [12] = GP). Correction : « ... [MarkwellStevens2022], after [GurzadyanPenrose2013] ». Remarque annexe : le gel (R4) dit que le titre de GP a été vérifié « dans les bibliographies de Tod et de Friedrich », alors que NOTE-202 dit « via S14 et S12 ». Les deux notes ne concordent pas sur ce point.

**E2.2 (E, FW-1) : Birrell-Davies.** L'article écrit « The fermionic pair-creation factor 1/(e^{2πm/H}+1) is standard [Boonpan2026, BirrellDavies] ». Birrell-Davies ne figure dans NOTE-202 à aucun niveau ; NOTE-202 §3.2 demandait de **lire** une source publiée (Kanno-Sasaki-Tanaka). Je n'ai pas pu établir que Birrell-Davies donne ce facteur fermionique en de Sitter. Boonpan le cite seulement comme référence générale [3]. Correction : retirer Birrell-Davies de cette phrase, ou le citer seulement pour le cadre général des coefficients de Bogoliubov.

**E2.3 (C) : Markwell-Stevens.** L'article écrit « the asymptotic decay of rest mass is an assumption that recent work does not address ». Markwell-Stevens disent : « this theory requires controversial physical assumptions, such as the asymptotic decay of rest-mass ... we do not address them here ». L'article transforme « nous ne les traitons pas » en « les travaux récents ne les traitent pas ». Correction : « Markwell and Stevens list the asymptotic decay of rest mass among the controversial assumptions of CCC that they do not address ».

**E2.4 (E) : Meissner-Penrose, §5.** L'article écrit « Tod and Meissner–Penrose assume a smooth conformal extension of the geometry and of conformally invariant matter ». La phrase vient de la v2.4. Or le résumé de M-P dit : « the geometry at the crossover surface is conformally smooth, **except at a discrete set of points ... Hawking points** ». NOTE-202 (S15) mentionne aussi les points de Hawking. Correction : « smooth except at a discrete set of Hawking points ».

**C2.5 : Allen-Lütken.** L'article écrit « the maximally symmetric state of Hadamard form [AllenLutken1986, DFMR2019] ». AL est au niveau [titre]. Le caractère Hadamard vient de DFMR (Prop. 4.5 et résumé). Il faut séparer : « maximally symmetric [AL], of Hadamard form [DFMR, Prop. 4.5] ».

**C2.6 : DHP2009.** L'article écrit « independently of the renormalisation prescription ». La Déf. 4.1 de DHP impose l'axiome 1 à toute prescription admissible, ce qui justifie la phrase pour les prescriptions qui satisfont les axiomes de Wald. Il faut ajouter « among prescriptions satisfying Wald's axioms ».

**K2.1 (important) : Ibison.** L'article présente Ibison comme le « noyau classique de la Prop. 3 », ce qui est exact (éq. 33). Mais Ibison, §8.3 et §10, conclut que « only two of the 4 bi-spinor components survive to the boundary » (seules les composantes d'énergie positive arrivent à scri, quelles que soient les données initiales) et que le 3-courant s'annule. Cette conclusion est incompatible avec la Prop. 1 et la Rem. 1 : la norme est constante, χ0 est arbitraire et ses deux composantes β = ±1 survivent. Elle provient d'une approximation \|λ\| ≫ 1 qui néglige des termes en e^{-π\|λ\|}. Un lecteur qui ouvre Ibison y trouvera l'affirmation contraire de celle de l'article. L'article doit le signaler en une phrase : « Ibison's conclusion that only one β-eigenspace reaches the boundary holds, for positive-frequency modes, up to terms of relative size e^{-2πm/H}; for general solutions both components persist (Proposition 1). » Cela renforce d'ailleurs la nouveauté de la Rem. 1 et de la Prop. 2(b).

**Conformes au niveau déclaré** : Cotaescu, DFMR (Lemme 3.1, Prop. 4.5, §3.3), Finster-Reintjes, Boonpan, Hollands, DHP2009 (Déf. 4.1, Thm 4.1), DHP2010, Wrochna, Pham, Mason-Nicolas (titres seulement), Friedrich 2015 (« each massive field ... own analysis »), Friedrich 2017, Bachelot, Tod 2022 (sections 2 et 3, conformément au gel), Tod 2015.

---

## E3. Surclassement

**E3.1 (E, de fond) : §5, « A matching rule that requires formal regularity of the conformal field equations therefore distinguishes these two classes, at the level of a test field. »**
- Au sens de la Déf. 1(c), la régularité formelle est « a property of a choice of unknowns, not of the solutions ». Elle ne peut donc pas distinguer des classes de solutions.
- La Rem. 2(1) affirme que l'équation de Dirac rescalée est formellement régulière si et seulement si m = Ωμ, et donc pour aucune masse constante. Une règle qui exige la régularité formelle du système (matière comprise) rejette les deux classes.
- NOTE-207 §6 dit explicitement : « la classe à un seul exposant est régulière au niveau des sources ; **aucune n'est régulière au niveau de l'équation de matière** ». NOTE-207 §7 précise que l'obstruction invariante est l'interférence **plus** le caractère singulier (Fuchs) de l'équation de Dirac. L'article ne garde que l'interférence (§4.3 : « what is independent of the choice of variable is the interference »).

Correction : « A matching rule that requires the *sources of the geometric equations* to be regular distinguishes these two classes at the level of a test field; the Dirac equation itself keeps its regular singular point in both (Remark 1, Remark 2(1)). » La même précision doit figurer dans la Rem. 2(4) et au §4.3.

**E3.2 (E) : §5, « bounded without limit for every solution that contains both a particle and an antiparticle component at scri ».** C'est faux pour k = 0. Une solution k = 0 peut avoir χ0+ et χ0− tous deux non nuls ; alors τ = mB e0e0 est constant et la source du Weyl est nulle (NOTE-207, tableau ; Rem. 2(4) elle-même range k = 0 avec les séries entières). L'amplitude est proportionnelle à k\|c+\|\|c−\|. Il faut ajouter « with **k** ≠ 0 ».

**E3.3 (E) : §4.3, « Dependence on the weight ».** L'article écrit « [the other components] ... for solutions with both exponents they carry the interference factor Ω^{∓2im/H}, bounded and without limit ». C'est faux sur deux points.
- τ_0a = −Ω k_a N, où N = u†u est constant (Lemme 1). Cette composante n'a aucun facteur d'interférence ; NOTE-207 la décrit « d'ordre Ω, non oscillant ».
- τ_0a et τ_ab sont O(Ω), donc tendent vers 0. Ce qui est « borné sans limite », c'est τ_ab/Ω, c'est-à-dire la contribution à S/Ω.

Correction : « τ_ab/Ω carries the interference factor ... ; τ_0a = −Ωk_aN carries none ».

**E3.4 : résumé, introduction, Prop. 5.** Conformes, sauf trois points :
- E1.4 (« regular singular point » sans restriction à de Sitter).
- **C3.5** : la Prop. 5(b), « the state contains at least one Dirac particle in the sense of Section 4.3 », renvoie au §4.3. Celui-ci n'établit la positivité du coefficient intégré que pour Bunch-Davies, à masse constante, sur de Sitter. Pour un autre état, ou pour une masse variable (cas même de la Prop. 5(b)), il faut un mode ajouté à composante particule dominante (NOTE-202, LB-4, « conséquence pour l'article »). Il faut ajouter cette condition explicitement.
- **C3.6** : le résumé (iii) écrit « For a one-particle excitation of a pure quasi-free Hadamard state the statement holds ». C'est exact quant au pôle ; le signe et la valeur du coefficient dépendent de l'état. On peut l'écrire en trois mots.

**Conclusion CCC conditionnelle.** Oui. La Prop. 5 est formulée sur des règles ; la phrase « Rule (b) is a choice » avec Friedrich 2017 est conforme au gel RJ ; on ne trouve pas d'« RG-4 réfutée » (FW-3 respecté).

**« Premier étage, champ test ».** C'est respecté : Rem. 2(4) (« test Dirac field on de Sitter space »), §5 (« at the level of a test field ... not established here »), §6 (« coupled system in the dust weight » non traité). **K3.1** : NOTE-207 §5 avertit que le couplage complet « pourrait réintroduire des pôles et toucher la classe à un seul exposant ». L'article dit seulement « whether ... preserve this distinction is not established ». Il faut ajouter que des pôles pourraient réapparaître.

---

## E4. Cohérence interne

- **Numérotation.** Prop. 1 à 5, Lemmes 1 et 2, Rem. 1 et 2, Déf. 1 : les renvois sont justes. La note compagnon renvoie bien à la « Remark 2 » et à la « Proposition 4 (a)(b)(c) ». Les colonnes du tableau HX correspondent bien aux conditions (a), (b), (c), que j'ai recalculées par l'équation indicielle α(α−3)+M2 = 0.
- **C4.1 (chapeau, Rem. 2(2) de l'article).** L'article écrit « T̂_{μν}[ψ;g] = Ω² T_{μν}[ψ̂;ĝ] ». Au §4.3, l'article définit T̂_ab = Ω^{-2}T_ab. Avec cette définition, la formule donnerait T = Ω⁴T[ψ̂;ĝ], ce qui est faux. La formule correcte en convention article est **T_{μν}[ψ;g] = Ω² T_{μν}[ψ̂;ĝ]**, sans chapeau à gauche. La note compagnon (chapeau côté physique) est, elle, correcte.
- **C4.2 (chapeau, Rem. 2(3) de l'article).** « a coupling ξR̂\|H\|² » désigne, en convention article, la courbure **non physique**. Il faut écrire ξR\|H\|². La v2.4 avait déjà cette coquille.
- **C4.3 (notation λ).** λ désigne la fonction de jauge (Déf. 1(b), Prop. 2) et la constante cosmologique (§3, Rem. 2(1)(3)) ; λ_h désigne de plus le couplage quartique. Il faut renommer la fonction de jauge (par exemple α ou ϑ).
- **C4.4 (notation H dans la note compagnon, §HX).** H est le doublet de Higgs et H le taux de Hubble dans la même phrase (« (λ = 3H²), with M2 = (m_h² + 12ξH²)/H² »). Il faut renommer H_dS ou Φ.
- **θ, U0, χ0±.** Les conventions sont cohérentes dans l'article : θ = ∫m dt, U0 = e^{-iβθ}, et −θ = (m/H)ln Ω sur de Sitter, ce qui est cohérent avec la v2.4. Prop. 2(c) avec λ = −θ donne bien e^{-iλ}u = (χ+, e^{2iθ}χ−) et A = e^{-1}dθ = −(m/eH)dΩ/Ω ; je l'ai vérifié. NOTE-207 utilise U0 = exp(iβθ) avec un θ de signe opposé. La note compagnon évite θ et écrit e^{-iβ(m/H)ln Ω}, ce qui est cohérent avec l'article. La note compagnon utilise χ0± sans les définir (voir E7).
- **C4.5 (Rem. 2 et Déf. 1(c)).** La Rem. 2 s'intitule « Formal regularity », mais son point (4) porte sur les sources évaluées sur des solutions (séries entières, bornées sans limite), alors que la Déf. 1(c) dit que la régularité formelle ne porte pas sur les solutions. Il faut dire que (4) est un énoncé « on solutions » (lien avec E3.1).
- **C4.6.** Les notions de la Déf. 1 sont en η, mais la Prop. 3 (« simple pole ») et la Prop. 4(c) (« smooth up to Ω = 0 ») sont en Ω. Sur de Sitter c'est équivalent ; sur FLRW général, Ω(η) peut ne pas être lisse en η. Il faut préciser la variable.

---

## E5. Note compagnon

**E5.1 (E) : résumé, « the fermion and W,Z mass coefficients are regular exactly when the rescaled Higgs is ».** Le §HX de la note compagnon dit lui-même que l'audit a restreint « the W,Z statement to sufficiency ». C'est vrai pour le fermion (yH_r est régulier si et seulement si H_r l'est, avec y ≠ 0), mais pour W,Z la quantité g\|H_r\| peut être régulière sans que H_r le soit (à cause de la phase). Correction : « the fermion mass coefficient is regular exactly when the rescaled Higgs is, and the W,Z masses are regular when it is ».

**E5.2 (C, surclassement) : §RJ, « so Friedrich's flow-adapted gauge does not transpose to it ».** NOTE-207 §5 range cette question parmi les choses « non faites » (« transposition de la jauge par géodésiques conformes à un flot de Dirac qui n'est pas géodésique ... : non fait »). La note compagnon transforme un « non fait » en résultat négatif. Correction : « ... so the transposition of Friedrich's flow-adapted gauge is not straightforward and has not been attempted ».

**C5.3 : numéros d'équations.** La note compagnon écrit « The other equations (2.13)–(2.16) have no negative power of Ω in this weight » ; les conventions renvoient à (2.13)–(2.17) de Friedrich 2015. NOTE-207 a établi ce résultat sur (3.3)–(3.7) de Friedrich 2017 (1601.04506). La correspondance entre les deux numérotations n'est ni dite ni vérifiée dans les pièces. Il faut citer les équations de Friedrich 2017 ou énoncer la correspondance.

**C5.4.** La note compagnon écrit « Checked exactly (sympy) ... and for a curved conformal metric ». D'après NOTE-207 §2, sympy a vérifié le cas de Minkowski avec des polynômes génériques ; la métrique courbe et les fonctions arbitraires relèvent de l'auditeur RA-2, sans méthode indiquée. Il faut écrire « confirmed by an auditor for ... ».

**K5.5.** « The spin-connection terms cancel in the symmetric part » ne figure pas dans NOTE-207, qui dit seulement « dérivé indépendamment par RA-1 depuis l'action avec connexion de spin ». L'énoncé est plausible, mais il faut une source dans les notes.

**K5.6.** Le tableau « Scripts and audit status » indique pour RJ « AU-V3 partial, fixed ». Il faut préciser si la v2 (rj_check_v2.py) a été réauditée ou seulement corrigée.

**Restrictions conservées :** « generic data » (HX : oui) ; « sufficiency for W,Z » (§HX : oui, résumé : non, voir E5.1) ; « non-abelian by weight counting only » (FW3 : oui, et §6 de l'article : oui) ; « premier étage » (RJ, Limits : oui sur le fond, sans le mot ; l'avertissement « pourrait réintroduire des pôles » manque, voir K3.1).

**Concordance avec NOTE-207 (seule note de chantier fournie parmi ED, HX, FW3, RJ).** P0 et P1 (rang 9 sur 10) concordent. Les composantes de τ (signe de τ_0a corrigé) concordent. Le tableau Fuchs concorde. La classe à un seul exposant analytique concorde, ainsi que l'affirmation qu'aucun V lisse ou indépendant de k ne rend les coefficients lisses. Pour ED, HX et FW3, je n'ai comme témoin que la Remarque de la v2.4. Le contenu de la note compagnon y est fidèle : identité T̂ = Ω²T, représentation lagrangienne en Ω^{-1} nulle modulo Dirac, condition m_h² + 4λξ = 2/3λ, coefficients de (2.17) en Ω^{-2} et Ω^{-1}, et sources jauge, quartique et Yukawa absentes des coefficients singuliers.

---

## E6. Pertes depuis la v2.4

**E6.1 (K, importante) : remarque ΛCDM du Lemme 2 supprimée.** La v2.4 disait que le couplage ajusté ℓ = m/(12H²) dans (m − ℓR)ψ̄ψ donne, sur ΛCDM, « an effective mass decaying like a^{-3} ». Or m_eff ∝ a^{-3} = Ω³ satisfie les **trois** conditions de la Prop. 4 (m = Ω·μ avec μ ∝ Ω², qui est lisse). C'est une issue explicite, ajustée mais réelle, à la conclusion de la Prop. 5(c). La v2.5 ne garde que « m_eff = 0 on de Sitter space », ce qui fait paraître l'issue plus étroite qu'elle n'est. Ce retrait n'est pas déclaré dans NOTE-212. Il faut rétablir la remarque, de préférence au §5.

**K6.2 : liste « non établi » de la v2.4.** Trois éléments ont disparu :
- « bare Majorana masses, **which remain singular** » : la v2.5 dit seulement « not treated », ce qui perd une information ;
- « the presence of Dirac quanta near scri » ;
- « a mechanism that would bring the Higgs to the symmetric point ».

Le dernier est en partie couvert par le §5 (« we do not construct or exclude »).

**K6.3 : section Verification.** Les réserves de la v2.4 ont été perdues : « the comparison printed alongside is taken at the same η and is only a consistency check » ; « χ0 in the β = +1 eigenspace up to O(10^{-8}) ».

**K6.4 : vérification numérique du facteur 1/(e^{2πm/H}+1).** La v2.4 la mentionnait (« to five digits »). Elle est remplacée par la seule citation de Boonpan ; on pourrait la garder comme contrôle indépendant.

**K6.5 : phrases de la v2.4 retirées.** Trois phrases utiles au lecteur ont été retirées :
- « Proposition 1 alone, being gauge dependent for such states, would not justify it » (§4.3) ;
- le résidu m_e/H∞ et « for a variable mass the relevant quantities are those of Proposition 4, not the instantaneous ratio m/H » (§ Orders of magnitude) ;
- « a rule formulated on other variables ... is not addressed » (§5), remplacée en partie par la discussion du poids poussière.

**K6.6 : historique.** La Provenance de la v2.4 détaillait ce que l'audit v2.1 avait trouvé faux (classe du Lemme trop large, Prop. 5(c) fausse en v2). La v2.5 résume « the corrections of a blind audit ». C'est acceptable, mais la traçabilité y perd.

---

## E7. Lisibilité pour un lecteur extérieur

1. **« one-particle projector P » (§4.3).** Avec f dans l'image de 1 − P et un nouveau projecteur P + \|f⟩⟨f\|, P est le projecteur des états **occupés** de la fonction à deux points (la mer de Dirac pour le vide), et non « le projecteur à une particule ». Il faut écrire « the projector P of the two-point function (occupied subspace) ».
2. **Fréquences.** La même phrase dit « modes of positive frequency as η → −∞ » et « characterisation by negative frequencies on the past boundary ». Les deux sont justes (DFMR §3.3 parle de la fonction à deux points), mais le lecteur y voit une contradiction. Une demi-phrase sur la convention suffit.
3. **Deux écritures du poids radiatif.** Le §4.3 écrit Ω^{-4}T_tt (repère orthonormé), la Prop. 5(b) écrit Ω^{-2}T_ab (composantes en (η, x)). Il faut rappeler l'équivalence dans la Prop. 5(b).
4. **Rem. 2.** Elle s'intitule « of the coupled systems » alors que (4) est un champ test. L'introduction annonce aussi « formal regularity of the coupled systems ».
5. **Note compagnon.** χ0±, « single-exponent », B, N et J sont utilisés sans rappel. Une ligne de renvoi à la Rem. 1 de l'article suffit.
6. **Saut logique au §5.** On passe de « what survives a change of weight is the interference » à « a matching rule that requires formal regularity ... distinguishes » sans dire que l'équation de Dirac reste singulière pour les deux classes (voir E3.1). Le lecteur risque de conclure que la classe à un seul exposant passe le raccord.
7. **Résumé (iii).** La phrase est dense : poids radiatif, poids poussière, interférence, quantique. On pourrait la scinder en deux.

---

## Liste des corrections à appliquer (ordre de priorité)

| # | Classe | Emplacement | Action |
|---|---|---|---|
| 1 | E | §5, Rem. 2(4), §4.3 | E3.1 : « régularité des sources géométriques » ; dire que l'équation de Dirac reste singulière pour les deux classes. |
| 2 | E | §5 | E3.2 : ajouter **k** ≠ 0. |
| 3 | E | §4.3 | E3.3 : interférence portée par τ_ab/Ω ; τ_0a ne l'a pas. |
| 4 | E | Compagnon, résumé | E5.1 : W,Z, suffisance seulement. |
| 5 | E | Résumé (i) | E1.4 : « on de Sitter space ». |
| 6 | E | après Prop. 4 | E1.3 : exemple Ω^{1/2} sur de Sitter. |
| 7 | E | Intro, Related work | E2.1 (GP via M-S), E2.2 (retirer Birrell-Davies de la phrase sur le facteur de paires). |
| 8 | E | §5, 1er paragraphe | E2.4 : Meissner-Penrose, sauf aux points de Hawking. |
| 9 | C | Intro | E2.3 : Markwell-Stevens. |
| 10 | C | §4.3 | C1.4 (Schwartz au lieu du support compact), C2.5, C2.6, E7.1, E7.2. |
| 11 | C | Rem. 2(2)(3) | C4.1, C4.2 (chapeaux). |
| 12 | C | Compagnon §RJ | E5.2, C5.3, C5.4. |
| 13 | K | §4.1 ou Related work | K2.1 (divergence avec Ibison). |
| 14 | K | §4.4 ou §5 | E6.1 (rétablir ΛCDM et a^{-3}). |
| 15 | C/K | divers | C1.1 à C1.6, C3.5, C4.3 à C4.6, K1.1, K3.1, K5.5, K5.6, K6.2 à K6.6, E1.1. |

## Non-surclassement de ce rapport

Ce rapport a été établi par un agent IA isolé et n'a été relu par aucun humain. Les sources externes ont été lues dans leur texte arXiv par outil. Je n'ai pas relancé les scripts (ils sont hors périmètre). L'argument de C1.4 (support compact et énergie positive) repose sur le cas de Minkowski et est seulement plausible pour Bunch-Davies en carte plate ; il n'est pas démontré ici. Les calculs de contrôle (exemples FLRW, signes de jauge, k = 0, τ_0a) sont élémentaires et ont été refaits à la main.

Sources consultées : arXiv 2202.10864, 2003.03356, 1009.5179, 2503.24263, 2212.06914, 1902.09144, 2610.00410, 1105.3767, hep-th/0109199, 1711.04011, 2107.06521 (via alphaXiv) ; [liste de publications de J.-P. Nicolas](https://jnicolas.pages.math.cnrs.fr/Publications.html), [Peeling of Dirac and Maxwell fields on a Schwarzschild background (arXiv:1101.4333)](https://ar5iv.org/html/1101.4333).
