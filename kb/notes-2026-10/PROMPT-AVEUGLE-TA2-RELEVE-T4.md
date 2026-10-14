# Consigne d'audit aveugle TA-2 : relevé numérique indépendant

Vous êtes un auditeur indépendant. Vous ne connaissez pas le programme qui vous mandate ni ses résultats. Faites les calculs demandés, avec votre propre script, et rendez un rapport. Travaillez seul dans `/home/claude/audit_p4/ta2/`.

## Données (unités ħ = c = 1)
- κ = 8πG.
- b = (N_S + 6 N_F + 12 N_V) / (120 (4π)²), où N_S, N_F, N_V comptent les scalaires réels, les fermions de Dirac et les champs de jauge sans masse.
- Entropie de de Sitter : S_dS = A/(4G) avec A l'aire de l'horizon, A = 4π/H² ; de plus Λ = 3H².

## Questions
**P1.** Calculez ε ≡ 8 b κ H² en fonction de G et H pour (i) N_S = 1 seul, (ii) N_F = 1 seul, (iii) N_V = 1 seul. Donnez les fractions exactes (pas de décimales) et le produit ε · S_dS pour chaque cas.

**P2.** Dans les unités où 8πG = 1, exprimez S_dS en fonction de Λ. Quel est le rapport (12π²/Λ) / S_dS ? Fraction exacte.

**P3.** Avec H = 1,5 × 10⁻³³ eV et M_P = 1,22 × 10¹⁹ GeV (G = 1/M_P²), donnez les ordres de grandeur de GH², de 1/S_dS et de ε pour N_V = 1.

**P4.** Vérifiez par un calcul numérique indépendant (pas la même formule réécrite : par exemple évaluez les deux membres séparément en flottants) l'identité que vous obtenez en P1 pour le cas général n = N_S + 6N_F + 12N_V.

**P5.** Répondez en une phrase : les deux quantités ε et 1/S_dS ont-elles la même dépendance en G et H ? Si oui, est-ce surprenant par analyse dimensionnelle, ou attendu ? Ne spéculez pas au-delà.

## Règles
- Script Python avec `fractions.Fraction` pour les fractions exactes ; archivez le script et sa sortie dans votre dossier.
- Rapport : `/home/claude/audit_p4/ta2/RAPPORT-TA2.md`, en français, puis `sha256sum` du rapport, du script et de la sortie dans `/home/claude/audit_p4/ta2/SHA256SUMS.txt`.
