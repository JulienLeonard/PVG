import sys
sys.path.insert(0, './../lib')

from utils    import *
from geoutils import *
from polygon  import *
from circle   import *

import unittest

class PolygonTest(unittest.TestCase):
    
    def test_contain(self):
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,0.0)),True)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,2.0)),False)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,1.0)),False)
        self.assertEqual(Circle().polygon(100).contain(Point(0.0,0.999)),True)
        self.assertEqual(Circle().polygon(100).contain(Point(0.9,0.9)),False)
        
