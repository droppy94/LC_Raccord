---
id: LC-WORK-CADRAGE-A2-NUMERIQUE
titre: "Cadrage gelé (paper-first, hors-algèbre / voie NUMÉRIQUE) du front A2★ — substantiation de la conjecture A2★ (non-cascade : Q(τ)=Σ_spikes C_F sous-exponentielle en τ) par une MODÉLISATION MÉSOSCOPIQUE de la production et de la charge des spikes, pilotée par la statistique d'ères de Gauss-Kuzmin DÉJÀ SCELLÉE (LC-D3-INTERAEON-P6). Fige, AVANT toute simulation et tout fetch (R-7, anti-fit), les cibles A2★-N1 (prolifération des surfaces n_s(τ)), A2★-N2 (pont u_ère→C_F : charge par spike bornée sous la mesure d'ère), A2★-N3 (synthèse Q=n_s·⟨C_F⟩ ⟹ R_grad,gen→0 via la déduction scellée verif_D3_C7b_A2_reduction.py), et A2★-R (réfutation : injection de cascade DOIT casser). Issues pré-enregistrées Nk-a/b/c, critère de verdict TRIPARTITE (dérivation candidate / déplacement / réfutation ; défaut = délimitation), forks de scoping S-A2N-1..4. DÉCISION DE PORTÉE FIGÉE : la voie NR GÉNÉRIQUE 3D reste `hors de portée` (confirmé C7b-VERDICT-A2, OA INCHANGÉE) ; on attaque la voie mésoscopique, qui contourne OB (ultralocalité du billard) PAR CONSTRUCTION (le modèle réadmet la structure spatiale de spike) mais dont le statut générique est lui-même un gap nommé (mésoscale → 3D NR). SANS SURCLASSEMENT (§6.4) : un cadrage ne tranche rien ; même au positif robuste, A2★ soutenue dans un régime mésoscopique générique-élargi ≠ A2★ tranchée en générique 3D (OA persiste) ⟹ réduction CANDIDATE à instruire (audit froid + sceau), PAS A2★ réduite ; {A4 ; A2★ ; N} INCHANGÉ ; C7 non levée ; D1 non clos ; CCC non démontrée."
codename: LC-RACCORD
type: "note de cadrage analytique (paper-first, voie numérique) — PAS un chaînon (aucun sceau ici). Premier front de la phase MODÉLISATION HORS-ALGÈBRE (point d'entrée LC-WORK-REPRISE-PRE-HORS-ALGEBRE §3). Subordonnée à LC-AUDIT-VERDICT §6.4. Exécution sur GO séparé."
statut: "work-active — CADRAGE GELÉ (anti-fit). Cibles A2★-N1..N3 + A2★-R figées AVANT toute exécution/fetch. Aucun sceau, aucune simulation, aucun fetch dans ce fichier. Gel SHA in-fichier recouvrable (R-36) = sha256 du fichier déposé."
version: "0.1"
langue: fr
date: "2026-06-17"
maj: "2026-06-17 — v0.1 : création du cadrage A2★ numérique sur GO Thierry (option A du triage hors-algèbre, note active §3). Premier front de la phase MODÉLISATION HORS-ALGÈBRE. Fige, AVANT toute simulation et tout fetch (R-7, anti-fit), la question A2★ par voie mésoscopique : Q(τ)=Σ_spikes C_F est-elle sous-exponentielle dans un modèle de production+charge de spikes piloté par la statistique d'ères de Gauss-Kuzmin déjà scellée ? Cibles A2★-N1 (prolifération n_s), A2★-N2 (pont u_ère→C_F), A2★-N3 (synthèse Q ⟹ R_grad,gen→0), A2★-R (firewall cascade). Issues Nk-a/b/c pré-enregistrées ; critère TRIPARTITE ; forks S-A2N-1..4 ; séparation positionnement (licite, sans gel) vs prédiction (gelée). Décision de portée figée : NR générique 3D `hors de portée` non ouverte (OA inchangée) ; voie mésoscopique contourne OB par construction, statut générique = gap nommé. AUCUN sceau, AUCUNE algèbre neuve, AUCUN fetch. Gel SHA in-fichier recouvrable (R-36). SANS SURCLASSEMENT (§6.4) : un cadrage ne tranche rien ; {A4 ; A2★ ; N} INCHANGÉ ; A2★ non tranchée ; C7 non levée ; D1 non clos ; N non fixé ; CCC non démontrée."
prerequis_kb: [LC-WORK-A2-CONJECTURE, LC-D-F3-A2STAR, LC-D3-C7B-VERDICT-A2, LC-D3-A1-SUPERHORIZON, LC-D3-INTERAEON-P6, LC-D3-SPIKES-C7B, LC-D3-GRADIENT-C7B, LC-D3-SILENCE-POC, LC-WORK-REPRISE-PRE-HORS-ALGEBRE, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_C7b_A2_reduction.py, verif_D3_C7b_A1_superhorizon.py, verif_D3_C7b_spikes.py, verif_D3_C7b_gradient.py]
source_externe: ["AUCUNE consommée ici (fetch HOLD par défaut, S-A2N-3). Positionnement adossé au KB : Garfinkle gr-qc/0312117 (mécanisme de spike, 0312117v4.pdf KB) ; Lim 0710.0628 (profil exact, C_F^Lim=2π·A² ; |w|>1 transitoire / 0<|w|<1 permanent, §5.1, KB) ; statistique d'ères Gauss-Kuzmin (couverte par l'oracle scellé LC-D3-INTERAEON-P6, R-21). Fetch ciblé conditionnel post-gel (KLSKS statistique d'ères ; Heinzle-Uggla spike statistics G₂) SEULEMENT si une cible l'exige, anti-fit/R-7 engagés."]
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte, piste / à étayer]
---

# Cadrage A2★ numérique — voie mésoscopique (phase hors-algèbre, front 1)

> **But.** Ouvrir le premier front de la phase **modélisation hors-algèbre** (point d'entrée
> `LC-WORK-REPRISE-PRE-HORS-ALGEBRE §3`, option A). A2★ est `décision ouverte`, **mieux située +
> faiblement soutenue (G₂)** après F3, avec un gap nommé : *extension G₂ → générique 3D + pont
> `u_ère → C_F`*. Ce cadrage **fige, avant toute exécution et tout fetch**, une attaque **numérique
> mésoscopique** de la **seule maille non scellée** — la **non-cascade** — sans prétendre au NR
> générique 3D (`hors de portée`). **Paper-first : aucun code, aucune simulation, aucun fetch ici.**
> Discipline `§6.4` : un cadrage ne tranche rien ; on **pose un modèle**, on ne cherche pas un acquis.

---

## 0. Objet du cadrage en une ligne `[cadrage]`

Fige la question : **`Q(τ) = Σ_spikes C_F` est-elle sous-exponentielle** dans un **modèle
mésoscopique de production + charge de spikes piloté par la statistique d'ères de Gauss-Kuzmin
déjà scellée** ? — décomposée en **prolifération** des surfaces `n_s(τ)` (A2★-N1) et **charge par
spike** `⟨C_F⟩` sous la mesure d'ère (A2★-N2, le pont `u_ère→C_F`), avec synthèse `Q=n_s·⟨C_F⟩`
(A2★-N3) et firewall de cascade (A2★-R). Cibles **gelées AVANT** simulation/fetch (anti-fit, R-7).

---

## 1. État hérité — ce qui est DÉJÀ scellé `[ne pas refaire]`

De `LC-WORK-A2-CONJECTURE` (réduction) et de ses sceaux, le résidu générique de C7-b s'écrit

```
    R_grad,gen(τ) = Q(τ) · I_spike^gen(τ) / ⟨Ω_σ⟩_bulk ,   Q(τ) = Σ_spikes C_F
```

avec, **déjà acquis** :

- **A1 (scellé, `verif_D3_C7b_A1_superhorizon.py`)** : `I_spike^gen = C_F·w/cosh(wτ) ≈
  2·C_F·w·e^{−|w|τ}` — scaling `1/ℓ → e^{−|w|τ}` **indépendant du profil** (le profil n'entre que
  par `C_F`).
- **Déduction §4 (scellée, `verif_D3_C7b_A2_reduction.py` partie A)** : pour **toute** `Q(τ)`
  **sous-exponentielle**, `R_grad,gen → 0`. Borne de bascule : `Q ~ e^{|w|τ}` (seuil exact) ⟹ `R`
  ne tend PAS vers 0 (= réfutation `R2`).
- **`N_b(τ)` sous-exponentiel (scellé, `verif_D3_C7b_A2_reduction.py` partie B)** : le **nombre de
  bounces** croît quasi-linéairement le long de l'oracle de Gauss-Kuzmin (`LC-D3-INTERAEON-P6`).
- **Profil exact (KB, Lim 0710.0628)** : `C_F^Lim = 2π·A²` ; spike **transitoire** si `|w|>1`,
  **permanent** si `0<|w|<1` (§5.1, vérifié en propre, R-20 de F3).

**La seule maille `décision ouverte` qui RESTE** = la **non-cascade** : `Q(τ)` sous-exponentielle.
Elle se factorise en `Q = n_s(τ)·⟨C_F⟩`, soit (N1) **prolifération des surfaces** `n_s` + (N2)
**charge moyenne par spike** `⟨C_F⟩` sous la mesure d'ère. `N_b` scellé borne le nombre de
*bounces*, **pas** le nombre de *surfaces de spike actives* ni la charge par spike : c'est là le gap.

**Obstructions F3 (rappel, INCHANGÉES) :** OA (aucune borne en générique 3D — Garfinkle hors régime
convergent, `hors de portée`) ; OB (billard ultralocal exclut les spikes par construction) ; OC (pont
`u_ère→C_F` non fait). Ce cadrage attaque **OC** et la part de **OA** atteignable hors NR 3D, en
**contournant OB par construction** (le modèle mésoscopique réadmet explicitement la structure
spatiale de spike que le billard ignore).

---

## 2. Cibles GELÉES (avant toute exécution / tout fetch) `[anti-fit, R-7]`

> Ces énoncés sont figés par le **sha256 du présent fichier** (gel in-fichier recouvrable, R-36).
> Tout réajustement ultérieur = **amendement R-7 daté**, jamais silencieux.

- **A2★-N1 — prolifération des surfaces de spike.** Dans un modèle mésoscopique où chaque ère
  produit des surfaces de spike selon une règle paramétrée (taux de production + facteur de
  réplication récursive `ρ`), le nombre de surfaces actives `n_s(τ)` croît-il **sous-exponentiellement**
  (`ρ` n'engendre pas d'auto-réplication multiplicative ⟹ `n_s` polynomial/quasi-linéaire) ou
  **exponentiellement** (cascade : chaque spike engendre récursivement des sous-spikes ⟹
  `n_s ~ e^{cτ}`) ? **Cible gelée : le SCALING de `n_s(τ)` en fonction de `ρ`.**

- **A2★-N2 — pont `u_ère → C_F` (charge par spike bornée).** La charge `C_F` exprimée comme fonction
  du paramètre d'ère `u` (via l'amplitude/raideur du profil de spike, raccord exact `C_F^Lim=2π·A²`),
  son espérance `⟨C_F⟩` sous la **mesure de Gauss-Kuzmin** sur `u` est-elle **finie/bornée** (ou
  sous-exp. en τ), ou **divergente** (queue de la mesure d'ère pesant sur les grands `|w|`/grandes
  amplitudes) ? **Cible gelée : la finitude/le scaling de `⟨C_F⟩_{Gauss-Kuzmin}`.**

- **A2★-N3 — synthèse.** `Q(τ) = n_s(τ)·⟨C_F⟩` sous-exponentielle ⟹ **via la déduction DÉJÀ
  scellée**, `R_grad,gen(τ) → 0` **dans le modèle**. **Cible gelée : la composition N1∧N2 ⟹ Q
  sous-exp.** (le maillon déduction est scellé ; la nouveauté est `Q` au niveau modèle).

- **A2★-R — réfutation / firewall.** L'injection d'une **règle de cascade** (réplication
  multiplicative `ρ>1` ⟹ `Q ~ e^{|w|τ}` ou pire) **DOIT** casser `R_grad,gen→0`. Contrôles de
  validité : (i) **reproduire le régime G₂** (spikes transitoires, non-cascade) comme cas limite ;
  (ii) **limite billard/ultralocale ⟹ zéro spike** (cohérence OB). **Cible gelée : le sceau MORD sur
  la mutation cascade ET reproduit les deux limites.**

---

## 3. Issues pré-enregistrées (par cible) `[pré-déclaration anti-fit]`

- **N1-a** : `n_s` sous-exp. **robuste** pour toute règle de production `O(1)`/ère **sans
  auto-réplication multiplicative** ⟹ **soutien dérivé** (la non-réplication est une propriété de la
  dynamique de bounce, pas une hypothèse).
- **N1-b** : `n_s` sous-exp. **seulement** sous hypothèse `ρ≤1` **posée** ⟹ **déplacement** (A2★
  déplacée vers « pas d'auto-réplication », non dérivée).
- **N1-c** : cascade (`n_s~e^{cτ}`) apparaît sous règle de production **générique** ⟹ **réfutation**
  (R2).
- **N2-a** : `⟨C_F⟩_{Gauss-Kuzmin}` **fini/borné** ⟹ **soutien dérivé** (pont fait : la mesure d'ère
  intègre `C_F(u)`).
- **N2-b** : borné **seulement** sous troncature/cutoff sur `u` ou `|w|` **posé** ⟹ **déplacement**.
- **N2-c** : `⟨C_F⟩` **divergent** (la queue de Gauss-Kuzmin sur les grands `u` rend `C_F(u)` non
  intégrable) ⟹ **obstruction/réfutation**.
- **N3** : PASS **ssi** N1 et N2 PASS (composition) ; sinon hérite du maillon le plus faible.
- **R** : firewall **mordant** sur la cascade + deux limites reproduites = condition de validité du
  sceau (sinon le sceau n'atteste rien).

---

## 4. Critère de verdict TRIPARTITE `[§6.4, pré-enregistré]`

1. **DÉRIVATION (réduction CANDIDATE du compte)** — `Q` sous-exp. **robuste** (N1-a ∧ N2-a),
   **sans** hypothèse de non-réplication/cutoff posée, + firewall mordant + deux limites reproduites.
   **MÊME LÀ** : ce n'est **PAS** le théorème générique 3D (OA persiste ; le régime testé est
   mésoscopique, non NR 3D) ⟹ **réduction CANDIDATE à instruire** (audit froid séparé + sceau réel),
   **PAS A2★ tranchée**, **PAS** `{A4 ; A2★ ; N}` modifié sans warrant formel.
2. **DÉPLACEMENT** — sous-exp. seulement sous règle/cutoff **posé** (N1-b et/ou N2-b) ⟹ A2★ **mieux
   située**, postulat **déplacé** (non réduit). Délimitation à lean positif consolidée.
3. **RÉFUTATION** — cascade générique (N1-c) et/ou `⟨C_F⟩` divergent (N2-c) ⟹ A2★ **fausse dans le
   modèle** ⟹ **négatif propre** (changement de compte négatif : warrant formel + audit froid + sceau
   requis avant toute propagation).
4. **DÉLIMITATION (défaut)** — résultat **régime-dépendant** / le « générique-élargi » mésoscopique
   est lui-même un gap ⟹ A2★ reste `décision ouverte`, mieux située, **gap re-nommé** (mésoscale →
   3D NR). C'est l'issue attendue la plus probable à honnêteté constante.

---

## 5. Forks de scoping `[S-A2N-1..4, adoptés par ce cadrage]`

- **S-A2N-1 — classe de modèle.** Modèle **mésoscopique stochastique** piloté par les ères
  (Gauss-Kuzmin **scellée**, `LC-D3-INTERAEON-P6`). **PAS** de NR générique 3D (OA `hors de portée`
  confirmée par C7b-VERDICT-A2 ; on ne l'ouvre pas). Contourne **OB** par construction (le modèle
  réadmet la structure spatiale de spike). Bibliothèques : NumPy/SciPy (stack §0).
- **S-A2N-2 — définition de « générique-élargi ».** Brisure de G₂ encodée par le **facteur de
  réplication `ρ`** et le **taux de production** ; **balayage** sur `ρ` (et sur la troncature de `u`)
  ; le régime validé est **nommé et borné** (mésoscale era-driven), le gap vers 3D NR **acknowledged**.
- **S-A2N-3 — fetch HOLD par défaut.** KB-local + machinerie D3-C7b existante d'abord. Fetch ciblé
  **conditionnel post-gel** (statistique d'ères KLSKS — déjà couverte par l'oracle scellé, R-21 ;
  spike statistics G₂ Heinzle-Uggla) **seulement** si une cible l'exige ; anti-fit/R-7 engagés.
- **S-A2N-4 — sceau.** Sceau **armé conditionnel/réversible** + **firewall** (mutation cascade
  `ρ>1` + contrôles G₂/billard), sur le modèle de F4/O2 (EXIT 0 + firewall mordant + compte consigné).
  Proposé, **non exécuté** ici.

---

## 6. Positionnement vs prédiction `[R-7, frontière explicite]`

- **Positionnement (licite, sans gel)** : mécanisme de production de spike (Garfinkle) ; arithmétique
  de la spike map / statistique d'ères de Gauss-Kuzmin (**déjà scellée**) ; transitoire/permanent
  (Lim, `|w|>1` vs `0<|w|<1`) ; profil exact `C_F^Lim=2π·A²`. Ces faits **contextualisent** le modèle.
- **Prédiction (gelée AVANT exécution/fetch, ce cadrage)** : le **scaling de `n_s(τ)`** (N1), le
  **`⟨C_F⟩` sous la mesure d'ère** (N2), et **`Q(τ)`** (N3). Ces cibles sont **figées par le sha256 du
  présent fichier**. Aucun chiffre cible n'est inscrit ici (anti-fit : on fige la *question* et les
  *issues*, pas une valeur attendue).

---

## 7. Ce que ce cadrage NE fait PAS `[§6.4]`

- Il **ne prouve pas** A2★ (donc **ne lève pas** C7).
- Il **n'ouvre pas** le NR générique 3D (OA reste `hors de portée`).
- Il **ne réduit pas** le compte : même un positif robuste = **réduction candidate à instruire**
  (audit froid + sceau), non une réduction actée. `{A4 ; A2★ ; N}` **INCHANGÉ** jusqu'à preuve formelle.
- Un **modèle posé n'est pas un acquis** : sa portée est exactement le régime mésoscopique nommé.

---

## 8. Sceau futur proposé (non exécuté) `[paper-first]`

`verif_A2_numerique.py` (nom proposé) — sur GO séparé : (A) modèle mésoscopique era-driven `n_s(τ)`,
balayage `ρ` ; (B) pont `C_F(u)` + intégration contre Gauss-Kuzmin ⟹ `⟨C_F⟩` ; (C) synthèse `Q` +
raccord à la déduction scellée ⟹ `R_grad,gen→0` ; (D) **firewall** : mutation cascade `ρ>1` DOIT
casser ; contrôles limites G₂ (transitoire) et billard (zéro spike). EXIT 0 + firewall mordant +
compte d'assertions consigné = condition de sceau réel. **Aucune exécution dans ce fichier.**

---

> **SANS SURCLASSEMENT (§6.4).** Un cadrage ne tranche rien. Même au positif robuste, A2★ soutenue
> dans un régime mésoscopique générique-élargi **≠** A2★ tranchée en générique 3D (OA persiste) ⟹
> **réduction candidate**, pas A2★ réduite. `{A4 ; A2★ ; N}` **INCHANGÉ** ; C7 non levée ; D1 non
> clos ; N non fixé ; CCC non démontrée.
