# RAPPORT AL-1 : audit aveugle de l'extrait « ARTICLE v2.4, propositions »

Auditeur isolé. Fichiers ouverts : la consigne, `EXTRAIT-ARTICLE-v2.4-props.tex`, et mes propres fichiers dans `work_al1/` (script `checks.py`). Aucun autre fichier local n'a été ouvert.

Outils : alphaXiv (lecture PDF par requêtes, découverte), WebSearch. Chaque titre cité ci-dessous a été lu sur la première page de l'article lui-même, sauf mention « titre lu dans la bibliographie de ... ».

Code des niveaux de lecture : [titre], [résumé], [sections lues : ...], [texte] (texte quasi intégral).

---

## Synthèse

| Question | Réponse courte |
|---|---|
| Q1 | La Proposition « Structure at scri » a **le même contenu analytique** que le Lemme 3.1 de arXiv:1902.09144. La correspondance passe par t = -ln(Ω)/H, η = τ/H et λ = ±k. La borne de l'extrait est même un peu plus forte. Le Lemme 3.1 imprimé contient une coquille : il manque le « -1 » dans la borne d'erreur. L'extrait doit citer ce lemme. |
| Q2 | Le caractère Hadamard est établi **sur de Sitter global** (feuilletage fermé), via Allen-Lütken (Prop. 4.5). En carte plate, les auteurs ne concluent ni que leur état FP est Hadamard, ni qu'il est la restriction de Bunch-Davies. Ils argumentent même qu'il ne l'est pas. |
| Q3 | N_out = 1/(e^{2πm/H}+1) et cos γ_out = tanh(πm/H). L'auteur présente ce plateau comme **standard** (« recover the standard Gibbons-Hawking Fermi-Dirac plateau »). |
| Q4 | Axiome 1 (Déf. 4.1) : différence des ⟨:T:⟩ = Tr[D̃^can (ω1^- - ω2^-)] pour deux états quasi-libres de différence lisse. Le Théorème 4.1 (c = -1/6, λ = λ_m) établit les axiomes de Wald réduits. |
| Q5 | **Oui.** ω_f est l'état quasi-libre pur de projecteur P' = P + \|f⟩⟨f\|. La différence des fonctions à deux points est de rang un, ± f ⊗ f̄. Preuve courte donnée ci-dessous et vérifiée numériquement. |
| Q6 | **Oui.** La condition de Hadamard est locale (ensemble de front d'onde ou forme locale). La carte plate est un ouvert globalement hyperbolique causalement convexe. |
| Q7 | Aucun travail trouvé ne contient les Propositions « Gauge » ou « Energy density » pour Dirac. **Bachelot (arXiv:2003.03356) contient l'analogue scalaire de « Variable mass »** : c'est un résultat partiel à citer. **Friedrich (arXiv:1601.04506) concerne directement la Proposition CCC (b)** : la poussière, dont la densité rescalée a un pôle en Ω^{-1}, admet un 𝓘⁺ lisse. |
| Q8 | Friedrich juge « forte » l'hypothèse de Penrose (seuls des champs sans masse près du raccord) et dit qu'aucun processus connu ne la justifie. Il se restreint au scalaire « only for the purpose of illustration, other fields could be considered as well ». |

---

## Q1. Lemme 3.1 de arXiv:1902.09144 contre la Proposition « Structure at scri »

**Source.** Dappiaggi, Finster, Murro, Radici, *The Fermionic Signature Operator in de Sitter Spacetime*, arXiv:1902.09144v2. Niveau : [sections lues : résumé, 1, 2.1, 2.5, 3.1 (avec la preuve complète du Lemme 3.1), 3.2 (Lemmes 3.2 à 3.4, Prop. 3.5 à Th. 3.8), 3.3, 4.1, 4.2, 4.5 (début), fin de 4.6].

**Énoncé exact.** Cadre : carte plate, signature (+,-,-,-), R(t) = e^t, donc H = 1. On a γ⁰ = diag(1,1,-1,-1), ψ_m = R^{-3/2}(u₁ φ_{k,±}, u₂ φ_{k,±}) et l'EDO (3.8) :

  i d/dt (u₁,u₂) = [[m, -λe^{-t}], [-λe^{-t}, -m]] (u₁,u₂), avec λ = ±|k|.

> **Lemma 3.1.** Asymptotically as t → +∞, every solution of (3.8) is of the form u(t) = (e^{-imt} f₁^∞, e^{imt} f₂^∞) + E(t), with the error term bounded by ‖E(t)‖ ≤ ‖f^∞‖ exp(|λ| e^{-t}).

- Hypothèses : aucune au-delà de l'EDO (m réel, k fixé, solution non triviale).
- Coordonnées : temps propre t, avec H = 1. Le temps conforme τ = -e^{-t} n'est introduit qu'après le lemme, pour l'étude en t → -∞.
- Preuve : ansatz u = diag(e^{-imt}, e^{imt}) f, inégalité de Kato, puis Grönwall. Les auteurs attribuent l'argument à Finster-Reintjes [20, Lemma 6.3] (feuilletage fermé ; titre lu dans la bibliographie de 1902.09144).

**Coquille dans le lemme imprimé.** La borne (3.10) ne tend pas vers 0, donc elle ne contrôle pas une erreur. Dans la preuve, intégrer d/dt exp(∫_t^{t_max} |λ|e^{-s}ds) de t à t_max donne exp(...) - 1, et non exp(...). La borne correcte est donc ‖E(t)‖ ≤ ‖f^∞‖(exp(|λ|e^{-t}) - 1) = O(e^{-t}). C'est cohérent avec le Lemme 4.2 du même article, qui écrit « hence entailing exponential decay ».

**Dictionnaire des variables.**

```
 Extrait (H général)                       1902.09144 (H = 1)
 ------------------------------------      --------------------------------------
 a = -1/(Hη) = e^{Ht},  Ω = 1/a = e^{-Ht}   R(t) = e^t,  τ = -e^{-t}
 η = τ/H,  |η| = e^{-Ht}/H                  e^{-t} = |τ|
 ψ̂ = Ω^{-3/2} ψ = a^{3/2} ψ  ->  u          ψ = R^{-3/2}(u₁φ, u₂φ)   (même u)
 β = γ⁰, α·k (k = |k|)                      bloc diag(m, -m), hors diag. -λe^{-t}, λ = ±|k|
 U₀ = exp(iβ (m/H) ln Ω) = exp(-iβ m t)     diag(e^{-imt}, e^{imt})
 χ(η)                                        f(t)
 χ₀                                          f^∞
 U₀(χ - χ₀)                                  E(t)
 ‖χ-χ₀‖ ≤ k|η| ‖χ₀‖ = (k/H)e^{-Ht}‖χ₀‖      ‖E‖ ≤ ‖f^∞‖(e^{|λ|e^{-t}} - 1)  (corrigé)
```

Dans chaque secteur d'hélicité, l'équation (eq:hk) de l'extrait se réduit, par le changement η → t (dη = dt/a), exactement à (3.8) : i∂_t u = (βm + α·k/a)u. Les deux « u » coïncident, car Ω^{-3/2} = R^{3/2}.

**Comparaison.**
1. La forme asymptotique est identique : u = U₀χ₀ + O(e^{-Ht}), avec la phase de Compton e^{∓imt} sur les sous-espaces propres β = ±1.
2. La borne de l'extrait, k|η|, est linéaire. Elle est donc **légèrement plus forte** que la borne corrigée du lemme, car x ≤ e^x - 1. Elle découle de l'unitarité (Lemme « Constant norm »), que Grönwall n'utilise pas.
3. L'extrait garde H général et ajoute le corollaire « u n'a pas de limite en η → 0⁻ ». Ce corollaire est immédiat, puisque χ₀ ≠ 0 par conservation de la norme.

**Verdict : même contenu analytique**, avec une constante marginalement meilleure et une formulation en variables conformes. L'extrait range « Proposition dirac » parmi les résultats « Established here ». Il faut donc citer le Lemme 3.1 de 1902.09144 (et Finster-Reintjes II, Lemma 6.3, pour le feuilletage fermé), et présenter la proposition comme une reformulation conforme d'un résultat connu.

**Vérification numérique** (`work_al1/checks.py`, H = 1, m = 3, k = 2, DOP853, rtol 1e-11) :
- la borne de l'extrait et la borne DFMR corrigée sont toutes deux respectées sur η ∈ [-5, -1e-7] ;
- le rapport maximal err/(k|η|) vaut 0,30 ;
- ‖u‖ est conservée à 6e-11 près.

---

## Q2. Caractère Hadamard du Bunch-Davies spinoriel dans 1902.09144

Niveau : [sections lues : résumé, 1, 2.5, 3.3, 4.2, Prop. 4.5 et sa preuve].

- **Région où le caractère Hadamard est établi : de Sitter global**, en feuilletage fermé R × S³ avec R(T) = cosh T. Le résumé dit : « In the case of a closed slicing, we construct the fermionic signature operator and show that the ensuing state is maximally symmetric and of Hadamard form, thus coinciding with the counterpart for spinors of the Bunch-Davies state ». La Proposition 4.5 identifie l'état FP à « the spinorial Bunch-Davies state ». Ce dernier est défini en §2.5 comme l'unique fonction à deux points maximalement symétrique compatible avec la forme de Hadamard, selon Allen-Lütken [1].
- **Carte plate (« cosmological de Sitter »).** La propriété de forte oscillation de masse échoue, à cause des termes de bord. Une « mass decomposition » (Th. 3.8) suffit pourtant à construire un état FP. Les auteurs écrivent en introduction : « we can conclude neither that it is of Hadamard form nor that it is the restriction of the global Bunch Davies state to the flat cover ». En §3.3, ils vont plus loin. S'appuyant sur [9] (Dappiaggi-Hack-Pinamonti, arXiv:1009.5179), ils notent que le BD spinoriel ne sélectionne que des fréquences négatives sur 𝓘⁻ (τ → -∞). Ils en concluent que l'état FP de la carte plate « cannot coincide » avec le BD, puisque des fréquences positives apparaissent en τ → 0.
- L'article **n'affirme rien** sur le caractère Hadamard de la restriction du BD à la carte plate. Il ne l'étudie pas. Voir Q6 pour la réponse.

---

## Q3. arXiv:2610.00410 : occupation tardive d'un mode de Dirac massif

**Source.** S. Boonpan, *Fermionic Particle Creation in Curved Spacetime: Physical Bloch-Vector Dynamics and Exact de Sitter Scaling*, arXiv:2610.00410v1. Niveau : [sections lues : résumé, 1, 2 (partiel), 4.2 (partiel), 5.1, 5.2, 5.5, 5.6, 6.1 à 6.4, 7.1, 8, annexe A (fin, A.31 à A.37)].

- **Expression.** Le mode est préparé dans l'état d'énergie positive instantanée à x = -kη ≫ 1 (vide adiabatique de type BD). On a alors, éq. (5.38), (5.53) et (A.36) :
  N_out = lim_{x→0⁺} F_ν(x) = |β_k|² = 1/(exp(2πm/H) + 1), avec |α_k|² = 1/(1 + e^{-2πν}).
  C'est une limite infrarouge physique à k comoving fixé (η → 0⁻, k/a → 0). Elle est indépendante de k et suppose ν = m/H > 0. La limite tardive est prise avant la limite sans masse ; les deux limites ne commutent pas (§5.5).
- **Relation avec tanh.** L'éq. (5.56) donne sin²(γ_out/2) = 1/(e^{2πν}+1), d'où l'éq. (5.57) : **cos γ_out = tanh(πν)**. Autrement dit 1 - 2N_out = tanh(πm/H). C'est exactement la quantité ‖χ₀⁺‖² - ‖χ₀⁻‖² (pour ‖χ₀‖ = 1) qu'utilise l'extrait. Identité vérifiée numériquement.
- **Nouveau ou standard ?** **Standard.** Le résumé dit « recover the standard Gibbons-Hawking Fermi-Dirac plateau ». En §5.6 et (A.37), c'est le facteur de Fermi-Dirac à T_dS = H/2π. Le §7.1 liste les résultats revendiqués comme nouveaux : loi d'échelle F_ν(-kη), échelle non adiabatique p = m/√2, couche limite à petite masse. Le plateau n'y figure pas. Le §8 dit : « reproduces the established asymptotic occupation ». L'article cite Gibbons-Hawking 1977 et Cotăescu 2002 [9, 22] pour ce contexte.

**Remarque d'audit sur l'extrait (§energy).** La formule Ω(ω_f - ω)(ρ̂) → m tanh(πm/H)‖f‖² est exacte **mode par mode**. Elle l'est aussi **après intégration spatiale** pour un paquet d'onde f, par Plancherel, puisque U₀ ne dépend pas de k et que N_out non plus. Ponctuellement en x, des termes croisés entre k différents subsistent. Le signe n'est alors plus garanti. Il faut aussi que f soit un paquet lisse (données de Cauchy à support compact), et non un mode plan. Je recommande de préciser « intégrée sur une tranche » ou « pour un paquet d'onde ».

---

## Q4. arXiv:0904.0612 : axiome 1 (Dirac) et théorème d'existence

**Source.** Dappiaggi, Hack, Pinamonti, *The extended algebra of observables for Dirac fields and the trace anomaly of their stress-energy tensor*, arXiv:0904.0612v1 (Rev. Math. Phys. 21 (2009) 1241, référence lue dans la bibliographie de 1009.5179). Niveau : [sections lues : résumé, 1 (partiel), 3.3 (début, Déf. 3.2 et notations ω^±), 4.2 (Déf. 4.1 et commentaires), 4.3 (Th. 4.1 et partie de la preuve)].

**Notations.** ω^+(f,h) = ω(ψ(h)ψ†(f)) et ω^-(f,h) = ω(ψ†(f)ψ(h)) (éq. 20).

**Énoncé exact de l'axiome 1** (Définition 4.1, « strong version of Wald's axioms ») :

> 1. Given two quasifree states ω₁ and ω₂, such that ω₁^-(x,y) - ω₂^-(x,y) is a smooth bispinor, ω₁(:T_μν(x):) - ω₂(:T_μν(x):) is equal to Tr[D̃^can_μν (ω₁^-(x,y) - ω₂^-(x,y))].

Ici D̃^can_μν = ½ γ_(μ(∇_ν) - g_ν'ν) ∇_ν'), avec D^can_μν = -D̃^can_μν D'_y : c'est l'opérateur canonique issu du tenseur classique (31).

**Hypothèses.**
- États **quasi-libres**, de différence ω₁^- - ω₂^- **lisse**.
- Dans le commentaire 1 et dans la preuve, ce sont des états **de Hadamard** (ω_i^- = -D'_y(H^- + W_i)/(8π²)), ce qui est nécessaire pour l'algèbre étendue.
- Les axiomes 1 à 4 forment la « reduced version » ; l'axiome 5 (pas de dérivées de la métrique d'ordre > 2) est abandonné.

**Théorème d'existence : Theorem 4.1.**
> Let λ_m = 2 exp(7/2 - 2γ) m^{-2} for m ≠ 0 and λ_m arbitrary for m = 0, [...] choose the Hadamard bidistribution to be the one with λ = λ_m and let ω(:T_μν(x):) be defined as in (33), with the differential operator D_μν = D^{-1/6}_μν defined as in (34). Then ω(:T_μν(x):) fulfils the reduced version of Wald's axioms.

Le théorème donne aussi l'anomalie de trace. Le choix c = -1/6 correspond à l'ajout de -(1/6)L g_μν au tenseur classique. Pour l'axiome 1, la preuve note que le terme ajouté, proportionnel à g_μν Tr[(D'_x D'_y - P_y) H^-] = -12 g_μν Tr[V₁], est indépendant de l'état (« axiom 1 holds for our regularisation scheme and two Hadamard states ω₁, ω₂ »).

**Conséquence pour l'extrait.** Combiné avec Q5, si ω est quasi-libre Hadamard et f une solution lisse, alors ω_f est quasi-libre et Hadamard (différence de rang un, lisse). L'axiome 1 donne ω_f(T) - ω(T) = Tr[D̃^can(±f ⊗ f†)]. C'est le tenseur classique canonique de f, sans ambiguïté de renormalisation. L'affirmation de l'extrait est donc correcte sous ces hypothèses. Je recommande de citer la Déf. 4.1 et le Th. 4.1, et d'exiger explicitement que ω soit Hadamard et f lisse.

---

## Q5. (raisonnement) a*(f) appliqué au vecteur GNS d'un état quasi-libre pur

**Convention.** CAR(𝔥), ω quasi-libre pur avec ω(a*(u)a(v)) = ⟨v, P u⟩, où P est un projecteur (sous-espace « occupé », la mer de Dirac en langage fermionique). Soit f ∈ Ran(1 - P) avec ‖f‖ = 1, Ω_ω le vecteur GNS et Φ = a*(f)Ω_ω.

**Réponse : oui.** ω_f est quasi-libre et pur, de projecteur **P' = P + |f⟩⟨f|**. C'est encore un projecteur, puisque f ⊥ Ran P.

**Preuve courte.**
1. *Caractérisation de ω.* Pour g ∈ Ran(1-P), on a ω(a*(g)a(g)) = 0, donc a(g)Ω_ω = 0. Pour h ∈ Ran P, on a ω(a(h)a*(h)) = ⟨h,(1-P)h⟩ = 0, donc a*(h)Ω_ω = 0.
2. *Norme.* ‖Φ‖² = ω(a(f)a*(f)) = ⟨f,(1-P)f⟩ = 1.
3. *Annihilateurs de P'.*
   - Si g ∈ Ran(1-P'), alors g ⊥ f et g ∈ Ran(1-P), d'où a(g)Φ = ⟨g,f⟩Ω_ω - a*(f)a(g)Ω_ω = 0.
   - Si h = h_P + c f ∈ Ran P', alors a*(h_P)a*(f)Ω_ω = -a*(f)a*(h_P)Ω_ω = 0 et a*(f)² = 0, d'où a*(h)Φ = 0.
4. *Unicité.* Soit φ un état vérifiant φ(c*c) = 0 pour tous les « annihilateurs » c de P', c'est-à-dire a(g) avec g ∈ Ran(1-P') et a*(h) avec h ∈ Ran P'. Par Cauchy-Schwarz, φ(Xc) = 0 = φ(c*X). Tout monôme se ramène, par les CAR, à l'ordre normal relatif à P'. Donc φ est déterminé et coïncide avec l'état quasi-libre ω_{P'}, qui vérifie ces conditions. Ainsi ω_f = ω_{P'}, qui est pur, car P' est un projecteur.

**Différence des fonctions à deux points (rang un).**

  ω_f(a*(u)a(v)) - ω(a*(u)a(v)) = ⟨v,f⟩⟨f,u⟩
  ω_f(a(v)a*(u)) - ω(a(v)a*(u)) = -⟨v,f⟩⟨f,u⟩

Pour le champ de Dirac (ψ = a(·) + b*(·), ou formalisme auto-dual d'Araki), cela donne ω_f^∓ - ω^∓ = ±f(x)f(y)† (projecteur de base P' = P + |f⟩⟨f| - |Γf⟩⟨Γf|). Si f est une solution lisse à données de Cauchy compactes, la différence est un bispineur lisse, donc ω_f reste Hadamard si ω l'est.

**Vérification numérique** (`checks.py`, 4 modes, Jordan-Wigner, P de rang 2 aléatoire) :
- G_ω = P ;
- ‖Φ‖ = 1 ;
- G_{ω_f} = P + |f⟩⟨f| ;
- G_{ω_f} est un projecteur ;
- la factorisation de Wick à 4 points est vérifiée pour ω_f.

Je n'ai pas retrouvé, dans les sources lues, d'énoncé publié identique avec texte vérifié. La preuve ci-dessus est autonome.

---

## Q6. Restriction à la carte plate d'un état Hadamard de de Sitter global

**Réponse : oui.**

**Argument.**
1. La carte plate O est un ouvert de dS₄ globalement hyperbolique et causalement convexe. C'est l'intérieur du futur d'un point de 𝓘⁻ dans la compactification, bordé par l'horizon cosmologique passé. Par covariance locale, l'algèbre CAR de O s'injecte dans celle de dS global (0904.0612, §3.2, titre de section lu).
2. La condition de Hadamard pour Dirac porte sur l'ensemble de front d'onde de ω^± (Kratzert, Hollands, Sahlmann-Verch). Pour la restriction, WF(ω^±|_{O×O}) = WF(ω^±) ∩ T*(O×O). L'ensemble « de Hadamard » de O coïncide avec celui de dS restreint à O×O. En effet, une géodésique nulle de dS joignant deux points de O reste dans O, par convexité causale.
3. De façon équivalente, la forme locale (éq. 2.10 de 1902.09144) porte sur des voisinages géodésiquement convexes. Le texte de 1902.09144 (§2.5) le dit : « this local characterization of the Hadamard condition is fully equivalent to the microlocal one ». Tout point de O possède un tel voisinage contenu dans O.

La restriction du BD spinoriel global (Hadamard d'après la Prop. 4.5 de 1902.09144) à la carte plate est donc Hadamard.

**Références.**
- Dappiaggi-Hack-Pinamonti, *Approximate KMS states for scalar and spinor fields in Friedmann-Robertson-Walker spacetimes*, arXiv:1009.5179. Niveau : [sections lues : résumé, 1, 2.3 (partiel), 3.2, 4 (début), 4.2]. Leur Théorème 4.2 construit des états de Dirac de Hadamard sur FRW plat à phase exponentielle initiale (ce qui inclut la carte plate de dS), à partir de données sur 𝓘⁻.
- Pour le critère microlocal, titres lus dans la bibliographie de 1009.5179 : Radzikowski, *Micro-Local Approach To The Hadamard Condition In Quantum Field Theory On Curved Space-Time* (CMP 179, 1996) ; Sahlmann-Verch, *Microlocal spectrum condition and Hadamard form for vector valued quantum fields in curved space-time* (RMP 13, 2001) ; K. Sanders, *Equivalence of the (generalised) Hadamard and microlocal spectrum condition for (generalised) free fields in curved spacetime* (arXiv:0903.1021).

**Point à préciser dans l'extrait.** Le « Bunch-Davies state » utilisé en §energy est défini par les modes de la carte plate (fréquence positive en η → -∞). Il faut dire qu'il coïncide avec la restriction du BD global. 1902.09144, §3.3, l'affirme en s'appuyant sur 1009.5179. C'est ce qui garantit son caractère Hadamard, nécessaire pour Q4.

---

## Q7. Recherche de travaux antérieurs

**Requêtes documentées (9).**

| # | Outil | Requête |
|---|---|---|
| 1 | alphaXiv discover | « Massive fermion or Dirac field near the crossover surface / future conformal boundary in Penrose CCC; fading of rest mass; regularity of massive spinor at scri » |
| 2 | alphaXiv discover | « Asymptotic behaviour of massive Dirac fields at future conformal infinity of de Sitter, oscillating phase, rescaled field, stress-energy near scri, gauge transformation » |
| 3 | alphaXiv discover | « Dirac fermion with time-dependent (decaying) mass in expanding de Sitter or FLRW, condition for conformal regularity at future infinity, mass decaying like 1/a, rescaled energy density » |
| 4 | alphaXiv discover | « Propagation of massive Dirac or spinor fields across the bang surface in CCC with decaying mass; follow-ups of Bachelot » |
| 5 | WebSearch | `"conformal cyclic cosmology" massive Dirac field electron rest mass crossover arXiv` |
| 6 | WebSearch | `Tod "The equations of conformal cyclic cosmology" arXiv` |
| 7 | WebSearch | `Penrose conformal cyclic cosmology electron mass "fade" OR "decay" Dirac equation conformal infinity singular mass term m/Omega` |
| 8 | WebSearch | `Lübbe "Conformal scalar fields, isotropic singularities and conformal cyclic cosmologies" massive fields` |
| 9 | WebSearch | `Bachelot Dirac field conformal cyclic cosmology pre-big bang massive spinor propagation across bang surface` |

**Candidats examinés.** Légende des colonnes : G = Prop. « Gauge », E = Prop. « Energy density », V = Prop. « Variable mass ».

| Réf. (titre vérifié) | Niveau de lecture | G | E | V | Commentaire |
|---|---|---|---|---|---|
| Bachelot, *Propagation of Massive Scalar Fields in Pre-Big Bang Cosmologies*, arXiv:2003.03356 | [sections lues : résumé, I, II (partiel), III, IV (Lemme IV.1, Prop. IV.3), V (début)] | non | non | **partiellement** | Scalaire conformément couplé, masse dépendant du temps, cadre CCC. Condition de propagation triviale ∫ m²Ω̄² dτ < ∞, soit ∫ m² e^{Ht} dt < ∞ en de Sitter (éq. III.26). Condition faible ∫ m² dt < ∞, avec renormalisation de Riccati (IV.4). **Analogue scalaire direct de V(a)** ; le coefficient m²a² borné correspond à m ≲ 1/a, comme V(b). Pas de spineur, pas de densité d'énergie. **À citer.** |
| Friedrich, *Sharp asymptotics for Einstein-λ-dust flows*, arXiv:1601.04506 | [sections lues : résumé, 1, 6 (début), 6.2, 8] | non | **partiellement (et en tension avec Prop. CCC (b))** | non | Ensemble ouvert de données Einstein-λ-poussière : 𝓘⁺ C^∞ (Th. 1.1). Densité rescalée ρ = Ω^{-3}ρ̂ régulière. Dans la convention de l'extrait (T̂ = Ω^{-2}T, ρ̂_extr = Ω^{-4}T_tt), cela donne ρ̂_extr = ρ/Ω, **un pôle simple en 1/Ω** : c'est l'image « gaz de particules au repos » de l'extrait. Donc un pôle de ce type n'empêche pas une frontière conforme lisse pour le système couplé. **À citer impérativement** à côté de Prop. CCC (b) et de sa parenthèse « not established here ». |
| Friedrich, *Smooth non-zero rest-mass evolution across time-like infinity*, arXiv:1311.0700 | [sections lues : résumé, 1, 2 (début), 3 avec Th. 3.1 et preuve partielle, 4 (Prop. 4.1), 5 (partiel)] | non | non | non | Scalaire seulement. Condition m² = 2λ/3. Déjà cité par l'extrait. Publié dans Ann. Henri Poincaré 16 (2015) 2215-2238 (référence lue dans les bibliographies de 1601.04506 et 2003.03356) : la clé « Friedrich2014 » devrait refléter 2015. |
| Roy, *dS/CFT Holography including Fermionic Fields*, arXiv:2609.34073 | [sections lues : résumé, 1, 2, 4 (partiel), 5.5, 6] | non | non | non | Contient la structure au bord : ψ ~ (-η)^{d/2 ± iMR} ψ_±, γ⁰ψ_± = ±ψ_±, et les poids Δ_± = d/2 ± iMR « for all non-zero M » (déjà reconnus comme connus par l'extrait). Son identité de Ward U(1) (§5.5) utilise une jauge A₀ = 0 et un paramètre indépendant de η : sans rapport avec G. |
| Tod, *The equations of Conformal Cyclic Cosmology*, arXiv:1309.7248 | [texte] | non | non | non | Matière près de 𝓘 : fluide de radiation, Maxwell et Λ. |
| Tod, *Some questions about Conformal Cyclic Cosmology*, arXiv:2202.10864 | [texte] | non | non (motivation qualitative) | non | Note que la poussière, ρ ∝ R^{-3}, domine la radiation sans mécanisme d'extinction. Question ouverte : « Can one implement mass fade-out? (Massless charged particles are usually regarded as problematical.) » |
| Tod, *Conformal methods in General Relativity with application to Conformal Cyclic Cosmology: A minicourse at IX IMLG*, arXiv:2102.02701 | [sections lues : 1.2.4, 2.2.1, 3.3 à 3.5, 3.6 (partiel)] | non | non | non | §3.4 : tenseur sans trace tardif supposé ; « not necessary for the appearance of a boundary I⁺ [...] one can for example find dust cosmologies with that property ». §3.5 : extinction de masse par Higgs inversé, « needs new physics ». |
| Meissner, Penrose, *The Physics of Conformal Cyclic Cosmology*, arXiv:2503.24263 | [sections lues : résumé, I, II (début), IV (extraits), annexe GWE] | non | non | non | Lissité conforme supposée au raccord (sauf aux points de Hawking) ; époque dominée par les ondes gravitationnelles. |
| Markwell, Stevens, *Toward fixing a framework for conformal cyclic cosmology*, arXiv:2212.06914 | [texte] | non | non | non | Mentionne « the asymptotic decay of rest-mass » comme hypothèse non traitée. |
| Szabados, *On gravity's role in the genesis of rest masses of classical fields*, arXiv:1802.04401 | [sections lues : résumé, 1, 2.1, 2.2, 3.3 (partiel), 4.3, 5] | non | non | non | Utile pour la discussion du mécanisme : avec couplage conforme du Higgs, le « reverse-BEH mechanism at the cosmological scale cannot provide the way in which the fields lose their rest mass », car la courbure moyenne tend vers √(Λ/3). Pertinent pour le dernier paragraphe de §ccc. |
| Dappiaggi et al., arXiv:1902.09144 | voir Q1 | non | non | non | Contient la Prop. « Structure at scri » (Q1). |
| Boonpan, arXiv:2610.00410 | voir Q3 | non | non | non | Seulement le facteur tanh, standard. |

**Verdict global Q7.**
- **G (Gauge)** : rien trouvé, dans la littérature CCC ou de Sitter, sur la paire « jauge qui fait converger ψ̂ pour un état particule » et « potentiel avec pôle non intégrable (m/eH) dΩ/Ω ». L'idée physique (retrait de la phase d'énergie de repos par A_t → A_t + m/e) est élémentaire. La nouveauté porte sur l'énoncé d'obstruction au raccord.
- **E (Energy density)** : non trouvé pour Dirac. Mais le pôle 1/Ω de la densité rescalée d'une matière massive au repos est implicite dans le traitement de la poussière par Friedrich (1601.04506). Ce traitement **affaiblit la portée de Prop. CCC (b)** : un 𝓘⁺ lisse existe malgré ce pôle, pour la poussière couplée à Einstein.
- **V (Variable mass)** : partiellement antérieur, en version scalaire, chez Bachelot (2003.03356). La version Dirac, avec l'ordonnancement strict (a) ⇐ (b) ⇐ (c), n'a pas été trouvée.

La phrase « Novelty » de §scope (« We have not found ... in the CCC literature ») devrait être amendée pour citer Bachelot et Friedrich 2016.

---

## Q8. Introduction de arXiv:1311.0700

**Source.** H. Friedrich, *Smooth non-zero rest-mass evolution across time-like infinity*, arXiv:1311.0700v2. Niveau : [sections lues : résumé, 1 (intégrale), 2 (début), 3, 4, 5 (partiel)].

- **Champs massifs près du raccord.** Citation : « In [13] [Cycles of Time] it has been assumed that there will be some past neighbourhood of the crossover surface in which only zero rest mass fields will be present. While it is far from obvious how massive fields behave at the end of an unlimited spatial expansion, this certainly seems to be a strong requirement. At present no process is known which would allow one to justify it. It is the main purpose of the following analysis to show that this restriction may not be necessary. »
- Il ajoute que la contrainte m² = 2λ/3 pourrait acquérir un pouvoir prédictif si l'on interprète le champ (« a relation between the cosmological constant and the dark matter ? »). Il estime m ≈ 4 × 10^{-33} eV.
- **Champs massifs autres que le scalaire.** Citations :
  - « The precise properties of the equations will depend there very much on the specific nature of the chosen matter field and each of them will need a special analysis. We shall concentrate here on the case of a non-linear scalar field ».
  - « it should be emphasized that the discussion in this article has been restricted to the scalar field only for the purpose of illustration, other fields could be considered as well. »
- Il écrit aussi qu'il « would be most interesting to understand the significance of condition (*) [...] and to see whether the system admits a range of masses for which the notion of crossover surface can be generalized ». Il note que « transitions from exponentially expanding to big bang phases are accompanied with losses of smoothness and that the insistence on too strict smoothness requirements may obstruct a modeling of such transitions ».

**Portée pour l'extrait.** Friedrich n'étudie aucun champ massif non scalaire. L'extension spinorielle de l'extrait (Remarque « Formal regularity ») répond donc bien à une question qu'il laisse ouverte. Sa dernière phrase invite cependant à ne pas lire « exiger un 𝓘⁺ lisse » comme la seule règle de raccord possible. L'extrait le reconnaît déjà en §ccc.

---

## Autres observations d'audit (hors questions)

1. La liste « Established here » de §scope inclut la Prop. « Structure at scri ». À requalifier en reformulation du Lemme 3.1 de 1902.09144 (Q1).
2. En §energy, préciser que ω est un état Hadamard quasi-libre et f un paquet d'onde lisse. Préciser aussi que la limite est prise après intégration spatiale (Q3, Q4, Q5).
3. Prop. CCC (b) : la parenthèse « Whether the conformal field equations with matter require exactly this boundedness is not established here » devrait renvoyer à Friedrich 1601.04506. Ce papier montre que, pour la poussière, une densité rescalée en Ω^{-1} est compatible avec un 𝓘⁺ C^∞.
4. Clé bibliographique « Friedrich2014 » : la version publiée est Ann. Henri Poincaré 16 (2015).
5. Vérifications numériques reproductibles : `/home/claude/LB/auditlb/work_al1/checks.py`.

---

## Références recommandées à l'article (titres vérifiés)

Titres lus sur la première page de l'article, sauf mention contraire.

1. C. Dappiaggi, F. Finster, S. Murro, E. Radici, *The Fermionic Signature Operator in de Sitter Spacetime*, arXiv:1902.09144. Lemme 3.1 (Q1) et Prop. 4.5 (BD Hadamard global, Q2).
2. F. Finster, M. Reintjes, *A non-perturbative construction of the fermionic projector on globally hyperbolic manifolds II - Space-times of infinite lifetime*, arXiv:1312.7209 (Lemma 6.3). Titre lu dans la bibliographie de 1902.09144.
3. C. Dappiaggi, T.-P. Hack, N. Pinamonti, *The extended algebra of observables for Dirac fields and the trace anomaly of their stress-energy tensor*, arXiv:0904.0612. Déf. 4.1 et Th. 4.1 (Q4).
4. C. Dappiaggi, T.-P. Hack, N. Pinamonti, *Approximate KMS states for scalar and spinor fields in Friedmann-Robertson-Walker spacetimes*, arXiv:1009.5179. États de Dirac de Hadamard en carte plate (Q6).
5. S. Boonpan, *Fermionic Particle Creation in Curved Spacetime: Physical Bloch-Vector Dynamics and Exact de Sitter Scaling*, arXiv:2610.00410. Facteur 1/(e^{2πm/H}+1) et tanh (Q3), en citant de préférence aussi les sources primaires suivantes.
6. G. W. Gibbons, S. W. Hawking, *Cosmological event horizons, thermodynamics, and particle creation*, Phys. Rev. D 15 (1977) 2738. Titre lu dans les bibliographies de 2610.00410 et 2102.02701.
7. H. Friedrich, *Smooth non-zero rest-mass evolution across time-like infinity*, arXiv:1311.0700 (Ann. Henri Poincaré 16 (2015) 2215). Déjà cité ; corriger l'année.
8. **H. Friedrich, *Sharp asymptotics for Einstein-λ-dust flows*, arXiv:1601.04506.** Indispensable pour Prop. CCC (b).
9. **A. Bachelot, *Propagation of Massive Scalar Fields in Pre-Big Bang Cosmologies*, arXiv:2003.03356.** Analogue scalaire de « Variable mass ».
10. A. Roy, *dS/CFT Holography including Fermionic Fields*, arXiv:2609.34073. Poids Δ_± = 3/2 ± im/H et modes au bord (référence pour les « complex boundary weights »).
11. P. Tod, *The equations of Conformal Cyclic Cosmology*, arXiv:1309.7248. Déjà cité.
12. K. A. Meissner, R. Penrose, *The Physics of Conformal Cyclic Cosmology*, arXiv:2503.24263. Déjà cité.
13. P. Tod, *Some questions about Conformal Cyclic Cosmology*, arXiv:2202.10864. Question ouverte « mass fade-out ».
14. L. B. Szabados, *On gravity's role in the genesis of rest masses of classical fields*, arXiv:1802.04401. Pour la discussion d'un mécanisme d'extinction par le Higgs.
15. Pour le critère microlocal Dirac (titres lus dans la bibliographie de 1009.5179) :
    - H. Sahlmann, R. Verch, *Microlocal spectrum condition and Hadamard form for vector valued quantum fields in curved space-time* ;
    - S. Hollands, *The Hadamard condition for Dirac fields and adiabatic states on Robertson-Walker space-times* ;
    - B. Allen, C. A. Lütken, *Spinor two point functions in maximally symmetric spaces* (titre lu dans la bibliographie de 1902.09144).

### Sources web consultées
- [Propagation of Massive Scalar Fields in Pre-Big Bang Cosmologies](https://arxiv.org/pdf/2003.03356)
- [The equations of Conformal Cyclic Cosmology](https://ar5iv.labs.arxiv.org/html/1309.7248)
- [Some questions about Conformal Cyclic Cosmology](https://ar5iv.labs.arxiv.org/html/2202.10864)
- [Conformal Methods in General Relativity with application to CCC (minicourse)](https://arxiv.org/pdf/2102.02701)
- [On gravity's role in the genesis of rest masses of classical fields](https://arxiv.org/pdf/1802.04401)
- [Toward fixing a framework for conformal cyclic cosmology](https://arxiv.org/pdf/2212.06914)
- [Conformal scalar fields, isotropic singularities and conformal cyclic cosmologies](https://arxiv.org/pdf/1312.2059) (titre seulement, non lu)
