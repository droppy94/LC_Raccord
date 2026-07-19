---
id: LC-WORK-A2STAR-P1-CSE4-IMPORTS
codename: LC-RACCORD
titre: "CSE-4 — REGISTRE D'IMPORTS GELÉS d'A2★ Phase-1 (dernier gate avant consommation). Voie déclarée par Thierry : O-ρ-an PRIMAIRE (dérivation analytique du facteur de réplication) + O-ρ-num CROSS-CHECK (corroboration numérique indépendante). GÈLE, AVANT toute lecture de contenu : (i) la liste EXACTE des imports primaires I1..I3 (machinerie de dérivation) ; (ii) la liste EXACTE des imports cross-check C1..C3 (observables numériques) ; (iii) le RÔLE-LOCK (primaire vs cross-check figé — aucun reclassement post-hoc, dents anti-fit) ; (iv) les exclusions (proxy scellé verif_A2_numerique HORS-import d3 ; conclusion Q sous-exp HORS-prémisse d1). Sources = les 11 PASS de CSE-3 v1.1 (identités R-41 ≥3 miroirs). R-36 : gel sha + horodatage HORS-FICHIER au dépôt ; ce fichier n'embarque pas son propre sha. R-54 mount-autoritaire. SANS SURCLASSEMENT (§6.4) : geler des imports ne consomme/scelle/réduit RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranché ; CCC non démontrée NI réfutée."
type: "livrable CSE-4 (registre d'imports gelés, paper-first — fige quoi/quel-rôle AVANT consommation). Candidat au gel R-36 + dépôt net +1. N'EMBARQUE PAS son propre sha."
statut: "RÉDIGÉ — candidat au gel R-36. NON consommé. La lecture/dérivation de contenu (exécution O-ρ) ne commence qu'APRÈS ce gel. Audit froid CSE-5 OBLIGATOIRE sur tout verdict de substance. À valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-12
prerequis_kb: [LC-WORK-A2STAR-P1-CSE3-IDENTITES, LC-WORK-AMENDEMENT-R7-A2STAR-PHASE1, LC-WORK-CADRAGE-A2-EXT-SPIKES, LC-SYNTHESE-SOCLES-5]
renvois: [LC-WORK-AMENDEMENT-R7-A2STAR-PHASE1, LC-WORK-A2STAR-P1-CSE3-IDENTITES]
tags: [CSE-4, R-36, R-54, imports-geles, A2star, phase1, rho, O-rho-an, O-rho-num, role-lock, anti-fit, d1, d3, gel-avant-consommation, spikes, Mixmaster, §6.4, non-surclassement]
tags_epistemiques: [formalisable, décision ouverte]
maj: "2026-07-12 — v1.0 : création sur GO Thierry (CSE-4 d'A2★ Phase-1 ; voie O-ρ-an primaire + O-ρ-num cross-check). Gèle le registre d'imports AVANT consommation, à partir des 11 sources PASS de CSE-3 v1.1 (identités R-41 ≥3 miroirs). Rôles primaire/cross-check VERROUILLÉS (anti-fit : un cross-check infirmant ne peut être rétrogradé). Aucune lecture de contenu à ce stade. §6.4 : geler ne consomme/scelle/réduit rien ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranché ; CCC non démontrée NI réfutée. R-36 : sha + horodatage hors-fichier au dépôt."
---

# CSE-4 — Registre d'imports gelés · A2★ Phase-1 · O-ρ-an primaire + O-ρ-num cross-check

> **Gel avant consommation.** Ce registre fige **quels** imports servent, **à quel rôle**, **AVANT** toute
> lecture de contenu. **R-36** : gel horodaté hors-fichier au dépôt. **R-54** : mount-autoritaire. La
> **dérivation/lecture (exécution O-ρ) ne commence qu'APRÈS ce gel**. **§6.4** : rien ici ne réduit/scelle.

## 0. Objet & discipline

Voie déclarée (décision Thierry, 2026-07-12) : **O-ρ-an PRIMAIRE** (ρ dérivé comme facteur de branchement
de la carte génératrice de spikes) **+ O-ρ-num CROSS-CHECK** (ρ corroboré par les observables numériques
de spikes récurrents). Estimateur figé **§2 de l'amendement** INCHANGÉ. Espace-verdict **{V1/V2/V3}** cité
du gel `478be3ac`, INCHANGÉ. Sources = 11 PASS de `LC-WORK-A2STAR-P1-CSE3-IDENTITES` v1.1 (identités R-41
≥3 miroirs).

## 1. Imports PRIMAIRES `[O-ρ-an — machinerie de dérivation, load-bearing]`

| Id | Source (CSE-3) | Objet importé (structure, PAS valeur pré-lue) | Rôle dans la dérivation de ρ |
|---|---|---|---|
| **I1** | S1-d Uggla–van Elst–Wainwright–Ellis 2003 (gr-qc/0304002) | Cadre à variables Hubble-normalisées scale-invariant / attracteur passé (Mixmaster généralisé) | **Substrat générique 3D** où ρ est défini (répond à la clause d'ancrage §3 : dynamique générique, pas proxy) |
| **I2** | S2-b Lim 2008 (0710.0628) | Solution explicite de spike + transformation génératrice (germe Bianchi II vide) | **Carte de génération d'un spike** — brique du facteur de branchement |
| **I3** | S2-e Heinzle–Uggla 2013 (1212.5500), volet analytique | Structure des séquences de Kasner à spikes **récurrents** (cadre de récurrence) | **Itération bounce-à-bounce** de la carte ⟹ facteur multiplicatif/additif = ρ |

*Contexte non load-bearing (backbone conceptuel, n'injecte aucune valeur de ρ)* : S1-a/b BKL 1970/1982,
S1-c Belinski–Henneaux 2017, S2-f Andersson et al. 2005 (silence asymptotique).

## 2. Imports CROSS-CHECK `[O-ρ-num — corroboration numérique indépendante]`

| Id | Source (CSE-3) | Observable importé | Rôle |
|---|---|---|---|
| **C1** | S2-a Garfinkle 2004 (gr-qc/0312117) | Comportement des spikes en numérique générique 3D vide **sans symétrie** | Corrobore/infirme le ρ dérivé au niveau générique |
| **C2** | S2-c Lim–Andersson–Garfinkle–Pretorius 2009 (PRD 79, 123526) | Spikes en régime Mixmaster de cosmologies G₂ (numérique) | Corrobore le régime de récurrence |
| **C3** | S2-d Heinzle–Uggla–Lim 2012 (PRD 86, 104049) + S2-e (1212.5500), volet numérique | Oscillations de spikes / distribution numérique des spikes récurrents | Corrobore la statistique de récurrence (n_s vs N_b) |

## 3. Rôle-lock `[dents anti-fit — figé AVANT consommation]`

- **Assignation primaire ↔ cross-check FIGÉE.** Aucun import ne peut être **reclassé** après lecture des
  résultats. En particulier : un **cross-check qui INFIRME** le ρ dérivé **ne peut PAS être rétrogradé** en
  « contexte » ni écarté — il déclenche **réexamen ⟹ V3** (ou V2 si l'infirmation est une cascade franche),
  jamais un silence. Standing probatoire du cross-check = **plein**.
- **S2-e (Heinzle–Uggla 2013) est splitté** : volet **analytique** = I3 (primaire) ; volet **numérique** =
  C3 (cross-check). Les deux volets sont gelés séparément pour éviter tout double-usage opportuniste.
- **d1 (relier≠ancrer)** : aucun de I1–I3 / C1–C3 ne peut servir à **injecter comme prémisse** (a)
  l'additivité mésoscopique Garfinkle ni (b) la conclusion `Q` sous-exp. I2/I3 fournissent la **carte**, pas
  la valeur `ρ=0`. Violation ⟹ **V3**.
- **d3 (proxy)** : le proxy mésoscopique scellé `verif_A2_numerique.py` (déchargé) est **HORS de ce registre**
  et **ne tient pas lieu** de générique 3D. Si requis en contrôle, **restore-on-demand + rejeu LIVE + ré-archivage**
  (jamais ré-import KB).

## 4. Exclusions gelées `[ce qui n'est PAS importé]`

- Proxy scellé `verif_A2_numerique.py` (d3) — hors-import.
- Hypothèse `Q` sous-exp (la conclusion) comme prémisse (d1) — hors-import.
- Toute source **hors des 11 PASS** de CSE-3 v1.1 — hors-import (R-41 : non identité-vérifiée = jamais consommée).
- Données initiales **non génériques** (symétrie imposée, fine-tuning) — si elles forcent ρ ⟹ **V3** (généricité, §3 amendement).

## 5. Suite `[CSE-4 → exécution O-ρ → CSE-5]`

Après gel de ce registre : **exécution O-ρ** (première étape où le contenu est lu/dérivé) —
dérivation analytique du facteur de branchement (I1–I3) sous estimateur figé §2, puis cross-check numérique
(C1–C3). Tout verdict de substance (V1/V2/V3) ⟹ **audit froid incognito souverain CSE-5** (Mode A zéro-fuite,
paquet sans zone opérateur nommant le verdict ; l'incognito prévaut) ⟹ **CSE-6** nommage H
(`établi (physique externe, sous hypothèses H)`, jamais « CCC vraie »).

## 6. Non-surclassement `[§6.4]`

Geler un registre d'imports **n'établit, ne consomme, ne scelle, ne réduit, ne démontre RIEN**. Aucune
algèbre, aucune dérivation, aucun contenu lu à ce stade. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ;
`N` non fixé (≡`Λ`) ; A4 non réduit ; **A2★ non tranché** ; O₂ non construit ; β **T-b** ; **CCC non
démontrée NI réfutée**.

*(R-36 : ce fichier n'embarque pas son propre sha ; gel sha + horodatage hors-fichier au dépôt. R-54 :
mount autoritaire.)*
