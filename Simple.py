import math

alpha = beta = gamma = delta = theta = 0
exactExists = True

def setConstants(a, b=None, c=None, d=None, e=None):
    global alpha, beta, gamma, delta, theta
    alpha, beta, gamma, delta, theta = a, b, c, d, e

def simple(i, t, y):
    # IVODE
    if (i == 0):
        return [y[0] * (-1)]
    # Exact value for the IVODE
    elif (i == 1):
        return [math.exp((-1) * t)]
    # Error associated with the IVODE
    else:
        return [y[0] - math.exp((-1) * t)]

'''
    alpha = 2.0/3.0
    beta = 4.0/3.0
    gamma = 1
    delta = 1
'''
def predatorPrey(i, t, y):
    global exactExists
    exactExists = False
    # IVODE
    if (i == 0):
        return [((alpha * y[0]) - (beta * y[0] * y[1])), ((delta * y[0] * y[1]) - (gamma * y[1]))]

def simple_sys(i, t, y):
    # IVODE
    if (i == 0):
        return [y[1], (y[0] * (-1))]
    # Exact value for the IVODE
    elif (i == 1):
        return [math.sin(t), math.cos(t)]
    # Error associated with the IVODE
    else:
        return [y[0] - math.sin(t), y[1] - math.cos(t)]

def TestF4(i, t, y):
    # IVODE
    if (i == 0):
        return [(-1/2) * (y[0] ** 3)]
    # Exact value for the IVODE
    elif (i == 1):
        return [(1 / math.sqrt(1 + t))]
    # Error associated with the IVODE
    else:
        return [y[0] - (1 / math.sqrt(1 + t))]

def TestF5(i, t, y):
    # IVODE
    if (i == 0):
        return [-2 * t * (y[0] ** 2)]
    # Exact value for the IVODE
    elif (i == 1):
        return [(1 / (1 + (t ** 2)))]
    # Error associated with the IVODE
    else:
        return [y[0] - (1 / (1 + (t ** 2)))]

def TestF6(i, t, y):
    # IVODE
    if (i == 0):
        return [(1/4) * y[0] * (1 - (y[0] / 20))]
    # Exact value for the IVODE
    elif (i == 1):
        return [(20 / (1 + (19 * math.exp(((-1) * t) / 4))))]
    # Error associated with the IVODE
    else:
        return [y[0] - (20 / (1 + (19 * math.exp(((-1) * t) / 4))))]

def TestF7(i, t, y):
    # IVODE
    if (i == 0):
        return [100 * (math.sin(t) - y[0])]
    # Exact value for the IVODE
    elif (i == 1):
        return [((100 * (math.exp(-100 * t) - math.cos(t)) + (10000 * math.sin(t))) / (10001))]
    # Error associated with the IVODE
    else:
        return [y[0] - ((100 * (math.exp(-100 * t) - math.cos(t)) + (10000 * math.sin(t))) / (10001))]

def TestF8(i, t, y):
    # IVODE
    if (i == 0):
        return [(15 * math.cos(10 * t)) / y[0]]
    # Exact value for the IVODE
    elif (i == 1):
        return [math.sqrt((3 * math.sin(10 * t)) + 4)]
    # Error associated with the IVODE
    else:
        return [y[0] - math.sqrt((3 * math.sin(10 * t)) + 4)]

def TestF9(i, t, y):
    # IVODE
    if (i == 0):
        return [(-1 * alpha * y[0]) - (math.exp(-1 * alpha * t) * math.sin(t))]
    # Exact value for the IVODE
    elif (i == 1):
        return [(math.exp(-1 * alpha * t) * math.cos(t))]
    # Error associated with the IVODE
    else:
        return [y[0] - (math.exp(-1 * alpha * t) * math.cos(t))]

def sampleCOVID19ModelInitializer():
    setConstants(0.125, 0.9, 0.06, (0.01/365), 37.741e06)
    
    y03 = 1
    y02 = 103
    return [theta-y03-y02, y02, y03, 0]

def sampleCOVID19Model(i, t, y):
    global exactExists
    exactExists = False
    # IVODE
    if (i == 0):
        y1 = ((-beta * y[0] * y[2]) / theta) + (delta * theta) - (delta * y[0])
        y2 = ((beta * y[0] * y[2]) / theta) - ((alpha + delta) * y[1])
        y3 = (alpha * y[1]) - ((gamma + delta) * y[2])
        y4 = (gamma * y[2]) - (delta * y[3])
        return [y1, y2, y3, y4]
