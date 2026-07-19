---
id: LC-D3-CROSSOVER-EINSTEIN3D
titre: "Front (a) — la régularité du crossover force-t-elle â_ij Einstein-3D ? (résolution du §4 de LC-D3-CROSSOVER-ANISOTROPE)"
codename: LC-RACCORD
tags: [module-D3, front-a, ccc, pivot-A3, einstein-3D, yamabe, WCH, régularité, anisotropie, isotropisation, crossover]
type: chaînon (résout le point dynamique résiduel §4 de LC-D3-CROSSOVER-ANISOTROPE ; étage verdict)
statut: verdict établi (aucune condition de régularité plus faible que A3 ne force Einstein-3D ; issue faible définitive au niveau d'UN crossover) / isotropisation dynamique inter-éons FRANCHIE à l'ordre dominant (∏κ_n→0 sous Penrose, §4) ; reste P6 (bang)
version: 0.4
langue: fr
date: 2026-06-07
maj: "2026-06-07 — v0.4 : §4 — P6 (B) TRANCHÉ (LC-D3-INTERAEON-P6 v0.2, oracle Gauss-Kuzmin). La frontière inter-éon n'est plus 'franchie' tout court : elle est franchie CONDITIONNELLEMENT à σ(0)=0/WCH. Le bang GÉNÉRIQUE (Ω_σ→1) ne contracte jamais (P(ε_out<κ·ε_in)=0), carte additive bang-set ⟹ ∏κ_n→0 non générique. 'Le bang gagne' ⟹ A3/A4 socles irréductibles RECONFIRMÉS (cohérent §3). v0.3 : §4 noté avec le POC P6 (A) (quiescent, κ fragile √Ω_σ, reste (B)). v0.2 : §4 passe à `établi (ordre dominant)` (carte contractante κ≈0.81<1, ∏κ_n→0 sous Penrose) ; reste P6. Sources : LC-D3-INTERAEON-CONVERGENCE, LC-D3-INTERAEON-KAPPA, LC-D3-INTERAEON-P6."
statut_id: provisoire — à enregistrer si validé (met à jour LC-D3-CROSSOVER-ANISOTROPE §4 ; LC-02, LC-AUDIT-VERDICT §5/§8, glossaire)
fichier_compagnon: verif_D1_einstein3d.py
prerequis_kb: [LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-D3-CROSSOVER-MATCHING, LC-AUDIT-VERDICT, LC-WORK-REPRISE-AUDIT]
renvois: [LC-D3-CROSSOVER-ANISOTROPE, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-A-D1-STABILITE-WEYL, LC-AUDIT-VERDICT, LC-WORK-REPRISE-AUDIT, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES, LC-00-INDEX]
modules_rattachement:
  - "[A] / front (a) — A3 est le pivot du raccord"
  - "[D3] hypothèse de Weyl — la marée g₃ est l'objet testé"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D3·Crossover·Einstein3D — La régularité force-t-elle l'isotropie de 𝓘 ?

> **Cible.** `LC-D3-CROSSOVER-ANISOTROPE` §4 a isolé le **point dynamique résiduel** qui
> seul pourrait restaurer l'issue forte (`A3⟸A4`) : *une condition de régularité du
> crossover force-t-elle la 3-métrique rescalée `â_ij` de 𝓘 à être un espace d'**Einstein
> 3D** ?* (En dim. 3 : Einstein ⟺ courbure constante ⟺ Ricci sans-trace nul ⟺ `σ̌=0` par
> Tod éq. 33.) Si oui → issue forte ; si non → issue faible **définitive**.
>
> **Verdict (établi — issue faible définitive au niveau d'un crossover).** **Non.** On teste
> la **hiérarchie complète** des conditions naturelles (sceau `verif_D1_einstein3d.py`) :
> (E1) **Yamabe** (courbure scalaire constante — la prescription *réelle* de Tod) est
> satisfaite **pour toute** la famille d'anisotropie `ε` ; elle fixe l'échelle, pas la
> forme. (E2) **WCH** (`C=0` au bang) est automatique **pour tout** `α₁` ; le Ricci
> sans-trace de 𝓘 (`∝ α₁`, Tod éq. 26) survit. (E3) Les **seules** conditions qui donnent
> Einstein-3D sont (a) « fluide parfait post-bang » (`σ̌=0`) = **A3** (circulaire), (b) WCH
> *forte* `C=o(τ̃²)` = postulat en plus (= A3), (c) `C≡0` partout = conformément plat = FRW
> (**vacueux** : tue toute onde gravitationnelle). **La condition Einstein-3D est
> logiquement équivalente à A3 — ou vacueuse.** Aucune régularité *plus faible* que A3 ne
> l'entraîne. **A3 est un postulat-socle irréductible.** La seule route non close vers
> l'isotropie est l'**isotropisation dynamique INTER-ÉONS** (`à inventer`, §4).

---

## 0. Rôle et garde-fou

Ce chaînon **clôt** le point laissé ouvert au §4 de `LC-D3-CROSSOVER-ANISOTROPE` — *au
niveau d'un crossover unique*. Il ne clôt **pas** la CCC : il établit que l'isotropie du
raccordement (A3) ne se gagne pas par une condition de régularité géométrique, donc qu'elle
**reste un postulat** (ou demande un mécanisme dynamique encore non construit). **Garde-fou
`[à ne pas perdre]`** : ce qui est `établi` ici est une **équivalence logique** (Einstein-3D
⟺ A3 ⟺ `σ̌=0`) et une **hiérarchie de conditions** (algèbre + structure de Tod), *pas* une
affirmation que la CCC est fausse ou vraie. Discipline d'audit (`LC-AUDIT-VERDICT` §6.4)
maintenue : `établi` de sceau = « l'algèbre est correcte ».

---

## 1. La question, formalisée `[établi]`

La marée future (`LC-A-D1-BIANCHI` §3, Tod éq. 33) est
`σ̌_ij = −4(R^{(â)}_{ij} − ⅓R^{(â)}â_{ij})`. Donc :

$$\check\sigma = 0 \iff R^{(\hat a)}_{ij} = \tfrac13 R^{(\hat a)}\hat a_{ij}
\iff \hat a_{ij}\ \text{Einstein-3D} \underset{\dim 3}{\iff} \text{courbure constante} \iff \text{isotrope}.$$

La question « `A3 ⟸ A4` (+régularité) ? » se **réduit exactement** à : *une condition de
régularité du crossover force-t-elle `â_ij` Einstein-3D ?* On teste la hiérarchie, du plus
faible (ce que Tod impose) au plus fort.

---

## 2. La hiérarchie des conditions `[établi — sceau verif_D1_einstein3d.py]`

Famille-test : 3-géométrie de 𝓘 de type Bianchi IX squashé, facteurs `(e^ε, e^{−ε}, 1)`
(volume gelé). Écart à Einstein-3D : `|S|² = 8ε²` (Ricci sans-trace, [B2]).

**[E1] Yamabe — courbure scalaire constante (la prescription RÉELLE de Tod).** `[établi]`
La 3-métrique étant **homogène**, sa courbure scalaire est un **nombre** pour tout `ε` :

$$R^{(3)}(\varepsilon) = 2\cosh 2\varepsilon - \cosh 4\varepsilon + \tfrac12 = \tfrac32 - 4\varepsilon^2 + O(\varepsilon^3),\quad R^{(3)}(0)=\tfrac32>0.$$

La prescription de Tod (« choisir `φ₁` pour que `â_ij` ait une courbure scalaire
constante », via Yamabe) est donc **satisfaite par toute la famille** : sous
`â → φ₁²â`, `R → R/φ₁²`, Yamabe **fixe l'échelle `φ₁`**, **pas la forme `ε`**. L'écart vers
Einstein-3D (`|S|²=8ε²`) reste **entièrement libre**. **Yamabe ne sélectionne pas
l'isotropie.**

**[E2] WCH — Weyl nul au bang (`C=0`, `E=O(τ̃²)`).** `[établi]`
Dans la construction de Tod, près de 𝓘 : `α = α₀ + α₁τ̃² + O(τ̃³)`, `E_ij = O(τ̃²)`,
`B_ij = O(τ̃³)`, et le Ricci sans-trace de 𝓘 vaut `R^I_{ij} − ⅓s^I â_{ij} = −(H²/a₁²)α₁`
(Tod éq. 26). Donc `E_ij(τ̃{=}0) = 0` **pour tout `α₁`** : la WCH (`C=0` *au* bang) est
satisfaite **que `â` soit isotrope ou non**. Elle **ne force pas `α₁=0`**, donc ne force pas
le Ricci sans-trace à s'annuler. **WCH ne sélectionne pas l'isotropie.**

**[E3] Les conditions qui DONNENT Einstein-3D — et pourquoi chacune échoue comme
*dérivation*.** `[établi]`

| condition | implique Einstein-3D ? | statut |
|---|---|---|
| (a) fluide parfait post-bang (`σ̌=0`) | **oui** (Tod 33 : `σ̌=0⟺`Ricci sans-trace`=0`) | **= A3** → **circulaire** (supposer le fluide parfait = supposer l'isotropie) |
| (b) WCH *forte* `C=o(τ̃²)` (`α₁=0`) | **oui** (Tod 26 : Ricci sans-trace `∝α₁`) | **postulat EN PLUS** (non requis par Tod, dont les solutions régulières ont `α₁≠0`) ; ≡ A3 |
| (c) `C≡0` *partout* (conformément plat) | **oui** (homogène conf. plat ⟹ FRW) | **vacueux** : tue toute onde gravitationnelle |

**Démonstration de (c)** (sceau) : pour Bianchi I vide, le Kasner non trivial `(2/3,2/3,−1/3)`
a `R=0` (vide) **mais** `E_xx = 2/(9t²) ≠ 0` ; le seul Kasner vide à Weyl nul est le
dégénéré `(1,0,0)` = espace-temps **plat**. Donc imposer `C≡0` partout, c'est imposer
FRW/plat : ce n'est pas un *principe de sélection*, c'est l'isotropie elle-même décrétée.

---

## 3. Verdict : Einstein-3D ⟺ A3, non dérivable d'une régularité plus faible `[établi]`

$$\boxed{\ \text{Aucune condition de régularité PLUS FAIBLE que A3 ne force } \hat a_{ij}\ \text{Einstein-3D.}\ }$$

- Yamabe (E1) et WCH (E2) — les seules régularités *réellement imposées* par CCC/Tod —
  laissent l'anisotropie de 𝓘 **libre**.
- Les conditions qui *donnent* Einstein-3D (E3) sont soit **circulaires** (= A3 déguisée),
  soit **vacueuses** (= FRW décrété).
- Donc l'énoncé « `â_ij` Einstein-3D » est **logiquement équivalent** au pivot A3 lui-même.
  Il n'est l'ombre **d'aucun** principe géométrique plus primitif.

**Conséquence.** L'issue faible de `LC-D3-CROSSOVER-ANISOTROPE` est **définitive au niveau
d'un crossover** : `A3 ⟸ A4 (+régularité)` est **faux**. **A3 est un postulat-socle
indépendant** — le coût explicite et irréductible de l'isotropie du raccordement.

<svg width="100%" viewBox="0 0 680 320" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>Hiérarchie des conditions : aucune régularité faible n'atteint Einstein-3D sauf = A3</title>
  <desc>Diagramme en couches. La couche la plus large, Yamabe (courbure scalaire constante), est satisfaite pour toute anisotropie epsilon. À l'intérieur, la couche WCH (Weyl nul au bang) est aussi satisfaite pour tout alpha-un. Aucune de ces deux régularités n'atteint la cible Einstein-3D (point central, sigma-check égale zéro, isotrope). Cette cible n'est atteinte que par trois conditions marquées : fluide parfait (circulaire, égale A3), WCH forte (postulat en plus, égale A3), et C identiquement nul partout (vacueux, FRW). La cible Einstein-3D coïncide donc avec le pivot A3.</desc>
  <rect x="30" y="28" width="620" height="262" rx="12" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.7"/>
  <text x="48" y="50" font-size="12.5" font-weight="500" fill="#0F6E56">[E1] Yamabe (R scalaire const) — satisfaite ∀ε  (prescription réelle de Tod)</text>
  <rect x="62" y="64" width="556" height="200" rx="10" fill="#EAF6E5" stroke="#5BA341" stroke-width="0.7"/>
  <text x="80" y="86" font-size="12.5" font-weight="500" fill="#3F7A2E">[E2] WCH (Weyl nul au bang) — satisfaite ∀α₁</text>
  <circle cx="340" cy="178" r="74" fill="#FAECE7" stroke="#A32D2D" stroke-width="1.1"/>
  <text x="340" y="166" text-anchor="middle" font-size="13.5" font-weight="600" fill="#A32D2D">Einstein-3D</text>
  <text x="340" y="186" text-anchor="middle" font-size="12" fill="#A32D2D">σ̌ = 0  (isotrope)</text>
  <text x="340" y="204" text-anchor="middle" font-size="12.5" font-weight="600" fill="#7A1D1D">≡ A3</text>
  <text x="148" y="250" text-anchor="middle" font-size="10.5" fill="#993C1D">(a) fluide parfait</text>
  <text x="148" y="263" text-anchor="middle" font-size="10" fill="#993C1D">= A3 (circulaire)</text>
  <text x="535" y="120" text-anchor="middle" font-size="10.5" fill="#993C1D">(b) WCH forte α₁=0</text>
  <text x="535" y="133" text-anchor="middle" font-size="10" fill="#993C1D">postulat en plus</text>
  <text x="535" y="250" text-anchor="middle" font-size="10.5" fill="#993C1D">(c) C≡0 partout</text>
  <text x="535" y="263" text-anchor="middle" font-size="10" fill="#993C1D">vacueux (FRW)</text>
  <line x1="195" y1="250" x2="280" y2="205" stroke="#A32D2D" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="495" y1="128" x2="405" y2="158" stroke="#A32D2D" stroke-width="1" stroke-dasharray="4 3"/>
  <line x1="495" y1="250" x2="405" y2="200" stroke="#A32D2D" stroke-width="1" stroke-dasharray="4 3"/>
  <text x="340" y="308" text-anchor="middle" font-size="11" fill="#3C3489">les régularités faibles (vert) n'atteignent jamais le centre ; seules (a)/(b)/(c) y mènent — et toutes ≡ A3 ou vacueuses</text>
</svg>

*Fig. — Yamabe (vert clair) et WCH (vert) sont satisfaites pour toute anisotropie : elles
n'atteignent pas la cible Einstein-3D (rouge). Celle-ci n'est touchée que par (a) fluide
parfait = A3, (b) WCH forte = A3, (c) `C≡0` = FRW vacueux. **Einstein-3D ≡ A3.**

---

## 4. L'isotropisation dynamique inter-éons — frontière FRANCHIE à l'ordre dominant `[établi (ordre dominant)]`

Le verdict du §3 vaut pour **un** crossover. Il subsistait **une seule** route non close vers
l'isotropie, de nature **dynamique et inter-éons** :

> **Question (jadis ouverte, désormais tranchée à l'ordre dominant).** *La carte d'anisotropie
> `ε_n ↦ ε_{n+1}` de 𝓘 d'éon en éon attire-t-elle vers `ε=0` ?* — c'est-à-dire : même si un
> crossover unique admet `â` anisotrope, la **suite** des éons isotropise-t-elle le raccordement ?

C'est l'**analogue anisotrope** du runaway `(m,λ)` de l'atlas FLRW (`LC-A-D1-FACTEUR-CONFORME`
§4-bis ; candidat #5) et **la vraie forme de la porte (ii)** dans le secteur anisotrope.

> **Mise à jour `[établi (ordre dominant) — sceaux verif_D3_interaeon_kappa.py + _convergence.py v2]`.**
> La porte (ii) est **franchie à l'ordre dominant**. En propageant `â` à travers l'éon futur
> via un noyau Bianchi IX + radiation + Λ (chaînons `LC-WORK-CADRAGE-INTERAEON`,
> `LC-D3-INTERAEON-KAPPA`, `LC-D3-INTERAEON-MATIERE`, `LC-D3-INTERAEON-CONVERGENCE`), la carte
> `ε_n↦ε_{n+1}` est **contractante** : `ε_{n+1}=κ ε_n`, `κ≈0.81<1` (intervalle GO-admissible
> `κ∈[0.70,0.94]`). Et **§5.1 est clos** : sous Penrose (Λ constante d'éon en éon),
> l'autocohérence de l'atlas D1 force le **point fixe `mλ=9k²/4`**, donc `κ` constant, donc
> **∏κ_n = κⁿ → 0** : isotropisation **TOTALE dynamique** (forme dynamique d'issue forte),
> **lente** (`κ→1` pour un bang radiation-dominé réaliste). L'audit froid (sceau v2) confirme
> qu'**aucune des deux branches runaway** (hors Penrose) ne laisse de résiduel dans le domaine
> GO : `mλ>2.25` (ρ_0→0, Λ→∞) sort via P6 à l'éon 24 avec `∏κ≈0.014` déjà atteint ; `mλ<2.25`
> (ρ_0→∞, Λ→0) **sature `κ≈0.795<1`** ⟹ `∏κ_n→0` aussi.
>
> **Garde-fou (discipline d'audit).** Ceci n'est **pas** une dérivation d'A3 à éon fini : c'est
> une **attraction dynamique multi-éon**, lente, à l'**ordre dominant** (noyau démarrant en ère
> radiation). `établi` = l'algèbre (κ<1 robuste, ∏κ_n→0). Ce qui reste : **P6** (intégration
> *à travers le bang* complet / Mixmaster — les bonds BKL changent-ils ou renversent-ils `κ` ?),
> seul chantier non clos du front (a). Voir `LC-WORK-REPRISE-P6` §5.
>
> **Mise à jour P6 — TRANCHÉ `[établi (ordre dominant) — LC-D3-INTERAEON-P6 v0.2]`.**
> P6 a été tranché en deux temps. **(A) radiation-era** : `σ≈0` de Tod est **quiescente**
> (réduction exacte `κ=0.8117`, pas de cascade), mais `ε_out` est dominé par `√Ω_σ` ⟹ la
> contraction présuppose `σ(0)≈0`. **(B) deep-bang générique** (oracle de Gauss-Kuzmin, `u`-map
> du billard BKL validé 0.8 %, noyau forward validé Radau≡DOP853) : le bang **générique**
> (`Ω_σ→1`) **ne contracte JAMAIS** (`P(ε_out<κ·ε_in)=0`), injecte une forme **O(1) ⊥ à
> l'héritage**, carte inter-éon **additive/bang-set** (`ε_{n+1}≈|\mathbf b_n−\mathbf w_n|`),
> **pas** une contraction `κε`. **Donc `∏κ_n→0` (porte ii, §4 ci-dessous) n'est PAS générique :
> c'est un artefact de `σ(0)=0` (Tod) / de la WCH (Penrose, A4).** **« Le bang gagne. »**
>
> **Ce que cela change pour ce chaînon.** La frontière inter-éon (§4) n'est **plus « franchie »**
> au sens inconditionnel : elle est **franchie *sous* A3/A4**, et le bang générique la **rouvre**.
> Cohérence parfaite avec le §3 : Einstein-3D ⟺ A3, A3 socle irréductible — ici **reconfirmé par
> une voie dynamique indépendante** (le bang ne dérive pas l'isotropie, il la requiert). La CCC
> n'est pas réfutée ; l'isotropisation dynamique l'est comme **mécanisme libre**. Détail complet
> et réserves (Heinzle-Uggla, GWE Meissner-Penrose) : `LC-D3-INTERAEON-P6` §4.

Sa résolution complète exigeait de **propager `â` à travers TOUT l'éon futur** jusqu'à son propre
𝓘 — **au-delà des deux premiers ordres post-bang** que donne Tod (éq. 33, valable seulement en
`O(Ť⁻¹)`). Le noyau ODE des chaînons INTERAEON réalise cette propagation à l'**ordre dominant**
(départ en ère radiation, `ρ≫³R,Λ`) ; lever ce contournement = **P6**. (Note : Wald/Starobinsky
donnent l'isotropisation *intra-éon* du cisaillement cinétique, mais pas la carte inter-éon de
l'anisotropie *gelée* de `â` — cf. `LC-D3-CROSSOVER-ANISOTROPE` §3.3.)

---

## 5. Conséquence pour le programme `[méta — établi]`

- **A3 confirmée comme socle irréductible.** Le pivot identifié par l'audit (§5) ne se
  réduit ni à A4 (porte i, `LC-D3-CROSSOVER-ANISOTROPE`) ni à une régularité géométrique
  (ce chaînon). Il reste une **hypothèse-socle indépendante**. La comptabilité de la
  conjecture (audit §8) ne se resserre pas : les socles indépendants demeurent **A1/A2
  (dS/CFT)**, **A3 (isotropie du raccordement)**, **A4 (WCH)**.
- **Repriorisation — porte (ii) franchie à l'ordre dominant.** La porte (ii) « renforcement du
  point fixe `g₃=0` » était **caduque telle quelle** (le point fixe n'existe pas hors isotropie,
  porte i). Sa **seule** forme licite — la **carte d'anisotropie inter-éon** du §4 — est
  désormais **franchie à l'ordre dominant** : la carte est contractante (`κ≈0.81<1`) et
  `∏κ_n→0` sous Penrose (isotropisation totale dynamique, lente). Il ne reste que **P6** (bang
  complet / Mixmaster) pour clore le front (a) à l'ordre dominant.
- **Résultat négatif honnête.** Comme `LC-E-PLANCK-RESIDUEL`, ce chaînon **borne** ce que la
  consolidation peut atteindre. Il transforme une « décision ouverte » (le §4 du frère) en
  un **fait** (Einstein-3D ≡ A3) + une **frontière nette** (l'isotropisation inter-éon).

---

## 6. Format de chaînon standard

- **Zone ambiguë.** « L'issue faible (porte i) laissait une porte de sortie : une régularité
  fine pourrait forcer `â` isotrope et restaurer `A3⟸A4`. »
- **Hypothèse testée.** Une condition de régularité du crossover force `â_ij` Einstein-3D.
- **Outil.** Tod éq. (26), (33) ; prescription Yamabe ; comptage WCH ; 3-Ricci de Milnor ;
  Weyl de Kasner. Sceau `verif_D1_einstein3d.py`.
- **Critère de réfutation de l'hypothèse.** Si une condition *strictement plus faible* que
  A3 forçait Einstein-3D, l'issue forte serait restaurée. — **Réfutée** : Yamabe et WCH ne
  la forcent pas ; les conditions qui la forcent sont = A3 ou vacueuses.
- **Verdict.** **Einstein-3D ⟺ A3** ; issue faible **définitive** (un crossover). A3 socle
  indépendant. Frontière suivante : isotropisation dynamique inter-éon `à inventer`.
  `[verdict établi ; suite à inventer]`

---

## 7. Renvois, glossaire, références

**Renvois.** **Résout `LC-D3-CROSSOVER-ANISOTROPE` §4** (le « point dynamique résiduel »
passe de `décision ouverte` à `établi (un crossover) + nouvelle frontière inter-éon`) ;
`LC-A-D1-BIANCHI` (mécanisme, Tod 33) ; `LC-A-D1-FACTEUR-CONFORME` §4-bis (atlas FLRW,
runaway — analogue du §4) ; `LC-A-D1-STABILITE-WEYL` (candidat #5 — la porte (ii) anisotrope
en est l'héritière) ; `LC-AUDIT-VERDICT` §5 (A3 pivot), §8 (suite) ; `LC-WORK-REPRISE-AUDIT`
§3.4, §5 ; contraste `LC-E-PLANCK-RESIDUEL`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Condition Einstein-3D de 𝓘* : `â_ij` à courbure constante (3D) ⟺ `σ̌=0` ⟺ isotropie ;
  **logiquement équivalente à A3**, non dérivable d'une régularité plus faible.
- *Yamabe (prescription de Tod)* : courbure scalaire constante de `â_ij` ; fixe l'échelle,
  pas la forme ; satisfaite pour toute anisotropie.
- *Isotropisation inter-éon (frontière)* : la carte `ε_n↦ε_{n+1}` attire-t-elle vers `ε=0` ?
  Analogue anisotrope du runaway `(m,λ)` ; forme licite de la porte (ii). **Franchie à l'ordre
  dominant** : carte contractante (`κ≈0.81<1`), `∏κ_n→0` sous Penrose ; reste `P6` (bang).

**Références (`LC-04`) — déjà introduites par les chaînons frères.**
- **K. P. Tod**, arXiv:1309.7248v2 = *GRG* **47**, 17 (2015) — éq. (26) (Ricci sans-trace de
  𝓘 `∝α₁`), éq. (33), prescription Yamabe (φ₁), `E=O(τ̃²)`.
- **K. Anguige & K. P. Tod**, *Ann. Phys.* **276** (1999) — Weyl nul ⟹ FRW (fluide parfait).
- **J. Milnor**, *Adv. Math.* **21** (1976) — 3-Ricci des métriques invariantes.
- **O. Markwell & C. Stevens**, *GRG* **55**, 93 (2023) ; arXiv:2212.06914 — éq. (6)-(7) : la
  part sans-trace `W̌_ab` du tenseur post-bang « has yet to obtain a physical
  interpretation » (= le `σ̌` de Tod, confirmation indépendante de l'objet).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
*Discipline d'audit (maintenue) : un `établi` de sceau = « l'algèbre est correcte », jamais
« la physique est établie ». Ici l'`établi` porte sur l'équivalence Einstein-3D ⟺ A3 et la
hiérarchie des conditions ; l'isotropisation inter-éon (§4) reste `à inventer`.*
