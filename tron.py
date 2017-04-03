from random import choice
import numpy as np

unit_step = lambda x: 0 if x < 0 else 1

class Point(object):
   def __init__(self, coords, label):
      assert(label == 0 or label ==1)

      self.coords = np.array(coords)
      self.dim = len(coords)
      self.label = label

   def __str__(self):
      return "Point: " + str(self.coords) + " " + str(self.label)
   
class Tron(object):
   def __init__(self, dim, points=[]):
      self.dim = dim
      self.points = points
      self.v = np.zeros(dim)

   def learn(self):
      for p in self.points:
         predicted = np.dot(self.v, p.coords)
         error = p.label - unit_step(predicted)
         self.v += error * p.coords
         
   def predict(self, points):
      for p in points:
         predicted = np.dot(p.coords, self.v)
         print unit_step(predicted)
   
   def addPoint(self, point):
      self.points.append(point)

if __name__ == '__main__':   
   training = [
      Point([0,0,1], 0),
      Point([0,1,1], 1),
      Point([1,0,1], 1),
      Point([1,1,1], 1),
   ]
   tron = Tron(3, training)
   tron.learn()
   tron.predict(tron.points)
