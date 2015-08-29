from utils    import *
from geoutils import *
from polygon  import *

#
# define a circle object
#
class Circle:
    def __init__(self,center=Point(0.0,0.0),radius=1.0):
        self.mcenter = center
        self.mradius = radius

    def coords(self,v=None):
        if not v == None:
            self.mcenter = Point(v[0],v[1])
            self.mradius = v[2]
            return self
        else:
            return (self.x(),self.y(),self.radius())

    def center(self,v=None):
        if not v == None:
            self.mcenter = v
            return self
        else:
            return self.mcenter

    def radius(self,v=None):
        if not v == None:
            self.mradius = v
            return self
        else:
            return self.mradius

    def r(self,v=None):
        return self.radius(v)

    def scale(self,ratio):
        return Circle(self.center(),self.radius() * ratio)

    def translate(self,tv):
        return Circle(self.center().add(tv),self.radius())

    def sample(self,abscissa):
        angle = anglerange().sample(abscissa)
        return self.center().add(VX0.rotate(angle).scale(self.r()))

    def samples(self,abscissas):
        return [self.sample(abscissa) for abscissa in abscissas]

    def viewbox(self):
        x,y,r = self.coords()
        return [x-r,y-r,x+r,y+r]

    def x(self):
        return self.center().x()

    def y(self):
        return self.center().y()

    def point(self,abscissa):
        return self.sample(abscissa)

    def polygon(self,npoints=30):
        return Polygon([self.point(i) for i in usamples(npoints+1)][:-1])
        

C0 = Circle()

#
#
#
def cscale(circle,ratio):
    return circle.scale(ratio)

#
# check if 2 circles intersect, given an error 
#
def circleintersect(c1,c2,errorsize = 0.0000001):
    cc1 = c1.center()
    cc2 = c2.center()
    r1  = c1.radius()
    r2  = c2.radius()

    v2 = dist2(cc1,cc2)
    r2 = (r1+r2)*(r1+r2)
    # print "differror",-0.00001
    result = False
    if ( (v2-r2)/r2 < -errorsize):
        result = True
    # print "circleintersect",c1,c2,"result",result,"v2",v2,"r2",r2,"criteria",(v2-r2)/r2
    return result

def circleviewbox(circle):
    return circle.viewbox()

def circlecoords(circle):
    return circle.coords()

def circlepoint(circle,abs):
    return circle.point(abs)

def circlepoints(circle,npoints,offset):
    abss = samples((offset,1.0+offset),npoints)
    return [circlepoint(circle,abs) for abs in abss]

def circlepolygon(circle,npoints):
    return circle.polygon(npoints)
