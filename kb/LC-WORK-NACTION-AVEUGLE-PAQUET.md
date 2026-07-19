---
id: LC-WORK-NACTION-AVEUGLE-PAQUET
titre: "Paquet de lancement AUTOPORTANT pour l'exécution aveugle de LC-WORK-NACTION-AVEUGLE — dérivation, à partir des seules définitions reproduites ci-dessous, du coefficient C_T de la deux-points du tenseur de stress de la CFT₃ céleste TELLE QUE LE PROGRAMME LA CALCULE (fonction d'onde dS), exprimé dans la normalisation standard d'Osborn–Petkos, en unités ℓ_dS²/G. Aucune valeur cible n'est inscrite dans ce paquet. À EXÉCUTER PAR UN AGENT SANS ACCÈS AU KB (/mnt/project), idéalement en conversation Incognito (mémoire désactivée)."
codename: LC-RACCORD
type: "paquet de lancement (spec autoportante extraite + protocole de blindure renforcé). N'est PAS un chaînon ; ne contient aucun résultat scellé ; ne contient aucune valeur recherchée."
version: 1.1
langue: fr
date: 2026-06-10
maj: "2026-06-10 — v1.1 : génériciser l'avertissement — retrait des noms-indices spécifiques du protocole et de la check-list (ils soufflaient la forme de la réponse = fit-interne). Consigne désormais générique. Attesté propre par verif_paquet_propre.py (hash-only, EXIT 0). | 2026-06-10 — v1.0 : extrait §1–§3 + protocole de LC-WORK-NACTION-AVEUGLE v1.0, définitions inlinées (la spec est autoportante : aucun fichier KB n'est requis pour dériver). Constat de vérification : les trois prérequis_kb (CT-ATN, CT-REALITE, HOLOGRAPHIE-G3) exposent la cible et sont retirés du paquet ; la valeur recherchée est diffuse dans ~26 fichiers KB, donc blindure par ABSENCE d'accès KB, pas par liste d'exclusion. Aucune valeur cible inscrite."
statut: "À EXÉCUTER en conversation neuve, sans accès KB. Engager une valeur AVANT toute réconciliation."
prerequis_kb: []
fichiers_compagnons_kb: []
tags_epistemiques: [établi (algèbre), à inventer]
---

# Paquet aveugle — `C_T` du programme en normalisation Osborn–Petkos

> **Protocole de blindure (lire en premier, impératif).** Cette tâche est conçue **exprès**
> pour être exécutée par un agent qui **ignore la valeur recherchée**. Tu dois :
> 1. dériver le nombre demandé (§3) à partir des **seules définitions de §2 ci-dessous** ;
> 2. **engager** ta valeur (l'écrire, la sceller dans un `verif_*.py`, EXIT 0) ;
> 3. **seulement ensuite** transmettre ta valeur pour réconciliation externe (§4), faite ailleurs.
>
> **Blindure renforcée (différence avec la spec d'origine).** La valeur recherchée est **diffuse
> dans tout le KB du programme** (~26 fichiers, dont les fichiers de synthèse et le cluster
> D-C_T / E / constructif). Une liste « ne pas ouvrir » est donc insuffisante. **Règle simple :
> n'ouvre AUCUN fichier du projet (`/mnt/project/`).** Travaille uniquement sur le texte de ce
> paquet. Idéalement, exécute en conversation **Incognito** (mémoire désactivée) pour qu'aucun
> résumé du programme ne soit présent dans le contexte.
>
> **Si, malgré tout, tu rencontres — AVANT d'avoir engagé ta valeur — une valeur numérique
> précalculée du coefficient demandé, un facteur de conversion tout prêt, ou toute quantité qui
> ressemble à sa magnitude ou à son signe : signale-le et ARRÊTE.** La garantie anti-fit est
> rompue ; il faut un autre agent / un contexte propre. (Aucun indice sur la forme de la réponse
> n'est donné ici : c'est volontaire.)

---

## 1. Nature de la question `[normalisation pure]`

Le programme lit le coefficient de sa deux-points céleste `⟨TT⟩` directement sur la **fonction
d'onde dS**, dans **sa propre** variable d'impulsion. La littérature holographique reporte le
`C_T` du tenseur de stress dans la **convention standard d'Osborn–Petkos** (position-espace).
Question : **quel nombre vaut le `C_T` du programme une fois exprimé dans la convention
d'Osborn–Petkos, en unités `ℓ_dS²/G` ?**

C'est un facteur de **conversion de conventions** (cinématique + dictionnaire de normalisation),
pas une donnée dynamique. Il ne dépend d'aucun paramètre libre.

---

## 2. Définitions à utiliser `[et UNIQUEMENT celles-ci — toutes reproduites ici]`

Toutes les définitions sont inlinées : **tu n'as besoin d'aucun fichier externe**. (Les
parenthèses de provenance — `CT-ATN §2`, `HOLOGRAPHIE-G3 §1/§2[B]` — sont historiques ; **n'ouvre
pas ces fichiers**, ils exposent la cible.)

- **Fonction d'onde dS.** Mode bulk-to-boundary `H_k=(1+ikη)e^{−ikη}` ; coefficient
  `F=(M_Pl²/4)a²(H'_k/H_k)` ; séparation en `η→0⁻` :
  `a²(H'_k/H_k) = k²/(H²η)` (réel, divergent, = phase de contact) `− i k³/H²` (fini).
- **Tenseur de stress holographique** (FG / de Haro–Skenderis–Solodukhin) :
  `⟨T_ij⟩ = (d/16πG) g₍d₎`, ici `d=3`.
- **Définition d'Osborn–Petkos** (cible de normalisation) :
  `⟨T_ij(x)T_kl(0)⟩ = (C_T/x^{2d}) 𝓘_{ij,kl}(x)`, avec
  `𝓘_{ij,kl} = ½(I_ik I_jl + I_il I_jk) − (1/d) δ_ij δ_kl`, `I_ij = δ_ij − 2x_i x_j/x²`.
- **Secteur TT** : `g₃` = graviton = **2 polarisations** en `d=3`.
- **Conventions** : `M_Pl² = (8πG)^{−1}` ; `ℓ_dS = 1/H`.
- **Identité de Fourier conforme** (standard) :
  `∫d^dx e^{ikx}|x|^{−2Δ} = π^{d/2} 2^{d−2Δ} Γ(d/2−Δ)/Γ(Δ) |k|^{2Δ−d}`.

Tu peux travailler en position ou en impulsion. **Trace toute convention de polarisation et de
projecteur explicitement.**

---

## 3. Livrable `[un nombre, dérivé puis scellé]`

$$C_T^{\text{prog (Osborn–Petkos)}} = c \cdot \frac{\ell_{dS}^2}{G},\qquad c = ?$$

Produire `verif_naction_aveugle.py` (EXIT 0) qui :
- pose les définitions de §2 ;
- dérive `c` symboliquement (sympy), en exhibant chaque facteur (Fourier, projecteur TT,
  dictionnaire `(d/16πG)`, polarisation) ;
- **sanity-checks sans donnée externe** : FT scalaire `d=3` = `π²/12` ; projecteur TT de
  trace 2, idempotent ;
- **ancre de calibration croisée** (permise — théorie de référence indépendante du programme) :
  recouper la **machinerie** de conversion via une théorie à `C_T` connu — le **scalaire conforme
  libre en `d=3`** — dont la valeur d'Osborn–Petkos est à **fetcher indépendamment** (source
  publiée ; p. ex. Osborn–Petkos 1994). Cette valeur ne concerne PAS le `C_T` du programme : elle
  ne valide que le pipeline Fourier+projecteur. Sa lecture ne rompt PAS la blindure.
- imprime `c` et le scelle.

**Engage `c` (EXIT 0) AVANT toute réconciliation (§4).**

---

## 4. Réconciliation `[APRÈS engagement de c — pas avant, et faite ailleurs]`

Une fois `c` scellé, transmettre la valeur à l'audit. La comparaison à la valeur holographique
externe (continuation `ℓ_AdS→iℓ_dS`, signe par `i^{d−1}`, magnitude) se fait dans un autre
contexte, avec les fichiers du programme.
- accord en magnitude ⟹ **convergence** (`établi`, algèbre, cohérence de coefficients) ;
- désaccord ⟹ **NO-GO** net (laissé tel quel, sans rattrapage).

Discipline `LC-AUDIT-VERDICT §6.4` : une convergence éventuelle ne dit **rien** de
« D1 fermé / N fixé / CCC démontrée ». Compte `{A4 ; A2★ ; N}` **inchangé**.

---

## Annexe — Check-list d'ouverture de l'agent aveugle

1. Confirmer le contexte : **aucun montage `/mnt/project/`** ; idéalement Incognito.
2. Confirmer qu'aucune valeur numérique précalculée du coefficient, aucun facteur de conversion
   tout prêt, aucune magnitude/signe de la réponse n'est présent dans le contexte. Si oui
   ⟹ ARRÊT, contexte non valide.
3. Dériver `c` (§2 → §3), exhiber chaque facteur, passer les deux sanity-checks internes.
4. Fetcher la valeur d'Osborn–Petkos du **scalaire conforme libre `d=3`** (calibration de la
   machinerie ; non liée au programme).
5. Sceller `c` dans `verif_naction_aveugle.py` (EXIT 0). **Stop ici.** Transmettre `c` pour §4.
