
import EulersMethod as em

em.displayFormulas()
fname = input("Enter the formula with values respectively (Use spaces between the values like shown above):\n")
em.setFormulaValues(fname)

j = 1
while(j <= 512):
    ee, tt, yy = em.eulersMethod(j)
    #em.findOrder(ee, j)
    j = j * 2
