from utils    import *
from range    import *
from geoutils import *

import unittest

class PointTest(unittest.TestCase):
    
    def test_defaultpoint(self):
        self.assertEqual(Point().x(),0.0)
        self.assertEqual(Point().y(),0.0)

    def test_x(self):
        self.assertEqual(Point().x(), 0.0)
        self.assertEqual(Point().x(1.0).x(), 1.0)

    def test_y(self):
        self.assertEqual(Point().y(), 0.0)
        self.assertEqual(Point().y(2.0).y(), 2.0)


    def test_coords(self):
        self.assertEqual(Point().coords(), (0.0,0.0))
        self.assertEqual(Point().coords((3.0,4.0)).coords(), (3.0,4.0))

    def test_add(self):
        self.assertEqual(Point().add(Vector()).coords(), (1.0,0.0))
        self.assertEqual(Point(1.0,2.0).add(Vector(3.0,4.0)).coords(), (4.0,6.0))

    def test_sub(self):
        self.assertEqual(Point(1.0,1.0).sub(Point(0.0,1.0)).coords(), (1.0,0.0))

    def test_rotate(self):
        self.assertEqual(True, (0.0001 > dist2(Point(1.0,0.0).rotate(Point(0.0,0.0),R.angle().sample(0.25)), Point(0.0,1.0))))
        self.assertEqual(True, (0.0001 > dist2(Point(2.0,2.0).rotate(Point(0.0,2.0),R.angle().sample(0.25)), Point(0.0,4.0))))
        
    def test_sym(self):
        self.assertEqual(Point(1.0,0.0).sym(Point(0.0,0.0)).coords(), (-1.0,0.0))
        self.assertEqual(Point(2.0,-3.0).sym(Point(0.0,0.0)).coords(), (-2.0,3.0))
    
        

class VectorTest(unittest.TestCase):
    
    def test_defaultvector(self):
        self.assertEqual(Vector().x(),1.0)
        self.assertEqual(Vector().y(),0.0)

    def test_x(self):
        self.assertEqual(Vector().x(), 1.0)
        self.assertEqual(Vector().x(2.0).x(), 2.0)

    def test_y(self):
        self.assertEqual(Vector().y(), 0.0)
        self.assertEqual(Vector().y(3.0).y(), 3.0)


    def test_coords(self):
        self.assertEqual(Vector().coords(), (1.0,0.0))
        self.assertEqual(Vector().coords((3.0,4.0)).coords(), (3.0,4.0))

    def test_points(self):
        self.assertEqual(Vector().points(Point(0.0,1.0),Point(2.0,3.0)).coords(), (2.0,2.0))

    def test_length2(self):
        self.assertEqual(Vector(2.0,0.0).length2(), 4.0)
        self.assertEqual(Vector(3.0,4.0).length2(), 25.0)

    def test_length(self):
        self.assertEqual(Vector(2.0,0.0).length(), 2.0)
        self.assertEqual(Vector(3.0,4.0).length(), 5.0)

    def test_normalize(self):
        oldv = Vector(2.0,0.0)
        newv = oldv.normalize()
        self.assertEqual(oldv.coords(), (2.0,0.0))
        self.assertEqual(newv.coords(), (1.0,0.0))

    def test_rotate(self):
        self.assertEqual(True, (0.0001 > dist2(Vector(0.0,0.2).rotate(R.angle().sample(0.25)), Vector(-0.2,0.0))))

    def test_scale(self):
        self.assertEqual(Vector(0.0,0.2).scale(10.0).coords(), (0.0,2.0))

    def test_cross(self):
        self.assertEqual(Vector(0.0,1.0).cross(Vector(0.0,1.0)), 0.0)
        self.assertEqual(Vector(0.0,1.0).cross(Vector(1.0,0.0)), -1.0)

class UtilsTest(unittest.TestCase):
    
    def test_anglerange(self):
        self.assertEqual(R.angle().v1(),0.0)
        self.assertEqual(R.angle().v2(),2* math.pi)
        
    def test_vector(self):
        self.assertEqual(vector(Point(0.0,1.0),Point(2.0,3.0)).coords(), (2.0,2.0))

    def test_dist2(self):
        self.assertEqual(dist2(Point(0.0,0.0),Point(3.0,4.0)), 25.0)
        self.assertEqual(dist2(Point(0.0,0.0),Point(1.0,0.0)), 1.0)

    def test_dist(self):
        self.assertEqual(dist(Point(0.0,0.0),Point(3.0,4.0)), 5.0)
        self.assertEqual(dist(Point(0.0,0.0),Point(1.0,0.0)), 1.0)

    def test_pmiddle(self):
        self.assertEqual(pmiddle([Point(0.0,0.0),Point(3.0,0.0),Point(0.0,3.0)]).coords(), (1.0,1.0))
        
    def test_rawintersection(self):
        # point intersections empty
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(0.0,0.0), Point(2.0,1.0), Point(2.0,1.0)), None)
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(2.0,0.0), Point(2.0,1.0), Point(2.0,1.0)), None)
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(2.0,0.0), Point(3.0,0.0), Point(3.0,0.0)), None)
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(0.0,0.0), Point(1.0,0.0), Point(3.0,0.0)), None)

        # parallel
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(2.0,1.0), Point(1.0,1.0)), None)

        # included points
        self.assertEqual(raw_intersection(Point(1.0,1.0), Point(1.0,1.0), Point(1.0,1.0), Point(1.0,1.0)).coords(), Point(1.0,1.0).coords())
        self.assertEqual(raw_intersection(Point(1.0,1.0), Point(1.0,1.0), Point(1.0,1.0), Point(2.0,1.0)).coords(), Point(1.0,1.0).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.5,0.0), Point(0.5,0.0)).coords(), Point(0.5,0.0).coords())
        self.assertEqual(raw_intersection(Point(0.8,0.0), Point(0.8,0.0), Point(0.0,0.0), Point(1.0,0.0)).coords(), Point(0.8,0.0).coords())

        # included segments
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.0,0.0),  Point(1.0,0.0)).coords(),  Segment(Point(0.0,0.0),Point(1.0,0.0)).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.5,0.0),  Point(0.75,0.0)).coords(), Segment(Point(0.5,0.0),Point(0.75,0.0)).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.75,0.0), Point(0.5,0.0)).coords(),  Segment(Point(0.5,0.0),Point(0.75,0.0)).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(2.0,0.0), Point(1.0,0.0),  Point(3.0,0.0)).coords(),  Segment(Point(1.0,0.0),Point(2.0,0.0)).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(2.0,0.0), Point(3.0,0.0),  Point(1.0,0.0)).coords(),  Segment(Point(1.0,0.0),Point(2.0,0.0)).coords())

        # point intersection
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.5,1.0), Point(0.5,-1.0)).coords(), Point(0.5,0.0).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(0.0,1.0), Point(0.0,-1.0)).coords(), Point(0.0,0.0).coords())
        self.assertEqual(raw_intersection(Point(0.0,0.0), Point(1.0,0.0), Point(1.0,0.0), Point(2.0,0.0)).coords(),  Point(1.0,0.0).coords())



class BBoxTest(unittest.TestCase):
    
    def test_unionsymx(self):
        self.assertEqual(BBox(-2.0,-2.0,-1.0,-1.0).unionsymx(0.0).coords(),(-2.0,-2.0,2.0,-1.0))
        self.assertEqual(BBox(-2.0,-2.0,-1.0,-1.0).unionsymx(-1.5).coords(),(-2.0,-2.0,-1.0,-1.0))





