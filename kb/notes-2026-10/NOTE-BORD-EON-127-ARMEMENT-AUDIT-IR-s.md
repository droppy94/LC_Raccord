---
id: NOTE-BORD-EON-127-ARMEMENT-AUDIT-IR-s
numero: 127
serie: I
branche: Q-M3 suite (audit IR-s)
reservation: 2026-10-12T11:48 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 127)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
statut: GEL (objets, prompts, espace des verdicts et prediction figes AVANT lancement des sous-agents)
decision: operateur (Thierry), 2026-10-12 13:48 heure de Paris : « IR-s : audit froid aveugle de NOTE-123 et 125 [...] le pole doit etre retrouve a l'aveugle avant toute suite »
depend: [NOTE-BORD-EON-123-IR-q-EXECUTION, NOTE-BORD-EON-125-IR-r-EXECUTION, NOTE-BORD-EON-126-ACTE-DECISION-CONVENTION-LISSE]
issue_attendue: "delimitation"
rouvre_si:
  - "pole de NOTE-125 non retrouve, artefact de jauge ou de repere, ou compense par la partie a"
  - "lecture des sources de NOTE-123 jugee infidele sur un point porteur"
---

# NOTE-127 : armement de l'audit froid aveugle de NOTE-123 et NOTE-125 (IR-s)

## 1. Objets audites
| Note | sha256 (16) | Scripts | sha256 (16) |
|---|---|---|---|
| NOTE-123 (IR-q) | 1884e07a52ba3d5b | irq_diff.py | 750ccc53430be3ea |
| NOTE-125 (IR-r) | 6150cb19aae7bc55 | irr_c.py ; irr_c_ctrl.py | ef0c3f4fac14d233 ; 8035a342d686d4f2 |

Sources de NOTE-123 : SOURCE-1309.7248v2-texte.txt (c929b1006031ce44), SOURCE-1311.0700-texte-alphaxiv.txt (1a8a8b55e95201f7), SOURCE-2503.24263v1-texte.txt (cfaa6dae167aa9c8).

## 2. Resultats porteurs
- **NOTE-125**
  - R-1 : sur ĝ = s⁻²(η + εh) avec un mode tensoriel de de Sitter, le tenseur physique du terme b∫√g φ C² (φ = −ln s) est sans trace, conserve et **sans ln s** ; le coefficient du log est proportionnel au tenseur de Bach, nul sur couche.
  - R-2 : le second membre de (2.17) porte un **pole Ω⁻¹ proportionnel au Weyl electrique rescale a 𝓘⁺**, coefficient 8bκ dans la normalisation de irr_c.py.
  - R-3 : ce pole n'est ni un artefact de jauge, ni un artefact de repere.
- **NOTE-123**
  - Q-1 : un ln Ω dans le second membre de l'equation de Bianchi rescalee correspond a un terme Ω⁴ ln Ω dans la metrique-pont : g est C³ non C⁴, W continue non C¹.
  - Q-2 : dans l'eon suivant (prescription reciproque), le fond est une radiation et la perturbation une contrainte anisotrope sans trace en ln Ť a l'ordre Ť⁰.
  - Q-3 : lecture des sources. La lissite est une hypothese chez Tod et chez Meissner et Penrose ; Friedrich envisage des pertes de lissite ; aucune source ne fixe une classe finie ni n'envisage de logarithmes.

**Porteurs au sens du verdict** : R-1, R-2, R-3 ; Q-1 ; Q-3.

## 3. Protocole
Quatre sous-agents frais, en parallele, sans acces aux notes ni entre eux.
- **S-a1**, re-derivation aveugle du bloc R : `PROMPT-AVEUGLE-Sa1-IR-r.md`, sha256 `b97abe56335543f20e2490ba615dc988c6464d39ecbe4deb3c9b80c08522cdad`. Le pole et son coefficient ne sont pas donnes.
- **S-a2**, re-derivation aveugle du calcul q-4 : `PROMPT-AVEUGLE-Sa2-IR-q.md`, sha256 `f2f2b5d4fb47260d03ac68941b9930f943c498c93f4b9942a38d608ef99bb78e`. Ni la classe C³ ni le ln Ť ne sont donnes.
- **S-b**, audit des scripts, reproduction et contre-exemples, avec une tentative de calcul de la partie a (Euler) sur le meme mode : `PROMPT-AVEUGLE-Sb-AUDIT-123-125.md`, sha256 `a705f4f5075ba1cdce6c55ad85385d3b9f9d5cffb8a833209cad4e62d5027ba0`.
- **S-c**, audit de lecture des trois sources : `PROMPT-AVEUGLE-Sc-LECTURE-123.md`, sha256 `16c31cd5402ff2d5806d9d812df2efabf3e0437ab54c5a34a27601299b9f4f76`.

Transparence : S-b et S-c connaissent les affirmations (c'est leur role) ; S-a1 et S-a2 ne les connaissent pas. La demande a S-b de calculer la partie a elargit l'audit au-dela de NOTE-125. Le resultat sera rapporte a part, sans entrer dans le verdict d'audit, et pourra servir de premiere instruction de la piste IR-t.

## 4. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Concordance totale sur les porteurs ; au plus des corrections de forme. |
| **AU-V2** | Concordance sur les porteurs (pole retrouve a l'aveugle, a normalisation de b pres ; C³ et ln Ť retrouves ; lecture fidele) ; corrections mineures ; qualifications nommees. |
| **AU-V3** | Discordance sur un porteur : pole absent, artefact de jauge ou de repere, structure differente ; log present sur couche ; regularite differente ; lecture infidele sur un point porteur. La note concernee est suspendue, partiellement si le defaut est localise. |
| **AU-V0** | Audit non concluant. |

Composites permis (par note). Le resultat eventuel de S-b sur la partie a n'entre pas dans ce verdict (§3).

## 5. Prediction declaree (anti-fit)
**AU-V2.**
- Le pole est retrouve a l'aveugle par S-a1, avec une normalisation de b eventuellement differente (facteur numerique ou signe). Le non-artefact est confirme.
- C³ et ln Ť sont retrouves par S-a2.
- La lecture est jugee fidele, avec au moins une nuance (par exemple sur la portee de « conformally smooth » chez Meissner et Penrose, ou sur les puissances demi-entieres de Tod).
- Reserve attendue : la dimension anormale de W (NOTE-125 §2.5) est jugee [derive] et non demontree.
- Sur la partie a, je ne fais aucune prediction de signe : S-b pourrait ne pas la mener a terme.

## 6. Non-surclassement
Un audit concordant n'eleve pas les notes au-dela de [conv]. M-V3 et G-V3 restent des candidats non graves (convention lisse, NOTE-126). Noyau {A4 ; A2★ ; N} inchange.
