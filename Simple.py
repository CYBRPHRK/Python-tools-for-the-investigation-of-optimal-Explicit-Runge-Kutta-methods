import math

alpha = 0

def setAlpha(a):
    global alpha
    alpha = a

def simple(i, t, y):
    if (i == 0):
        return [y[0] * (-1)]
    else:
        return [y[0] - math.exp((-1) * t)]

def simple_sys(i, t, y):
    if (i == 0):
        return [y[1], (y[0] * (-1))]
    else:
        return [y[0] - math.sin(t), y[1] - math.cos(t)]

def TestF4(i, t, y):
    if (i == 0):
        return [(-1/2) * (y[0] ** 3)]
    else:
        return [y[0] - (1 / math.sqrt(1 + t))]

def TestF5(i, t, y):
    if (i == 0):
        return [-2 * t * (y[0] ** 2)]
    else:
        return [y[0] - (1 / (1 + (t ** 2)))]

def TestF6(i, t, y):
    if (i == 0):
        return [(1/4) * y[0] * (1 - (y[0] / 20))]
    else:
        return [y[0] - (20 / (1 + (19 * math.exp(((-1) * t) / 4))))]

def TestF7(i, t, y):
    if (i == 0):
        return [100 * (math.sin(t) - y[0])]
    else:
        return [y[0] - ((100 * (math.exp(-100 * t) - math.cos(t)) + (10000 * math.sin(t))) / (10001))]

def TestF8(i, t, y):
    if (i == 0):
        return [(15 * math.cos(10 * t)) / y[0]]
    else:
        return [y[0] - math.sqrt((3 * math.sin(10 * t)) + 4)]

def TestF9(i, t, y):
    if (i == 0):
        return [(-1 * alpha * y[0]) - (math.exp(-1 * alpha * t) * math.sin(t))]
    else:
        return [y[0] - (math.exp(-1 * alpha * t) * math.cos(t))]
