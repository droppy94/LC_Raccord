---
id: NOTE-BORD-EON-99-ARMEMENT-AUDIT-CHAMP-COHERENT
numero: 99
serie: I
branche: Q-M3 suite (audit)
reservation: 2026-10-10T12:17 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 99)
date: 2026-10-10
programme: LC-RACCORD
grade: "[conv]"
statut: GEL (prompts et espace des verdicts figes AVANT lancement des sous-agents)
depend: [NOTE-BORD-EON-98-CHAMP-COHERENT-EXECUTION, NOTE-BORD-EON-97-ARMEMENT-CHAMP-COHERENT]
issue_attendue: "delimitation"
rouvre_si:
  - "discordance non resolue entre C-a et C-b, ou sur l'argument de symetrie"
---

# NOTE-99 : armement de l'audit froid aveugle de NOTE-98

## 1. Resultats porteurs soumis a l'audit (NOTE-98)
- Q-1 : `F_xy = B₀` resout l'equation de jauge ; `X^M = (B₀²/e²) Ω² (½ − β̃ ln Ω) diag(1,1,1,−1)`, sans trace ; `∇̂^μ X^M_μ0 = β̃B₀²Ω³/e²`.
- Q-2 : trace anomale `T̂ = −(β̃B₀²/e²) Ω⁴`.
- Q-3 : sous C-iso, (2.17) porte ln Ω avec coefficients `−κβ̃B₀²/e²` (deux composantes) et `+2κβ̃B₀²/e²` (une) ; regulier a β̃ = 0.
- Q-4 : budget requis `Π = (2β̃B₀²/3e²) Ω² ln Ω + …`, exactement oppose a la partie anisotrope logarithmique du secteur Maxwell.
- Q-5 : argument de symetrie [derive] (§3 de NOTE-98) : pour toute completion `∫ Ω[g] F²`, la partie non Maxwell est isotrope pour ce champ ; compensation impossible.

## 2. Protocole
- **C-a, re-derivation independante** (cecite stricte, sans script ni note ni resultat) : `PROMPT-AVEUGLE-Ca-CHAMP-COHERENT.md`, sha256 `5eb84503b788ee56e8b80556ef47199320e45d13c260704d3a717009f1106f8b`. Sa question 7 sur la structure de la completion est posee de facon neutre.
- **C-b, audit du code v3 et de l'argument (B)** : `PROMPT-AVEUGLE-Cb-CHAMP-COHERENT-AUDIT.md`, sha256 `08330ed7b6df429fa52f2724f43cf225a9014fb6cee5bc71edfb0ed4df9eca21` ; copie du script dans /home/claude/audit_cb/ (sha256 9c7d5c04…). L'argument est soumis en texte, sans NOTE-98.
- Limite de cecite declaree : C-b voit le script, qui imprime ses resultats ; C-a porte la cecite stricte.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Concordance totale sur Q-1 a Q-5. |
| **AU-V2** | Concordance sur Q-3 et Q-4 (resultats porteurs du calcul), corrections mineures ; Q-5 valide sous hypotheses nommees. |
| **AU-V3** | Discordance sur Q-3, Q-4, ou Q-5 juge invalide : NOTE-98 suspendue (partiellement si seul Q-5 tombe). |
| **AU-V0** | Audit non concluant. |

## 4. Prediction declaree
**AU-V2** : calcul confirme ; l'argument Q-5 juge valide sous hypotheses (role de S_flat, definition de l'etat pour l'operateur non local), avec au moins une reserve nommee.

## 5. Non-surclassement
Un audit concordant n'eleve pas NOTE-98 au-dela de [conv]. M-V3 reste un candidat conditionnel. Noyau {A4 ; A2★ ; N} inchange.
