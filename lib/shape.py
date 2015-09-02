from geoutils import *
from circle   import *

class Shape:

    @staticmethod
    def intersect(shape1,shape2):
        if isinstance(shape1,Circle) and isinstance(shape2,Circle):
            return Circle.intersect(shape1,shape2)
        if isinstance(shape1,Segment) and isinstance(shape2,Segment):
            return Segment.intersect(shape1,shape2)

