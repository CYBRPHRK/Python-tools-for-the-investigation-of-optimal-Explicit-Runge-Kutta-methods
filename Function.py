import math
import Simple as s
import PredatorPrey as pp

formulaNumber = 0

def displayFormulas():
    print ("Simple: f1 t tfinal y0")
    print ("Predator Prey: f2 t tfinal x y alpha beta gamma delta")
    print ("Simple for System: f3 t tfinal x y")

def setFormulaValues(fname):
    global formulaNumber
    y0 = []
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
    return data[1], data[2], y0

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
        return y[:]
    elif (formulaNumber == 3):
        return [y[0] - math.sin(t), y[1] - math.cos(t)]
