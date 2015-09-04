from utils    import *
from geoutils import *
from polygon  import *
from circle   import *

import unittest

class PolygonTest(unittest.TestCase):
    
    def test_points(self):
        self.assertEqual(Circle().polygon(2).coords(),[1.0,0.0,-1.0,1.2246467991473532e-16])
        self.assertEqual(Polygon.square(Point.P0(),1.0).coords(),[-0.5,-0.5,-0.5,0.5,0.5,0.5,0.5,-0.5,-0.5,-0.5])
        self.assertEqual(len(Polygon.square(Point.P0(),1.0).points(10)),10)

    def test_segments(self):
        self.assertEqual([seg.coords() for seg in Polygon.square(Point.P0(),1.0).segments()],[(-0.5,-0.5,-0.5,0.5),(-0.5,0.5,0.5,0.5),(0.5,0.5,0.5,-0.5),(0.5,-0.5,-0.5,-0.5)])
        
    def test_bbox(self):
        self.assertEqual(Circle().polygon(100).bbox().coords(),(-1.0,-1.0,1.0,1.0))

    def test_contain(self):
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,0.0)),True)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,2.0)),False)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,1.0)),False)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,0.999)),True)
        self.assertEqual(Circle().polygon(100).contain(Point(0.9,0.9)),False)

    def test_samples(self):
        self.assertEqual([coord for p in Polygon.square(Point.P0(),1.0).samples(9) for coord in p.coords()],[-0.5,-0.5,-0.5,0.0,-0.5,0.5,0.0,0.5,0.5,0.5,0.5,0.0,0.5,-0.5,0.0,-0.5,-0.5,-0.5])

    def test_lengthsamples(self):
        self.assertEqual([coord for p in Polygon.square(Point.P0(),1.0).lengthsamples(0.5) for coord in p.coords()],[-0.5,-0.5,-0.5,0.0,-0.5,0.5,0.0,0.5,0.5,0.5,0.5,0.0,0.5,-0.5,0.0,-0.5,-0.5,-0.5])
        
    def test_lengths(self):
        self.assertEqual([parange.coords() for parange in Polygon.square(Point.P0(),1.0).paranges()],[[0.0, 0.25, (-0.5, -0.5, -0.5, 0.5)],[0.25, 0.5, (-0.5, 0.5, 0.5, 0.5)],[0.5, 0.75, (0.5, 0.5, 0.5, -0.5)],[0.75, 1.0, (0.5, -0.5, -0.5, -0.5)]])

    def test_length(self):
        self.assertEqual(Polygon.square(Point.P0(),1.0).length(),4.0)
