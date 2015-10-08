from utils            import *
from circlepackingbao import *
from baopattern       import *

def index2color(period,index):
    return color.hue2color((index%period)/(float(period)))

#
# TODO: do proper inheritance of constructor
#
class BaoPatternSwitch(BaoPattern):
    def __init__(self):
        self.msidepattern   = [1.0]
        self.mradiuspattern = [1.0]
        self.mcolorpattern  = [Color.black()]
        self.mindex   = 0

    #
    # return (Side,RatioRadius,Color)
    #
    #def next(self):
    #    self.mindex += 1
    #    return self

    def side(self):
        return lcircular(self.msidepattern,self.mindex)    

    def sidepattern(self,sidepattern):
        self.msidepattern = sidepattern
        return self

#
# To build Sides patterns
#
class BS:
    def __init__(self):
        self.mlist = []

    def push(self,ntimes):
        lastside = 1.0
        if len(self.mlist) > 0:
            lastside = -self.mlist[-1]
        self.mlist = lconcat(self.mlist,lrepeat([lastside],ntimes))
        return self

    def list(self):
        return self.mlist

    def alts(self,list):
        for item in list:
            self.push(item)
        return self
        
#
# PackingBao with switch bao direction specification
#
class CirclePackingBaoSwitch(CirclePackingBao):

    def __init__(self,boundaries=None,nodes=None,baopattern_=None,quadtree=None):
        self.mstack       = BaoStack(nodes)
        self.mlastindex   = self.mstack.lastindex()
        self.mlastside    = None
        self.mquadtree    = iff(quadtree==None,QuadTree(),quadtree)
        self.mquadtree.adds( boundaries + nodes )
        self.mbaopattern = baopattern_
        for node in nodes:
            node.packing(self)
        
    
    def iter(self,niter=1):

        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            newside              = self.mbaopattern.next().side()
            if not (newside == self.mlastside or self.mlastside == None):
                self.mstack.switch()
            (lastnode,othernode) = self.mstack.lastseed()
            newr                 = self.mbaopattern.radius()

            # compute new node if possible
            newbaonode = None

            for othernode in CirclePackingBao.genothernodes(othernode,self.mquadtree,lastnode,self.mstack,newr):
                # puts("genothernodes",lastnode,othernode)
                newbaonode = self.computenextnode(self.mquadtree,lastnode,othernode,newr,self.mstack.newindex(),newside)
                if not newbaonode == None:
                    break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                self.mlastindex = self.mstack.rewindtofreenode(self.mlastindex)
            else:
                othernode.retouch(True)
                self.mquadtree.add(newbaonode)
                self.mbaopattern.draw(newbaonode,newbaonode.colorindex())
                self.mlastindex = self.mstack.stack(newbaonode,othernode)

            if self.mlastindex < 1:
                break

            self.mlastside = newside
            
        return self
