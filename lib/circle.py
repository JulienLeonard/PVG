from geoutils import *

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
            self.mr = v
            return self
        else:
            return self.mr

    def scale(self,ratio):
        return Circle(self.center(),self.radius() * ratio)

    def translate(self,tv):
        return Circle(self.center().addv(tv),self.radius())

    def sample(self,abscissa):
        return self.center().addv(v0.rotate(rangeangle().sample(abscissa)).scale(self.radius()))

    def samples(self,abscissas):
        return [self.sample(abscissa) for abscissa in abscissas]
