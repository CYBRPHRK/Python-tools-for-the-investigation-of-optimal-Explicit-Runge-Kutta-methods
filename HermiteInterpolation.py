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
Name: hermite
Description: This function evaluates Hermite form for u_i(t_i + (theta * h_i))
                and the associated defect.
Parameters:
        tt    : tt is the list of times after each step.
        yy    : yy is the list of lists of y values at the given times at each step.
        ffy   : ffy is the function value for f(t, y) using the above values.
Returns:
        t     : t is the list of points on the whole domain.
        uu    : uu is the list of lists of lists of Hermite forms at uniform points
                 for system of equations in each interval. These are known as
                 the continuous approximate numerical solutions.
        ffe   : ffe is the list of exact solutions at all the t values.
        delta : delta is the defect associated with the continuous approximate
                 numerical solution.
'''
def hermite(tt, yy, ffy):
    h = tt[1] - tt[0]
    # To store all the t values from start to end
    t = []
    # To store the u value computed at (t_i + (theta * h_i)).
    u = []
    # To store the derivative of u computed at (t_i + (theta * h_i)).
    u_d = []
    # To store the defect at (t_i + (theta * h_i)).
    d = []
    # To store all the u values computed
    uu = []
    # To store all the exact solutions at all the t values
    ffe = []
    # To store all the defect values in variable 'delta'
    delta = []

    for k in range (0, len(yy[0])):
        # For the first value, u_0(t_0)
        u.append((yy[0][k] * h00(0)) + (h * ffy[0][k] * h10(0)) + (yy[1][k] * h01(0)) + (h * ffy[1][k] * h11(0)))

        # For the first derivative value, u_0'(t_0)
        u_d.append(((yy[0][k] / h) * h00_d(0)) + (ffy[0][k] * h10_d(0)) + ((yy[1][k] / h) * h01_d(0)) + (ffy[1][k] * h11_d(0)))
    # Here fu = f(t_0, u_0(t_0))
    fu = f.formula(0, tt[0], u[:])
    if (f.exactExists):
        # Exact value at t_0
        fe = f.formula(1, tt[0], u[:])
        # Storing the value in the list named 'ffe'
        ffe.append(fe)

    # d_0(t_0) = u_0'(t_0) - f(t_0, u_0(t_0))
    for k in range (0, len(u)):
        d.append(u_d[k] - fu[k])

    # Storing the values in their corresponding lists
    t.append(tt[0])
    uu.append(u)
    delta.append(d)

    # Performing hermite interpolation on all the intervals
    for i in range (0, len(tt) - 1):
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
            fu = f.formula(0, (tt[i] + (theta * h)), u[:])

            if (f.exactExists):
                # Exact value at (t_i + (theta * h_i))
                fe = f.formula(1, (tt[i] + (theta * h)), u[:])
                # Storing the value in the list named 'ffe'
                ffe.append(fe)

            # d_i(t_i + (theta * h_i)) = u_i'(t_i + (theta * h_i)) - f(t_i + (theta * h_i), u_i(t_i + (theta * h_i)))
            for k in range (0, len(u)):
                d.append(u_d[k] - fu[k])

            # Storing the values in their corresponding lists
            t.append(tt[i] + (theta * h))
            uu.append(u)
            delta.append(d)
    return t, uu, ffe, delta

'''
Name: displayResults
Description: This function performs Hermite interpolation and displays the
                results in the console.
Parameters:
        reset  : reset is used to check if the lists containing the data require
                    a reset or not. The default value for reset is False.
Returns:    None
'''
def displayResults(reset=False):
    # For a full display of hermite interpolant 
    for i in range (0, len(config.t)):
        t, u, fe, d = hermite(config.t[i], config.y[i], config.f[i])
        if (f.exactExists):
            print ("i\t\t\tt\t\t\tu\t\t\tf\t\t\td")
            for i in range (0, len(t)):
                print (i+1, "\t", t[i], "\t", u[i], "\t", fe[i], "\t", d[i])
        else:
            print ("i\t\t\tt\t\t\tu\t\t\td")
            for i in range (0, len(t)):
                print (i+1, "\t", t[i], "\t", u[i], "\t", d[i])
        input("Press Enter to continue")
    if(reset):
        config.t = []
        config.y = []
        config.f = []

'''
Name: plotHermite
Description: This function performs Hermite interpolation and plots those results
                on the graph. It provides two graphs:
                Hermite Interpolant.html
                Defect.html
Parameters : None
Returns    : None
'''
def plotHermite():
    # Calling the hermite() function on the data at the smallest stepsize
    t, u, fe, d = hermite(config.t[len(config.t)-1], config.y[len(config.y)-1], config.f[len(config.f)-1])

    # Creating lists to prepare them for plotting
    t_list = []
    u_list = []
    if (f.exactExists):
        f_list = []
    d_list = []
    for j in range (0, len(u[0])):
        t_list.append(t)
        u_list.append([])
        if (f.exactExists):
            f_list.append([])
        d_list.append([])

    # Preparing the lists for plotting
    for i in range (0, len(t)):
        for j in range (0, len(u[i])):
            u_list[j].append(u[i][j])
            if (f.exactExists):
                f_list[j].append(fe[i][j])
            d_list[j].append(d[i][j])

    # Creating an object to create an HTML file for plotting
    bp.output_file("Plots/Hermite Interpolant.html")

    # Creating a figure to plot in the HTML file
    p = bp.figure(plot_width = 1366, plot_height = 768)

    # Plotting the data
    if (f.exactExists):
        p.multi_line(t_list + t_list, u_list + f_list)
    else:
        p.multi_line(t_list, u_list)

    # Showing the data in the browser
    bp.show(p)

    # Creating an object to create an HTML file for plotting
    bp.output_file("Plots/Defect.html")

    # Creating a figure to plot in the HTML file
    p = bp.figure(plot_width = 1366, plot_height = 768)

    # Plotting the data
    p.multi_line(t_list, d_list)

    # Showing the data in the browser
    bp.show(p)
