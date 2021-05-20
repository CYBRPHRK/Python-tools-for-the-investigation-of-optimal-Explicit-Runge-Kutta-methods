import Function as f
import config

methodNumber = alpha = beta = case = 0

def displayMethods():
    print ("1. Forward Eulers Method")
    print ("2. Explicit Midpoint Method")
    print ("3. Heuns Second Order Method")
    print ("4. Second Order RK Method")
    print ("5. Heuns Third Order Method")
    print ("6. Ralston's Third Order Method")
    print ("7. Third Order RK Method")
    print ("8. RK4 Method")
    print ("9. FourthOrderRKMethod")
    mname = input("\nEnter the method with values respectively (Use spaces between the values like shown above):\n")
    config.log.info("mname =", mname)
    setMethodValues(mname, False)

def setMethodValues(mname, auto, caseNumber=None):
    config.log.info("setMethodValues() started")
    global methodNumber, case
    
    methodNumber = int(mname)
    if ((methodNumber < 1) or (methodNumber > 9)):
        print ("No Method with that number.\n")
        displayMethods()
    else:
        if (auto):
            case = caseNumber
            autoChooseCase()
        else:
            userChooseCase()

def autoChooseCase():
    config.log.info("autoChooseCase() started")
    global alpha, beta
    caseInfo = ""
    if (methodNumber == 4):
        alpha = 2/3
        caseInfo = " alpha=" + str(alpha)
    elif (methodNumber == 7):
        if (case == 1):
            alpha = 0.49650476
            beta = 0.75174749
            caseInfo = " c2=" + str(alpha) + " c3=" + str(beta)
        elif (case == 2):
            alpha = 1/8
            caseInfo = " b3=" + str(alpha)
        else:
            alpha = 3/8
            caseInfo = " b3=" + str(alpha)
    elif (methodNumber == 9):
        if (case == 1):
            alpha = 0.35774159
            beta = 0.59148821
            caseInfo = " c2=" + str(alpha) + " c3=" + str(beta)
        elif (case == 2):
            alpha = 0.83316441
            caseInfo = " b3=" + str(alpha)
        elif ((case == 3) or (case == 4)):
            alpha = 1/6
            caseInfo = " b" + str(case) + "="+ str(alpha)
        else:
            alpha = 1
            caseInfo = " c2=" + str(alpha)
    config.file.write(caseInfo)

def userChooseCase():
    config.log.info("userChooseCase() started")
    global alpha, beta, case
    if (methodNumber == 4):
        alpha = input("Enter the alpha: ")
        if ("/" in str(alpha)):
            res = alpha.split('/')
            alpha = int(res[0]) / int(res[1])
        else:
            alpha = float(alpha)
    elif (methodNumber == 7):
        print ("Case 1: if c2≠0, 2/3, c3; c3≠0, c2, then enter: 1 c2 c3")
        print ("Case 2: if b3≠0, where c3=0, then enter: 2 b3")
        print ("Case 3: if b3≠0, where c3≠0, then enter: 3 b3")
        choice = input("\nEnter your case choice: ")
        data = choice.split()
        for i in range(1, len(data)):
            if ("/" in str(data[i])):
                res = data[i].split('/')
                data[i] = int(res[0]) / int(res[1])
            else:
                data[i] = float(data[i])
        
        case = int(data[0]) 
        if (case == 1):
            alpha, beta = data[1], data[2]
        elif ((case == 2) or (case == 3)):
            alpha = data[1]
        else:
            print ("No case of that choice.")
            exit(0)
    elif (methodNumber == 9):
        print ("Case 1: 0, c2, c3, 1 all distinct,",
               "\nc2≠1/2 and 3 - 4(c2 + c3) + 6*c2*c3 ≠ 0, then enter: 1 c2 c3")
        print ("Case 2: c2 = c3 = 1/2, b3≠0, then enter: 2 b3")
        print ("Case 3: c2 = 1/2, c3 = 0, b3≠0, then enter: 3 b3")
        print ("Case 4: c2 = 1, c3 = 1/2, b4≠0, then enter: 4 b4")
        print ("Case 5: c2≠0, c3 = 1/2, b2 = 0, then enter: 5 c2")
        choice = input("\nEnter your case choice: ")
        data = choice.split()
        for i in range(1, len(data)):
            if ("/" in str(data[i])):
                res = data[i].split('/')
                data[i] = int(res[0]) / int(res[1])
            else:
                data[i] = float(data[i])
        
        case = int(data[0]) 
        if (case == 1):
            alpha, beta = data[1], data[2]
        elif ((case == 2) or (case == 3) or (case == 4) or (case == 5)):
            alpha = data[1]
        else:
            print ("No case of that choice.")
            exit(0)

def method(t, y, h):
    if (methodNumber == 1):
        return forwardEulersMethod(t, y)
    elif (methodNumber == 2):
        return explicitMidpointMethod(t, y, h)
    elif (methodNumber == 3):
        return HeunsSecondOrderMethod(t, y, h)
    elif (methodNumber == 4):
        return secondOrderRKMethod(t, y, h)
    elif (methodNumber == 5):
        return HeunsThirdOrderMethod(t, y, h)
    elif (methodNumber == 6):
        return RalstonsThirdOrderMethod(t, y, h)
    elif (methodNumber == 7):
        return thirdOrderRKMethod(t, y, h)
    elif (methodNumber == 8):
        return RK4Method(t, y, h)
    elif (methodNumber == 9):
        return FourthOrderRKMethod(t, y, h)

def forwardEulersMethod(t, y):
    fy = f.formula(t, y[:])
    config.ffy.append(fy)
    return fy

def explicitMidpointMethod(t, y, h):
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + ((h/2) * k1[i]))
    fy = f.formula((t + (h/2)), yn[:])

    return fy

def HeunsSecondOrderMethod(t, y, h):
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * k1[i]))
    k2 = f.formula((t + h), yn[:])
    fy = []
    for i in range (0, len(k2)):
        fy.append((1/2) * (k1[i] + k2[i]))
        
    return fy

def secondOrderRKMethod(t, y, h):
    global alpha
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (alpha * k1[i])))
    k2 = f.formula((t + (alpha * h)), yn[:])
    fy = []
    for i in range (0, len(k1)):
        fy.append(((1 - (1/(2 * alpha))) * k1[i]) + ((1/(2 * alpha)) * k2[i]))

    return fy

def HeunsThirdOrderMethod(t, y, h):
    c2 = 1/3
    c3 = 2/3
    b1 = 1/4
    b2 = 0
    b3 = 3/4
    a31 = 0
    a32 = 2/3
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)

    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (c2 * k1[i])))
    k2 = f.formula((t + (c2 * h)), yn[:])

    yn.clear()
    for i in range (0, len(k2)):
        yn.append(y[i] + (h * ((a31 * k1[i]) + (a32 * k2[i]))))
    k3 = f.formula((t + (c3 * h)), yn[:])

    fy = []
    for i in range (0, len(y)):
        fy.append((b1 * k1[i]) + (b2 * k2[i]) + (b3 * k3[i]))

    return fy

def RalstonsThirdOrderMethod(t, y, h):
    c2 = 1/2
    c3 = 3/4
    b1 = 2/9
    b2 = 1/3
    b3 = 4/9
    a31 = 0
    a32 = 3/4
    
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)

    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (c2 * k1[i])))
    k2 = f.formula((t + (c2 * h)), yn[:])

    yn.clear()
    for i in range (0, len(k2)):
        yn.append(y[i] + (h * ((a31 * k1[i]) + (a32 * k2[i]))))
    k3 = f.formula((t + (c3 * h)), yn[:])

    fy = []
    for i in range (0, len(y)):
        fy.append((b1 * k1[i]) + (b2 * k2[i]) + (b3 * k3[i]))

    return fy

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

def thirdOrderRKMethod(t, y, h):
    #Here, alpha is used for c2 or b3 and beta for c3
    global alpha, beta

    c2, c3, b1, b2, b3, a31, a32 = setValuesForThirdOrder([alpha, beta])

    '''print ("\nc2 =", c2)
    print ("c3 =", c3)
    print ("b1 =", b1)
    print ("b2 =", b2)
    print ("b3 =", b3)
    print ("a31 =", a31)
    print ("a32 =", a32)'''

    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (c2 * k1[i])))
    k2 = f.formula((t + (c2 * h)), yn[:])

    yn.clear()
    for i in range (0, len(k2)):
        yn.append(y[i] + (h * ((a31 * k1[i]) + (a32 * k2[i]))))
    k3 = f.formula((t + (c3 * h)), yn[:])

    fy = []
    for i in range (0, len(y)):
        fy.append((b1 * k1[i]) + (b2 * k2[i]) + (b3 * k3[i]))

    return fy

def RK4Method(t, y, h):
    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + ((h / 2) * k1[i]))
    k2 = f.formula((t + (h / 2)), yn[:])
    yn.clear()
    for i in range (0, len(k2)):
        yn.append(y[i] + ((h / 2) * k2[i]))
    k3 = f.formula((t + (h / 2)), yn[:])
    yn.clear()
    for i in range (0, len(k3)):
        yn.append(y[i] + (h * k3[i]))
    k4 = f.formula((t + h), yn[:])
    fy = []
    for i in range (0, len(y)):
        fy.append((1/6) * (k1[i] + (2 * k2[i]) + (2 * k3[i]) + k4[i]))

    return fy

def FourthOrderRKMethod(t, y, h):
    #Here, alpha is used for c2, b3 or b4 and beta for c3
    global alpha, beta

    if (case == 1):
        c2 = alpha
        c3 = beta
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
        b3 = alpha
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
        b3 = alpha
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
        b4 = alpha
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
        c2 = alpha
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

    k1 = f.formula(t, y[:])
    config.ffy.append(k1)
    
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (c2 * k1[i])))
    k2 = f.formula((t + (c2 * h)), yn[:])

    yn.clear()
    for i in range (0, len(k2)):
        yn.append(y[i] + (h * ((a31 * k1[i]) + (a32 * k2[i]))))
    k3 = f.formula((t + (c3 * h)), yn[:])

    yn.clear()
    for i in range (0, len(k3)):
        yn.append(y[i] + (h * ((a41 * k1[i]) + (a42 * k2[i]) + (a43 * k3[i]))))
    k4 = f.formula((t + (c4 * h)), yn[:])

    fy = []
    for i in range (0, len(y)):
        fy.append((b1 * k1[i]) + (b2 * k2[i]) + (b3 * k3[i]) + (b4 * k4[i]))

    return fy
