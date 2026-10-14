"""wc_t3_cone.py -- solutions homogenes de box^2 singulieres (portees par le cone r = s)."""
import sympy as sp
s,x,y,z=sp.symbols('s x y z',real=True)
box=lambda f: -sp.diff(f,s,2)+sp.diff(f,x,2)+sp.diff(f,y,2)+sp.diff(f,z,2)
r2=x**2+y**2+z**2
for f in [1/(r2-s**2), s/(r2-s**2), sp.log(r2-s**2)]:
    print(f, ": box =", sp.simplify(box(f)), "; box^2 =", sp.simplify(box(box(f))))
print("restriction a r=0 de log(r^2-s^2) :", sp.log(-s**2), "(comportement ln s sur l'axe seulement)")
print("EXIT 0")
