---
id: NOTE-REPRISE-GIT-S7
titre: "Note de reprise autoportante — fin de session S7 (2026-07-22) : lot R-7 repris de ZÉRO, dérivé, clos et déposé (REPRODUIT-SOUS-RÉSERVE E-2). Silo R à 10/12. Têtes [B] ABSENTES du dépôt (fait mesuré) mais FOURNIES hors-KB par l'opérateur en fin de S7, mises en quarantaine, corps NON ouverts : R-9 est DÉBLOQUÉ. Prochain geste : R-9 ou R-11, au choix de l'opérateur."
codename: LC-RACCORD
type: "note de reprise — HORS base scellée du mount. Elle ne scelle rien, ne compte rien, ne démontre rien (§6.4). Le mount /mnt/project reste autoritaire (R-54) ; ce dépôt git est le miroir vérifiable."
version: 1.0
langue: fr
date: 2026-07-22
piege_R36: "Cette note NE PORTE NI son propre sha NI le commit qui la dépose. Attendu à l'ouverture : HEAD = le commit dont le message commence par « Reprise S7 » ; le vérifier par git log, JAMAIS par cette note."
---

# Note de reprise S7 — état, acquis, et prochain geste

## 0. Attendus vérifiables à l'ouverture (§0-lite du dépôt)

À exécuter en tête de session neuve, AVANT tout geste :

    git clone https://github.com/droppy94/LC_Raccord.git && cd LC_Raccord
    git log --oneline -9   # attendu : HEAD = « Reprise S7 … », puis b24cd65 (R-7),
                           #   7e245d2 (Reprise S6), f415070 (R-10), db10757 (Reprise S5),
                           #   c0ea2ba (R-8), 7c9fb0b (Reprise S4), a931a4c (R-1),
                           #   9568756 (R-12)
    ls instruments/*.py | wc -l                    # attendu : 29   (28 en S6, + redemo_R7_A4QW.py)
    ls instruments/archives-scelees/*.py | wc -l   # attendu : 76
    ls audit/ | wc -l                              # attendu : 27
    ls kb/*.md | wc -l                             # attendu : 215
    python3 instruments/inventaire_sceaux.py       # attendu : 6 LIVE / 76 ARCHIVE / 1 ABSENT
    python3 instruments/run_sceau.py verif_paquet_propre    # attendu : sha8=051e2833 rc=0
    python3 instruments/redemo_R4_CT_b.py          # attendu : 35/35 PASS +  5 consignations
    python3 instruments/redemo_R5_reductions_b.py  # attendu : 17/17 PASS +  5 consignations
    python3 instruments/redemo_R3_spectre.py       # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R6_nongauss.py      # attendu : 16/16 PASS +  6 consignations
    python3 instruments/redemo_R2_D1.py            # attendu : 12/12 PASS +  8 consignations
    python3 instruments/redemo_R12_O2.py           # attendu : 11/11 PASS +  7 consignations
    python3 instruments/redemo_R1_moduleA.py       # attendu :   6/6 PASS +  3 consignations
    python3 instruments/redemo_R8_A2star.py        # attendu : 21/21 PASS + 10 consignations
    python3 instruments/redemo_R10_nonlin.py       # attendu : 40/40 PASS + 14 consignations
    python3 instruments/redemo_R7_A4QW.py          # attendu : 45/45 PASS + 10 consignations
                                                   #   (NOUVEAU S7 ; sympy seul)

**Total attendu : 219/219 PASS + 74 consignations, 10/10 rc = 0.**

**L'addition est DÉCOMPOSÉE, pas supposée** — elle a été exécutée d'un bloc
en fin de S7, sur le dépôt à `b24cd65` :

    PASS  : 35 + 17 + 16 + 16 + 12 + 11 + 6 + 21 + 40 + 45 = 219
    CONS. :  5 +  5 +  6 +  6 +  8 +  7 + 3 + 10 + 14 + 10 =  74

et **recomptée indépendamment** (comptage des marqueurs `[PASS]` /
`[CONSIGNATION]` dans les logs, sans faire confiance à la ligne de bilan
que chaque script imprime sur lui-même) : **219 + 74, concordant lot par
lot**. Aucun instrument ne sur-déclare son compte.

Tout écart est à décomposer AVANT de poursuivre (leçon V62). Le premier
chiffre à décomposer en cas d'écart reste **l'addition**, puis le lot
divergent, puis l'assert.

### Leçons d'environnement opposables

Toutes MAINTENUES : rejeu long = `setsid nohup … &` puis poll (S2) ;
créer un répertoire de logs dans un appel SÉPARÉ du lancement (S4) ;
vérification de push = repli `origin/main` (S4) ; compter `ls audit/` et
non `ls audit/*.md` (S5) ; `verif_D3_P6_specB_oracle.py` est LENT
(~130 s) ; `verif_nonlin_cotton` ≈ 139 s, `verif_nonlin_parity` ≈ 308 s
(canari) ; ne PAS lancer deux sceaux en concurrence dans le même arbre
(S6). Branche distante `origin/front-pq` : RÉSIDUELLE, contenue dans
main — bénigne, ne pas toucher.

**Écart d'arbre bénin, récurrent et attendu** : `inventaire_sceaux.py`
réécrit sa propre ligne de date à chaque exécution (bilan identique :
6/76/1). Restaurer par `git checkout -- audit/INVENTAIRE-SCEAUX.md` ;
vérifié en S7 : `git diff --stat` = 1 fichier, 1 insertion, 1 suppression,
et le diff nominal est exactement la date. Ce n'est pas une modification
de substance.

**Nouveau S7 — les durées ne se reportent pas.** `redemo_R7_A4QW.py` a
mesuré ≈ 12 s au rejeu final et plusieurs minutes lors des passages de
mise au point (charge concurrente du conteneur). Précédent S6 maintenu et
renforcé : **la durée d'exécution n'est pas une clé de sceau** ; les
durées consignées attestent UNE exécution sur CE clone à CETTE date.

## 1. Ce qui a été fait en S7 (sur GO opérateur, R-55 tenu fichier par fichier)

1. **§0-lite S6 rejoué CONFORME** sur toute la ligne : 174/174 PASS,
   64 consignations, 9/9 rc = 0, HEAD et comptes exacts. L'addition
   174/64 — jamais exécutée d'un bloc jusque-là — **tombe juste**, et le
   recompte indépendant concorde lot par lot.
2. **LOT R-7 REPRIS DE ZÉRO, DÉRIVÉ ET CLOS** (commit `b24cd65`).
   **Corps de `LC-D-A4-QW` (lignes 16–159) JAMAIS OUVERT** ; les six
   prérequis KB déclarés et l'amendement `…-TYPEI-CORR` sont restés
   **fermés** — l'aveuglement est intact et le reste, disponible pour
   toute contestation ultérieure. Gel `ef6e9f5e…6b47` figé AVANT la
   première ligne d'instrument, **plafond E-2 annoncé AU GEL**.
   45/45 PASS discriminants + 10 consignations, rc 0. Harnais de
   mutation **6/6 mordantes**. Rejeu 2/2 rc 0 aux comptes et sha8 EXACTS
   du gel : `verif_A4_QW` LIVE `a4637a2c` **14/14** · `verif_A4_QW_typeI_succ`
   LIVE `79f09a8c` **8/8**. Grade **E-2**, plafond atteint non dépassé ;
   aucun audit froid déclenché (issue conforme, §2.0-5).
3. **AUTO-AUDIT CONTRE LE PILOTE, avant tout grade.** La v1 de
   l'instrument portait un assert d'évolution **mal construit et
   quasi-vacant** (comparaison d'une expression à elle-même). Détecté,
   retiré, **la v1 n'a jamais servi de base à un grade** ; remplacé par
   une identité à **coefficients indéterminés RÉSOLUS** (½, ½, −½, −½).
   Quatre autres blocs fragiles corrigés au même cycle. Balayage
   statique : 46 blocs `check`, **aucun `True` littéral**, aucun
   coefficient posé puis comparé à lui-même.
4. **R-9 INSTRUIT SANS ÊTRE OUVERT** (voir §4) : les têtes [B] sont
   **ABSENTES du dépôt git** — fait mesuré, plus une conjecture. **Puis,
   en fin de session, l'opérateur a FOURNI la tranche [B] hors-KB** :
   archive `hors-KB_B_objet-sur-S2_TRANCHE-2026-07-18.zip`, sha256
   `b0ea7a7d4880f8b909518befe4b28d52fdd4774f373906385bd36b07dce5333f`,
   **mise en quarantaine, corps NON ouverts**. R-9 est DÉBLOQUÉ.
5. Le commit qui dépose la présente note (swap −S6 +S7 ; S1–S6 restent
   dans l'historique git).

**Bilan Silo R : 10/12 lots clos — R-1 ✓ R-2 ✓ R-3 ✓ R-4 ✓ R-5 ✓ R-6 ✓
R-7 ✓ R-8 ✓ R-10 ✓ R-12 ✓, TOUS au grade REPRODUIT-SOUS-RÉSERVE (E-2).
Restent : R-9 (DÉBLOQUÉ — têtes [B] absentes du git mais fournies
hors-KB, §4) ; R-11 (gabarit lourd, exécutable en autonomie).**

## 2. Contenu de substance de R-7 — pour mémoire

- **Q5** `Σq_i = 0` **et** `Σq_i² = 2/3` **RÉSOLUS depuis la seule
  contrainte hamiltonienne** : injection de
  `a_i = sinh^{1/3}(3Ht)·tanh^{q_i}(3Ht/2)` ; le coefficient de
  `cosh(3Ht)` résout `Σq=0`, le terme constant s'ajuste en `9·e₂+3` par
  `solve` ⟹ `e₂ = −1/3` ⟹ `Σq² = 2/3`. **L'évolution ne contraint que
  `Σq=0`.** FIREWALL : le système `{Σq=0 ; Σq²=2/3 ; q₁=q₂=q₃}` est
  **SANS SOLUTION** ⟹ le type I VIDE ne contient **aucun** point
  isotrope.
- **Q2** taux 3 **RÉSOLU** par `ω = √(3Λ) = 3H` (annulation du
  coefficient de `sinh²` dans `V'² = 3ΛV² + (3/2)Σc²`). Firewalls de
  taux mordants des deux côtés : `e^{2Ht}E → 0`, `e^{4Ht}|E| → ∞`.
- **Q3 — la coïncidence est STRUCTURELLE, pas un accident de d = 3.**
  Racines indicielles `{0, d}` par Frobenius ; en dimension `d` la
  contrainte isotrope résout `H = √(2Λ/d(d−1))`, donc `θ = dH`, donc taux
  de cisaillement `= d`. Taux et `Δ₊` sont **la même expression en d** —
  3 et 3 à `d=3`, 4 et 4 à `d=4`.
- **Q5/Q9** série FG en `η` : **aucun terme η¹**, **`g₂ = 0`**, et
  `g₃ = −4·q·g₀` avec le coefficient **RÉSOLU par solve**.
- **Q4** Weyl 4D calculé depuis la métrique ⟹ `lim e^{3Ht}E_i = 6H²q_i` ;
  résidu rescalé `𝓔_i = 6q_i/H`, fini, non nul, sans trace ; rapport
  `𝓔/g₃` résolu ⟹ facteur **3/2 reproduit EXACTEMENT**.
- **Q8 — TRANSCRIPTION.** Le coefficient du mode décroissant du Weyl NU
  est **proportionnel à `g₃`, avec le MÊME rapport sur les trois axes**.
  Weyl nu → 0 (taux 3) ET résidu rescalé ≠ 0 **simultanément** ⟹ le
  chaînon « no-hair ⟹ Weyl-rescalé-propre » **CASSE** ⟹ **W2**.
- **Q7** le point `q=0` (`a_i = sinh^{1/3}`) est isotrope mais **NON
  VIDE** : `ρ = 3H²/sinh²(3Ht)`, `ρ·a⁶` constant ⟹ **fluide raide**. De
  Sitter `a_i = e^{Ht}` est le membre isotrope **VIDE**, `g_ii(η) = H²`
  constant ⟹ **`g₃ = 0`**. Deux points isotropes **distincts** ⟹
  universalité de `g₃=−4q_i` **RETIRÉE**, W2 générique intact — concordant
  avec le successeur `[05']`.
- **Q6** `Cotton[Nil] ≠ 0` sur **8 composantes** (`C_{xyz} = −1/2`) avec
  `R = −1/2` **CONSTANT** ; FIREWALL de contrôle `Cotton[δ₃] = 0`. Le
  verrou magnétique tient à la **non-platitude conforme**, PAS à la
  constance de `R` (recoupe R-10/Q1). Aucun `q_i`, aucun `g₃` n'entre
  dans `Cotton[Nil]` ⟹ **𝓑 indépendant des données**.

**Trois consignations de fond, à ne pas perdre :**

- **(a) ÉCART DE SIGNE NOMMÉ, NON CORRIGÉ.** Sous les conventions
  déclarées en tête d'instrument, le `solve` rend `𝓔 = −(3/2H)·g₃` ; la
  cible écrit `+`. **Magnitude et facteur 3/2 exacts** ; l'écart est borné
  à un **signe global commun aux trois composantes** et tient à une
  convention que le front-matter ne fixe pas — notamment l'orientation de
  la normale à ℐ⁺, **de genre ESPACE en dS**, ce qui échange les rôles
  électrique/magnétique par rapport au cas lorentzien. **Aucune tolérance
  desserrée** (précédents R-2/Q6 et R-10/(a)).
- **(b) `g₃` est porté par le SEUL facteur anisotrope `tanh^{2q_i}`.**
  Muter l'exposant `2/3` du facteur `((1−η⁶)/2)` **ne change pas**
  `g₃/q = −4` : ce facteur ne contribue qu'à l'ordre `η⁶`. Mutation
  **vacante par mauvais ciblage**, détectée par le harnais, remplacée par
  la mutation `2q → q` qui mord (−4 → −2).
- **(c) Homonymie R-7.** Les fichiers `LC-WORK-AMENDEMENT-R7-A4-QW-*`
  relèvent de la **règle de discipline R-7** (« cibles tenues telles
  qu'écrites, zéro amendement, zéro fetch »), **non du lot R-7**. Ce
  n'est pas une fuite d'aveuglement.

## 3. Discipline en vigueur (inchangée + précédents S7)

Discipline amendée post-CSE (note S3 §2), précédents S4, S5 et S6 :
**tous maintenus**. Précédents **S7** opposables :

- **Une mutation peut être VACANTE PAR MAUVAIS CIBLAGE, pas seulement par
  invariance.** Le précédent S5 disait « mutation invariante = vacante » ;
  S7 l'étend : une mutation peut porter sur un facteur qui **ne contribue
  pas à l'ordre où vit la cible**. Elle est alors vacante bien que le
  paramètre muté soit réel. **Un harnais de mutation doit donc muter le
  porteur identifié de la cible, pas un paramètre voisin.** Une mutation
  qui ne mord pas se REMPLACE ; elle ne se compte jamais.
- **Un assert qui ÉCHOUE peut être un assert MAL CONSTRUIT, pas une cible
  qui tombe.** En S7 l'assert d'évolution a FAIL au premier passage : le
  diagnostic n'était pas « la cible est fausse » mais « ma condition
  compare une expression à elle-même ». **Lire l'assert avant d'accuser la
  cible.** Corollaire : ne jamais « réparer » un assert en relâchant sa
  condition — le reformuler en `solve` à coefficients indéterminés.
- **Substituer la contrainte AVANT de dériver.** Un `simplify` non borné a
  tourné **14 minutes** sur un seul assert ; substituer `Σq=0` avant la
  dérivation réduit `V` à `sinh(3Ht)` exactement et ramène le même test à
  **1,6 s**. Généralisation : imposer les contraintes du problème le plus
  tôt possible dans la chaîne symbolique.
- **Un bloc évalué hors de la surface de contrainte échoue légitimement.**
  Le bloc Weyl de S7 a d'abord été évalué sur la famille à `q₃` LIBRE
  alors que les équations d'Einstein imposent `Σq=0` : l'échec était
  correct. **Vérifier sur quelle surface un bloc est évalué avant de
  toucher à quoi que ce soit d'autre.**
- **`pgrep -f <motif>` S'AUTO-MATCHE** quand le motif figure dans la
  commande de sondage. En S7 cette fausse détection a fait croire trois
  fois qu'un process tué était vivant. **Sonder par
  `ps -eo pid,etime,cmd | grep "[p]ython3"`**, jamais par `pgrep -f` sur
  le nom du script.
- **L'ordre du token a été tenu MALGRÉ une fourniture anticipée.** En S7
  le token a été collé au premier message, contre l'ordre prescrit ; il
  n'a été **utilisé qu'au push**, après annonce des trois sha et GO
  opérateur. La règle S6 (« le token est le DERNIER intrant ») reste la
  bonne pratique **et se tient même quand l'opérateur la court-circuite**.
- **Les sha s'annoncent, se re-confrontent, puis se déposent** — et le
  contenu INDEXÉ se vérifie identique au contenu disque, blob par blob,
  avant le commit (fait en S7 sur les trois pièces).

## 4. R-9 — instruit sans être ouvert : les têtes [B] sont ABSENTES

Recherche menée en S7 **sans ouvrir aucun corps** (lignes `id:` et
`tags:` seules, comptages de fichiers) :

- **aucune tête ne porte le tag `module-B`** ;
- **aucune occurrence de « Cartan » dans un `id:` ou un `tags:`** — le
  terme n'apparaît que dans les quatre fichiers de cadrage
  `kb/01_cadre-conceptuel.md`, `kb/02_programme.md`, `kb/03_glossaire.md`,
  `kb/04_references.md` ;
- le seul match superficiel sur « TRACTEUR » était
  `LC-D3-CROSSOVER-ATTRACTEUR.md` — **faux positif** (sous-chaîne de
  « ATTRACTEUR »).

**Conclusion, à opposer** : les têtes du module [B] (tracteur S²,
`Ω^𝒯 = Weyl ⊕ Cotton`, verdict B-PAUVRE, durcissement dS perturbé V98)
**n'existent pas dans le dépôt git**. La suspicion portée par la note S6
(« possiblement ABSENTES ») est **confirmée par mesure**.

⟹ **R-9 ne peut PAS être ouvert depuis le git seul.** Ouvrir le lot sans
les têtes reviendrait à reconstruire la cible, ce que le §2.0 interdit.

### 4bis. Intrant FOURNI en fin de S7 — R-9 débloqué

L'opérateur a fourni la tranche [B] hors-KB. **Archive** :
`hors-KB_B_objet-sur-S2_TRANCHE-2026-07-18.zip`, sha256
`b0ea7a7d4880f8b909518befe4b28d52fdd4774f373906385bd36b07dce5333f`,
14110 octets, datée 2026-07-18. **Quatre pièces**, extraites en
**quarantaine hors dépôt**, sha256 calculés, **aucun corps ouvert** :

| pièce | sha256 (32 premiers) | octets | lignes |
|---|---|---|---|
| `LC-RESULTAT-B-TRACTEUR.md` | `91bf1057a9024f65118faba7b3f74389…` | 13060 | 230 |
| `LC-PAQUET-B-OBJET-S2.md` | `d23ff97945de3f2e592e6a24c1a6a23a…` | 9451 | 183 |
| `verif_B_tracteur.py` | `8e3866861f816e0dd7c8e7bde1e4ddd8…` | 6976 | 144 |
| `REIMPORT.txt` | `ace2218aa01c455f7b257e08cc920bf4…` | 1751 | 34 |

Front-matters : `LC-RESULTAT-B-TRACTEUR.md` clos ligne 13 (corps 14–230) ;
`LC-PAQUET-B-OBJET-S2.md` clos ligne 12 (corps 13–183).

**Trois constats de sondage STRUCTUREL** (comptages seuls, aucun texte
affiché), à opposer au gel de R-9 :

1. **`REIMPORT.txt` ne porte AUCUN sha256 ni sha8.** Ce n'est donc **pas**
   l'index nom↔sha attendu pour G-1 ; il porte 4 lignes à mentions de
   résultat. **À traiter comme pièce potentiellement guidante**, pas
   comme un manifeste neutre.
2. **Le front-matter de `LC-RESULTAT-B-TRACTEUR.md` porte le verdict**
   (5 mentions verdict/Weyl/Cotton/tracteur) ; celui de
   `LC-PAQUET-B-OBJET-S2.md` est **propre** (0 mention). Même structure
   qu'`LC-D-A4-QW` : un aveuglement TOTAL est impossible par
   construction.
3. **LIMITE STRUCTURELLE ANTÉRIEURE, à ne pas dissimuler** : le document
   `LC-WORK-LOTISSEMENT-SILOS-v0.1.md`, présent au dépôt ET dans le
   contexte de travail depuis l'ouverture, **énonce déjà la cible de
   R-9** — « [B] tracteur S² : Ω^𝒯 = Weyl ⊕ Cotton, verdict B-PAUVRE,
   durci sur dS perturbé (V98) ». Le verdict de R-9 était donc **révélé
   avant même la réception de l'archive**, indépendamment d'elle.

⟹ **Plafond de grade de R-9 : E-2, inatteignable au-dessus**, à annoncer
AU GEL et non à découvrir après. Motifs : verdict révélé par le
lotissement (constat 3) ET par le front-matter (constat 2), plus la
pièce `REIMPORT.txt` potentiellement guidante (constat 1).

## 5. Décisions opérateur EN ATTENTE

- **G-4** : autorité mount vs git (hypothèse reconduite : mount
  autoritaire R-54, git miroir vérifiable).
- **Priorisation de substance** : β / P-1 (cartographie v1.2 : β#1
  maintenu) vs report modulaire d = 3 / P-3 (recommandation #1 des decks).
- **PDF du mount** (5014 Ko) : confrontation à `sources/2503_19957v1.pdf`.
- **G-5b/c** : index `LC-00-INDEX`, arborescence des silos — cadrages non
  exécutés.
- **Têtes [B]** : à fournir depuis le mount, ou décision de laisser R-9
  ouvert avec écart consigné (voir §4 et §6).

## 6. PROCHAIN GESTE — ordre de la session neuve

1. **§0-lite** (attendus §0 ci-dessus, 10 redemo, 219/74).
2. **R-9 ou R-11 — le choix revient à l'opérateur**, les deux étant
   désormais ouvrables. **R-9** : têtes fournies en quarantaine (§4bis),
   gel de cible depuis les SEULS front-matters, corps NON ouverts,
   plafond **E-2 annoncé au gel**. **DÉCISION OPÉRATEUR PRISE EN S7 :
   `REIMPORT.txt` se lit APRÈS le gel**, jamais avant — le lire avant
   dégraderait la force probante, le lire après ne guide plus rien.
   Opposable, à ne pas rouvrir.
   Le dépôt de la tranche [B] au git relève de **G-1** et demande un GO
   distinct : les pièces sont hors-KB et n'ont pas encore de place
   arrêtée dans l'arborescence.
3. **R-11 — gabarit lourd** : lot du Silo R exécutable en autonomie
   COMPLÈTE depuis le git — têtes ET sceaux présents (vérifié en S7).
   Falsifiabilité F1–F6 « épuisée » + mémoire BMS (BORD-EON V-A) +
   W2/WCH-GWE.

   **Têtes présentes au git (20 fichiers recensés)** : `LC-D-F1-SPN`,
   `LC-D-F2-TTT-PLANCK`, `LC-D-F3-A2STAR`, `LC-D-F4-A4-PRINCIPIEL`,
   `LC-D-F5-ETAT-RACCORD`, `LC-D-F6-BMS-MEMOIRE`, `LC-D-F6-BORDEON-VA`,
   `LC-D-F6-G3-LAMBDA-BMS`, `LC-D-F6-NOTE07-VB`, `LC-D3-WCH-GWE`,
   `LC-D3-WCH-CANCELLATION`, `LC-WORK-BRANCHE-FALSIFIABILITE`, les
   cadrages `LC-WORK-CADRAGE-F4/F5/F6-*`, l'amendement
   `LC-WORK-AMENDEMENT-R7-F5-RETENUE`, et les notes
   `NOTE-BORD-EON-06/07`.

   **Sceaux : les cinq cités sont PRÉSENTS, tous en ARCHIVE** —
   `verif_F1_spn`, `verif_F4_principiel`, `verif_F5_scaling`,
   `verif_F6_memoire_cisaillement`, `verif_D3_WCH_GWE`. **CORRECTION
   D'UNE ERREUR DE CETTE NOTE, consignée** : une version antérieure de
   ce §6 les déclarait ABSENTS et prescrivait la voie G-1
   « réécriture ». C'était un **report du lotissement v0.1
   (2026-07-21)**, antérieur au ré-import des 76 sceaux déchargés, et
   **non une mesure**. Mesuré en S7 : les cinq sont en
   `instruments/archives-scelees/`. Précédent opposable : **un statut de
   présence se MESURE sur le clone, il ne se reporte jamais d'un
   document de cartographie**, si récent soit-il.

   **Gel de cible AVANT la première ligne d'instrument, corps NON
   ouverts, plafond de grade annoncé au gel.** Prévoir un lot LOURD :
   c'est le gabarit le plus large du Silo R (six axes F1–F6 + deux
   têtes WCH).
4. Silos P/V/X : inchangés (P-3 report d = 3 recommandé #1 des decks ;
   tracker R-53 : 0/4).

**Ordre du Silo R après R-7 : la contrainte matérielle qui imposait
R-11 d'abord est LEVÉE** — les têtes [B] ayant été fournies (§4bis), R-9
et R-11 sont tous deux ouvrables et **l'ordre revient à l'opérateur**.
Éléments de fait à peser : R-9 arrive avec un plafond **E-2 déjà
plafonné bas** (verdict révélé par deux canaux indépendants) et ses
têtes ne survivent pas à la réinitialisation du conteneur ; R-11 est
**intégralement autoportant depuis le git** (têtes et cinq sceaux
présents) mais **large** — six axes plus deux têtes WCH.

## 7. Intrants à fournir en session neuve

- **Token GitHub NEUF** (fine-grained, dépôt `LC_Raccord` seul,
  Contents R/W, courte durée) — **à fournir seulement une fois
  l'exécuteur confirmé vivant et les sha annoncés**, pas au premier
  message. **Le token de S7 est à RÉVOQUER** : il a servi au push de
  `b24cd65` et reste lisible en conversation. L'opérateur a déclaré en
  S7 que ceux de S3–S6 étaient déjà révoqués.
- **Les têtes [B]** : FOURNIES en fin de S7 (§4bis), en quarantaine hors
  dépôt. À re-fournir en session neuve — la quarantaine ne survit pas à
  la réinitialisation du conteneur, et elles ne sont PAS déposées au git.
- ~~Décision sur `REIMPORT.txt`~~ : **PRISE en S7 — lecture APRÈS le gel
  de R-9.** Reportée au §6, close.
- **Décision G-1** : place des quatre pièces [B] dans l'arborescence du
  dépôt, si elles doivent y entrer.
- **Une seule instance à la fois** sur le dépôt.
- **AUCUN intrant requis pour R-11** : têtes ET cinq sceaux présents au
  dépôt (mesuré en S7). C'est le lot le plus autoportant du Silo R.
- L'**ordre R-9 / R-11** : décision opérateur (§6).

## 8. Périmètre — INCHANGÉ

`{ A4 ; A2★ ; N }` INCHANGÉ · **W2 = DÉLIMITATION** de la route
A4-par-ℐ⁺, **A4 NON réfuté**, statut de postulat **RENFORCÉ** ; le
no-hair de Wald reste un **IMPORT** ; le périmètre de R-7 est **type I
(électrique) + type II/Nil (magnétique)** — type V non traité,
VI/VII/VIII **non exécutés** ; les réserves `[10]` semi-vacante et
`[06]/[07]` du sceau d'origine ne sont **ni levées ni reproduites** ·
verrou un-point de R-10 conditionnel à A3 et spécifique à `d = 3` ·
`⟨g₃g₃⟩ ∝ k³` reste la donnée de Cauchy irréductible, pendue à la seule
amplitude `A_T ~ 1/N` · A3/A4 NON fusionnés · A2★ décision ouverte,
C7 non levée · D1 non clos · N non fixé (≡Λ, R-53 : 0/4) · O₂ non
construit (β ≡ G3 seul facteur ouvert) · nœud (i) INDÉTERMINÉ (pas A) ·
**CCC non démontrée NI réfutée**.

*§6.4 — sentinelle terminale. Reprendre un lot de zéro, muter, rejouer,
consigner un écart de signe et constater l'absence d'un jeu de têtes :
aucun de ces gestes ne scelle, ne réduit, ne compte, ne démontre quoi que
ce soit.*
