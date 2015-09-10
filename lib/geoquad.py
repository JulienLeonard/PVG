from utils        import *
from geoutils     import *
from curvebuilder import *

#
# 
#
class GeoQuad:

    def __init__(self,left,up,right,down):
        self.mleft  = left
        self.mup    = up
        self.mright = right
        self.mdown  = down
        
    def point(self,p):
        x,y = p.coords()

    def horizontal(self,t):
        return Polygon([self.point(Point(x,t)) for x in usamples(100)])
