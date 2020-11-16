import Function as f

methodNumber = alpha = beta = case = 0

def displayMethods():
    print ("Forward Eulers Method: m1")
    print ("Explicit Midpoint Method: m2")
    print ("Heuns Method: m3")
    print ("Second Order RK Method: m4 alpha")
    print ("Third Order RK Method: m5")
    print ("RK4 Method: m6")

def setMethodValues(mname):
    global methodNumber, alpha

    data = mname.split()
    for i in range(1, len(data)):
        data[i] = float(data[i])

    if (data[0] == "m1"):
        methodNumber = 1
    elif (data[0] == "m2"):
        methodNumber = 2
    elif (data[0] == "m3"):
        methodNumber = 3
    elif (data[0] == "m4"):
        methodNumber = 4
        alpha = data[1]
    elif (data[0] == "m5"):
        methodNumber = 5
    elif (data[0] == "m6"):
        methodNumber = 6
    else:
        print ("No Method with that name.")
        exit(0)
    chooseCase()

def chooseCase():
    global alpha, beta, case
    if (methodNumber == 5):
        print ("Case 1: if c2≠0, 2/3, c3; c3≠0, c2, then enter: 1 c2 c3")
        print ("Case 2: if b3≠0, then enter: 2 b3")
        print ("Case 3: if b3≠0, then enter: 3 b3")
        choice = input("\nEnter your case choice: ")
        data = choice.split()
        for i in range(1, len(data)):
            data[i] = float(data[i])
        
        case = int(data[0]) 
        if (case == 1):
            alpha, beta = data[1], data[2]
        elif ((case == 2) or (case == 3)):
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
        return HeunsMethod(t, y, h)
    elif (methodNumber == 4):
        return secondOrderRKMethod(t, y, h)
    elif (methodNumber == 5):
        return thirdOrderRKMethod(t, y, h)
    elif (methodNumber == 6):
        return RK4Method(t, y, h)

def forwardEulersMethod(t, y):
    fy = f.formula(t, y[:])
    return fy

def explicitMidpointMethod(t, y, h):
    k1 = f.formula(t, y[:])
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + ((h/2) * k1[i]))
    fy = f.formula((t + (h/2)), yn[:])

    return fy

def HeunsMethod(t, y, h):
    k1 = f.formula(t, y[:])
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
    yn = []
    for i in range (0, len(k1)):
        yn.append(y[i] + (h * (alpha * k1[i])))
    k2 = f.formula((t + (alpha * h)), yn[:])
    fy = []
    for i in range (0, len(k1)):
        fy.append(((1 - (1/(2 * alpha))) * k1[i]) + ((1/(2 * alpha)) * k2[i]))

    return fy

def thirdOrderRKMethod(t, y, h):
    #Here, alpha is used for c2 or b3 and beta for c3
    global alpha, beta

    if (case == 1):
        c2 = alpha
        c3 = beta
        b1 = (2 - (3 * (c2 + c3)) + (6 * c2 * c3)) / (6 * c2 * c3)
        b2 = (c3 - (2/3)) / (2 * c2 * (c3 - c2))
        b3 = ((2/3) - c2) / (2 * c3 * (c3 - c2))
        a31 = (c3 * ((c3 * 3 * c2) + (3 * c2 * c2))) / (c2 * ((3 * c2) - 2))
        a32 = (c3 * (c2 - c3)) / (c2 * ((3 * c2) - 2))
    elif (case == 2):
        c2 = 2/3
        c3 = 0
        b3 = alpha
        b1 = (1/4) - b3
        b2 = 3/4
        a31 = -1 / (4 * b3)
        a32 = 1 / (4 * b3)
    else:
        c2 = c3 = 2/3
        b3 = alpha
        b1 = 1/4
        b2 = (3/4) - b3
        a31 = ((8 * b3) - 3) / (12 * b3)
        a32 = 1 / (4 * b3)

    k1 = f.formula(t, y[:])
    
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
