---
id: NOTE-BORD-EON-155-IR-ac-LECTURE-FNW-RADZIKOWSKI
numero: 155
serie: I
branche: Q-M3 suite (IR-ac, lecture)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 155)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
version: 2
remplace: "v1, sha256 11b7c34f6424357ee1baeb3425e0f16606472e9408a2f987d2bf5fea6d95058b (conservee)"
greffe: "IR-ac entee le 2026-10-13 par NOTE-BORD-EON-162 (precisions de l'audit froid aveugle NOTE-161, AU-V2)"
audit: "NOTE-BORD-EON-160 (gel) / NOTE-BORD-EON-161 (concordance) : AU-V2 ; enonces releves verbatim par ACA-1, propagation sans positivite confirmee, lacune et attributions confirmees"
gel: NOTE-BORD-EON-154-ARMEMENT-IR-ac-LECTURE-FNW-RADZIKOWSKI (sha256 a90829a9fc544a1833bee3bf3df2289ecfc01a55eb112a11b66e1c96b01527c0, sceau 2026-10-13T11:02:23Z)
sources:
  - "Primaires (metadonnees EX-7 verifiees chez Springer, TEXTE NON LU) : Radzikowski CMP 179 (1996) 529-553 ; Radzikowski-Verch CMP 180 (1996) 1-22 ; Fulling-Sweeny-Wald CMP 63 (1978) 257-264. Non verifiee : Fulling-Narcowich-Wald Ann. Phys. 136 (1981) 243-272 (ScienceDirect refuse l'acces robot)."
  - "Secondaires lues (repli declare) : Khavkine-Moretti arXiv:1412.5945v3 (2015), pages 37-40, 45, 48-51, 57-59 ; Sanders arXiv:0903.1021v1 (2009), pages 1-11, 16, 18."
  - "Extraits et metadonnees : src/SOURCE-IR-ac-extraits.txt"
depend: [NOTE-BORD-EON-154-ARMEMENT-IR-ac-LECTURE-FNW-RADZIKOWSKI, NOTE-BORD-EON-146-IR-y-EXECUTION (v2), NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE]
verdict: "AC-V2 ⊕ AC-V4 : enonces confirmes avec hypotheses precises par une source secondaire de revue ; sources primaires inaccessibles"
prediction_realisee: "oui, avec deux corrections d'attribution (theoreme de propagation : Fulling-Sweeny-Wald 1978 ; comblement de la lacune : Sahlmann-Verch 2001 et Khavkine-Moretti 2015, non Sanders 2010)"
rouvre_si:
  - "audit froid"
  - "acces au texte de Radzikowski 1996 (p. 547-548, Theorem 5.1) ou de Radzikowski-Verch 1996 (Theorem 4.3, 9.2)"
---

# NOTE-155 : IR-ac (v2 : voir greffe). Les enonces (E1) et (E2) sont confirmes, avec leurs hypotheses exactes, par une source secondaire de revue ; la propagation microlocale ne requiert que la bisolution, la positivite n'entre qu'a l'equivalence avec la forme locale ; deux attributions de memoire sont corrigees. Verdict **AC-V2 ⊕ AC-V4**

> **Greffe IR-ac (v2, 2026-10-13).** Precisions issues de l'audit froid aveugle NOTE-161 (AU-V2 ; rapport ACA-1 92640de841c280e7…). Verdict AC-V2 ⊕ AC-V4 inchange.
> 1. [ajout IR-ac] **Chemin alternatif pour y-3** : Th. 9 (a) sur le demi-espace (etat, positivite consommee ici) → Rem. 23 sur R⁴ (propagation, sans positivite) → Sanders Lemma 2.9, dont la preuve n'utilise que les inclusions de fronts d'onde, avec partie antisymetrique commune iE/2 : w = ω₂ − ω₂^Mink est C^∞ sur R⁴ × R⁴. Ce chemin ne consomme la positivite qu'au depart ; le chemin du §0 (ac-4), par Th. 9 (b), la consomme a l'arrivee (prolongement de Cauchy positif). Les deux sont valides et se completent.
> 2. [ajout IR-ac] La preuve de Prop. 16 (b) n'etablit que l'**inclusion** WF(ω₂) ⊂ H ; l'egalite (forme de Hadamard au sens fort de Th. 9) vient, pour un champ libre, de l'hermiticite de ω₂ (positivite) par Sanders Prop. 2.8 et 3.2 (WF(ω₂) = WF(E) ∩ Γ₂, Corollary 3.3). Pour y-3 l'inclusion suffit (Lemma 2.9).
> 3. [corrige IR-ac] S1 attribue la propagation de la condition globale a [24] Fulling-Sweeny-Wald 1978 **et [70] Wald 1994** ; FNW 1981 [26] est cite pour les etats statiques et dans la liste [24, 26, 45] de Rem. 23. Le comblement de la lacune est aussi dans la these de Sanders 2008 (arXiv:0809.4828), outre Sahlmann-Verch 2001 et S1 (idee de Pinamonti).
> 4. [ajout IR-ac] Hypotheses a expliciter dans l'argument : existence et unicite du prolongement bisolution (formule ω₂ = S^t∘ω₂∘S de la preuve de Prop. 16) ; controle de la partie antisymetrique du prolongement (= iE/2 par construction) ; identification des cones H (S1) et Γ₂ (S2) et de la relation ∼ sur le demi-espace comme restriction de celle de R⁴ (geodesiques nulles du demi-espace = segments de celles de R⁴).
> 5. [ajout IR-ac] Acces : l'auditeur a obtenu un refus HTTP 429 de Springer pour Radzikowski 1996 et Radzikowski-Verch 1996 ; les metadonnees du §0 avaient ete obtenues avant ce refus ; statut inchange (non libres).

## 0. Resume
- **Acces** : Project Euclid (archives CMP) bloque l'acces par un dispositif anti-robot (Incapsula), rencontre avec WebFetch puis avec le navigateur integre ; il n'a pas ete contourne. Springer ne donne que l'apercu (articles non libres). ScienceDirect refuse l'acces robot. Les quatre sources primaires n'ont donc pas ete lues ; les metadonnees EX-7 de trois d'entre elles sont verifiees (Springer). Repli declare au gel : Khavkine-Moretti 1412.5945 (S1) et Sanders 0903.1021 (S2), lus.
- **ac-1 (E1)** [extrait, secondaire] : **correction d'attribution**. Le theoreme de propagation (« si la fonction a deux points a la structure de Hadamard au voisinage d'une surface de Cauchy, elle l'a partout ») est celui de **Fulling-Sweeny-Wald 1978** (CMP 63, resume Springer : « Cauchy evolution preserves the Hadamard singularity structure ») ; FNW 1981 en est la suite (« II »). S1, Remark 18 (4) : « An important feature of the global Hadamard condition for a quasifree Hadamard state is that it propagates [24, 70]: If it holds in a neighborhood of a Cauchy surface it holds in a neighborhood of any other Cauchy surface », [24] = FSW 1978. Version microlocale, S1 Proposition 16 (b) : si WF(ω₂|_{O×O}) a la forme de Hadamard sur un voisinage ouvert O d'une surface de Cauchy lisse de genre espace, alors WF(ω₂) a la forme de Hadamard sur tout M ; hypotheses : ω₂ ∈ D′(M × M) bisolution, M globalement hyperbolique de dimension ≥ 2 ; **aucune hypothese de positivite** (Remark 23 : il suffit meme que ω₂ satisfasse KG aux deux arguments a une fonction lisse pres). Preuve par le theoreme de composition des noyaux et les fronts d'onde des solutions fondamentales E± (S1, Proposition 15), c'est-a-dire par la propagation des singularites de Hormander.
- **ac-2 (E2)** [extrait, secondaire] : S1 Theorem 9 (« Radzikowski theorem ») : pour un etat ω (positif, pas necessairement quasi-libre) de Klein-Gordon (m², ξ quelconques, note 11) sur M globalement hyperbolique de dimension 4 : (i) ω Hadamard local (Def. 15) ⟺ (ii) WF(ω₂) = H (condition spectrale microlocale, eq. 76) ; (b) pour deux etats Hadamard, **ω₂ − ω′₂ ∈ C^∞(M × M)**. Preuve : (i) ⟹ global par Radzikowski-Verch Th. 9.2, global ⟹ (ii) par Radzikowski Th. 5.1 ; (ii) ⟹ global ⟹ local par Th. 5.1 ; (b) par Radzikowski-Verch Th. 4.3. La **positivite** entre ici, par l'objet « etat » (S2, Proposition 2.8 et 4.1 : c'est la positivite qui oriente les covecteurs du front d'onde, via la construction GNS ; Corollary 3.3 : pour un champ libre satisfaisant KG et les CCR, Hadamard generalise ⟺ Hadamard « by the result of Radzikowski »).
- **ac-3 (lacune)** [extrait, secondaire] : **confirmee, avec correction d'attribution**. S1 Remark 23 et note 12 : la preuve de Radzikowski Th. 5.1 (1 ⟹ 3) comporte une lacune (« The reasoning presented there cannot exclude elements of the form either (x₁, x₂, 0, p₂) or (x₁, x₂, p₁, 0) from WF(ω₂) outside N », p. 547), « previously explicitly identified and filled in the work of Sahlmann and Verch [61] » (Rev. Math. Phys. 13 (2001) 1203), et comblee a nouveau par S1 Proposition 16 (b) / Remark 23. **Sanders 2010 n'est pas la source du comblement** (S2 ne mentionne pas la lacune) : la citation de memoire de NOTE-154 §1 etait fausse sur ce point. Versions a citer : Radzikowski 1996 + Sahlmann-Verch 2001 (ou Khavkine-Moretti 2015, Prop. 16 et Rem. 23).
- **ac-4 (application a y-3)** [derive, sur enonces secondaires] : couverte, et plus simplement que prevu. Chaine : (1) l'etat quasi-libre Hadamard sur le demi-espace {η < 0} est Hadamard local (Def. 15) sur cet ouvert globalement hyperbolique, donc WF(ω₂) = H sur {η < 0} (Th. 9 (a), applique au demi-espace comme espace-temps) ; (2) le demi-espace est un voisinage ouvert O de la surface de Cauchy Σ_ε = {η = −ε} de Minkowski ; le prolongement de ω₂ par le probleme de Cauchy des bisolutions (YA-1, NOTE-150) est une bisolution sur R⁴ × R⁴ ; par **Prop. 16 (b)** (sans positivite), WF(ω₂) a la forme de Hadamard sur tout Minkowski ; (3) le prolongement est positif (positivite testee sur les donnees de Cauchy : meme forme symplectique, memes donnees), donc c'est un etat ; par **Th. 9 (a) (ii) ⟹ (i) et (b)**, ω₂ − ω^Mink₂ ∈ C^∞(R⁴ × R⁴) ; avec H = parametrix de Minkowski (Remark 18 (3) : le vide de Minkowski est Hadamard), **w est lisse jointement sur R⁴ × R⁴, en particulier a travers η = 0**. Hypothese a expliciter, comme prevu : le prolongement est l'etat quasi-libre de memes donnees de Cauchy (fait par YA-1) ; la positivite est requise a l'etape (3) seulement.
- **ac-5 (E3)** : l'invariance conforme de la condition de Hadamard a ξ = 1/6 n'apparait dans aucune des pages lues ; reste citee de memoire (taux EX-8).

## 1. Table de concordance (enonces de NOTE-145/146 v2 contre les sources lues)
| Enonce du programme | Source lue | Concordance | Hypotheses exactes |
|---|---|---|---|
| (E1) propagation depuis un voisinage d'une surface de Cauchy | S1 Rem. 18 (4) [FSW 1978] ; S1 Prop. 16 (b) (microlocal) | oui | bisolution (ou KG a lisse pres), M globalement hyperbolique ; **pas de positivite** |
| (E2) caracterisation microlocale, equivalence local/global | S1 Th. 9 [Radzikowski 1996 Th. 5.1 ; Radzikowski-Verch 1996 Th. 9.2, 4.3] | oui | **etat** (positif), dim 4, KG a m², ξ quelconques |
| difference de deux etats Hadamard lisse sur M × M | S1 Th. 9 (b) ; S2 Lemma 2.9, 4.6 | oui | etats Hadamard, meme commutateur |
| role de la positivite (YA-1) | S2 Prop. 2.8, 4.1 ; S1 Th. 9 | oui : oriente le front d'onde, passage local → global | |
| lacune de Radzikowski | S1 Rem. 23, note 12 | oui | comblee par Sahlmann-Verch 2001, Khavkine-Moretti 2015 ; **pas Sanders** |
| attribution de (E1) a FNW 1981 | S1 [24] vs [26] | **corrigee** : FSW 1978 ; FNW 1981 = suite | |
| (E3) invariance conforme | aucune page lue | non couverte | reste de memoire |
| (E4) propagation des singularites de Hormander | S1 Rem. 22, Prop. 15-16 | oui (instrument des preuves) | |

```
   argument y-3 reconstruit sur les enonces lus (S1 = Khavkine-Moretti)
   ------------------------------------------------------------------------------------
   etat Hadamard sur {eta < 0}      --Th.9(a)-->   WF(omega_2) = H sur {eta < 0}
   prolongement de Cauchy (bisolution) --Prop.16(b), sans positivite-->  WF = H sur R^4
   prolongement positif (donnees de Cauchy) --Th.9(a)(b)-->  omega_2 - omega_2^Mink lisse sur R^4 x R^4
   ==> w lisse a travers eta = 0 ; T-hat_Gamma ~ s^2 x lisse ; pas de pole   (Y-V1)
```

## 2. Lecture [derive]
1. **Y-V2 au niveau des enonces** : les deux enonces exterieurs sont confirmes, avec des hypotheses plus faibles que celles supposees (la propagation microlocale ne demande pas la positivite). L'argument y-3 tient tel que YA-1 l'a reconstruit, et la positivite y a exactement la place que YA-1 lui donnait : au passage de la forme microlocale a l'equivalence avec la forme locale et a la lissite de la difference.
2. **Y-V2 au niveau de la provenance** : les sources primaires ne sont pas lues ; S1 est une introduction de revue par deux specialistes, qui cite les theoremes avec numeros (Th. 5.1 de [57], Th. 4.3 et 9.2 de [58]) et en reprouve un (Prop. 16 (b)). Le taux EX-8 passe de « cite de memoire » a « [extrait, secondaire] avec numeros de theoremes ». C'est une levee partielle : AC-V2 pour la substance, AC-V4 pour la provenance.
3. **Deux corrections de memoire** a porter : (a) (E1) ↦ Fulling-Sweeny-Wald 1978 (FNW 1981 en complement) ; (b) comblement de la lacune ↦ Sahlmann-Verch 2001, Khavkine-Moretti 2015. La reserve de NOTE-154 §1 (« Sanders 2010 ») etait fausse dans son attribution, juste dans son existence.
4. **Rien ne change pour G-V3** : la classe « WZ integrable + Γ[g] dans un etat Hadamard » tient ; la qualification Y-V2 de NOTE-146 v2 peut etre reformulee (greffe v3 proposee, non entee) : « enonces (E1), (E2) confirmes par Khavkine-Moretti 2015 (Th. 9, Prop. 16, Rem. 23) et Sanders 2009 ; primaires non lues ; (E3) de memoire ».

## 3. Verdict
**AC-V2 ⊕ AC-V4.**
- **AC-V2** : enonces lus (secondaires) compatibles avec y-3 sous les precisions : positivite requise a l'equivalence local/global et a la lissite de la difference, non a la propagation ; version corrigee a citer (Sahlmann-Verch 2001 ; Khavkine-Moretti 2015) ; attribution de (E1) corrigee (FSW 1978).
- **AC-V4** : sources primaires inaccessibles (anti-robot, paywall) ; Y-V2 maintenue au titre de la provenance, avec taux reduit ; piste de lecture primaire conservee.

## 4. Confrontation a la prediction
Prediction (NOTE-154 §4 : AC-V2 avec composante AC-V4 pour FNW) : ac-1 [**realise** sur la substance ; **corrige** sur l'attribution : FSW 1978] ; ac-2 [**realise** : equivalence, local-vers-global avec positivite, Hormander central] ; ac-3 [**realise** sur l'existence de la lacune et le role de la positivite ; **corrige** sur l'attribution du comblement] ; ac-4 [**realise**, hypothese a expliciter = prolongement de Cauchy positif] ; ac-5 [**realise** : (E3) non couverte]. La composante AC-V4 est plus large que prevue (Radzikowski aussi inaccessible, par blocage anti-robot et non par paywall seul).

## 5. Consequences (rien n'est grave)
- Greffe v3 de NOTE-146 proposee (non entee) : reformulation de la qualification Y-V2 ; references exactes ; corrections (a), (b).
- NOTE-145 §1 et NOTE-154 §1 : attributions de memoire corrigees par la presente note (pas de version nouvelle : les gels ne se modifient pas).
- Libelle de G-V3 (NOTE-138 v3) : inchange.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 6. Pistes
- Lecture primaire de Radzikowski 1996 et Radzikowski-Verch 1996 si l'operateur dispose d'un acces (bibliotheque, Springer) ; depot des PDF sur D:\temporaire\src pour gel.
- Audit froid de NOTE-155 (lecture aveugle de S1 Th. 9, Prop. 16, Rem. 23).
- (E3) : lecture d'une source sur l'invariance conforme de la condition de Hadamard (Pinamonti 2009 ou Hack 2010, cites de memoire).

## 7. Non-surclassement
[conv], non audite. Enonces [extrait, secondaire] ; primaires non lues ; (E3) de memoire. G-V3 reste un candidat non grave.
