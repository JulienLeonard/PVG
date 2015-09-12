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
        self.assertEqual(len(eg.edges()),16)
        self.assertEqual(len(eg.polyfaces()),4)
        self.assertEqual(len(eg.polygraph().polyfaces()),4)

    def test_adj(self):
        segments  = Circle().polygon(4).close().segments() + [Segment(Point(-1.0,0.0),Point(1.0,0.0)),Segment(Point(0.0,-1.0),Point(0.0,1.0))]
        intersegs = IntersectionBuilder().intersectionsegs( segments )
        eg = EdgeGraph().loadwithsegments(intersegs)
        polygraph = eg.polygraph()
        for face in polygraph.polyfaces():
            self.assertEqual(len(polygraph.adjacents(face)), 2)

