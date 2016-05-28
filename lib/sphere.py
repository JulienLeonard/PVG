from utils    import *
from geoutils3D import *

#
# define a sphere object
#
class Sphere:
    def __init__(self,center=Point3D(0.0,0.0,0.0),radius=1.0):
        self.mcenter = center
        self.mradius = radius
        self.mcoords = (self.mcenter.x(),self.mcenter.y(),self.mcenter.z(),radius)
        x,y,z,r = self.mcoords
        self.mbbox   = BBox3D(x-r,y-r,z-r,x+r,y+r,z+r)

    def coords(self,v=None):
        if not v == None:
            self.mcenter = Point3D(v[0],v[1],v[2])
            self.mradius = v[3]
            return self
        else:
            # return (self.x(),self.y(),self.radius())
            return self.mcoords

    def center(self,v=None):
        if not v == None:
            self.mcenter = v
            self.mcoords[0] = mcenter.x()
            self.mcoords[1] = mcenter.y()
            self.mcoords[2] = mcenter.z()
            x,y,z,r = self.mcoords
            self.mbbox      = BBox3D(x-r,y-r,z-r,x+r,y+r,z+r)
            return self
        else:
            return self.mcenter

    def radius(self,v=None):
        if not v == None:
            self.mradius = v
            self.mcoords[3] = v
            x,y,z,r = self.mcoords
            self.mbbox      = BBox(x-r,y-r,z-r,x+r,y+r,z+r)
            return self
        else:
            return self.mradius

    def radius2(self):
        return self.mradius * self.mradius

    def r(self,v=None):
        return self.radius(v)

    def scale(self,ratio):
        return Sphere(self.center(),self.radius() * ratio)

    def translate(self,tv):
        return Sphere(self.center().add(tv),self.radius())

    def symx(self,symx):
        return Sphere(self.center().symx(symx),self.radius())

    #def sample(self,abscissa):
    #    angle = R.angle().sample(abscissa)
    #    return self.center().add(Vector.VX0().rotate(angle).scale(self.r()))

    #def samples(self,npoints=None,abscissas=None):
    #    if not npoints == None:
    #        return [self.sample(abscissa) for abscissa in usamples(npoints)]
    #    if not abscissas == None:
    #        return [self.sample(abscissa) for abscissa in abscissas]
    #    return None

    #def points(self,npoints=None,abscissas=None):
    #    return self.samples(npoints,abscissas)

    def viewbox(self):
        return self.mbbox

    def bbox(self):
        return self.mbbox

    def x(self):
        return self.mcoords[0]

    def y(self):
        return self.mcoords[1]

    def z(self):
        return self.mcoords[2]
    
    def point(self,abscissa):
        return self.sample(abscissa)

    def containpoint(self,p,strict=False):
        op = iff(strict, inf, infeq) 
        return op(vector3D(self.center(),p).length(),self.radius())
        
    @staticmethod
    def intersect(c1,c2,strict=False):
        return sphereintersect(c1,c2)

    #def polygon(self,npoints=30):
    #    return Polygon(self.samples(npoints=npoints+1)[:-1])

    #def circlestring(self,ncircles = 10):
    #    # ncircles = int(self.polygon(100).length()/circlesize)
    #    points   = self.polygon(100).close().samples(ncircles)
    #    points = points + [points[0]]
    #    result = [Circle.fromDiameter(p1,p2) for (p1,p2) in pairs(points)]
    #    return result

    @staticmethod
    def fromcoords(coords):
        if len(coords) < 4:
            return None
        return Sphere(Point3D(coords[0],coords[1],coords[2]),coords[3])


    @staticmethod
    def fromSegment(segment,radius,abscissa=0.5):
        center = segment.sample(abscissa).add(segment.normal().scale(size))
        return Sphere(center,radius)

    @staticmethod
    def fromDiameter(p1,p2):
        ccenter = pmiddle3D([p1,p2])
        r = dist3D(p1,p2)/2.0
        return Sphere(ccenter,r)


Sphere.S0 = Sphere()

Sphere.Unitary = Sphere(Point3D(0.5,0.5,0.5),0.5)

#
#
#
def sscale(sphere,ratio):
    return sphere.scale(ratio)

#
# check if 2 circles intersect, given an error 
#
def sphereintersect(s1,s2,errorsize = 0.0000001):
    #cc1 = c1.center()
    #cc2 = c2.center()
    x1,y1,z1,r1 = s1.mcoords
    x2,y2,z2,r2 = s2.mcoords
    
    #r1  = c1.radius()
    #r2  = c2.radius()

    #v2 = dist2(cc1,cc2)
    x12 = (x1 - x2)
    y12 = (y1 - y2)
    z12 = (z1 - z2)
    v2 = x12*x12 + y12*y12 + z12*z12
    r12 = r1+r2
    r22 = r12*r12
    # print "differror",-0.00001
    result = False
    if ( (v2-r22)/r22 < -errorsize):
        result = True
    # print "circleintersect",c1,c2,"result",result,"v2",v2,"r2",r2,"criteria",(v2-r2)/r2
    return result

def sphereviewbox(sphere):
    return sphere.viewbox()

def spherecoords(sphere):
    return sphere.coords()

#def circlepoint(circle,abs):
#    return circle.point(abs)

#def circlepoints(circle,npoints,offset):
#    abss = R(offset,1.0+offset).samples(npoints)
#    return [circlepoint(circle,abs) for abs in abss]

#def circlepolygon(circle,npoints):
#    return circle.polygon(npoints)
