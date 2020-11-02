alpha = beta = gamma = delta = 0

def setConstants(a, b, g, d):
    global alpha, beta, gamma, delta
    alpha, beta, gamma, delta = a, b, g, d

def predatorPrey(t, y):
    global alpha, beta, gamma, delta
    x = [((alpha * y[0]) - (beta * y[0] * y[1])), ((delta * y[0] * y[1]) - (gamma * y[1]))]
    return x
