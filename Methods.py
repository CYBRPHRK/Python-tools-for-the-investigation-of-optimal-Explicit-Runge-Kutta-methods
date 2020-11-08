import Function as f

methodNumber = alpha = 0

def displayMethods():
    print ("Forward Eulers Method: m1")
    print ("Explicit Midpoint Method: m2")
    print ("Heuns Method: m3")
    print ("Second Order RK Method: m4 alpha")
    print ("RK4 Method: m5")

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
    else:
        print ("No Method with that name.")
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
        yn.append(y[i] + ((alpha * h) * k1[i]))
    k2 = f.formula((t + (alpha * h)), yn[:])
    fy = []
    for i in range (0, len(k1)):
        fy.append(((1 - (1/(2 * alpha))) * k1[i]) + ((1/(2 * alpha)) * k2[i]))

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
