from utils    import *
from color    import *

import unittest

class ColorTest(unittest.TestCase):

    def test_init(self):
        self.assertEqual(Color().r(),0.0)
        self.assertEqual(Color().g(),0.0)
        self.assertEqual(Color().b(),0.0)
        self.assertEqual(Color().a(),1.0)
        self.assertEqual(Color(0.1,0.2,0.3,0.4).r(),0.1)
        self.assertEqual(Color(0.1,0.2,0.3,0.4).g(),0.2)
        self.assertEqual(Color(0.1,0.2,0.3,0.4).b(),0.3)
        self.assertEqual(Color(0.1,0.2,0.3,0.4).a(),0.4)

    def test_values(self):
        self.assertEqual(Color(0.1,0.2,0.3,0.4).values(),[0.1,0.2,0.3,0.4])
        self.assertEqual(Color().values(),[0.0,0.0,0.0,1.0])

    def test_r(self):
        self.assertEqual(Color().r(),0.0)
        c = Color()
        self.assertNotEqual(c.r(0.1),c)
        self.assertEqual(c.r(0.1).r(),0.1)

    def test_g(self):
        self.assertEqual(Color().g(),0.0)
        c = Color()
        self.assertNotEqual(c.g(0.1),c)
        self.assertEqual(c.g(0.1).g(),0.1)

    def test_b(self):
        self.assertEqual(Color().b(),0.0)
        c = Color()
        self.assertNotEqual(c.b(0.1),c)
        self.assertEqual(c.b(0.1).b(),0.1)
        
    def test_a(self):
        self.assertEqual(Color().a(),1.0)
        c = Color()
        self.assertNotEqual(c.a(0.1),c)
        self.assertEqual(c.a(0.1).a(),0.1)
    
    def test_name(self):
        self.assertEqual(Color.name("red").values(),  [1.0,0.0,0.0,1.0])
        self.assertEqual(Color.name("green").values(),[0.0,1.0,0.0,1.0])
        self.assertEqual(Color.name("white").values(),[1.0,1.0,1.0,1.0])

    def test_random(self):
        random.seed(0.0)
        self.assertEqual(Color.random().values(),  [0.8444218515250481, 0.7579544029403025, 0.420571580830845, 1.0])
        self.assertEqual(Color.random(0.5).values(),  [0.25891675029296335, 0.5112747213686085, 0.4049341374504143, 0.5])

    def test_random(self):
        random.seed(0.0)
        self.assertEqual(Color.rand().values(),  [0.8444218515250481, 0.7579544029403025, 0.420571580830845, 1.0])
        self.assertEqual(Color.rand(0.5).values(),  [0.25891675029296335, 0.5112747213686085, 0.4049341374504143, 0.5])

    def test_trimcolor(self):
        self.assertEqual(Color.trimcolor(Color(1.1,-0.1,0.5,1.3)).values(),  [1.0,0.0,0.5,1.0])

    def test_hsv(self):
        self.assertEqual(Color.hsv(0.0,1.0,1.0,1.0).values(),  [1.0,0.0,0.0,1.0])
        
    def test_hsl(self):
        self.assertEqual(Color.hsl(0.0,1.0,0.5,1.0).values(),  [1.0,0.0,0.0,1.0])

    def test_hue2color(self):
        self.assertEqual(Color.hue2color(0.0).values(),  [1.0,0.0,0.0,1.0])
                           

        

        



