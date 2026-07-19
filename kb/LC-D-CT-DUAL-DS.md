---
id: LC-D-CT-DUAL-DS
titre: "Module D / dS-CFT — LEAD « DUALITÉ GRAVITON-DUAL DE DE HARO » (arXiv:0808.2054), ÉTAGE S2 : CONTINUATION dS de la dualité (successeur de LC-D-CT-DUAL S1/AdS). Exécute les étapes 2-3 de LC-WORK-CADRAGE-S2 §5. Ce chaînon SCELLE deux sceaux : (i) verif_D_CT_dual_dS.py (EXIT 0, 13 asserts) — GO/NO-GO R1 = GO : l'EOM TT de dS f''−(2/η)f'+k²f=0 a la MÊME forme que l'EOM radiale AdS de de Haro y''−(2/u)y'+y=0 (squelette f_a=cos u+u sin u, f_b=u cos u−sin u transplanté sous u→k|η|), S=[[0,−1],[1,0]], S²=−𝟙, vp ±i (éq.51) PRÉSERVÉ, et la condition de Bunch–Davies DIAGONALISE S (BD=(1−ikη)e^{ikη}=f_a−i f_b = mode propre +i ; BD*→−i ; contrôle négatif) ⟹ la carte S referme sur les modes dS ; (ii) verif_D_CT_gardefou_dS.py (EXIT 0, 14 asserts, firewall inclus) — le GARDE-FOU de signe PERSISTE en dS : la continuation de REALITE attache i^{d-1} au SEUL préfacteur ℓ^{d-1} (même puissance pour C_T et C̃_T en branche 1), tandis que le `−2` (éq.63) et le `−` relatif W̃=−W (éq.61-62), sans ℓ, ne sont PAS continués ⟹ le rapport C̃_T/C_T=+1 est INVARIANT ⟹ C̃_T=+C_T survit (les deux réels négatifs en d=3) ; firewall : injecter (à tort) un i sur le `−2` basculerait à C̃_T=−C_T (break) ⟹ résultat SENSIBLE, non tautologique. VERDICT S2 : CONSOLIDATION (branche α du cadrage §3) — source UNIQUE du signe (ℓ→iℓ), dual CONFIRMATOIRE, PAS de seconde route indépendante. SANS SURCLASSEMENT (§6.4) : « carte S referme en dS + garde-fou persiste » = établi (ALGÈBRE) GIVEN (1) la règle de REALITE (scellée) et (2) l'ℓ-indépendance des facteurs de dictionnaire dual (lecture éq.61-63/66) ; JAMAIS « seconde route au signe acquise » (il n'y en a pas — consolidation), ni « D1 fermé / CCC démontrée ». RÉSIDU décision ouverte / à inventer : validité PHYSIQUE de (2) sous continuation dS complète (structure de Legendre éq.66 en dS) ; identité tensorielle COMPLÈTE éq.44 (□^{3/2}, ε, i^{d-1}) en dS ; question 3 (CFT de raccordement Dirichlet vs duale) NON déclenchée (conditionnelle à une route propre, absente). Le compte {A4 ; A2★ ; N} INCHANGÉ ; D1 NON clos ; (A) physique conditionnel au seul A2★ INCHANGÉ."
codename: LC-RACCORD
tags: [module-D, ds-cft, dualite, graviton-dual, de-haro, bunch-davies, electrique-magnetique, S-dualite, charge-centrale, C_T, signe, garde-fou, continuation-dS, source-unique, consolidation, adS-vs-dS, S2, sceau, D1]
type: chaînon (résultat — scelle l'ÉTAGE S2 du lead dualité de de Haro : continuation dS, étapes 2-3 de LC-WORK-CADRAGE-S2 ; SCEAUX FAITS verif_D_CT_dual_dS.py + verif_D_CT_gardefou_dS.py ; VERDICT consolidation)
statut: "établi (algèbre), SCEAUX FAITS — S2 EN dS. ÉTAPE 2 (GO/NO-GO R1) = GO : carte S referme sur les modes BD de dS (EOM dS de même forme que l'EOM radiale AdS ; squelette (f_a,f_b) transplanté ; S²=−𝟙, vp ±i préservé ; BD=f_a−i f_b = mode propre +i ; contrôle négatif). ÉTAPE 3 (persistance du garde-fou, lève (ii)) = PERSISTANCE : i^{d-1} sur le seul ℓ^{d-1} (même puissance C_T et C̃_T en branche 1) ; `−2` (éq.63) et `−` relatif (éq.61-62) sans ℓ, non continués ⟹ C̃_T/C_T=+1 invariant ⟹ C̃_T=+C_T en dS (réels négatifs, d=3) ; firewall par injection d'erreur (break⟹C̃_T=−C_T, écarté). VERDICT : CONSOLIDATION (branche α §3) — source unique du signe, dual confirmatoire, PAS de seconde route. RÉSIDU décision ouverte : validité physique de l'ℓ-indépendance des facteurs duaux sous dS complet ; identité tensorielle complète éq.44 en dS ; question 3 non déclenchée. SANS SURCLASSEMENT (§6.4) : algèbre établie GIVEN intrants (1)+(2) ; JAMAIS « route acquise » (consolidation, pas réduction du compte) ni « D1 fermé ». Compte {A4 ; A2★ ; N} inchangé."
statut_id: "validé après sceaux (verif_D_CT_dual_dS.py + verif_D_CT_gardefou_dS.py déposés en KB, EXIT 0, 13+14 asserts) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §6) : LC-D-CT-DUAL §Conséquence-pour-S2 (S2 tranché : consolidation), LC-WORK-CADRAGE-S2 (addendum : (i) levée, étapes 2-3 faites, verdict), LC-D-CT-REALITE (renvoi : la continuation i^{d-1} se propage identiquement au dual ⟹ garde-fou invariant), LC-D-HOLOGRAPHIE-G3 §3 (item « CFT de raccordement » : la dualité duale en reste un candidat, question 3 ouverte), LC-AUDIT-VERDICT §8bis, LC-00-INDEX, 03_glossaire, 02_programme, 04_references (de Haro 0808.2054 DÉJÀ en KB)."
version: 0.1
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v0.1 : scelle l'ÉTAGE S2 du lead « dualité graviton-dual de de Haro » (continuation dS ; étapes 2-3 de LC-WORK-CADRAGE-S2 §5), après contrôle d'ouverture (versions 8/8, ancres OK, verif_D_CT_dual.py re-exécuté EXIT 0 18/18 ; stack 3.12/sympy1.14/numpy2.4) et levée préalable de l'incertitude (i) (LC-WORK-S2-LECTURE-EQ65 : coefficient dual de branche 2 ∝ ℓ^{−2}). DEUX sceaux : verif_D_CT_dual_dS.py (EXIT 0, 13 asserts, 3 blocs) — GO R1, carte S referme sur les modes BD de dS, S²=−𝟙 préservé, BD diagonalise S ; verif_D_CT_gardefou_dS.py (EXIT 0, 14 asserts, 4 blocs, firewall) — garde-fou persiste sous continuation dS (rapport C̃_T/C_T=+1 invariant ; le `−2` et le `−` relatif sans ℓ non continués). VERDICT S2 : consolidation (branche α §3) — source unique du signe, PAS de seconde route indépendante. SANS SURCLASSEMENT (§6.4) : établi (algèbre) GIVEN (1) règle REALITE + (2) ℓ-indépendance des facteurs duaux (lecture éq.61-63/66) ; résidu décision ouverte (validité physique de (2) sous dS complet ; identité tensorielle complète éq.44 ; question 3). Aucune touche aux chaînons existants (algèbre DUAL/REALITE/ATN/NONLIN-VERROU intacte). Propagation §6 NON exécutée (proposée, lot séparé). Compte {A4 ; A2★ ; N} inchangé ; D1 NON clos ; (A) physique conditionnel au seul A2★ inchangé ; CCC non démontrée."
fichier_compagnon: verif_D_CT_dual_dS.py
fichiers_compagnons_kb: [verif_D_CT_dual_dS.py, verif_D_CT_gardefou_dS.py, verif_D_CT_dual.py, verif_D_CT_realite.py]
prerequis_kb: [LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-CT-ATN, LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-WORK-CADRAGE-S2, LC-WORK-S2-LECTURE-EQ65, LC-AUDIT-VERDICT, LC-00-INDEX]
renvois: [LC-D-CT-DUAL, LC-D-CT-REALITE, LC-D-CT-ATN, LC-D-NONLIN-VERROU, LC-D3-WEYL-BUNCHDAVIES, LC-D-HOLOGRAPHIE-G3, LC-WORK-CADRAGE-S2, LC-WORK-S2-LECTURE-EQ65, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] holographie / dS-CFT — continue la dualité électrique/magnétique de de Haro de S1 (AdS) au bulk dS₄ : la carte S referme sur les modes de Bunch–Davies (S²=−1 préservé, BD = mode propre +i) et le garde-fou de signe est continuation-invariant ⟹ le dual CONFIRME le signe de C_T au lieu de le déterminer indépendamment. Verdict : consolidation (source unique du signe), pas de seconde route."
  - "[D] / réalité de C_T — verrouille la lecture de LC-D-CT-REALITE : la continuation i^{d-1} se propage IDENTIQUEMENT au secteur dual (même ℓ^{d-1}) ⟹ C̃_T=+C_T survit ⟹ aucune lecture erronée d'un flip dual indépendant. Consolide l'item « CFT de raccordement » sans réduire le compte."
tags_epistemiques: [établi (algèbre), décision ouverte, à inventer, hors de portée]
---

# LC-D·C_T·dual-dS — Dualité de de Haro, étage S2 (dS) scellé : verdict consolidation

> **But.** `LC-WORK-CADRAGE-S2` cadre l'**étage S2** : continuer la dualité graviton-dual de de Haro
> (arXiv:0808.2054) du bulk **AdS** (S1, `LC-D-CT-DUAL`) au bulk **dS₄**, et tester l'existence d'une
> **seconde route, indépendante**, au signe de `C_T`. Ce chaînon **scelle les étapes 2-3** du cadrage
> (`§5`) via deux sceaux (`verif_D_CT_dual_dS.py`, EXIT 0 13/13 ; `verif_D_CT_gardefou_dS.py`,
> EXIT 0 14/14). L'incertitude **(i)** avait été levée au préalable (`LC-WORK-S2-LECTURE-EQ65`).
>
> **Verdict (calculé ; deux sceaux ; tout EN dS, `d=3`).**
> **[Étape 2] La carte `S` referme sur les modes dS (GO/NO-GO R1 = GO)** `[établi — algèbre]`.
> L'EOM TT de dS `f''−(2/η)f'+k²f=0` (`LC-D3-WEYL-BUNCHDAVIES`) a la **même forme** que l'EOM radiale
> AdS de de Haro `y''−(2/u)y'+y=0` : le squelette `(f_a,f_b)` se transplante sous `u→k|η|` (aucun `i`
> *dans l'équation* ; les `i` de continuation vivent dans les coefficients `C_T∝ℓ²`, `□^{3/2}∝k³`).
> `S=[[0,−1],[1,0]]`, `S²=−𝟙`, vp `±i` (éq. 51) **préservé**. Le mode de **Bunch–Davies**
> `(1−ikη)e^{ikη} = f_a − i f_b` est le **mode propre de `S` pour `+i`** (BD\* → `−i`) — la condition
> BD **diagonalise** la S-dualité ; contrôle négatif inclus.
> **[Étape 3] Le garde-fou de signe persiste en dS (lève (ii))** `[établi — algèbre ; le cœur de S2]`.
> En AdS, `C̃_T=+C_T` car le `−` relatif `W̃=−W` (éq. 61-62) est compensé par le `−2` de
> `⟨T̃⟩=−2δW̃/δh̃` (éq. 63). Sous continuation `ℓ_AdS→iℓ_dS`, la règle de `REALITE` attache `i^{d-1}`
> au **seul** préfacteur `ℓ^{d-1}` — porté **identiquement** par `C_T` et `C̃_T` (branche 1, dual
> « même forme » éq. 90) — tandis que le `−2` et le `−` relatif, **sans `ℓ`**, ne sont **pas** continués.
> Donc `i^{d-1}` **se simplifie dans le rapport** : `C̃_T/C_T=+1` est **invariant**, le garde-fou
> **persiste** (les deux réels négatifs en `d=3`). Firewall : injecter (à tort) un `i` sur le `−2`
> basculerait à `C̃_T=−C_T` (break) ⟹ résultat **sensible**, non tautologique.
>
> **Conséquence (verdict S2).** C'est la branche **(α)** du cadrage `§3` : **source unique du signe**
> (`ℓ→iℓ`), dual **confirmatoire** (pas indépendant) ⟹ **consolidation** — **pas** de seconde route,
> **pas** de réduction du compte. **Rien n'est surclassé** (§6.4) : « carte S referme + garde-fou
> persiste » est `établi (algèbre)` **GIVEN** (1) la règle de `REALITE` (scellée) et (2) l'ℓ-indépendance
> des facteurs de dictionnaire dual (lecture éq. 61-63/66) ; jamais « route acquise » (il n'y en a pas)
> ni « D1 fermé ». `[D1 non clos ; compte {A4 ; A2★ ; N} inchangé ; (A) physique conditionnel au seul
> A2★ inchangé ; CCC non démontrée]`

---

## 0. Rôle et garde-fou `[discipline §6.4]`

S2 était, dans `LC-D-CT-DUAL`, le **vrai `à inventer`** : continuer la dualité au bulk dS et trancher
si le secteur magnétique/dual livre `sign(C_T)<0` en `d=3` **indépendamment**. Ce chaînon le tranche :
**non** — le dual **confirme** le signe (source unique `ℓ→iℓ`), il ne le détermine pas par une
opération distincte. C'est un verdict de **consolidation**, `§6.4`-valide : il **resserre** la
cartographie (le signe a une source unique, le garde-fou est continuation-invariant) **sans** réduire
le périmètre irréductible `{A4 ; A2★ ; N}`.

> **Ce que ce chaînon N'EST PAS.** Il ne scelle ni « seconde route au signe » (elle n'existe pas —
> consolidation), ni l'identité tensorielle **complète** éq. 44 en dS (`□^{3/2}`, `ε`, `i^{d-1}` — le
> squelette des modes est scellé, pas le tenseur complet), ni « D1 fermé / CCC démontrée ». Il reste en
> `d=3` (parité de `ℓ^{d-1}` ; `S²=−1` en `d=3`).

---

## 1. Le résultat, en une ligne `[ce que les deux sceaux confirment]`

**La dualité de de Haro se continue en dS sans livrer de seconde route au signe de `C_T` : la carte `S`
referme (S²=−1 préservé, BD = mode propre `+i`) et le garde-fou est invariant (C̃_T=+C_T survit) ⟹
source unique du signe ⟹ consolidation.**

---

## 2. Étape 2 — la carte `S` referme sur les modes dS `[établi — algèbre ; sceau verif_D_CT_dual_dS.py, 13/13]`

**Identité de forme AdS↔dS.** EOM TT de dS : `f''−(2/η)f'+k²f=0` ⟺ (en `x=kη`) `f_xx−(2/x)f_x+f=0`.
EOM radiale AdS de de Haro : `y''−(2/u)y'+y=0`. **Même forme.** Les fonctions de mode `f_a=cos u+u sin u`,
`f_b=u cos u−sin u` (éq. 43) solvent les **deux** sous `u↔x=k|η|` (sceau, bloc [A]). Le squelette du
mode se transplante ; aucun `i` *dans l'équation*.

**`S` et `S²`.** `S=[[0,−1],[1,0]]`, `S²=−𝟙`, vp `±i` (éq. 51) reproduite (bloc [B]).

**BD diagonalise `S`.** `BD=(1−ikη)e^{ikη}=f_a−i f_b`, soit le vecteur de coefficients `(a,b)=(1,−i)`
= vecteur propre de `S` pour `+i` ⟹ `S(BD)=+i·BD` ; `BD*=f_a+i f_b` → `−i` ; contrôle négatif (mode réel
pur non propre) (bloc [C]). **GO** : la carte referme, le lead ne s'arrête pas (`hors de portée` écarté).

---

## 3. Étape 3 — le garde-fou de signe persiste en dS `[établi — algèbre ; le cœur ; sceau verif_D_CT_gardefou_dS.py, 14/14]`

**Structure AdS (rappel S1).** `⟨T⟩=+2δW/δh`, `⟨T̃⟩=−2δW̃/δh̃` (éq. 63) ; `W̃=−W` (éq. 61-62, `−`
relatif). Produit `(−2)×(−relatif)=+` ⟹ `C̃_T=+C_T` en AdS (bloc [A]).

**Continuation (REALITE).** `ℓ_AdS→iℓ_dS` attache `i^{d-1}` au **seul** préfacteur `ℓ^{d-1}` de `C_T`
(`i²=−1` en `d=3`). En branche 1 (dual « même forme » éq. 90), `C̃_T` porte la **même** puissance
`ℓ^{d-1}` ⟹ **même** `i^{d-1}`. Le `−2` (éq. 63) et le `−` relatif (éq. 61-62) ont **0 puissance de
`ℓ`** ⟹ **non continués** (bloc [B]).

**Persistance.** `i^{d-1}` se factorise identiquement sur `C_T` et `C̃_T` et **se simplifie dans le
rapport** : `C̃_T/C_T=+1` **invariant** ⟹ garde-fou **persiste** (les deux réels négatifs en `d=3`).
Mécanisme : `rapport = (defT̃·c_W̃)/(defT·c_W)`, indépendant de `i^{d-1}` (bloc [C]).

**Firewall (injection d'erreur).** Un break exigerait que le `−2` *ou* le `−` relatif acquière un
`i^{d-1}` : le rapport basculerait à `−1` (`C̃_T=−C_T`). Le sceau vérifie `break(−1)≠persistance(+1)`
⟹ le résultat est **sensible** et **pourrait échouer** ; il ne le fait pas car le `−2` vient du
dictionnaire de Legendre (éq. 66), sans `ℓ` (bloc [D]).

---

## 4. Verdict S2 et résidus `[consolidation — §6.4]`

**Verdict : consolidation (branche α du cadrage §3).** Le signe de `C_T` a une **source unique**
(`ℓ→iℓ`) ; le secteur dual le **confirme** (même `i^{d-1}`) au lieu de le déterminer par une opération
indépendante. **Pas de seconde route** ⟹ **pas de réduction du compte**. Cohérent avec
`LC-WORK-S2-LECTURE-EQ65` (branche 2 `∝ℓ^{−2}` → `i^{−2}=−1`, aussi réel négatif, non indépendante) :
les **deux** branches retombent sur la source unique.

**Résidus explicitement délimités** `[NON scellés]` :
- **`décision ouverte`** — validité **physique** de l'ℓ-indépendance des facteurs duaux sous
  continuation dS **complète** : la structure de Legendre (éq. 66) se continue-t-elle sans injecter de
  `ℓ`-dépendance dans le `−2` / le `−` relatif ? Aucune indication de break ; non scellé.
- **`à inventer`** — identité tensorielle **complète** éq. 44 en dS (`□^{3/2}`, `ε`, `i^{d-1}` ; le
  squelette des modes est scellé, pas le tenseur intégral).
- **`décision ouverte`** — **question 3** (Dirichlet vs duale = raccordement, R2) **non déclenchée** :
  elle ne l'était que « si 1–4 livrent une route propre » (cadrage `§5.5`) ; le verdict étant
  consolidation, elle reste ouverte sur l'item « CFT de raccordement » (`LC-D-HOLOGRAPHIE-G3 §3`, dont
  la CFT duale demeure un candidat de structure).

---

## 5. Format de chaînon

- **Type** : résultat (scelle S2/dS, étapes 2-3 ; deux sceaux). **Statut** : `établi (algèbre)` GIVEN
  intrants (1)+(2) ; verdict consolidation. **Sceaux** : `verif_D_CT_dual_dS.py` (13/13),
  `verif_D_CT_gardefou_dS.py` (14/14, firewall). Stack : Python 3.12 / sympy 1.14 / numpy 2.4.
- **Ne touche aucun chaînon existant** : algèbre `DUAL` (S1), `REALITE`, `ATN`, `NONLIN-VERROU` intacte.
- **Réexécution** : les deux sceaux sont re-exécutables, EXIT 0.

---

## 6. Propagation / housekeeping `[à appliquer — note de reprise séparée ; NON exécutée ici]`

Additif uniquement (`str_replace`, ancres `count==1`, contrôle de delta ; suppressions limitées à
`{version, maj}`). À présenter pour validation avant dépôt. Cibles :
- **`LC-00-INDEX`** : enregistrer `LC-D-CT-DUAL-DS v0.1` (+ sceaux) ; ligne carte ajoutée.
- **`LC-D-CT-DUAL`** (§Conséquence-pour-S2) : note additive « S2 tranché : consolidation (source
  unique du signe) ; carte S referme en dS, garde-fou persiste ; pas de seconde route ».
- **`LC-WORK-CADRAGE-S2`** : addendum « (i) levée ; étapes 2-3 faites ; verdict consolidation ».
- **`LC-D-CT-REALITE`** : renvoi « la continuation i^{d-1} se propage identiquement au dual ⟹ garde-fou
  invariant (LC-D-CT-DUAL-DS) ».
- **`LC-D-HOLOGRAPHIE-G3 §3`** : item « CFT de raccordement » — la CFT duale en reste candidat ;
  question 3 ouverte.
- **`LC-AUDIT-VERDICT §8bis`** : journaliser le verdict S2 (consolidation), **sans surclassement**.
- **`03_glossaire`, `02_programme`** : entrées S2/dS. `04_references` : de Haro 0808.2054 DÉJÀ en KB.

*(Aucune de ces touches ne change le compte `{A4 ; A2★ ; N}` ni un statut physique.)*

---

## 7. Renvois, glossaire, références

- **Prérequis** : `LC-D-CT-DUAL` (S1/AdS), `LC-D-CT-REALITE` (continuation `i^{d-1}`),
  `LC-D3-WEYL-BUNCHDAVIES` (modes BD, `E_ij=(d/2H)g₃`), `LC-WORK-CADRAGE-S2`, `LC-WORK-S2-LECTURE-EQ65`.
- **Source** : de Haro, arXiv:0808.2054 (`JHEP 01 (2009) 042`) — éq. 43-44, 50-51, 61-63, 65, 90 ;
  pages 14, 16, 20. DÉJÀ en KB (`04_references`).
- **Glossaire** : S-dualité ; garde-fou de signe ; source unique du signe ; consolidation vs réduction.

---

## Appendice — Légende des tags épistémiques

`établi (algèbre)` = l'algèbre est correcte et les cibles reproduites (jamais « physique CCC établie »,
§6.4). `décision ouverte` = choix/validation non tranché. `à inventer` = construction non faite.
`hors de portée` = hors des moyens actuels. **S2 = `établi (algèbre)` (consolidation) GIVEN intrants
(1)+(2) ; résidus `décision ouverte` / `à inventer` délimités au §4.**
