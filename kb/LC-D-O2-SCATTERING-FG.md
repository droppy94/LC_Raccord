---
id: LC-D-O2-SCATTERING-FG
titre: "Résultat de l'exploitation latérale scattering / Fefferman-Graham petites-données (P-1) — verdict par cible SFG-1/SFG-2/SFG-3 contre le cadrage gelé 8979aa5e. AUCUN sceau, AUCUNE algèbre."
codename: LC-RACCORD
tags: [module-D, O2, scattering-FG, exploitation-laterale, jonction-D-N, facteur-beta, beta-G3, TG-1, contre-termes, A4, weyl-rescale, petites-donnees, Leimbacher, Hintz-Vasy, fetch-R7, sans-sceau]
statut: "délimitation-consolidation — 3/3 cibles = POSITIF-consolidation (consolidation LOCALE stricte, aucune cible ne dépasse ⟹ audit froid NON déclenché par le cadrage §Phases). SFG-1 : dictionnaire de données {g₍₀₎, g₍ₙ₎} instancié RIGOUREUSEMENT en dS lorentzien (correspondance 1-1, g₍₃₎ TT libre) = la PRÉMISSE cinématique de la lecture D↔N d'O2-JONCTION est consolidée ; (C-O2) NON prouvée, P1/P2 intactes. SFG-2 : cas-témoin FG lorentzien-dS SANS AUCUN contre-terme ⟹ carry-over TG-1 LISIBLE = ABSENT au niveau géométrique, concordant DELTA-C T2(a) ; mur R2″ (renorm marginale graviton propageant) INTACT, β reste T-b. SFG-3 : borne-témoin Weyl acquise (s²g lisse à 𝓘⁺, Weyl rescalé fini porté par {g₍₀₎, g₍₃₎}) + g₍₃₎ LIBRE même petites-données ⟹ A4 non dérivé = statut de postulat CONSOLIDÉ ; hors P12 par construction."
type: "chaînon (résultat — DÉLIMITATION-CONSOLIDATION) : exécute les Phases 0 (KB-only), 1 (fetch R-7, 2 sources) et 2 (confrontation) du cadrage gelé LC-WORK-CADRAGE-O2-SCATTERING-FG v1.0 (gel R-36 = 8979aa5e82ab75b5fe52963201e6e29774b96ba1c90413d170329ce73dad3458, horodaté 2026-07-02 au manifeste v2.22, INTOUCHÉ)."
fichier_compagnon: "(aucun sceau) — zéro algèbre ; confrontation textuelle des sources contre les cibles gelées ; précédents sans-sceau : O2-JONCTION, O2-C1-ADS, FACTORISATION, G3-TRANSPORT."
version: 0.1
langue: fr
date: 2026-07-02
prerequis_kb: [LC-WORK-CADRAGE-O2-SCATTERING-FG, LC-D-O2-JONCTION, LC-D-O2-FACTORISATION, LC-D-G3-TRANSPORT, LC-D-O2-DELTA-C, LC-D-IRREDUCTIBILITE-MOYENS, LC-D-F4-A4-PRINCIPIEL, LC-D3-SPECTRE-K3, LC-D-NONLIN-2PT]
maj: "2026-07-02 — v0.1 : verdict initial (Phases 0-2 du cadrage 8979aa5e). Fetch R-7 daté 2026-07-02, limité aux 2 sources armées : arXiv:2605.03481 (Leimbacher, texte intégral HTML consommé) + arXiv:2409.15460 (Hintz-Vasy, abstract + méthode via le porteur primaire). Identités R-41 CONFIRMÉES ; sha256 des PDF INFAISABLE via web (réseau bash sans arxiv.org) ⟹ vérification consignée au grade identité-vérifiée (précédent PRISMA, cf. §5). 3/3 POSITIF-consolidation. AUCUN sceau, AUCUNE algèbre, AUCUN amendement R-7 (zéro source hors-liste consommée)."
---

# Exploitation latérale scattering/FG — verdict SFG-1..3 `[Phases 0-2, cadrage 8979aa5e]`

## 0. Rôle et garde-fou `[§6.4 + R-7]`

Ce chaînon exécute le cadrage gelé `LC-WORK-CADRAGE-O2-SCATTERING-FG` v1.0
(gel R-36 `8979aa5e…3458`, 2026-07-02, INTOUCHÉ) : lire l'infrastructure
scattering / Fefferman-Graham petites-données récemment consignée « intérêt
latéral non adjugé » (`LC-D-IRREDUCTIBILITE-MOYENS` §6quinquies) STRICTEMENT
contre trois cibles pré-gelées, chacune à espace de verdicts figé
{POSITIF-consolidation ; NÉGATIF ; INDÉTERMINÉ-fetch-gated}.

**Interdiction par construction (rappel du cadrage)** : les deux sources sont
PETITES-DONNÉES ⟹ elles ne mordent pas sur P12 (no-hair générique
grandes-données) ⟹ AUCUNE réduction du périmètre `{A4 ; A2★ ; N}` n'est
atteignable par ce chaînon, quel que soit le verdict. Toute lecture qui
prétendrait le contraire est une erreur.

## 1. Sources consommées & discipline `[R-7 / R-41]`

- **S1 (primaire)** : Leimbacher, *Stability of de Sitter Space and Expansion
  at the Conformal Boundary*, arXiv:2605.03481v1 (math.AP, 2026-05-05 ;
  mémoire de master ETH sous la direction de P. Hintz). Texte intégral HTML
  consommé (fetch daté 2026-07-02). Identité R-41 : titre + auteur +
  affiliation + date + abstract CONFIRMÉS concordants sur deux miroirs
  (arxiv.org/abs et arxiv.org/html).
- **S2 (lignée/méthode)** : Hintz-Vasy, *Stability of the expanding region of
  Kerr-de Sitter spacetimes and smoothness at the conformal boundary*,
  arXiv:2409.15460 (gr-qc/math.AP/math.DG, 2024-09, 63 pp.). Abstract consommé
  (fetch daté 2026-07-02) ; la méthode [HV24] est reproduite et généralisée en
  détail dans S1 (jauge harmonique généralisée modifiée à la Ringström,
  constraint damping, racines indicielles, Nash-Moser) — S1 = porteur effectif.
  Identité R-41 : CONFIRMÉE (listings arXiv sept. 2024 + page de recherche +
  CV de Hintz, concordants).
- Zéro source hors-liste consommée ⟹ AUCUN amendement R-7 requis.

## 2. SFG-1 — jonction D↔N ↔ dictionnaire de scattering `[POSITIF-consolidation]`

**Ce que la source établit (tel qu'imprimé).** S1, Thm 1.2 + §1.2 : pour n≥3
impair (cas du programme, n=3), toute solution proche de dS admet près de 𝓘⁺
la forme bloc-diagonale `g = (−ds² + H)/s²` avec expansion en puissances de s
dont les coefficients `g₍ᵢ₎`, i<n, sont déterminés par `g₍₀₎` seul, les ordres
impairs i<n nuls, et le premier coefficient libre est `g₍ₙ₎`, **transverse et
sans trace** (`tr g₍ₙ₎ = 0`, `δ g₍ₙ₎ = 0`) ; tous les ordres supérieurs sont
déterminés par `{g₍₀₎, g₍ₙ₎}`. La solution possède **deux degrés de liberté
fonctionnels asymptotiques** — `g₍₀₎` et `g₍ₙ₎` — et « data of this type is
called scattering data ». Via [FG85/FG08] + [RSR18] + [Hin24], S1 établit une
**correspondance 1-1** entre solutions du vide proche-dS et données de
scattering prescrites au bord conforme, en dimension générale, extension aux
asymptotiquement-dS à section spatiale compacte (Remark 1.1). Cadre :
LORENTZIEN, Λ>0 genuine, 𝓘⁺ spacelike, aucun régulateur, aucune continuation.

**Confrontation à la cible gelée.** La lecture D↔N d'`O2-JONCTION` §2
présuppose un espace de données de bord à deux tenseurs indépendants
{`g₀` (donnée Dirichlet/source), `g₃` (donnée Neumann/VEV, TT)} au 𝓘⁺
spacelike de dS. Le théorème INSTANCIE RIGOUREUSEMENT cet espace : les deux
tenseurs existent comme données libres indépendantes en dS lorentzien natif,
`g₍₃₎` est TT — en concordance exacte avec le datum TT du programme
(`SPECTRE-K3` branche k³ ; `NONLIN-2PT` C1). La prémisse CINÉMATIQUE de la
transition Dirichlet→Neumann (que les deux quantifications aient des espaces
de données bien définis au 𝓘⁺ dS, sans régulateur) est désormais adossée à un
théorème PDE indépendant de toute holographie.

**Ce que la source n'établit PAS.** La correspondance est donnée↔solution
(cinématique). Elle ne fournit NI transformée de Legendre entre fonctionnelles
génératrices, NI appariement symplectique, NI quantification, NI S-map ⟹ la
conjecture (C-O2) [réciprocité de Penrose ≟ S-map de de Haro] reste NON
prouvée ; les gates P1 ∧ P2 restent à inventer, telles quelles.

**Verdict SFG-1 = POSITIF-consolidation** (de la prémisse de la lecture D↔N ;
jamais preuve de C-O2).

**Sous-produit latéral consigné, NON adjugé (route axe γ).** Lemma 3.2 de S1 :
racines indicielles de l'opérateur d'Einstein jaugé = {0, 2, 3, n, n+1} ; pour
n=3, les racines extrêmes du secteur métrique {0, 3} = les exposants
{Δ₋, Δ₊} = {0, 3} de l'étalon AdS₄ (`LC-D-GAMMA-NSTAR-ADS4` NA-1), désormais
exhibés en dS lorentzien NATIF (aucune continuation ℓ→iℓ — la contrainte mγ-3
est satisfaite par construction). MAIS : S1 ne dit rien de la normalisabilité
(aucun énoncé L² sur la branche r^{Δ₊}), rien de la quantification ⟹ ce
sous-produit ne remplit AUCUNE case de la matrice γ ; toute consommation vers
γ exigerait un re-gel R-7 dédié.

## 3. SFG-2 — cas-témoin FG lorentzien-dS & lisibilité TG-1 `[POSITIF-consolidation]`

**Ce que la source établit.** L'expansion FG de S1 (Thm 1.2/4.1) est obtenue
par pure analyse asymptotique géométrique : lissité de `s²g` jusqu'à 𝓘⁺
(n impair), coefficients polynomiaux en s, coefficient libre `g₍ₙ₎` FINI TEL
QUEL. **Aucun contre-terme, aucune soustraction, aucune renormalisation
n'apparaît nulle part dans la construction** — ni dans la preuve de stabilité,
ni dans l'extraction des asymptotiques, ni dans la correspondance 1-1.

**Confrontation à la cible gelée (obstruction TG-1 de `G3-TRANSPORT` §2).**
TG-1 demandait si le carry-over des contre-termes AdS conventionnels vers dS
est présent / absent / contourné. Le cas-témoin rigoureux répond au niveau où
il est compétent : **au niveau géométrique/cinématique (structure de la
métrique et de ses données), le carry-over est ABSENT** — l'expansion dS
lorentzienne est finie et complète sans aucun appareil de contre-termes. Ceci
CONCORDE avec `DELTA-C` T2(a) (les contre-termes AdS conventionnels
disparaissent sous la continuation Schwinger-Keldysh ; renorm relocalisée sur
champ tardif/source) : le lean négatif structurel de TG-1 acquiert un témoin
rigoureux INDÉPENDANT (PDE hyperbolique, zéro holographie) ⟹ la lisibilité
demandée par SFG-2 est ACQUISE, valeur = ABSENT (au niveau géométrique).

**Ce que la source n'établit PAS.** Le témoin lit la MÉTRIQUE et ses données,
pas l'action on-shell renormalisée ni les corrélateurs ⟨TT⟩/⟨TTT⟩. Le mur
résiduel de β (cellule R1″∧R2″∧R4″ : carte shadow RENORMALISÉE AU PAS MARGINAL
pour le graviton d'Einstein PROPAGEANT, deux-bords D↔N, en dS₄/CFT₃ —
`G3-TRANSPORT` §7ter/§7quater) est un énoncé de QFT holographique que le
théorème ne touche pas ⟹ **β reste T-b**, O₂ non construit, la
re-qualification du pencher-obstruction est une CONSOLIDATION du versant
« le carry-over n'est pas le verrou » (déjà lean), pas une levée du mur.

**Verdict SFG-2 = POSITIF-consolidation** (lisibilité acquise, carry-over
ABSENT au niveau géométrique ; mur R2″ INTACT).

## 4. SFG-3 — borne-témoin Weyl petites-données ↔ maillon A4 `[POSITIF-consolidation]`

**Ce que la source établit.** n=3 : `s²g` lisse jusqu'à 𝓘⁺ avec restes
décroissant plus vite que toute puissance prescrite (Thm 1.2(1)) ; espace-temps
futur-géodésiquement complet (Thm 3.2). La lissité de la métrique rescalée
⟹ le tenseur de Weyl rescalé s'étend continûment à 𝓘⁺, entièrement porté par
les données de scattering — secteur électrique par `g₍₃₎` (dictionnaire scellé
`E = (d/2H)g₃`, `LC-D3-WEYL-BUNCHDAVIES`), secteur magnétique par le Cotton de
`g₍₀₎` (`LC-D-CB-WEYL-MAGNETIQUE`). C'est l'énoncé quantitatif de régularité
demandé par la cible : **borne-témoin ACQUISE** (le Weyl rescalé ne peut pas
exploser en petites-données ; sa valeur-limite est la donnée elle-même).

**Point structurel (consolidation du statut d'A4).** Dans le théorème,
`g₍₃₎` est une donnée LIBRE : toute perturbation TT petite est atteinte par la
correspondance 1-1. RIEN, même dans le régime petites-données le plus docile,
ne force dynamiquement `g₍₃₎ → 0`. Le témoin rigoureux confirme donc que
A4 (bas-Weyl au 𝓘⁺) est une SÉLECTION DE DONNÉE, pas une conséquence du flot —
en cohérence exacte avec `F4-A4-PRINCIPIEL` (délimitation : A4 non dérivé) et
avec le graphe d'`IRREDUCTIBILITE-MOYENS` §3 (A4 ← externe). Le maillon A4
TIENT, et son statut de postulat est CONSOLIDÉ par une route indépendante.

**Ce que la source n'établit PAS (interdiction par construction).**
Petites-données ⟹ AUCUN statut sur P12 (no-hair générique grandes-données
sans symétrie) ; A4 NON réduit ; la borne-témoin est un CONTROL, pas un
théorème de nettoyage générique.

**Verdict SFG-3 = POSITIF-consolidation** (borne-témoin acquise + statut de
postulat d'A4 consolidé ; hors P12 par construction).

## 5. Limitations documentées `[R-41]`

1. **sha256 des PDF non consignable** : le réseau bash du poste n'atteint pas
   arxiv.org ; la consommation est passée par les outils web (recherche +
   fetch HTML). Vérification d'identité au grade « identité-vérifiée »
   (titre/auteurs/date/abstract concordants multi-miroirs), précédent PRISMA
   v2.0/v2.1. Toute exploitation future de S1/S2 en zone PORTEUSE avec sceau
   devra re-consigner l'identité (idéalement dépôt PDF opérateur + sha).
2. **S2 consommé au niveau abstract + méthode-via-S1** : suffisant pour le
   rôle de lignée assigné par le cadrage (aucune cible ne repose sur un
   contenu propre à S2 absent de S1) ; consigné.
3. **S1 = préprint v1 (mémoire de master, non publié)** : poids de source
   consigné ; les résultats s'appuient sur [FG85/FG08, RSR18, Hin24, Rin08]
   publiés, et la correspondance 1-1 est présentée comme assemblage de
   résultats établis + le théorème d'expansion propre.

## 6. Verdict global & trichotomie `[figée au cadrage]`

**3/3 cibles = POSITIF-consolidation.** Portée = consolidation LOCALE stricte
(chaque cible consolide un maillon existant sans en créer, sans lever aucun
mur, sans remplir aucune case) ⟹ le déclencheur d'audit froid du cadrage
(« si portée > consolidation locale ») n'est PAS atteint ; AUCUN sceau (zéro
algèbre) ⟹ §0-full non déclenché.

Gains nets (tous sans comptage) : (i) la prémisse cinématique de la lecture
D↔N d'O₂ est adossée à un théorème PDE lorentzien-dS indépendant ; (ii) le
lean négatif de TG-1 a un témoin rigoureux, le mur de β est mieux localisé
(purement QFT/renorm marginale, plus du tout géométrique) ; (iii) le maillon
A4 est testé-consolidé par une route neuve ; (iv) sous-produit γ consigné
non-adjugé (exposants {0,3} natifs dS).

## 6.4. Non-surclassement `[terminal]`

Trois consolidations ne réduisent RIEN : consolider une prémisse ≠ prouver
(C-O2) ≠ construire O₂ (β reste T-b, α reste C1-b) ≠ fermer D1 ; un témoin
petites-données ≠ P12 ≠ A4 réduit ; des exposants natifs ≠ case γ remplie.
`{A4 ; A2★ ; N}` INCHANGÉ ; D1 non clos ; N non fixé (≡Λ) ; A4 non réduit ;
A2★ non tranché ; CCC non démontrée NI réfutée.

## 7. Renvois

`LC-WORK-CADRAGE-O2-SCATTERING-FG` (cadrage gelé 8979aa5e) ;
`LC-D-O2-JONCTION` §2 (lecture D↔N) ; `LC-D-G3-TRANSPORT` §2/§7ter (TG-1, mur
R2″) ; `LC-D-O2-DELTA-C` (T2a SK) ; `LC-D-F4-A4-PRINCIPIEL` ;
`LC-D-IRREDUCTIBILITE-MOYENS` §3/§6quinquies ; `LC-D3-SPECTRE-K3` ;
`LC-D-NONLIN-2PT` ; `LC-D-GAMMA-NSTAR-ADS4` (NA-1, sous-produit γ) ;
arXiv:2605.03481 ; arXiv:2409.15460.
