---
id: LC-WORK-CADRAGE-CAPACITE-3VOIES
codename: LC-RACCORD
titre: "CADRAGE GELÉ R-36 — session dédiée CAPACITÉ (levier b+c couplés). GÈLE, AVANT toute touche à la machinerie d'intégrité, le PÉRIMÈTRE et l'ESPACE-VERDICT de la redéfinition du 77-seal (cadence §0-full, AUD §9bis) COUPLÉE à l'architecture de décharge 3-voies (hachée / annexe-sha-consignée / archive-froide). Motivation : KB 100% ; masse réelle = .md 3577 Ko (81%) > .py 803 Ko (18%) ; compaction hash-neutre épuisée ; seul le retrait/décharge de porteurs desserre. INVARIANTS DURS non-négociables : NACTION-AVEUGLE-PAQUET jamais externalisé (DEFAULT_PKG, incident v1.46) ; verif_paquet_propre reste live avec son .md ; mount-autoritaire (R-54) ; réversibilité byte-exacte ; recette PKG-SHA intègre. PAPER-FIRST : ZÉRO exécution machinerie, ZÉRO décharge, ZÉRO re-baseline dans CE cadrage. Audit froid Mode B (pilote disqualifié) OBLIGATOIRE avant toute décharge effective. §6.4 : dégager de la capacité ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
type: "cadrage gelé R-36 (work-active) — session dédiée capacité. NE scelle rien, ZÉRO algèbre/fetch/décharge. Administratif/architecture, §6.4-neutre. Subordonné à LC-SYNTHESE-SOCLES-5 et à AUD §9bis."
statut: "cadrage RÉDIGÉ — candidat au gel R-36 (sha + horodatage HORS-FICHIER au dépôt). Gèle périmètre + invariants + espace-verdict AVANT toute réécriture de la cadence §0-full et toute décharge. Dépôt net-positif ⟹ à coupler à un swap (ou au lot a cluster-8 différé). À valider par Thierry."
version: 1.0
langue: fr
date: 2026-07-09
prerequis_kb: [LC-SYNTHESE-SOCLES-5, LC-WORK-AUDIT-PAQUET-GEL, LC-WORK-NACTION-AVEUGLE-PAQUET, verif_paquet_propre.py, AUD, IDX_v208]
fichiers_compagnons_kb: [verif_paquet_propre.py, LC-WORK-NACTION-AVEUGLE-PAQUET.md, AUD]
tags: [cadrage, gel-R-36, capacite, 77-seal, cadence-0full, AUD-9bis, annexe, split-3voies, hors-table-sha, decharge, porteurs-pinnes, terminus-pin, cb0939c4, re-baseline-PKG-SHA, mount-autoritaire, R-54, reversibilite, DEFAULT_PKG, audit-froid, mode-B, §6.4, non-surclassement]
tags_epistemiques: [formalisable]
maj: "2026-07-09 — v1.0 : création sur GO Thierry (choix : session dédiée, b+c couplés, sous cadrage + audit froid, sans pression Phase-1). §0-lite du jour PASS (mount PKG-SHA 326b7c14 = v2.67 post −V58 +V59 ; 242 hachés = 165 .md + 77 .py ; 0 doublon ; manifeste unique __64_ v2.66 fa8404f0 après retrait résidu __63_ ; parité IDX/GLO/AUD 5/5/7 Δ=0 ; stack conforme). Ce cadrage GÈLE le périmètre {redéf cadence §0-full + architecture 3-voies}, les INVARIANTS DURS, l'espace-verdict {W-OK / W-PARTIEL / W-REJET}, le firewall f1..f5 et le pipeline phasé — AVANT toute touche machinerie. R-36 : sha + horodatage HORS-FICHIER (ce fichier N'embarque PAS son propre sha). §6.4 : geler un cadrage de capacité ne scelle/réduit/compte rien ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
---

# Cadrage gelé R-36 — session dédiée CAPACITÉ (levier b + c couplés)

> **Paper-first.** ZÉRO touche machinerie, ZÉRO décharge, ZÉRO re-baseline **dans ce fichier**. Ce
> cadrage **gèle**, AVANT la session dédiée, la question de conception, les invariants durs, l'espace-
> verdict et le firewall. La réécriture de la cadence §0-full, la décharge et le re-baseline PKG-SHA
> sont **gatés** par ce gel et par un **audit froid Mode B** (pilote disqualifié). **R-36** : sha de CE
> fichier + horodatage **hors-fichier** au dépôt. **§6.4** : dégager de la capacité ne réduit rien.

## 1. Constat mesuré `[mount 2026-07-09]`

- KB **100%**, 4 394 Ko. Masse réelle : **`.md` 3 577 Ko (81%, 165)** ; **`.py` 803 Ko (18%, 77)** ;
  manifeste 14 Ko. Le gros gisement absolu est **le corpus `.md`**, pas les `.py`.
- Compaction hash-neutre **épuisée**. Seul le **retrait/décharge de porteurs** desserre réellement.
- Presque tous les 77 `.py` appartiennent à des fronts internes **clos + PINNÉS** (`cb0939c4`, doc
  hors-KB `6f3be495`) : D3 (278 Ko), D (144), O2 (61), nonlin (61), naction (48), D1 (46)…
- **Précision machinerie** : `verif_paquet_propre.py` n'est PAS le runner du 77-seal ; c'est le sceau
  de **propreté** du paquet aveugle, couplé EN DUR à `LC-WORK-NACTION-AVEUGLE-PAQUET.md`
  (`DEFAULT_PKG`) + `STRUCTURE_ANCHORS`. Le **« 77-seal » = la cadence §0-full** (rejeu des 77,
  `AUD §9bis`). Redéfinir le 77-seal ⟹ changer **l'ensemble rejoué**, en gardant `verif_paquet_propre`
  + son `.md` **live**.

## 2. Question de conception `[gelée]`

**Peut-on redéfinir la cadence §0-full (77-seal) pour ne rejouer LIVE que les sceaux des fronts ACTIFS
+ la machinerie, et DÉCHARGER hors-KB (voie annexe sha-consignée, réversible) les sceaux des fronts
internes clos+pinnés — SANS casser aucun invariant dur, et avec un re-baseline PKG-SHA propre ?**

Couplage `b + c` : la **décharge** (b, ce qu'on cesse de hacher/rejouer) n'a de sens que si le
**tracé** (c, où le déchargé reste attesté) est défini. Les deux se traitent **ensemble**.

## 3. Architecture 3-voies `[gelée — définition]`

- **Voie A — hachée (dans PKG-SHA)** : substance vive + machinerie. Comprend **obligatoirement**
  `verif_paquet_propre.py` + `LC-WORK-NACTION-AVEUGLE-PAQUET.md` + les sceaux des fronts **actifs**
  (dont la future simulation A2★ Phase-1). Recette PKG-SHA **inchangée** ; `.py` restants **rejoués**
  au §0-full.
- **Voie B — annexe sha-consignée (HORS-hachage, réversible)** : sceaux `.py` (et éventuellement
  `.md` consommés) des fronts **pinnés**, déchargés du mount, **sha listés au manifeste**
  (mécanisme EXISTANT : précédent PDF `2511_05417` hors-table, sha déposé, PKG-SHA **intouché**,
  réversible). Attestés par **pin `cb0939c4` + EXIT-0 consigné + sha bundle** ; **restore-on-demand**
  pour rejeu. **Tension à trancher en Phase-1** : une table d'annexe ré-inflate le manifeste qu'on
  vient de compacter (arbitrage in-manifeste vs bundle-index hors-KB).
- **Voie C — archive froide** : bundles non-référencés (`LC-RACCORD-ARCHIVE-LOT*.zip`), pure
  conservation.

## 4. Invariants DURS `[gelés — non-négociables]`

1. **`LC-WORK-NACTION-AVEUGLE-PAQUET.md` jamais externalisé** (DEFAULT_PKG ; incident v1.46). Reste
   Voie A.
2. **`verif_paquet_propre.py` reste live** avec son `.md` compagnon ; son scope propreté n'est PAS
   dégradé (STRUCTURE_ANCHORS/n-grammes intacts).
3. **Mount-autoritaire (R-54)** : la Voie B est **sha-attestée + restore-on-demand**, JAMAIS une
   seconde source de vérité concurrente du mount.
4. **Réversibilité byte-exacte** : tout déchargé est restaurable byte-exact (bundle sha-listé +
   trace manifeste).
5. **Recette PKG-SHA intègre** : inchangée sur la Voie A ; le re-baseline 242→N' est **recomputé
   DIRECT sur mount**, delta = **exactement** l'ensemble déchargé, 0 dérive.
6. **Décharge admissible SEULEMENT pour fronts pinnés `cb0939c4` clos** ; un sceau de front **actif**
   ne se décharge jamais.

## 5. Espace-verdict `[gelé AVANT exécution]`

- **W-OK** : mécanisme 3-voies admissible — décharge exécutable, invariants 1-6 tous tenus, re-baseline
  propre, audit froid CONFIRMATION. Gain = décharge des `.py` pinnés (jusqu'à ~0,79 Mo, borné par la
  part réellement pinnée+déchargeable).
- **W-PARTIEL** : admissible mais périmètre restreint (p. ex. `.py` pinnés seuls, `.md` exclus) ⟹
  gain borné, consigné.
- **W-REJET** : un invariant dur ne peut être satisfait (R-54 cassé, NACTION externalisé, réversibilité
  non garantie, ou perte d'intégrité au rejeu réduit) ⟹ **statu quo**, capacité re-adressée par la
  voie (a) retrait ciblé.

## 6. Firewall f1..f5 `[anti-circularité — le besoin de place ne corrompt pas l'intégrité]`

- **f1 anti-pression** : le besoin de capacité ne justifie JAMAIS l'externalisation de NACTION ni un
  rescope de `verif_paquet_propre` affaiblissant l'attestation de propreté.
- **f2 R-54** : si « off-mount » devient une source de vérité concurrente ⟹ mutation cassante ⟹ REJET.
- **f3 attestation≠rejeu** : décharger remplace « rejeu live » par « pin + EXIT-0 consigné + sha
  bundle » ; admissible pour pinnés clos SEULEMENT ; un front actif déchargé DOIT casser.
- **f4 réversibilité** : un déchargé non restaurable byte-exact DOIT casser.
- **f5 compte propre** : un re-baseline dont le delta ≠ exactement l'ensemble déchargé DOIT casser.

## 7. Pipeline phasé `[gated]`

- **Phase 0 — CE cadrage (KB-only)** : gel périmètre + invariants + verdict-space + firewall. ZÉRO
  touche machinerie.
- **Phase 1 — design (KB-only)** : spécifier (i) la **table de partition** des 77 `.py` en
  {actifs-live / pinnés-déchargeables / machinerie-intouchable} ; (ii) le **mécanisme annexe**
  (extension hors-table-sha ; arbitrage in-manifeste vs bundle-index) ; (iii) la **réécriture de scope
  de la cadence §0-full** (AUD §9bis). **Sans exécuter.** Validation Thierry avant Phase 2.
- **Phase 2 — exécution machinerie** : réécrire la cadence, décharger vers Voie B (bundle + sha
  manifeste), **re-baseline PKG-SHA** (recompute direct mount, delta borné), consigner v-suivante.
  Timeouts étendus + `setsid` pour les sceaux lourds (rejeu de contrôle avant décharge).
- **Phase 3 — audit froid Mode B** (instance incognito souveraine, pilote disqualifié, paquet
  zéro-fuite) : vérifie f1..f5, réversibilité (restore byte-exact d'un échantillon), intégrité du
  rejeu réduit. **Discordance pilote↔froid ⟹ incognito prévaut.**

## §6.4 — Non-surclassement `[terminal]`

Redéfinir un seal / définir une annexe / décharger des sceaux pinnés / re-baseliner le PKG-SHA =
**aucun sceau de substance, aucun compte de front, aucune réduction, aucune démonstration**.
`{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non clos ; N non fixé (≡Λ) ; O₂ non construit ; A4 non réduit ;
A2★ non tranché ; β **T-b** ; **CCC non démontrée NI réfutée**.

*(R-36 : ce cadrage N'embarque PAS son propre sha ; sha + horodatage hors-fichier au dépôt. Dépôt
net-positif ⟹ à coupler à un swap ou au lot a cluster-8 différé.)*
