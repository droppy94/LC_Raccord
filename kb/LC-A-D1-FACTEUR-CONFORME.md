---
id: LC-A-D1-FACTEUR-CONFORME
titre: "Module A / verrou D1 — l'unicité du facteur conforme au crossover"
codename: LC-RACCORD
tags: [module-A, D1, ccc, facteur-conforme, reciprocite, crossover, bandage, tod, newman, nurowski, friedrich-data]
type: chaînon (verrou du module A, isolé par LC-A-SURVIE-CONFORME)
statut: cartographie établie (sous-détermination + dispositif + atlas FLRW : liberté réduite au seul c₁) ; DÉLIMITÉ par le verdict d'axe LC-D-D1-VERROU-DELIMITATION (aucun sélecteur de prescription par les moyens internes ; §5 candidats SUPERSÉDÉS) ; condition (ii) D1c3-3 DÉCHARGÉE (généricité confirmée — audit froid CONFIRMATION) ; résidu réellement ouvert = amplitude A_T~1/N (|≤3-pt ; ≥4 ouvert) ; sélection par intrant externe = décision ouverte / à inventer
version: 0.5
langue: fr
date: 2026-06-09
maj: "2026-06-28 — v0.5 : CONSOLIDATION cartographique (net-zéro, SANS sceau, patch ADDITIF — corps §0–§8 intact ; seuls version/statut/maj modifiés + 2 insertions §0-bis/§5). Ajout §0-bis : inscription du verdict d'axe LC-D-D1-VERROU-DELIMITATION (DÉLIMITATION — aucun sélecteur de prescription par les moyens internes ; secteur symétrique FLRW = Δ1-b [LC-D-D1-VERROU-FLRW], secteur inhomogène Bianchi A = D1c3-c [LC-D-D1-VERROU-INHOMOGENE, sceau EXIT 0] ; ni fermeture ni réfutation ; converge avec LC-D-IRREDUCTIBILITE-MOYENS, A4 nœud-source) ; condition (ii) DÉCHARGÉE — D1c3-3 confirmé GÉNÉRIQUE (non-artefact d'homogénéité ; sceau verif_D1c3_genericite.py b615d6b4, audit froid incognito = CONFIRMATION ; levée portée à l'étage axe par LC-WORK-AMENDEMENT-R7-D1-AXE-II-LEVEE), reste la seule condition (i) ; §5 (candidats-sélecteurs) marqué SUPERSÉDÉ (#5 stabilité rétrogradé [LC-A-D1-STABILITE-WEYL] ; D3-inhomogène → délimitation : la régularité ne sélectionne pas) ; résidu ouvert restaté = amplitude A_T~(H/M_P)²~1/C_T~1/N rattachée au compte N, qualificatif |≤3-pt ; ≥4 ouvert (LC-D-D1-VERROU-AMPLITUDE). §6.4 : consolider une carte ne PROUVE rien, ne construit rien, ne ferme pas D1 (OUVERT, caractérisé), ne fixe pas N (≡Λ), ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée. | 2026-06-09 — v0.4 : §5 (candidat-sélecteur 3) — propagation de la passerelle D1⟷E (LC-WORK-D1-E-AMPLITUDE v0.1, paper-first). Précision ajoutée : la FORME du deux-point ⟨g₃g₃⟩∝k³ est elle-même scellée (SPECTRE-K3) ; la prescription D1 ne reste donc à inventer que pour une AMPLITUDE A_T~(H/M_P)² (et non plus un deux-point), candidat-fixée par la charge centrale céleste A_T~1/C_T~1/N (scaling) — le résidu de D1 se rattachant au compte N de [E]. SANS fermeture : D1 reste le verrou ouvert ; aucune touche algèbre/atlas/verdict. | 2026-06-09 — v0.3 : §5 (candidat-sélecteur 3, hypothèse de Weyl) précisé après la passerelle A3⟷D1 (LC-WORK-A3-D1-PASSERELLE v0.2, sceau verif_A3_D1_passerelle.py 11/11). A3 (dS-invariance) et A4 (WCH) fixent DÉJÀ le UN-POINT de la marée g₍₃₎ (⟨g₃⟩=0, coïncidence Bunch-Davies scellée au un-point perturbatif) ; la prescription D1 ne reste donc `à inventer` que pour le DEUX-POINT ⟨g₃g₃⟩~k³ (SPECTRE-K3). Précision de cartographie, SANS fermeture : D1 reste le verrou ouvert (le deux-point = donnée de Cauchy [D]) ; aucune touche à l'algèbre, à l'atlas §4-bis ni au verdict. Portée FLRW inchangée. | 2026-06-07 — v0.2 : ajout de l'atlas explicite (§4-bis) en FLRW radiation+Λ, d'après Markwell-Stevens (GRG 55,93 2023). Les trois prescriptions (Tod/Newman/Nurowski) convergent sur la famille Ω̂=c₁â ; toute la liberté D1 se concentre dans le constant c₁. Sceau dur (verif_D1_atlas.py) : coïncidence au point fixe m̂λ̂=9k²/4, divergence sinon, et bifurcation INSTABLE de l'itération inter-éons (runaway de m,λ) sauf accord fin. Seule la condition de Penrose (55d) est satisfiable. Candidat-sélecteur #5 ajouté (stabilité inter-éons). Portée : FLRW seulement, cas inhomogène non couvert ; cartographie, non fermeture. v0.1 : dispositif + sous-détermination + sceau background."
statut_id: enregistré en KB (LC-00 v1.8, LC-02 v1.2, LC-03 v1.8) — v0.2 ajoute l'atlas
fichier_compagnon: [verif_D1_facteur.py, verif_D1_atlas.py]
renvois: [LC-00-INDEX, LC-01-CADRE, LC-02-PROGRAMME, LC-A-SURVIE-CONFORME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[A] survie conforme — D1 en est le verrou formel"
  - "[D] holographie — la donnée g₃ non fixée = donnée de Cauchy de [D]"
  - "[E] retour de l'échelle — le facteur conforme EST le champ d'échelle"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-A·D1 — Le facteur conforme au crossover

> **Cible.** `LC-A` a établi que le cœur géométrique du module A passe (extension
> conforme régulière à `𝓘⁺` spacelike, Friedrich) et que la charge ouverte **migre**
> vers **D1 : comment choisir le facteur conforme de façon unique au crossover ?**
> C'est *le* problème ouvert majeur de la CCC, et le verrou formel de A.
>
> **Verdict (cartographie + sceau).** La **sous-détermination est établie** : la
> réciprocité de Penrose est *une* relation scalaire ; elle fixe le **background** de
> la transition (sceau : dS-Λ → FRW-radiation) et la **classe conforme** au crossover,
> mais **ne fixe pas la donnée dynamique** (`g₃` = Weyl rescalé de `LC-A`). Le passage
> `ĝ₃ ↦ ǧ₃` est le contenu d'une **prescription**, et les trois prescriptions connues
> (Newman 2014, Tod 2015, Nurowski 2021) **divergent**. **D1 n'est pas clos** : statut
> `décision ouverte / à inventer`. Ce document est l'étage *cartographie* (analogue de
> `LC-07`), pas l'étage *fermeture* (analogue de `LC-10`).

---

## 0. Rôle et garde-fou

D1 est au module A ce que le verrou Gauss–Seidel (`LC-09`) était au sous-programme φ :
le point où « la géométrie tient » se heurte à « quelle règle physique fixe l'objet
restant ? ». **Différence honnête `[à ne pas perdre]`** : le verrou φ a été *fermé*
(`établi sous principes`) ; **D1 ne l'est pas**. Ici on *cartographie* le décidable et
on *isole* le choix — on ne le tranche pas. Présenter D1 comme « résolu » serait une
surinterprétation du type de celle corrigée en `LC-05` v0.2→v0.3.

---

## 0-bis. Consolidation (v0.5) — délimitation d'axe & condition (ii) déchargée `[lecture / non scellé]`

> **Mise à jour cartographique.** Ce nœud (rédigé v0.1–v0.4) a depuis été **délimité** par la chaîne
> verrou-D1. Le **§5** ci-dessous (candidats-sélecteurs) est **superséé** : il se lit en historique.
> Rien n'est scellé ici ; **§6.4** : consolider ne réduit rien.

**Verdict d'axe (gravé) — `LC-D-D1-VERROU-DELIMITATION` (2026-06-28).** Le verrou D1 **n'admet aucun
sélecteur de prescription par les moyens internes**. Deux secteurs consolidés :

- **secteur symétrique (FLRW) = `Δ1-b`** (`LC-D-D1-VERROU-FLRW`) : l'atlas (§4-bis) ramène toute la
  liberté à `c₁` ; le **candidat #5** (stabilité inter-éons) est **rétrogradé** — il ne fixe qu'une
  *relation* `m̂λ̂=9k²/4`, est **vacant à `k=0`** (univers plat), et **⊥ Weyl** (`C≡0` en FLRW) ; son
  ancrage `A4` y est mort. (`LC-A-D1-STABILITE-WEYL`.)
- **secteur inhomogène (Bianchi A) = `D1c3-c`** (`LC-D-D1-VERROU-INHOMOGENE`, sceau EXIT 0) : aucune
  condition de **régularité naturelle** (Friedrich — donnée de bord `h^{TT}` **libre** ; ni « Cotton→0 »,
  strictement **plus faible** qu'Einstein-3D) ne force `â` Einstein-3D ⟹ `σ̌=−4·(Ricci sans-trace)≠0`
  ⟹ **la régularité (D3) ne sélectionne pas** ; `A3` reste **socle indépendant** (`FW-3` : la seule
  condition sélectionnante — Ricci sans-trace `=0` imposé — est ≥ postulat indépendant non dérivable d'`A4`).

⟹ **Ni fermeture, ni réfutation.** Le sélecteur n'est pas *trouvé* : il est *caractérisé comme absent en
interne*. Seul un **intrant externe** (principe de sélection neuf, ou **postulat assumé**) rouvrirait une
route. **Converge** avec `LC-D-IRREDUCTIBILITE-MOYENS` (`A4` nœud-source ; routes internes épuisées).

**Condition (ii) déchargée `[neuf, cette session]`.** La clôture `R-53` du verdict d'axe était
conditionnelle à *(ii) le résultat inhomogène (Bianchi A) **généralise** — `D1c3-3` PENDANTE*. `D1c3-3` est
désormais **confirmé GÉNÉRIQUE** (non-artefact d'homogénéité : un mode TT inhomogène source un Ricci
sans-trace `½k²H ≠0`, `∝k²` ; sceau `verif_D1c3_genericite.py`, audit froid incognito indépendant =
**CONFIRMATION**). La condition (ii) est **levée** — portée à l'étage axe par
`LC-WORK-AMENDEMENT-R7-D1-AXE-II-LEVEE`. **Reste la seule condition (i)** : aucun principe de sélection
interne exhibé.

**Résidu réellement ouvert.** Le **un-point** `⟨g₃⟩=0`, la **forme** du deux-point `∝k³` et le secteur
Weyl-magnétique sont **scellés** ; ce qui reste libre est l'**amplitude** `A_T~(H/M_P)²~1/C_T~1/N`,
rattachée au **compte `N`** de `[E]` avec qualificatif **`|≤3-pt ; ≥4 ouvert`** (`LC-D-D1-VERROU-AMPLITUDE`).
C'est le **dernier degré de liberté de D1** — il **pointe vers `N`** (périmètre `{A4 ; A2★ ; N}`), il n'est
**pas tranché**.

> **`§6.4`.** Consolidation cartographique, **sans sceau**, aucune algèbre neuve : ne ferme pas D1 (OUVERT,
> caractérisé), ne fixe pas `N` (`≡Λ`), ne réduit pas `A4`. `{A4 ; A2★ ; N}` **INCHANGÉ** ; CCC non
> démontrée NI réfutée.

---

## 1. Le dispositif — bandage region et réciprocité `[établi, sourcé]`

Autour de la 3-surface de crossover `𝒞` (le « wound » de Penrose : `𝓘⁺` du passé ≡
Big Bang du futur), la **bandage region** porte **trois métriques** conformément
reliées (notation chapeau = éon passé, caron = éon futur) :

$$\hat g_{ab} = \hat\Omega^2\, g_{ab}\quad(\text{passé, physique}),\qquad
\check g_{ab} = \check\Omega^2\, g_{ab}\quad(\text{futur, physique}),$$

avec `g` une métrique **régulière** (le « pont ») au crossover. À l'approche de `𝒞`,
le facteur conforme **se retourne** : l'un tend vers `0`, l'autre vers `∞`.

**Hypothèse réciproque de Penrose** `[sourcé]` :

$$\boxed{\;\hat\Omega\,\check\Omega = -1\;}\qquad(\text{Penrose, } Cycles\ of\ Time, 2010).$$

Les deux métriques physiques doivent en outre satisfaire **chacune** les équations
d'Einstein (avec leur `Λ` et leur matière). `[établi — dispositif standard ; Penrose,
Tod 2015, Nurowski 2021]`

---

## 2. Sceau — le background de la transition `[établi]`

Compagnon : `verif_D1_facteur.py` (sympy). Pont conformément plat
`g = -\mathrm{d}\eta^2 + \mathrm{d}\vec x^2`. Si le passé est exactement de Sitter
(slicing plat, `\hat\Omega = -1/(H\eta)`), la réciprocité donne
`\check\Omega = -1/\hat\Omega = H\eta`, d'où la métrique physique future

$$\check g = \check\Omega^2 g = H^2\eta^2\big(-\mathrm{d}\eta^2 + \mathrm{d}\vec x^2\big),
\qquad a(\eta)=H\eta.$$

Calcul symbolique :

$$R(\check g)=0,\qquad G_{00}=\frac{3}{\eta^2}>0,\qquad \mathrm{tr}\,G^a{}_a = 0.$$

Trace nulle + densité positive ⟹ **fluide de radiation** (`w=1/3`, sans `Λ`).

$$\boxed{\;\text{réciprocité : passé Λ-dominé (dS)} \;\longrightarrow\; \text{futur radiation-dominé (Big Bang)}\;}$$

C'est exactement l'image qualitative de la CCC, ici **vérifiée explicitement**. Le
*background* de la transition est donc **fixé** par la réciprocité. `[établi]`

> **Mais c'est le background seulement.** Ce calcul suppose le passé *exactement* dS
> (vide-`Λ`). Le vrai éon a de la matière, des perturbations, un tenseur de Weyl non
> trivial — c'est la **donnée dynamique `g₃`** de `LC-A` (Weyl rescalé). La réciprocité
> ne dit rien de son devenir au crossover. C'est là que vit D1.

---

## 3. Le cœur de D1 — la sous-détermination `[comptage établi]`

**Comptage de données conformes (via `LC-A` / Friedrich).** Près d'un `𝓘` spacelike,
une solution Einstein-`Λ` est déterminée par **deux** pièces (Friedrich, `LC-A` §2b) :

$$\text{donnée conforme} = \big(\underbrace{g_{(0)}}_{\text{3-métrique conforme}},\ \underbrace{g_{(3)}}_{\text{tenseur TT = Weyl rescalé}}\big).$$

Or la réciprocité `\hat\Omega\check\Omega=-1` est **une seule relation scalaire**. Elle
peut, au mieux :

- identifier la **classe conforme** `g_{(0)}` de part et d'autre de `𝒞` (le crossover
  partage une 3-géométrie conforme — conformément plate dans les modèles de Tod/Nurowski) ;
- fixer le **comportement de tête** du facteur conforme (le background, §2).

Elle **ne fournit pas** la seconde pièce `g_{(3)}` du futur. Autrement dit :

$$\boxed{\;\{\hat g_{(0)},\hat g_{(3)}\}\ +\ \text{réciprocité}\ \nRightarrow\ \check g_{(3)}.\;}$$

Le passage `\hat g_{(3)} \mapsto \check g_{(3)}` — *comment la donnée de Weyl du vieil
éon devient celle du neuf* — est précisément ce qu'une **prescription** doit ajouter.
La sous-détermination n'est pas un défaut de calcul : c'est, en clair (Nurowski),
« pour utiliser la réciprocité il faut choisir *soit* `\Omega` *soit* `g` » — un degré
de liberté fonctionnel non contraint. `[comptage établi ; formalisable]`

*(Lien `[E]` : ce facteur conforme indéterminé **est** le champ d'échelle `Ω` du
module `[E]` — « phantom field » de Penrose. D1 et `[E]` sont le même objet vu de deux
modules.)*

---

## 4. Cartographie des prescriptions `[formalisable / décision ouverte]`

Comme `LC-07` cartographiait les bundles avant d'assumer, on cartographie les
prescriptions sans en élire une. Chacune ajoute une condition pour fermer le degré de
liberté `g_{(3)}` ; elles **divergent** (Markwell–Stevens 2023).

| Prescription | Condition ajoutée | Cas traité | Statut / accroc |
|---|---|---|---|
| **Penrose** (2010) | réciprocité `\hat\Omega\check\Omega=-1` + Weyl `→0` + phantom field | qualitatif | sous-déterminé ; certains choix **écartés** par Markwell–Stevens |
| **Newman** (2014) | équations pour le champ d'échelle au crossover | FRW | **incohérences** corrigées par Markwell–Stevens (2023) |
| **Tod** (2015) | `\hat\Lambda = \mathrm{const}` ⟹ une **EDP pour `\Omega`** | FRW, Bianchi A | transition **unique** dans les cas symétriques traités |
| **Nurowski** (2021) | **Poincaré–Einstein** / Fefferman–Graham depuis `(\Sigma,[h_0])` conf. plat | radiatif (onde sphérique) | analyticité FG ; relié à la donnée de Friedrich |
| **Markwell–Stevens** (2023) | extension de Newman + nouvelle classe | comparaison | accord avec Penrose **sous une relation additionnelle** |

Lecture : il existe des prescriptions qui *ferment* D1 **dans les cas symétriques**
(Tod : EDP soluble ; Nurowski : FG) — donc D1 n'est **pas réfuté** (le raccordement
dynamique existe au moins là). Mais elles **ne coïncident pas** et reposent sur des
conditions additionnelles distinctes : **aucune n'est établie comme *la* prescription
physique**. `[le décidable : les prescriptions en cas symétriques — formalisable ;
le choix : décision ouverte]`

---

## 4-bis. Atlas explicite (FLRW radiation + Λ) — sceau dur `[formalisable, calculé]`

Comme `LC-07` réduisait φ à un **choix fini de bundle**, l'atlas FLRW réduit D1 à un
**choix d'une seule constante**. Source des équations : Markwell & Stevens, *Gen.
Rel. Grav.* **55**, 93 (2023), qui mettent les trois prescriptions côte à côte.
Compagnon : `verif_D1_atlas.py`.

**Réduction (le fait marquant).** Dans le cas FLRW radiation, les trois prescriptions
(Tod 2015 ; Newman 2014 étendu ; Nurowski 2021 corrigé) **convergent sur une seule
famille** :

$$\hat\Omega = c_1\,\hat a,\qquad \text{pont à courbure scalaire constante }\;
R = 6k\,c_1^2 = 4\lambda,$$

(équation de Yamabe/phantom-field $(\Box+\tfrac16 R)\hat\Omega=\tfrac16\hat R\hat\Omega^3$
satisfaite). **Toute la sous-détermination de D1 se concentre alors dans le seul
constant $c_1$.** Le `g₍₃₎` libre du §3 devient, en symétrie FLRW, ce scalaire. C'est
le pendant exact de la cartographie `LC-07` : la liberté fonctionnelle est ramenée à
un paramètre nommé.

**Atlas — comment chaque prescription fixe $c_1$ (et ce qu'elle sacrifie).**

| Prescription | choix de $c_1$ | $\lambda_{\text{pont}}=\tfrac{R}4$ | $(\check m,\check\lambda)$ | Penrose $\hat\lambda{=}\lambda$ ? |
|---|---|---|---|---|
| **Tod 2015** | $c_1=(\hat\lambda/\hat m)^{1/4}$ | $\tfrac32 k\sqrt{\hat\lambda/\hat m}$ | $(\hat m,\hat\lambda)$ **constants** | **non** (sauf accord fin) |
| **Markwell–Stevens / Penrose (55d)** | $c_1=\sqrt{2\hat\lambda/3k}$ | $\hat\lambda$ | $\big(\tfrac{9k^2}{4\hat\lambda},\ \tfrac{4\hat\lambda^2\hat m}{9k^2}\big)$ **itèrent** | **oui** |
| **Nurowski 2021 (corrigé)** | $c_1$ libre (forme analytique explicite de $\hat\Omega^2$) | $6kc_1^2/4$ | famille générale (chaque éon un $\lambda$) | selon $c_1$ |

**Sceau numérique (`verif_D1_atlas.py`, $k=1$).**
- **Coïncidence au point fixe** $\hat m\hat\lambda = \tfrac94 k^2$ : Tod = New = Nurowski
  (ex. $\hat m=\hat\lambda=1{,}5 \Rightarrow c_1=1$, $\check m=\check\lambda=1{,}5$,
  Penrose satisfait). Le désaccord **disparaît** sur cette courbe.
- **Divergence hors du point fixe** (ex. $\hat m=1{,}0,\ \hat\lambda=2{,}0$) : Tod garde
  $(\check m,\check\lambda)=(1{,}0,\ 2{,}0)$ **mais** $\lambda_{\text{pont}}=2{,}12\neq\hat\lambda$
  (viole Penrose) ; la classe Penrose-cohérente impose $\lambda_{\text{pont}}=\hat\lambda$
  **mais** $(\check m,\check\lambda)=(1{,}125,\ 1{,}778)\neq(\hat m,\hat\lambda)$.

**Sceau dur — le verrou a des dents `[établi numériquement]`.** L'itération
inter-éons de la classe **Penrose-cohérente** (récurrence
$\lambda_{i+1}=4\lambda_i^2 m_i/9k^2$, $m_{i+1}=9k^2/4\lambda_i$) conserve le produit
$m\lambda$ mais **fait diverger les composantes** : hors de l'accord fin
$\hat m\hat\lambda=\tfrac94 k^2$, on a $m\to 0$ et $\lambda\to\infty$ (ou l'inverse) au
fil des éons — **bifurcation instable** (sceau : $m\lambda=2{,}40$ fixe, mais $m$
décroît géométriquement de $0{,}9375$/éon). L'ambiguïté D1 n'est donc pas
cosmétique : selon la prescription, soit on sacrifie l'hypothèse $\hat\lambda=\lambda$
de Penrose (Tod), soit on subit un **emballement de la constante cosmologique et de la
densité** entre éons (classe Penrose-cohérente), sauf réglage fin.

**Verdict de Markwell–Stevens (repris) `[sourcé]`.** Parmi les quatre conditions de
Penrose pour fixer $\hat\Omega$ (leurs eq. 55a–d), testées sur ce modèle FLRW, **une
seule est satisfiable** : $3\Pi_a\Pi^a-\hat\lambda = O(\check\Omega^3)$ — qui impose
$c_1^2=2\hat\lambda/3k$, donc la classe Penrose-cohérente (avec « masse au repos
supprimée », $Q=0$). Les autres exigent $k=0\Rightarrow\lambda=0$ (violant
$\hat\lambda=\lambda$).

> **Portée honnête `[à ne pas perdre]`.** (i) Cet atlas est en symétrie **FLRW
> radiation** ; le cas **inhomogène** (`g₍₃₎` tensoriel complet) n'est pas couvert —
> la convergence des prescriptions sur une seule famille pourrait n'y plus tenir.
> (ii) Réduire D1 à *un constant* $c_1$ + un menu fini de conditions est un **progrès
> de cartographie** (analogue `LC-07`), **non une fermeture** (analogue `LC-10`) :
> aucune condition n'est *établie* comme physiquement obligatoire, et la condition la
> mieux placée (55d) entraîne un emballement inter-éons non résolu. **D1 reste
> ouvert.**

---

## 5. Le verrou — quel principe sélectionne LA prescription ?

> **⚠ SUPERSÉDÉ (v0.5) — lecture historique.** Le verdict d'axe `LC-D-D1-VERROU-DELIMITATION` a tranché :
> **aucun sélecteur de prescription par les moyens internes**. Candidat #5 **rétrogradé**
> (`LC-A-D1-STABILITE-WEYL`) ; route D3-inhomogène → **délimitation** (la régularité ne sélectionne pas,
> `D1c3-c`). Voir **§0-bis**. Les candidats ci-dessous se lisent désormais en historique de cartographie.

C'est le cœur ouvert. Par analogie avec φ (où la **quantification** a sélectionné
Gauss–Seidel parmi les Trotterisations), on cherche un **principe physique** qui
sélectionne `\check g_{(3)}` à partir de `\hat g_{(3)}`. Candidats `[à inventer]` :

1. **Analyticité de Fefferman–Graham** (Nurowski) : exiger une extension
   Poincaré–Einstein analytique fixe l'expansion. *Accroc* : l'analyticité est une
   hypothèse forte, non une nécessité physique.
2. **Continuation des données de Friedrich** : imposer que `(g_{(0)},g_{(3)})` se
   continue à travers `𝒞` comme solution unique des équations conformes (au sens de
   `LC-A`). *Accroc* : `𝒞` est une singularité du facteur conforme — la continuation
   n'est pas automatique.
3. **Hypothèse de Weyl (D3) comme contrainte** : `C_{abcd}\to 0` au crossover impose
   `\hat g_{(3)}\to 0`, ce qui *réduirait* la liberté. *Accroc* : ne fixe que la
   limite, pas l'application complète ; et la nécessité dynamique de Weyl `→0` est
   elle-même `décision ouverte`. *Précision `[passerelle A3⟷D1, LC-WORK-A3-D1-PASSERELLE
   v0.2]`* : A3 (dS-invariance de l'état) et A4 (WCH) fixent **déjà le un-point** de la
   marée, `⟨g₍₃₎⟩=0` (coïncidence Bunch-Davies, scellée au un-point perturbatif,
   `verif_A3_D1_passerelle.py` 11/11). La sous-détermination de D1 **est donc levée au
   un-point** ; la prescription ne reste `à inventer` que pour le **deux-point**
   `⟨g₍₃₎g₍₃₎⟩~k³` (`LC-D3-SPECTRE-K3`) — exactement la donnée de Cauchy de `[D]`.
   *Précision `[passerelle D1⟷E, LC-WORK-D1-E-AMPLITUDE v0.1]`* : la **forme** de ce
   deux-point (`∝k³`, `Δ=3`) est elle-même scellée (`SPECTRE-K3`) ; il ne reste donc
   `à inventer` qu'une **amplitude** `A_T~(H/M_P)²`, candidat-fixée par la charge centrale
   céleste `A_T~1/C_T~1/N` (scaling) — le résidu de D1 se rattachant au compte `N` de `[E]`.
4. **Principe variationnel / d'entropie** (spéculatif) : sélectionner la prescription
   extrémisant une fonctionnelle (entropie gravitationnelle de Penrose ?). *Pont
   possible* avec la colonne modulaire/KMS de `LC-RACCORD` — non construit.
5. **Stabilité / uniformité inter-éons** `[émergent de l'atlas §4-bis]` : exiger que la
   suite des $(m_i,\lambda_i)$ **ne s'emballe pas** d'éon en éon sélectionne le point
   fixe $\hat m\hat\lambda = \tfrac94 k^2$ — précisément la courbe où Tod, la classe
   Penrose-cohérente et Nurowski **coïncident**. La pathologie de runaway (sceau
   §4-bis) devient ainsi un *critère de sélection* : c'est le candidat le plus concret,
   issu directement de l'atlas. *Accroc* : il fixe une *relation* $\hat m\hat\lambda$,
   pas les valeurs ; et sa justification (pourquoi exiger la stabilité ?) reste à poser
   — possiblement reliée à l'hypothèse de Weyl / faible entropie (D3).

Aucun candidat n'est établi ; le candidat 5 (stabilité) est le plus directement motivé
par l'atlas. **D1 reste le verrou ouvert.** `[décision ouverte / à inventer]`

<svg width="100%" viewBox="0 0 680 300" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Verrou D1 : la réciprocité fixe le background, pas la donnée dynamique</title>
  <desc>Au crossover, la réciprocité Ω̂Ω̌=-1 relie passé et futur et fixe le background (dS vers radiation) et la classe conforme g0, mais laisse libre la donnée dynamique g3 (Weyl rescalé). Trois prescriptions (Newman, Tod, Nurowski) proposent des applications différentes de g3 passé vers g3 futur ; aucune n'est sélectionnée.</desc>
  <line x1="340" y1="40" x2="340" y2="260" stroke="#534AB7" stroke-width="3"/>
  <text x="340" y="32" text-anchor="middle" font-size="13" font-weight="500" fill="#3C3489">crossover 𝒞</text>
  <rect x="40" y="60" width="270" height="180" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="175" y="84" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">éon passé (ĝ=Ω̂²g)</text>
  <text x="175" y="120" text-anchor="middle" font-size="12" fill="#0F6E56">dS / Λ-dominé</text>
  <text x="175" y="150" text-anchor="middle" font-size="12" fill="#3d3d3a">g₍₀₎ (classe conf.)</text>
  <text x="175" y="174" text-anchor="middle" font-size="12" fill="#993C1D">ĝ₍₃₎ (Weyl rescalé)</text>
  <rect x="370" y="60" width="270" height="180" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="505" y="84" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">éon futur (ǧ=Ω̌²g)</text>
  <text x="505" y="120" text-anchor="middle" font-size="12" fill="#993C1D">radiation / Big Bang</text>
  <text x="505" y="150" text-anchor="middle" font-size="12" fill="#3d3d3a">g₍₀₎ (partagée)</text>
  <text x="505" y="174" text-anchor="middle" font-size="12" fill="#A32D2D">ǧ₍₃₎ = ?</text>
  <line x1="310" y1="118" x2="370" y2="118" stroke="#534AB7" stroke-width="2" stroke-dasharray="0"/>
  <text x="340" y="110" text-anchor="middle" font-size="10.5" fill="#3C3489">Ω̂Ω̌=-1</text>
  <text x="340" y="210" text-anchor="middle" font-size="11" fill="#0F6E56">✓ background fixé</text>
  <text x="340" y="226" text-anchor="middle" font-size="11" fill="#0F6E56">✓ g₍₀₎ fixée</text>
  <line x1="310" y1="174" x2="370" y2="174" stroke="#A32D2D" stroke-width="2" stroke-dasharray="5 4"/>
  <text x="340" y="166" text-anchor="middle" font-size="10.5" fill="#A32D2D">ĝ₃↦ǧ₃ ?</text>
  <text x="340" y="282" text-anchor="middle" font-size="11" fill="#A32D2D">✗ donnée dynamique g₃ non fixée — prescription requise (D1)</text>
</svg>

*Fig. — La réciprocité fixe le background et la classe conforme `g₍₀₎` (vert), mais
laisse libre la donnée dynamique `g₍₃₎` (rouge). Newman/Tod/Nurowski proposent des
applications `ĝ₃↦ǧ₃` différentes ; le principe qui en sélectionnerait une est le
verrou ouvert D1.*

---

## 6. Format de chaînon standard

- **Zone ambiguë.** « Le facteur conforme relie les éons » — mais lequel ?
- **Hypothèse de travail.** La réciprocité `\hat\Omega\check\Omega=-1` + Einstein des
  deux côtés + une **prescription** ferment le degré de liberté `g_{(3)}`.
- **Outil.** Équations conformes de Friedrich (donnée `(g_{(0)},g_{(3)})`) ; EDP de Tod
  (`\Lambda` const) ; expansion Fefferman–Graham (Nurowski) ; cas symétriques
  (FRW, Bianchi A) calculables.
- **Critère de réfutation.** Si l'on démontre qu'**aucune** prescription cohérente
  n'existe (toute application `ĝ_{(3)}\mapsto\check g_{(3)}` viole Einstein d'un côté),
  le raccordement *dynamique* échoue — et avec lui la CCC comme théorie, même si la
  géométrie de `LC-A` tient.
- **Verdict.** Critère **non satisfait** (des prescriptions existent en cas
  symétriques : Tod, Nurowski). Mais **aucune unicité** : la sélection est
  `décision ouverte / à inventer`. **D1 est le verrou actif du module A.**

---

## 7. Conséquence et pont vers le reste du programme

- **D1 est l'analogue, côté programme principal, du verrou Gauss–Seidel de φ** —
  *mais resté ouvert*. Étage atteint : **cartographie** (`LC-07`-like), pas
  **fermeture** (`LC-10`-like). Honnêteté stricte : ne pas surclasser.
- **D1 = `[E]`** : le facteur conforme indéterminé est le champ d'échelle. Trancher D1
  *est* trancher la dynamique de `[E]`. Les deux modules fusionnent sur cet objet.
- **D1 → `[D]`** : la donnée libre `\check g_{(3)}` (Weyl rescalé) est exactement la
  donnée de Cauchy holographique que `[D]` cherche à fixer (`LC-A` §2b). Une CFT
  céleste qui fournirait `\check g_{(3)}` *serait* une prescription D1 — pont concret
  et non encore exploité.
- **Prochain pas décidable recommandé** : refaire explicitement la cartographie §4 en
  un cas symétrique unique (FRW radiation + `Λ`), calculer les trois prescriptions
  côte à côte, et **exhiber numériquement leur divergence** (un sceau « atlas des
  prescriptions », analogue de l'atlas `LC-07`). C'est `formalisable` et borné.

---

## 8. Renvois, glossaire, références

**Renvois.** `LC-A-SURVIE-CONFORME` (parent : D1 isolé ; donnée `(g₀,g₃)`) ;
`LC-02` [A],[D],[E] ; `LC-01` §1 ; `LC-00`. Analogie : `LC-07` (cartographie),
`LC-09`/`LC-10` (verrou φ, *fermé* — contraste).

**Glossaire à ajouter (`LC-03`).**
- *Bandage region / wound / crossover `𝒞`* (déjà amorcé v1.7).
- *Réciprocité `\hat\Omega\check\Omega=-1`* (déjà amorcé v1.7).
- *Sous-détermination du facteur conforme (verrou D1)* : réciprocité = 1 relation,
  ne fixe pas `g₍₃₎`.
- *Prescription (Newman / Tod / Nurowski)* : condition additionnelle fermant `g₍₃₎`.
- *Expansion de Fefferman–Graham / Poincaré–Einstein* (Nurowski).

**Références (`LC-04`).** Déjà intégrées v1.5 (Friedrich, Penrose, Tod 2010/2015,
Newman 2014, Nurowski 2021, Markwell–Stevens 2023). À préciser : Tod, *The equations
of Conformal Cyclic Cosmology*, Gen. Rel. Grav. **47**, 17 (2015) `[confirmé]` ;
Nurowski, *Poincaré–Einstein approach to Penrose's CCC*, Class. Quantum Grav. **38**,
145004 (2021) `[confirmé]`.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
