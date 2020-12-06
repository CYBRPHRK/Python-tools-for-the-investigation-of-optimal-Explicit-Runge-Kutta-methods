import math
import bokeh.plotting as bp
import Methods as m
import Function as f

t0 = tf = 0
eeOld = y0 = []

def setInitialValues(t, tfinal, y):
    global t0, tf, y0
    t0, tf, y0 = t, tfinal, y[:]

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
        #fy = formula(t, y[:])
        fy = m.method(t, y[:], h)
        for i in range(0, len(y)):
            y[i] = y[i] + (h * fy[i])
        t = t + h
        tt.append(t)
        yy.append(y[:])
    
    for j in range(0, len(yy)):
        e = f.formulaExact(tt[j], yy[j])
        ee.append(e[:])
    return ee, tt, yy

def findOrder(ee, steps):
    global eeOld
    i = 0
    if (steps > 1):
        for e in ee[len(ee) -1]:
            ratio = eeOld[i]/e
            '''
            print ("ee[" + str(i) + "]:", e, "\teeOld["+ str(i) +"]:", eeOld[i],
                       "\tSteps:", math.pow(2, (steps * (-1))), "\teeOld/ee: ", ratio,
                       "\tOrder:", round(math.log(ratio, 2))) '''
            print ("ee[" + str(i) + "]:", e, end='')
            print ("\teeOld["+ str(i) +"]:", eeOld[i], end='')
            print ("\tSteps:", math.pow(2, (steps * (-1))), end='')
            print ("\teeOld/ee: ", ratio, end='')
            if (ratio <= 0):
                print ("\tOrder: n/a")
            else:
                print ("\tOrder:", round(math.log(ratio, 2)))
            
            i += 1
        print()
    eeOld = ee[len(ee) - 1]

#Depreciated
def plotGraph(index, ee, tt, yy):
    bp.output_file("Plot" + str(index) + ".html")

    p = bp.figure(plot_width = 400, plot_height = 400)

    p.multi_line([tt,tt],[yy,ee])

    bp.show(p)
