# Prompt W-a : recalcul aveugle d'un coefficient logarithmique, normalisation et signe (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_wa/ (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/, ni dans d'autres dossiers audit_*). N'utilise pas de recherche bibliographique : tout doit etre derive. Travaille avec sympy (python3) dans /home/claude/audit_wa/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Probleme
Gravite d'Einstein avec constante cosmologique, signature (−,+,+,+), couplee a N champs conformes libres traites semi-classiquement : G_ab + Λ g_ab = 8πG ⟨T_ab⟩, avec ⟨T_ab⟩ = −(2/√−g) δW/δg^{ab}, W etant l'action effective lorentzienne des champs (S_total = S_EH + W, S_EH = (1/16πG)∫√−g (R − 2Λ)).
La trace anomale est ⟨T^a_a⟩ = b C_abcd C^abcd − b' E + (terme en □R), ou b > 0 est le coefficient du carre de Weyl (on prendra pour un scalaire conformement couple b = 1/(120 (4π)²) ; l'audit ne porte pas sur cette valeur mais sur tout le reste).
Fond : de Sitter plat, ĝ = s⁻² η, s > 0 temps conforme (s → 0 au bord futur 𝓘⁺, facteur d'echelle a = 1/s, H = 1).

## Taches
1. **Partie locale de W en charge de Weyl.** Ecris ĝ = e^{2σ} g avec g = η + εh et σ = −ln s. Etablis, a partir de la seule exigence que la trace ci-dessus soit reproduite avec la convention ⟨T_ab⟩ = −(2/√−g)δW/δg^{ab}, le **signe et le coefficient** du terme local ∫√−g (coefficient) σ C² de W (la partie non locale W[g] et les parties en E et □R sont hors sujet ici). Montre ta derivation (variation sous σ → σ + δσ a g fixe et identification avec la trace).
2. **Tenseur.** Calcule le tenseur ⟨T̂_ab⟩ produit par ce seul terme sur ĝ, a l'ordre ε, pour le mode tensoriel h_yy = −h_zz = u(s) cos kx, u₀ = A(cos ks + ks sin ks) + B(sin ks − ks cos ks) (solution du vide sur ce fond). Methode libre, mais fais au moins un controle independant (par exemple variation brute d'Euler-Lagrange contre une forme fermee).
3. **Equation completee.** Resous au premier ordre en G (reduction d'ordre : u = u₀ + G u₁, source evaluee sur u₀) l'equation d'Einstein linearisee completee pour la composante yy, pres de s = 0, en autorisant des termes s^n ln s.
4. **Weyl electrique.** Calcule la partie electrique du Weyl rescale, W_E,yy = C_sysy[η + εh]/s (Weyl de la metrique de reference), pour u₀ + G u₁, et mets-la sous la forme W_E ≈ W₀ (1 + Γ ln a + …), a = 1/s. Donne **Γ** en fonction de G et b, puis sa valeur numerique en unites de G pour un scalaire conforme. Dis si le Weyl rescale **croit ou decroit** quand a → ∞.
5. Independance de Γ vis-a-vis de k et des donnees A, B ; role de A.
6. Liste tes hypotheses et toute ambiguite de convention qui pourrait changer le signe ou un facteur numerique (facteur 2 dans κ, signe de la trace, signature, definition de T_ab, sens du temps).

Rends un rapport structure, avec les empreintes sha256 de tes scripts et sorties.
