from geoutils3D import *
from polygon3D  import *
from sphere   import *
# from bezier   import *

class Shape3D:

    @staticmethod
    def intersectSegmentSphere(segment,sphere,strict=False):
        result = False
        for p in segment.points():
            if sphere.containpoint(p,strict):
                result = True
                break
        if not result:    
            p1,p2 = segment.points()
            p3    = sphere.center()
            u = ((p3.x()-p1.x()) * (p2.x()-p1.x()) + (p3.y()-p1.y())*(p2.y() - p1.y()) + (p3.z()-p1.z())*(p2.z() - p1.z())) / segment.length2()
            op = iff(strict, inf, infeq) 
            if op(-1.0, u) and op(u, 1.0):
                nearestpoint = p1.add(vector3D(p1,p2).scale(u))
                    # puts("nearestpoint",nearestpoint.coords())
                result = sphere.containpoint(nearestpoint,strict)
            else:
                result = False
            # puts("intersect segment",segment.coords(),"circle",circle.coords(),"result",result)
        return result

    @staticmethod
    def intersect(shape1,shape2,strict=False):
        if isinstance(shape1,Sphere) and isinstance(shape2,Sphere):
            return Sphere.intersect(shape1,shape2,strict)
        if isinstance(shape1,Segment3D) and isinstance(shape2,Segment3D):
            return Segment3D.intersect(shape1,shape2,strict)
        if isinstance(shape1,Segment3D) and isinstance(shape2,Sphere):
            return Shape3D.intersectSegmentSphere(shape1,shape2,strict)
        if isinstance(shape1,Sphere) and isinstance(shape2,Segment3D):
            return Shape3D.intersectSegmentSphere(shape2,shape1,strict)
        puts("intersect not defined",shape1,shape2)


    @staticmethod
    def contain(shape1,shape2,strict=False):
        puts("Shape3D.contain",shape1,shape2)
        if isinstance(shape1,Sphere) and isinstance(shape2,Sphere):
            return Sphere.contain(shape1,shape2,strict)
        if isinstance(shape1,Segment3D) and isinstance(shape2,Segment3D):
            return Segment3D.contain(shape1,shape2,strict)
        if isinstance(shape1,Polygon3D) and isinstance(shape2,Polygon3D):
            return Polygon3D.contain(shape1,shape2,strict)
        
