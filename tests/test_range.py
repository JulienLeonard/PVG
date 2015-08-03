# some_file.py
import sys
sys.path.insert(0, './../lib')

from utils import *

import unittest

class RangeTest(unittest.TestCase):
    
    def test_init(self):
        self.assertEqual(R(1.0,2.0).v1(),1.0)
        self.assertEqual(R(1.0,3.0).v2(),3.0)

    def test_sample(self):
        self.assertEqual(R(1.0,3.0).sample(0.0),1.0)
        self.assertEqual(R(1.0,3.0).sample(1.0),3.0)
        self.assertEqual(R(1.0,3.0).sample(0.5),2.0)
        # TODO self.assertEqual(R(1.0,3.0).sample(-1.0),1.0)
        # TODO self.assertEqual(R(1.0,3.0).sample(2.0),3.0)
        
