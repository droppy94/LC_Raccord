---
id: LC-WORK-C7-POC-SILENCE
titre: "Lancement du POC « silence asymptotique » — attaquer le VERROU C7 (rétro-action inhomogène) sur le front (a)/GWE, dans une conversation NEUVE. Successeur opérationnel de LC-WORK-REPRISE-INHOMOGENE : le housekeeping §4 que cette dernière laissait « à faire » est désormais FAIT et en KB (chaînon LC-D3-WCH-GWE v0.3 + sceau verif_D3_WCH_GWE.py v0.3 + 6 fichiers propagés). Cette note ne refait NI l'audit (log en KB) NI le housekeeping (clos) : elle porte UNIQUEMENT (i) le delta de scellement produit en session — le mode exact (A) ∀ kη est désormais ASSERTÉ par le sceau, donc C1 est moot-scellé et C7 est le verrou unique et propre ; (ii) la réduction de C7 affûtée par ce scellement ; (iii) une SPEC EXÉCUTABLE du POC §3.3 (silence asymptotique) construite sur les outils déjà en main, avec observables, critères pass/fail, et la réduction qu'un succès ouvre. Référence la substance par id ; ne duplique aucun fichier KB."
codename: LC-AUDIT
type: note de lancement (autoportante) — ouvre une conversation NEUVE de recherche pour EXÉCUTER le POC du §3.3 de LC-WORK-REPRISE-INHOMOGENE (silence asymptotique, verrou C7). Subordonnée au verdict d'audit (LC-AUDIT-LOG-WCH-GWE v1.0) et à la discipline LC-AUDIT-VERDICT §6.4.
version: 1.0
langue: fr
date: 2026-06-08
portee: "Porte le delta NON ENCORE consigné comme PLAN exécutable : (i) le housekeeping §4 est clos (état KB à jour, à NE PAS refaire) ; (ii) le sceau atteste maintenant lui-même le mode exact (A) ∀ kη (bloc [6bis]) ⟹ C7 est le verrou unique, propre, sur le chemin critique ; (iii) la spec du POC silence asymptotique : QUOI calculer sur le flot near-bang homogène (verif_D3_interaeon_kappa.py / diag_bounces.py), avec quels observables, quels seuils de décision, et ce que confirme/réfute chaque issue. Ne duplique pas l'algèbre (LC-D3-WCH-GWE), ni les 10 verdicts (log), ni le cadrage C7 général (LC-WORK-REPRISE-INHOMOGENE §1-2). Discipline §6.4 maintenue : un `établi` de sceau = l'algèbre, jamais la physique ; C7 ne sera levée que si silence ET sélection WCH pointwise ET négligeabilité des spikes sont PROUVÉS, pas postulés."
prerequis_kb: [LC-WORK-REPRISE-INHOMOGENE, LC-AUDIT-LOG-WCH-GWE, LC-D3-WCH-GWE, LC-D3-INTERAEON-P6, LC-D3-INTERAEON-CONVERGENCE, LC-WORK-P6-SPEC-NEARBANG, LC-A-SURVIE-CONFORME, LC-A-D1-BIANCHI, LC-WORK-BIBLIO-FRONT-A, LC-AUDIT-VERDICT]
fichiers_compagnons_kb: [verif_D3_interaeon_kappa.py, diag_bounces.py, verif_D3_P6_specB_oracle.py, verif_D3_WCH_GWE.py]
source_externe: ["Uggla, van Elst, Wainwright, Ellis — 'The past attractor in inhomogeneous cosmology' (Phys. Rev. D 68, 103502, 2003) : formulation orthonormée Hubble-normalisée, DÉFINITION du silence asymptotique (les coefficients de repère spatiaux E_i^a → 0 à l'approche de la singularité ⟹ découplage spatial, dynamique du 'bord silencieux'). [arXiv à confirmer en KB : LC-04-REFERENCES / LC-WORK-BIBLIO-FRONT-A.] SPIKES : Lim (thèse + 'recurring spikes'), Garfinkle (numérique inhomogène), Berger-Moncrief, Uggla-Wainwright — structures inhomogènes de mesure nulle mais dynamiquement réelles (le contre-exemple au non-sequitur 'mesure nulle ⟹ négligeable'). PDFs en KB : 0901_0806 (Heinzle-Uggla, attracteur IX + avertissement inhomogène), 0901_0776 (Mixmaster fact vs belief), 0212256 (Damour-Henneaux-Nicolai, billard = BKL moderne), 1005_4908 (Reiterer-Trubowitz, BKL rigoureux). À CHARGER : la littérature silence/spikes ci-dessus (pas encore en PDF KB)."
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# Lancement du POC « silence asymptotique » — attaquer C7

> **But.** Dans une conversation **neuve**, **exécuter** le POC du §3.3 de
> `LC-WORK-REPRISE-INHOMOGENE` (silence asymptotique), seul moyen tractable d'attaquer le verrou
> **C7** (rétro-action inhomogène) du front (a)/GWE. Autoportant : recharger les `prerequis_kb`,
> lire le **§1-2** (l'état post-scellement, le delta de session), puis exécuter le **§4** (la spec
> du POC). Discipline `LC-AUDIT-VERDICT §6.4` : un `établi` de sceau = « l'algèbre est correcte »,
> jamais « la physique est établie ».

---

## 0. Mode d'emploi
1. **Recharger** : `LC-WORK-REPRISE-INHOMOGENE` (le cadrage C7 complet : §1 état, §2 verrou déplacé,
   §3.2 les deux sous-questions pointwise) ; `LC-D3-WCH-GWE` v0.3 (le pont + le mode exact §1/§6bis) ;
   `LC-D3-INTERAEON-P6` (l'oracle (B) §4.5 ; §4bis inhomogène `hors de portée`) ;
   `LC-WORK-P6-SPEC-NEARBANG` (le noyau, conventions §1bis) ; `LC-A-SURVIE-CONFORME` (régularité de
   Friedrich, sélection WCH).
2. **Lire §1-2** (l'état exact post-scellement et le delta de session — non ailleurs). **NE PAS
   refaire le housekeeping** (§4 de la reprise = clos, en KB).
3. **Exécuter §4** : le POC, en trois diagnostics A/B/C sur le flot near-bang **déjà en main**.
   Démarrer par **A** (le moins coûteux : un quadrature sur `a(N), H(N)`).
4. Tenir §6.4 : C7 n'est levée que si **silence ET sélection WCH pointwise ET spikes négligeables**
   sont **prouvés**.

---

## 1. État en une ligne `[résumé]`
Le pont `Ω_σ=(kη)⁴ε²/27` est **`établi (algèbre)`**, et — **nouveau, scellé en session** — le mode
régulier **exact** `Ω_σ/ε²=(x\cos x-\sin x)²/(3x²)` est **(A) à toute échelle** (plafond **0.377**,
atteint `x≈2.74`, ne croise **jamais** 0.5), **asserté par le sceau** (`verif_D3_WCH_GWE.py` v0.3,
bloc `[6bis]`). ⟹ **C1 (spectre M-P) est moot-scellé** ; **C7** (rétro-action inhomogène,
*hors de portée*) est le **verrou unique** de (A) physique, **sur le chemin critique**. Tout le reste
est en KB (log d'audit ; chaînon v0.3 ; 6 fichiers propagés à v1.17/v1.11/v1.17/v1.5/v0.3/v0.4).

---

## 2. Le delta de cette session — ce qui n'est pas (encore) un PLAN ailleurs `[méta]`

1. **Le housekeeping §4 est CLOS.** Les 4 corrections de cadrage (log §4.5) sont **appliquées et en
   KB** : `LC-D3-WCH-GWE` v0.3 (titre, §1 mode exact, §4 anti-« suppression UV active », §5 α/β/γ,
   §6.1/§6.2 verrou→C7, §8 tableau + scan deux-colonnes, appendice) ; sceau v0.3 ; et les 6 propagés
   (`00_index`, `02`, `03_glossaire`, `LC-AUDIT-VERDICT`, `LC-D3-INTERAEON-P6`,
   `LC-D3-INTERAEON-CONVERGENCE`). `LC-D3-WEYL-BUNCHDAVIES` laissé intact à dessein (`E=(d/2H)g₃`
   = la dérivation **dS légitime**, hors champ de la correction C2). ⟹ La conversation neuve **ne
   refait pas** ce travail ; elle démarre directement au POC.

2. **Le sceau s'auto-atteste maintenant.** Avant : le sceau scellait `(kη)⁴/27` *leading* et
   « exhibait une sensibilité » (bascule à 1.9). Après v0.3 : le bloc `[6bis]` **dérive
   symboliquement** le mode exact (différence avec la cible = 0), **vérifie** que sa limite
   super-horizon redonne `x⁴/27`, et **asserte numériquement** `max < 0.5` (≈0.377) — donc
   l'**absence de bascule** est désormais une propriété **scellée**, pas une lecture. Conséquence
   pour C7 : la question « le mode régulier est-il (A) ? » est close *homogène/pointwise-en-mode* ;
   il ne reste que « ce mode régulier est-il bien ce que voit le noyau, **point par point**, dans un
   bang **inhomogène** ? » — c'est-à-dire **C7 et rien d'autre**.

3. **Ce que C7 devient, post-scellement (affûtage de la reprise §3.2).** Les deux sous-questions
   pointwise se reformulent en s'appuyant sur ce que le sceau a **déjà** établi homogène :
   - **C7-a (sélection WCH pointwise).** Le sceau `[1]`+`[2-4]` établit, *homogène*, la **dichotomie**
     mode régulier `j₀` (coeff. FG un-point `g₃=0`, cohérent WCH) vs mode singulier `y₀` (pôle, =
     mécanisme `Y`, exclu par Friedrich `Ψ̃→0` à 𝓘⁺). C7-a = **relever cette dichotomie au pointwise**
     dans un bang inhomogène : la régularité de Friedrich sélectionne-t-elle `j₀` **en chaque point** ?
     Sous **silence asymptotique**, cette sélection est une **condition locale** ⟹ si le silence tient,
     C7-a se réduit à « la dichotomie homogène scellée, appliquée point par point ».
   - **C7-b (rétro-action des spikes).** Les spikes (exceptions inhomogènes de mesure nulle EN
     LOCALISATION, mais dynamiquement réelles) modifient-ils `⟨Ω_σ⟩` ? Mesure des spikes × amplitude
     de leur contribution. Le non-sequitur « mesure nulle ⟹ négligeable » est corrigé en KB ; il faut
     **quantifier**, pas postuler.

---

## 3. Pourquoi le silence asymptotique est la bonne réduction `[formalisable]`
Le silence asymptotique (Uggla-van Elst-Wainwright-Ellis) : près d'une singularité spatiale
générique, les **horizons de particules rétrécissent** ⟹ les points spatiaux **perdent le contact
causal** ⟹ dans les équations en repère orthonormé Hubble-normalisé, les **coefficients de repère
spatiaux `E_i^a`** (qui portent les gradients `∂_a`) **→ 0** ⟹ la dynamique en chaque point se
**découple** et devient une **ODE de Mixmaster pointwise** (le « bord silencieux »). Si ce silence
tient sur le flot near-bang du noyau :
- **côté (B)** : l'oracle homogène de P6 (`verif_D3_P6_specB_oracle.py`, Gauss-Kuzmin) s'applique
  **point par point** ⟹ le verdict (B) du bang générique **s'étend** à l'inhomogène, **sauf aux
  spikes** ;
- **côté (A)** : C7-a (sélection WCH) étant locale, la dichotomie `j₀`/`y₀` scellée donne **(A)
  pointwise**.
⟹ C7 se réduit alors à **(oracle homogène déjà scellé) + (mesure/backreaction des spikes)** —
beaucoup plus borné que « résoudre BKL inhomogène ».

---

## 4. La spec exécutable du POC `[le chantier — à coder]`

**Contrainte d'honnêteté (à graver d'emblée).** Les outils en main
(`verif_D3_interaeon_kappa.py`, `diag_bounces.py`) sont **homogènes** (Bianchi IX, repère orthonormé,
temps e-fold `N=ln a`, état `[w_i, σ_i, H, ρ]`, CI de Tod `σ(0)=0`, source de courbure `³S_i`). Un
solveur homogène **ne peut pas prouver** le silence inhomogène plein (il n'a pas de `E_i^a` spatial à
regarder). Il peut tester les **signatures nécessaires** du silence (A, B) et un **proxy
inhomogène minimal** (C, famille de modèles voisins). C'est exactement le statut `formalisable /
partiellement hors de portée` attendu — un POC, pas une preuve. Coder les trois :

### Diagnostic A — l'horizon de particules rétrécit-il ? `[le moins coûteux]`
Le silence requiert que l'**horizon de particules passé** d'un observateur comobile **→ 0** à
l'approche du bang (cônes de lumière passés qui se ferment).
- **Observable.** Sur le flot du noyau (`a=e^N`, `H(N)` déjà produits), calculer le **rayon comobile
  passé** `χ_PH(N) = ∫ dN'/(H(N')·e^{N'})` intégré **vers le bang**, et tester `χ_PH → 0` (fermeture).
  Équivalent géométrique : la singularité est-elle **velocity-dominated** (a→0 plus vite que la
  lumière ne traverse) le long du flot ?
- **Pass.** `χ_PH` fini et décroissant vers 0 vers le bang ⟹ horizons rétrécissent ⟹ **silence
  possible**. **Fail.** `χ_PH` ne se ferme pas ⟹ silence en défaut d'emblée (couplage spatial
  irréductible) ⟹ C7 reste `hors de portée`.

### Diagnostic B — les termes de gradient sont-ils sous-dominants (sauf rebonds isolés) ? `[le cœur homogène]`
L'ombre homogène du silence : les variables de **courbure spatiale** Hubble-normalisées sont
sous-dominantes **entre** des rebonds **isolés** (mesure nulle en `N`).
- **Observable.** Le long du flot, suivre `³S_i(N)/H²` (ou `Ω_k=−³R/6H²`) ; **diag_bounces.py
  calcule déjà** les pics de `|³S|` et les renversements de vitesse de forme (les rebonds) **et**
  `Ω_σ(N)`. Mesurer (i) la **fraction de `N`** où la courbure est dynamiquement active (doit → 0) ;
  (ii) l'**isolement** des rebonds (durée en `N`, doit → 0 par rebond) ; (iii) le comportement
  **Kasner-libre** entre rebonds.
- **Pass.** Courbure active sur une fraction de `N` → 0, rebonds isolés ⟹ **Mixmaster pointwise**
  compatible. **Fail.** Courbure persistante ⟹ pas de découplage Kasner ⟹ silence en défaut.

### Diagnostic C — deux points voisins se découplent-ils ? `[le proxy inhomogène minimal]`
Le seul test (homogène) de « les points spatiaux se découplent » : une **famille à un paramètre** de
modèles voisins.
- **Observable.** Intégrer deux flots `{ε, ε+δ}` (ou `{u, u+δ}` dans le paramètre de Kasner), au
  même `N`, et mesurer la **séparation en espace d'états** `Δ(N)` vs le **rayon comobile** `χ_PH(N)`
  du diagnostic A. Découplage ⟺ la séparation **ne peut plus être communiquée causalement** :
  `χ_PH` tombe **sous** l'échelle comobile de la perturbation ⟹ les deux points évoluent comme des
  Mixmaster **indépendants**.
- **Pass.** `χ_PH ≪` échelle de la perturbation tandis que `Δ` reste local ⟹ **découplage** ⟹ silence
  confirmé au niveau proxy. **Fail.** Les voisins restent couplés (séparation propagée) ⟹ couplage
  spatial irréductible.

---

## 5. Verdicts possibles et la réduction qu'ils ouvrent `[l'enjeu]`
- **A ∧ B ∧ C tous PASS** ⟹ silence asymptotique **soutenu** (au niveau POC). C7 se réduit à
  **(oracle homogène pointwise, déjà scellé) + (mesure des spikes, C7-b)**. Étape suivante : charger
  la littérature spikes (Lim, Garfinkle, Berger-Moncrief) et **quantifier** la contribution des
  spikes à `⟨Ω_σ⟩` (mesure × amplitude). Si négligeable ET sélection WCH pointwise (C7-a) tient ⟹ C7
  levée : (A) passe de `formalisable` à `établi (sous WCH/A3-A4, cadre CCC)`. **Front (a) clos par la
  physique.**
- **Silence PASS mais spikes non quantifiés** ⟹ C7 partiellement levée ; le verrou résiduel est
  C7-b (à **prouver** petit, pas postuler).
- **Un diagnostic FAIL** ⟹ couplage spatial irréductible ; **C7 reste `hors de portée`**, (A)
  demeure `formalisable` conditionnel. **C'est un résultat honnête à consigner**, pas un échec :
  il borne précisément ce que la WCH peut délivrer.

---

## 6. Outillage et références `[pratique]`
- **Sceaux réutilisables (KB).** `verif_D3_interaeon_kappa.py` + `diag_bounces.py` (flot near-bang
  homogène, `³S_i`, `Ω_σ`, compteurs de rebonds — base des diagnostics A/B/C) ;
  `verif_D3_P6_specB_oracle.py` (oracle Gauss-Kuzmin homogène, à appliquer **pointwise** si silence
  confirmé) ; `verif_D3_WCH_GWE.py` v0.3 (la dichotomie `j₀`/`y₀` scellée pour C7-a).
- **Refs à charger** (cf. `LC-WORK-BIBLIO-FRONT-A`, `LC-04-REFERENCES`) : **silence asymptotique** —
  Uggla-van Elst-Wainwright-Ellis (PRD 68, 103502, 2003 ; *arXiv à confirmer en KB*) ; **spikes** —
  Lim, Garfinkle, Berger-Moncrief, Uggla-Wainwright. PDFs déjà en KB : `0901_0806` (Heinzle-Uggla),
  `0901_0776` (fact vs belief), `0212256` (DHN billard), `1005_4908` (Reiterer-Trubowitz).
- **Leçon C5 (transférée).** Près d'une échelle `O(1)`, **mode/quantité EXACT** obligatoire, jamais le
  développement dominant (le leading fabrique des sensibilités/seuils inexistants). À appliquer aux
  seuils du POC (ne pas conclure « silence » sur un proxy tronqué).

---

## 7. Premier pas concret pour la conversation neuve
> Recharger §0 → lire §1-2 (delta : housekeeping clos, mode exact scellé ⟹ C7 verrou unique) →
> **coder le diagnostic A** (`χ_PH(N)=∫dN'/(H e^{N'})` sur le flot de `diag_bounces.py` /
> `verif_D3_interaeon_kappa.py`) : l'horizon de particules passé se ferme-t-il vers le bang ? Si
> **PASS**, enchaîner **B** (sous-dominance de courbure + isolement des rebonds, déjà partiellement
> outillé par diag_bounces) puis **C** (famille `{ε, ε+δ}`, découplage vs `χ_PH`). Selon l'issue
> (§5), soit réduire C7 à (oracle pointwise + spikes) et attaquer C7-b en chargeant la littérature
> spikes, soit consigner le couplage irréductible comme borne honnête. Tenir §6.4 : tout `établi` de
> POC reste « signature numérique », et C7 ne sera levée que sous **preuve**, pas postulat.

---

## Appendice — rappels
**Le fait de lancement (scellé, à ne pas re-prouver).** `verif_D3_WCH_GWE.py` v0.3 atteste :
`Ω_σ/ε²=(x\cos x-\sin x)²/(3x²)`, `max=0.377<0.5` à `x≈2.74`, limite super-horizon `=x⁴/27` ⟹ mode
régulier **(A) ∀ kη**, **aucune bascule**. Donc C1 (spectre) moot ; **C7 = verrou unique**.

**Tags épistémiques.** `établi` / `formalisable` / `à inventer` / `hors de portée` / `décision
ouverte` (cf. `LC-00-INDEX`). *Discipline : `établi (algèbre)` du sceau = le pont + le mode exact ;
le régime (A) **physique** reste `formalisable`, conditionnel à **C7** (rétro-action inhomogène) et
au cadre CCC. Le présent POC vise à faire passer C7 de `hors de portée` à `formalisable` borné — pas
à le déclarer `établi`.*
