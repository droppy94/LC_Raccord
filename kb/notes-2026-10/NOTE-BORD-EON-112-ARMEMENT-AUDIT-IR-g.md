---
id: NOTE-BORD-EON-112-ARMEMENT-AUDIT-IR-g
numero: 112
serie: I
branche: Q-M3 suite (audit IR-g)
reservation: 2026-10-11T15:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 112)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL (prompts et espace des verdicts figes AVANT lancement des sous-agents)
depend: [NOTE-BORD-EON-108-IR-g-EXECUTION, NOTE-BORD-EON-107-ARMEMENT-IR-g]
issue_attendue: "delimitation"
rouvre_si:
  - "discordance non resolue sur G2 (loi 3 beta kappa/e^2 Q_tf) ou contre-exemple confirme"
---

# NOTE-112 : armement de l'audit froid aveugle de NOTE-108 (IR-j)

## 1. Resultats porteurs soumis a l'audit
- G1 : log de X^M = −2(T_B − T_E), Poynting sans log.
- G2 : **loi** coefficient de ln s dans R_{isi} = (3βκ/e²) × partie sans trace de Q = ⟨B_iB_j − E_iE_j⟩ ; trace sans effet.
- G3 : coupure de source (cos kD, sin kD), partie independante de D, moyenne spectrale.
- G4 : dipole (4/5)(mm − ⅓m²) ; ensemble isotrope nul.
- G5 : critere decisif = Q_tf, pas « magnetique / E = B ».

## 2. Protocole
- **J-a, re-derivation independante (cecite stricte, sans source externe)** : `PROMPT-AVEUGLE-Ja-IR-g.md`, sha256 `a80f50c445efb8c0890016747e9c86a3d69954d8b91e4ab5915e449a7cfd5abe`. La loi n'est pas donnee : J-a doit la trouver (Q2) et la tester hors diagonale (Q3).
- **J-b, audit du code et contre-exemples** : `PROMPT-AVEUGLE-Jb-IR-g-AUDIT.md`, sha256 `0eb8945399c63b4b5a9a1f76d94f9048995f9bcc13465b922419d7a86fab63cc` ; copie de ir_g.py (69496f14…) dans /home/claude/audit_jb/.
- NOTE-111 (version inhomogene) n'est pas soumise a cet audit.

## 3. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Concordance totale sur G1 a G5. |
| **AU-V2** | Concordance sur G1, G2 (loi et coefficient 3), G4 ; corrections mineures ; G5 valide sous hypotheses nommees. |
| **AU-V3** | Discordance sur G2 (coefficient, role de la trace, ou contre-exemple hors diagonale) ou G5 invalide : NOTE-108 suspendue (partiellement si seule G5 tombe). |
| **AU-V0** | Audit non concluant. |

## 4. Prediction declaree
**AU-V2** : G1, G2, G4 confirmes ; la loi s'etend sous forme tensorielle aux configurations hors diagonale (avec des composantes de R hors diagonale), avec au moins une reserve nommee (fermeture C-iso, partie homogene, ou termes croises entre modes qui ne se moyennent pas tous).

## 5. Non-surclassement
Un audit concordant n'eleve pas NOTE-108 au-dela de [conv]. Noyau {A4 ; A2★ ; N} inchange.
