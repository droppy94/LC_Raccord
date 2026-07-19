---
id: LC-A-SURVIE-CONFORME
titre: "Module A — Survie conforme à Λ≠0 : 𝓘⁺ spacelike, fatal ou contournable ?"
codename: LC-RACCORD
tags: [module-A, ccc, scri, de-sitter, lambda, friedrich, equations-conformes, weyl, crossover, survie-conforme]
type: chaînon du programme principal (premier maillon A→F)
statut: établi (le cœur géométrique : extension conforme régulière à 𝓘⁺ spacelike) / la difficulté réelle migre vers matière + facteur conforme + Weyl
version: 0.1
langue: fr
date: 2026-06-07
statut_id: provisoire — à enregistrer dans LC-00-INDEX et LC-02-PROGRAMME
fichier_compagnon: verif_moduleA_scri.py
renvois: [LC-00-INDEX, LC-01-CADRE, LC-02-PROGRAMME, LC-03-GLOSSAIRE, LC-04-REFERENCES]
modules_rattachement:
  - "[A] survie conforme / CCC (ce document)"
  - "[D] holographie / donnée de Cauchy à 𝓘 (données conformes de Friedrich)"
  - "[E] retour de l'échelle (le rayon de Sitter est la condition de A)"
tags_epistemiques: [établi, formalisable, à inventer, hors de portée, décision ouverte]
---

# LC-A — Survie conforme à Λ≠0

> **Question frontale.** En présence de $\Lambda>0$, l'infini conforme futur
> $\mathcal{I}^+$ est de **genre espace** (et non nul comme en asymptotiquement
> plat). `LC-01` §3 présente ce fait comme une *complication / faiblesse héritée de
> la CCC*. Est-ce **fatal** au raccordement, ou **contournable** ?
>
> **Verdict (calcul explicite + Friedrich 1986).** *Ni l'un ni l'autre : c'est la
> condition **requise** et le cas le **mieux posé**.* Le cœur géométrique du module A
> — l'existence d'une extension conforme régulière à travers $\mathcal{I}^+$ — est
> **`établi`**. La difficulté réelle n'est pas le caractère spacelike (qui est un
> atout) ; elle **migre** vers (i) l'invariance conforme de la matière, (ii) l'unicité
> du facteur conforme au crossover, (iii) l'hypothèse de Weyl. `LC-01` §3 est à
> **corriger** (§3 ci-dessous).

---

## 0. Cible et garde-fou

Module A (`LC-02` [A]) demande : *la structure conforme survit-elle à la fin d'éon
avec $\Lambda\neq0$ ?* C'est le **premier maillon** de la chaîne A→F : son échec
rendrait tout le reste sans objet (`LC-00`). On l'attaque par son point réputé le
plus dur — $\mathcal{I}^+$ spacelike — au niveau **explicite** (équations d'Einstein
conformes, régularité au crossover).

**Garde-fou `[à respecter]`.** « Le cœur géométrique de A est `établi` » ne veut pas
dire « la conjecture avance ». Cela veut dire : *le maillon réputé bloquant ne bloque
pas* — il se déplace. La CCC reste un cadre `spéculatif encadré` ; ce document
**relocalise** honnêtement sa charge ouverte, il ne la dissout pas.

---

## 1. Sceau explicite — structure conforme de de Sitter `[établi]`

Compagnon : `verif_moduleA_scri.py` (sympy, sans réseau). Re-exécutable.

**[A.dS.1] C'est bien de Sitter.** En tranchage fermé, temps conforme $\eta=\mathrm{gd}(Ht)$
(sans dimension, $\eta\in(-\tfrac\pi2,\tfrac\pi2)$), facteur d'échelle
$a(\eta)=H^{-1}\sec\eta$ :

$$\mathrm{d}s^2 = \frac{1}{H^2\cos^2\eta}\big(-\mathrm{d}\eta^2 + \mathrm{d}\Omega_3^2\big),
\qquad R = 12H^2 = 4\Lambda,\quad R_{ab}=\Lambda g_{ab},\quad \Lambda=3H^2.$$

(Vérifié symboliquement : Ricci scalaire constant $=12H^2$, équations d'Einstein
vide $+\Lambda$ satisfaites.) `[établi]`

**[A.dS.2] Caractère causal de $\mathcal{I}$.** On rescale par $\Omega=\cos\eta$ :
$\tilde g = \Omega^2 g = H^{-2}(-\mathrm{d}\eta^2+\mathrm{d}\Omega_3^2)$, **régulière et
non dégénérée** en $\eta=\pm\tfrac\pi2$ (les deux infinis $\mathcal{I}^\pm$). La norme
du gradient du facteur conforme y vaut :

$$\boxed{\;N \equiv \tilde g^{ab}\,\partial_a\Omega\,\partial_b\Omega
= -H^2\sin^2\eta\;\xrightarrow{\;\mathcal{I}^\pm\;}\; -H^2 = -\frac{\Lambda}{3} < 0\;}$$

Gradient **temporel** $\Rightarrow$ $\mathcal{I}^\pm$ **de genre espace**. Le résultat
est gauge-invariant en signe :

$$\mathrm{signe}(N)\big|_{\mathcal{I}} = -\,\mathrm{signe}(\Lambda):\quad
\Lambda>0\ \text{spacelike}\ \cdot\ \Lambda=0\ \text{null}\ \cdot\ \Lambda<0\ \text{timelike}.$$

La valeur canonique $N|_{\mathcal{I}}=-\Lambda/3$ coïncide avec le cadre
asymptotique à $\Lambda>0$ (Ashtekar et al.). `[établi]`

> **Lecture.** L'infini nul de l'asymptotiquement plat ($\Lambda=0$) est un *cas
> limite dégénéré* ($N\to0$). Dès que $\Lambda>0$, $\mathcal{I}^+$ devient une
> **3-surface spacelike propre** sur laquelle $\tilde g$ est lisse et non dégénérée.

---

## 2. Verdict frontal — spacelike $\mathcal{I}^+$ n'est pas fatal : il est requis `[établi]`

Trois faits convergents montrent que le caractère spacelike est un **atout**, non un
obstacle.

**(a) Friedrich 1986 — extension non dégénérée + problème de Cauchy régulier.**
H. Friedrich (*On the existence of n-geodesically complete… solutions… with smooth
asymptotic structure*, Comm. Math. Phys. 107, 587, 1986) a montré que pour
$\Lambda>0$, les **équations d'Einstein conformes régulières** (où le facteur
conforme est l'une des inconnues) s'étendent **non dégénérément à travers
$\mathcal{I}^+$ spacelike**. La stabilité non linéaire globale de de Sitter se
**réduit à un résultat local-en-temps** pour un système symétrique hyperbolique. Une
petite perturbation des données de de Sitter redonne un espace-temps
asymptotiquement simple. `[établi]`

**(b) Les données conformes à $\mathcal{I}^+$ sont une donnée de Cauchy.** Le théorème
de Friedrich établit une correspondance 1-1 (près du bord) entre solutions
asymptotiquement simples et **données de diffusion à $\mathcal{I}^+$** : une métrique
riemannienne $g_{(0)}$ (métrique induite) et un tenseur TT $g_{(3)}$ (composantes du
tenseur de Weyl *rescalé*), sur une 3-variété compacte. *C'est exactement l'objet
« donnée initiale fixée par le bord » que demande le module $[D]$* (`LC-02` [D] :
« la CFT céleste peut-elle fixer une donnée de Cauchy ? »). **A alimente D de façon
précise.** `[établi côté A ; pont vers D formalisable]`

**(c) La CCC a *besoin* de $\mathcal{I}^+$ spacelike.** Le programme de Penrose (CCC,
*Cycles of Time*, 2010) raccorde le futur lointain d'un éon au Big Bang du suivant.
Le Big Bang, après rescaling conforme, est une 3-surface **spacelike**. Pour qu'il y
ait raccord causalement cohérent, le bord futur de l'éon précédent doit l'être aussi.
Or $\Lambda>0$ permet précisément de *réduire l'échelle* pour adjoindre un bord futur
spacelike. Un $\mathcal{I}^+$ **nul** ($\Lambda=0$) serait du *mauvais* type causal
pour jouer le rôle d'un Big Bang. **Le spacelike est la condition d'existence du
raccord, pas son obstacle.** `[établi]`

$$\boxed{\;\text{« }\mathcal{I}^+\text{ spacelike »} \;=\; \text{contournable et favorable}
\;:\;\text{extension régulière (Friedrich), Cauchy bien posé, match spacelike↔spacelike.}\;}$$

### Diagramme conforme — pourquoi le spacelike est ce qu'il faut

<svg width="100%" viewBox="0 0 680 430" role="img" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif">
  <title>de Sitter : 𝓘± spacelike, et raccord CCC spacelike↔spacelike</title>
  <desc>À gauche, le diagramme conforme de de Sitter : un carré, bord supérieur 𝓘+ et bord inférieur 𝓘- tous deux spacelike (horizontaux), cônes de lumière à 45°. À droite, le raccord CCC : 𝓘+ de l'éon n (spacelike) est identifié au Big Bang spacelike de l'éon n+1 ; deux surfaces spacelike se collent naturellement.</desc>
  <!-- gauche : dS -->
  <text x="150" y="28" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">de Sitter (Λ&gt;0)</text>
  <rect x="60" y="50" width="180" height="180" fill="#EEEDFE" stroke="#534AB7" stroke-width="1"/>
  <line x1="60" y1="50" x2="240" y2="50" stroke="#1D9E75" stroke-width="3.5"/>
  <line x1="60" y1="230" x2="240" y2="230" stroke="#1D9E75" stroke-width="3.5"/>
  <text x="150" y="44" text-anchor="middle" font-size="12" fill="#0F6E56">𝓘⁺ (spacelike)</text>
  <text x="150" y="246" text-anchor="middle" font-size="12" fill="#0F6E56">𝓘⁻ (spacelike)</text>
  <line x1="80" y1="230" x2="170" y2="140" stroke="#D85A30" stroke-width="1.4"/>
  <line x1="170" y1="140" x2="220" y2="190" stroke="#D85A30" stroke-width="1.4"/>
  <text x="196" y="150" font-size="11" fill="#993C1D">cône 45°</text>
  <text x="52" y="145" text-anchor="end" font-size="11" fill="#73726c" transform="rotate(-90 52 145)">η (pôle χ=0)</text>
  <text x="248" y="145" font-size="11" fill="#73726c" transform="rotate(90 248 145)">pôle χ=π</text>
  <!-- droite : raccord CCC -->
  <text x="500" y="28" text-anchor="middle" font-size="14" font-weight="500" fill="#3C3489">raccord CCC</text>
  <rect x="410" y="50" width="180" height="120" fill="#FAECE7" stroke="#D85A30" stroke-width="0.8"/>
  <text x="500" y="115" text-anchor="middle" font-size="12" fill="#993C1D">éon n+1</text>
  <text x="500" y="132" text-anchor="middle" font-size="11" fill="#993C1D">(nouveau)</text>
  <rect x="410" y="230" width="180" height="120" fill="#E1F5EE" stroke="#1D9E75" stroke-width="0.8"/>
  <text x="500" y="295" text-anchor="middle" font-size="12" fill="#0F6E56">éon n</text>
  <line x1="410" y1="170" x2="590" y2="170" stroke="#534AB7" stroke-width="4"/>
  <line x1="410" y1="230" x2="590" y2="230" stroke="#534AB7" stroke-width="4"/>
  <text x="500" y="205" text-anchor="middle" font-size="11.5" fill="#3C3489">crossover 𝒞 (spacelike)</text>
  <text x="500" y="164" text-anchor="middle" font-size="10.5" fill="#73726c">= Big Bang(n+1)</text>
  <text x="500" y="247" text-anchor="middle" font-size="10.5" fill="#73726c">= 𝓘⁺(n)</text>
  <text x="500" y="372" text-anchor="middle" font-size="11" fill="#534AB7">spacelike ↔ spacelike : raccord cohérent</text>
  <text x="500" y="390" text-anchor="middle" font-size="11" fill="#73726c">(Λ&gt;0 ⟹ bord futur spacelike — Friedrich : extension régulière)</text>
  <text x="150" y="372" text-anchor="middle" font-size="11" fill="#73726c">𝓘⁺ nul (Λ=0) serait du mauvais</text>
  <text x="150" y="388" text-anchor="middle" font-size="11" fill="#73726c">type causal pour un Big Bang</text>
</svg>

*Fig. — À gauche : $\mathcal{I}^\pm$ de de Sitter sont des bords **spacelike** (Friedrich :
$\tilde g$ s'y étend non dégénérément). À droite : le raccord CCC colle $\mathcal{I}^+(n)$
spacelike au Big Bang spacelike de l'éon $n{+}1$ — deux surfaces de même type causal,
raccord cohérent. Le caractère spacelike est la **condition**, pas l'obstacle.*

---

## 3. Correction de `LC-01` §3 `[à corriger]`

Le texte actuel de `LC-01` §3 (maillon §1) :

> « §1 — disparition de la masse non acquise `[hors de portée / spéculatif]`. […]
> surtout, une constante cosmologique `Λ ≠ 0` réintroduit une échelle (rayon de
> Sitter) et rend `𝓘⁺` de genre espace, ce qui complique le raccordement. Faiblesse
> héritée de la CCC. »

**Imprécision à corriger.** Le caractère spacelike de $\mathcal{I}^+$ n'est **pas** ce
qui « complique le raccordement » — c'en est la **condition d'existence** (§2). La
formulation conflate deux choses distinctes :

1. *La réintroduction d'une échelle par $\Lambda$* — réelle, mais c'est l'objet du
   **module $[E]$** (retour de l'échelle), pas une faiblesse de A ; et c'est elle qui
   rend $\mathcal{I}^+$ spacelike, donc raccordable.
2. *La disparition de la masse* — réelle difficulté (matière), à conserver
   `[hors de portée / spéculatif]`, mais elle relève de la matière (§4-D2), non de la
   géométrie de $\mathcal{I}^+$.

**Reformulation proposée pour `LC-01` §3 (maillon §1)** :

> « §1 — *Géométrie* : à $\Lambda>0$, $\mathcal{I}^+$ est spacelike et l'extension
> conforme y est **régulière** (Friedrich 1986) — c'est la condition *favorable* du
> raccordement, non une faiblesse (cf. `LC-A`). La faiblesse réelle est ailleurs :
> (a) disparition de la masse / invariance conforme de la matière
> `[hors de portée / spéculatif]` ; (b) unicité du facteur conforme au crossover et
> hypothèse de Weyl `[décision ouverte / à inventer]`. »

*(Édit non appliqué à `LC-01` ici ; recommandé en propagation, comme la cascade φ.)*

---

## 4. Où migre la vraie difficulté `[la charge ouverte, relocalisée]`

Le cœur géométrique passant (§2), la charge ouverte de A→raccord se concentre en
quatre points **nommés**, distincts du caractère causal de $\mathcal{I}^+$ :

- **D1 — Unicité du facteur conforme au crossover** `[décision ouverte / à inventer]`.
  *Le* problème ouvert majeur de la CCC : choisir $\Omega$ de façon unique. La CCC
  pose la relation *réciproque* de Penrose $\Omega\,\omega=-1$ (avec
  $\hat g=\Omega^2 g$, $\check g=\omega^2 g$), de sorte qu'un représentant fini existe
  au crossover. Mais les prescriptions de **Newman** (2014), **Tod** (2015) et
  **Nurowski** (2021) **divergent** entre elles et d'avec Penrose. C'est le verrou
  formel de A — analogue, pour le programme principal, au verrou Gauss–Seidel du
  sous-programme φ.
- **D2 — Invariance conforme de la matière** `[hors de portée / spéculatif]`. La
  « bandage region » exige une matière **sans masse au repos** (tenseur
  énergie-impulsion de trace nulle) pour que seule la structure de cônes de lumière
  détermine les deux espace-temps. La décroissance asymptotique de la masse au repos
  est physiquement non établie (cf. `LC-01` §5, anomalie de trace).
- **D3 — Hypothèse de courbure de Weyl** `[décision ouverte]`. $C_{abcd}\to0$ au
  crossover (entropie gravitationnelle basse au nouveau Big Bang). Justifiée
  thermodynamiquement par Penrose ; sa *nécessité* dynamique est étudiée (Anguige–Tod :
  Weyl nul initial $\Rightarrow$ conformément plat, pour fluide parfait). Statut
  dynamique non tranché.
- **D4 — Perte d'information dans les trous noirs** `[décision ouverte / controversé]`.
  Hypothèse de Penrose (perte de degrés de liberté) ; incompatible avec l'unitarité au
  sens de l'information quantique. Des versions *unitaires* de CCC (information
  préservée à travers le crossover via intrication avec des d.o.f. gravitationnels)
  sont proposées — **pont direct vers le module $[C]$** (l'intrication comme colle) et
  vers la colonne modulaire de `LC-RACCORD`.

> **Carte de statut du module A (révisée).**
> | Sous-question | Avant (`LC-01`) | Après `LC-A` |
> |---|---|---|
> | $\mathcal{I}^+$ spacelike fatal ? | « complique, faiblesse » | **non — requis & favorable** `[établi]` |
> | extension conforme régulière à $\Lambda>0$ ? | implicitement douteuse | **existe** (Friedrich) `[établi]` |
> | unicité du facteur conforme (D1) | non isolé | **verrou ouvert** `[à inventer]` |
> | matière sans masse (D2) | `[hors de portée]` | `[hors de portée]` (inchangé) |
> | hypothèse de Weyl (D3) | non isolé | `[décision ouverte]` |

---

## 5. Format de chaînon standard

- **Zone ambiguë** (`LC-01` §1–3). « $\Lambda\neq0$ rend $\mathcal{I}^+$ spacelike,
  ce qui complique le raccordement. »
- **Hypothèse de travail.** À $\Lambda>0$, le bord futur admet une extension conforme
  **lisse et non dégénérée** au-delà de $\mathcal{I}^+$, via les équations d'Einstein
  conformes régulières (facteur conforme comme inconnue dynamique).
- **Outil.** Équations conformes de Friedrich (système symétrique hyperbolique) ;
  contraintes conformes sur une hypersurface spacelike ; calcul explicite §1.
- **Critère de réfutation** (`LC-02` [A]). *« S'il est démontré qu'aucune extension
  régulière n'existe pour $\Lambda\neq0$ sans conditions sur la matière physiquement
  intenables, le raccordement géométrique est mort. »*
- **Verdict.** Critère **NON satisfait** : l'extension régulière **existe** (Friedrich),
  *sans* condition intenable sur la matière au seul niveau géométrique. Le cœur de A
  est `établi`. La charge se reporte sur D1/D2/D3 (§4).

---

## 6. Conséquence pour le programme

$$\boxed{\;\text{Module A n'est pas le maillon le plus faible — c'est le plus solide.}\;}$$

Le pessimisme implicite de `LC-01` est inversé : le maillon réputé bloquant
(géométrie à $\Lambda>0$) est `établi`. Cela **resserre** la cible du programme :
- ce qui décide du sort de la CCC n'est **pas** « la géométrie survit-elle ? » (oui),
  mais **D1** (facteur conforme unique) et **D2** (matière conforme) ;
- D1 est un problème *mathématique fini et attaquable* (comparer/contraindre les
  prescriptions Newman/Tod/Nurowski), candidat naturel au **prochain chaînon** ;
- les données conformes de Friedrich $(g_{(0)},g_{(3)})$ à $\mathcal{I}^+$ sont le
  **branchement explicite vers $[D]$** (donnée de Cauchy holographique) et, via D4,
  vers $[C]$.

Ordre recommandé inchangé (A → B → {C,D} → E → F), mais **A est franchi sur son cœur
géométrique** ; le travail actif se déplace vers D1 (au sein de A/E) puis B.

---

## 7. Renvois, glossaire, références

**Renvois.** `LC-01` §1,3,5 (cadre, à corriger §3) ; `LC-02` [A],[D],[E] (chaînon, à
enregistrer) ; `LC-00` (chaîne logique). Pont aval : $[D]$ (données conformes de
Friedrich = donnée de Cauchy), $[C]$/$[E]$ (D4 unitaire, échelle).

**Glossaire à ajouter (`LC-03`).**
- *Infini conforme $\mathcal{I}$ ; caractère causal* : $\mathrm{signe}(N)|_{\mathcal{I}}=-\mathrm{signe}(\Lambda)$.
- *Équations d'Einstein conformes (Friedrich)* : système régulier où $\Omega$ est inconnue.
- *Asymptotiquement simple / stabilité non linéaire de de Sitter* (Friedrich 1986).
- *Données conformes à $\mathcal{I}^+$* : $(g_{(0)},g_{(3)})$ (métrique induite + Weyl rescalé TT).
- *Crossover / bandage region* (CCC) ; *hypothèse réciproque* $\Omega\omega=-1$.
- *Hypothèse de courbure de Weyl* (forte / faible).

**Références (`LC-04`, à intégrer ; `[à vérifier]` sauf mention).**
- H. Friedrich, *On the existence of n-geodesically complete or future complete
  solutions of Einstein's field equations with smooth asymptotic structure*,
  Comm. Math. Phys. **107**, 587 (1986). `[confirmé]` — extension conforme régulière à
  $\mathcal{I}^+$ spacelike, stabilité non linéaire de dS.
- R. Penrose, *Cycles of Time*, 2010 — CCC. `[confirmé]`
- K. P. Tod, *Penrose's Weyl curvature hypothesis and conformally-cyclic cosmology*,
  J. Phys. Conf. Ser. **229**, 012013 (2010) ; et *Gen. Rel. Grav.* (2015) — crossover,
  facteur conforme. `[confirmé]`
- E. T. Newman (2014) ; P. Nurowski, Class. Quantum Grav. **38**, 145004 (2021) —
  prescriptions du facteur conforme (divergentes). `[à vérifier]`
- C. Lübbe & J. A. Valiente Kroon (2013) — stabilité FRW (fluide de radiation) par
  équations conformes. `[confirmé]`
- A. Ashtekar et al., asymptotique à $\Lambda>0$ ($N|_{\mathcal{I}}=-\Lambda/3$). `[à vérifier — auteur/année exacts]`
- Anguige & Tod — singularités isotropes, Weyl nul $\Rightarrow$ conformément plat. `[à vérifier]`
- Markwell & Stevens, *Toward fixing a framework for CCC*, Gen. Rel. Grav. (2023) —
  comparaison des prescriptions. `[à vérifier]`

---

## Appendice — Légende des tags épistémiques
`établi` / `formalisable` / `à inventer` / `hors de portée` / `décision ouverte`
(cf. `LC-00-INDEX`).
