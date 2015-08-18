from utils import *
from range import *

#
# define angle range
#
def anglerange():
    return R(0.0,2* math.pi)


#
# define a Point range
#
class PR:
    def __init__(self,v1,v2):
        self.mv1 = v1
        self.mv2 = v2

    def sample(self,t):
        return psample((self.mv1,self.mv2),t)


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
    
    def sub(self,p):
        return Vector(self.x() - p.x(),self.y() - p.y())

    def rotate(self,center,angle):
        return center.add( vector(center,self).rotate(angle) )

    def sym(p,center):
        return center.add(vector(p,center))


#
# class Vector
#
class Vector(Coords):

    #
    # constructor
    #
    def __init__(self,x=1.0,y=0.0):
        self.mx = x
        self.my = y
        self.ml  = None
        
    #
    # compute coords of vector from extremities
    #
    def points(self,p1,p2):
        self.mx = (p2.x() - p1.x())
        self.my = (p2.y() - p1.y())
        self.ml  = None
        return self

    #
    # compute the power2 of the length of the vector
    #
    def length2(self):
        _x = self.x()
        _y = self.y()
        return _x *_x + _y *_y

    #
    # compute the norm of the vector
    #
    def length(self):
        if self.ml == None:
            self.ml = math.sqrt(self.length2())
        return self.ml

    #
    # return a normalized vector
    #
    def normalize(self):
        l = self.length()
        if l == 0.0:
            return Vector(0.0,0.0)
        else:
            return self.scale(1.0/l)

    #
    # rotate a vector
    #
    def rotate(self,angle):
        cosa = math.cos(angle)
        sina = math.sin(angle)
        x = self.x()
        y = self.y()
        return Vector((x * cosa - y * sina),(x * sina + y * cosa ))

    #
    # scale a vector
    #
    def scale(self,ratio):
        return Vector(self.x()*ratio,self.y()*ratio)

#
# default defs
#
VX0 = Vector(1.0,0.0)
VY0 = Vector(0.0,0.1)
V0  = Vector(0.0,0.0)
P0  = Point(0.0,0.0)

#
# shortcut: build a vector from extremities
#
def vector(p1,p2):
    return Vector().points(p1,p2)

#
# compute the power2 of the dist between 2 points
#
def dist2(p1,p2):
    return vector(p1,p2).length2()

#
# compute the dist betweem 2 points
#
def dist(p1,p2):
    return vector(p1,p2).length()

        
#
# compute the average point of a list of points
#
def pmiddle(points):
    listx = [p.x() for p in points]
    listy = [p.y() for p in points]
    return Point(sum(listx)/float(len(points)),sum(listy)/float(len(points)))


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

def viewportfromviewbox(cviewbox,factor):
    (xmin,ymin,xmax,ymax) = cviewbox
    xc = (xmin + xmax)/2.0;
    yc = (ymin + ymax)/2.0;
    d1 = xmax - xmin
    d2 = ymax - ymin
    dmax = dist(Point(0.0,0.0),Point(d1,d2))
    viewport = (xc,yc,(dmax / 2.0) * factor)
    return viewport



def bboxresize(bbox,factor):
    xmin,ymin,xmax,ymax = bbox
    newwidth  = (xmax - xmin) * factor
    newheight = (ymax - ymin) * factor
    xcenter,ycenter = pmiddle([Point(xmin,ymin),Point(xmax,ymax)]).coords()
    newxmin = xcenter - newwidth/2.0
    newxmax = xcenter + newwidth/2.0
    newymin = ycenter - newheight/2.0
    newymax = ycenter + newheight/2.0
    return (newxmin,newymin,newxmax,newymax)

def unionviewboxes(viewboxes):
    cviewbox = viewboxes[0]
    for ccviewbox in viewboxes:
        cviewbox = mergeviewboxes(cviewbox,ccviewbox)
    return cviewbox

def mergeviewboxes(viewbox1,viewbox2):
    xmin1,ymin1,xmax1,ymax1 = viewbox1
    xmin2,ymin2,xmax2,ymax2 = viewbox2
    
    xmin = xmin1
    ymin = ymin1
    xmax = xmax1
    ymax = ymax1

    if xmin2 < xmin:
        xmin = xmin2
    if ymin2 < ymin:
        ymin = ymin2
    if xmax2 > xmax:
        xmax = xmax2
    if ymax2 > ymax:
        ymax = ymax2

    return (xmin,ymin,xmax,ymax)

def viewboxpoints(points):
    xmin = points[0].x();
    xmax = points[0].y();
    ymin = points[0].x();
    ymax = points[0].y();
    for point in points[1:]:
        (x,y) = point.coords()
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
    return [xmin,ymin,xmax,ymax]


def square(center,size):
    return [(center[0]-size/2.0,center[1]-size/2.0),
            (center[0]-size/2.0,center[1]+size/2.0),
            (center[0]+size/2.0,center[1]+size/2.0),
            (center[0]+size/2.0,center[1]-size/2.0)]

def rectangle(x1,y1,x2,y2):
    return [(x1,y1),(x2,y1),(x2,y2),(x1,y2)]

def vscale(v,ratio):
    return (v[0] * ratio, v[1] * ratio)

def vsangle(v1,v2):
    return (vangle(v1) - vangle(v2))

def vangle(v):
    l = v.length()
    result = 0.0
    if (l > 0.0):
        norm = v.normalize()
        cosx,siny = norm.coords()
        result = math.acos( cosx )
        if (siny < 0.0):
            result = -result
    return result

def polygonsignedarea(points):
    signedArea = 0
    index = 0
    for (p1,p2) in pairs(points):
        signedArea += (p1.x() * p2.y() - p2.x() * p1.y())
    return signedArea / 2

def polygonclockwise(polygon):
    if ispolygonclockwise(polygon):
        return polygon
    return lreverse(polygon)

def ispolygonclockwise(polygon):
    if polygonsignedarea(polygon) < 0.0:
        return True
    return False


#
# order shapes by imbrication levels: level 0 is the highest (ie shapes not contained by any other)
#
def computeshapelevels(allbeziers):
    containgraph = {}
    for bezier1 in allbeziers:
        if not bezier1 in containgraph:
            containgraph[bezier1] = []
        for bezier2 in allbeziers:
            if not bezier2 == bezier1:
                if viewboxinside(bezier2.viewbox(),bezier1.viewbox()):
                    if not bezier2 in containgraph:
                        containgraph[bezier2] = []
                    puts("bezier",bezier2,"contains in bezier",bezier1)
                    containgraph[bezier2].append(bezier1)

    puts("define imbrication hierarchy ...")
    levels = {}
    levels["levels"] = []
    for bezier in allbeziers:
        ncontainers = len(containgraph[bezier])
        if not ncontainers in levels:
            levels[ncontainers] = []
            levels["levels"].append(ncontainers)
        levels[ncontainers].append(bezier)
    levels["levels"].sort()
    puts("levels list",levels["levels"])
    return levels

def viewboxinside(vb1,vb2):
    (xmin1,ymin1,xmax1,ymax1) = vb1
    (xmin2,ymin2,xmax2,ymax2) = vb2

    if xmin1 >= xmin2 and ymin1 >= ymin2 and xmax1 <= xmax2 and ymax1 <= ymax2:
        return True
    return False
