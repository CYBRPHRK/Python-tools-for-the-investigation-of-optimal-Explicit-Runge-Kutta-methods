import Simple as s
import config

formulaNumber = 0

'''
Name: displayFormulas
Description: A function to get the formula number along
                with the respective values.
Parameters:
        None
Returns:
        fname   : returns a string with the formula number
                    and values provided by the user
'''
def displayFormulas():
    config.log.info("displayFormulas() started")
    print ("Simple: f1 t tfinal y0")
    print ("Predator Prey: f2 t tfinal x y alpha beta gamma delta")
    print ("Simple for System: f3 t tfinal x y")
    print ("Test F4: f4 t tfinal y0")
    print ("Test F5: f5 t tfinal y0")
    print ("Test F6: f6 t tfinal y0")
    print ("Test F7: f7 t tfinal y0")
    print ("Test F8: f8 t tfinal y0")
    print ("Test F9: f9 t tfinal y0 alpha")
    print ("Sample COVID-19 Model: f10 t tfinal")
    fname = input("\nEnter the formula with values respectively (Use spaces between the values like shown above):\n")
    config.log.info("fname =", fname)
    return fname

'''
Name: setFormulaValues
Description: A function to set formula number and the
                respective values for the formulas accordingly.
Parameters:
        fname   : fname has the formula number as well as the
                    respective values for the formulas to be used
Returns:
        data[1] : The value of t0 for the initial time of the
                    formula
        data[2] : The value of tf for the final time of the
                    formula (tfinal)
        y[0]    : A list of initial values of y at time t0
'''
def setFormulaValues(fname):
    config.log.info("setFormulaValues() started")
    global formulaNumber
    y0 = []
    data = fname.split()
    for i in range(1, len(data)):
        data[i] = float(data[i])
        
    formulaNumber = int (data[0][1:])

    if(formulaNumber == 2):
        y0.append(data[3])
        y0.append(data[4])
        s.setConstants(data[5], data[6], data[7], data[8])
    elif (formulaNumber == 3):
        y0.append(data[3])
        y0.append(data[4])
    elif (formulaNumber == 9):
        y0.append(data[3])
        s.setConstants(data[4])
    elif (formulaNumber == 10):
        y0 = s.sampleCOVID19ModelInitializer()
    elif ((formulaNumber == 1) or ((formulaNumber >= 4) and (formulaNumber <= 8))):
        y0.append(data[3])
    else:
        print ("No formula with that name.")
        exit(0)
        
    return data[1], data[2], y0

'''
Name: formula
Description: A function to get the:
                i = 0: approximate values of y
                i = 1: exact values of y
                i = 2: error values at t with a given y

             by calling the respective formula function
             according to the formula number.
Parameters:
        t   : The value of t after a certain steps
        y   : The list of values of y at step t
Returns:
        for i = 0:
            y[t+h]  : The list of approximate values of y from
                      the respective formula function for the
                      next step t + h
        for i = 1:
            y[t]    : The list of exact values of y from the
                      respective formula function for the
                      step t
        for i = 2:
            e       : The list of error values with a given y
                      from the respective formula function
                      for the step t
'''
def formula(i, t, y):
    config.log.info("formula() started")
    if (formulaNumber == 1):
        return s.simple(i, t, y)
    elif (formulaNumber == 2):
        return s.predatorPrey(i, t, y)
    elif (formulaNumber == 3):
        return s.simple_sys(i, t, y)
    elif (formulaNumber == 4):
        return s.TestF4(i, t, y)
    elif (formulaNumber == 5):
        return s.TestF5(i, t, y)
    elif (formulaNumber == 6):
        return s.TestF6(i, t, y)
    elif (formulaNumber == 7):
        return s.TestF7(i, t, y)
    elif (formulaNumber == 8):
        return s.TestF8(i, t, y)
    elif (formulaNumber == 9):
        return s.TestF9(i, t, y)
    elif (formulaNumber == 10):
        return s.sampleCOVID19Model(i, t, y)
