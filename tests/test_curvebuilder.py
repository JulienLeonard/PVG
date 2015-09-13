from utils        import *
from geoutils     import *
from polygon      import *
from circle       import *
from curvebuilder import *

import unittest

class CurveBuilderTest(unittest.TestCase):
    
    def test_maponpoints(self):
        poly = Polygon([Point(-1.0,0.0),Point(0.0,0.0),Point(1.0,0.0)])
        self.assertEqual(poly.maponpoints(Point(0.0,0.0),Point(1.0,0.0)).coords(),[0.0,0.0,0.5,0.0,1.0,0.0])
        self.assertEqual(poly.maponpoints(Point(1.0,1.0),Point(1.0,2.0)).coords(),[1.0,1.0,1.0,1.5,1.0,2.0])

