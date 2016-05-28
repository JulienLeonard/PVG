from utils import *
from range import *

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

    def sym(self,center):
        return center.add(vector(self,center))

    def symx(self,symx):
        return Point(2.0*symx-self.x(),self.y())

    @staticmethod
    def P0():
        return Point(0.0,0.0)


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
        x = self.x()
        y = self.y()
        return (x *x + y *y)

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


    def scalex(self,rx):
        return Vector(self.x()*rx,self.y())


    def scaley(self,ry):
        return Vector(self.x(),self.y() * ry)

    #
    # compute the ortho vector of a vector
    #
    def ortho(self):
        return Vector(-self.y(),self.x())

    #
    # cross product
    #
    def cross(self,ov):
        return (self.x() * ov.y() - self.y() * ov.x())

    def add(self,v):
        return Vector(self.x() + v.x(),self.y() + v.y())

    @staticmethod
    def V0():
        return Vector(0.0,0.0)

    @staticmethod
    def VX0():
        return Vector(1.0,0.0)
    
    @staticmethod
    def VY0():
        return Vector(0.0,1.0)


#
# shortcut: build a vector from extremities
#
def vector(p1,p2):
    return Vector().points(p1,p2)

#
# compute the trigo vector from an angle
#
def angle2vector(a):
    return Vector(math.cos(a),math.sin(a))

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

#
# Segment
#
class Segment:
    
    def __init__(self,p1,p2):
        self.mp1 = p1
        self.mp2 = p2
        self.mrx = R(self.mp1.x(),self.mp2.x())
        self.mry = R(self.mp1.y(),self.mp2.y())
        

    def p1(self):
        return self.mp1

    def p2(self):
        return self.mp2

    def isPoint(self):
        return self.p1().coords() == self.p2().coords()

    def middle(self):
        return self.sample(0.5)

    def sample(self,t):
        t = R(0.0,1.0).trim(t)
        return Point(self.mrx.sample(t),self.mry.sample(t))

    def samples(self,npoints=None,abscissas=None):
        if not npoints == None:
            return [self.sample(abs) for abs in usamples(npoints)]
        if not abscissas == None:
            return [self.sample(abs) for abs in abscissas]

    def points(self):
        return (self.p1(),self.p2())

    def point(self,t):
        return self.sample(t)

    def coords(self):
        return self.p1().coords() + self.p2().coords()

    def vector(self):
        return vector(self.p1(),self.p2())

    def normal(self):
        return self.vector().ortho().normalize()

    def length(self):
        return self.vector().length()

    def length2(self):
        return self.vector().length2()

    def split(self,ntimes):
        return [Segment(p1,p2) for (p1,p2) in pairs(self.samples(ntimes+1))]

    def splitmaxsize(self,maxsize):
        if self.length() <= maxsize:
            return [self]
        else:
            return self.split(int(math.ceil(self.length()/maxsize)))

    def subsegment(self,t1,t2):
        return Segment(self.sample(t1),self.sample(t2))

    def bbox(self):
        return points2bbox([self.p1(),self.p2()])

    @staticmethod
    def intersect(seg1,seg2,strict=False):
        return (not raw_intersection(seg1.p1(),seg1.p2(),seg2.p1(),seg2.p2()) == None)

    @staticmethod
    def intersection(seg1,seg2):
        return raw_intersection(seg1.p1(),seg1.p2(),seg2.p1(),seg2.p2())

    @staticmethod
    def sort(segments):
        sortlist = [(seg.p1().x(),seg.p2().x(),seg) for seg in segments]
        sortlist.sort()
        return [seg for (dum,dum,seg) in sortlist]

    @staticmethod
    def S0():
        return Segment(Point(0.0,0.0),Point(1.0,0.0))



def pequal(p1,p2,error=0.00001):
    if (vector(p1,p2).length() < error):
        return True
    return False

def pdiff(p1,p2,error):
    return False if pequal(p1,p2,error) else True 

class Viewport:
    def __init__(self,center,radius):
        self.mcenter = center
        self.mradius = radius

    def center(self):
        return self.mcenter

    def radius(self):
        return self.mradius

    def circle(self):
        return Circle(self.center(),self.radius())

    def size(self):
        return self.radius() * 2.0

    def xmin(self):
        return self.mcenter.x() - self.radius()

    def ymin(self):
        return self.mcenter.y() - self.radius()


class BBox:

    def __init__(self,xmin,ymin,xmax,ymax):
        self.mxmin = xmin
        self.mxmax = xmax
        self.mymin = ymin
        self.mymax = ymax
        self.mcoords = (self.mxmin,self.mymin,self.mxmax,self.mymax)
        
    @staticmethod
    def fromCenterSize(ccenter,csize):
        return BBox(ccenter.x() - csize/2.0,ccenter.y() - csize/2.0, ccenter.x() + csize/2.0, ccenter.y() + csize/2.0)

    def coords(self):
        return self.mcoords

    def center(self):
        return Point((self.mxmin + self.mxmax)/2.0, (self.mymin + self.mymax)/2.0)

    def xsize(self):
        return (self.mxmax - self.mxmin)

    def ysize(self):
        return (self.mymax - self.mymin)

    def width(self):
        return self.xsize()

    def height(self):
        return self.ysize()

    def size(self):
        return max(self.xsize(),self.ysize())
    
    def radius(self):
        rx = self.xsize()/2.0
        ry = self.ysize()/2.0
        return math.sqrt(rx * rx + ry * ry)

    def viewport(self,ratio = 1.0):
        return Viewport(self.center(), self.radius() * ratio)

    def resize(self,factor):
        # xmin,ymin,xmax,ymax = self.coords()
        newwidth  = self.xsize() * factor
        newheight = self.ysize() * factor
        xcenter,ycenter = self.center().coords()
        newxmin = xcenter - newwidth/2.0
        newxmax = xcenter + newwidth/2.0
        newymin = ycenter - newheight/2.0
        newymax = ycenter + newheight/2.0
        return BBox(newxmin,newymin,newxmax,newymax)

    def contain(self,point):
        xmin,ymin,xmax,ymax = self.coords()
        x,y                 = point.coords()
        if xmin <= x and x <= xmax and ymin <= y and y <= ymax:
            return True
        return False

    def containbbox(self,obbox):
        xmin1,ymin1,xmax1,ymax1 = self.coords()
        xmin2,ymin2,xmax2,ymax2 = obbox.coords()
        if xmin1 < xmin2 and xmax2 < xmax1 and ymin1 < ymin2 and ymax2 < ymax1:
            return True
        return False

    
    def corners(self):
        xmin,ymin,xmax,ymax = self.coords()
        return [Point(xmin,ymin),Point(xmax,ymin),Point(xmax,ymax),Point(xmin,ymax)]

    def squarepoints(self):
        size   = self.size()
        center = self.center()
        return [Point(center.x()-size/2.0,center.y()-size/2.0),
                Point(center.x()-size/2.0,center.y()+size/2.0),
                Point(center.x()+size/2.0,center.y()+size/2.0),
                Point(center.x()+size/2.0,center.y()-size/2.0)]

    def intersect(self,obbox):
        xmin0,ymin0,xmax0,ymax0 = self.mcoords
        xmin,ymin,xmax,ymax     = obbox.mcoords
        return (xmin <= xmax0 and xmax >= xmin0 and ymin <= ymax0 and ymax >= ymin0)
        # if obbox.mcoords[0] > self.mcoords[2]:
        #     return False
        # if obbox.mcoords[2] < self.mcoords[0]:
        #     return False
        # if obbox.mcoords[1] > self.mcoords[3]:
        #     return False
        # if obbox.mcoords[3] < self.mcoords[1]:
        #     return False
        # return True
        

    def split4(self):
        (xmin,ymin,xmax,ymax) = self.coords()

        middlex = (xmin + xmax)/2.0
        middley = (ymin + ymax)/2.0
        
        return [BBox(xmin,    ymin   , middlex, middley),
                BBox(xmin,    middley, middlex, ymax   ),
                BBox(middlex, ymin   , xmax,    middley),
                BBox(middlex, middley, xmax,    ymax   )]

    def symx(self,symx):
        newxmin = 2.0 * symx - self.mxmin
        newxmax = 2.0 * symx - self.mxmax
        xmin  = min(newxmin,newxmax)
        xmax  = max(newxmin,newxmax)
        return BBox(xmin,self.mymin,xmax,self.mymax)

    def unionsymx(self,symx):
        return bbunion(self,self.symx(symx))

    def xmin(self):
        return self.coords()[0]

    def ymin(self):
        return self.coords()[1]

    def xmax(self):
        return self.coords()[2]

    def ymax(self):
        return self.coords()[3]

def bbunion(bbox1,bbox2):
    # puts ("bbunion",bbox1,bbox2)
    xmin1,ymin1,xmax1,ymax1 = bbox1.coords()
    xmin2,ymin2,xmax2,ymax2 = bbox2.coords()
    xmin = min(xmin1, xmin2)
    ymin = min(ymin1, ymin2)
    xmax = max(xmax1, xmax2)
    ymax = max(ymax1, ymax2)
    return BBox(xmin,ymin,xmax,ymax)

def bbunions(bboxlist):
    result = bboxlist[0]
    for bbox in bboxlist[1:]:
        result = bbunion(result,bbox)
    return result

def point2bbox(p):
    return BBox(p,p)

def points2bbox(points):
    if len(points) < 1:
        return None
    xmin = points[0].x()
    ymin = points[0].y()
    xmax = xmin
    ymax = ymin
    for p in points[1:]:
        xmin = min(p.x(),xmin)
        ymin = min(p.y(),ymin)
        xmax = max(p.x(),xmax)
        ymax = max(p.y(),ymax)
    return BBox(xmin,ymin,xmax,ymax)

def polygons2bbox(polygons):
    if len(polygons) < 1:
        return None
    return bbunions([polygon.viewbox() for polygon in polygons])

def segviewbox(seg):
    return BBox().frompoints([seg[0],seg[1]])

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
                    if bezier1.polygon().contain(bezier2.polygon().middle()):
                        if not bezier2 in containgraph:
                            containgraph[bezier2] = []
                        # puts("bezier",bezier2,"contains in bezier",bezier1)
                        containgraph[bezier2].append(bezier1)

    # puts("define imbrication hierarchy ...")
    levels = {}
    levels["levels"] = []
    for bezier in allbeziers:
        ncontainers = len(containgraph[bezier])
        if not ncontainers in levels:
            levels[ncontainers] = []
            levels["levels"].append(ncontainers)
        levels[ncontainers].append(bezier)
    levels["levels"].sort()
    # puts("levels list",levels["levels"])
    return levels

def viewboxinside(vb1,vb2):
    (xmin1,ymin1,xmax1,ymax1) = vb1.coords()
    (xmin2,ymin2,xmax2,ymax2) = vb2.coords()

    if xmin1 >= xmin2 and ymin1 >= ymin2 and xmax1 <= xmax2 and ymax1 <= ymax2:
        return True
    return False

def raw_intersection (p1,p2,p3,p4):
    x1,y1 = p1.coords()
    x2,y2 = p2.coords()
    x3,y3 = p3.coords()
    x4,y4 = p4.coords()
    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    uanum = (x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)
    ubnum = (x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)
    if (denom == 0.0 and uanum == 0.0 and ubnum == 0.0):
        # puts("denom == 0.0 and uanum == 0.0 and ubnum == 0.0")
        pp1 = min((x1,y1),(x2,y2))
        pp2 = max((x1,y1),(x2,y2))
        pp3 = min((x3,y3),(x4,y4))
        pp4 = max((x3,y3),(x4,y4))
        x1,y1 = pp1
        x2,y2 = pp2
        x3,y3 = pp3
        x4,y4 = pp4

        if x1 == x2 and x2 == x3 and x3 == x4:
            if R(y1,y2).contain(y3):
                if R(y1,y2).contain(y4):
                    result = Segment(Point(x3,y3),Point(x4,y4))
                else:
                    result = Segment(Point(x3,y3),Point(x2,y2))
            else:
                if R(y1,y2).contain(y4):
                    result = Segment(Point(x1,y1),Point(x4,y4))
                else: 
                    if R(y3,y4).contain(y1) and R(y3,y4).contain(y2):
                        result =  Segment(Point(x1,y1),Point(x2,y2))
                    else:
                        result = None
        else:
            if R(x1,x2).contain(x3):
                if R(x1,x2).contain(x4):
                    result = Segment(Point(x3,y3),Point(x4,y4))
                else:
                    result = Segment(Point(x3,y3),Point(x2,y2))
            else:
                if R(x1,x2).contain(x4):
                    result = Segment(Point(x1,y1),Point(x4,y4))
                else: 
                    if R(x3,x4).contain(x1) and R(x3,x4).contain(x2):
                        result =  Segment(Point(x1,y1),Point(x2,y2))
                    else:
                        result = None

        if not result == None:
            if result.isPoint():
                result = result.p1()
        return result

    elif (denom == 0.0):
	return None
    else:
	ua = uanum / denom
	ub = ubnum / denom
	if (ua >= 0 and ua <= 1 and ub >= 0 and ub <= 1):
	    x = x1 + ua * (x2 - x1)
	    y = y1 + ua * (y2 - y1)
	    return Point(x, y)
	return None

def preduce(points,ratio):
    middle = pmiddle(points)
    result = []
    for p in points:
        v = vector(middle,p)
        newp = middle.add(v.scale(ratio))
        result.append(newp)
    return result

def vsanglepos(v1,v2):
    result = vsangle(v1,v2)
    if result < -math.pi:
        result += 2.0 * math.pi
    if result > math.pi:    
        result -= 2.0 * math.pi
    return result
