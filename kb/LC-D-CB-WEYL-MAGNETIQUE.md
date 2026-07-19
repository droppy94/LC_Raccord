---
id: LC-D-CB-WEYL-MAGNETIQUE
titre: "Module D — ÉPINGLAGE DE c_B, SCELLÉ : la normalisation du Weyl MAGNÉTIQUE rescalé à 𝓘⁺ en unités programme est DÉRIVÉE de la définition (jamais posée) — 𝓑_ij = (1/H)·C_ij[g₀], c_B = 1/H EXACT, signe compris (cohérence d'orientation interne : même ε pour B̂=½εĈ et pour le Cotton ab initio). Conséquence (CB-2) : l'équipartition ⟨𝓑𝓑⟩=⟨𝓔𝓔⟩ est EXACTE AUSSI EN UNITÉS PROGRAMME — le scoping R-11 (« en unités de dualité ») est LEVÉ PAR DÉRIVATION, pas par suppression ; refermeture dH (49)/(50) via la map prog↔dH (facteur fixe pur), slack nul. Ferme la promesse C2pt-4 du cadrage 2PT (« la seule constante non encore explicite en KB »). Sceau verif_cb_weyl_magnetique.py (EXIT 0, 26 asserts, sha256 e1bef559bb10c115241081e46b60f95e2f70cd12d96ebb2bfe6f7a0c4888344f). Enseignement structurel : le d/2 de l'électrique (E=(d/2H)g₃) est ABSENT côté magnétique — il vient du dictionnaire ⟨T⟩=(d/16πG)g₃ (côté ÉTAT) ; 𝓑 est pure GÉOMÉTRIE. Couple programme complet : 𝓔=(3/2H)g₃ | 𝓑=(1/H)C[g₀]. R-7 : cibles gelées au cadrage (LC-WORK-CADRAGE-CB v0.1) TENUES TELLES QU'ÉCRITES, zéro amendement."
codename: LC-RACCORD
tags: [module-D, weyl-magnetique, cotton, c_B, equipartition, unites-programme, R-11, bunch-davies, scri-plus]
dependances:
  - "LC-D3-WEYL-BUNCHDAVIES — route du Weyl linéarisé + E=(d/2H)g₃ (étalon de non-régression, reproduit asserts 02/06)."
  - "LC-D-NONLIN-2PT C3 — Cotton linéarisé (i/2)k³(Dh), coefficient ½ (recoupé assert 13) ; équipartition en unités de dualité (dH 49/50) ; ⟨EB⟩=0 (non-régression assert 18)."
  - "LC-D-NONLIN-VERROU — décomposition E∝g₃ (état) / B∝Cotton (géométrie), deux parités."
  - "LC-WORK-CADRAGE-CB v0.1 — cibles gelées CB-1/CB-2/CB-3, scopings S-CB-1..4 tranchés (Thierry, 2026-06-12, « tout recommandé »)."
statut: "établi (algèbre), SCEAU FAIT — CB-1 : c_B = 1/H exact, dérivé, identique sur les deux polarisations, indépendant de k et x ; CB-2 : ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩ = 1 exacte en unités programme, refermeture dH (49)/(50) slack nul ⟹ scoping R-11 LEVÉ PAR DÉRIVATION ; CB-3 : 0 entrée libre < 2 sorties appariées ; firewall 3/3 (Ω discriminant ; Cotton ×2 casse ×4 ; parité). R-7 : zéro amendement des cibles gelées. CONDITIONNEL : perturbatif, mode TT de Bunch-Davies, d=3, conventions exhibées. NON SCELLÉ / inchangé : l'amplitude A_T~1/N (décision ouverte) ; D1 non clos ; compte {A4 ; A2★ ; N} inchangé."
statut_id: "validé après sceau (verif_cb_weyl_magnetique.py déposé en KB, EXIT 0, 26 asserts, sha256 e1bef559…344f) — à enregistrer (LC-00-INDEX) ; PROPAGER (cf. §7, lot additif SÉPARÉ, NON exécuté ici) : 00_index (carte + changelog), LC-D-CT-DUAL §7 (note : R-11 levé par dérivation), 03_glossaire (entrée c_B + note additive à l'entrée équipartition), LC-AUDIT-VERDICT §8bis (bullet), 02_programme (renvoi Module [D]). 04_references : RIEN à faire (dH (47),(49),(50) ⊂ renvois (43)-(53) déjà déposés v1.14)."
version: 0.1
date: 2026-06-12
langue: fr
maj: "2026-06-12 — v0.1 : scelle le petit front c_B (recommandation de LC-WORK-REPRISE-POST-PROPAGATION-NONLIN-2PT §4 ; cadrage paper-first LC-WORK-CADRAGE-CB v0.1 validé avant tout calcul, R-7 active). verif_cb_weyl_magnetique.py (EXIT 0, 26 asserts) : [A] non-régression bunchdavies — Ĉ₀₁₀₁=(i/2)Ak³η·e^{ik(z−η)} reproduit, E_lim/g₃=3/(2H) retrouvé ; [B] B̂=½εĈ symétrique/sans trace/TT, motif DUAL (𝓑(+)∝e^×), grandeur η¹, limite rescalée finie non nulle ; [C] Cotton ab initio (même ε) coefficient ½ recoupé ⟹ c_B = 𝓑/C^lin = 1/H sur les DEUX polarisations, indépendant de k,x — CB-1 TENUE ; [D] équipartition ⟨𝓑𝓑⟩/⟨𝓔𝓔⟩=1 EXACTE en unités programme, ⟨𝓔𝓑⟩=0, map prog↔dH transparente, refermeture dH (49)/(50) slack nul — CB-2 TENUE, R-11 levé PAR DÉRIVATION ; [F] firewall 3/3 + mutation pilote externe (mode non-BD ⟹ CASSE assert 02). Scopings S-CB-1..4 : tout recommandé (rang perturbatif TT BD ; B̂=½εĈ_{kl0j} ; PAS d'audit à froid (a), réversible ; nouveau chaînon, NONLIN-2PT reste v0.1). SANS SURCLASSEMENT (§6.4) ; compte {A4 ; A2★ ; N} inchangé ; D1 non clos ; CCC non démontrée. Propagation §7 NON exécutée (proposée, lot séparé)."
---

# LC-D·c_B — Weyl magnétique rescalé : `𝓑 = (1/H)·C[g₀]` dérivé ; équipartition en unités programme (algèbre)

> **Sceau** : `verif_cb_weyl_magnetique.py` — EXIT 0, **26 asserts**, sha256
> `e1bef559bb10c115241081e46b60f95e2f70cd12d96ebb2bfe6f7a0c4888344f`.
> **Cibles gelées** : `LC-WORK-CADRAGE-CB` v0.1 §3 — **tenues telles qu'écrites** (R-7,
> zéro amendement). Mono-phase, **aucun fetch externe** (comparanda dH déjà en KB).

---

## 0. Rôle et garde-fou `[discipline §6.4]`

Ce chaînon est un **épinglage d'unités et une refermeture** — déductif, coût faible. Il
ferme la promesse **C2pt-4** du cadrage 2PT (la normalisation exacte de `B∝Cotton`,
*« seule constante non encore explicite en KB, déductive, pas ajustable »*) et lève la
`décision ouverte` **R-11** (traduction de l'équipartition en unités programme).

Il ne dit **rien** sur A4, A2★ ou N. Un EXIT 0 ici atteste l'algèbre et la reproduction
des cibles gelées — jamais « D1 clos / N fixé / CCC démontrée ». Compte **{A4 ; A2★ ; N}
inchangé**. Conditionnel : perturbatif, mode TT de Bunch-Davies, `d=3`.

---

## 1. Le résultat, en une ligne `[ce que le sceau confirme]`

$$\boxed{\ \mathcal{B}_{ij}\big|_{\mathcal I^+} \;=\; \frac{1}{H}\,C_{ij}[g_{(0)}]\ }
\qquad c_B = \frac1H\ \text{exact, DÉRIVÉ (jamais posé), signe compris.}$$

Couple complet des normalisations programme du secteur de Weyl rescalé :

$$\mathcal{E} = \frac{3}{2H}\,g_{(3)}\ \ (\text{scellé, bunchdavies})\qquad\Big|\qquad
\mathcal{B} = \frac{1}{H}\,C[g_{(0)}]\ \ (\text{ICI}).$$

**Conséquence (CB-2)** : `⟨𝓑𝓑⟩ = ⟨𝓔𝓔⟩` **exacte aussi en unités programme** — le
scoping R-11 (« exacte *en unités de dualité* ») est **levé par dérivation**.

---

## 2. La dérivation `[établi — algèbre ; le cœur]`

Analogue magnétique **exact** de `LC-D3-WEYL-BUNCHDAVIES §3` (même route, même mode,
même rescaling) :

1. **Frame conforme.** Fond dS planaire conformément plat (`Ω=−Hη`) ⟹ Weyl de fond nul,
   tout le Weyl est dans la perturbation. Weyl linéarisé du mode TT de BD
   `h=A(1+ikη)e^{−ikη}` calculé ab initio (Riemann → Ricci → Weyl, `n=4`).
2. **Magnétique.** `B̂_{ij}=\tfrac12\varepsilon_i{}^{kl}\hat C_{kl0j}` (S-CB-2,
   `ε₁₂₃=+1`). Fait utile exhibé par le calcul : sur `C_{kl0j}` les corrections de
   Schouten **s'annulent** (`R_{0i}=0` pour TT spatial) ⟹ `B̂` ne voit que le Riemann.
   Structure (asserts 07-10) : symétrique, sans trace, TT, **motif dual**
   (`B̂(+)∝e^×` — la parité en acte), grandeur **`η¹`** comme l'électrique :
   `B̂_{12} = −\tfrac{i}{2}Ak^3\eta\,e^{ik(z−η)}`.
3. **Rescaling.** `𝓑 = lim_{η→0} B̂/Ω` : finie, non nulle (assert 11) —
   `𝓑_{12} = \tfrac{i}{2H}Ak^3 e^{ikz}`.
4. **Identification.** Cotton-York 3D linéarisé **dérivé ab initio dans le même script
   avec le même `ε`** (`C_{ij}=ε_i{}^{kl}∇_kP_{lj}`, `P=Ric−\tfrac R4 g`) : coefficient
   `½` recoupé (NONLIN-2PT C3 ; dH 47). Ratio :
   `c_B = 𝓑/C^{lin} = 1/H` — **identique sur les deux polarisations, indépendant de
   `k` et `x`** (asserts 14-16). La cohérence d'orientation est *interne* (même `ε`
   des deux côtés) ⟹ le **signe** de `c_B` est convention-cohérent, pas choisi.

**Enseignement structurel.** Le `d/2` de l'électrique est **absent** côté magnétique :
il provient du dictionnaire `⟨T⟩=(d/16πG)g_{(3)}` — côté **état**. `𝓑` est pure
**géométrie** (Cotton de `g₀`) : seule l'échelle `1/H` du rescaling survit. La
dichotomie état/géométrie du verrou un-point (`LC-D-NONLIN-VERROU`) se lit jusque dans
les normalisations.

---

## 3. Équipartition en unités programme ; R-11 levé `[établi — algèbre]`

Avec le couple dérivé, sur BD (`g_{(3)}=−\tfrac{i}{3}k^3g_{(0)}`) :

$$\mathcal{E} = -\frac{i}{2H}k^3\,g_{(0)},\qquad
\mathcal{B} = -\frac{i}{2H}k^3\,(Dg_{(0)})\quad\Rightarrow\quad
\frac{\langle\mathcal{B}\mathcal{B}\rangle}{\langle\mathcal{E}\mathcal{E}\rangle} = 1
\ \ \text{EXACTE (D isométrie sur TT)},\qquad \langle\mathcal{E}\mathcal{B}\rangle=0.$$

- **Refermeture dH (49)/(50), slack nul** : la map prog↔dH (`κ²/(Hℓ²)`, facteur fixe
  pur) est transparente dans tout ratio ; côté dH le produit net des conventions
  (`2` des préfacteurs × `½` du Cotton)² `= 1` (cas {2,4,8} **déjà résolu** au chaînon
  NONLIN-2PT, re-vérifié assert 20). Ratio prog = ratio dH = 1.
- **R-11** : le scoping « en unités de dualité » attaché à toute occurrence de
  l'équipartition est **levé par dérivation** — l'énoncé vaut désormais aussi en unités
  programme, avec traduction explicite. (La levée est une dérivation, pas une
  suppression : les occurrences existantes en KB restent vraies telles qu'écrites ;
  la propagation §7 ajoute la note, n'efface rien.)

---

## 4. Firewall `[3/3 + pilote externe]`

| injection | effet | verdict |
|---|---|---|
| rescaling `Ω⁰` (aucun) | `B̂∼η¹` ⟹ limite **nulle** (signal tué) | CASSE (asserts 21-22) |
| rescaling `Ω²` | `∼1/η` ⟹ **diverge** | CASSE (assert 21, par la série) |
| Cotton ×2 (coeff. `1` au lieu de `½`) | `c_B'=1/(2H)` ; équipartition cassée **×4** | CASSE (asserts 23-24) |
| lecture **électrique** du canal magnétique | `𝓑(+)⊥e^+` : projection **nulle** | CASSE (assert 25) |
| pilote externe : mode non-BD (`A e^{−ikη}`) | étalon bunchdavies non reproduit | CASSE (assert 02, vérifié hors sceau) |

Anti-numérologie (CB-3) : **0 entrée libre < 2 sorties appariées** (`c_B` vs attendu ;
refermeture dH) — assert 26.

---

## 5. Ce que ce chaînon n'est PAS `[sans surclassement]`

- Pas une fermeture de D1 : l'**amplitude** `A_T~1/N` reste l'unique décision ouverte
  du résidu gaussien (NONLIN-2PT), pendue à N seul.
- Pas un résultat non-perturbatif : rang perturbatif, mode TT BD (S-CB-1), même rang
  que `E=(d/2H)g₃`.
- Pas une physique neuve : un épinglage **déductif** d'unités + une refermeture. La
  `consolidation ≠ réduction de comptage` s'applique : {A4 ; A2★ ; N} **inchangé**.
- Pas audité à froid (S-CB-3a, décision Thierry) — **réversible** : un audit peut être
  commandé après coup ; R-14 s'appliquerait alors.

---

## 6. Format de chaînon

- **Entrées (toutes scellées en amont)** : mode BD + `Ω` + route Weyl linéarisé
  (bunchdavies) ; Cotton `(i/2)k³(Dh)` (NONLIN-2PT C3) ; map prog↔dH (NONLIN-2PT [D/E]) ;
  définitions S-CB-1/2 figées au cadrage.
- **Sorties** : `c_B = 1/H` (CB-1) ; équipartition en unités programme + refermeture dH
  slack nul (CB-2) ; couple complet `𝓔=(3/2H)g₃ | 𝓑=(1/H)C[g₀]`.
- **Sceau** : `verif_cb_weyl_magnetique.py`, EXIT 0, 26 asserts, mono-phase, sha256
  `e1bef559…344f`. Byte-identité à préserver (R-10 si phase ultérieure).

---

## 7. Propagation / housekeeping `[à appliquer — lot additif SÉPARÉ, NON exécuté]`

1. **`00_index`** : ligne carte (chaînon + sceau) + changelog.
2. **`LC-D-CT-DUAL §7`** : note additive datée — la `décision ouverte` c_B (R-11) est
   **levée par dérivation** (`c_B=1/H`, ce chaînon) ; l'occurrence « en unités de
   dualité » reste vraie telle qu'écrite.
3. **`03_glossaire`** : entrée *Normalisation magnétique `c_B` (dérivée)* + note
   additive à l'entrée *Équipartition* (« également exacte en unités programme,
   `c_B=1/H` dérivé — R-11 levé »).
4. **`LC-AUDIT-VERDICT §8bis`** : bullet (petit front c_B SOLDÉ ; R-7 tenue ; S-CB-3a
   sans audit à froid, réversible).
5. **`02_programme`** : bullet de renvoi en fin de Module [D].
6. **`04_references`** : **rien** (dH (47),(49),(50) ⊂ renvois (43)-(53) déposés v1.14).

Discipline du lot : strictement additif, ancres `count==1`, suppressions ⊆
`{version, maj}`, validation fichier par fichier.

---

## 8. Renvois

`LC-WORK-CADRAGE-CB` (cibles gelées, scopings) ; `LC-D3-WEYL-BUNCHDAVIES §3` (route,
`E=(d/2H)g₃`) ; `LC-D-NONLIN-2PT` (Cotton C3, équipartition dualité, {2,4,8}) ;
`LC-D-NONLIN-VERROU` (état/géométrie, deux parités) ; `LC-D-CT-DUAL §7` (R-11
catalogué) ; `LC-AUDIT-VERDICT §6.4` (discipline).

---

## Appendice — Légende des tags épistémiques

`établi (algèbre)` : algèbre correcte + cibles gelées reproduites, conditionnel aux
conventions exhibées — jamais un énoncé de physique fermée. `décision ouverte` :
choix non tranché, catalogué. R-7/R-10/R-11/R-14 : cf. `LC-AUDIT-VERDICT §8bis`.
