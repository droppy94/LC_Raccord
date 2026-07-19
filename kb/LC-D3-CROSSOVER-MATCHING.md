---
id: LC-D3-CROSSOVER-MATCHING
titre: "Module D / crossover (a1) — consistance du matching ĝ₃=0 ↦ ǧ₃=0 : le vide est-il un point fixe du raccordement ?"
codename: LC-RACCORD
tags: [module-D, D3, crossover, raccordement, matching, reciprocite, g3, weyl, bunch-davies, point-fixe, atlas, D1, bianchi]
type: chaînon (front (a) du raccord, étape a1 ; pose le non-linéaire en isolant l'étape linéaire)
statut: point fixe ĝ₃=0↦ǧ₃=0 établi au niveau linéaire (fond FLRW), forcé pour les 3 prescriptions / non-linéaire + anisotrope + non-unitaire décision ouverte
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer si validé (index, programme [D]/crossover, glossaire, refs)
fichier_compagnon: verif_D3_crossover_matching.py
renvois: [LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-A-SURVIE-CONFORME, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-WORK-REPRISE-RACCORD, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D3] hypothèse de Weyl (C→0) — ici testée comme condition de raccordement, pas de bord"
  - "[A]/D1 facteur conforme — la réciprocité + l'atlas (c₁) induisent la carte ĝ₃↦ǧ₃"
  - "[D] holographie — ĝ₃,ǧ₃ = ⟨T⟩ de part et d'autre de 𝒞"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·CROSSOVER (a1) — Le vide comme point fixe du raccordement

> **Cible.** `LC-D3` a établi, **sur un mode TT de dS et à un seul bord** `𝓘⁺`, la
> coïncidence un-point `⟨g₍₃₎⟩_{BD}=0=g₍₃₎(C→0)`. Mais un crossover n'est pas un bord
> isolé : c'est **deux éons recollés** (`𝓘⁺` de l'éon passé ≡ Big Bang du futur, `LC-A`).
> L'énoncé « le nouvel éon naît dans le vide » est donc une **hypothèse sur le matching**
> `ĝ₍₃₎ ↦ ǧ₍₃₎`, pas un fait acquis. Première étape du front (a) (`LC-RACCORD` §10) :
> *le datum de vide `ĝ₍₃₎=0` (= `C→0`) se raccorde-t-il en `ǧ₍₃₎=0` — le vide est-il un
> **point fixe** de la carte de crossover induite par la réciprocité + les prescriptions
> de l'atlas D1 ?*
>
> **Verdict (calculé, `verif_D3_crossover_matching.py`).** **Oui — au niveau linéaire,
> et forcé.** Trois faits l'imposent. (i) Le **fond** du crossover (réciprocité
> dS-Λ → radiation) est **sans marée** : `Ĉ=Č=0`, donc `ĝ₍₃₎=ǧ₍₃₎=0` — le point fixe
> *existe*, le vide est littéralement le fond. (ii) La marée est **portée par le pont
> partagé** `g` du bandage ; le Weyl `(1,3)` `C^a{}_{bcd}` étant **conformément
> invariant** (vérifié), `ĝ₍₃₎` et `ǧ₍₃₎` sont deux rescalings du **même** datum
> radiatif. (iii) La carte induite par `Ω̂Ω̌=−1` est **homogène** (multiplicative :
> `δlnΩ̌=−δlnΩ̂`, aucune source additive), et aucune source TT ne peut être *fabriquée*
> localement sur un fond **isotrope** (la projection TT d'un tenseur `∝δ_ij` est nulle).
> Donc `ĝ₍₃₎=0 ⟹ ǧ₍₃₎=0` **pour Tod, Newman et Nurowski** : la liberté `c₁` de l'atlas
> ne déplace que le **facteur** de la carte des tides non nulles (objet de (a3)), pas
> l'existence du point fixe à zéro. `[établi, linéaire, FLRW]`
>
> **Ce que (a1) ne dit pas (le non-linéaire reste).** Homogénéité **linéaire** seulement :
> la back-réaction des fluctuations `k³` peut casser `0↦0` à `O(h²)` (→ (a2)) ; le point
> fixe peut être **instable** (couplage au runaway `(m,λ)` de l'atlas §4-bis → (a3)) ; un
> fond **anisotrope** (Bianchi A) fournit une structure TT et peut rendre la carte
> *inhomogène* (→ atlas inhomogène) ; un état de raccordement **non unitaire** (dS/CFT)
> pourrait injecter une source non-locale (→ (a2)). `[décision ouverte / à inventer]`

---

## 0. Rôle et garde-fou

Ce chaînon **pose** (a1) et le **tranche au niveau linéaire** ; il ne ferme pas le front
(a). Ce qui est `établi` : l'existence et le caractère **forcé** du point fixe `ĝ₍₃₎=0↦
ǧ₍₃₎=0` autour du fond FLRW du crossover, pour les trois prescriptions. Ce qui reste
`décision ouverte / à inventer` : tout ce qui est intrinsèquement non linéaire ((a2),
(a3)), le cas anisotrope, et la nature de l'état de raccordement. On ne surclasse pas :
« le vide est un point fixe » ne dit **ni** qu'il est stable, **ni** qu'il est unique,
**ni** qu'il survit à `O(h²)` — ces trois questions sont nommées et reportées.

---

## 1. Le datum à raccorder, et pourquoi un bord ≠ un crossover `[cadre]`

Au crossover `𝒞`, la **bandage region** (`LC-A-D1` §1) porte trois métriques
conformément reliées au **même pont régulier** `g` :

$$\hat g = \hat\Omega^2 g\ \ (\text{passé, physique}),\qquad
\check g = \check\Omega^2 g\ \ (\text{futur, physique}),\qquad
\hat\Omega\,\check\Omega = -1\ \ (\text{réciprocité, Penrose}).$$

La donnée de Friedrich/FG de chaque côté est `(g₍₀₎, g₍₃₎)` (`LC-A` §2b) : `g₍₀₎` la
classe conforme (partagée), `g₍₃₎` la **marée** TT (= Weyl rescalé = `⟨T⟩`, `LC-D`).
`LC-D3` a montré, **à un bord**, que le vide de Bunch–Davies donne `⟨g₍₃₎⟩=0`, ce qui
**est** `C→0`. Mais à un bord, il n'y a rien à raccorder : l'état est posé. À `𝒞`,
`𝓘⁺(n)` *devient* le Big Bang de `n+1` ; la marée du futur `ǧ₍₃₎` n'est pas libre —
elle est **ce que le passé livre**, transformé par la carte de crossover. D'où la
question propre : `ĝ₍₃₎=0 ↦ ?`.

---

## 2. [S1] Le fond du crossover est sans marée — le point fixe existe `[établi]`

Compagnon `verif_D3_crossover_matching.py`, sceau [S1] (réutilise le pont
conformément plat de `verif_D1_facteur`). Passé exactement dS planaire
`Ω̂=−1/(Hη)` ; réciprocité `Ω̌=−1/Ω̂=Hη` ⟹ futur `a(η)=Hη`, **radiation** (`R=0`).
Calcul du Weyl `(1,3)` des deux côtés :

$$C^a{}_{bcd}(\hat g_{\text{dS}}) = 0\quad(\text{conformément plate}),\qquad
C^a{}_{bcd}(\check g_{\text{rad}}) = 0\quad(\text{FLRW radiation}).$$

Donc, sur le fond, `ĝ₍₃₎ = ǧ₍₃₎ = 0` : **le vide est littéralement le fond du
crossover**, et `0↦0` y est trivialement réalisé. C'est le pendant, côté raccordement,
du fait `Weyl FLRW≡0` de `LC-A-D1-STABILITE-WEYL` §4 : la marée vit *au-dessus* de ce
fond. `[établi]`

---

## 3. [S2] La marée est partagée — Weyl `(1,3)` conformément invariant `[établi]`

Le point structurant. Le Weyl `(1,3)` `C^a{}_{bcd}` est **conformément invariant**
(théorème standard), vérifié explicitement (sceau [S2]) sur une métrique-test à Weyl
**non nul** (`diag(−1,t²,t⁴,t⁶)`) : `C^a{}_{bcd}[g] = C^a{}_{bcd}[\Omega^2 g]` pour tous
les indices. Conséquence pour le bandage : `ĝ`, `g`, `ǧ` étant **mutuellement
conformes**, ils partagent **un seul et même** `C^a{}_{bcd}`. La marée n'est pas deux
objets indépendants de part et d'autre : `ĝ₍₃₎` et `ǧ₍₃₎` sont **deux rescalings du
datum radiatif unique du pont** `g`. Si le pont est sans marée (Weyl nul), les deux
côtés le sont ; si le passé arrive avec `Ĉ→0`, le pont est sans Weyl, donc `Č→0`. La
réciprocité (relation **scalaire**, `LC-A-D1` §3) ne touche pas ce secteur TT : elle ne
fixe que le poids du rescaling, jamais la présence ou non d'une marée. `[établi]`

---

## 4. [S3]+[S4] La carte `ĝ₍₃₎↦ǧ₍₃₎` est homogène, et nulle prescription ne peut la sourcer `[établi, linéaire]`

**[S3] Réciprocité homogène.** Perturbons `Ω̂ → Ω̂(1+εφ)` ; la réciprocité exacte donne

$$\check\Omega(\varepsilon) = -\frac{1}{\hat\Omega(1+\varepsilon\varphi)}
= \check\Omega_{\text{fond}}\,(1 - \varepsilon\varphi + \varepsilon^2\varphi^2 - \dots),$$

soit `δlnΩ̌ = −δlnΩ̂` : **purement multiplicatif, aucun terme additif** (sceau : le
coefficient `ε⁰` est le fond intact, le `ε¹` vaut `−φ·Ω̌_fond`). Une perturbation passée
nulle (`φ=0`) donne une perturbation future nulle. La carte linéarisée de la marée est
donc `ǧ₍₃₎ = M\,ĝ₍₃₎` **sans constante** : `0 ↦ 0`.

**[S4] Pas de source possible.** Pour casser l'homogénéité, une prescription devrait
*injecter* une marée TT à partir d'un passé sans marée — donc construire un tenseur TT
à partir du **fond isotrope**. Or (sceau [S4]) la projection transverse-sans-trace d'un
tenseur isotrope `S_{ij}=c\,δ_{ij}` est **identiquement nulle** : un fond FLRW (Ricci,
Schouten `∝δ_{ij}`) n'admet **aucune** structure TT locale. Donc `g₍₂₎` (Schouten,
local) n'a pas de part TT, et le mode libre `g₍₃₎` étant nul par hypothèse, `ǧ₍₃₎^{TT}=0`.
Même une prescription **non locale** d'analyticité (Nurowski/FG) n'a rien à forcer :
sans datum libre entrant, l'extension analytique autour d'un fond conformément plat est
le fond. `[établi, linéaire]`

**Lien à l'atlas (le `c₁`).** Le facteur `M` de la carte est fixé par les échelles de
fond `(m̂,λ̂,k)` via le constant `c₁` auquel l'atlas (`LC-A-D1` §4-bis) réduit toute la
liberté D1. (a1) dit : **quel que soit `c₁`**, le point fixe `g₍₃₎=0` est préservé ;
`c₁` ne rescale que la carte des tides **non nulles**. C'est précisément cette carte des
tides non nulles, et la stabilité du point fixe sous itération inter-éons, qui sont
l'objet de (a3).

<svg width="100%" viewBox="0 0 680 350" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>(a1) Le vide ĝ₃=0 est un point fixe forcé du raccordement, au niveau linéaire</title>
  <desc>Au crossover C, le bandage relie le passé (gauche, dS Lambda-dominé) et le futur (droite, radiation) au même pont régulier g par les facteurs Omega chapeau et Omega caron avec la réciprocité Omega chapeau fois Omega caron égale moins un. La marée g3 est portée par le pont partagé car le Weyl (1,3) est conformément invariant ; ainsi g3 chapeau et g3 caron rescalent un même datum. La carte induite par la réciprocité est multiplicative donc homogène : zéro va vers zéro. De plus un fond isotrope FLRW n'admet aucune structure TT locale, donc aucune prescription (Tod, Newman, Nurowski) ne peut envoyer g3 chapeau nul vers g3 caron non nul. Le vide est un point fixe forcé. En bas, trois réserves : ordre deux (back-réaction k3) renvoyée à a2, stabilité et runaway renvoyés à a3, fond anisotrope Bianchi A renvoyé à l'atlas inhomogène.</desc>
  <line x1="340" y1="40" x2="340" y2="240" stroke="#534AB7" stroke-width="3"/>
  <text x="340" y="32" text-anchor="middle" font-size="12.5" font-weight="500" fill="#3C3489">crossover 𝒞 (pont partagé g)</text>
  <rect x="40" y="58" width="270" height="120" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="175" y="82" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">passé  ĝ = Ω̂²g  (dS, Λ)</text>
  <text x="175" y="108" text-anchor="middle" font-size="12" fill="#3d3d3a">fond : Ĉ = 0  (sans marée)</text>
  <text x="175" y="132" text-anchor="middle" font-size="12.5" fill="#0F6E56">datum de vide :  ĝ₍₃₎ = 0</text>
  <text x="175" y="156" text-anchor="middle" font-size="11" fill="#73726c">(= C→0 de LC-D3 / Bunch–Davies)</text>
  <rect x="370" y="58" width="270" height="120" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="505" y="82" text-anchor="middle" font-size="12.5" font-weight="500" fill="#0F6E56">futur  ǧ = Ω̌²g  (radiation)</text>
  <text x="505" y="108" text-anchor="middle" font-size="12" fill="#3d3d3a">fond : Č = 0  (sans marée)</text>
  <text x="505" y="132" text-anchor="middle" font-size="12.5" fill="#0F6E56">résultat forcé :  ǧ₍₃₎ = 0</text>
  <text x="505" y="156" text-anchor="middle" font-size="11" fill="#73726c">le vide se raccorde au vide</text>
  <line x1="310" y1="118" x2="370" y2="118" stroke="#1D9E75" stroke-width="2.2"/>
  <text x="340" y="110" text-anchor="middle" font-size="10" fill="#3C3489">Ω̂Ω̌=−1</text>
  <text x="340" y="200" text-anchor="middle" font-size="11.5" fill="#0F6E56">carte homogène (×), 0↦0 — Weyl (1,3) invariant ⟹ marée partagée</text>
  <text x="340" y="220" text-anchor="middle" font-size="11.5" fill="#0F6E56">pas de source TT sur fond isotrope ⟹ Tod=New=Nurowski : 0↦0</text>
  <rect x="40" y="262" width="600" height="74" rx="9" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="340" y="284" text-anchor="middle" font-size="12" font-weight="500" fill="#993C1D">réserves (non couvert — le non-linéaire) :</text>
  <text x="340" y="304" text-anchor="middle" font-size="11" fill="#3d3d3a">O(h²) back-réaction k³ → (a2)   ·   stabilité / runaway (m,λ) → (a3)</text>
  <text x="340" y="322" text-anchor="middle" font-size="11" fill="#3d3d3a">fond anisotrope (Bianchi A : cisaillement = structure TT) → atlas inhomogène</text>
</svg>

*Fig. — (a1). Le fond du crossover est sans marée des deux côtés ([S1], vert), la marée
est partagée par le pont (Weyl invariant, [S2]), et la carte de réciprocité est homogène
([S3]) sans source possible sur fond isotrope ([S4]) : le vide `ĝ₍₃₎=0` est un **point
fixe forcé**, identique pour les trois prescriptions. Les réserves (orange) sont
exactement le contenu non linéaire, renvoyé à (a2)/(a3) et à l'atlas inhomogène.*

---

## 5. Conséquences pour le programme

- **(a1) clôt l'objection « bord ≠ crossover » au niveau linéaire.** L'énoncé de `LC-D3`
  (« né dans le vide de BD ») n'est pas seulement un choix d'état à un bord : c'est un
  **point fixe auto-cohérent du raccordement**, robuste au choix de prescription. La
  convergence D1+D3+[D] passe du « bord » au « crossover » — *en linéaire*.
- **Le verrou se déplace vers le facteur, pas le point fixe.** Toute la dépendance en
  prescription (`c₁`, et donc la pathologie de runaway de l'atlas) vit dans la carte des
  tides **non nulles**. (a1) isole donc proprement (a3) : *le point fixe `g₍₃₎=0`
  est-il un attracteur sous l'itération inter-éons, ou le runaway `(m,λ)` l'amplifie-t-il ?*
- **(a1) localise précisément où l'homogénéité peut tomber.** Trois portes, toutes
  nommées : `O(h²)` (les fluctuations `k³` sourcent-elles `⟨g₍₃₎⟩` au second ordre ? →
  (a2)) ; anisotropie (Bianchi A donne une structure TT → carte inhomogène possible) ;
  non-unitarité dS/CFT (source non-locale par l'état de raccordement). Le front (a) est
  ainsi réduit à ces trois inconnues explicites.

---

## 6. Format de chaînon

- **Hypothèse testée.** Le datum de vide `ĝ₍₃₎=0` (= `C→0`) se raccorde en `ǧ₍₃₎=0` sous
  la réciprocité `Ω̂Ω̌=−1` + une prescription de l'atlas (Tod/Newman/Nurowski), au niveau
  linéaire autour du fond FLRW.
- **Outil.** Bandage region + réciprocité (`LC-A-D1`) ; donnée `(g₍₀₎,g₍₃₎)` de Friedrich
  (`LC-A`) ; invariance conforme du Weyl `(1,3)` ; perturbation de la réciprocité ;
  projecteur TT sur fond isotrope. Sceau `verif_D3_crossover_matching.py` (sympy).
- **Critère de réfutation.** *Issue « source »* : si une prescription cohérente envoyait
  `ĝ₍₃₎=0 ↦ ǧ₍₃₎≠0` (création de marée TT à partir d'un passé sans marée), le vide ne
  serait pas un point fixe et « né dans le vide » tomberait. **Non observé en linéaire/FLRW**
  (S2–S4 l'interdisent). *Réfutation forte (reportée)* : exhiber une telle source à
  `O(h²)` (a2), ou en fond anisotrope (Bianchi A), ou via un état de raccordement non
  unitaire.
- **Verdict.** Point fixe `ĝ₍₃₎=0↦ǧ₍₃₎=0` **existant, forcé, indépendant de la
  prescription** `[établi, linéaire, FLRW]`. Stabilité/unicité du point fixe et survie au
  non-linéaire `[décision ouverte / à inventer]`.

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D3-WEYL-BUNCHDAVIES` (résultat à un bord, étendu ici au crossover ;
`E=(d/2H)g₍₃₎`, `⟨g₍₃₎⟩_{BD}=0`) ; `LC-A-SURVIE-CONFORME` (crossover spacelike↔spacelike,
donnée `(g₍₀₎,g₍₃₎)`) ; `LC-A-D1-FACTEUR-CONFORME` (réciprocité ; sous-détermination ;
atlas §4-bis et le constant `c₁` ; runaway → (a3)) ; `LC-A-D1-STABILITE-WEYL` (Weyl
FLRW≡0 — pourquoi le fond est sans marée ; fond⊥marée) ; `LC-D-HOLOGRAPHIE-G3`
(`g₍₃₎=⟨T⟩` ; état de raccordement non construit) ; `LC-WORK-REPRISE-RACCORD` §10 (front (a)).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Carte de crossover `ĝ₍₃₎↦ǧ₍₃₎`* : application de la marée passée vers la marée future,
  induite par `Ω̂Ω̌=−1` + prescription ; linéaire homogène autour du fond FLRW.
- *Point fixe de vide (a1)* : `ĝ₍₃₎=0↦ǧ₍₃₎=0`, forcé par invariance conforme du Weyl +
  isotropie du fond ; indépendant de Tod/Newman/Nurowski.
- *Marée partagée par le pont* : `ĝ₍₃₎,ǧ₍₃₎` = deux rescalings d'un même `C^a{}_{bcd}`
  (conformément invariant) du pont régulier `g`.
- *Lemme « pas de source TT »* : projection TT d'un tenseur isotrope `∝δ_{ij}` nulle ⟹
  aucune marée locale constructible sur fond FLRW.

**Références (`LC-04`, en KB v1.8).** Penrose, *Cycles of Time* (2010) `[confirmé]` —
réciprocité `Ω̂Ω̌=−1` ; Friedrich, CMP **107**, 587 (1986) `[confirmé]` — donnée
`(g₍₀₎,g₍₃₎)` à `𝓘⁺` spacelike ; de Haro–Skenderis–Solodukhin, CMP **217**, 595 (2001)
`[confirmé]` — FG ; Markwell–Stevens, GRG **55**, 93 (2023) `[confirmé en KB :
2212.06914v2.pdf]` — atlas des prescriptions (`c₁`, runaway). (Invariance conforme du
Weyl `(1,3)` : standard, vérifiée au sceau §3.)

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
