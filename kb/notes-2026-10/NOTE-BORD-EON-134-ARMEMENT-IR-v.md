---
id: NOTE-BORD-EON-134-ARMEMENT-IR-v
numero: 134
serie: I
branche: Q-M3 suite (IR-v)
reservation: 2026-10-12T12:43 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 134)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (question, regle de conversion, espace des verdicts et prediction figes AVANT toute lecture de la source)
decision: operateur (Thierry), 2026-10-12 14:43 heure de Paris
depend: [NOTE-BORD-EON-133-IR-u-EXECUTION]
issue_attendue: "delimitation"
rouvre_si:
  - "la source renvoie a un autre travail pour la resommation des ondes gravitationnelles (a lire sous nouveau gel)"
  - "audit froid de NOTE-133 modifiant la conversion des normalisations ou le signe"
---

# NOTE-134 : armement de IR-v. La resommation de Woodard donne-t-elle W_E ∝ Ω^(−8bκH²) ?

## 0. Origine
NOTE-133 : au premier ordre, W_E ≈ W₀(1 + 8bκ ln a) (convention physique Carroll-Wald), coefficient identique a celui de Foraci, Litos et Woodard (arXiv:2606.17963) pour trois especes de champs conformes. Ces auteurs ecrivent que la croissance seculaire « can be summed up using a variant of the renormalization group » et renvoient a Woodard 2025 (Int. J. Mod. Phys. D 34, 2542002 ; arXiv:2501.05077), cite et non lu. La forme resommee W ∝ Ω^γ est conditionnelle a cette lecture.

## 1. Cadre (fige)
- **Source** : arXiv:2501.05077 (R. P. Woodard), via alphaXiv. Si la version arXiv est inaccessible, verdict V-V3 sans substitution par une autre source dans cette note.
- **Lecture minimale (EX-9)** : resume ; section ou la variante du groupe de renormalisation est formulee ; section ou elle est appliquee a la matiere conforme (potentiel newtonien, ondes gravitationnelles ou Weyl) ; jusqu'a la fin de la section suivante. Textes sauvegardes, empreintes.
- **Regle de conversion** (reprise de NOTE-133 §2.4, figee) : κ = 8πG ; b = coefficient de C² dans ⟨T^a_a⟩, normalisation c = (N_S + 6N_F + 12N_V)/(120(4π)²) ; κ_W² = 16πG chez Woodard ; Ω ∝ 1/a sur de Sitter (s = −η, Ω = Hs) ; H = 1 sauf mention.
- **Cible** : forme resommee du Weyl electrique (ou de la fonction de mode a l'ordre (k/aH)³) des ondes gravitationnelles pour la matiere conforme, a temps tardif a → ∞ (Ω → 0).

## 2. Sous-questions
- **v-1** : la source donne-t-elle une forme resommee pour les ondes gravitationnelles (Weyl electrique ou fonction de mode), ou seulement pour d'autres observables (potentiel newtonien, etc.) ?
- **v-2** : cette forme est-elle une loi de puissance en a ? Son exposant, converti, vaut-il 8bκH² (soit G H²/(30π) par scalaire conforme) ?
- **v-3** : quelles conditions de validite la source enonce-t-elle (logarithmes dominants seulement, regime perturbatif, exposant au premier ordre en κ²H², nature du « variant ») ?
- **v-4** : la forme resommee est-elle presentee comme valable pour a → ∞, c'est-a-dire precisement la ou se pose la question du raccord ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **V-V1** | La source resomme les logarithmes en une loi de puissance en a pour le Weyl (ou la fonction de mode) des ondes gravitationnelles, avec un exposant egal, apres conversion, a 8bκH² ; presentee comme valable a temps tardif. D'ou W_E ∝ Ω^(−8bκH²) [extrait + derive], qualifications nommees. |
| **V-V2** | La source fournit une resommation en loi de puissance, mais pour une autre observable, ou sous une forme generique (equation de Callan-Symanzik) dont l'application aux ondes gravitationnelles est une extension non ecrite par l'auteur, ou avec un exposant different ; la forme Ω^(−8bκH²) reste conditionnelle, condition nommee. |
| **V-V3** | Pas de resommation exploitable (source inaccessible, resommation non en loi de puissance, ou contradiction) ; G-V3 reste etabli au premier ordre seulement. |
| **V-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**V-V2, avec possibilite V-V1.**
- La source formule une variante du groupe de renormalisation ou les logarithmes seculaires de la matiere conforme viennent de ce que les contre-termes en C² (et R²) dependent de l'echelle μ, remplacee effectivement par aH ; l'equation de type Callan-Symanzik resomme les logarithmes dominants en puissances de a.
- L'exposant est, par construction, le coefficient du premier ordre (logarithmes dominants), donc compatible avec 8bκH² si l'observable est la meme.
- Je m'attends a ce que l'application explicite porte d'abord sur le potentiel newtonien ; que les ondes gravitationnelles soient traitees ou non dans ce texte est l'incertitude principale (d'ou V-V2 plutot que V-V1).
- Conditions attendues : logarithmes dominants seulement, premier ordre en κ²H² pour l'exposant.

## 5. Instruments prevus
Lecture alphaXiv (answer_pdf_queries, puis texte complet si necessaire) ; extraits sauvegardes avec empreintes ; eventuel script de conversion `irv_conversion.py` (sympy), empreinte avant execution.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Une concordance de lecture ne grave rien.
