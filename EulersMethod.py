import math
import bokeh.plotting as bp
import Simple as s
import PredatorPrey as pp
import copy

t0 = tf = formulaNumber = 0
eeOld = y0 = []

def displayFormulas():
    print("Simple: f1 t tfinal y0") 
    print("Predator Prey: f2 t tfinal x y alpha beta gamma delta")

def setFormulaValues(fname):
    global formulaNumber, t0, tf, y0
    data = fname.split()
    for i in range(1, len(data)):
        data[i] = float(data[i])
        
    if (data[0] == "f1"):
        formulaNumber = 1
        y0.append(data[3])
    elif (data[0] == "f2"):
        formulaNumber = 2
        y0.append(data[3])
        y0.append(data[4])
        pp.setConstants(data[5], data[6], data[7], data[8])
    else:
        print ("No formula with that name.")
        exit(0)
    t0, tf = data[1], data[2]
        
def formula(t, y):
    if (formulaNumber == 1):
        return s.simple(t, y)
    elif (formulaNumber == 2):
        return pp.predatorPrey(t, y)

def eulersMethod(steps):
    t = t0
    tfinal = tf
    y = copy.deepcopy(y0)
    h = (tfinal - t) / steps
    tt = [t]
    yy = [copy.deepcopy(y)]
    ee = []
    
    while (t < tfinal):
        fy = formula(t, y)
        for i in range(0, len(y)):
            y[i] = y[i] + (h * fy[i])
        #y = y + (h * formula(t, y))
        t = t + h
        tt.append(t)
        yy.append(copy.deepcopy(y))
        
    for j in range(0, len(yy)):
        e = []
        for k in yy[j]:
            e.append(k - math.exp((-1) * tt[j]))
        ee.append(copy.deepcopy(e))
    print ("Start")
    for e in ee:
        print (e)
    return ee, tt, yy

def findOrder(ee, steps):
    global eeOld
    i = 0
    if (steps > 1):
        for e in ee[len(ee) -1]:
            print ("ee[", i, "]: ", e, "\teeOld[", i, "]: ", eeOld[i],
                       "\tsteps: ", steps, "\teeOld/ee: ", eeOld[i]/e)
            i += 1
        #print ("ee: " + str(ee[len(ee) - 1]) + "\teeOld: " + str(eeOld) +
                   #"\tsteps: " + str(steps) + "\teeOld/ee: " + str(eeOld/ee[len(ee) - 1]))
        print("\n")
    eeOld = ee[len(ee) - 1]

def plotGraph(index, ee, tt, yy):
    bp.output_file("Plot" + str(index) + ".html")

    p = bp.figure(plot_width = 400, plot_height = 400)

    p.multi_line([tt,tt],[yy,ee])

    bp.show(p)
