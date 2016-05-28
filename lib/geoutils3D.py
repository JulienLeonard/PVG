from utils import *
from range import *

#
# Interface to define 2D geometry entity (Point or Vector)
#
class Coords3D:
    def __init__(self,x=0.0,y=0.0,z=0.0):
        self.mx = x
        self.my = y
        self.mz = z

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

    def z(self,v=None):
        if not v == None:
            self.mz = v
            return self
        else:
            return self.mz

        
    def coords(self,v=None):
        if not v == None:
            self.mx = v[0]
            self.my = v[1]
            self.mz = v[2]
            return self
        else:
            return (self.mx,self.my,self.mz)


#
# class Point3D
#
class Point3D(Coords3D):

    def add(self,v):
        return Point3D(self.x() + v.x(),self.y() + v.y(),self.z() + v.z())
    
    def sub(self,p):
        return Vector3D(self.x() - p.x(),self.y() - p.y(),self.z() - p.z())

    #def rotate(self,center,angle):
    #    return center.add( vector(center,self).rotate(angle) )

    def sym(self,center):
        return center.add(vector(self,center))

    def symx(self,symx):
        return Point3D(2.0*symx-self.x(),self.y(),self.z())

    @staticmethod
    def P0():
        return Point3D(0.0,0.0,0.0)


#
# class Vector3D
#
class Vector(Coords3D):

    #
    # constructor
    #
    def __init__(self,x=1.0,y=0.0,z=0.0):
        self.mx = x
        self.my = y
        self.mz = z
        self.ml  = None
        
    #
    # compute coords of vector from extremities
    #
    def points(self,p1,p2):
        self.mx = (p2.x() - p1.x())
        self.my = (p2.y() - p1.y())
        self.mz = (p2.z() - p1.z())
        self.ml  = None
        return self

    #
    # compute the power2 of the length of the vector
    #
    def length2(self):
        x = self.x()
        y = self.y()
        z = self.z()
        return (x *x + y *y + z *z)

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
            return Vector3D(0.0,0.0,0.0)
        else:
            return self.scale(1.0/l)

    #
    # rotate a vector
    #
    #def rotate(self,angle):
    #    cosa = math.cos(angle)
    #    sina = math.sin(angle)
    #    x = self.x()
    #    y = self.y()
    #    return Vector((x * cosa - y * sina),(x * sina + y * cosa ))

    #
    # scale a vector
    #
    def scale(self,ratio):
        return Vector3D(self.x()*ratio,self.y()*ratio,self.z()*ratio)


    def scalex(self,rx):
        return Vector3D(self.x()*rx,self.y(),self.z())


    def scaley(self,ry):
        return Vector3D(self.x(),self.y() * ry,self.z())

    def scalez(self,rz):
        return Vector3D(self.x(),self.y(),self.z() * rz)

    
    #
    # compute the ortho vector of a vector
    #
    def ortho(self):
        return Vector3D(-self.y(),self.x(),self.z())

    #
    # cross product
    #
    #def cross(self,ov):
    #    return (self.x() * ov.y() - self.y() * ov.x())

    def add(self,v):
        return Vector3D(self.x() + v.x(),self.y() + v.y(),self.z() + v.z())

    @staticmethod
    def V03D():
        return Vector3D(0.0,0.0,0.0)

    @staticmethod
    def VX03D():
        return Vector3D(1.0,0.0,0.0)
    
    @staticmethod
    def VY03D():
        return Vector3D(0.0,1.0,0.0)


#
# shortcut: build a vector from extremities
#
def vector3D(p1,p2):
    return Vector3D().points(p1,p2)

#
# compute the trigo vector from an angle
#
#def angle2vector(a):
#    return Vector(math.cos(a),math.sin(a))

#
# compute the power2 of the dist between 2 points
#
def dist23D(p1,p2):
    return vector3D(p1,p2).length2()

#
# compute the dist betweem 2 points
#
def dist3D(p1,p2):
    return vector3D(p1,p2).length()

        
#
# compute the average point of a list of points
#
def pmiddle3D(points):
    listx = [p.x() for p in points]
    listy = [p.y() for p in points]
    listz = [p.z() for p in points]
    return Point3D(sum(listx)/float(len(points)),sum(listy)/float(len(points)),sum(listz)/float(len(points)))

#
# Segment
#
class Segment3D:
    
    def __init__(self,p1,p2):
        self.mp1 = p1
        self.mp2 = p2
        self.mrx = R(self.mp1.x(),self.mp2.x())
        self.mry = R(self.mp1.y(),self.mp2.y())
        self.mrz = R(self.mp1.z(),self.mp2.z())
        

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
        return Point3D(self.mrx.sample(t),self.mry.sample(t),self.mrz.sample(t))

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
        return vector3D(self.p1(),self.p2())

    def normal(self):
        return self.vector3D().ortho().normalize()

    def length(self):
        return self.vector3D().length()

    def length2(self):
        return self.vector3D().length2()

    def split(self,ntimes):
        return [Segment3D(p1,p2) for (p1,p2) in pairs(self.samples(ntimes+1))]

    def splitmaxsize(self,maxsize):
        if self.length() <= maxsize:
            return [self]
        else:
            return self.split(int(math.ceil(self.length()/maxsize)))

    def subsegment(self,t1,t2):
        return Segment3D(self.sample(t1),self.sample(t2))

    def bbox(self):
        return points2bbox3D([self.p1(),self.p2()])

    @staticmethod
    #def intersect(seg1,seg2,strict=False):
    #    return (not raw_intersection(seg1.p1(),seg1.p2(),seg2.p1(),seg2.p2()) == None)

    @staticmethod
    #def intersection(seg1,seg2):
    #    return raw_intersection(seg1.p1(),seg1.p2(),seg2.p1(),seg2.p2())

    @staticmethod
    def sort(segments):
        sortlist = [(seg.p1().x(),seg.p2().x(),seg) for seg in segments]
        sortlist.sort()
        return [seg for (dum,dum,seg) in sortlist]

    @staticmethod
    def S03D():
        return Segment3D(Point3D(0.0,0.0,0.0),Point3D(1.0,0.0,0.0))



def pequal3D(p1,p2,error=0.00001):
    if (vector3D(p1,p2).length() < error):
        return True
    return False

def pdiff3D(p1,p2,error):
    return False if pequal3D(p1,p2,error) else True 


class BBox3D:

    def __init__(self,xmin,ymin,zmin,xmax,ymax,zmax):
        self.mxmin = xmin
        self.mxmax = xmax
        self.mymin = ymin
        self.mymax = ymax
        self.mzmin = zmin
        self.mzmax = zmax
        self.mcoords = (self.mxmin,self.mymin,self.mzmin,self.mxmax,self.mymax,self.mzmax)
        
    @staticmethod
    def fromCenterSize(ccenter,csize):
        return BBox3D(ccenter.x() - csize/2.0,ccenter.y() - csize/2.0,ccenter.z() - csize/2.0, ccenter.x() + csize/2.0, ccenter.y() + csize/2.0,ccenter.z() + csize/2.0)

    def coords(self):
        return self.mcoords

    def center(self):
        return Point3D((self.mxmin + self.mxmax)/2.0, (self.mymin + self.mymax)/2.0, (self.mzmin + self.mzmax)/2.0)

    def xsize(self):
        return (self.mxmax - self.mxmin)

    def ysize(self):
        return (self.mymax - self.mymin)

    def zsize(self):
        return (self.mzmax - self.mzmin)
    
    def width(self):
        return self.xsize()

    def height(self):
        return self.ysize()

    def depth(self):
        return self.zsize()
    
    def size(self):
        return max(self.xsize(),self.ysize(),self.zsize())
    
    def radius(self):
        rx = self.xsize()/2.0
        ry = self.ysize()/2.0
        rz = self.zsize()/2.0
        return math.sqrt(rx * rx + ry * ry + rz * rz)

    #def viewport(self,ratio = 1.0):
    #    return Viewport(self.center(), self.radius() * ratio)

    def resize(self,factor):
        # xmin,ymin,xmax,ymax = self.coords()
        newwidth  = self.xsize() * factor
        newheight = self.ysize() * factor
        newdepth  = self.zsize() * factor
        xcenter,ycenter,zcenter = self.center().coords()
        newxmin = xcenter - newwidth/2.0
        newxmax = xcenter + newwidth/2.0
        newymin = ycenter - newheight/2.0
        newymax = ycenter + newheight/2.0
        newzmin = zcenter - newdepth/2.0
        newzmax = zcenter + newdepth/2.0

        return BBox3D(newxmin,newymin,newzmin,newxmax,newymax,newzmax)

    def contain(self,point):
        xmin,ymin,zmin,xmax,ymax,zmax = self.coords()
        x,y,z                 = point.coords()
        if xmin <= x and x <= xmax and ymin <= y and y <= ymax and zmin <= z and z <= zmax:
            return True
        return False

    def containbbox(self,obbox):
        xmin1,ymin1,zmin1,xmax1,ymax1,zmax1 = self.coords()
        xmin2,ymin2,zmin2,xmax2,ymax2,zmax2 = obbox.coords()
        if xmin1 < xmin2 and xmax2 < xmax1 and ymin1 < ymin2 and ymax2 < ymax1 and zmin1 < zmin2 and zmax2 < zmax1:
            return True
        return False

    
    def corners(self):
        xmin,ymin,zmin,xmax,ymax,zmax = self.coords()
        return [Point3D(xmin,ymin,zmin),Point3D(xmax,ymin,zmin),Point3D(xmax,ymax,zmin),Point3D(xmin,ymax,zmin),  Point3D(xmin,ymin,zmax),Point3D(xmax,ymin,zmax),Point3D(xmax,ymax,zmax),Point3D(xmin,ymax,zmax)  ]

    #def cubepoints(self):
    #    size   = self.size()
    #    center = self.center()
    #    return [Point3D(center.x()-size/2.0,center.y()-size/2.0),
    #            Point3D(center.x()-size/2.0,center.y()+size/2.0),
    #            Point3D(center.x()+size/2.0,center.y()+size/2.0),
    #            Point3D(center.x()+size/2.0,center.y()-size/2.0)]

    def intersect(self,obbox):
        xmin0,ymin0,zmin0,xmax0,ymax0,zmax0 = self.mcoords
        xmin,ymin,zmin,xmax,ymax,zmax       = obbox.mcoords
        return (xmin <= xmax0 and xmax >= xmin0 and ymin <= ymax0 and ymax >= ymin0 and zmin <= zmax0 and zmax >= zmin0)
        
    def split8(self):
        (xmin,ymin,zmin,xmax,ymax,zmax) = self.coords()

        middlex = (xmin + xmax)/2.0
        middley = (ymin + ymax)/2.0
        middlez = (zmin + zmax)/2.0
        
        return [BBox3D(xmin,    ymin   , zmin, middlex, middley, middlez),
                BBox3D(xmin,    middley, zmin, middlex, ymax   , middlez),
                BBox3D(middlex, ymin   , zmin, xmax,    middley, middlez),
                BBox3D(middlex, middley, zmin, xmax,    ymax   , middlez),

                BBox3D(xmin,    ymin   , middlez, middlex, middley, zmax),
                BBox3D(xmin,    middley, middlez, middlex, ymax   , zmax),
                BBox3D(middlex, ymin   , middlez, xmax,    middley, zmax),
                BBox3D(middlex, middley, middlez, xmax,    ymax   , zmax)]

    def symx(self,symx):
        newxmin = 2.0 * symx - self.mxmin
        newxmax = 2.0 * symx - self.mxmax
        xmin  = min(newxmin,newxmax)
        xmax  = max(newxmin,newxmax)
        return BBox3D(xmin,self.mymin,self.mzmin,xmax,self.mymax,self.mzmax)

    def unionsymx(self,symx):
        return bbunion3D(self,self.symx(symx))

    def xmin(self):
        return self.coords()[0]

    def ymin(self):
        return self.coords()[1]

    def zmin(self):
        return self.coords()[2]
    
    def xmax(self):
        return self.coords()[3]

    def ymax(self):
        return self.coords()[4]

    def zmax(self):
        return self.coords()[5]
    

def bbunion3D(bbox1,bbox2):
    # puts ("bbunion",bbox1,bbox2)
    xmin1,ymin1,zmin1,xmax1,ymax1,zmax1 = bbox1.coords()
    xmin2,ymin2,zmin2,xmax2,ymax2,zmax2 = bbox2.coords()
    xmin = min(xmin1, xmin2)
    ymin = min(ymin1, ymin2)
    zmin = min(zmin1, zmin2)
    xmax = max(xmax1, xmax2)
    ymax = max(ymax1, ymax2)
    zmax = max(zmax1, zmax2)
    return BBox3D(xmin,ymin,zmin,xmax,ymax,zmax)

def bbunions3D(bboxlist):
    result = bboxlist[0]
    for bbox in bboxlist[1:]:
        result = bbunion3D(result,bbox)
    return result

def point2bbox3D(p):
    return BBox3D(p,p)

def points2bbox3D(points):
    if len(points) < 1:
        return None
    xmin = points[0].x()
    ymin = points[0].y()
    zmin = points[0].z()
    xmax = xmin
    ymax = ymin
    zmax = zmin
    for p in points[1:]:
        xmin = min(p.x(),xmin)
        ymin = min(p.y(),ymin)
        zmin = min(p.z(),zmin)
        xmax = max(p.x(),xmax)
        ymax = max(p.y(),ymax)
        zmax = max(p.z(),zmax)
    return BBox3D(xmin,ymin,zmin,xmax,ymax,zmax)

def polygons2bbox3D(polygons):
    if len(polygons) < 1:
        return None
    return bbunions3D([polygon.viewbox() for polygon in polygons])

def segviewbox3D(seg):
    return BBox3D().frompoints([seg[0],seg[1]])

def vscale3D(v,ratio):
    return (v[0] * ratio, v[1] * ratio, v[2] * ratio)

#def vsangle3D(v1,v2):
#    return (vangle(v1) - vangle(v2))

#def vangle(v):
#    l = v.length()
#    result = 0.0
#    if (l > 0.0):
#        norm = v.normalize()
#        cosx,siny = norm.coords()
#        result = math.acos( cosx )
#        if (siny < 0.0):
#            result = -result
#    return result




def viewboxinside3D(vb1,vb2):
    (xmin1,ymin1,zmin1,xmax1,ymax1,zmax1) = vb1.coords()
    (xmin2,ymin2,zmin2,xmax2,ymax2,zmax2) = vb2.coords()

    if xmin1 >= xmin2 and ymin1 >= ymin2 and zmin1 >= zmin2 and xmax1 <= xmax2 and ymax1 <= ymax2 and zmax1 <= zmax2:
        return True
    return False


def preduce3D(points,ratio):
    middle = pmiddle3D(points)
    result = []
    for p in points:
        v = vector3D(middle,p)
        newp = middle.add(v.scale(ratio))
        result.append(newp)
    return result

# def vsanglepos(v1,v2):
#     result = vsangle(v1,v2)
#     if result < -math.pi:
#         result += 2.0 * math.pi
#     if result > math.pi:    
#         result -= 2.0 * math.pi
#     return result
