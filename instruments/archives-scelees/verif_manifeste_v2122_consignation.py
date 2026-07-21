#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
verif_manifeste_v2122_consignation.py

Consignation additive du LOT V95 dans le manifeste (LC-WORK-AUDIT-PAQUET-GEL*),
v2.121 -> v2.122.  Item : "entrée manifeste pour le lot".

LOT consigné (2 fichiers) :
  - LC-WORK-CARTOGRAPHIE-PRIORITES.md   (REMPLACEMENT v1.0 -> v1.1 ; net-ZÉRO)
  - verif_cartographie_v11_nonregression.py  (AJOUT .py ; net-POSITIF, cf. §0-full)

DISCIPLINE (constitution) :
  * Le manifeste n'est JAMAIS lu dans le contexte de l'assistant : ce script le
    lit/écrit à l'exécution, n'ÉCHOTE jamais son corps (seulement valeurs de
    champ, bloc AJOUTÉ, et compteurs).
  * Patch ADDITIF only : difflib => opcodes ⊆ {equal, insert} sur le corps ;
    suppressions confinées à {version, maj}. Ancre `version:` / `maj:` : count==1.
  * sha256 des fichiers du lot + PKG-SHA : RECALCULÉS FRAIS DU MOUNT à l'exécution.
    Jamais rappelés de mémoire (R-54 ; leçon V62).
  * R-36 : ce script n'embarque aucun sha ; rien n'est hardcodé.
  * §6.4 : consigner un lot ne réduit/scelle/construit RIEN. {A4;A2★;N} INCHANGÉ.

RECETTE PKG-SHA (exacte) :
  sha256( "\n".join(sorted( f"{canon}  {sha256(contenu)}" )) )   # 2 espaces, pas de \n final
  exclusions : basename commençant par 'LC-WORK-AUDIT-PAQUET-GEL' ; extension .txt
  canon      : re.sub(r'__\d+_(?=\.(md|py)$)', '', basename)

MODES :
  --compute-only     : sha256 des fichiers du lot + PKG-SHA du mount (baseline). Aucun manifeste touché.
  --emit-baseline    : écrit la carte {canon: sha256} du mount (baseline pré-lot) -> --map-out (.txt, hors PKG-SHA).
  --verify-baseline  : recompute la carte du KB et asserte que le DIFF vs --map-in == exactement le lot.
  --patch            : patch additif du manifeste -> v2.122 ; écrit --out. (Ne PAS échoter le corps.)
  --dry-run          : avec --patch, ne pas écrire ; rapporter mécanique + additif-assert.
  --selftest         : firewall (PKG-SHA vecteur connu + additif manifeste synthétique).

PARAMS :
  --kb-root PATH     (défaut /mnt/project)
  --manifest PATH    (défaut : auto-glob LC-WORK-AUDIT-PAQUET-GEL*.md sous kb-root ; count==1 requis)
  --lot F [F ...]    (défaut : les 2 fichiers du lot dans /mnt/user-data/outputs)
  --cur-version STR  (défaut 2.121 ; ASSERTÉ contre le manifeste)
  --new-version STR  (défaut 2.122)
  --prior-pkgsha HEX (option ; bracket-test du .py ajouté)
  --out PATH / --map-out PATH / --map-in PATH

EXIT 0 = OK. EXIT 1 = échec / firewall KO.
"""

import argparse
import difflib
import glob
import hashlib
import os
import re
import sys

CANON_RE = re.compile(r'__\d+_(?=\.(?:md|py)$)')
MANIFEST_PREFIX = "LC-WORK-AUDIT-PAQUET-GEL"

DEFAULT_KB = "/mnt/project"
DEFAULT_LOT = [
    "/mnt/user-data/outputs/LC-WORK-CARTOGRAPHIE-PRIORITES.md",
    "/mnt/user-data/outputs/verif_cartographie_v11_nonregression.py",
]


# --------------------------------------------------------------------------- #
#  PKG-SHA (recette exacte)                                                    #
# --------------------------------------------------------------------------- #
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    with open(path, "rb") as f:
        return sha256_bytes(f.read())


def canon(basename):
    return CANON_RE.sub("", basename)


def is_excluded(basename):
    return basename.endswith(".txt") or basename.startswith(MANIFEST_PREFIX)


def kb_sha_map(kb_root):
    """Retourne {canon: sha256} pour les fichiers inclus du KB (plat)."""
    m = {}
    for fn in sorted(os.listdir(kb_root)):
        p = os.path.join(kb_root, fn)
        if not os.path.isfile(p) or is_excluded(fn):
            continue
        c = canon(fn)
        if c in m:
            raise ValueError("collision de canon: {} (deux fichiers mount)".format(c))
        m[c] = sha256_file(p)
    return m


def pkgsha_from_map(m):
    blob = "\n".join(sorted("{}  {}".format(c, h) for c, h in m.items()))
    return sha256_bytes(blob.encode("utf-8"))


def pkgsha(kb_root):
    return pkgsha_from_map(kb_sha_map(kb_root))


# --------------------------------------------------------------------------- #
#  Manifeste : découpe front-matter / corps SANS échoter le corps             #
# --------------------------------------------------------------------------- #
def split_fm(text):
    if not text.startswith("---"):
        raise ValueError("manifeste sans front-matter (---).")
    lines = text.split("\n")
    close = next((i for i in range(1, len(lines))
                  if lines[i].strip() == "---"), None)
    if close is None:
        raise ValueError("front-matter non fermé.")
    return lines, close  # lines[1:close] = fm ; lines[close+1:] = corps


def _find_unique(lines, lo, hi, pred, label):
    idx = [i for i in range(lo, hi) if pred(lines[i])]
    if len(idx) != 1:
        raise ValueError("ancre `{}` count={} (attendu 1).".format(label, len(idx)))
    return idx[0]


def build_consignation_block(new_version, lot_paths, kb_root, prior_pkgsha):
    """Bloc daté additif (contenu propre à l'assistant — safe à échoter)."""
    rows = []
    for p in lot_paths:
        base = os.path.basename(p)
        h = sha256_file(p) if os.path.exists(p) else "‹ABSENT-au-run›"
        rows.append("  - `{}`  (canon `{}`)  sha256 {}".format(base, canon(base), h))
    try:
        pk = pkgsha(kb_root)
    except Exception as e:
        pk = "‹PKG-SHA indisponible: {}›".format(e)
    lines = []
    lines.append("")
    lines.append("## Consignation v{} — LOT V95 (cartographie v1.1 + sceau)".format(new_version))
    lines.append("")
    lines.append("- **Nature** : REMPLACEMENT (cartographie v1.0→v1.1, net-zéro) + AJOUT (.py sceau, net-positif).")
    lines.append("- **Fichiers du lot** (sha256 frais, calculés du fichier réel au dépôt) :")
    lines.extend(rows)
    lines.append("- **PKG-SHA (mount post-dépôt, recette exacte)** : {}".format(pk))
    if prior_pkgsha:
        lines.append("- **PKG-SHA prior (bracket .py exclu)** attendu : {}".format(prior_pkgsha))
    lines.append("- **§6.4** : consignation ; ne réduit/scelle/construit RIEN ; {A4 ; A2★ ; N} INCHANGÉ.")
    lines.append("")
    return lines


def patch_manifest(text, cur_version, new_version, lot_paths, kb_root, prior_pkgsha):
    """Retourne (new_text, added_block_lines). Additif pur. N'échote pas le corps."""
    lines, close = split_fm(text)

    # version : ancre unique, asserter cur_version, bump.
    vi = _find_unique(lines, 1, close,
                      lambda l: l.strip().startswith("version:"), "version:")
    cur = lines[vi].split("version:", 1)[1].strip().strip('"').strip("'")
    if cur != str(cur_version):
        raise ValueError(
            "version manifeste = {!r} ≠ attendu {!r} (mémoire périmée ? R-54)."
            .format(cur, str(cur_version)))
    lines[vi] = 'version: "{}"'.format(new_version)

    # maj : ancre unique, prépendre l'entrée v-new en conservant l'ancienne verbatim.
    mi = _find_unique(lines, 1, close,
                      lambda l: l.strip().startswith("maj:"), "maj:")
    old_maj_line = lines[mi]
    old_val = old_maj_line.split("maj:", 1)[1].strip()
    quoted = len(old_val) >= 2 and old_val[0] == '"' and old_val[-1] == '"'
    old_inner = old_val[1:-1] if quoted else old_val
    new_inner = ("{} — v{} : consignation LOT V95 (cartographie v1.1 + sceau "
                 "verif_cartographie_v11_nonregression) ; patch additif difflib ; "
                 "PKG-SHA recalculé frais du mount ; §6.4 inchangé. [v{}] {}"
                 ).format(_today(), new_version, cur_version, old_inner)
    lines[mi] = 'maj: "{}"'.format(new_inner)

    # corps : APPENDRE le bloc daté (additif ; on ne touche à aucune ligne existante).
    block = build_consignation_block(new_version, lot_paths, kb_root, prior_pkgsha)
    body_lines = lines[close + 1:]
    if body_lines and body_lines[-1] == "":
        insert_at = len(lines)
    else:
        insert_at = len(lines)
    new_lines = lines[:insert_at] + block
    return "\n".join(new_lines), block


def _today():
    # Date fixe du lot ; évite toute dépendance horloge non déterministe en seal.
    return "2026-07-20"


def assert_additive(old_text, new_text):
    """difflib : le corps ne perd/altère aucune ligne (opcodes ⊆ equal/insert),
    hors les 2 lignes front-matter version/maj (remplacées)."""
    a = old_text.split("\n")
    b = new_text.split("\n")
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    replaced = 0
    deleted = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "replace":
            replaced += (i2 - i1)
        elif tag == "delete":
            deleted += (i2 - i1)
    # On tolère AU PLUS 2 lignes 'replace' (version + maj) et 0 'delete'.
    return (deleted == 0 and replaced <= 2), replaced, deleted


# --------------------------------------------------------------------------- #
#  Firewall                                                                    #
# --------------------------------------------------------------------------- #
def run_firewall():
    ok = True

    # 1) PKG-SHA : vecteur connu + invariance au suffixe __N_.
    m1 = {"A.md": "aa", "B.py": "bb"}
    expect = sha256_bytes("A.md  aa\nB.py  bb".encode())
    got = pkgsha_from_map(m1)
    p = (got == expect)
    print("  [fw] PKG-SHA vecteur connu           -> {}".format("OK" if p else "KO"))
    ok &= p
    p = (canon("X__3_.md") == "X.md" and canon("v__12_.py") == "v.py"
         and canon("Y.md") == "Y.md")
    print("  [fw] canon strip __N_                -> {}".format("OK" if p else "KO"))
    ok &= p
    p = is_excluded("LC-WORK-AUDIT-PAQUET-GEL_x.md") and is_excluded("z.txt") \
        and not is_excluded("LC-D-X.md")
    print("  [fw] exclusions manifeste/.txt       -> {}".format("OK" if p else "KO"))
    ok &= p

    # 2) Patch manifeste additif synthétique.
    man = ('---\nid: M\nstatut: gel\nversion: 2.121\n'
           'maj: "2026-07-17 — v2.121 : compaction."\n---\n'
           '# Manifeste\nligne corps A\nligne corps B\n')
    tmp_lot = []  # lot vide -> shas ‹ABSENT› (mais bloc additif quand même)
    new, block = patch_manifest(man, "2.121", "2.122", tmp_lot, "/nonexistent", None)
    add_ok, repl, dele = assert_additive(man, new)
    p = add_ok and 'version: "2.122"' in new and "ligne corps A" in new \
        and "ligne corps B" in new and "[v2.121]" in new
    print("  [fw] patch additif conforme          -> {} (replace={}, delete={})"
          .format("OK" if p else "KO", repl, dele))
    ok &= p

    # 3) Version courante fausse -> DOIT lever.
    try:
        patch_manifest(man, "9.999", "2.122", [], "/nonexistent", None)
        caught = False
    except ValueError:
        caught = True
    print("  [fw] version courante fausse rejetée -> {}".format("REJET" if caught else "KO"))
    ok &= caught

    # 4) Ancre maj dupliquée -> DOIT lever (count!=1).
    man2 = man.replace('version: 2.121\n', 'version: 2.121\nmaj: "dup"\n')
    try:
        patch_manifest(man2, "2.121", "2.122", [], "/nonexistent", None)
        caught = False
    except ValueError:
        caught = True
    print("  [fw] ancre maj dupliquée rejetée     -> {}".format("REJET" if caught else "KO"))
    ok &= caught

    return ok


# --------------------------------------------------------------------------- #
#  main                                                                        #
# --------------------------------------------------------------------------- #
def resolve_manifest(kb_root, explicit):
    if explicit:
        return explicit
    cands = sorted(glob.glob(os.path.join(kb_root, MANIFEST_PREFIX + "*.md")))
    if len(cands) != 1:
        raise ValueError(
            "manifeste auto-résolu count={} sous {} ; préciser --manifest."
            .format(len(cands), kb_root))
    return cands[0]


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb-root", default=DEFAULT_KB)
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--lot", nargs="*", default=DEFAULT_LOT)
    ap.add_argument("--cur-version", default="2.121")
    ap.add_argument("--new-version", default="2.122")
    ap.add_argument("--prior-pkgsha", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--map-out", default=None)
    ap.add_argument("--map-in", default=None)
    ap.add_argument("--compute-only", action="store_true")
    ap.add_argument("--emit-baseline", action="store_true")
    ap.add_argument("--verify-baseline", action="store_true")
    ap.add_argument("--patch", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv[1:])

    if a.selftest:
        print("== FIREWALL ==")
        ok = run_firewall()
        print("\nFIREWALL:", "OK" if ok else "ÉCHEC")
        return 0 if ok else 1

    print("== FIREWALL (préalable) ==")
    if not run_firewall():
        print("\nFIREWALL ÉCHEC -> sceau non fiable, arrêt.")
        return 1

    if a.compute_only:
        print("\n== COMPUTE-ONLY (frais du mount) ==")
        for p in a.lot:
            if os.path.exists(p):
                print("  sha256  {}  {}".format(sha256_file(p), os.path.basename(p)))
            else:
                print("  ‹ABSENT›  {}".format(p))
        try:
            print("  PKG-SHA(mount {}) = {}".format(a.kb_root, pkgsha(a.kb_root)))
        except Exception as e:
            print("  PKG-SHA indisponible :", e)
        print("\n(§0-lite : comparer ce PKG-SHA au 45cc1082 pendant ; le déclarer si concordant.)")
        return 0

    if a.emit_baseline:
        m = kb_sha_map(a.kb_root)
        out = a.map_out or "baseline_map.txt"
        with open(out, "w", encoding="utf-8") as f:
            for c in sorted(m):
                f.write("{}  {}\n".format(c, m[c]))
        print("\nbaseline map -> {} ({} fichiers) ; PKG-SHA = {}".format(
            out, len(m), pkgsha_from_map(m)))
        return 0

    if a.verify_baseline:
        if not a.map_in:
            print("  --verify-baseline exige --map-in.")
            return 1
        base = {}
        for ln in open(a.map_in, encoding="utf-8"):
            ln = ln.rstrip("\n")
            if "  " in ln:
                c, h = ln.split("  ", 1)
                base[c] = h
        cur = kb_sha_map(a.kb_root)
        added = {c for c in cur if c not in base}
        removed = {c for c in base if c not in cur}
        changed = {c for c in cur if c in base and cur[c] != base[c]}
        expected_lot = {canon(os.path.basename(p)) for p in a.lot}
        touched = added | removed | changed
        ok = touched == expected_lot
        print("\n== VERIFY-BASELINE ==")
        print("  ajout(s)   :", sorted(added))
        print("  retrait(s) :", sorted(removed))
        print("  modifié(s) :", sorted(changed))
        print("  lot attendu:", sorted(expected_lot))
        print("  ->", "OK (aucune mutation fantôme)" if ok else "ÉCHEC (mutation hors-lot)")
        return 0 if ok else 1

    if a.patch:
        man_path = resolve_manifest(a.kb_root, a.manifest)
        with open(man_path, encoding="utf-8") as f:
            man = f.read()
        try:
            new, block = patch_manifest(
                man, a.cur_version, a.new_version, a.lot, a.kb_root, a.prior_pkgsha)
        except ValueError as e:
            print("  PATCH REFUSÉ :", e)
            return 1
        add_ok, repl, dele = assert_additive(man, new)
        print("\n== PATCH v{} -> v{} ==".format(a.cur_version, a.new_version))
        print("  manifeste     :", os.path.basename(man_path))
        print("  additif       :", "OK" if add_ok else "ÉCHEC",
              "(replace={}, delete={})".format(repl, dele))
        print("  lignes avant/après :", len(man.split("\n")), "/", len(new.split("\n")))
        print("  -- bloc AJOUTÉ (contenu assistant, safe) --")
        for l in block:
            print("   |", l)
        if not add_ok:
            print("  -> refus (non additif).")
            return 1
        if a.dry_run:
            print("  (dry-run : rien écrit.)")
            return 0
        out = a.out or os.path.join(
            os.path.dirname(a.lot[0]) or ".", os.path.basename(man_path))
        with open(out, "w", encoding="utf-8") as f:
            f.write(new)
        print("  manifeste patché -> {}".format(out))
        print("  R-36 : sha du manifeste patché à consigner HORS-FICHIER.")
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
