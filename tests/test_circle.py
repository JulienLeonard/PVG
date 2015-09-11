from utils    import *
from geoutils import *
from circle   import *

import unittest

class CircleTest(unittest.TestCase):
    
    def test_defaultcircle(self):
        self.assertEqual(Circle().center().x(),0.0)
        self.assertEqual(Circle().center().y(),0.0)
        self.assertEqual(Circle().radius(),1.0)

    def test_coords(self):
        self.assertEqual(Circle().coords(), (0.0,0.0,1.0))
        self.assertEqual(Circle().coords((3.0,4.0,5.0)).coords(), (3.0,4.0,5.0))

    def test_center(self):
        self.assertEqual(Circle().center().x(), 0.0)
        self.assertEqual(Circle().center(Point(1.0,2.0)).center().x(), 1.0)
        self.assertEqual(Circle().center(Point(1.0,2.0)).center().y(), 2.0)

    def test_radius(self):
        self.assertEqual(Circle().radius(), 1.0)
        self.assertEqual(Circle().radius(3.0).radius(), 3.0)

    def test_scale(self):
        self.assertEqual(Circle().scale(3.0).radius(), 3.0)
        self.assertEqual(Circle().scale(3.0).center().x(), 0.0)
        self.assertEqual(Circle().scale(3.0).center().y(), 0.0)

    def test_translate(self):
        self.assertEqual(Circle().coords((1.0,2.0,3.0)).translate(Vector(3.0,2.0)).radius(), 3.0)
        self.assertEqual(Circle().coords((1.0,2.0,3.0)).translate(Vector(3.0,2.0)).center().x(), 4.0)
        self.assertEqual(Circle().coords((1.0,2.0,3.0)).translate(Vector(3.0,2.0)).center().y(), 4.0)

    def test_contain(self):
        self.assertEqual(Circle().containpoint(Point.P0()),           True)
        self.assertEqual(Circle().containpoint(Point(0.5,0.5)),       True)
        self.assertEqual(Circle().containpoint(Point(1.0,0.0)),       True)
        self.assertEqual(Circle().containpoint(Point(1.0,0.0),True),  False)
        self.assertEqual(Circle().containpoint(Point(1.01,0.0)),      False)
        self.assertEqual(Circle().containpoint(Point(1.0,1.0)),       False)

    
