# R-4b / R-5b — INSTRUCTION DU VERDICT CSE E-3 (2026-07-21)

Instruction des défauts nommés par `audit/CSE-R4R5-VERDICT.md`, sur GO
opérateur. Les instruments v1 (`redemo_R4_CT.py`,
`redemo_R5_reductions.py`) restent au dépôt tels quels (historique
jamais réécrit) ; les instruments amendés `redemo_R4_CT_b.py` et
`redemo_R5_reductions_b.py` les remplacent EN AVAL.

## Discipline amendée (leçon CSE, désormais opposable à tout lot R-n)

Deux issues dans le harnais : **PASS** (assert discriminant — calcule,
et une mutation le fait échouer) et **CONSIGNATION** (déclaration
importée, triviale ou non dérivable — imprimée, hors décompte). Le
décompte final n'agrège QUE les PASS. Aucune disjonction rendant un
assert infaillible. Les docstrings ne revendiquent plus « redérivation
indépendante » : statut déclaré **REPRODUCTION GUIDÉE**.

## Table d'instruction — R-4 (prioritaire)

| défaut CSE (verdict) | instruction appliquée (R-4b) | issue |
|---|---|---|
| T9 « invariance s=±1 » : s mort (s·0), Abs(−x)=Abs(x) | s VIVANT : F=δr+i·s·F_im, 𝒫(s=+1)=𝒫(s=−1) par substitution ; firewall : sans le module, la mutation mord | PASS ×3 |
| « C_T_signé porte δr » : expression fabriquée | NON DÉRIVABLE depuis les prémisses de l'instrument — assert retiré, cible requalifiée consignation reportée (instruction au niveau tête si réouverture) | CONSIGNATION |
| T8-signé : −x+x=0 (CT_prog posé par fiat) | chaîne dérivée : C_T^dH=ℓ²/κ² calculé → γ=n²\|_{n=2}=4 dérivé de la carte → C_T^prog=C_T^dH/γ=N/(32π²) DÉRIVÉ → C_T_signé=i²·C_T^prog=−N/(32π²) ; firewall d=4 non réel | PASS ×3 |
| « N_action=γ/4 » : 1==1, objet inexistant | définition importée du gel, DÉCLARÉE consignation ; valeurs calculées sur γ dérivé (1 canonique, 1/4 nu) consignées | CONSIGNATION |
| « γ ∉ 𝒫 » : littéral True | testé sur les EXPRESSIONS (free_symbols de 𝒫_holo et 𝒫_canon) ; firewall : une 𝒫 contaminée échoue au prédicat | PASS ×2 |
| « C̃_T/C_T=+1 » : x/x=1, localisation non testée | LOCALISATION testée par substitution ℓ→iℓ sur C_T=K·ℓ^{d−1}/κ² pour d=2,3,4 (facteur=i^{d−1}) ; firewall : attaché à κ², facteur −i≠i² ; le ratio devient corollaire consigné | PASS ×4 + CONSIGNATION |
| T13 « n=2 unique/FORCÉ » à démontrer ou dégrader | DÉGRADÉ : n=2 = convention Brown–York, prémisse nommée non démontrée ici ; firewall n=1 conservé (valeur distincte) | CONSIGNATION + PASS |
| ratio dH/prog=4 « posé par fiat » (contenu mince) | absorbé par la chaîne dérivée ci-dessus (le 4 EST γ dérivé) | PASS |
| S²=−𝟙, vp ±i (arithmétique triviale) | requalifié consignation, vérifié hors décompte | CONSIGNATION |

Résultat R-4b : **35/35 PASS discriminants + 5 consignations déclarées,
EXIT 0** (v1 : 32 « PASS » dont ≈17 discriminants selon le CSE).

## Table d'instruction — R-5 (second)

| défaut CSE (verdict) | instruction appliquée (R-5b) | issue |
|---|---|---|
| P5-#13 « résidu = 1 nombre » : A·k³/k³, paraphrase | assert retiré ; théorème de caractérisation gaussienne DÉCLARÉ prémisse importée (non testable par free_symbols) ; l'identification #14 (calculée) conservée | CONSIGNATION + PASS |
| P6-#16 : disjonction infaillible (or vacant) | assert retiré ; remplacé par un calcul d'ÉLIMINATION indépendant : (H/M_Pl)²=8π²/N (solve, solution unique) ⟹ A_T(N)=16/N exactement, free_symbols={N} ; firewall coefficient muté | PASS ×3 |
| 4 check(True) littéraux | « A4⟹⟨g₃⟩=0 » → consignation (trivial) ; « inclusion STRICTE » → consignation portée par les 2 PASS témoins ; « écart ≠ f(un-point) » → CALCULÉ (⟨g₃g₃⟩_connexe=\|a\|²V, m se cancelle ; firewall : le moment non connexe dépend de m) ; « RÉDUCTION PAS FERMETURE » → consignation §6.4 | 2 PASS + 3 CONSIGNATIONS |
| P7 set==set | retiré ; recombinaison déclarée DANS l'instrument (plus seulement au rapport) | CONSIGNATION |
| sonde auditeur : Π^TT discrimine (anisotrope≠0) | intégrée comme firewall permanent | PASS |

Résultat R-5b : **17/17 PASS discriminants + 5 consignations déclarées,
EXIT 0** (v1 : 18 « PASS » dont ≈9 discriminants selon le CSE).

## Traitement des 8 consignations mandatées

1. Décomptes-vitrines → seuls les PASS discriminants sont agrégés (fait,
   les deux instruments).
2. « REDÉRIVATION INDÉPENDANTE » en docstring → remplacé par
   « REPRODUCTION GUIDÉE », réserve et verdict cités (fait).
3. E-1 mort-né dans l'espace gelé → défaut de CONSTRUCTION D'ESPACE
   consigné, opposable : tout futur espace-verdict est vérifié contre
   les pièces du paquet avant gel (règle ajoutée à la leçon de méthode).
4. Nom de T9 surdéclarant → T9 réécrit avec s vivant (fait).
5. Disjonction P6-#16 → retirée, remplacée (fait).
6. R-5 §2 « P1–P6 redérivés de bout en bout » → INEXACT pour P5-#13 et
   P6-#16 v1 ; le rapport v1 n'est pas réécrit, la présente table fait
   foi en aval.
7. « Premier passage sans correction » présenté comme force → ne se
   présente plus ainsi ; les instruments _b sont un SECOND passage sous
   instruction, déclaré tel.
8. Réconciliation (a) « sans effet » affirmée non testée → l'invariance
   de la magnitude sous le signe est désormais TESTÉE (T9 : 𝒫(s=±1) par
   substitution + firewall) ; la représentation ±i de la carte S reste
   une convention consignée.

## Grade résultant — sans surclassement

Conformément au verdict (« après instruction, au mieux E-2 ») :
**R-4 et R-5 se lisent REPRODUIT-SOUS-RÉSERVE au sens E-2 —
reproduction guidée, valeur de corroboration faible.** JAMAIS E-1. La
réserve d'aveuglement demeure ; le correctif structurel (adjudicateur
externe) a fonctionné une fois et reste la règle pour les lots suivants :
R-3 et R-6 s'ouvriront sous la discipline amendée (gel nommant ce que le
front-matter révèle du mécanisme ; PASS/CONSIGNATION ; espace-verdict
vérifié contre pièces).

## §6.4

Instruire un verdict ne scelle, ne réduit, ne compte, ne démontre rien.
35+17 PASS n'« établissent » rien de plus que : algèbre correcte +
cibles reproduites SOUS GUIDAGE, hypothèses explicites.
{ A4 ; A2★ ; N } INCHANGÉ · D1 non clos · CCC non démontrée NI réfutée.
