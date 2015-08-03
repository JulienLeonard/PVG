# some_file.py
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

    def test_addv(self):
        self.assertEqual(Point().addv(Vector()).coords(), (1.0,0.0))
        self.assertEqual(Point(1.0,2.0).addv(Vector(3.0,4.0)).coords(), (4.0,6.0))


if __name__ == '__main__':
    unittest.main()

unittest.main()



