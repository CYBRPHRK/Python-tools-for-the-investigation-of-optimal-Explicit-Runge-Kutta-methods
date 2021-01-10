import math
import bokeh.plotting as bp
import Methods as m
import Function as f
import config

t0 = tf = 0
eeOld = y0 = []

def setInitialValues(t, tfinal, y):
    global t0, tf, y0
    t0, tf, y0 = t, tfinal, y[:]

def eulersMethod(steps):
    t = t0
    tfinal = tf
    y = y0[:]
    h = math.pow(2, (steps * (-1)))
    tt = [t]
    yy = [y[:]]
    ee = []
    
    while (t < tfinal):
        #fy = formula(t, y[:])
        fy = m.method(t, y[:], h)
        for i in range(0, len(y)):
            y[i] = y[i] + (h * fy[i])
        t = t + h
        tt.append(t)
        yy.append(y[:])
    
    for j in range(0, len(yy)):
        e = f.formulaExact(tt[j], yy[j])
        for i in range (0, len(e)):
            #print ("In")
            e[i] = abs(e[i])
        #print (e)
        ee.append(e[:])
    return ee, tt, yy

def findOrder(ee, steps):
    global eeOld
    i = 0
    orders = []
    for e in ee[len(ee) -1]:
        order = {}
        order["ee[" + str(i) + "]"] = e
        order["Steps"] = math.pow(2, (steps * (-1)))
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

def methodAccuracyRatio(orders):
    config.file.write("Method Accuracy Ratios:")
    for j in range (0, len(orders[0])):
        minError = min(orders[1][j].get("ee[" + str(j) + "]"), orders[2][j].get("ee[" + str(j) + "]"),
                       orders[3][j].get("ee[" + str(j) + "]"))
        orders[1][j]['RelError'] = (orders[1][j].get("ee[" + str(j) + "]")) / minError
        orders[2][j]['RelError'] = (orders[2][j].get("ee[" + str(j) + "]")) / minError
        orders[3][j]['RelError'] = (orders[3][j].get("ee[" + str(j) + "]")) / minError
        
        minError = min(orders[4][j].get("ee[" + str(j) + "]"), orders[5][j].get("ee[" + str(j) + "]"),
                       orders[6][j].get("ee[" + str(j) + "]"), orders[7][j].get("ee[" + str(j) + "]"))
        orders[4][j]['RelError'] = (orders[4][j].get("ee[" + str(j) + "]")) / minError
        orders[5][j]['RelError'] = (orders[5][j].get("ee[" + str(j) + "]")) / minError
        orders[6][j]['RelError'] = (orders[6][j].get("ee[" + str(j) + "]")) / minError
        orders[7][j]['RelError'] = (orders[7][j].get("ee[" + str(j) + "]")) / minError

        minError = min(orders[8][j].get("ee[" + str(j) + "]"), orders[9][j].get("ee[" + str(j) + "]"),
                       orders[10][j].get("ee[" + str(j) + "]"), orders[11][j].get("ee[" + str(j) + "]"),
                       orders[12][j].get("ee[" + str(j) + "]"))
        orders[8][j]['RelError'] = (orders[8][j].get("ee[" + str(j) + "]")) / minError
        orders[9][j]['RelError'] = (orders[9][j].get("ee[" + str(j) + "]")) / minError
        orders[10][j]['RelError'] = (orders[10][j].get("ee[" + str(j) + "]")) / minError
        orders[11][j]['RelError'] = (orders[11][j].get("ee[" + str(j) + "]")) / minError
        orders[12][j]['RelError'] = (orders[12][j].get("ee[" + str(j) + "]")) / minError

    for x in orders:
        for y in x:
            config.file.write(dictToString(y))
        config.file.write("")

def dictToString(dict):
    dictString = ""
    for x in dict:
        dictString = dictString + x + ": " + str(dict.get(x)) + "\t"
    return dictString.strip()

#Depreciated
def plotGraph(index, ee, tt, yy):
    bp.output_file("Plot" + str(index) + ".html")

    p = bp.figure(plot_width = 400, plot_height = 400)

    p.multi_line([tt,tt],[yy,ee])

    bp.show(p)
