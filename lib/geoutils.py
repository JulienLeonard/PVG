from utils import *

def dist2(p1,p2):
    return Vector().points(p1,p2).length2()

def dist(p1,p2):
    return Vector().points(p1,p2).length()

def anglerange():
    return R(0.0,2* math.pi)


#
# Interface to define 2D geometry entity (Point or Vector)
#
class Coords:
    def __init__(self,x=0.0,y=0.0):
        self.mx = x
        self.my = y

    def x(self,v=None):
        if not v == None:
            self.mx = v
            return self
        else:
            return self.mx

    def y(self,v=None):
        if not v == None:
            self.my = v
            return self
        else:
            return self.my

    def coords(self,v=None):
        if not v == None:
            self.mx = v[0]
            self.my = v[1]
            return self
        else:
            return (self.mx,self.my)


#
# class Point
#
class Point(Coords):

    def add(self,v):
        return Point(self.x() + v.x(),self.y() + v.y())
    

#
# class Vector
#
class Vector(Coords):

    def __init__(self,x=1.0,y=0.0):
        self.mx = x
        self.my = y
        self.ml  = None

    def points(self,p1,p2):
        self.mx = (p2.x() - p1.x())
        self.my = (p2.y() - p1.y())
        self.ml  = None
        return self

    def length2(self):
        _x = self.x()
        _y = self.y()
        return _x *_x + _y *_y

    def length(self):
        if self.ml == None:
            self.ml = math.sqrt(self.length2())
        return self.ml

    def normalize(self):
        l = self.length()
        if l == 0.0:
            return Vector(0.0,0.0)
        else:
            return self.scale(1.0/l)

    def rotate(self,angle):
        cosa = math.cos(angle)
        sina = math.sin(angle)
        x = self.x()
        y = self.y()
        return Vector((x * cosa - y * sina),(x * sina + y * cosa ))

    def scale(self,ratio):
        return Vector(self.x()*ratio,self.y()*ratio)

VX0 = Vector(1.0,0.0)
VY0 = Vector(0.0,0.1)
V0  = Vector(0.0,0.0)
P0  = Point(0.0,0.0)
        
#
# compute the average point of a list of points
#
def pmiddle(points):
    listx = [p.x() for p in points]
    listy = [p.y() for p in points]
    return (sum(listx)/float(len(points)),sum(listy)/float(len(points)))


def bbox(points):
    xmin = points[0].x()
    xmax = points[0].x()
    ymin = points[0].y()
    ymax = points[0].y()
    
    for p in points:
        x,y = (p.x(),p.y())
        if (x < xmin):
            xmin = x
        elif (x > xmax):
            xmax = x
                
        if (y < ymin):
            ymin = y
        elif (y > ymax):
            ymax = y
    return [xmin,ymin,xmax,ymax]

def bbunion(bbox1,bbox2):
    # puts ("bbunion",bbox1,bbox2)
    xmin1,ymin1,xmax1,ymax1 = bbox1
    xmin2,ymin2,xmax2,ymax2 = bbox2
    xmin = lmin([xmin1,xmin2])
    ymin = lmin([ymin1,ymin2])
    xmax = lmax([xmax1,xmax2])
    ymax = lmax([ymax1,ymax2])
    return [xmin,ymin,xmax,ymax]

def bbunions(bboxlist):
    result = bboxlist[0]
    for bbox in bboxlist[1:]:
        result = bbunion(result,bbox)
    return result

def segviewbox(seg):
    return bbox([seg[0],seg[1]])

def bboxresize(bbox,factor):
    xmin,ymin,xmax,ymax = bbox
    newwidth  = (xmax - xmin) * factor
    newheight = (ymax - ymin) * factor
    xcenter,ycenter = pmiddle([Point(xmin,ymin),Point(xmax,ymax)])
    newxmin = xcenter - newwidth/2.0
    newxmax = xcenter + newwidth/2.0
    newymin = ycenter - newheight/2.0
    newymax = ycenter + newheight/2.0
    return (newxmin,newymin,newxmax,newymax)

def square(center,size):
    return [(center[0]-size/2.0,center[1]-size/2.0),
            (center[0]-size/2.0,center[1]+size/2.0),
            (center[0]+size/2.0,center[1]+size/2.0),
            (center[0]+size/2.0,center[1]-size/2.0)]

def rectangle(x1,y1,x2,y2):
    return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]
