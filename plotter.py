import tron
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import numpy as np
from pylab import norm

perceptron = tron.Tron(2)
fig = None
line = None

def onclick(event):
   if (event.xdata is None or event.ydata is None):
      return None

   if event.button == 1:
      perceptron.addPoint(tron.Point([event.xdata, event.ydata, 1], -1))
      perceptron.update()
   elif event.button == 3:
      perceptron.addPoint(tron.Point([event.xdata, event.ydata, 1], 1))
      perceptron.update()
   else:
      return None

   plt.cla()
   plt.xlim(-2, 2)
   plt.ylim(-2, 2)

   if len(perceptron.points) > 1:
        if perceptron.w[1] != 1:
            x = (-(perceptron.w[0]*-1.5) - perceptron.w[2])/perceptron.w[1]
            y = (-(perceptron.w[0]*1.5) - perceptron.w[2])/perceptron.w[1]
            ax = plt.gca()
            ax.add_line(lines.Line2D([-2, 2], [x, y]))
   
   for p in perceptron.points:
      if p.label == -1:
         line.plot(p.coords[0], p.coords[1], "ro")
      elif p.label == 1:
         line.plot(p.coords[0], p.coords[1], "bo")

   plt.draw()
   plt.show()
 

fig = plt.figure()

line = fig.add_subplot(111)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig.show()
input()
