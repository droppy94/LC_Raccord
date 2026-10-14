# Prompt M-a2 : re-derivation independante (cecite stricte), sources causales et partie sans trace de Q

Tu es un auditeur froid. Tu n'as acces a aucun travail anterieur : ne lis AUCUN fichier existant sur le disque en dehors de ceux que tu crees dans /home/claude/audit_ma2/ ; ne cherche pas de notes, scripts ou resultats anterieurs (en particulier rien sous /mnt/user-data/ ni sous /home/claude/irm/) ; ne consulte pas de sources externes. Tout ce qu'il faut est ci-dessous. Travaille avec sympy (python3), et numpy si utile. Reponds en francais, sans tirets longs. Etiquettes : [calcule], [derive].

## Cadre
- Repere conforme plat (electromagnetisme de Maxwell libre ordinaire), temps η < 0, surface finale η = 0. Unites c = 1.
- Source : courant transverse J(t, x) a support compact en espace et en temps, eteint avant η = 0. Champ a η = 0 par la fonction de Green retardee, mode de Fourier par mode : A_k(0) et E_k(0). Note J₊ = Ĵ(ω = +k, k) et J₋ = Ĵ(ω = −k, k) les composantes du courant sur la couche de masse (convention de Fourier a preciser par toi).
- Objet : Q = ⟨B_iB_j − E_iE_j⟩ a η = 0 (moyenne spatiale, donc somme sur les modes par Parseval : Q = Σ_k Re[k²(k̂ × a)(k̂ × a)† − b b†], a = A_k(0), b = E_k(0)). Q_tf est sa partie sans trace.
- Decomposition de Stokes dans le plan transverse a k̂ : intensite, polarisation lineaire (tenseur symetrique sans trace L dans le plan transverse), polarisation circulaire V.

## Questions
1. Donne a et b en fonction de J₊, J₋. Controle numerique sur un exemple de source.
2. Donne Q_k (contribution d'un mode) en fonction de J₊ et J₋, sous forme exacte. Separe une partie « diagonale » (J₊J₊†, J₋J₋†) et une partie d'interference (J₊ et J₋ melanges). Quelles composantes de Stokes (intensite, L, V) contribuent a la partie diagonale ?
3. Comment la partie d'interference depend-elle de l'instant d'emission t₀ d'une impulsion ? Que devient-elle apres moyenne sur une bande de k ?
4. Apres moyenne de l'interference, Q_tf est une integrale sur les directions k̂ d'un tenseur de polarisation. Quelle composante angulaire (multipole ℓ, type E ou B) du motif de polarisation survit ? Combien de conditions reelles faut-il imposer pour annuler Q_tf ?
5. Calcule Q_tf (ou la moyenne angulaire pertinente) pour : dipole magnetique lineaire m ; dipole electrique lineaire p ; dipole magnetique tournant (m ∝ x̂ − i ŷ) ; dipole « chiral » (p et m colineaires, de meme amplitude, en quadrature) ; ensemble isotrope d'orientations ; motif de polarisation E pur ℓ = 2 ; motif B pur ℓ = 2 ; combinaison generique (p, m et un quadrupole electrique). L'helicite d'une partie du rayonnement suffit-elle a annuler Q_tf ?
6. Pour un dipole magnetique lineaire, donne ⟨ε_Bε_B − ε_Eε_E⟩ (moyenne sur les directions, ε_E le long du potentiel, ε_B le long de k̂ × ε_E, poids inclus) en unites de (mm − ⅓m²𝟙), et sa relation avec la moyenne de L.
7. Conclusion : la classe des sources causales a Q_tf = 0 est-elle generique ou exceptionnelle ?

Rends un rapport structure (questions 1 a 7) avec les noms et empreintes sha256 de tes scripts et sorties.
