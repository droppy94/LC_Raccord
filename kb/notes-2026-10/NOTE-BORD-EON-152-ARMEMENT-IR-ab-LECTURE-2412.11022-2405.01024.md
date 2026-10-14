---
id: NOTE-BORD-EON-152-ARMEMENT-IR-ab-LECTURE-2412.11022-2405.01024
numero: 152
serie: I
branche: Q-M3 suite (IR-ab, lecture)
reservation: 2026-10-13T10:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 152)
date: 2026-10-13
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 AVANT FETCH (questions, espace des verdicts et prediction figes avant toute lecture des sources)
decision: operateur (Thierry), 2026-10-13 12:53 heure de Paris (« traite les elements marques en priorite 1 », piste 1 de la reprise v2 §5.1)
depend: [NOTE-BORD-EON-147-ARMEMENT-IR-z-LECTURE-2501.01972, NOTE-BORD-EON-148-IR-z-LECTURE-2501.01972 (v2), NOTE-BORD-EON-150-AUDIT-IR-y-IR-z-CONCORDANCE, NOTE-BORD-EON-151-ACTE-GREFFES-ET-REVISION-G-V3, NOTE-BORD-EON-138-ACTE-G-V3-SIGNE-CONVENTION (v3)]
issue_attendue: "lecture (statut de la clause resommee de G-V3 : justification du procede de groupe de renormalisation)"
sources_declarees:
  - "[8] A. J. Foraci, R. P. Woodard, arXiv:2412.11022 : d'apres NOTE-148 v2, source des resultats de Sitter (35)-(37) de 2501.01972 pour la boucle de photon (Maxwell), lue par proportionnalite 1/2 pour Dirac. Titre, date et type a verifier au fetch (EX-7) ; souvenir de travail : « Gravitational response to a massless, charged fermion/photon loop » ou voisin, decembre 2024, prepublication."
  - "[27] S. P. Miao, N. C. Tsamis, R. P. Woodard, arXiv:2405.01024 : d'apres NOTE-148 v2, source de la renormalisation de champ du graviton δZ = D[2(D−1)c₁ − c₂]κ²H² (eq. 39 de 2501.01972). Titre, date et type a verifier au fetch (EX-7) ; souvenir de travail : mai 2024, prepublication, sujet « summing gravitational effects from loops of inflationary scalars / graviton field strength renormalization »."
rouvre_si:
  - "audit froid de NOTE-153"
  - "source anterieure du procede (Miao-Tsamis-Woodard 2021-2023 sur les logarithmes de boucle des scalaires MMC) accessible et lue"
---

# NOTE-152 : armement de IR-ab. Lecture des deux sources amont de 2501.01972 : d'ou vient le procede de resommation, et que vaut-il ?

## 0. Origine
NOTE-148 v2 (Z-V1 qualifie Z-V2, audite AU-V1) a etabli que, dans Foraci-Woodard 2501.01972 : (i) les resultats de Sitter (35)-(37) ne sont pas recalcules mais lus a partir de [6] et [8] par proportionnalite ; (ii) la renormalisation de champ du graviton (eq. 39), qui fixe γ et donc l'exposant resomme a^(κ_W²H²/(80π²)), est empruntee a [27] ; (iii) la resommation est introduite par « This suggests that the secular logarithms can be resummed using a variant of the renormalization group », sans verification a l'ordre superieur. NOTE-138 v3 §1.3 porte en consequence la clause resommee de G-V3 avec la mention « procede de groupe de renormalisation, non verifie a l'ordre superieur ». La reprise v2 §5.1 demande de remonter la justification du procede aux deux sources amont. C'est l'objet de cette lecture.

## 1. Cadre (fige)
- Lecture (EX-9 : lire jusqu'a la fin de la section suivante de tout passage utilise) ; extraits sauvegardes et empreintes dans `src\SOURCE-2412.11022-extraits.txt` et `src\SOURCE-2405.01024-extraits.txt`. Aucun calcul nouveau au-dela de conversions de normalisation (script `irab_conv.py` si necessaire, empreinte avant execution).
- Conversions du programme (NOTE-133, 137, 148 v2) : κ = 8πG ; κ_W² = 16πG chez Woodard ; b = (N_S + 6N_F + 12N_V)/(120(4π)²) ; 8bκ = G/(30π) par scalaire conforme, G/(5π) par Dirac, 2G/(5π) par photon ; chez FW, l'exposant est κ_W²H²/(80π²) pour Dirac et son double pour le photon.
- Ce qui compte pour G-V3 : la clause resommee seule (W ∝ Ω^(−ε)). Le coefficient du logarithme (γ = 8) est deja etabli dans le programme ([calcule] NOTE-133, aveugle NOTE-137, source NOTE-148 v2) ; il n'est pas l'objet principal ici, seulement un controle (ab-1).
- Ce qui ne compte pas : les details de la boucle (regularisation, contre-termes) au-dela de ce qui fonde ou limite le procede.

## 2. Questions de lecture (figees)
- **ab-1 (controle du coefficient)** : [8] donne-t-il, pour la boucle de photon, la correction a une boucle du Weyl electrique (ou du mode graviton, ou du potentiel) sous la forme 1 + c ln a avec c = κ_W²H²/(40π²) (double de Dirac), soit 2G/(5π) H² = 8bκH² pour N_V = 1 ? Et [8] est-il la source de la lecture « Dirac = 1/2 Maxwell » ?
- **ab-2 (origine du procede)** : dans laquelle des deux sources le procede « equation de Callan-Symanzik avec ln μ → ln a » est-il **formule pour la premiere fois** ou justifie ? Que dit [27] de δZ (eq. 39 de FW) : d'ou vient la formule D[2(D−1)c₁ − c₂]κ²H², et comment la renormalisation de champ du graviton est-elle definie (contre-termes R² et C² sur de Sitter, regularisation dimensionnelle) ?
- **ab-3 (justification)** : la justification du remplacement ln μ → ln a est-elle structurelle (les contre-termes de regularisation dimensionnelle apportent des facteurs μ^(D−4) a^(D−4) qui apparient ln μ et ln a ; les logarithmes seculaires sont « reliques » de la renormalisation) ou seulement heuristique (analogie) ? Les sources distinguent-elles les logarithmes seculaires d'origine ultraviolette (resommables par le groupe de renormalisation) et ceux d'origine infrarouge (resommables par le formalisme stochastique de Starobinsky) ? Le cas des champs conformes (photon, fermion sans masse, scalaire conforme) est-il classe comme purement ultraviolet ?
- **ab-4 (controle independant)** : l'une des sources compare-t-elle la resommation par groupe de renormalisation a un calcul independant : deux boucles explicites, formalisme stochastique, ou cas exactement soluble ? Y a-t-il un enonce de type « verifie a l'ordre κ⁴ » ou au contraire « conjecture » ?
- **ab-5 (jauge et etat)** : [27] discute-t-il la dependance de jauge de la renormalisation de champ du graviton (choix de jauge, invariance de δZ, observables) ? L'etat est-il celui de Bunch-Davies / vide conforme ?
- **ab-6 (domaine de validite)** : les sources enoncent-elles une limite de validite de la resommation (duree de la phase de Sitter, seuil p ln a ~ 1, rupture de la theorie des perturbations, comportement pour a → ∞) ?

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AB-V1** | Les deux sources confirment le coefficient (ab-1) et fondent le procede sur un argument **structurel** (appariement ln μ / ln a par la regularisation dimensionnelle, logarithmes seculaires d'origine ultraviolette pour les champs conformes), sans verification d'ordre superieur ni calcul independant ; la clause de NOTE-138 v3 est **maintenue telle quelle**, avec, a porter dans une revision, la mention de l'argument structurel et de ses deux sources. |
| **AB-V2** | Comme AB-V1, mais l'une des sources apporte un **controle independant** (deux boucles, cas soluble, formalisme stochastique concordant) : la clause « non verifie a l'ordre superieur » doit etre **adoucie** en « verifie dans un cas / a un ordre » avec la reference. |
| **AB-V3** | Le coefficient de [8] pour le photon, converti, differe de 2G/(5π) : NOTE-133/137/148 a reexaminer. |
| **AB-V4** | L'une des sources **affaiblit** le procede : dependance de jauge non maitrisee de δZ, ou enonce explicite que la resommation n'est qu'une conjecture, ou restriction de validite excluant le regime utile a G-V3 : la clause doit etre **durcie** (mention explicite de la limitation). |
| **AB-V0** | Source inaccessible, ou questions mal posees (a nommer). |

Composites permis.

## 4. Prediction declaree (anti-fit)
**AB-V1, avec une composante AB-V4 faible (jauge).**
- ab-1 : oui, [8] donne pour le photon le double du coefficient de Dirac, converti 2G/(5π) ; [8] est bien la source de la lecture par proportionnalite.
- ab-2 : le procede est formule dans [27] (ou dans une source anterieure de Miao-Tsamis-Woodard qu'il cite) pour les boucles de scalaires, et [8] l'applique au photon ; δZ vient des deux contre-termes R² (c₁) et C² (c₂) de la gravite sur de Sitter en regularisation dimensionnelle.
- ab-3 : justification structurelle : les contre-termes portent μ^(D−4), les boucles a^(D−4) ; les logarithmes seculaires des champs conformes sont d'origine ultraviolette (ils accompagnent les divergences) et la variante du groupe de renormalisation est motivee par cet appariement ; les logarithmes infrarouges des scalaires MMC sont renvoyes au formalisme stochastique.
- ab-4 : aucune verification a deux boucles pour la gravite ; peut-etre un controle dans un cas scalaire (MMC) ou la resommation RG est comparee au stochastique ; pas de cas exactement soluble pour le graviton.
- ab-5 : [27] discute la jauge au moins en la nommant (jauge de de Donder simple sur de Sitter) ; la dependance de jauge des logarithmes seculaires est reconnue comme probleme ouvert ou traitee par un argument d'observable ; etat de Bunch-Davies.
- ab-6 : validite « tant que de Sitter persiste » ; rien sur a → ∞.
- Consequence attendue : clause de G-V3 maintenue ; une revision du libelle pourrait citer [27] pour l'origine du procede et noter que l'independance de jauge n'est pas etablie.

## 5. Instruments prevus
Fetch du texte (alphaXiv ou arXiv), extraits empreintes ; `irab_conv.py` (sympy) seulement si une conversion de normalisation non triviale est requise.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v3) et M-V3 candidats non graves ; noyau {A4 ; A2★ ; N} inchange. Aucune lecture des sources avant le scellement de cette note.
