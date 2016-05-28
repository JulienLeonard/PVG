from utils import *

class PointAbscissaRange:
        
    def __init__(self,t1,t2,seg):
        self.mra   = R(t1,t2)
        self.mseg  = seg

    def arange(self):
        return self.mra

    def a1(self):
        return self.arange().v1()

    def a2(self):
        return self.arange().v2()

    def segment(self):
        return self.mseg

    def sample(self,t):
        rt = self.mra.abscissa(t)
        return self.mseg.point(rt)

    def contain(self,t):
        return (self.mra.v1() <= t and t <= self.mra.v2())

    def point(self,t):
        return self.sample(t)

    def vector(self):
        return self.mseg.vector()

    def coords(self):
        return [self.a1(),self.a2(),self.segment().coords()]

    def point1(self):
        return self.mseg.p1()

    def point2(self):
        return self.mseg.p2()
