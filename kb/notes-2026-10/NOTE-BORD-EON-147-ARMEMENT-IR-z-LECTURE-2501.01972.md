---
id: NOTE-BORD-EON-147-ARMEMENT-IR-z-LECTURE-2501.01972
numero: 147
serie: I
branche: Q-M3 suite (IR-z, lecture)
reservation: 2026-10-12T15:20 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 147)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 AVANT FETCH (questions, espace des verdicts et prediction figes avant toute lecture de la source)
decision: operateur (Thierry), 2026-10-12 17:02 heure de Paris (« execute les 3 en sequence », piste 3) ; « go » 17:19
depend: [NOTE-BORD-EON-134-ARMEMENT-IR-v, NOTE-BORD-EON-135-IR-v-EXECUTION, NOTE-BORD-EON-137-AUDIT-IR-w-CONCORDANCE, NOTE-BORD-EON-133-IR-u-EXECUTION, NOTE-BORD-EON-146-IR-y-EXECUTION]
issue_attendue: "lecture (statut de la forme resommee de G-V3)"
source_declaree: "A. J. Foraci, R. P. Woodard, « Resumming Fermion Loops for Inflationary Gravity », arXiv:2501.01972, soumis le 27 decembre 2024 (titre, auteurs, date verifies par recherche web le 2026-10-12, EX-7) ; type : prepublication, pas de reference de revue relevee"
rouvre_si:
  - "audit froid de NOTE-148"
  - "autre source primaire de la resommation (Starobinsky stochastique, Fabris-Pelinson-Shapiro) accessible"
---

# NOTE-147 : armement de IR-z. Lecture de la source primaire des resommations (Foraci-Woodard 2501.01972) : la forme W ∝ Ω^(−8bκH²) tient-elle a la source ?

## 0. Origine
NOTE-135 (V-V1) a lu Woodard 2501.05077, revue qui presente la resommation des logarithmes de boucle sur de Sitter par un groupe de renormalisation modifie (ln μ → ln a) et donne, pour le Weyl electrique des ondes gravitationnelles, C^tree × a^p avec p = 8bκH² exactement pour scalaire conforme, fermion de Dirac et photon (eq. 148, 151, 154). Elle cite comme source primaire des resommations de boucles de fermions l'article 2501.01972, non lu (NOTE-135 §7, reprise du 12 octobre §4.6). NOTE-137 (W-b) a retrouve a l'aveugle n = 8 pour les trois especes. Reste a verifier **a la source** la derivation de la forme resommee, ses hypotheses, et son domaine de validite, dont depend la clause « resomme, W ∝ Ω^(−ε) » du libelle de G-V3 (NOTE-138 v2).

## 1. Cadre (fige)
- Lecture (EX-9 : lire jusqu'a la fin de la section suivante de tout passage utilise) ; extraits sauvegardes et empreintes dans `src\SOURCE-2501.01972v1-extraits.txt`. Aucun calcul nouveau au-dela de conversions de normalisation (script `irz_conv.py` si necessaire, empreinte avant execution).
- Conversions du programme : κ = 8πG ; κ_W² = 16πG chez Woodard ; b = (N_S + 6N_F + 12N_V)/(120(4π)²) ; 8bκ pour un fermion de Dirac = G/(5π) (NOTE-133, 137). Convention de signe physique Carroll-Wald (NOTE-138).
- Ce qui compte pour G-V3 : (i) la forme fonctionnelle du facteur resomme sur le Weyl electrique (puissance de a, ou autre) ; (ii) la valeur de l'exposant pour le fermion ; (iii) la methode (equation de groupe de renormalisation, variante stochastique, ou autre) et ses hypotheses (logarithmes dominants, etat, jauge, gauge-independence) ; (iv) le domaine de validite declare (« tant que de Sitter persiste », nombre d'e-folds, rupture) ; (v) ce que la source dit du passage ln a → puissance (demonstration, conjecture, verification a deux boucles ?).

## 2. Questions de lecture (figees)
- **z-1** : la source donne-t-elle explicitement, pour le fermion sans masse, la correction a une boucle du Weyl electrique (ou du mode graviton) sous la forme 1 + c ln a, et quelle est la valeur de c dans ses unites ? Convertie, vaut-elle 8bκ = G/(5π) (soit, avec b_F = 6/(120(4π)²) = 1/(320π²), 8bκ = 8 × 8πG/(320π²) = G/(5π)) ?
- **z-2** : la resommation : quelle equation (groupe de renormalisation avec quelle fonction β ou γ ; substitution ln μ → ln a ; justification) ; le resultat est-il une puissance a^p exacte, et p = c ?
- **z-3** : hypotheses declarees : logarithmes dominants seulement ? etat (Bunch-Davies / vide conforme) ; prescription in-in ; independance de jauge ; terme constant ou fini non resomme ; role de la renormalisation (contre-termes, μ).
- **z-4** : domaine de validite declare : duree de la phase de Sitter, condition sur p ln a, mention d'une echelle de rupture ou d'un nombre maximal d'e-folds ; la source parle-t-elle d'un comportement a « temps infini » (limite a → ∞), pertinent pour 𝓘⁺ ?
- **z-5** : la source traite-t-elle aussi du scalaire conforme ou du photon, ou renvoie-t-elle ailleurs ; dit-elle quelque chose de la **reponse a une masse ponctuelle** (potentiel) qui recouperait le statut du Weyl electrique ?
- **z-6** : la source est-elle une derivation de la puissance (preuve ou verification d'ordre superieur) ou une conjecture de resommation ? Formuler le statut avec les mots de la source.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **Z-V1** | La source donne explicitement 1 + c ln a pour le fermion avec c converti egal a 8bκ = G/(5π), et une resommation en a^p, p = c, par groupe de renormalisation, avec ses hypotheses nommees ; la forme Ω^(−ε) de G-V3 est **ancree a la source primaire** ; statut de la puissance = celui que la source declare (z-6). |
| **Z-V2** | Coefficient a une boucle confirme, mais la resommation en puissance est presentee par la source comme une conjecture ou un procede sans controle d'ordre superieur ; la clause « resomme » de G-V3 reste [extrait] mais doit porter la mention « conjecturale selon la source ». |
| **Z-V3** | Le coefficient a une boucle ou l'exposant resomme differe de 8bκ apres conversion ; NOTE-133/135/137 a reexaminer. |
| **Z-V4** | La source ne traite pas le Weyl electrique des ondes gravitationnelles (seulement le potentiel ou la fonction de mode) ; la clause resommee de G-V3 reste adossee a 2501.05077 seul. |
| **Z-V0** | Source inaccessible, ou questions mal posees (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**Z-V1 qualifie Z-V2.**
- z-1 : oui, correction logarithmique explicite ; c converti = G/(5π) (coherence avec NOTE-135 eq. 151 et NOTE-137 W-b).
- z-2 : groupe de renormalisation avec ln μ → ln a, puissance a^p, p = c.
- z-3 : logarithmes dominants, etat de Bunch-Davies, in-in (Schwinger-Keldysh), discussion de la jauge ; la partie non logarithmique n'est pas resommee.
- z-4 : validite « tant que la phase de Sitter persiste » ; pas d'enonce sur la limite a → ∞ en tant que telle ; le seuil p ln a ~ 1 n'est probablement pas commente comme rupture.
- z-5 : scalaire et photon renvoyes a d'autres travaux ; la reponse a une masse ponctuelle est traitee (resume de l'article).
- z-6 : resommation presentee comme un procede justifie par analogie avec le groupe de renormalisation et par la structure des logarithmes, sans verification a deux boucles ; d'ou la qualification Z-V2.
- Consequence attendue : le libelle de G-V3 garde « sous la prescription de resommation de Woodard (logarithmes dominants) », en precisant « procede de groupe de renormalisation, non verifie a l'ordre superieur selon la source ».

## 5. Instruments prevus
Fetch du texte (alphaXiv ou arXiv), extraits empreintes ; `irz_conv.py` (sympy) seulement si une conversion de normalisation non triviale est requise.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v2) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Aucune lecture de la source avant le scellement de cette note.
