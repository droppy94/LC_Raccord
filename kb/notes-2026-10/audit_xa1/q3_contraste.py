import sympy as sp
s=sp.symbols('s',positive=True)
print('EPD (d_s^2+(1/s)d_s) ln s =', sp.simplify(sp.diff(sp.log(s),s,2)+sp.diff(sp.log(s),s)/s))
