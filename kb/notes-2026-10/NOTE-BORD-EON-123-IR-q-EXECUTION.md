---
id: NOTE-BORD-EON-123-IR-q-EXECUTION
numero: 123
serie: I
branche: Q-M3 suite (critere IR-q)
reservation: 2026-10-11T17:51 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 123)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-122-ARMEMENT-IR-q (sha256 d64d191cdc470b49e61c1da701351e3ae9fb77b6946ee3bfada7e4f9474201bb, sceau 2026-10-11T17:52:52Z)
sources:
  - "T : K. P. Tod, The equations of Conformal Cyclic Cosmology, arXiv:1309.7248v2 (2 fevrier 2015), GRG 47 (2015) 17 ; PDF local sha256 c990cd6456b6fd78 ; lu en entier (11 pages) ; texte SOURCE-1309.7248v2-texte.txt (c929b1006031ce44)"
  - "F : H. Friedrich, Smooth non-zero rest-mass evolution across time-like infinity, arXiv:1311.0700 (texte alphaXiv) ; §1 relu en entier, fin du §4 et debut du §5 ; §2-§4 lus en NOTE-90 ; texte SOURCE-1311.0700-texte-alphaxiv.txt (1a8a8b55e95201f7)"
  - "MP : K. A. Meissner, R. Penrose, The Physics of Conformal Cyclic Cosmology, arXiv:2503.24263v1 (31 mars 2025), prepublication ; PDF local sha256 1afdc73e9f4859b8 ; lus : resume, §I en entier, §II (region R, perturbation faible, lissite), §III (passages sur la conservation et l'isotropie locale), §VI.A ; texte SOURCE-2503.24263v1-texte.txt (cfaa6dae167aa9c8)"
instruments:
  - "irq_diff.py, sha256 750ccc53430be3eaafb8d07ac963d5f740cc27774159c948de25e2988aa10a21, 2026-10-11T17:55:19Z : EXIT 0, sortie irq_diff_sortie.txt (ba32eaa9fd169fb2)"
depend: [NOTE-BORD-EON-122-ARMEMENT-IR-q, NOTE-BORD-EON-90-Q-M3-EXECUTION, NOTE-BORD-EON-121-ACTE-GREFFE-IR-m]
verdict: "Q-V3 qualifie Q-V1"
prediction_realisee: "oui, avec un resultat supplementaire (§3.3)"
rouvre_si:
  - "texte de Penrose (Cycles of Time, appendice B ; EPAC 2006) fixant une classe de regularite finie du raccord, non lu ici (EX-8)"
  - "C. Lubbe, arXiv:1312.2059 ; E. T. Newman, arXiv:1309.7271 (autres equations de la CCC), non lus"
  - "decision de l'operateur sur la convention de regularite (§5)"
---

# NOTE-123 : IR-q. La CCC suppose un raccord lisse ; le log de (2.17) le rend C³. Verdict **Q-V3 qualifie Q-V1**

## 0. Resume
- **Ce que disent les sources.** Les formulations de la CCC lues supposent une structure conforme **lisse** au raccord (Tod : « assumed to be smooth » ; Meissner et Penrose : « it is an assumption of CCC that the conformal geometry is smooth along X »). Elles le posent comme **hypothese**, sans fixer de classe de differentiabilite ni discuter de termes logarithmiques. Friedrich, auteur du critere (2.17), ecrit au contraire que la transition d'une phase exponentielle a un Big Bang « peut s'attendre a s'accompagner de pertes de lissite » et que des exigences de lissite trop strictes peuvent empecher de la modeliser.
- **Ce que fait le log.** Un ln Ω dans le second membre de (2.17) ne casse pas le raccord. Il abaisse la regularite de la metrique-pont de C^∞ a **C³** (terme en Ω⁴ ln Ω), rend la courbure de Weyl rescalee W continue mais non C¹, et injecte dans l'eon suivant, selon la prescription de Tod, une **contrainte anisotrope sans trace en ln Ť a l'ordre Ť⁰**, deux ordres sous la radiation dominante.
- **Consequence.** Le critere (2.17) est la traduction fidele de la CCC **telle qu'enoncee** (lisse) : c'est la part Q-V1. Mais aucune source ne montre que la lissite soit physiquement necessaire, et l'auteur du critere en doute : c'est la part Q-V3. M-V3 doit donc se dire **« incompatibilite avec un raccord lisse »**, pas « incompatibilite avec le raccord ». Sous une convention de regularite finie (C³ ou polyhomogene admis), le canal anomal ne fait pas obstacle.

## 1. Extraits [extrait]
**T (Tod 2015)**
- T1 (§1) : « There is therefore a conformal metric common to consecutive aeons, which is assumed to be smooth ».
- T2 (§1) : les trois tenseurs de Weyl sont egaux et « the Bianchi identity forces all three to vanish at Σ (see Appendix B12 of [12]) ».
- T3 (§1) : hypothese reciproque Ω̌Ω̂ = −1, d'ou ǧ = Ω̂⁻⁴ĝ (eq. 2-3) : la metrique de l'eon suivant est **definie** par celle du precedent, et non obtenue en prolongeant les equations conformes.
- T4 (§1) : resultats de Friedrich invoques pour les sources a **tenseur sans trace** (Yang-Mills ; fluide de radiation par Lubbe et Valiente Kroon).
- T5 (§2) : developpement de Starobinsky g = dt² − e^{2Ht}(a + e^{−2Ht}b + e^{−3Ht}c + …), justifie par Rendall pour fluides parfaits, vide et Yang-Mills. Seules des puissances apparaissent ; aucun terme logarithmique n'est envisage.
- T6 (§6, §7) : « The results that we obtain are satisfactory to the first two orders in a post-bang time-coordinate ». Le developpement d'apres-Bang contient des puissances demi-entieres du temps propre (V = 1 + O(Ť^{3/2}), ȟ = Ť ǎ + Ť² b̌ + O(Ť^{5/2})).

**MP (Meissner et Penrose 2025)**
- MP1 (resume) : le raccord est « conformally smooth, except at a discrete set of points » (points de Hawking).
- MP2 (§I) : « the space-time geometry at crossover remains entirely classical though with a conformal, rather than the usual metric structure being smooth at crossover ».
- MP3 (§II) : « it is an assumption of CCC that the conformal geometry is smooth along X ».
- MP4 (§I, §III) : la lissite sert d'outil. La loi de conservation masse-energie « results from the assumed smoothness » ; « conformal smoothness across X implies an initial local isotropy ». La metrique physique g_ab « is certainly far from being smooth in the neighbourhood of X ». La quantite transportee est ψ̃ (Weyl rescale, poids −1), finie a 𝓘⁺ (Friedrich).
- MP5 (§VI.A) : l'approche du raccord est dominee par une epoque d'ondes gravitationnelles ; « The Einstein equations do not carry full information about this 'gravitational' epoch ». Les masses (matiere noire « erebons ») sont supposees se desintegrer en gravitons. Rien n'est dit des electrons ni du Higgs.

**F (Friedrich 2014/2015)**
- F1 (§1) : les champs a tenseur sans trace obeissant a des equations conformement covariantes traversent 𝓘⁺ (vide, Maxwell, Yang-Mills).
- F2 (§1) : prolonger les equations conformes de facon lisse au-dela de X donne une solution qui **se contracte**, et non un Big Bang. D'ou la prescription de Penrose et Tod, distincte de l'evolution conforme.
- F3 (§1) : « it can be expected that transitions from exponentially expanding to big bang phases are accompanied with losses of smoothness and that the insistence on too strict smoothness requirements may obstruct a modeling of such transitions ».
- F4 (th. 3.1) : regularite au sens « no terms of the form Ω⁻ᵏ … the right hand sides are in fact smooth function of the unknowns ». Un ln Ω viole la seconde clause.
- F5 (§5) : en homogene conformement plat, « (2.16), (2.17) are trivially satisfied » (concorde avec NOTE-90 §3.4).

## 2. Lecture [derive]
1. **q-1 (T)** : la lissite est une hypothese de definition (T1), pas un resultat. Tod n'envisage pas de termes logarithmiques (T5). Il juge la construction satisfaisante a deux ordres seulement (T6), et ses developpements d'apres-Bang sont deja non analytiques dans le temps propre. La regle de raccord (T3) agit sur la metrique-pont : celle-ci coincide, cote ancien eon, avec la metrique conforme de Friedrich. La regularite de (2.17) **est donc exactement ce qui garantit la lissite de la metrique-pont cote ancien eon**.
2. **q-2 (F)** : l'auteur du critere le presente comme une condition suffisante pour un prolongement lisse, et exprime un doute explicite sur la pertinence d'une lissite stricte pour la transition (F3). Il signale aussi que le prolongement conforme lisse ne produit pas de Big Bang (F2).
3. **q-3 (MP)** : lissite supposee (MP1 a MP3), utilisee pour la conservation et l'isotropie (MP4). Les auteurs s'ecartent du cadre des equations d'Einstein pres du raccord (MP5). Ils ne traitent pas les masses des fermions.

## 3. Calcul q-4 [calcule, irq_diff.py]
Modele : metrique-pont g = −dτ² + (δ_ij + ε d_ij f(τ)) dx^i dx^j, d = diag(1, 1, −2), Ω = τ au premier ordre, premier ordre en ε.

### 3.1 Coherence avec un ln dans R
Avec f = τ⁴ ln τ :
- Weyl electrique de g : (−3, −3, +6) ε (τ² ln τ + (7/12)τ²).
- W = C/Ω : en τ ln τ, tend vers 0 (donnee libre W₀ omise), continue.
- dW/dτ : (−3, −3, +6) ln τ + constantes, **non borne**.

C'est la signature d'un second membre R ~ ln Ω dans l'equation de Bianchi rescalee ∇·W = R. Un ln Ω dans (2.17) correspond donc a un terme Ω⁴ ln Ω dans la metrique-pont, au premier ordre et dans ce modele.

### 3.2 Regularite de la metrique-pont
Les derivees de f en τ = 0 sont 0, 0, 0 pour les ordres 1 a 3, puis −∞ a l'ordre 4. La metrique-pont est **C³ et non C⁴**, polyhomogene. Dans le developpement de Starobinsky de l'eon precedent, cela correspond a un terme t e^{−4Ht} absent de T5.

### 3.3 Eon suivant (prescription de Tod, Ω̌ ∝ τ, temps propre Ť = τ²/2)
- Fond : G_00 = −3/(4Ť²), G_ii = 1/(4Ť²). C'est la radiation de Tod (eq. 27, terme dominant 3/(4ť²)).
- Perturbation : G_00 sans terme d'ordre ε ; partie spatiale **sans trace**, proportionnelle a d, egale a ε d_ii (5 ln Ť + ln 32 + 9/2).
- Donc une contrainte anisotrope sans trace en **ln Ť a l'ordre Ť⁰** : finie relativement a la radiation (rapport ~ Ť² ln Ť), non analytique, et absente des deux ordres verifies par Tod (Ť⁻², Ť⁻¹).

### 3.4 Lecture
Le log ne produit ni divergence de W a 𝓘⁺, ni courbure de Weyl non nulle au Big Bang suivant (C = ΩW → 0, ce qui preserve T2 et l'hypothese de courbure de Weyl), ni matiere singuliere d'ordre dominant. Il produit une **perte de regularite**, de C^∞ a C³, et une contrainte anisotrope logarithmique sous-dominante.

C'est un obstacle d'une autre nature, et bien plus faible, que celui de l'electron massif qui fonde RG-4 (S26-02 §2.3). Dans ce cas, le champ rescale n'a pas de limite (phase exp(i(m/H) ln Ω)) et n'est meme pas continu.

```
                     regularite a travers scri+
   C^inf ──────── C^4 ──── C^3 ─────────── C^0 ──────────── pas de limite
     │                       │                                  │
   CCC telle qu'enoncee   canal anomal (ln dans 2.17)       electron massif
   (Tod, MP : hypothese)  M-V3 : viole C^inf, garde C^3      RG-4 (S26-02)
```

## 4. Verdict
**Q-V3 qualifie Q-V1.**
- **Q-V1 (part)** : la CCC telle que formulee par Tod et par Meissner et Penrose suppose une structure conforme lisse au raccord. La regularite de (2.17), cote ancien eon, est exactement la condition de lissite de la metrique-pont. Un ln Ω la viole. Le critere est donc fonde **relativement a l'enonce de la CCC**.
- **Q-V3 (qualification)** : aucune source ne fixe une classe de regularite finie ni ne montre que la lissite soit physiquement necessaire. L'auteur du critere juge plausible qu'elle soit trop stricte pour la transition. La CCC de Meissner et Penrose s'ecarte du cadre d'Einstein au raccord. Le log ne produit qu'une perte de regularite (C³) et une contrainte anisotrope logarithmique sous-dominante dans l'eon suivant. Le choix entre « lisse » et « differentiabilite finie » est une **convention a arbitrer**.

## 5. Consequences (rien n'est grave)
- **M-V3 reformule** : « incompatibilite du canal de jauge anomal (sous C-M1) avec un raccord **lisse** au sens de Tod et de Meissner et Penrose, pour un champ coherent generique ». Sous une convention C³ ou polyhomogene, il n'y a pas d'incompatibilite par ce canal ; il reste une signature : la contrainte anisotrope en ln Ť de l'eon suivant.
- **Decision operateur proposee (non prise)** : adopter pour le programme l'une des conventions suivantes.
  - (a) Lissite litterale (C^∞, fidelite a l'enonce) : M-V3 garde sa force de candidat.
  - (b) Regularite finie C^k, k ≥ 2 : M-V3 tombe comme incompatibilite ; le log devient une prediction de structure.
  - (c) Les deux, en parallele, avec double libelle.
- **RG-4 inchangee.** Sa base (electron massif, pas de limite du champ rescale) est d'une autre nature que le log de (2.17) ; aucune convention de regularite raisonnable ne la leve. A signaler au dossier de lecture exterieure : la qualification de NOTE-90 §5 (libelle de RG-4) reste pendante.
- **Lien avec IR-r** : le cadre « fond fixe » (de Sitter, Weyl-plat) masque un canal gravitationnel. Le terme φC² de l'anomalie peut produire un log au meme ordre des que le fond porte de la courbure de Weyl. Ce point est instruit en NOTE-124/125.

## 6. Passe adverse interne (ne vaut pas audit froid)
1. « Le modele de §3 n'est qu'une famille diagonale homogene. » Exact. Il montre la correspondance d'ordres (ln dans R ↔ Ω⁴ ln Ω dans g) et l'effet sur l'eon suivant ; il ne resout pas (2.17) pour une source inhomogene. La correspondance d'ordres est locale et ne depend que de la structure ∇·W = R.
2. « Tod suppose aussi Ω̌ = −1/Ω̂ exactement ; au premier ordre, Ω̌ ∝ τ. » Exact. Les corrections de φ (eq. 12, 14) modifient les constantes, pas l'ordre du log.
3. « Penrose (Cycles of Time, app. B) pourrait fixer une classe C^k. » Non lu (EX-8) : ce point est consigne dans rouvre_si.
4. « Le ln Ť de l'eon suivant pourrait etre exclu comme matiere non physique. » Ce serait un argument de convention de plus : Tod accepte deja une matiere d'apres-Bang non parfaite a l'ordre Ť⁻¹ (eq. 33).

## 7. Greffes proposees (non entees)
- **IR-q-a** : S27-02 et la reprise du 2026-10-11 : libeller M-V3 « incompatibilite avec un raccord lisse ».
- **IR-q-b** : registre des hypotheses de CCC + M : ajouter « convention de regularite du raccord (lisse / C^k) », decision operateur.
- **IR-q-c** : NOTE-90 : citer F3 (Friedrich lui-meme envisage des pertes de lissite).

## 8. Non-surclassement
[conv], non audite. Lecture de trois sources, calcul de premier ordre dans un modele diagonal. M-V3 reste un candidat non grave, desormais conditionnel a une convention nommee. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.
