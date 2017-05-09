import sys
from random import choice
import numpy as np
from numpy import linalg as lin

def sign(a):
   if a >= 0:
     return 1
   else:
     return -1

def classify(w, p):
    return sign(np.inner(w, p))


class Point(object):
   def __init__(self, coords, label):
      assert(label == -1 or label == 1)

      self.coords = np.array(coords)
      self.dim = len(coords)
      self.label = label

   def normalize(self):
      self.coords = np.multiply(self.coords, 1/lin.norm(self.coords))

   def __str__(self):
      return "Point: " + str(self.coords) + " " + str(self.label)
   
class Tron(object):
   def __init__(self, dim, points=[]):
      self.dim = dim
      self.points = points
      self.w = np.zeros(dim + 1)

   def addPoint(self, point):
      self.points.append(point)

   def update(self):
      for p in self.points:
          tmp = Point(p.coords, p.label)
          tmp.normalize()
          self.w = np.add(self.w, np.multiply(tmp.label, tmp.coords))

   def readPoints(self, filename):
        dim = 0
        points = []
        f = open(filename, 'r')

        for line in f.readlines():
            line = line.rstrip('\n')
            chars = line.split(" ")

            if len(chars) == 1:
                self.dim = int(chars[0])
            else:
                coords = []
                for c in chars[:-1]:
                    coords.append(float(c))
                coords.append(1)

                l = int(chars[-1])
                assert(l == 1 or l == -1)

                p = Point(coords, l)
                p.normalize()
                points.append(p)

        self.points = points

if __name__ == '__main__':
    perceptron = Tron(0)
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        perceptron.readPoints(filename)
        perceptron.update()
        print "Weights: ", perceptron.w
