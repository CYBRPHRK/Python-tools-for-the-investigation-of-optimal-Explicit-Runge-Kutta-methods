import scipy.optimize as scope
from math import inf
import Logger.Logger as logger

case = 0

def optimize(f):
    if (f == E2):
        alpha = [0.1]
    elif(f == E3):
        alpha = [0.01, 0.01]
    elif(f == E4):
        if (case == 1):
            alpha = [0.1, 0.2]
        elif ((case == 2) or (case == 3) or (case == 4) or (case == 5)):
            alpha = [0.1]
            
    log.info("alpha: ", alpha)
    res = scope.minimize(f, alpha, tol=1e-8)
    print (res)

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

def setValuesForThirdOrderCase1(alpha):
    c2 = alpha[0]
    c3 = alpha[1]
    b1 = (2 - (3 * (c2 + c3)) + (6 * c2 * c3)) / (6 * c2 * c3)
    b2 = (c3 - (2/3)) / (2 * c2 * (c3 - c2))
    b3 = ((2/3) - c2) / (2 * c3 * (c3 - c2))
    a31 = (c3 * (c3 - (3 * c2) + (3 * c2 * c2))) / (c2 * ((3 * c2) - 2))
    a32 = (c3 * (c2 - c3)) / (c2 * ((3 * c2) - 2))

    log.info("Coefficients selected for E3 are:")
    log.info("c2, c3, b1, b2, b3, a31, a32", c2, c3, b1, b2, b3, a31, a32)
    return c2, c3, b1, b2, b3, a31, a32

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

    #For Equation 1
    eq1 = E3Eq1(c, b, A)

    #For Equation 2
    eq2 = E3Eq2(c, b, A)

    #For Equation 3
    eq3 = E3Eq3(c, b, A)

    #For Equation 4
    eq4 = E3Eq4(c, b, A)

    #E3^2
    result = (eq1 ** 2) + (eq2 ** 2) + (eq3 ** 2) + (eq4 ** 2)

    return result

def setValuesForFourthOrder(alpha):
    if (case == 1):
        c2 = alpha[0]
        c3 = alpha[1]
        c4 = 1
        a31 = (c3 * ((3 * c2) - c3 - (4 * c2 * c2))) / (2 * c2 * (1 - (2 * c2)))
        a32 = (c3 * (c3 - c2)) / (2 * c2 * (1 - (2 * c2)))
        a41 = (((c3 ** 2) * ((12 * c2 * c2) - (12 * c2) + 4)) - (c3 * ((12 * c2 * c2) - (15 * c2) + 5)) + ((4 * c2 * c2) - (6 * c2) + 2)) / ((2 * c2 * c3) * (3 - (4 * (c2 + c3)) + (6 * c2 * c3)))
        a42 = (((-4 * c3 * c3) + (5 * c3) + c2 - 2) * (1 - c2)) / ((2 * c2) * (c3 - c2) * (3 - (4 * (c2 + c3)) + (6 * c2 * c3)))
        a43 = ((1 - (2 * c2)) * (1 - c3) * (1 - c2)) / (c3 * (c3 - c2) * (3 - (4 * (c2 + c3)) + (6 * c2 * c3)))
        b1 = (1 - (2 * (c2 + c3)) + (6 * c2 * c3)) / (12 * c2 * c3)
        b2 = ((2 * c3) - 1) / ((12 * c2) * (c3 - c2) * (1 - c2))
        b3 = (1 - (2 * c2)) / ((12 * c3) * (c3 - c2) * (1 - c3))
        b4 = (3 - (4 * (c2 + c3)) + (6 * c2 * c3)) / (12 * (1 - c2) * (1 - c3))
    elif (case == 2):
        b3 = alpha[0]
        c2 = c3 = 1/2
        c4 = 1
        a31 = ((3 * b3) - 1) / (6 * b3)
        a32 = 1 / (6 * b3)
        a41 = 0
        a42 = 1 - (3 * b3)
        a43 = 3 * b3
        b1 = 1/6
        b2 = (2 / 3) - b3
        b4 = 1/6
    elif (case == 3):
        b3 = alpha[0]
        c2 = 1/2
        c3 = 0
        c4 = 1
        a31 = -1 / (12 * b3)
        a32 = 1 / (12 * b3)
        a41 = (-1/2) - (6 * b3)
        a42 = 3/2
        a43 = 6 * b3
        b1 = (1/6) - b3
        b2 = 2/3
        b4 = 1/6
    elif (case == 4):
        b4 = alpha[0]
        c2 = 1
        c3 = 1/2
        c4 = 1
        a31 = 3/8
        a32 = 1/8
        a41 = 1 - (1 / (4 * b4))
        a42 = -1 / (12 * b4)
        a43 = 1 / (3 * b4)
        b1 = 1/6
        b2 = 1/6 - b4
        b3 = 2/3
    elif (case == 5):
        c2 = alpha[0]
        c3 = 1/2
        c4 = 1
        a31 = ((4 * c2) - 1) / (8 * c2)
        a32 = 1 / (8 * c2)
        a41 = (1 - (2 * c2)) / (2 * c2)
        a42 = -1 / (2 * c2)
        a43 = 2
        b1 = 1/6
        b2 = 0
        b3 = 2/3
        b4 = 1/6

    log.info("Coefficients selected for E4 are:")
    log.info("c2, c3, c4, b1, b2, b3, b4, a31, a32, a41, a42, a43", c2, c3, c4, b1, b2, b3, b4, a31, a32, a41, a42, a43)
    return c2, c3, c4, b1, b2, b3, b4, a31, a32, a41, a42, a43

def E4Eq1(c, b, A):
    #For Equation 1, find b*c^4
    cquad = [c[0] ** 4, c[1] ** 4, c[2] ** 4, c[3] ** 4]
    bcquad = (b[0] * cquad[0]) + (b[1] * cquad[1]) + (b[2] * cquad[2]) + (b[3] * cquad[3])

    return ((1/24) * (bcquad - (1/5)))

def E4Eq2(c, b, A):
    #For Equation 2, find b*c^2*A*c
    csq = [c[0] ** 2, c[1] ** 2, c[2] ** 2, c[3] ** 2]
    bcsq = [b[0] * csq[0], b[1] * csq[1], b[2] * csq[2], b[3] * csq[3]]
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2]) + (A[0][3] * c[3])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2]) + (A[1][3] * c[3])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]) + (A[2][3] * c[3])),
          ((A[3][0] * c[0]) + (A[3][1] * c[1]) + (A[3][2] * c[2]) + (A[3][3] * c[3]))]

    bcsqAc = (bcsq[0] * Ac[0]) + (bcsq[1] * Ac[1]) + (bcsq[2] * Ac[2]) + (bcsq[3] * Ac[3])

    return ((1/2) * (bcsqAc - (1/10)))

def E4Eq3(c, b, A):
    #For Equation 3, find b*c*A*c^2
    csq = [c[0] ** 2, c[1] ** 2, c[2] ** 2, c[3] ** 2]
    bc = [b[0] * c[0], b[1] * c[1], b[2] * c[2], b[3] * c[3]]
    Acsq = [((A[0][0] * csq[0]) + (A[0][1] * csq[1]) + (A[0][2] * csq[2]) + (A[0][3] * csq[3])),
            ((A[1][0] * csq[0]) + (A[1][1] * csq[1]) + (A[1][2] * csq[2]) + (A[1][3] * csq[3])),
            ((A[2][0] * csq[0]) + (A[2][1] * csq[1]) + (A[2][2] * csq[2]) + (A[2][3] * csq[3])),
            ((A[3][0] * csq[0]) + (A[3][1] * csq[1]) + (A[3][2] * csq[2]) + (A[3][3] * csq[3]))]
    bcAcsq = (bc[0] * Acsq[0]) + (bc[1] * Acsq[1]) + (bc[2] * Acsq[2]) + (bc[3] * Acsq[3])

    return ((1/2) * (bcAcsq - (1/15)))

def E4Eq4(c, b, A):
    #For Equation 4, find b*c*A^2*c
    bc = [b[0] * c[0], b[1] * c[1], b[2] * c[2], b[3] * c[3]]
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2]) + (A[0][3] * c[3])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2]) + (A[1][3] * c[3])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]) + (A[2][3] * c[3])),
          ((A[3][0] * c[0]) + (A[3][1] * c[1]) + (A[3][2] * c[2]) + (A[3][3] * c[3]))]
    AAc = [((A[0][0] * Ac[0]) + (A[0][1] * Ac[1]) + (A[0][2] * Ac[2]) + (A[0][3] * Ac[3])),
           ((A[1][0] * Ac[0]) + (A[1][1] * Ac[1]) + (A[1][2] * Ac[2]) + (A[1][3] * Ac[3])),
           ((A[2][0] * Ac[0]) + (A[2][1] * Ac[1]) + (A[2][2] * Ac[2]) + (A[2][3] * Ac[3])),
           ((A[3][0] * Ac[0]) + (A[3][1] * Ac[1]) + (A[3][2] * Ac[2]) + (A[3][3] * Ac[3]))]
    bcAAc = (bc[0] * AAc[0]) + (bc[1] * AAc[1]) + (bc[2] * AAc[2]) + (bc[3] * AAc[3])

    return (bcAAc - (1/30))

def E4Eq5(c, b, A):
    #For Equation 5, find b*(A*c)^2
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2]) + (A[0][3] * c[3])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2]) + (A[1][3] * c[3])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]) + (A[2][3] * c[3])),
          ((A[3][0] * c[0]) + (A[3][1] * c[1]) + (A[3][2] * c[2]) + (A[3][3] * c[3]))]

    AcAc = [Ac[0] ** 2, Ac[1] ** 2, Ac[2] ** 2, Ac[3] ** 2]
    bAcAc = (b[0] * AcAc[0] + b[1] * AcAc[1] + b[2] * AcAc[2] + b[3] * AcAc[3])

    return ((1/2) * (bAcAc - (1/20)))

def E4Eq6(c, b, A):
    #For Equation 6, find b*A*c^3
    ccube = [c[0] ** 3, c[1] ** 3, c[2] ** 3, c[3] ** 3]
    Accube = [((A[0][0] * ccube[0]) + (A[0][1] * ccube[1]) + (A[0][2] * ccube[2]) + (A[0][3] * ccube[3])),
              ((A[1][0] * ccube[0]) + (A[1][1] * ccube[1]) + (A[1][2] * ccube[2]) + (A[1][3] * ccube[3])),
              ((A[2][0] * ccube[0]) + (A[2][1] * ccube[1]) + (A[2][2] * ccube[2]) + (A[2][3] * ccube[3])),
              ((A[3][0] * ccube[0]) + (A[3][1] * ccube[1]) + (A[3][2] * ccube[2]) + (A[3][3] * ccube[3]))]
    bAccube = (b[0] * Accube[0] + b[1] * Accube[1] + b[2] * Accube[2] + b[3] * Accube[3])

    return ((1/6) * (bAccube - (1/20)))

def E4Eq7(c, b, A):
    #For Equation 7, find b*A*c*(A*c)
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2]) + (A[0][3] * c[3])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2]) + (A[1][3] * c[3])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]) + (A[2][3] * c[3])),
          ((A[3][0] * c[0]) + (A[3][1] * c[1]) + (A[3][2] * c[2]) + (A[3][3] * c[3]))]
    cAc = [c[0] * Ac[0], c[1] * Ac[1], c[2] * Ac[2], c[3] * Ac[3]]
    AcAc = [((A[0][0] * cAc[0]) + (A[0][1] * cAc[1]) + (A[0][2] * cAc[2]) + (A[0][3] * cAc[3])),
            ((A[1][0] * cAc[0]) + (A[1][1] * cAc[1]) + (A[1][2] * cAc[2]) + (A[1][3] * cAc[3])),
            ((A[2][0] * cAc[0]) + (A[2][1] * cAc[1]) + (A[2][2] * cAc[2]) + (A[2][3] * cAc[3])),
            ((A[3][0] * cAc[0]) + (A[3][1] * cAc[1]) + (A[3][2] * cAc[2]) + (A[3][3] * cAc[3]))]
    bAcAc = (b[0] * AcAc[0]) + (b[1] * AcAc[1]) + (b[2] * AcAc[2]) + (b[3] * AcAc[3])

    return (bAcAc - (1/40))

def E4Eq8(c, b, A):
    #For Equation 8, find b*A^2*c^2
    csq = [c[0] ** 2, c[1] ** 2, c[2] ** 2, c[3] ** 2]
    Acsq = [((A[0][0] * csq[0]) + (A[0][1] * csq[1]) + (A[0][2] * csq[2]) + (A[0][3] * csq[3])),
            ((A[1][0] * csq[0]) + (A[1][1] * csq[1]) + (A[1][2] * csq[2]) + (A[1][3] * csq[3])),
            ((A[2][0] * csq[0]) + (A[2][1] * csq[1]) + (A[2][2] * csq[2]) + (A[2][3] * csq[3])),
            ((A[3][0] * csq[0]) + (A[3][1] * csq[1]) + (A[3][2] * csq[2]) + (A[3][3] * csq[3]))]
    AAcsq = [((A[0][0] * Acsq[0]) + (A[0][1] * Acsq[1]) + (A[0][2] * Acsq[2]) + (A[0][3] * Acsq[3])),
             ((A[1][0] * Acsq[0]) + (A[1][1] * Acsq[1]) + (A[1][2] * Acsq[2]) + (A[1][3] * Acsq[3])),
             ((A[2][0] * Acsq[0]) + (A[2][1] * Acsq[1]) + (A[2][2] * Acsq[2]) + (A[2][3] * Acsq[3])),
             ((A[3][0] * Acsq[0]) + (A[3][1] * Acsq[1]) + (A[3][2] * Acsq[2]) + (A[3][3] * Acsq[3]))]
    bAAcsq = (b[0] * AAcsq[0]) + (b[1] * AAcsq[1]) + (b[2] * AAcsq[2]) + (b[3] * AAcsq[3])

    return ((1/2) * (bAAcsq - (1/60)))

def E4Eq9(c, b, A):
    #For Equation 9, find b*A^3*c
    Ac = [((A[0][0] * c[0]) + (A[0][1] * c[1]) + (A[0][2] * c[2]) + (A[0][3] * c[3])),
          ((A[1][0] * c[0]) + (A[1][1] * c[1]) + (A[1][2] * c[2]) + (A[1][3] * c[3])),
          ((A[2][0] * c[0]) + (A[2][1] * c[1]) + (A[2][2] * c[2]) + (A[2][3] * c[3])),
          ((A[3][0] * c[0]) + (A[3][1] * c[1]) + (A[3][2] * c[2]) + (A[3][3] * c[3]))]
    AAc = [((A[0][0] * Ac[0]) + (A[0][1] * Ac[1]) + (A[0][2] * Ac[2]) + (A[0][3] * Ac[3])),
           ((A[1][0] * Ac[0]) + (A[1][1] * Ac[1]) + (A[1][2] * Ac[2]) + (A[1][3] * Ac[3])),
           ((A[2][0] * Ac[0]) + (A[2][1] * Ac[1]) + (A[2][2] * Ac[2]) + (A[2][3] * Ac[3])),
           ((A[3][0] * Ac[0]) + (A[3][1] * Ac[1]) + (A[3][2] * Ac[2]) + (A[3][3] * Ac[3]))]
    AAAc = [((A[0][0] * AAc[0]) + (A[0][1] * AAc[1]) + (A[0][2] * AAc[2]) + (A[0][3] * Ac[3])),
            ((A[1][0] * AAc[0]) + (A[1][1] * AAc[1]) + (A[1][2] * AAc[2]) + (A[1][3] * Ac[3])),
            ((A[2][0] * AAc[0]) + (A[2][1] * AAc[1]) + (A[2][2] * AAc[2]) + (A[2][3] * Ac[3])),
            ((A[3][0] * AAc[0]) + (A[3][1] * AAc[1]) + (A[3][2] * AAc[2]) + (A[3][3] * Ac[3]))]

    bAAAc = (b[0] * AAAc[0]) + (b[1] * AAAc[1]) + (b[2] * AAAc[2]) + (b[3] * AAAc[3])

    return (bAAAc - (1/120))

def E4(alpha):
    if (case == 1):
        if ((alpha[0] <= 0) or (alpha[1] <= 0) or (alpha[0] == 1) or (alpha[1] == 1)
            or (alpha[0] == alpha[1]) or (alpha[0] == 1/2) or ((3 - (4 * (alpha[0] + alpha[1])) + (6 * alpha[0] * alpha[1])) == 0)):
            return 1
    elif ((case == 2) or (case == 3) or (case == 4) or (case == 5)):
        if (alpha[0] == 0):
            return 1

    c2, c3, c4, b1, b2, b3, b4, a31, a32, a41, a42, a43 = setValuesForFourthOrder(alpha)
    
    c = [0, c2, c3, c4]
    b = [b1, b2, b3, b4]
    A = [[0, 0, 0, 0],[c2, 0, 0, 0],[a31, a32, 0, 0], [a41, a42, a43, 0]]

    #For Equation 1
    eq1 = E4Eq1(c, b, A)

    #For Equation 2
    eq2 = E4Eq2(c, b, A)

    #For Equation 3
    eq3 = E4Eq3(c, b, A)

    #For Equation 4
    eq4 = E4Eq4(c, b, A)

    #For Equation 5
    eq5 = E4Eq5(c, b, A)

    #For Equation 6
    eq6 = E4Eq6(c, b, A)

    #For Equation 7
    eq7 = E4Eq7(c, b, A)

    #For Equation 8
    eq8 = E4Eq8(c, b, A)

    #For Equation 9
    eq9 = E4Eq9(c, b, A)
    
    result = (eq1 ** 2) + (eq2 ** 2) + (eq3 ** 2) + (eq4 ** 2) + (eq5 ** 2) + (eq6 ** 2) + (eq7 ** 2) + (eq8 ** 2) + (eq9 ** 2)
    
    return result

def displayMenu():
    print ("1. Optimize E2")
    print ("2. Optimize E3")
    print ("3. Optimize E4")
    choice = input("Enter your choice: ")
    
    return int(choice);

def chooseE4Case():
    print ("1. Case 1: 0, c2, c3, 1 all distinct,",
           "\nc2≠1/2 and 3 - 4(c2 + c3) + 6*c2*c3 ≠ 0")
    print ("2. Case 2: c2 = c3 = 1/2, b3≠0")
    print ("3. Case 3: c2 = 1/2, c3 = 0, b3≠0")
    print ("4. Case 4: c2 = 1, c3 = 1/2, b4≠0")
    print ("5. Case 5: c2≠0, c3 = 1/2, b2 = 0")
    choice = input("\nEnter your case choice: ")
    
    return int(choice)

def initializeOptimizer(choice):
    global case
    if (choice == 1):
        log.info("Optimizing E2")
        optimize(E2)
    elif (choice == 2):
        log.info("Optimizing E3")
        optimize(E3)
    elif (choice == 3):
        case = chooseE4Case()
        log.info("Optimizing E4 with case: ", case)
        optimize(E4)

log = logger.Logger("Optimization Log")
initializeOptimizer(displayMenu())

del log
