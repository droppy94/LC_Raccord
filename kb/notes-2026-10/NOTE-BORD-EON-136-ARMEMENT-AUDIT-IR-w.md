---
id: NOTE-BORD-EON-136-ARMEMENT-AUDIT-IR-w
numero: 136
serie: I
branche: Q-M3 suite (IR-w, audit)
reservation: 2026-10-12T12:50 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 136)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (consignes aveugles, criteres de concordance, espace des verdicts et prediction figes AVANT le lancement des auditeurs)
decision: operateur (Thierry), 2026-10-12 14:49 heure de Paris
objet: [NOTE-BORD-EON-131-IR-t-EXECUTION, NOTE-BORD-EON-133-IR-u-EXECUTION, NOTE-BORD-EON-135-IR-v-EXECUTION]
consignes:
  - "PROMPT-AVEUGLE-Wa-NORMALISATION-SIGNE.md, sha256 97e9d6d86441590340a3ef6b2cf62fa379885a65fd246f61641b306357e25832"
  - "PROMPT-AVEUGLE-Wb-LECTURE-SOURCES.md, sha256 5bd7a1a5c9749645c196eed6f604874c5ac9ca305c6046a9f8395678ee63855c"
  - "PROMPT-AVEUGLE-Wc-AUDIT-131.md, sha256 ae094de5faea30c107b07f769f1e46c162e6d95d541aa857616e7a3991b04825"
issue_attendue: "consolidation ou correction"
---

# NOTE-136 : armement de l'audit froid aveugle IR-w (NOTE-131, 133, 135)

## 0. Origine
La chaine G-V3 repose maintenant sur une conversion : γ = 8 (NOTE-133, convention de calcul c₀ = +8), coefficient egal a celui de Foraci-Litos-Woodard et exposant resomme egal a celui de Woodard 2025 (NOTE-135), sous les hypotheses κ = 8πG, b = coefficient de C² dans la trace (normalisation HHR) et signe physique Carroll-Wald (croissance du Weyl). Ni la normalisation du terme local bσC² par rapport a la trace, ni le signe physique n'ont ete etablis par une chaine independante.

## 1. Dispositif (fige)
Trois auditeurs independants, lances en parallele, chacun dans un dossier isole, sans acces aux notes 123 a 135 ni au registre :
- **W-a** (priorite) : recalcul de bout en bout depuis la seule donnee de la trace anomale et de la convention ⟨T_ab⟩ = −(2/√−g)δW/δg^{ab} : signe et coefficient du terme local, tenseur, equation completee, coefficient Γ du ln a dans le Weyl electrique rescale, croissance ou decroissance. Aucune lecture bibliographique.
- **W-b** : lecture aveugle des trois sources (2606.17963, 2501.05077, hep-th/0010232), releve des coefficients et exposants, conversion en n × bκ, transposabilite au Weyl rescale.
- **W-c** : audit des scripts et des affirmations t-1, t-2, t-3 de NOTE-131, recherche de contre-exemples.
Les consignes sont celles dont les empreintes figurent en tete. Elles ne contiennent ni γ, ni les coefficients des sources, ni le signe attendu.

## 2. Criteres de concordance (figes)
- **C-1 (module)** : W-a trouve |Γ| = 8bκ (soit G/(30π) par scalaire conforme), a 10⁻⁶ pres en valeur exacte.
- **C-2 (signe)** : W-a trouve un Weyl rescale **croissant** quand a → ∞ (Γ > 0 en ln a) avec la convention physique.
- **C-3 (sources)** : W-b trouve n = 8 pour les trois champs, au premier ordre (S1, S2) et pour l'exposant resomme (S2), et la transposabilite au Weyl rescale.
- **C-4 (NOTE-131)** : W-c juge t-1, t-2, t-3 valides (eventuellement sous hypotheses nommees compatibles avec celles de NOTE-131).

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **W-V1** | C-1 a C-4 satisfaits : la conversion, le signe et NOTE-131 sont confirmes a l'aveugle ; G-V3 consolide (premier ordre et resomme). |
| **W-V2** | C-1 et C-3 satisfaits, mais C-2 discordant, ou un facteur de convention a corriger (signe du terme local, facteur 2) : versions v2 de 133 et/ou 135 avec greffe encadree ; G-V3 inchange en module. |
| **W-V3** | C-1 ou C-3 discordant (valeur de Γ ou de n differente) : la concordance avec la litterature tombe ; NOTE-133 et 135 a reprendre. |
| **W-V4** | C-4 discordant : une affirmation de NOTE-131 invalide ; le caractere non compense du pole est a reexaminer. |
| **W-V0** | Audit inexploitable (auditeur hors consigne, outil indisponible) : a nommer, relance. |

Composites permis.

## 4. Prediction declaree (anti-fit)
**W-V1**, avec reserves attendues : (i) W-a signalera l'ambiguite du signe du terme local selon la convention de T_ab, et la tranchera en faveur de la croissance avec la convention physique ; (ii) W-b relevera le caractere de prescription (logarithmes dominants) de la resommation ; (iii) W-c pourra signaler que t-2 repose sur la conservation et la trace nulle du tenseur teste. Risque principal : un facteur de normalisation entre le coefficient du terme local de W et b (C-1).

## 5. Procedure apres retour
Rapports sauvegardes avec empreintes ; NOTE-137 (concordance) confronte chaque critere ; aucune correction de 131, 133, 135 avant NOTE-137 ; corrections eventuelles par versions v2 avec greffe encadree et acte.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange.
