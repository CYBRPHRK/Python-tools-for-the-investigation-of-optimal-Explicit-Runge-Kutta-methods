import math
import bokeh.plotting as bp
import Simple as s
import PredatorPrey as pp

y0 = formulaNumber = eeOld = 0

def displayFormulas():
    print("Simple: f1 y0") 
    print("Predator Prey for x: f2 x y alpha beta gamma delta")
    print("Predator Prey for y: f3 x y alpha beta gamma delta")

def setFormulaValues(fname):
    global formulaNumber, y0
    data = fname.split()
    for i in range(1, len(data)):
        data[i] = int(data[i])
        
    if (data[0] == "f1"):
        formulaNumber = 1
        y0 = data[1]
    elif (data[0] == "f2"):
        formulaNumber = 2
        y0 = data[1]
        pp.setConstants(data[1], data[2], data[3], data[4], data[5], (data[6]))
    elif (data[0] == "f3"):
        formulaNumber = 3
        y0 = data[2]
        pp.setConstants(data[1], data[2], data[3], data[4], data[5], data[6])
    else:
        print ("No formula with that name.")
        exit(0)
        
def formula(t, y):
    if (formulaNumber == 1):
        return s.simple(t, y)
    elif (formulaNumber == 2):
        return pp.predatorPreyForX(t, y)
    elif (formulaNumber == 3):
        return pp.predatorPreyForY(t, y)

def eulersMethod(steps):
    global y0
    t = 0
    tfinal = 1
    y = y0
    #i = 1
    h = (tfinal - t) / steps
    tt = [t]
    yy = [y]
    ee = []
    
    while (t < tfinal):
        y = y + (h * formula(t, y))
        t = t + h
        #t = i * h
        #i = i + 1
        tt.append(t)
        yy.append(y)
        
    for j in range(0, len(yy)):
        ee.append(yy[j] - math.exp((-1) * tt[j]))
    return ee, tt, yy

def findOrder(ee, steps):
    global eeOld
    if (steps > 1):
        print ("ee: " + str(ee[len(ee) - 1]) + "\teeOld: " + str(eeOld) +
                   "\tsteps: " + str(steps) + "\teeOld/ee: " + str(eeOld/ee[len(ee) - 1]))
    eeOld = ee[len(ee) - 1]

def plotGraph(index, ee, tt, yy):
    bp.output_file("Plot" + str(index) + ".html")

    p = bp.figure(plot_width = 400, plot_height = 400)

    p.multi_line([tt,tt],[yy,ee])

    bp.show(p)
