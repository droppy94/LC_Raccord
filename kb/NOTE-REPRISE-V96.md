---
id: NOTE-REPRISE-V96
titre: "Note de reprise autoportante V96 (CLÔTURE). Série NOTE-REPRISE-V<N> — en-KB, hachée, swap net-zéro à chaque session. Porte l'état de fermeture V96 et le protocole de démarrage V97. NE contient PAS le PKG de clôture (fichier haché ⟹ circularité interdite, R-36 généralisé) : le PKG de clôture est porté par le MANIFESTE (v2.124), à lire au boot."
codename: LC-RACCORD
statut: reprise-cloture-V96
version: "1.0"
langue: fr
date: 2026-07-20
pkg_de_cloture: "PORTÉ PAR LE MANIFESTE v2.124 (R-36) — NON reproduit ici"
---

# Note de reprise autoportante — V96 (clôture)

## 0. Discipline de boot
R-54 (mount autoritaire) · R-55 (rien de non déposé n'est « livré ») · R-36 (aucun fichier haché n'embarque son propre PKG ni le PKG de clôture) · §6.4 (mesurer ≠ réduire) · capacité KB **>100 %** ⟹ net-zéro obligatoire, tout net-positif exige retrait compensatoire ou dérogation opérateur consignée.

## 1. Protocole de démarrage V97 (opposable)
1. Ouvrir la discussion en **présentant cette note en prompt** (restaure le contexte).
2. **Recomputer le PKG de la KB active** (boot §0-lite, `python3 LC-WORK-BOOT-SESSION*.py`).
3. Demander/relire la **valeur de clôture V96 déclarée au MANIFESTE** (v2.124).
4. **Continuité OK ⟺ PKG recomputé == PKG déclaré au manifeste.** Égal ⟹ la KB est exactement dans l'état de fermeture V96. Écart non nommé ⟹ STOP (mount dérivé ou dépôt hors-protocole).

## 2. État de clôture V96 (ce qui a été fait)
- **P-8 SOLDÉ.** Générateur `LC-WORK-GEN-PAQUET-CSE2` v2.0→v2.1 (swap net-zéro, instrument) : livraison séquencée instrumentée — **(i)** deux tranches nommées, refus de la tranche unique par défaut ; **(ii)** inapplicabilité sur drapeau explicite + clause P-6 écrite PAR LE SCRIPT ; **(iii)** scan P-7 des formulations interdites → rc non nul ; **(iv)** champ nommé `regime_livraison` ; **verrou P-1** : refuse l'inapplicabilité si le paquet instancie un mécanisme de retour. `--selftest` 16/16 PASS. **P-9 : le dépôt NE RÉPARE PAS D-01** — mesuré à la prochaine gate. **GATES β DÉBLOQUÉES.**
- **Front p_Q matérialisé** (délimitation). 4 fichiers déposés : `REPRISE_fissure-croisee-spin4_reduction-pQ-isomorphisme-transport-C1b` (reconstruction fidèle d'un front phantom GLOSSAIRE v1.69) ; `LC-D-Q-DICTIONNAIRE-AB` **SUPERSEDED** (trace) ; `dico_Q.py` + `audit_neutral_dico.py` **reclassés INSTRUMENTS hors S2** (comparateur `sceau_s2` v1.2→v1.3). Verdict = **INDÉTERMINÉ (pas A)** ; §6.4 : aucun sceau, aucune algèbre neuve. Audit froid `audit_neutral_dico` corrobore la démotion (3 « faits » de branche A = artefact / tautologie / positivité déguisée).
- **Cartographie v1.1→v1.2** : **gate §A levée sur la SEULE condition (i)** (REPRISE matérialisé). (ii) proxy porteur et (iii) question sharp d=3 **NON levées** ⟹ **NON PRIORISÉ**, **β (#1) / α-coin (#2) MAINTENU** (§5.7). Pilote **DISQUALIFIÉ** sur substance.
- **GLO v1.74→v1.75** : **port p_Q** (2 blocs additifs), **FORK glossaire RÉSOLU** côté KB (mount = axe γ v1.70-v1.74 **+** p_Q).
- **Contamination `verre_fraicheur_3d.jpg`** (hors-périmètre) débusquée par §0-lite (N_autre 0→1→0), **retirée** (leçon V62 : le firewall a mordu).
- **Consignation v2.124** = dernier geste, PKG de clôture recomputé une seule fois.

## 3. Invariants (inchangés)
`{A4 ; A2★ ; N}` INCHANGÉ · R-53 0/4 · O₂ non construit · β **T-b** (SEUL facteur d'O₂ ouvert, **débloqué** par P-8) · α = C1-b (délimitation conditionnelle `p`) · D1 non clos · N non fixé (≡Λ) · **nœud (i) INDÉTERMINÉ (pas A)** · têtes scellées intactes · CCC non démontrée NI réfutée.

## 4. Ouvert pour V97
- **Substance β** (transport AdS→dS du joint graviton, cellule résiduelle `R1″∧R2″∧R4″`, levier PRESCRIPTION-DÉPENDANT) : **DÉBLOQUÉE** par P-8, prête à être engagée AVEC le générateur v2.1 (livraison séquencée obligatoire en multi-tours). Cadrage gelé (R-7) + audit froid souverain requis avant tout verdict.
- **Promotion p_Q en #1** conditionnée à (ii) proxy **porteur** non forcé (5.3-P) + (iii) **question sharp d=3** énoncée (5.3-R) — **non levées**. Reste NON priorisé ; pilote disqualifié.
- **Copie opérateur hors-KB `03_glossaire` v1.70 STALE** (manque axe γ v1.70-v1.74) : **à re-sync du mount v1.75** pour clore le fork définitivement.
- **D-01 / D-08** non mesurés (P-9) : à mesurer à la prochaine gate par un fait vérifiable (tranche 2 après issue Phase 2 ; recette au bloc écrite par le script).
- **Q A/B** (γ-2 §0ter) non tranchée · **§9.4** append-only rouvert.
- **Bump boot v1.3→v1.4 DIFFÉRÉ** : l'ATTENDU imprimé dit encore « instruments_exclus 4 » alors que le réel = **6** (dico_Q + audit_neutral_dico ajoutés). Cosmétique, n'affecte pas rc ; à corriger au prochain touch d'instrument.
- **Registre de sortie** (sha pour ré-import) : `verre_fraicheur_3d.jpg` [NON consigné, hors-périmètre], gen-paquet v2.0 `168a08a4`, sceau_s2 v1.2 `cba1017d`, cartographie v1.1 `db13d524` [reconstruit, réserve type 588d09f5], GLO v1.74 `8906b786` [reconstruit, idem].

## 5. Règle de séquence (opposable, gravée boot v1.3, reconduite)
1. La **consignation est le DERNIER geste** de la discussion.
2. Le **PKG de clôture se calcule UNE seule fois**, après **tous** les dépôts hachés (y compris ce swap de note).
3. **Rien de haché** n'est déposé après la consignation (sinon PKG désynchronisé).
4. Le PKG de clôture est porté par le **MANIFESTE** (PKG-exclu), **jamais** par la reprise (hachée ⟹ circularité interdite).
5. Tout fichier **sorti de KB active** : son sha256 est consigné au manifeste (registre de sortie) pour authentifier un ré-import.

## 6. §6.4 — sentinelle
Exécuter P-8, matérialiser p_Q, résoudre un fork, classer des instruments, booter, mesurer, consigner : **ne scelle, ne réduit, ne compte, ne démontre RIEN.** `{A4 ; A2★ ; N}` INCHANGÉ ; nœud (i) INDÉTERMINÉ (pas A) ; CCC non démontrée ni réfutée.
