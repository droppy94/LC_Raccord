# Prompt XA-1 : question d'EDP, derivation aveugle (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_xa1/ (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/, ni dans d'autres dossiers audit_*). Pas de recherche bibliographique : cite les theoremes que tu utilises de memoire, avec leur enonce exact et leurs hypotheses. Travaille avec sympy (python3) dans /home/claude/audit_xa1/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive], [cite de memoire].

## Probleme
Sur R⁴ de coordonnees (s, x, y, z), on considere l'operateur □ = −∂_s² + ∂_x² + ∂_y² + ∂_z² et son carre □². Le domaine est s > 0 ; l'hypersurface {s = 0} est son bord.

## Questions
1. Existe-t-il une solution u de □²u = 0 sur s > 0 (au sens des distributions) qui se comporte comme α(x, y, z) ln s + (termes plus reguliers) quand s → 0⁺, avec α non nulle sur un ouvert de {s = 0} ? Reponds de deux facons independantes :
   (a) par un calcul formel : ansatz u = Σ_{n=0}^{N} (a_n(x,y,z) + c_n(x,y,z) ln s) sⁿ avec N ≥ 6, coefficients fonctions arbitraires ; quelles contraintes □²u = 0 impose-t-il aux c_n ?
   (b) par un argument d'EDP general. Enonce precisement le resultat utilise (propagation des singularites, theoreme de regularite par rapport a une variable normale a une hypersurface non caracteristique, probleme de Cauchy, etc.), ses hypotheses (classe de u : distributions, croissance temperee en 1/s, ...), et dis s'il s'applique ici.
2. Les fonctions ln σ, 1/σ, s/σ, avec σ = x² + y² + z² − s², sont-elles solutions de □² = 0 hors de {σ = 0} ? Ou se trouve leur support singulier ? Se comportent-elles comme α ln s sur un ouvert de {s = 0} ? Si l'on deplace le sommet hors du bord (σ' = r² − (s + s₀)², s₀ > 0, sommet en s = −s₀), ou se trouve l'intersection du support singulier avec {s = 0} et quelle est sa nature ?
3. Existe-t-il une classe de solutions (donnees non distributionnelles, croissance non temperee, hyperfonctions, superpositions infinies) qui echapperait a ta conclusion de 1 ? Construis un exemple si possible, ou explique pourquoi c'est exclu dans une classe raisonnable.
4. Conclusion : ensemble de {s = 0} sur lequel un comportement en ln s est possible pour une solution homogene, selon la classe.

Rends un rapport structure dans /home/claude/audit_xa1/RAPPORT-XA1.md, avec les empreintes sha256 de tes scripts et sorties.
