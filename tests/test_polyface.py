from utils    import *
from geoutils import *
from polygon  import *
from edgegraph import *
from polyface import *

import unittest

class PolyfaceTest(unittest.TestCase):
    
    def test_init(self):
        eg = EdgeGraph().loadwithsegments(Circle().polygon(10).close().segments())
        self.assertEqual(len(eg.polyfaces()),1)
        polyface = eg.polyfaces()[0]
        self.assertEqual(len(polyface.arccycle().points()),11)

    def test_longitudes(self):
        eg = EdgeGraph().loadwithsegments(Circle().polygon(9).close().segments())
        polyface = eg.polyfaces()[0]
        longitudes = polyface.longitudes()
        self.assertEqual(len(longitudes[0]),1)
        

