from utils import *

import unittest

class RangeTest(unittest.TestCase):
    
    def test_init(self):
        self.assertEqual(R(1.0,2.0).v1(),1.0)
        self.assertEqual(R(1.0,3.0).v2(),3.0)

    def test_minv(self):
        self.assertEqual(R(1.0,3.0).minv(),1.0)
        self.assertEqual(R(4.0,2.0).minv(),2.0)

    def test_maxv(self):
        self.assertEqual(R(3.0,5.0).maxv(),5.0)
        self.assertEqual(R(-4.0,-6.0).maxv(),-4.0)

    def test_sample(self):
        self.assertEqual(R(1.0,3.0).sample(0.0),1.0)
        self.assertEqual(R(1.0,3.0).sample(1.0),3.0)
        self.assertEqual(R(1.0,3.0).sample(0.5),2.0)
        self.assertEqual(R(1.0,3.0).sample(-1.0),None)
        self.assertEqual(R(1.0,3.0).sample(2.0),None)

    def test_sample2(self):
        self.assertEqual(R(3.0,1.0).sample(0.0),3.0)
        self.assertEqual(R(3.0,1.0).sample(1.0),1.0)
        self.assertEqual(R(3.0,1.0).sample(0.5),2.0)
        self.assertEqual(R(3.0,1.0).sample(-1.0),None)
        self.assertEqual(R(3.0,1.0).sample(2.0),None)
        
    def test_abscissa(self):
        self.assertEqual(R(1.0,3.0).abscissa(2.0),0.5)
        self.assertEqual(R(1.0,3.0).abscissa(1.0),0.0)
        self.assertEqual(R(1.0,3.0).abscissa(3.0),1.0)
        self.assertEqual(R(1.0,3.0).abscissa(4.0),None)
        self.assertEqual(R(1.0,3.0).abscissa(0.0),None)

    def test_abscissa2(self):
        self.assertEqual(R(3.0,1.0).abscissa(2.0),0.5)
        self.assertEqual(R(3.0,1.0).abscissa(1.0),1.0)
        self.assertEqual(R(3.0,1.0).abscissa(3.0),0.0)
        self.assertEqual(R(3.0,1.0).abscissa(4.0),None)
        self.assertEqual(R(3.0,1.0).abscissa(0.0),None)
        
    def test_contain(self):
        self.assertEqual(R(0.0,1.0).contain(0.5),True)
        self.assertEqual(R(0.0,1.0).contain(0.0),True)
        self.assertEqual(R(0.0,1.0).contain(1.0),True)
        self.assertEqual(R(0.0,1.0).contain(1.1),False)
        self.assertEqual(R(0.0,1.0).contain(-0.1),False)
        
    def test_contain2(self):
        self.assertEqual(R(1.0,-1.0).contain(0.5),True)
        self.assertEqual(R(1.0,-1.0).contain(0.0),True)
        self.assertEqual(R(1.0,-1.0).contain(1.0),True)
        self.assertEqual(R(1.0,-1.0).contain(-1.0),True)
        self.assertEqual(R(1.0,-1.0).contain(1.1),False)
        self.assertEqual(R(1.0,-1.0).contain(-1.1),False)

    def test_contain3(self):
        self.assertEqual(R(1.0,1.0).contain(1.0),True)
        self.assertEqual(R(1.0,1.0).contain(1.1),False)

        
