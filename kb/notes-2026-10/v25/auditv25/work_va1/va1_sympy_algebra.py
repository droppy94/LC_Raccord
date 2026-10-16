# VA-1 : verifications algebriques (sympy)
# Conventions de l'article : {g^a,g^b} = -2 eta^{ab}, eta = diag(-1,1,1,1), representation de Dirac.
import sympy as sp

I = sp.I
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
Z2 = sp.zeros(2); I2 = sp.eye(2)
def blk(a, b, c, d):
    return sp.Matrix(sp.BlockMatrix([[a, b], [c, d]]))
g0 = blk(I2, Z2, Z2, -I2)
gs = [blk(Z2, s, -s, Z2) for s in (s1, s2, s3)]
G = [g0] + gs
eta = sp.diag(-1, 1, 1, 1)
ok = all(sp.simplify(G[a]*G[b] + G[b]*G[a] + 2*eta[a, b]*sp.eye(4)) == sp.zeros(4) for a in range(4) for b in range(4))
print("Clifford {g,g}=-2eta :", ok)
beta = g0
alpha = [g0*g for g in gs]
print("alpha hermitiens :", all(A == A.H for A in alpha))
print("{alpha_i,beta}=0 :", all(A*beta + beta*A == sp.zeros(4) for A in alpha))
g5 = I*G[0]*G[1]*G[2]*G[3]
print("g5^2 =", sp.simplify(g5*g5) == sp.eye(4), " g5 hermitien :", g5 == g5.H,
      " anticommute :", all(g5*g + g*g5 == sp.zeros(4) for g in G))

# ---- Equation de mode : i g^mu d_mu u - m a u = 0, u = e^{ik.x} u(eta)
k1, k2, k3, ma = sp.symbols('k1 k2 k3 ma', real=True)
kv = [k1, k2, k3]
Hk = sum((alpha[i]*kv[i] for i in range(3)), sp.zeros(4)) + beta*ma
# i g0 u' + i g^j (i k_j) u = ma u  ->  u' = -i g0 ( ma - i*i g^j k_j ) ... verifions que u' = -i H u resout
uu = sp.Matrix(sp.symbols('u0:4'))
du = -I*Hk*uu
res = I*g0*du + sum((I*gs[j]*(I*kv[j])*uu for j in range(3)), sp.zeros(4, 1)) - ma*uu
print("Equation (3) [i d_eta u = H u] equivalente a (i Dslash - m a)u=0 :", sp.simplify(res) == sp.zeros(4, 1))

# ---- Tenseur energie-impulsion (forme cinetique symetrisee) sur hat g plat, mode plan
# T_{mn} = (i/4)[psibar g_m d_n psi + psibar g_n d_m psi - (d_n psibar) g_m psi - (d_m psibar) g_n psi]
pr = sp.symbols('p0:4', real=True); qi = sp.symbols('q0:4', real=True)
u = sp.Matrix([pr[j] + I*qi[j] for j in range(4)])
ud = u.H
glow = [eta[a, a]*G[a] for a in range(4)]           # g_mu = eta_{mu nu} g^nu
# derivees : d_eta psi = -i H psi ; d_j psi = i k_j psi
D = [-I*Hk*u] + [I*kv[j]*u for j in range(3)]
Dd = [d.H for d in D]                                # (d psi)^dagger
bar = lambda v: v*g0                                 # psibar = psi^dagger g0 (vecteur ligne)
def T(m, n):
    e = (bar(ud)*glow[m]*D[n] + bar(ud)*glow[n]*D[m] - bar(Dd[n])*glow[m]*u - bar(Dd[m])*glow[n]*u)[0]
    return sp.expand(sp.simplify(I/4*e))
T00 = T(0, 0)
rho = sp.expand((ud*Hk*u)[0])
sgn = sp.simplify(T00/rho) if sp.simplify(T00 - rho) != 0 else 1
print("T_etaeta / (u^dag H u) =", sgn)
norm2 = sp.expand((ud*u)[0])
for i in range(3):
    Ti0 = T(0, i+1)
    print(f"T_eta{i+1} - (signe)*k_{i+1}|u|^2 =", sp.simplify(Ti0 - sgn*kv[i]*norm2), "  (ne contient pas ma :", not Ti0.has(ma), ")")
for i in range(3):
    for j in range(i, 3):
        Tij = T(i+1, j+1)
        cand = -sgn*sp.Rational(1, 2)*(kv[i]*(ud*alpha[j]*u)[0] + kv[j]*(ud*alpha[i]*u)[0])
        print(f"T_{i+1}{j+1} - (-signe/2)(k_i u^dag a_j u + k_j u^dag a_i u) =", sp.simplify(sp.expand(Tij - cand)), " contient ma :", Tij.has(ma))
# trace
tr = -T(0, 0) + sum(T(i, i) for i in (1, 2, 3))
print("trace eta^{mn}T_mn + signe*ma*psibar psi =", sp.simplify(tr + sgn*ma*(bar(ud)*u)[0]))

# ---- Lemme 2 : relation de dispersion de [(Z1+Z2 g5) i g.d - (m + i m5 g5)] psi = 0
Z1, Zb, m, m5, P0, P1, P2, P3 = sp.symbols('Z1 Z2 m m5 P0 P1 P2 P3', real=True)
gp = G[0]*P0 + G[1]*P1 + G[2]*P2 + G[3]*P3          # g^a p_a (psi ~ e^{-i p.x})
Mop = (Z1*sp.eye(4) + Zb*g5)*gp - (m*sp.eye(4) + I*m5*g5)
det = sp.factor(sp.simplify(Mop.det()))
print("det =", det)
target = (Z1**2 - Zb**2)*(P0**2 - P1**2 - P2**2 - P3**2) - (m**2 + m5**2)
print("det = [(Z1^2-Z2^2)(p0^2-p^2) - (m^2+m5^2)]^2 :", sp.simplify(det - target**2) == 0)
print(" => m_eff^2 = (m^2+m5^2)/(Z1^2-Z2^2)  (et non m^2+m5^2 quand Z1^2-Z2^2 != 1)")
# masse apres multiplication par l'inverse : A + B g5 ; est-elle de forme hermitienne m' + i m5' g5 ?
Minv = ((Z1*sp.eye(4) + Zb*g5).inv()*(m*sp.eye(4) + I*m5*g5)).applyfunc(sp.simplify)
A = sp.simplify((Minv*(sp.eye(4)+g5)/2)[0, 0] if False else (Minv.trace()/4))
B = sp.simplify((Minv*g5).trace()/4)
print("Masse effective apres inversion : A =", A, " ; B =", B)
print("  Im(A) =", sp.simplify(sp.im(A)), " Re(B) =", sp.simplify(sp.re(B)), " -> non hermitienne si Z2*m5 != 0 ou Z2*m != 0")

# ---- Annexe A : terme d_a psibar sigma^{ab} d_b psi -> masse constante sur de Sitter
sig = [[I/2*(G[a]*G[b] - G[b]*G[a]) for b in range(4)] for a in range(4)]
ss = sp.zeros(4)
for a in range(4):
    for b in range(4):
        ss += sig[a][b]*eta[a, a]*eta[b, b]*sig[a][b]
print("sigma^{ab} sigma_{ab} =", sp.simplify(ss))
# R_{abcd} = H^2 (g_ac g_bd - g_ad g_bc) ; sigma^{ab} R_{abcd} sigma^{cd}
Hs = sp.symbols('H', positive=True)
acc = sp.zeros(4)
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                R = Hs**2*(eta[a, c]*eta[b, d] - eta[a, d]*eta[b, c])
                if R != 0:
                    acc += sig[a][b]*R*sig[c][d]   # indices de sigma deja hauts, R bas
print("sigma^{ab} R_{abcd} sigma^{cd} (de Sitter) =", sp.simplify(acc), " -> multiple de l'identite : terme de masse constant")
