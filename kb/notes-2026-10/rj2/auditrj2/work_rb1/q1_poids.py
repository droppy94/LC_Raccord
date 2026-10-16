# Q1 : tau_jk = Omega^{-3} T(e_j,e_k) = Omega * T_c(e^c_j, e^c_k) pour Omega quelconque
import sympy as sp
from conv import gu, gl, eta, E4, I
from dirac_curved import Geo

t, x, y, z = sp.symbols('t x y z', real=True)
X = (t, x, y, z)

def test(Ec, w, label):
    Om = sp.exp(w)
    Ep = Om*Ec                      # g = Omega^{-2} g_c  =>  e_a = Omega e^c_a
    gc = Geo(Ec, X, c=sp.Rational(-1, 4))
    gp = Geo(Ep, X, c=sp.Rational(-1, 4))
    psi = sp.Matrix([sp.Function('p%d' % i)(*X) for i in range(4)])
    chi = sp.Matrix([[sp.Function('q%d' % i)(*X) for i in range(4)]])   # adjoint traite comme independant (test plus fort)
    psiP = sp.exp(sp.Rational(3, 2)*w)*psi; chiP = sp.exp(sp.Rational(3, 2)*w)*chi
    d1 = sp.simplify(gp.slashD(psiP) - sp.exp(sp.Rational(5, 2)*w)*gc.slashD(psi))
    print(label, "(a) Dslash_phys(Om^{3/2} psi_c) - Om^{5/2} Dslash_c psi_c = 0 :", d1 == sp.zeros(4, 1))
    Tp = gp.T(psiP, chiP); Tc = gc.T(psi, chi)
    d2 = sp.simplify(Tp - Om**2*Tc)
    print(label, "(b) T_{mu nu} - Om^2 T^c_{mu nu} = 0 (coordonnees) :", d2 == sp.zeros(4))
    # (c) composantes de repere : tau_jk = Om^{-3} T(e_j,e_k)  vs  Om T_c(e^c_j,e^c_k)
    tau = sp.Matrix(4, 4, lambda j, k: Om**-3*sum(Ep[j, m]*Ep[k, n]*Tp[m, n] for m in range(4) for n in range(4)))
    Tcf = sp.Matrix(4, 4, lambda j, k: sum(Ec[j, m]*Ec[k, n]*Tc[m, n] for m in range(4) for n in range(4)))
    d3 = sp.simplify(tau - Om*Tcf)
    print(label, "(c) tau_jk - Om T_c(e^c_j,e^c_k) = 0 :", d3 == sp.zeros(4))

w = sp.Function('w')(t, x, y, z)
test(E4, w, "[g_c plat, Omega(t,x,y,z) quelconque]")
A = sp.Function('A')(t, x); B = sp.Function('B')(t, y)
w2 = sp.Function('w')(t, x, y)
test(sp.diag(1/A, 1, 1/B, 1), w2, "[g_c diagonale non plate, Omega(t,x,y)]")
