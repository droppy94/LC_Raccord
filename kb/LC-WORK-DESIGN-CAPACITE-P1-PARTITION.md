---
id: LC-WORK-DESIGN-CAPACITE-P1-PARTITION
codename: LC-RACCORD
titre: "DESIGN Phase-1 (KB-only) de la session dédiée CAPACITÉ, gaté par le gel R-36 `1651cbcf` (LC-WORK-CADRAGE-CAPACITE-3VOIES). Spécifie, SANS exécuter, les 3 livrables de la Phase-1 : (i) la TABLE DE PARTITION des 77 `.py` en {actifs-live / pinnés-déchargeables / machinerie-intouchable} ; (ii) le MÉCANISME ANNEXE (extension hors-table-sha, arbitrage in-manifeste vs bundle-index) ; (iii) la RÉÉCRITURE DE SCOPE de la cadence §0-full (AUD §9bis). Constat central : machinerie-intouchable = {verif_paquet_propre.py} SEUL ; actifs-live = ∅ (aucun `.py` de front externe A2★/A4/N n'existe encore ; relier≠ancrer interdit de reclasser les proxies internes A2) ; pinnés-déchargeables = 76 (796,2 Ko) tous sous pin cb0939c4. PAPER-FIRST : ZÉRO exécution, ZÉRO décharge, ZÉRO re-baseline. Décisions ouvertes (forks D1/D2/D3) laissées à Thierry. §6.4 : dégager de la capacité ne scelle/réduit/compte/démontre RIEN ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
type: "design Phase-1 (work-active) — subordonné à LC-WORK-CADRAGE-CAPACITE-3VOIES (gel R-36 1651cbcf) et à AUD §9bis. NE scelle rien, ZÉRO algèbre/fetch/décharge/re-baseline. Administratif/architecture, §6.4-neutre."
statut: "design VALIDÉ — 3 livrables Phase-1 spécifiés + forks D1/D2/D3 TRANCHÉS (GO Thierry 2026-07-09, cf. §7bis) : D1=(β)-fixe canari · D2=(b) bundle-index hors-KB · D3=par-grappe. Phase-2 ARMÉE, gatée (exécution machinerie + audit froid Mode B). Déjà déposé (swap −RB1-LP +DESIGN ⟹ v2.70 7629af51) ; ce patch v1.1 = swap net-zéro −v1.0 +v1.1. N'embarque PAS de PKG-SHA propre (R-36)."
version: 1.1
langue: fr
date: 2026-07-09
prerequis_kb: [LC-WORK-CADRAGE-CAPACITE-3VOIES, LC-SYNTHESE-SOCLES-5, LC-WORK-AUDIT-PAQUET-GEL, LC-WORK-NACTION-AVEUGLE-PAQUET, verif_paquet_propre.py, AUD]
tags: [design, phase-1, capacite, gel-R-36, 1651cbcf, 77-seal, cadence-0full, AUD-9bis, partition-py, annexe, bundle-index, hors-table-sha, decharge, porteurs-pinnes, terminus-pin, cb0939c4, re-baseline-PKG-SHA, mount-autoritaire, R-54, reversibilite, DEFAULT_PKG, relier-ancrer, §6.4, non-surclassement]
tags_epistemiques: [formalisable]
maj: "2026-07-09 — v1.1 : forks TRANCHÉS sur GO Thierry (D1=(β)-fixe · D2=(b) · D3=par-grappe) ⟹ ajout §7bis (décisions + composition du canari fixe : verif_nonlin_parity, verif_D3_P6_specB_oracle, verif_A2_numerique, diag_bounces — couvrant SymPy/NumPy/SciPy/setsid-lourd + chemin diag ; NetworkX exercé par 0 sceau, non couvrable). Re-chiffres : déchargeables 76→72 (~757 Ko), Voie A live = machinerie(1)+canari(4)=5 .py ⟹ re-baseline projeté 242→170 hachés (165 .md + 5 .py). Verdict projeté W-PARTIEL (β). Patch ADDITIF (version+statut+maj+§7bis ; suppr. ⊆ {version, statut, maj} ; §7 conservée = espace d'options). Parité guillemets droits Δ=0. ZÉRO exécution/décharge/re-baseline (⟹ Phase-2). Swap net-zéro −v1.0 +v1.1. §6.4 : trancher un fork de design ne scelle/réduit/compte rien ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée. | 2026-07-09 — v1.0 : création sur GO Thierry (cran 1 = session capacité Phase-1 design). §0-lite du jour PASS (mount PKG-SHA v2.69 cebe290a post −V59 +V60 ; 242 hachés = 165 .md + 77 .py ; 0 doublon ; parité IDX/GLO/AUD 5/5/7 Δ=0 ; stack conforme). Design KB-only des 3 livrables §7-Phase-1 du cadrage gelé. Frontière machinerie VÉRIFIÉE au mount : verif_paquet_propre.py auto-contenu (n'ouvre que LC-WORK-NACTION-AVEUGLE-PAQUET.md ; STRUCTURE_ANCHORS = chaînes attendues DANS le paquet, PAS des dépendances runtime .py). ZÉRO touche machinerie, ZÉRO décharge, ZÉRO re-baseline. R-36 : n'embarque pas son propre sha. §6.4 : un design de partition ne scelle/réduit/compte rien ; {A4 ; A2★ ; N} INCHANGÉ ; CCC non démontrée NI réfutée."
---

# Design Phase-1 — partition des 77 `.py`, mécanisme annexe, rescope §0-full

> **Paper-first.** ZÉRO exécution machinerie, ZÉRO décharge, ZÉRO re-baseline **dans ce document**.
> Ce design **spécifie** les 3 livrables Phase-1 du cadrage gelé `LC-WORK-CADRAGE-CAPACITE-3VOIES`
> (gel R-36 `1651cbcf`) et **énumère** les décisions ouvertes (forks) — il n'en tranche aucune.
> L'exécution (Phase-2) et l'audit froid Mode B (Phase-3) restent **gatés**. **R-36** : ce document
> n'embarque pas son propre sha. **§6.4** : dégager de la capacité ne réduit rien.

## 1. Données mesurées `[mount 2026-07-09, v2.69 cebe290a]`

- 77 `.py` = **803,1 Ko** brut. 165 `.md` = 3 577 Ko. KB ~100%.
- **Frontière machinerie vérifiée** : `verif_paquet_propre.py` importe seulement `sys/hashlib/unicodedata`,
  n'ouvre que `LC-WORK-NACTION-AVEUGLE-PAQUET.md` (`DEFAULT_PKG`). Sa liste `STRUCTURE_ANCHORS`
  (dont la chaîne `"verif_naction_aveugle.py"`) est un ensemble de **chaînes attendues DANS le paquet**,
  **PAS** des dépendances runtime sur des fichiers `.py`. ⟹ décharger n'importe quel `.py` de front
  (y compris `verif_naction_aveugle.py`) **ne casse pas** `verif_paquet_propre.py`.
- Tous les fronts internes sont **clos + PINNÉS** (`cb0939c4`, doc hors-KB `6f3be495`).

## 2. Livrable (i) — Table de partition des 77 `.py` `[spécifiée]`

Trois classes, selon les invariants durs du cadrage (#2 machinerie live, #6 décharge ⟺ pinné clos) :

### 2.1 — machinerie-intouchable (Voie A, live inconditionnel) — **1 fichier, 6,9 Ko**

| fichier | rôle | invariant |
|---|---|---|
| `verif_paquet_propre.py` | sceau de PROPRETÉ du paquet aveugle (couplé `NACTION` + `STRUCTURE_ANCHORS`) | #2 (live), f1 (jamais rescopé) |

Compagnon `.md` obligatoire en Voie A : `LC-WORK-NACTION-AVEUGLE-PAQUET.md` (invariant #1, jamais
externalisé, `DEFAULT_PKG`, incident v1.46).

### 2.2 — actifs-live (Voie A, live car front actif) — **∅ (0 fichier)**

**Constat de design** : aucun `.py` de front **actif** n'existe à ce jour. Les fronts actifs sont les
fronts **externes** (A2★ #1, A4 #2, N≡Λ #3, SOCLES-5 §4) ; **aucun n'a encore de sceau `.py`** (la
simulation générique 3D d'A2★ Phase-1 n'est pas construite). **`relier≠ancrer`** (drapeau CSE-1) :
les proxies **internes** A2 (`verif_A2_numerique.py`, `verif_D3_C7b_spikes.py`, `…_A2_reduction.py`)
**NE peuvent PAS** être reclassés « actifs » du front externe — ils resteraient un ancrage mésoscopique
Garfinkle, précisément ce que la Phase-1 A2★ doit ré-établir en générique 3D. Ils restent **pinnés** (§2.3).

> Conséquence : le premier `.py` neuf (sceau A2★ Phase-1) entrera en Voie A **actifs-live** au moment de
> son dépôt — hors du présent périmètre, déclenchera §0-full (déclencheur « `.py` neuf » inchangé).

### 2.3 — pinnés-déchargeables (Voie B candidat) — **76 fichiers, 796,2 Ko**

Tous sous pin `cb0939c4`. Ventilation par grappe-front (base des bundles par-front, fork D3) :

| grappe-front | n | Ko |
|---|---|---|
| D3 (front a / interaeon / P6 / crossover) | 24 | 278,5 |
| D-nongauss (TTT / 4pt) | 4 | 73,8 |
| D1 (verrou stabilité / atlas / bianchi / c3) | 8 | 64,8 |
| O2 (P1 / P2 / hodge / bprime / coin / scattering) | 8 | 61,3 |
| nonlin (2pt verrou) | 4 | 61,1 |
| D-C_T (dual / realite / atn / constructif) | 6 | 60,1 |
| naction / C_T | 4 | 47,9 |
| F-branche (F1 / F4 / F5 / F6) | 4 | 35,4 |
| G3 / β (adm-imports / m4-chainon) | 2 | 25,6 |
| A2 / A3 (numerique / passerelle) | 2 | 22,5 |
| cB (weyl magnetique) | 1 | 14,9 |
| socle / diag (phi / scri / bounces) | 3 | 12,5 |
| E / N (crosscheck / planck) | 2 | 11,8 |
| D-W3 / g3 | 2 | 10,5 |
| SpN | 1 | 8,6 |
| γ (nstar-ads4) | 1 | 6,6 |
| **TOTAL déchargeable** | **76** | **796,2** |

**Gain maximal borné** ≈ 796 Ko (concorde avec le plafond W-OK du cadrage §5, « ~0,79 Mo »).

## 3. Livrable (ii) — Mécanisme annexe `[spécifié]`

- **Précédent existant** (cadrage §3 Voie B) : PDF `2511_05417` déjà hors-table, sha déposé au manifeste,
  PKG-SHA **intouché**, réversible. Le mécanisme `.py` en est l'extension.
- **Attestation d'un déchargé** = pin `cb0939c4` + **EXIT-0 consigné** (rejeu de contrôle Phase-2 AVANT
  décharge) + **sha du bundle** ; **restore-on-demand** pour tout rejeu ultérieur.
- **f2 / R-54** : l'annexe est **sha-attestée + restore**, **JAMAIS** une seconde source de vérité
  concurrente du mount. Le mount reste autoritaire ; l'annexe n'est consultée qu'au restore.

**Fork D2 — où vivent les sha des déchargés :**
- **(a) table sha in-manifeste** : 76 lignes `nom␣␣sha` ajoutées au manifeste. Simple mais **ré-inflate
  le manifeste qu'on vient de compacter** (tension explicite du cadrage §3) ; ~+8 Ko sur un fichier à 16 Ko.
- **(b) bundle-index hors-KB** *(recommandé)* : les `.py` déchargés sont empaquetés en bundle(s) `.zip`
  hors-KB ; l'**index nom↔sha vit DANS le bundle** ; seul le **sha du (des) bundle(s)** est listé au
  manifeste (1 ligne par bundle). Manifeste maigre ; réversibilité byte-exacte garantie par le sha du
  bundle + l'index interne.

**Fork D3 — granularité du (des) bundle(s) :**
- **bundle unique** 76-en-1 : 1 ligne sha au manifeste ; restore = tout ou rien.
- **bundles par-grappe** *(recommandé)* : ~16 bundles (table §2.3) ; ~16 lignes sha ; **restore ciblé**
  (ex. ré-armement A2★ ⟹ restore de la grappe D3 + A2/A3 seules, sans réhydrater D-C_T ni O2).

## 4. Livrable (iii) — Réécriture de scope de la cadence §0-full `[spécifiée]`

**Constat de désync** : AUD §9bis énonce « §0-full = §0-lite + rejeu des **74 sceaux** (73 `verif_*.py`
+ `diag_bounces`) ». **Stale** : le mount porte 76 `verif_*.py` + `diag_bounces` = 77 ; hors machinerie
(`verif_paquet_propre`), l'ensemble rejouable RÉEL courant = **76** (75 `verif_*` front + `diag_bounces`),
soit un undercount de **2** dans le texte §9bis (dépôts `.py` postérieurs à la gravure v1.68). La
réécriture corrige ce compte **et** redéfinit l'ensemble.

**Nouveau scope §0-full (proposé) :**

> **§0-full** = §0-lite + rejeu LIVE de **{machinerie} ∪ {sceaux des fronts ACTIFS}** (EXIT 0) + parité
> transverse complète. Les fronts **pinnés déchargés** ne sont PAS rejoués LIVE : leur intégrité est
> portée par **attestation** (pin `cb0939c4` + EXIT-0 consigné + sha bundle), **rejouable sur
> restore-on-demand**.
>
> **Déclencheurs inchangés** : mismatch PKG-SHA / changement de stack / dépôt `.py` neuf / avant verdict
> majeur. **Ajout** : tout **restore-on-demand** d'un pinné ⟹ rejeu LIVE du sceau restauré avant usage.

**Effet selon fork D1 (périmètre de décharge) :**
- **(α) décharge maximale** : live-set = `{verif_paquet_propre}` seul (0 front actif) ⟹ §0-full ≈
  §0-lite + propreté. Gain ~796 Ko. Verdict projeté **W-OK**.
- **(β) échantillon-témoin** : garder LIVE un sous-ensemble **tournant** de K sceaux pinnés (préserve un
  signal d'exécutabilité de l'environnement, cf. justification §9bis « le conteneur se réinitialise »),
  décharger le reste. Gain borné (~796 Ko − masse des K gardés). Verdict projeté **W-PARTIEL**.

## 5. Espace-verdict projeté `[gelé au cadrage §5]`

- **W-OK** ⟸ fork D1=(α) : invariants 1-6 tenus, re-baseline propre (242→166 hachés = 165 .md + 1 .py),
  audit froid CONFIRMATION.
- **W-PARTIEL** ⟸ fork D1=(β) ou périmètre restreint : gain borné, consigné.
- **W-REJET** ⟸ un invariant dur insatisfiable. **Aucun identifié en design** (frontière machinerie propre,
  réversibilité par bundle sha, delta borné). Le rejet ne surgirait qu'à l'exécution (f2..f5) — d'où
  l'audit froid Mode B obligatoire.

## 6. Firewall f1..f5 `[contrôle de design]`

- **f1 anti-pression** ✓ — `NACTION` reste Voie A ; `verif_paquet_propre` non rescopé (propreté intacte).
- **f2 R-54** ✓ — annexe = sha-attestée + restore (reco bundle-index) ; jamais source concurrente.
- **f3 attestation≠rejeu** ✓ — décharge SEULEMENT pinnés clos ; 0 front actif déchargé (§2.2 = ∅) ;
  **test de casse** (un actif déchargé DOIT casser) reporté en Phase-3 sur échantillon.
- **f4 réversibilité** ✓ — chaque déchargé restaurable byte-exact (bundle sha-listé + trace manifeste).
- **f5 compte propre** ✓ — re-baseline Phase-2 = recompute DIRECT mount ; delta = **exactement**
  l'ensemble déchargé (76 si (α)) ; recette PKG-SHA Voie A inchangée.

## 7. Décisions ouvertes — forks pour Thierry `[Phase-1 ne tranche pas]`

| fork | option | reco |
|---|---|---|
| **D1** périmètre décharge | (α) maximale 76/76 → W-OK · (β) échantillon-témoin tournant → W-PARTIEL | à trancher : (α) = capacité max ; (β) = garde un signal d'exécutabilité |
| **D2** localisation sha | (a) table in-manifeste · (b) bundle-index hors-KB | **(b)** — n'inflate pas le manifeste compacté |
| **D3** granularité bundle | unique 76-en-1 · par-grappe (~16) | **par-grappe** — restore ciblé (ré-armement A2★) |

## 7bis. Décisions tranchées `[validées Thierry 2026-07-09]`

| fork | tranché | effet |
|---|---|---|
| **D1** | **(β)-fixe** | canari fixe de 4 sceaux gardés LIVE en Voie A ; les 72 autres pinnés déchargés |
| **D2** | **(b)** bundle-index hors-KB | sha du/des bundle(s) au manifeste ; index nom↔sha DANS le bundle |
| **D3** | **par-grappe** | ~16 bundles (table §2.3) ; restore ciblé |

**Canari fixe (β) — jeu ARRÊTÉ, non tournant** (couvre les classes de dépendance stack RÉELLEMENT
exercées + le chemin d'exécution lourd) :

| sceau | classe couverte | Ko |
|---|---|---|
| `verif_nonlin_parity.py` | SymPy + **setsid-lourd #1** | 10,0 |
| `verif_D3_P6_specB_oracle.py` | SciPy + **setsid-lourd #2** | 11,4 |
| `verif_A2_numerique.py` | NumPy pur | 13,0 |
| `diag_bounces.py` | unique non-`verif_` (chemin diag) + numpy/scipy | 3,5 |
| **canari total (Voie A)** | | **~38,8** |

- **Couverture stack** : SymPy (57 sceaux), NumPy (27), SciPy (16) tous représentés ; **NetworkX = 0
  sceau** (aucun `.py` ne l'exerce) ⟹ non couvrable par canari, **hors périmètre de décharge** (constat,
  pas un défaut introduit ici).
- **Voie A live après décharge** : machinerie(1) + canari(4) = **5 `.py`**. **Déchargeables : 72** (~757 Ko).
- **Re-baseline projeté (Phase-2)** : 242 → **170 hachés = 165 `.md` + 5 `.py`** ; delta = **exactement**
  les 72 déchargés (f5).
- **Verdict projeté** : **W-PARTIEL** (β) — gain borné (~757 Ko), signal d'exécutabilité conservé au
  §0-full (le canari rejoue à chaque déclencheur « stack change »). Confirmé seulement après audit
  froid Mode B (Phase-3).
- **Scope §0-full (β)** : LIVE = machinerie ∪ canari(4) ∪ {fronts actifs = ∅} = **5 sceaux** ; pinnés
  déchargés = attestation + restore-on-demand.

## 8. Ce que la Phase-1 ne fait PAS `[gated]`

ZÉRO exécution, ZÉRO décharge, ZÉRO re-baseline (⟹ Phase-2, timeouts étendus + `setsid` pour les sceaux
lourds `verif_nonlin_parity` / `verif_D3_P6_specB_oracle`, rejeu de contrôle EXIT-0 AVANT décharge).
**Audit froid Mode B** (instance incognito souveraine, pilote disqualifié, paquet zéro-fuite ;
discordance ⟹ incognito prévaut) OBLIGATOIRE avant toute décharge effective (⟹ Phase-3).

## §6.4 — Non-surclassement `[terminal]`

Partitionner des `.py`, spécifier une annexe, réécrire un scope de cadence = **aucun sceau de substance,
aucun compte de front, aucune réduction, aucune démonstration**. `{A4 ; A2★ ; N}` **INCHANGÉ** ; D1 non
clos ; N non fixé (≡Λ) ; O₂ non construit ; A4 non réduit ; A2★ non tranché ; β **T-b** ; **CCC non
démontrée NI réfutée**.

*(R-36 : ce design N'embarque PAS son propre sha. Dépôt net-positif ⟹ à coupler à un swap ou au lot
`a` cluster-8 différé. Reste subordonné au gel `1651cbcf` — aucune touche machinerie ici.)*
