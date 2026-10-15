---
id: RAPPORT-CA2
objet: audit adverse aveugle de NOTE-176 (CAL-F, execution)
date: 2026-10-15
pieces_lues: PROMPT-AVEUGLE-CA2.md, NOTE-176.md, cal_f.py, cal_f_sortie.txt, SOURCE-1311.0700-fulltext.txt (rien d'autre)
espace_de_travail: /tmp/claude-0/ca2/
scripts_ajoutes: /tmp/claude-0/ca2/ca2_tests.py (+ sortie ca2_tests_sortie.txt), /tmp/claude-0/ca2/ca2_t3b.py (+ sortie ca2_t3b_sortie.txt)
empreinte_cal_f: sha256 47fb1d46aae577d45b8fcde06e4cecf7c2294b34ed9562ebc68c5f849a45aa0b
---

# Rapport CA-2 : audit adverse de NOTE-176

## 0. Verdicts

| Tache | Objet | Verdict |
|---|---|---|
| E1 | Fidelite des citations (§1) | **Correction mineure**, plus une erreur de fond sur la combinaison (m²/3 − λ/18) |
| E2 | Script et resultats (1)-(4) | **Correct** pour l'implementation et les quatre resultats ; **interpretation a corriger** : le test est aveugle a la masse et ne calibre pas le critere de Friedrich |
| E3 | Obstruction Dirac = coefficient m/Ω, sans masse speciale | **Correct sur le fond** pour l'equation de matiere (et renforcable) ; argument de jauge du §5.2 **non demontre** ; formulation « au sens de Friedrich » a borner |
| E4 | Greffes G-CAL-a, G-D1-e, article v2.2 | G-CAL-a : **correction mineure** ; G-D1-e : **correction** (lecture (ii) juste, phrase sur (2.17) a reformuler) ; v2.2 : **non demontre** pour la clause « (2.17) ne requiert pas la Prop. 5(b) » et pour « veritable counterpart du theoreme 3.1 » |

Le point structurant de l'audit : la note teste (2.17) en **evaluant son second membre sur des solutions** (valeur sur couche, champ de test sur dS fixe), alors que le critere de Friedrich porte sur la **forme des seconds membres comme fonctions des inconnues rescalees**. La note enonce correctement ce critere au §1 (« Lecture »), puis ne l'applique pas aux §2-§4. Ces deux choses different, et la difference est mesurable (T1, T2, T3 ci-dessous).

```
critere de Friedrich (th. 3.1)            test de la note (cal_f.py)
---------------------------------         ---------------------------------
second membre F(inconnues; Omega)          valeur F(solution(eta); Omega)
contient-il Omega^-k, k>0 ?                presente-t-elle un pole en eta -> 0 ?
          |                                            |
   (m^2 - 2l/3) Omega^-2 psi^2 dOmega^g     homogene : 0 pour TOUTE masse (T1)
   (m^2 - 2l/3) Omega^-1 psi dpsi^g         inhomogene, m^2 != 2l/3, psi borne :
   present meme si psi = psi(tau) (T2)        s^(1/2) non lisse, pas de pole (T3)
```

## 1. E1 : fidelite des citations

Verifie contre SOURCE-1311.0700-fulltext.txt (lignes indiquees).

1. **(2.17)** (l. 879-892) : « ∇_μ W^μ_ρνλ = 2 Ω^-1 ∇̂_[ν L̂_λ]ρ ». Fidele. La relation « ∇̂_ρ L̂_μν = (κ/2) ∇̂_ρ(T̂_μν − (1/3) T̂ ĝ_μν) » (l. 908-930) : fidele. Les chapeaux designent bien la metrique physique ĝ (l. ~600 : g = Ω² ĝ, ĝ solution d'Einstein (2.1)). « T*_ρμ = T̂_ρμ − (1/4) T̂ ĝ_ρμ » (l. 894-907) : fidele. Homonymie avec T* ≡ Ω^-2 T̂ de (3.7) (l. 1257-1272) : reelle.
2. **(3.11)** (l. 1371-1397) : « □_g ψ − (1/6) R ψ = Ω^-2 (m² − (2/3) λ) ψ + (κ/6) T* ψ + 4 ψ³ U(Ωψ) + Ω ψ⁴ U′(Ωψ) », ψ = Ω^-1 φ, et la phrase « Its most conspicuous feature, however, is the first term on the right hand side, which is singular where Ω → 0 » (l. 1402-1404) : fidele. Precision utile absente de la note : (3.11) suppose μ = 0 (terme 3μΩ^-1ψ² de (3.5) ecarte, l. 1223-1235).
3. **Theoreme 3.1** (l. 1406-1433). Le texte est : « If and only if the single condition m² = (2/3) λ, (3.13) is satisfied this system is regular in the sense that on the right hand sides of the equations no terms of the form Ω^-k, k > 0, occur and the right hand sides are in fact smooth function of the unknowns. » La note **inverse l'ordre** des fragments (« is regular [...] If and only if ») et **ampute** la seconde clause (« the right hand sides are in fact smooth function of the unknowns »). Le sens global est preserve, mais la clause amputee est precisement celle qui dit que le critere porte sur les seconds membres **comme fonctions des inconnues**, ce qui est le point manque aux §2-§4. Correction mineure de citation, consequence non mineure.
4. **Systeme couple entier, equation de matiere comprise** : exact. L'enonce liste (2.13)-(2.19) et (3.11) pour les inconnues (3.12) qui incluent ψ ; la preuve commence par « (3.13) renders equation (3.11) regular » (l. 1452). L'introduction le confirme : « the singular terms occur in the scalar field equation as well as in the geometric background equations always in the form (m² − (2/3)λ) Ω^-k, k = 1, 2 ». L'affirmation de la note (« la singularite du scalaire est **d'abord** dans l'equation de matiere ») est une lecture defendable (Friedrich met (3.11) en avant), mais « d'abord » n'est pas dans la source : les termes singuliers sont **aussi** dans (2.16)-(2.17), sans hierarchie.
5. **« Critical are equations (2.16), (2.17) »** (l. 1531) : fidele. **Mais** « ou les termes en Ω^-1 se combinent en multiples de (m²/3 − λ/18) » est **faux**. Le facteur (m²/3 − λ/18) n'apparait que dans des termes intermediaires (developpement de −(1/12)∇_[ρT* g_μ]ν et de −(1/6)T*∇_[ρΩ g_μ]ν). La combinaison finale (3.16) est (κ/2)·(1/3)(m² − 2λ/3)·[...]. Verification : λ/6 + (m²/3 − λ/18) − λ/3 = m²/3 − 2λ/9 = (1/3)(m² − 2λ/3). Or m²/3 − λ/18 s'annule en m² = λ/6, pas au point de Friedrich. Erreur de transcription sur la quantite meme qui porte le theoreme.

Verdict E1 : **correction mineure** (citations fideles a deux defauts pres), **avec une erreur de fond au point 5** a corriger avant toute greffe.

## 2. E2 : le script

### 2.1 Execution
`python3 cal_f.py` dans /tmp/claude-0/ca2/ : sortie **identique octet pour octet** a cal_f_sortie.txt (diff vide).

### 2.2 Implementation
- Christoffel de ĝ = η^-2 diag(−1,1,1,1) : calcul direct, correct. `cov(T,a,b,c)` = ∇_c T_ab, correct.
- S = (∇_ν L̂_λρ − ∇_λ L̂_νρ)/Ω = 2Ω^-1 ∇̂_[ν L̂_λ]ρ avec Ω = −η > 0 et g = Ω²ĝ = η_M : conforme a (2.17).
- L̂ = (κ/2)(T̂ − T̂ ĝ/3) : correct ; omission de (λ/6)ĝ legitime (∇̂ĝ = 0, et c'est exactement l'argument de Friedrich l. 1563-1570).
- Fluide : u_η = 1/η, norme −1, futur-dirige : correct (la ligne 50 est une affectation morte ecrasee par la ligne 51, sans effet).
- Klein-Gordon homogene : □h = −η²h″ + 2ηh′, d'ou h″ = (2/η)h′ − m²h/η² : correct (signature −+++, (3.1) de la source).
- Conservation en temps conforme ρ′ = 3(ρ+p)/η (a = −1/η) : correct.
- Derivation analytique du §2.1 (L̂ = A uu + B ĝ, ∇̂_[νL̂_λ]ρ = −(AH + Ḃ) u_[ν h_λ]ρ, A = κ(ρ+p)/2, B = κρ/6) : verifiee a la main, correcte.

### 2.3 Resultats (1)-(4)
Tous **justes** tels qu'enonces. Deux reserves d'interpretation :

- (2) et (4) sont des **cas particuliers de (1)** : un scalaire homogene sur couche et une poussiere ρ ∝ a^-3 sont des fluides homogenes isotropes conserves. Ils n'apportent pas d'information independante.
- « Reflet de la platitude conforme de FLRW (W = 0) » : le calcul est un champ de test sur dS fixe, pas un FLRW couple. La nullite vient de la conservation plus la symetrie, comme le montre la derivation analytique. Heuristique acceptable, pas une justification.

### 2.4 Tests complementaires (copie modifiee, /tmp/claude-0/ca2/ca2_tests.py et ca2_t3b.py)

**T1. Le test homogene est aveugle a la masse.** Hors couche, pour toute masse m : S_(i,0,i) = −(κ/6η) · h′ · (h″ − 2h′/η + m²h/η²). La source de (2.17) evaluee est donc l'equation de Klein-Gordon multipliee par h′ : nulle sur couche **pour toute masse**, au point de Friedrich comme ailleurs. Un instrument qui rend la meme reponse au point regulier et aux points singuliers ne calibre pas la detection de la singularite.

**T2. Le terme singulier formel de Friedrich existe pour une configuration homogene.** Partie singuliere de (3.16), (κ/6)(m² − 2λ/3)[ψ ∇_[ρψ g_μ]ν + Ω^-1 ψ² ∇_[ρΩ g_μ]ν], evaluee sur la solution homogene de test m² = 35/16 (λ = 3), φ = s^(5/4) : non nulle, d'ordre s^(-1/2) dans ∇̂L̂, donc s^(-3/2) dans le second membre de (2.17). Au point m² = 2 : nulle (le facteur s'annule). La somme totale etant nulle sur couche (T1), ce terme singulier est **compense sur couche** par des termes « reguliers » de K (qui contiennent ∇∇ψ, lui-meme porteur de Ω^-2(m² − 2λ/3) via (3.11)). L'affirmation de la note « pour un scalaire homogene, (2.17) ne voit rien ; [...] pour un scalaire inhomogene, par les termes de (2.16)-(2.17) que Friedrich exhibe » est donc **fausse dans sa partie descriptive** : les termes singuliers de Friedrich ne demandent pas d'inhomogeneite ; c'est la **valeur sur couche** qui s'annule.

**T3. Champ inhomogene de test, h = f(η) cos kx.** Six composantes non nulles.
- m² = 2 (point de Friedrich), f = η(cos kη + sin kη), solution exacte : toutes les composantes sont **O(1)**, regulieres en s → 0. Ceci est une vraie calibration positive, coherente avec le theoreme 3.1 ; la note ne l'a pas faite.
- m² = 35/16 (ψ ~ Ω^(1/4), borne mais non lisse) : S ~ **s^(1/2)**, sans pole. L'irregularite au sens de Friedrich se manifeste sur couche par une **perte de lissite** (puissances fractionnaires), pas par un pole.
- m² = 0 (ψ ~ Ω^-1, inconnue elle-meme singuliere) : poles s^-2 et s^-1.

Consequence : chercher un **pole** dans la valeur sur couche de (2.17) n'est ni necessaire ni suffisant pour diagnostiquer l'irregularite au sens de Friedrich. Cela touche la « regle de comptage » de NOTE-163 au-dela de ce que dit la note (non seulement imprecise, mais formulee sur le mauvais objet si elle vise le critere de Friedrich).

**Ce que les pieces ne permettent pas de verifier** : l'affirmation « l'implementation du corpus (irr_c.py) est correcte » et « le pole de G-V3 a ete etabli par calcul covariant explicite ». cal_f.py est un script distinct ; seule sa propre implementation est validee ici.

Verdict E2 : **correct** (implementation et resultats (1)-(4)) ; **non demontre** pour la portee « la calibration reussit » au-dela de cal_f.py ; interpretation des resultats (2)-(4) a corriger (T1, T2).

## 3. E3 : l'obstruction Dirac

### 3.1 Ce qui est correct
- Avec le poids conforme standard ψ̂ = Ω^-3/2 ψ, l'operateur de Dirac sans masse est conformement covariant et le terme de masse devient m/Ω : l'equation rescalee porte un coefficient d'ordre Ω^-1 de residu m. Exact.
- Pas de masse constante speciale **en couplage minimal** : le seul terme d'ordre Ω^-1 est m/Ω · Id ; aucune contribution de courbure de meme ordre n'apparait dans l'operateur du premier ordre. Pour le scalaire, la masse speciale vient de la competition entre m² et le terme R/6 (via (2.2) : R̂ = 4λ − κT̂) ; le spineur n'a pas d'homologue. L'extension aux couplages non minimaux s'appuie sur le « Lemme 2 de l'article », absent des pieces : non verifiable ici.

### 3.2 Renforcement (T4)
Mode homogene : i γ⁰ ∂_η ψ̂ = (m/Ω) ψ̂ donne ψ̂ ∝ Ω^(±i m/H). Exposants indiciels ±im/H, jamais entiers pour m ≠ 0 : les solutions generiques sont bornees mais **non lisses** en Ω = 0 (derivee ~ Ω^-1). Le mode k ≠ 0 a le meme comportement dominant (terme en k sous-dominant d'un facteur Ω). Il en decoule un argument plus fort que celui de la note : **aucune redefinition lisse et inversible des inconnues** ne peut rendre l'equation reguliere au sens de Friedrich, car un systeme lineaire symetrique hyperbolique a coefficients lisses a travers Ω = 0 aurait des solutions lisses pour des donnees lisses. Les redefinitions qui suppriment le pole (par exemple χ = exp(i (m/H) γ⁰ ln Ω) ψ̂) introduisent des coefficients log-oscillants, non lisses : elles deplacent l'obstruction sans la lever.

### 3.3 Ce qui est non demontre ou surdimensionne
- **§5.2, jauge λ = (m/H) ln Ω** : une phase U(1) vectorielle ψ̂ = e^{iλ}χ produit un terme −γ^μ ∂_μλ χ, proportionnel a une matrice γ (de trace nulle), alors que le terme de masse est proportionnel a l'identite. Il ne peut pas l'absorber. L'enonce « deplace le coefficient singulier dans le potentiel (A_η ~ 1/Ω) » renvoie a la Prop. 2 de l'article, absente des pieces, et ne se verifie pas par le calcul elementaire. Non demontre ; a remplacer par l'argument du §3.2.
- **« analogue spin 1/2 exact du premier terme de (3.11) »** : « exact » est trop fort. Le scalaire a un terme Ω^-2 dans une equation du second ordre, qui s'annule pour une masse non nulle ; le spineur a un terme Ω^-1 dans une equation du premier ordre, qui ne s'annule que pour m = 0. L'analogie est structurelle (exposants indiciels), pas exacte.
- **« au sens de Friedrich »** : le theoreme 3.1 ne traite que le scalaire (Friedrich : « other fields could be considered as well »). Il s'agit du **critere de Friedrich transpose**, avec un choix d'inconnues (poids 3/2) qui est celui de la note. Pour le systeme Einstein-Dirac couple, la regularite de (2.13)-(2.17) n'est pas etablie ; la note le declare ouvert, ce qui est correct, mais le verdict du §0 et G-D1-e parlent de « l'obstruction au sens de Friedrich » sans cette borne.
- **Identification « gaz de Dirac homogene = poussiere conservee »** : vraie pour une moyenne isotrope de particules au repos ; pour un mode classique unique, l'isotropie du tenseur energie-impulsion n'est pas montree dans les pieces. Mineur.

Verdict E3 : **correct sur le fond et proportionne pour l'equation de matiere**, a condition de dire « critere de Friedrich transpose a l'equation de Dirac » ; l'argument anti-redefinition du §5.2 est **non demontre** et doit etre remplace par l'argument de non-lissite (§3.2), qui repond a la question « une redefinition l'eviterait-elle ? » par la negative pour toute redefinition lisse.

## 4. E4 : les greffes

**G-CAL-a (NOTE-163, ligne Comptage).** Direction juste (le resume « pole ssi p = 1 » est trop fort). Deux corrections :
- « pole possible seulement si p ≤ 1 » est encore une regle de comptage generique, non demontree par CAL-F ;
- la clause « sources homogenes isotropes conservees : contribution nulle » doit preciser « valeur sur couche, pour toute masse, donc sans pouvoir discriminant pour la regularite au sens de Friedrich » (T1).
- « G-V3 inchange » et « etabli par calcul covariant explicite (irr_c.py, NOTE-128) » : non verifiable avec les pieces ; la greffe peut le reprendre a titre de renvoi, pas comme acquis de CAL-F.
Verdict : **correction mineure**.

**G-D1-e (S26-02 v2 §7).** La structure a deux lectures est justifiee, et la lecture (ii) (coefficient m/Ω de l'equation rescalee, sans masse speciale) l'est aussi, sous la borne « critere transpose, equation de matiere seulement ». La phrase « (2.17) ne voit pas une poussiere homogene » confond valeur sur couche et regularite formelle : la reformuler en « la valeur sur couche du second membre de (2.17) est nulle pour toute source homogene isotrope conservee, quelle que soit la masse ; la regularite formelle de (2.16)-(2.17) pour Einstein-Dirac n'est pas etablie ». « RG-4 reste declenchee sous les deux lectures » : justifie pour (i), justifie pour (ii) au niveau de l'equation de matiere. Verdict : **correction** (moderee).

**Article v2.2.** « La condition pertinente est la Prop. 4(c) (coefficient lisse) » : acceptable pour l'equation de matiere. « C'est la le veritable counterpart spin 1/2 du theoreme 3.1 » : **surdimensionne**, le theoreme 3.1 porte sur le systeme couple et seule la partie matiere est transposee. « La Prop. 5(b) (tenseur rescale borne) est un critere distinct, que (2.17) ne requiert pas pour une source homogene » : **non demontre**, et fonde sur le test aveugle a la masse (T1). Que la regularite formelle de (2.13)-(2.17) exige ou non une borne sur le tenseur rescale est precisement le point ouvert du §3 de la note. Verdict : **non demontre** pour ces deux clauses ; a retirer ou a marquer conjectural.

## 5. Erreurs par gravite

**Graves (affectent les conclusions ou les greffes)**
1. Confusion entre **valeur sur couche** du second membre de (2.17) et **regularite formelle** des seconds membres en fonction des inconnues (le critere du theoreme 3.1, que la note enonce pourtant au §1). Elle porte la phrase de G-D1-e « (2.17) ne voit pas une poussiere homogene » et la clause v2.2 « Prop. 5(b) [...] que (2.17) ne requiert pas ».
2. La « calibration reussit » est surevaluee : le test homogene est **aveugle a la masse** (T1 : S ∝ h′ · KG pour tout m). Il valide la derivee covariante de cal_f.py, pas la capacite a detecter la singularite de Friedrich. La calibration positive pertinente (inhomogene, m² = 2, T3) n'a pas ete faite.

**Moyennes**
3. « termes en Ω^-1 se combinent en multiples de (m²/3 − λ/18) » : faux ; la combinaison de (3.16) est (1/3)(m² − 2λ/3).
4. « pour un scalaire inhomogene, [la singularite passe] par les termes de (2.16)-(2.17) que Friedrich exhibe » : faux ; ces termes existent pour des configurations homogenes (T2), seule leur somme sur couche s'annule.
5. Argument de jauge du §5.2 non demontre et contredit par le calcul elementaire (une phase U(1) n'absorbe pas un terme ∝ Id) ; l'argument correct est la non-lissite des solutions Ω^(±im/H).
6. « veritable counterpart spin 1/2 du theoreme 3.1 » et « obstruction au sens de Friedrich » sans la borne « critere transpose, equation de matiere seule ».

**Mineures**
7. Citation du theoreme 3.1 : ordre des fragments inverse, clause « smooth function of the unknowns » amputee.
8. « d'abord dans l'equation de matiere » : interpretation absente de la source.
9. « analogue spin 1/2 exact » : l'analogie est structurelle (Ω^-2 au second ordre contre Ω^-1 au premier ordre).
10. Resultats (2) et (4) presentes comme independants alors qu'ils sont des cas de (1) ; « reflet de la platitude conforme de FLRW » pour un champ de test sur dS fixe.
11. Hypothese μ = 0 de (3.11) non rappelee.
12. Identification gaz de Dirac homogene = poussiere conservee non justifiee dans les pieces pour un mode unique.
13. Ligne morte cal_f.py l. 50 (sans effet).

**Non verifiable avec les pieces autorisees** : correction d'irr_c.py, pole de G-V3 (NOTE-128), Lemme 2, Prop. 2, 4(c), 5(b) de l'article.
