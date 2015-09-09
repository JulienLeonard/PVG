from utils        import *
from geoutils     import *
from polygon      import *
from edgegraph    import *
from polyface     import *
from voronoiutils import *

import unittest

class VoronoiTest(unittest.TestCase):
    
    def test_init(self):
        points   = Circle().polygon(4).points() + [Point.P0()]
        polygons = Voronoi(points).polygons()
        self.assertEqual(len(polygons),1)

        

