import math
import bokeh.plotting as bp
import Simple as s
import PredatorPrey as pp

eeOld = 0

def displayFormulas():
    print("Simple: f1 t tfinal y ")
    print("Predator Prey: f2 x y alpha beta gamma delta")

def formula(fname):
    data = fname.split()
    if (data[0] == "f1"):
        s.simple(data[1],data[2])
    elif (data[0] == "f2"):
        pp.predatorPrey(data[1], data[2], data[3], data[4], data[5], data[6])
    else:
        print ("No formula with that name.")

def eulersMethod(steps):
    t = 0
    tfinal = 1
    y = 1
    #i = 1
    h = (tfinal - t) / steps
    tt = [t]
    yy = [y]
    ee = []
    
    while (t < tfinal):
        y = y + (h * s.simple(t, y))
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
