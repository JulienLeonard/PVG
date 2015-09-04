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

    def test_lsum(self):
        self.assertEqual(lsum([]),None)
        self.assertEqual(lsum([1.0]),[1.0])
        self.assertEqual(lsum([1.0,-1.0]),[1.0,0.0])

    def test_lacc(self):
        self.assertEqual(lacc([]),None)
        self.assertEqual(lacc([1.0]),[1.0])
        self.assertEqual(lacc([1.0,-1.0]),[1.0,0.0])

    def test_lrepeat(self):
        self.assertEqual(lrepeat([],0),[])
        self.assertEqual(lrepeat([1],0),[])
        self.assertEqual(lrepeat([1],1),[1])
        self.assertEqual(lrepeat([1],2),[1,1])
        self.assertEqual(lrepeat([1,2],2),[1,2,1,2])

    def test_lfront(self):
        self.assertEqual(lfront([]),None)
        self.assertEqual(lfront([1]),1)
        self.assertEqual(lfront([2,1]),2)

    def test_lback(self):
        self.assertEqual(lback([]),None)
        self.assertEqual(lback([1]),1)
        self.assertEqual(lback([2,1]),1)

    def test_litems(self):
        self.assertEqual(litems([],1),[])
        self.assertEqual(litems([],2),[])
        self.assertEqual(litems([1],1),[1])
        self.assertEqual(litems([2],1),[2])
        self.assertEqual(litems([1,2],1),[1,2])
        self.assertEqual(litems([1,2,3,4],1),[1,2,3,4])
        self.assertEqual(litems([1,2,3,4],2),[1,3])
        self.assertEqual(litems([1,2,3,4],2,1),[2,4])

    def test_lsublist(self):
        self.assertEqual(lsublist([],1),[])
        self.assertEqual(lsublist([],2),[])
        self.assertEqual(lsublist([1],1),[1])
        self.assertEqual(lsublist([2],1),[2])
        self.assertEqual(lsublist([1,2],1),[1,2])
        self.assertEqual(lsublist([1,2,3,4],1),[1,2,3,4])
        self.assertEqual(lsublist([1,2,3,4],2),[1,3])
        self.assertEqual(lsublist([1,2,3,4],2,1),[2,4])

    def test_mean(self):
        self.assertEqual(mean(0.0,0.0),0.0)
        self.assertEqual(mean(0.0,2.0),1.0)

    def test_lmean(self):
        self.assertEqual(lmean([]),None)
        self.assertEqual(lmean([0.0,1.0,2.0]),1.0)

    def test_lmiddle(self):
        self.assertEqual(lmiddle([]),None)
        self.assertEqual(lmiddle([0.0,1.0,2.0]),1.0)
        self.assertEqual(lmiddle([0.0,1.0]),1.0)

    def test_lreverse(self):
        self.assertEqual(lreverse([]),[])
        self.assertEqual(lreverse([1.0]),[1.0])
        self.assertEqual(lreverse([1.0,2.0]),[2.0,1.0])

    def test_lflattern(self):
        self.assertEqual(lflatten([]),[])
        self.assertEqual(lflatten([[1.0]]),[1.0])
        self.assertEqual(lflatten([[1.0],[2.0]]),[1.0,2.0])
        self.assertEqual(lflatten([[1.0,2.0],[3.0,4.0]]),[1.0,2.0,3.0,4.0])

    def test_lsplit(self):
        self.assertEqual(lsplit([],2),[])
        self.assertEqual(lsplit([1.0],2),[[1.0]])
        self.assertEqual(lsplit([1.0,2.0],2),[[1.0,2.0]])
        self.assertEqual(lsplit([1.0,2.0,3.0,4.0],2),[[1.0,2.0],[3.0,4.0]])
        self.assertEqual(lsplit([1.0,2.0,3.0,4.0],3),[[1.0,2.0,3.0],[4.0]])
        
    def test_lrange(self):
        self.assertEqual(lrange([]),None)
        self.assertEqual(lrange([1.0]),(1.0,1.0))
        self.assertEqual(lrange([2.0,1.0]),(1.0,2.0))

    def test_lclose(self):
        self.assertEqual(lclose([]),[])
        self.assertEqual(lclose([0.0]),[0.0])
        self.assertEqual(lclose([0.0,1.0]),[0.0,1.0,0.0])

    def test_sign(self):
        self.assertEqual(sign( 0.0),1.0)
        self.assertEqual(sign( 2.0),1.0)
        self.assertEqual(sign(-3.0),-1.0)

    def test_iff(self):
        self.assertEqual(iff(True,0.0,1.0),0.0)
        self.assertEqual(iff(False,0.0,1.0),1.0)
    
    def test_lgeo(self):
        self.assertEqual(lgeo((2.0,0.0),0.5,0),[])
        self.assertEqual(lgeo((2.0,0.0),0.5,1),[2.0])
        self.assertEqual(lgeo((2.0,0.0),0.5,2),[2.0,0.0])
        self.assertEqual(lgeo((2.0,0.0),0.5,3),[2.0, 0.6666666666666667, 0.0])
        self.assertEqual(lgeo((2.0,0.0),0.5,4),[2.0, 0.8571428571428572, 0.2857142857142858, 0.0])
        
    def test_lzip(self):
        self.assertEqual(lzip([],[]),[])
        self.assertEqual(lzip([1.0],[]),[])
        self.assertEqual(lzip([],[1.0]),[])
        self.assertEqual(lzip([1.0],['a']),[(1.0,'a')])
        self.assertEqual(lzip([1.0,2.0],['a']),[(1.0,'a')])
        self.assertEqual(lzip([1.0,2.0],['a','b']),[(1.0,'a'),(2.0,'b')])

    def test_lzipflat(self):
        self.assertEqual(lzipflat([],[]),[])
        self.assertEqual(lzipflat([1.0],[]),[])
        self.assertEqual(lzipflat([],[1.0]),[])
        self.assertEqual(lzipflat([1.0],['a']),[1.0,'a'])
        self.assertEqual(lzipflat([1.0,2.0],['a']),[1.0,'a'])
        self.assertEqual(lzipflat([1.0,2.0],['a','b']),[1.0,'a',2.0,'b'])

    def test_lunzip(self):
        self.assertEqual(lunzip([]),([], []))
        self.assertEqual(lunzip([(1.0,2.0)]),([1.0],[2.0]))
        self.assertEqual(lunzip([(1.0,2.0),(3.0,4.0)]),([1.0,3.0],[2.0,4.0]))
        
    def test_puts(self):
        puts("toto","titi")
        
    def test_lidentity(self):
        self.assertEqual(lidentity([]),[])
        self.assertEqual(lidentity(True),True)

    def test_lshuffle(self):
        self.assertEqual(lshuffle([]),[])
        self.assertEqual(lshuffle([1.0]),[1.0])
        random.seed(0.0)
        self.assertEqual(lshuffle([1.0,2.0,3.0]),[1.0,2.0,3.0])

    def test_popfront(self):
        self.assertEqual(popfront([]),(None,[]))
        self.assertEqual(popfront([1.0]),(1.0,[]))
        self.assertEqual(popfront([1.0,2.0]),(1.0,[2.0]))

    def test_lappends(self):
        self.assertEqual(lappends([],0.0),[0.0])
        self.assertEqual(lappends(['a'],0.0,1.0,'b'),['a',0.0,1.0,'b'])
        
    def test_lshift(self):
        self.assertEqual(lshift([],0),[])
        self.assertEqual(lshift([],2),[])
        self.assertEqual(lshift([1.0,2.0],0),[1.0,2.0])
        self.assertEqual(lshift([1.0,2.0],1),[2.0,1.0])
        self.assertEqual(lshift([1.0,2.0],3),[2.0,1.0])

    def test_vtrim(self):
        self.assertEqual(vtrim(0.0,1.0,0.0),0.0)
        self.assertEqual(vtrim(0.0,1.0,1.0),1.0)
        self.assertEqual(vtrim(0.0,1.0,0.5),0.5)
        self.assertEqual(vtrim(0.0,1.0,-0.5),0.0)
        self.assertEqual(vtrim(0.0,1.0, 1.5),1.0)

    def test_bidirection(self):
        self.assertEqual(bidirection(3,3),3)
        self.assertEqual(bidirection(4,3),2)
        self.assertEqual(bidirection(5,3),1)
        self.assertEqual(bidirection(6,3),0)
        self.assertEqual(bidirection(7,3),1)
        
        

    def test_alt(self):
        self.assertEqual(alt(True,0.0,1.0),0.0)
        self.assertEqual(alt(False,0.0,1.0),1.0)

    def test_ldoublesym(self):
        self.assertEqual(ldoublesym([]),[])
        self.assertEqual(ldoublesym([1.0]),[1.0])
        self.assertEqual(ldoublesym([1.0,2.0]),[1.0,2.0])
        self.assertEqual(ldoublesym([1.0,2.0,3.0]),[1.0,2.0,3.0,2.0])
        

        

    
        
        
        
        
        

        
        
    

        
        

    
        
        

    
        
        
        



        
        


        
        
    

        
        





    
        
        
        
        
        

        
        

        
        
        
        
    
        
    
        
        
        
        
    
        
        
        
        
        
        

        


        
