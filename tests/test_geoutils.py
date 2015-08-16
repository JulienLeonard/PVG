import sys
sys.path.insert(0, './../lib')

from utils import *
from geoutils import *

import unittest

class PointTest(unittest.TestCase):
    
    def test_defaultpoint(self):
        self.assertEqual(Point().x(),0.0)
        self.assertEqual(Point().y(),0.0)

    def test_x(self):
        self.assertEqual(Point().x(), 0.0)
        self.assertEqual(Point().x(1.0).x(), 1.0)

    def test_y(self):
        self.assertEqual(Point().y(), 0.0)
        self.assertEqual(Point().y(2.0).y(), 2.0)


    def test_coords(self):
        self.assertEqual(Point().coords(), (0.0,0.0))
        self.assertEqual(Point().coords((3.0,4.0)).coords(), (3.0,4.0))

    def test_add(self):
        self.assertEqual(Point().add(Vector()).coords(), (1.0,0.0))
        self.assertEqual(Point(1.0,2.0).add(Vector(3.0,4.0)).coords(), (4.0,6.0))

class VectorTest(unittest.TestCase):
    
    def test_defaultvector(self):
        self.assertEqual(Vector().x(),1.0)
        self.assertEqual(Vector().y(),0.0)

    def test_x(self):
        self.assertEqual(Vector().x(), 1.0)
        self.assertEqual(Vector().x(2.0).x(), 2.0)

    def test_y(self):
        self.assertEqual(Vector().y(), 0.0)
        self.assertEqual(Vector().y(3.0).y(), 3.0)


    def test_coords(self):
        self.assertEqual(Vector().coords(), (1.0,0.0))
        self.assertEqual(Vector().coords((3.0,4.0)).coords(), (3.0,4.0))

    def test_length(self):
        self.assertEqual(Vector(2.0,0.0).length(), 2.0)
        self.assertEqual(Vector(3.0,4.0).length(), 5.0)

    def test_normalize(self):
        oldv = Vector(2.0,0.0)
        newv = oldv.normalize()
        self.assertEqual(oldv.coords(), (2.0,0.0))
        self.assertEqual(newv.coords(), (1.0,0.0))


    






