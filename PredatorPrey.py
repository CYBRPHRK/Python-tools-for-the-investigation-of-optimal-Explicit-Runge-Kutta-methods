x = y = alpha = beta = gamma = delta = 0

def setConstants(x0, y0, a, b, g, d):
    global x, y, alpha, beta, gamma, delta
    x, y, alpha, beta, gamma, delta = x0, y0, a, b, g, d

def predatorPreyForX(t, x):
    global y, alpha, beta, gamma, delta
    return ((alpha * x) - (beta * x * y))

def predatorPreyForY(t, y):
    global x, alpha, beta, gamma, delta
    return ((delta * x * y) - (gamma * y))
