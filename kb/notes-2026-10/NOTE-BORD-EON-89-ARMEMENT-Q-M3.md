---
id: NOTE-BORD-EON-89-ARMEMENT-Q-M3
numero: 89
serie: I
branche: Q-M3 (chantier D / CCC + M)
reservation: 2026-10-09T16:27 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 89)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (espace des verdicts fige AVANT lecture de source et AVANT calcul)
depend: [S26-02-VERDICT-CHANTIER-D, S27-02-VERDICTS-M-ET-REPLI, REPRISE-AUTOPORTANTE-ROUTE-KAPPA-2026-08-24, ACTE-DECISION-RG4-LECTURE-STRICTE-2026-09-23]
issue_attendue: "delimitation"
rouvre_si:
  - "lecture d'une source traitant le systeme conforme de Friedrich avec une source a trace non nulle autre que le scalaire massif"
  - "objection exterieure sur S26-02 §2.3"
---

# NOTE-89 : armement du chantier Q-M3 (critere de regularite de la trace a 𝓘⁺)

## 0. Origine
S27-02 §A.4 nomme une tension non tranchee, Q-M3. Sous C-M1 (Higgs au point symetrique, m_h² = 2H∞²), l'electron devient sans masse, ne decouple plus, et l'anomalie (β/2e)F² revient. Deux questions ouvertes :
- **(a)** sous H-1, le canal de jauge revient a l'ordre Ω⁰ dans la trace rescalee du corpus ;
- **(b)** le critere de regularite lui-meme est a verifier : le corpus juge la trace par Ω⁻⁴·T (physique), Friedrich travaille avec T* = Ω⁻²·T et localise les singularites dans l'equation de Cotton (terme (m² − 2λ/3)Ω⁻¹). « Si le critere de Friedrich est le bon, une trace physique en Ω⁴ est inoffensive et (a) tombe. »

Q-M3 conditionne toute conclusion sur CCC + M (reprise du 2026-10-09, §4). Il ne touche pas la CCC dans sa forme actuelle (RG-4, electron massif).

## 1. Constat prealable, fait AVANT ce gel (transparence R-7)
En preparant l'armement, j'ai lu la reprise route κ du 24 aout, §2 (l. 42-50), qui ecrit la convention du corpus : `T^μ_ν = Ω⁻⁴ T̃^μ_ν`, **indices mixtes**, et precise elle-meme : « T_{μν} porterait Ω⁻², T^{μν} Ω⁻⁶ ». Le T* de Friedrich est ecrit en indices covariants. Il est donc possible que l'ecart « Ω⁻⁴ contre Ω⁻² » de S27-02 §A.4(b) soit une homonymie de position d'indice. **Ce constat oriente ma prediction (§5) ; il n'est ni calcule ni verifie a la source a l'heure du gel.**

## 2. Sous-questions gelees
- **Q-1 (identite des objets).** Le tenseur rescale du corpus (indices mixtes, poids Ω⁻⁴, convention g = Ω²g̃, g̃ physique) et le T* de Friedrich (covariant, poids Ω⁻²), une fois les deux ecrits dans la meme convention et la meme position d'indices, sont-ils le meme objet ? Meme question pour leurs traces prises avec la metrique rescalee.
- **Q-2 (ou Friedrich place l'obstruction).** Dans 1311.0700, quelle partie de la source produit les termes singuliers en Ω⁻¹ et Ω⁻² : la trace de T*, sa partie sans trace, ses derivees, ou la combinaison de la trace avec le terme de Λ ? A lire au texte (EX-9 : section citee lue jusqu'a la fin de la section suivante).
- **Q-3 (consequence pour (a)).** Avec le critere retenu a l'issue de Q-1 et Q-2, une trace rescalee d'ordre Ω⁰ (non nulle) au bord est-elle reguliere ou singuliere dans le systeme conforme ? Et l'anomalie (β/2e)F², qui est quantique, entre-t-elle dans le cadre classique de Friedrich ?

## 3. Espace des verdicts (fige)

### Sur (b), le critere
| Id | Enonce |
|---|---|
| **B-V1** | Meme objet : les deux ecritures coincident apres alignement des conventions et des indices. (b) tombe comme question de critere ; il ne reste qu'un critere. |
| **B-V2** | Objets distincts, critere de Friedrich PLUS FAIBLE : une trace rescalee d'ordre Ω⁰ y est inoffensive. (a) tombe, comme l'envisage S27-02. |
| **B-V3** | Objets distincts, critere de Friedrich PLUS FORT : il rend singuliere une trace que le comptage du corpus jugeait finie. |
| **B-V0** | Question mal posee pour une autre raison (a nommer). |

### Sur (a), le canal de jauge sous C-M1
| Id | Enonce |
|---|---|
| **A-V1** | Une trace rescalee d'ordre Ω⁰ non nulle est reguliere dans le systeme conforme lu : le canal de jauge n'est pas une obstruction. Q-M3 se resout en faveur de CCC + M sur ce point. |
| **A-V2** | Une trace rescalee d'ordre Ω⁰ non nulle produit des termes singuliers (Ω⁻¹ ou pire) : Q-M3 devient une incompatibilite candidate de C-M1 (candidat M-V3, a soumettre a lecture exterieure). |
| **A-V3** | Indecidable avec les sources lues : le cadre de Friedrich est classique, l'anomalie est quantique ; le transport du critere a une source anomale n'est pas fourni par la source. Q-M3 reste ouvert, deplace et precise. |
| **A-V4** | Question deplacee : sous C-M1, H-1 ou l'objet du canal change (a nommer), de sorte que la question (a) ne se pose plus sous la forme de S27-02. |

Composites permis (un verdict par axe). Tout verdict hors de cet espace est un resultat negatif sur le gel et se dit comme tel.

## 4. Objets externes vises (EX-7) et imports non lus (EX-8)
- **Vise** : H. Friedrich, « Smooth non-zero rest-mass evolution across time-like infinity », arXiv:1311.0700v2 (19 fevrier 2014), article original de recherche. Deja lu en S26 (resume, §1, §3, §4, debut §5) ; relecture ciblee du systeme d'equations et de l'origine des termes singuliers.
- **Imports non lus, ecrits en taux** : theoreme de basse energie de type SVZ (S26-02 §2.2, [M]) ; Friedrich 1991, systeme d'Einstein-Maxwell-Yang-Mills (regularite des sources conformes, [M], non vise ici).
- Corpus lu au texte pour ce gel : S26-02, S27-02, reprise route κ du 24 aout §1 a §5.1.

## 5. Prediction declaree (anti-fit)
**B-V1 ⊕ A-V3.** Conviction : l'ecart Ω⁻⁴ / Ω⁻² est une homonymie d'indices (§1) ; sur (a), la source classique ne tranchera pas une question d'anomalie quantique. Inclinaison secondaire, non engagee : si une trace classique d'ordre Ω⁰ entre dans le systeme de Friedrich, elle y produit plutot des termes en Ω⁻¹ (la singularite du scalaire massif semble venir de sa trace), ce qui pencherait vers A-V2 et non vers A-V1.

## 6. Instruments prevus
- Script `qm3_poids.py` (sympy) : alignement des conventions, abaissement d'indice avec la metrique rescalee, traces ; empreinte prise avant execution.
- Lecture alphaXiv de 1311.0700 (texte complet), avec citation des passages porteurs et texte elide joint (EX-9).

## 7. Non-surclassement
Ce gel ne tranche rien. RG-4 et son statut provisoire ne dependent pas de Q-M3 (electron massif). Noyau {A4 ; A2★ ; N} inchange, p_Q non fixe, N non chiffre, P2 et P3 non tranchees.
