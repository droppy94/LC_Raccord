---
id: NOTE-BORD-EON-142-AUDIT-IR-x-CONCORDANCE
numero: 142
serie: I
branche: Q-M3 suite (IR-x, audit)
reservation: 2026-10-12T13:22 UTC (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 142)
date: 2026-10-12
programme: LC-RACCORD
grade: "[conv]"
gel: NOTE-BORD-EON-141-ARMEMENT-AUDIT-IR-x (sha256 35af1520a84ccdb175074bce9d3c190f79c6c032a44d179a1861599b966469aa, sceau 2026-10-12T13:23:14Z)
rapports:
  - "audit_irxa/RAPPORT-IR-x-XA1.md, sha256 482220e3f4500b7a637b16b70652ae1ecf93f14770d5010e957b7632838e591d (derivation aveugle de la question d'EDP)"
  - "audit_irxa/RAPPORT-IR-x-XA2.md, sha256 e8647942b05a0ebdd511db9e7fac023521f4db0f9a491d50dfdfc731a0967163 (audit du script et contre-exemples)"
objet: [NOTE-BORD-EON-140-IR-x-EXECUTION]
verdict: "XA-V2"
prediction_realisee: "oui pour le verdict ; deux points de detail non realises (§5)"
rouvre_si:
  - "version purement ponctuelle sans domination locale (non tranchee par XA-1)"
---

# NOTE-142 : concordance de l'audit froid court de NOTE-140. Conclusion confirmee, argument a reformuler, ensembles exceptionnels elargis. Verdict **XA-V2**

## 0. Resume
- **x-3 confirme deux fois** : c_n = 0 pour tous les n (XA-1 jusqu'a n = 8, XA-2 jusqu'a n = 11 et par recurrence exacte pour tout n), y compris avec puissances non entieres s^μ et ln² s (XA-2).
- **Argument general reformule et renforce** (XA-1) : le bon resultat n'est pas la « propagation des singularites » mais le **probleme de Cauchy hyperbolique** (Garding) joint a l'**unicite de Holmgren** : toute solution distributionnelle sur une tranche (0, ε) × Ω se prolonge en fonction C^∞ de s a travers s = 0, a valeurs distributions. **Aucune hypothese de croissance temperee n'est necessaire** ; les hyperfonctions n'echappent pas non plus.
- **x-2 confirme** (XA-2), avec une precision : l'absence de pole hors du sommet est structurelle (vraie pour tout T lisse), donc le test ne sonde que la regularite de φ au point choisi ; R ~ σ⁻³ sur le cone en direction generique (24 composantes).
- **Ensembles exceptionnels elargis** (XA-1, XA-2) : un comportement en ln s (et un R en s⁻¹) est possible ponctuellement sur des **points** (sommets sur le bord), des **2-spheres** (cone de sommet au-dela du bord qui traverse s = 0), des **2-plans** (superposition plane de sommets), et des unions denombrables (eventuellement denses) ; toujours d'interieur vide, de mesure nulle, et nul au sens des distributions.

## 1. Confrontation aux criteres (figes, NOTE-141 §2)
| Critere | Resultat | Statut |
|---|---|---|
| **C-1 (x-3)** | XA-1 : c₀..c₈ = 0 ; XA-2 : c₀..c₁₁ = 0, recurrence P(m)c_m − 2(m−2)(m−3)Δc_{m−2} + Δ²c_{m−4} = 0 avec P(m) ≠ 0 [calcule par les auditeurs] | **satisfait** |
| **C-2 (argument general)** | XA-1 : Cauchy hyperbolique (Garding) + Holmgren (+ regularite normale, Hormander) ; u ∈ C^∞([−δ, s₁], D') sans hypothese de croissance [derive + cite de memoire par l'auditeur] | **satisfait, mais avec un theoreme different de celui de NOTE-140** |
| **C-3 (x-2)** | XA-2 : pas de 1/s hors sommet (deux points, parametres symboliques) ; e⁻³ sur le cone en direction generique | **satisfait** |
| **C-4 (contre-exemples)** | aucun ln s ni pole sur un ouvert ; exceptions : points, spheres, plans, unions denombrables, toutes de mesure nulle | **satisfait** |

## 2. Points de detail [rapporte]
### 2.1 XA-1
- Propagateur explicite de □² : K̂(s, k) = (sin ks − ks cos ks)/(2k³), entier en s ; dans l'espace physique, K(s) = sgn(s) 1_{|x|<|s|}/(8π).
- Solutions de cone : solutions distributionnelles de □² sur R⁴ prive du sommet (via σ + i0). Sommet decale en s = −s₀ : intersection transverse avec s = 0 sur la sphere r = s₀ ; ln |σ′| = ln s + ln(s + 2s₀) : un ln |s| des deux cotes, trace d'un front nul qui traverse le bord, non un phenomene de bord.
- Superposition denombrable dense Σ 2^{−j} ln |σ_j| : ln s ponctuel sur un ensemble dense, invisible aux fonctions test ; coefficient distributionnel nul.
- Contraste : un ln s generique exigerait un operateur fuchsien en s = 0 (exemple d'Euler-Poisson-Darboux) ou un bord caracteristique ; ni l'un ni l'autre ici.
- Reste ouvert : la version purement ponctuelle sans domination locale (pathologique, aucun exemple connu).

### 2.2 XA-2
- Script conforme (empreinte), reexecution identique octet pour octet.
- Defauts mineurs : test x-2 non discriminant par construction ; droite symetrique et A = 0 pour l'ordre au cone ; conclusion automatique de x-3 limitee a c₀..c₄ (resultat imprime juste) ; `coeff(s, 0)` ignore les termes s⁰ ln s (inoffensif ici).
- Sommet hors du bord : R en s⁻¹ sur la sphere r = s₀, homogene de degre −1 en la distance au coin (σ⁻³ attenue par C = O(s) et par T̂ = s²T / Ω).
- Superposition plane de 1/σ (valeur principale) : φ = −π ln |z² − s²| ; sur le plan z = 0, φ = −2π ln s exactement et R ~ s⁻¹ ; hors du plan, regulier.

## 3. Lecture [derive]
1. La conclusion de NOTE-140 (pas de compensation du pole hors d'un ensemble de mesure nulle, quel que soit l'etat) **tient et se renforce** : elle vaut pour toute solution distributionnelle, sans hypothese de croissance, et au sens des distributions l'ensemble exceptionnel est vide.
2. L'enonce de NOTE-140 §2.1 (« propagation des singularites ») est **imprecis** : la propagation du front d'onde est un enonce interieur ; le resultat pertinent est le prolongement a travers une hypersurface non caracteristique d'un operateur hyperbolique (Cauchy + Holmgren).
3. La phrase de NOTE-140 « ln s qu'aux sommets, points isoles » est **trop etroite** : les exceptions comprennent aussi des spheres (fronts nuls traversant le bord) et des plans (superpositions), toujours de mesure nulle. Avec un poids ajuste, une superposition plane pourrait compenser le pole **sur ce plan** ; jamais sur un ouvert.

```
   ensembles de scri+ ou un ln s ponctuel est possible (solution homogene)

   sommet sur le bord        -> point
   cone venant d'au-dela     -> 2-sphere (front nul transverse)
   superposition plane       -> 2-plan
   superposition denombrable -> ensemble dense d'interieur vide
   au sens des distributions -> vide (Cauchy hyperbolique + Holmgren)
```

## 4. Verdict
**XA-V2.** C-1 a C-4 satisfaits. Conclusion de NOTE-140 inchangee et renforcee. Corrections de redaction a porter en v2 : (i) remplacer l'argument de propagation des singularites par Cauchy hyperbolique + Holmgren, sans hypothese de croissance ; (ii) elargir l'ensemble exceptionnel (points, spheres, plans, unions denombrables ; vide au sens des distributions) ; (iii) noter le caractere structurel de x-2.

## 5. Confrontation a la prediction
Prediction (NOTE-141 §4) : XA-V2 [**realise**] ; reformulation de l'argument [**realise**, mais vers un theoreme plus fort que celui predit : la regularite normale temperee n'est pas necessaire, l'hyperbolicite suffit] ; spheres pour sommets hors du bord [**realise**, plus les plans et les unions denombrables] ; classes non temperees ou hyperfonctions echappant formellement [**non realise** : XA-1 les exclut aussi].

## 6. Consequences
- **Greffe** proposee : NOTE-140 v2 avec greffe encadree (§4 i a iii), par acte, sur decision de l'operateur.
- La classe de G-V3 (NOTE-140 §5) est confirmee : « WZ integrable + Γ[g] etat regulier », sans condition sur φ_h.
- RG-4 inchangee. Noyau {A4 ; A2★ ; N} inchange. G-V3 et M-V3 candidats non graves.

## 7. Pistes
- Acte d'entree de la greffe NOTE-140 v2.
- IR-y : regularite de Γ[g] en 𝓘⁺ pour un etat Hadamard non regulier en 𝓘⁺ (seule hypothese d'etat restante).
- Lecture de Foraci-Woodard 2501.01972, sous gel.

## 8. Non-surclassement
[conv]. Audit par agents isoles du meme systeme ; theoremes cites de memoire par l'auditeur, numeros non certifies.
