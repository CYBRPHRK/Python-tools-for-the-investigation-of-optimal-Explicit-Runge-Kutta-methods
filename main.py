import EulersMethod as em
import Function as f
import Methods as m
import FileIO.FileIO as FileIO
import config
import Logger.Logger as log
import HermiteInterpolation as hi
#import bokeh.plotting as bp

def displayMenu():
    config.log.info("displayMenu() started")
    print ("1. Specific ODE on Specific Method")
    print ("2. Specific ODE on All Methods and Export in an file")
    choice = input("Enter your choice: ")
    config.log.info("choice:", choice)
    print ("")
    return int(choice)

def chooseMenuOption(choice):
    if (choice == 1):
        specificODESpecificMethod()
    elif (choice == 2):
        specificODEAllMethods()
    else:
        config.log.error("Invalid Choice.")
        print ("Invalid Choice.\n")
        chooseMenuOption(displayMenu())

def specificODESpecificMethod():
    t0, tf, y0 = f.setFormulaValues(f.displayFormulas())
    em.setInitialValues(t0, tf, y0)

    m.displayMethods()

    j = 1
    while(j <= 6):
        ee, tt, yy = em.eulersMethod(j)
        order = em.findOrder(ee, j)
        for x in order:
            print (em.dictToString(x))
        print ()
        j = j + 1

def specificODEAllMethods():
    t0, tf, y0 = f.setFormulaValues(f.displayFormulas())
    em.setInitialValues(t0, tf, y0)

    config.file = FileIO.FileIO("Test Results/F" + str(f.formulaNumber) + ".txt", "w")
    fname = "F" + str(f.formulaNumber) + " " + str(t0) + " " + str(tf)
    for y in y0:
        fname = fname + " " + str(y)
    config.file.write(fname, end='\n\n')

    orders = []
    methodNumber = 1
    i = 1
    while(methodNumber < 10):
        case = i
        methodInfo = "methodNumber: " + str(methodNumber)
        if (methodNumber == 7) or (methodNumber == 9):
            methodInfo = methodInfo + " Case: " + str(case)

        config.file.write(methodInfo, end='')
        m.setMethodValues(methodNumber, True, case)
        j = 1
        while(j <= 6):
            ee, tt, yy = em.eulersMethod(j)
            order = em.findOrder(ee, j)
            for x in order:
                config.file.write(em.dictToString(x))
            config.file.write("")
            j = j + 1
        orders.append(order)
        if ((methodNumber != 7) and (methodNumber != 9)):
            methodNumber += 1
        else:
            if (((methodNumber == 7) and (i == 3)) or ((methodNumber == 9) and (i == 5))):
                methodNumber += 1
                i = 1
            else:
                i += 1
    em.methodAccuracyRatio(orders)

config.log = log.Logger("Numerical Analysis Research Thesis Log")
chooseMenuOption(displayMenu())

# For Full test
for i in range (0, len(config.t)):
    u, e = hi.hermite(config.t[i], config.y[i], config.f[i])
    d = hi.defect(config.t[i], config.y[i], config.f[i])
    print ("\tu\t\t\tf\t\t\td")
    for j in range (0, len(u)):
        print ("Step:", j+1)
        print ("t =", config.t[i][j])
        for k in range (0, len(u[i])):
            print (u[j][k], "\t", e[j][k], "\t", d[j][k])

del config.file
del config.log

'''
ee, tt, yy = em.eulersMethod(3)

bp.output_file("Plot.html")

p = bp.figure(plot_width = 400, plot_height = 400)

y1 = y2 = []

for i in yy:
    y1.append(i[0])
    y2.append(i[1])

p.multi_line([tt,tt],[y1,y2])

bp.show(p)
'''
