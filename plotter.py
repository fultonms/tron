import tron
import matplotlib.pyplot as plt
import numpy as np
from pylab import norm

perceptron = tron.Tron(2)
fig = None
line = None

def onclick(event):
   if (event.xdata is None or event.ydata is None):
      return None

   if event.button == 1:
      perceptron.addPointAndUpdate(tron.Point([event.xdata, event.ydata], -1))
   elif event.button == 3:
      perceptron.addPointAndUpdate(tron.Point([event.xdata, event.ydata], 1))
   else:
      return None

   plt.cla()

   n = norm(perceptron.w)
   ww = perceptron.w/n
   ww1 = [ww[1], -ww[0]]
   ww2 = [-ww[1], ww[0]]
   
   line.plot([ww1[0], ww2[0]],[ww1[1], ww2[1]])
   print perceptron.w
   for p in perceptron.points:
      if p.label == -1:
         line.plot(p.coords[0], p.coords[1], "ro")
      elif p.label == 1:
         line.plot(p.coords[0], p.coords[1], "bo")

   fig.canvas.draw()
 

fig = plt.figure()

line = fig.add_subplot(111)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig.show()
input()
