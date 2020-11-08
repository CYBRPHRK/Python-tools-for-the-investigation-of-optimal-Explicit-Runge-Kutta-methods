import EulersMethod as em
import Function as f
import Methods as m
import bokeh.plotting as bp

f.displayFormulas()
fname = input("\nEnter the formula with values respectively (Use spaces between the values like shown above):\n")
t0, tf, y0 = f.setFormulaValues(fname)
em.setInitialValues(t0, tf, y0)

m.displayMethods()
mname = input("\nEnter the method with values respectively (Use spaces between the values like shown above):\n")
m.setMethodValues(mname)

j = 1
while(j <= 6):
    ee, tt, yy = em.eulersMethod(j)
    em.findOrder(ee, j)
    j = j + 1

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
