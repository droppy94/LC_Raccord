# RAPPORT DB-2 : audit adverse aveugle de NOTE-181 (chantier ED)

Date : 2026-10-15. Pièces lues : PROMPT-AVEUGLE-DB2.md, NOTE-181.md, ed_check.py, ed_check_sortie.txt, SOURCE-1311.0700-fulltext.txt. Rien d'autre.
Répertoire de travail : /tmp/claude-0/db2/ (copie du script, variantes, sorties).

## Synthèse

| Point | Verdict | En une ligne |
|---|---|---|
| F1 | **CONFIRMÉ avec réserves** | Les identités sont justes et survivent à une métrique non physique non plate et à l'autre signature ; mais (B) ne teste pas la connexion de spin, et (A) fixe c par la propriété à vérifier. |
| F2 | **CONFIRMÉ** | Lecture correcte de (2.13)-(2.17) et de L̂ ; aucun terme de matière manquant dans ces équations ; réserve de signature sans effet sur le comptage. |
| F3 | **CONFIRMÉ SUR LE FOND, FORMULATION À CORRIGER** | « Même contenu singulier » est vrai modulo l'équation de Dirac, pas comme identité formelle des seconds membres ; le tenseur de Hilbert est la forme lagrangienne, et la forme cinétique s'obtient en utilisant l'équation de Dirac, ce que Friedrich s'autorise (il réécrit avec (3.8) et (2.14)). |
| F4 | **PROPORTIONNÉE SUR LE FOND, §5 INSUFFISANT** | Le « seulement si » n'est établi qu'à inconnues fixées (ψ̂ = Ω^{-3/2}ψ) ; une vérification indépendante sur de Sitter (exposants ±i m/H) corrobore « pas de masse spéciale ». |

**ED-V1 n'est pas réfuté.** Aucune erreur grave. Trois erreurs moyennes, neuf mineures (§6).

## 1. Exécutions reproduites

`python3 ed_check.py 2` puis `python3 ed_check.py 1` : sortie identique à ed_check_sortie.txt (A : c = 1/4 ; B, C : True ; D : 0 pour Ω², -1 pour Ω¹ ; E : Ω⁰).
Remarque : la ligne « --- variante --- » de ed_check_sortie.txt n'est pas produite par le script ; la sortie est la concaténation manuelle de deux exécutions. Sans conséquence, mais à signaler dans la note.

Loi de décalage du compteur (D), testée pour cinq poids :

| L̂ = Ω^p Y | p = -1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|
| plus basse puissance de Ω dans (2.17) | -3 | -2 | -1 | **0** | 1 |

Le compteur suit exactement p - 2 : il est cohérent (un facteur Ω^{-1} explicite et un Ω^{-1} venant des Christoffel de ĝ). Le cas p = 0 donne -2, ce qui correspond au scalaire de Friedrich (Ω^{-1} dans ∇̂L̂, cf. (3.15)-(3.16), puis Ω^{-2} dans (2.17)).

## 2. F1 : le script vérifie-t-il ce que la note affirme ?

### 2.1 Variantes (fichier /tmp/claude-0/db2/variants.py, sortie variants_sortie.txt)
Construction indépendante : connexion de spin **dérivée de la tétrade** (ω_μ^a_b = e^a_ν(∂_μE_b^ν + Γ^ν_{μλ}E_b^λ), Γ_μ = ¼ ω_μab γ^aγ^b), donc sans ajustement de c ; champs ψ̂(x), Ω = e^{w(x)}, fonctions réelles génériques ; vérification hors couche.

| Variante | cov. Dirac | cov. T cinétique | adjoint ∇ψ̄ = (∇ψ)‾ | cov. Lag_sym |
|---|---|---|---|---|
| V1 g plate, connexion dérivée | True | True | True | True |
| V1 **g non plate** diag(e^{2h0}, -e^{2h1}, -e^{2h2}, -e^{2h3}), h_i(x) génériques | True | True | True | True |
| V2 poids Ω^{1/2} (témoin négatif) | False | False | True | False |
| V2 signe de la connexion inversé (témoin) | False | **True** | True | **True** |
| V6 signature (-,+,+,+), γ' = iγ, plate | True | True | True | True |
| V6 signature (-,+,+,+), non plate | True | True | True | True |

Confirmations :
- l'identité T̂[ψ ; ĝ] = Ω² T[ψ̂ ; g] tient hors couche pour une métrique non physique non plate (tétrade diagonale générique, non conformément plate en général) et dans l'autre signature. La première limite du §5 peut donc être levée (pour les tétrades diagonales) ;
- c = 1/4 est bien la connexion de Levi-Civita : la connexion dérivée de la tétrade donne la covariance de l'opérateur de Dirac ;
- la version réelle symétrisée du lagrangien est aussi covariante : Lag_sym[ψ ; ĝ] = Ω⁴ Lag_sym[ψ̂ ; g](m → m/Ω).

Réfutations partielles (sur la méthode, pas sur le résultat) :
- **(B) ne teste pas la connexion de spin.** Avec le signe inversé, (B) reste True, aussi bien dans ma variante que dans le script d'origine (ed_check_wrongc.py : A False, B True, C False). Raison : dans le tenseur symétrisé, la connexion n'entre que par ψ̄{γ_(μ, Γ_ν)}ψ ; pour la partie conforme, {γ_μ, [γ_ν, γ^ρ]} est totalement antisymétrique et s'annule par symétrisation en (μν). (B) est en fait un simple comptage de poids : T̂ ~ Ω³ · Ω^{-1} = Ω², les termes en ∂Ω de Ω^{3/2} s'annulant dans la combinaison antisymétrique ψ̄γ∂ψ - ∂ψ̄γψ. La phrase « Conventions vérifiées d'abord (FW-2) ... avec ce coefficient » laisse croire que (B) dépend de (A) : c'est faux.
- **(A) est circulaire par construction** : c est choisi dans une liste finie pour que la covariance tienne, puis la covariance est déclarée vérifiée. Le résultat est juste (V1 le confirme sans ajustement), mais (A) seul n'établit rien.
- **(C) utilise un lagrangien non réel** ψ̄(iγ·∇ - m)ψ ; c'est lui que la note met dans « g_hat Lag » au §3, ce qui rendrait T complexe. Il faut le lagrangien symétrisé (réel) ; V3 montre que l'identité tient aussi pour lui, et le terme singulier ne change pas (ψ̄ψ est réel).

### 2.2 Structure réelle de Dirac dans (2.17) (fichier v5_lagform.py, sortie v5_sortie.txt)
Le script (D) ne traite que Y générique. J'ai calculé la source de (2.17) avec la structure effective de Dirac (ψ̂(x), Ω(x) génériques, métrique non physique plate) :

| Représentation de T̂ | plus basse puissance de Ω dans 2Ω^{-1}∇̂_[ν L̂_λ]ρ |
|---|---|
| cinétique T_kin | **0** (régulier) |
| hilbertienne T_kin - ĝ Lag_sym | **-1**, coefficient (κ m/2) ψ̄̂ψ̂ ∂Ω (structure η_ρλ ∂_νΩ - η_ρν ∂_λΩ) |

Cela confirme la « variante » de la note avec la structure réelle et non une borne générique. Analytiquement : le terme ajouté à L̂ vaut (κ/6) ĝ Lag = (κ/6) Ω² R η avec R = ψ̄̂(iγ·∂ - m/Ω)ψ̂ (forme symétrisée), et sa contribution à (2.17) est une combinaison de R et ∂R, d'où la partie singulière -(κ/6)·6 m ψ̄̂ψ̂ ∂Ω/Ω à la normalisation de l'antisymétrisation près. Seule (2.17) est touchée : (2.13), (2.15) restent régulières (T̂ reçoit -4Lag = O(Ω³)), (2.14) et T* ne voient pas le terme de trace.

**Verdict F1 : CONFIRMÉ avec réserves** (erreurs M3, m1, m5, m6 ci-dessous).

## 3. F2 : lecture de Friedrich (2.13)-(2.17)

Lu dans la source (lignes 812-931) et recoupé avec la dérivation de Friedrich :

| Éq. | Second membre chez Friedrich | Note | Contrôle |
|---|---|---|---|
| (2.13) | -(κ/4) T̂ | Ω⁴Θ_tr, régulier | correct |
| (2.14) | (κ/2) Ω T*_μν | Ω³(...) régulier | correct ; vient de ΩŜ_μν, Ŝ = (κ/2)T* |
| (2.15) | (κ/2) ∇^ρΩ T*_ρμ - (κ/24) Ω^{-1} ∇̂_μ T̂ | régulier | correct ; signe vérifié via (2.8) et R̂ = 4λ - κT̂ |
| (2.16) | 2 ∇̂_[ν L̂_λ]ρ | traité avec (2.17) | O(Ω), régulier |
| (2.17) | 2 Ω^{-1} ∇̂_[ν L̂_λ]ρ | O(Ω⁰) | correct |
| déf. | T*_ρμ = T̂_ρμ - ¼ T̂ ĝ_ρμ ; ∇̂L̂ = (κ/2)∇̂(T̂ - ⅓T̂ĝ) | idem, plus λĝ/6 annulé | correct |

J'ai rederivé L̂ = (κ/2)(T̂ - ⅓T̂ĝ) + (λ/6)ĝ à partir de (2.1)-(2.2) : conforme à la note et à la décomposition de la preuve du théorème 3.1 (L̂ = (κ/2)T* - (κ/24)T̂ĝ + (λ/6)ĝ).

Attention à la surcharge de notation chez Friedrich : T*_μν (partie sans trace, indices en bas, sans facteur Ω) et le scalaire T* ≡ Ω^{-2}T̂ de (3.7). La note emploie correctement le premier dans (2.14)-(2.15).

**Terme de matière manquant ?** Non dans (2.13)-(2.17) : la matière n'entre que par T̂, T* et ∇̂L̂ ; (2.18)-(2.19) n'en contiennent pas ; en Einstein-Dirac (Levi-Civita, sans torsion) il n'y a pas d'autre couplage. Deux précisions qui ne sont pas des manques mais devraient être dites :
- Friedrich suppose T̂ symétrique et conservé ; pour Dirac, la conservation et l'annulation de la partie antisymétrique du tenseur canonique n'ont lieu que sur couche (propagation de la contrainte (2.13) dépendante de l'équation de Dirac) ;
- le système étendu (inconnue χ_μ = ∇_μψ̂) contient l'équation dérivée de Dirac, où entrent m/Ω, m∂Ω/Ω² et des termes de courbure ¼R_μνab γ^aγ^b ψ̂, réguliers via (2.19) (ΩW + L). La note le dit en substance (« m/Ω et ses dérivées »).

Signature : Friedrich est en (-,+,+,+) (g = -dτ² + h, (3.8) : ∇Ω·∇Ω = -λ/3 + ...), la note et le script en (+,-,-,-). La note écrit à juste titre dΩ·dΩ = λ/3 + ... dans sa convention, mais transpose les équations sans le signaler. Sans effet sur le comptage des puissances de Ω (V6 le confirme pour l'identité B).

**Verdict F2 : CONFIRMÉ** (erreur m4).

## 4. F3 : forme cinétique contre forme lagrangienne, au sens FORMEL

Schéma de la situation :

```
          tenseur de Hilbert (variation de la tétrade)
                 T_H = T_kin - ĝ·Lag_sym
                        |
          utiliser l'éq. de Dirac (Lag_sym = 0 sur couche)
                        v
                 T_kin  (forme cinétique)

  géométrie (2.13)-(2.17)          matière (Dirac rescalée)
  T_H   : Ω^-1 · m ψ̄̂ψ̂ ∂Ω  [*]       iγ·∇ψ̂ = (m/Ω) ψ̂      (toujours)
  T_kin : régulier                  ∇χ ⊃ m∂Ω/Ω² ψ̂        (système étendu)
  [*] = combinaison de R et ∂R, R = résidu de Dirac
```

1. **Au sens formel strict** (seconds membres comme fonctions des inconnues), les deux représentations ne sont pas équivalentes : en forme hilbertienne, (2.17) contient le terme singulier (κm/2)ψ̄̂ψ̂∂Ω/Ω ; en forme cinétique, aucun. La phrase « même contenu singulier » n'est donc pas une identité formelle. Ce qui est vrai : la partie singulière ajoutée appartient à l'idéal engendré par l'équation de Dirac et sa dérivée première (elle s'annule sur couche, et peut être retirée en substituant l'équation de Dirac). C'est une égalité *modulo les équations du système*, et c'est ainsi qu'il faut l'écrire.
2. **Légitimité chez Friedrich** : oui. Friedrich réécrit lui-même les seconds membres à l'aide d'équations du système (preuve du théorème 3.1 : « Direct calculations using (3.14), (2.14) and (3.8) » ; (3.8) vient de la contrainte (2.13)), et énonce la régularité d'un système une fois réécrit (« the right hand sides are in fact smooth functions of the unknowns »). Son critère est donc existentiel sur les réécritures admissibles. Utiliser l'équation de Dirac pour passer de T_H à T_kin relève de la même pratique. Mais la note doit le dire : elle présente la forme cinétique comme le choix par défaut, alors que le tenseur canonique de Hilbert est la forme lagrangienne. Pour le scalaire, Friedrich n'a pas ce choix : son (3.2) est exactement la forme de Hilbert, et le terme ĝ·L n'y est pas proportionnel à un résidu.
3. **Ce qui rend le verdict système-global robuste** : quelle que soit la représentation de T̂, l'équation de Dirac rescalée fait partie du système et porte m/Ω ψ̂ ; aucune autre équation du système ne fournit d'expression régulière de ψ̂/Ω qui permettrait de la réécrire. La régularité « de la géométrie » dépend de la représentation ; la régularité du système complet n'en dépend pas.

**Verdict F3 : CONFIRMÉ SUR LE FOND, FORMULATION À CORRIGER** (erreur M1).

## 5. F4 : proportion de la conclusion et limites

**« Régulier ssi m = Ωμ »** :
- « si » : avec m = Ωμ, μ lisse, m/Ω = μ et ∂(m/Ω) = ∂μ sont réguliers ; le terme hilbertien devient -μΩ²ψ̄̂ψ̂η, régulier aussi. Correct.
- « seulement si » : établi par la note **à inconnues fixées** (ψ̂ = Ω^{-3/2}ψ). Rien n'y exclut un autre choix d'inconnues (poids réel différent, rescaling matriciel, rotation chirale dépendant de Ω). Un poids réel différent ajoute un terme k γ·∂Ω/Ω de structure matricielle différente de m/Ω, qui ne peut pas le compenser ; une rotation chirale produit un terme axial ψ̄γ^μγ5ψ, qui ne compense pas une masse scalaire ; un rescaling matriciel exp(M ln Ω) introduit des ln Ω dans les coefficients. L'argument manque dans la note.

**Vérification indépendante (v7_desitter.py, sortie v7_sortie.txt)** : sur de Sitter exact (métrique non physique plate, Ω = -Hτ, H² = λ/3), champs tests :
- Dirac : la matrice indicielle a pour valeurs propres **±i m/H** pour tout mode k ; la solution homogène exacte est ψ̂ = exp(i (m/H) γ⁰ ln|τ|) ψ̂₀ (vérifiée symboliquement). Pour tout m ≠ 0, ψ̂ reste borné mais **n'a pas de limite** en 𝓘 (oscillation en ln|τ|) : aucune formulation à inconnues lisses ne peut être régulière, quel que soit le rescaling à poids réel ;
- scalaire (3.11) : exposants r = (1 ± √(9 - 4m²/H²))/2, qui valent **0 et 1** exactement pour m² = 2H² = 2λ/3 : c'est la masse spéciale de Friedrich.

Le contraste confirme la conclusion « pas de masse spéciale pour le spin 1/2 » par une voie qui ne dépend ni de la représentation de T̂ ni du choix du poids (exposants Δ = 3/2 ± i m/H, toujours complexes). La conclusion est donc **proportionnée sur le fond**.

**Limites du §5 : insuffisantes.** Manquent :
1. la dépendance du choix des inconnues (point ci-dessus) ; à fermer en citant l'argument de Sitter ;
2. le caractère « modulo l'équation de Dirac » de la régularité géométrique (F3) ;
3. la transposition de signature (-,+,+,+) → (+,-,-,-) ;
4. le statut des renvois externes (Lemme 2, Prop. 4(c)), non vérifiables avec les pièces de cet audit ;
5. l'interprétation physique : m = Ωμ n'est pas une masse constante, c'est une masse qui s'annule sur 𝓘 ; « régulier ssi m = Ωμ » équivaut à « régulier ssi m = 0 pour une masse constante ».
À l'inverse, la première limite (fond plat) peut être levée : V1 vérifie l'identité B pour une métrique non physique non plate.

**Verdict F4 : PROPORTIONNÉE SUR LE FOND, §5 INSUFFISANT** (erreur M2).

## 6. Erreurs classées par gravité

### Graves
Aucune.

### Moyennes
- **M1 (F3, §3 et §4 de la note)** : « le contenu singulier est donc le même dans les deux représentations » est présenté comme formel ; ce n'est vrai que modulo l'équation de Dirac (idéal engendré par R et ∂R). La note ne dit pas non plus que le tenseur de Hilbert est la forme lagrangienne, ni que la forme cinétique s'obtient en utilisant l'équation de matière (légitime chez Friedrich, qui réécrit avec (3.8) et (2.14)). Il faut reformuler : « géométrie formellement régulière dans la représentation cinétique, obtenue de la forme de Hilbert par l'équation de Dirac ; régularité du système complet indépendante de ce choix ».
- **M2 (F4, §4-§5)** : le « seulement si » et « aucune masse constante non nulle ne convient » ne sont établis qu'à inconnues fixées ψ̂ = Ω^{-3/2}ψ ; le §5 ne le mentionne pas. Le résultat est corroboré par les exposants de Sitter ±i m/H (V7), qu'il faudrait ajouter.
- **M3 (F1, partie A/B du script et §1 de la note)** : (A) fixe c par la propriété à démontrer (circulaire), et (B) est insensible à la connexion de spin (True avec le signe inversé). « Conventions vérifiées d'abord » surévalue ce que le script contrôle. Le résultat reste juste (connexion dérivée de la tétrade, V1).

### Mineures
- **m1** : lagrangien non réel dans (C) et au §3 (« g_hat Lag ») ; utiliser Lag_sym (covariance vérifiée en V3, coefficient singulier inchangé).
- **m2** : §4, « L_hat a une composante d'ordre 1 » (scalaire) se lit comme Ω⁰ alors que le §3 écrit « ordre Omega^1 » au sens de Ω¹ ; ambigu. Avec Ω¹, (2.17) n'aurait que du Ω^{-1}, pas le Ω^{-2} annoncé ; le sens correct est O(Ω⁰).
- **m3** : §4, « aucune composante d'ordre Ω⁰ ou Ω¹ dans L̂ » oublie (λ/6)ĝ = O(Ω^{-2}), annulé par ∇̂ ; préciser « hors terme cosmologique ».
- **m4** : signatures mêlées (Friedrich (-,+,+,+), note (+,-,-,-)) non signalées ; sans effet sur le comptage.
- **m5** : ed_check_sortie.txt est une concaténation manuelle de deux exécutions ; la « variante » est le cas Y générique p = 1, pas la structure lagrangienne réelle (désormais vérifiée en V5 : -1, coefficient (κm/2)ψ̄̂ψ̂∂Ω).
- **m6** : §5, première limite trop prudente : l'identité B est vérifiée pour une métrique non physique non plate (tétrades diagonales génériques).
- **m7** : la partie (E) est un contrôle trivial (m²φ²ĝ = m²ψ²η) ; elle ne reproduit rien du théorème 3.1, ce que la note dit déjà pour la combinaison (m² - 2λ/3).
- **m8** : noms de symboles par `hash()` dans (D) : dépendent de PYTHONHASHSEED (collision improbable) ; sans effet.
- **m9** : renvois « Lemme 2 » et « Prop. 4(c) de l'article » non vérifiables dans le périmètre de l'audit.

## 7. Fichiers produits (/tmp/claude-0/db2/)
| Fichier | sha256 (16) | Rôle |
|---|---|---|
| ed_check.py | (copie) | script d'origine |
| ed_check_wrongc.py | 3164bf0d262a917f | témoin : signe de connexion inversé |
| variants.py, variants_sortie.txt | aae6670c2bda9294 | V1, V2, V3, V4, V6 |
| v5_lagform.py, v5_sortie.txt | caf704763104a0c2 | structure réelle de (2.17), deux représentations |
| v7_desitter.py, v7_sortie.txt | d8a92d84aeb5a995 | exposants indiciels de Sitter, Dirac et scalaire |

Recommandation : NOTE-181 peut être maintenue en ED-V1 après corrections M1 à M3 (reformulation F3, ajout de l'argument de Sitter au §4-§5, description honnête de ce que (A) et (B) contrôlent) et des mineures m1 à m6.
