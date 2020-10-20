import EulersMethod as em

em.displayFormulas()
fname = input("\nEnter the formula with values respectively (Use spaces between the values like shown above):\n")
em.setFormulaValues(fname)

j = 1
while(j <= 8):
    ee, tt, yy = em.eulersMethod(j)
    em.findOrder(ee, j)
    j = j * 2
