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
        self.interx = CR(self.mleft,self.mright)
        self.intery = CR(self.mdown,self.mup)

    def polygon(self):
        return self.mleft.concat(self.mup).concat(self.mright.reverse()).concat(self.mdown.reverse())

    def xcurve(self,x):
        return self.interx.sample(x).maponpoints(self.mdown.sample(x),self.mup.sample(x))

    def ycurve(self,y):
        return self.intery.sample(y).maponpoints(self.mleft.sample(y),self.mright.sample(y))

    def xpoint(self,p):
        return self.xcurve(p.x()).sample(p.y())

    def ypoint(self,p):
        return self.ycurve(p.y()).sample(p.x())


    @staticmethod
    def square(center = Point(0.5,0.5),size = 1.0,npointsperface = 10):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.square(center,size).points())]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())

    @staticmethod
    def rectangle(x1,y1,x2,y2,npointsperface):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.rectangle(x1,y1,x2,y2).points())]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())


    #
    # split the quad in 2 horizontally, returning 2 subquads
    #
    def ysplit(self,abscissa):
        (newleft1,newleft2)   = self.mleft.split(abscissa=abscissa)
        (newright1,newright2) = self.mright.split(abscissa=abscissa)
        newup1 = self.ycurve(abscissa)
        return (GeoQuad(newleft1,newup1,newright1,self.mdown),GeoQuad(newleft2,self.mup,newright2,newup1))

    def xsplit(self,abscissa):
        (newup1,newup2)     = self.mup.split(abscissa=abscissa)
        (newdown1,newdown2) = self.mdown.split(abscissa=abscissa)
        newleft1 = self.xcurve(abscissa)
        return (GeoQuad(self.mleft,newup1,newleft1,newdown1),GeoQuad(newleft1,newup2,self.mright,newdown2))

    def reduce(self,amount):
        margin = (1.0 - amount) * 0.5
        frame = [self.xcurve(margin), 
                 self.ycurve(1.0-margin),
                 self.xcurve(1.0-margin),
                 self.ycurve(margin)]
        frame = [curve.subline(margin,1.0-margin) for curve in frame]
        return GeoQuad(frame[0],frame[1],frame[2],frame[3])
