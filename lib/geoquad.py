from utils        import *
from geoutils     import *
from curvebuilder import *

#
# Geometric contour defined by 2 x 2 curves
#
class GeoQuad:

    def __init__(self,left,up,right,down):
        self.mleft  = left
        self.mup    = up
        self.mright = right
        self.mdown  = down
        
    # def point(self,p):
    #     x,y = p.coords()

    # def horizontal(self,t):
    #     return Polygon([self.point(Point(x,t)) for x in usamples(100)])

    def polygon(self):
        return self.mleft.concat(self.mup).concat(self.mright.reverse()).concat(self.mdown.reverse())

    @staticmethod
    def square(center,size,npointsperface):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.square(center,size))]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())

    @staticmethod
    def rectangle(x1,y1,x2,y2,npointsperface):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.rectangle(x1,y1,x2,y2))]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())

        
