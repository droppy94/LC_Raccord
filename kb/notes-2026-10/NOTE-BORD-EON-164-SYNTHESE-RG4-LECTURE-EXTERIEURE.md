---
id: NOTE-BORD-EON-164-SYNTHESE-RG4-LECTURE-EXTERIEURE
numero: 164
serie: I
branche: Chantier D (synthese RG-4 pour lecture exterieure)
reservation: 2026-10-13T13:20 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 164)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
nature: "PIECE D'APPAREIL : synthese autoportante de la regle RG-4 et de son declenchement (S26-01, S26-02, acte du 2026-09-23) destinee a un relecteur humain exterieur. Aucun calcul, aucune lecture nouvelle, aucune gravure."
decision: operateur (Thierry), 2026-10-13 15:16 heure de Paris (« je valide »)
depend: [S26-01-GEL-CHANTIER-D, S26-02-VERDICT-CHANTIER-D, ACTE-DECISION-RG4-LECTURE-STRICTE-2026-09-23, ACTE-ADOPTION-RG-ARRET-v2-2026-09-23, S27-02-VERDICTS-M-ET-REPLI]
destinataire: "relecteur humain exterieur (profil : cosmologie conforme cyclique, equations conformes de Friedrich) ; aucune connaissance prealable du programme supposee"
---

# Synthese de RG-4 : la masse de l'electron et le raccord conforme de la CCC

## 0. Ce que cette piece est

Le programme LC-RACCORD s'est dote, le 23 septembre 2026, de regles de refutation nommees RG-1 a RG-4, adoptees **avant** les calculs qui pouvaient les declencher. RG-4 porte sur la matiere massive au bord futur. Elle a ete declenchee le meme jour, **a titre provisoire** : la regle exige que le chantier « etablisse » le fait, et le programme considere qu'un resultat au grade [conv], non relu par un tiers, n'est pas etabli. La presente piece resume ce qui a ete fait, pour que ce tiers puisse lire la piece decisive (S26-02 §2.3) et dire si une objection emporte.

**Ce que nous demandons au relecteur** : (i) la derivation du §2.3 pour le spineur est-elle correcte ? (ii) la lecture du theoreme 3.1 de Friedrich (§2.2) est-elle fidele ? (iii) la regle RG-4, telle que lue strictement (§3), est-elle une regle raisonnable ?

---

## 1. La regle

**RG-4 (texte adopte le 2026-09-23)** : « La CCC est refutee dans sa forme actuelle si le chantier (D) etablit, dans le regime d'echelle retenu au bord, que la contribution de l'electron a la trace rescalee diverge a 𝓘⁺ (ordre Ω⁻¹ non reabsorbable) sans mecanisme d'effacement des masses. »

**Lecture stricte (acte du 2026-09-23)** : « sans mecanisme d'effacement des masses » s'entend « sans mecanisme physique connu et etabli ». Un postulat d'effacement, sans mecanisme, ne suffit pas a eviter la refutation. Motivation de l'operateur : « un postulat est une solution qui me semble etre une fausse solution en attendant une decouverte ».

---

## 2. Ce que le chantier (D) etablit (S26-02, verdict D-V2 ⊕ D-V0 partiel)

### 2.1 Une seule variable de controle : la masse rescalee diverge
Sous ĝ = Ω⁻²g (convention du programme : g physique ; chez Friedrich les chapeaux sont inverses, FW-6), toute grandeur de dimension inverse-longueur se rescale en X̂ = X/Ω. Donc **m̂ = m/Ω**, et non Ωm comme une lecture anterieure du programme l'avait suppose (candidat (iii), retire). Le rapport m/ω est invariant conforme ; pour le rayonnement qui atteint 𝓘⁺, ω → 0, donc m/ω → ∞ dans tous les cadres : la masse ne s'efface pas, elle domine. Controle independant : l'equation (3.5) de Friedrich fait apparaitre Ω⁻²m² dans l'equation rescalee.

### 2.2 Le vide decouple ; le scalaire ne traverse que pour une masse precise
- Dans le regime ω/m → 0, l'electron sort de la theorie effective : sa contribution de boucle a la trace est remplacee par un residu de dimension six, supprime en (ω/m)² (theoreme de basse energie de type SVVZ, cite de memoire, EX-8). **Le vide ne produit pas d'obstruction** ; la branche Ω⁰ de l'anomalie de jauge est remplacee par Ω⁺².
- **Source lue** : H. Friedrich, « Smooth non-zero rest-mass evolution across time-like infinity », arXiv:1311.0700v2, resume, §1, §3 (theoreme 3.1 et preuve), §4, debut du §5. Le theoreme 3.1 dit : les equations conformes couplees a un scalaire massif sont regulieres a 𝓘⁺ **si et seulement si m² = 2λ/3** ; sinon apparaissent des termes (m² − 2λ/3)Ω^(−k), k = 1, 2.
- **Lecture du programme** : en de Sitter R̂ = 4λ, donc 2λ/3 = R̂/6 : la masse de Friedrich est exactement celle qui rend le scalaire minimalement couple equivalent au scalaire conforme sans masse. Verification sur le mode homogene : le champ rescale se comporte en Ω^(1/2 ∓ μ), μ = √(9/4 − m²/H²), lisse seulement pour m² = 2H². Le theoreme ne montre donc pas qu'une masse generique traverse 𝓘⁺ ; il montre que le seul scalaire massif qui traverse est celui qui, au bord, ne se distingue pas d'un champ conforme. Friedrich lui-meme (§1) : « At present no process is known which would allow one to justify it » (l'effacement des masses).

### 2.3 Le spineur : aucune masse non nulle ne traverse (la piece decisive)
Derivation de seance (grade [conv], non auditee a l'aveugle, non relue) : pour un fermion de Dirac, aucun terme de courbure ne peut jouer le role que joue 2λ/3 pour le scalaire. Sur le mode homogene, le champ rescale (poids conforme 3/2) vaut ψ̂ = exp(i (m/H) ln Ω) : module 1, phase qui tourne sans fin ; sa derivee par rapport au temps conforme diverge en 1/τ ; **ψ̂ n'a pas de limite a 𝓘⁺**. Seul m = 0 donne un champ regulier. Avec m_e ≈ 5,1 × 10⁵ eV et H_∞ ≈ 1,2 × 10⁻³³ eV, la phase tourne d'environ 4 × 10³⁸ radians par facteur e de Ω.

**Passe adverse interne** (S26-02 §4, ne vaut pas audit) : les modes homogenes suffisent a exhiber la non-regularite (un contre-exemple suffit) et concordent avec le theoreme general de Friedrich pour le scalaire ; le poids 3/2 est celui qui rend l'operateur de Dirac sans masse covariant conforme, et avec un autre poids le terme de masse reste en m/Ω.

### 2.4 Ce que (D) n'etablit pas
Que l'obstruction prenne exactement la forme « trace rescalee en Ω⁻¹ » pour un gaz d'electrons (comptage du corpus, non refait au texte) ; ce qui arrive aux electrons avant 𝓘⁺ (annihilation, capture par des trous noirs qui s'evaporent : l'hypothese de Penrose, qui laisse en general des electrons isoles).

```
   bord futur, Omega -> 0
   -------------------------------------------------------------------------------
   boucles de l'electron (le vide)    : decouplent, residu Omega^+2        pas d'obstruction
   scalaire massif present dans l'etat : regulier ssi m^2 = 2 lambda/3     (Friedrich th. 3.1, lu)
   spineur massif present dans l'etat  : psi-hat = exp(i (m/H) ln Omega)  pas de limite, pour tout m != 0
   -------------------------------------------------------------------------------
   aucun mecanisme connu n'efface m_e  ==>  RG-4 declenchee (lecture stricte), a titre provisoire
```

---

## 3. Ce qui est refute, et ce qui ne l'est pas (acte du 2026-09-23)

**Refute, a titre provisoire** : la CCC dans sa forme actuelle, c'est-a-dire un raccord conforme regulier a 𝓘⁺ qui suppose le secteur matiere conforme au voisinage du bord sans mecanisme connu d'effacement des masses. Formule a employer : « la CCC exige une physique absente du Modele standard ; sous la regle adoptee, cette exigence non satisfaite la refute dans sa forme actuelle ».

**Non refute** : le cote Big Bang (A2★, RG-1), independant ; les resultats mathematiques du programme sur dS₄ et sa frontiere conforme (front β/O₂, fil s_max, branche PREMISSE) ; et **CCC + M**, hypothese nouvelle ou un mecanisme M rend nulle (et non seulement petite) la masse de tout fermion massif au voisinage de 𝓘⁺. Le programme note que M revient a une restauration de la symetrie electrofaible dans un univers froid et vide (condition C-M1 : Higgs au point symetrique, m_h² = 2H_∞², soit un changement de signe et environ 87 ordres de grandeur, S27-02), a contre-courant de la restauration thermique connue ; la classe candidate nommee est le Modele standard conforme (Meissner-Nicolai 2007), non integree. CCC + M est par ailleurs atteinte par le candidat G-V3 (synthese NOTE-163), qui ne depend pas de M.

**Pourquoi provisoire** : RG-4 exige que (D) « etablisse » ; S26-02 est au grade [conv], non lu par un tiers ; la partie spin 1/2 (§2.3) est une derivation de seance. La refutation passe au grade etabli apres une lecture exterieure de S26-02 §2.3 sans objection emportante ; elle tombe si une objection emporte.

---

## 4. Objections anticipees, et ce que le programme repond aujourd'hui

1. **« Penrose postule explicitement la perte des masses au bord ; refuter la CCC sur ce point, c'est refuser son postulat, pas sa theorie. »** C'est exactement l'alternative tranchee par la lecture stricte (§1). Le programme la nomme comme un choix de l'operateur, et distingue « CCC (forme actuelle) : refutee, provisoirement » de « CCC + M : hypothese ouverte ». Le relecteur peut recuser la lecture stricte ; il ne peut pas recuser le fait sous-jacent (§2.3) sans objection technique.
2. **« Les electrons auront disparu avant 𝓘⁺ (annihilation, trous noirs). »** Non etabli, et Penrose lui-meme reconnait des electrons isoles residuels ; un seul electron present dans l'etat suffit a l'argument du §2.3, qui porte sur la regularite du champ rescale, pas sur une densite.
3. **« Le mode homogene est trop particulier. »** Un contre-exemple suffit a la non-regularite ; pour le scalaire le resultat concorde avec le theoreme general de Friedrich.
4. **« Le poids conforme 3/2 est une convention. »** C'est le poids qui rend l'operateur de Dirac sans masse covariant conforme ; tout autre poids laisse le terme de masse en m/Ω (S26-02 §4.2).
5. **« Le theoreme de basse energie (decouplage du vide) n'est pas lu. »** Exact, declare [M] / EX-8 ; il ne porte que sur le vide, qui n'est pas la source de l'obstruction.
6. **« La trace rescalee en Ω⁻¹ n'est pas demontree pour un gaz. »** Exact (§2.4) ; l'obstruction du §2.3 est formulee sur le champ rescale, plus faible et plus sure que le comptage de trace.

---

## 5. Comment relire
Pieces a lire, dans l'ordre (une heure) : `ACTE-ADOPTION-RG-ARRET-v2-2026-09-23.md` (les regles) ; `S26-01-GEL-CHANTIER-D.md` (ce qui etait predit avant le calcul) ; `S26-02-VERDICT-CHANTIER-D.md`, en particulier §2.3 ; `ACTE-DECISION-RG4-LECTURE-STRICTE-2026-09-23.md`. Script : d_poids_conformes.py (empreinte dans l'en-tete de S26-02). Source : Friedrich arXiv:1311.0700v2. Sceaux : S26-01-SCEAU.txt, S26-03-SCEAU-CLOTURE.txt, SCEAU-ACTE-RG4.txt. Depot : D:\temporaire, Zenodo v2 et `github.com/droppy94/LC_Raccord` (a venir).

## 6. Non-surclassement
Cette piece compile ; elle ne grave rien. RG-4 est declenchee a titre provisoire ; la CCC n'est ni demontree ni refutee au grade etabli tant que la lecture exterieure n'a pas eu lieu. p_Q non fixe, N non chiffre, P2 et P3 non tranchees ; noyau {A4 ; A2★ ; N} inchange.
