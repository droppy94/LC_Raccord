---
id: "à assigner — proposé : HKB-07 « V1.d.i.α.1 : Weyl linéarisé, verdict, pont mémoire »"
titre: "Weyl électrique linéarisé du graviton au bord — verdict à deux niveaux et raccord bord↔horizon par l'observable de mémoire"
programme: LC-RACCORD
parent: NOTE-BORD-EON-05 (§6, §10-V1.d.i.α.1)
version: v0.1
date: 2026-07-12
statut: brouillon de calcul + verdict soumis à évaluation
charte: L-001
provenance: >
  Calcul posé en dialogue avec un assistant IA. La dérivation §1 (Weyl linéarisé) est faite
  DEPUIS ZÉRO et doit être re-vérifiée indépendamment (ground-truth, L-001). Les faits §4–§5
  (IR du scalaire MMC ; vide dS-invariant du graviton ; corrélateur Weyl ∼ dist⁻⁴) sont sourcés.
tags_globaux: [établi, calcul, décision-ouverte, rejeté]
verdict_court: >
  Le raccourci « graviton = 2 scalaires libres » ÉCHOUE (le scalaire MMC n'a pas de vide
  dS-invariant : IR/mémoire, v∼1/τ, nucléarité divergente). MAIS le graviton GAUGE-INVARIANT
  a un bon vide (corrélateur de Weyl ∼ dist⁻⁴), donc T2 reste PLAUSIBLE — à condition de
  travailler sur l'algèbre dressée. Et la mémoire (= mode gelé) relie le bord à l'horizon (voie H).
---

# NOTE-BORD-EON-06 — Weyl linéarisé, verdict, et le pont mémoire (V1.d.i.α.1)

## 0. Verdict en une ligne

Le calcul ne tranche pas « quel mode » (§2 montre pourquoi la question était mal posée) : il
révèle que **strong WCH = vide de gravitons complet**, donc la nucléarité est une propriété de
l'**état**, pas d'un mode classique. Et là, deux niveaux :

- **Route naïve (2 scalaires libres) : ÉCHOUE** — le scalaire minimalement couplé n'a pas de
  vide de Sitter-invariant (IR/mémoire), le mode gelé donne v ∼ 1/τ, la borne L²-nucléaire diverge.
- **Route physique (graviton gauge-invariant) : PLAUSIBLE** — le graviton linéarisé a, lui, un
  vide dS-invariant, et le corrélateur de Weyl décroît en dist⁻⁴ (bon falloff).

Conclusion : **T2 tient possiblement, mais seulement sur l'algèbre dressée gauge-invariante ; le
raccourci scalaire est exactement ce qui la casse.** Et le mécanisme qui sauve le graviton — le
traitement de la **mémoire** — passe par l'horizon cosmologique : le bord et l'horizon (voie H)
se rejoignent ici, concrètement.

---

## 1. Calcul explicite — le Weyl électrique linéarisé [calcul depuis zéro, à re-vérifier]

Fond conformément plat (de Sitter = a²·Minkowski). Par invariance conforme du Weyl mixte,
δC^a_{bcd}[g̃] = δC^a_{bcd}[η_Mink + h], soit le Weyl plat linéarisé de la perturbation TT h.
Jauge TT : h_{0μ}=0, h^i_i=0, ∂^i h_{ij}=0. Mode ε_ij h(η)e^{ik·x}.

Riemann linéarisé :
- Partie électrique de Riemann : δR_{0i0j} = −½ ∂_0² h_{ij} = −½ h'' ε_ij .
- Ricci linéarisé (TT) : δR_{ij} = −½ □ h_{ij}, avec □ = −∂_0² + ∇², donc
  □h = (−h'' − k²h) et **δR_{ij} = ½(h'' + k²h) ε_ij** ; δR_{00}=0, δR=0.

Weyl (4d), composante électrique C_{0i0j} = R_{0i0j} + ½ R_{ij} (les autres termes s'annulent
car g_{0j}=0, R_{00}=R=0, g_{00}=−1) :

    E_ij = δC_{0i0j} = −½ h'' ε + ½·½(h'' + k²h) ε
                     = −¼ ( h'' − k²h ) ε_ij .                              (★)

Partie magnétique (dual) : B_ij ∝ ε_i^{kl} ∂_0 ∂_k h_{lj} ∝ k h' .          (★★)

**Comportement aux deux modes près de Σ** (τ = −η → 0), avec les solutions de Frobenius de
NOTE-05 : mode gelé h_F = 1 + (k²/2)η² − (k⁴/8)η⁴ + … ; mode décroissant h_D ∼ η³ :

| Composante | mode gelé | mode décroissant | portée dominante |
|---|---|---|---|
| E ∝ (h″ − k²h) | ∼ −2k⁴η² (ordre η²) | ∼ 6η (ordre η¹) | **décroissant** |
| B ∝ k h′ | ∼ k³η (ordre η¹) | ∼ 3kη² (ordre η²) | **gelé** |

E et B sont donc portés, au premier ordre, par des modes **opposés**.

---

## 2. Pourquoi « quel mode » était mal posé — strong WCH = vide complet [calcul + établi]

Strong WCH impose le **Weyl rescalé total nul** en Σ, soit E=0 **et** B=0. Par (★)–(★★) et le
tableau, cela annule au premier ordre **les deux** coefficients (décroissant via E, gelé via B).
Il n'y a que 2 coefficients par (polarisation, k) ; deux conditions ⇒ **aucun mode classique ne
survit** : strong WCH = **vide de gravitons complet** au bord, pas une sélection de branche.

Corollaire : la nucléarité pertinente est celle de l'**état de vide** sélectionné par Weyl=0, non
d'un mode résiduel. Le calcul de §1 n'était pas inutile — il montre que la question classique
s'effondre et renvoie à une question **quantique** sur le vide. C'est là qu'est le vrai contenu.

---

## 3. La question quantique — nucléarité du vide Weyl=0 [reformulation]

Il faut la fonction à deux points W(x,x′) du vide graviton (Weyl=0) près de Σ, et estimer
‖Δ_Õ^{1/4} Δ_O^{-1/4}‖₁. Deux formulations donnent des réponses **opposées** — c'est le nœud.

---

## 4. Route naïve (2 scalaires MMC) — ÉCHEC [établi, sourcé]

Le raccourci « graviton = 2 scalaires sans masse **minimalement** couplés » bute sur un fait dur :

- **Le scalaire minimalement couplé sans masse n'a PAS de vide de Sitter-invariant** (Allen 1985 ;
  Allen–Folacci 1987). Le « mode constant » (gelé) et sa **mémoire** rendent la fonction à deux
  points IR-divergente / non-décroissante ; ⟨T_{μν}⟩ tend vers une constante non nulle (Allen–Folacci),
  pas vers zéro. [réf. 1, 2]
- Concrètement au bord : le mode gelé donne v = a·h ∼ 1/τ (divergent, NOTE-05), et W ne décroît
  pas en Σ ⇒ contribution de collerette ∝ τ⁻² ⇒ **borne L²-nucléaire divergente**.

Donc, sur l'algèbre des scalaires nus, **T2 est faux** : la nucléarité échoue par l'IR/mémoire.
Ce n'est PAS un artefact de Weyl=0 ; c'est intrinsèque au scalaire MMC en de Sitter.

---

## 5. Route physique (graviton gauge-invariant) — PLAUSIBLE [établi, sourcé]

Le graviton physique n'est pas 2 scalaires nus : c'est un champ **de jauge à contraintes**, et sa
partie observable se comporte bien mieux :

- **Le graviton linéarisé A un vide de Sitter-invariant.** Critère (Hollands / cadre ABK) :
  existence d'un vide dS-invariant ⟺ les observables locales **commutent avec l'observable de
  mémoire** sur l'horizon cosmologique. Ce critère est **satisfait** par le scalaire massif, le
  champ EM et le **champ gravitationnel linéarisé** — mais **PAS** par le scalaire MMC. [réf. 3]
- **Le corrélateur de Weyl décroît proprement.** La fonction à deux points du graviton
  **gauge-invariante** équivaut au corrélateur du tenseur de Weyl, qui décroît en **(distance)⁻⁴**
  pour séparation spatiale dans le patch de Poincaré de de Sitter. [réf. 4]

Un falloff en dist⁻⁴ est exactement le comportement Hadamard/UV sain requis par la nucléarité
(Verch, Longo). Donc, sur l'algèbre **gauge-invariante**, la nucléarité est **plausible**, et
**T2 peut tenir**.

Le contraste est net : la pathologie IR de la route naïve est **de jauge** ; l'observable
gauge-invariant (Weyl) l'évacue. Le raccourci « 2 scalaires libres » est précisément ce qui
injecte la fausse divergence.

---

## 6. Le pont concret bord ↔ horizon — l'observable de mémoire [formalisable — le gain]

Le mécanisme qui sauve le graviton (§5) est le **traitement de la mémoire** : le vide dS-invariant
existe ssi les observables commutent avec l'**observable de mémoire sur l'horizon cosmologique**
(réf. 3). Or la mémoire, c'est **le mode gelé** (§1, la partie magnétique / Coulombique). Donc :

> Le mode gelé — celui qui faisait diverger la nucléarité du bord (route naïve) — n'est pas éliminé
> mais **absorbé par l'observable de mémoire de l'horizon**.

C'est le **raccord concret entre le bord (crossover) et l'horizon (voie H, CLPW, NOTE-02)** :
la difficulté du bord (mémoire/mode gelé) est résolue par la structure d'horizon. Les deux voies
de NOTE-02 ne sont pas des alternatives — elles sont **couplées par la mémoire**. Le dressing par
observateur de CLPW et l'observable de mémoire sont vraisemblablement le **même objet**.

Ce résultat unifie : le pont WCH ⇒ scission (chantier bord) passe nécessairement par la structure
d'horizon (chantier KMS/voie H), via la mémoire. C'est le gain le plus substantiel de la chaîne.

---

## 7. Vérification de cohérence — Tod [établi]

La donnée libre de Tod à la singularité isotrope est la **3-métrique conforme** (donnée
Coulombique/cinématique), le Weyl **radiatif** étant contraint. Cela concorde avec (★) : la partie
qui distingue radiatif (E, décroissant) de mémoire (B, gelé) est exactement la structure que WCH
manipule, et la donnée « qui reste » (3-métrique) est du côté mémoire/gelé — le côté horizon.
Cohérence non triviale entre géométrie (Tod), calcul (★) et algèbre (mémoire).

---

## 8. Ce qui reste — V1.d.i.α.1.a–c

- **V1.d.i.α.1.a [central, positif].** Prouver la nucléarité (borne L²) du vide **gauge-invariant**
  du graviton près du Σ **spacelike** (pas seulement patch de Poincaré), en utilisant le falloff
  dist⁻⁴ ; établir T2 sur l'algèbre dressée.
- **V1.d.i.α.1.b [le pont].** Identifier explicitement l'**observable de mémoire de l'horizon** au
  dressing d'observateur de CLPW ; montrer que c'est le même objet ⇒ raccord bord↔horizon formel.
- **V1.d.i.α.1.c.** Terme log (NOTE-05 §5) et corrections Hadamard ; effet des Hawking points sur
  la mémoire (NOTE-02 §4).

---

## 9. Garde-fous [rejeté / attention]

- **« Graviton = 2 scalaires libres »** : **réfuté ici** comme base de la nucléarité — introduit une
  divergence IR de jauge. La nucléarité doit se lire sur l'algèbre gauge-invariante (Weyl/dressée).
- **Ne pas conclure T2 vrai** : §5 donne « plausible » (falloff dist⁻⁴), pas « démontré » ; la
  preuve au bord spacelike reste à faire (V1.d.i.α.1.a).
- **Dérivation (★) depuis zéro** : re-vérifier indépendamment (signes, coefficient ¼) avant usage.
- **de Sitter / patch de Poincaré** : le corrélateur dist⁻⁴ est établi là ; l'extension au vrai
  crossover et au bord spacelike global reste à confirmer.

---

## 10. Synthèse taguée

**établi / calcul**
- (★) E_ij = −¼(h″ − k²h)ε_ij ; (★★) B_ij ∝ k h′. E porté par le décroissant, B par le gelé (ordres opposés).
- Strong WCH (E=0 et B=0) ⇒ **vide graviton complet** ; la nucléarité est une question d'état, pas de mode.
- Scalaire MMC : **pas de vide dS-invariant** (Allen–Folacci) ⇒ route naïve **échoue** (IR/mémoire, v∼1/τ).
- Graviton **gauge-invariant** : **a** un vide dS-invariant (critère mémoire-horizon) ; corrélateur de Weyl ∼ dist⁻⁴.

**formalisable**
- T2 **plausible sur l'algèbre gauge-invariante/dressée** (falloff dist⁻⁴ ⇒ nucléarité).
- **Pont mémoire** : le mode gelé du bord est absorbé par l'observable de mémoire de l'horizon ⇒
  raccord concret bord↔horizon (voie H) ; dressing CLPW ≈ observable de mémoire.

**décision-ouverte**
- a. nucléarité gauge-invariante au Σ spacelike (au-delà du patch de Poincaré) ⇒ preuve de T2.
- b. identité formelle observable-de-mémoire ↔ dressing CLPW.
- c. log + Hawking points sur la mémoire.

**rejeté / garde-fous**
- « graviton = 2 scalaires libres » comme base de nucléarité (IR de jauge).
- conclure T2 démontré (seulement plausible).

**Phrase-noyau** : *le Weyl linéarisé explicite montre que strong WCH annule les deux modes (vide
graviton complet), déplaçant la question vers la nucléarité de l'état ; là, le raccourci « 2
scalaires » échoue par l'IR incurable du scalaire minimalement couplé, mais le graviton
gauge-invariant a un vrai vide de Sitter et un corrélateur de Weyl en dist⁻⁴, si bien que T2 tient
possiblement sur l'algèbre dressée — et le mécanisme qui l'y sauve, l'observable de mémoire sur
l'horizon cosmologique, est précisément le raccord concret entre le bord et la voie H.*

---

## 11. Références sourcées [vérif. — sources primaires + re-dérivation (★) exigées, L-001]

1. B. Allen — « Vacuum states in de Sitter space », Phys. Rev. D 32, 3136 (1985). [pas de vide
   dS-invariant pour le scalaire MMC]
2. B. Allen, A. Folacci — « The Massless Minimally Coupled Scalar Field in de Sitter Space »,
   Phys. Rev. D 35, 3771 (1987). [mode zéro/mémoire ; ⟨T⟩ → const non nulle]
3. « Vacua and infrared radiation in de Sitter quantum field theory » (cadre Hollands / ABK) —
   critère : vide dS-invariant ⟺ observables commutant avec l'observable de mémoire sur l'horizon ;
   satisfait par massif, EM, **graviton linéarisé** ; PAS par MMC. [réf. via ResearchGate
   « De Sitter invariance of the dS graviton vacuum »]
4. « Linearized Weyl–Weyl correlator in a de Sitter breaking gauge » — la fonction à deux points
   graviton gauge-invariante = corrélateur de Weyl, décroît en (distance)⁻⁴ (patch de Poincaré). [arXiv ~2012]
5. Perturbations cosmologiques (Mukhanov et al.) ; modes de Frobenius : NOTE-05.
6. R. Longo (L²-nucléarité, math-ph/0603083) ; R. Verch (nucléarité/scission KG courbe, 1993) :
   NOTE-04. G. W. Gibbons, S. W. Hawking (1977) : température d'horizon (voie H, NOTE-02).
7. Ashtekar–Bonga–Kesavan (Asymptotics with positive Λ, I–III) : Weyl rescalé électrique, flux au
   bord spacelike : NOTE-05 réf. 4.

---

*Fin de NOTE-BORD-EON-06 v0.1. Calcul (★) explicite ; verdict à deux niveaux ; pont mémoire
bord↔horizon dégagé. Sous-verrous V1.d.i.α.1.a–c ouverts. La chaîne a produit son premier
raccord concret entre les deux chantiers de LC-RACCORD.*
