from random import choice
import numpy as np

def sign(w, x, b):
   if sum(wi * xi for wi, xi in zip(w, x)) + b > 0:
      return -1
   else:
      return 1


class Point(object):
   def __init__(self, coords, label):
      assert(label == -1 or label == 1)

      self.coords = np.array(coords)
      self.dim = len(coords)
      self.label = label

   def __str__(self):
      return "Point: " + str(self.coords) + " " + str(self.label)
   
class Tron(object):
   def __init__(self, dim, points=[]):
      self.dim = dim
      self.points = points
      self.w = np.zeros(dim)
      self.b = 0


   def addPointAndUpdate(self, point):
    if (point.label != sign(self.w, point.coords, self.b)):
      self.w += point.label * point.coords
      self.b += point.label

    self.points.append(point)