import scipy.optimize as scope
from math import inf

case = 0

def optimize(f):
    if (f == E2):
        alpha = [0.1]
    elif(f == E3):
        if (case == 1):
            alpha = [0.01, 0.01]
        elif ((case == 2) or (case == 3)):
            alpha = [0.01]
    elif(f == E4):
        if (case == 1):
            alpha = [0.1, 0.1]
        elif ((case == 2) or (case == 3) or (case == 4) or (case == 5)):
            alpha = [0.1]

    res = scope.minimize(f, alpha)
    print (res)

def f1(x):
    return (x**2) + 2

def setValuesForThirdOrder(alpha):
    if (case == 1):
        c2 = alpha[0]
        c3 = alpha[1]
        b1 = (2 - (3 * (c2 + c3)) + (6 * c2 * c3)) / (6 * c2 * c3)
        b2 = (c3 - (2/3)) / (2 * c2 * (c3 - c2))
        b3 = ((2/3) - c2) / (2 * c3 * (c3 - c2))
        a31 = (c3 * (c3 - (3 * c2) + (3 * c2 * c2))) / (c2 * ((3 * c2) - 2))
        a32 = (c3 * (c2 - c3)) / (c2 * ((3 * c2) - 2))
    elif (case == 2):
        c2 = 2/3
        c3 = 0
        b3 = alpha[0]
        b1 = (1/4) - b3
        b2 = 3/4
        a31 = -1 / (4 * b3)
        a32 = 1 / (4 * b3)
    else:
        c2 = c3 = 2/3
        b3 = alpha[0]
        b1 = 1/4
        b2 = (3/4) - b3
        a31 = ((8 * b3) - 3) / (12 * b3)
        a32 = 1 / (4 * b3)

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

def E3(alpha):
    if (case == 1):
        if ((alpha[0] == 0) or (alpha[0] == 2/3) or (alpha[1] == 0) or (alpha[0] == alpha[1])):
            print (inf)
            return inf
    elif (alpha[0] == 0):
        print (inf)
        return inf

    print (alpha)
    c2, c3, b1, b2, b3, a31, a32 = setValuesForThirdOrder(alpha)

    c = [0, c2, c3]
    b = [b1, b2, b3]
    A = [[0, 0, 0],[c2, 0, 0],[a31, a32, 0]]

    #For Equation 1, find b*c^3
    ccube = [c[0] ** 3, c[1] ** 3, c[2] ** 3]
    bccube = (b[0] * ccube[0]) + (b[1] * ccube[1]) + (b[2] * ccube[2])

    #For Equation 2, find b*c*A*c
    bc = [(b[0] * c[0]), (b[1] * c[1]), (b[2] * c[2])]
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]))]
    bcAc = (bc[0] * Ac[0]) + (bc[1] * Ac[1]) + (bc[2] * Ac[2])

    #For Equation 3, find b*A*c^2
    csq = [c[0] ** 2, c[1] ** 2, c[2] ** 2]
    Acsq = [((A[0][0] * csq[0]) + (A[0][1] * csq[1]) + (A[0][2] * csq[2])),
          ((A[1][0] * csq[0]) + (A[1][1] * csq[1]) + (A[1][2] * csq[2])),
          ((A[2][0] * csq[0]) + (A[2][1] * csq[1]) + (A[2][2] * csq[2]))]
    bAcsq = (b[0] * Acsq[0]) + (b[1] * Acsq[1]) + (b[2] * Acsq[2])

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

    #E3^2
    result = (((1/6) * (bccube - (1/4))) ** 2) + ((bcAc - (1/8)) ** 2) + (((1/2) * (bAcsq - (1/12))) ** 2) + ((bAsqc - (1/24)) ** 2)

    return result

def E4(alpha):
    return 0

case = 1

#optimize(E3)

#print (E3([0.5, 0.75]))
