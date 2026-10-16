# Conventions communes RB-1
# signature (-,+,+,+), {gamma^a, gamma^b} = -2 eta^{ab}  (=> gamma^0^2=+1, gamma^i^2=-1 : matrices de Dirac usuelles)
import sympy as sp

I = sp.I
eta = sp.diag(-1, 1, 1, 1)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -I], [I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
Z2 = sp.zeros(2); I2 = sp.eye(2)
def blk(A, B, C, D):
    M = sp.zeros(4)
    M[:2, :2] = A; M[:2, 2:] = B; M[2:, :2] = C; M[2:, 2:] = D
    return M
gu = [blk(I2, Z2, Z2, -I2)] + [blk(Z2, s, -s, Z2) for s in (s1, s2, s3)]  # gamma^a (indice haut)
gl = [sum((eta[a, b] * gu[b] for b in range(4)), sp.zeros(4)) for a in range(4)]  # gamma_a
E4 = sp.eye(4)
g0 = gu[0]

def check_clifford():
    ok = True
    for a in range(4):
        for b in range(4):
            if sp.simplify(gu[a]*gu[b] + gu[b]*gu[a] + 2*eta[a, b]*E4) != sp.zeros(4):
                ok = False
    return ok

def dbar(M):
    """adjoint de Dirac d'une matrice : gamma^0 M^dagger gamma^0"""
    return g0 * M.H * g0

if __name__ == "__main__":
    print("Clifford {g^a,g^b} = -2 eta^{ab} :", check_clifford())
    print("gamma^0 hermitienne :", gu[0].H == gu[0], "; gamma^i antihermitiennes :", all(gu[i].H == -gu[i] for i in (1, 2, 3)))
    print("gamma^0 gamma^a^dag gamma^0 = gamma^a :", all(sp.simplify(dbar(gu[a]) - gu[a]) == sp.zeros(4) for a in range(4)))
