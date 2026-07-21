# R-12 — CIBLES GELÉES (protocole §2.0 amendé post-CSE) — 2026-07-21 (S4)

Source : front-matters SEULS de LC-D-O2-JONCTION (v0.5), LC-D-O2-DELTA-C
(v0.2), LC-D-O2-COIN-TRANSMISSION (v0.3), LC-D-O2-P1 (v0.3),
LC-D-O2-P2 (v0.1), LC-D-O2-HODGE (v0.1) — corps NON lus, code des
sceaux NON lu. Lus au dépôt git (R-54 tenu). Figé AVANT toute
redérivation ; sha256 consigné hors-fichier en session.

## DÉCLARATION DE RÉVÉLATION DU MÉCANISME (règle post-CSE, opposable)

Les front-matters portent la chaîne interne ENTIÈRE et toutes les
valeurs d'arrivée : matrices explicites J=[[0,1],[1,0]] et
S=[[0,−1],[1,0]] avec leurs invariants (det, ordre, vp) ;
P=[[0,s],[1,0]], P²=s·𝟙, s=+1 pour l'involution nue (z~Ω⁻², signe
carré perdu) ; dét[v_α|S·v_α]=4μ ; garde-fou W̃=−W ∧ ⟨T̃⟩=−2δW̃/δh̃
⟹ C̃_T=+C_T ; i^{d−1}|_{d=3}=−1 ; ledger de dimensions (trace d=3,
courbure² 4, courbure×EMT d+2, TT̄ 2d à coeff (d−3)/2) ;
S_TC=−(1/8πG)∮√σ[η+κ(p)Φ], η=arcsinh(n·s), table b=2/⅔/0 ;
tous les verdicts (délimitation, discordance G1-c∧G2-c, TC-b, C1-b).
Sont révélés comme FETCHS EXTERNES : modes (f_a,f_b) de de Haro
(0808.2054), Freelance Holography II éq.7.13, Skenderis 2312.17316,
LMPS 1609.00207, LSW 2402.04308, Odak–Speziale 2109.02883 (table b/c),
Gustavsson 1911.04178, WCH (=A4, socle).

⟹ PLAFOND DE GRADE ANNONCÉ AU GEL : au mieux REPRODUIT-SOUS-RÉSERVE
au sens E-2. JAMAIS E-1.

CONTENU DISCRIMINANT ATTENDU (le reste = consignations) :
(a) ALGÈBRE MATRICIELLE RECALCULÉE (moteur sympy, pas une redite) :
    invariants de classe J vs S, P²=s·𝟙, vecteurs propres e±,
    échange des racines par J, commutation de S réelle avec la
    conjugaison, déterminant d'exclusion des α-vacua ;
(b) COMPOSITIONS DE SIGNES avec firewalls : involution z↦1/z (signe
    carré perdu ⟹ s=+1), garde-fou C̃_T=+C_T, réalité de i^{d−1}
    ⟺ d impair ;
(c) BOOKKEEPING DE DIMENSIONS d=3 (ledger, coefficient (d−3)/2=0,
    trichotomie signe(Δ_𝒞−d)=0 → C1-b) ;
(d) STRUCTURE DU COIN : additivité en rapidité de η=arcsinh(n·s) ;
    limite m2 (κ→0 ⟹ η-term nu).
Comptages de sources, table b=2/⅔/0, transport dS bloqué (lecture
Skenderis), et tous les verdicts : IMPORTS/verdicts consignés.

## Cibles

| # | cible | valeur revendiquée |
|---|---|---|
| Q1 | jonction | crossover 𝒞 = jonction DISCRÈTE Dirichlet\|Neumann (n : g₀ fixé, g₃=⟨T⟩ ; n+1 : g₃=0 par WCH, g₀ libre) ; eigenmode +i = condition d'état, pas d'angle Robin libre — cartographie, consignation |
| Q2 | P1-G1/G2 | z~Ω⁻² sous Ω↦−1/Ω ⟹ z↦1/z (signe CARRÉ PERDU) ⟹ involution nue s=+1 ; P=[[0,s],[1,0]], P²=s·𝟙 ; P=S ⟺ s=−1 ⟹ P²=+𝟙 ≠ S²=−𝟙 |
| Q3 | Hodge J≠S | J : det=−1, ordre 2, vp ±1 ; S : det=+1, ordre 4, vp ±i — invariants de classe ⟹ J ≁ S à TOUTE base près |
| Q4 | garde-fou | W̃=−W ∧ ⟨T̃⟩=−2δW̃/δh̃ ⟹ C̃_T = +C_T : la jonction NE flippe PAS le signe physique |
| Q5 | source unique | i^{d−1} réel ⟺ d impair ; = −1 à d=3 ; DISTINCT du −𝟙 de S² (structural) — deux −𝟙, aucun double-comptage |
| Q6 | P2-α | dét[v_α \| S·v_α] = 4μ, s'annule ⟺ μ=0 (BD) ⟹ α-vacua exclus SANS intrant d'état ; resserrement ∞ → {BD, BD*} |
| Q7 | P2-β / G2 | S RÉELLE commute avec la conjugaison, qui échange e₊↔e₋ (paire NON ordonnée ⟹ +i non structurel) ; J·e₊ ∝ e₋ (la jonction échange BD↔BD*, traite ±i symétriquement) |
| Q8 | Δ_𝒞 | ledger d=3 : trace dim 3 (le plus relevant, marginal Δ_𝒞=d) < courbure² 4 < courbure×EMT 5 < TT̄ 6 à coeff (d−3)/2=0 ⟹ trichotomie → C1-b ; transport dS BLOQUÉ = lecture, consignation |
| Q9 | coin | S_TC=−(1/8πG)∮√σ[η+κ(p)Φ] ; η=arcsinh(n·s) ADDITIF en rapidité ; m2 : face N→Dirichlet ⟹ κ→0 ⟹ retour EXACT au η-term nu ; p LIBRE ∀p ⟹ α = C1-b POSITIF (classification finale) — table b=2/⅔/0 = import |
| Q10 | verdicts | (C-O2) forte NON établie ; P1 réduite à s=(−1)^w (décision ouverte) ; P2 = DISCORDANCE (G1-c∧G2-c) ; TC-b ; β≡G3 = SEUL facteur d'O₂ ouvert — verdicts, consignation |

Sceaux du lot (rejeu de confirmation, GO opérateur à demander) :
verif_O2_P1 (sha8 attendu 6b23b2ae), verif_O2_P2 (f2b110e8),
verif_O2_hodge (421d5f29), verif_O2_coin_transmission_* — statuts
LIVE/ARCHIVE à relever à l'inventaire. Leur CODE n'est pas lu avant
la redérivation.

Grades possibles : REPRODUIT-SOUS-RÉSERVE (E-2) ·
REPRODUIT-SOUS-RÉSERVE (écart nommé borné) · NON-REPRODUIT.

§6.4 : figer des cibles ne scelle, ne réduit, ne compte, ne démontre
rien. « Reproduit » vaudra cohérence d'algèbre et d'invariants —
JAMAIS « O₂ construit » (O₂ n'existe pas ; β≡G3 reste ouvert), ni
« A4 réduit », ni « D1 fermé », ni « N fixé ».
{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée.
