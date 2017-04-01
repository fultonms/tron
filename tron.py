from sympy.geometry import Point

class TronPoint(object):
   def __init__(self, point, label):
      self.point = point
      self.label = label

   def setPoint(point):
      self.point = point

   def setLabel(label):
      self.label = label

   def __str__(self):
      return "TronPoint" + str(self.point) + ' Label:' + str(self.label) + "\n"

class Tron(object):
   def __init__(self, dim, points=[]):
      self.dim = dim
      self.points = points
      self.v = None

   def setPoints(self, points):
      self.points = points

   def addPoints(self,p):
      self.points.append(p)

   def __str__(self):
      s = ""
      s += "Tron:\n"
      s += "dim = " +  str(self.dim) + "\n"
      s += "Points:\n"
      for p in self.points:
         s += '\t' + str(p)
      return s

   def updateVector(self):
      return None

if __name__ == '__main__':
   tron = None

   print("Welcome to tron.\n\n")

   fileb = raw_input("Point file [Y/N]?")

   if fileb == 'Y':
      filename = raw_input("Filename:")
      f = open(filename, 'r')

      dim = 0
      points = []

      for line in f.readlines():
         line = line.rstrip('\n')
         chars = line.split(" ")
         if len(chars) == 1:
            dim = int(chars[0])
         else:
            coords = []
            for c in chars[:-1]:
               coords.append(int(c))

            p = Point(coords)
            assert(p.ambient_dimension == dim)
      
            l = int(chars[-1])
            assert(l == 1 or l == -1)

            tp = TronPoint(p,l)
            points.append(tp)

      tron = Tron(dim, points)
      print(str(tron))
         
   else:
      dim = input("Enter your dimmension:")
      stop= raw_input("Enter a point? [Y/N]?")

      points = []
      while(stop == 'Y'):
         coords = []
         while (len(coords) < dim):
            coords.append(raw_input())

         p = Point(coords)
         assert(p.ambient_dimension == dim)

         l = input("Label:")
         assert(l == 1 or l == -1)

         tp = TronPoint(p, l)
         points.append(p)
         stop = raw_input("Enter a point? [Y/N]?")

      tron = Tron(dim, points)
      print(str(tron))

else:
   print "pls no importerino senpai"
