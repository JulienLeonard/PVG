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
        self.assertEqual(len(Polygon.square(Point.P0(),1.0).points(abscissas=[0.1,0.2])),2)
        self.assertEqual(len(Polygon.square(Point.P0(),1.0).points(bylength=0.5)),9)

    def test_point1(self):
        self.assertEqual(Polygon.square(Point.P0(),1.0).point1().coords(),(-0.5,-0.5))
        self.assertEqual(Polygon.square(Point.P0(),1.0).ext1().coords(),(-0.5,-0.5))


    def test_point2(self):
        self.assertEqual(Polygon.square(Point.P0(),1.0).point2().coords(),(-0.5,-0.5))
        self.assertEqual(Polygon.square(Point.P0(),1.0).ext2().coords(),(-0.5,-0.5))

    def test_pointextremities(self):
        self.assertEqual([p.coords() for p in Polygon.square(Point.P0(),1.0).pointextremities()],[(-0.5,-0.5),(-0.5,-0.5)])

    def test_minmax(self):
        polygon = Circle().polygon(4)
        # puts("polygon coords",polygon.coords())
        self.assertEqual(polygon.minx(),-1.0)
        self.assertEqual(polygon.miny(),-1.0)
        self.assertEqual(polygon.maxx(),1.0)
        self.assertEqual(polygon.maxy(),0.0)

    def test_segments(self):
        self.assertEqual([seg.coords() for seg in Polygon.square(Point.P0(),1.0).segments()],[(-0.5,-0.5,-0.5,0.5),(-0.5,0.5,0.5,0.5),(0.5,0.5,0.5,-0.5),(0.5,-0.5,-0.5,-0.5)])
        self.assertEqual([seg.coords() for seg in Polygon.square(Point.P0(),1.0).segments(abscissas=[0.0,0.5,1.0])],[(-0.5,-0.5,0.5,0.5),(0.5,0.5,-0.5,-0.5)])
        self.assertEqual([seg.coords() for seg in Polygon.square(Point.P0(),1.0).segments(bylength=0.5)],[(-0.5,-0.5,-0.5,0.0),(-0.5,0.0,-0.5,0.5),(-0.5,0.5,0.0,0.5),(0.0,0.5,0.5,0.5),(0.5,0.5,0.5,0.0),(0.5,0.0,0.5,-0.5),(0.5,-0.5,0.0,-0.5),(0.0,-0.5,-0.5,-0.5)])
        
    def test_bbox(self):
        self.assertEqual(Circle().polygon(100).bbox().coords(),(-1.0,-1.0,1.0,1.0))

    def test_containpoint(self):
        self.assertEqual(Circle().polygon(100).containpoint(Point(0.0,0.0)),True)
        self.assertEqual(Circle().polygon(100).containpoint(Point(0.0,2.0)),False)
        self.assertEqual(Circle().polygon(100).containpoint(Point(0.0,1.0)),False)
        self.assertEqual(Circle().polygon(100).containpoint(Point(0.0,0.999)),True)
        self.assertEqual(Circle().polygon(100).containpoint(Point(0.9,0.9)),False)

    def test_samples(self):
        self.assertEqual([coord for p in Polygon.square(Point.P0(),1.0).samples(9) for coord in p.coords()],[-0.5,-0.5,-0.5,0.0,-0.5,0.5,0.0,0.5,0.5,0.5,0.5,0.0,0.5,-0.5,0.0,-0.5,-0.5,-0.5])

    def test_lengthsamples(self):
        self.assertEqual([coord for p in Polygon.square(Point.P0(),1.0).lengthsamples(0.5) for coord in p.coords()],[-0.5,-0.5,-0.5,0.0,-0.5,0.5,0.0,0.5,0.5,0.5,0.5,0.0,0.5,-0.5,0.0,-0.5,-0.5,-0.5])
        
    def test_lengths(self):
        self.assertEqual([parange.coords() for parange in Polygon.square(Point.P0(),1.0).paranges()],[[0.0, 0.25, (-0.5, -0.5, -0.5, 0.5)],[0.25, 0.5, (-0.5, 0.5, 0.5, 0.5)],[0.5, 0.75, (0.5, 0.5, 0.5, -0.5)],[0.75, 1.0, (0.5, -0.5, -0.5, -0.5)]])

    def test_length(self):
        self.assertEqual(Polygon.square(Point.P0(),1.0).length(),4.0)

    def curveabscissa(self):
        polygon = Polygon.square(Point.P0(),1.0)
        self.assertEqual(polygon.curveabscissa(Point(-0.5,-0.5)),0.0)
        self.assertEqual(polygon.curveabscissa(Point(-0.5,0.0)),0.175)
        self.assertEqual(polygon.curveabscissa(Point(-0.5,0.5)),0.25)
        self.assertEqual(polygon.curveabscissa(Point(0.0,-0.5)),0.825)
