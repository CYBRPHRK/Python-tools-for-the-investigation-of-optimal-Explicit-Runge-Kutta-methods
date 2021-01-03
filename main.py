import EulersMethod as em
import Function as f
import Methods as m
import FileIO.FileIO as FileIO
import config
import Logger.Logger as log
#import bokeh.plotting as bp

def displayMenu():
    config.log.info("displayMenu() started")
    print ("1. Specific ODE on Specific Method")
    print ("2. Specific ODE on All Methods and Export in an file")
    print ("3. Analyze the Computations from a file")
    choice = input("Enter your choice: ")
    config.log.info("choice:", choice)
    print ("")
    return int(choice)

def chooseMenuOption(choice):
    if (choice == 1):
        specificODESpecificMethod()
    elif (choice == 2):
        specificODEAllMethods()
    elif (choice == 3):
        computationsAnalysis()
    else:
        log.error("Invalid Choice.")
        print ("Invalid Choice.")

def specificODESpecificMethod():
    t0, tf, y0 = f.displayFormulas()
    em.setInitialValues(t0, tf, y0)

    m.displayMethods()

    j = 1
    while(j <= 6):
        ee, tt, yy = em.eulersMethod(j)
        order = em.findOrder(ee, j)
        print (order)
        j = j + 1

def specificODEAllMethods():
    t0, tf, y0 = f.displayFormulas()
    em.setInitialValues(t0, tf, y0)

    config.file = FileIO.FileIO("Test Results/F" + str(f.formulaNumber) + ".txt", "w")
    fname = "F" + str(f.formulaNumber) + " " + str(t0) + " " + str(tf)
    for y in y0:
        fname = fname + " " + str(y)
    config.file.write(fname)

    orders = []
    methodNumber = 1
    i = 1
    while(methodNumber < 10):
        case = i
        methodInfo = "\nmethodNumber: " + str(methodNumber)
        if (methodNumber == 7):
            case = case + 1
            methodInfo = methodInfo + " Case: " + str(case)
        elif (methodNumber == 9):
            if (i != 1):
                case = case + 1

            methodInfo = methodInfo + " Case: " + str(case)
        config.file.write(methodInfo, end='')
        m.setMethodValues(methodNumber, True, case)
        j = 1
        while(j <= 6):
            ee, tt, yy = em.eulersMethod(j)
            order = em.findOrder(ee, j)
            config.file.write(order)
            j = j + 1
        orders.append(order)
        if ((methodNumber != 7) and (methodNumber != 9)):
            methodNumber += 1
        else:
            if (((methodNumber == 7) and (i == 2)) or ((methodNumber == 9) and (i == 4))):
                methodNumber += 1
                i = 1
            else:
                i += 1

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
