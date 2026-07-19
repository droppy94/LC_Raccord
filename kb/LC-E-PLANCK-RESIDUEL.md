---
id: LC-E-PLANCK-RESIDUEL
titre: "Module E — l'échelle de Planck du nouvel éon émerge-t-elle du résidu de Sitter du vieil éon ?"
codename: LC-RACCORD
tags: [module-E, retour-echelle, planck, de-sitter, holographie, entropie, ccc, facteur-conforme, exploratoire]
type: note exploratoire (première pièce du module E ; hypothèse spéculative documentée)
statut: cadre documenté / hypothèse à inventer / fermeture hors de portée
version: 0.3
langue: fr
date: 2026-06-07
maj: "2026-06-10 — v0.3 : §6 — RENVOI ADDITIF (propagation de LC-E-N-CROSSCHECK v0.1, sceau verif_E_N_crosscheck.py EXIT 0 19/19). La question « qu'est-ce qui fixe N ? » posée ici a été attaquée sur l'axe β (cross-check empirique) : verdict CONSOLIDATION — toutes les prises sur N (A_T=16/N, C_T/N=1/(32π²), cutoff √(N/π), marée P_T∝H²) sont f(N) par scellement, 1 seul intrant Λ à ℓ_P fixe ⟹ « fixer N » ≡ « fixer Λ » (la circularité de §3/§6 est CONFIRMÉE par comptage explicite, non brisée). Acquis falsifiable NÉGATIF : A_T=16/S_dS≈5×10⁻¹²² (échelle dS asymptotique) ~10¹¹¹ sous le spectre observé ⟹ le deux-point de vide inter-éon n'est pas le CMB. Note datée ajoutée en fin de §6. Aucune touche à l'algèbre ni au verdict (hors de portée réaffirmé). SANS SURCLASSEMENT ; compte {A4 ; A2★ ; N} inchangé. | 2026-06-09 — v0.2 : §3 — propagation de la passerelle D1⟷E (LC-WORK-D1-E-AMPLITUDE v0.1, paper-first). Note ajoutée après la réserve « qu'est-ce qui fixe N ? » : le compte N ne porte pas que l'échelle ℓ_P — via la passerelle D1⟷E, l'amplitude primordiale A_T~(H/M_P)² (résidu complet de D1 au niveau gaussien) s'y rattache aussi par A_T~1/C_T~1/N (charge centrale céleste C_T~N=S_dS, scaling). « Fixer N » fixerait donc à la fois ℓ_P ET A_T. Circularité NON aggravée (seulement plus chargée : un compte N, deux résidus). Aucune touche à l'algèbre ni au verdict ; reste formalisable (scaling) → à inventer (coefficient). | v0.1 : note exploratoire — ℓ_P=√(3π/ΛN) (pont holographique, circulaire) ; compte N holographique (non sériel/φ-tick) ; sceau verif_E_planck.py."
statut_id: provisoire — note de sécurité, à enregistrer si validée
fichier_compagnon: verif_E_planck.py
renvois: [LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-05-PHI-ENTROPIE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[E] retour de l'échelle — objet central de la note"
  - "[D] holographie — le compte N qui fixerait l'échelle y vit"
  - "[D1] facteur conforme — l'échelle = le champ Ω non fixé"
  - "sous-programme φ — le tick comme candidat (écarté) du compte N"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-E·Planck — L'échelle de Planck comme résidu de l'éon précédent ?

> **Statut d'emblée `[à ne pas sur-lire]`.** Ceci est une **note exploratoire**, posée
> *par sécurité* pour consigner une hypothèse de travail et ses garde-fous — **pas** un
> chaînon de résultat. Le cœur de l'hypothèse est `à inventer` ; sa fermeture est
> `hors de portée` (elle demande une CCC quantique). Ce qui est `établi` ici, c'est un
> **obstacle** et un **test négatif** précis, qui balisent où l'idée peut — ou non —
> vivre.

> **Question.** L'échelle de Planck `ℓ_P` du nouvel éon pourrait-elle **émerger des
> valeurs résiduelles** du vieil éon parvenu en de Sitter (fin de croissance, gel
> causal), fixant ainsi le « cadre » du neuf ?
>
> **Réponses (calculées).** (A) **Non, pas à partir des seuls résidus classiques.**
> `{c, Λ}` ne fixent qu'**une** échelle (`ℓ_dS = √(3/Λ)`) ; le rapport `ℓ_P/ℓ_dS ~
> 10⁻⁶¹` est un **nombre sans dimension** qu'aucune quantité classique du vieil éon ne
> détermine. `[établi]` (B) **Oui, conditionnellement**, *si* le vieil éon transmet en
> plus un **compte sans dimension `N`** : alors `ℓ_P = √(3π/ΛN)` (formule de l'entropie
> de de Sitter retournée), arithmétiquement juste pour `N ~ 10¹²²`. `[formalisable,
> mais circulaire]` (C) **Ce compte `N` n'est PAS sériel.** Le « tick » de devenir
> (colonne φ) donne un compte *logarithmique* (~10²), pas `10¹²² `; `N` est un compte
> **holographique** (aire d'horizon), qui vit dans le module `[D]` — et il **présuppose
> `ℓ_P`** (circularité non brisée). `[établi]`

---

## 0. Rôle et garde-fou

Première pièce du module `[E]` (retour de l'échelle). Elle naît d'une intuition juste —
*l'échelle réapparaît juste après le crossover, dans le nouvel éon, quand la masse
revient* (résolution des tensions T1/T2 de la discussion D1) — et d'une question
féconde : *quel résidu du vieil éon gelé fixe cette échelle ?* On documente
l'hypothèse, on pose l'obstacle exact, on teste le candidat le plus naturel (le tick),
et on dit honnêtement ce qui reste ouvert. **Discipline** : aucun pont conjecturé n'est
promu ; les seuls verdicts `établi` sont l'obstacle dimensionnel et le test négatif du
compte sériel.

*Précision physique `[établi]`.* « de Sitter, fin d'expansion, gelé » : de Sitter n'est
pas une *fin* d'expansion mais une **accélération éternelle** ; « gelé » désigne le
**gel causal** (les structures comobiles sortent de l'horizon — les « îles » de
`LC-05`), pas un arrêt. Ce point est décisif pour (C) : l'éternité de de Sitter fait
**diverger** tout compte temporel, ne laissant fini que le compte spatial (horizon).

---

## 1. L'hypothèse, située

Le crossover efface l'échelle (invariance conforme, masse nulle). L'échelle doit donc
**réapparaître** dans le nouvel éon — c'est la définition du module `[E]`. Le champ qui
la porte est le **facteur conforme `Ω`** (le « phantom field »), c'est-à-dire le degré
de liberté **non fixé de D1**. L'hypothèse : ce qui pose `Ω` (donc l'échelle, donc
peut-être `ℓ_P`) serait un **résidu du vieil éon** parvenu en de Sitter. Idée séduisante
car elle relierait trois fils du projet — `[E]` (échelle), `[D1]` (facteur conforme),
`[D]` (holographie) — et la colonne φ (le tick).

---

## 2. L'obstacle dimensionnel `[établi]`

Que possède un éon gelé en de Sitter comme invariants **purement résiduels** (avant tout
retour de masse) ? Deux, et deux seulement :

- **`c`** — la structure nulle/conforme, qui traverse `𝒞` (l'« invariant lumineux ») ;
- **`Λ`** — la constante cosmologique `[L⁻²]`, qui pose `ℓ_dS = √(3/Λ)`.

Or `ℓ_P = √(ℏG/c³)` exige `ℏ` (action) et `G` (couplage gravitationnel). Le point exact
(compagnon [A], `verif_E_planck.py`) :

$$\{c,\Lambda\}\ \Rightarrow\ \text{une seule longueur }\ \ell_{\rm dS}=\sqrt{3/\Lambda}\,;\qquad
\frac{\ell_P}{\ell_{\rm dS}}\approx 10^{-61}\ \text{est }\textbf{sans dimension} \Rightarrow \textbf{non fixé}.$$

`ℓ_P` est bien une longueur — mais **une seconde longueur indépendante** de `ℓ_dS`, et
leur rapport est un nombre pur que `c` et `Λ` ne peuvent pas produire. **Le vieil éon
classique ne peut donc pas, à lui seul, générer Planck** : il lui manque un nombre sans
dimension. Circularité à éviter : `T_dS` et `S_dS` (Gibbons–Hawking) *contiennent déjà*
`ℏ` et `G` ; seul `Λ` est vraiment « pré-Planck ».

---

## 3. Le pont holographique `[formalisable, circulaire]`

Si — et seulement si — le vieil éon transmet un **nombre sans dimension `N`**
(un *compte* de degrés de liberté), `ℓ_P` est déterminé. C'est la formule de l'entropie
de de Sitter, lue à l'envers (compagnon [B]) :

$$S_{\rm dS}=\frac{3\pi}{\Lambda\,\ell_P^{2}}\quad\Longrightarrow\quad
\boxed{\ \ell_P=\sqrt{\dfrac{3\pi}{\Lambda\,N}}\ },\qquad N\equiv S_{\rm dS}.$$

Arithmétique juste : `Λ ~ 1{,}1\times10^{-52}\,{\rm m^{-2}}`, `N ~ 3{,}3\times10^{122}`
⟹ `ℓ_P ~ 1{,}6\times10^{-35}\,{\rm m}` (recalculé, exact). Le pont **existe**, à
condition d'y faire passer `N ~ 10¹²²`.

> **Réserve `[à ne pas perdre]`.** Cette relation **définit** `N` autant qu'elle
> « dérive » `ℓ_P`. Tant que `N` n'est pas fixé par un principe *indépendant*, c'est une
> ré-écriture de l'entropie de de Sitter, non une dérivation. Tout le contenu est
> reporté sur : **qu'est-ce qui fixe `N` ?**

**Rattachement `[passerelle D1⟷E, 2026-06-09]`.** `N` ne porte pas que l'échelle : via la
passerelle `D1⟷E` (`LC-WORK-D1-E-AMPLITUDE`), l'**amplitude primordiale** `A_T~(H/M_P)²` —
le résidu complet de D1 au niveau gaussien — s'y rattache aussi, par `A_T ~ 1/C_T ~ 1/N`
(charge centrale céleste `C_T~N=S_dS`, scaling). Donc « qu'est-ce qui fixe `N` ? » fixerait
**à la fois** `ℓ_P` (cette note) **et** `A_T` (le résidu de D1) : la circularité n'est pas
aggravée, seulement **plus chargée** — un seul compte `N` porte deux résidus.
`[formalisable (scaling) → à inventer (coefficient) ; circularité non brisée]`

---

## 4. Tentative : le compte `N` est-il sériel (φ-tick) ou holographique ? `[établi]`

C'était l'espoir le plus concret (et le plus « nôtre ») : `N` = nombre de **ticks** de
devenir du vieil éon, calculable depuis le gel en de Sitter (`LC-05`, `a_n = φⁿ`).
**Test direct** (compagnon [C]) :

| candidat pour `N` | nature | valeur | verdict |
|---|---|---|---|
| ticks φ d'expansion (`a_n=φⁿ` pour dilater de `ℓ_dS/ℓ_P`) | sériel / temporel | `n = ln(ℓ_dS/ℓ_P)/ln φ ≈ 292` | **~10² (log)** — pas `N` |
| ticks de Planck sur un temps de Hubble | sériel / temporel | `N_time = ℓ_dS/ℓ_P ≈ 10⁶¹` | `= √(N/π)` |
| cellules de Planck sur l'horizon (aire/`ℓ_P²`) | **holographique / spatial** | `S_dS ≈ 3,3×10¹²²` | **= `N`** |

Avec la relation exacte `S_dS = \pi\,N_{\rm time}^2` (vérifiée : rapport `= 1{,}000`).

**Trois conclusions.**

1. **Le φ-tick ne donne pas `N`.** Un compte d'**expansion** (`a_n=φⁿ`) est
   *logarithmique* (~10²) : il compte des e-folds, pas des cellules d'horizon. Le lien
   espéré « `N` = nombre de ticks » **échoue par l'échelle** (10² vs 10¹²²).
2. **`N` est holographique, pas sériel.** Le seul compte *fini* est l'aire de l'horizon
   en cellules de Planck — un objet du module `[D]`. Et c'est cohérent avec l'éternité
   de de Sitter : tout compte **temporel** diverge ; seul le compte **spatial** est
   fini. Le tick (temporel) est donc la **mauvaise observable** pour `N`.
3. **La circularité n'est pas brisée.** `N = S_dS = (ℓ_dS/ℓ_P)²` présuppose `ℓ_P`. Le
   gel φ ne fournit aucun nombre indépendant qui la lèverait.

*Motif suggestif (non prouvé).* `N_{\rm aire} = \pi\,N_{\rm time}^2` : l'aire ≈ (compte
temporel)². C'est la signature d'une relation holographique (bord = volume²), proche de
motifs discutés en gravité entropique — mais ici **constatée, non dérivée**. `[à inventer]`

<svg width="100%" viewBox="0 0 660 250" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Deux échelles, un nombre manquant N</title>
  <desc>Le vieil éon gelé fournit la constante cosmologique Lambda, qui fixe une seule longueur, le rayon de de Sitter ell_dS d'ordre 10^26 mètres. La longueur de Planck ell_P d'ordre 10^-35 mètres est une seconde longueur indépendante ; le rapport entre les deux, d'ordre 10^-61, est un nombre sans dimension non fixé par c et Lambda. Le pont vers ell_P passe par un compte N d'ordre 10^122, qui est l'entropie de l'horizon de de Sitter, donc un compte holographique d'aire, et non un compte sériel de ticks (qui ne donne que d'ordre 10^2).</desc>
  <rect x="30" y="46" width="200" height="150" rx="10" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="130" y="72" text-anchor="middle" font-size="13" font-weight="500" fill="#0F6E56">vieil éon gelé</text>
  <text x="130" y="98" text-anchor="middle" font-size="12" fill="#3d3d3a">résidu : c, Λ</text>
  <text x="130" y="124" text-anchor="middle" font-size="12" fill="#0F6E56">ℓ_dS=√(3/Λ)</text>
  <text x="130" y="142" text-anchor="middle" font-size="11.5" fill="#3d3d3a">~10²⁶ m (1 échelle)</text>
  <text x="130" y="172" text-anchor="middle" font-size="11.5" fill="#A32D2D">ℏ, G absents</text>
  <rect x="430" y="46" width="200" height="150" rx="10" fill="#FAECE7" stroke="#D85A30" stroke-width="0.7"/>
  <text x="530" y="72" text-anchor="middle" font-size="13" font-weight="500" fill="#993C1D">nouvel éon</text>
  <text x="530" y="98" text-anchor="middle" font-size="12" fill="#3d3d3a">cadre : ℓ_P</text>
  <text x="530" y="124" text-anchor="middle" font-size="12" fill="#993C1D">ℓ_P~10⁻³⁵ m</text>
  <text x="530" y="142" text-anchor="middle" font-size="11.5" fill="#3d3d3a">2ᵉ échelle indép.</text>
  <text x="530" y="172" text-anchor="middle" font-size="11.5" fill="#3d3d3a">ℓ_P/ℓ_dS~10⁻⁶¹</text>
  <line x1="230" y1="110" x2="430" y2="110" stroke="#534AB7" stroke-width="2" marker-end="url(#a)"/>
  <defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#534AB7" stroke-width="1.5"/></marker></defs>
  <text x="330" y="100" text-anchor="middle" font-size="12" fill="#3C3489">ℓ_P=√(3π/ΛN)</text>
  <text x="330" y="132" text-anchor="middle" font-size="11.5" fill="#993C1D">N~10¹²² = entropie d'horizon</text>
  <text x="330" y="150" text-anchor="middle" font-size="11" fill="#0F6E56">holographique [D]</text>
  <text x="330" y="166" text-anchor="middle" font-size="11" fill="#A32D2D">≠ sériel (φ-tick ~10²)</text>
  <text x="330" y="222" text-anchor="middle" font-size="11" fill="#A32D2D">N présuppose ℓ_P : circularité non brisée — il faut un principe pour N</text>
</svg>

---

## 5. Les réserves de structure `[à ne pas perdre]`

- **Définitionnel tant que `N` n'est pas fixé** (§3) — sinon numérologie.
- **Passe par D1 non résolu.** « Le `Λ` résiduel » n'est pas un donné propre : dans
  l'atlas (`LC-A-D1` §4-bis), `λ` se propage de façon *dépendante de la prescription*
  (Tod constant, classe Penrose en runaway, Nurowski libre). Utiliser « `Λ` ancien »
  présuppose qu'on a tranché D1.
- **Tension avec la remise à zéro de l'entropie (Penrose).** La CCC réinitialise
  l'entropie gravitationnelle au crossover (hypothèse de Weyl, faible désordre au
  nouveau Big Bang). Faire traverser `N ~ 10¹²²` doit se concilier avec ce reset —
  l'entropie d'**horizon** de de Sitter (maximum, mort thermique) et l'entropie de
  **Weyl** (basse au Big Bang) sont distinctes, et la frontière n'est pas résolue.

---

## 6. Verdict et redirection

- **L'idée vise juste mais ne ferme pas.** Le bon lieu de l'échelle est `[E]` (retour),
  porté par `Ω` (=D1). L'obstacle dimensionnel est réel : il faut un nombre `N`.
- **Le candidat sériel (φ-tick) est écarté `[établi]`** : `N` est holographique (aire
  d'horizon, `[D]`), pas un compte de ticks (logarithmique). De Sitter éternel impose
  que le compte fini soit spatial.
- **La circularité subsiste** : `N` présuppose `ℓ_P`. Sans principe indépendant fixant
  `N`, l'hypothèse reste `à inventer`.
- **Redirection.** Si l'on poursuit, le bon terrain n'est **pas** le tick mais le
  **compte holographique de l'horizon** (`[D]`), et la question dure devient : *qu'est-ce
  qui fixe `N ~ 10¹²²` ?* — c'est-à-dire le **problème de la constante cosmologique /
  de l'entropie de de Sitter**, l'une des questions ouvertes les plus profondes.
  L'apport propre du projet serait de la reformuler : `N` = nombre de cellules de
  l'horizon = la borne holographique de `[D]` ; le tick n'y entre, au mieux, que comme
  `√N` (compte temporel), via `N = π N_time²` (motif `à inventer`). `[hors de portée]`
> **[Mis à jour 2026-06-10 — axe β tranché.]** La question dure de cette note (« qu'est-ce qui fixe `N` ? ») a reçu son verdict sur l'axe **β** (cross-check empirique), scellé dans `LC-E-N-CROSSCHECK` v0.1 (sceau `verif_E_N_crosscheck.py`, 19/19). **Aucun cross-check indépendant** : `A_T=16/N`, `C_T/N=1/(32π²)`, le cutoff `√(N/π)` et la marée `P_T∝H²` sont **toutes** des fonctions de l'unique `N` *par scellement* ⟹ à `ℓ_P` fixe, **un seul intrant `Λ`** ⟹ **« fixer `N` » ≡ « fixer `Λ` »** — la circularité de §3/§6 est **confirmée par comptage explicite** (non brisée), `hors de portée` réaffirmé. Acquis falsifiable **négatif** : `A_T=16/S_dS≈5×10⁻¹²²` (échelle dS asymptotique) est `~10¹¹¹` **sous** le spectre observé ⟹ le deux-point de **vide** inter-éon **n'est pas** le CMB. `[cf. LC-E-N-CROSSCHECK]`

---

## 7. Format de chaînon

- **Hypothèse testée.** « L'échelle de Planck du nouvel éon émerge des résidus du vieil
  éon de Sitter ; le compte qui la fixe est le nombre de ticks. »
- **Outil.** Analyse dimensionnelle `{c,Λ}` ; formule d'entropie de de Sitter ;
  comparaison des comptes sériel / temporel / holographique (numérique).
- **Critère de réfutation (de l'hypothèse).** Si le compte de ticks reproduisait `N ~
  10¹²²`, l'idée aurait un moteur sériel. — **Réfuté** : le φ-tick donne ~10²
  (logarithmique) ; `N` est holographique et présuppose `ℓ_P`.
- **Verdict.** Volet sériel **écarté** ; cadre **documenté** (obstacle + pont +
  réserves) ; fermeture `hors de portée` (CCC quantique). `[note de sécurité — acquis
  négatif + balisage]`

---

## 8. Renvois, glossaire, références

**Renvois.** `LC-A-D1-FACTEUR-CONFORME` (Ω = échelle non fixée ; `Λ` propagé) ;
`LC-A-D1-STABILITE-WEYL` (autre condition de fond écartée) ; `LC-05-PHI-ENTROPIE`
(gel causal `a_n=φⁿ`, îles de de Sitter) ; module `[D]` (holographie, où vit `N`).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Hypothèse Planck-résiduel (module E)* : `ℓ_P` du nouvel éon depuis un résidu du
  vieil éon ; obstacle `{c,Λ}↛ℓ_P` ; pont `ℓ_P=√(3π/ΛN)`.
- *Compte holographique `N` (vs sériel)* : `N=S_dS~10¹²²` (aire d'horizon, [D]) ; le
  φ-tick donne un compte logarithmique, pas `N`.
- *Entropie / rayon de de Sitter* : `ℓ_dS=√(3/Λ)`, `S_dS=3π/(Λℓ_P²)=π(ℓ_dS/ℓ_P)²`.

**Références (`LC-04`).** Gibbons–Hawking (entropie de de Sitter) `[à vérifier — Phys.
Rev. D 15, 2738 (1977)]` ; Penrose, *Cycles of Time* (reset d'entropie / Weyl) ;
't Hooft / Susskind (borne holographique) `[à vérifier]`. — *Spéculatif* :
Padmanabhan (gravité entropique, comptage cosmique) `[à vérifier]`.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
