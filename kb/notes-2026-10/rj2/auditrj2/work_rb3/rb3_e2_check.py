"""RB-3 : co-repere inverse corrige de dirac_op (E2) : E*Ed = Id + O(eps^2) pour h symetrique generique."""
import sympy as sp
eta=sp.diag(-1,1,1,1); eps=sp.Symbol('eps')
h=sp.Matrix(4,4,lambda i,j: sp.Symbol('h%d%d'%(min(i,j),max(i,j))))
E=sp.eye(4)-eps*(eta*h)/2; Ed=sp.eye(4)+eps*(eta*h)/2; Edv1=sp.eye(4)+eps*(h*eta)/2
d=lambda M: (M-sp.eye(4)).applyfunc(lambda x: sp.expand(x).coeff(eps,1))
print("v2 : premier ordre de E*Ed - Id nul :", d(E*Ed).is_zero_matrix, "; Ed*E :", d(Ed*E).is_zero_matrix)
print("v1 : premier ordre de E*Ed - Id :", d(E*Edv1).tolist())
# e^a_mu e^b_nu eta_ab = g_mu nu au premier ordre
print("v2 : Ed^T eta Ed = eta + eps h :", (Ed.T*eta*Ed-eta-eps*h).applyfunc(lambda x: sp.expand(x).coeff(eps,1)).is_zero_matrix)
