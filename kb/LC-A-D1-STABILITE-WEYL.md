---
id: LC-A-D1-STABILITE-WEYL
titre: "Verrou D1 — le candidat-sélecteur #5 (stabilité inter-éons) ferme-t-il D1 ? rapport à D3 (Weyl)"
codename: LC-RACCORD
tags: [module-A, D1, D3, ccc, stabilite-inter-eons, weyl, bifurcation, facteur-conforme]
type: chaînon (sous-investigation de LC-A-D1, candidat-sélecteur #5)
statut: verdict établi (ne ferme pas D1) / redirection vers le secteur inhomogène décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (mineur : LC-A-D1 §5, LC-02, glossaire)
fichier_compagnon: verif_D1_stabilite.py
renvois: [LC-A-D1-FACTEUR-CONFORME, LC-A-SURVIE-CONFORME, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-A·D1·S5 — Stabilité inter-éons et Weyl : tentative de fermeture de D1

> **Question.** L'atlas (`LC-A-D1` §4-bis) a fait émerger un candidat-sélecteur #5 :
> *exiger la stabilité inter-éons des paramètres `(m,λ)` sélectionnerait le point fixe
> `m̂λ̂ = 9k²/4` où les trois prescriptions coïncident* — et on l'a soupçonné relié à
> l'hypothèse de Weyl (D3). **Ce candidat ferme-t-il D1 ? Se réduit-il à D3 ?**
>
> **Verdict (établi, calculé).** **Non, deux fois.** (1) La stabilité ne fixe qu'une
> **relation** (`m̂λ̂=9k²/4`), pas un facteur conforme unique : elle laisse une famille
> à un paramètre, et **dégénère au cas physique `k=0`** (univers plat). (2) En FLRW le
> tenseur de **Weyl est identiquement nul** : D3 est *vacant* dans le secteur
> symétrique, et le runaway de `(m,λ)` est un phénomène de **fond** que Weyl ne voit
> pas — **le pont #5 → D3 ne tient pas là**. Conséquence utile : **la fermeture de D1
> ne peut pas venir du secteur symétrique** ; elle exige le secteur **inhomogène**
> (la donnée `g₍₃₎`), qui est précisément le domaine propre de D3 (Weyl). #5 est
> rétrogradé ; **D3-dans-le-cas-inhomogène** est promu comme la route principielle.

---

## 1. La carte de stabilité, exacte `[établi]`

Compagnon : `verif_D1_stabilite.py` [A]. La classe Penrose-cohérente (condition 55d)
induit, d'éon en éon, la carte (Markwell–Stevens éq. 14, `k≠0`) :

$$T:\quad (m_i,\lambda_i)\ \longmapsto\ \Big(m_{i+1},\lambda_{i+1}\Big)
=\Big(\tfrac{9k^2}{4\lambda_i},\ \tfrac{4\lambda_i^2 m_i}{9k^2}\Big).$$

Faits exacts (vérifiés symboliquement) :

- **Invariant.** `m_{i+1}\lambda_{i+1} = m_i\lambda_i` : le produit `mλ` est **conservé**.
- **Ensemble fixe.** `T(m,λ)=(m,λ) ⟺ mλ = 9k²/4` : une **droite fixe** entière (toute
  la branche d'hyperbole), pas un point isolé.
- **Nature.** Jacobien sur la droite fixe `J=\begin{psmallmatrix}0 & -9k^2/4\lambda^2\\ 4\lambda^2/9k^2 & 2\end{psmallmatrix}`,
  `tr J = 2`, `det J = 1`, valeur propre **`μ=1` double** : carte **non-hyperbolique**
  (marginale), pas un attracteur.
- **Emballement.** Sur un niveau `mλ=P`, on a le ratio géométrique constant
  `m_{i+1}/m_i = 9k^2/4P`. Pour `P≠9k²/4`, ce ratio `≠1` : **runaway géométrique**
  (`m→0, λ→∞` ou l'inverse) — la « bifurcation instable » de l'atlas, ici caractérisée
  exactement. La droite fixe n'attire pas : c'est un **bord marginal**, pas un bassin.

---

## 2. Ce que la stabilité fixe — et ce qu'elle ne fixe pas `[établi]`

La donnée *physique* est le passé `(m̂,λ̂,k)`. Exiger la stabilité (`m̌=m̂, λ̌=λ̂`)
impose **une seule équation** :

$$\boxed{\ \hat m\,\hat\lambda = \tfrac94 k^2\ }\qquad(k\neq 0).$$

C'est une **relation**, pas une détermination. Sur cette droite, `c_1=\sqrt{2\hat\lambda/3k}`
varie encore (avec `λ̂` libre, `m̂=9k²/4λ̂`) : il reste une **famille à un paramètre** de
facteurs conformes. Donc :

$$\text{stabilité}\ \Rightarrow\ \text{1 contrainte}\ \not\Rightarrow\ \text{facteur unique}.$$

**La stabilité ne ferme pas D1** ; elle réduit la liberté (de « un constant `c₁` » à
« une relation entre `m̂,λ̂` »), comme un cran de plus dans la cartographie — sans
atteindre la fermeture. C'est un résultat de type `LC-07` (réduction), non `LC-10`.

*Lecture physique (intéressante).* Sous CCC + Penrose (`λ̂=λ`) + stabilité, l'univers
clos/ouvert devrait satisfaire `m̂λ̂=9k²/4` : une **relation falsifiable** entre densité
de radiation, constante cosmologique et courbure spatiale. C'est une *prédiction*
conditionnelle, pas une fermeture du formalisme.

---

## 3. Le cas physique `k=0` — le candidat #5 s'éteint `[établi]`

Notre univers est spatialement **plat** (`k≈0`) avec `Λ>0`. Or toute la construction
de #5 vit à `k≠0` :

- La condition de Penrose (55d) impose `c_1^2 = 2\hat\lambda/3k`, qui **diverge** quand
  `k→0`.
- La droite fixe `m̂λ̂=9k²/4` dégénère en `m̂λ̂=0` (triviale).
- À `k=0`, c'est la prescription de **Tod** (`c_1=(\hat\lambda/\hat m)^{1/4}`) qui est
  régulière : elle donne `(m̌,λ̌)=(m̂,λ̂)` — donc **déjà stable**, automatiquement —
  mais avec courbure de pont `λ_{\text{pont}}=0≠\hat\lambda` (elle **sacrifie** `λ̂=λ`).

Donc à `k=0` : la stabilité est **générique** (Tod la fournit sans condition) et ne
**sélectionne rien** ; le désaccord résiduel n'est plus « stable vs instable » mais
« `λ̂=λ` (Penrose, indisponible à `k=0`) vs Tod (stable mais `λ̂≠λ`) ». **Le candidat
#5 est vacant comme sélecteur pour un univers plat.**

---

## 4. Le pont vers D3 (Weyl) — examiné, et infirmé dans le secteur symétrique `[établi]`

L'espoir était : « stabilité ⟺ faible désordre gravitationnel ⟺ Weyl `→0` (D3) ».
Test direct (compagnon [B]) — tenseur de Weyl complet `C_{abcd}` :

| modèle | matière | `C_{txtx}` | lecture |
|---|---|---|---|
| FLRW radiation `a(τ)=τ` | radiation + `Λ` | **`0`** | conformément plat : **Weyl ≡ 0** |
| Kasner `(2/3,2/3,−1/3)` | **vide** (`Ric=0`) | `2/(9t^{2/3})` ≠ 0 | Weyl = Riemann, **sourcé par l'anisotropie** |

Deux conclusions exactes :

1. **En FLRW, `Weyl ≡ 0` quels que soient `(m,λ)`.** L'hypothèse de Weyl (`C→0`) est
   donc **automatiquement satisfaite et sans contenu** dans tout l'atlas symétrique :
   D3 ne peut **pas** y sélectionner quoi que ce soit. Le runaway de `(m,λ)` se produit
   *à Weyl nul* : c'est un phénomène de **fond** (background), aveugle à D3.
2. **Weyl vit dans un autre secteur.** Le modèle de Kasner (vide, anisotrope) a `Weyl≠0`
   **sans aucune matière ni `Λ`** : le tenseur de Weyl est le **champ gravitationnel
   libre** (marée/cisaillement), sourcé par l'**anisotropie/inhomogénéité**, orthogonal
   au secteur `(m,λ)`.

$$\boxed{\ \text{stabilité (secteur } (m,\lambda)\text{, fond)}\ \perp\ \text{Weyl (secteur } g_{(3)}\text{, marée) — dans le cas symétrique.}\ }$$

**Le pont #5 → D3 ne tient pas dans le secteur symétrique.** Les deux principes sont
indépendants : l'un contraint le fond, l'autre la partie sans-trace transverse `g₍₃₎`
(cf. `LC-A` : `g₍₃₎` = Weyl rescalé). Ils ne se recouvrent qu'au-delà de FLRW.

<svg width="100%" viewBox="0 0 660 250" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Deux secteurs orthogonaux : fond (m,λ) / marée (Weyl, g₃)</title>
  <desc>Le verrou D1 a deux secteurs. Le secteur de fond porte les paramètres m et lambda ; la stabilité inter-éons y agit et fixe une relation. Le secteur de marée porte le tenseur de Weyl rescalé g3 ; l'hypothèse de Weyl D3 y agit. En FLRW le secteur de marée est vide (Weyl nul), donc D3 est vacant et la stabilité n'y rencontre pas Weyl. La fermeture de D1 doit venir du secteur de marée, dans le cas inhomogène.</desc>
  <rect x="30" y="40" width="270" height="170" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="165" y="66" text-anchor="middle" font-size="13.5" font-weight="500" fill="#0F6E56">secteur de FOND</text>
  <text x="165" y="92" text-anchor="middle" font-size="12" fill="#3d3d3a">paramètres (m, λ), g₍₀₎</text>
  <text x="165" y="126" text-anchor="middle" font-size="12" fill="#0F6E56">candidat #5 : stabilité</text>
  <text x="165" y="146" text-anchor="middle" font-size="11.5" fill="#3d3d3a">fixe la relation m̂λ̂=9k²/4</text>
  <text x="165" y="172" text-anchor="middle" font-size="11.5" fill="#A32D2D">ne ferme pas (1 param.)</text>
  <text x="165" y="192" text-anchor="middle" font-size="11.5" fill="#A32D2D">dégénère à k=0</text>
  <rect x="360" y="40" width="270" height="170" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="495" y="66" text-anchor="middle" font-size="13.5" font-weight="500" fill="#993C1D">secteur de MARÉE</text>
  <text x="495" y="92" text-anchor="middle" font-size="12" fill="#3d3d3a">Weyl rescalé = g₍₃₎</text>
  <text x="495" y="126" text-anchor="middle" font-size="12" fill="#993C1D">D3 : hypothèse de Weyl</text>
  <text x="495" y="146" text-anchor="middle" font-size="11.5" fill="#3d3d3a">FLRW : Weyl ≡ 0 (vacant)</text>
  <text x="495" y="172" text-anchor="middle" font-size="11.5" fill="#0F6E56">agit dans l'inhomogène</text>
  <text x="495" y="192" text-anchor="middle" font-size="11.5" fill="#0F6E56">→ route de fermeture ?</text>
  <line x1="300" y1="125" x2="360" y2="125" stroke="#534AB7" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="330" y="117" text-anchor="middle" font-size="11" fill="#A32D2D">⊥</text>
  <text x="330" y="234" text-anchor="middle" font-size="11" fill="#3C3489">indépendants en FLRW</text>
</svg>

*Fig. — Les deux secteurs du verrou D1. La stabilité (#5) agit sur le fond `(m,λ)` ; la
condition de Weyl (D3) sur la marée `g₍₃₎`. En FLRW le secteur de marée est vide
(Weyl≡0), donc les deux ne se rencontrent pas — la fermeture doit venir de la marée,
hors symétrie.*

---

## 5. Verdict et redirection

- **Candidat #5 ne ferme pas D1.** (a) Il fixe une *relation* (`m̂λ̂=9k²/4`), laissant
  une famille à un paramètre ; (b) il **dégénère à `k=0`** (univers plat), où la
  stabilité est générique et ne sélectionne rien ; (c) il est **indépendant de D3**
  dans le secteur symétrique (Weyl≡0). `[établi]`
- **Acquis positif.** La fermeture de D1 **ne peut pas provenir du secteur symétrique**
  (fond `(m,λ)`) : tout y est soit cartographié (atlas), soit marginal (stabilité), soit
  vacant (Weyl). Le degré de liberté qui *reste* à fixer est `g₍₃₎`, la marée — secteur
  où la condition de Weyl (D3) a, elle, un contenu réel.
- **Redirection (la vraie leçon).** Le bon candidat-sélecteur n'est pas la stabilité du
  fond mais **D3 (Weyl `→0`) dans le cas inhomogène** : imposer que la marée du nouvel
  éon naisse « lisse » (`g₍₃₎` contraint par `C_{abcd}→0` au crossover) est le principe
  qui agit sur le bon degré de liberté. C'est `décision ouverte / à inventer`, et
  **hors de portée** d'un sceau FLRW — il faut un modèle anisotrope/inhomogène
  (Bianchi A, déjà traité par Tod ; ou perturbations de FLRW).

---

## 6. Format de chaînon

- **Hypothèse testée.** « La stabilité inter-éons sélectionne une prescription unique
  et coïncide avec D3. »
- **Outil.** Carte de récurrence de Markwell–Stevens (analyse exacte : invariant,
  Jacobien, ratio) ; tenseur de Weyl symbolique (FLRW vs Kasner).
- **Critère de réfutation de l'hypothèse.** Si la stabilité fixait un facteur unique
  *et* équivalait à `C→0`, #5 fermerait D1. — **Réfutée** : relation seulement,
  dégénérescence `k=0`, `Weyl≡0` en FLRW.
- **Verdict.** #5 **rétrogradé** (contrainte, non fermeture). **D3-inhomogène promu**
  comme route principielle vers la fermeture de D1. `[verdict établi ; suite décision ouverte]`

---

## 7. Renvois, glossaire, références

**Renvois.** Parent `LC-A-D1-FACTEUR-CONFORME` (§5 candidat #5 ; §4-bis atlas ; §3
`g₍₃₎`) ; `LC-A-SURVIE-CONFORME` (`g₍₃₎` = Weyl rescalé) ; module `[D3]` Weyl,
`[E]` échelle ; contraste φ (verrou *fermé*).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Stabilité inter-éons (candidat #5)* : exiger `(m,λ)` non emballés ⟹ relation
  `m̂λ̂=9k²/4` (`k≠0`) ; ne ferme pas D1 ; vacant à `k=0`.
- *Secteur de fond / secteur de marée* : décomposition `(m,λ,g₍₀₎)` vs `g₍₃₎` (Weyl
  rescalé) ; stabilité agit sur le fond, Weyl sur la marée ; indépendants en FLRW.
- *Carte non-hyperbolique / bifurcation marginale* : Jacobien à valeur propre 1 double ;
  droite fixe non attractive ; runaway géométrique hors d'elle.

**Références (`LC-04`).** Markwell–Stevens, GRG **55**, 93 (2023) `[confirmé, KB]` (carte
éq. 14) ; Kasner `[établi, manuel]` ; hypothèse de Weyl : Penrose, *Cycles of Time*
(2010) ; Tod, J. Phys. Conf. Ser. **229**, 012013 (2010).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
