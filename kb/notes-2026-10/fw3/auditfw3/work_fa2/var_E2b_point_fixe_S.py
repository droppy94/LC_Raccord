#!/usr/bin/env python3
"""var_E2b_point_fixe_S.py -- audit FA-2 (reprise), point E2 (circularite). Le script traite T* = S_ab et Omega^-2 That = Str
comme des symboles generiques, alors qu'avec xi != 0 That depend lui-meme de S, Str (via dd Omega (2.14) et n.n (3.8) dans
les termes d'amelioration). On mesure l'ordre en Omega auquel S, Str, s, L entrent dans That_ab (indices bas) et dans
Omega^-2 That : si c'est >= 1, l'equation implicite S = T*[jets ; S, Str] se resout par point fixe en une fonction reguliere.
"""
import sympy as sp
from fw3_fa2_lib import *
J = Jet('friedrich')
That, ex = build_matter(J, xi, gauge=True, ym=True)
tr = sp.expand(sum(ghatinv[a, b]*That[a, b] for a in idx for b in idx)/W**2)
def low(expr, syms):
    out = 99
    for z in syms:
        d = sp.expand(sp.diff(expr, z))
        if d != 0:
            lv = laurent(reduce_nn(d)); out = min(out, min(lv) if lv else 99)
    return out
groups = {'S_ab': list(set(S)), 'Str': [Str], 's': [s], 'L_ab': list(set(L))}
for name, syms in groups.items():
    lt = min(low(That[a, b], syms) for a in idx for b in idx)
    print(f"  {name} : plus basse puissance de Omega dans d That_ab / d {name} : {lt} ; dans d(Omega^-2 That)/d {name} : {low(tr, syms)}")
