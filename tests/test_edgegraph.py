import sys
sys.path.insert(0, './../lib')

from utils     import *
from geoutils  import *
from edgegraph import *
from circle    import *

import unittest

class EdgeGraphTest(unittest.TestCase):
    
    def test_loadwithpointsequence(self):
        eg = EdgeGraph().loadwithpointsequence([Point(0.0,0.0),Point(1.0,0.0),Point(2.0,0.0)])
        self.assertEqual(len(eg.edges()),4)
        self.assertEqual(len(eg.nodes()),3)
        self.assertEqual(eg.edges()[0].coords(),(0.0,0.0,1.0,0.0))
        self.assertEqual(eg.edges()[1].coords(),(1.0,0.0,0.0,0.0))
        self.assertEqual(eg.edges()[2].coords(),(1.0,0.0,2.0,0.0))
        self.assertEqual(eg.edges()[3].coords(),(2.0,0.0,1.0,0.0))

    def test_loadwithpointpairs(self):
        eg = EdgeGraph().loadwithpointpairs([(Point(0.0,0.0),Point(1.0,0.0)),(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.edges()),4)
        self.assertEqual(len(eg.nodes()),3)
        self.assertEqual(eg.edges()[0].coords(),(0.0,0.0,1.0,0.0))
        self.assertEqual(eg.edges()[1].coords(),(1.0,0.0,0.0,0.0))
        self.assertEqual(eg.edges()[2].coords(),(1.0,0.0,2.0,0.0))
        self.assertEqual(eg.edges()[3].coords(),(2.0,0.0,1.0,0.0))

    def test_arcs(self):
        eg = EdgeGraph().loadwithpointpairs([(Point(0.0,0.0),Point(1.0,0.0)),(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.nodes()),3)
        self.assertEqual(len(eg.edges()),4)
        self.assertEqual(len(eg.arcs()),2)
        self.assertEqual(len(eg.arcs()[0].edges()),2)

    def test_arcs2(self):
        p1s = [p for p in pairs(Circle(Point(0.0,0.0),1.0).polygon(4).points())]
        p2s = [(Point(1.0,0.0),Point(2.0,0.0))]
        p3s = [p for p in pairs(Circle(Point(3.0,0.0),1.0).polygon(4).points())]
        eg = EdgeGraph().loadwithpointpairs(p1s + p2s + p3s)
        self.assertEqual(len(eg.edges()),14)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)

    def test_arcs3(self):
        p1s = [p for p in pairs(Circle(Point(0.0,0.0),1.0).polygon(4).close().points())]
        p2s = [(Point(1.0,0.0),Point(2.0,0.0))]
        p3s = [p for p in pairs(Circle(Point(3.0,0.0),1.0).polygon(4).close().points())]
        eg = EdgeGraph().loadwithpointpairs(p1s + p2s + p3s)
        # puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),18)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)
