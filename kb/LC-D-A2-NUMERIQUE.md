---
id: LC-D-A2-NUMERIQUE
titre: "Verdict du front A2★ NUMÉRIQUE (phase MODÉLISATION HORS-ALGÈBRE, front 1) — exécute le cadrage gelé LC-WORK-CADRAGE-A2-NUMERIQUE v0.1 (gel sha 179d2f00…eca7a21b). Teste la conjecture A2★ (non-cascade : Q(τ)=Σ_spikes C_F sous-exponentielle) par un modèle MÉSOSCOPIQUE de production+charge de spikes piloté par la statistique d'ères de Gauss-Kuzmin déjà scellée. RÉSULTAT À DEUX ÉTAGES (analogue F1/F3). (N1, prolifération) le modèle établit la DICHOTOMIE non-cascade ⟺ ρ=0 (production ADDITIVE/bulk, O(1)/bounce indépendante de n_s) : ρ=0 ⟹ n_s sous-exp ; ρ>0 ⟹ cascade n_s~(1+ρ)^{N_b} (taux=ln(1+ρ) exact, monotone) — MAIS ρ=0 est un input physique MOTIVÉ (mécanisme Garfinkle), NON dérivé d'un théorème générique 3D ⟹ soutien CONDITIONNEL à l'additivité. (N2, pont u_ère→C_F) ⟨C_F⟩_GK FINI (=7.18) : exposants de Kasner BORNÉS ∀ u ⟹ charge par spike bornée ; seuil de convergence DÉRIVÉ de la mesure (s*=1) > s_phys=0 ⟹ OC ADRESSÉ (pont établi conditionnel à l'amplitude bornée par la géométrie, robuste au seuil). (N3) Q=n_s·⟨C_F⟩ sous-exp ⟹ R_grad,gen→0 via la déduction DÉJÀ scellée (verif_D3_C7b_A2_reduction.py). Sceau verif_A2_numerique.py EXIT 0/22, firewall MORDANT (m1 cascade / m2 charge divergente / m3 seuil exact CASSENT ; contrôles limites G₂ et billard reproduits), sha 76e9257cfdd337b6. VERDICT : DÉLIMITATION à lean positif — A2★ reste décision ouverte, MIEUX SITUÉE ; OC adressé ; gap RE-NOMMÉ (dériver l'additivité ρ=0 de la dynamique générique 3D ≡ OA, qui PERSISTE `hors de portée`). Aucune réfutation. SANS SURCLASSEMENT (§6.4) : périmètre {A4 ; A2★ ; N} INCHANGÉ ; A2★ ni prouvée ni réfutée ; C7 non levée ; D1 non clos ; N non fixé ; CCC non démontrée."
codename: LC-RACCORD
type: "chaînon / verdict de substantiation (phase modélisation hors-algèbre, front 1). Exécute LC-WORK-CADRAGE-A2-NUMERIQUE v0.1 (cibles A2★-N1/N2/N3 + R adoptées). Sceau réel verif_A2_numerique.py (EXIT 0/22, firewall mordant). Étage cartographie/délimitation, NON fermeture. Subordonné à LC-AUDIT-VERDICT §6.4."
statut: "VERDICT A2★-numérique — délimitation à lean positif. A2★ : décision ouverte, mieux située ; OC adressé ; gap re-nommé (additivité ρ=0 ⟸ générique 3D ≡ OA). Sceau verif_A2_numerique.py EXIT 0/22, firewall mordant, sha 76e9257cfdd337b6. {A4 ; A2★ ; N} INCHANGÉ ; C7 non levée ; CCC non démontrée."
version: "0.1"
langue: fr
date: "2026-06-17"
maj: "2026-06-17 — v0.1 : exécution du front A2★ numérique sur GO Thierry (phase modélisation hors-algèbre, front 1), selon le cadrage gelé LC-WORK-CADRAGE-A2-NUMERIQUE v0.1 (gel sha 179d2f00…eca7a21b, cibles figées AVANT exécution, anti-fit/R-7 tenu). Sceau neuf verif_A2_numerique.py (EXIT 0/22 assertions, firewall mordant m1/m2/m3 + contrôles c1/c2, sha 76e9257cfdd337b6) déposé en KB (continuité, .py 66→67, rejeu EXIT 0). Lecture anti-fit selon le critère tripartite gelé (§4 du cadrage) : N1 = dichotomie non-cascade⟺ρ=0 établie, soutien CONDITIONNEL à l'additivité (input motivé Garfinkle, non dérivé générique 3D) ; N2 = pont u_ère→C_F adressé (⟨C_F⟩_GK fini, exposants Kasner bornés + seuil dérivé s*=1) = OC adressé ; N3 = synthèse PASS conditionnel via déduction scellée. VERDICT = délimitation à lean positif, aucune réfutation. Gap re-nommé : G₂→3D NR + pont ⟶ dériver ρ=0 de la dynamique générique 3D (≡ OA `hors de portée`). Audit froid DIFFÉRÉ PAR CONCEPTION (non positif-gate, délimitation ; précédent F4), ré-armable avant toute propagation de la formule « OC adressé » ou si une construction s'appuie sur le pont N2. Strictement additif (fichier neuf). SANS SURCLASSEMENT (§6.4) : un modèle posé n'est pas un acquis ; soutien mésoscopique ≠ théorème générique 3D ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranchée ; C7 non levée ; D1 non clos ; N non fixé ; CCC non démontrée."
prerequis_kb: [LC-WORK-CADRAGE-A2-NUMERIQUE, LC-WORK-A2-CONJECTURE, LC-D-F3-A2STAR, LC-D3-C7B-VERDICT-A2, LC-D3-A1-SUPERHORIZON, LC-D3-INTERAEON-P6, LC-WORK-REPRISE-PRE-HORS-ALGEBRE, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_A2_numerique.py, verif_D3_C7b_A2_reduction.py, verif_D3_C7b_A1_superhorizon.py]
source_externe: ["AUCUNE consommée (fetch HOLD tenu, S-A2N-3). Positionnement KB-local : Garfinkle gr-qc/0312117 (mécanisme de spike, production aux bounces — 0312117v4.pdf KB) ; Lim 0710.0628 (profil exact C_F^Lim=2π·A² ; |w|>1 transitoire / 0<|w|<1 permanent — KB) ; statistique d'ères de Gauss-Kuzmin (oracle scellé LC-D3-INTERAEON-P6)."]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte, piste / à étayer]
---

# A2★ numérique — verdict (front 1, phase modélisation hors-algèbre)

> **But.** Exécuter le cadrage gelé `LC-WORK-CADRAGE-A2-NUMERIQUE` v0.1 : confronter la **seule
> maille non scellée d'A2★ — la non-cascade** — à un **modèle mésoscopique** de production + charge
> de spikes piloté par la statistique d'ères de Gauss-Kuzmin **déjà scellée**, sans prétendre au NR
> générique 3D (`hors de portée`, OA non ouverte). Discipline `§6.4` : pas de surclassement ; on
> **pose un modèle** et on **lit** le scaling. Cibles `A2★-N1/N2/N3 + R` **figées avant exécution**
> (anti-fit, R-7).

---

## 0. Verdict en une ligne `[décision]`

**Délimitation à lean positif.** Le modèle mésoscopique **soutient** A2★ (non-cascade) **dans le
régime additif `ρ=0`** et **adresse le pont `u_ère→C_F`** (charge par spike bornée sous la mesure
d'ère), **mais ne dérive pas** l'additivité d'un théorème générique 3D (OA persiste). **Aucune
réfutation.** A2★ reste **`décision ouverte`, mieux située** ; le gap est **re-nommé**.
**`{A4 ; A2★ ; N}` INCHANGÉ.** Sceau réel `verif_A2_numerique.py` EXIT 0/22, firewall mordant.

---

## 1. Ce qui est testé / ce qui est hérité `[anti-doublon]`

Le résidu générique de C7-b (réduit par `LC-WORK-A2-CONJECTURE`) :
`R_grad,gen(τ) = Q(τ)·I_spike^gen(τ)/⟨Ω_σ⟩_bulk`, `Q(τ)=Σ_spikes C_F`.

**Déjà scellé (non refait) :** A1 (`I_spike^gen=C_F·w/cosh(wτ)≈2C_F·w·e^{−|w|τ}`,
`verif_D3_C7b_A1_superhorizon.py`) ; déduction §4 (`Q` sous-exp ⟹ `R→0`) et `N_b` sous-exp
(`verif_D3_C7b_A2_reduction.py`). **Seule maille `décision ouverte` :** la **non-cascade** —
`Q=n_s·⟨C_F⟩` sous-exponentielle, factorisée en **prolifération** `n_s(τ)` (N1) + **charge par
spike** `⟨C_F⟩` sous la mesure d'ère (N2).

---

## 2. Résultat du sceau `[verif_A2_numerique.py, EXIT 0/22, sha 76e9257c…]`

**N1 — prolifération `n_s(τ)`.** Modèle era-driven : par bounce, production **additive** (bulk,
`O(1)`, indépendante de `n_s`), réplication **multiplicative** `ρ·n_s` (cascade), décroissance des
transitoires (Lim `|w|>1`). Balayage de `ρ` (taux = `ln(n_s(b+1)/n_s(b))` asymptotique, mesuré en
ratio renormalisé sans overflow) :

| `ρ` | 0 | 0.05 | 0.2 | 0.5 | 1.0 |
|---|---|---|---|---|---|
| taux | `3.3e-4` (≈0) | `0.0488` | `0.1823` | `0.4055` | `0.6770` |
| | sous-exp | `=ln1.05` | `=ln1.2` | `=ln1.5` | `≈ln2` |

⟹ **non-cascade ⟺ `ρ=0`** (production additive). La dichotomie est nette et le taux de cascade
reproduit `ln(1+ρ)` exactement. **`ρ=0` est l'input physique porteur** (Garfinkle : production
`O(1)`/bounce, non multiplicative par spike existant) — **motivé, non dérivé** en générique 3D.

**N2 — pont `u_ère→C_F`.** Exposants de Kasner `p_i(u)` **bornés ∀ `u≥1`** (`Σp=1`, `Σp²=1`,
`p∈[−1/3,1]`) ⟹ charge `C_F=2π·A²` **bornée** (`A` = écart d'anisotropie borné ; `C_F(u→∞)→2π`).
Sous la mesure de Gauss-Kuzmin (`P(k)=log₂(1+1/(k(k+2)))`) : **`⟨C_F⟩_GK = 7.18`, fini**. Seuil de
convergence **dérivé de la mesure** : `C_F~k^s` converge ⟺ `s<1` (vérifié : `s=0.5` converge,
`s=1`/`s=2` divergent) ; `s_phys=0 < s*=1` ⟹ **pont robuste**. **OC adressé** (conditionnel à
l'amplitude bornée par la géométrie de Kasner).

**N3 — synthèse.** `Q=n_s·⟨C_F⟩` (avec `n_s` linéaire à `ρ=0`) ⟹ `lim ln Q/τ = 0 < |w|` ⟹
`R_grad,gen→0` via la **déduction déjà scellée**. PASS conditionnel à N1∧N2.

**Firewall MORDANT.** m1 cascade (`Q~e^{ln2·τ}`, `|w|=ln2/2`) ⟹ `R→∞` (CASSE) ; m2 charge
divergente (`C_F~k²`) ⟹ `⟨C_F⟩` non stabilisée (CASSE) ; m3 seuil exact (`Q=e^{wτ}`) ⟹ `R↛0`
(CASSE, réfutation R2). Contrôles : G₂ (transitoire-dominé, `ρ=0`) ⟹ `n_s` sous-exp **reproduit** ;
billard/ultralocal (production nulle) ⟹ `n_s≡0` (**cohérence OB**).

---

## 3. Lecture tripartite `[critère gelé §4 du cadrage]`

- **Pas une DÉRIVATION** : N1 conditionnel à l'additivité `ρ=0` **posée/motivée**, non dérivée d'un
  théorème générique 3D ; et le régime testé est **mésoscopique**, non NR 3D (**OA persiste**).
- **Pas une RÉFUTATION** : aucune cascade en régime physique (`ρ=0`) ; charge bornée.
- **DÉPLACEMENT partiel + DÉLIMITATION à lean positif** : la non-cascade tient **sous additivité
  motivée** (déplacement du postulat vers « production additive ») ; le pont N2 est **adressé**
  (avancée réelle sur OC). Issue retenue : **délimitation à lean positif**.

---

## 4. Gap re-nommé + statut épistémique `[§6.4]`

Avant : *« A2★ = décision ouverte ; gap = extension G₂→générique 3D + pont `u_ère→C_F` »* (F3).
Après : le pont (**OC**) est **adressé** ; **OB** est contournée par construction ; **OA persiste**.
**Gap re-nommé** : *« la non-cascade tient si la production de spikes est additive (`ρ=0`) ; reste à
**dériver cette additivité de la dynamique générique 3D** »* — ce qui **est** OA (`hors de portée`,
NR générique 3D). A2★ reste `décision ouverte`, **mieux située** ; **aucune réduction de compte**.

---

## 5. Audit froid `[différé par conception]`

Ce verdict n'est **pas un positif-gate** (délimitation, aucune réduction de `{A4 ; A2★ ; N}`).
L'audit incognito séparé est **différé par conception** (précédent F4), **réversible**. **Ré-armement
obligatoire** : avant toute propagation de la formule **« OC adressé / pont fait »** (point N2, le plus
fort), ou si une construction future s'appuie sur le pont `u_ère→C_F`. Instrument prêt : sceau
`verif_A2_numerique.py` + ce verdict + cadrage gelé.

---

## 6. Propagation additive `[à exécuter sur GO séparé]`

Non incluse ici (housekeeping ultérieur, file-by-file) : `00_index` (+1 chaînon, carte) ;
`03_glossaire` (entrée *A2★ numérique / non-cascade additive*) ; `LC-WORK-BRANCHE-FALSIFIABILITE`
(repoint A2★ « mieux située, OC adressé ») ; `LC-AUDIT-VERDICT §8bis` (consignation de l'audit
différé S-A2N). **Aucune avant GO.**

---

> **SANS SURCLASSEMENT (§6.4).** Un modèle posé n'est pas un acquis ; un soutien mésoscopique n'est
> pas un théorème générique 3D (OA persiste). « OC adressé » est **conditionnel** (amplitude bornée
> par la géométrie). `{A4 ; A2★ ; N}` **INCHANGÉ** ; A2★ ni prouvée ni réfutée ; C7 non levée ; D1
> non clos ; N non fixé ; CCC non démontrée.
