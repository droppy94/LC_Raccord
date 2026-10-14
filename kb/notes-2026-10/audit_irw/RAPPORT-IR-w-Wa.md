# RAPPORT W-a : recalcul aveugle du coefficient logarithmique Γ (normalisation et signe)

Auditeur froid, aucun fichier lu hors de /home/claude/audit_wa/ (en dehors de la consigne elle-même), aucune recherche bibliographique. Calculs sympy 1.14.0 dans /home/claude/audit_wa/work/.

## 0. Résultat en une ligne

**Γ = 64 π G b = 8πG × 8b** [calculé, deux méthodes]. Pour un scalaire conforme (b = 1/(120 (4π)²)) : **Γ = G/(30π) ≈ 0,0106103 G** [calculé]. Γ > 0 : le Weyl électrique rescalé **croît** (logarithmiquement) quand a → ∞, W_E ≈ W₀ (1 + Γ ln a). Γ ne dépend ni de k ni de A, B ; le terme logarithmique est porté exclusivement par la donnée B.

Réserve principale : ce Γ est la contribution du **seul** terme local b∫σC² (consigne). Les secteurs b'E, □R et la partie non locale W[g] ne sont pas inclus et pourraient, a priori, ajouter des logarithmes du même ordre (voir §6).

```
 bord futur 𝓘⁺ (s→0, a→∞)
     │   W_E(s) = W₀ [1 + Γ ln a + ...] ,  W₀ = −B k³/2
     │            ▲ croissance logarithmique (Γ = 64πGb > 0)
     │
 s ──┴──────────────────────────────▶  passé (s grand)
```

## 1. Partie locale de W en charge de Weyl [dérivé]

Conventions : ĝ = e^{2σ} g, σ = −ln s = ln a, g = η + εh, T_ab = −(2/√−g) δW/δg^{ab}.

Variation à g fixe, σ → σ + δσ : δĝ^{ab} = −2 δσ ĝ^{ab}. Donc
δW = ∫ (δW/δĝ^{ab}) δĝ^{ab} = ∫ (−½ √−ĝ T̂_ab)(−2 δσ ĝ^{ab}) = ∫ √−ĝ T̂^a_a δσ,
soit **δW/δσ = √−ĝ ⟨T̂^a_a⟩**.

En dimension 4, C^a_bcd est invariant conforme, donc √−ĝ Ĉ_abcd Ĉ^abcd = √−g C_abcd C^abcd (contrôlé symboliquement à l'ordre ε² sur le mode étudié [calculé] : différence nulle). Exiger ⟨T̂^a_a⟩ ⊃ b Ĉ² donne δW/δσ ⊃ b √−g C²[g], d'où

**W ⊃ + b ∫ d⁴x √−g σ C²[g]**, coefficient **+b** (signe positif, sans facteur 2 ni 1/2).

Ce terme s'écrit aussi + b ∫ √−ĝ σ Ĉ², σ étant une fonction externe fixée (le partage ĝ = e^{2σ}g se fait à σ fixe ; toute la variation métrique passe par g).

## 2. Tenseur produit par ce terme

### 2a. Forme fermée [dérivé]
Sur le fond de référence plat, C = O(ε). Avec δR_abcd = ½(∂_b∂_c δh_ad + ∂_a∂_d δh_bc − ∂_a∂_c δh_bd − ∂_b∂_d δh_ac), les quatre termes donnent la même contribution par les symétries de C, et la partie de Ricci est tuée par l'absence de trace de C :
δ(b∫σC²) = 2b∫σ C^{abcd} δR_abcd = −4b ∫ ∂_a∂_c(σ C^{abcd}) δh_bd,
d'où T^{bd} = 2 δW/δh_bd, soit

**T_ab[g] = −8 b ∂^c∂^d (σ C_acbd) + O(ε²)**, et, comme δĝ^{ab} = e^{−2σ} δg^{ab} et √−ĝĈ² = √−gC², **T̂_ab = e^{−2σ} T_ab[g] = s² T_ab[g]**.

### 2b. Contrôles indépendants [calculé] (t2_tenseur.py)
1. Euler-Lagrange brut de b σ C²[η+εh] (h_yy = p(s,x), h_zz = q(s,x) génériques et indépendants) : T_yy / [b ∂^c∂^d(σC_ycyd)] = **−8** identiquement.
2. Euler-Lagrange brut directement sur ĝ = s⁻²(η+εh) avec b√−ĝ σĈ² : T̂_yy(direct) − s² T_yy[g] = 0.
3. Fond de Sitter : Weyl nul à l'ordre 0, G_ab + 3ĝ_ab = 0 à l'ordre 0 (t3).

### 2c. Résultat sur le mode h_yy = −h_zz = u(s) cos kx (par unité ε cos kx) [calculé]
T̂_yy = 2b [ (u'' − k²u) − 2s (u''' + k² u') + s² σ (∂_s² + k²)² u ],  σ = −ln s.

Weyl de référence : C_sysy[η+εh] = (k²u − u'')/4.

Sur u₀ : (∂_s²+k²)² u₀ = 0, donc **le terme explicite en σ disparaît** et
T̂_yy[u₀] = 4 b k³ s (A sin ks − B cos ks) = **8 b C_sysy[u₀]** (aucun ln s dans la source).

## 3. Équation d'Einstein complétée [calculé] (t3_einstein.py, t4_exact.py)

Linéarisation (par ε cos kx) : δ(G + Λĝ)_yy = ½ (u'' − 2u'/s + k² u), Λ = 3 ; les composantes 00, 01, 11, 02, 23 et yy+zz sont nulles (mode TT cohérent). u₀ annule l'opérateur.

Avec u = u₀ + G u₁ : u₁'' − 2u₁'/s + k² u₁ = 16π T̂_yy[u₀] = 64 π b k³ s (A sin ks − B cos ks).

**Solution exacte** (variation des constantes, wronskien k³s², résidu nul) :
u₁ = 16πb { −y₁ [2A ln s + A cos 2ks − 2A Ci(2ks) + A + 2Bks + B sin 2ks − 2B Si(2ks)] − (ks cos ks − sin ks)[2Aks − A sin 2ks + 2A Si(2ks) − 2B ln s + B cos 2ks − 2B Ci(2ks) + B] },
y₁ = cos ks + ks sin ks, à des solutions homogènes près (renormalisation de A, B).

**Près de s = 0** (série avec logarithmes, contrôle indépendant, résidu nul jusqu'à s³) :
u₁ = (640π/3) A b + (320π/3) A b k² s² + (256π/15) B b k³ s³ − (32π/3) A b k⁴ s⁴ + (−(64π/3) s³ + (32π/15) k² s⁵) B b k³ ln s + (homogènes).
Le seul log dominant est **−(64π/3) b B k³ s³ ln s**, résonance de la source ∝ s avec la solution homogène en s³.

## 4. Weyl électrique rescalé [calculé]

W_E,yy = C_sysy[η+εh]/s (par ε cos kx) :
- W_E0 = (k³/2)(A sin ks − B cos ks) = −B k³/2 + A k⁴ s/2 + B k⁵ s²/4 + …
- W_E1 exact = 16πb k³ [ (B cos ks − A sin ks) ln s + Ci(2ks)(A sin ks + B cos ks) + Si(2ks)(B sin ks − A cos ks) − A(sin ks + ks cos ks) − B ks sin ks ].

Comme Ci(2ks) = ln s + (γ + ln 2k + série entière), la partie en ln s est, **exactement et à tous ordres en s** :
[W_E1]_{ln s} = 32π b B k³ cos ks ln s = −64π b ln s × W_E0|_{A=0}.

Donc, avec W₀ = −Bk³/2 et ln a = −ln s :

**W_E ≈ W₀ [1 + 64π G b ln a + O(G, s)]**, **Γ = 64 π G b**.

Scalaire conforme : Γ = 64π G /(1920 π²) = **G/(30π) ≈ 0,0106103 G**.

Γ > 0 : **le Weyl rescalé croît** (logarithmiquement à cet ordre perturbatif ; resommé formellement ∝ a^Γ) quand a → ∞.

| quantité | valeur | statut |
|---|---|---|
| coefficient de σC² dans W | +b | [dérivé] |
| T_ab[g] (ordre ε) | −8b ∂^c∂^d(σC_acbd) | [dérivé] + [calculé] |
| T̂_yy[u₀] | 8b C_sysy[u₀] | [calculé] |
| source u₁ | 64πbk³ s (A sin ks − B cos ks) | [calculé] |
| Γ | 64πGb | [calculé, série et exact] |
| Γ (scalaire) | G/(30π) ≈ 0,01061 G | [calculé] |

## 5. Indépendance vis-à-vis de k, A, B ; rôle de A [calculé]

- **k** : le rapport [W_E1]_{ln s} / W_E0|_{A=0} vaut −64πb sans k. k n'apparaît que dans la constante finie (16πbk³B(ln 2k + γ)), qui est de toute façon absorbable dans une redéfinition de B (solution homogène). Remarque : le log est ln s (c'est-à-dire ln(Hs) avec H = 1) et non ln(ks).
- **B** : porte W₀ et le log ; Γ ne dépend pas de sa valeur.
- **A** : n'entre ni dans W₀ ni dans Γ. Pour la partie A, le ln s explicite et celui de Ci(2ks) **se compensent exactement** : aucun logarithme n'affecte la contribution A à aucun ordre en s ; elle subit seulement une renormalisation finie (16πbk⁴ s (ln 2k + γ − 4) au premier ordre). Si B = 0, W_E → 0 à 𝓘⁺, W₀ = 0 et la forme W₀(1 + Γ ln a) est dégénérée (pas de log au premier ordre).

## 6. Hypothèses et ambiguïtés de convention

Hypothèses :
1. Signature (−,+,+,+), Riemann R^a_bcd = ∂_cΓ^a_bd − …, Ricci R_bd = R^a_bad, H = 1, Λ = 3.
2. Seul le terme b∫σC² est retenu (W[g] non local, secteurs b'E et □R exclus par la consigne). σ = −ln s fixé (externe) lors de la variation métrique.
3. Réduction d'ordre au premier ordre en G, source évaluée sur u₀ ; solutions homogènes de u₁ absorbées dans A, B.
4. Composante yy seule ; le mode reste TT à l'ordre ε (autres composantes de l'équation nulles côté géométrique ; côté source non vérifiées hors yy).

Ambiguïtés pouvant changer le signe ou un facteur :

| ambiguïté | effet sur Γ |
|---|---|
| Signe de la trace (⟨T⟩ = +bC² vs −bC², selon la convention de T_ab ou euclidien/lorentzien W_E = −W_L) | **change le signe** (Γ linéaire en b) |
| Définition T_ab = −(2/√−g)δW/δg^{ab} vs ±(1/√−g)… ou δ/δg_ab sans signe compensé | facteur 2 et/ou signe, **si** la trace n'est pas recalée dans la même convention ; si b est toujours défini par la trace dans la convention du membre de droite d'Einstein, Γ = 8πG·8b est robuste |
| Normalisation du couplage : 8πG vs κ² = 32πG vs 16πG | Γ = 64πGb = 2κ²b (κ² = 32πG) = 8κ²b (κ² = 8πG) : facteurs 2 à 8 si mal convertis |
| Sens du temps / signe de σ (σ = +ln s par erreur, ou ln s confondu avec ln a) | **change le signe** de Γ |
| Convention de Riemann | aucun effet (C² quadratique ; W_E et W₀ changent ensemble) |
| Rescaling du Weyl (C/s, Ω^n C) | aucun effet sur le coefficient du log tant qu'il s'agit d'une puissance de s |
| Valeur de b (1/(120(4π)²) pour un scalaire) | Γ proportionnel ; N champs : b → Σb |
| Secteurs exclus : le WZ du terme b'E contient des termes ∝ ∂σ∂σ qui couplent linéairement à h sur fond plat de référence ; ils peuvent produire des sources en puissances de s résonantes (comme ici, où le log vient de la résonance et **non** d'un σ explicite) ; idem pour W[g] non local (ln □) | Γ total **non garanti** égal à 64πGb ; à instruire séparément |

Point structurel notable : sur u₀, le terme en σ du tenseur s'annule ; le logarithme n'est pas « hérité » de σ = ln a mais naît de la résonance entre la source ∝ s et la solution homogène en s³. Un calcul qui attribuerait Γ directement au σ explicite du tenseur se tromperait de mécanisme (le résultat numérique reste ici 64πGb).

## 7. Empreintes sha256 (dossier /home/claude/audit_wa/work/)

```
66729e2ce314830d7fde764a3af1d61e0de92f06907024f80f3605f579f4fce0  geom.py
d76d41a701b275a5980fc95a83f2e370deda82cbcd18d7a788a52e7dc24eeb15  t2_tenseur.py
3b30b0c5197c931f7c41f56bd5e6f237fe4683e888f13aae8d7cdc36a3bc8766  t3_einstein.py
b078a9d82e01436f6f874bd940ba497273751a0ede8226cec053b53b64fa139d  t4_exact.py
af79ee83792fcd761159e8a2d33e0e47a6cbd0331fd4f0ab8772ac2724278152  t2_out.txt
edb3fbfeb4459113c64844419bb3f34fc5ad6a2f5ba8134c5b8a4ba39bee7434  t3_out.txt
3fe932a559d49a9a9685b22a97ba7f7f1f856c540df14546692f82095ac3cd5f  t4_out.txt
3efd2e4d0af03253fb13a0ac7cd79d299cd18fa5aa6d7ede317d0f4ace1c351d  t2_out.pkl
8951b1a0e6a3e4169ab86c1dfd443c981c90980894c821a47f12ebd4be9b8f67  t3_out.pkl
```

Note de traçabilité : un premier passage de t3 comportait un défaut d'extraction (coeff(ε) sur une expression non développée), détecté par le contrôle « fond G + Λg = 0 » qui échouait ; corrigé par expand avant extraction. Un premier découpage du log dans t4 annulait le ln s caché dans Ci (Ci → Ci_reg + L avec Ci_reg contenant −ln s, donc substitution neutre) et ne voyait que le ln s explicite (résultat erroné 32πGb, en contradiction avec la série) ; corrigé avec un symbole Creg. Les sorties ci-dessus sont celles des versions corrigées.
