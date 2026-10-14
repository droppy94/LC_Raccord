---
id: NOTE-BORD-EON-154-ARMEMENT-IR-ac-LECTURE-FNW-RADZIKOWSKI
numero: 154
serie: I
branche: Q-M3 suite (IR-ac, lecture)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 154)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 AVANT FETCH (questions, espace des verdicts et prediction figes avant toute lecture des sources)
decision: operateur (Thierry), 2026-10-13 12:53 heure de Paris (« traite les elements marques en priorite 1 », piste 2 de la reprise v2 §5.1)
depend: [NOTE-BORD-EON-145-ARMEMENT-IR-y, NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE, NOTE-BORD-EON-151-ACTE-GREFFES-ET-REVISION-G-V3]
issue_attendue: "lecture (levee ou maintien de la qualification Y-V2 de NOTE-146 v2)"
sources_declarees:
  - "(E1) S. A. Fulling, F. J. Narcowich, R. M. Wald, « Singularity structure of the two-point function in quantum field theory in curved spacetime, II », Annals of Physics 136 (1981) 243-272 (reference citee de memoire, a verifier EX-7). Article de revue, non disponible sur arXiv ; acces attendu difficile (Elsevier)."
  - "(E2) M. J. Radzikowski, « Micro-local approach to the Hadamard condition in quantum field theory on curved space-time », Communications in Mathematical Physics 179 (1996) 529-553 (reference citee de memoire, a verifier EX-7). Article de revue, non disponible sur arXiv ; acces attendu par Project Euclid (archives CMP en libre acces)."
  - "Repli declare (taux EX-8) si l'une des sources primaires est inaccessible : enonces lus dans une source secondaire de revue qui les cite avec hypotheses, parmi : I. Khavkine, V. Moretti, arXiv:1412.5945 (introduction aux etats Hadamard quasi-libres) ; K. Sanders, arXiv:0903.1021 (equivalence Hadamard / condition spectrale microlocale, et discussion de la preuve local-vers-global de Radzikowski). Tout enonce pris au repli est marque [extrait, secondaire]."
rouvre_si:
  - "audit froid de NOTE-155"
  - "acces ulterieur a une source primaire non lue ici"
---

# NOTE-154 : armement de IR-ac. Les enonces (E1) et (E2), cites de memoire dans IR-y, disent-ils ce que l'argument y-3 leur fait dire ?

## 0. Origine
NOTE-146 v2 (Y-V1 qualifie Y-V2, audite AU-V2) etablit que, pour un champ conforme, tout etat Hadamard sur l'eon est regulier en 𝓘⁺ dans le repere plat (w se prolonge en bisolution C^∞ jointe a travers η = 0). Dans la classe homogene, c'est calcule. Dans la classe generale (y-3), l'argument repose sur deux enonces exterieurs cites de memoire : (E1) la condition de Hadamard se propage depuis un voisinage d'une surface de Cauchy a tout le domaine de dependance [Fulling-Narcowich-Wald 1981] ; (E2) caracterisation microlocale de la condition de Hadamard, et equivalence local / global [Radzikowski 1996]. L'audit YA-1 (NOTE-150) a renforce l'argument (probleme de Cauchy des bisolutions, formule de Kirchhoff) et releve que la **positivite** de l'etat est necessaire au passage local-vers-global. La qualification Y-V2 tient a ces citations de memoire. Cette lecture vise a la lever ou a la preciser.

## 1. Cadre (fige)
- Ce que l'argument y-3 utilise exactement : soit Σ_ε = {η = −ε} une surface de Cauchy de Minkowski, et ω₂ la fonction a deux points d'un etat quasi-libre Hadamard sur le demi-espace {η < 0} (ouvert globalement hyperbolique de Minkowski contenant Σ_ε). On prolonge ω₂ a tout Minkowski par le probleme de Cauchy des bisolutions (donnees sur Σ_ε × Σ_ε). Il faut : (a) le prolongement est la fonction a deux points d'un etat (positivite conservee par le probleme de Cauchy, puisque la positivite se teste sur les donnees de Cauchy) ; (b) le prolongement est Hadamard sur tout Minkowski ; (c) donc w = ω₂ − H est C^∞ sur R⁴ × R⁴, en particulier a travers η = 0.
- (b) est le contenu attendu de (E1) : « Hadamard au voisinage d'une surface de Cauchy ⟹ Hadamard partout ». La version microlocale (E2) : WF(ω₂) = C⁺ (condition spectrale microlocale) equivaut a la forme de Hadamard globale ; et la propagation des singularites de Hormander pour □ donne (b) a partir de la forme locale au voisinage de Σ_ε, **sous reserve** du passage local-vers-global dont YA-1 dit qu'il requiert la positivite.
- Point de vigilance connu du souvenir de travail (a verifier a la lecture, taux EX-8) : la preuve de Radzikowski du theoreme « local Hadamard + positivite ⟹ global Hadamard » (ou de l'equivalence) a ete signalee comme incomplete et corrigee ou completee ulterieurement (Sanders 2010 ; Sahlmann-Verch). Si c'est le cas, le programme doit citer la version corrigee, non Radzikowski seul.
- Aucun calcul. Lecture seule (EX-9). Extraits empreintes dans `src\SOURCE-FNW1981-extraits.txt`, `src\SOURCE-Radzikowski1996-extraits.txt`, ou `src\SOURCE-<secondaire>-extraits.txt`.

## 2. Questions de lecture (figees)
- **ac-1 (enonce de (E1))** : quel est l'enonce precis du theoreme de propagation de FNW 1981 : hypotheses (espace-temps globalement hyperbolique ; champ de Klein-Gordon avec quel couplage ; etat quasi-libre ou bidistribution quelconque ; forme de Hadamard locale ou globale ; voisinage causal normal d'une surface de Cauchy) et conclusion (forme de Hadamard sur tout l'espace-temps, ou sur le domaine de dependance) ? L'enonce suppose-t-il la positivite de ω₂ ?
- **ac-2 (enonce de (E2))** : quel est l'enonce precis de Radzikowski 1996 : (i) equivalence entre forme de Hadamard globale et condition WF(ω₂) = C⁺ pour une bisolution satisfaisant la commutation (partie antisymetrique = iE) ; (ii) theoreme local-vers-global : hypotheses (positivite ?) et conclusion ; (iii) role de la propagation des singularites de Hormander et de l'axiome de tranche temporelle.
- **ac-3 (lacune)** : la preuve local-vers-global de Radzikowski est-elle complete selon la source elle-meme ou selon la litterature ulterieure accessible (Sanders 0903.1021 ; Khavkine-Moretti 1412.5945) ? Quelle est la version corrigee a citer, avec ses hypotheses (positivite requise ou non) ?
- **ac-4 (application a y-3)** : les enonces lus couvrent-ils le cas utilise : Minkowski entier, surface de Cauchy η = −ε, etat quasi-libre defini a priori sur le demi-espace seulement, prolongement par le probleme de Cauchy ? Y a-t-il une hypothese supplementaire (par exemple : l'etat doit etre defini sur un voisinage **ouvert** de la surface de Cauchy, satisfait ici ; ou Hadamard au sens global sur ce voisinage) que l'argument de NOTE-146 v2 / YA-1 doit expliciter ?
- **ac-5 (champs conformes)** : l'invariance conforme de la condition de Hadamard pour le scalaire a ξ = 1/6 (enonce (E3) de NOTE-145) est-elle dans l'une des sources lues ou dans le repli ? Sinon, reste citee de memoire (noter le taux).

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AC-V1** | (E1) et (E2) lus aux sources primaires ; les enonces couvrent l'usage y-3 sans hypothese supplementaire ; la positivite est soit requise et satisfaite (prolongement de Cauchy), soit non requise ; **Y-V2 levee** : NOTE-146 v2 passe a Y-V1 sans qualification (greffe v3 a proposer). |
| **AC-V2** | Enonces lus (primaires ou secondaires) et compatibles avec y-3, mais sous une hypothese ou une correction a expliciter (positivite ; version corrigee de la preuve local-vers-global : Sanders ou Sahlmann-Verch) ; **Y-V2 levee sous cette precision**, a porter en greffe v3 de NOTE-146 avec les references exactes. |
| **AC-V3** | Un enonce lu **differe** de l'usage qu'en fait y-3 (par exemple : propagation seulement sur le domaine de dependance futur, ou hypothese non satisfaite par l'etat du demi-espace) ; Y-V2 **maintenue** et l'argument y-3 a reformuler ; la classe « Γ[g] etat Hadamard » de G-V3 est a requalifier. |
| **AC-V4** | Sources primaires inaccessibles ; seul le repli secondaire lu ; les enonces y sont conformes a y-3 ; Y-V2 **maintenue avec taux** (enonces [extrait, secondaire]) et piste de lecture primaire conservee. |
| **AC-V0** | Questions mal posees (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**AC-V2, avec composante AC-V4 pour FNW 1981** (acces Elsevier improbable ; Radzikowski accessible par Project Euclid).
- ac-1 : FNW 1981 : pour un espace-temps globalement hyperbolique et le champ de Klein-Gordon (couplage general), si la fonction a deux points d'un etat quasi-libre est de forme de Hadamard (globale) dans un voisinage causal normal d'une surface de Cauchy, elle l'est partout ; l'enonce porte sur la bidistribution ; la positivite n'y est pas explicitement une hypothese du theoreme de propagation mais l'objet est une fonction a deux points d'etat.
- ac-2 : Radzikowski 1996 : (i) equivalence globale Hadamard ⟺ WF(ω₂) = C⁺ pour une bisolution a partie antisymetrique iE ; (ii) local-vers-global avec positivite ; (iii) propagation des singularites de Hormander centrale ; tranche temporelle via (i).
- ac-3 : la preuve local-vers-global de Radzikowski comporte une lacune signalee ulterieurement (Sanders 2010 ; Sahlmann-Verch 2001 pour le spin) ; la version corrigee exige la positivite (ou une hypothese equivalente) ; le programme devra citer Radzikowski **et** la correction.
- ac-4 : l'usage y-3 est couvert : voisinage ouvert de la surface de Cauchy, etat defini sur un ouvert globalement hyperbolique, prolongement de Cauchy positif ; hypothese a expliciter : le prolongement est bien l'etat quasi-libre de donnees de Cauchy identiques (fait par YA-1).
- ac-5 : (E3) non dans les sources lues ; reste cite de memoire.
- Consequence attendue : greffe v3 de NOTE-146 : Y-V1 sans qualification de lecture, avec references exactes et mention de la positivite ; libelle de G-V3 inchange (la classe « Γ[g] dans un etat Hadamard » tient).

## 5. Instruments prevus
Fetch (Project Euclid, Elsevier, alphaXiv pour les replis) ; extraits empreintes. Aucun script.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v3) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Aucune lecture des sources avant le scellement de cette note.
