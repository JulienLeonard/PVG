from utils      import *
from geoutils   import *
from geomatcher import *
from polygon    import *

import unittest

class GeomatcherTest(unittest.TestCase):
    
    def test_geomatcher0(self):
        segments = [Segment.S0()]
        newsegs  = GeoMatcher().checksegments(segments)
        self.assertEqual(segments,newsegs)
        self.assertEqual(segments[0].p1(),newsegs[0].p1())
        self.assertEqual(segments[0].p2(),newsegs[0].p2())

    def test_geomatcher1(self):
        segments = Segment.S0().split(10)
        newsegs  = GeoMatcher().checksegments(segments)
        self.assertEqual(sorted(segments),sorted(newsegs))

    def test_geomatcher2(self):
        segments = Segment.S0().split(2) + [Segment.S0()]
        newsegs  = GeoMatcher().checksegments(segments)
        
        segmentspoints = lunique([p for seg in segments  for p in seg.points()])
        newsegspoints  = lunique([p for seg in newsegs   for p in seg.points()])

        # puts("newsegspoints",newsegspoints)

        self.assertEqual(len(newsegs),len(segments))
        self.assertEqual(len(newsegspoints), (len(segmentspoints) - 2))
