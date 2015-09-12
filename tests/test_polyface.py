from utils     import *
from geoutils  import *
from polygon   import *
from edgegraph import *
from polygraph import *

import unittest

class PolyfaceTest(unittest.TestCase):
    
    def test_init(self):
        eg = EdgeGraph().loadwithsegments(Circle().polygon(10).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0))])
        polygraph = Polygraph(eg)
        self.assertEqual(len(polygraph.polyfaces()),2)
        polyface = polygraph.polyfaces()[0]
        self.assertEqual(len(polyface.faces()),2)

    def test_longitudes(self):
        eg = EdgeGraph().loadwithsegments(Circle().polygon(10).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0))])
        polygraph = Polygraph(eg)
        self.assertEqual(len(polygraph.polyfaces()),2)
        polyface1 = polygraph.polyfaces()[0]
        self.assertEqual(len(polyface1.faces()),2)
        polyface2 = polygraph.polyfaces()[1]
        self.assertEqual(len(polyface2.faces()),2)
        (longitudes,sides) = polyface1.longitudes()
        self.assertEqual(len(longitudes),2)
        self.assertEqual(len(sides),0)
        long1,long2 = iff(len(longitudes[0].points()) > len(longitudes[1].points()),(longitudes[0],longitudes[1]),(longitudes[1],longitudes[0]))
        self.assertEqual(len(long1.points()),6)
        self.assertEqual(len(long2.points()),2)
        

