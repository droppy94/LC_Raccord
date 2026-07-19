---
id: LC-WORK-CADRAGE-O2-P1B-SOPERATION
titre: "Cadrage gelé R-36 — test de la gate P1 via la S-OPÉRATION GRAVITATIONNELLE sur le doublet de bord (Witten SL(2,Z) / Leigh-Petkou / de Haro) : la réciprocité conforme de Penrose, écrite en coefficients FG sur {g₀, g₃}, coïncide-t-elle avec l'opération S — FACTEURS COMPRIS, en particulier le −𝟙 ? Ré-arme la route b′ (parité du poids w) laissée fetch-gated par LC-D-O2-P1 (2026-06-15). Cibles SP-1..SP-3 + firewall SP-R figées AVANT toute lecture engagée."
codename: LC-RACCORD
tags: [work, cadrage, R-36, R-7, anti-fit, O2, P1, route-b-prime, S-operation, SL2Z, Witten, Leigh-Petkou, de-Haro, doublet-de-bord, Legendre, Chern-Simons, moins-un, fetch-gated]
statut: "cadrage GELÉ (R-36 ; sha hors-fichier consigné au manifeste au dépôt) — AUCUNE algèbre, AUCUN fetch, AUCUN sceau dans ce fichier. Origine : crible du portrait (LC-WORK-PORTRAIT-INTRANT-EXTERNE §4) sur question opérateur + document externe de criblage lu 2026-07-03 (hors-KB, non-adjugeant) ; constat KB : Witten hep-th/0307041 et Leigh-Petkou hep-th/0309177 JAMAIS consommés (grep zéro occurrence), alors que la S-map de de Haro est testée par 4 chaînons scellés (CT-DUAL, CT-DUAL-DS, O2-P1, O2-HODGE). Classement P-α (route A-d, traits C1+C2). L'enjeu exact : O2-P1 a établi que l'involution conforme nue donne s=+1 (le −𝟙 manque) et a réduit P1 au signe s=(−1)^w, fetch-gated ; la couche SL(2,Z)/CS fournit-elle ce −𝟙 PAR LA QUANTIFICATION (niveau Chern-Simons, structure symplectique du doublet) — telle qu'imprimée, au niveau GRAVITON (pas seulement U(1)) ?"
type: "cadrage d'exécution (anti-fit / R-7) : fige cibles, espace de verdicts, sources armées, firewall et interdictions AVANT toute lecture engagée des sources non-consommées."
version: 1.0
langue: fr
date: 2026-07-03
prerequis_kb: [LC-D-O2-P1, LC-D-O2-HODGE, LC-D-CT-DUAL, LC-D-CT-DUAL-DS, LC-D-CT-REALITE, LC-D-O2-JONCTION, LC-D-O2-SCATTERING-FG, LC-WORK-PORTRAIT-INTRANT-EXTERNE, LC-D-G3-TRANSPORT]
maj: "2026-07-03 — v1.0 : rédaction initiale et gel. Sources armées : S1 = Witten hep-th/0307041 (SL(2,Z) action on 3d CFTs) ; S2 = Leigh-Petkou hep-th/0309177 (dualité gravitationnelle AdS₄/CFT₃) ; S3 = de Haro 0808.2054 (KB-locale, re-lecture ciblée éq. S-map) ; S4 = réciprocité conforme de Penrose, Cycles of Time (KB [LC-A]). Amendement R-7 : S1/S2 = EXTENSION DE PORTÉE de la route b′ (qui listait Cycles of Time + lois FG de de Haro) — le présent cadrage VAUT amendement daté, consigné au manifeste avec le gel."
---

# Cadrage P1-b′ — la S-opération fournit-elle le −𝟙 ? `[GELÉ AVANT LECTURE]`

## 0. Rôle, origine, garde-fou `[§6.4 + R-7 + R-36]`

**Question unique (gelée).** La gate P1 d'O₂ (réciprocité conforme de Penrose
≟ S-map de de Haro, FACTEURS COMPRIS) bute depuis `O2-P1` sur un point
précis : le swap `g₀↔g₃` est induit par l'inversion `Ω↦−1/Ω`, mais
l'involution conforme NUE donne `P²=+𝟙` (s=+1), pas `S²=−𝟙`. Le facteur
décisif a été isolé : `s=(−1)^w` (parité du poids conforme w du mode TT sous
facteur négatif), resté fetch-gated. La couche structurelle au-dessus de
de Haro — Witten SL(2,Z) sur les CFT₃, Leigh-Petkou dualité gravitationnelle —
n'a JAMAIS été consommée. Le présent cadrage arme sa lecture contre UNE
question : **le −𝟙 de S est-il porté par la couche de QUANTIFICATION (niveau
Chern-Simons, structure symplectique du doublet de bord) et cette couche
s'applique-t-elle, telle qu'imprimée, au doublet GRAVITON (T↔Cotton) ?**

**Trois interdictions par construction :**
1. **mγ-3 / AdS-side** : S1/S2/S3 sont AdS₄/euclidiens. TOUT verdict (même
   POSITIF) reste côté AdS ; le transport vers le 𝓘⁺ dS spacelike = β
   (`G3-TRANSPORT`), STRICTEMENT hors scope. Aucun blanchiment de continuation.
2. **Anti-contamination** : le document externe de criblage (lu 2026-07-03,
   hors-KB) a fourni le ROUTAGE, pas les verdicts. Ses affirmations (« S²=−𝟙
   dans la version abélienne », « générateur CS marginal », « le −𝟙 vient de
   la quantification ») sont des HYPOTHÈSES À TESTER contre les sources
   primaires telles qu'imprimées — jamais des acquis.
3. **Non-surclassement anticipé** : même un POSITIF plein (P1 franchie côté
   AdS) ne construit PAS O₂ : P2 (+i) et β (transport) restent entiers ;
   aucune réduction du périmètre `{A4 ; A2★ ; N}` n'est atteignable par ce
   chaînon.

## 1. Cibles gelées `[espace de verdicts FIGÉ]`

**SP-1 — Existence et périmètre du S²=−𝟙 (PORTANTE).**
Telle qu'imprimée : chez Witten (S1), l'opération S est définie sur les CFT₃
à courant U(1) et satisfait S²=−𝟙 (élément central de SL(2,Z)) — VÉRIFIER le
niveau exact (action sur la théorie, sur les conditions de bord, sur le
doublet (J, J_dual)) et le statut du −𝟙 (démontré / conventionnel). Chez
Leigh-Petkou (S2) et de Haro (S3) : la version GRAVITONIQUE (doublet
T↔Cotton, {g₀, g₃}) porte-t-elle un S²=−𝟙 DÉMONTRÉ pour ce doublet, ou
hérité/conjecturé depuis le cas U(1) ? Issues : {démontré-graviton ;
hérité-U(1)-seul ; absent}.

**SP-2 — Générateur et niveau (quantification).**
Le générateur de la transformée de Legendre entre les deux quantifications
est-il, telle qu'imprimée, un terme de Chern-Simons GRAVITATIONNEL de bord
(d=3), marginal (Δ=d), et le −𝟙 est-il porté par la structure de
quantification (niveau k entier, appariement symplectique des données) plutôt
que par la géométrie conforme ? Recoupement gelé : cohérence exigée avec
`O2-HODGE` (source unique du −1 physique = i^{d-1} dS) — si S1/S2 exhibent un
−𝟙 AdS-side de nature quantificationnelle, consigner l'articulation
(deux −𝟙 distincts ? le même sous continuation ?) SANS l'adjuger ici.

**SP-3 — Le signe s=(−1)^w (cible b′ historique, INCHANGÉE).**
La réciprocité tensorielle de Penrose (S4, Ω̂Ω̌=−1, lois de transformation FG
de S3) fixe-t-elle la parité du poids conforme w du mode TT sous ω<0 ?
Trichotomie gelée de `O2-P1` : w impair ⟹ s=−1 (P=S possible) ; w pair ⟹
s=+1 (P≠S, discordance confirmée) ; indécidable sur pièces. Si SP-1/SP-2
fournissent le −𝟙 par une route indépendante de w, le consigner comme
BIFURCATION (le −𝟙 par quantification dispense-t-il de w impair ?) — à
trancher au verdict, pas au cadrage.

**SP-R — Firewall (mutations obligatoires au raisonnement, sceau si algèbre) :**
- m1 : anti-blanchiment AdS→dS (tout énoncé S1/S2/S3 reste AdS-side ; toute
  phrase du verdict qui transporterait vers dS sans β doit être cassée) ;
- m2 : anti-identification U(1)→graviton silencieuse (le S²=−𝟙 abélien ne
  vaut pour le doublet graviton QUE si imprimé pour lui) ;
- m3 : anti-contamination du crible (aucune cible reformulée d'après le
  document externe en cours de lecture) ;
- m4 : garde-fou signe scellé (C̃_T=+C_T, `CT-DUAL` §3) — tout résultat qui
  flipperait le signe de C_T par S doit être confronté au scellé, pas absorbé.

**Espace de verdicts FIGÉ (par cible et global) :**
{POSITIF-AdS (P1 franchie côté AdS, facteurs compris) ; PARTIEL-délimitation
(structure confirmée, −𝟙 non porté au graviton ou w non fixé) ; NÉGATIF
(discordance confirmée : P≠S même avec la couche SL(2,Z)) ;
INDÉTERMINÉ-fetch-gated (pièces insuffisantes)}.
Si POSITIF-AdS : portée > consolidation locale ⟹ **audit froid incognito
OBLIGATOIRE avant propagation** + sceau si algèbre exécutée.

## 2. Sources armées & discipline `[R-7 / R-41]`

- **S1** : Witten, *SL(2,Z) action on three-dimensional conformal field
  theories with abelian symmetry*, hep-th/0307041. NON consommée (grep 0).
- **S2** : Leigh-Petkou, dualité gravitationnelle AdS₄/CFT₃, hep-th/0309177.
  NON consommée (grep 0).
- **S3** : de Haro 0808.2054 — KB-locale, CONSOMMÉE (4 chaînons) ; re-lecture
  CIBLÉE seulement (S-map, lois FG, éq. 43-44/61-63/90) ; aucun re-gel.
- **S4** : Penrose, Cycles of Time — KB [LC-A] ; réciprocité conforme.
- Fetch web si nécessaire : identité R-41 multi-miroirs, grade
  identité-vérifiée consigné (précédent PRISMA/SCATTERING-FG) ; sha PDF si
  dépôt opérateur.
- TOUTE source hors S1-S4 = amendement R-7 daté AVANT consommation.
- Le présent cadrage VAUT amendement R-7 d'extension de la route b′
  (S1/S2 ajoutés à la liste historique {S4, lois FG de S3}).

## 3. Phases d'exécution `[sur GO séparés]`

- **Phase 0 (KB-only)** : relecture `O2-P1` (trichotomie w), `O2-HODGE`
  (transport du −1), `CT-DUAL`/`CT-DUAL-DS` (S²=−𝟙 niveau EOM, garde-fou
  signe), `JONCTION` §2 (Legendre D↔N). Zéro fetch.
- **Phase 1 (fetch R-7 daté)** : S1 puis S2, lecture contre SP-1..SP-3 SEULES.
- **Phase 2 (confrontation)** : verdict par cible dans l'espace figé ;
  chaînon `LC-D-O2-P1B-SOPERATION` ; sceau si et seulement si algèbre ;
  audit froid si POSITIF-AdS.

## 6.4. Non-surclassement `[terminal]`

Un POSITIF-AdS établirait P1 CÔTÉ AdS seulement : C-O2 resterait
conditionnelle au transport β (T-b) et à P2 (+i, choix non dérivé) ; O₂ non
construit ; D1 non clos. Un NÉGATIF confirmerait la discordance sans réduire.
`{A4 ; A2★ ; N}` INCHANGÉ quel que soit le verdict ; N non fixé (≡Λ) ;
CCC non démontrée NI réfutée.

## 7. Renvois

`LC-D-O2-P1` (s=+1, route b′) ; `LC-D-O2-HODGE` ; `LC-D-CT-DUAL` /
`CT-DUAL-DS` ; `LC-D-CT-REALITE` (i^{d-1}) ; `LC-D-O2-JONCTION` (C-O2) ;
`LC-D-O2-SCATTERING-FG` (prémisse {g₀,g₃} rigoureuse) ;
`LC-WORK-PORTRAIT-INTRANT-EXTERNE` §4 (crible, P-α) ;
hep-th/0307041 ; hep-th/0309177 ; 0808.2054 ; Cycles of Time [LC-A].
