---
id: LC-D-O2-P1
titre: "Pivot O₂, étape (b) — TEST de P1 (la réciprocité conforme de Penrose Ω·ω=−1 induit-elle EXACTEMENT la S-map de de Haro, facteurs compris ?). Résultat à DEUX étages : (G1) l'inversion de Penrose induit le SWAP source↔VEV (g₀↔g₃) sur les modes radiaux de de Haro (f_a, f_b) — ÉTABLI (algèbre) ; (G2/G3) la map induite P=[[0,s],[1,0]] a pour carré P²=s·𝟙, donc P=S ⟺ s=−1 — MAIS l'inversion Ω·ω=−1 agit sur la coordonnée comme une INVOLUTION (z↦−1/z, le signe se carre dans z~Ω⁻² et se perd) ⟹ une involution conforme NUE donne s=+1 ⟹ P²=+𝟙 ≠ S²=−𝟙 : la réciprocité conforme NE FOURNIT PAS le −𝟙 de la dualité par sa seule géométrie. Le −𝟙 (= carré de Hodge/E-M pour la S-map P²=−𝟙 [structural, sign-neutre sur C_T via garde-fou, NON transporté par la jonction — cf. O2-HODGE étape c] ; le SIGNE de l'observable provient d'une SOURCE UNIQUE i^{d-1} dS [déjà scellée CT-DUAL S2] — deux −𝟙 DISTINCTS, AUCUN double-comptage) exige que le facteur conforme NÉGATIF ω<0 DESCENDE en −1 sur le mode TT, soit s=(−1)^w (w=parité du poids conforme) — NON pinçable KB-local, DÉCISION OUVERTE, fetch-conditionnel (contingence S-O2-b-1 déclenchée). VERDICT : (C-O2) en forme forte NON établie ; P1 RÉDUITE à un unique signe s ; penche structurellement vers la DISCORDANCE (opération conforme = poids positif ; −1 exige poids impair sous ω<0, non générique) sans la trancher. Même si s=−1 plus tard : P1 n'est qu'UNE des deux gates (P2 reste). Sceau verif_O2_P1.py EXIT 0/20, firewall 3 mutations. {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; CCC non démontrée."
codename: LC-RACCORD
tags: [module-D, O2, P1, etape-b, branche-falsifiabilite, jonction, dirichlet-neumann, graviton-dual, de-haro, S-dualite, penrose-reciprocite, fefferman-graham, f_a-f_b, involution, S2=-1, poids-conforme, eigenmode, A4, sceau, firewall, delimitation, §6.4, pivot]
type: "chaînon de front (branche FALSIFIABILITÉ, pivot O₂) — étage (b) TEST de P1, SCELLÉ (verif_O2_P1.py). Portée S-O2-b-2=(α). Subordonné à LC-AUDIT-VERDICT §6.4 et au cadrage gelé LC-WORK-CADRAGE-O2-P1 v0.1 (sha256 9859e78c3da3…, cibles P1-G1..G4 gelées avant algèbre/fetch)."
statut: "délimitation — (b) test de P1 FAIT (interne, KB-local, sceau réel). (G1) SWAP source↔VEV (g₀↔g₃) induit par l'inversion de Penrose : ÉTABLI (algèbre). (G2/G3) map induite P=[[0,s],[1,0]], P²=s·𝟙, P=S ⟺ s=−1 ; l'inversion Ω·ω=−1 est une INVOLUTION de coordonnée (z↦−1/z, signe carré perdu) ⟹ involution conforme nue s=+1 ⟹ P²=+𝟙 ≠ S²=−𝟙 : la réciprocité conforme NE fournit PAS le −𝟙. (E) facteur décisif s=(−1)^w (descente du signe ω<0 sur le mode TT, parité du poids w) NON pinçable KB-local ⟹ DÉCISION OUVERTE, fetch-conditionnel (S-O2-b-1 déclenchée). VERDICT : (C-O2) forte NON établie ; P1 réduite à un signe ; penche DISCORDANCE sans trancher ; même si s=−1, P2 reste. Sceau verif_O2_P1.py EXIT 0/20, firewall 3 mutations (m1 signe S inversé, m2 carré forcé indépendant de s, m3 swap absent). SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos ; N non fixé (≡ Λ) ; CCC non démontrée."
statut_id: "validé après sceau (verif_O2_P1.py, EXIT 0, 20 asserts, firewall 3 mutations, sha256 6b23b2ae2b3c) — à enregistrer si validé ; PROPAGER (lot séparé) : LC-AUDIT-VERDICT §8bis, 00_index, 03_glossaire, 04_references (fetch P1 = note active), LC-WORK-BRANCHE-FALSIFIABILITE (fiche F5/O₂), LC-D-O2-JONCTION (renvoi G4 : gate P1 réduite au signe)."
version: 0.3
langue: fr
date: 2026-06-15
maj: "2026-06-26 — v0.3 (F-α, patch audit froid, RÉDACTIONNEL) : désambiguïsation du libellé du −𝟙 dans le titre. L'ancienne formule (« −𝟙 porté par la structure Hodge/E-M ET le i^{d-1} dS ») invitait une lecture DOUBLE-COMPTAGE. Corrigé : le −𝟙 de la S-map P²=−𝟙 EST le carré de Hodge (structural, sign-neutre sur C_T via garde-fou, NON transporté par la jonction — O2-HODGE c) ; le SIGNE de l'observable a une SOURCE UNIQUE i^{d-1} (CT-DUAL S2) ⟹ deux −𝟙 distincts, pas de double-comptage. Re-dérivé indépendamment (audit froid α : verif_O2_P1 laisse s SYMBOLIQUE = aucun −1 injecté ; verif_O2_hodge bannit le transport ; garde-fou ratio +1). PUREMENT rédactionnel : corps/dérivation et sceaux INTACTS, verdict (b) délimitation INCHANGÉ. AUCUN sceau, AUCUNE algèbre, AUCUN fetch. SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée. | 2026-06-15 — v0.2 : RENVOI ADDITIF (propagation du verdict (c), LC-D-O2-HODGE v0.1, sceau verif_O2_hodge.py EXIT 0/28, sha256 421d5f29a9ee). Le PENCHANT-DISCORDANCE laissé ouvert au §3 est désormais FERMÉ — non par un calcul de parité (la tentative (b′) LC-D-O2-BPRIME a été RÉFUTÉE comme épissure), mais par la STRUCTURE : (c) établit que le −1 du Hodge n'est PAS dans la jonction (J=Swap(s=+1)≠S, invariant de classe det/ordre ; garde-fou C̃_T=+C_T ; le −1 physique = i^{d-1} dS, source unique INDÉPENDANTE). s=+1 confirmé structurellement ; le signe décisif n'était pas une parité mais l'appartenance sectorielle du −1. Note datée ajoutée en fin de §6 ; aucune touche à l'algèbre (b) ni au sceau verif_O2_P1.py (corps intact, s reste symbolique dans le sceau). SANS SURCLASSEMENT (§6.4) : {A4 ; A2★ ; N} INCHANGÉ ; A4 non réduit ; D1 non clos. | 2026-06-15 — v0.1 : ouverture/scellement de l'étape (b) du pivot O₂ — test de P1. Exécute le cadrage gelé LC-WORK-CADRAGE-O2-P1 v0.1 (portée (α), S-O2-b-1=KB-local, S-O2-b-3=sceau+firewall). Sceau verif_O2_P1.py (EXIT 0, 20 asserts, firewall 3 mutations cassantes ; sha256 6b23b2ae2b3c). Acquis amont NON re-dérivés : S-map scellée S²=−𝟙 vp ±i (CT-DUAL S1 18 + S2, BD=+i) ; modes (f_a,f_b)=(source,VEV) (de Haro 0808.2054) ; jonction = transition Dirichlet→Neumann + gates P1/P2 (LC-D-O2-JONCTION (a)). RÉSULTAT : (G1) swap ÉTABLI ; (G2/G3) le −𝟙 NON fourni par la réciprocité conforme nue (involution ⟹ P²=+𝟙) ; P1 réduite à s=(−1)^w (parité du poids TT sous ω<0), DÉCISION OUVERTE / fetch-conditionnel. (C-O2) forte NON établie. SANS SURCLASSEMENT (§6.4) : un test d'algèbre qui réduit P1 à un signe ne construit pas O₂, ne fixe aucun coefficient, ne réduit pas A4 ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos."
fichier_compagnon: "verif_O2_P1.py (SCEAU, EXIT 0, 20 assertions, firewall 3 mutations cassantes — m1 signe S inversé / m2 carré forcé indépendant de s / m3 swap absent ; sha256 6b23b2ae2b3c)"
prerequis_kb: [LC-WORK-CADRAGE-O2-P1, LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-RACCORDEMENT, LC-D-CT-DUAL, LC-D-HOLOGRAPHIE-G3, LC-D-CT-REALITE, LC-D-F5-ETAT-RACCORD, LC-A-SURVIE-CONFORME, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_O2_P1.py, verif_D_CT_dual.py]
renvois: [LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-P1, LC-D-CT-DUAL, LC-D-HOLOGRAPHIE-G3, LC-WORK-BRANCHE-FALSIFIABILITE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [délimitation, établi, formalisable, à inventer, décision ouverte, piste / à étayer]
---

# LC-D · O₂ — test de P1 : la réciprocité de Penrose ≟ la S-map (étape b)

> **Objet de cette étape.** Le cadrage gelé (`LC-WORK-CADRAGE-O2-P1` v0.1) a figé la question **P1**
> et les cibles **P1-G1..G4** avant toute algèbre. (b) **teste** P1 par l'algèbre KB-local (portée
> (α) : map induite sur `(f_a,f_b)` + carré/swap/signe). Résultat : le swap est `établi`, mais le
> `−𝟙` de la dualité **n'est pas fourni** par la réciprocité conforme nue ; **P1 se réduit à un
> unique signe** `s=(−1)^w`, `décision ouverte` / fetch-conditionnel. **Rien ici ne construit O₂, ne
> fixe un coefficient, ni ne réduit A4.** Interne, KB-local, **scellé** (`verif_O2_P1.py`).

---

## 0. Rôle et garde-fou `[§6.4 + R-7]`

- **Étage.** (b) est un **test d'algèbre** d'une proposition nommée (P1). Ce qui y est `établi` est
  un **fait d'algèbre** (le swap ; la dépendance `P²=s·𝟙`), **jamais** la construction d'O₂ ni la
  réduction d'A4.
- **Non-surclassement (§6.4).** **P1 réduite à un signe ≠ P1 tranchée ≠ A4 réduit.** Même
  concordance future (`s=−1`) ne franchirait qu'**une** des deux gates (`LC-D-O2-JONCTION §5`) — il
  resterait **P2**. Le compte **{A4 ; A2★ ; N}** reste **INCHANGÉ** ; N ≡ Λ `hors de portée`.
- **Anti-fit.** Cibles P1-G1..G4 gelées au cadrage **avant** l'algèbre. Le signe décisif `s` est
  laissé **symbolique** dans le sceau (garde-fou explicite : `s∈free_symbols`) ⟹ P1 **n'est pas
  forcée** vers oui ni non.
- **R-7 / additivité.** Aucune touche aux chaînons amont scellés (`CT-DUAL`, `HOLOGRAPHIE-G3`
  byte-identiques) ; patchs ultérieurs additifs.

---

## 1. Rappel `[hérité — NE PAS refaire]`

**P1** (`LC-D-O2-JONCTION §5`) : la réciprocité conforme de Penrose au `𝒞` (`Ω·ω=−1`, retournement
inside-out) **induit-elle EXACTEMENT la S-map de de Haro** (scellée) — **facteurs compris** ? Côté
scellé : `S=[[0,−1],[1,0]]`, `S²=−𝟙`, vp `±i`, BD=`+i` ; modes radiaux `(f_a,f_b)` = (source, VEV)
(de Haro `0808.2054`). On ne re-dérive ni `S²=−𝟙` (`CT-DUAL`), ni le dictionnaire FG.

---

## 2. Résultat de l'algèbre `[(b) — sceau verif_O2_P1.py]`

**[A] Modes de de Haro.** `f_a = cos u + u sin u` (`f_a(0)=1` : **source**, non normalisable, `g₀`) ;
`f_b = u cos u − sin u` (`f_b ~ −u³/3` : **VEV**, normalisable, `g₃=⟨T⟩`). Recoupement Bessel
`f_a=−u²y₁`, `f_b=−u²j₁`.

**[B] S-map scellée (référence).** `S²=−𝟙`, vp `±i`, `det S=1`, `tr S=0` (rotation 90°, ordre 4).

**[C] L'inversion de Penrose est une involution de coordonnée.** `Ω~1/z` ⟹ `Ω↦−1/Ω` induit
`z↦−1/z`, **involution** (carré = identité). Le signe de `Ω·ω=−1` **se carre** dans `z~Ω⁻²` : il
**disparaît** au niveau de la coordonnée.

**[D] Map induite — SWAP établi, carré porté par un signe.** Sur `(f_a,f_b)`, l'inversion **échange
source↔VEV** ⟹ `P=[[0,s],[1,0]]` (hors-diagonale), avec `s` = signe de la patte VEV→source.
- **P1-G1 (swap) — `établi (algèbre)`** : `P` hors-diagonale ⟹ `g₀↔g₃`.
- `P² = s·𝟙` ⟹ **`P=S` ⟺ `s=−1`** (`P−S=[[0,s+1],[0,0]]`).
- **involution conforme NUE ⟹ `s=+1` ⟹ `P²=+𝟙` ≠ `S²=−𝟙`.** La réciprocité conforme **ne fournit
  pas** le `−𝟙` de la dualité par sa seule action de coordonnée.

**[E] Le facteur décisif, isolé et OUVERT.** Le seul porteur possible du `−1` est le facteur conforme
**négatif** `ω<0` de `Ω·ω=−1`, **s'il descend** en `−1` sur le mode TT : une mise à l'échelle
conforme donne le facteur `ω^w`, dont le signe (pour `ω<0`) est `(−1)^w` ⟹ **`s=(−1)^w`**, `w` =
parité du poids conforme du mode TT. `w` impair ⟹ `s=−1` (match S) ; `w` pair ⟹ `s=+1` (involution,
discordance). **`w` n'est pas pinçable KB-local** ⟹ `s` reste **symbolique** (garde-fou).

> **Sceau.** `verif_O2_P1.py` (EXIT 0, **20 assertions**) avec **firewall 3 mutations cassantes** :
> **(m1)** signe `S` inversé `[[0,1],[−1,0]]` ⟹ casse P1-G3 ; **(m2)** carré forcé indépendant de
> `s` ⟹ casse P1-G2 (car `P²=s·𝟙`) ; **(m3)** swap absent (map diagonale) ⟹ casse P1-G1. sha256
> `6b23b2ae2b3c`.

---

## 3. Verdict `[(b)]`

`délimitation`. **(C-O2) en forme forte « Penrose = S-map, facteurs compris » n'est PAS établie.** Le
test n'a pas dit oui : la réciprocité conforme fournit le **swap** (P1-G1 `établi`) mais **pas** le
`−𝟙` de la dualité par sa seule géométrie (involution ⟹ `P²=+𝟙`). **P1 est réduite à un unique
signe** `s=(−1)^w`. Le `−𝟙` de S vit dans la structure **Hodge/électrique-magnétique** et le
`i^{d-1}` **dS** (déjà scellé **source unique du signe** en `CT-DUAL` S2) — **pas** dans la
réciprocité conforme.

**Penchant honnête (NON tranché).** Le résultat **penche vers la discordance** : une opération
conforme est une mise à l'échelle de **poids positif**, le `−1` exige un poids **impair** sous `ω<0`,
non générique. Mais `w` n'est pas dérivé ici ⟹ **ni concordance ni réfutation à plat** : le signe est
l'objet précis du prochain pas (b′).

**Conséquence pour la réduction d'A4.** Le chemin « jonction = S (pleine dualité) ⟹ état=eigenmode
⟹ WCH » de `LC-D-O2-JONCTION §5` est **suspendu au signe `s`** : si `s=+1` (discordance), la jonction
n'est qu'un **swap involutif**, pas la dualité `S`, et la gate P1 **échoue** ⟹ pas de réduction d'A4
par cette voie. Si `s=−1`, P1 franchie — mais **P2 reste** (`à inventer`).

---

## 4. Format de chaînon

- **Hypothèse.** L'inversion conforme de Penrose reproduit la S-map de de Haro (facteurs compris).
- **Outil.** Algèbre KB-local : modes de Haro `(f_a,f_b)`, S-map scellée, action de l'inversion
  `Ω·ω=−1` (de coordonnée) ; sceau symbolique laissant `s` libre.
- **Critère de réfutation (du chaînon lui-même).** (i) si l'inversion **ne** swappait **pas**
  source↔VEV, P1-G1 serait faux (firewall m3) ; (ii) si l'on prétendait `P²=−𝟙` **indépendamment** de
  `s`, faux (`P²=s·𝟙`, firewall m2) ; (iii) si l'on fixait `s` sans dériver `w`, ce serait un
  **surclassement** (anti-fit : `s` reste libre).
- **Verdict.** (b) **`délimitation`** : swap `établi` ; `−𝟙` **non** fourni par la réciprocité
  conforme nue ; **P1 réduite à `s=(−1)^w`**, `décision ouverte` / fetch-conditionnel. **(C-O2) forte
  non établie ; ne construit pas O₂ ; ne fixe aucun coefficient ; ne réduit pas A4 ; {A4 ; A2★ ; N}
  inchangé.**

---

## 5. Prochain pas `[handoff — sur GO]`

- **(b′) — fetch post-gel ciblé (contingence S-O2-b-1 déclenchée).** Trancher `s=(−1)^w` = déterminer
  la **parité du poids conforme** du mode TG/VEV sous le facteur conforme **négatif** de Penrose
  (`Cycles of Time`, déjà en KB [LC-A] ; + lois de transformation FG de de Haro). **Cadrage gelé
  dédié** (cible = parité de `w`, gelée AVANT fetch). Issue : concordance (`s=−1`, gate P1 franchie,
  P2 restante) ou discordance (`s=+1`, C-O2 tombe, O₂ reste `à inventer`).
- **Audit froid (b)** : différable (réversible ; sceau symbolique, `s` libre, firewall en place).

---

## 6. Renvois, glossaire, références

**Renvois.** `LC-D-O2-JONCTION §3,§5` (P1, (C-O2), gates) ; `LC-WORK-CADRAGE-O2-P1` (cible gelée) ;
`LC-D-CT-DUAL` (S-map scellée, `(f_a,f_b)`, `S²=−𝟙`, BD=`+i`, source unique du signe `i^{d-1}`) ;
`LC-D-HOLOGRAPHIE-G3` (FG, modes source/VEV) ; `LC-AUDIT-VERDICT §6.4`.

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Test de P1 (O₂-b)* : la réciprocité de Penrose induit le swap `g₀↔g₃` mais pas le `−𝟙` de S (elle
  est une involution conforme) ; P1 réduite au signe `s=(−1)^w` (parité du poids TT sous `ω<0`),
  `décision ouverte`.

**Références (`LC-04`).** S-O2-b-1 = KB-local. Source `[ANTI-FETCH / post-gel, b′]` : réciprocité
conforme de Penrose (`Ω·ω=−1`, parité du poids conforme), `Cycles of Time` (déjà en KB [LC-A]) —
**non consommée** ici ; de Haro `0808.2054` KB-locale.

**Ajout (2026-06-15, propagation `LC-D-O2-HODGE` v0.1 — verdict (c) `discordance`).**
Le **penchant-discordance** du §3 (« opération conforme = poids positif ; `−1` exige poids impair sous
`ω<0`, non générique ») est **FERMÉ**, mais **pas** par la voie envisagée en §5 (parité de `w`) : cette
voie (b′, `LC-D-O2-BPRIME`) a été **RÉFUTÉE** (épissure de deux opérations — swap `Δ↦d−Δ` sign-neutre
vs `Δ↦−Δ`). (c) **relocalise et tranche** par la **structure** : `s=+1` est confirmé **non** parce
qu'un poids serait pair, mais parce que **le `−1` du Hodge n'appartient pas au secteur de la
jonction** — `J=Swap(s=+1) ≠ S` (invariant de classe `det/ordre`) ; garde-fou `CT-DUAL` §3
`C̃_T=+C_T` ; le `−1` physique est l'apport dS **indépendant** `i^{d-1}` (source unique du signe). La
réduction « P1 `=` signe `s=(−1)^w` » du §2[E] est donc **dépassée** : le signe décisif n'était pas
une **parité** mais l'**appartenance sectorielle** du `−1`. Le sceau `verif_O2_P1.py` (où `s` reste
symbolique) demeure **intact et valide**. `{A4 ; A2★ ; N}` **INCHANGÉ** ; A4 non réduit ; D1 non clos.

---

## Appendice — Légende des tags épistémiques
`établi` : (b) — le **swap** (P1-G1) et la dépendance `P²=s·𝟙` (algèbre correcte) ; **rien d'autre**.
`délimitation` : P1 réduite à un signe `s=(−1)^w` ; (C-O2) forte non établie.
`à inventer` : O₂ (construction) ; coefficient O(1) (différé) ; P2.
`décision ouverte` : le signe `s` / la parité `w` (b′, fetch-conditionnel).
`piste / à étayer` : (C-O2) — testée, réduite à `s`, non tranchée.
**A4 non réduit ; D1 non clos ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé ; CCC non démontrée.**
