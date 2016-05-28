from polygon import *

class Polygon3D(Polygon):

    def __init__(self,points):
        self.mpoints    = points
        # puts("createpolygon",[p.coords() for p in points])
        self.msegments  = [Segment3D(p1,p2) for (p1,p2) in pairs(self.mpoints)]
        self.mparanges  = None
        self.mlength    = None

