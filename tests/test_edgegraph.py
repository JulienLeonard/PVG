import sys
sys.path.insert(0, './../lib')

from utils     import *
from geoutils  import *
from edgegraph import *

import unittest

class EdgeGraphTest(unittest.TestCase):
    
    def test_loadwithpoints(self):
        eg = EdgeGraph().loadwithpoints([Point(0.0,0.0),Point(1.0,0.0),Point(2.0,0.0)])
        self.assertEqual(len(eg.edges()),2)
        self.assertEqual(eg.edge(0).coords(),(0.0,0.0,1.0,0.0))
        self.assertEqual(eg.edge(1).coords(),(1.0,0.0,2.0,0.0))
