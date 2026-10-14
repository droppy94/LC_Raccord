---
id: REPRISE-AUTOPORTANTE-2026-10-11-ETAT-CCC-ET-CANAL-ANOMAL
date: 2026-10-11
programme: LC-RACCORD
destination: projet « deux bords » (piece d'ouverture unique, remplace la reprise du 2026-10-09 comme point d'entree)
nature: PIECE DE PASSATION autoportante. Compile l'etat au 9 octobre (reprise precedente, resumee ici) et TOUT ce qui a ete produit du 9 au 11 octobre (NOTE-89 a NOTE-118). N'ajoute aucune substance, ne grave rien, ne tranche rien.
grade: "[conv]"
supersede_comme_entree: "01-REPRISE-AUTOPORTANTE-2026-10-09-ETAT-CCC.md (reste valide comme piece, ses §3 a §7 sont repris et condenses ici)"
premier_numero_libre: 119
---

# Reprise autoportante : etat de la CCC, de LC-RACCORD et du canal anomal de jauge au 11 octobre 2026

> Cette piece suffit pour reprendre le programme dans une discussion neuve du projet « deux bords ». Elle contient : la procedure d'ouverture (§0), l'etat de la CCC (§1), l'ambition et la methode du programme (§2), les acquis anterieurs condenses (§3), **tous les resultats des seances du 9 au 11 octobre** (§4), l'etat consolide (§5), les pistes suivantes (§6), les regles en vigueur (§7), l'emplacement des pieces (§8) et le cahier des charges de la presentation a produire en premier (§9).

---

## 0. Procedure d'ouverture (a suivre dans l'ordre)

### Etape 0 : verifications d'usage
1. Lire cette piece en entier.
2. Ouvrir `claude/REGISTRE-CENTRAL-NUMEROS-NOTES.md` (base du projet). Verifier que la derniere ligne emise est **118** et que **119 est libre**. En cas d'ecart, le registre fait foi (R-54) et l'ecart est signale avant toute ecriture.
3. Si la discussion est reliee a l'ordinateur de l'operateur, verifier sur `D:\temporaire` la presence et l'empreinte (sha256, 16 premiers caracteres) de quelques pieces de la table du §4.6, au minimum : NOTE-118 `17d0fd95a495d414`, NOTE-116 `8436e99a79bc0b3c`, NOTE-113 `f3031c13beee7144`, NOTE-108 v2 `f1c33b3dd60075fe`, registre `a7a703f52337ad2c`. Methode sure : `device_stage_files` puis sha256 sur la copie (ne jamais faire confiance a un depot sans re-staging, cf. §7.4).
4. Rappels a l'operateur, une fois : (a) **revoquer les jetons GitHub** colles en clair dans la discussion du 9 octobre et dans le LISEZMOI anterieur ; (b) verifier que les commits prepares dans `D:\ProjetsClaude\LCRaccord` (amendement `CLAUDE.md`, regle 5.4 bis) ont bien ete pousses sur `github.com/droppy94/LC_Raccord`.
5. Ne rien ecrire de substantiel avant d'avoir reserve un numero au registre (§7.3).

### Etape 1 : premiere production, la presentation illustree
Avant toute autre tache, produire la **presentation illustree** decrite au §9 : tout le programme, son ambition initiale, ses resultats, ce qui reste a faire, et sa place dans la cosmologie actuelle. **Chaque paragraphe en deux versions : texte scientifique, puis version vulgarisee.** Les faits sur la litterature exterieure (§9.4) doivent etre verifies par recherche web avant d'etre affirmes (EX-7, EX-8).

### Etape 2 : reprise du travail
Proposer a l'operateur les pistes du §6, dans l'ordre de priorite indique, sans en engager aucune sans son accord.

---

## 1. Statut de la CCC au 11 octobre 2026

| Forme | Statut | Piece qui le fixe |
|---|---|---|
| **CCC, forme actuelle** (raccord conforme regulier a 𝓘⁺, matiere supposee conforme au bord, sans effacement des masses) | **REFUTEE A TITRE PROVISOIRE** (RG-4 declenchee le 2026-09-23, lecture stricte). Passe a « etablie » apres une lecture exterieure de S26-02 §2.3 sans objection emportante. | `ACTE-DECISION-RG4-LECTURE-STRICTE-2026-09-23.md`, `S26-02-VERDICT-CHANTIER-D.md` |
| **CCC + M** (un mecanisme M annule la masse de tout fermion massif pres de 𝓘⁺ ; condition C-M1 : Higgs au point symetrique, electron sans masse) | **Hypothese ouverte.** Depuis le 9 octobre, une **condition supplementaire** pese sur elle : la regularite de l'equation (2.17) de Friedrich dans le canal anomal de jauge (§4). Un candidat d'incompatibilite **M-V3** est **renforce mais non grave**. | `S27-02-VERDICTS-M-ET-REPLI.md` ; NOTE-89 a NOTE-118 |
| **Repli acyclique** (bord conforme au seul Big Bang, type Tod) | Seule forme survivante sans physique nouvelle ; son sort depend de A2★, donc d'OA-2. | `S27-02` §B ; serie R |
| Resultats mathematiques (front β/O₂, fil s_max, branche PREMISSE) | Non touches par RG-4. | `ACTE-DECISION-RG4` §4 |

Formule imposee : « la CCC exige une physique absente du Modele standard ; sous la regle adoptee, cette exigence non satisfaite la refute dans sa forme actuelle ». Toujours distinguer « CCC (forme actuelle) : refutee, provisoirement » et « CCC + M : hypothese ouverte ».

Noyau irreductible **{A4 ; A2★ ; N}** : **inchange**. p_Q non fixe, N non chiffre, P2 et P3 non tranchees.

```
                 COTE BIG BANG                               COTE I+ (futur)
   ---------------------------------------    ------------------------------------------------
   Omega -> 0 : m~ = Omega.m -> 0               Omega -> 0 : m^ = m/Omega -> infini
   repli acyclique : electron inoffensif        electrons de l'etat : champ rescale non regulier
   reste : A2* (spikes BKL)                      ==> RG-4 declenchee (CCC forme actuelle)
   seul test refutant : OA-2 (RG-1)              CCC + M : electron sans masse (C-M1)
   ROMEO phase 0, 250 GPU.h                       ==> anomalie de trace QED revient
                                                  ==> canal anomal : ln Omega dans (2.17)
                                                      pour un champ coherent generique
                                                      (NOTE-98 a 118, candidat M-V3 renforce)
```

---

## 2. Le programme LC-RACCORD : ambition et methode

### 2.1 Ambition initiale
LC-RACCORD est un programme independant de physique theorique (operateur : Thierry, Paris) qui teste la **Cosmologie Conforme Cyclique (CCC)** de R. Penrose par **reduction des hypotheses** : au lieu de defendre ou d'attaquer la CCC en bloc, on isole une a une les hypotheses dont depend le raccord conforme entre la fin d'un eon (𝓘⁺, infini futur de genre espace) et le Big Bang de l'eon suivant, on les nomme, on les instruit separement et on reduit l'ensemble a un **noyau irreductible**. Outils : equations de champ conformes de Friedrich, geometrie de Sitter et sa frontiere conforme, theorie quantique des champs algebrique (AQFT), theorie modulaire de Tomita-Takesaki, cosmologie des singularites (BKL, spikes), anomalies de trace.

### 2.2 Methode (discipline epistemique)
- **Gel avant calcul** (R-7) : cadre, espace des verdicts et prediction anti-fit fixes et horodates **avant** toute algebre, lecture ou execution ; confrontation a la prediction ensuite.
- **Audits froids aveugles** par sous-agents frais (re-derivation en cecite stricte + audit de code), concordance ecrite.
- **Calibration** de chaque enonce : [extrait] (source lue), [derive] (raisonnement), [calcule] (sortie de script empreinte).
- **Pas d'actif fantome** (R-55) : tout script echoue est conserve avec sa sortie et son defaut nomme.
- **Registre central** des numeros ; **versions** des notes corrigees (v1 conservee, v2, v3 avec en-tete `remplace` et encadre de greffe).
- **Non-surclassement** : un resultat [conv] n'est jamais promu sans audit et lecture exterieure.

---

## 3. Acquis anterieurs au 9 octobre (condenses de la reprise du 2026-10-09)

1. **Front β/O₂** : le residu est **un** objet (chantier K) ; **Q n'existe que dans le secteur gaussien** (S25-03 : C_T = 0 impose) ; objet survivant **τ = κ + i C_T** sous τ → −1/τ, cloture negative = RG-3 ; chaine O-1 a lire dans l'ordre (la conclusion Q-V1 du 22 sept. est depassee). Fiche de l'irreductible v1.4.
2. **PREMISSE** : P1 (𝓘⁺ de genre espace) / P2 (asymptotiquement de Sitter), P2 ⟹ P1 ; **P2 n'est ni refutable ni etablissable par l'expansion seule** ; sept resultats durs dependent de P2 (dont la CCC) ; donnees w0wa contre ΛCDM a 2,7-3,5 σ au 23 sept. ; pince geometrique (hors P2, 𝓘⁺ n'est pas une infinite conforme reguliere).
3. **Chantier D (electron)** : variable de controle m/ω ; masse rescalee **m^ = m/Ω** ; scalaire regulier a 𝓘⁺ seulement si m² = 2λ/3 (Friedrich 1311.0700, th. 3.1) ; spineur : aucune masse non nulle reguliere ; **RG-4 declenchee** ; **CCC + M** : Higgs au point symetrique avec m_h² = 2H∞², changement de signe et 87 ordres de grandeur ; classe candidate pour M : Modele Standard Conforme (Meissner-Nicolai 2007), non integree.
4. **DSI** : log-periodicite = mode, pas symetrie (DSI-V1 ⊕ V3).
5. **A2★ (Big Bang)** : V3 OA-gated, quadruplement audite ; T-GAUSS T-V2, T-PERSIST P-V2, T-SPIKE S-V3 (S = K∘K, k = 2v + 1, correspondance avec Petersen 2609.20809) ; **OA-2** option (b), verdict borne V1-num ; **dossier ROMEO v5.1** : 250 GPU·h H100.
6. **Dossiers paralleles** : AQFT-CALOTTE (cinq impossibilites, statut des disciplines EX-11 a EX-13 a verifier), lecture spherique du raccord (no-go), lecture relationnelle (hors noyau).
7. **Fil s_max** : s_max/ln(ℓ/ℓ_UV) ∈ [1/6π, 1/4π].
8. **Regles du 23 sept.** : EX-7/8/9, RG v2 (RG-1 a RG-4), calendrier (bilan 30 juin 2027, arret en statu quo 31 dec. 2027 sauf mise a l'epreuve, deja realisee pour RG-4). Detail complet : reprise du 2026-10-09 §3 a §7.

---

## 4. Resultats des seances du 9 au 11 octobre 2026 (NOTE-89 a NOTE-118)

### 4.1 La question de depart : Q-M3
Sous C-M1 (electron sans masse), l'anomalie de trace QED revient pres de 𝓘⁺. Question : le systeme conforme de Friedrich reste-t-il regulier ? Equation pivot, **(2.17)** de Friedrich (arXiv:1311.0700v2) : R_ρνλ = 2Ω⁻¹ ∇̂_[ν L̂_λ]ρ, avec L̂ = (κ/2)(T̂ − ⅓ T̂ ĝ) (tenseur de type Schouten). Le terme a surveiller est un **ln Ω non borne** dans ce second membre.

### 4.2 Chaine des resultats (verdicts, toutes [conv])

| Notes | Objet | Verdict | Resultat porteur |
|---|---|---|---|
| 89/90 | Critere de regularite | **B-V0 ⊕ A-V3** | Le critere du corpus (Ω⁻⁴T bornee) n'est **pas** celui de Friedrich (absence structurelle de Ω⁻ᵏ dans le systeme en inconnues rescalees) et n'en est pas une condition necessaire. Q-M3 se deplace vers la **partie sans trace**, en Ω² ln Ω. Deux T* chez Friedrich (homonymie). |
| 91/92 (+ audit 93/94 AU-V2) | ln de (2.17), source inhomogene de trace imposee AΩ⁴ | **L-V4 qualifie L-V3** | Le ln est **force dans la source** ; (2.17) n'est regulier que pour un etat **asymptotiquement isotrope** (e₂ = A/3). |
| 95/96 | Isotropie de l'etat anomal (lecture) | **ISO-V3 qualifie ISO-V4** | Source S2 = Benevides, Dabholkar, Kobayashi, arXiv:1808.08237 (JHEP 11 (2018) 039) : couplage de Maxwell courant en ln a, I² = e⁻²[1 + 2β̃ ln(a/a⋆)] ; le vide de Bunch-Davies reste quantique (κ_k ~ 1/(2cos πβ̃)) donc isotrope ; le cas ouvert devient celui des **champs classiques coherents**. |
| 97/98 (+ audit 99/100 AU-V2) | Champ magnetique uniforme coherent | **CB-V2 qualifie CB-V3** | (2.17) porte un ln Ω de coefficients (−1, −1, +2)·κβ̃B₀²/e² ; la compensation exigerait un budget anisotrope exactement oppose. Audit : argument de symetrie valide sous H1-H5 ; point ouvert **OP-IR** (echelle infrarouge du terme non local). |
| 101/102 (v3 en vigueur) | OP-IR par un mode a k fini (a⋆ = k/M) | **IR-V1** (qualification reduite) | Le ln a persiste a k fini, coefficient 2β̃ ; la partie homogene reproduit NOTE-98 avec B₀² → ⟨B²⟩. Operateurs sur le mode libre : plat 0, Hodge 0, Bochner −4H². |
| 103/104 (v2 en vigueur) | Lecture de la ref. [21] de S2 | **OP-V1 qualifie OP-V3** | [21] = Bautista, Benevides, Dabholkar, arXiv:1711.00135 (JHEP06(2018)055), lu en entier : partie anomale **exacte** sur toute metrique Weyl-plate ; reste = **action plate du repere conforme** (aucun Ω) ; pas de terme en H² dans l'operateur ; residu de S2 d'ordre β² ; reserve : action plate valide seulement si F² ≪ ∇²F (u₀ ≪ k ; champ uniforme hors domaine). |
| 105/106 (v3 en vigueur) | Audit conjoint de 102 et 104 | **AU-V2** | Calculs concordants ; hypotheses nommees (champs charges conformes, vide conforme, prescription in-in) ; dependance a l'etat decouverte. |
| 107/108 (v2 en vigueur) | Etat a 𝓘⁺ d'un champ d'origine causale | **G-V0 qualifie G-V3** | **Loi** : le ln de (2.17) est porte par la partie sans trace de Q = ⟨B_iB_j − E_iE_j⟩ ; la trace (⟨F²⟩) n'y entre pas. Log de X^M = −2(T_B − T_E) (Poynting sans log). |
| 109 | Acte de greffe IR-d'' | acte | Versions v2 de 102, 104, 106. |
| 110/111 | Version inhomogene, dipole | **I-V1 qualifie I-V3** | Loi **locale** a l'ordre s⁰ (gradients en s ln s) ; dipole magnetique eteint a η = −D : boule r < D vide (pas de log), coquille rayonnee (structure 4/5), reliquat statique r > D (structure 1/5). |
| 112/113 | Audit froid de NOTE-108 | **AU-V3 partiel** | Loi confirmee et renforcee (tensorielle, retrouvee a l'aveugle) ; **enonce faux retire** : « survit pour tout champ coherent polarise » (contre-exemples : onde circulaire, onde helicoidale, faisceau non polarise, Q = 0). Prediction AU-V2 **non** realisee. |
| 114 | Acte de greffe IR-d''' | acte | NOTE-108 v2, 102 v3, 106 v3, 109 v2. |
| 115/116 | Quelles sources donnent Q_tf = 0 ? | **L-V1** | Formule exacte en fonction du courant sur couche ; seule la polarisation **lineaire** compte ; apres moyenne, seule la composante **E ℓ = 2** survit ; Q_tf = 0 en **codimension 5** (helicite pure, pas de E ℓ = 2, ensemble isotrope). Source causale generique : log present. |
| 117/118 | Test de H-loc par la completion de Riegert | **K-V1 qualifie K-V3** | Le tenseur de la partie (b) de Riegert = derivees **plates** de ψ (□_η²ψ = −J), sans φ, sans log, sans pole, aveugle a la polarisation ; la loi se retrouve avec le seul secteur Maxwell : **H-loc est inutile pour le log**. |

### 4.3 Formules a retenir (cadre S2 + [21], premier ordre en β̃, convention s = −τ = Ω, H = 1)
- Action simplifiee : S = −¼∫ I² F_μν F^μν (indices par η), I² = e⁻²[1 + 2β̃(λ − ln s)], λ = ln(M/k).
- Equation de mode : (I²u_s)_s + k²I²u = 0 ; pres de 𝓘⁺ : u = u₀cos(ks) + (c/k)sin(ks) + β̃u₁ ; branche magnetique gelee (X ∝ I²), branche electrique (I²u_s conserve, X ∝ 1/I²).
- Log du secteur Maxwell (ordre s²) : X^M|_ln = −2β̃ ln s · (T_B − T_E) ; Poynting sans log ; divergence exacte sur couche ∇^μX^M_μν = −¼∂_ν(I²)F², sans log.
- **Loi tensorielle** (partie homogene ou point par point) :
  **R_isj |_{β̃ ln s, s⁰} = (3β̃κ/e²) (Q_ij − ⅓δ_ij tr Q)**, Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺ ; en τ le signe change.
- **Critere** : ln Ω present dans (2.17) **si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf** a 𝓘⁺.
- Source eteinte (courant J, J± = Ĵ(±k)) : Q_k = −½ L(J₊J₊† + J₋J₋†) − ½ Re(J₊·J₋*)(δ − k̂k̂) ; L = polarisation lineaire ; le second terme oscille en cos(2kt₀).
- Dipole magnetique : ⟨ε_Bε_B − ε_Eε_E⟩ = (4/5)(mm − ⅓m²) ; ⟨L⟩ = −(2/5)(mm − ⅓m²).
- Riegert partie (b) (famille diagonale) : T_x = −(1/6)∂_s⁴ψ + (1/6)∂_s²∂_x²ψ ; T_y = T_z = −(1/6)∂_s⁴ψ − (1/6)∂_x⁴ψ + (1/3)∂_s²∂_x²ψ.

### 4.4 Table « ln dans (2.17) ? »

| Configuration a 𝓘⁺ | Q_tf | ln dans (2.17) |
|---|---|---|
| Vide de Bunch-Davies, ensemble isotrope | 0 | non |
| Champ magnetique coherent (uniforme ou reliquat statique) | ≠ 0 | oui |
| Dipole lineaire ou tournant rayonne | ≠ 0 | oui |
| Onde progressive lineaire ou elliptique | ≠ 0 | oui |
| Onde progressive circulaire, dipole chiral, onde helicoidale a Q = 0 | 0 | non |
| Faisceau non polarise | 0 | non |
| Source causale generique (dipoles + quadrupole) | ≠ 0 | **oui** |

### 4.5 Hypotheses sous lesquelles tout cela vaut
Cadre S2 + [21] : metrique exactement Weyl-plate (de Sitter fixe), champs charges **conformement couples et sans masse**, **vide conforme**, prescription **causale in-in** ; **premier ordre en β̃** (non uniforme quand β̃ ln(1/s) ~ 1, sauf branche magnetique ou le log est exact dans l'action simplifiee) ; action plate dans son domaine (champ rapidement variable, u₀ ≪ k) ; completion covariante de la classe « Riegert + partie invariante de Weyl a tenseur plat lisse » ; variation de la partie invariante de Weyl **hors orbite** non calculee (S2 note 4) ; famille de metriques testee diagonale ; et **le choix de (2.17) comme critere de regularite pertinent pour CCC + M**.

### 4.6 Pieces produites (versions en vigueur, empreintes sha256 tronquees a 16)
Toutes deposees dans `D:\temporaire` (machine de l'operateur), avec sceaux `NOTE-nnn-SCEAU*.txt`, scripts et sorties.

| Note | Fichier (version en vigueur) | sha256 |
|---|---|---|
| 89 | NOTE-BORD-EON-89-ARMEMENT-Q-M3.md | 6b8cfacda331cb14 |
| 90 | NOTE-BORD-EON-90-Q-M3-EXECUTION.md | 51a9aa3c746a252e |
| 91 | NOTE-BORD-EON-91-ARMEMENT-Q-M3-LOG.md | 9bdb1d59c6bf3e09 |
| 92 | NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION.md | 0f10849922ecc718 |
| 93 | NOTE-BORD-EON-93-ARMEMENT-AUDIT-FROID-Q-M3.md | b2673a078f203d87 |
| 94 | NOTE-BORD-EON-94-AUDIT-FROID-Q-M3-CONCORDANCE.md | 831ba9c2058b9188 |
| 95 | NOTE-BORD-EON-95-ARMEMENT-ISOTROPIE-ETAT-ANOMAL.md | 69b0e7c7d268b75c |
| 96 | NOTE-BORD-EON-96-ISOTROPIE-ETAT-ANOMAL-EXECUTION.md | f05e4429fade024f |
| 97 | NOTE-BORD-EON-97-ARMEMENT-CHAMP-COHERENT.md | 510f9c6fabadf311 |
| 98 | NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION.md | 9d56285a646e65f0 |
| 99 | NOTE-BORD-EON-99-ARMEMENT-AUDIT-CHAMP-COHERENT.md | 58b35dce573141e4 |
| 100 | NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE.md | 849cb0fc82514dae |
| 101 | NOTE-BORD-EON-101-ARMEMENT-OP-IR.md | e4c36854d2d29bb4 |
| 102 | NOTE-BORD-EON-102-OP-IR-EXECUTION-**v3**.md (v1 ea774ca5…, v2 4bc0b729… conservees) | 7339dcd22c936f02 |
| 103 | NOTE-BORD-EON-103-ARMEMENT-IR-a.md | 7b8e9ac5ea638fcc |
| 104 | NOTE-BORD-EON-104-IR-a-LECTURE-REF21-**v2**.md (v1 95df64c4… conservee) | 47b25752fb16efdb |
| 105 | NOTE-BORD-EON-105-ARMEMENT-AUDIT-OP-IR.md | 3b4b2fcdfae713e5 |
| 106 | NOTE-BORD-EON-106-AUDIT-OP-IR-CONCORDANCE-**v3**.md (v1 d89e75b2…, v2 1e4ec783… conservees) | 76bdcc81c390850c |
| 107 | NOTE-BORD-EON-107-ARMEMENT-IR-g.md | 7bc4705105dd05a5 |
| 108 | NOTE-BORD-EON-108-IR-g-EXECUTION-**v2**.md (v1 925cf153… conservee, suspendue en partie) | f1c33b3dd60075fe |
| 109 | NOTE-BORD-EON-109-ACTE-GREFFE-IR-d2-**v2**.md (v1 872b9b27… conservee) | 183081ec2743d0b9 |
| 110 | NOTE-BORD-EON-110-ARMEMENT-IR-i.md | e44b4f05a5a374ba |
| 111 | NOTE-BORD-EON-111-IR-i-EXECUTION.md | 7f8597f1edf6be3b |
| 112 | NOTE-BORD-EON-112-ARMEMENT-AUDIT-IR-g.md | 43986f6fdd483136 |
| 113 | NOTE-BORD-EON-113-AUDIT-IR-g-CONCORDANCE.md | f3031c13beee7144 |
| 114 | NOTE-BORD-EON-114-ACTE-GREFFE-IR-d3.md | d6aa6bf4d8ab7227 |
| 115 | NOTE-BORD-EON-115-ARMEMENT-IR-l.md | 7ed4cd22f2b9db99 |
| 116 | NOTE-BORD-EON-116-IR-l-EXECUTION.md | 8436e99a79bc0b3c |
| 117 | NOTE-BORD-EON-117-ARMEMENT-IR-k.md | e4e862322e80a456 |
| 118 | NOTE-BORD-EON-118-IR-k-EXECUTION.md | 17d0fd95a495d414 |

Rapports d'audit : `RAPPORT-CSE-Q-M3-AUDIT-AVEUGLE.md` (94), `RAPPORT-CSE-CHAMP-COHERENT-AUDIT-AVEUGLE.md` (100), `RAPPORT-OP-IR-AUDIT-AVEUGLE-Da-Db.md` (106), `RAPPORT-IR-g-AUDIT-AVEUGLE-Ja-Jb.md` (113) ; scripts des auditeurs dans `D:\temporaire\audit_op_ir\` et `D:\temporaire\audit_ir_g\`. Source lue sauvegardee : `SOURCE-arXiv-1711.00135v1-texte.txt` (b89ca1f03e41e1d9).

Scripts de reference (tous conserves avec leurs versions echouees, R-55) : qm3_poids v1-v3 ; q_m3_log v1-v5 ; cb_coherent v1-v3 ; op_ir v1, op_ir_v2, op_ir_v2_ctrl ; ctrl_etat ; ir_g ; ir_i ; ir_l v1 (interrompue), ir_l_v2 ; ir_k, ir_k_affichage, ir_k_ctrl.

Registre central : version `a7a703f52337ad2c` (sur D:\temporaire et dans la base du projet), **premier numero libre 119**.

---

## 5. Etat consolide (une phrase par niveau)
- **Scientifique** : dans le cadre S2 + [21] et sous les hypotheses du §4.5, le second membre de l'equation (2.17) de Friedrich porte, pres de 𝓘⁺, un terme en ln Ω de coefficient (3β̃κ/e²)(Q_ij − ⅓δ_ij trQ), present des que la partie sans trace de ⟨B_iB_j − E_iE_j⟩ ne s'annule pas, ce qui est le cas generique pour un champ electromagnetique coherent issu d'une source causale ; aucune completion covariante de la classe consideree ne le compense.
- **En clair** : si l'univers futur garde, tout au bout, un champ electromagnetique « organise » (pas du simple bruit isotrope), alors l'effet quantique des electrons devenus sans masse laisse une petite trace qui grandit sans limite au raccord : la condition de raccord lisse de Penrose est violee, sauf reglage special du champ.
- **Statut** : candidat M-V3 renforce, non grave ; aucune promotion sans l'audit IR-m et une lecture exterieure.

---

## 6. Prochaines pistes (consignees, aucune engagee)

### 6.1 Priorite 1 : verrouiller la chaine qui renforce M-V3
| Id | Objet | Pourquoi | Note de depart |
|---|---|---|---|
| **IR-m** | Audit froid aveugle conjoint de NOTE-111, NOTE-116 et NOTE-118 | Ce sont les trois maillons non audites qui portent M-V3 | 111, 116, 118 |
| **IR-n** | Riegert partie (b) pour des perturbations metriques generales (h_0μ, hors diagonale) | Leve la 2e qualification de K-V3 | 118 §3 |
| **IR-o** | Variation hors orbite de Weyl de la partie invariante de Weyl (S_flat covariantise) | Leve la 1re qualification de K-V3 | 118 §3, 104 |
| **IR-e** | Action plate en regime de champ quasi constant (Euler-Heisenberg sans masse) | Seule voie pour k → 0 (champ uniforme hors domaine de [21]) | 104 §4.3 |
| **IR-h** | Lire Prokopec, Tornkvist, Woodard (2002) pour delimiter l'hypothese « champs charges conformes » (masse de photon ∝ H en QED scalaire minimale, cite de memoire par l'auditeur D-b, non lu) | Hypothese porteuse du cadre | 106 |
| **IR-p** (nouvelle) | Au-dela du premier ordre en β̃ (non-uniformite pres de 𝓘⁺) | Le premier ordre cesse d'etre fiable quand β̃ ln(1/s) ~ 1 | 102 §3, 106 |
| **IR-q** (nouvelle) | Le critere : (2.17) est-il bien la condition de regularite pertinente pour CCC + M (lien a Friedrich th. 3.1, a Tod, a la forme exacte du raccord) ? | Toute la chaine en depend | 90 |

### 6.2 Priorite 2 : decisions et lectures exterieures
- Lecture exterieure de S26-02 §2.3 (RG-4 provisoire → etablie ou tombe) ; libelle de RG-4 a amender (Q-M3-c : le declencheur est ecrit dans le critere du corpus, qui n'est pas celui de Friedrich).
- Depot Zenodo v2 (acte RG-4, S27, ROMEO v5, et la chaine 89-118).
- OA-2 phase 0 sur ROMEO (RG-1, seul test refutant de la forme survivante).

### 6.3 Greffes proposees, non entees (a soumettre a l'operateur)
| Id | Objet | Origine |
|---|---|---|
| Q-M3-a | En-tete de la table des ordres : « comptage de trace ; pas le critere de Friedrich » | 90 |
| Q-M3-b | S27-02 §A.4(b) : (a) deplacee vers la partie sans trace | 90 |
| Q-M3-c | RG-4 : reecrire le declencheur en regularite du champ rescale | 90 |
| Q-M3-d | Registre d'homonymie : deux T* chez Friedrich | 90 |
| Q-M3-e | NOTE-92 : famille reguliere plus large ; « independante de k » a l'ordre dominant seulement | 94 |
| ISO-a | Homonymie Ω (S2 : ln a ; corpus : 1/a) | 96 |
| ISO-b | Specification de CCC + M (S27-02 §C) : ajouter (v) « contenu electromagnetique a 𝓘⁺ sans partie sans trace de ⟨B_iB_j − E_iE_j⟩ » (formulation mise a jour par NOTE-113/114 ; la v1 de ISO-b disait « quantique statistiquement isotrope ») | 96, 114 |
| CB-a | NOTE-98 : restreindre « secteur non Maxwell isotrope » a H1 ; ajouter H2-H5 ; « ne change pas la dependance en ln a » seulement avec echelle comobile | 100 |
| CB-b | Realisee par NOTE-101/102 (a marquer comme entee) | 100 |
| Correction NOTE-111 | Lier NOTE-111 a NOTE-118 : H-loc levee pour le log | 118 §4 |
| Anterieures | K-1..K-6, A-1..A-5 (DSI), C4bis, C4 clause C, A-1..A-6 (V1.d), S25-a..d, S26-a..d, B-1..B-6 (OA-2) | reprise du 2026-10-09 §6 |

### 6.4 Ouvert de plus longue date (reprise du 2026-10-09 §4)
Objet τ = κ + i C_T sous ℓ → iℓ (RG-3) ; suites T-SPIKE ; statut des disciplines EX-11 a EX-13 ; versement de la branche Higgs (Modele Standard Conforme) comme classe candidate pour M.

---

## 7. Regles en vigueur

### 7.1 Discipline
R-7 (geler avant fetch, algebre ou run, gel horodate et scelle avant execution) ; R-36 ; R-41 (au moins 3 miroirs pour une source) ; R-53 ; R-54 (les tetes font foi) ; R-55 (pas d'actif fantome) ; EX-7 (declarer titre, auteurs, date, type avant verdict) ; EX-8 (import non lu ecrit en taux) ; EX-9 (lire jusqu'a la fin de la section suivante ; joindre le texte elide) ; §6.4 non-surclassement ; d1 relier ≠ ancrer ; d2 pas de back-fit ; d3 proxy non transportable.

### 7.2 RG v2 et precedence
RG-1 (OA-2, refutante), RG-2 (non refutante), RG-3 (cloture negative de τ), RG-4 (declenchee, provisoire). Regle 5.4 bis (decision du 9 oct., portee dans `CLAUDE.md` du depot) : les regles posterieures au 23 sept. prevalent ; l'interdit « ne jamais conclure sur la CCC » est remplace par la distinction forme actuelle / CCC + M.

### 7.3 Numerotation
Un seul compteur ; **reserver la ligne au registre AVANT d'ecrire** (gel et execution reservent deux numeros). Premier libre : **119**. Les versions corrigees gardent leur numero (suffixe -v2, -v3) et sont tracees au registre.

### 7.4 Flux de depot (machine de l'operateur)
- Ecrire dans le conteneur, copier vers `/mnt/user-data/outputs/<dossier unique>/`, deposer avec `device_commit_files` vers `D:\temporaire\`, puis **re-stager et recalculer le sha256** : un depot a partir d'un chemin deja utilise peut servir un contenu perime.
- Registre : mettre a jour sur `D:\temporaire\REGISTRE-CENTRAL-NUMEROS-NOTES.md` **et** dans la base du projet (`claude/REGISTRE-CENTRAL-NUMEROS-NOTES.md`, via `project_write` avec `local_path`).
- Pas de barre verticale « | » dans le texte d'une cellule du registre (casse le tableau).
- **Livraison a l'operateur : toujours par piece jointe telechargeable** (SendUserFile) ; la base du projet ne sert qu'a la persistance.

### 7.5 Redaction
Francais ; pas de tirets longs ni de tropes d'IA ; illustrer chaque fois que c'est utile (tableaux, schemas) ; sur les sujets debattus, analyse factuelle d'abord.

---

## 8. Ou sont les pieces
| Emplacement | Contenu |
|---|---|
| `D:\temporaire\` | Toutes les notes 89 a 118 (toutes versions), sceaux, scripts et sorties, rapports d'audit, registre courant |
| Base du projet « deux bords » | Registre courant ; reprises ; noyau verse le 9 oct. (S22 a S27, actes du 23 sept., ROMEO v5.1, NOTE-55 a 88, etc.) |
| `D:\ProjetsClaude\LCRaccord` | Copie locale du depot `droppy94/LC_Raccord` (amendement `CLAUDE.md`, regle 5.4 bis ; bundle git et `RESTAURER-GIT.cmd`) ; push a confirmer |
| `D:\temporaire\PACKAGE-LC-RACCORD\` | Package du 6 aout (corpus anterieur, references PDF) |
| Zenodo DOI 10.5281/zenodo.22919751 | v1 (S25, S26, sans acte RG-4) |
| Introuvables | NOTE-BORD-EON-01 a 05, SYNTHESE-BORD-EON |

---

## 9. Cahier des charges de la presentation illustree (Etape 1)

### 9.1 Forme
- **Support** : presentation de diapositives, faite avec l'outil Artifact (type « Slides » s'il est liste ; sinon un fichier .pptx). Livree en piece jointe ou en lien d'artifact.
- **Chaque diapositive** comporte : un titre ; un bloc **« Version scientifique »** (precis, avec les equations et le vocabulaire du domaine) ; un bloc **« En clair »** (meme contenu en vulgarisation, sans formule, avec une image mentale ou une analogie) ; une **illustration** (schema, diagramme, tableau, frise). Les deux blocs disent la meme chose ; le second ne simplifie pas au point de fausser.
- Ton : sobre, sans tirets longs, sans tropes d'IA. Chaque affirmation sur un resultat du programme renvoie a sa note (numero). Chaque affirmation sur la litterature exterieure est verifiee par recherche web et citee (§9.4).
- Environ 22 a 28 diapositives.

### 9.2 Plan impose
1. **Titre** : « LC-RACCORD : tester la cosmologie conforme cyclique par reduction des hypotheses ».
2. **La CCC en une image** : eons, 𝓘⁺ d'un eon recolle au Big Bang du suivant ; rescaling conforme ĝ = Ω⁻²g. Illustration : diagramme de Penrose de deux eons.
3. **Pourquoi la CCC interesse** : entropie, fleche du temps, condition de faible courbure de Weyl, absence de masse au bout du temps.
4. **L'ambition du programme** : ne pas croire ni rejeter, mais nommer chaque hypothese et la tester ; le noyau irreductible {A4 ; A2★ ; N}. Illustration : arbre des hypotheses.
5. **La methode** : gel avant calcul, prediction anti-fit, audits froids aveugles, calibration [extrait]/[derive]/[calcule], registre. Illustration : chaine gel → calcul → confrontation → audit.
6. **Les outils** : equations conformes de Friedrich, de Sitter et sa frontiere, AQFT et theorie modulaire, singularites BKL et spikes, anomalies de trace.
7. **Cote Big Bang : A2★** (spikes, T-GAUSS, T-PERSIST, T-SPIKE, Petersen) et **OA-2** (le seul test refutant, ROMEO 250 GPU·h). Illustration : carte des spikes.
8. **Cote futur : la premisse P1/P2** (𝓘⁺ de genre espace, asymptotiquement de Sitter) et l'etat des donnees (DESI). Illustration : courbes a(t) et horizon.
9. **Le front β/O₂** : Q n'existe que dans le secteur gaussien ; l'objet survivant τ = κ + i C_T.
10. **Le probleme de l'electron (chantier D)** : m^ = m/Ω, Friedrich th. 3.1, spineur jamais regulier. Illustration : masse rescalee qui explose vers 𝓘⁺.
11. **RG-4 : la CCC sous sa forme actuelle est refutee a titre provisoire.** Ce que cela veut dire et ne veut pas dire.
12. **CCC + M** : effacer les masses (Higgs au point symetrique, 87 ordres de grandeur ; Modele Standard Conforme comme classe candidate).
13. **Le prix de C-M1 : l'anomalie de trace revient** (Q-M3, NOTE-89/90). Illustration : deux criteres de regularite differents.
14. **Le ln force dans la source et la condition d'isotropie** (NOTE-92, 94).
15. **L'etat quantique reste isotrope, le champ coherent non** (NOTE-96, S2).
16. **Le champ magnetique coherent et le ln Ω** (NOTE-98, 100). Illustration : motif (−1, −1, +2).
17. **L'echelle infrarouge et la lecture de [21]** (NOTE-102, 104, 106). Illustration : trois operateurs (plat, Hodge, Bochner).
18. **La loi : 3β̃κ/e² × partie sans trace de ⟨B_iB_j − E_iE_j⟩** (NOTE-108, 113, 114). Illustration : table du §4.4.
19. **La carte d'un dipole eteint** (NOTE-111). Illustration : boule vide, coquille rayonnee, reliquat statique (§ schema de NOTE-111).
20. **Quelles sources echappent au log ?** (NOTE-116) : polarisation lineaire, composante E ℓ = 2, codimension 5, dipole chiral. Illustration : motifs de polarisation sur la sphere.
21. **Riegert ne compense pas** (NOTE-118). Illustration : decomposition du tenseur (§ schema de NOTE-118).
22. **Etat consolide** : candidat M-V3 renforce, hypotheses du §4.5, rien de grave.
23. **Ce qu'il reste a faire** : §6 (IR-m, IR-n, IR-o, IR-e, IR-h, IR-p, IR-q ; RG-4 exterieure ; OA-2 ; Zenodo v2).
24. **Le programme dans le panorama de la cosmologie actuelle** (voir §9.4) : 2 ou 3 diapositives.
25. **Conclusion** : ce que le programme a deja appris, quel que soit le sort de la CCC.

### 9.3 Exigences de fond
- Ne rien surclasser : employer « refutee a titre provisoire », « candidat non grave », « [conv] ».
- Distinguer clairement ce qui est **etabli dans le programme** (avec audit) de ce qui est **conditionnel**.
- Les versions vulgarisees peuvent s'inspirer du manuscrit de vulgarisation du programme (projet « Le raccord ») mais doivent rester fideles aux notes.

### 9.4 Panorama de la cosmologie actuelle : points a verifier par recherche web avant d'affirmer (EX-7, EX-8)
Liste de pistes, **non verifiees dans cette piece** (souvenirs de travail, a confirmer et dater) :
- CCC : R. Penrose, *Cycles of Time* (2010) ; cercles concentriques dans le CMB (Gurzadyan et Penrose, 2010) et leurs refutations statistiques (Wehus et Eriksen ; Moss, Scott et Zibin ; Hajian, 2010-2011) ; « points de Hawking » (An, Meissner, Nurowski, Penrose, 2018-2020) et critiques (par ex. Jow et Scott, 2020) ; travaux de K. P. Tod sur la singularite isotrope et les equations de la CCC ; Meissner et Penrose (2025, cite au corpus : arXiv:2503.24263).
- Cadre mathematique : equations de champ conformes de H. Friedrich ; stabilite de de Sitter ; singularites BKL et spikes (Berger, Moncrief, Lim, Uggla) ; Petersen (2026, arXiv:2609.20809, cite au corpus).
- Contexte observationnel : DESI DR2 et l'energie noire evolutive (2025) ; tensions de ΛCDM (H0) ; contraintes Planck.
- Cosmologies concurrentes : inflation (paradigme dominant), rebond (bounce), ekpyrotique et cyclique de Steinhardt-Turok, cosmologie quantique a boucles, scenarios de type « univers-miroir ».
- Anomalies de trace et magnetogenese primordiale : Dolgov (1993), Benevides-Dabholkar-Kobayashi (2018), Bautista-Benevides-Dabholkar (2018).
Pour chaque point retenu : titre, auteurs, date, type (EX-7), au moins une source primaire ; ce qui n'est pas verifie est ecrit au conditionnel ou retire.

---

## 10. Non-surclassement
Cette piece compile ; elle ne grave rien. CCC (forme actuelle) : refutee a titre provisoire (RG-4). CCC + M : hypothese ouverte, chargee d'une condition de regularite du canal anomal et d'un candidat M-V3 renforce mais non grave. Repli acyclique suspendu a A2★. Noyau {A4 ; A2★ ; N} inchange ; p_Q non fixe ; N non chiffre ; P2 et P3 non tranchees.
