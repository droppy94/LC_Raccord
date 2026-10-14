---
id: NOTE-BORD-EON-113-AUDIT-IR-g-CONCORDANCE
numero: 113
serie: I
branche: Q-M3 suite (audit IR-g)
reservation: 2026-10-11T15:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 113)
date: 2026-10-11
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-112-ARMEMENT-AUDIT-IR-g (sha256 43986f6fdd4831367cb1bddcf170ae4fcee5c9e825901ca76d6693346b370652, 2026-10-11T15:23:12Z)
rapport: RAPPORT-IR-g-AUDIT-AVEUGLE-Ja-Jb.md
depend: [NOTE-BORD-EON-112-ARMEMENT-AUDIT-IR-g, NOTE-BORD-EON-108-IR-g-EXECUTION]
verdict: "AU-V3 partiel (G5, seconde moitie) ; G1-G4 confirmes, G2 sous forme tensorielle"
prediction_realisee: "non (prediction AU-V2)"
suspend: "NOTE-108 : enonce G5 seconde moitie (§0, §3 qualification, §6 premier point) ; idem par report dans NOTE-102 v2 (greffe point 3), NOTE-106 v2 (greffe point 2), NOTE-109 §3"
rouvre_si:
  - "contre-exemple a la loi tensorielle hors partie homogene ou hors C-iso"
---

# NOTE-113 : audit froid aveugle de NOTE-108. Verdict **AU-V3 partiel**

## 0. Resume
La **loi** de NOTE-108 est confirmee par les deux auditeurs et renforcee. J-a l'a retrouvee seul par ajustement, sans qu'elle lui soit donnee. J-b l'a soumise a 11 configurations, sans contre-exemple. Elle s'ecrit sous forme **tensorielle**, hors diagonale comprise :

  R_isj |_{β ln s, s⁰} = (3βκ/e²) (Q_ij − ⅓ δ_ij tr Q),  Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺ (convention s = −τ),

et la trace de Q n'y entre pas. En revanche la conclusion physique G5 tombe pour moitie. J-b exhibe des champs coherents et polarises a Q = 0, donc sans log : une onde progressive a polarisation circulaire, une onde stationnaire helicoidale. Il exhibe aussi un faisceau anisotrope non polarise a Q = 0. L'enonce « la partie sans trace survit pour tout champ coherent polarise et ne s'annule que pour un ensemble isotrope non polarise » est **faux**. Le bon critere est ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf. Selon le gel (§3), c'est **AU-V3 partiel** : NOTE-108 est suspendue sur ce seul point, et la prediction AU-V2 n'est **pas** realisee.

## 1. Concordance

| Affirmation | J-a | J-b | Etat |
|---|---|---|---|
| G1 log de X^M = −2(T_B − T_E), Poynting sans log | identique (forme covariante 2Q̃ − δ tr Q̃, X_ss = −tr Q̃) | confirme a l'ordre s² ; β ln s oscillant en X_sx a s³ | **concordant, precise** (« a l'ordre s² ») |
| G2 loi 3βκ/e² Q_tf, trace sans effet | retrouvee par ajustement (α = 3, γ = 0), hors diagonale | 11 cas, hors diagonale, robuste a T̂ deforme, λ et C_r absents | **concordant, renforce** (forme tensorielle) |
| G3 coupure de source | facteurs ¼ ; terme en cos 2kD × (δ − k̂k̂) | facteurs ¼ ; terme dependant de D alimente aussi Q_tf ; x^−(n+2) pour n pair | **concordant, corrige** |
| G4 dipole (4/5)(mm − ⅓m²), isotrope nul | identique ((4/15)(3mm − m²δ)) | identique | **concordant** |
| G5 critere | premiere moitie confirmee | premiere moitie valide ; **seconde moitie invalide** (T7, T9, T11) | **discordance avec NOTE-108** |

## 2. Ce qui tombe et ce qui le remplace
- **Tombe** (NOTE-108 §0, §3 qualification, §6 premier point) : « Q_tf survit pour tout champ coherent polarise, quel que soit le rapport E/B ; il ne s'annule que pour un ensemble isotrope non polarise ».
- **Remplace par** : le ln de (2.17) est present si et seulement si ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺. Exemples :

| Configuration a 𝓘⁺ | Q_tf | ln dans (2.17) |
|---|---|---|
| reliquat magnetostatique (E = 0) | ≠ 0 | oui |
| dipole coherent rayonne | (4/5)(mm − ⅓m²) × … | oui |
| onde progressive lineaire ou elliptique | ≠ 0 (mesure la polarisation lineaire) | oui |
| onde progressive **circulaire** | 0 | **non** |
| onde stationnaire helicoidale a Q = 0 | 0 | non |
| faisceau anisotrope non polarise, E = B | 0 | non |
| ensemble isotrope (vide) | 0 | non |

- **Reste valide** : la dichotomie « dominante magnetique / E = B en module » n'est pas le critere (elle ne porte que sur tr Q) ; E = B en module ne suffit pas a supprimer le log (onde lineaire), mais ne l'interdit pas non plus.

## 3. Corrections mineures a porter sur NOTE-108
1. G1 : « exactement » devient « a l'ordre s² » (β ln s oscillant en X_sx a s³, de moyenne nulle).
2. G2 : ecrire la loi tensorielle ; fixer la convention (s = −τ ; en τ le signe change).
3. G3 : avec Q moyenne spatiale, facteurs ¼ ; le terme en cos 2kD contribue a Q_tf via (⅓𝟙 − k̂k̂) sauf distribution isotrope des k̂ ; decroissance x^−(n+2) pour n pair ; le poids spectral est celui de a²k².
4. Script : reference Q codee en diagonale (couverture comblee par l'audit) ; controle de trace tautologique ; code mort ligne 94.
5. Hypotheses de G5 (moitie valide) : partie homogene, C-iso, premier ordre en β, ordre s⁰ de R, Q pris a l'ordre zero au bord.

## 4. Report sur les autres notes
La phrase fausse a ete reprise ailleurs :
- NOTE-102 v2, greffe point 3 ;
- NOTE-106 v2, greffe point 2 (« survit pour tout champ coherent polarise ») ;
- NOTE-109 §3 (« present pour tout champ coherent polarise, absent pour un ensemble isotrope non polarise »).

Ces passages sont suspendus avec NOTE-108. NOTE-111 (loi locale, carte du dipole) n'est pas touchee : son enonce est local, le dipole a Q_tf ≠ 0, et localement Q_tf = 0 exige E = ±B paralleles. Une greffe de correction (IR-d''') est proposee ci-dessous, **non entee**.

## 5. Verdict
**AU-V3 partiel.** G1 a G4 confirmes (G2 renforcee en loi tensorielle) ; G5 seconde moitie invalide ; NOTE-108 suspendue sur ce point et maintenue pour le reste. Prediction du gel (AU-V2) **non realisee** : la reserve attendue portait sur la loi (fermeture, termes croises), alors que c'est la conclusion physique qui tombe.

## 6. Portee sur Q-M3 et CCC + M
- La condition de M-V3 devient : ⟨B_iB_j⟩_tf ≠ ⟨E_iE_j⟩_tf a 𝓘⁺ (et H-loc pour un champ localise, NOTE-111).
- Le ln Ω n'est plus « generique pour tout champ coherent polarise ». Il depend de la structure de polarisation et de la nature (stationnaire ou progressive) du champ a 𝓘⁺. Une source causale coherente de type dipole le produit ; une onde circulaire non.
- Rien n'est grave. RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange.

## 7. Greffes proposees (non entees)
- **IR-d'''** : corriger NOTE-108 (versions v2, §2 et §3 ci-dessus), et les passages repris dans NOTE-102 v2, NOTE-106 v2 et NOTE-109 (v3 ou addendum).
- **IR-l** : caracteriser la classe des champs d'origine causale a ⟨B_iB_j⟩_tf = ⟨E_iE_j⟩_tf (helicite, ondes progressives), et dire si une source causale generique y tombe.
- **IR-k** (rappel) : partie non Maxwell de la completion de Riegert pour une source localisee (teste H-loc).

## 8. Non-surclassement
[conv]. Audit froid conduit (AU-V3 partiel). Aucune incompatibilite gravee. Noyau inchange.
