# RAPPORT XA-1 : solutions de □²u = 0 en ln s au bord {s = 0}

Audit aveugle. Seul fichier lu hors de /home/claude/audit_xa1/ : la consigne PROMPT-AVEUGLE-XA1-DERIVATION.md. Je n'ai fait aucune recherche bibliographique. Les théorèmes sont cités de mémoire et marqués comme tels. Les numéros de théorèmes donnés pour Hörmander (ALPDO) sont indicatifs et non certifiés.

Étiquettes : [calculé] = sortie sympy, [dérivé] = raisonnement fait ici, [cité de mémoire] = résultat connu.

Conventions. □ = −∂_s² + Δ avec Δ = ∂_x² + ∂_y² + ∂_z². On pose P = ∂_s² − Δ = −□, donc □² = P² = ∂_s⁴ − 2Δ∂_s² + Δ². Le symbole principal de □² est (ξ_s² − |ξ'|²)². Au covecteur conormal ds = (1,0,0,0) il vaut 1 ≠ 0 : **{s = 0} est non caractéristique (de genre espace)**, et □² est hyperbolique (au sens de Gårding) par rapport à ds.

## Réponse courte

| Question | Verdict |
|---|---|
| 1(a) ansatz formel | Tous les c_n sont nuls (n = 0..8, N = 8). a_0..a_3 restent libres (ce sont les données de Cauchy). [calculé] |
| 1(b) argument d'EDP | Toute solution u ∈ D'((0,ε)×Ω) est C^∞ en s jusqu'à s = 0 (et même au-delà), à valeurs dans D'. Cela n'exige **aucune hypothèse de croissance** : l'hyperbolicité la rend automatique. Un comportement α ln s avec α ≠ 0 sur un ouvert est donc impossible. [dérivé + cité] |
| 2 fonctions de cône | Ce sont des solutions de □² hors de {σ = 0}, et aussi des solutions distributions sur s > 0 (vertex exclu). Leur support singulier est le cône {r = s, s > 0}. Le ln s ponctuel n'apparaît qu'en un point (le sommet). Avec un sommet décalé, il apparaît sur une 2-sphère de rayon s₀, par croisement transverse d'un front nul. Aucun ouvert. [calculé + dérivé] |
| 3 classes exotiques | Hyperfonctions, croissance non tempérée, superpositions convergentes : aucune n'échappe. Seules échappent les sorties du cadre lui-même : solution non définie sur une tranche entière, opérateur dégénéré (fuchsien) en s = 0, ou bord caractéristique. |
| 4 ensemble possible | Au sens D'-valué : vide, dans toute classe raisonnable. Au sens ponctuel : seulement sur des ensembles d'intérieur vide (points, 2-surfaces, unions dénombrables). Jamais sur un ouvert sous une hypothèse de domination locale. |

Schéma de l'argument 1(b) :

```
   s
   ^        données de Cauchy à s = s1 (distributions sur Ω)
 s1 +=====[==========K==========]=====   <- tranche connue
    |      \                    /
    |       \  domaine de      /         propagation à vitesse 1 (cône)
    |        \ dépendance     /          solution v = Σ K^(j)(s - s1) * g_j
  0 +---------[======K'======]--------   <- v est C^∞ en s à travers s = 0
    |          (v se prolonge aussi en s < 0)
```

---

## 1. Existence d'une solution en α ln s

### 1(a) Calcul formel [calculé]

Script : `work/q1a_ansatz.py`, sortie : `work/q1a_ansatz.out`.

Ansatz : u = Σ_{n=0}^{8} (a_n(x,y,z) + c_n(x,y,z) ln s) sⁿ, avec des fonctions arbitraires. On calcule s⁴·□²u et on remplace ln s par un symbole L. On impose ensuite les coefficients de s^{j−4} L^e pour j ≤ N. Ce sont les seuls ordres que la troncature ne pollue pas.

Équations obtenues :

- Termes sans log, ordres singuliers :
  - s⁻⁴ : −6 c_0 = 0
  - s⁻³ : 2 c_1 = 0
  - s⁻² : −2 c_2 + 2Δc_0 = 0
  - s⁻¹ : 6 c_3 − 2Δc_1 = 0

  Donc c_0 = c_1 = c_2 = c_3 = 0.
- Termes en ln s, ordre s^k pour k ≥ 0 : (k+4)(k+3)(k+2)(k+1) c_{k+4} − 2(k+2)(k+1) Δc_{k+2} + Δ²c_k = 0. Par exemple, k = 0 donne 24 c_4 − 4Δc_2 + Δ²c_0 = 0.
- La résolution récurrente donne **c_n = 0 pour tout n ≤ 8**. Aucun c_n n'échappe à la contrainte.
- Les a_4..a_8 sont déterminés par a_0..a_3. Exemple : a_4 = −Δ²a_0/24 + Δa_2/6. Les a_0..a_3 restent libres. C'est la série de Cauchy–Kovalevskaya, avec pour données de Cauchy (u, ∂_s u, ∂_s² u, ∂_s³ u) à s = 0.

Interprétation [dérivé] :

- La partie en ∂_s⁴ a pour polynôme indiciel n(n−1)(n−2)(n−3) (vérifié dans `q1b_propagateur.out`). Ses racines 0, 1, 2, 3 sont simples.
- Un ln s ne peut être forcé que par une racine indicielle double, ou par une résonance d'un terme source, et il n'y en a pas ici. En fait s = 0 n'est même pas un point singulier régulier : l'équation est régulière en s. Les termes en c_n ln s injectent des puissances négatives s^{n−4}, ..., que rien ne compense.
- Portée : ce calcul ne couvre que la classe de l'ansatz (polynômes en s et ln s à coefficients lisses). La partie 1(b) fournit l'argument général.

### 1(b) Argument d'EDP général

**Résultats utilisés [cité de mémoire]**

R1. Régularité partielle par rapport à une variable normale non caractéristique (Hörmander, ALPDO I, Thm 4.4.8, numéro indicatif).
- Hypothèses : X = Ω × I ouvert de Rⁿ, avec I un intervalle en s. Q = Σ_{j≤m} Q_j(x, D_x) ∂_s^j est d'ordre m, à coefficients C^∞, et le coefficient de ∂_s^m est inversible (non caractéristique). u ∈ D'(X) et Qu ∈ C^k(I, D'(Ω)).
- Conclusion : u ∈ C^{k+m}(I, D'(Ω)).
- Ici Q = P², m = 4, Qu = 0, ce qui donne u ∈ C^∞((0,ε), D'(Ω)). Ce résultat est intérieur et ne dit rien en s = 0.

R2. Problème de Cauchy hyperbolique à coefficients constants (Gårding ; Hörmander ALPDO II, §12.5).
- Hypothèses : P(D) à coefficients constants, hyperbolique par rapport à N : P_m(N) ≠ 0 et P(ξ + iτN) ≠ 0 pour ξ réel et τ < −τ₀.
- Conclusions : il existe des solutions fondamentales E_± à support dans les cônes propagatifs. Le problème de Cauchy sur {⟨x,N⟩ = c} est bien posé dans C^∞ et dans D' (données distributions), avec vitesse finie de propagation.

R3. Théorème d'unicité de Holmgren, version distributions (Hörmander ALPDO I, Thm 8.6.5, numéro indicatif), avec sa forme globale de F. John.
- Hypothèses : P à coefficients analytiques réels, u ∈ D' solution de Pu = 0 qui s'annule d'un côté d'une hypersurface C¹ non caractéristique près de x₀.
- Conclusion : u = 0 près de x₀.
- En balayant par une famille d'hypersurfaces de genre espace, on obtient l'unicité dans le domaine de dépendance (double cône).

R4 (pour comparaison, non nécessaire ici). Valeurs au bord des distributions prolongeables (Hörmander, ALPDO III, annexe B, numéro non certifié).
- Hypothèses : u ∈ D'(X₊) prolongeable (de façon équivalente : croissance tempérée en 1/s près du bord), Pu ∈ C^∞(X̄₊), bord non caractéristique.
- Conclusion : u ∈ C^∞([0,ε), D').
- Ce résultat vaut pour tout opérateur, elliptique compris, mais il exige la croissance tempérée.

**Dérivation [dérivé, éléments calculés]**

Script : `work/q1b_propagateur.py`, sortie : `work/q1b_propagateur.out`.

1. Propagateur. Après transformée de Fourier en x, P² devient (∂_s² + k²)². Le propagateur K, défini par K(0) = K'(0) = K''(0) = 0 et K'''(0) = δ, vaut :

   K̂(s,k) = (sin ks − ks cos ks)/(2k³) [calculé : il vérifie l'EDO et les données initiales].

   Sa série s³/6 − k²s⁵/60 + ... est entière en s, sans aucun log. Dans l'espace physique, K(s) = sgn(s)·1_{|x|<|s|}/(8π) [calculé : TF de l'indicatrice de la boule].
   - Contrôle indépendant [calculé] : P[θ(s−r)/(8π)] = δ(s−r)/(4πr), qui est le noyau retardé de P. Donc θ(s−r)/(8π) est le noyau retardé de P².
   - K est C^∞ en s ∈ R à valeurs dans E'(R³). En effet K̂ est entière en s, et ses dérivées en s sont à croissance polynomiale en k, uniformément sur les compacts en s. De plus supp K(s) ⊂ boule de rayon |s|.

2. Soit u ∈ D'((0,ε)×Ω) avec □²u = 0. Par R1, u ∈ C^∞((0,ε), D'(Ω)).
   - On fixe s₁ ∈ (0,ε) et les données g_j = ∂_s^j u(s₁) ∈ D'(Ω), j = 0..3.
   - Soit χ ∈ C_c^∞(Ω) qui vaut 1 sur Ω_χ.
   - On pose v(s) = Σ_j L_j(Δ) K^{(i_j)}(s − s₁) * (χ g_j). C'est la formule de Duhamel–Kirchhoff : combinaison linéaire de K''', K'', K', K et de leurs Δ, convolués aux données.
   - Alors v ∈ C^∞(R_s, E'(R³)), □²v = 0 sur R⁴, et v a les mêmes données que u à s = s₁ sur Ω_χ.

3. Par R3, u = v sur le domaine de dépendance {(s,x) : |s − s₁| < dist(x, R³∖Ω_χ)}. Pour un compact K' avec dist(K', R³∖Ω_χ) > s₁, on obtient u|_{(0,s₁]×K'} = v. Donc **u se prolonge en une fonction C^∞ de s ∈ [−δ, s₁] à valeurs dans D'(K')**. En particulier, pour tout M :

   u(s) = Σ_{j≤M} v_j s^j + O(s^{M+1}) dans D'(K').

4. Conséquence. Pour φ ∈ C_c^∞(K'°), ⟨u(s), φ⟩ est C^∞ sur [0, s₁], donc ⟨u(s), φ⟩/ln s → 0. Une écriture u = α ln s + (termes plus réguliers, au sens o(ln s) dans D') force ⟨α, φ⟩ = 0 pour tout φ, donc α = 0 sur l'ouvert.
   - Version ponctuelle : supposons u ∈ L¹_loc, u(s,x) = α(x) ln s + w(s,x), et |u(s,x)| ≤ C|ln s| + g(x) avec g ∈ L¹_loc (domination locale). Par convergence dominée, ⟨u(s),φ⟩/ln s → ∫αφ. Ceci contredit le point précédent, sauf si α = 0 presque partout sur l'ouvert.

**Les hypothèses s'appliquent-elles ici ?** Oui, et toutes sont vérifiées :
- coefficients constants (donc analytiques) ;
- {s = 0} non caractéristique ;
- □² hyperbolique par rapport à ds (produit d'hyperboliques) ;
- u distribution sur un ouvert (0,ε)×Ω.

Point clé [dérivé] : **aucune hypothèse de croissance tempérée en 1/s n'est nécessaire**. La donnée à s₁ > 0, intérieure, suffit, et la propagation hyperbolique vers le passé traverse s = 0. Toute solution distribution sur une tranche est automatiquement prolongeable. Le cas elliptique est différent : là, R4 exige la croissance tempérée.

---

## 2. Fonctions de cône ln σ, 1/σ, s/σ, avec σ = r² − s²

Script : `work/q2_cones.py`, sortie : `work/q2_cones.out`.

**Solutions classiques hors de {σ = 0} [calculé].** On a □σ = 8 et η(dσ,dσ) = 4σ. Puis :

| f | □f | □²f |
|---|---|---|
| ln σ | 4/σ | 0 |
| 1/σ | 0 | 0 |
| s/σ | −4s/σ² | 0 |

Formule générale [dérivé] : □σ^p = 4p(p+1)σ^{p−1}.

**Solutions distributions sur s > 0 [calculé + dérivé].** On régularise σ → σ + iε. Identités exactes :

| f | □²f |
|---|---|
| ln(σ+iε) | 96ε²/(σ+iε)⁴ |
| 1/(σ+iε) | −192iε(σ−iε)/(σ+iε)⁵ |
| s/(σ+iε) | −384ε²s/(σ+iε)⁵ |

Hors de l'origine dσ ≠ 0, donc (σ+i0)^{−k} est une distribution bien définie, limite de (σ+iε)^{−k} [cité de mémoire : tiré en arrière par une submersion]. Les seconds membres sont O(ε)·(σ+iε)^{−k}, qui tend vers 0 dans D'(R⁴∖{0}).

Donc ln(σ+i0), (σ+i0)^{−1} et s(σ+i0)^{−1} sont solutions distributions de □² sur R⁴∖{0}, donc sur {s > 0}. Il en va de même de leurs parties réelles ln|σ|, vp 1/σ et s·vp 1/σ, puisque □² est réel. Sur R⁴ entier, il reste une source ponctuelle au sommet, par exemple □²ln(σ+i0) = c·δ.

**Support singulier.** Sur s > 0, c'est la nappe future du cône privée de son sommet, {r = s, s > 0}. Le coefficient s ne s'y annule pas. Son adhérence rencontre {s = 0} au seul point x = 0.

**Comportement en s → 0.**
- Sur {s = 0}∖{0} (ouvert), σ(0,x) = r² ≠ 0. Les trois fonctions y sont analytiques réelles en s, sans aucun ln s. Exemple : ln σ = ln r² − s²/r² + ...
- Sur la droite x = 0 seulement : ln|σ| = 2 ln s [calculé], 1/σ = −1/s², s/σ = −1/s. Un ln s ponctuel n'existe donc qu'au point x = 0, et seulement pour ln σ.
- Au sens D'-valué, même autour de x = 0, tout est lisse. Avec un poids radial de test (pour ln|σ|) [calculé] :

  F(s) = ∫₀^R r² ln|r² − s²| dr = (2/3)R³ ln R − 2R³/9 − R s² + s⁴/(2R) + s⁶/(9R³) + ...

  La série ne contient aucun log(s). C'est encore vrai avec le poids r²(R² − r²)². La partie imaginaire de ln(σ + i0), iπ·1_{r<s}, contribue iπ·s³/3 (×4π), un polynôme. Ces calculs sont cohérents avec 1(b).
- Conclusion : non, aucune de ces fonctions ne se comporte comme α ln s sur un ouvert de {s = 0}.

**Sommet décalé : σ' = r² − (s + s₀)², sommet en s = −s₀ < 0 [calculé + dérivé].**
- Ce sont des solutions sur R⁴∖{sommet}, donc sur un voisinage entier de {s = 0}.
- Le support singulier est le cône {r = |s + s₀|}. Son intersection avec {s = 0} est **la 2-sphère {r = s₀}**.
- Nature :
  - En (s=0, r=s₀), dσ' = (−2s₀ ∂_s-composante, 2s₀ ∂_r-composante). C'est un covecteur nul, non colinéaire à ds : l'intersection est **transverse**. Le front d'onde WF ⊂ {covecteurs nuls} ne contient pas ±ds.
  - La restriction à {s = 0} est donc bien définie [cité de mémoire : Hörmander Thm 8.2.4, restriction quand WF ∩ conormale = ∅]. Elle vaut ln|r² − s₀²|, singularité conormale à la sphère de type logarithmique. Pour 1/σ' on obtient vp 1/(r² − s₀²), un pôle simple conormal. Pour s/σ', la restriction est nulle à s = 0.
  - Ponctuellement sur la sphère : ln|σ'| = ln s + ln(s + 2s₀) [calculé]. On a bien un « ln s ponctuel » sur une 2-surface, mais c'est en réalité ln|s|, des deux côtés de s = 0. C'est la trace d'un front nul qui traverse le bord, pas un phénomène de bord.
  - Ailleurs, la fonction est analytique en s. L'intégrale radiale G(t), avec t = s + s₀, est analytique pour 0 < t < R [calculé], donc lisse D'-valuée.

---

## 3. Classes susceptibles d'échapper à la conclusion de 1

| Classe | Échappe ? | Raison |
|---|---|---|
| Distributions sans croissance tempérée en 1/s | Non | 1(b) n'utilise aucune croissance. L'hyperbolicité rend toute solution sur une tranche automatiquement prolongeable. [dérivé] |
| Superpositions infinies convergentes dans D'(s > 0) | Non | La limite est une solution distribution, et 1(b) s'applique. Exemple ci-dessous. |
| Hyperfonctions | Non (sous les théorèmes cités) | Unicité de Holmgren pour les hyperfonctions (Kashiwara) et problème de Cauchy hyperbolique bien posé dans les hyperfonctions, avec propagation dans le cône d'influence (Bony–Schapira, 1972) [cité de mémoire]. Le même argument de recollement depuis s₁ > 0 s'applique. WF_A(u) ⊂ Char(□²) ne contient pas ±ds, donc u dépend analytiquement de s (restriction aux tranches définie). Cela s'étend aux ultradistributions, qui sont contenues dans les hyperfonctions. Niveau de confiance : bon sur le principe, énoncés exacts non revérifiés. |
| Fonctions définies seulement ponctuellement, solutions classiques hors d'un fermé | Non pertinent | Si le fermé singulier ne recouvre pas d'ouvert, on est dans le cas distributions dès que u ∈ L¹_loc. Sinon, la notion de solution perd son sens. |
| Solution non définie sur une tranche entière (0,ε)×Ω (définie seulement dans un coin, ou dans l'intérieur d'un cône caractéristique) | Oui, mais hors cadre | La question pose « solution sur s > 0 ». |
| Opérateur dégénéré en s = 0 (fuchsien) | Oui, autre problème | Exemple : Euler–Poisson–Darboux ∂_s² + (1/s)∂_s, dont ln s est solution [calculé : `q3_contraste.out`]. Le ln s y provient d'une racine indicielle double. □² plat n'a pas cette structure. |
| Bord caractéristique (hypersurface nulle) | Oui, autre problème | R1–R3 ne s'appliquent plus. |

**Exemple construit (superposition dénombrable) [dérivé].** Soit (y_j) une suite dense dans un ouvert U ⊂ {s = 0}, et σ_j = |x − y_j|² − s². On pose :

u = Σ_j 2^{−j} ln|σ_j|.

- Les normes L¹_loc de ln|σ_y| sont uniformément bornées pour y dans un compact. La série converge donc dans L¹_loc(s > 0), et □²u = 0 dans D'(s > 0).
- Ponctuellement, le terme j contribue 2^{1−j} ln s sur la droite x = y_j, c'est-à-dire sur un ensemble dense de points du bord. Le reste de la série n'est pas contrôlé ponctuellement en général.
- Par 1(b), u est néanmoins C^∞ en s jusqu'à 0 à valeurs D'. Le « coefficient α » au sens des distributions est nul.
- Cela illustre le mécanisme : un ln s ponctuel sur un ensemble de mesure nulle, même dense, est invisible aux fonctions test. Il ne constitue pas un comportement α ln s sur un ouvert.
- Une superposition continue ∫ρ(y) ln|σ_y| dy, avec ρ lisse, donne une trace continue ∫ρ(y) ln|x−y|² dy, sans ln s ponctuel.

**Ce qui reste ouvert.** Je n'ai ni démontré ni réfuté la version purement ponctuelle sans domination locale : u(s,x)/ln s → α(x) pour chaque x ∈ U, sans majoration uniforme. Le cas est pathologique, il n'a pas d'interprétation distributionnelle et il n'est pas exclu par l'argument ci-dessus. Je ne connais aucun exemple.

---

## 4. Conclusion : sur quelle partie de {s = 0} un ln s est-il possible pour une solution homogène ?

| Classe de u (solution de □²u = 0 sur (0,ε)×Ω) | Ensemble de {s = 0} portant un comportement α ln s, α ≠ 0 |
|---|---|
| D' sans hypothèse de croissance, sens D'-valué | ∅. Aucun ouvert, aucun ensemble au sens des distributions : u ∈ C^∞([0,ε'), D'). [dérivé + cité] |
| Hyperfonctions | ∅ (sous Bony–Schapira et Holmgren–Kashiwara). [cité de mémoire] |
| L¹_loc avec domination locale \|u\| ≤ C\|ln s\| + g, sens ponctuel | Ensemble de mesure nulle ; jamais un ouvert. [dérivé] |
| Sens ponctuel, exemples explicites | Un point (sommet de cône sur le bord : ln\|σ\| = 2 ln s en x = 0). Une 2-surface (croisement transverse d'un front nul porteur d'une singularité log : sphère r = s₀, ln\|s\|). Unions dénombrables de tels ensembles, éventuellement denses, mais d'intérieur vide et de mesure nulle. [calculé + dérivé] |
| Sens ponctuel sans domination | Non tranché (cas pathologique). Aucun exemple sur un ouvert connu. |

Origine des ln s ponctuels : ils viennent soit d'un sommet de cône caractéristique posé sur le bord, soit d'un front nul qui traverse le bord. Ce sont des singularités transportées le long de caractéristiques nulles, transverses à {s = 0}. Aucune ne correspond à une donnée de bord en ln s indépendante. Un ln s générique sur un ouvert demanderait un bord caractéristique ou un opérateur fuchsien en s = 0. Le problème posé (□² plat, bord {s = 0} de genre espace) ne contient ni l'un ni l'autre.

---

## Empreintes sha256

Répertoire : /home/claude/audit_xa1/work/

```
1fb3157852a8d1680f8e320badc53fabd53052a1690224c67d556d6d075faa20  q1a_ansatz.py
8760895643b09e84dae4c8d113d2e1ec521683c2c1b2917db9c0190b03ddaf19  q1a_ansatz.out
77503ccbefe53f34a24f8fa34934a9db21acc45b76288c9d46dc54d557ea482b  q1b_propagateur.py
af6ae4f59b49a7efdd9574a7e86c12cab9b1ba03a88be6f620da0b353a0f89c6  q1b_propagateur.out
d38d48854db20234273aeacc30fe1c531ea6e45440a2017119aa3f35d83c2234  q2_cones.py
a93d30eae367240e2fea23c7bc745a58b0d04473a0f2e1d48630dd5cb4fbc9fc  q2_cones.out
20e820ff2f533dc239d99eed8ca2cdc7b870ef45c1f5b829753a7e0f47d657e9  q3_contraste.py
4ba500aeb4a2f3c8bfb8fd873063257def6709d373011d752686991a556e7c55  q3_contraste.out
```

Environnement : python3.13, sympy 1.14.0.
