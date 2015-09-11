from geoutils import *
from polygon  import *
from circle   import *
from bezier   import *

class Shape:

    @staticmethod
    def intersectSegmentCircle(segment,circle,strict=False):
        result = False
        for p in segment.points():
            if circle.containpoint(p,strict):
                result = True
                break
        if not result:    
            p1,p2 = segment.points()
            p3    = circle.center()
            u = ((p3.x()-p1.x()) * (p2.x()-p1.x()) + (p3.y()-p1.y())*(p2.y() - p1.y())) / segment.length2()
            op = iff(strict, inf, infeq) 
            if op(-1.0, u) and op(u, 1.0):
                nearestpoint = p1.add(vector(p1,p2).scale(u))
                    # puts("nearestpoint",nearestpoint.coords())
                result = circle.containpoint(nearestpoint,strict)
            else:
                result = False
            # puts("intersect segment",segment.coords(),"circle",circle.coords(),"result",result)
        return result

    @staticmethod
    def intersect(shape1,shape2,strict=False):
        if isinstance(shape1,Circle) and isinstance(shape2,Circle):
            return Circle.intersect(shape1,shape2,strict)
        if isinstance(shape1,Segment) and isinstance(shape2,Segment):
            return Segment.intersect(shape1,shape2,strict)
        if isinstance(shape1,Segment) and isinstance(shape2,Circle):
            return Shape.intersectSegmentCircle(shape1,shape2,strict)
        if isinstance(shape1,Circle) and isinstance(shape2,Segment):
            return Shape.intersectSegmentCircle(shape2,shape1,strict)
        puts("intersect not defined",shape1,shape2)


    @staticmethod
    def contain(shape1,shape2,strict=False):
        puts("Shape.contain",shape1,shape2)
        if isinstance(shape1,Circle) and isinstance(shape2,Circle):
            return Circle.contain(shape1,shape2,strict)
        if isinstance(shape1,Segment) and isinstance(shape2,Segment):
            return Segment.contain(shape1,shape2,strict)
        if isinstance(shape1,Polygon) and isinstance(shape2,Polygon):
            return Polygon.contain(shape1,shape2,strict)
        
