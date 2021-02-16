import scipy.optimize as scope
from math import inf

case = 0

def optimize(f):
    if (f == E2):
        alpha = [0.1]
    elif(f == E3):
        alpha = [0.01, 0.01]
    elif(f == E4):
        if (case == 1):
            alpha = [0.1, 0.1]
        elif ((case == 2) or (case == 3) or (case == 4) or (case == 5)):
            alpha = [0.1]

    res = scope.minimize(f, alpha)
    print (res)

def f1(x):
    return (x**2) + 2

def setValuesForThirdOrderCase1(alpha):
    c2 = alpha[0]
    c3 = alpha[1]
    b1 = (2 - (3 * (c2 + c3)) + (6 * c2 * c3)) / (6 * c2 * c3)
    b2 = (c3 - (2/3)) / (2 * c2 * (c3 - c2))
    b3 = ((2/3) - c2) / (2 * c3 * (c3 - c2))
    a31 = (c3 * (c3 - (3 * c2) + (3 * c2 * c2))) / (c2 * ((3 * c2) - 2))
    a32 = (c3 * (c2 - c3)) / (c2 * ((3 * c2) - 2))

    return c2, c3, b1, b2, b3, a31, a32

def E2(alpha):
    b = [1 - (1 / (2 * alpha[0])), 1 / (2 * alpha[0])]
    c = [0, alpha[0]]
    A = [[0, 0], [alpha[0], 0]]

    csq = [c[0] ** 2, c[1] ** 2]
    bcsq = (b[0] * csq[0]) + (b[1] * csq[1])
    Ac = [(A[0][0] * c[0]) + (A[0][1] * c[1]),(A[1][0] * c[0]) + (A[1][1] * c[1])]
    bAc = (b[0] * Ac[0]) + (b[1] * Ac[1])
    result = (((1/2) * (bcsq - (1/3))) ** 2) + ((bAc - (1/6)) ** 2)

    return result

def E3Eq1(c, b, A):
    #For Equation 1, find b*c^3
    ccube = [c[0] ** 3, c[1] ** 3, c[2] ** 3]
    bccube = (b[0] * ccube[0]) + (b[1] * ccube[1]) + (b[2] * ccube[2])

    return ((1/6) * (bccube - (1/4)))

def E3Eq2(c, b, A):
    #For Equation 2, find b*c*A*c
    bc = [(b[0] * c[0]), (b[1] * c[1]), (b[2] * c[2])]
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]))]
    bcAc = (bc[0] * Ac[0]) + (bc[1] * Ac[1]) + (bc[2] * Ac[2])

    return (bcAc - (1/8))

def E3Eq3(c, b, A):
    #For Equation 3, find b*A*c^2
    csq = [c[0] ** 2, c[1] ** 2, c[2] ** 2]
    Acsq = [((A[0][0] * csq[0]) + (A[0][1] * csq[1]) + (A[0][2] * csq[2])),
          ((A[1][0] * csq[0]) + (A[1][1] * csq[1]) + (A[1][2] * csq[2])),
          ((A[2][0] * csq[0]) + (A[2][1] * csq[1]) + (A[2][2] * csq[2]))]
    bAcsq = (b[0] * Acsq[0]) + (b[1] * Acsq[1]) + (b[2] * Acsq[2])

    return ((1/2) * (bAcsq - (1/12)))

def E3Eq4(c, b, A):
    #For Equation 4, find b*A^2*c
    Asq = []
    for i in range (0, len(A)):
        Asq.append([])
        for j in range (0, len(A)):
            Asq[i].append((A[i][0] * A[0][j]) + (A[i][1] * A[1][j]) + (A[i][2] * A[2][j]))
            
    Asqc = [((Asq[0][0] * c[0]) + (Asq[0][1] * c[1]) + (Asq[0][2] * c[2])),
          ((Asq[1][0] * c[0]) + (Asq[1][1] * c[1]) + (Asq[1][2] * c[2])),
          ((Asq[2][0] * c[0]) + (Asq[2][1] * c[1]) + (Asq[2][2] * c[2]))]
    bAsqc = (b[0] * Asqc[0]) + (b[1] * Asqc[1]) + (b[2] * Asqc[2])

    return (bAsqc - (1/24))

def E3(alpha):
    if ((alpha[0] == 0) or (alpha[0] == 2/3) or (alpha[1] == 0) or (alpha[0] == alpha[1])):
        return 1
    
    c2, c3, b1, b2, b3, a31, a32 = setValuesForThirdOrderCase1(alpha)

    c = [0, c2, c3]
    b = [b1, b2, b3]
    A = [[0, 0, 0],[c2, 0, 0],[a31, a32, 0]]

    #For Equation 1, find b*c^3
    eq1 = E3Eq1(c, b, A)

    #For Equation 2, find b*c*A*c
    eq2 = E3Eq2(c, b, A)

    #For Equation 3, find b*A*c^2
    eq3 = E3Eq3(c, b, A)

    #For Equation 4, find b*A^2*c
    eq4 = E3Eq4(c, b, A)

    #E3^2
    result = (eq1 ** 2) + (eq2 ** 2) + (eq3 ** 2) + (eq4 ** 2)

    return result

def E4(alpha):
    return 0

optimize(E3)

#print (E3([0.5, 0.75]))
