---
id: NOTE-BORD-EON-93-ARMEMENT-AUDIT-FROID-Q-M3
numero: 93
serie: I
branche: Q-M3 suite (audit)
reservation: 2026-10-09T17:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 93)
date: 2026-10-09
programme: LC-RACCORD
grade: "[conv]"
statut: GEL (prompts et espace des verdicts figes AVANT lancement des sous-agents)
depend: [NOTE-BORD-EON-92-Q-M3-LOG-EXECUTION, NOTE-BORD-EON-91-ARMEMENT-Q-M3-LOG]
issue_attendue: "delimitation"
rouvre_si:
  - "discordance non resolue entre S-a et S-b"
---

# NOTE-93 : armement de l'audit froid aveugle de NOTE-92 (script q_m3_log_v5)

## 0. Objet
NOTE-92 a ete obtenue apres quatre versions defectueuses du script (v1 a v4), dont une (v4) imprimait une conclusion sans fondement. Avant tout usage de NOTE-92, ses resultats porteurs sont soumis a un audit froid aveugle (Mode A, sous-agents frais n'ayant pas vu le travail).

## 1. Resultats porteurs soumis a l'audit (NOTE-92 §0, §2)
- P-1 : equations de conservation et de trace du secteur scalaire ; exposant indiciel 2, resonance de la source A τ².
- P-2 : aux ordres controles (m ≤ 1), la regularite du second membre de (2.17) impose c₀ = c₁ = 0, e₀ = e₁ = e₃ = f₂ = f₃ = 0, **e₂ = A/3** ; c₂, c₃, α, β libres.
- P-3 : le ln Ω est present dans la source pour tout etat regulier si A ≠ 0 ; l'etat regulier a une structure logarithmique dominante isotrope.
- P-4 : etat sans ln : coefficient `κ(A + c₀k²)/2 · ln Ω` (composante (1,0,1)) ; c₀ = −A/k² le supprime au prix d'un pole `−c₀κ/2 · Ω⁻²`.
- P-5 : argument de troncature (le coefficient de τ^m dans R depend de c jusqu'a τ^(m+2)).

## 2. Protocole
- **S-a, re-derivation independante** : `PROMPT-AVEUGLE-Sa-QM3-REDERIVATION.md`, sha256 `bfad7ce8778b614dc658e96882287abac73b93073003fb1936039a6c4d1bc58f`. Enonce du probleme seul ; ni script, ni note, ni conclusion.
- **S-b, audit de code** : `PROMPT-AVEUGLE-Sb-QM3-AUDIT-CODE.md`, sha256 `662106050fe36d28cee4982c0d7500a4082540017aff977e76d7da6651c8f131`. Script v5 seul (copie dans /home/claude/audit_b/, sha256 d240832c...), sans NOTE-92.
- Deux sous-agents distincts, lances en parallele, sans acces declare aux fichiers du travail.
- **Limite de cecite declaree** : l'en-tete du script v5 contient l'historique des versions, dont la mention que la v2 « excluait la solution homogene isotrope ». C'est un indice pour S-b. S-a n'y a pas acces : c'est S-a qui porte la cecite stricte.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Concordance totale de S-a et S-b sur P-1 a P-5. |
| **AU-V2** | Concordance sur les resultats porteurs (P-2, P-3), avec corrections mineures a nommer. |
| **AU-V3** | Discordance sur au moins un resultat porteur (P-2 ou P-3) : NOTE-92 est suspendue jusqu'a resolution. |
| **AU-V0** | Audit non concluant (rapport inexploitable, cecite rompue, ou echec technique). |

## 4. Prediction declaree
**AU-V2** : concordance sur P-2/P-3, avec au moins une reserve (composantes de R non toutes evaluees, ou portee de l'argument de troncature).

## 5. Non-surclassement
Un audit concordant n'eleve pas NOTE-92 au-dela de [conv] dans son cadre (lineaire, fond fixe, mode unique, secteur scalaire). Noyau {A4 ; A2★ ; N} inchange.
