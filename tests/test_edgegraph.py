import sys
sys.path.insert(0, './../lib')

from utils     import *
from geoutils  import *
from edgegraph import *
from circle    import *

import unittest

class EdgeGraphTest(unittest.TestCase):
    
    def test_loadwithpointseuqnece(self):
        eg = EdgeGraph().loadwithpointsequence([Point(0.0,0.0),Point(1.0,0.0),Point(2.0,0.0)])
        self.assertEqual(len(eg.edges()),2)
        self.assertEqual(eg.edge(0).coords(),(0.0,0.0,1.0,0.0))
        self.assertEqual(eg.edge(1).coords(),(1.0,0.0,2.0,0.0))

    def test_loadwithpointpairs(self):
        eg = EdgeGraph().loadwithpointpairs([(Point(0.0,0.0),Point(1.0,0.0)),(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.edges()),2)
        self.assertEqual(eg.edge(0).coords(),(0.0,0.0,1.0,0.0))
        self.assertEqual(eg.edge(1).coords(),(1.0,0.0,2.0,0.0))
        self.assertEqual(len(eg.edge(0).prevs()),0)
        self.assertEqual(len(eg.edge(0).nexts()),1)
        self.assertEqual(len(eg.edge(1).prevs()),1)
        self.assertEqual(len(eg.edge(1).nexts()),0)
        self.assertEqual(eg.edge(0).nexts()[0].coords(),(1.0,0.0,2.0,0.0))
        self.assertEqual(eg.edge(1).prevs()[0].coords(),(0.0,0.0,1.0,0.0))

    def test_arcs(self):
        eg = EdgeGraph().loadwithpointpairs([(Point(0.0,0.0),Point(1.0,0.0)),(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.arcs()),1)
        self.assertEqual(len(eg.arcs()[0].edges()),2)

    def test_arcs2(self):
        p1s = [p for p in pairs(Circle(Point(0.0,0.0),1.0).polygon(4).points())]
        p2s = [(Point(2.0,0.0),Point(3.0,0.0))]
        p3s = [p for p in pairs(Circle(Point(4.0,0.0),1.0).polygon(4).points())]
        eg = EdgeGraph().loadwithpointpairs(p1s + p2s + p3s)
        self.assertEqual(len(eg.arcs()),3)


    # def test_cutedges(self):    
    #     eg = EdgeGraph().loadwithpointsequence([Point(0.0,0.0),Point(1.0,0.0)])
    #     eg = eg.loadwithpointsequence([Point(0.5,1.0),Point(0.5,-1.0)])
    #     self.assertEqual(len(eg.edges()),2)
    #     eg.cutedges()
    #     self.assertEqual(len(eg.edges()),4)

    # def test_cutedges2(self):    
    #     eg = EdgeGraph().loadwithpointsequence([Point(0.0,0.0),Point(1.0,0.0)])
    #     eg = eg.loadwithpointsequence([Point(0.45,1.0),Point(0.55,-1.0)])
    #     eg = eg.loadwithpointsequence([Point(0.25,1.0),Point(0.75,-1.0)])
    #     self.assertEqual(len(eg.edges()),3)
    #     eg.cutedges()
    #     self.assertEqual(len(eg.edges()),7)

    # def test_cutedges3(self):    
    #     eg = EdgeGraph().loadwithpointsequence([Point(0.0,0.0),Point(1.0,0.0)])
    #     eg = eg.loadwithpointsequence([Point(-0.1,1.0),Point(1.0,-2.0)])
    #     eg = eg.loadwithpointsequence([Point(-0.2,-2.0),Point(1.0,1.0)])
    #     self.assertEqual(len(eg.edges()),3)
    #     eg.cutedges()
    #     self.assertEqual(len(eg.edges()),9)
        
