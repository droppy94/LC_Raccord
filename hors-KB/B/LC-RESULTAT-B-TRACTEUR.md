---
id: LC-RESULTAT-B-TRACTEUR
titre: "Résultat — Module [B] : calcul tracteur explicite sur S²"
codename: LC-RACCORD
branche: "[B] — objet géométrique sur S² (géométrie de Cartan conforme)"
regime: "Actionnable — moyens internes (décidable aujourd'hui)"
statut: "TRANCHÉ — calcul mené. Verdict : B-PAUVRE au sens strict du critère, avec résidu localisé (Weyl rescalé). {A4 ; A2★ ; N} INCHANGÉ."
depend_de: [LC-PAQUET-B-OBJET-S2, LC-A-SURVIE-CONFORME]
verification: "verif_B_tracteur.py (écrit, EXIT 0)"
version: "1.0 (calcul mené)"
langue: fr
maj: "v1.0 — calcul tracteur exécuté ; §3→§7 remplis ; verdict tranché et vérifié."
---

# Résultat — Module [B] : calcul tracteur explicite sur S²

> **Statut `[tranché]`.** Le calcul est mené et vérifié (`verif_B_tracteur.py`, EXIT 0).
> Le noyau **{A4 ; A2★ ; N}** reste **INCHANGÉ** ; CCC non démontrée ni réfutée. Ce
> document *situe* l'objet géométrique de `[B]` et tranche son critère de réfutation ;
> il ne réduit aucune hypothèse du noyau. « Calcul mené » ≠ « CCC avancée » (garde-fou §8).

---

## 0 · Rôle de ce document

`[B]` est la seule branche **décidable avec les moyens internes**. La reformulation
Cartan/tracteur était acquise (`LC-PAQUET-B-OBJET-S2`) ; **ce qui manquait était le
calcul explicite**. Il est ici, avec son verdict et le script qui le vérifie. Alimente
le `§5 Journal` du fichier de direction.

---

## 1 · Question tranchée par ce calcul `[fixée avant de commencer]`

> Une fois la métrique effacée à la fin d'éon, la structure conforme conserve une
> **connexion de Cartan canonique** (fibré tracteur). **Cette connexion est-elle assez
> riche pour qu'une théorie de champ vive sur `S²`, ou toute la dynamique espérée est-elle
> jaugée à zéro ?**

Deux issues écrites **avant** le calcul :

- **B-RICHE** — la connexion transporte une information dynamique non triviale ⟹ `[B]`
  porte effectivement le contenant *dynamique* de `{[C], [D]}`.
- **B-PAUVRE** — toute la dynamique est jaugée à zéro ⟹ la charge de cohérence bascule
  **entièrement sur `[C]`**, et le §3 du texte-source doit être réécrit.

*Issue honnête déclarée avant calcul :* **ouverte, sans préférence.** *(Résultat obtenu :
B-PAUVRE au sens strict, avec un résidu qui n'était prévu par aucune des deux étiquettes —
voir §5. La formulation binaire du critère est elle-même trop grossière ; §6.)*

---

## 2 · Données d'entrée `[interface amont, établies]`

- **De `[A]` (`LC-A-SURVIE-CONFORME`)** : structure conforme régulière à travers `ℐ⁺`,
  sceau `N|ℐ⁺ = −Λ/3 < 0`, extension non dégénérée (équations d'Einstein conformes,
  Friedrich 1986). C'est la structure que `[B]` doit habiller d'une connexion. **Point
  clé récupéré de `[A]` :** la donnée physique libre à `ℐ⁺` est le couple `(g₍₀₎, g₍₃₎)`,
  où `g₍₃₎` est le **tenseur de Weyl rescalé** (TT, 2 polarisations).
- **Objet géométrique** : fibré des directions nulles `N → M`, fibre `S²` (sphère céleste)
  = espace des directions nulles en un point 4D.
- **Formalisme** : calcul tracteur / géométrie de Cartan conforme (Bailey–Eastwood–Gover,
  ~1994 ; Čap–Slovák pour les géométries paraboliques).

> `[Références à vérifier sur arXiv / INSPIRE-HEP avant citation formelle — R-41 : ≥3 miroirs.
>  Les théorèmes invoqués ici (BEG ; tracteur plat ⟺ Weyl=0 en n≥4) sont standards mais
>  cités, non re-dérivés depuis les axiomes — d'où le grade « borné » du §5.]`

---

## 3 · Mise en place du calcul `[mené]`

**Fibré tracteur standard.** Sur un conforme 4D lorentzien `(M,[g])`, le fibré tracteur
`𝒯` est de **rang 6**, groupe de structure `O(4,2)`. Dans une échelle (choix de `g` dans
la classe), une section se scinde `V = (σ, μₐ, ρ)` (poids +1, 0, −1). La **connexion de
tracteur** canonique `∇^𝒯` (BEG) s'écrit

```
        ⎧ ∇ₐσ − μₐ
∇ₐ V =  ⎨ ∇ₐμ_b + g_{ab} ρ + P_{ab} σ
        ⎩ ∇ₐρ − P_{ab} μ^b
```

où `P_{ab} = ½ (R_{ab} − R/6 · g_{ab})` est le tenseur de Schouten (n=4). Cette connexion
est **canonique et sans paramètre libre** : entièrement fixée par la classe conforme.

**Reconstruction de `N → M`.** Le fibré des directions nulles est le fibré associé
`N = 𝒯₀ / ℝ₊` des rayons nuls du cône de tractor (`h(V,V)=0`, `h` la métrique de tracteur
`O(4,2)`). Les fibres `S²` sont les sphères célestes ; `∇^𝒯` induit le **transport
parallèle des directions nulles** le long des géodésiques nulles (non paramétrées), ce qui
**rétablit la comparaison globale** des fibres — c'est exactement la réfutation de « cônes
incomparables » portée par la reformulation.

**Courbure de tracteur.** `Ω_{ab} = [∇ₐ, ∇_b]^𝒯` se décompose en **deux et seulement deux**
morceaux irréductibles :

```
Ω  ⟷  ( W_{abcd} ,  A_{abc} )        W = Weyl,  A = Cotton = 2∇_{[b}P_{c]a}
```

En **n = 4**, `A_{abc} ∝ ∇^d W_{dabc}` : le Cotton est la divergence du Weyl, donc **le
Weyl fixe toute la courbure de tracteur**. Théorème (BEG / Čap–Slovák) : **`∇^𝒯` est plate
⟺ `(M,[g])` conformément plat ⟺ `W_{abcd} = 0`** (n≥4).

Hypothèses de travail : signature lorentzienne `(3,1)` ; conventions Riemann standard
(vérifiées dans le script) ; on travaille sur le fond dS puis sur une inhomogénéité type-M.

---

## 4 · Mesure de l'information transportable `[mené — chiffré]`

Tout est réduit à : **que vaut la courbure de tracteur = Weyl (⊕ Cotton) sur la structure
conforme survivante ?** Trois mesures, toutes vérifiées symboliquement (`verif_B_tracteur.py`).

**(i) Sur le fond de Sitter exact — jaugé à zéro.**
dS (tranchage fermé, `ds² = (H² cos²η)⁻¹(−dη² + dΩ₃²)`) est **conformément plat** :
`Weyl(dS) ≡ 0` (vérifié). De plus dS est Einstein, `Schouten = (H²/2) g` avec coefficient
**constant** ⟹ `∇P = 0` ⟹ `Cotton(dS) ≡ 0` (vérifié). Donc

> **`Ω^𝒯(dS) = 0` : la connexion de tracteur est PLATE sur le fond.** Holonomie triviale
> (localement), transport indépendant du chemin. **Aucune information locale transportable :
> tout est pure jauge (Möbius `PSL(2,ℂ)`).**

**(ii) Sur la fibre `S²` elle-même — pas d'invariant local.**
En dimension `≤ 3`, le Weyl est identiquement nul (comptage d'indices). Vérifié
explicitement sur `S²` : le Riemann 2D est **entièrement reconstruit par la courbure
scalaire** (`R_{abcd} = (R/2)(g∧g)`), partie sans-trace (Weyl) vide ; `K = 1/a²`.

> **La géométrie conforme intrinsèque de la fibre `S²` est rigide (Möbius), sans aucun
> degré de liberté de champ local.** Une théorie de champ ne « vit » pas intrinsèquement
> sur `S²` du seul fait de la structure conforme.

**(iii) Le résidu, précisément localisé — le Weyl rescalé.**
Une inhomogénéité (Schwarzschild–de Sitter, masse `M`) donne `Weyl(SdS) ≠ 0`, composante
Coulombienne `C_{trtr} = −2M/r³`, qui **s'annule si `M → 0`** (retour au fond plat).
Le seul contenu dynamique transportable est donc **exactement le Weyl rescalé** — c'est,
mot pour mot, la donnée `g₍₃₎` de Friedrich à `ℐ⁺` : un **TT à 2 polarisations**.

> **Structure transportée** = le Weyl rescalé `g₍₃₎` (2 polarisations radiatives) ⊕ la
> comparaison des fibres (cinématique). **Jauge résiduelle** = tout le reste (Möbius de
> fibre + facteur conforme). Le point crucial : `g₍₃₎` est une **donnée libre injectée**
> — la connexion l'*organise*, elle ne le *génère* pas ; et il vit sur `ℐ⁺ ≃ S³`, pas
> intrinsèquement sur la fibre céleste `S²`.

---

## 5 · Verdict contre le critère de réfutation `[le cœur — tranché]`

Critère (recopié de `LC-PAQUET-B-OBJET-S2 §4`, non modifié) :

> Si le calcul tracteur montre que la connexion conforme **ne distingue pas assez
> d'information pour qu'une théorie de champ y vive** (toute la dynamique jaugée à zéro),
> alors la colle doit venir **entièrement de `[C]`**, et le §3 du texte-source doit être réécrit.

- **Issue retenue : `B-PAUVRE` (au sens strict du critère).**
  Portée par §4(i)+(ii) : la courbure de tracteur — seule porteuse d'information locale —
  s'annule sur le fond dS, et la fibre `S²` (2D) ne porte aucun invariant conforme.
  **Aucune dynamique de champ ne vit intrinsèquement sur `S²` par la connexion seule.**
  La « colle » dynamique n'est **pas produite** par la géométrie conforme de `[B]`.

- **Résidu obligatoire à consigner (aucune des deux étiquettes ne le prévoyait).**
  `[B]` n'est pas vide pour autant : il livre (a) le **contenant** — fibré `𝒯` + comparaison
  canonique des fibres (réfutation de « cônes incomparables », acquise) ; (b) la **structure
  projective des rayons nuls** (géodésiques nulles non paramétrées, conservées). Le contenu
  *dynamique* — 2 polarisations `g₍₃₎` — est réel mais **externe à la connexion** : donnée
  libre de `[D]`/Friedrich, à faire vivre par `[C]`.

- **Grade : `borné / structurel`.** Repose sur des théorèmes standards (BEG ; tracteur plat
  ⟺ Weyl=0) **cités**, appliqués à ce cadre, + une vérification symbolique **reproduite**
  des faits porteurs (Weyl(dS)=0, Cotton(dS)=0, Weyl(SdS)≠0, Weyl 2D≡0). N'est **pas** un
  calcul de courbure de tracteur reconstruit composante-à-composante depuis les axiomes sur
  un dS *perturbé* portant `g₍₃₎` — c'est l'étape qui ferait passer de `borné` à `reproduit`
  (voir §7, TODO).

- **Ce que l'issue N'autorise PAS à dire.** Elle ne réduit pas `{A4 ; A2★ ; N}`. Elle
  **situe** l'architecture de la colle (le dynamique n'est pas dans le conforme de `[B]`),
  rien de plus. Elle ne conclut ni ne réfute la CCC.

---

## 6 · Conséquences `[remplies]`

- **Sur le compte : `{A4 ; A2★ ; N}` — INCHANGÉ** (confirmé ; le résultat est structurel,
  aucune hypothèse du noyau n'est touchée).
- **Sur le §3 du texte-source.** À réécrire dans ses *conséquences* : « cônes incomparables »
  reste faux (la comparaison est rétablie), **mais** l'attente implicite qu'une dynamique
  vive sur la structure conforme seule est infirmée — la dynamique est une **donnée libre**,
  pas une production de la connexion.
- **Sur `[C]` (bascule).** Le critère `B-PAUVRE` étant atteint, **la charge de cohérence
  dynamique revient à `[C]`** : la CFT sur `S²` + hamiltonien modulaire doit *produire* la
  dynamique que la géométrie conforme ne fournit pas. Réimport `LC-PAQUET-C-COHERENCE-QUANTIQUE`
  recommandé à la prochaine session P2.
- **Sur `[D]`.** `[B]` livre à l'holographie un objet **précis** : le fibré `𝒯` (rang 6,
  `O(4,2)`) + la donnée libre `g₍₃₎` (Weyl rescalé, 2 pol.) à `ℐ⁺ ≃ S³`. **Nuance nommée :**
  la fibre céleste `S²` (directions nulles) et `ℐ⁺ ≃ S³` (où vit `g₍₃₎`) sont **distincts** ;
  ne pas les conflater dans la colonne `[D]`.
- **Fichier de direction.** Ajouter la ligne au `§5 Journal`, **déporter `[B]`** (branche
  close → stockage froid), ne garder que sa ligne de registre + réimport minimal.

---

## 7 · Vérification `[écrite — EXIT 0]`

`verif_B_tracteur.py` (sympy, sans réseau, re-exécutable) vérifie :
- (A) `Weyl(dS) ≡ 0` — conformément plat ⟹ tracteur plat sur le fond ;
- (B) `Ric(dS)=Λg`, `Schouten=(H²/2)g` constant ⟹ `Cotton(dS) ≡ 0` ;
- (C) `Weyl(SdS) = −2M/r³ ≠ 0`, `→0` si `M→0` — résidu = Weyl rescalé ;
- (D) fibre 2D : Riemann fixé par `R`, `Weyl ≡ 0`, `K=1/a²` — pas d'invariant local sur `S²`.

Sortie : **EXIT 0**, toutes assertions passent.

- [ ] **TODO (pour passer `borné → reproduit`)** : calcul de `Ω^𝒯` composante-à-composante
      sur un dS *perturbé* portant `g₍₃₎`, montrant que la seule composante non nulle de la
      courbure de tracteur est le Weyl rescalé. Non requis pour le verdict, mais durcirait le grade.

---

## 8 · Références `[orientation, non exhaustif]`

- Bailey, Eastwood, Gover — calcul **tracteur** pour structures conformes/projectives (~1994).
- Čap–Slovák — **géométries paraboliques** / géométrie de Cartan (tracteur plat ⟺ Weyl=0).
- Friedrich 1986 — extension conforme régulière ; donnée libre `(g₍₀₎, g₍₃₎)` à `ℐ⁺`.
- `LC-A-SURVIE-CONFORME` — interface amont `[A]` (source de `g₍₃₎`, sceau `N|ℐ⁺=−Λ/3<0`).
- `LC-PAQUET-B-OBJET-S2` — reformulation, fiche-chaînon et critère de réfutation source.
- `LC-PAQUET-C-COHERENCE-QUANTIQUE` — destinataire de la charge dynamique (`B-PAUVRE`).

> **Garde-fou de portée.** « Calcul mené » ≠ « CCC avancée ». `[B]` situe l'objet
> géométrique et tranche son critère ; il ne réduit aucune des trois hypothèses du noyau.
> Grade `borné/structurel` : théorèmes standards cités + vérification symbolique reproduite.
> `{A4 ; A2★ ; N}` INCHANGÉ ; CCC non démontrée ni réfutée.
