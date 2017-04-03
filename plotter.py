import tron
import matplotlib.pyplot as plt
import numpy as np

perceptron = tron.Tron(2)
fig = None
line = None

def onclick(event):
   if (event.xdata == None or event.ydata == None):
      return None

   if event.button == 1:
      perceptron.addPoint(tron.Point([event.xdata, event.ydata], 0))
      perceptron.learn()     
   elif event.button == 3:
      perceptron.addPoint(tron.Point([event.xdata, event.ydata], 1))
      perceptron.learn()
   else:
      return None

   plt.cla()
   line.plot(perceptron.v)
   for p in perceptron.points:
      if p.label == 0:
         line.plot(p.coords[0], p.coords[1], "ro")
      elif p.label == 1:
         line.plot(p.coords[0], p.coords[1], "bo")

   fig.canvas.draw()
 

fig = plt.figure()

line = fig.add_subplot(111)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

fig.show()
input()
