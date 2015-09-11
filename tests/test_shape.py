from utils    import *
from geoutils import *
from circle   import *
from shape    import *

import unittest

class ShapeTest(unittest.TestCase):
    
    def test_intersectCircleSegment(self):
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(0.0,0.0),Point(2.0,0.0)),Circle(Point(0.0,0.0),1.0)),       True)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(0.0,0.0),Point(1.0,0.0)),Circle(Point(0.0,0.0),1.0)),       True)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(1.0,0.0),Point(2.0,0.0)),Circle(Point(0.0,0.0),1.0)),       True)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(1.0,0.0),Point(2.0,0.0)),Circle(Point(0.0,0.0),1.0),True),  False)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(1.1,0.0),Point(2.0,0.0)),Circle(Point(0.0,0.0),1.0)),       False)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(1.0,1.0),Point(1.0,-1.0)),Circle(Point(0.0,0.0),1.0)),      True)
        self.assertEqual(Shape.intersectSegmentCircle(Segment(Point(1.0,1.0),Point(1.0,-1.0)),Circle(Point(0.0,0.0),1.0),True), False)
        



    
