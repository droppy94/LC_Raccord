---
id: LC-D-O2-BPRIME
titre: "Pivot O₂, étape (b′) — DÉTERMINATION de la parité du poids conforme w et résolution du signe s=(−1)^w isolé en (b). Résultat : w = Δ_+ − Δ_- = d (gap dimensionnel FG : Δ_-=0 source g₀, Δ_+=d VEV g₃=⟨T⟩, KB-local de Haro/HOLOGRAPHIE-G3) ; sous la réciprocité NÉGATIVE de Penrose Ω·ω=−1, une branche Ω^Δ prend le facteur (−1)^Δ, et comme s est le signe RELATIF entre les deux branches FG, le poids GLOBAL (placement d'indices, facteur a² d'ensemble) se SIMPLIFIE ⟹ s = (−1)^{Δ_+−Δ_-} = (−1)^d. ÉTABLI (algèbre+descente, KB-local) : la PARITÉ de w est la parité de d. Cas physique CCC d=3 (IMPAIR) ⟹ s=−1 ⟹ P=[[0,−1],[1,0]]=S, P²=−𝟙=S² ⟹ la réciprocité conforme de Penrose REPRODUIT la S-map de de Haro, facteurs compris ⟹ (C-O2) en forme forte ÉTABLIE au niveau P1, GATE P1 FRANCHIE. Le penchant honnête (b)=discordance est RENVERSÉ — principiellement (le prior raisonnait sur un scalaire ; le bon objet est le signe relatif inter-branches = le gap d, impair en d=3 ; cet indice (ii) avait été nommé au cadrage). Fetch externe (b′)-1(ii) NON déclenché : KB-local a suffi (réciprocité négative déjà digérée en LC-A-D1-FACTEUR-CONFORME ; descente tensorielle non sign-blind via S-dualité de Haro 0808.2054 + loi de Weyl Maldacena). Sceau verif_O2_bprime.py EXIT 0/21, firewall 3 (m1 parité inversée, m2 descente triviale w=0, m3 inversion positive Ω·ω=+1). SANS SURCLASSEMENT (§6.4) : franchir P1 ≠ réduire A4 — P2 (cohérence jonction ⟹ état=eigenmode) reste `à inventer` ; {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; N non fixé (≡Λ) ; CCC non démontrée."
codename: LC-RACCORD
tags: [module-D, O2, bprime, b-prime, etape-bprime, P1, P2, poids-conforme, parite, s=(-1)^d, gap-dimensionnel, jonction, dirichlet-neumann, graviton-dual, de-haro, S-dualite, penrose-reciprocite, fefferman-graham, f_a-f_b, descente-tensorielle, concordance, S2=-1, eigenmode, A4, sceau, firewall, reduction, §6.4, pivot]
type: "chaînon de front (branche FALSIFIABILITÉ, pivot O₂) — étage (b′) résolution du signe, SCELLÉ (verif_O2_bprime.py). Portée S-O2-b′-2=parité seule. Subordonné à LC-AUDIT-VERDICT §6.4 et au cadrage gelé LC-WORK-CADRAGE-O2-BPRIME v0.1 (sha256 0bd33386f6bb…, cibles (b′)-G1/G2 + critère de verdict gelés avant fetch/algèbre)."
statut: "RÉFUTÉ (R-7, 2026-06-15, audit froid 2 passes indépendantes CONVERGENTES) — la dérivation (b′) est INVALIDE : le maillon (C2)/(C3) IMPORTE le facteur de signe (−1)^Δ de l'opération R (Ω↦−1/Ω, soit Δ↦−Δ, qui N'ÉCHANGE PAS les modes : d↦−d ∉ {0,d}) puis l'agrafe à la matrice du SWAP, lequel est réalisé par l'opération DISTINCTE Δ↦d−Δ (Dirichlet→Neumann/Legendre, SIGN-NEUTRE) ⟹ sous la vraie opération d'échange, P=[[0,1],[1,0]], s=+1 ∀d, AUCUNE dépendance de parité ; s=(−1)^d est un ARTEFACT d'épissure. Le −1 de S provient du CARRÉ DE HODGE (E-M duality, CT-DUAL, source unique du signe), PAS de la parité du gap FG. (C1) non distingué (Δ_-=0 masque l'arbitraire gap/Δ_+/somme) ; (C5) sur-énoncé/circulaire. CONCORDANCE RETIRÉE ; GATE P1 NON FRANCHIE. RETOUR au verdict (b) (LC-D-O2-P1, délimitation) : la réciprocité conforme fournit le SWAP mais PAS le −𝟙 (porté par Hodge/E-M) ; question relocalisée = la jonction réalise-t-elle la S COMPLÈTE (avec Hodge) ou seulement le swap conforme sign-neutre ? Sceau verif_O2_bprime.py ENCODE UN PAS ILLÉGITIME (bannière de retrait ajoutée) — NE PAS rejouer comme sceau de continuité. NE PAS PROPAGER. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ (JAMAIS propagé — l'audit-avant-propagation a confiné l'erreur) ; A4 non réduit ; D1 non clos ; N non fixé (≡Λ) ; CCC non démontrée."
statut_id: "RÉFUTÉ (audit froid 2 passes, R-7 2026-06-15) — NE PAS PROPAGER. Aucun lot transverse n'a été déposé ; les transverses restent à l'état pré-(b′) (AUDIT-VERDICT v1.40, 00_index v1.53, glossaire v1.46, références v1.25, BRANCHE v0.8) — RIEN à rétracter en aval. Le chaînon est conservé (mémoire d'erreur, discipline R-7 additive) avec son statut RÉFUTÉ ; le sceau verif_O2_bprime.py est marqué retiré. Verdict standing = celui de (b) (LC-D-O2-P1, délimitation, INCHANGÉ)."
version: 0.3
langue: fr
date: 2026-06-15
maj: "2026-06-26 — v0.3 (F-AUDIT, patch audit froid, TRAÇABILITÉ) : référence ajoutée à verif_O2_bprime_AUDIT.py = COPIE D'AUDIT (positif seul, SANS firewall) de verif_O2_bprime.py, fournie DÉLIBÉRÉMENT à l'auditeur froid pour qu'il conçoive ses propres mutations. Son absence de .md-résultat est VOULUE PAR CONSTRUCTION (PAS un orphelin de chaîne §5 ISO-19011). Résout le nit de traçabilité relevé par l'audit froid (verif_O2_bprime_AUDIT n'était cité que dans le manifeste de gel). NB : verif_O2_bprime.py reste marqué RETIRÉ [(b′) RÉFUTÉ] ; verif_O2_bprime_AUDIT n'est PAS un sceau de continuité. PUREMENT documentaire. AUCUN sceau, AUCUNE algèbre. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée. | 2026-06-15 — v0.2 (R-7, RETRAIT sur audit froid) : le chaînon (b′) est RÉFUTÉ par deux passes d'audit froid indépendantes CONVERGENTES (passes incognito, agents séparés). Diagnostic : (C2)/(C3) importent le signe (−1)^Δ de l'inversion R (Δ↦−Δ, qui n'échange PAS les modes) et l'agrafent à la matrice du swap (réalisé par l'opération distincte Δ↦d−Δ, sign-neutre) ⟹ sous la vraie opération d'échange s=+1 ∀d ; s=(−1)^d est un ARTEFACT. Le −1 de S est le carré de Hodge (E-M, CT-DUAL), pas la parité du gap. CONCORDANCE RETIRÉE, gate P1 NON franchie ; RETOUR au verdict (b). NE PAS propager ; sceau marqué retiré. {A4 ; A2★ ; N} INCHANGÉ (jamais propagé). [Le texte des §0-§6 ci-dessous reflète la revendication v0.1 ERRONÉE — conservé comme mémoire d'erreur ; lire d'ABORD la §R-7.] | 2026-06-15 — v0.1 : ouverture/scellement de l'étape (b′) du pivot O₂ — résolution de la parité de w. Exécute le cadrage gelé LC-WORK-CADRAGE-O2-BPRIME v0.1 (portée parité seule, S-O2-b′-1=KB-local d'abord, S-O2-b′-3=sceau+firewall). Sceau verif_O2_bprime.py (EXIT 0, 21 asserts, firewall 3 mutations cassantes ; sha256 2ee47bc586c8). Acquis amont NON re-dérivés : exposants FG {0,d} (HOLOGRAPHIE-G3/verif_D_g3) ; S-map scellée S²=−𝟙 vp ±i (CT-DUAL S1/S2) ; réciprocité négative Ω·ω=−1 (LC-A-D1-FACTEUR-CONFORME) ; swap g₀↔g₃ + P²=s·𝟙 + P=S⟺s=−1 (LC-D-O2-P1). RÉSULTAT [ERRONÉ, cf. R-7] : w=d ⟹ s=(−1)^d ; d=3 impair ⟹ s=−1 ⟹ P=S (concordance, gate P1 franchie) ; (C-O2) forte ÉTABLIE au niveau P1. SANS SURCLASSEMENT (§6.4) : une concordance d'algèbre qui franchit UNE des deux gates ne construit pas O₂, ne fixe aucun coefficient, ne réduit pas A4 (P2 reste) ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos."
fichier_compagnon: "verif_O2_bprime.py (SCEAU, EXIT 0, 21 assertions, firewall 3 mutations cassantes — m1 parité inversée (−1)^(d+1) / m2 descente triviale w=0 / m3 inversion positive Ω·ω=+1 ; sha256 2ee47bc586c8)"
prerequis_kb: [LC-D-O2-P1, LC-WORK-CADRAGE-O2-BPRIME, LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-P1, LC-D-CT-DUAL, LC-D-HOLOGRAPHIE-G3, LC-A-D1-FACTEUR-CONFORME, LC-A-SURVIE-CONFORME, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_O2_bprime.py, verif_O2_P1.py, verif_D_g3.py, verif_D_CT_dual.py]
renvois: [LC-D-O2-P1, LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-BPRIME, LC-D-CT-DUAL, LC-D-HOLOGRAPHIE-G3, LC-A-D1-FACTEUR-CONFORME, LC-WORK-BRANCHE-FALSIFIABILITE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [réfuté, réduction, établi, formalisable, à inventer, décision ouverte, piste / à étayer]
---

# LC-D · O₂ — (b′) : la parité du poids conforme tranche le signe `s=(−1)^d`

> **Objet de cette étape.** Le cadrage gelé (`LC-WORK-CADRAGE-O2-BPRIME` v0.1) a figé, avant tout
> fetch/algèbre, la question (b′) : **quelle est la parité de `w`** dans `s=(−1)^w` (signe résiduel
> isolé en (b)) ? (b′) la **tranche** par l'algèbre KB-local : `w = Δ_+ − Δ_- = d` (gap dimensionnel
> FG), et la **descente du signe** sous la réciprocité **négative** de Penrose donne `s=(−1)^d`. En
> `d=3` (CCC, impair), **`s=−1` ⟹ `P=S`** : la réciprocité reproduit la S-map, **gate P1 franchie**.
> **Rien ici ne construit O₂, ne fixe un coefficient, ni ne réduit A4** (P2 reste). Interne,
> KB-local, **scellé** (`verif_O2_bprime.py`).

---

## R-7 — RETRAIT (2026-06-15, audit froid 2 passes convergentes) `[LIRE EN PREMIER]`

> **Ce chaînon est RÉFUTÉ.** Les §0–§6 ci-dessous reflètent la revendication **v0.1 erronée** ; ils
> sont **conservés comme mémoire d'erreur** (discipline R-7 additive), **subordonnés à cette §R-7**.

**Diagnostic (convergent sur deux passes d'audit froid indépendantes, incognito, agents séparés).**

1. **Confusion de deux opérations (maillon (C2) + identification).** Le **swap** source↔VEV (`g₀↔g₃`)
   est réalisé par la réflexion **`Δ ↦ d−Δ`** (Dirichlet→Neumann / Legendre) : `0↦d`, `d↦0` — la
   **seule** compatible avec le spectre `{0,d}`, et elle est **SIGN-NEUTRE**. Le facteur `(−1)^Δ` de
   (C2) provient de **`Δ ↦ −Δ`** (l'inversion `Ω↦−1/Ω`, via `(−1/Ω)^Δ=(−1)^ΔΩ^{−Δ}`), qui **N'ÉCHANGE
   PAS** les modes (`d↦−d ∉ {0,d}`, sort du doublet — `R` ne peut donc être la matrice 2×2 `P`). La
   dérivation **agrafe le mécanisme de signe de `R` à la structure de swap de la Legendre** : pas
   caché illégitime.
2. **(C4) artefact.** Sous la vraie opération d'échange, `P=[[0,1],[1,0]]`, **`s=+1 ∀d`**, aucune
   dépendance de parité. `s=(−1)^d` n'existe que par l'injection du `(−1)^Δ` parasite. La
   « non-généricité » présentée comme vertu était le **symptôme** de l'erreur.
3. **Origine réelle du `−1`.** `S²=−𝟙` vient du **carré de Hodge** (dualité électrique-magnétique :
   `S(E)=B`, `S(B)=−E`), déjà scellé en `CT-DUAL` comme **source unique du signe** — **pas** de la
   parité du gap FG.
4. **(C3) non dérivé.** L'assignation asymétrique (`+1` sur une patte, `(−1)^d` sur l'autre) est un
   **choix**, pas un théorème ; la lecture symétrique donne `s=+1`.
5. **(C1) non distingué.** `Δ_-=0` fait coïncider gap / `Δ_+` / somme ; la robustesse n'était pas
   testée, seule la valeur.
6. **(C5) sur-énoncé / circulaire** : « reproduit `S`, facteurs compris, par algèbre seule » est
   exactement ce que l'algèbre ne montre pas.

**Conséquence.** **Concordance RETIRÉE ; gate P1 NON franchie.** On **revient au verdict (b)**
(`LC-D-O2-P1`, `délimitation`, INCHANGÉ) : la réciprocité conforme fournit le **swap** mais **pas**
le `−𝟙`. **Question relocalisée** (honnête, non résolue) : la jonction Dirichlet→Neumann réalise-t-elle
la **S complète (avec le Hodge)** ou seulement le **swap conforme sign-neutre** ? — c'est le résidu de
(b), pas un acquis.

**Statut KB.** **NON propagé** (l'audit-avant-propagation a confiné l'erreur) ⟹ rien à rétracter en
aval ; transverses inchangés. Sceau `verif_O2_bprime.py` **marqué retiré** (bannière) — **retiré de la
liste des sceaux de continuité**. **`{A4 ; A2★ ; N}` INCHANGÉ** sur toute la séquence.

---

## 0. Rôle et garde-fou `[§6.4 + R-7]` — [v0.1 ERRONÉE, cf. §R-7]

- **Étage.** (b′) **résout** une décision ouverte (le signe `s`) par un **fait** : la parité de `w`,
  pincée par le **gap dimensionnel FG** et la **descente** du facteur conforme négatif. Ce qui est
  `établi` est cette parité (donc `s`), **jamais** la construction d'O₂ ni la réduction d'A4.
- **Non-surclassement (§6.4).** **Franchir P1 ≠ réduire A4.** `s=−1` (en `d=3`) franchit **une** des
  deux gates (`LC-D-O2-JONCTION §5`) ; il reste **P2** (cohérence de jonction ⟹ état = eigenmode,
  `à inventer`, le lien le plus risqué). Le compte **{A4 ; A2★ ; N}** reste **INCHANGÉ** ; N ≡ Λ
  `hors de portée`. **Une `réduction` ici porte sur la décision ouverte P1, PAS sur le périmètre
  irréductible.**
- **Anti-fit.** La question (b′), les cibles (b′)-G1/G2 et le critère de verdict (`w` impair ⟹ `s=−1`)
  étaient figés au cadrage **avant** l'algèbre. La parité est **dérivée** (gap = `d`), pas choisie.
  Le penchant honnête de (b) (discordance) est **renversé**, mais par dérivation — l'indice opposé
  (ii) (`d=3` impair) avait été **nommé au cadrage §6**, donc la bascule est principielle, non un fit.
- **R-7 / additivité.** Aucune touche aux chaînons amont scellés (`O2-P1`, `CT-DUAL`,
  `HOLOGRAPHIE-G3`, `A-D1-FACTEUR-CONFORME` byte-identiques) ; patchs ultérieurs additifs.

---

## 1. Rappel `[hérité de (b) — NE PAS refaire]`

(b) (`LC-D-O2-P1` §2) : l'inversion de Penrose **swappe** source↔VEV (`g₀↔g₃`) ⟹ `P=[[0,s],[1,0]]`,
`P²=s·𝟙`, **`P=S ⟺ s=−1`** ; l'involution conforme **nue** donne `s=+1`. Le seul porteur possible du
`−1` = le facteur conforme **négatif** `ω<0`, **s'il descend** comme `ω^w` ⟹ `s=(−1)^w`. La S-map
scellée : `S=[[0,−1],[1,0]]`, `S²=−𝟙`, vp `±i`. Modes `(f_a,f_b)=(source,VEV)`. On ne re-dérive ni
`S²=−𝟙` (`CT-DUAL`), ni le dictionnaire FG (`HOLOGRAPHIE-G3`), ni le swap (`O2-P1`).

---

## 2. Résultat de l'algèbre `[(b′) — sceau verif_O2_bprime.py]`

**[A] Le poids `w` est le gap dimensionnel FG.** L'équation indicielle du mode TT,
`z²H'' + (1−d)zH' = 0`, a pour racines `{0, d}` (`verif_D_g3`, `HOLOGRAPHIE-G3`) : `Δ_-=0` (source
`g₀`, branche `z⁰`) et `Δ_+=d` (VEV `g₃=⟨T⟩`, branche `z^d`). Le poids séparant les deux branches —
celui que la patte VEV→source `s` met à l'échelle — est le **gap** :
$$w \;=\; \Delta_+ - \Delta_- \;=\; d.$$

**[B] Descente du signe sous la réciprocité NÉGATIVE de Penrose.** La réciprocité `Ω̂·Ω̌=−1`
(`LC-A-D1-FACTEUR-CONFORME`, *Cycles of Time*) agit comme `Ω ↦ ω = −1/Ω`. Une branche se comportant
comme `Ω^Δ` devient
$$\omega^{\Delta} = (-1/\Omega)^{\Delta} = (-1)^{\Delta}\,\Omega^{-\Delta},$$
donc prend le **facteur de signe `(−1)^Δ`**. La branche source (`Δ_-=0`) prend `(−1)⁰=+1` ; la
branche VEV (`Δ_+=d`) prend `(−1)^d`.

**[C] Le poids GLOBAL se simplifie — `s` ne dépend que du gap.** `s` est le coefficient **relatif**
entre les deux branches. Tout poids **d'ensemble** (placement d'indices ; facteur conforme global
`a²` — p. ex. le tenseur de Weyl tout-bas a poids `+2`, pair) multiplie **les deux pattes de `P` à
l'identique** et **se simplifie** dans le signe. Ne survit que le signe **relatif** :
$$\boxed{\,s \;=\; (-1)^{\Delta_+ - \Delta_-} \;=\; (-1)^{d}\,}\qquad(\text{indépendant du placement d'indices}).$$
La **descente est non triviale** (`w=d≠0`) et **non sign-blind** : la réciprocité de Penrose est
**négative**, et la loi de transformation tensorielle (S-dualité de Haro `0808.2054` eq.50-51 :
`E=⟨T⟩`, `B=Cotton`, `S²=−1` ; loi de Weyl de Maldacena : le tenseur de Weyl du mode prend une
**puissance** du facteur conforme) confirme que le signe **descend** sur le mode TT — il n'est pas
absorbé dans un `ω²` aveugle au signe. **(b′)-G2 satisfaite.**

**[D] Branchement parité — concordance ⟺ `d` impair.** `s=(−1)^d` ⟹
- `d` **impair** ⟹ `s=−1` ⟹ `P=[[0,−1],[1,0]]=S`, `P²=−𝟙=S²` : **concordance**.
- `d` **pair** ⟹ `s=+1` ⟹ `P²=+𝟙≠S²` : discordance (involution).

**[E] Cas physique CCC.** Le bord pertinent est `𝓘⁺` **spacelike** de de Sitter ⟹ `d=3`
(`HOLOGRAPHIE-G3` §2). `d=3` **impair** ⟹ `s=−1` ⟹ **`P=S`**. La réciprocité conforme de Penrose
**reproduit la S-map de de Haro, facteurs compris** (swap `établi` en (b) + signe `−1` `établi` ici).

> **Sceau.** `verif_O2_bprime.py` (EXIT 0, **21 assertions**) avec **firewall 3 mutations cassantes** :
> **(m1)** parité inversée `(−1)^d↦(−1)^{d+1}` ⟹ à `d=3`, `s=+1`, `P≠S` (casse la concordance) ;
> **(m2)** descente triviale `w=0` ⟹ `s=+1 ∀d`, `P²=+𝟙≠S²` (casse) ; **(m3)** inversion **positive**
> `Ω·ω=+1` ⟹ branche `Ω^Δ↦(+1)^Δ`, `s=+1 ∀d` (le signe ne descend pas — casse). Contrôle [C] :
> un poids global `c>0` laisse `sign(s)` inchangé. sha256 `2ee47bc586c8`.

---

## 3. Verdict `[(b′)]`

`réduction` **(de la décision ouverte P1 — PAS du périmètre).** La parité de `w` est **tranchée** :
`w = Δ_+−Δ_- = d`, `s = (−1)^d`. En **`d=3`** (CCC, impair), **`s=−1`** ⟹ `P=S`, `P²=−𝟙=S²`. Donc :

**(C-O2) en forme forte « Penrose = S-map, facteurs compris » est ÉTABLIE au niveau P1** ⟹
**GATE P1 FRANCHIE** (concordance). Le `−𝟙` de la dualité, dont (b) avait montré qu'il **n'est pas**
fourni par l'involution conforme nue, **EST** fourni par la **réciprocité négative** combinée au
**gap dimensionnel impair** `d=3` : `s=(−1)³=−1`.

**Renversement assumé du penchant (b).** (b) penchait **discordance** (raisonnement sur un facteur
**scalaire**, poids positif). (b′) renverse : le bon objet est le signe **relatif inter-branches** =
le **gap `d`**, **impair** en `d=3`. Cet indice avait été **nommé au cadrage §6 (ii)** ; la bascule
est donc **principielle** (dérivée), non un fit. C'est l'intérêt d'avoir **gelé la cible avant** de
calculer.

**Sensibilité dimensionnelle (falsifiable).** Le résultat `s=(−1)^d` est **propre à la parité de `d`** :
en `d` pair il y aurait discordance. La CCC vit en `d=3` (bord `𝓘⁺` spacelike, `d` impair) — c'est
**précisément** le régime concordant. Résultat non générique mais **réalisé** par le cas physique.

**Fetch externe NON déclenché.** Le point (b′)-1(ii) (descente tensorielle) était **prévu
fetch-conditionnel** ; **KB-local a suffi** : la réciprocité **négative** était déjà digérée
(`LC-A-D1-FACTEUR-CONFORME`), et la **non-sign-blindness** de la descente est portée par la S-dualité
de Haro + la loi de Weyl de Maldacena (KB-locales). L'entrée `[ANTI-FETCH — b′]` de `04_references`
reste donc **NON consommée**.

**Conséquence pour A4 `[§6.4 — pas de surclassement]`.** Le chemin « jonction = S (pleine dualité) ⟹
état=eigenmode ⟹ WCH » de `LC-D-O2-JONCTION §5` voit sa **première gate franchie**. Mais **P2**
(cohérence de jonction ⟹ état = eigenmode de `S`) **reste `à inventer`** — c'est le lien le plus
risqué (il pourrait masquer un choix d'état déguisé). **A4 n'est PAS réduit ; {A4 ; A2★ ; N}
INCHANGÉ.**

---

## 4. Format de chaînon

- **Hypothèse.** Le signe résiduel `s=(−1)^w` vaut `−1` (i.e. `w` impair), de sorte que `P=S`.
- **Outil.** Algèbre KB-local : exposants FG `{0,d}` (gap = `w`), réciprocité **négative** de Penrose
  (descente `(−1)^Δ` par branche), simplification du poids global (signe relatif), S-dualité de Haro
  + loi de Weyl (non-sign-blindness). Sceau avec firewall 3 mutations.
- **Critère de réfutation (du chaînon lui-même).** (i) si le facteur de signe ne descendait **pas**
  (`ω²` aveugle), `s=+1` (firewall m3) ; (ii) si la parité était l'opposée, `s=+1` à `d=3` (firewall
  m1) ; (iii) si `w` était nul/pair (descente triviale), `s=+1` (firewall m2). Le résultat **dépend**
  de la parité de `d` — il **bascule** en `d` pair (test honnête, pas un OUI forcé).
- **Verdict.** `réduction` **(décision ouverte P1 → tranchée)** : `s=(−1)^d`, **`s=−1` en `d=3`**,
  `P=S` ⟹ **(C-O2) forte établie au niveau P1, gate P1 franchie**. **Ne construit pas O₂ ; ne fixe
  aucun coefficient ; ne réduit pas A4 (P2 reste) ; {A4 ; A2★ ; N} inchangé.**

---

## 5. Prochain pas `[handoff — sur GO]`

- **P2 — la seconde (et dernière) gate de la réduction d'A4.** Tester : la **cohérence de jonction**
  (recollement Dirichlet|Neumann au `𝒞`, avec la dualité `S` maintenant `établie` comme map de
  jonction) **force-t-elle** l'état à être l'**eigenmode `+i` de `S`** (BD) — **sans** réintroduire
  un choix d'état déguisé ? `à inventer` ; cadrage gelé dédié AVANT toute algèbre/fetch. **C'est le
  seul verrou restant entre O₂ et une réduction effective d'A4** (qui resterait, même alors,
  subordonnée à un audit froid + sceau).
- **Audit froid (b′)** : recommandé (résultat **positif** qui franchit une gate ⟹ enjeu de
  surclassement ; passe incognito + agent séparé, conformément à la discipline). Le sceau est
  symbolique en `d` (firewall en place), donc auditable à froid.

---

## 6. Renvois, glossaire, références

**Renvois.** `LC-D-O2-P1 §2[E],§5` (signe `s=(−1)^w` isolé, prochain pas b′) ;
`LC-D-O2-JONCTION §5` (gates P1/P2 ; G4 = gate P1 désormais franchie) ; `LC-WORK-CADRAGE-O2-BPRIME`
(cible gelée) ; `LC-D-CT-DUAL` (`S²=−𝟙`, S-dualité `E/B`, source unique du signe) ;
`LC-D-HOLOGRAPHIE-G3` (exposants FG `{0,d}`, `⟨T⟩=(d/16πG)g₃`) ; `LC-A-D1-FACTEUR-CONFORME`
(réciprocité **négative** `Ω·ω=−1`) ; `LC-AUDIT-VERDICT §6.4`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Étape (b′) (O₂)* : la parité du poids conforme `w` du mode TT = parité du **gap dimensionnel**
  `Δ_+−Δ_-=d` ; sous la réciprocité **négative** de Penrose, `s=(−1)^d` (poids global simplifié) ;
  `d=3` (CCC) impair ⟹ `s=−1` ⟹ `P=S` ⟹ **gate P1 franchie**. Ne réduit pas A4 (P2 reste).

**Références (`LC-04`).** S-O2-b′-1 = KB-local (a **suffi** ; fetch externe **non** déclenché).
Entrée `[ANTI-FETCH — b′]` : réciprocité conforme **tensorielle** de Penrose, *Cycles of Time*
(2010, **déjà en KB [LC-A]**) — reste **NON consommée** (la réciprocité négative était déjà digérée
en `LC-A-D1-FACTEUR-CONFORME`) ; de Haro `0808.2054` (S-dualité) + Maldacena (loi de Weyl)
KB-locales.

---

## Appendice — Légende des tags épistémiques
`réduction` : la **décision ouverte** P1 (signe `s=(−1)^w`) est **tranchée** (`s=−1` en `d=3`) ;
**réduction d'une décision ouverte, PAS du périmètre `{A4 ; A2★ ; N}`**.
`établi` : (b′) — `w=d` (gap FG), `s=(−1)^d` (descente du signe), `P=S` à `d=3` (algèbre+descente
KB-local) ; **rien d'autre**.
`formalisable` : P2 (cohérence de jonction ⟹ eigenmode) — la voie est posée, le test reste à faire.
`à inventer` : O₂ (construction) ; coefficient O(1) (G3, différé) ; **P2** (gate restante vers A4).
`décision ouverte` : il n'en reste **plus** sur P1 ; la suivante est **P2**.
`piste / à étayer` : (C-O2) — **forte établie au niveau P1** ; sa portée pour A4 dépend de P2.
**A4 non réduit ; D1 non clos ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé ; CCC non démontrée.**
