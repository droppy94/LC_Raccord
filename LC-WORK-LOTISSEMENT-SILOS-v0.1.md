---
id: LC-WORK-LOTISSEMENT-SILOS
titre: "Lotissement du programme LC-RACCORD en silos — redémonstration des établis, fronts ouverts, branches non étudiées, fiabilisation du dépôt documentaire"
codename: LC-RACCORD
type: "document de travail / cartographie de reprise — HORS base scellée. Il ne scelle rien, ne compte rien, ne démontre rien (§6.4)."
version: 0.1
langue: fr
date: 2026-07-21
statut: "PROPOSITION — soumise au GO opérateur avant tout dépôt sur le dépôt git (R-55 : rien ne se dépose sans GO, fichier par fichier)."
sources_analysees: [CCC_presentation.pptx, CCC_presentation.html, LC-RACCORD-guideline.pptx (V94), LC-RACCORD-guideline__1_.pptx (V94+V98), LC-RACCORD-presentation-v2.pptx (V94), github.com/droppy94/LC_Raccord (clone 2026-07-21, état V96, manifeste v2.124, PKG 914c077a)]
garde_fou: "{ A4 ; A2★ ; N } INCHANGÉ · CCC non démontrée NI réfutée · ce lotissement est un acte d'organisation, jamais un verdict de substance."
---

# 0. Objet et méthode

Ce document lotit le programme en **cinq silos** :

- **Silo R** — résultats pour lesquels un statut « établi / acquis / soldé » est stipulé : **tout redémontrer** et vérifier que le résultat est établi correctement (algèbre rejouée + sceau exécutable + cible gelée).
- **Silo P** — branches **partiellement étudiées** (décision ouverte, pivot actif, adjudication pendante).
- **Silo V** — branches **en veille** (closes en l'état, réouvrables sur intrant externe nommé).
- **Silo X** — branches **non encore étudiées / à inventer / hors de portée**.
- **Silo G** — **fiabilisation du dépôt documentaire** (GitHub `droppy94/LC_Raccord`), condition de possibilité de tous les autres.

Discipline appliquée : chaque redémonstration du Silo R suit le protocole §2.0 (cible gelée AVANT relecture de source ; script `verif_*.py` EXIT 0 ; sha256 ; audit froid pour tout verdict de substance). « Redémontré » signifiera au mieux **« algèbre correcte + cibles reproduites, sous hypothèses explicites »** — jamais davantage.

---

# 1. Constat d'audit du dépôt (2026-07-21)

Faits mesurés sur le clone :

1. **Composition** : 259 fichiers — `kb/` 215 .md, `instruments/` 13 .py, `manifest/` 1 .md (v2.124). Cohérent avec le §0 déclaré (228 hachés = 215 .md + 13 .py).
2. **Écart sceaux cités / sceaux présents** : la KB cite **83** scripts `verif_*.py` distincts ; le dépôt en contient **6** (`verif_A2_numerique`, `verif_A4_QW`, `verif_A4_QW_typeI_succ`, `verif_D3_P6_specB_oracle`, `verif_nonlin_parity`, `verif_paquet_propre`). **77 sceaux cités sont absents** — conséquence de la décharge v2.74 (72 .py pinnés-clos → 16 bundles hors-KB, réversibles, détenus opérateur). Le défaut #10 du manifeste (« sceaux cités absents du mount, 3/8 ») est un cas particulier de cet écart général côté dépôt git.
3. **Portabilité des sceaux** : rejoués sur le clone — `verif_A4_QW_typeI_succ.py` : **8/8 EXIT 0** ✓ ; `verif_paquet_propre.py` : **ÉCHEC** (« paquet introuvable ») car il résout son fichier cible au niveau racine alors que le repo range la KB sous `kb/`. Les sceaux présument le layout du mount `/mnt/project` (R-54) et ne sont pas rejouables tels quels depuis le git.
4. **Source PDF** : retirée du périmètre haché en V95/V96 (« 0 autre ») ; absente du dépôt. Les gates R-41 futures qui la citent ne sont pas rejouables depuis le git seul.
5. **Manifeste** : le journal de gel est présent (v2.124) mais le PKG-SHA porte sur le **mount**, pas sur l'arborescence git — les deux registres d'intégrité (PKG-SHA / commit-SHA) ne sont pas encore raccordés par une recette écrite.

Conclusion d'audit : le dépôt git est aujourd'hui une **archive lisible fiable pour les têtes .md**, mais **non autoportante pour la vérification** : la majorité des « établis » y sont affirmés sans leur sceau exécutable. C'est l'objet des silos R et G.

---

# 2. Silo R — redémonstration des résultats stipulés « établis »

## 2.0 Protocole commun de redémonstration (applicable à chaque lot R-n)

1. **Gel de cible** : extraire de la tête KB (`LC-D-*`) les cibles numériques/algébriques revendiquées ; les figer (sha256) AVANT toute redérivation.
2. **Redérivation indépendante** : refaire l'algèbre depuis les prémisses nommées de la tête, sans lire le corps de dérivation d'origine (dérivation aveugle → réconciliation, précédent [B]).
3. **Sceau** : écrire (ou ré-importer puis rejouer) le `verif_*.py` ; exigence EXIT 0, firewalls mordants (mutations de contrôle), sha256 consigné hors-fichier.
4. **Grade** : trois issues possibles par lot — `REPRODUIT` (byte/cible-exact) · `REPRODUIT-SOUS-RÉSERVE` (écart nommé, borné) · `NON-REPRODUIT` (le statut « établi » est alors requalifié en décision ouverte — c'est un résultat, pas un échec).
5. **Audit froid** obligatoire pour tout lot dont l'issue diffère de la tête scellée.

## 2.1 Lots de redémonstration

| Lot | Résultat stipulé « établi » | Têtes KB (dépôt) | Sceau(x) cité(s) | Présent au git |
|---|---|---|---|---|
| **R-1** | [A] Extension conforme régulière à Λ>0 (Friedrich 1986) ; N\|ℐ⁺ = −Λ/3 < 0, métrique non dégénérée | LC-01/06 cadre, LC-A-* | `verif_moduleA_scri.py` | ✗ |
| **R-2** | Verrou D1 cartographié (Newman, Tod, Nurowski convergent en radiation ; liberté = une constante) | LC-A-D1-*, LC-D-D1-* | `verif_D1_facteur.py`, `verif_D1_atlas.py`, `verif_D1_bianchiA.py`, `verif_D1_stabilite.py` | ✗ |
| **R-3** | Spectre primordial ⟨g₃g₃⟩ ~ k³ (invariance d'échelle, contact CMB) | LC-D3-SPECTRE-K3 | `verif_D3_spectre_k3.py`, `verif_D3_bunchdavies.py` | ✗ |
| **R-4** | Charge centrale C_T ∝ N ; A_T·N = 16 par deux routes convergentes | LC-D-CT-DUAL, LC-D-CT-DUAL-DS, LC-D-CT-GAMMA | `verif_D_CT_ATN.py` (45 citations), `verif_D_CT_dual.py`, `verif_D_CT_dual_dS.py`, `verif_D_CT_realite.py`, `verif_D_CT_gardefou_dS.py` | ✗ |
| **R-5** | Trois réductions (A3⟷D1, D1⟷E, sceau C_T) ⟹ arc gaussien ramené à { A4 ; A2★ ; N } | LC-WORK-A3-D1-PASSERELLE, LC-WORK-D1-E-AMPLITUDE, LC-SYNTHESE-SOCLES-* | `verif_A3_D1_passerelle.py` | ✗ |
| **R-6** | Non-gaussien ⟨TTT⟩ reproduit sous gravité d'Einstein (audité 4/4, ACQUIS) ; verrou 4-pt ∝N⁻³ | LC-WORK-CADRAGE-NONGAUSS(-4PT) | `verif_D_nongauss_TTT.py` (+ variantes lourd/4pt) | ✗ |
| **R-7** | W2 « résidu-cassant » (no-hair ne nettoie pas le Weyl rescalé) — 14/14 + successeur type-I 8/8 | LC-D-A4-QW | `verif_A4_QW.py`, `verif_A4_QW_typeI_succ.py` | ✓ (successeur rejoué 8/8 EXIT 0 le 2026-07-21) |
| **R-8** | A2★ mésoscopique (modèle Gauss-Kuzmin, non-cascade) + oracle P6 | LC-D3-INTERAEON-P6, LC-D3-C7B-VERDICT-A2 | `verif_A2_numerique.py` ✓, `verif_D3_P6_specB_oracle.py` ✓, `verif_D3_C7b_*` ✗ | partiel |
| **R-9** | [B] tracteur S² : Ω^𝒯 = Weyl ⊕ Cotton, verdict B-PAUVRE, durci sur dS perturbé (V98) | têtes [B] (à localiser au mount ; non vues au git) | sceau non identifié au dépôt | ✗ |
| **R-10** | Parité non-linéaire du Weyl rescalé (E pair / B impair, 5+5=10) + deux-point + Cotton + représentation | LC-D3-*, têtes nonlin | `verif_nonlin_parity.py` ✓, `verif_nonlin_deuxpoint.py` ✗, `verif_nonlin_cotton.py` ✗, `verif_nonlin_repr.py` ✗ | partiel |
| **R-11** | Falsifiabilité F1–F6 « épuisée » + mémoire BMS (BORD-EON V-A) + W2/WCH-GWE | LC-WORK-BRANCHE-FALSIFIABILITE, LC-D-F6-*, LC-D-F4-* | `verif_F1_spn.py`, `verif_F4_principiel.py`, `verif_F5_scaling.py`, `verif_F6_memoire_cisaillement.py`, `verif_D3_WCH_GWE.py` | ✗ |
| **R-12** | O₂ : jonction D→N, Δ_𝒞 = d au pas C1-b, Hodge, coin-transmission (α = C1-b POSITIF) | LC-D-O2-JONCTION, LC-D-O2-DELTA-C, LC-D-O2-COIN-TRANSMISSION, LC-D-O2-P1/P2 | `verif_O2_P1.py`, `verif_O2_P2.py`, `verif_O2_hodge.py`, `verif_O2_coin_transmission_*.py` | ✗ |

**Priorité interne au Silo R** : R-4 → R-5 → R-3 → R-6 d'abord (c'est l'arc qui porte la réduction { A4 ; A2★ ; N }, le résultat le plus revendiqué du programme) ; puis R-2 et R-12 (racines communes D1/O₂ du front vif) ; R-1, R-11 ensuite ; R-7/R-8/R-10 en simple rejeu + complétion (sceaux partiellement présents).

---

# 3. Silo P — branches partiellement étudiées (décisions ouvertes)

| Lot | Front | État stipulé (V96/V98) | Prochain pas défini |
|---|---|---|---|
| **P-1** | **β ≡ G3** — transport AdS→dS (« T-b »), seul facteur d'O₂ ouvert | Mur RE⁴ situé, résidu nommé, levier prescription-dépendant ; gates β **débloquées** par P-8 (générateur v2.1) | Consommation des 3 sources pistées (Bros–Moschella ; Nakayama ; Ghaffari–Luciano–Mantica) sous gate R-41 ≥3 miroirs + espace-verdict gelé |
| **P-2** | **p★ / P-SELECTEUR** (poids b, Odak–Speziale) | Adjudication **PENDANTE sous constat BIAISÉ** (CSE-1 : G-2) ; fork bloqué à sa gate ; question A/B non tranchée | Amendement b4 daté et postérieur réparant l'atteignabilité de P-1, OU constat P-3 / intrant nommé |
| **P-3** | **Nœud (i) — entier p_Q** (fissure croisée spin-4) | Matérialisé V96, verdict **INDÉTERMINÉ (pas A)**, délimitation ; ≅ transport AdS→dS au pas C1-b ≅ intrant p★ | Report modulaire d = 3 (**recommandé #1** dans les decks) : arbitre du proxy 2D + route vers p_Q (racine commune g₃) — gate §A levée sur (i) seulement, (ii) proxy porteur et (iii) question sharp d=3 restent à lever |
| **P-4** | **D1 — sélection du facteur conforme** | Cartographié (3 prescriptions convergent), sélection non tranchée ; racine commune avec β | Verrou jumeau de β : suit P-1 |
| **P-5** | **[C] — structure modulaire du vide** | Délimitée V98 (fork SO(4,1)/SO(4,2) tranché ; Σ≃S³ caractérisé ; R1–R5 miroir-vérifiés ; lacune Wiesbrock comblée) ; **cœur restant à inventer** : relèvement Tier 2 = boost modulaire dS II₁ (CLPW) ⊕ reconstruction Borchers–Wiesbrock | Cadrage du relèvement Tier 2 (glisse vers Silo X si l'invention domine) |
| **P-6** | **File C1 — admissibilité** | ⚠ statut à trancher : à distinguer du « critère C1 resserré » de N (clos 07-13) avant de compter comme item P1 restant | Passe de désambiguïsation KB-only, puis décision opérateur |
| **P-7** | **W³** — falsifiabilité non-gaussienne d'ordre supérieur | Ouverte (aval de ⟨TTT⟩) ; R-c (≥5-pt / boucles) = seule strate encore imprimable en interne | Sceau ≥5-pt arbre Einstein-pur (durcit la RÉSERVE sans réduire le compte) |
| **P-8** | **Nœud (ii)** — dégradation signée O(γ₄) de la balance détaillée | En veille active (peut rouvrir même si (i) reste gaté) | Surveillance ; cadrage si réouverture |
| **P-9** | **Croisé M_ab** | Forme croisée avec intertwiner correct + signe global dS | Audit froid obligatoire avant tout statut |

---

# 4. Silo V — veille (closes en l'état, réouvrables sur intrant externe nommé)

Tracker R-53 : **0/4 franchi**. Chaque lot porte, écrite, sa condition de réouverture.

| Lot | Hypothèse | Clôture | Intrant qui rouvrirait |
|---|---|---|---|
| **V-1** | **A4** (courbure de Weyl) | Route par-ℐ⁺ délimitée (W2), postulat renforcé, non réfuté | No-hair **générique** prouvé (RG inhomogène, grandes données) |
| **V-2** | **A2★** (additivité / non-cascade) | Parquée : soutenue en G₂, gap au générique 3D nommé | Résultat externe de RG générique 3D — statistique des spikes |
| **V-3** | **N ≡ Λ** | Voie A close, confirmée et resserrée (amendement √S_dS audité) | Intrant de gravité quantique : comptage microscopique de S_dS |
| **V-4** | Réouverture jointe **A4 + D1** | — | β / O₂ résolu (la CFT de raccordement construite) |

Routes internes refermées, à ne PAS ré-explorer sans ingrédient neuf : handle g₃ (circulaire) · transport Δ-𝒞 (bloqué, carte D↔N/shadow non renormalisée) · KPS / réplique Marolf–Morrison (hors-domaine K-B, 0,93 — horizon cosmologique, pas ℐ⁺ ; veille v2 de la source avant toute réouverture).

---

# 5. Silo X — non étudiées / à inventer / hors de portée

| Lot | Objet | Statut |
|---|---|---|
| **X-1** | **La masse** — toutes les particules effectivement sans masse à ℐ⁺ (condition nécessaire du raccord) | Non géométrique, **jamais instruit** ; aucun front ouvert |
| **X-2** | **Secteur dilaton [E]** — la brique qui scellerait p_Q | Hypothèse de travail **non construite** (CCC quantique) ; redirige vers [D] |
| **X-3** | **O₂ — la CFT de raccordement elle-même** | N'existe pas ; à INVENTER (β en est le seul facteur ouvert — P-1) |
| **X-4** | **[C] Tier 2** — boost modulaire dS II₁ ⊕ Borchers–Wiesbrock | Cœur à inventer (interface avec P-5) |
| **X-5** | **[F] Unification RG–MQ** | Largement hors de portée ; non attaqué |

Ces lots ne reçoivent pas de plan d'exécution : ils reçoivent un **cadrage d'entrée** chacun (une page : question, prémisses, ce qui compterait comme premier résultat, firewall anti-circularité) — livrable du Silo G, pas un engagement de substance.

---

# 6. Silo G — fiabilisation du dépôt documentaire (GitHub)

C'est le silo **prioritaire chronologiquement** : les silos R et P s'y adossent.

- **G-0 — Inventaire d'écart (fait, à déposer).** Table exhaustive « sceau cité ↔ présent/absent » (83 cités / 6 présents / 77 absents), générée par script rejouable (`instruments/inventaire_sceaux.py`), sortie versionnée. Étend le défaut #10 du manifeste au périmètre git complet.
- **G-1 — Ré-import des sceaux déchargés.** Les 16 bundles hors-KB de la décharge v2.74 sont sha-attestés et réversibles : ré-import des 72 .py dans `instruments/` (ou dans `instruments/archives-scelees/` pour distinguer sceaux LIVE / pinnés-clos), confrontation sha au registre de sortie du manifeste. **Alternative si les bundles ne sont pas fournis** : chaque sceau absent est réécrit lors de son lot R-n — plus coûteux, mais c'est précisément la redémonstration demandée ; l'écart éventuel entre sceau réécrit et sha d'origine devient une donnée d'audit.
- **G-2 — Portabilité des sceaux.** Correctif de résolution de chemin (variable `LC_KB_ROOT`, défaut `kb/` en repo, `/mnt/project` au mount), sans toucher aux clés de sceau ; `verif_paquet_propre.py` est le cas témoin (échec constaté sur le layout git). Tout swap d'instrument suit la discipline existante (grade « instruments bornés par invariants »).
- **G-3 — Harnais de rejeu (CI).** Un `rejeu_sceaux.py` (ou workflow GitHub Actions) qui rejoue tous les sceaux LIVE, exige EXIT 0, recompute les sha256, et publie un rapport ; les canaris lourds (≥600 s) en tâche séparée. Équivalent instrumenté du §0-full, exécutable par quiconque clone.
- **G-4 — Raccord des deux registres d'intégrité.** Recette écrite reliant PKG-SHA (mount, R-54) et commit-SHA (git) : le README l'esquisse, il manque la recette exécutable (script qui recompute le PKG-SHA sur l'arborescence git et le confronte au §0 du manifeste). Décision opérateur à acter : le mount **reste** autoritaire (R-54) ; le git est miroir vérifiable — ou bascule d'autorité, à cadrer séparément.
- **G-5 — Complétude documentaire.** (a) Sort de la source PDF (5 Mo, retirée du hachage V95) : Git LFS, ou pointeur sha + miroirs R-41 ; (b) index `LC-00-INDEX` absent du clone : à déposer ou à générer (`LC-WORK-GEN-INDEX.py` présent) ; (c) arborescence des silos : un `silos/SILO-{R,P,V,X,G}/README.md` chacun, portant sa table de lots et le statut courant — c'est le présent document éclaté en unités de suivi.

---

# 7. Séquencement proposé

1. **G-0 → G-2** (une session) : inventaire déposé, chemins portables, sceaux présents rejoués verts sur le git.
2. **G-1** dès réception des bundles (ou décision « réécriture ») ; **G-3** dans la foulée.
3. **Silo R** dans l'ordre R-4 → R-5 → R-3 → R-6 → R-2/R-12 → reste ; un lot = un cycle complet du protocole §2.0.
4. **Silo P** en parallèle sur décision opérateur, en tête P-3 (report modulaire d = 3, la recommandation #1 des decks — arbitre + route), sans court-circuiter les gates existantes (β#1/α#2 maintenu par la cartographie v1.2 : la priorisation entre P-1 et P-3 **appartient à l'opérateur**).
5. Silos V et X : pas d'exécution ; cadrages d'entrée (G-5c) et tracker R-53 tenus à jour.

---

# 8. Éléments requis de l'opérateur

1. **Accès GitHub en écriture** — un *fine-grained Personal Access Token* limité au seul dépôt `droppy94/LC_Raccord`, permissions : Contents (Read/Write) + Metadata (Read). Durée courte (7 jours), révocable, à régénérer au besoin : l'environnement de travail est réinitialisé entre sessions, le token devra être refourni à chaque session de dépôt. Push via `https://<TOKEN>@github.com/droppy94/LC_Raccord.git` (le réseau sortant vers github.com est autorisé ici). Réserve de sûreté : un token collé en conversation y reste lisible — le scoper au strict minimum et le révoquer après la campagne de dépôts est la bonne pratique.
2. **Les 16 bundles hors-KB** de la décharge v2.74 (les 72 .py pinnés-clos + leur index nom↔sha), pour G-1 — ou le GO explicite pour la voie « réécriture au fil des lots R-n ».
3. **La source PDF** retirée en V95 (ou son sha + références de miroirs), pour G-5a.
4. **Trois décisions** : (a) autorité mount vs git (G-4) ; (b) G-1 ré-import vs réécriture ; (c) priorisation P-1 (β) vs P-3 (report d = 3) — la cartographie v1.2 maintient β#1, les decks recommandent d = 3 : le choix revient à l'opérateur.
5. **GO fichier par fichier** avant tout push (discipline R-55 conservée : chaque dépôt git sera annoncé — chemin, sha256, message de commit — et poussé après confirmation).

---

*§6.4 — sentinelle terminale. Ce lotissement organise ; il ne scelle, ne réduit, ne compte, ne démontre rien. { A4 ; A2★ ; N } INCHANGÉ · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) · O₂ non construit · β T-b seul facteur d'O₂ ouvert · nœud (i) INDÉTERMINÉ (pas A) · CCC non démontrée NI réfutée.*
