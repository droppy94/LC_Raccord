# R-9 — REDÉMONSTRATION « module [B] : tracteur S², B-PAUVRE, résidu = Weyl rescalé » — rapport de lot (2026-07-22, S8)

Protocole §2.0 du lotissement, exécuté dans l'ordre.

## 0. Intrant et quarantaine

Archive `hors-KB_B_objet-sur-S2_TRANCHE-2026-07-18.zip` refournie par
l'opérateur en S8 ; sha256 vérifié AVANT extraction :
`b0ea7a7d4880f8b909518befe4b28d52fdd4774f373906385bd36b07dce5333f`,
14110 octets — concordant au registre S7. Extraction en quarantaine
hors dépôt (`/home/claude/S8/quarantaine-B/B/`) ; les 4 pièces
concordent au registre S7 (sha32, octets, lignes, 4/4). Corps des deux
têtes JAMAIS ouverts (RESULTAT l.14–230 ; PAQUET l.13–183).
`REIMPORT.txt` lu APRÈS le gel seulement (décision S7 close, tenue).
`verif_B_tracteur.py` jamais lu ; rejoué par exécution seule.

## 1. Gel de cible (étape 1)

`audit/R9-CIBLES-GELEES.md` — **sha256
7018b47efa8857c94afebeb48abe0435dec6550341383dcb7065a9f4bc4f91d1**,
2515 octets, figé 2026-07-22T19:33:16Z, AVANT la première ligne
d'instrument. 7 cibles (B1–B7) extraites des SEULS front-matters
(RESULTAT l.1–13 ; PAQUET l.1–12) + ligne R-9 du lotissement v0.1
(canal de révélation nommé). **Plafond E-2 annoncé AU GEL** (verdict
révélé par deux canaux ; REIMPORT.txt potentiellement guidant, différé
post-gel).

## 2. Redérivation (étape 2)

`instruments/redemo_R9_tracteur.py` — sympy, depuis les prémisses
nommées (S² = section conforme 2D de ℐ⁺ de genre espace [module A] ;
géométrie de Cartan conforme normale ; ambiant d=4). **16/16 PASS +
8 consignations, EXIT 0, premier passage sans correction
d'instrument.** Jambes redérivées de bout en bout :

- **A2** — métrique 2D GÉNÉRIQUE (E,F,G fonctions libres) :
  R_abcd = K(g_ac g_bd − g_ad g_bc) IDENTIQUEMENT (16/16 composantes)
  ⟹ le Riemann 2D est pure courbure scalaire, aucun invariant conforme
  local ne survit — le cœur algébrique du verdict ;
- **A3** — comptage du Weyl f(n)=n(n+1)(n+2)(n−3)/12 : f(3)=0,
  f(4)=10 ⟹ tout « Weyl » sur S² est une donnée AMBIANTE ;
- **A4** — ronde explicite : K[4/(1+r²)²δ]=1 EXACT (stéréographique) ;
- **A5** — Cotton[e^{2φ}δ₃]=0, 27/27 composantes, sur une famille à
  3 paramètres à troisièmes dérivées non triviales (jambe C de Ω=W⊕C) ;
- **A6** — FIREWALL : Cotton[Nil]≠0 avec R=−1/2 constant — recoupe
  R-7/Q6, redérivé indépendamment ici ; la nullité d'A5 n'est pas une
  vacance ;
- **A7** — les deux jambes nulles sur la classe plate (A4) ⟹ Ω^𝒯=0,
  géométrie de Cartan PLATE ⟹ **B-PAUVRE** au sens « zéro invariant
  conforme local intrinsèque » ;
- **A8** — durcissement : A2 étant générique (aucune rondeur utilisée),
  toute section perturbée reste couverte ; firewall dimensionnel : en
  4D le même argument CASSE (f(4)=10) ;
- **A9** — cohérence du résidu : intrinsèque nul ∧ Weyl ambiant
  existant ⟹ tout contenu non trivial est ambiant-restreint, conforme
  à « résidu localisé = Weyl rescalé ».

**Harnais de mutation : 6/6 MORDANTES** (`instruments/harnais_R9.py`),
chaque mutation frappant le porteur identifié de sa cible (m1 rang ;
m2 coefficient de section 2D ; m3 comptage Weyl ; m4 facteur rond ;
m5 coefficient de Schouten n=3 ; m6 témoin Nil). Aucune vacante.

## 3. Sceau (étape 3) — rejoué

| sceau | provenance | sha8 | issue |
|---|---|---|---|
| verif_B_tracteur.py | archive hors-KB (quarantaine) | 8e386686 | rc=0 |

Sha8 concordant au registre S7. Sa ligne de bilan (sortie d'exécution,
code non lu) déclare : Weyl(dS)=0 ∧ Cotton(dS)=0 ⟹ tracteur PLAT ;
Weyl(SdS)≠0 ⟹ résidu transportable = Weyl rescalé ; fibre 2D ⟹ aucun
invariant intrinsèque — **convergente avec la redérivation aveugle**.

## 4. Réconciliation — consignations de fond

- **(a) Témoin du résidu non redérivé.** Le sceau porte un témoin
  Schwarzschild–de Sitter (Weyl(SdS)≠0) que l'instrument S8 n'a pas
  redérivé ; A9 n'établit que la COHÉRENCE (résidu nécessairement
  ambiant), la valeur s'appuyant sur le recoupement R-7/Q4. B3 est
  cohérent et recoupé, PAS redémontré en substance.
- **(b) Critère non confronté.** « B-PAUVRE au sens strict du
  critère » : le critère vit au corps NON OUVERT ; lu ici comme « zéro
  invariant local ». REIMPORT.txt (post-gel) confirme la nuance : le
  déclencheur (a) de réouverture distingue « connexion plate » de
  « connexion sans champ propre mais organisatrice de donnée libre —
  le cas réellement trouvé ». La lecture S8 est compatible mais non
  identique au libellé du corps.
- **(c) Import structurel.** La décomposition Ω^𝒯 = Weyl ⊕ Cotton
  (BEG/Čap–Gover) est un IMPORT ; seules ses deux jambes sont
  redérivées. Même statut que Friedrich en R-1.
- **(d) REIMPORT.txt post-gel.** Identifie le résidu à g₍₃₎ (cohérent
  avec la donnée libre de Friedrich, R-5/P1) ; révèle que la tête
  portait déjà un TODO §7 « durcir grade borné → reproduit : Ω^𝒯
  composante-à-composante sur dS perturbé portant g₍₃₎ » — la
  robustesse B7 redérivée en A8 (générique 2D) est plus faible que ce
  TODO ; consigné, non exécuté (il exigerait le corps).
- **(e) V98 non confronté.** Le contenu exact du durcissement V98 vit
  au corps ; A8 n'en redérive que le mécanisme dimensionnel.

## 5. Grade (étape 4)

**REPRODUIT-SOUS-RÉSERVE (E-2)** — plafond du gel atteint, non
dépassé. 7/7 cibles gelées couvertes (16 asserts + 8 consignations),
harnais 6/6 mordantes, sceau d'origine rejoué rc=0 sha8 concordant,
cinq consignations de fond. Issue conforme aux têtes ⟹ pas d'audit
froid déclenché (§2.0-5).

## 6. §6.4 — sans surclassement

« REPRODUIT-SOUS-RÉSERVE » = algèbre correcte + cibles couvertes, sous
hypothèses explicites et double révélation du verdict — JAMAIS « [B]
scellé », JAMAIS « le raccord établi ». B-PAUVRE = un constat de
PAUVRETÉ (l'objet intrinsèque est le modèle plat ; la charge bascule
vers l'ambiant/g₍₃₎ et vers [C]) — pas une brique de démonstration.
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos · N non fixé · O₂ non
construit · nœud (i) INDÉTERMINÉ (pas A) · CCC non démontrée NI
réfutée.
