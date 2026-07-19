---
id: LC-WORK-NACTION-AVEUGLE
titre: "Tâche de dérivation AUTONOME et AVEUGLE — calculer, à partir des seules définitions, le coefficient C_T de la deux-points du tenseur de stress de la CFT₃ céleste TELLE QUE LE PROGRAMME LA CALCULE (fonction d'onde dS), EXPRIMÉ dans la normalisation standard d'Osborn–Petkos, en unités ℓ_dS²/G. Objet purement cinématique/de normalisation. À EXÉCUTER EN CONVERSATION NEUVE SÉPARÉE : ne pas ouvrir LC-WORK-REPRISE-POST-R1 ni le bloc [C] de verif_D_CT_constructif.py avant d'avoir ENGAGÉ une valeur dérivée — ces fichiers contiennent une valeur recherchée et leur lecture préalable ANNULE la garantie anti-fit. La réconciliation (la valeur dérivée recoupe-t-elle la donnée holographique externe ?) se fait APRÈS engagement, ailleurs. Subordonnée à LC-AUDIT-VERDICT §6.4."
codename: LC-RACCORD
type: "tâche de dérivation aveugle (spec autoportante) — calcul de normalisation, agent séparé. N'est PAS un chaînon ; ne contient aucun résultat scellé."
version: 1.1
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v1.1 : CORRECTION DE PIÈGE (additif). Vérification (conversation contaminée, audit) : les trois prerequis_kb exposent la valeur recherchée — LC-D-CT-ATN et LC-D-CT-REALITE lourdement (magnitude/signe = charge utile de §4), LC-D-HOLOGRAPHIE-G3 partiellement (signe + scaling). De plus la valeur est diffuse dans ~26 fichiers KB. Or la spec §2 est AUTOPORTANTE (toutes les définitions y sont inlinées) : aucun prérequis KB n'est requis pour dériver. ⟹ prerequis_kb effectif = [] (ancien champ conservé, marqué superseded ; cf. prerequis_kb_effectif). Paquet de lancement propre (sans accès KB, hash-only) : LC-WORK-NACTION-AVEUGLE-PAQUET v1.1, attesté par verif_paquet_propre.py (EXIT 0, 13 asserts). | 2026-06-10 — v1.0 : pose la dérivation aveugle du facteur de normalisation reliant la lecture ⟨TT⟩ du programme (fonction d'onde dS) au C_T standard d'Osborn–Petkos. Aucune valeur cible inscrite. Protocole de blindure explicite."
statut: "À EXÉCUTER en conversation neuve séparée et aveugle. Engager une valeur AVANT toute réconciliation."
prerequis_kb: [LC-D-HOLOGRAPHIE-G3, LC-D-CT-ATN, LC-D-CT-REALITE]
prerequis_kb_effectif: []  # v1.1 — les 3 prérequis ci-dessus sont CONTAMINANTS (superseded) ; spec autoportante (§2 inline) ; agent aveugle = aucun accès KB
fichiers_compagnons_kb: []
tags_epistemiques: [établi (algèbre), à inventer]
---

# Tâche aveugle — `C_T` du programme en normalisation Osborn–Petkos

> **Protocole de blindure (lire en premier, impératif).** Cette tâche est routée ici
> **exprès** pour être exécutée par un agent qui **ignore la valeur recherchée**. Tu dois :
> 1. dériver le nombre demandé (§3) à partir des **seules définitions** de §2 ;
> 2. **engager** ta valeur (l'écrire, la sceller dans un `verif_*.py`) ;
> 3. **seulement ensuite** consulter la réconciliation externe.
> N'ouvre PAS `LC-WORK-REPRISE-POST-R1`, ni le bloc `[C]` de `verif_D_CT_constructif.py`, ni
> aucune note mentionnant un « facteur 4 » ou une valeur de `𝒩_action`, **avant l'étape 2**.
> Si tu rencontres une telle valeur avant d'avoir engagé la tienne, signale-le et arrête : la
> garantie est rompue, il faut un autre agent.

> **Note v1.1 (additive — correction de piège).** Le champ `prerequis_kb` d'origine
> (`LC-D-HOLOGRAPHIE-G3`, `LC-D-CT-ATN`, `LC-D-CT-REALITE`) est **superseded** : ces trois
> fichiers **exposent la valeur recherchée** (les deux derniers lourdement — c'est la charge
> utile de réconciliation §4). La valeur est par ailleurs **diffuse dans ~26 fichiers du KB**.
> Comme **§2 est autoportante** (toutes les définitions y sont inlinées), l'agent aveugle n'a
> besoin d'**aucun** fichier KB. Blindure robuste = **aucun accès `/mnt/project/`** (idéalement
> Incognito), pas une liste d'exclusion. Le paquet de lancement propre à remettre à l'agent est
> **`LC-WORK-NACTION-AVEUGLE-PAQUET`** (attesté par `verif_paquet_propre.py`, EXIT 0). Les noms
> d'indices que ce protocole mentionne ci-dessus (« facteur 4 », etc.) sont **retirés du paquet**
> remis à l'agent ; ils ne subsistent ici que comme guide pour le routeur (déjà contaminé).

---

## 1. Nature de la question `[normalisation pure]`

Le programme lit le coefficient de sa deux-points céleste `⟨TT⟩` directement sur la **fonction
d'onde dS** (route holographique de `CT-ATN`), dans **sa propre** variable d'impulsion. La
littérature holographique, elle, reporte le `C_T` du tenseur de stress dans la **convention
standard d'Osborn–Petkos** (position-espace). Question : **quel nombre vaut le `C_T` du
programme une fois exprimé dans la convention d'Osborn–Petkos, en unités `ℓ_dS²/G` ?**

C'est un facteur de **conversion de conventions** (cinématique + dictionnaire de
normalisation), pas une donnée dynamique. Il ne dépend d'aucun paramètre libre.

---

## 2. Définitions à utiliser `[et UNIQUEMENT celles-ci]`

- **Fonction d'onde dS** (`CT-ATN §2`). Mode bulk-to-boundary `H_k=(1+ikη)e^{−ikη}`,
  coefficient `F=(M_Pl²/4)a²(H'_k/H_k)`, séparation en `η→0⁻` :
  `a²(H'_k/H_k) = k²/(H²η)` (réel, divergent, = phase de contact) `− i k³/H²` (fini).
- **Tenseur de stress holographique** (FG/dHSS, `HOLOGRAPHIE-G3 §1`) :
  `⟨T_ij⟩ = (d/16πG) g₍d₎`, ici `d=3`.
- **Définition d'Osborn–Petkos** (cible de normalisation) :
  `⟨T_ij(x)T_kl(0)⟩ = (C_T/x^{2d}) 𝓘_{ij,kl}(x)`, avec
  `𝓘_{ij,kl} = ½(I_ik I_jl + I_il I_jk) − (1/d) δ_ij δ_kl`, `I_ij = δ_ij − 2x_i x_j/x²`.
- **Secteur TT** (`HOLOGRAPHIE-G3 §2 [B]`) : `g₃` = graviton = **2 polarisations** en `d=3`.
- **Conventions** : `M_Pl² = (8πG)^{−1}` ; `ℓ_dS = 1/H`.

Tu peux travailler en position ou en impulsion (l'identité de Fourier conforme
`∫d^dx e^{ikx}|x|^{−2Δ} = π^{d/2}2^{d−2Δ}Γ(d/2−Δ)/Γ(Δ)|k|^{2Δ−d}` est standard). Trace toute
convention de polarisation et de projecteur **explicitement**.

---

## 3. Livrable `[un nombre, dérivé puis scellé]`

$$C_T^{\text{prog (Osborn–Petkos)}} = c \cdot \frac{\ell_{dS}^2}{G},\qquad c = ?$$

Produire `verif_naction_aveugle.py` (EXIT 0) qui :
- pose les définitions de §2 ;
- dérive `c` symboliquement (sympy), en exhibant chaque facteur (Fourier, projecteur TT,
  dictionnaire `(d/16πG)`, polarisation) ;
- **sanity-checks sans donnée externe** : FT scalaire `d=3` = `π²/12` ; projecteur TT trace 2,
  idempotent ;
- **ancre de calibration croisée** (réservée à cet audit) : recouper la conversion de
  normalisation via une théorie de référence à `C_T` connu (scalaire conforme libre `d=3`),
  fetchée indépendamment ;
- imprime `c` et le scelle.

**Engage `c` (EXIT 0) AVANT de lire toute réconciliation.**

---

## 4. Réconciliation `[APRÈS engagement de c — pas avant]`

Une fois `c` scellé : comparer `c` à la valeur holographique externe (continuation
`ℓ_AdS→iℓ_dS`, signe par `i^{d−1}`, magnitude) reportée dans `LC-WORK-REPRISE-POST-R1`.
- accord en magnitude ⟹ **convergence** (`établi`, algèbre, cohérence de coefficients) ;
- désaccord ⟹ **NO-GO** net (laissé tel quel, sans rattrapage).

Discipline `§6.4` : une convergence éventuelle ne dit **rien** de « D1 fermé / N fixé / CCC
démontrée ». Compte `{A4 ; A2★ ; N}` **inchangé**.
