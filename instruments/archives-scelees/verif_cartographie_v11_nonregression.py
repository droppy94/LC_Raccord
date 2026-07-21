#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_cartographie_v11_nonregression.py

Sceau de NON-RÉGRESSION ADDITIVE pour l'amendement
LC-WORK-CARTOGRAPHIE-PRIORITES  v1.0 -> v1.1  (item D.4 du squelette).

INVARIANT VÉRIFIÉ (discipline additive-only) :
  CORPS (post front-matter)
    - AUCUNE ligne de corps v1.0 supprimée NI modifiée.
    - difflib.SequenceMatcher : opcodes limités à {'equal','insert'}.
      ('delete' ou 'replace' => ÉCHEC.)
  FRONT-MATTER
    - id, titre, codename, type, langue, statut : BYTE-EXACT identiques.
      (Suppressions confinées à {version, maj, statut} ; statut ici INCHANGÉ.)
    - version : changée, v1.1 == "1.1" (quotée ; garde YAML-float).
    - maj     : la valeur v1.0 est PRÉSERVÉE VERBATIM (sous-chaîne de la v1.1).
    - prerequis_kb / tags / tags_epistemiques : ADDITIFS (set(v1.0) ⊆ set(v1.1)).
    - aucune clé v1.0 retirée ; clés neuves autorisées (additif).

R-54 : v1.0 lu sur le mount. R-36 : ce script n'embarque aucun sha.
§6.4 : vérifier un patch NE réduit/scelle/construit RIEN.

Usage :
  python verif_cartographie_v11_nonregression.py [V10] [V11]
    V10 défaut : /mnt/project/LC-WORK-CARTOGRAPHIE-PRIORITES.md
    V11 défaut : ./LC-WORK-CARTOGRAPHIE-PRIORITES.md (candidat construit)
  python verif_cartographie_v11_nonregression.py --selftest   (firewall seul)

EXIT 0 = tous les contrôles passent. EXIT 1 = au moins un échec / firewall KO.
"""

import sys
import difflib

try:
    import yaml  # PyYAML
except ImportError:
    sys.stderr.write(
        "ERREUR : PyYAML requis (import yaml). "
        "Installer : pip install --break-system-packages pyyaml\n")
    sys.exit(2)

DEFAULT_V10 = "/mnt/project/LC-WORK-CARTOGRAPHIE-PRIORITES.md"
DEFAULT_V11 = "LC-WORK-CARTOGRAPHIE-PRIORITES.md"

# Champs de front-matter qui DOIVENT rester byte-exact.
FROZEN_FIELDS = ("id", "titre", "codename", "type", "langue", "statut")
# Champs-listes autorisés en AJOUT seulement (jamais de retrait).
ADDITIVE_LIST_FIELDS = ("prerequis_kb", "tags", "tags_epistemiques")


# --------------------------------------------------------------------------- #
#  Découpage front-matter / corps                                             #
# --------------------------------------------------------------------------- #
def split_frontmatter(text):
    """Retourne (fm_dict, body_str). Le corps = tout après le 2e '---'."""
    if not text.startswith("---"):
        raise ValueError("pas de front-matter YAML en tête (---).")
    # 1er fence = ligne 0 ; chercher le fence de fermeture.
    lines = text.split("\n")
    close = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            close = i
            break
    if close is None:
        raise ValueError("front-matter non fermé (--- manquant).")
    fm_raw = "\n".join(lines[1:close])
    body = "\n".join(lines[close + 1:])
    fm = yaml.safe_load(fm_raw)
    if not isinstance(fm, dict):
        raise ValueError("front-matter ne parse pas en dict.")
    return fm, body


# --------------------------------------------------------------------------- #
#  Cœur de validation (opère sur des chaînes -> réutilisable par firewall)    #
# --------------------------------------------------------------------------- #
def validate(v10_text, v11_text):
    """Retourne (passed: bool, results: list[(nom, ok, detail)])."""
    R = []

    def check(name, ok, detail=""):
        R.append((name, bool(ok), detail))
        return bool(ok)

    fm10, body10 = split_frontmatter(v10_text)
    fm11, body11 = split_frontmatter(v11_text)

    # ---- CORPS : zéro ligne perdue / modifiée (difflib) --------------------
    b10 = body10.split("\n")
    b11 = body11.split("\n")
    sm = difflib.SequenceMatcher(a=b10, b=b11, autojunk=False)
    bad_ops = [op for op in sm.get_opcodes() if op[0] in ("delete", "replace")]
    n_equal = sum((i2 - i1) for tag, i1, i2, j1, j2 in sm.get_opcodes()
                  if tag == "equal")
    n_insert = sum((j2 - j1) for tag, i1, i2, j1, j2 in sm.get_opcodes()
                   if tag == "insert")
    check("corps: aucune suppression/modification (opcodes ⊆ equal/insert)",
          not bad_ops,
          "OK : {} lignes conservées, {} insérées".format(n_equal, n_insert)
          if not bad_ops else
          "VIOLATION opcodes={}".format(bad_ops[:5]))
    check("corps: toutes les lignes v1.0 conservées",
          n_equal == len([l for l in b10]),
          "conservées {} / v1.0 {}".format(n_equal, len(b10)))

    # ---- FRONT-MATTER : clés v1.0 non retirées -----------------------------
    missing_keys = [k for k in fm10 if k not in fm11]
    check("front-matter: aucune clé v1.0 retirée",
          not missing_keys,
          "OK" if not missing_keys else "manquantes: {}".format(missing_keys))

    # ---- champs gelés byte-exact -------------------------------------------
    for f in FROZEN_FIELDS:
        if f in fm10:
            check("front-matter[{}] byte-exact".format(f),
                  fm11.get(f) == fm10.get(f),
                  "OK" if fm11.get(f) == fm10.get(f)
                  else "MODIFIÉ (interdit hors {version,maj})")

    # ---- version : bump vers "1.1" -----------------------------------------
    v10v, v11v = str(fm10.get("version")), str(fm11.get("version"))
    check("version: bumpée v1.0->v1.1", v11v == "1.1" and v11v != v10v,
          "v1.0={!r} v1.1={!r}".format(fm10.get("version"),
                                       fm11.get("version")))
    check("version: quotée en str (garde YAML-float)",
          isinstance(fm11.get("version"), str),
          "type={}".format(type(fm11.get("version")).__name__))

    # ---- maj : v1.0 préservée en sous-chaîne -------------------------------
    maj10, maj11 = fm10.get("maj", ""), fm11.get("maj", "")
    check("maj: texte v1.0 préservé verbatim (sous-chaîne)",
          isinstance(maj10, str) and isinstance(maj11, str)
          and maj10 in maj11,
          "OK" if (isinstance(maj10, str) and maj10 in str(maj11))
          else "texte v1.0 ABSENT de la maj v1.1")
    check("maj: v1.1 mentionne l'ancre v1.1",
          "v1.1" in str(maj11),
          "OK" if "v1.1" in str(maj11) else "aucune ancre v1.1")

    # ---- listes additives : set(v1.0) ⊆ set(v1.1) --------------------------
    for f in ADDITIVE_LIST_FIELDS:
        if f in fm10:
            s10 = set(fm10.get(f) or [])
            s11 = set(fm11.get(f) or [])
            removed = s10 - s11
            added = s11 - s10
            check("front-matter[{}] additif (⊆)".format(f),
                  not removed,
                  "OK +{} ajout(s)".format(len(added)) if not removed
                  else "RETRAIT interdit: {}".format(sorted(removed)))

    passed = all(ok for _, ok, _ in R)
    return passed, R


# --------------------------------------------------------------------------- #
#  Firewall : le sceau DOIT rejeter des patchs non conformes                  #
# --------------------------------------------------------------------------- #
_FW_V10 = """---
id: LC-X
titre: "abstract intact ≡ {A4 ; A2★ ; N}"
codename: LC-RACCORD
type: "note"
statut: work-active
version: 1.0
langue: fr
maj: "2026-06-22 — v1.0 : creation."
prerequis_kb: [A, B]
tags: [x, y]
tags_epistemiques: [cartographie]
---
# Titre
ligne un
ligne deux
## 4. Sans surclassement (§6.4)
fin corps v1.0
"""

_FW_V11_OK = """---
id: LC-X
titre: "abstract intact ≡ {A4 ; A2★ ; N}"
codename: LC-RACCORD
type: "note"
statut: work-active
version: "1.1"
langue: fr
maj: "2026-07-20 — v1.1 : addendum. [v1.0] 2026-06-22 — v1.0 : creation."
prerequis_kb: [A, B, C]
tags: [x, y, z]
tags_epistemiques: [cartographie, enregistrement-front]
---
# Titre
ligne un
ligne deux
## 4. Sans surclassement (§6.4)
fin corps v1.0

## 5. Addendum v1.1
contenu neuf
"""

# Mutations qui DOIVENT échouer.
_FW_MUTATIONS = {
    "FW1 corps: ligne supprimée":
        _FW_V11_OK.replace("ligne deux\n", ""),
    "FW2 titre modifié":
        _FW_V11_OK.replace("abstract intact", "abstract MODIFIÉ"),
    "FW3 prerequis retiré":
        _FW_V11_OK.replace("prerequis_kb: [A, B, C]", "prerequis_kb: [A]"),
    "FW4 maj v1.0 non préservée":
        _FW_V11_OK.replace(
            "[v1.0] 2026-06-22 — v1.0 : creation.", "sans tail v1.0."),
    "FW5 statut changé":
        _FW_V11_OK.replace("statut: work-active", "statut: gelé"),
    "FW6 corps: ligne modifiée":
        _FW_V11_OK.replace("ligne un", "ligne un ALTÉRÉE"),
    "FW7 version non bumpée":
        _FW_V11_OK.replace('version: "1.1"', "version: 1.0"),
}


def run_firewall():
    ok_all = True
    # Le cas conforme DOIT passer.
    passed, _ = validate(_FW_V10, _FW_V11_OK)
    tag = "PASS" if passed else "FAIL"
    print("  [firewall] cas conforme -> {} (attendu PASS)".format(tag))
    ok_all &= passed
    # Chaque mutation DOIT échouer.
    for name, mut in _FW_MUTATIONS.items():
        try:
            passed, _ = validate(_FW_V10, mut)
        except Exception as e:  # un parse cassé compte comme rejet
            passed = False
        caught = (not passed)
        print("  [firewall] {:<32} -> {} (attendu REJET)".format(
            name, "REJET" if caught else "NON-CAPTÉ"))
        ok_all &= caught
    return ok_all


# --------------------------------------------------------------------------- #
#  Rapport / main                                                             #
# --------------------------------------------------------------------------- #
def print_report(results):
    width = max(len(n) for n, _, _ in results)
    for name, ok, detail in results:
        print("  [{}] {:<{w}}  {}".format(
            "OK " if ok else "XX ", name, detail, w=width))


def main(argv):
    if "--selftest" in argv:
        print("== FIREWALL (auto-test du sceau) ==")
        ok = run_firewall()
        print("\nFIREWALL:", "OK (7/7 mutations rejetées + conforme accepté)"
              if ok else "ÉCHEC")
        return 0 if ok else 1

    args = [a for a in argv[1:] if not a.startswith("--")]
    v10p = args[0] if len(args) >= 1 else DEFAULT_V10
    v11p = args[1] if len(args) >= 2 else DEFAULT_V11

    print("== FIREWALL (préalable) ==")
    if not run_firewall():
        print("\nFIREWALL ÉCHEC -> sceau non fiable, arrêt.")
        return 1

    print("\n== NON-RÉGRESSION ADDITIVE v1.0 -> v1.1 ==")
    print("  v1.0 (mount, R-54) :", v10p)
    print("  v1.1 (candidat)    :", v11p)
    try:
        with open(v10p, encoding="utf-8") as f:
            v10 = f.read()
    except OSError as e:
        print("  ERREUR lecture v1.0 :", e)
        return 1
    try:
        with open(v11p, encoding="utf-8") as f:
            v11 = f.read()
    except OSError as e:
        print("  v1.1 introuvable :", e)
        print("  (le candidat v1.1 n'est pas encore construit — firewall OK, "
              "checker prêt.)")
        return 1

    passed, results = validate(v10, v11)
    print()
    print_report(results)

    # Diff unifié tronqué, pour l'œil.
    print("\n-- difflib unified_diff (tronqué 40 lignes) --")
    ud = list(difflib.unified_diff(
        v10.split("\n"), v11.split("\n"),
        fromfile="v1.0", tofile="v1.1", lineterm=""))
    for line in ud[:40]:
        print("  " + line)
    if len(ud) > 40:
        print("  ... (+{} lignes de diff)".format(len(ud) - 40))

    print("\nRÉSULTAT:", "NON-RÉGRESSION OK — patch strictement additif."
          if passed else "ÉCHEC — patch NON conforme (voir XX ci-dessus).")
    print("§6.4 : vérifier ce patch ne réduit/scelle/construit RIEN ; "
          "{A4 ; A2★ ; N} INCHANGÉ.")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
