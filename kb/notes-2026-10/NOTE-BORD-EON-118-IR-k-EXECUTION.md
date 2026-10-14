---
id: NOTE-BORD-EON-118-IR-k-EXECUTION
numero: 118
serie: I
branche: Q-M3 suite (OP-IR, greffe IR-k)
reservation: 2026-10-11T16:11 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 118)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-117-ARMEMENT-IR-k (sha256 e4e862322e80a4563624d755a9b149557374a243417a46a846cbcf3b838c0410, 2026-10-11T16:12:17Z)
instruments:
  - "ir_k.py, sha256 d58327fe5149ecaf7a69d17b997414375e7aab865cb1c3283feb185b48e7ac40, 2026-10-11T16:13:21Z : EXIT 0, sortie ir_k_sortie.txt"
  - "ir_k_affichage.py, sha256 ff8cbab65034da49d36cc878698979c6f58228ef3d5c0ed8c924dc85884536db, 2026-10-11T16:17:32Z : EXIT 0 (affichage des T_i, meme calcul)"
  - "ir_k_ctrl.py, sha256 1ef8a3ba6c9458ea8bb14cefd10214db76bb428ca0dc5bf3bbd08b1141005fd5, 2026-10-11T16:18:54Z : EXIT 0 (partie C du gel)"
depend: [NOTE-BORD-EON-117-ARMEMENT-IR-k, NOTE-BORD-EON-111-IR-i-EXECUTION, NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION]
verdict: "K-V1 qualifie K-V3"
prediction_realisee: "oui, avec un renforcement (§5)"
rouvre_si:
  - "variation metrique de la partie invariante de Weyl W hors orbite (S2 note 4) produisant un log"
  - "etat de psi non causal ou non lisse en eta = 0"
  - "ordres superieurs en beta ; metrique perturbee hors de la famille diagonale testee"
---

# NOTE-118 : IR-k. La completion de Riegert rend H-loc inutile pour le log. Verdict **K-V1 qualifie K-V3**

## 0. Resume
Le tenseur energie-impulsion de la partie (b) de la completion de Riegert se reduit, pres de 𝓘⁺, a des derivees **plates** du champ auxiliaire ψ (□_η²ψ = −J). Le facteur conforme φ = −ln s y disparait entierement. Il n'y a donc ni log ni puissance negative de s, et ce tenseur ne voit le champ qu'a travers le scalaire J = √g F², donc pas sa polarisation. Par ailleurs, la loi R_ln(x) = (3βκ/e²) Q_tf(x) se retrouve **avec le seul secteur Maxwell**, sans aucun secteur non Maxwell, et la divergence de ce secteur est sans log. Le log de (2.17) ne depend donc pas de la fermeture : H-loc n'etait pas necessaire. Aucune completion de la classe « Riegert + partie invariante de Weyl a tenseur plat lisse » ne peut le compenser.

## 1. Resultats [calcule]

### A. Divergence du secteur Maxwell (ir_k_sortie.txt)
Pour le mode mixte non moyenne, au premier ordre en β : ∇^μ X^M_μν + ¼ ∂_ν(I²) F² = 0 pour les quatre composantes (identite exacte sur couche), et le coefficient de ln s dans ∇^μ X^M_μν est **0**. La conservation n'exige aucun terme logarithmique dans le secteur non Maxwell.

### B. Partie (b) de Riegert, famille g = s⁻² diag(−1, 1 + εh₁, 1 + εh₂, 1 + εh₃)(s, x)
- Fond : Δ₄(−ln s) − F₄/4 = 0, F₄ = 24 (de Sitter, H = 1).
- Densite d'action au premier ordre en ε : 8 termes. Equations d'Euler-Lagrange (T_i = δS_b/δh_i, d'ou T_ii = 2s² T_i en composantes coordonnees) :

| | Expression exacte |
|---|---|
| T_1 (x) | −(1/6)∂_s⁴ψ + (1/6)∂_s²∂_x²ψ |
| T_2 (y) = T_3 (z) | −(1/6)∂_s⁴ψ − (1/6)∂_x⁴ψ + (1/3)∂_s²∂_x²ψ |

- Aucun log(s), **aucune trace de φ** : ce sont des derivees plates de ψ.
- T_2 − T_3 = 0 : la partie (b) ne distingue pas y et z, alors que Q_tf du mode les distingue (B selon z, E selon y).
- Avec ψ lisse (ψ = Σ s^j a_j(x)) : plus basse puissance de s dans T_i = s⁰, donc T_ii ~ s², du meme ordre que la partie non logarithmique de X^M ; aucune puissance negative.
- Anisotropie T_1 − T_2 a l'ordre s⁰ : (∂_x⁴a₀ − 2∂_x²a₂)/6, fixee par les gradients de ψ, donc de J.

### C. La loi ne vient que du secteur Maxwell (ir_k_ctrl_sortie.txt)
R calcule avec T = X^M seul (aucun secteur non Maxwell) : coefficients de ln s a l'ordre s⁰ egaux a (3βκ/e²) Q_tf(x) pour (i, s, i), **ecart 0**, aucun autre log.

## 2. Lecture [derive]
1. **K-1** : T^(b) est sans log parce que φ = −ln s n'y entre pas (seules des derivees plates de ψ apparaissent, signe de l'invariance de Weyl de √g Δ₄) et parce que ψ, solution causale de □_η²ψ = −J avec J analytique pres de η = 0, est lisse en η = 0. Pour la partie invariante de Weyl W, T^W[g] = s² T^W[η] evalue sur des champs du repere plat lisses : sans log, sous l'hypothese que la variation hors orbite respecte l'invariance de Weyl.
2. **K-2** : T^(b) ne depend du champ que par J (un scalaire) et ne porte que des anisotropies de gradient (∂_i∂_jψ) ; il ne peut pas reproduire l'anisotropie de polarisation Q_tf (exemple : y ↔ z).
3. **K-3** : la divergence de X^M est sans log ; aucune contrainte logarithmique n'est imposee au reste. Comme R est lineaire en T, son log a l'ordre s⁰ ne provient que des termes logarithmiques de T, c'est-a-dire de X^M seul.
4. **K-4** : T^(b) n'apporte que des termes en s² (non logarithmiques) dans les composantes T_ii ; il modifie les constantes de R a l'ordre s⁰, pas son log, et ne cree pas de pole.

```
   T total = X^M (part (a))   +   T^(b) (Riegert)   +   T^W (invariant de Weyl)
             porte I² ~ ln s      derivees plates de ψ     s² × T^W[η] lisse
             log = −2β(T_B−T_E)   pas de ln, pas de φ      pas de ln
                    │                    │                        │
                    └──────── R(2.17) a l'ordre s⁰ ───────────────┘
                     ln s : (3βκ/e²) Q_tf(x), venu de X^M seul
```

## 3. Verdict
**K-V1 qualifie K-V3.**
- K-V1 : dans la classe « Riegert + invariant de Weyl a tenseur plat lisse », le secteur non Maxwell est sans log et aveugle a la polarisation ; il ne peut pas compenser le log ; la loi locale tient sans H-loc.
- Qualification K-V3 : la variation de W hors orbite de Weyl reste inaccessible (seule l'invariance de Weyl est utilisee) ; la famille de metriques testee est diagonale (pas de perturbations h_0μ ni hors diagonale) ; l'etat de ψ est suppose causal et lisse en η = 0.

## 4. Consequence sur NOTE-111
H-loc est **levee** comme hypothese pour le coefficient du log : la loi R_ln(x) = (3βκ/e²) Q_tf(x) vaut localement pour toute completion de la classe. H-loc reste une hypothese pour les termes **non** logarithmiques de R (constantes), que T^(b) modifie.

## 5. Confrontation a la prediction
Prediction (NOTE-117 §4) : « K-V1 qualifie K-V3 ; φ seulement derive, ψ lisse, pas de log ; T^(b)_yy = T^(b)_zz ; divergence de X^M sans log ; qualification : puissances de s possiblement singulieres et W hors orbite ». **Realisee**, avec un renforcement : φ ne figure **pas du tout** dans T^(b) (pas seulement derive), et les puissances de s ne sont pas singulieres (T_ii ~ s²). La qualification porte donc seulement sur W hors orbite, la famille de metriques et l'etat de ψ.

## 6. Portee sur Q-M3 et CCC + M
- Avec NOTE-116 : pour une source causale generique, Q_tf ≠ 0 et le ln Ω de (2.17) est present ; et, par la presente note, aucune completion de la classe consideree ne le compense.
- M-V3 (incompatibilite du canal de jauge anomal avec la regularite de (2.17) pour un champ coherent generique) se trouve renforce comme candidat. Ses conditions restantes sont : cadre S2 + [21] (champs charges conformes, vide conforme, in-in), premier ordre en β, fond fixe, variation de W hors orbite, source causale generique (Q_tf ≠ 0), et le fait que la regularite de (2.17) soit bien le critere pertinent de CCC + M. **Rien n'est grave** ; un audit froid est prealable a toute promotion. RG-4 inchangee.

## 7. Greffes proposees (non entees)
- **IR-m** : audit froid aveugle conjoint de NOTE-111, NOTE-116 et NOTE-118 (la chaine qui renforce M-V3).
- **IR-n** : etendre B a une famille de perturbations metriques generales (h_0μ, hors diagonale) pour lever la deuxieme qualification.
- **IR-o** : instruire la variation de W hors orbite (S_flat covariantise) pour la premiere qualification.

## 8. Non-surclassement
[conv], non audite. Premier ordre en β, fond fixe, cadre S2 + [21], completion de Riegert. Noyau {A4 ; A2★ ; N} inchange.
