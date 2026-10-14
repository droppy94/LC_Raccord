# RAPPORT TA-2 : relevé numérique indépendant

Auditeur : indépendant, aveugle au programme mandant. Date : 2026-10-14.
Dossier de travail : `/home/claude/audit_p4/ta2/`. Script : `audit_ta2.py` (exécuté avec `python3 -I`), sortie : `audit_ta2_sortie.txt`.

## Données et quantités dérivées (ħ = c = 1)

- κ = 8πG
- b = n / (120 (4π)²) = n / (1920 π²), avec n = N_S + 6 N_F + 12 N_V
- A = 4π/H², S_dS = A/(4G) = π/(G H²)
- Λ = 3H²

## P1. ε = 8 b κ H²

Réduction algébrique : ε = 8 · n/(1920π²) · 8πG · H² = n G H² / (30π).

| Cas | n | b | ε | ε · S_dS |
|---|---|---|---|---|
| (i) N_S = 1 | 1 | 1/(1920π²) | G H² / (30π) | 1/30 |
| (ii) N_F = 1 | 6 | 1/(320π²) | G H² / (5π) | 1/5 |
| (iii) N_V = 1 | 12 | 1/(160π²) | 2 G H² / (5π) | 2/5 |

Identité générale : ε · S_dS = n/30 (sans dimension, indépendante de G, H et π).

## P2. Unités 8πG = 1

G = 1/(8π), donc S_dS = π/(G H²) = 8π²/H². Avec H² = Λ/3 : S_dS = 24π²/Λ.

Rapport (12π²/Λ) / S_dS = 12/24 = **1/2**.

## P3. Ordres de grandeur

H = 1,5 × 10⁻³³ eV = 1,5 × 10⁻⁴² GeV ; G = 1/M_P² = 6,72 × 10⁻³⁹ GeV⁻².

- G H² ≈ 1,5 × 10⁻¹²²
- S_dS = π/(G H²) ≈ 2,1 × 10¹²², soit 1/S_dS ≈ 4,8 × 10⁻¹²³
- ε (N_V = 1) = 2 G H²/(5π) ≈ 1,9 × 10⁻¹²³

Contrôle : ε · S_dS = 0,400000 numériquement, conforme à 2/5.

## P4. Contrôle numérique indépendant

Les deux membres de ε · S_dS = n/30 ont été évalués séparément en flottants, à partir des définitions brutes (b, κ, A, S_dS calculés directement avec `math.pi`, sans passer par la réduction symbolique), pour 2000 tirages aléatoires de (N_S, N_F, N_V) dans 0..7 et de G, H log-uniformes sur 128 et 48 décades. Écart relatif maximal observé < 10⁻¹² : identité vérifiée. Vérifié aussi sur les valeurs physiques de P3 pour n = 1, 6, 12 (0,0333…, 0,2, 0,4 à 15 décimales).

## P5. Réponse en une phrase

Oui : ε ∝ G H² et 1/S_dS = G H²/π ont exactement la même dépendance en G et H, et cela est attendu par analyse dimensionnelle, puisque G H² est la seule combinaison sans dimension constructible à partir de G et H (en ħ = c = 1), de sorte que toute quantité sans dimension bâtie sur ces deux seules grandeurs lui est proportionnelle ; seul le coefficient numérique (n/30 ici) porte une information non dimensionnelle.

## Remarques d'audit

- Aucune ambiguïté rencontrée dans l'énoncé ; la convention b = n/(120(4π)²) a été appliquée telle quelle, sans vérification de son origine physique (hors mandat).
- Les fractions ont été obtenues avec `fractions.Fraction`, π étant traité comme un exposant entier symbolique.
