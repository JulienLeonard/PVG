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

    def test_urandsamples(self):
        random.seed(0.0)
        vrands = urandsamples(4)
        self.assertEqual(urandsamples(0),[])
        self.assertEqual(urandsamples(1),[0.0])
        self.assertEqual(urandsamples(2),[0.0,1.0])
        self.assertEqual(len(vrands),4)
        self.assertEqual(vrands[0],0.0)
        self.assertEqual(vrands[-1],1.0)
        self.assertEqual(vrands[1] < vrands[2],True)

    def test_rand(self):
        random.seed(0.0)
        v = rand(0.0,1.0)
        self.assertEqual(v >= 0.0,True)
        self.assertEqual(v <= 1.0,True)

    def test_rands(self):
        random.seed(0.0)
        vs = rands((0.0,1.0),5)
        self.assertEqual(len(vs),5)
        for v in vs:
            self.assertEqual(v >= 0.0,True)
            self.assertEqual(v <= 1.0,True)

    def test_lrand(self):
        random.seed(0.0)
        self.assertEqual(lrand([]),"")
        self.assertEqual(lrand([0]),0)
        self.assertEqual(lrand([0,1]),1)
        self.assertEqual(lrand([0,1]),0)

    def test_pi(self):
        self.assertEqual(pi(),math.pi)

    def test_normangle(self):
        self.assertEqual(normangle(0.0),0.0)
        self.assertEqual(normangle(pi()),pi())
        self.assertEqual(normangle(2.0* pi()), 2.0 * pi())
        self.assertEqual(normangle(3.0* pi()), pi())
        self.assertEqual(normangle(-0.1),2.0 * pi() - 0.1)
        # self.assertEqual(normangle(2.0 * pi() + 0.1), 0.1)

    def test_multisamples(self):
        self.assertEqual(multisamples([(0.0,0.0),(0.5,1.0),(1.0,0.0)],0.0),0.0)
        self.assertEqual(multisamples([(0.0,0.0),(0.5,1.0),(1.0,0.0)],1.0),0.0)
        self.assertEqual(multisamples([(0.0,0.0),(0.5,1.0),(1.0,0.0)],0.5),1.0)
        self.assertEqual(multisamples([(0.0,0.0),(0.5,1.0),(1.0,0.0)],0.25),0.5)
        self.assertEqual(multisamples([(0.0,0.0),(0.5,1.0),(1.0,0.0)],0.75),0.5)

        self.assertEqual(multisamples([(1.0,0.0),(2.0,1.0),(4.0,0.0)],0.0),0.0)
        self.assertEqual(multisamples([(1.0,0.0),(2.0,1.0),(4.0,0.0)],1.0),0.0)
        self.assertEqual(multisamples([(1.0,0.0),(2.0,1.0),(4.0,0.0)],1.5),0.5)
        self.assertEqual(multisamples([(1.0,0.0),(2.0,1.0),(4.0,0.0)],2.0),1.0)
        self.assertEqual(multisamples([(1.0,0.0),(2.0,1.0),(4.0,0.0)],3.0),0.5)

        #self.assertEqual(multisamples([],0.0),"")
        #self.assertEqual(multisamples([(0.0,0.0)],0.0),"")

    def rangle(self):
        self.assertEqual(rangle(),(0.0,2.0*pi()))

    def test_abscissa(self):
        self.assertEqual(abscissa((1.0,3.0),1.0),0.0)
        self.assertEqual(abscissa((1.0,3.0),2.0),0.5)
        self.assertEqual(abscissa((1.0,3.0),3.0),1.0)
        self.assertEqual(abscissa((1.0,3.0),-1.0),0.0)
        self.assertEqual(abscissa((1.0,3.0),4.0),1.0)

    def test_circularnext(self):
        self.assertEqual(circularnext([0.0,1.0,2.0],0.0),1.0)
        self.assertEqual(circularnext([0.0,1.0,2.0],1.0),2.0)
        self.assertEqual(circularnext([0.0,1.0,2.0],2.0),0.0)
        self.assertEqual(circularnext([],2.0),"")
        self.assertEqual(circularnext([1.0],1.0),1.0)
        self.assertEqual(circularnext([2.0],1.0),"")

    def test_circularprev(self):
        self.assertEqual(circularprev([0.0,1.0,2.0],0.0),2.0)
        self.assertEqual(circularprev([0.0,1.0,2.0],1.0),0.0)
        self.assertEqual(circularprev([0.0,1.0,2.0],2.0),1.0)
        self.assertEqual(circularprev([],2.0),"")
        self.assertEqual(circularprev([1.0],1.0),1.0)
        self.assertEqual(circularprev([2.0],1.0),"")

    def test_lunique(self):
        self.assertEqual(lunique([]),[])
        self.assertEqual(lunique([0.0]),[0.0])
        self.assertEqual(lunique([0.0,0.0]),[0.0])
        self.assertEqual(lunique([0.0,1.0,0.0]),[0.0,1.0])
        self.assertEqual(lunique([0.0,1.0,0.0,1.0]),[0.0,1.0])

    def test_lremove(self):
        self.assertEqual(lremove([],0.0),[])
        self.assertEqual(lremove([0.0],0.0),[])
        self.assertEqual(lremove([0.0,0.0],0.0),[])
        self.assertEqual(lremove([0.0,1.0,0.0],0.0),[1.0])
        
    def test_lsubstract(self):
        self.assertEqual(lsubstract([],[0.0,1.0]),[])
        self.assertEqual(lsubstract([0.0],[0.0,1.0]),[])
        self.assertEqual(lsubstract([0.0,1.0],[0.0,1.0]),[])
        self.assertEqual(lsubstract([0.0,1.0,0.0,1.0],[0.0,1.0]),[])
        self.assertEqual(lsubstract([0.0,1.0,2.0,1.0],[0.0,1.0]),[2.0])

    def test_lmin(self):
        self.assertEqual(lmin([]),None)
        self.assertEqual(lmin([1.0,2.0]),1.0)
        self.assertEqual(lmin(1.0,2.0),1.0)

    def test_lmax(self):
        self.assertEqual(lmax([]),None)
        self.assertEqual(lmax([1.0]),1.0)
        self.assertEqual(lmax([1.0,2.0]),2.0)

    def test_lconcat(self):
        self.assertEqual(lconcat([]),[])
        self.assertEqual(lconcat([],[]),[])
        self.assertEqual(lconcat([],[1.0]),[1.0])
        self.assertEqual(lconcat([],[1.0],[2.0,3.0]),[1.0,2.0,3.0])

    def test_ladd(self):
        self.assertEqual(ladd([]),None)
        self.assertEqual(ladd([1.0]),1.0)
        self.assertEqual(ladd([1.0,-1.0]),0.0)
        
        
        
        
        

        
        

        
        
        
        
    
        
    
        
        
        
        
    
        
        
        
        
        
        

        


        
