from utils import *

def dist2(p1,p2):
    x = p2.x - p1.x
    y = p2.y - p1.y
    return x*x + y*y

def dist(p1,p2):
    return math.sqrt(dist2(p1,p2))

def anglerange():
    return R(0.0,2* math.pi)


#
# Interface to define 2D geometry entity (Point or Vector)
#
class Coords:
    def __init__(self,x=0.0,y=0.0):
        self.mx = x
        self.my = y

    def x(self,v=""):
        if not v == "":
            self.mx = v
            return self
        else:
            return self.mx

    def y(self,v=""):
        if not v == "":
            self.my = v
            return self
        else:
            return self.my

    def coords(self,v=""):
        if not v == "":
            self.mx = v[0]
            self.my = v[1]
            return self
        else:
            return (self.mx,self.my)


#
# class Point
#
class Point(Coords):

    def addv(self,v):
        return Point(self.x() + v.x(),self.y() + v.y())
    

#
# class Vector
#
class Vector(Coords):

    def __init__(self,x=1.0,y=0.0):
        self.mx = x
        self.my = y
        self.ml  = None

    def length(self):
        if self.ml == None:
            x = self.x()
            y = self.y()
            self.ml = math.sqrt(x*x + y*y)
        return self.ml

    def normalize(self):
        if self.length() == 0.0:
            return Vector(0.0,0.0)
        else:
            return Vector(self.x()/self.length(),self.y()/self.length())

    def rotate(self,angle):
        cosa = math.cos(angle)
        sina = math.sin(angle)
        x1 = self.x()
        y1 = self.y()
        return Vector((x1 * cosa - y1 * sina),(x1 * sina + y1 * cosa ))

    def scale(self,ratio):
        return Vector(self.x()*ratio,self.y()*ratio)
        
#
# compute the average point of a list of points
#
def pmiddle(points):
    listx = [p.x for p in points]
    listy = [p.y for p in points]
    return (sum(listx)/float(len(coords)),sum(listy)/float(len(coords)))


