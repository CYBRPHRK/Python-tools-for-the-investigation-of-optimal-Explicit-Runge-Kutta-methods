import math
import bokeh.plotting as bp
import Methods as m
import Function as f
import config

t0 = tf = 0
eeOld = y0 = []

'''
Name: setInitialValues
Description: This function sets the initial values for a method.
Parameters:
        t       : t is the initial time.
        tfinal  : tfinal is the final time.
        y       : y is the initial value for the given IVODE.
Returns:    None
'''
def setInitialValues(t, tfinal, y):
    global t0, tf, y0
    t0, tf, y0 = t, tfinal, y[:]

'''
Name: eulerMethod
Description: This function computes the approximate solution for an IVODE using a
                given ERK method.
Parameters:
        steps   : steps is the parameter provided to compute the stepsize.
Returns:
        if (f.exactExists = True):
            ee  : ee is the list of lists of errors in approximate numerical
                    solutions for the IVODE.
            tt  : tt is the list of points on the domain where the approximate
                    numerical solution for the IVODE is computed.
            yy  : yy is the list of approximate numerical solutions for the IVODE
                    computed at points (tt) on the domain.
        if (f.exactExists = False):
            tt  : tt is the list of points on the domain where the approximate
                    numerical solution for the IVODE is computed.
            yy  : yy is the list of approximate numerical solutions for the IVODE
                    computed at points (tt) on the domain.
'''
def eulersMethod(steps):
    # Setting up all the initial values
    t = t0
    tfinal = tf
    y = y0[:]
    h = math.pow(2, (steps * (-1)))
    tt = [t]
    yy = [y[:]]
    ee = []
    config.ffy = []

    # Computing the approximate numerical solution
    while (t < tfinal):
        fy = m.method(t, y[:], h)
        for i in range(0, len(y)):
            y[i] = y[i] + (h * fy[i])
        t = t + h
        tt.append(t)
        yy.append(y[:])
    m.method(t, y[:], h)
    config.t.append(tt[:])
    config.y.append(yy[:])
    config.f.append(config.ffy[:])

    if (f.exactExists):
        # Computing the error
        for j in range(0, len(yy)):
            e = f.formula(2, tt[j], yy[j])
            for i in range (0, len(e)):
                e[i] = abs(e[i])
            ee.append(e[:])
        return ee, tt, yy
    else:
        return tt, yy

'''
Name: findOrder
Description: This function computes the ratio of the errors and
                order of convergence of a given ERK method.
Parameters:
        ee      : ee is the list of lists of errors in approximate numerical
                    solutions for the IVODE.
        steps   : steps is the parameter provided to compute the stepsize.
Returns:
        orders  : orders is the list of dictionaries which has error(s), stepsize,
                    ratio of the errors and order of convergence of the method.
'''
def findOrder(ee, steps):
    global eeOld
    i = 0
    orders = []
    for e in ee[len(ee) -1]:
        order = {}
        order["ee[" + str(i) + "]"] = e
        order["Stepsize"] = math.pow(2, (steps * (-1)))
        if (steps > 1):
            ratio = eeOld[i]/e
            order['eeOld/ee'] = ratio
            if (ratio == 0):
                order['Order'] = 'n/a'
            else:
                order['Order'] = round(math.log(ratio, 2))
        i += 1
        orders.append(order)
    eeOld = ee[len(ee) - 1]
    return orders

'''
Name: relToMinError
Description: This function computes the relative to minimum error for each order of
                ERK method and print them in the results text file.
Parameters:
        orders  : orders is the list of dictionaries which has error(s), stepsize,
                    ratio of the errors and order of convergence of the method.
Returns:    None
'''
def relToMinError(orders):
    config.file.write("Rel. To Min. Errors:")
    for j in range (0, len(orders[0])):
        minError = min(orders[1][j].get("ee[" + str(j) + "]"), orders[2][j].get("ee[" + str(j) + "]"),
                       orders[3][j].get("ee[" + str(j) + "]"))
        orders[1][j]['RelError'] = (orders[1][j].get("ee[" + str(j) + "]")) / minError
        orders[2][j]['RelError'] = (orders[2][j].get("ee[" + str(j) + "]")) / minError
        orders[3][j]['RelError'] = (orders[3][j].get("ee[" + str(j) + "]")) / minError
        
        minError = min(orders[4][j].get("ee[" + str(j) + "]"), orders[5][j].get("ee[" + str(j) + "]"),
                       orders[6][j].get("ee[" + str(j) + "]"), orders[7][j].get("ee[" + str(j) + "]"),
                       orders[8][j].get("ee[" + str(j) + "]"))
        orders[4][j]['RelError'] = (orders[4][j].get("ee[" + str(j) + "]")) / minError
        orders[5][j]['RelError'] = (orders[5][j].get("ee[" + str(j) + "]")) / minError
        orders[6][j]['RelError'] = (orders[6][j].get("ee[" + str(j) + "]")) / minError
        orders[7][j]['RelError'] = (orders[7][j].get("ee[" + str(j) + "]")) / minError
        orders[8][j]['RelError'] = (orders[8][j].get("ee[" + str(j) + "]")) / minError

        minError = min(orders[9][j].get("ee[" + str(j) + "]"), orders[10][j].get("ee[" + str(j) + "]"),
                       orders[11][j].get("ee[" + str(j) + "]"), orders[12][j].get("ee[" + str(j) + "]"),
                       orders[13][j].get("ee[" + str(j) + "]"), orders[14][j].get("ee[" + str(j) + "]"))
        orders[9][j]['RelError'] = (orders[9][j].get("ee[" + str(j) + "]")) / minError
        orders[10][j]['RelError'] = (orders[10][j].get("ee[" + str(j) + "]")) / minError
        orders[11][j]['RelError'] = (orders[11][j].get("ee[" + str(j) + "]")) / minError
        orders[12][j]['RelError'] = (orders[12][j].get("ee[" + str(j) + "]")) / minError
        orders[13][j]['RelError'] = (orders[13][j].get("ee[" + str(j) + "]")) / minError
        orders[14][j]['RelError'] = (orders[14][j].get("ee[" + str(j) + "]")) / minError

    for x in orders:
        for y in x:
            config.file.write(dictToString(y))
        config.file.write("")

'''
Name: dictToString
Description: This function converts the data stored in a dictionary into string.
Parameters:
        dict    : dict is the dictionary in which the data is stored.
Returns:
        dictString  : dictString is the string converted from the dictonary.
'''
def dictToString(dict):
    dictString = ""
    # Fetching data from the dictonary and saving it in the string
    for x in dict:
        dictString = dictString + x + ": " + str(dict.get(x)) + "\t"
    # Returning the string after removing the extra whitespace
    return dictString.strip()
