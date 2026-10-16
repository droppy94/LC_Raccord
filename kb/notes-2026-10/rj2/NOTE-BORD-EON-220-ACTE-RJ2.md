---
id: NOTE-BORD-EON-220-ACTE-RJ2
numero: 220
serie: I
branche: Chantier D (chantier RJ, second etage)
reservation: 2026-10-16T16:37:05Z (REGISTRE-CENTRAL-NUMEROS-NOTES, ligne 220)
date: 2026-10-16
programme: LC-RACCORD
grade: "[conv]"
borne_par: "NOTE-BORD-EON-219-AUDIT-RJ2-CONCORDANCE.md (AU-V3 ; §7 re-audit RB-3 ; sha256 be5b60fa19b47d70)"
decision: "operateur (Thierry), 2026-10-16 : « Enter la v2 »"
---

# Acte d'entee RJ2

## 1. Greffe
- **G-RJ2** : NOTE-217 v2 (sha256 `78ec0038d3d770fb`), corrections E1 a E3, C1 a C9 de NOTE-219, puis K1, K2, M1 du re-audit RB-3 ; v1 conservee (`9fdf5d619104418d`), non entee. Scripts : v1 (rj2_lemmes.py, rj2_series.py, rj2_ops.py, rj2_ops_check.py, rj2_lin_check.py, rj2_test.py) et v2 (rj2_ops.py corrige, rj2_test_v2.py), empreintes aux sceaux NOTE-217-SCEAU.txt et NOTE-217-v2-SCEAU.txt.
- **Contenu ente (RJ2-V1 restreint)** :
  - Partie singuliere du tenseur de Dirac sur une solution de Fuchs : exactement (m/Omega)(psibar psi) n n/\|n\|^2, dans tout repere ; termes croises nuls dans psibar psi ; dans le noyau de S : aucune relation regularisante pour les seconds membres de matiere.
  - Exposant de Fuchs constant sur scri par (3.3) ; lapse nul sur scri ; seul canal de resonance a epsilon^3 : le lapse sur scri.
  - Classe a un seul exposant **preservee par le couplage** : formellement sous H1 et H2 (hypothese de resolubilite nouvelle, non demontree), et perturbativement a epsilon^3 sur de Sitter (deux calculs independants, deux jauges, deux jeux de vecteurs d'onde) ; geometrie en series entieres.
  - Classe generique : sans pole ni logarithme a epsilon^3 ; Weyl rescale continu, pas C^1 ; Schouten et courbure scalaire de la metrique conforme sans limite dans la jauge longitudinale, avec limite dans la jauge B : la regularite de la geometrie depend du facteur conforme.

## 2. Precedent (xvi ter)
Le precedent (xvi bis) s'etend a une note de calcul dont l'erreur **affaiblit une clause** du verdict sans toucher son resultat principal, si : (a) le resultat principal est etabli independamment par les deux auditeurs ; (b) la v2 restreint la clause fautive et la fonde sur un calcul scelle reproduisant les deux auditeurs ; (c) un re-audit court, consigne scellee avant lancement, conclut qu'aucune erreur ne reste ; (d) l'operateur decide l'entee. Une erreur qui renverserait le resultat principal reste soumise a une nouvelle execution sous gel propre.

## 3. Consequences
- **RG-4** : refutee a titre provisoire, raison resserree : (1) le spineur n'a pas de limite a scri pour toute masse constante non nulle ; (2) pour une matiere generique, la regularite de la geometrie a scri depend du facteur conforme, c'est-a-dire de la regle de raccord. La classe a un seul exposant (asymptotiquement que des particules, ou que des antiparticules) donne une geometrie en series entieres, analogue spinoriel de la poussiere de Friedrich, avec rho = m psibar psi positif.
- **Question ouverte nouvelle** : une regle de raccord CCC fixe-t-elle le facteur conforme a scri (par exemple R prescrit, comme dans la jauge de Friedrich) ? Si oui, la geometrie generique est-elle reguliere dans ce choix ? Test : jauge conforme de Friedrich, non faite.
- **Article** : v2.6 a preparer (Rem. 2(4) selon le texte de NOTE-217 v2 §5, reformule par RB-3), apres le depot Zenodo de la v2.5 par l'operateur.
- **Reprise v12** a rediger (compilation 201 a 220, PSE, RJ2).

## 4. Non-surclassement
Calcul et audit par IA, non relus par un humain. Formel (conditionnel) et perturbatif. Noyau {A4 ; A2★ ; N} inchange.
