---
id: LC-D-CT-DUAL
titre: "Module D / dS-CFT — LEAD « DUALITÉ GRAVITON-DUAL DE DE HARO » (arXiv:0808.2054, AdS4/CFT3, Cotton holographique), ÉTAGE S1 : reproduction EN AdS et ÉPINGLAGE DES CONVENTIONS, AVANT continuation dS (= S2, NON couvert). Exécute la recommandation principale de LC-WORK-REPRISE-POST-CT-REALITE §4 (« seconde route, indépendante, au signe/réalité de C_T via le secteur magnétique B=Cotton »). Ce chaînon SCELLE (verif_D_CT_dual.py, EXIT 0, 18 asserts, 3 blocs) : [A] DUALITÉ DES EOM — sur la solution physique TT (de Haro éq. 43, f_a=cos u+u sin u, f_b=u cos u−sin u, u=|p|r), l'identité de 3e dérivée (éq. 44) referme sur les MÊMES deux fonctions avec échange de coefficients S:(a,b)↦(−b,a) ⟹ S=[[0,−1],[1,0]], S²=−𝟙 (éq. 51), valeurs propres ±i ; contrôle négatif (sans échange, l'identité tombe) ; [B] GARDE-FOU DE SIGNE (le cœur) — W=+ℓ²/8κ²∫h₀□^{3/2}h₀ (éq. 61) et W̃=−ℓ²/8κ²∫h̃₀□^{3/2}h̃₀ (éq. 62) portent un `−` relatif RÉEL, MAIS ⟨T⟩=2δW/δh tandis que ⟨T̃⟩=−2δW̃/δh̃ (éq. 63, `−2` explicite) ⟹ dérivé symboliquement, ⟨T̃T̃⟩ a le MÊME signe que ⟨TT⟩ ⟹ C̃_T=+C_T EN AdS : la dualité AdS NE FLIPPE PAS C_T (le `−` de W̃ est compensé) ⟹ tout flip viendra de la continuation dS (i^{d-1}, déjà scellé LC-D-CT-REALITE) et/ou de S²=−1 (vp ±i), pas de la dualité AdS ; [C] DICTIONNAIRE — éq. (1) de de Haro ⟨T⟩=(d/16πG)g₃ = dictionnaire programme (identité, d=3) ; C_T=coeff de |p|³Π=ℓ²/κ² (éq. 90) ∝ℓ²/G∝N (ℓ_dS=1/H, N=π/GH²) ; C_T/N=nombre PUR (verrouillage, H,G,k se simplifient) ; valeur nue de Haro 1/(8π²) vs scellée programme 1/(32π²) reliées par un FACTEUR DE CONVENTION fixe =4 (normalisation de Π + préfacteurs), figé et NON caché. SANS SURCLASSEMENT (§6.4) : S1 est EN AdS ; algèbre de de Haro reproduite + conventions épinglées, JAMAIS « seconde route au signe acquise » (c'est S2), ni « D1 fermé / CCC établie ». À INVENTER (S2, NON couvert) : continuation dS de la dualité ; le secteur magnétique/dual livre-t-il sign(C_T)<0 en d=3 INDÉPENDAMMENT, et S²=−1 porte-t-il le i² structurellement ? quelle CFT (Dirichlet vs duale) joue 'raccordement' ? Le compte {A4 ; A2★ ; N} INCHANGÉ ; D1 NON clos ; (A) physique conditionnel au seul A2★ INCHANGÉ."
codename: LC-RACCORD
tags: [module-D, ds-cft, dualite, graviton-dual, de-haro, cotton-york, electrique-magnetique, S-dualite, chern-simons, legendre, charge-centrale, C_T, signe, garde-fou, dictionnaire, verrouillage, N-holographique, adS-vs-dS, S1, sceau, D1]
type: chaînon (résultat — scelle l'ÉTAGE S1 du lead dualité de de Haro : reproduction AdS + conventions + garde-fou de signe ; exécute la reco principale de LC-WORK-REPRISE-POST-CT-REALITE §4 ; SCEAU FAIT verif_D_CT_dual.py)
statut: "établi (algèbre), SCEAU FAIT — S1 EN AdS SEULEMENT. [A] dualité des EOM de de Haro reproduite (éq. 43-44) ; S=[[0,−1],[1,0]], S²=−𝟙, vp ±i (éq. 51) ; contrôle négatif. [B] GARDE-FOU : sign(C̃_T)=sign(C_T) en AdS malgré sign(W̃)=−sign(W) (le `−` de W̃ compensé par le `−2` de ⟨T̃⟩, éq. 63) ⟹ la dualité AdS ne flippe pas C_T. [C] dictionnaire C_T↔ℓ²/κ²↔N reproduit (éq. 1, 90) ; C_T/N nombre pur (verrouillage) ; facteur de convention deHaro/programme =4, figé. À inventer / NON couvert (S2) : continuation dS de la dualité ; seconde route au signe (secteur magnétique/dual) ; rôle de S²=−1 dans le i² ; CFT de raccordement = Dirichlet ou duale. SANS SURCLASSEMENT (§6.4) : S1 en AdS, algèbre reproduite, JAMAIS « seconde route acquise ». D1 NON clos ; compte {A4 ; A2★ ; N} inchangé."
statut_id: "validé après sceau (verif_D_CT_dual.py déposé en KB, EXIT 0, 18 asserts) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §6) : LC-D-CT-REALITE §renvoi (S1 pose la base AdS de la 2e route), LC-D-NONLIN-VERROU §renvoi (même décomposition E/B, niveau deux-point vs un-point), LC-D-HOLOGRAPHIE-G3 §3, LC-AUDIT-VERDICT §8bis, LC-00-INDEX, 03_glossaire, 02_programme, 04_references (de Haro 0808.2054 DÉJÀ en KB)."
version: 0.7
langue: fr
date: 2026-06-09
maj: "2026-06-12 — v0.7 : RENVOI ADDITIF (petit front c_B — LC-D-CB-WEYL-MAGNETIQUE v0.1, sceau verif_cb_weyl_magnetique.py EXIT 0/26, sha256 e1bef559…344f ; cadrage LC-WORK-CADRAGE-CB v0.1, R-7 tenue). La décision ouverte cataloguée au §7 (épinglage de c_B en unités programme, R-11) est LEVÉE PAR DÉRIVATION : c_B = 1/H exact, dérivé de la définition du Weyl rescalé (jamais posé), signe compris (même ε pour B̂=½εĈ et le Cotton ab initio). Équipartition ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ exacte AUSSI en unités programme (couple 𝓔=(3/2H)g₃ | 𝓑=(1/H)C[g₀]) ; refermeture dH (49)/(50) slack nul. Note datée ajoutée au §7 ; l'énoncé « en unités de dualité » reste vrai tel qu'écrit (levée par dérivation, pas par suppression). Aucune touche algèbre ni sceaux ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos. | 2026-06-12 — v0.6 : RENVOIS ADDITIFS (lot de propagation NONLIN-2PT — LC-D-NONLIN-2PT v0.1, sceau verif_nonlin_deuxpoint.py EXIT 0/41 ; audité à froid 4/4 ACQUIS, LC-AUDIT-LOG-NONLIN-2PT v0.1). (i) §2 : D²=−𝟙 du chaînon rang 2 (construit ab initio sur (𝓔,𝓑), phase 1 isolée EXIT 0/27) RECOUPE INDÉPENDAMMENT le S²=−𝟙 scellé ici (autre route, même involution ±i). (ii) §7 : équipartition ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ exacte EN UNITÉS DE DUALITÉ (dH 49/50) — scoping R-11 attaché (2e convention dH p.14 ⟹ scoping nécessaire) ; épinglage de c_B en unités programme (attendu 1/H, à dériver, jamais à poser) = décision ouverte cataloguée. (iii) §7 : corroborations EXCÉDENTAIRES de l'audit consignées — dH (121) recoupe indépendamment le Cotton (i/2)k³ ; dH (90) exhibe C1+C2 dans la source même (pair k³Π radiatif + impair Chern-Simons contact). Aucune touche algèbre ni sceaux ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos. | 2026-06-11 — v0.5 : RENVOI ADDITIF (propagation map opérateur γ, LC-D-CT-GAMMA v0.1) — le PRODUIT =4 du facteur de convention (§4) est NOMMÉ comme la map opérateur canonique γ_canonique=⟨TT⟩_canon/ψ₂=8c_W/2c_W=4, dérivée ab initio et tranchée (sceau verif_naction_gamma_dHSS.py EXIT 0 18 asserts). Les deux 2 (préfacteurs W↔⟨TT⟩) = deux applications de T=2δW/δg (Brown-York) ; N_action=γ/4 (canonique γ=4→1, C_T^prog=C_T^dH ; nu γ=1→1/4, convention). Part « norm. de Π »=1 et PRODUIT =4 INCHANGÉS ; renvoi de nommage seulement. Note datée ajoutée au §4. Aucune touche à l'algèbre S1 ni au sceau verif_D_CT_dual.py. SANS SURCLASSEMENT (§6.4) ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos. (cf. LC-D-CT-GAMMA) | 2026-06-10 — v0.4 : RENVOI ADDITIF (propagation route α∪R-2, LC-AUDIT-LOG-NACTION-ALPHA v1.0) — PRÉCISION D'ATTRIBUTION du facteur de convention =4 (§4) : le calcul explicite (sceau verif_naction_alpha.py, de Haro éq.119 Appendix C.2 ≡ PiTT, 81 comp.) montre que la part « normalisation du projecteur Π » vaut 1 (Π de Haro = projecteur unité, identique au programme) ⟹ tout le facteur 4 est dans les préfacteurs W↔⟨TT⟩ (les deux 2 de l'éq.63 : ⟨T⟩=2δW/δh, ⟨TT⟩=2δ⟨T⟩/δh, sur C_T^dH=8c_W vs lecture programme C_T^prog=2c_W). Le PRODUIT =4 et l'algèbre S1 sont INCHANGÉS ; seule la décomposition verbale du §4 est précisée. Note datée ajoutée au §4. SANS SURCLASSEMENT (§6.4) ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos. | 2026-06-10 — v0.3 : RENVOI ADDITIF (propagation) — l'étage S2 (continuation dS) est scellé dans LC-D-CT-DUAL-DS v0.1 (sceaux verif_D_CT_dual_dS.py 13/13 + verif_D_CT_gardefou_dS.py 14/14, firewall). Verdict S2 : CONSOLIDATION — la carte S referme sur les modes BD (S²=−1 préservé, BD=mode propre +i) et le garde-fou persiste (C̃_T=+C_T survit, i^{d-1} porté identiquement) ⟹ source unique du signe, PAS de seconde route indépendante. Note datée ajoutée au blockquote « Conséquence pour S2 ». Aucune touche à l'algèbre S1 ni au sceau verif_D_CT_dual.py. SANS SURCLASSEMENT (§6.4) ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos. | 2026-06-09 — v0.2 : ERRATUM bibliographique — référence de Haro corrigée « JHEP 11 (2008) 059 » → « JHEP 01 (2009) 042 » (§7 ; alignée sur 04-REFERENCES v1.10, web-vérifiée) ; aucune touche à l'algèbre ni au sceau. | 2026-06-09 — v0.1 : scelle l'ÉTAGE S1 du lead « dualité graviton-dual de de Haro » (reco principale de LC-WORK-REPRISE-POST-CT-REALITE §4). verif_D_CT_dual.py (EXIT 0, 18 asserts, 3 blocs) : [A] dualité des EOM (éq. 43-44) referme avec échange S:(a,b)↦(−b,a) ⟹ S²=−𝟙, vp ±i (éq. 51) ; contrôle négatif inclus ; [B] garde-fou de signe — W̃=−W (éq. 61-62) MAIS ⟨T̃⟩=−2δW̃/δh̃ (éq. 63) ⟹ C̃_T=+C_T en AdS (dualité AdS ne flippe pas C_T) ; [C] dictionnaire C_T↔ℓ²/κ²↔N (éq. 1, 90), C_T/N nombre pur, facteur de convention =4 figé. SANS SURCLASSEMENT (§6.4) : S1 en AdS ; algèbre reproduite + conventions épinglées, JAMAIS « 2e route au signe acquise » (S2) ni « D1 fermé ». Aucune touche aux chaînons existants (algèbre ATN/REALITE/NONLIN-VERROU intacte). Propagation §6 NON exécutée (proposée, lot séparé)."
fichier_compagnon: verif_D_CT_dual.py
prerequis_kb: [LC-D-CT-ATN, LC-D-CT-REALITE, LC-D-NONLIN-VERROU, LC-D-HOLOGRAPHIE-G3, LC-E-PLANCK-RESIDUEL, LC-D3-SPECTRE-K3, LC-AUDIT-VERDICT, LC-WORK-REPRISE-POST-CT-REALITE, LC-00-INDEX]
fichiers_compagnons_kb: [verif_D_CT_ATN.py, verif_D_CT_realite.py, verif_E_planck.py, verif_nonlin_cotton.py]
renvois: [LC-D-CT-ATN, LC-D-CT-REALITE, LC-D-NONLIN-VERROU, LC-D-HOLOGRAPHIE-G3, LC-E-PLANCK-RESIDUEL, LC-D3-SPECTRE-K3, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-WORK-REPRISE-POST-CT-REALITE, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[D] holographie / dS-CFT — pose la base AdS de la dualité électrique/magnétique de de Haro (E∝g₃∝⟨T⟩ ; B∝Cotton ; S²=−1 ; W̃=−W) au niveau du DEUX-POINT (où vit C_T), prélude à une 2e route au signe ; reproduit le dictionnaire C_T↔ℓ²/κ²↔N. Ne tranche aucune physique ; S2 (dS) à inventer."
  - "[D] / front (a) — relie le secteur électrique E∝g₃ (déjà LC-D-NONLIN-VERROU au UN-POINT) à son enveloppe DEUX-POINT (C_T) ; le garde-fou de signe protège LC-D-CT-REALITE d'une lecture erronée du `−` dual."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·C_T·dual — Dualité graviton-dual de de Haro, étage S1 (AdS) scellé

> **But.** `LC-WORK-REPRISE-POST-CT-REALITE §4` recommande la **dualité graviton-dual de de Haro**
> (arXiv:0808.2054) comme lead le plus pointu : une **seconde route, indépendante**, au signe/réalité
> de `C_T`, via le secteur **magnétique** `B=Cotton`. Le travail est découpé en deux étages —
> **S1** (reproduction **en AdS** + épinglage des conventions, **risque faible**) puis **S2**
> (continuation dS, le vrai `à inventer`). **Ce chaînon scelle S1 uniquement** (`verif_D_CT_dual.py`,
> EXIT 0, 18 asserts).
>
> **Verdict (calculé, `verif_D_CT_dual.py`, EXIT 0 ; 3 blocs — tout EN AdS).**
> **[A] Dualité des EOM, `S²=−𝟙`** `[établi — algèbre]`. Sur la solution physique TT (éq. 43),
> l'identité de 3e dérivée (éq. 44) referme sur les **mêmes** deux fonctions avec échange de
> coefficients `S:(a,b)↦(−b,a)` ⟹ `S=[[0,−1],[1,0]]`, `S²=−𝟙` (éq. 51), valeurs propres `±i`.
> Contrôle négatif : sans l'échange, l'identité tombe (`S` est bien l'involution non triviale).
> **[B] Garde-fou de signe** `[établi — algèbre ; le cœur de S1]`. `W=+ℓ²/8κ²∫h₀□^{3/2}h₀` (éq. 61)
> et `W̃=−ℓ²/8κ²∫h̃₀□^{3/2}h̃₀` (éq. 62) portent un `−` relatif **réel**, **mais** `⟨T⟩=2δW/δh`
> tandis que `⟨T̃⟩=−2δW̃/δh̃` (éq. 63, `−2` **explicite**). Dérivé symboliquement : `⟨T̃T̃⟩` a le
> **même signe** que `⟨TT⟩` ⟹ **`C̃_T=+C_T` EN AdS**. La dualité AdS **ne flippe pas** `C_T` — le
> `−` de `W̃` est **compensé**.
> **[C] Dictionnaire `C_T↔ℓ²/κ²↔N`** `[établi — algèbre]`. Éq. (1) de de Haro `⟨T⟩=(d/16πG)g₃` =
> dictionnaire programme (identité ; `d=3`). `C_T=`coeff de `|p|³Π = ℓ²/κ²` (éq. 90) `∝ℓ²/G∝N`
> (`ℓ_dS=1/H`, `N=π/GH²`) ; `C_T/N` est un **nombre pur** (verrouillage). Valeur nue de de Haro
> `1/(8π²)` vs scellée programme `1/(32π²)` : **facteur de convention fixe `=4`** (normalisation de
> `Π` + préfacteurs), **figé et non caché**.
>
> **Conséquence pour S2.** Le signe négatif de `C_T` ne peut venir **que** de la continuation dS
> (`i^{d-1}`, déjà scellé `LC-D-CT-REALITE`) et/ou de `S²=−1` (vp `±i`, moteur candidat du `i²`
> **structurel**). **Rien n'est surclassé** (§6.4) : S1 est **en AdS** ; aucune « seconde route au
> signe » n'est acquise — c'est S2. `[D1 non clos ; compte {A4 ; A2★ ; N} inchangé ; (A) physique
> conditionnel au seul A2★ inchangé]`
>
> **[Mis à jour 2026-06-10 — S2 tranché.]** L'étage S2 (continuation dS) est scellé dans
> `LC-D-CT-DUAL-DS` v0.1 (sceaux `verif_D_CT_dual_dS.py` 13/13 + `verif_D_CT_gardefou_dS.py` 14/14,
> firewall) : la carte `S` referme sur les modes BD de dS (`S²=−1` préservé, BD `= f_a−i f_b` = mode
> propre `+i`) et le garde-fou **persiste** (`C̃_T=+C_T` survit ; `i^{d-1}` porté identiquement par
> `C_T` et `C̃_T`). **Verdict : consolidation** — source **unique** du signe (`ℓ→iℓ`), dual
> **confirmatoire**, **pas** de seconde route indépendante, **pas** de réduction du compte
> `{A4 ; A2★ ; N}`. `[établi (algèbre) GIVEN REALITE + ℓ-indépendance des facteurs duaux ; résidus
> décision ouverte au §4 de LC-D-CT-DUAL-DS]`

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce chaînon **scelle l'algèbre** d'une **reproduction en AdS** et **épingle les conventions** ; il ne
tranche aucune physique de la CCC et ne franchit pas la continuation dS. Ce qui est
`établi (algèbre)` : les trois blocs `[A][B][C]`, tous reproduits par `verif_D_CT_dual.py`. Ce qui
reste `à inventer` (S2, **non couvert**) : la continuation dS de la dualité ; la question de savoir
si le secteur magnétique/dual livre `sign(C_T)<0` en `d=3` **indépendamment** du `|p|³` électrique ;
si `S²=−1` porte le `i²` **structurellement** ; et laquelle des deux CFT (Dirichlet vs duale) joue
le « raccordement ». Discipline `LC-AUDIT-VERDICT §6.4` : un `établi` de sceau atteste que **l'algèbre
est correcte et les cibles de de Haro reproduites**, jamais « la seconde route au signe est acquise »
ni « la physique de la CCC est établie ».

**Statut adossé (aucun sceau neuf au-delà de celui-ci).** Décomposition électrique/magnétique
`E∝g₃∝⟨T⟩` (pair) / `B∝Cotton[g₀]` (impair) au **un-point** (`LC-D-NONLIN-VERROU`,
`verif_nonlin_cotton.py`) ; verrouillage `C_T∝N` en magnitude, `C_T/N=1/(32π²)` (`LC-D-CT-ATN`) ;
route électrique du signe `i^{d-1}`, `d=3` réel négatif (`LC-D-CT-REALITE`) ; `N=S_dS`
(`verif_E_planck.py`). **Aucune de ces algèbres n'est touchée** — S1 les **prolonge** au deux-point
et **les protège** (garde-fou `[B]`).

---

## 1. Le résultat, en une ligne `[ce que le sceau confirme]`

S1 reproduit la dualité de de Haro **en AdS** et en tire un fait de conventions **non trivial** :

$$\boxed{\;S^2=-\mathbb 1\ (\text{vp }\pm i),\qquad
\underbrace{\operatorname{sign}\widetilde W=-\operatorname{sign}W}_{\text{éq. 61–62}}
\ \ \text{MAIS}\ \
\underbrace{\operatorname{sign}\widetilde C_T=+\operatorname{sign}C_T}_{\text{AdS, éq. 63}},
\qquad C_T\propto\frac{\ell^2}{\kappa^2}\propto N\ (\tfrac{C_T}{N}\ \text{pur}).\;}$$

La dualité AdS **ne flippe pas** `C_T` (le `−` de `W̃` est compensé par le `−2` de la définition
duale). Donc le `C_T<0` dont la CCC a besoin **ne peut pas** être un simple artefact de la dualité
AdS : il faut **la continuation dS** et/ou **`S²=−1`** — c'est exactement le périmètre de S2.

---

## 2. Dualité des équations de mouvement et `S²=−1` `[établi — algèbre]`

La solution physique (transverse-sans-trace) du graviton de bulk en AdS₄ s'écrit (de Haro éq. 43,
`u=|p|r`) :

$$\bar h_{ij}[a,b]=a_{ij}(p)\,\underbrace{(\cos u+u\sin u)}_{f_a}
+\,b_{ij}(p)\,\underbrace{(u\cos u-\sin u)}_{f_b}.$$

Le tenseur de Cotton ayant **dimension 3**, on le compare à la **troisième dérivée radiale**. Par
inspection (éq. 44) :

$$\frac{d^3}{dr^3}\,\bar h_{ij}[-b,a]=|p|^3\,\bar h_{ij}[a,b]-\frac{3|p|}{r}\,\bar h'_{ij}[a,b]
\qquad(\text{vérifié : } \mathrm{diff}=0\ \text{symbolique}).$$

L'opération referme donc sur les **mêmes** deux fonctions, avec **échange de coefficients**
`S:(a,b)↦(−b,a)`, soit la matrice

$$S=\begin{pmatrix}0&-1\\[1mm]1&0\end{pmatrix},\qquad S^2=-\mathbb 1\quad(\text{éq. 51}),
\qquad \text{valeurs propres }\pm i.$$

Ceci est la dualité électrique-magnétique de de Haro **au niveau des EOM** (valable à tout rayon `r`,
pas seulement au bord) : `S(E)=B`, `S(B)=−E`, avec `E` = tenseur de stress renormalisé (`∝g₃`) et
`B` = tenseur de Cotton. **Contrôle négatif** scellé : sans l'échange, l'identité (44) **ne tient
pas** — `S` est bien l'**involution non triviale** (et non l'identité, qui donnerait `S²=+1`). Les
valeurs propres `±i` sont le **moteur candidat** d'un `i` du côté magnétique — mais leur effet sur
le **signe de `C_T`** est une question de S2 (continuation), pas de S1.

**Recoupement indépendant (2026-06-12, `LC-D-NONLIN-2PT` v0.1, audité 4/4 ACQUIS).** Le
chaînon rang 2 construit **ab initio** (sceau autonome `verif_nonlin_deuxpoint.py`, phase 1
exécutable en isolation EXIT 0/27) l'opérateur de dualité `D` sur le couple `(𝓔,𝓑)` du
Weyl rescalé et obtient `D²=−𝟙` — recoupant **indépendamment** le `S²=−𝟙` scellé ici
(autre route, autre objet de départ, même structure d'involution non triviale à valeurs
propres `±i`).

---

## 3. Le garde-fou de signe : la dualité AdS ne flippe pas `C_T` `[établi — algèbre ; le cœur]`

C'est le résultat le plus utile de S1, et le motif du **nugget P1** (objet structurel signé `≠`
observable). Les deux fonctionnelles génératrices (éq. 61–62) portent un signe **opposé** :

$$W[h]=+\frac{\ell^2}{8\kappa^2}\!\int\! h_{(0)}\,\Box^{3/2}h_{(0)},\qquad
\widetilde W[\tilde h]=-\frac{\ell^2}{8\kappa^2}\!\int\! \tilde h_{(0)}\,\Box^{3/2}\tilde h_{(0)}.$$

Le `−` relatif est **réel** (engendré par la transformation de Legendre = terme de Chern-Simons
gravitationnel, éq. 58–60). On pourrait être tenté de lire ce `−` comme un flip de `C_T`. **C'est
faux** : la **définition du tenseur dual porte elle-même un `−2`** (éq. 63), là où la définition
directe porte `+2` :

$$\langle T\rangle=2\,\frac{\delta W}{\delta h}\ \Rightarrow\ \langle TT\rangle\propto+\,\Box^{3/2},
\qquad
\langle \tilde T\rangle=-2\,\frac{\delta \widetilde W}{\delta \tilde h}\ \Rightarrow\
\langle \tilde T\tilde T\rangle\propto +\,\Box^{3/2}.$$

Dérivé symboliquement (sceau) : `⟨T̃T̃⟩` a le **même signe** que `⟨TT⟩`, et de fait le **même
coefficient** — exactement ce que de Haro annonce (éq. 90 : *« the dual two-point function takes the
same form »*). Donc **en AdS** :

$$\boxed{\ \operatorname{sign}\widetilde C_T=+\operatorname{sign}C_T\ \ (\text{AdS}),\qquad
\text{le `−` de }\widetilde W\ \text{est compensé par le `−2` de }\langle\tilde T\rangle.\ }$$

**Conséquence (la valeur du garde-fou).** Le `C_T<0` de la CCC **ne peut pas** provenir de la dualité
AdS seule. Les **seuls** moteurs candidats du signe sont (i) la **continuation dS** `ℓ^2_{AdS}\to
-\ell^2_{dS}` (facteur `i^{d-1}`, `d=3` réel négatif — **déjà scellé** `LC-D-CT-REALITE`), et (ii)
`S^2=-1` (vp `±i`). S1 **élimine** un troisième candidat erroné (le `−` dual) et **protège**
`LC-D-CT-REALITE` d'une lecture qui aurait compté deux fois le signe.

<svg width="100%" viewBox="0 0 700 560" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>S1 : la dualité AdS ne flippe pas C_T ; le signe vient de la continuation dS et/ou de S²=−1 (S2)</title>
  <desc>En haut, secteur AdS établi (vert). La S-dualité des équations de mouvement donne S au carré égale moins un, valeurs propres plus et moins i. Les deux fonctionnelles génératrices W et W tilde ont des signes opposés (moins relatif réel). Mais la définition du tenseur de stress direct porte plus deux et la définition duale porte moins deux ; en conséquence les deux fonctions à deux points ont le même signe, donc C_T tilde égale plus C_T en AdS : la dualité AdS ne flippe pas C_T, le moins de W tilde est compensé. À droite, le dictionnaire : C_T égale ell carré sur kappa carré, proportionnel à ell carré sur G, proportionnel à N ; le rapport C_T sur N est un nombre pur ; facteur de convention de Haro sur programme égale quatre. En bas, séparé par une ligne de démarcation, le domaine S2 à inventer (orange) : la continuation dS attache i puissance d moins un, en d égale trois réel négatif ; et S au carré égale moins un est le moteur candidat du i au carré structurel ; ce sont les seuls moteurs du signe négatif. Question ouverte S2 : quelle CFT, Dirichlet ou duale, joue le raccordement.</desc>
  <defs><marker id="ard" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="#534AB7" stroke-width="1.5"/></marker></defs>
  <text x="20" y="26" font-size="12.5" font-weight="600" fill="#0F6E56">S1 — secteur AdS (établi, algèbre)</text>
  <rect x="20" y="38" width="300" height="46" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="170" y="60" text-anchor="middle" font-size="12.5" fill="#0F6E56">S-dualité des EOM (éq. 43-44)</text>
  <text x="170" y="77" text-anchor="middle" font-size="12" font-weight="500" fill="#0F6E56">S² = −𝟙   ·   vp ±i</text>
  <rect x="20" y="100" width="145" height="60" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="92" y="123" text-anchor="middle" font-size="12" fill="#0F6E56">W = +ℓ²/8κ²·…</text>
  <text x="92" y="140" text-anchor="middle" font-size="11" fill="#0F6E56">⟨T⟩ = +2 δW/δh</text>
  <text x="92" y="154" text-anchor="middle" font-size="10.5" fill="#73726c">(éq. 61)</text>
  <rect x="175" y="100" width="145" height="60" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="247" y="123" text-anchor="middle" font-size="12" fill="#0F6E56">W̃ = −ℓ²/8κ²·…</text>
  <text x="247" y="140" text-anchor="middle" font-size="11" fill="#0F6E56">⟨T̃⟩ = −2 δW̃/δh̃</text>
  <text x="247" y="154" text-anchor="middle" font-size="10.5" fill="#73726c">(éq. 62-63, −2 explicite)</text>
  <line x1="92" y1="160" x2="150" y2="192" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ard)"/>
  <line x1="247" y1="160" x2="190" y2="192" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ard)"/>
  <rect x="20" y="194" width="300" height="58" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="1.1"/>
  <text x="170" y="216" text-anchor="middle" font-size="12.5" font-weight="600" fill="#0F6E56">⟨TT⟩ et ⟨T̃T̃⟩ : MÊME signe</text>
  <text x="170" y="234" text-anchor="middle" font-size="12" fill="#0F6E56">⟹ C̃_T = +C_T  (AdS)</text>
  <text x="170" y="248" text-anchor="middle" font-size="10.5" fill="#0F6E56">garde-fou : le `−` de W̃ est compensé</text>
  <rect x="372" y="100" width="306" height="152" rx="8" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.6"/>
  <text x="525" y="124" text-anchor="middle" font-size="12.5" font-weight="600" fill="#0F6E56">Dictionnaire (éq. 1, 90)</text>
  <text x="525" y="150" text-anchor="middle" font-size="12.5" fill="#0F6E56">⟨T⟩ = (d/16πG) g₃  ≡ programme</text>
  <text x="525" y="174" text-anchor="middle" font-size="12.5" fill="#0F6E56">C_T = ℓ²/κ² ∝ ℓ²/G ∝ N</text>
  <text x="525" y="198" text-anchor="middle" font-size="12.5" fill="#0F6E56">C_T/N = nombre pur (verrouillage)</text>
  <text x="525" y="224" text-anchor="middle" font-size="11.5" fill="#0F6E56">facteur de convention deHaro/prog = 4</text>
  <text x="525" y="242" text-anchor="middle" font-size="10.5" fill="#73726c">1/(8π²)  vs  1/(32π²) — figé, non caché</text>
  <line x1="14" y1="288" x2="686" y2="288" stroke="#888780" stroke-width="0.7" stroke-dasharray="5 4"/>
  <text x="20" y="282" font-size="11" fill="#73726c">démarcation S1 (AdS, établi) ▲  /  S2 (continuation dS, à inventer) ▼</text>
  <text x="20" y="312" font-size="12.5" font-weight="600" fill="#993C1D">S2 — seuls moteurs candidats du signe négatif (à inventer)</text>
  <rect x="20" y="326" width="320" height="64" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="180" y="350" text-anchor="middle" font-size="12.5" font-weight="500" fill="#993C1D">continuation dS  ℓ²_AdS → −ℓ²_dS</text>
  <text x="180" y="370" text-anchor="middle" font-size="12" fill="#993C1D">i^(d−1) ;  d=3 → réel négatif</text>
  <text x="180" y="385" text-anchor="middle" font-size="10.5" fill="#993C1D">(déjà scellé : LC-D-CT-REALITE)</text>
  <rect x="358" y="326" width="320" height="64" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="0.6"/>
  <text x="518" y="350" text-anchor="middle" font-size="12.5" font-weight="500" fill="#993C1D">S² = −1  (vp ±i)</text>
  <text x="518" y="370" text-anchor="middle" font-size="12" fill="#993C1D">moteur candidat du i² structurel</text>
  <text x="518" y="385" text-anchor="middle" font-size="10.5" fill="#993C1D">(secteur magnétique / dual — S2)</text>
  <line x1="180" y1="390" x2="300" y2="430" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ard)"/>
  <line x1="518" y1="390" x2="398" y2="430" stroke="#534AB7" stroke-width="1.5" marker-end="url(#ard)"/>
  <rect x="160" y="432" width="378" height="58" rx="8" fill="#FAECE7" stroke="#D85A30" stroke-width="1.0"/>
  <text x="349" y="455" text-anchor="middle" font-size="12.5" font-weight="600" fill="#993C1D">2e route au signe de C_T ?  (objectif S2)</text>
  <text x="349" y="474" text-anchor="middle" font-size="11" fill="#993C1D">+ quelle CFT joue 'raccordement' : Dirichlet vs duale ?</text>
  <text x="20" y="524" font-size="11" fill="#73726c">vert = établi (algèbre, AdS) · orange = à inventer (S2, dS) · pointillé = démarcation S1/S2</text>
  <text x="20" y="542" font-size="11" fill="#73726c">S1 élimine un 3e candidat ERRONÉ (le `−` dual) et protège LC-D-CT-REALITE d'un double comptage du signe.</text>
</svg>

*Fig. — Architecture S1/S2. En haut (vert) : le secteur AdS établi — `S²=−1`, et le garde-fou
`C̃_T=+C_T` malgré `W̃=−W`. En bas (orange) : les **deux seuls** moteurs candidats du signe négatif,
réservés à S2 (la continuation dS, déjà scellée pour la route électrique ; et `S²=−1` pour la route
magnétique/dual). S1 retire le `−` dual de la liste des candidats.*

---

## 4. Dictionnaire `C_T↔ℓ²/κ²↔N` et facteur de convention `[établi — algèbre]`

**Dictionnaire de bord.** L'éq. (1) de de Haro, `⟨T_{ij}⟩=(d\,\ell^2/16\pi G)\,g_{(3)ij}`, **est** le
dictionnaire déjà employé par le programme (`LC-D-CT-ATN`, `LC-D-NONLIN-VERROU`) ; à `d=3` le
coefficient vaut `3\ell^2/16\pi G`. Identité exacte (scellée).

**Verrouillage.** La charge centrale est le coefficient du `|p|^3\Pi_{ijkl}` dans `⟨TT⟩` (éq. 90) :

$$C_T=\frac{\ell^2}{\kappa^2}\ \ (\kappa^2=8\pi G)\ \propto\ \frac{\ell^2}{G}
\ \xrightarrow{\ \ell_{dS}=1/H\ }\ \frac{1}{8\pi G H^2}\ \propto\ N\quad(N=\tfrac{\pi}{GH^2}=S_{dS}).$$

Le rapport `C_T/N` est un **nombre pur** : `H,G,k` se simplifient. C'est exactement le **verrouillage**
de `LC-D-CT-ATN` (`C_T` n'est pas une inconnue indépendante : c'est `N`, vu côté CFT), retrouvé ici
**par la route de de Haro**.

**Facteur de convention — figé, non caché.** En normalisation **nue** de de Haro, `C_T/N=1/(8\pi^2)` ;
la valeur **scellée** du programme (`LC-D-CT-ATN`) est `1/(32\pi^2)`. Les deux sont reliées par un
**facteur de convention constant `=4`** (normalisation du projecteur `\Pi_{ijkl}` + préfacteurs entre
`W` et `⟨TT⟩`). Ce `4` est une **convention**, **pas** une contradiction : `C_T/N` est sans
dimension et `H,G,k`-indépendant dans **les deux** normalisations. (Il sera réutilisé tel quel en S2
pour comparer les coefficients de Haro à `LC-D-CT-ATN` sans ambiguïté.)

> **[Précision d'attribution — ajouté 2026-06-10, propagation route α∪R-2.]** Le calcul explicite
> (`verif_naction_alpha.py` ; projecteur de Haro éq. 119 [Appendix C.2] vérifié **identique** au
> `PiTT` du programme, 81 composantes, trace 2) montre que la part **« normalisation du projecteur
> `Π` »** de ce facteur `=4` vaut en fait **1**. **Tout le `4` réside dans les préfacteurs
> `W↔⟨TT⟩`** — les deux `2` de l'éq. 63 (`⟨T⟩=2δW/δh`, `⟨TT⟩=2δ⟨T⟩/δh`), donnant `C_T^{dH}=8c_W`
> contre la lecture programme `C_T^{prog}=2c_W` (`|Im F|/k³`). **Le PRODUIT `=4` est inchangé** ;
> seule la décomposition verbale ci-dessus est précisée. `[établi (algèbre) ; LC-AUDIT-LOG-NACTION-ALPHA]`
>
> **[Renvoi — γ via dHSS, 2026-06-11, `LC-D-CT-GAMMA`.]** Le PRODUIT `=4` ci-dessus **est** la map opérateur canonique `γ`canonique`=⟨TT⟩`canon`/ψ₂=8c_W/2c_W=4`, désormais **dérivée ab initio** et **tranchée** (sceau `verif_naction_gamma_dHSS.py`, EXIT 0). Les deux `2` (préfacteurs `W↔⟨TT⟩`) sont les **deux applications de la définition de `T=2δW/δg`** (Brown-York). Conséquence : `N_action=γ/4` ⟹ canonique `γ=4`→`N_action=1` (`C_T^prog=C_T^dH`) ; la valeur **nue** `γ=1` (`O=T/2`, `N_action=1/4`) est une **convention**. La part « normalisation de `Π` » `=1` et le PRODUIT `=4` sont **inchangés** ; ce renvoi ne fait que **nommer** le `4` comme `γ` canonique. `[établi (algèbre) ; LC-D-CT-GAMMA]`

---

## 5. Format de chaînon

- **Hypothèse testée (S1).** « La structure de dualité de de Haro (`S²=−1`, `W̃=−W`,
  `C_T∝ℓ²/κ²`) se reproduit-elle correctement en AdS, et le `−` relatif de `W̃` **flippe-t-il**
  `C_T` ? » — préalable obligatoire avant la continuation dS (S2).
- **Outil.** Solution physique TT du bulk (de Haro éq. 43) ; identité de 3e dérivée (éq. 44) ;
  fonctionnelles génératrices (éq. 61–62) ; définitions `⟨T⟩=2δW/δh`, `⟨T̃⟩=−2δW̃/δh̃` (éq. 63) ;
  deux-point (éq. 90) ; dictionnaire (éq. 1) ; `κ²=8πG`, `ℓ_dS=1/H`, `N=π/GH²`. Sceau
  `verif_D_CT_dual.py` (sympy ; EXIT 0 ; 18 asserts ; contrôle négatif inclus).
- **Critère de réfutation.** *Issue « la dualité AdS flippe `C_T` »* : si `sign(C̃_T)≠sign(C_T)` en
  AdS ⟹ le `−` dual serait un vrai second flip et S2 compterait double. **Non observé** : `−` de `W̃`
  compensé par `−2` de `⟨T̃⟩`, `C̃_T=+C_T`. *Issue « `S²≠−1` »* : si l'identité (44) tenait sans
  échange ⟹ `S=𝟙`, `S²=+1`, pas de moteur `±i`. **Non observé** : contrôle négatif. *Issue
  « dictionnaire incohérent »* : si `C_T/N` dépendait de `H,G,k` ⟹ pas de verrouillage. **Non
  observé** : nombre pur, facteur de convention constant.
- **Verdict.** `[A]` dualité EOM, `S²=−𝟙`, vp `±i` **`[établi — algèbre]`** ; `[B]` garde-fou
  `C̃_T=+C_T` en AdS **`[établi — algèbre ; cœur]`** ; `[C]` dictionnaire `C_T↔ℓ²/κ²↔N`, `C_T/N`
  pur, convention `=4` **`[établi — algèbre]`**. **Non couvert (S2, `à inventer`)** : continuation
  dS ; seconde route au signe (secteur magnétique/dual) ; rôle de `S²=−1` dans le `i²` ; CFT de
  raccordement = Dirichlet ou duale. **S1 est en AdS ; D1 non clos ; la CCC n'est pas démontrée.**

---

## 6. Propagation / housekeeping `[à appliquer — note de reprise séparée ; NON exécutée]`

À l'enregistrement (cf. `statut_id`), propagation **additive** (jamais réécriture d'historique) :

1. **`LC-D-CT-REALITE §renvoi`** — S1 pose la **base AdS** de la 2e route au signe et **protège** ce
   chaînon : le `−` relatif de `W̃` **ne** retourne **pas** `C_T` (garde-fou), donc le `i^{d-1}` de la
   route électrique n'est pas compté deux fois. Algèbre de REALITE **inchangée**.
2. **`LC-D-NONLIN-VERROU §renvoi`** — même décomposition `E∝g₃` / `B∝Cotton` (de Haro), ici au
   **deux-point** (où vit `C_T`) et non au un-point ; lien explicite entre les deux niveaux.
3. **`LC-D-HOLOGRAPHIE-G3 §3`** — ajouter la dualité graviton-dual comme **lead de structure** pour
   l'item « CFT de raccordement » (`à inventer`) : la CFT duale (Neumann) est un candidat naturel à
   tester en S2.
4. **`LC-AUDIT-VERDICT §8bis`** — bullet daté : « sceau dualité S1 (AdS) : `S²=−1` (vp ±i) ;
   garde-fou `C̃_T=+C_T` (le `−` de `W̃` compensé) ; dictionnaire `C_T↔ℓ²/κ²↔N`, convention `=4` ;
   S2 (dS) à inventer ; D1 non clos ».
5. **`LC-00-INDEX`** — nouvelle ligne carte (`LC-D-CT-DUAL`, module [D], résultat S1) + changelog.
6. **`03_glossaire`** — entrées : *dualité graviton-dual (de Haro)* ; *garde-fou de signe (le `−`
   dual compensé)* ; *facteur de convention deHaro/programme `=4`*.
7. **`02_programme`, `04_references`** — renvois (de Haro 0808.2054 **déjà en KB** ; aucune réf neuve).

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-D-CT-ATN` (verrouillage `C_T∝N` en magnitude — retrouvé ici par la route de
de Haro) ; `LC-D-CT-REALITE` (route électrique du signe `i^{d-1}` — **protégée** par le garde-fou) ;
`LC-D-NONLIN-VERROU` (décomposition `E/B` au un-point ; même dictionnaire de de Haro) ;
`LC-D-HOLOGRAPHIE-G3 §3` (cadre dS/CFT, CFT de raccordement `à inventer`) ; `LC-E-PLANCK-RESIDUEL`
(`N=S_dS`) ; `LC-D3-SPECTRE-K3` (forme `⟨TT⟩∝k³`) ; `LC-D3-FRONT-A-SYNTHESE` (verdict figé,
**inchangé**) ; `LC-AUDIT-VERDICT §6.4` (discipline) ; `LC-WORK-REPRISE-POST-CT-REALITE §4`
(recommandation exécutée ici, étage S1).

**Ajouts (2026-06-12, lot de propagation NONLIN-2PT — `LC-D-NONLIN-2PT` v0.1 +
`LC-AUDIT-LOG-NONLIN-2PT` v0.1, verdict ACQUIS 4/4).**
- *`D²=−𝟙` recoupé indépendamment* : cf. note du §2 — le chaînon rang 2 reconstruit la
  dualité sur `(𝓔,𝓑)` et retrouve l'involution à valeurs propres `±i` par une route
  autonome.
- *Équipartition `⟨𝓑𝓑⟩=⟨𝓔𝓔⟩`* : exacte **en unités de dualité** (dH éq. (49)/(50)) —
  scoping **obligatoirement attaché** à toute occurrence (R-11 : la 2e convention dH
  p.14, `𝓑=2C`, rend le scoping nécessaire). L'épinglage de `c_B` en **unités
  programme** (attendu `c_B=1/H`, à dériver du Weyl rescalé, jamais à poser) est une
  `décision ouverte` cataloguée (R-11).
  **Note (2026-06-12, LC-D-CB-WEYL-MAGNETIQUE v0.1)** : cette `décision ouverte` est
  **LEVÉE PAR DÉRIVATION** — `c_B = 1/H` exact, dérivé de la définition du Weyl rescalé
  (sceau `verif_cb_weyl_magnetique.py`, EXIT 0, 26 asserts, sha256 `e1bef559…344f` ;
  cibles gelées au cadrage `LC-WORK-CADRAGE-CB` v0.1, tenues telles qu'écrites, R-7).
  Conséquence : l'équipartition `⟨𝓑𝓑⟩=⟨𝓔𝓔⟩` est exacte **aussi en unités programme**
  (couple complet `𝓔=(3/2H)g₃ | 𝓑=(1/H)C[g₀]`) ; refermeture dH (49)/(50) slack nul.
  L'énoncé ci-dessus « en unités de dualité » **reste vrai tel qu'écrit** (la levée est
  une dérivation, pas une suppression). {A4 ; A2★ ; N} inchangé ; D1 non clos.
- *Corroborations excédentaires consignées* (passe 3 de l'audit, source dH intégrale) :
  dH éq. **(121)** (App. C.2) recoupe **indépendamment** le Cotton `(i/2)k³` ; dH éq.
  **(90)** exhibe **dans la source même** le couple C1+C2 du chaînon (pair `k³Π`
  radiatif + impair Chern-Simons **contact**).

**Glossaire (`LC-03`) — à ajouter si validé.**
- *Dualité graviton-dual (de Haro)* : en AdS₄/CFT₃, le graviton fixe (Dirichlet) source `⟨T⟩` ; le
  graviton dual fixe (Neumann) source un `⟨T̃⟩` qui **est** le tenseur de Cotton de la première CFT.
  Les deux CFT sont reliées par une transformation de Legendre = Chern-Simons gravitationnel ;
  électrique `E∝g₃∝⟨T⟩`, magnétique `B∝Cotton` ; `S(E)=B`, `S(B)=−E`, `S²=−1`.
- *Garde-fou de signe (S1)* : `W̃=−W` (éq. 61-62) mais `⟨T̃⟩=−2δW̃/δh̃` (éq. 63) ⟹ `C̃_T=+C_T` en
  AdS ; la dualité AdS **ne flippe pas** `C_T` ⟹ le signe négatif requis ne peut venir que de la
  continuation dS (`i^{d-1}`) et/ou de `S²=−1` (S2).
- *Facteur de convention deHaro/programme* : `C_T/N=1/(8π²)` (normalisation nue de de Haro) vs
  `1/(32π²)` (scellé `LC-D-CT-ATN`) ⟹ constant `=4` (normalisation de `Π` + préfacteurs) ; pas une
  contradiction.

**Références (`LC-04`, en KB).** de Haro, JHEP **01** (2009) 042, arXiv:0808.2054 (graviton dual,
Cotton holographique, `S²=−1`, `W̃=−W`) ; de Haro–Skenderis–Solodukhin, CMP **217**, 595 (2001)
(`⟨T⟩=(d/16πG)g_{(d)}`, `2κ²=16πG`) ; Strominger, JHEP **10** (2001) 034 (dS/CFT) ;
Gibbons & Hawking, Phys. Rev. D **15**, 2738 (1977) (`N=S_dS`).

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`). Ici : dualité EOM `S²=−1` + garde-fou `C̃_T=+C_T` (AdS) + dictionnaire
`C_T↔ℓ²/κ²↔N` **`établi (algèbre — sceau, EN AdS)`** ; continuation dS + seconde route au signe +
rôle de `S²=−1` dans le `i²` + CFT de raccordement (Dirichlet vs duale) **`à inventer` (S2)** ;
**D1 non clos** ; compte `{A4 ; A2★ ; N}` **inchangé**.
