import sys
sys.path.insert(0, './../lib')

from utils import *

import unittest

class BasicTest(unittest.TestCase):
    
    def test_circular(self):
        self.assertEqual(circular([0.0,1.0,2.0],0),0.0)
        self.assertEqual(circular([0.0,1.0,2.0],2),2.0)
        self.assertEqual(circular([0.0,1.0,2.0],3),0.0)
        self.assertEqual(circular([0.0,1.0,2.0],4),1.0)
        self.assertEqual(circular([0.0,1.0,2.0],5),2.0)
        self.assertEqual(circular([0.0,1.0,2.0],7),1.0)

    def test_lcircular(self):
        self.assertEqual(lcircular([0.0,1.0,2.0],0),0.0)
        self.assertEqual(lcircular([0.0,1.0,2.0],2),2.0)
        self.assertEqual(lcircular([0.0,1.0,2.0],3),0.0)
        self.assertEqual(lcircular([0.0,1.0,2.0],4),1.0)
        self.assertEqual(lcircular([0.0,1.0,2.0],5),2.0)
        self.assertEqual(lcircular([0.0,1.0,2.0],7),1.0)
    
    def test_sliceIterator(self):
        self.assertEqual([i for i in sliceIterator(range(5),3)],[[0,1,2],[1,2,3],[2,3,4]])
    
    def test_foreach2(self):
        self.assertEqual([i for i in foreach2(range(5))],[[0,1],[2,3]])

    def test_foreachn(self):
        self.assertEqual([i for i in foreachn(range(7),3)],[[0,1,2],[3,4,5]])

    def test_pairs(self):
        self.assertEqual([i for i in pairs(range(4))],[(0,1),(1,2),(2,3)])

    def test_triplets(self):
        self.assertEqual([i for i in triplets(range(4))],[(0,1,2),(1,2,3)])
        
    def test_circlepairs(self):
        self.assertEqual([i for i in circlepairs(range(4))],[(0,1),(1,2),(2,3),(3,0)])

    def test_sample(self):
        self.assertEqual(sample((0.0,2.0),0.5),1.0)
        self.assertEqual(sample((0.0,3.0),1.0),3.0)
        self.assertEqual(sample((1.0,2.0),0.0),1.0)
        self.assertEqual(sample((1.0,2.0),-1.0),0.0)
        self.assertEqual(sample((1.0,2.0),2.0),3.0)

    def test_rangefit(self):
        self.assertEqual(rangefit((0.0,2.0),0.5),0.5)
        self.assertEqual(rangefit((0.0,3.0),1.0),1.0)
        self.assertEqual(rangefit((1.0,2.0),0.0),1.0)
        self.assertEqual(rangefit((1.0,2.0),-1.0),1.0)
        self.assertEqual(rangefit((1.0,2.0),2.0),2.0)

    def test_samples(self):
        self.assertEqual(samples((0.0,2.0),0),[])
        self.assertEqual(samples((0.0,2.0),1),[0.0])
        self.assertEqual(samples((0.0,2.0),2),[0.0,2.0])
        self.assertEqual(samples((0.0,2.0),3),[0.0,1.0,2.0])

    def test_usamples(self):
        self.assertEqual(usamples(0),[])
        self.assertEqual(usamples(1),[0.0])
        self.assertEqual(usamples(2),[0.0,1.0])
        self.assertEqual(usamples(3),[0.0,0.5,1.0])

        


        
