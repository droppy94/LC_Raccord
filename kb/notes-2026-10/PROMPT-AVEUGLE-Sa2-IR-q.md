# Prompt S-a2 : re-derivation independante (cecite stricte), regularite du raccord en presence d'un logarithme dans l'equation de Bianchi rescalee

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_sa2/ ; ne cherche pas de notes, scripts ou resultats anterieurs (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/ ni dans d'autres dossiers audit_*) ; ne consulte pas de sources externes. Tout ce qu'il faut est ci-dessous. Travaille avec sympy (python3). Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Cadre
- Metrique « pont » (non physique) g pres d'une hypersurface spatiale Σ = {τ = 0} ; facteur conforme Ω = τ au premier ordre (τ > 0 d'un cote). On note W = C[g]/Ω la courbure de Weyl rescalee. Dans le systeme conforme de Friedrich, W obeit a ∇^μ W_μνλρ = R_νλρ, ou R est un second membre construit a partir de la matiere.
- Hypothese a examiner : R contient un terme A ln Ω (A tenseur non nul) a l'ordre dominant.
- Modele : g = −dτ² + (δ_ij + ε d_ij f(τ)) dx^i dx^j, d = diag(1, 1, −2), premier ordre en ε.
- Regle de raccord a utiliser pour la question 3 (prescription dite « reciproque ») : la metrique physique du cote suivant est ǧ = Ω̌² g avec Ω̌ ∝ τ au premier ordre (meme repere g), et l'on exprime le resultat en temps propre Ť de ǧ (dŤ = Ω̌ dτ).

## Questions
1. Quel comportement f(τ) pres de τ = 0 est compatible avec dW/dτ ~ ln τ (au premier ordre, dans ce modele) ? Verifie-le par calcul de la courbure de Weyl de g.
2. Quelle est alors la classe de differentiabilite de g en τ = 0 ? W est-elle continue ? C¹ ?
3. Pour ǧ = τ² g, calcule le tenseur d'Einstein (repere orthonorme) en temps propre Ť : terme d'ordre zero en ε (quelle matiere ?) et terme d'ordre ε (structure tensorielle, ordre en Ť, presence de ln Ť).
4. Le raccord « casse-t-il » (divergence des quantites physiques dominantes) ou perd-il seulement de la regularite ? Precise.

Rends un rapport structure (questions 1 a 4) avec les noms et empreintes sha256 de tes scripts et sorties.
