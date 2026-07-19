---
id: LC-D-SPN
type: chaînon (verdict — NON scellant pour les (a,b,c) propres)
codename: LC-RACCORD
prerequis_kb: [LC-WORK-CADRAGE-SPN]
version: 0.2
date: 2026-06-13
statut: "établi (algèbre) — sous-front (b) Sp(N). Le modèle Sp(N) libre (AHS, dual higher-spin de Vasiliev en dS₄) réalise un exemple dS/CFT explicite de la branche paire-scalaire, avec C_T = −C_T^O(N) < 0 ∝ −N en d=3, COHÉRENT avec le firewall i^(d−1). Cibles gelées T-B1..4 : 4/4 concordantes (R-7). Verdict : CONSOLIDATION → DÉCISION OUVERTE DOCUMENTÉE : higher-spin ≠ Einstein ⟹ les (a,b,c) propres NE SONT PAS fixés. Compte {A4 ; A2★ ; N} INCHANGÉ. Ne permet PAS de dire « CFT de raccordement identifiée / D1 clos / N fixé / CCC démontrée »."
maj: "2026-07-06 — v0.2 : hygiène (§1.4.2 reprise V54) — ajout de l'arête prerequis_kb: [LC-WORK-CADRAGE-SPN] (recollage de l'in-degree structurel ; provenance déjà scellée par sha 1b87ffdf…da82 en corps/maj v0.1 et docstring de verif_spn.py). Additif, 0 ligne de corps perdue, aucun changement de substance ; établi (algèbre) inchangé ; {A4 ; A2★ ; N} INCHANGÉ ; D1 non clos ; N non fixé ; CCC non démontrée. | 2026-06-13 — v0.1 : création en clôture du sous-front (b). Cadrage gelé LC-WORK-CADRAGE-SPN v0.1 (sha 1b87ff…da82) ; source 1108.5735v1 consommée (eq. 2.1-2.5, règle de signe eq. 2.4) ; sceau verif_spn.py (sha d34031…5687, EXIT 0, 23 asserts dont firewall 7/7)."
---

# LC-D-SPN — Sous-front (b) : modèle Sp(N) (AHS dS/CFT higher-spin)

> §6.4 : `établi (algèbre)` = algèbre correcte + cibles reproduites. Ce chaînon
> NE permet PAS de dire « (a,b,c) propres fixés / CFT de raccordement identifiée
> / D1 clos / N fixé / CCC démontrée ». Le verdict est borné d'avance par T-B4.

## 0. Provenance et gel anti-fit

- **Cadrage gelé** : `LC-WORK-CADRAGE-SPN` v0.1, sha256
  `1b87ffdf27dd9bd63d7f28ce7e5a0c18f3dcc28a5fd2ef4492821cb555d8da82`,
  consigné AVANT ouverture du PDF (ordre gel→fetch tracé en conversation).
- **Source** : arXiv:1108.5735v1, Anninos–Hartman–Strominger, *Higher Spin
  Realization of the dS/CFT Correspondence*, CQG **34** (2017) 015009.
- **Sceau** : `verif_spn.py`, sha256
  `d34031f0b572be547538cc89bd658751d1db1685fd4f3ab6013593d6012e5687`,
  EXIT 0, 23 asserts (A:4 / B:5 / C:7 / firewall 7/7).

## 1. Relevé source `[établi — telle qu'imprimée]`

1. **Conjecture AHS** : Vasiliev higher-spin en dS₄ ↔ modèle vectoriel
   **Sp(N) euclidien libre** à scalaires **anticommutants** (CFT non-unitaire,
   structure « pseudo-unitaire ») ; analogue dS de la dualité GKPY O(N)/AdS₄.
2. **Modèle libre** (éq. 2.1) : action à forme symplectique Ω, χ scalaire
   anticommutant à N composantes, **N pair**. Courants singlets conservés de
   **tous les spins PAIRS** (éq. 2.2), Δ = s+1. Le tenseur d'énergie-impulsion
   est le courant **s = 2** (Δ = 3 = d).
3. **Règle de signe** (éq. 2.4) : pour les corrélateurs singlets,
   `⟨J^(s₁)…J^(sₙ)⟩_Sp(N) = − ⟨J^(s₁)…J^(sₙ)⟩_O(N)`. Un **(−1) par boucle**
   (Fermi) ; un corrélateur connecté libre à n insertions = **une** boucle.
   Toute la dépendance en N étant dans le facteur global, ceci équivaut à
   **N → −N** (`O(−N) = Sp(N)`, transpose des tableaux de Young : bosons↔fermions).
4. **Origine** : continuation EAdS₄↔dS₄ renversant Λ→−Λ (G_N fixe) ; `N ∼ 1/(ΛG_N)`
   ⟹ N→−N. Version **parity-invariant** ⟹ secteur impair libre nul.

## 2. Confrontation aux cibles gelées T-B `[établi — 4/4, R-7]`

| Cible | Prédiction gelée (pré-fetch) | Source AHS | Verdict |
|---|---|---|---|
| **T-B1** parité | paire seule au niveau libre, 0 impaire | spins pairs uniquement, parity-invariant | CONCORDANT |
| **T-B2** signe C_T | opposé à O(N), négatif, recoupe i^(d−1) | C_T^Sp = −C_T^O < 0 (éq. 2.4, n=2) | CONCORDANT (cohérence) |
| **T-B3** magnitude | ∝ N (linéaire) | facteur global 1-boucle ⟹ ∝ −N | CONCORDANT |
| **T-B4** plafond | (a,b,c) propres NON fixés ; décision ouverte | dual = Vasiliev higher-spin (∀ spins pairs) ≠ Einstein | CONCORDANT (gelé) |

Aucune cible amendée après ouverture (R-7).

## 3. Mapping (a,b,c) `[établi — aucune structure surnuméraire]`

`⟨TTT⟩_Sp(N) = − ⟨TTT⟩_O(N libre)` = structure du **scalaire libre** ×(−N).
Ceci réalise la branche **paire « boson/scalaire »** du comptage **2+1** scellé
(PL-D, GPY), **signe basculé** ; **zéro structure paire neuve**, pas de
surnuméraire. Le modèle Sp(N) **n'introduit aucun `(a,b,c)` indépendant** et
**ne fixe pas** les `(a,b,c) propres` du dual Einstein.

## 4. Cross-check de signe — cohérence, PAS convergence `[décision de discipline]`

Le signe négatif AHS (N→−N / Fermi) et la négativité programme (`C_T` réel
négatif en d=3 via i^(d−1)) **partagent la même origine** : la continuation dS
(Λ→−Λ / fonction d'onde Hartle-Hawking). C'est donc une **cohérence /
consolidation** — **une seule chaîne ancrée**, **pas** une convergence
indépendante. Aucune indépendance n'est revendiquée (firewall F-7). Apport :
le firewall de négativité reçoit une **réalisation dS/CFT explicite et
entièrement calculée**, ce qui renforce la confiance sans réduire le compte.

## 5. Verdict `[décision ouverte documentée]`

**CONSOLIDATION.** Le sous-front (b) documente que la CFT Sp(N) d'AHS, bien
qu'elle soit un exemple dS/CFT explicite cohérent avec les acquis programme
(branche paire-scalaire ; C_T < 0 ∝ −N en d=3), **ne peut pas fixer les
`(a,b,c) propres`** : son dual est higher-spin (Vasiliev), pas Einstein. La
décision ouverte `(a,b,c) propres / CFT de raccordement` **reste ouverte**,
désormais **documentée** (point de référence higher-spin + cross-check de signe).

**Sans surclassement (§6.4).** Périmètre ouvert irréductible **{A4 ; A2★ ; N}**
**INCHANGÉ** (zéro réduction). D1 non clos ; `N` non fixé (≡ Λ) ; CCC non
démontrée. Caveat permanent : **higher-spin ≠ Einstein**.

## 6. Audit à froid

**S-B5 différé / réversible** (volet faible : consolidation pure, source = papier
fondateur dS/CFT, relevé = règle de signe explicite imprimée). Aucune dette.
