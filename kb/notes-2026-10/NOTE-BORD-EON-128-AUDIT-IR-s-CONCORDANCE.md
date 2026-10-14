---
id: NOTE-BORD-EON-128-AUDIT-IR-s-CONCORDANCE
numero: 128
serie: I
branche: Q-M3 suite (audit IR-s)
reservation: 2026-10-12T11:48 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 128)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-127-ARMEMENT-AUDIT-IR-s (sha256 b1bc0714c415e2dec8d09c443a0f5af3c9fb260562a439800359ea020769466f, sceau 2026-10-12T11:51:18Z)
rapport: RAPPORT-IR-s-AUDIT-AVEUGLE.md
depend: [NOTE-BORD-EON-127-ARMEMENT-AUDIT-IR-s, NOTE-BORD-EON-123-IR-q-EXECUTION, NOTE-BORD-EON-125-IR-r-EXECUTION, NOTE-BORD-EON-126-ACTE-DECISION-CONVENTION-LISSE]
verdict: "AU-V2 (NOTE-123 et NOTE-125) ; pole retrouve en cecite stricte (8bκ, signe selon la convention de T) ; C³ et ln Ť retrouves ; lecture fidele avec nuances"
prediction_realisee: "oui (AU-V2)"
hors_verdict: "partie a (Euler) de l'action anomale, calculee par S-b : sans contribution a R a l'ordre ε (premiere instruction de IR-t)"
rouvre_si:
  - "partie non locale Γ[g] de l'action effective (reference η + εh, b∫C ln(□/μ²)C) singuliere pres de scri+"
  - "modes homogenes de l'equation auxiliaire pour φ ; etat non conforme"
---

# NOTE-128 : audit froid aveugle de NOTE-123 et NOTE-125. Verdict **AU-V2**

## 0. Resume
- **Le pole de NOTE-125 est retrouve a l'aveugle.** S-a1, sans connaitre le resultat, trouve R_isj = −(8bκ/Ω) W_E,ij|𝓘⁺, porte par la seule donnee de rayonnement libre. La valeur absolue (8bκ) est identique ; le signe est oppose. S-b explique l'ecart : il tient a la convention de normalisation du tenseur, et l'existence du pole n'en depend pas. S-b reproduit tout, et montre que le pole resiste a la polarisation croix, a un k oblique, a une superposition de modes, aux diffeomorphismes lineaires et au changement de facteur conforme.
- **Hors verdict, resultat important.** S-b calcule la partie a (Euler) de l'action anomale sous sa forme de Wess-Zumino integrable : a l'ordre ε, elle se reduit a 6a ĝ, sans effet sur R. **Le pole n'est pas compense par la partie a.** Il reste a calculer la partie non locale (dependante de l'etat).
- **NOTE-123 tient.** S-a2 retrouve a l'aveugle f ~ τ⁴ ln τ, la classe C³ non C⁴, la radiation et le ln Ť. S-c juge la lecture fidele, sans contradiction frontale, avec des nuances a porter.
- Corrections mineures : convention de signe de c0 et de R-D ; etiquette G⁰₀ ; validite de l'absence de log restreinte a la couche ; consequence d'un pole pour W precisee (divergence logarithmique au premier ordre, g seulement C²) ; plusieurs nuances de lecture.

## 1. Concordance par resultat porteur

| Resultat | Re-derivation aveugle | S-b | Etat |
|---|---|---|---|
| R-1 T̂ sans trace, conserve, sans ln s sur couche | S-a1 : identique ; T̂_ij = −8b C_sisj (sa convention) | identique ; valide sous Bach = 0 ; log present hors couche | **concordant** (validite precisee) |
| R-2 pole (8bκ/Ω) w_ij | S-a1 : −(8bκ/Ω) W_E ; meme valeur absolue, signe oppose ; decomposition −12 + 4 | reproduit ; formule generale −c0 bκ W_E/Ω si Bach = 0 | **concordant, a convention de signe pres** |
| R-3 non-artefact | S-a1 : Stewart-Walker ; θΩ | jauge invariante ; θΩ ; polarisations, k oblique, superposition | **concordant, renforce** |
| Q-1 C³ non C⁴, W C⁰ non C¹ | S-a2 : identique, f explicite | identique (prolongement τ < 0 a preciser) | **concordant** |
| Q-2 radiation + ln Ť sans trace | S-a2 : identique (5 ln Ť) | identique (etiquette G⁰₀) | **concordant** |
| Q-3 lecture | | S-c : fidele, aucune contradiction frontale ; nuances (T3, T6, MP3, MP4, MP5, F1, I2) | **concordant, nuances** |

## 2. Corrections et precisions (greffes proposees, non entees)
**NOTE-125 (greffe IR-s-b)**
1. **Convention de signe.** Avec T_ab = (2/√g)δS/δg^{ab}, convention ecrite au gel NOTE-124 §1, c0 = +8 et le pole vaut **−(8bκ/Ω) w_ij**. Avec T^{ab} = (2/√−g)δS/δg_ab (Carroll, Wald), coherente avec ⟨T^a_a⟩ = bC² + … pour l'action +b∫σC², c0 = −8 et le pole vaut +(8bκ/Ω) w_ij. La valeur absolue et l'existence ne dependent pas de la convention. Le commentaire de la ligne 59 de irr_c.py est a corriger (script conserve, R-55).
2. **Generalite** : R_isj|pole = −c0 bκ W_E,ij/Ω des que Bach[g] = 0, pour toute polarisation, tout k, toute superposition (S-b). Forme exacte : T̂_ij = ∓8b Ω W_sisj (signe selon la convention). La donnee B porte la partie electrique, la donnee A la partie magnetique (Cotton du bord), qui ne donne pas de pole.
3. **Absence de log** : seulement sur couche (Bach = 0). Pour un h source par une matiere, T̂ contient s² ln s et R un ln s (S-b), sans changer le pole. Cela concorde avec l'ordre κ²b du cas (ii).
4. **Consequence sur W (§2.5-2.6)** : au premier ordre en bκ, W diverge logarithmiquement a 𝓘⁺ (W ≈ W₀(1 + c bκ ln Ω)), et la metrique-pont n'est que **C²** (modele f = τ³ ln τ, S-b). La forme resommee W ∝ Ω^γ et la classe C^{2,γ} restent **conjecturales**. La regularite de W exige W_E|𝓘⁺ = 0 (S-a1).
5. **Qualification R-V3 reduite** : la partie a ne contribue pas (S-b, hors verdict, a confirmer). Restent la partie non locale Γ[g] de la reference (b∫C ln(□/μ²)C, dependante de l'etat) et les modes homogenes de l'equation auxiliaire pour φ.

**NOTE-123 (greffe IR-s-a)**
6. T3 : ǧ = Ω̂⁻⁴ĝ est une consequence de (1) et (2) ; « non obtenue en prolongeant les equations conformes » est etiquete [derive].
7. T6 : les puissances demi-entieres n'apparaissent que dans les restes de la §7 de Tod, en Ť ; en τ̃ les series sont entieres.
8. MP3 : completer la citation (« – except at Hawking points such as H – »). MP4 : « fini a 𝓘⁺ » est [derive] ; la quantite conservee est l'integrale M (eq. 47). MP5 : l'epoque GW est proposee ; les masses (matiere noire) se desintegrent avant le raccord.
9. F1 : completer. La these de Friedrich est qu'un champ **massif** traverse aussi (m² = 2λ/3), et il juge « strong » l'exigence de seuls champs sans masse.
10. I2 : chez Friedrich, la lissite du prolongement est demontree dans les cas couverts ; le resume de Meissner et Penrose la presente comme decoulant de l'epoque GW, sans derivation dans le corps.
11. Ajouter les passages omis :
    - Tod : φ₂ = 0, « Delayed Rest Mass Hypothesis » ; « element of risk » ; trace non nulle au troisieme ordre ;
    - Meissner et Penrose, eq. 88-89 : exposant irrationnel au raccord, l'ansatz jugee inappropriee par les auteurs ;
    - Friedrich : le procede de blow-up n'a pas d'equations hyperboliques et est instable.
12. Script irq_diff.py : etiquette G_00 a lire G⁰₀ ; Q-B a lire avec un prolongement a τ < 0 (τ⁴ ln|τ|).

## 3. Verdict
**AU-V2** pour NOTE-123 et NOTE-125. Tous les resultats porteurs concordent : pole retrouve a l'aveugle a convention de signe pres ; non-artefact renforce ; C³ et ln Ť retrouves ; lecture fidele. Corrections mineures ; qualifications precisees.

## 4. Confrontation a la prediction
Prediction (NOTE-127 §5) : AU-V2.
- Pole retrouve, normalisation de b eventuellement differente (« facteur numerique ou signe ») : **realise** (signe).
- C³ et ln Ť retrouves : **realise**.
- Lecture fidele avec au moins une nuance, citant notamment « conformally smooth » chez Meissner et Penrose et les demi-entiers de Tod : **realise** (les deux nuances citees sont relevees par S-c).
- Reserve sur la dimension anormale : **realisee** et precisee (divergence logarithmique au premier ordre, forme resommee conjecturale).
- Non anticipe : la partie a calculee et sans effet ; la classe C² (et non C^{2,γ}) au premier ordre ; la tension F1 (Friedrich admet un champ massif a m² = 2λ/3).

## 5. Consequences (rien n'est grave)
- **G-V3 est consolide** comme candidat : le pole est retrouve a l'aveugle, robuste, et non compense par la partie a. Sous la convention lisse (NOTE-126), il suffit a lui seul a rendre (2.17) irregulier des qu'il y a du rayonnement gravitationnel a 𝓘⁺ et des champs quantiques conformes, avec ou sans C-M1. Derniere reserve majeure : la partie non locale dependante de l'etat.
- **M-V3** reste candidat, desormais secondaire par l'ordre : un log, contre un pole pour G-V3.
- **Tension avec Meissner et Penrose** : leur raccord est domine par les ondes gravitationnelles, et ce canal y est maximal. S-c releve qu'eux-memes trouvent un exposant irrationnel au raccord dans leur ansatz (eq. 88-89).
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 6. Pistes proposees (non engagees)
- **Entee des greffes** IR-s-a (NOTE-123 v2) et IR-s-b (NOTE-125 v2), par un acte.
- **IR-t** (reformulee) : acter le resultat de S-b sur la partie a (note d'execution et audit), puis instruire la partie non locale Γ[g] (b∫C ln(□/μ²)C) sur de Sitter pres de 𝓘⁺ : est-elle reguliere pour un etat de Bunch-Davies ?
- **IR-u** : equation de transport complete de W avec la source polaire ; dimension anormale exacte ; lecture de la litterature sur les perturbations tensorielles et l'anomalie de trace (EX-7, EX-8).

## 7. Non-surclassement
[conv]. Audit froid conduit (AU-V2). NOTE-123 et NOTE-125 restent [conv]. M-V3 et G-V3 sont des candidats non graves sous la convention lisse. Aucune promotion sans lecture exterieure.
