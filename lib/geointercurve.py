from geoutils     import *
from polygon      import *
from curvebuilder import *

class GeoIntercurve:
    def __init__(self,long1,long2):
        self.mlong1  = long1
        self.mlong2  = long2
        self.minter  = CR(self.mlong1,self.mlong2)

    def _xcurve(self,x):
        return Polygon([self.mappoint(Point(x,t)) for t in usamples(100)])

    def _ycurve(self,y):
        return self.minter.sample(y)

    def sample(self,abscissa):
        return self._ycurve(abscissa)

    def curve(self,abscissa):
        return self._ycurve(abscissa)

    #
    # WARNING: points must be normalized
    #
    def mappoint(self,point):
        ycurve = self._ycurve(point.y())
        return ycurve.point(point.x())

    def mappolygon(self,polygon):
        return Polygon([self.mappoint(p) for p in polygon.points()])

    def contour(self):
        return self.mlong1.concat(self.mlong2.reverse()).close()

    
