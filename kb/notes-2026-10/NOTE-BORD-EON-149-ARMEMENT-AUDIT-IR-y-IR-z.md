---
id: NOTE-BORD-EON-149-ARMEMENT-AUDIT-IR-y-IR-z
numero: 149
serie: I
branche: Q-M3 suite (audit IR-y et IR-z)
reservation: 2026-10-12T15:36 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 149)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL R-7 (consignes aveugles, criteres, espace des verdicts et prediction figes AVANT le lancement des auditeurs)
decision: operateur (Thierry), 2026-10-12 17:34 heure de Paris (« realise les 3 suites possibles », suite 1)
objet: [NOTE-BORD-EON-146-IR-y-EXECUTION, NOTE-BORD-EON-148-IR-z-LECTURE-2501.01972]
consignes:
  - "PROMPT-AVEUGLE-YA1-ETAT-HADAMARD.md, sha256 3989bda6869eb536d2651c92006279d3f770d5e9f48db27a063bccaebab5b179"
  - "PROMPT-AVEUGLE-YA2-SCRIPT.md, sha256 888220de878b6015acca436ee28971baed120a2927267caaaffa5f06d54257e3"
  - "PROMPT-AVEUGLE-ZA1-LECTURE-2501.01972.md, sha256 c152a062a9ea79c77f0aa6c4d7a47b9d8e3fe9ac05ab0d80cc65db12ae8c3a2a"
---

# NOTE-149 : armement de l'audit froid aveugle conjoint de NOTE-146 (IR-y) et NOTE-148 (IR-z)

## 1. Dispositif (fige)
Trois auditeurs isoles, en parallele, sans acces aux notes, au registre ni aux dossiers de travail :
- **YA-1** (cecite stricte) : derivation aveugle de la question de theorie quantique des champs seule (aucune mention de G-V3, de la CCC, du pole ni de l'equation (2.17)) : classe homogene de Bogoliubov, comportement en η → 0⁻, cone reflechi et condition de Hadamard, argument general de prolongement avec enonce et hypotheses des theoremes, regularite jointe.
- **YA-2** : audit du script iry_state_v2.py (seul fichier fourni), reproduction independante, erreurs, contre-exemples (α β* oscillants ou a support compact).
- **ZA-1** (lecture aveugle) : releve dans 2501.01972 des eq. 35, 42, 46, de la methode de resommation et de ses mots, des conditions de validite et des absences ; conversion en n × b κ_P² H².

## 2. Criteres (figes)
- **C-1 (y-1)** : YA-1 et YA-2 retrouvent T^w ~ |η|^(N−4), 1/η pour N = 3 seulement, fonction entiere pour une decroissance rapide.
- **C-2 (y-2)** : YA-1 et YA-2 retrouvent le cone reflechi (η + η′)² = |x − x′|² rencontrant le domaine, et la caracterisation Hadamard ⟺ decroissance rapide dans la classe homogene.
- **C-3 (y-3)** : YA-1 fournit un argument general Hadamard ⟹ w lisse a travers η = 0 avec un theoreme nomme ; precise le statut de la regularite jointe.
- **C-4 (contre-exemples)** : YA-2 ne trouve aucune famille donnant T^w ~ 1/η avec une fonction a deux points reguliere dans le domaine.
- **C-5 (z-1, z-2)** : ZA-1 retrouve les coefficients (eq. 35, 46, photon = 2 × Dirac) et n = 8 pour les trois especes ; forme resommee a^p, exposant egal au coefficient du log.
- **C-6 (z-3, z-4, z-6)** : ZA-1 releve la methode (Callan-Symanzik, γ, β = 0, ln μ → ln a), le mot « suggests », l'absence de verification d'ordre superieur, la validite « tant que de Sitter persiste », et les absences (jauge, a → ∞, e-folds, rupture).

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | C-1 a C-6 satisfaits sans correction : NOTE-146 et NOTE-148 confirmees. |
| **AU-V2** | Criteres satisfaits avec corrections de detail ou precisions (annotation de signe du script, theoreme a nommer autrement, regularite jointe a qualifier, extrait manquant) : greffes v2 proposees, verdicts Y-V1/Y-V2 et Z-V1/Z-V2 inchanges. |
| **AU-V3** | Un critere porteur echoue (contre-exemple Hadamard a 1/η ; exposant different de 8bκ ; argument general invalide) : verdict de la note concernee a reexaminer. |
| **AU-V0** | Audit inexploitable (a nommer), relance. |

Composites permis (un verdict par note).

## 4. Prediction declaree (anti-fit)
**AU-V2 pour NOTE-146, AU-V1 ou AU-V2 pour NOTE-148.**
- YA-1 retrouvera C-1 et C-2 ; pour C-3, il nommera le theoreme de propagation de la condition de Hadamard (Fulling-Narcowich-Wald) ou la propagation des singularites de Hormander, et signalera que la regularite jointe pres de la diagonale sur η = 0 exige la propagation de Hadamard (microlocale) plutot que l'argument a une variable : precision a porter en v2 de NOTE-146 §2.2.
- YA-2 relevera la coquille de signe de l'annotation « attendu −1/2 » et le fait que la v1 du script est defectueuse ; aucun contre-exemple ; peut relever que le terme |β|² ne joue aucun role.
- ZA-1 retrouvera n = 8 pour les trois especes et les mots « suggests » et « a variant of the renormalization group » ; il pourra relever une absence non notee par NOTE-148 (par exemple la reference [8] pour le photon, ou le statut « to the order we are working » de β = 0).

## 5. Procedure
Dossiers /home/claude/audit_ya1, audit_ya2, audit_za1 ; rapports sauvegardes avec empreintes ; NOTE-150 confronte les criteres ; aucune correction de NOTE-146 ni NOTE-148 avant NOTE-150.

## 6. Non-surclassement
[conv]. RG-4 inchangee ; G-V3 (libelle NOTE-138 v2) et M-V3 candidats non graves ; noyau inchange.
