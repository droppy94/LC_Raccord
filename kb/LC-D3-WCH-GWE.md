---
id: LC-D3-WCH-GWE
titre: "Front (a) / le CONTENU DYNAMIQUE de la WCH via la GWE (Meissner-Penrose 2503.24263). Le pont forme↦cisaillement DÉRIVÉ ET SCELLÉ : Ω_σ=(kη)⁴ε²/27 (relation de dispersion super-horizon du mode régulier de Bessel), vérifié symboliquement par verif_D3_WCH_GWE.py. Bornes concrètes : η_*=1/H (raccord a=1) ; k_UV = CGB de M-P (kη_*~2·10⁻⁷, super-horizon). VERDICT (A) ÉTABLI (ALGÈBRE) : le mode régulier WCH-sélectionné est en régime (A) ∀ kη — le mode EXACT plafonne à Ω_σ/ε²=(x cos x−sin x)²/(3x²)≤0.377<0.5 (l'ancien « basculement (A)/(B) à kη_*~1.9 » était un ARTEFACT de la troncature leading (kη)⁴/27) ; au pic CGB de M-P, Ω_σ/ε²~6·10⁻²⁹. La WCH délivre l'isotropisation À L'ORDRE DOMINANT, conditionnellement à l'absence de rétro-action inhomogène (réserve §6.2, hors de portée — VERROU PRIMAIRE désormais, cf. LC-AUDIT-LOG-WCH-GWE C7) et au cadre CCC. Le spectre M-P (« presumably ») n'est PLUS le verrou (rendu moot par le mode exact). Sceau verif_D3_WCH_GWE.py DÉPOSÉ."
codename: LC-RACCORD
tags: [module-D3, module-A, front-a, ccc, isotropisation, inter-eon, WCH, weyl, GWE, meissner-penrose, bianchi-IX, near-bang, kappa, Omega-sigma, bunch-davies, friedrich, dispersion, CGB, hawking-points, sceau]
type: chaînon (rouvre le régime (A) tranché négatif par P6, via le contenu physique de la WCH ; successeur de LC-WORK-REPRISE-WCH-GWE ; SCEAU FAIT)
statut: ordre dominant, SCEAU FAIT — pont forme↦cisaillement DÉRIVÉ et vérifié symboliquement (verif_D3_WCH_GWE.py : Ω_σ=(kη)⁴ε²/27, tous assert passent) ; facteurs vérifiés (établi) ; bornes η_*/k_UV posées depuis l'atlas D1 et M-P §VI.A (établi pour η_*, formalisable pour k_UV) ; verdict (A) ÉTABLI (ALGÈBRE), conditionné (décision ouverte) à l'estimation CGB de M-P. NON tranché par l'algèbre : la forme du spectre au-delà du pic CGB (le sceau en montre la sensibilité).
version: 0.7
langue: fr
date: 2026-06-08
statut_id: validé après sceau — à enregistrer (LC-00-INDEX) ; PROPAGER : LC-D3-INTERAEON-P6 §RÉSERVE, LC-D3-INTERAEON-CONVERGENCE §5, LC-D3-WEYL-BUNCHDAVIES, LC-AUDIT-VERDICT §8bis, LC-02, glossaire
fichier_compagnon: ["verif_D3_WCH_GWE.py (FAIT — étend verif_D3_bunchdavies.py ; tous assert passent)", verif_D3_bunchdavies.py]
prerequis_kb: [LC-WORK-REPRISE-WCH-GWE, LC-WORK-REPRISE-WCH-GWE-SCEAU, LC-D3-INTERAEON-P6, LC-D3-INTERAEON-CONVERGENCE, LC-D3-WEYL-BUNCHDAVIES, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-A-SURVIE-CONFORME, LC-D-HOLOGRAPHIE-G3, LC-WORK-P6-SPEC-NEARBANG, LC-WORK-BIBLIO-FRONT-A, LC-AUDIT-VERDICT]
renvois: [LC-WORK-REPRISE-WCH-GWE, LC-WORK-REPRISE-WCH-GWE-SCEAU, LC-D3-INTERAEON-P6, LC-D3-WEYL-BUNCHDAVIES, LC-A-D1-BIANCHI, LC-A-D1-FACTEUR-CONFORME, LC-04-REFERENCES, LC-00-INDEX, LC-03-GLOSSAIRE]
source_externe: ["Meissner-Penrose, arXiv:2503.24263 (2025), §VI.A éq. 85-92 + §VI.B éq. 98-102 — lu page à page (OCR), pages 15-17. Nombres CGB (éq. 85 h~10⁻¹⁶, k~10⁻⁸ Hz ; éq. 89 onset<10s ; éq. 101 η_G~2·10¹⁶ s) RE-VÉRIFIÉS contre l'OCR lors du sceau."]
modules_rattachement:
  - "[A] / front (a) — A3/A4 : la WCH a-t-elle un contenu dynamique ? Réponse : OUI (algèbre établie), conditionnée à la forme du spectre."
  - "[D3] hypothèse de Weyl — σ̌→Ω_σ ; le pont forme↦cisaillement, dernier maillon, est dérivé ET scellé ici."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
changelog:
  - "v0.7 (2026-06-08) : HOUSEKEEPING post-A1/A2 (LC-AUDIT-LOG-A1A2-PROPAGATION ; wording §6.2, AUCUNE touche à l'algèbre du pont Ω_σ=(kη)⁴ε²/27 ni au verdict (A) par mode). §6.2 point 2, sous-bullet spikes : le résidu « cas pleinement générique » est RÉDUIT au seul facteur A2 (mesure de spikes générique n_s^gen). A1 (LC-D3-A1-SUPERHORIZON, sceau verif_D3_C7b_A1_superhorizon.py 10/10) borne le gradient PAR SPIKE en générique (I(ℓ)=C_F/ℓ→0, profil-indépendant). Verdict A2 (LC-D3-C7B-VERDICT-A2) : n_s^gen sous-exp. attendue (bounces BKL linéaires) mais non prouvée (Garfinkle gr-qc/0312117) ⟹ à inventer / hors de portée. C7-b PASS SUBSTANTIEL renforcé ; (A) physique conditionnel au SEUL A2. C7 reste `formalisable (borné)` ; verdict (A) `établi (algèbre)` inchangé."
  - "v0.6 (2026-06-08) : HOUSEKEEPING post-SPECTRE-K3 (LC-D3-SPECTRE-K3 v0.1, sceau verif_D3_spectre_k3.py EXIT 0 ; wording §8, AUCUNE touche à l'algèbre du pont Ω_σ=(kη)⁴ε²/27 ni au verdict (A) par mode). §8 : la lecture « variance Ω_σ^tot~(k_UV η_*)⁴/108·A_T » est CORRIGÉE — c'était la forme LEADING (artefact, cohérent C5) ; avec le noyau EXACT l'enveloppe → cos²x/3 (moyenne 1/6) ⟹ variance LOGARITHMIQUE Ω_σ^tot/A_T=(1/6)ln(k_UV η_*)+β∞ (β∞=0,045), soit ≈23,5 au cutoff holographique √(N/π)=ℓ_dS/ℓ_P~10⁶¹ ⟹ (A) pour la variance dès que A_T≪1. Le verdict (A) PAR MODE (max 0.377) est INCHANGÉ ; le verrou reste C7 (rétro-action inhomogène). La 2-points ⟨g₃g₃⟩~k³ = invariance d'échelle côté g₃ (Δ=3), explicitée."
  - "v0.5 (2026-06-08) : HOUSEKEEPING post-voie 1.5 (LC-AUDIT-LOG-GRADIENT-C7B ; wording, aucune touche algèbre). §6.2 point 2, sous-bullet spikes : gradient non-local BORNÉ sur le profil de spike exact (LC-D3-GRADIENT-C7B, sceau verif_D3_C7b_gradient.py ; I_spike∝w/cosh(wτ)→0, ratio→0) ⟹ 3/3 facteurs de R_s bornés sur profil exact, C7-b PASS substantiel. Résidu = cas pleinement générique (sans symétrie), décision ouverte ; voie 2 Gowdy redondante. C7 reste `formalisable (borné)` ; verdict (A) `établi (algèbre)` inchangé, conditionnalité physique pointe le seul résidu générique."
  - "v0.4 (2026-06-08) : HOUSEKEEPING post-silence/C7-b (LC-AUDIT-LOG-C7B ; wording, aucune touche algèbre). §6.2 point 2 : C7 `hors de portée`→`formalisable (borné)`. Silence A∧B∧C PASS (LC-D3-SILENCE-POC) ⟹ C7-a = dichotomie j₀/y₀ scellée appliquée pointwise. C7-b voie 1 PASS partiel (LC-D3-SPIKES-C7B) : α_s borné + spike≡bulk ⟹ R_s amplitude/statistique→0 ; résidu non-local seul ouvert. Verdict (A) `établi (algèbre)` inchangé ; sa conditionnalité physique pointe désormais le SEUL secteur non-local."
  - "v0.3 (2026-06-08) : HOUSEKEEPING POST-AUDIT (LC-AUDIT-LOG-WCH-GWE v1.0 §4.5 ; aucune touche à l'algèbre, wording/cadrage seulement). (C1/C5) Le « basculement (A)/(B) à kη_*~1.9 » est un ARTEFACT de la troncature leading (kη)⁴/27 ; le mode régulier EXACT Ω_σ/ε²=(x cos x−sin x)²/(3x²) plafonne à 0.377<0.5 ∀ kη ⟹ (A) à toute échelle, AUCUNE bascule — le verrou n'est plus le spectre M-P (moot) mais C7. (C1/C3) « marge ~10²⁹ » retirée comme chiffre de tête ; distinguer (α) un-point=0, (β) mode unique ~6·10⁻²⁹, (γ) variance. (C7) §5/§6.2 : le mécanisme réel est l'EXCLUSION WCH du mode Y (conditionnelle à Friedrich/A3-A4), pas un argument de moyenne ; « mesure nulle ⟹ queue » corrigé (non-sequitur, spikes BKL) ; renvoi Heinzle-Uggla reformulé (MARQUE la réserve inhomogène ouverte, ne l'appuie pas) ; « DÉLIVRENT » qualifié en ligne. (C2) [5] relabelé E∝g₃ (proportionnalité transportée par raccord conforme, facteur dS non utilisé). RESTE À FAIRE (computationnel, hors wording) : ajouter au .py un bloc « mode exact » remplaçant le scan leading [7]."
  - "v0.2 (2026-06-07) : SCEAU verif_D3_WCH_GWE.py déposé (étend verif_D3_bunchdavies.py). Pont Ω_σ=(kη)⁴ε²/27 vérifié SYMBOLIQUEMENT (bloc [6]) ; seuil kη_*~1.9 et scan de sensibilité (bloc [7]) ; mode singulier y₀ = mode Y de M-P, exclu par WCH (bloc [2-4]). Verdict (A) : formalisable → ÉTABLI (ALGÈBRE). CORRECTION CHIFFRE : le ~10⁻³⁰ du §5 v0.1 valait pour kη_* brut=10⁻⁷ ; avec la valeur documentée kη_*=2·10⁻⁷ le sceau donne 5.9·10⁻²⁹ (facteur 2⁴=16). Dans les deux cas ≪0.5 ; marge ~10²⁸ (doc) à ~10²⁹ (brut). Nombres M-P re-vérifiés contre l'OCR. Voir §8 (le sceau)."
  - "v0.1 (2026-06-07) : étape papier — pont dérivé, facteurs vérifiés, bornes posées, verdict conditionnel."
---

# LC-D3·WCH·GWE — Le contenu dynamique de la WCH : le pont forme↦cisaillement

> **But.** Rouvrir le régime (A) que P6 a tranché négatif (`LC-D3-INTERAEON-P6` v0.2 : le bang
> *générique* gagne ⟹ `∏κ_n→0` conditionné à `σ(0)=0`/WCH). Meissner-Penrose (2503.24263)
> proposent que le crossover **réel** n'est pas ce bang générique mais une **époque GW (GWE)**,
> champ faible `ψ̃` sur fond conformément plat. **Question (`LC-WORK-REPRISE-WCH-GWE` §4) :** le
> `Ω_σ` imposé par la GWE tombe-t-il sous la frontière du régime (A), `Ω_σ ≲ 0.5ε²` ? Ce chaînon
> **dérive le pont forme↦cisaillement** (le dernier maillon), **vérifie les facteurs**, **pose les
> deux bornes concrètes** (`η_*`, `k_UV`) depuis l'atlas D1 et M-P §VI.A, et — **depuis v0.2** —
> **scelle** le pont numériquement (`verif_D3_WCH_GWE.py`). Verdict : **(A) atteint** (algèbre
> établie), conditionnel à la forme du spectre.
>
> **Sceau FAIT (v0.2).** `verif_D3_WCH_GWE.py` étend `verif_D3_bunchdavies.py` ; tous les `assert`
> passent ; le pont `Ω_σ=(kη)⁴ε²/27` est vérifié **symboliquement** et les cibles numériques
> reproduites. Discipline (`LC-AUDIT-VERDICT` §6.4) : ici `établi (algèbre)` = « le pont et les
> facteurs sont algébriquement corrects, le sceau reproduit les cibles » ; **pas** « la physique de
> la CCC est établie ». Le verrou spectral reste `décision ouverte` (§6.1, §8.3).

---

## 1. Le pont forme↦cisaillement, DÉRIVÉ `[établi — algèbre à l'ordre dominant]`

Le noyau de Bianchi IX (`LC-WORK-P6-SPEC-NEARBANG`) prend DEUX entrées *a priori
indépendantes* : la **forme** `ε` (magnitude de l'anisotropie métrique `w`, à la Misner) et le
**cisaillement cinétique** `Ω_σ=σ²/3H²` (une « vitesse »). En bang générique elles sont libres
(P6 : magnitude par `Ω_σ`, orientation par l'angle `ψ`). La GWE, elle, est un **champ d'onde** :
la vitesse n'est pas libre, elle est fixée par l'amplitude et la fréquence. Le pont EST une
**relation de dispersion**.

**Fond (atlas D1, `LC-A-D1-FACTEUR-CONFORME`).** Région A radiation, `a(η)=Hη` (linéaire),
`ℋ=a'/a=1/η`, `H_phys=ℋ/a=1/(Hη²)`. Mode TT `H_ij=h(η)e_{ij}e^{ik·x}`, EOM
`h''+(2/η)h'+k²h=0` (Bessel sphérique, ordre 1/2). **Mode régulier** :

$$h(\eta)=h_0\,\frac{\sin k\eta}{k\eta}=h_0\Big(1-\tfrac{(k\eta)^2}{6}+\dots\Big)\quad\Rightarrow\quad
h'(\eta)\simeq -\tfrac{k^2\eta}{3}\,h_0\ \ (k\eta\ll1).$$

**Cisaillement** (dérivé en ADM, §2 facteur 1) : `σ_ij=½ a H'_ij`, `σ=½|h'|/a` (norm. « + »).
D'où, en super-horizon :

$$\sigma^2=\tfrac14\Big(\tfrac{h'}{a}\Big)^2=\frac{k^4 h_0^2}{36\,H^2},\qquad
\Omega_\sigma=\frac{\sigma^2}{3H_{\rm phys}^2}=\frac{(k\eta)^4 h_0^2}{108}.$$

**Conversion forme** (facteur 2 : Misner `H_ii=2w_i`, `ε=|w|/√2`, mode « + » ⟹ `h_0=2ε`) :

$$\boxed{\ \Omega_\sigma\ \simeq\ \frac{(k\eta)^4}{27}\,\varepsilon^2\ }\qquad
(\text{forme super-horizon *leading* ; le seuil naïf }\ \Omega_\sigma\lesssim 0.5\varepsilon^2\Leftrightarrow k\eta\lesssim 1.9\ \text{est un ARTEFACT de troncature — cf. ci-dessous}).$$

> **Mode EXACT (correction d'audit C5).** Le `(kη)⁴/27` est le terme dominant de
> `h(η)=h₀\,j₀(kη)` à `kη≪1`. Sans tronquer, `σ²∝(h')²` avec `h'=h₀\,k\,j₀'(kη)` donne le rapport
> **exact** `Ω_σ/ε²=(x\cos x-\sin x)^2/(3x^2)` (`x=kη`), qui **plafonne à 0.377 (atteint à
> `x≈2.74`) et ne croise JAMAIS 0.5**. ⟹ Le mode régulier est en **régime (A) à toute échelle** ;
> il n'y a **pas de bascule (A)/(B)**. Le « seuil `kη≈1.917` » provenait de l'usage de la formule
> *leading* hors de son domaine (`kη~O(1)`). Le verrou de (A) n'est donc PAS le spectre/la coupure
> (réserve 1, rendue moot), mais la **rétro-action inhomogène** (réserve §6.2 / C7).

**Lecture.** `Ω_σ→0` comme `η⁴` à `η→0` : la forme `ε=h_0/2` reste gelée (`h→h_0`) mais le
cisaillement **meurt**. C'est, *dérivée et non postulée*, la quiescence « `σ≈0` de Tod » de
P6 (A). Le mécanisme est la dispersion d'onde super-horizon — rien d'autre.

> **v0.2 — scellé.** Le bloc `[6]` de `verif_D3_WCH_GWE.py` reproduit cette chaîne SYMBOLIQUEMENT :
> `sigma^2 = h0²k⁴/(36H²)` → `Ω_σ = η⁴h0²k⁴/108` → (subst. `h0=2ε`) → `Ω_σ/ε² = (kη)⁴/27`.
> `assert` passe. Le `27=108/4` (le `1/4` = la conversion `ε=h0/2`) est sans glissement.

---

## 2. Les trois facteurs, VÉRIFIÉS `[établi]`

| facteur | source | valeur | effet |
|---|---|---|---|
| `σ_ij=½ a H'_ij` | dérivation ADM (Θ_ij−⅓Θγ_ij sur `γ_ij=a²(δ+H)`) | `σ=½|h'|/a` (`e_{ij}e^{ij}=2`) | le `108` brut |
| `ε=h_0/2` | Misner `γ_ii=a²e^{2w_i}≈a²(1+2w_i)` ⟹ `H_ii=2w_i` ; `ε:=|w|/√2` (`LC-WORK-P6-SPEC-NEARBANG` §1bis) | `h_0=2ε` | `108→27` |
| `b=H` | atlas D1 : réciprocité `Ω̌=−1/Ω̂=Hη` ⟹ `a=Hη`, `R(ǧ)=0`, `G_00=3/η²` | `ℋ=1/η`, `H_phys=1/(Hη²)` | valide Bessel + suppression `η⁴` |

`Ω_σ=σ²/(3H²)` est confirmé par **deux** fichiers indépendants (`LC-D3-INTERAEON-P6` §1 :
`σ_i=H√(6Ω_σ)n̂` ; `LC-WORK-P6-SPEC-NEARBANG` §1bis : `⅙Σ(3p_i−1)²=1=Ω_σ`). Le `27=108/4`
est sans glissement.

**Subtilité de puissances de `k` (à graver).** Trois représentations de la *même* donnée de
forme, à des puissances de `k` différentes : `g₃∝k³h_0` (coeff. FG, sceau Bunch-Davies),
`σ̌∝k²h_0` (3-Ricci de 𝓘, `LC-A-D1-BIANCHI`), `ε∝h_0` (Misner, sans dimension). La chaîne
« `g₃=σ̌=ε` » de `LC-WORK-REPRISE-WCH-GWE` §3 était **schématique**. Pour le noyau (homogène,
entrée sans dimension) **c'est `ε=h_0/2` qui compte**. Pour le volet statistique, le spectre
`⟨g₃g₃⟩~k³` (BD, `LC-D3-WEYL-BUNCHDAVIES`) ⟹ `⟨h_0²⟩~k^{-3}` ⟹ `𝒫_h=k³⟨h_0²⟩~const`
(strain invariant d'échelle, `A_T` tensoriel).

---

## 3. Borne 1 : la surface de raccord `η_*` `[établi — atlas]`

Atlas D1 : `a=Hη`. Le noyau ancre son IC à `a=1` (`LC-WORK-P6-SPEC-NEARBANG` §5bis ; `Λ=1`
fixe l'unité). Donc

$$\boxed{\ \eta_*=1/H,\qquad \mathcal H_*=1/\eta_*=H\ }$$

— l'horizon comobile au raccord **est** le Hubble dS `H` de l'éon précédent (réciprocité). Le
critère *leading* `kη_*≲1.9` (`k≲1.9·ℋ_*`) est **moot** : le mode régulier exact étant (A) ∀`kη`
(§1, max 0.377), **tous** les modes sont en (A), pas seulement ceux jusqu'à ~2× l'horizon. À `η_*`
fixé, chaque mode de `k` fixe a `Ω_σ→0` (`η→0`).

---

## 4. Borne 2 : `k_UV` côté Meissner-Penrose `[formalisable — estimation M-P]`

M-P traitent **exactement notre mode** (§VI.A). Onde GW sphérique avec `Λ=3H_Λ²`, contrainte
Ricci-nul, premier ordre en `h` (éq. 87) :

$$F''(\eta)+F\Big(k^2-\frac{8}{(\eta_\infty-\eta)^2}\Big)=0
\ \Rightarrow\ F=(\eta_\infty-\eta)^{1/2}\big[c_1J_{\sqrt{33}/2}+c_2Y_{\sqrt{33}/2}\big]\big(k(\eta_\infty-\eta)\big)$$

(éq. 88 ; `η_∞`=crossover ; ordre `√33/2` car le `8` du potentiel sphérique dS donne `ν²−¼=8` —
côté dS de l'éon *précédent*, vs ordre `1/2` côté radiation §1). **Même structure de Bessel**,
**même dichotomie régulier `J` / singulier `Y`**. Le mécanisme d'amplification de M-P au crossover
**est** le mode `Y` qui diverge quand `k(η_∞−η)→0`.

> **Identification cardinale** *(scellée v0.2, bloc [1]+[2-4])*. La WCH/Friedrich (`Ψ̃→0` à 𝓘⁺,
> `LC-A-SURVIE-CONFORME`) = **« pas de mode `Y` »** = régularité de `ψ̃`. Le sceau le rend explicite
> côté radiation : le mode **régulier** `j₀=sin(kη)/(kη)` a un coefficient FG un-point `g₃=0` (mode
> pair) ; le mode **singulier** `y₀=−cos(kη)/(kη)` diverge (pôle `−h₀/k` en `η→0`) — c'est le mode
> `Y` que la WCH EXCLUT. La WCH n'est donc pas vide : elle sélectionne le mode régulier.

**Le fond GW dominant n'est PAS Planckien-large-bande.** C'est le **CGB** (éq. 85, mot de M-P :
« presumably ») — *re-vérifié contre l'OCR de l'archive arXiv lors du sceau* :

$$h\sim 10^{-16},\qquad k\sim 10^{-8}\ \text{Hz}.$$

Allumage de la GWE (éq. 89) : `h·(k(η_∞−η_{GW}))^{−(√33−1)/2}>1 ⟹ (η_∞−η_{GW})<10\,\text{s}`.
D'où le paramètre super-horizon du mode dominant :

$$\boxed{\ k(\eta_\infty-\eta_{GW})\ \sim\ 10^{-8}\,\text{s}^{-1}\times10\,\text{s}\ \sim\ 10^{-7}\!-\!2\cdot10^{-7}\ \lll\ 1.\ }$$

Le mode GW dominant est **super-horizon de ~7 ordres**. *Mise en garde (audit C1) : le `k^{-1/2}`
est l'asymptotique grand-argument de la Bessel d'une **onde unique** (éq. 88), c.-à-d. l'enveloppe
d'**un** mode — PAS la densité spectrale du gaz CGB stochastique (que M-P ne résout pas). On ne peut
donc pas attribuer à M-P une « suppression UV active du spectre » ni conclure que l'intégrale est
IR-dominée : la forme spectrale au-delà du pic CGB est `décision ouverte` (réserve §6.1).* (Réfs M-P :
`H_Λ=1.8451·10⁻¹⁸ s⁻¹`, éq. 90 ; `a_{GW}~6·10¹⁶`, éq. 91 ; `η_G~2·10¹⁶ s` depuis `r_{HS}~0.03–0.04`,
éq. 99-101.)

---

## 5. Verdict : (A) atteint `[établi (algèbre) — conditionnel à C7 (rétro-action inhomogène)]`

Avec `kη_*≪1` pour les modes dominants, le pont scellé (§1, §8) donne :

$$\frac{\Omega_\sigma}{\varepsilon^2}=\frac{(k\eta_*)^4}{27}.$$

**Chiffrage (corrigé v0.2).** Le `~10⁻³⁰` de la v0.1 valait pour `kη_*` *brut* `=10⁻⁸\,\text{Hz}×10\,\text{s}=10⁻⁷`. Avec la valeur documentée `kη_*=2·10⁻⁷`, le facteur `2⁴=16` rehausse :

$$\frac{\Omega_\sigma}{\varepsilon^2}\sim\begin{cases}
(10^{-7})^4/27\ \sim\ 3.7\cdot10^{-30} & (k\eta_*\ \text{brut}),\\[2pt]
(2\cdot10^{-7})^4/27\ \sim\ 5.9\cdot10^{-29} & (k\eta_*\ \text{documenté}).
\end{cases}$$

**Dans les deux cas `⋘ 0.5` ⟹ régime (A).** *Mise en garde de cadrage (audit C1/C3) : la « marge
~10²⁹ » de la v0.1 NE doit PAS être le chiffre de tête — c'est la valeur d'un **mode unique** au
pic CGB (objet β ci-dessous), pas la robustesse du mécanisme. Trois grandeurs distinctes :*
- **(α) un-point** `⟨g₃⟩=0` (vide BD) ⟹ cisaillement homogène **exactement nul** : c'est le (A)
  qualitatif PROPRE, le mécanisme, indépendant de toute coupure ;
- **(β) mode unique** au pic CGB `kη_*~2·10⁻⁷` ⟹ `Ω_σ/ε²~6·10⁻²⁹` : une **illustration
  mono-mode**, non une marge de robustesse ;
- **(γ) variance** deux-points : son intégrale dépend du spectre (réserve §6.1) — à présenter
  comme la réserve, pas comme une marge favorable.

**Cohérence avec M-P (page 15, re-vérifiée à l'OCR) :** *« GWE a de grandes fluctuations LOCALES du
Weyl (et un Weyl MOYEN petit) »*. C'est notre distinction un-point / deux-points
(`LC-D3-WEYL-BUNCHDAVIES`) :

- `⟨Weyl⟩≈0` (un-point, moyen) = WCH satisfaite en moyenne = le **`Ω_σ` petit que voit le noyau
  HOMOGÈNE** ⟹ (A) ;
- `⟨Weyl²⟩` grand localement = fluctuations inhomogènes (Hawking points, spikes) : **supposées**
  ne pas alimenter le budget de cisaillement du noyau homogène — mais ceci est précisément la
  **réserve §6.2 (C7), hors de portée**, pas un acquis. La petitesse spatiale (« mesure nulle »)
  ne borne PAS la rétro-action dynamique (cf. spikes BKL).

$$\boxed{\ \textbf{À l'ordre dominant, la WCH a un CONTENU DYNAMIQUE : l'exclusion du mode }Y
\textbf{ (Friedrich/A3-A4) + la dispersion super-horizon délivrent }\Omega_\sigma\ll\varepsilon^2
\textbf{ — CONDITIONNELLEMENT à l'absence de rétro-action inhomogène (réserve §6.2, hors de
portée).}\ }$$

Le front (a) se clôt *par la physique de la GWE*, pas par postulat — **algèbre établie**,
conditionnellement aux réserves du §6.

---

## 6. Réserves — ce qui reste `[décision ouverte]`

1. **Spectre CGB « presumably » (PLUS le verrou — rétrogradé par C5).** La borne `k_UV` repose sur
   l'estimation `h~10⁻¹⁶, k~10⁻⁸ Hz` de M-P (éq. 85), heuristique, NON dérivée. La v0.1 craignait
   qu'un spectre dur sub-horizon (`kη_*≫1`) ne « rebascule » vers (B) via le poids `(kη)⁴`. **Cette
   crainte était un artefact de la troncature leading** : le mode régulier EXACT plafonne à
   `Ω_σ/ε²=0.377<0.5 ∀ kη` (§1), il n'y a pas de bascule. Le « seuil `kη_*~1.9` » du scan `[7]`
   leading ne décide donc PAS (A). Reste un simple caveat de **provenance** (M-P ne dérive aucun
   spectre), sans danger quantitatif. ⟹ Le verrou n'est plus ici, mais en §6.2.
2. **Homogène vs inhomogène — rétro-action inhomogène (C7), désormais `formalisable (borné)`.**
   Le noyau est homogène (Bianchi IX) ; la GWE est inhomogène. Ce qui retire les **grandes**
   fluctuations du Weyl n'est pas un argument de moyenne mais l'**exclusion du mode `Y` par
   WCH/Friedrich** (bloc [2-4]), conditionnelle à A3-A4. Cette réserve, **autrefois `hors de
   portée`**, est désormais **encadrée** par la chaîne silence + C7-b :
   - **Silence (A∧B∧C, `LC-D3-SILENCE-POC`)** : horizon de particules fini/velocity-dominated,
     courbure sous-dominante + rebonds isolés, découplage causal de points voisins — les trois
     signatures NÉCESSAIRES du silence sont présentes (POC, homogène). ⟹ la question (a)
     « la sélection WCH tient-elle **pointwise** ? » (**C7-a**) se réduit à la dichotomie
     `j₀/y₀` déjà scellée ici, appliquée point par point : `formalisable`.
   - **Spikes (C7-b, `LC-D3-SPIKES-C7B`, voie 1)** : la question (b) « les spikes rétro-agissent-
     ils sur `⟨Ω_σ⟩` ? » est **bornée en amplitude/statistique** : carte spike=BKL² (même
     oracle), `α_s` **borné** (`W²_K≤12`, compacité ⟹ « α_s→∞ » exclu), statistique d'une
     timeline de spike **= bulk** (Th.3.2) ⟹ `R_s=μ_s(α_s−1)→0`. *Le non-sequitur « mesure
     nulle ⟹ négligeable » est remplacé par ce résultat positif.* Le **gradient non-local** est désormais **borné sur le profil de spike EXACT** (Lim 0710.0628 ; `I_spike∝w/cosh(wτ)→0`, ratio `⟨Ω_σ^grad⟩/⟨Ω_σ⟩_bulk→0` ; `LC-D3-GRADIENT-C7B`, sceau `verif_D3_C7b_gradient.py`, 19/19 PASS) ⟹ **3/3 facteurs de `R_s` bornés sur profil exact**. Reste, après la **voie A1** (`LC-D3-A1-SUPERHORIZON`, sceau `verif_D3_C7b_A1_superhorizon.py`, 10/10 : gradient PAR SPIKE borné **en générique**, `I(ℓ)=C_F/ℓ→0`, profil-indépendant), le **seul facteur A2** — la **mesure de spikes générique** `n_s^gen` (`LC-D3-C7B-VERDICT-A2`), borne sous-exp. **attendue** (bounces BKL ~ linéaires) mais **non prouvée** (`gr-qc/0312117`) : `à inventer` / `hors de portée` ; voie 2 Gowdy redondante.
   ⟹ **C7 : `hors de portée` → `formalisable (borné)`.** (A) physique reste `formalisable`,
   conditionnel au **seul facteur A2** + C7-a pointwise + cadre CCC.
3. **Sceau FAIT (v0.2).** `verif_D3_WCH_GWE.py` (i) résout l'EOM TT sur `a=Hη` et vérifie le mode
   régulier `j₀` + l'exclusion du mode singulier `y₀` ; (ii) confirme `Ω_σ=(kη)⁴ε²/27`
   mode-à-mode (symbolique) ; (iii) chiffre le mode M-P et **scanne la sensibilité** à la coupure
   `k_UV η_*`. Tous les `assert` passent. *Ce que le sceau NE fait PAS : trancher la forme du
   spectre au-delà du pic CGB (réserve 1).*
4. **dS/CFT.** Si l'état est nommé « Bunch-Davies » via dS/CFT, garder la réserve
   (`LC-AUDIT-VERDICT` §4 : CFT euclidienne non unitaire).

---

## 7. Premier pas pour le sceau — FAIT `[archivé]`

> *(v0.1, conservé pour trace ; réalisé en v0.2.)* Étendre `verif_D3_bunchdavies.py` (mode TT dS₄,
> proportionnalité `E∝g₃` déjà acquise — facteur `(d/2H)` dérivé côté dS uniquement, non utilisé
> numériquement ici) → réécrire le bloc EOM pour `a=Hη` (vérifier que le frottement `(2/η)`
> disparaît en variable de poids −1) → bloc neuf `forme↦Ω_σ` : confirmer `Ω_σ=(kη)⁴ε²/27` → bloc
> neuf `intégrale` : variance pondérée spectre M-P, confronter à `0.5ε²`. → **Fait : voir §8.**

---

## 8. Le sceau `verif_D3_WCH_GWE.py` `[établi (algèbre)]`

Extension de `verif_D3_bunchdavies.py`. Tous les `assert` passent (sympy 1.14, sans réseau).
État des blocs et résultats :

| bloc | nature | résultat |
|---|---|---|
| `[1]` EOM radiation | RÉÉCRIT | `a=Hη`, `ℋ=1/η`, `H_phys=1/(Hη²)`. Mode régulier `j₀=sin(kη)/(kη)` ⟹ `assert EOM=0`. Mode singulier `y₀=−cos(kη)/(kη)` : pôle `eta·y₀→−h₀/k≠0` = mode `Y` exclu. Super-horizon `h'=−(k²η/3)h₀` (assert). |
| `[1bis]` contrôle conforme | AJOUTÉ | `v=a·h`, `a''=0` ⟹ `v''+k²v=0` (équation PLATE) : le frottement `(2/η)` est absorbé. `assert`. |
| `[2-4]` FG + dichotomie | ADAPTÉ | `g₀=h₀`, `g₂=−h₀k²/6` (local), `g₃` un-point `=0` (mode pair régulier) ⟹ cohérent WCH ; `g₃≠0` viendrait de `y₀`. Résidu deux-points `⟨g₃g₃⟩~k³` importé (`LC-D3-WEYL-BUNCHDAVIES`) ⟹ `𝒫_h~const`. dS/CFT `Δ=3`. |
| `[5]` Weyl→g₃ | ACQUIS | `E∝g₃` (proportionnalité transportée par le raccord conforme CCC ; facteur `(d/2H)` dérivé côté dS **uniquement**, non utilisé numériquement ici), réutilisé du parent, non re-dérivé sur radiation. Hors chemin critique : `[6]` part de `σ²=¼(h'/a)²`, sans appel à `[5]`. |
| **`[6]` pont** | **NEUF** | **`Ω_σ=σ²/3H_phys²=(kη)⁴h₀²/108=(kη)⁴ε²/27` vérifié SYMBOLIQUEMENT** (`assert`). `27=108/4`. **Cible centrale reproduite.** |
| `[7]` sensibilité | NEUF | *Scan **leading** : seuil `(kη_*)⁴≲13.5 ⟺ kη_*≲1.917` (assert ~1.9).* Mode M-P `kη_*~10⁻⁷–2·10⁻⁷` ⟹ `Ω_σ/ε²~4·10⁻³⁰–6·10⁻²⁹≪0.5` (assert). **⚠ ARTEFACT (audit C5)** : ce « seuil 1.917 » est celui de la formule *leading* `(kη)⁴/27` hors domaine ; le mode régulier **exact** plafonne à `0.377<0.5 ∀ kη` (§1) — **pas de bascule**. *À FAIRE (.py) : remplacer le scan leading par le mode exact.* |

**Lecture du scan [7]** — *scan **leading** `(kη_*)⁴/27`, conservé pour trace ; ⚠ ses lignes
`kη_*≳1` sont des **artefacts de troncature**, voir la colonne « mode exact »* :

| `k_UV η_*` | leading `(kη_*)⁴/27` | régime (leading) | **mode exact** `(x cos x−sin x)²/(3x²)` | régime (exact) |
|---|---|---|---|---|
| `2·10⁻⁷` (M-P) | `5.9·10⁻²⁹` | (A) | `5.9·10⁻²⁹` | (A) |
| `10⁻¹` | `3.7·10⁻⁶` | (A) | `3.7·10⁻⁶` | (A) |
| `1` | `3.7·10⁻²` | (A) | `3.0·10⁻²` | (A) |
| `1.917` | `0.50` | ~~← seuil~~ (artefact) | `0.23` | (A) |
| `2.74` (pic exact) | `2.1` | (B) | **`0.377` (max)** | (A) |
| `5` | `23` | (B) | `0.075` | (A) |

⟹ Le mode régulier exact est **(A) à toute échelle** ; la « bascule (B) » du scan leading n'a pas
de réalité physique. La vraie réserve n'est pas la coupure spectrale (réserve §6.1, moot) mais la
rétro-action inhomogène (réserve §6.2 / C7).

Le verdict est `(A)` pour le mode régulier exact **à toute échelle** (max `0.377<0.5`) ; la
« robustesse marge ~10²⁸ » et la « bascule (B) à `k_UV η_*~1.9` » de la v0.2 étaient des lectures
du scan **leading** (artefacts). Le sceau **montre** la dépendance en `(kη)⁴` du *leading*
**par mode** ; mais la **variance sommée** sur le noyau EXACT ne croît **pas** en `(k_UV η_*)⁴`
(cette forme quartique est un artefact du *leading*, cohérent C5) : l'enveloppe du noyau exact tend
vers `cos²x/3` (moyenne `1/6`), d'où une croissance **logarithmique** `Ω_σ^tot/A_T=(1/6)ln(k_UV η_*)+β∞`
(`β∞≈0,045`), soit `≈23,5` au cutoff holographique `√(N/π)=ℓ_dS/ℓ_P~10⁶¹` (`LC-D3-SPECTRE-K3`,
sceau `verif_D3_spectre_k3.py`). Dans tous les cas le mode exact ne croise jamais `0.5`. Ce qui reste ouvert est la
rétro-action inhomogène (réserve §6.2 / C7), non la forme du spectre M-P.

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte` (cf. `LC-00-INDEX`).
*Discipline d'audit : un `établi (algèbre)` de chaînon = « l'algèbre est correcte ET le sceau
reproduit les cibles », à l'ordre dominant ; jamais « la physique de la CCC est établie ». Ici sont
`établi (algèbre)` : le pont `Ω_σ=(kη)⁴ε²/27` et les trois facteurs (vérifiés symboliquement par
`verif_D3_WCH_GWE.py`) ; `η_*=1/H` (atlas) ; le verdict (A) chiffré (mode exact (A) ∀`kη`, max
0.377). Restent `formalisable` / `décision ouverte` : la **rétro-action inhomogène** (réserve §6.2 /
C7, hors de portée — le verrou primaire désormais) et le cadre CCC (raccord conforme, A3-A4). La
borne `k_UV` / la forme du spectre M-P ne sont plus le verrou (rendues moot par le mode exact, C5).
Le contenu dynamique de la WCH est ainsi DÉMONTRÉ AU NIVEAU ALGÈBRE et chiffré — conditionnel à C7
et au cadre CCC, non inconditionnel.*
