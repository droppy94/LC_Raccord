# Prompt M-b : audit des scripts et des affirmations, recherche de contre-exemples (aveugle au travail anterieur)

Tu es un auditeur froid. Tu ne connais pas le travail qui a produit les fichiers ci-dessous. Lis uniquement les fichiers de /home/claude/audit_mb/ (scripts et sorties) ; ne cherche pas d'autres notes ou fichiers sur le disque (rien sous /mnt/user-data/ ni sous /home/claude/irm/). Travaille avec sympy (python3) dans /home/claude/audit_mb/work/. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

Verifie d'abord les empreintes sha256 :
- ir_i.py 060efdf85b2213f64cb3e485ee325bcad618d34291c543b7770cf44d7b4e4972
- ir_l_v2.py bc17eb35414874c0bddd2cb956258f1464848e533d7d791edef91ebb74a2c38c
- ir_k.py d58327fe5149ecaf7a69d17b997414375e7aab865cb1c3283feb185b48e7ac40
- ir_k_affichage.py ff8cbab65034da49d36cc878698979c6f58228ef3d5c0ed8c924dc85884536db
- ir_k_ctrl.py 1ef8a3ba6c9458ea8bb14cefd10214db76bb428ca0dc5bf3bbd08b1141005fd5

## Cadre commun (rappel)
de Sitter H = 1, s = −τ = Ω > 0, ĝ = Ω⁻²η ; action simplifiee I² = e⁻²[1 + 2β(λ − ln s)] ; premier ordre en β ; mode A_y = u(s)cos(kx), u = u₀cos(ks) + (c/k)sin(ks) + βu₁ ; X^M = I²(F F ĝ⁻¹ − ¼ĝ F·F) ; L̂ = (κ/2)(T − ⅓ĝ trT) ; R_ρνλ = Ω⁻¹(∇̂_νL̂_λρ − ∇̂_λL̂_νρ). Q = ⟨B_iB_j − E_iE_j⟩ a 𝓘⁺, Q_tf sa partie sans trace.

## Affirmations soumises a l'audit
**Bloc I (ir_i.py, ir_i_sortie.txt)**
- I-A : sous une fermeture locale isotrope du secteur non Maxwell (H-loc : X^R = diag(r0,r1,r1,r1)(s,x) + composante (s,x), trace totale = T̂ locale, conservation), le coefficient de β ln s a l'ordre s⁰ dans R_isi(x) vaut (3κ/e²) × partie sans trace de Q(x) = B_iB_j − E_iE_j local (non moyenne) ; les gradients n'entrent qu'a l'ordre s ln s ; les 60 coefficients libres de la fermeture n'entrent dans aucun coefficient de log.
- I-A' : la ligne de sortie « loi locale verifiee … : False » est un defaut d'etiquette (la variable dite « termes negatifs en s » contient les termes positifs en s, d'ordre s ln s) ; le drapeau aurait du etre vrai.
- I-B : dipole magnetique eteint a t = −D (D = 10, w = 1/2) : a t = 0, boule r < D sans champ (pas de log) ; coquille r ≈ D rayonnee ; reliquat statique r > D. Moyennes angulaires des parties sans trace : statique (3n n_z − ẑ)² → 1/5 ; rayonnee (n n_z − ẑ)² − (n × ẑ)² → 4/5, en unites de diag(−⅓,−⅓,⅔). Integrales radiales : coquille 21,45 contre 21,36 predit (ecart 0,4 % attribue au melange statique-rayonne) ; reliquat 3,8108e-4 contre 3,8132e-4.

**Bloc L (ir_l_v2.py, ir_l_v2_sortie.txt)**
- L-A : pour une source eteinte, Q_k = −½ L(J₊J₊† + J₋J₋†) − ½ Re(J₊·J₋*)(δ − k̂k̂), exacte, ou L est la partie polarisation lineaire (symetrique sans trace dans le plan transverse).
- L-B : l'intensite et la polarisation circulaire ne contribuent pas ; identites Re(R M Rᵀ − M) = −2 L(M) et Re(R C Rᵀ + C) = tr(C) 𝟙.
- L-C : le terme d'interference oscille en cos(2k t₀) et se moyenne vers 0 ; apres moyenne seule la composante E ℓ = 2 du motif de polarisation survit ; Q_tf = 0 impose 5 conditions reelles (codimension 5) ; y echappent seulement l'helicite pure, un motif sans E ℓ = 2, un ensemble isotrope.
- L-D : valeurs de ⟨L⟩ : dipole magnetique lineaire −(2/5)(mm − ⅓m²) ; electrique +(2/5)(pp − ⅓p²) ; magnetique tournant diag(−2/15, −2/15, 4/15) ; chiral 0 dans chaque direction ; isotrope 0 ; E pur ℓ = 2 (2/5)A ; B pur ℓ = 2 0 ; generique non nul.

**Bloc K (ir_k.py, ir_k_affichage.py, ir_k_ctrl.py et sorties)**
- K-A : ∇^μ X^M_μν + ¼ ∂_ν(I²) F² = 0 sur couche (4 composantes), et le coefficient de ln s dans ∇^μ X^M_μν est nul au premier ordre en β.
- K-B : pour la famille g = s⁻² diag(−1, 1 + εh₁, 1 + εh₂, 1 + εh₃)(s, x), la partie (b) de Riegert donne T_1 = −(1/6)∂_s⁴ψ + (1/6)∂_s²∂_x²ψ et T_2 = T_3 = −(1/6)∂_s⁴ψ − (1/6)∂_x⁴ψ + (1/3)∂_s²∂_x²ψ ; aucun log, aucune trace de φ = −ln s ; pour ψ lisse, T_ii ~ s² ; T_2 = T_3.
- K-C : R calcule avec T = X^M seul redonne, pour le coefficient de ln s a l'ordre s⁰, (3βκ/e²) Q_tf(x) (ecart 0), sans autre log.
- K-D (conclusion) : l'hypothese H-loc est inutile pour le coefficient du log ; aucune completion de la classe « Riegert + partie invariante de Weyl a tenseur plat lisse » ne compense le log ; qualifications : variation de W hors orbite de Weyl, famille de metriques diagonale, etat de ψ causal et lisse.

## Mission
1. Audite chaque script point par point : OK / DEFAUT, avec des controles independants la ou un controle du script serait tautologique. Confirme ou infirme I-A'.
2. Reproduis independamment les resultats porteurs I-A, I-B (au moins les moyennes 1/5 et 4/5 et l'absence de champ dans r < D), L-A, L-C, L-D, K-A, K-B, K-C.
3. **Cherche activement des contre-exemples** :
   - bloc I : composantes de R autres que (i, s, i), gradient a l'ordre s⁰, coefficient libre de la fermeture dans un log ;
   - bloc L : une source causale a Q_tf = 0 hors des trois classes annoncees ; un motif qui annule la composante E ℓ = 2 sans etre de l'une de ces classes (cela est-il compatible avec « codimension 5 » ?) ; un cas ou l'interference ne se moyenne pas ;
   - bloc K : presence de φ ou de log dans T^(b) pour une autre famille simple (par exemple dependance en (s, x, y), ou une composante hors diagonale h_xy si c'est faisable rapidement) ; dependance de K-C a une hypothese cachee du script.
4. Juge K-D : valide, valide sous hypotheses (nomme-les), ou invalide.
5. Liste reserves et corrections.

Rends un rapport structure (blocs I, L, K) avec les empreintes de tes scripts et sorties.
