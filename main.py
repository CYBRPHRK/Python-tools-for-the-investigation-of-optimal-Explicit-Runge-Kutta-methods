import EulersMethod as em
import Function as f
import Methods as m
import bokeh.plotting as bp

def displayMenu():
    print ("1. Specific ODE on Specific Method")
    print ("2. Specific ODE on All Methods and Export in an file")
    print ("3. Analyze the Computations from a file")
    choice = input("Enter your choice: ")
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
        print ("Invalid Choice.")

def specificODESpecificMethod():
    t0, tf, y0 = f.displayFormulas()
    em.setInitialValues(t0, tf, y0)

    m.displayMethods()

    j = 1
    while(j <= 6):
        ee, tt, yy = em.eulersMethod(j)
        em.findOrder(ee, j)
        j = j + 1

def specificODEAllMethods():
    t0, tf, y0 = f.displayFormulas()
    em.setInitialValues(t0, tf, y0)

    methodNumber = 1
    i = 1
    while(methodNumber < 10):
        print ("methodNumber:", methodNumber)
        m.setMethodValues(methodNumber)
        j = 1
        while(j <= 6):
            ee, tt, yy = em.eulersMethod(j)
            em.findOrder(ee, j)
            j = j + 1
            
        if ((methodNumber != 7) and (methodNumber != 9)):
            methodNumber += 1
        else:
            if (((methodNumber == 7) and (i == 2)) or ((methodNumber == 9) and (i == 4))):
                methodNumber += 1
                i = 1
            else:
                i += 1

chooseMenuOption(displayMenu())

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
