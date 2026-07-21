# R-2 — CIBLES GELÉES (protocole §2.0 amendé post-CSE) — 2026-07-21 (S4)

Source : front-matters SEULS de LC-A-D1-FACTEUR-CONFORME (v0.5),
LC-A-D1-BIANCHI (v0.1), LC-A-D1-STABILITE-WEYL (v0.1),
LC-D-D1-VERROU-AMPLITUDE (v0.3), LC-D-D1-VERROU-DELIMITATION (v0.1),
LC-D-D1-VERROU-FLRW (v0.1), LC-D-D1-VERROU-INHOMOGENE (v0.1) — corps
NON lus, code des sceaux NON lu. Lus au dépôt git (R-54 tenu : mount
autoritaire, git miroir). Figé AVANT toute redérivation ; sha256
consigné hors-fichier en session.

## DÉCLARATION DE RÉVÉLATION DU MÉCANISME (règle post-CSE, opposable)

Ces front-matters sont MASSIVEMENT révélants — davantage que ceux de
R-6 : ils portent la chaîne interne ENTIÈRE (famille Ω̂=c₁â ;
c₁=√(2λ̂/3k) [Penrose-55d] ; c₁=(λ̂/m̂)^{1/4} [Tod] ; point fixe
m̂λ̂=9k²/4 ; dégénérescence k=0 ; C≡0 FLRW vs C≠0 Kasner ;
σ̌=−4·Ricci-sans-trace(â) [Tod éq.33] ; contre-exemples Bianchi IX
squashé et g=e^{2x}δ₃) et TOUTES les valeurs d'arrivée (|σ̌|²=128ε²,
Ricci-tf=(⅔,−⅓,−⅓)e^{−2x}, det J*=1, A_T·N=16, C_T/N=1/(32π²)).
Sont révélés comme FETCHS EXTERNES : la carte de Markwell-Stevens
(GRG 55,93 2023, éq.14 — sa FORME n'est pas dans les front-matters),
la convergence historique des trois prescriptions (Newman/Tod/
Nurowski), Tod 1309.7248 §7 (lissité du crossover squashé),
Friedrich 1986 (donnée de bord libre), Milnor 1976.

⟹ PLAFOND DE GRADE ANNONCÉ AU GEL : au mieux REPRODUIT-SOUS-RÉSERVE
au sens E-2. JAMAIS E-1.

CONTENU DISCRIMINANT ATTENDU du lot (le reste = consignations) :
(a) GÉOMÉTRIE RECALCULÉE par moteurs génériques, pas des redites :
    Ricci left-invariant (Koszul sur repère + constantes de structure,
    SANS formule de Milnor importée) pour le Bianchi IX squashé ;
    Ricci/Cotton en coordonnées pour g=e^{2x}δ₃ ; Weyl 4D pour
    FLRW-radiation et Kasner ;
(b) IDENTITÉS ALGÉBRIQUES : coïncidence 55d/Tod ⟺ m̂λ̂=9k²/4 ;
    dégénérescence k=0 ; cross-cohérence A_T·C_T (N-libre) ;
(c) ADJUDICATION DE CONVENTION pour le coefficient 128 (normalisation
    des σᵢ × paramétrisation du squash) : jeu de conventions ÉNUMÉRÉ
    ET DÉCLARÉ AVANT comparaison ; la cible adjuge ; si aucune
    convention naturelle ne donne 128 ⟹ écart nommé borné ou
    NON-REPRODUIT partiel — jamais d'ajustement (anti-fit).
La forme de la carte MS éq.14, ses conséquences propres (Jacobien
v.p. 1 double, det J*=1, runaway), la lissité de Tod §7, et les
verdicts d'axe : IMPORTS/verdicts consignés, jamais comptés PASS.

## Cibles

| # | cible | valeur revendiquée |
|---|---|---|
| Q1 | famille D1 | les trois prescriptions convergent sur Ω̂=c₁â ; TOUTE la liberté D1 = le seul constant c₁ — convergence = IMPORT, consignation ; la compatibilité algébrique des deux formules de c₁ est Q2 |
| Q2 | coïncidence au point fixe | c₁²=2λ̂/3k (Penrose-55d) et c₁=(λ̂/m̂)^{1/4} (Tod) coïncident ⟺ m̂λ̂ = 9k²/4 EXACTEMENT |
| Q3 | dégénérescence k=0 | à k=0 : 55d diverge (pôle en k) ; la droite fixe dégénère en m̂λ̂=0 triviale ; #5 vacant |
| Q4 | dynamique inter-éons | droite fixe entière, Jacobien non-hyperbolique (v.p. 1 double), det J*=1, runaway hors droite, bifurcation instable — dépend de la FORME de MS éq.14 : IMPORT, consignation |
| Q5 | Weyl et secteurs | C_abcd ≡ 0 en FLRW (conformément plat) ; C ≠ 0 en Kasner ⟹ fond (m,λ) ⊥ marée (g₃) en symétrie |
| Q6 | [R1] Bianchi IX squashé | σ̌ = −4·Ricci-tf(â) ⟹ |σ̌|² = 128ε² + O(ε⁴) ; σ̌ ≠ 0 à ε=½ ; lim_{ε→0} = 0 ; S³ ronde Einstein (tf = 0) |
| Q7 | [R2] contre-exemple Cotton | Cotton(e^{2x}δ₃) ≡ 0 (27 composantes) ∧ Ricci-sans-trace = (⅔,−⅓,−⅓)·e^{−2x} ≠ 0 |
| Q8 | FW-3 / strictité | Einstein-3D ⊊ {Cotton=0} : la strictité suit de Q7 (dérivable) ; « aucune régularité naturelle ne sélectionne ; A3 socle indépendant » = verdict, consignation |
| Q9 | jambe amplitude | A_T = 16/N ∧ C_T/N = 1/(32π²) ⟹ A_T·C_T = 1/(2π²), N-LIBRE (cross-cohérence des deux scellés) ; amplitude absorbée dans N |
| Q10 | verdict d'axe | DÉLIMITATION : aucun sélecteur de prescription interne (FLRW Δ1-b ; inhomogène D1c3-c) ; ni fermeture ni réfutation ; D1c3-3 (généricité) DÉCHARGÉE (audit froid CONFIRMATION) — verdicts, consignation |

Sceaux du lot (rejeu de confirmation, GO opérateur à demander) :
verif_D1_facteur, verif_D1_atlas, verif_D1_bianchiA, verif_D1_stabilite,
verif_D1c3_regularite, verif_D1c3_genericite (sha8 attendu b615d6b4)
— statuts LIVE/ARCHIVE à relever à l'inventaire. Leur CODE n'est pas
lu avant la redérivation.

Grades possibles : REPRODUIT-SOUS-RÉSERVE (E-2) ·
REPRODUIT-SOUS-RÉSERVE (écart nommé borné) · NON-REPRODUIT.

§6.4 : figer des cibles ne scelle, ne réduit, ne compte, ne démontre
rien. « Reproduit » vaudra cohérence d'algèbre et de coefficients —
JAMAIS « D1 fermé » (D1 reste OUVERT, cartographié), ni « sélecteur
trouvé », ni « N fixé ».
{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
