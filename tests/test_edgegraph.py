from utils     import *
from geoutils  import *
from edgegraph import *
from polygon   import *

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
        eg = EdgeGraph().loadwithsegments([Segment(Point(0.0,0.0),Point(1.0,0.0)),Segment(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.edges()),4)
        self.assertEqual(len(eg.nodes()),3)
        #self.assertEqual(eg.edges()[0].coords(),(0.0,0.0,1.0,0.0))
        #self.assertEqual(eg.edges()[1].coords(),(1.0,0.0,0.0,0.0))
        #self.assertEqual(eg.edges()[2].coords(),(1.0,0.0,2.0,0.0))
        #self.assertEqual(eg.edges()[3].coords(),(2.0,0.0,1.0,0.0))

    def test_arcs(self):
        eg = EdgeGraph().loadwithsegments([Segment(Point(0.0,0.0),Point(1.0,0.0)),Segment(Point(1.0,0.0),Point(2.0,0.0))])
        self.assertEqual(len(eg.nodes()),3)
        self.assertEqual(len(eg.edges()),4)
        self.assertEqual(len(eg.arcs()),2)
        self.assertEqual(len(eg.arcs()[0].edges()),2)

    def test_arcs2(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).segments()
        s2s = [Segment(Point(1.0,0.0),Point(2.0,0.0))]
        s3s = Circle(Point(3.0,0.0),1.0).polygon(4).segments()
        eg = EdgeGraph().loadwithsegments(s1s + s2s + s3s)
        self.assertEqual(len(eg.edges()),14)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)

    def test_arcs3(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        s2s = [Segment(Point(1.0,0.0),Point(2.0,0.0))]
        s3s = Circle(Point(3.0,0.0),1.0).polygon(4).close().segments()
        eg = EdgeGraph().loadwithsegments(s1s + s2s + s3s)
        # puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),18)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)


    def test_polygons(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).segments()
        s2s = [Segment(Point(1.0,0.0),Point(2.0,0.0))]
        s3s = Circle(Point(3.0,0.0),1.0).polygon(4).segments()
        eg = EdgeGraph().loadwithsegments(s1s + s2s + s3s)
        #puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),14)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)
        polygons = eg.polygons()
        #puts("polygons",[[p.coords() for p in polygon] for polygon in polygons])
        self.assertEqual(len(polygons),0)


    def test_polygons1(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        eg = EdgeGraph().loadwithsegments(s1s)
        #puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),8)
        self.assertEqual(len(eg.nodes()),4)
        self.assertEqual(len(eg.arcs()),2)
        polygons = eg.polygons()
        #puts("polygons",[[p.coords() for p in polygon] for polygon in polygons])
        self.assertEqual(len(polygons),2)

    def test_polygons1b(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        s2s = [Segment(Point(-2.0,0.0),Point(-1.0,0.0)),Segment(Point(-1.0,0.0),Point(0.0,0.0))]
        eg = EdgeGraph().loadwithsegments(s1s + s2s)
        #puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),12)
        self.assertEqual(len(eg.nodes()),6)
        self.assertEqual(len(eg.arcs()),6)
        polygons = eg.polygons()
        #puts("polygons",[[p.coords() for p in polygon] for polygon in polygons])
        self.assertEqual(len(polygons),2)


    def test_polygons2(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        s2s = [Segment(Point(1.0,0.0),Point(2.0,0.0))]
        s3s = Circle(Point(3.0,0.0),1.0).polygon(4).close().segments()
        eg = EdgeGraph().loadwithsegments(s1s + s2s + s3s)
        # puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.edges()),18)
        self.assertEqual(len(eg.nodes()),8)
        self.assertEqual(len(eg.arcs()),6)
        polygons = eg.polygons()
        #puts("closedpolygons test_polygons2",[[p.coords() for p in polygon] for polygon in polygons])
        self.assertEqual(len(polygons),2)

    def test_polygons3(self):
        p1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        p2s = [Segment(Point(-1.0,0.0),Point(1.0,0.0))]
        eg = EdgeGraph().loadwithsegments(p1s + p2s)
        #puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.nodes()),4)
        self.assertEqual(len(eg.edges()),10)
        self.assertEqual(len(eg.arcs()),6)
        # puts("closedpolygons test_polygons3",[[p.coords() for p in polygon] for polygon in eg.closedpolygons()])
        polygons = eg.polygons()
        #puts("polygons",[[p.coords() for p in polygon] for polygon in polygons])
        self.assertEqual(len(polygons),3)

    def test_polygons4(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        s2s = [Segment(Point(-2.0,0.0),Point(-1.0,0.0)),Segment(Point(-1.0,0.0),Point(1.0,0.0)),Segment(Point(1.0,0.0),Point(2.0,0.0))]
        eg = EdgeGraph().loadwithsegments(s1s + s2s)
        # puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.nodes()),6)
        self.assertEqual(len(eg.edges()),14)
        self.assertEqual(len(eg.arcs()),10)
        #puts("closedpolygons test_polygons4",[[p.coords() for p in polygon] for polygon in eg.closedpolygons()])
        self.assertEqual(len(eg.polygons()),3)

    def test_polygons5(self):
        s1s = Circle(Point(0.0,0.0),1.0).polygon(4).close().segments()
        s2s = [Segment(Point(-2.0,0.0),Point(-1.0,0.0)),Segment(Point(-1.0,0.0),Point(0.0,0.0)),Segment(Point(0.0,0.0),Point(1.0,0.0)),Segment(Point(1.0,0.0),Point(2.0,0.0)),Segment(Point(0.0,0.0),Point(0.0,-1.0)),Segment(Point(0.0,0.0),Point(0.0,1.0))]
        eg = EdgeGraph().loadwithsegments(s1s + s2s)
        # puts("edges",[edge.coords() for edge in eg.edges()])
        self.assertEqual(len(eg.nodes()),7)
        self.assertEqual(len(eg.edges()),20)
        self.assertEqual(len(eg.arcs()),20)
        #puts("closedpolygons test_polygons5",[[p.coords() for p in polygon] for polygon in eg.closedpolygons()])
        self.assertEqual(len(eg.polygons()),5)
