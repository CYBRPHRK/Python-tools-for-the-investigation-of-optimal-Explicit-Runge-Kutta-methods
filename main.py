import EulersMethod as em
import Function as f
import Methods as m
import FileIO.FileIO as FileIO
import config
import Logger.Logger as log
import HermiteInterpolation as hi

def displayMenu():
    config.log.info("displayMenu() started")
    print ("1. Specific IVODE on Specific Method")
    print ("2. Specific IVODE on All Methods and Export results to a file")
    choice = input("Enter your choice: ")
    config.log.info("choice:", choice)
    print ("")
    return int(choice)

def chooseMenuOption(choice):
    if (choice == 1):
        specificIVODESpecificMethod()
    elif (choice == 2):
        specificIVODEAllMethods()
    else:
        config.log.error("Invalid Choice.")
        print ("Invalid Choice.\n")
        chooseMenuOption(displayMenu())

def specificIVODESpecificMethod():
    t0, tf, y0 = f.setFormulaValues(f.displayFormulas())
    em.setInitialValues(t0, tf, y0)

    m.displayMethods()

    j = 1
    while(j <= 6):
        if (f.exactExists):
            ee, tt, yy = em.eulersMethod(j)
            order = em.findOrder(ee, j)
            for x in order:
                print (em.dictToString(x))
            print ()
        else:
            k = 0
            tt, yy = em.eulersMethod(j)
            for y in yy[len(yy) - 1]:
                print ("Steps:", (2 ** (j * (-1))), "\ty[" + str(k) + "]:", y)
                k += 1
            print ()
        j = j + 1
    hi.plotHermite()

def specificIVODEAllMethods():
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
            if (f.exactExists):
                ee, tt, yy = em.eulersMethod(j)
                order = em.findOrder(ee, j)
                for x in order:
                    config.file.write(em.dictToString(x))
                config.file.write("")
            else:
                k = 0
                tt, yy = em.eulersMethod(j)
                for y in yy[len(yy) - 1]:
                    config.file.write("Steps: " + str(2 ** (j * (-1))) + "\ty[" + str(k) + "]: " + str(y))
                    k += 1
                config.file.write("")
            j = j + 1
        if (f.exactExists):
            orders.append(order)
        if ((methodNumber != 7) and (methodNumber != 9)):
            methodNumber += 1
        else:
            if (((methodNumber == 7) and (i == 3)) or ((methodNumber == 9) and (i == 5))):
                methodNumber += 1
                i = 1
            else:
                i += 1
    if (f.exactExists):
        em.relToMinError(orders)

config.log = log.Logger("Numerical Analysis Research Thesis Log")
chooseMenuOption(displayMenu())

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
