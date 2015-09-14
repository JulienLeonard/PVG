from utils        import *
from geoutils     import *
from polygon      import *
from circle       import *
from geoquad      import *

import unittest

class GeoQuadTest(unittest.TestCase):
    
    def test_init(self):
        geoquad = GeoQuad.square(Point(1.0,1.0),2.0)
        self.assertEqual(geoquad.xpoint(Point(0.5,0.5)).coords(),(1.0,1.0))

    def test_split(self):
        geoquad = GeoQuad.square(Point(1.0,1.0),2.0)
        self.assertEqual(len(geoquad.xsplit(0.5)),2)

