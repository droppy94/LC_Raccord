---
id: LC-D-NONLIN-VERROU
titre: "Module A↔D — GÉNÉRALISATION NON-LINÉAIRE DU VERROUILLAGE UN-POINT « A4 ⟹ A3 », SCELLÉE PAR TRIPTYQUE (secteur de Weyl complet). Successeur NON-PERTURBATIF de LC-WORK-A3-D1-PASSERELLE [2] (qui n'avait l'argument qu'au niveau TT linéaire). Thèse : sous A3 (dS-invariance de l'état de raccordement), la fonction à UN POINT du tenseur de Weyl rescalé COMPLET (électrique E ⊕ magnétique B, relatif à la normale au bord 𝓘⁺) s'annule EXACTEMENT (tous ordres) et sur LES DEUX parités. Triptyque, trois sceaux EXIT 0 : sub-Q1 (verif_nonlin_cotton.py, 12/12) — secteur MAGNÉTIQUE B∝Cotton[g0], parité IMPAIRE : sous A3 le fond est maximalement symétrique ⟹ conformément plat (d=3) ⟹ Cotton=0 ⟹ ⟨B⟩=0 identiquement, SANS argument de représentation ; sub-Q2 (verif_nonlin_repr.py, 14/14) — secteur ÉLECTRIQUE E∝g3∝⟨T⟩, parité PAIRE : g3 transverse+sans trace par les Ward EXACTES (d=3 impair, pas d'anomalie) ⟹ PUR spin-2 tous ordres ; spin-2 ∩ invariants = {0} (Π^TT(δ)=Π^TT(P)=0) ; polarisations d'hélicité ±2 (pas d'hélicité 0) ⟹ ⟨E⟩=0 exactement ; sub-Q3 (verif_nonlin_parity.py, 5/5) — cohérence de PARITÉ : Cotton = PSEUDO-tenseur (parité impaire), Ricci/Schouten/stress = tenseur VRAI (parité paire) ; (E,B)=(5,5)=10 complet, disjoint, sans croisé ; chaque secteur annulé par SON argument RESPECTANT sa parité, aucun n'exigeant la parité-invariance de l'état. EFFET : « A4 ⟹ A3-un-point » passe de `établi perturbatif` à `établi` AU UN-POINT. SANS SURCLASSEMENT (§6.4) : un-point SEULEMENT — le DEUX-POINT ⟨g3 g3⟩∝k³ (SPECTRE-K3) reste libre, IRRÉDUCTIBLE ⟹ A3/A4 NON fusionnés tout court ; conditionnel à A3 ; spécifique d=3 ; D1 NON clos. C_T~N est DÉJÀ géométrique (non-perturbatif, LC-D-CT-ATN) ; ce chaînon rend non-perturbatif le MAILLON un-point A4⟹A3, fermant le résidu non-linéaire un-point de R1."
codename: LC-RACCORD
tags: [module-A, module-D, front-a, A3, A4, WCH, weyl-rescale, electrique-magnetique, cotton-york, fefferman-graham, stress-tensor, g3, representation, spin-2, helicite, parite, pseudo-tenseur, conforme-plat, ds-cft, non-lineaire, un-point, passerelle, sceau, D1]
type: "chaînon (résultat — scelle la généralisation NON-LINÉAIRE du verrouillage un-point A4⟹A3 sur le secteur de Weyl complet ; successeur non-perturbatif de LC-WORK-A3-D1-PASSERELLE ; TRIPTYQUE SCELLÉ : verif_nonlin_cotton.py, verif_nonlin_repr.py, verif_nonlin_parity.py)"
statut: "établi (algèbre), TRIPTYQUE SCELLÉ — sub-Q1 magnétique (Cotton=0 sur conf. plat ⟹ ⟨B⟩=0, parité impaire) ; sub-Q2 électrique (g3 pur spin-2 par Ward exactes ⟹ ⟨E⟩=0, parité paire) ; sub-Q3 cohérence de parité (E vrai-tenseur / B pseudo-tenseur ; couverture disjointe + complète des deux parités). ⟹ un-point du Weyl complet = 0 sous A3, NON-perturbativement ⟹ A4⟹A3-un-point devient `établi` au un-point. NON SCELLÉ / décision ouverte : le DEUX-POINT ⟨g3 g3⟩∝k³ reste libre (irréductible, SPECTRE-K3) ⟹ A3/A4 NON fusionnés — PRÉCISÉ 2026-06-12 (LC-D-NONLIN-2PT v0.1, audité 4/4 ACQUIS) : la FORME du deux-point est verrouillée par invariance ; le résidu libre = la SEULE amplitude A_T~1/N. Conditionnel à A3 ; spécifique d=3 ; D1 NON clos."
version: 0.4
langue: fr
date: 2026-06-09
maj: "2026-06-12 — v0.4 : renvoi (lot de propagation NONLIN-2PT) — LC-D-NONLIN-2PT v0.1 (sceau verif_nonlin_deuxpoint.py EXIT 0/41, byte-identique sha 1e40f5e8…eedde ; AUDITÉ à froid 4/4 ACQUIS, LC-AUDIT-LOG-NONLIN-2PT v0.1) : le point ouvert §4 « Le deux-point » est PRÉCISÉ additivement — la FORME du deux-point du Weyl rescalé complet est verrouillée PAR INVARIANCE (pair : 1 forme k³·Π^TT ; impair : contact, aucune amplitude radiative neuve ; deux parités), analogue rang 2 du présent triptyque ; le résidu libre n'est plus la donnée [D] entière mais la SEULE amplitude A_T~1/N (décision ouverte, pendue à N). Statut actualisé en place. Le k³ reste la donnée de Cauchy irréductible ; A3/A4 NON fusionnés ; D1 non clos ; compte {A4 ; A2★ ; N} inchangé. Aucune touche algèbre ni sceaux. | 2026-06-09 — v0.3 : renvoi — LC-D-CT-DUAL v0.1 (dualité graviton-dual de de Haro, étage S1/AdS, verif_D_CT_dual.py EXIT 0) emploie la MÊME décomposition électrique/magnétique (E∝g₃∝⟨T⟩ pair ; B∝Cotton impair), ici au DEUX-POINT (où vit C_T) et non au un-point : lien explicite entre les deux niveaux. Aucune touche algèbre ni sceaux. | 2026-06-09 — v0.2 : ERRATUM bibliographique + propagation EXÉCUTÉE. (i) Erratum : « Bakas-Skenderis » (mention informelle erronée) corrigé en « Bakas » (3 occurrences : statut_id, §1, §6) — la référence est I. Bakas, JHEP 01 (2009) 003, arXiv:0809.4852 ; aucune touche à l'algèbre ni aux sceaux. (ii) Propagation §6 EXÉCUTÉE et déposée (lot du 2026-06-09) : LC-00-INDEX v1.29, LC-AUDIT-VERDICT v1.17 §8bis, 02-PROGRAMME v1.15, 03-GLOSSAIRE v1.27, LC-WORK-A3-D1-PASSERELLE v0.3 (un-point relevé), LC-D3-FRONT-A-SYNTHESE v1.3 §6 (caveat A3 levé, verdict figé inchangé), 04-REFERENCES v1.10 (réfs « Weyl magnétique = Cotton » web-vérifiées et confirmées : de Haro 0808.2054 ; de Haro-Petkou 0710.0965 ; Mansi-Petkou-Tagliabue 0808.1212/1213 ; Bakas 0809.4852 ; dorsale FG+Ward de Haro-Skenderis-Solodukhin déjà confirmée). Statut/§6 actualisés en conséquence. | 2026-06-09 — v0.1 : scelle la généralisation NON-LINÉAIRE du verrouillage un-point « A4⟹A3 ». Successeur non-perturbatif de LC-WORK-A3-D1-PASSERELLE [2] (TT linéaire). Triptyque, trois sceaux EXIT 0 : [sub-Q1] verif_nonlin_cotton.py (12/12) — B∝Cotton[g0] (parité impaire) ; Cotton(S³)=Cotton(R³)=Cotton(H³)=0 exactement ⟹ sous A3 (fond max. sym. ⟹ conf. plat en d=3) ⟨B⟩=0 IDENTIQUEMENT, sans représentation ; Cotton linéarisé d'une perturbation TT non nul + symétrique/sans trace/transverse (objet TT, pas de fuite de singlet). [sub-Q2] verif_nonlin_repr.py (14/14) — E∝g3∝⟨T⟩ (parité paire) ; décomposition SVT complète en d=3 (symbolique n=ẑ + numérique 200 directions, <1e-12) ; Π^TT(δ)=Π^TT(P)=0 (spin-2 ∩ invariants={0}) ; hélicité ±2 (R_z(ψ)e^±R_z^T=e^{∓2iψ}e^±, pas d'hélicité 0) ; g3 transverse+sans trace par Ward EXACTES (d=3 impair) ⟹ pur spin-2 tous ordres ⟹ ⟨E⟩=⟨g3⟩=0 EXACTEMENT (upgrade non-perturbatif de la passerelle [2]). [sub-Q3] verif_nonlin_parity.py (5/5) — Cotton = pseudo-tenseur (y_R=det(R)(R⊗R)y(Rx), contrôle négatif inclus) ⟹ B impair ; Ricci = tenseur vrai (sans det, contrôle négatif inclus) ⟹ E pair ; (E,B)=(5,5)=10 complet, disjoint, sans croisé. EFFET : A4⟹A3-un-point `établi perturbatif`→`établi` au un-point. SANS SURCLASSEMENT (§6.4) : un-point seulement ; DEUX-POINT k³ libre/irréductible ⟹ A3/A4 NON fusionnés ; conditionnel à A3 ; spécifique d=3 ; D1 NON clos ; PAS la CCC. C_T~N déjà géométrique (LC-D-CT-ATN). « Le bang gagne » (P6 B) intact, aucune touche à l'algèbre amont. Propagation §6 NON exécutée (proposée, lot séparé)."
statut_id: "ENREGISTRÉ et PROPAGÉ (lot 2026-06-09) : LC-00-INDEX v1.29 (ligne carte + changelog), LC-WORK-A3-D1-PASSERELLE v0.3 (un-point `établi perturbatif`→`établi` non-perturbatif), LC-D3-FRONT-A-SYNTHESE v1.3 §6 (caveat A3 levé ; verdict figé inchangé), LC-AUDIT-VERDICT v1.17 §8bis, 02-PROGRAMME v1.15, 03-GLOSSAIRE v1.27, 04-REFERENCES v1.10 (réfs confirmées : de Haro / Bakas / Mansi-Petkou-Tagliabue pour E∝g3, B∝Cotton ; de Haro-Skenderis-Solodukhin pour Ward d impair). Erratum v0.2 : « Bakas-Skenderis »→« Bakas »."
fichier_compagnon: verif_nonlin_cotton.py
fichiers_compagnons: [verif_nonlin_cotton.py, verif_nonlin_repr.py, verif_nonlin_parity.py]
prerequis_kb: [LC-WORK-A3-D1-PASSERELLE, LC-D3-WEYL-BUNCHDAVIES, LC-D3-SPECTRE-K3, LC-A-D1-STABILITE-WEYL, LC-D-HOLOGRAPHIE-G3, LC-D-CT-ATN, LC-D3-FRONT-A-SYNTHESE, LC-AUDIT-VERDICT, LC-00-INDEX]
fichiers_compagnons_kb: [verif_A3_D1_passerelle.py, verif_D3_bunchdavies.py, verif_D3_spectre_k3.py, verif_D_CT_ATN.py]
renvois: [LC-WORK-A3-D1-PASSERELLE, LC-D3-WEYL-BUNCHDAVIES, LC-D3-SPECTRE-K3, LC-A-D1-STABILITE-WEYL, LC-D-HOLOGRAPHIE-G3, LC-D-CT-ATN, LC-D3-FRONT-A-SYNTHESE, LC-SYNTHESE-SOCLES, LC-AUDIT-VERDICT, LC-00-INDEX, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[A] / front (a) — rend NON-perturbatif le maillon un-point « A4 (g3→0) ⟹ A3-un-point (⟨g3⟩=0) » sur le secteur de Weyl complet (électrique + magnétique), au-delà du mode TT linéaire de la passerelle. Ne dérive ni A3 ni A4 ; D1 non clos."
  - "[D] holographie / dS-CFT — repose sur le dictionnaire FG : E∝g3∝⟨T⟩ (donnée d'état, électrique) et B∝Cotton[g0] (donnée géométrique, magnétique) en d=3 ; Ward EXACTES en d impair (pas d'anomalie) ⟹ g3 pur spin-2."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-D·NONLIN — Verrouillage NON-LINÉAIRE du un-point `A4 ⟹ A3`, scellé (triptyque)

> **But.** La passerelle `LC-WORK-A3-D1-PASSERELLE` `[2]` avait montré « A4 ⟹ A3-un-point »
> (`⟨g₃⟩=0`) **au niveau TT linéaire** (mode unique, relation BD `g₃=-(i/3)k³g₀`), laissant
> la **généralisation non-linéaire** (au-delà du TT perturbatif, secteur de Weyl complet) en
> `décision ouverte` (cf. `LC-D3-WEYL-BUNCHDAVIES §6`). Ce chaînon **ferme ce résidu un-point**,
> non-perturbativement, par un **triptyque** scellé.
>
> **Thèse.** Sous **A3** (dS-invariance de l'état de raccordement, Def-2), la fonction à **un
> point** du tenseur de Weyl rescalé **complet** — décomposé relativement à la normale en
> électrique `E_ij` ⊕ magnétique `B_ij` — **s'annule exactement (tous ordres) et sur les deux
> parités**.
>
> **Verdict (calculé ; 3 sceaux EXIT 0 ; 31 asserts).**
> **(1)** Secteur **magnétique** `B∝Cotton[g₀]` (**parité impaire**) : sous A3 le fond est
> maximalement symétrique ⟹ **conformément plat** (`d=3`) ⟹ `Cotton=0` ⟹ `⟨B⟩=0`
> **identiquement**, *sans* argument de représentation `[établi — algèbre]`.
> **(2)** Secteur **électrique** `E∝g₃∝⟨T⟩` (**parité paire**) : `g₃` est transverse + sans
> trace par les **Ward exactes** (`d=3` impair, pas d'anomalie) ⟹ **pur spin-2 tous ordres** ;
> le secteur spin-2 ne contient **aucun invariant** (hélicité `±2`) ⟹ `⟨E⟩=⟨g₃⟩=0`
> **exactement** `[établi — algèbre]`.
> **(3)** **Cohérence de parité** : `E` est un tenseur **vrai** (parité paire), `B` un
> **pseudo-tenseur** (parité impaire) ; `(E,B)=(5,5)=10` épuise le Weyl, **disjointement**,
> sans terme croisé `[établi — algèbre]`.
>
> ⟹ **« A4 ⟹ A3-un-point » passe de `établi perturbatif` à `établi` (au un-point).**

---

## 0. Rôle et garde-fou

Ce chaînon est un **résultat de comptage**, pas une démonstration physique. Discipline
`LC-AUDIT-VERDICT §6.4` : un `établi (algèbre)` atteste que **l'algèbre est correcte et les faits
reproduits**, **jamais** « la physique de la CCC est établie ». Ici précisément :

- Le résultat est **un-point** (fond / fonction à un point). Au **second ordre**,
  `⟨δWeyl⟩ ∼ ⟨δg δg⟩ ≠ 0` : c'est le **deux-point**, déjà le résidu **irréductible**
  `⟨g₃g₃⟩∝k³` (`LC-D3-SPECTRE-K3`), **hors** de la réduction un-point. **A3 et A4 ne
  fusionnent donc PAS *tout court*** — leur écart vit entièrement au deux-point.
- Le résultat est **conditionnel à A3** (état dS-invariant) : on ne **dérive pas** A3.
- Il est **spécifique à `d=3`** (4D bulk) : `B = Cotton =` courbure conforme est une
  particularité de la dimension 3.
- **D1 n'est pas clos** ; le deux-point reste donnée de Cauchy libre de `[D]`.

---

## 1. La thèse, en une ligne `[ce que le triptyque scelle]`

$$\langle \tilde C_{abcd}\rangle_{\text{un-point}}\;=\;\underbrace{\langle E_{ij}\rangle}_{\text{pair}}\;\oplus\;\underbrace{\langle B_{ij}\rangle}_{\text{impair}}\;=\;0\quad(\text{sous A3, exactement, tous ordres}).$$

Le Weyl rescalé au bord `𝓘⁺` (développement de Fefferman-Graham, `d=3`) se répartit en deux
secteurs (dualité électrique/magnétique, de Haro ; Bakas ; Mansi-Petkou-Tagliabue) :

$$E_{ij}\ \propto\ g_{(3)ij}\ \propto\ \langle T_{ij}\rangle\quad(\text{donnée d'ÉTAT}),\qquad B_{ij}\ \propto\ C_{ij}[g_{(0)}]=\varepsilon_i{}^{kl}\nabla_k P_{lj}\quad(\text{Cotton-York, GÉOMÉTRIE}).$$

L'identification électrique `E_ij=(d/2H)g₃` est **déjà scellée** en amont
(`verif_D3_bunchdavies.py`) ; ce chaînon **ne la rejoue pas** — il scelle (i) le secteur
magnétique, (ii) le caractère **exact/non-perturbatif** du secteur électrique, (iii) leur
cohérence de parité.

---

## 2. Le triptyque `[établi — algèbre ; 3 sceaux]`

### sub-Q1 — secteur MAGNÉTIQUE = Cotton (parité impaire) — `verif_nonlin_cotton.py` (12/12)

`B_ij` n'est **pas une donnée d'état** : c'est le **tenseur de Cotton-York** de la métrique de
bord `g₀`, qui en `d=3` **est** la courbure conforme (`C_ij=0 ⟺ g₀` conformément plat — le Weyl
3D étant identiquement nul). Sceau : `Cotton-York(S³)=Cotton-York(ℝ³)=Cotton-York(H³)=0`
**exactement** (les trois signes de courbure ⟹ propriété de symétrie maximale, pas artefact). Or
A3 ⟹ fond **maximalement symétrique** ⟹ **conformément plat** en 3D ⟹

$$C_{ij}[g_{(0)}]=0\ \Longrightarrow\ \langle B_{ij}\rangle=0\ \text{au un-point, IDENTIQUEMENT, SANS représentation.}$$

Contrôle de non-trivialité/structure : sur une perturbation **TT** du plat, le Cotton-York
linéarisé est **non nul** (`∝` dérivée tierce des amplitudes) et reste **symétrique + sans trace
+ transverse** (objet TT = magnétique du Weyl ; **pas de fuite de singlet**).

### sub-Q2 — secteur ÉLECTRIQUE = représentation (parité paire) — `verif_nonlin_repr.py` (14/14)

`g₃∝⟨T_ij⟩` vérifie, en `d=3` (**impair**), les **Ward exactes** : **sans trace**
(`g₀^{ij}g₃_{ij}=0`, *pas d'anomalie* — même fait que côté `C_T`) et **conservé**
(`∇^i g₃_{ij}=0`). Ces deux identités sont **exactes, non-perturbatives**
(de Haro-Skenderis-Solodukhin) ⟹ `g₃` est **pur spin-2, tous ordres**. Sceau : décomposition
SVT complète en `d=3` (symbolique `n=ẑ` + numérique sur 200 directions génériques, écart
`<10⁻¹²`) ; `Π^TT(δ)=Π^TT(P)=0` ⟹ **`spin-2 ∩ invariants = {0}`** (les seuls tenseurs
symétriques isotropes `{δ,P}` sont pure trace) ; polarisations TT d'**hélicité `±2`**
(`R_z(ψ)e^±R_z^T=e^{∓2iψ}e^±`, **pas d'hélicité 0**). Donc, dans un état dS/rotation-invariant :

$$\langle E_{ij}\rangle=\langle g_{(3)ij}\rangle_{\text{spin-2}}=0\quad\text{EXACTEMENT}\ \ (\text{upgrade NON-perturbatif de la passerelle [2]}).$$

Une **trace** éventuelle `⟨T⟩∝g_ij` est un **singlet** (contre-terme local), **hors** de la
donnée de Weyl `g₃` : **pas d'admixture de singlet dans le spin-2**.

### sub-Q3 — cohérence de PARITÉ — `verif_nonlin_parity.py` (5/5)

`E_ij` ne porte **aucun** `ε` ⟹ **tenseur vrai** ⟹ **parité paire** ; `B_ij` porte **un** `ε`
⟹ **pseudo-tenseur** ⟹ **parité impaire**. Sceau (réflexion `R=diag(1,1,-1)`, `det R=-1`) :
le Cotton-York se transforme en `y_R=\det(R)\,(R\otimes R)\,y(Rx)` (**pseudo**, contrôle négatif
inclus) ; le Ricci/Schouten/stress en `\text{Ric}_R=(R\otimes R)\text{Ric}(Rx)` (**vrai**, contrôle
négatif inclus). `(E,B)=(5,5)=10` = Weyl complet relatif à la normale (**pas de 3e secteur**), et
la parité **conserve** chaque secteur (pair↔pair, impair↔impair, **sans croisé**). Chaque secteur
est annulé par **son** argument, **respectant sa parité** — `⟨E⟩=0` par représentation (pair),
`⟨B⟩=0` par Cotton (impair) — **sans qu'aucun n'exige la parité-invariance de l'état**.

---

## 3. Synthèse `[le tableau ; portée §6.4]`

| secteur | parité | objet (bord, `d=3`) | annulé par | sceau (EXIT 0) |
|---|---|---|---|---|
| électrique | **paire** | `E∝g₃∝⟨T⟩` | représentation spin-2 (Ward exactes ⟹ pur spin-2 ; hélicité ±2) | `verif_nonlin_repr.py` (14/14) |
| magnétique | **impaire** | `B∝Cotton[g₀]` | `Cotton=0` (fond conf. plat sous A3) | `verif_nonlin_cotton.py` (12/12) |
| cohérence | — | `(E,B)=(5,5)=10` | parité respectée des deux côtés ; couverture disjointe + complète | `verif_nonlin_parity.py` (5/5) |

**Effet (réduction de comptage).** Le **maillon un-point `A4⟹A3`** passe de `établi perturbatif`
(passerelle `[2]`, TT linéaire) à **`établi`** — non-perturbatif, secteur de Weyl complet, deux
parités. Le **résidu non-linéaire un-point de R1** (laissé `décision ouverte` par la passerelle)
est **fermé**.

**Portée (anti-surclassement, §6.4) :**
- **Un-point seulement.** Le **deux-point** `⟨g₃g₃⟩∝k³` (`LC-D3-SPECTRE-K3`) reste **libre,
  irréductible** ⟹ **A3 et A4 NON fusionnés tout court** ; l'écart A3/A4 vit entièrement au
  deux-point.
- **`C_T~N` n'est PAS l'objet de ce chaînon.** Le verrouillage `C_T∝N` est **déjà géométrique**
  (`C_T~ℓ^{d-1}/G`, non-perturbatif, `LC-D-CT-ATN`) ; ce qu'on a rendu non-perturbatif est le
  maillon **un-point `A4⟹A3`**.
- **Conditionnel à A3** (on ne dérive pas A3) ; **spécifique `d=3`** ; **D1 non clos** ; **pas la
  CCC**.

---

## 4. Ce qui reste ouvert `[décision ouverte / hors de portée]`

- **Le deux-point.** La généralisation au **deux-point** exigerait de contraindre la donnée de
  Cauchy radiative `[D]` entière (le spectre `k³`), ce qui est **précisément** ce que la WCH ne
  fait pas et que A3 ne fixe pas : `irréductible` (`LC-D3-SPECTRE-K3`). `décision ouverte`.
  **Précision (2026-06-12, `LC-D-NONLIN-2PT` v0.1, audité 4/4 ACQUIS,
  `LC-AUDIT-LOG-NONLIN-2PT`)** : la **forme** du deux-point du Weyl rescalé complet est
  désormais **verrouillée par invariance** — analogue rang 2 du présent chaînon
  (secteur pair : dimension 1, forme `k³·Π^TT` forcée ; secteur impair : dimension 1 ET
  contact, aucune amplitude radiative neuve ; deux parités couvertes). Ce qui reste libre
  n'est donc PLUS la donnée `[D]` entière mais la **seule amplitude** `A_T~1/N`
  (`décision ouverte`, pendue à `N` seul) ; le `k³` **reste** la donnée de Cauchy
  irréductible. Sans surclassement : « forme verrouillée » = comptage de représentation,
  conditionnel à A3 et aux entrées amont scellées — ne ferme PAS D1, ne fusionne PAS A3/A4.
- **`C_T` réelle en dS** : la valeur/réalité de la charge centrale dans la continuation
  non-unitaire dS/CFT reste `à inventer` (`LC-D-CT-ATN §3`) — indépendant de ce chaînon.
- **Fixation de `N`** : circularité `LC-E` non brisée — `hors de portée` sans principe neuf.

---

## 5. Format de chaînon / sceaux

- **Type** : chaînon scellé (résultat). **Statut** : `établi (algèbre)`, triptyque scellé.
- **Fichiers compagnons** : `verif_nonlin_cotton.py` (sub-Q1), `verif_nonlin_repr.py` (sub-Q2),
  `verif_nonlin_parity.py` (sub-Q3). Tous **EXIT 0**, re-exécutables, sans réseau (sympy ; numpy
  pour la confirmation multi-directions de sub-Q2).
- **Aucune algèbre neuve dans les chaînons amont** ; ce chaînon **ajoute** un résultat
  non-perturbatif au-dessus de la passerelle, sans la modifier.

---

## 6. Propagation / housekeeping `[à appliquer — lot séparé, sur validation]`

Propagation **additive** proposée (NON exécutée ici) :
- **`LC-WORK-A3-D1-PASSERELLE`** : renvoi — le un-point `A4⟹A3` passe de `établi perturbatif`
  à `établi` (non-perturbatif) ; l'écart A3/A4 demeure le deux-point `k³`.
- **`LC-D3-FRONT-A-SYNTHESE §6`** : verdict — maillon un-point A4⟹A3 relevé en `établi`
  (deux parités, secteur complet) ; (A) physique conditionnel au seul A2★ **inchangé**.
- **`LC-AUDIT-VERDICT §8bis`** : bullet daté.
- **`LC-00-INDEX`** (ligne carte + changelog), **`02-PROGRAMME`**, **`03-GLOSSAIRE`** (entrées :
  *Weyl électrique/magnétique au bord*, *Cotton-York comme magnétique du Weyl*, *verrouillage
  un-point non-perturbatif*).
- **`04-REFERENCES`** v1.10 : **FAIT** (réfs `Weyl magnétique = Cotton` web-vérifiées et `confirmé` :
  de Haro arXiv:0808.2054 ; de Haro-Petkou 0710.0965 ;
  Mansi-Petkou-Tagliabue 0808.1212/1213 ; Bakas 0809.4852 ; dorsale FG+Ward
  de Haro-Skenderis-Solodukhin déjà en KB). Dette PRISMA **close**.

---

## 7. Renvois, glossaire, références

- **Parent perturbatif** : `LC-WORK-A3-D1-PASSERELLE` `[2]` (un-point TT linéaire).
- **Identification électrique** : `LC-D3-WEYL-BUNCHDAVIES` (`E_ij=(d/2H)g₃`).
- **Résidu deux-point irréductible** : `LC-D3-SPECTRE-K3` (`⟨g₃g₃⟩∝k³`).
- **Dualité au deux-point** : `LC-D-CT-DUAL` (même décomposition `E∝g₃` / `B∝Cotton` de de Haro, portée au deux-point `⟨TT⟩`/`C_T` ; étage S1/AdS ; garde-fou : la dualité AdS ne flippe pas `C_T`).
- **Devise commune `g₃`** : `LC-A-D1-STABILITE-WEYL` (fond ⊥ marée) ; `LC-D-HOLOGRAPHIE-G3`
  (`g₃=⟨T⟩`).
- **`C_T~N` géométrique** : `LC-D-CT-ATN`.
- **Synthèse programme** : `LC-D3-FRONT-A-SYNTHESE`, `LC-SYNTHESE-SOCLES`, `LC-AUDIT-VERDICT`.

---

## Appendice — Légende des tags épistémiques

- `établi` : algèbre correcte **et** cibles/faits reproduits par sceau re-exécutable. **Jamais**
  « physique de la CCC établie » (§6.4).
- `formalisable` : structure mathématique disponible, sceau faisable, non encore exécuté.
- `à inventer` : nécessite un ingrédient (principe, coefficient, prescription) non disponible.
- `hors de portée` : hors d'atteinte des outils actuels sans idée/ressource nouvelle.
- `décision ouverte` : question bien posée, tranchable, non tranchée.
