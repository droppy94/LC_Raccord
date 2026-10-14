# Prompt XA-2 : audit d'un script et recherche de contre-exemples (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail anterieur. Lis uniquement les fichiers de /home/claude/audit_xa2/ ; ne lis rien d'autre sur le disque (rien sous /mnt/user-data/, /home/claude/irm/, /home/claude/irq/, ni dans d'autres dossiers audit_*). Travaille avec sympy (python3) dans /home/claude/audit_xa2/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

Empreinte a verifier : irx_cone.py 827df834e7ff941c8647edb7fa99e0b8d79fded2a790613739528e81b50ec713

Contexte : de Sitter plat ĝ = s⁻²(η + εh), bord futur s = 0 ; equation de Friedrich (2.17) : R_ρνλ = Ω⁻¹(∇̂_ν L̂_λρ − ∇̂_λ L̂_νρ), L̂ = (κ/2)(T̂ − ⅓ĝ trT̂), Ω = s ; T̂ = s² T, T_ab = −8b ∂^c∂^d(φ C_acbd[h]) ; mode h_yy = −h_zz = u cos kx, u = A(cos ks + ks sin ks) + B(sin ks − ks cos ks).

## Affirmations
- **x-1** : ln σ, 1/σ, s/σ (σ = r² − s²) verifient □² = 0 hors du cone.
- **x-2** : pour φ = ln σ, en un point (3/2, 1/2, 0) de s = 0, aucune composante de R n'a de terme en 1/s ; pres du cone (x = s + e, s = ½, y = z = 0) les composantes non nulles de R divergent comme e⁻³.
- **x-3** : dans l'ansatz φ = Σ_{n=0}^{7} (a_n(x,y,z) + c_n(x,y,z) ln s) sⁿ, □²φ = 0 force c₀ = … = c₇ = 0.
- **x-4** : □² f(s) = f'''' ; solution cubique.

## Mission
1. Audite le script point par point (OK / DEFAUT). Pour x-3 en particulier : l'extraction des coefficients (puissances de s et de ln s apres multiplication par s⁴) est-elle correcte ? La troncature a n = 7 laisse-t-elle des ordres mal resolus ? L'ordre de resolution peut-il masquer une solution avec c_n ≠ 0 ? Pour x-2 : le point choisi est-il hors du cone pour tout s petit ; le developpement en serie est-il fiable ; ln σ est-il bien defini (σ > 0) dans la zone testee ?
2. Reproduis independamment x-2 (au moins une autre position, par exemple un point avec z ≠ 0, et la composante la plus singuliere) et x-3 (implementation differente).
3. **Contre-exemples** : (a) sommet du cone hors du bord (σ' = r² − (s + s₀)², s₀ > 0) : le cone coupe s = 0 sur une sphere ; y a-t-il un pole en 1/s sur cette sphere, ou une autre singularite ? (b) φ = α(x) ln s + correcteurs : peut-on choisir des correcteurs (y compris des puissances non entieres s^μ, ou ln² s) pour obtenir □² = 0 avec α ≠ 0 ? (c) superposition de cones a sommets repartis sur une droite ou un plan de s = 0 avec un poids lisse : comportement pres de s = 0.
4. Juge chaque affirmation : valide, valide sous hypotheses (nomme-les), ou invalide.

Rends un rapport structure dans /home/claude/audit_xa2/RAPPORT-XA2.md, avec les empreintes de tes scripts et sorties.
