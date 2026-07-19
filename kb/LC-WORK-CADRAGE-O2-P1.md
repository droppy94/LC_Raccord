---
id: LC-WORK-CADRAGE-O2-P1
titre: "Cadrage gelé du test de P1 (étape (b) du pivot O₂). Gèle, AVANT toute algèbre et tout fetch (anti-fit), la question (P1 : la réciprocité conforme de Penrose au crossover 𝒞 — inversion Ω·ω=−1 — induit-elle EXACTEMENT la S-map de de Haro scellée, FACTEURS COMPRIS ?), les deux côtés (scellé = S:(E,B)↦(B,−E), S=[[0,−1],[1,0]], S²=−𝟙, vp ±i, BD=+i, solution radiale (f_a,f_b) ; à tester = l'échange dominant↔sous-dominant g₀↔g₃ induit par l'inversion FG), les quatre cibles P1-G1..G4 (swap / carré=−𝟙 / signes / structure propre ±i), le critère de réfutation (tout mismatch G1–G3 réfute P1 et (C-O2)), et les forks tranchés : S-O2-b-1 = KB-LOCAL d'abord (de Haro FG + S scellée + relation réciproque Ω·ω=−1 déjà en KB [LC-A] ; fetch Penrose post-gel SEULEMENT si un facteur manque) ; S-O2-b-2 = portée (α) MAP INDUITE SUR (f_a,f_b) + carré/swap/signe SEULEMENT (coefficient/C_T(θ) = G3 différé) ; S-O2-b-3 = SCEAU réel verif_O2_P1.py avec firewall (mutations cassantes : signe inversé, carré +𝟙, swap absent). NE prouve rien (cadrage). Prior honnête : indécis, à fort enjeu — le lien « inversion scalaire Ω ⟹ map tensorielle sur modes TT » n'est PAS automatique et peut ÉCHOUER (le test doit pouvoir dire NON). Et P1 concordante ≠ A4 réduit (il reste P2). Périmètre {A4 ; A2★ ; N} INCHANGÉ."
codename: LC-RACCORD
tags: [work, cadrage, gel, O2, P1, etape-b, jonction, dirichlet-neumann, graviton-dual, de-haro, S-dualite, penrose-reciprocite, fefferman-graham, f_a-f_b, S2=-1, eigenmode, bunch-davies, anti-fit, sceau, firewall, §6.4, A4, branche-falsifiabilite, pivot]
type: "document de cadrage (work) — forme GELÉE avant algèbre/fetch (paper-first / anti-fit). Subordonné à LC-AUDIT-VERDICT §6.4 et au cadrage LC-WORK-CADRAGE-O2-RACCORDEMENT v0.1. Ouvre l'étape (b) du pivot O₂ (test de P1) ; la cartographie (a) est figée dans LC-D-O2-JONCTION v0.1. AUCUN résultat, AUCUNE algèbre, AUCUN fetch dans ce fichier."
statut: "cadrage gelé — forme figée le 2026-06-15 (sha256 reporté hors-fichier au dépôt). Forks tranchés : S-O2-b-1=KB-local ; S-O2-b-2=(α) ; S-O2-b-3=sceau+firewall. Exécution (b) sur GO séparé. NE teste rien ici ; A4 non réduit ; D1 non clos ; N non fixé ; CCC non démontrée ; {A4 ; A2★ ; N} INCHANGÉ."
statut_id: provisoire — à enregistrer si validé
version: 0.1
langue: fr
date: 2026-06-15
maj: "2026-06-15 — v0.1 : ouverture/gel de l'étape (b) du pivot O₂ (test de P1). Cible figée AVANT toute algèbre/fetch : question P1, les deux côtés (scellé / à tester), cibles P1-G1..G4, critère de réfutation, forks S-O2-b-1/2/3 tranchés (KB-local ; (α) ; sceau+firewall). Acquis amont (NON re-dérivés ici) : S-map de Haro scellée AdS (CT-DUAL S1, verif_D_CT_dual.py 18) + dS (S2, verif_D_CT_dual_dS.py 13 + gardefou 14 ; BD=+i mode propre, S²=−𝟙 préservé) ; dictionnaire FG ⟨T⟩=(d/16πG)g₃ (HOLOGRAPHIE-G3) ; jonction = transition Dirichlet→Neumann + gates P1/P2 (LC-D-O2-JONCTION (a)). SANS SURCLASSEMENT (§6.4) : un cadrage ne teste rien ; P1 concordante (si obtenue) ≠ A4 réduit (il resterait P2) ; {A4 ; A2★ ; N} INCHANGÉ."
prerequis_kb: [LC-WORK-CADRAGE-O2-RACCORDEMENT, LC-D-O2-JONCTION, LC-D-CT-DUAL, LC-D-HOLOGRAPHIE-G3, LC-D-CT-REALITE, LC-D-CT-GAMMA, LC-D-F5-ETAT-RACCORD, LC-A-SURVIE-CONFORME, LC-AUDIT-VERDICT]
renvois: [LC-D-O2-JONCTION, LC-WORK-CADRAGE-O2-RACCORDEMENT, LC-D-CT-DUAL, LC-WORK-BRANCHE-FALSIFIABILITE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
tags_epistemiques: [à inventer, formalisable, décision ouverte, piste / à étayer, établi]
---

# LC-WORK · Cadrage gelé du test de P1 (étape (b) du pivot O₂)

> **Statut de ce fichier.** Cadrage **gelé** (paper-first / anti-fit). Il **pose le test** et **fige la
> cible** avant toute algèbre et tout fetch ; il **ne teste rien**, **ne prouve rien**, **ne réduit
> pas A4**. Le sha256 de la forme figée est reporté hors-fichier au dépôt (marqueur de gel anti-fit).
> Exécution de l'étape (b) sur **GO séparé**.

---

## 0. Rôle, garde-fous `[§6.4 + anti-fit + R-7]`

- **Étage.** (b) est un **test d'algèbre** d'une proposition nommée (P1). Ce qui pourra être `établi`
  en aval est **la concordance ou la discordance des facteurs** (un fait d'algèbre), **jamais** la
  construction d'O₂ ni la réduction d'A4.
- **Non-surclassement (§6.4).** **P1 concordante ≠ A4 réduit.** P1 est **une** des deux gates de la
  réduction d'A4 (`LC-D-O2-JONCTION §5`) ; il resterait **P2** (cohérence de jonction ⟹ état =
  eigenmode). Le compte **{A4 ; A2★ ; N}** reste **INCHANGÉ** quel que soit le verdict de (b). N ≡ Λ
  `hors de portée`, non touché.
- **Anti-fit.** La question P1, les cibles P1-G1..G4 (§3) et le critère de réfutation sont **figés
  ici, avant** toute algèbre et tout fetch. La S-map scellée est la **référence connue** ; (b)
  teste si l'inversion de Penrose la **reproduit** — la prédiction gelée est un **OUI/NON** sur les
  facteurs, jamais un ajustement de l'inversion pour coller à `S`. Tout amendement de cible = R-7
  daté.
- **R-7 / additivité.** Aucun déplacement de fichier ; aucune touche aux chaînons amont scellés
  (`CT-DUAL`, `HOLOGRAPHIE-G3` byte-identiques). Patchs ultérieurs strictement additifs.

---

## 1. La question P1 `[hérité de (a) — NE PAS re-poser]`

**P1 :** la **réciprocité conforme de Penrose** au crossover `𝒞` (inversion du facteur conforme
`Ω·ω=−1`, le « retournement » inside-out de la CCC) **induit-elle, sur la donnée holographique et
les observables radiatives, EXACTEMENT la S-map de de Haro** (scellée) — **facteurs compris** (signe,
carré, swap) ?

Si **oui** : la gate 1 de la réduction d'A4 (`LC-D-O2-JONCTION`) est franchie. Si **non** : **(C-O2)
tombe** et O₂ reste `à inventer` sans chemin vers A4.

---

## 2. Les deux côtés du test `[objets, non re-dérivés]`

**Côté SCELLÉ (référence, KB — `LC-D-CT-DUAL` S1+S2).**
- S-map : `S:(E,B)↦(B,−E)`, `S=[[0,−1],[1,0]]`, `S²=−𝟙`, valeurs propres `±i`.
- Secteurs : électrique `E∝g₃∝⟨T⟩` (parité paire) ; magnétique `B∝Cotton` (parité impaire).
- Solution radiale de de Haro `(f_a,f_b)` (éq. 43), identité de 3ᵉ dérivée (éq. 44) refermant avec
  l'échange `(a,b)↦(−b,a)`.
- dS (S2) : `S²=−𝟙` préservé ; **BD = mode propre `+i`** (`BD=f_a−i f_b`).

**Côté À TESTER (l'inversion de Penrose).**
- `Ω·ω=−1` au `𝒞` : géométriquement, un **échange dominant↔sous-dominant** dans l'expansion de
  Fefferman-Graham — candidat au swap `g₀↔g₃`.
- **Test** : cet échange, porté sur la solution radiale `(f_a,f_b)`, induit-il la **matrice `S`** —
  avec le **bon carré (`−𝟙`)**, le **bon swap**, le **bon signe** ?

---

## 3. Cibles GELÉES P1-G1..G4 `[anti-fit — figées avant algèbre/fetch]`

- **P1-G1 — swap.** L'inversion `Ω·ω=−1` induit-elle l'échange `g₀↔g₃` (dominant↔sous-dominant FG) ?
- **P1-G2 — carré.** La map induite **carre-t-elle à `−𝟙`** (≡ `S²=−𝟙`) ?
- **P1-G3 — signe.** Les **signes** collent-ils : `S=[[0,−1],[1,0]]` (et non `[[0,1],[−1,0]]`, ni un
  signe global opposé) ?
- **P1-G4 — structure propre.** Les valeurs propres `±i` sont-elles **préservées**, et **BD (`+i`)**
  mappé de façon **cohérente** (pas envoyé hors de son sous-espace propre) ?

**Critère de réfutation gelé.** **Tout** mismatch structurel sur **P1-G1, P1-G2 ou P1-G3** réfute
P1 — et donc **(C-O2)**. (P1-G4 est un contrôle de cohérence ; un échec isolé y serait consigné comme
réserve, non comme réfutation pleine, à adjuger.)

---

## 4. Forks de scope `[S-O2-b-N — tranchés]`

- **S-O2-b-1 `[TRANCHÉ : KB-local d'abord]`.** Algèbre sur acquis KB : de Haro FG + `(f_a,f_b)` +
  S-map scellée + **relation réciproque `Ω·ω=−1` déjà en KB** (Penrose, *Cycles of Time*, [LC-A]).
  **Fetch post-gel** de Penrose **seulement si** un facteur précis de l'inversion (signe, domaine)
  manque au KB — décision séparée, post-gel, avec consommation explicite (cf. `04_references`
  `[ANTI-FETCH — P1]`).
- **S-O2-b-2 `[TRANCHÉ : portée (α)]`.** Calcul de la **map induite sur `(f_a,f_b)`** + vérification
  **carré / swap / signe** **seulement**. Le coefficient (action induite sur `C_T(θ)`, levier G3 de
  `LC-D-O2-JONCTION`) est **différé** — (b) teste P1 **chirurgicalement**, sans toucher au coefficient
  O(1) (qui reste `à inventer`).
- **S-O2-b-3 `[TRANCHÉ : sceau + firewall]`.** (b) est de l'algèbre ⟹ **sceau réel**
  `verif_O2_P1.py` (EXIT 0, compte d'assertions consigné) avec **firewall** : mutations cassantes
  obligatoires — **(m1)** signe inversé `S↦[[0,1],[−1,0]]` doit casser P1-G3 ; **(m2)** carré forcé
  `+𝟙` doit casser P1-G2 ; **(m3)** swap absent (map diagonale) doit casser P1-G1. Sceau réversible
  tant que (b) non validé (précédent S-F5-2).

---

## 5. Méthode `[(b) — sur GO]`

1. Poser l'inversion `Ω·ω=−1` comme transformation de la coordonnée radiale / du facteur conforme FG,
   et calculer son action sur le couple `(f_a,f_b)` (KB-local, de Haro éq. 43-44).
2. Lire la matrice induite `M` dans la base `(f_a,f_b)` ; comparer à `S=[[0,−1],[1,0]]`.
3. Vérifier **P1-G1** (swap : `M` hors-diagonale), **P1-G2** (`M²=−𝟙`), **P1-G3** (signes), **P1-G4**
   (vp `±i`, image de BD).
4. Sceller (`verif_O2_P1.py`) avec les 3 mutations firewall (§4, S-O2-b-3).
5. Verdict : **concordance** (P1 `établi (algèbre)`, gate 1 franchie) **ou** **discordance** ((C-O2)
   réfutée, O₂ reste `à inventer`). Audit froid : différable (réversible), à décider au verdict.

---

## 6. Prior honnête `[§6.4]`

- **Issue indécise, à fort enjeu.** Le maillon **risqué** : la réciprocité de Penrose est une relation
  sur un **scalaire** (`Ω`), la S-map agit sur la **donnée tensorielle** (modes graviton TT). Le lien
  « inversion scalaire ⟹ map tensorielle » n'est **pas** automatique et peut **échouer** (l'inversion
  pourrait agir trivialement sur les modes TT, ou avec une autre structure de signe). **Le test doit
  pouvoir dire NON.**
- **Garde d'honnêteté.** Risque de **construire une attente trop nette** (récit propre). Le firewall
  (§4) et le critère de réfutation (§3) sont là pour que la discordance soit **détectable** et
  **consignée**, pas absorbée.
- **Même si P1 concorde : `{A4 ; A2★ ; N}` INCHANGÉ.** P1 = **une** gate ; il resterait **P2**
  (`à inventer`, le lien le plus risqué). Concordance = « gate 1 franchie », **pas** réduction d'A4,
  **pas** fermeture de D1, **pas** fixation de N.

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D-O2-JONCTION §3,§5` (P1 nommée, (C-O2), gates) ; `LC-D-CT-DUAL` (S-map scellée
AdS+dS, `(f_a,f_b)`, BD=`+i`) ; `LC-D-HOLOGRAPHIE-G3` (FG, `⟨T⟩=(d/16πG)g₃`) ;
`LC-WORK-CADRAGE-O2-RACCORDEMENT` (cadre O₂, gates) ; `LC-AUDIT-VERDICT §6.4`.

**Références (`LC-04`).** S-O2-b-1 = KB-local. Source `[ANTI-FETCH / post-gel]` pour un facteur
manquant de l'inversion : réciprocité conforme de Penrose (`Ω·ω=−1`), R. Penrose *Cycles of Time*
(2010, **déjà en KB [LC-A]**) — **non re-consommée** tant que (b) n'a pas montré qu'un facteur manque.
de Haro `0808.2054` (S-map, `(f_a,f_b)`) **KB-locale**.

---

## Appendice — Légende des tags épistémiques
`à inventer` : P1 (non testée) ; P2 ; O₂ (construction) ; coefficient O(1) (G3, différé).
`formalisable` : la méthode §5 (algèbre KB-local sur de Haro FG + S scellée).
`piste / à étayer` : (C-O2) — testée via P1 en (b).
`établi` : ici, RIEN (cadrage). En aval : la concordance/discordance des FACTEURS sera `établi (algèbre)`, jamais « A4 réduit / D1 clos / CCC démontrée ».
**A4 non réduit ; D1 non clos ; {A4 ; A2★ ; N} INCHANGÉ ; N non fixé ; CCC non démontrée.**
