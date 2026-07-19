---
id: LC-02-OSSATURE
---
<!--
  Section à insérer dans 02_programme-de-recherche.md
  Emplacement recommandé : juste après la définition des modules, en amont du
  bloc [F], car l'objet est transverse à {[C], [D]} et sert d'ossature à [F].
-->

## Ossature fibrée — contenant géométrique de {[C], [D]}, ossature nominale de [F]

**Identifiant stable** : `LC-02-OSSATURE`

**Statut global** : `formalisable`. Charge `hors de portée` localisée (le flux RG
joint → [F]). Outils mobilisés : `établi`. Une hypothèse `à inventer`
(identification environnement ⇄ modes RG).

**Position dans la chaîne** : objet *transverse*. Contenant commun à la branche
`{[C], [D]}` ; ossature nominale de `[F]`. Présuppose l'aboutissement de
`[A]`–`[B]` (au même titre que `[C]` et `[D]`).

### O.0 Rôle et garde-fou

Le fibré de Hilbert ci-dessous est la tentative de loger dans un seul objet
géométrique la métrique d'espace-temps, la dynamique quantique, la décohérence et
la RG. Nominalement c'est l'ossature de `[F]` : la ligne de flux
`d/dlogΛ (g, H, D) = β(…)` *est* le contenu formel de la prétention d'unification.

**Garde-fou** `[à respecter]` : `[F]` est étiqueté `hors de portée`. On ne
présente donc pas ce fibré comme une preuve de `[F]`. Son apport *décidable* est
ailleurs : forcer `[C]` (fibres) et `[D]` (base) à partager base, fibres et
connexion, c'est-à-dire à être mutuellement compatibles. La ligne RG est un
horizon, pas un acquis.

### O.1 L'objet

Fibré de Hilbert `(E, π, B)` au-dessus de l'espace-temps émergent :

- **base `B`** : variété issue du graphe causal coarse-grainé ; porte `g_μν`
  (→ `[D]`, `[E]`) ;
- **fibre `H_x`** : structure quantique locale en `x` ;
- **total `E = ⊔ₓ H_x`**, projection `π : E → B`, `π(ψ_x) = x`.

Sur ce fibré, **deux structures de nature distincte** — à ne pas amalgamer
(cf. O.3) :

1. une **connexion `∇`** dont la composante temporelle est le Hamiltonien `H(x)`
   (transport horizontal, réversible) : `iℏ ∇_t ψ_x = H(x) ψ_x` ;
2. un **champ de dissipateurs `D_x`** (structure verticale, irréversible) agissant
   sur les sections de matrices densité `ρ(x) ∈ End(H_x)` :
   `dρ/dt = −(i/ℏ)[H(x), ρ] + D_x(ρ)`.

**Correspondance pièce ↔ physique ↔ module :**

| Pièce du fibré            | Contenu physique                  | Module          | Statut          |
|---------------------------|-----------------------------------|-----------------|-----------------|
| base + métrique `g_μν`    | géométrie d'espace-temps          | `[D]`, `[E]`    | `formalisable`  |
| fibres (algèbre locale)   | cohérence quantique globale       | `[C]`           | `formalisable`  |
| connexion unitaire `∇`    | propagation ondulatoire (Schröd.) | —               | `établi` (objet math) |
| champ `D_x`               | décohérence, états pointer        | `[C]`/`[D]` (frontière) | `formalisable` |
| flux sur `(g, H, D)`      | unification RG–MQ                 | `[F]`           | `hors de portée` |

**Correction de vocabulaire** `[à corriger dans les versions antérieures]` : la
fibre ne doit **pas** porter un Hilbert nu muni de Fubini–Study, mais l'**algèbre
de von Neumann locale et sa structure modulaire** (cf. `[C]`, reformulation
Tomita–Takesaki). C'est cette structure qui donne au contenu des fibres un ancrage
**indépendant de la métrique**, donc la seule échappatoire à la circularité
métrique/intrication relevée dans `LC-01-CADRE`.

### O.2 Statut de chaînon (format standard du programme)

- **Hypothèse de travail** : les structures de `[C]` (fibres/algèbres) et de `[D]`
  (base/métrique) se laissent loger dans un seul fibré muni d'une connexion
  unitaire et d'un champ de dissipateurs, de façon mutuellement cohérente.
- **Outil** : fibrés de Hilbert / familles d'algèbres de von Neumann ; connexions
  à valeurs dans les `*`-automorphismes ; semi-groupes dynamiques quantiques
  (forme GKLS).
- **Critère de réfutation** : (i) *incompatibilité de structure* — la connexion
  exigée par `[D]` (transport de la métrique émergente) est incompatible avec la
  structure modulaire exigée par `[C]` ; (ii) *échec de sélection* — aucun champ
  `D_x` à bilan détaillé modulaire ne produit les états pointer attendus.
- **Verdict de faisabilité** : la mise en fibré de `{[C], [D]}` est
  `formalisable`. Le **flux RG joint** des trois structures (ligne `[F]`) reste
  `hors de portée` : rien n'impose un `β` unique sans une action sous-jacente dont
  le coarse-graining induise *simultanément* `g`, `H` et `D`.

### O.3 Durcissement de la pièce dissipative

**Problème** : `D_x` n'est pas une « partie de la connexion ». Une connexion =
transport horizontal (anti-symétrique / unitaire) ; un Lindbladien = objet
vertical détruisant la phase. Trois voies pour le rendre géométrique sans abus,
de la plus comptable à la plus profonde.

**V1 — Fibré des générateurs GKLS** `[formalisable]`.
`D_x` = section du fibré dont la fibre est le **cône des générateurs complètement
dissipatifs** (forme GKLS) sur `End(H_x)`. Générateur total
`ℒ_x = −(i/ℏ)[H, ·] + D_x` : la part unitaire descend de `∇`, `D_x` est une donnée
distincte. Nettoie le vocabulaire (« connexion **et** champ de dissipateurs »).
*Minimum à appliquer partout, immédiatement.*

**V2 — Dilatation de Stinespring** `[formalisable]` ; interprétation physique
`[à inventer]`.
Tout semi-groupe CPTP provient d'une **unitaire sur un fibré dilaté**
`E ⊕ E_env`. Donc `D_x` = trace partielle d'une vraie connexion unitaire du fibré
dilaté. Le slogan « décohérence = partie non-unitaire d'une connexion » redevient
exact, à la précision près : *connexion unitaire d'un fibré dilaté, restreinte au
sous-fibré observable*. Hypothèse physique propre au projet `[à inventer]` :
`E_env` = degrés de liberté intégrés par la RG → raccorde décohérence et
coarse-graining (prise vers `[F]`).

**V3 — Flux de gradient / géométrie de l'information** `[formalisable]` —
*voie canonique recommandée*.
Un Lindbladien à **bilan détaillé** s'écrit comme **flux de gradient de l'entropie
relative** pour une métrique sur les matrices densité (Bures / BKM ; cadre
Carlen–Maas). Conséquence : **deux géométries distinctes**, et non « une connexion
à deux parties » —

- connexion = géométrie de *transport* (horizontale, réversible) ;
- `D_x` = *flux de gradient* pour une métrique sur l'espace des états de la fibre
  (verticale, irréversible).

Les **états pointer** deviennent les *attracteurs* du flux de gradient — plus
posés à la main.

**Couplage à `[C]`** `[formalisable]` : imposer le **bilan détaillé modulaire**
(condition KMS vis-à-vis du flux modulaire de Tomita–Takesaki du vide). Gains :
(i) ancrage algébrique **indépendant de la métrique** ; (ii) `D_x` et `[C]`
partagent un seul objet — le flux modulaire — fin de la juxtaposition ;
(iii) structure de flux de gradient obtenue automatiquement.

**Recommandation** : **V3 + bilan détaillé modulaire** comme version canonique ;
**V2** comme interprétation physique du « pourquoi » ; **V1** comme propreté de
notation immédiate.

**Statut des outils** : Stinespring, GKLS/Lindblad, Carlen–Maas, Tomita–Takesaki
sont `établi`. Leur **application** à un fibré sur espace-temps émergent est
`formalisable`. L'identification `E_env ⇄ modes RG` est `à inventer`. Rien de tout
cela ne fait de `[F]` un acquis.

### O.4 Renvois

- `LC-01-CADRE` — nature de la conjecture ; circularité métrique/intrication ;
  reformulation modulaire (« la colle quantique n'est pas l'entropie d'intrication
  mais la structure modulaire algébrique du vide »).
- `[C]` — fournit la structure des fibres (algèbres de von Neumann) et le bilan
  détaillé modulaire.
- `[D]` — fournit la base et la connexion de transport de la métrique émergente.
- `[E]` — facteur conforme `Ω` sur la base (changement d'échelle).
- `[F]` — destinataire de la ligne « flux » ; statut `hors de portée`.
- `LC-03-GLOSSAIRE` — entrées à créer : *fibré de Hilbert*, *connexion (`∇`)*,
  *générateur GKLS / Lindblad*, *dilatation de Stinespring*, *flux modulaire
  (Tomita–Takesaki)*, *bilan détaillé (KMS)*, *flux de gradient (Bures/BKM)*,
  *état pointer*.
- `LC-04-REFERENCES` — orientation, par ordre d'utilité : GKLS
  (Gorini–Kossakowski–Sudarshan ; Lindblad) ; théorème de dilatation de
  Stinespring ; Carlen–Maas (flux de gradient entropique pour semi-groupes à
  bilan détaillé) ; Tomita–Takesaki / théorie modulaire et condition KMS.
  `[à vérifier sur arXiv/INSPIRE-HEP avant citation formelle]`
