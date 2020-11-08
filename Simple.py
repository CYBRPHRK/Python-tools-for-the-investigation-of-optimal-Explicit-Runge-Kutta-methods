def simple(t, y):
    y[0] = (y[0] * (-1))
    return y

def simple_sys(t, y):
    return [y[1], (y[0] * (-1))]

