import bokeh.plotting as bp
import Function as f
import config

'''
Names: h00(t), h10(t), h01(t) and h11(t)
Description: The functions given below work as Hermite Basis Polynomials,
                h00(t), h10(t), h01(t) and h11(t).
Parameters:
        t    : The quantity t measures the relative distance across the subinterval
Returns:
        result for the Hermite Basis Polynomial at t.
'''
def h00(t):
    return ((1 + (2 * t)) * (1 - t)**2)

def h10(t):
    return (t * (1 - t)**2)

def h01(t):
    return ((t**2) * (3 - (2 * t)))

def h11(t):
    return ((t**2) * (t - 1))

'''
Names: h00_d(t), h10_d(t), h01_d(t) and h11_d(t)
Description: The functions given below work as derivatives of Hermite Basis Polynomials,
                h00(t), h10(t), h01(t) and h11(t).
Parameters:
        t    : The quantity t measures the relative distance across the subinterval
Returns:
        result for the derivative of Hermite Basis Polynomial at t.
'''
def h00_d(t):
    return (6 * t * (t - 1))

def h10_d(t):
    return (1 + (3 * (t**2)) - (4 * t))

def h01_d(t):
    return (6 * t * (1 - t))

def h11_d(t):
    return ((3 * (t**2)) - (2 * t))

'''
Names: hermite
Description: This function evaluates Hermite form for u_i(t_i + (theta * h_i))
Parameters:
        tt  : tt is the list of times after each step.
        yy  : yy is the list of lists of y values at the given times at each step.
        ffy : ffy is the function value for f(t, y) using the above values.
Returns:
        uu  : uu is the list of lists of lists of Hermite forms at uniform points
                for system of equations in each interval
'''
def hermite(tt, yy, ffy):
    h = tt[1] - tt[0]
    uu = []
    ffu = [] #Extra
    for i in range (0, len(tt) - 1):
        u_i = []
        fu_i = [] #Extra
        for j in range (1, 11):
            theta = j/10
            u = []
            # u_i(t_i + (theta * h_i))
            for k in range (0, len(yy[i])):
                u.append((yy[i][k] * h00(theta)) + (h * ffy[i][k] * h10(theta)) + (yy[i + 1][k] * h01(theta)) + (h * ffy[i + 1][k] * h11(theta)))
            fu = f.formulaExact((tt[i] + (theta * h)), u[:]) #Extra
            #fu = f.error((tt[i] + (theta * h)), u[:]) #Extra
            u_i.append(u)
            fu_i.append(fu) #Extra
        ffu.append(fu_i)  #Extra
        uu.append(u_i)
    return uu, ffu  #Extra

def defect(tt, yy, ffy):
    h = tt[1] - tt[0]
    delta = []

    for i in range (0, len(tt) - 1):
        d_i = []
        for j in range (1, 11):
            theta = j/10
            u = []
            u_d = []
            d = []
            for k in range (0, len(yy[i])):
                # u_i(t_i + (theta * h_i))
                u.append((yy[i][k] * h00(theta)) + (h * ffy[i][k] * h10(theta)) + (yy[i + 1][k] * h01(theta)) + (h * ffy[i + 1][k] * h11(theta)))

                # u_i'(t_i + (theta * h_i))
                # Here u_d denotes the derivative of u
                u_d.append(((yy[i][k] / h) * h00_d(theta)) + (ffy[i][k] * h10_d(theta)) + ((yy[i + 1][k] / h) * h01_d(theta)) + (ffy[i + 1][k] * h11_d(theta)))

            # Here fu = f(t_i + (theta * h_i), u_i(t_i + (theta * h_i)))
            fu = f.formula((tt[i] + (theta * h)), u[:])
            # d_i(t_i + (theta * h_i)) = u_i'(t_i + (theta * h_i)) - f(t_i + (theta * h_i), u_i(t_i + (theta * h_i)))
            for k in range (0, len(u)):
                d.append(u_d[k] - fu[k])
            d_i.append(d)
        delta.append(d_i)
    return delta

def displayResults():
    # For Full test
    for i in range (0, len(config.t)):
        u, f = hermite(config.t[i], config.y[i], config.f[i])
        d = defect(config.t[i], config.y[i], config.f[i])
        print ("\tu\t\t\tf\t\t\td")
        for j in range (0, len(u)):
            print ("Step:", j+1)
            print ("t =", config.t[i][j])
            for k in range (0, len(u[i])):
                print (u[j][k], "\t", f[j][k], "\t", d[j][k])
    config.t = []
    config.y = []
    config.f = []

def test():
    print ("h00(0) = " + str(h00(0)) + ", h00(1) = " + str(h00(1)) + ", h00'(0) = " + str(h00_d(0)) + ", h00'(1) = " + str(h00_d(1)))
    print ("h10(0) = " + str(h10(0)) + ", h10(1) = " + str(h10(1)) + ", h10'(0) = " + str(h10_d(0)) + ", h10'(1) = " + str(h10_d(1)))
    print ("h01(0) = " + str(h01(0)) + ", h01(1) = " + str(h01(1)) + ", h01'(0) = " + str(h01_d(0)) + ", h01'(1) = " + str(h01_d(1)))
    print ("h11(0) = " + str(h11(0)) + ", h11(1) = " + str(h11(1)) + ", h11'(0) = " + str(h11_d(0)) + ", h11'(1) = " + str(h11_d(1)))
