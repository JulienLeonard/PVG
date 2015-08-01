from utils import *

#
# Interface to define 2D geometry entity (Point or Vector)
#
class Coords:
    def __init__(self,x=0.0,y=0.0):
        self.mx = x
        self.my = y

    def x(self,v=""):
        if not v == "":
            self.mx = x
            return self
        else:
            return self.mx

    def y(self,v=""):
        if not v == "":
            self.my = y
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


#
# define a circle object
#
class Circle:
    def __init__(self,pcenter=Point(0.0,0.0),r=1.0):
        self.mcenter = pcenter
        self.mr      = r

    def coords(self,v=""):
        if not v == "":
            self.mcenter = Point(v[0],v[1])
            self.mr      = v[2]
            return self
        else:
            return (self.mcenter.x(),self.mcenter.y(),self.mr)


    def center(self,v=""):
        if not v == "":
            self.mcenter = v
            return self
        else:
            return self.mcenter

    def radius(self,v=""):
        if not v == "":
            self.mradius = v
            return self
        else:
            return self.mradius



def circlefromcoords(x,y,r):
    return Circle().coords(x,y,r)

def circlefromlist(coords):
    if len(coords) > 0:
        return circlefromcoords(coords[0],coords[1],coords[2])
    return ""

def pmiddle(points):
    listx = [p.x for p in points]
    listy = [p.y for p in points]
    return (sum(listx)/float(len(coords)),sum(listy)/float(len(coords)))

def dist2(p1,p2):
    x = p2.x - p1.x
    y = p2.y - p1.y
    return x*x + y*y

def dist(p1,p2):
    return math.sqrt(dist2(p1,p2))

