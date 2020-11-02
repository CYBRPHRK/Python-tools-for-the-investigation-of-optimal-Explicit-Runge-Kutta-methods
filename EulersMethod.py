import math
import bokeh.plotting as bp
import Simple as s
import PredatorPrey as pp

t0 = tf = formulaNumber = 0
eeOld = y0 = []

def displayFormulas():
    print ("Simple: f1 t tfinal y0") 
    print ("Predator Prey: f2 t tfinal x y alpha beta gamma delta")
    print ("Simple for System: f3 t tfinal x y")

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
    elif (data[0] == "f3"):
        formulaNumber = 3
        y0.append(data[3])
        y0.append(data[4])
    else:
        print ("No formula with that name.")
        exit(0)
    t0, tf = data[1], data[2]
        
def formula(t, y):
    if (formulaNumber == 1):
        return s.simple(t, y)
    elif (formulaNumber == 2):
        return pp.predatorPrey(t, y)
    elif (formulaNumber == 3):
        return s.simple_sys(t, y)

def functionError(t, y):
    if (formulaNumber == 1):
        return [y[0] - math.exp((-1) * t)]
    elif (formulaNumber == 2):
        return [1, 1]
    elif (formulaNumber == 3):
        return [y[0] - math.sin(t), y[1] - math.cos(t)]

def eulersMethod(steps):
    t = t0
    tfinal = tf
    y = y0[:]
    #h = (tfinal - t)/steps
    h = math.pow(2, (steps * (-1)))
    tt = [t]
    yy = [y[:]]
    ee = []
    
    while (t < tfinal):
        fy = formula(t, y[:])
        for i in range(0, len(y)):
            y[i] = y[i] + (h * fy[i])
        #y = y + (h * formula(t, y))
        t = t + h
        tt.append(t)
        yy.append(y[:])
        
    for j in range(0, len(yy)):
        e = functionError(tt[j], yy[j])
        '''
        for k in range(0, len(yy[j]):
            e.append(yy[j][k] - math.exp((-1) * tt[j]))
        '''
        ee.append(e[:])
    return ee, tt, yy

def findOrder(ee, steps):
    global eeOld
    i = 0
    if (steps > 1):
        for e in ee[len(ee) -1]:
            print ("ee[", i, "]: ", e, "\teeOld[", i, "]: ", eeOld[i],
                       "\tsteps: ", steps, "\teeOld/ee: ", eeOld[i]/e)
            i += 1
        print()
    eeOld = ee[len(ee) - 1]

def plotGraph(index, ee, tt, yy):
    bp.output_file("Plot" + str(index) + ".html")

    p = bp.figure(plot_width = 400, plot_height = 400)

    p.multi_line([tt,tt],[yy,ee])

    bp.show(p)
