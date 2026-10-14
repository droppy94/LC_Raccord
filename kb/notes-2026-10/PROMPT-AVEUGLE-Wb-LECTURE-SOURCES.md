# Prompt W-b : lecture aveugle de trois sources et conversion (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Ne lis aucun fichier du disque en dehors de /home/claude/audit_wb/ (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/, ni dans d'autres dossiers audit_*). Lis les sources via les outils alphaXiv (answer_pdf_queries, get_paper_content). Reponds en francais, sans tirets longs. Etiquettes : [extrait] (citation verbatim, avec numero d'equation et page), [calcule], [derive].

## Sources
- S1 : arXiv:2606.17963 (Foraci, Litos, Woodard 2026).
- S2 : arXiv:2501.05077 (Woodard 2025).
- S3 : arXiv:hep-th/0010232 (Hawking, Hertog, Reall 2001).

## Taches
1. Dans S1 et S2 : releve, pour un scalaire conformement couple, un fermion de Dirac et un photon, le coefficient du terme en ln a dans la correction a une boucle de la **partie electrique du Weyl** des ondes gravitationnelles sur de Sitter, et, s'il existe, l'exposant de la forme resommee. Releve la convention de κ, la definition de h (metrique physique ou rescalee), et ce que represente « C^tree » (puissance de a qu'il porte).
2. Releve les conditions de validite enoncees (logarithmes dominants, duree de la phase de Sitter, dependance de jauge, etat initial).
3. Dans S3 : releve la normalisation du coefficient du carre de Weyl dans la trace anomale (scalaires, fermions de Dirac, vecteurs) et la convention de signe de ⟨T_ij⟩.
4. **Conversion** : exprime chaque coefficient de S1/S2 en unites de G (H = 1). Puis, en notant b le coefficient du carre de Weyl dans la trace (normalisation S3) et κ = 8πG, exprime-le sous la forme Γ = n × b κ et donne n pour chacun des trois champs. Les trois n sont-ils egaux ?
5. Le facteur multiplicatif (1 + Γ ln a) ou a^Γ s'applique-t-il tel quel au Weyl **rescale** W = C/Ω (Ω ∝ 1/a) d'une metrique conformement compactifiee ? Argumente en tenant compte de ta reponse sur « C^tree ».
6. Signale toute ambiguite de convention qui changerait n ou son signe.

Rends un rapport structure ; sauvegarde les extraits verbatim dans /home/claude/audit_wb/work/ avec leurs empreintes sha256.
