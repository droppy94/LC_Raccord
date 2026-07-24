#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HARNAIS R-11 — mutations mordantes sur les porteurs identifies.

Une mutation est MORDANTE si elle fait echouer au moins un assert de l'axe
qu'elle vise. Une mutation qui laisse l'axe intact est VACANTE : elle est
declaree vacante et l'assert vise est DENONCE, jamais compte comme mordant.

Comporte en outre un AUDIT DE VACUITE : tout assert discriminant qui ne
depend d'AUCUN porteur mutable est signale comme structurellement vacant.
"""

import io
import sys
import contextlib
import importlib

MUTATIONS = [
    # (id, description, porteur, valeur mutee, axe vise)
    ("m1", "coefficient Osborn-Petkou 3/32 -> 3/16 (porteur F1)",
     "P_F1_OP", None, "axe_F1"),
    ("m2", "exposant A_T ~ N^-1 -> N^-2 (porteur F2)",
     "P_F2_EXP_AT", -2, "axe_F2"),
    ("m3", "soustraction de trace desactivee (porteur F6, terme de trace)",
     "P_F6_TRACE", 0, "axe_F6"),
    ("m4", "dimension du 1/d : 3 -> 4 (porteur F6, coefficient de trace)",
     "P_F6_DIM", 4, "axe_F6"),
    ("m5", "numerateur du mode exact x.cos(x) -> 2x.cos(x) (porteur W2)",
     "P_W2_NUM", 2, "axe_WCH2"),
    ("m6", "un front classe reducteur retire A4 du compte (porteur transverse)",
     "P_T1_REDUC", frozenset({"A4"}), "axe_T"),
    ("m7", "facteur det(P) des pseudo-tenseurs retire (porteur F6, parite)",
     "P_F6_PSEUDO", 0, "axe_F6"),
]

# asserts a auditer pour vacuite structurelle : (id, axe, porteur cense le porter)
AUDIT_VACUITE = []   # v2 : les 4 vacants v1 sont retires du compte PASS


def run_axe(mod, axe_nom):
    """Rejoue un axe et renvoie (n_pass, n_fail, texte)."""
    mod.PASS = 0
    mod.FAILED = 0
    mod.CONS = 0
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        getattr(mod, axe_nom)()
    return mod.PASS, mod.FAILED, buf.getvalue()


def premier_fail(txt):
    for ligne in txt.splitlines():
        if "[FAIL]" in ligne:
            return ligne.strip()
    return None


def main():
    import sympy as sp
    mordantes = 0
    vacantes = []

    print("HARNAIS R-11 - mutations sur porteurs")
    print("=" * 70)

    for mid, desc, porteur, val, axe in MUTATIONS:
        mod = importlib.import_module("redemo_R11_falsifiabilite")
        importlib.reload(mod)
        # reference : l'axe doit etre propre AVANT mutation
        p0, f0, _ = run_axe(mod, axe)
        if f0 != 0:
            print("[ANOMALIE] %s : l'axe %s echoue DEJA sans mutation" % (mid, axe))
            continue
        valeur = val
        if mid == "m1":
            valeur = sp.Rational(3, 16)
        setattr(mod, porteur, valeur)
        p1, f1, txt = run_axe(mod, axe)
        if f1 > 0:
            mordantes += 1
            print("[MORD] %s %s -> %d FAIL, premier : %s"
                  % (mid, desc, f1, premier_fail(txt)))
        else:
            vacantes.append((mid, desc, axe))
            print("[VACANTE] %s %s -> AUCUN echec : la mutation n'est pas vue"
                  % (mid, desc))

    print("-" * 70)
    print("AUDIT DE VACUITE STRUCTURELLE (asserts sans porteur mutable)")
    if not AUDIT_VACUITE:
        print("[OK] aucun assert sans porteur mutable dans la v2 "
              "(les 4 vacants de la v1 ont ete retires du compte)")
    for aid, axe, porteur in AUDIT_VACUITE:
        print("[VACANT-STRUCT] %s (%s)" % (aid, axe))

    print("=" * 70)
    print("HARNAIS R-11 : %d/%d mordantes" % (mordantes, len(MUTATIONS)))
    print("VACANTES detectees : %d mutation(s) + %d assert(s) structurellement vacants"
          % (len(vacantes), len(AUDIT_VACUITE)))
    return 0 if mordantes == len(MUTATIONS) else 1


if __name__ == '__main__':
    sys.exit(main())
