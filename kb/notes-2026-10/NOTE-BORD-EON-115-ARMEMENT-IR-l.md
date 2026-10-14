---
id: NOTE-BORD-EON-115-ARMEMENT-IR-l
numero: 115
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-l)
reservation: 2026-10-11T15:54 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 115)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-114-ACTE-GREFFE-IR-d3, NOTE-BORD-EON-113-AUDIT-IR-g-CONCORDANCE, NOTE-BORD-EON-108-IR-g-EXECUTION]
sources: ["aucune ; rayonnement dipolaire electrique et magnetique, parametres de Stokes : formules standard, utilisees comme [derive] et controlees par le calcul"]
issue_attendue: "delimitation"
rouvre_si:
  - "source persistante jusqu'a scri+ ; charges nettes (champ longitudinal)"
  - "ordres superieurs en beta, retroaction"
---

# NOTE-115 : armement de IR-l. Quelles sources causales donnent ⟨B_iB_j⟩_tf = ⟨E_iE_j⟩_tf a 𝓘⁺ ?

## 0. Origine
NOTE-113/114 : le ln Ω de (2.17) est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺. L'audit a exhibe des champs coherents a Q = 0 (onde circulaire, helicoidale). Il faut savoir si une source causale **generique** tombe dans cette classe.

## 1. Cadre (fige)
- Repere conforme plat, η < 0, 𝓘⁺ = {η = 0} ; dynamique de β = 0 (l'etat a l'ordre zero suffit pour Q).
- Source : courant transverse J(t, x) a support compact en espace et en temps (eteinte avant η = 0). Champ a η = 0 par la fonction de Green retardee, mode par mode : A_k(0) et E_k(0) exprimes avec les composantes sur couche Ĵ(±k, k) (notees J₊, J₋).
- Q = Σ_k [k²(k̂ × a)(k̂ × a)† − b b†] (partie reelle, moyenne spatiale par Parseval), a = A_k(0), b = E_k(0).
- Decomposition de chaque terme : partie « diagonale » (J₊J₊†, J₋J₋†) et partie d'interference (J₊J₋†), cette derniere portant la phase d'emission (cos 2kD de NOTE-108).
- Decomposition de Stokes dans le plan transverse : intensite, polarisation lineaire (L), polarisation circulaire (V).
- Sources tests : dipole magnetique lineaire ; dipole magnetique tournant ; dipole « chiral » p = i m (combinaison electrique et magnetique) ; ensemble isotrope ; combinaison generique de dipoles et d'un quadrupole.

## 2. Sous-questions
- **L-1** : quelle est l'expression de Q_tf en fonction de la source ? Quelle partie de la polarisation du rayonnement y contribue (lineaire, circulaire, intensite) ?
- **L-2** : apres moyenne de la partie d'interference (emission sous-Hubble), a quelle composante angulaire du motif de polarisation dans l'espace des k Q_tf se reduit-il ?
- **L-3** : quelles sources tests donnent Q_tf = 0 ? En particulier, l'helicite de la source suffit-elle (dipole tournant contre dipole chiral) ?
- **L-4** : combien de conditions reelles faut-il imposer a une source generique pour annuler Q_tf ? La classe Q_tf = 0 est-elle exceptionnelle ou generique ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **L-V1** | Q_tf = 0 est exceptionnel (codimension ≥ 1) : il faut une source a helicite pure, ou un motif de polarisation sans la bonne composante angulaire, ou un ensemble isotrope ; une source causale generique donne Q_tf ≠ 0 et le ln Ω existe. |
| **L-V2** | Une propriete generale des sources causales (conservation, causalite) impose Q_tf = 0 : le ln Ω est genericement absent. |
| **L-V3** | Pas d'enonce generique : la reponse depend de la source sans structure identifiable. |
| **L-V0** | Question mal posee (a nommer). |

## 4. Prediction declaree (anti-fit)
**L-V1** : la partie rayonnee de Q_tf est proportionnelle a l'integrale sur les directions de k du tenseur de polarisation **lineaire** du rayonnement (l'intensite et la polarisation circulaire ne contribuent pas) ; par parite, seule la composante quadrupolaire de type E (ℓ = 2) du motif de polarisation survit ; Q_tf = 0 impose 5 conditions reelles ; dipole chiral p = i m (helicite pure) : Q_tf = 0 ; dipole tournant : Q_tf ≠ 0 (l'helicite d'une partie du rayonnement ne suffit pas) ; dipole lineaire : (4/5)(mm − ⅓m²) a la normalisation pres ; ensemble isotrope : 0 ; combinaison generique : ≠ 0. La partie d'interference oscille avec l'instant d'emission et se moyenne vers 0 pour une emission sous-Hubble.

## 5. Instruments prevus
Script `ir_l.py` (sympy), empreinte avant execution.

## 6. Non-surclassement
[conv], ordre zero de l'etat, source compacte eteinte, cadre S2 + [21] pour la loi. Noyau {A4 ; A2★ ; N} inchange.
