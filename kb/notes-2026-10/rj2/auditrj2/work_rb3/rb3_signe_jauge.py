"""RB-3 : variation de h = a^{-2} g - eta sous un diffeomorphisme xi, a = -1/eta, Omega = -eta fixe comme fonction de coordonnee."""
import sympy as sp
X=sp.symbols('eta x y z'); et=X[0]; Om=-et
etam=sp.diag(-1,1,1,1); a=-1/et; g=a**2*etam
xi=[sp.Function('xi%d'%i)(*X) for i in range(4)]
Lg=sp.Matrix(4,4,lambda m,n: sum(xi[c]*sp.diff(g[m,n],X[c]) for c in range(4))+sum(g[c,n]*sp.diff(xi[c],X[m])+g[m,c]*sp.diff(xi[c],X[n]) for c in range(4)))
Leta=sp.Matrix(4,4,lambda m,n: sum(etam[c,n]*sp.diff(xi[c],X[m])+etam[m,c]*sp.diff(xi[c],X[n]) for c in range(4)))
dh=(Lg/a**2).applyfunc(sp.simplify)
print("a^-2 L_xi(a^2 eta) - L_xi eta - 2 (xi^eta/Omega) eta = 0 :", (dh-Leta-2*xi[0]/Om*etam).applyfunc(sp.simplify).is_zero_matrix)
print("a^-2 L_xi(a^2 eta) - L_xi eta + 2 (xi^eta/Omega) eta = 0 :", (dh-Leta+2*xi[0]/Om*etam).applyfunc(sp.simplify).is_zero_matrix)
