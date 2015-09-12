from utils               import *
from geoutils            import *
from polygon             import *
from edgegraph           import *
from polygraph           import *
from intersectionbuilder import *
import unittest

class PolygraphTest(unittest.TestCase):
    
    def test_init(self):
        segments  = Circle().polygon(4).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0)),Segment(Point(0.0,-1.0),Point(0.0,1.0))]
        intersegs = IntersectionBuilder().intersectionsegs( segments )
        eg = EdgeGraph().loadwithsegments(intersegs)
        polygraph = Polygraph(eg)
        self.assertEqual(len(polygraph.polyfaces()),4)

    def test_adj(self):
        segments  = Circle().polygon(4).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0)),Segment(Point(0.0,-1.0),Point(0.0,1.0))]
        intersegs = IntersectionBuilder().intersectionsegs( segments )
        eg = EdgeGraph().loadwithsegments(intersegs)
        polygraph = Polygraph(eg)
        for polyface in polygraph.polyfaces():
            self.assertEqual(len(polyface.adjacents()), 2)

