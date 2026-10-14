---
id: NOTE-BORD-EON-119-ARMEMENT-AUDIT-IR-m
numero: 119
serie: I
branche: Q-M3 suite (audit IR-m)
reservation: 2026-10-11T16:55 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 119)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
statut: GEL (objets, prompts, espace des verdicts et prediction figes AVANT lancement des sous-agents)
decision: operateur (Thierry), 2026-10-11 18:54 heure de Paris : « commencer par IR-m, qui reservera les numeros 119 (gel) et 120 (concordance) »
depend: [NOTE-BORD-EON-111-IR-i-EXECUTION, NOTE-BORD-EON-116-IR-l-EXECUTION, NOTE-BORD-EON-118-IR-k-EXECUTION, NOTE-BORD-EON-113-AUDIT-IR-g-CONCORDANCE]
issue_attendue: "delimitation"
rouvre_si:
  - "contre-exemple confirme a la loi locale (bloc I), a la codimension 5 (bloc L) ou a l'absence de log dans T^(b) (bloc K)"
  - "discordance non resolue entre une re-derivation aveugle et la note auditee"
---

# NOTE-119 : armement de l'audit froid aveugle conjoint de NOTE-111, NOTE-116 et NOTE-118 (IR-m)

## 0. Origine
Reprise du 2026-10-11, §6.1, priorite 1 : NOTE-111, NOTE-116 et NOTE-118 sont les trois maillons **non audites** qui portent le renforcement du candidat M-V3 (incompatibilite du canal de jauge anomal avec la regularite de (2.17) pour un champ coherent generique). Aucune promotion n'est possible sans cet audit.

## 1. Objets audites (empreintes verifiees le 2026-10-11 sur copies fraiches de D:\temporaire)

| Note | Fichier | sha256 (16) | Scripts | sha256 (16) |
|---|---|---|---|---|
| 111 | NOTE-BORD-EON-111-IR-i-EXECUTION.md | 7f8597f1edf6be3b | ir_i.py | 060efdf85b2213f6 |
| 116 | NOTE-BORD-EON-116-IR-l-EXECUTION.md | 8436e99a79bc0b3c | ir_l_v2.py | bc17eb35414874c0 |
| 118 | NOTE-BORD-EON-118-IR-k-EXECUTION.md | 17d0fd95a495d414 | ir_k.py ; ir_k_affichage.py ; ir_k_ctrl.py | d58327fe5149ecaf ; ff8cbab65034da49 ; 1ef8a3ba6c9458ea |

## 2. Resultats porteurs soumis a l'audit
- **Bloc I (NOTE-111)**
  - I-A : sous H-loc, loi locale R_ln(x) = (3βκ/e²) Q_tf(x) a l'ordre s⁰, gradients en s ln s, fermeture libre sans effet sur les logs.
  - I-A' : lecture du defaut d'etiquette de ir_i.py (R-55).
  - I-B : carte du dipole eteint (boule vide, coquille 4/5, reliquat 1/5, integrales radiales).
  - I-C : sans H-loc, compensation anisotrope possible (point repris par K).
- **Bloc L (NOTE-116)**
  - L-A : formule exacte de Q_k en J₊, J₋.
  - L-B : seule la polarisation lineaire contribue.
  - L-C : interference moyennee ; composante E ℓ = 2 seule ; codimension 5 ; trois classes d'exception.
  - L-D : valeurs des sources tests.
- **Bloc K (NOTE-118)**
  - K-A : divergence de X^M sans log.
  - K-B : T^(b) de Riegert = derivees plates de ψ, sans φ ni log, T_2 = T_3, T_ii ~ s².
  - K-C : loi retrouvee avec X^M seul.
  - K-D : H-loc inutile pour le log, sous qualifications.

**Porteurs au sens du verdict** : I-A ; L-A et L-C ; K-B et K-C.

## 3. Protocole
Quatre sous-agents frais, lances en parallele, sans acces aux notes ni entre eux.
- **M-a1**, re-derivation independante du bloc I, cecite stricte : `PROMPT-AVEUGLE-Ma1-IR-i.md`, sha256 `f2b5cdc92a1f81c6948f46772c306d6deaab0bb9ed0e79720ef8fde052d6326b`. Les resultats (4/5, 1/5, ordre des gradients) ne sont pas donnes.
- **M-a2**, re-derivation independante du bloc L : `PROMPT-AVEUGLE-Ma2-IR-l.md`, sha256 `f57281f9c7d0224d126a4b631ab2d67fb08d75b8374a6f230230d29e20bf335d`. La formule de Q_k, la composante survivante, le nombre de conditions et les valeurs des sources ne sont pas donnes.
- **M-a3**, re-derivation independante du bloc K : `PROMPT-AVEUGLE-Ma3-IR-k.md`, sha256 `44a897176afe73d3a4eb595f5b3766fc9fc33305dc0dbb97e6bfd46d6b8b7274`. Les expressions de T^(b) et leur structure ne sont pas donnees ; la loi homogene deja auditee (NOTE-113) est donnee comme acquis.
- **M-b**, audit des cinq scripts, reproduction et recherche active de contre-exemples : `PROMPT-AVEUGLE-Mb-AUDIT-111-116-118.md`, sha256 `861d953224b46b599c4c3ba10ab6583e41db4bed09abe07b20bce049dfcc7adf` ; copies des scripts et sorties dans /home/claude/audit_mb/.

Transparence : M-b connait les affirmations (c'est son role) ; M-a1 a M-a3 ne les connaissent pas. La loi homogene (3κ/e²)Q_tf, auditee en NOTE-113, est fournie aux trois M-a comme acquis.

## 4. Espace des verdicts (fige)
| Id | Enonce |
|---|---|
| **AU-V1** | Concordance totale sur les trois blocs ; au plus des corrections de forme. |
| **AU-V2** | Concordance sur tous les resultats porteurs (I-A ; L-A, L-C ; K-B, K-C) ; corrections mineures (normalisations, facteurs, etiquettes, couverture des controles) ; qualifications nommees. |
| **AU-V3** | Discordance sur au moins un resultat porteur (contre-exemple confirme, coefficient, gradient a l'ordre s⁰, log ou φ dans T^(b), classe Q_tf = 0 plus large que la codimension 5) : la note concernee est suspendue, partiellement si le defaut est localise ; la part correspondante du renforcement de M-V3 est retiree. |
| **AU-V0** | Audit non concluant (rapports incomplets ou contradictoires sans arbitrage possible). |

Composites permis (par bloc).

## 5. Prediction declaree (anti-fit)
**AU-V2.** Les resultats porteurs sont confirmes. Corrections mineures attendues :
- normalisation des integrales radiales de NOTE-111 ;
- I-A' confirme comme pur defaut d'etiquette ;
- precision sur la codimension 5 de NOTE-116 (conditions sur le tenseur integre, pas sur la source elle-meme) ;
- au moins une qualification nommee sur K-D (W hors orbite, famille diagonale).

Risque principal identifie avant lancement : une hypothese cachee dans ir_k_ctrl.py, ou une classe d'exceptions a Q_tf = 0 plus large que les trois annoncees.

## 6. Instruments
Sous-agents outilles (sympy). Rapports reproduits dans `RAPPORT-IR-m-AUDIT-AVEUGLE.md`. Concordance en NOTE-120.

## 7. Non-surclassement
Un audit concordant n'eleve pas les notes au-dela de [conv]. M-V3 reste un candidat non grave. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.
