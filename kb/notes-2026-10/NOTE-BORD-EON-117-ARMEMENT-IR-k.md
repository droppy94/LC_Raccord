---
id: NOTE-BORD-EON-117-ARMEMENT-IR-k
numero: 117
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-k)
reservation: 2026-10-11T16:11 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 117)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (cadre, espace des verdicts et prediction figes AVANT tout calcul)
depend: [NOTE-BORD-EON-111-IR-i-EXECUTION, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION, NOTE-BORD-EON-100-AUDIT-CHAMP-COHERENT-CONCORDANCE, NOTE-BORD-EON-104-IR-a-LECTURE-REF21]
sources: ["aucune nouvelle ; operateur de Riegert Δ₄ et F₄ tels que reproduits par S2 (2.13)-(2.16) et [21] (3.31)-(3.36), deja lus (NOTE-104)"]
issue_attendue: "delimitation"
rouvre_si:
  - "variation metrique de la partie invariante de Weyl W hors orbite de Weyl (S2 note 4)"
  - "etat de psi non causal ou modes homogenes de Δ₄ singuliers en s"
  - "ordres superieurs en beta"
---

# NOTE-117 : armement de IR-k. La completion de Riegert remplace-t-elle l'hypothese H-loc ?

## 0. Origine
NOTE-111 etablit la loi locale R_ln(x) = (3βκ/e²) Q_tf(x) sous une fermeture isotrope locale du secteur non Maxwell (H-loc), et note qu'une contrainte anisotrope d'ordre s² ln s pourrait compenser le log. Il faut calculer ce que fournit la completion covariante elle-meme.

## 1. Cadre (fige)
- Action anomale covariante : S_B = −(β/2e²) ∫ √g Ω[g] F², Ω[g] = ¼ Δ₄⁻¹ F₄ (Riegert ; Ω = −ln s sur le fond). Decomposition (NOTE-98) : partie (a), variation de √g F² a Ω fixe (secteur Maxwell X^M, porte I²) ; partie (b), variation de Ω[g] a J = √g F² fixe.
- Forme locale de (b) : S_b = ∫ J φ + ∫ √g ψ (Δ₄φ − ¼F₄), φ et ψ auxiliaires ; sur couche φ = Ω, √g Δ₄ ψ = −J, soit □_η² ψ = −J dans le repere conforme (invariance de Weyl de √g Δ₄). ψ causal (retarde) ; J d'ordre zero en β, analytique en η pres de η = 0.
- Partie W invariante de Weyl (dont l'action plate S_flat) : tenseur de poids de Weyl, T^W[g] = s² T^W[η] (fond conformement plat) ; T^W[η] evalue sur les champs du repere plat.
- Calculs prevus :
  (A) identite exacte ∇^μ X^M_μν = −¼ ∂_ν(I²) F² sur couche, et absence de log dans cette divergence au premier ordre (mode mixte non moyenne) ;
  (B) variation metrique explicite de S_b pour une famille de metriques g = s⁻² diag(−1, 1 + εh₁, 1 + εh₂, 1 + εh₃)(s, x), au premier ordre en ε, avec ψ(s, x) et φ = −ln s : tenseurs T^(b)_ii ; recherche de log en s ; puissances de s ; symetrie y ↔ z ;
  (C) confrontation a la structure de Q_tf du mode (B selon z, E selon y).

## 2. Sous-questions
- **K-1** : le tenseur T^(b) contient-il des ln s pres de 𝓘⁺ (ψ lisse) ? Et T^W ?
- **K-2** : quelles anisotropies T^(b) peut-il porter ? Peut-il reproduire la partie sans trace de Q (anisotropie de polarisation) ?
- **K-3** : la divergence de X^M est-elle sans log au premier ordre, de sorte qu'aucun terme logarithmique du secteur non Maxwell n'est requis par la conservation ?
- **K-4** : T^(b) apporte-t-il des puissances de s qui modifieraient la regularite de (2.17) hors log ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **K-V1** | Dans la classe « Riegert + partie invariante de Weyl a tenseur plat lisse », le secteur non Maxwell est sans log et ne voit le champ qu'a travers J (partie (b)) : il ne peut pas compenser le log ; la loi locale tient sans H-loc. |
| **K-V2** | La partie (b) (ou W) fournit un terme anisotrope en s² ln s capable de compenser le log : H-loc est fausse et le log est eliminable. |
| **K-V3** | Indecidable dans le cadre : la conclusion depend de W hors orbite, de l'etat de ψ, ou de termes singuliers en s non controles. |
| **K-V0** | Question mal posee (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**K-V1 qualifie K-V3** : φ n'apparait que derive dans T^(b) (invariance par translation de φ), ψ est lisse en s, donc T^(b) est sans log ; T^(b) ne depend du champ que par J, de sorte que T^(b)_yy = T^(b)_zz pour un J(s, x) alors que Q_tf distingue y et z : aucune compensation possible ; la divergence de X^M est sans log. Qualification : T^(b) porte des termes en puissances de s (eventuellement singuliers) qui touchent la regularite de (2.17) hors log, et la variation de W hors orbite reste inaccessible (seule l'invariance de Weyl est utilisee).

## 5. Instruments prevus
Script `ir_k.py` (sympy), empreinte avant execution.

## 6. Non-surclassement
[conv], premier ordre en β, fond fixe, cadre S2 + [21] et completion de Riegert. Noyau {A4 ; A2★ ; N} inchange.
