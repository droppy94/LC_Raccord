# RAPPORT VA-3 : re-audit court et adverse de la v2.5 corrigée

Auditeur isolé VA-3, 2026-10-16. Pièces ouvertes, et seulement elles : la consigne PROMPT-REAUDIT-VA3.md ; auditv25/ARTICLE-v2.5.tex (version auditée) ; dirac-mass-scri-v2.5.tex (version corrigée) ; auditv25/COMPANION.tex et companion-formal-regularity.tex (note avant et après) ; RAPPORT-VA1.md, RAPPORT-VA2.md ; NOTE-BORD-EON-214-AUDIT-V25-CONCORDANCE.md. Aucune référence externe, aucun script du programme. Travail dans work_va3/ :

| Fichier | Contenu |
|---|---|
| `article.diff`, `article.wdiff`, `companion.diff` | diffs ligne et mot des deux versions |
| `va3_checks.py` / `.out` | sympy : Clifford, dispersion et remise à l'échelle chirale du Lemme 2, courant conservé, termes sigma, identité de la Rem. 1, forme de Fuchs, signes de la Prop. 2(c), masse ΛCDM |
| `va3_numerics.py` / `.out` | numérique de Sitter (H = 1, DOP853, rtol 1e-11) : borne de la Prop. 3, pôle simple, identité tanh, exemples de la Prop. 4 |

Classes : **erreur** (énoncé faux tel qu'écrit), **correction** (imprécision, incohérence, surclassement léger), **remarque**.

## 0. Synthèse

| Axe | Résultat |
|---|---|
| R1 application | Les 11 lignes du §1 et les 20 entrées du §2 de la concordance sont appliquées dans le texte. Trois sont partielles (K6.2, K6.5, C5) et une est répercutée imparfaitement dans la note compagnon (E3/k = 0). |
| R1 justesse | Tous les calculs demandés sont confirmés : m_eff² = (m²+m₅²)/(Z₁²−Z₂²), s² = (Z₁−Z₂)/(Z₁+Z₂), réduction sigma (σRσ = 24H²·1), preuves de la Rem. 1, borne de la Prop. 3 sur de Sitter, condition de Plancherel, conditions de la Prop. 4 pour ΛCDM (au signe près, voir C-2). |
| R2 nouvelles fautes | Aucune erreur mathématique introduite dans l'article. Une phrase nouvelle surclasse légèrement (ΛCDM « not excluded », C-1) et ignore le signe de la masse (C-2). Deux incohérences locales nouvelles (annexe, C-3 ; intro, C-4). Les modifications hors liste sont toutes tirées des rapports et sont bénignes. |
| Note compagnon | **Une erreur résiduelle** : le résumé garde « bounded without limit otherwise », faux pour k = 0 (E-1). Sa définition de la régularité formelle n'a pas suivi la Déf. 1(c) corrigée (C-5). |
| R3 | Les quatre reports du §3 sont acceptables. |
| R4 | Au sens strict, **non en l'état** à cause d'E-1 (note compagnon). L'article seul ne garde aucune erreur parmi les points audités. Après E-1, C-1 à C-5 (une ligne chacune), entable sans nouvel audit. |

---

## R1. Corrections annoncées : application et justesse

### R1.1 Concordance §1 (constats concordants)

| Constat | Appliqué | Juste | Vérification VA-3 |
|---|---|---|---|
| Rem. 1, « can be present only if » ; X = β à l'ordre Ω | oui | oui | sympy : χ₀⁺†βχ₀⁻ = 0, donc le terme d'ordre 0 s'annule. |
| §5, k ≠ 0 | oui | oui | La phrase dit « for every solution with **k** ≠ 0 that contains both ». Le cas k = 0 avec deux exposants (source nulle) n'est rangé dans aucune des deux classes. « Distinguishes these two classes » reste vrai (pas de partition revendiquée). |
| Régularité formelle contre sources | oui | oui | §5 : règle sur les sources géométriques ; « a rule that requires formal regularity of the matter equation rejects both ». C'est cohérent avec la Déf. 1(c) corrigée et avec la Rem. 2(1). La Rem. 2(4) est marquée « statement on solutions ». Au §4.3, le point singulier régulier est ajouté aux invariants. |
| Poids poussière, repère orthonormé | oui | oui | Avec T[ψ;g] = Ω²T[ψ̂;ĝ] et e₀ = Ω∂_η, e_i = Ω∂_i, on trouve Ω⁻³T(e₀,e_i) = ΩT̂_ηi = −Ωk_i u†u et Ω⁻³T(e_i,e_j) = ΩT̂_ij = (Ω/2)(k_iJ_j+k_jJ_i). Ce sont les formules du texte. Pour deux exposants et k ≠ 0, le coefficient croisé χ₀⁺†α_jχ₀⁻ ne peut s'annuler pour tout j (b a† de rang 1 n'est pas ∝ 1). Les contraintes divisées par Ω portent donc bien le facteur d'interférence. |
| Exemple Ω^{1/2} sur de Sitter | oui | oui | ∫3e^{−t/2}dt = 6 (convergent) ; m a = 3e^{t/2} non borné. L'exemple Ω(1+Ω^{1/2}) est dit « on any background », ce qui est juste : m a = 1+Ω^{1/2}. |
| Prop. 3 : pôle simple, de Sitter | oui | oui | Voir R1.3(d). |
| f = (1−P)g/‖·‖, Plancherel en hélicité | oui | oui | Voir R1.3(e). |
| Prop. 5(b) classique et quantique | oui | oui | (b) renvoie à la Prop. 4(b) pour ‖χ₀⁺‖ ≠ ‖χ₀⁻‖. La version quantique est restreinte (masse constante, de Sitter, BD, intégrée). Le terme du vide est signalé après la proposition. La composante ηη de Ω⁻²T_ab est bien ρ̂ (Ω⁻²T_ηη = Ω⁻⁴T_tt) ; la composante ηi, −k_i‖u‖², est bornée, donc l'échec vient de ηη seul. |
| Chapeaux Rem. 2(2)(3) | oui | oui | T = Ω²T[ψ̂;ĝ] : Ω³ (deux spineurs) × Ω⁻¹ (γ_a abaissé). ξR physique, R = 4λ, donc m_h²+ξR = R/6, ce qui donne la condition annoncée. |
| Lissité en η ou en Ω | oui | oui | Déf. 1 : « same notions with Ω when stated » ; Prop. 4(c) « as a function of Ω ». |
| P±(0) à une phase près | oui | oui | −θ = μ ln Ω + c donne e^{−iβθ} = Ω^{iμβ}e^{icβ}, donc P₊(0) = e^{ic}χ₀⁺. |

### R1.2 Concordance §2 (constats d'un seul auditeur)

| Entrée | Appliqué | Juste | Note |
|---|---|---|---|
| VA-1 C9 (masse effective) | oui | oui | R1.3(a). |
| VA-1 C8 (termes sigma) | oui | oui | R1.3(b) ; voir C-3 et R-3. |
| VA-1 C3(ii)(iii) (Rem. 1) | oui | oui | R1.3(c). |
| VA-1 C4 (m > 0, cas χ₀⁺ = 0, potentiel non intégrable) | oui | oui | sympy : A_Ω = −m/(eHΩ). Avec ς = +θ, e^{−iς}u = (e^{−2iθ}χ⁺, χ⁻) converge, et le potentiel est opposé. ∫m a dη = ∫m dt = ∞ sur tout FLRW. |
| VA-1 C7 (autre état) | oui | oui | Invariance par translation, diagonalité en hélicité, poids dépendant de k, positivité si la particule domine. |
| VA-1 C11(c) | oui | oui | « On exact de Sitter space and within the class of Lemma 2 … on other backgrounds … Proposition 4 applies ». |
| VA-2 E1.4 | oui | oui | Résumé (i) : « On de Sitter space, in conformal time ». |
| VA-2 E2.1 à E2.4 | oui | non vérifiable ici | GP « after » ; Birrell-Davies retiré de la phrase sur les paires (il reste cité, à juste titre, pour la covariance conforme au §4.1) ; Markwell-Stevens ; points de Hawking. Ces formulations reprennent mot pour mot les corrections de VA-2. |
| VA-2 C2.5, C2.6 | oui | oui | AL pour la symétrie maximale, DFMR Prop. 4.5 pour Hadamard ; « for every renormalisation prescription satisfying Wald's axioms ». |
| VA-2 K2.1 (Ibison) | oui | oui | Voir R-4 sur « relative size ». |
| VA-2 E5.1, E5.2, C5.3, C5.4, K5.5, K5.6 | oui | voir C-6, R-5 | W,Z en suffisance ; « not attempted » ; « established by an auditor » ; « v2 corrected, not re-audited » ; H_Λ ; notations χ₀±. |
| VA-2 E6.1 (ΛCDM) | oui | oui au signe près | R1.3(f) ; C-1, C-2. |
| VA-2 K6.2, K6.3, K6.5 | partiel | oui | Rétablis : Majorana « remain singular, having weight −1 » (cohérent : ψ^TCψ a le même poids −1 que ψ̄ψ) ; quanta de Dirac près de scri ; réserves de Verification ; phrase m/H ; « rule on still other variables ». **Non rétablis** : « Proposition 1 alone, being gauge dependent for such states, would not justify it » (K6.5) et « a mechanism that would bring the Higgs to the symmetric point » (K6.2, en partie couvert par le §5). La concordance écrit « rétablies » sans réserve (R-6). |
| VA-2 C4.3 (ς) | oui | oui | Plus aucun λ de jauge dans le texte. |
| VA-2 E7.1, E7.2 | oui | oui | P de la fonction à deux points ; convention de fréquences. |
| VA-2 E1.1 | oui | oui | « standard explicitations, not new results ». |
| VA-2 C1.3 | oui | oui | dirac_scri_check_v2_1.py expliqué. |

### R1.3 Vérifications par calcul (demandées par la consigne)

**(a) Masse effective du Lemme 2.** `va3_checks.out` [1a] : det[(Z₁+Z₂γ₅)γ·p − (m+im₅γ₅)] = [(Z₁²−Z₂²)(p₀²−p²) − (m²+m₅²)]², identité exacte. [1b] : avec ψ = (sP_L+P_R)φ et la normalisation à gauche T = P_R/(s(Z₁+Z₂)) + P_L/(Z₁−Z₂), on obtient M_R = (m+im₅)/(s(Z₁+Z₂)) et M_L = s(m−im₅)/(Z₁−Z₂). On a M_L = M_R* (masse chirale hermitienne, rendue réelle par une rotation chirale) si et seulement si s² = (Z₁−Z₂)/(Z₁+Z₂), ce qui demande Z₁² > Z₂². Alors |M|² = (m²+m₅²)/(Z₁²−Z₂²). [1c] : le courant conservé de l'action d'origine vaut (Z₁−Z₂) fois le courant standard de φ. « Change … by constant factors » est donc exact. La formule et la preuve corrigées sont justes. La chiralité qui reçoit s dépend de la convention P_L = (1−γ₅)/2, que l'article ne fixe pas (R-3).

**(b) Termes sigma.** [2] : σ^{ab}σ_{ab} = 12·1 et σ^{ab}R_{abcd}σ^{cd} = 24H²·1 sur de Sitter. De même σ^{ab}(¼R_{abcd}γ^cγ^d) = −6iH²·1, qui commute avec γ₅. L'intégration par parties ∇_aψ̄σ^{ab}∇_bψ = ∇_a(ψ̄σ^{ab}∇_bψ) − ½ψ̄σ^{ab}[∇_a,∇_b]ψ est correcte (σ est covariantement constant). La réduction à ψ̄ψ et à ψ̄γ₅ψ à coefficients constants est juste. Le terme ∇ψ̄σ∇ψ est imaginaire pur ; il faut un facteur i pour que l'action soit réelle (R-3). La version γ₅ est réelle telle quelle et se réduit à 3H²ψ̄iγ₅ψ.

**(c) Rem. 1, transformations V.**
- Premier argument : si les coefficients pour χ sont lisses, donc bornés, χ converge ; avec V continu en 0, u = Vχ converge, ce que la Prop. 1 exclut. C'est juste. L'inversibilité de V sert seulement à écrire l'équation pour χ.
- Second argument : à k = 0, avec B₀ lisse, V = Ω^{iμβ}M donne M' = −MB₀, donc M est lisse et inversible ([3] vérifie d/dΩ Ω^{iμβ} = (iμβ/Ω)Ω^{iμβ}). Ensuite Ω^{−iμβ}α_jΩ^{iμβ} = α_jΩ^{2iμβ} (identité exacte, [3]). Si M⁻¹(α·k)Ω^{2iμβ}M était lisse, alors (α·k)Ω^{2iμβ} le serait aussi, ce qui est faux pour k ≠ 0. La preuve est complète.
- La forme de Fuchs (i/H)(βm/Ω + α·k) est confirmée à partir de (3).

**(d) Prop. 3 sur de Sitter.** La borne découle déjà de (4) : |χ†βχ − χ₀†βχ₀| ≤ (2k|η| + k²η²)‖χ₀‖², donc (m/Ω)·O(k|η|) = O(mk/H). Avec la Déf. 1 (Ωf → c ≠ 0 et f − c/Ω borné), l'équivalence « pôle simple si et seulement si c ≠ 0, borné sinon » est juste dans les deux sens. Numérique (`va3_numerics.out`) :

| Cas | Mesure | Résultat |
|---|---|---|
| ‖χ₀⁺‖ = ‖χ₀⁻‖, (m,k) = (1, 0.5) | sup\|ρ̂\| sur Ω ∈ [1e-9, 1] | 0.44 (borne m k/H + k = 1) |
| ‖χ₀⁺‖ = ‖χ₀⁻‖, (m,k) = (3, 2) | sup\|ρ̂\| | 0.49 (borne 8) |
| ‖χ₀⁺‖ = ‖χ₀⁻‖, (m,k) = (0.3, 1) | sup\|ρ̂\| | 0.99 (borne 1.3) |
| c ≠ 0, (m,k) = (1, 0.5) | Ωρ̂ à Ω = 1e-9 ; sup\|ρ̂ − c/Ω\| | 0.6000000 = c ; 0.35 |
| c ≠ 0, (m,k) = (3, 2) | Ωρ̂ à Ω = 1e-9 ; sup\|ρ̂ − c/Ω\| | 1.8000000 = c ; 0.47 |

Dans tous les cas, la norme est conservée à 2e-14 près. La réserve FLRW (« needs a separate estimate ») est honnête.

**(e) Plancherel et convergence dominée.** Pour un mode normalisé, |Ωu†(α·k)u + m u†βu| ≤ Ω₁k + m. Le majorant (Ω₁k + m)|f̂|² est intégrable si et seulement si ∫k|f̂|² < ∞ (‖f‖ étant fini). La limite ponctuelle est m(1−2w) avec w = 1/(e^{2πm/H}+1). L'identité 1 − 2/(e^{2πx}+1) = tanh(πx) est vérifiée à 1e-16. Les termes croisés entre hélicités s'annulent : α·k et β commutent avec l'hélicité, et des spineurs d'hélicités différentes sont orthogonaux. La condition est juste et suffisante. Elle est d'ailleurs automatique pour f = (1−P)g avec g à données lisses à support compact, car |f̂| ≤ |ĝ| et ĝ décroît vite (R-2).

**(f) Masse ΛCDM et Prop. 4.** [5] : en signature (−,+,+,+), R = 8πGρ_m + 4Λ (le rayonnement est sans trace) et 12H∞² = 4Λ. On obtient m_eff = m(1 − R/12H∞²) = −m ρ_m/(4ρ_Λ), qui s'annule sur de Sitter. |m_eff| ∝ a⁻³ = Ω³ vérifie les trois conditions : (a) ∫Ω³dt < ∞ ; (b) m a ∝ Ω² est borné ; (c) m = Ωμ avec μ ∝ Ω², lisse. L'affirmation est juste pour |m_eff|. Mais m_eff est **négatif** pour m > 0, alors que la Prop. 4 suppose m(t) ≥ 0 (C-2).

**(g) Prop. 2(c) et Prop. 1.** Signes vérifiés en R1.2. La nouvelle fin de preuve de la Prop. 1 (« along θ = 2πn ») est exacte pour m > 0 (R-1).

### R1.4 Note compagnon

Le diff compte sept retouches, toutes listées (E5.1 à K5.6, C4.4) ; toutes sont appliquées. On ne peut pas contrôler ici la justesse de « (3.3)–(3.6) of Friedrich 2017 » ni des attributions aux auditeurs (C-6, R-5).

---

## R2. Erreurs, contradictions ou surclassements introduits ; modifications hors liste

**C-1 (correction ; surclassement introduit par la correction E6.1).** §4.4 : « This is a fine-tuning of a new scale against H∞, not a mechanism, but it is not excluded. » Le modèle donne m_eff ∝ ρ_m pendant toute l'ère de matière, donc m_eff(z) = m_eff(0)(1+z)³. Pour l'électron, la masse varierait d'un facteur 8 dès z = 1 et d'environ 10⁹ à la recombinaison. C'est incompatible avec les bornes observationnelles bien établies sur la variation de m_e (spectres de quasars, CMB). « Not excluded » n'est vrai qu'au sens des conditions de la Prop. 4. Il faut écrire : « not excluded by the conditions of Proposition 4; for a mass measured today, it implies m_eff ∝ (1+z)³ during matter domination, which observations of m_e exclude ». La concordance (E6.1, « issue ajustée, non exclue ») hérite de la même imprécision.

**C-2 (correction).** Même phrase : m(1 − R/12H∞²) = −mρ_m/(4ρ_Λ) < 0 sur ΛCDM, alors que la Prop. 4 est énoncée pour m(t) ≥ 0. La conclusion tient après le changement constant ψ → γ₅ψ, qui inverse le signe de la masse, ou en écrivant |m_eff|. Il faut le dire.

**C-3 (correction ; incohérence introduite par C8).** La première phrase de l'Annexe A dit encore : « has the form ψ̄ΓDψ … where D is the identity or one covariant derivative ». La troisième puce ajoute des termes ∇ψ̄σ∇ψ, qui ne sont pas de cette forme. Il faut étendre la phrase (« or ∇ψ̄ Γ ∇ψ when no second-order term results »).

**C-4 (correction ; incohérence de titre).** Le titre de la Rem. 2 est devenu « Formal regularity, and the sources on solutions », mais l'introduction (l. 43) dit toujours « summarises the formal regularity of the coupled systems ». C'est VA-2 E7.4, appliqué à moitié. Il faut ajouter « and, for a test field, the sources on solutions ».

**Contradictions internes.** Je n'en trouve aucune autre dans l'article. Contrôles faits :
- Prop. 3 (de Sitter) contre Prop. 4(b) (FLRW, ‖χ₀⁺‖ ≠ ‖χ₀⁻‖ seulement) ;
- Déf. 1(c) corrigée contre Rem. 2(1), (3) et (4) ;
- §4.3 contre §5 contre Rem. 2(4) (k ≠ 0) ;
- Prop. 5(b) et (c) contre Lemme 2 et Prop. 4 ;
- résumé (i) et (iii) contre le corps.

**Modifications hors liste.** Toutes viennent des rapports, sans contenu nouveau. Elles sont bénignes.
- VA-2 C1.5 : suites θ = 2πn dans la preuve de la Prop. 1.
- VA-1 C4(iii) / VA-2 K1.1 : « Maxwell field is a background, A = 0, no back-reaction ».
- VA-2 C4.5 / E7.4 : titre de la Rem. 2.
- VA-2 K3.1 : « the coupling could reintroduce poles », dans l'article (Rem. 2(4), §5) et dans la note (« first stage … could reintroduce poles »).
- Seconde moitié de VA-1 C10 : « (b) remains true, but its physical reading assumes … ».
- VA-2 C3.6 : « its coefficient depends on the state », résumé (iii).

Aucun résultat nouveau n'apparaît hors chantier. Seul C-1 est un léger surclassement.

**Note compagnon.**

**E-1 (erreur, résiduelle).** Résumé : « a power series for single-exponent solutions, bounded without limit otherwise ». Pour k = 0 avec χ₀⁺ et χ₀⁻ non nuls, la source est nulle : le tableau de la note le dit lui-même (ligne k = 0, source 0) et la Rem. 2(4) de l'article aussi. C'est exactement le défaut E2/E3.2 corrigé dans l'article et non répercuté. La première ligne du tableau (« both exponents present ») devrait aussi porter « k ≠ 0 ». Correction : « bounded without limit for solutions with both exponents and **k** ≠ 0 ».

**C-5 (correction ; incohérence entre pièces).** La définition de la régularité formelle dans la note (l. 33) garde l'ancienne formulation : « contain no negative powers of Ω and no ln Ω; we also count as irregular … ». Elle ne suit pas la Déf. 1(c) corrigée (« depend smoothly on Ω up to Ω = 0 »). Avec cette formulation, le « if and only if m = Ωμ with μ smooth » du §2 de la note n'est plus garanti littéralement. L'objection E3 de VA-1 n'est levée que si les jets de ψ_r de tous ordres sont inclus ; même alors, μ = 1 + Ω² sin(1/Ω) ne produit au premier ordre aucune puissance négative littérale. Il faut aligner la note sur l'article.

**C-6 (correction ; traçabilité).** Note l. 87 : « The spin-connection terms cancel in the symmetric part (derived independently by the two auditors) ». Selon VA-2, NOTE-207 n'attestait qu'une dérivation par RA-1, et VA-2 demandait une source. Si « the two auditors » désigne VA-1 (R2) et RA-1, il faut le dire. Sinon, l'attribution dépasse ce que les pièces attestent. Je n'ai pas pu le vérifier sous isolement.

---

## R3. Constats non appliqués (§3 de la concordance)

| Constat | Jugement | Motif |
|---|---|---|
| VA-2 C1.1 (a croissant contre a → ∞) | acceptable | J'ai relu les preuves : aucune n'utilise la monotonie de a. La Prop. 1 n'utilise que la continuité et la finitude du temps conforme. La Prop. 4(a) utilise la monotonie de θ, qui vient de m ≥ 0. La Prop. 3 est restreinte à de Sitter. |
| VA-2 K6.4 (facteur à cinq chiffres) | acceptable | VA-1 a recalculé le poids (écart ≤ 7e-7 pour m/H ≤ 1, tableau V5). Le texte cite Boonpan et n'affirme aucun contrôle propre. |
| VA-2 K6.6 (historique) | acceptable | Voir toutefois R-7 sur l'étiquette de version. |
| VA-1 R9 (Prop. 5 sans titre) | acceptable | Purement formel. La numérotation automatique donne bien 5. |

S'y ajoutent deux reports non déclarés (K6.5 « Prop. 1 alone … » et K6.2 « Higgs symmetric point ») et le point non traité de VA-1 C5 (R-6, R-8). Tous sont acceptables sur le fond, mais la concordance devrait les déclarer.

---

## Remarques

- **R-1.** Prop. 1 : « Let m ≠ 0 » et, dans la preuve, « since θ → ∞ ». Pour m < 0, θ → −∞. Ce défaut est antérieur (« θ = mt → ∞ » en v2.5 auditée) et sans conséquence. On peut écrire « |θ| → ∞ » ou supposer m > 0 par ψ → γ₅ψ.
- **R-2.** §4.3 : la condition ∫k|f̂|² < ∞ est automatique pour f = (1−P)g avec g à support compact. On peut le dire pour éviter de laisser croire à une hypothèse supplémentaire.
- **R-3.** Annexe : le terme ∇ψ̄σ^{ab}∇ψ est anti-hermitien et doit porter un i (i∇ψ̄σ∇ψ, comme chez VA-1) ; la version γ₅ est réelle. Lemme 2 : préciser la convention P_L = (1−γ₅)/2 pour la chiralité remise à l'échelle.
- **R-4.** Related work : « up to terms of relative size e^{−2πm/H} » vaut pour le poids (norme au carré). En amplitude, l'ordre est e^{−πm/H}. Il vaut mieux écrire « relative weight ».
- **R-5.** Note : « (3.3)–(3.6) of Friedrich 2017 ». VA-2 rapporte que NOTE-207 établissait le résultat sur (3.3)–(3.7). Il faut vérifier si (3.7) est l'équation de Weyl, traitée à part (« the other »), ou si elle a été perdue.
- **R-6.** VA-1 C5, dernier point, n'est pas traité. « Ω⁻³T_tt = Ωρ̂ is regular » (corps et résumé) : pour une solution à deux exposants, Ωρ̂ = mB + Ωk·J contient un terme Ω^{1∓2iμ}. La densité a donc une limite mais n'est pas C¹. Comme la Déf. 1 donne maintenant des notions précises, « has a limit » serait plus juste que « regular ».
- **R-7.** La version corrigée garde la même étiquette (« version 2.5 », 16 octobre 2026) que la version auditée, et la Provenance ne mentionne ni l'audit VA-1/VA-2 de la v2.5 ni ses corrections. Pour la traçabilité, il faudrait une étiquette distincte (2.5.1, par exemple) ou une phrase dans la Provenance. La note compagnon dit « audited by two isolated AI agents each » et marque en même temps RJ v2 « not re-audited » : la nuance doit passer dans le résumé de la note. Elle s'applique aussi à la Rem. 2 de l'article (« confirmed by isolated AI auditors »).
- **R-8.** La concordance §2 dit « K6.2, K6.5 : rétablies ». Deux éléments ne le sont pas : « Proposition 1 alone … would not justify it » et « mechanism … symmetric point ». Il faut corriger la concordance ou les rétablir.

---

## R4. Verdict

| Pièce | Erreur restante parmi les points audités | Corrections |
|---|---|---|
| Article (dirac-mass-scri-v2.5.tex) | **aucune** | C-1, C-2, C-3, C-4 (une ligne chacune) |
| Note compagnon (companion-formal-regularity.tex) | **une** : E-1 (k = 0 dans le résumé), résidu du constat concordant E2/E3.2 | C-5, C-6 |

**Verdict VA-3 :** au sens strict de la consigne, la v2.5 corrigée **ne peut pas être entée en l'état**, à cause d'E-1 dans la note compagnon. L'article seul satisfait le critère : toutes les corrections annoncées sont appliquées et justes, et les calculs demandés sont confirmés. Aucune nouvelle erreur mathématique n'a été introduite. Après E-1 et C-1 à C-6, toutes locales et contrôlables par diff, l'ensemble peut être enté sans nouvel audit complet. Les remarques R-1 à R-8 sont facultatives. La décision reste celle de l'opérateur.

## Non-surclassement

Ce rapport a été établi par un agent IA isolé et n'a été relu par aucun humain. Les références externes n'ont pas été consultées : les attributions de la concordance §2 (E2.x, C2.x, K2.1) n'ont été contrôlées que pour leur conformité aux corrections proposées par VA-2. Les scripts du programme n'ont pas été relancés. C-1 s'appuie sur des bornes observationnelles connues sur la variation de m_e, rappelées de mémoire et non revérifiées ici.
