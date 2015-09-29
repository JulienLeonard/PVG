from utils                  import *
from circlepackingbao       import *
from circlepackingbaoswitch import *
from baopattern             import *

#
# Extension of BaoPattern for layer, to have a hook for drawing layers altogether
#
class BaoPatternLayer(BaoPattern):
    def __init__(self):
        self.mradiuspattern      = [1.0]
        self.mcolorpattern       = [Color.black()]
        self.mindex              = 0
        self.mindexlayer         = 0
        self.mfdraw              = None
        self.mfdrawlayer         = None
        self.mradiuspatternlayer = None
        self.mcolorpatternlayer  = None

    def nextlayer(self):
        self.mindexlayer += 1
        return self

    def radiuspatternlayer(self,radiuspattern):
        self.mradiuspatternlayer = radiuspattern
        return self

    def colorpatternlayer(self,colorpattern):
        self.mcolorpatternlayer = colorpattern
        return self

    def radius(self):
        if self.mradiuspatternlayer == None:
            return  super(BaoPatternLayer,self).radius()
        else:
            return lcircular(self.mradiuspatternlayer,self.mindexlayer)

    def colorlayer(self,index=None):
        if index == None:
            index = self.mindexlayer
        return lcircular(self.mcolorpatternlayer,index)


    def fdrawlayer(self, v = None):
        if v == None:
            return self.mfdrawlayer
        else:
            self.mfdrawlayer = v
            return self

    def draw(self,newnode,index):
        if not self.fdraw() == None:
            self.fdraw()(newnode,index,self.color(index))

    def drawlayer(self,nodes,ilayer):
        if not self.fdrawlayer() == None:
            self.fdrawlayer()(nodes,ilayer,self.colorlayer(ilayer))

#
# TODO: create layerstack to take care of layers
#
class BaoStackLayer(BaoStack):

    def __init__(self,nodes):
        super(BaoStackLayer,self).__init__(nodes)
        self.mlayers = []
        self.mclayer = nodes[:]

    def stacklayer(self):
        self.mlayers.append(self.mclayer)
        self.mclayer = []

    def lastlayer(self):
        return self.mlayers[-1]

    def layers(self):
        return self.mlayers

    def nlayers(self):
        return len(self.mlayers)

    def stack(self,newnode,othernode):
        self.mclayer.append(newnode)
        return super(BaoStackLayer,self).stack(newnode,othernode)

    def currentLayerEmpty(self):
        return (len(self.mclayer) == 0)

#
# PackingBao with direction changed when colliding, defining layers of nodes
#
class CirclePackingBaoLayer(CirclePackingBao):

    def __init__(self,boundaries=None,nodes=None,baopattern_=None,side0=None,quadtree=None):
        self.mstack       = BaoStackLayer(nodes)
        self.mlastindex   = self.mstack.lastindex()
        self.mcside       = side0
        self.mbaopattern  = baopattern_
        self.mquadtree    = iff(quadtree == None, QuadTree(), quadtree)
        self.mquadtree.adds( boundaries + nodes )
        for node in nodes:
            node.packing(self)
        self.miterperlayer = 0

    def niterperlayer(self):
        return self.miterperlayer

    def computenextnode(self,quadtree,node2,node1,newr,index,side):
        result = (None,False)
        newcircle = circles2tangentout(node2,node1,newr,side)
        if not newcircle == None:
            collidings  = lsubstract(quadtree.colliding(newcircle),[node1,node2])
            # puts("newcircle",newcircle.coords(),"collidings",[(c,c.coords()) for c in collidings])
            if len(collidings) == 0:
                newbaonode = BaoNode(self,newcircle,node2.colorindex() + 1,index + 1)
                return (newbaonode,False)
            else:
                endlayer = False
                for colliding in collidings:
                    if not isinstance(colliding,BaoNode) or not colliding.packing() == self:
                        endlayer = True
                        break
                result = (None,endlayer)
        return result

    def iter(self,niter=1):

        for iiter in range(niter):
            self.miterperlayer += 1

            ifputs(iiter != 0 and iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            (lastnode,othernode) = self.mstack.lastseed()
            newr                 = self.mbaopattern.next().radius()
            # puts("current paramaters",lastnode,othernode)

            # compute new node if possible
            newbaonode = None

            foreigncollision = False
            for othernode in CirclePackingBao.genothernodes(othernode,self.mquadtree,lastnode,self.mstack,newr):
                (newbaonode,foreigncollision) = self.computenextnode(self.mquadtree,lastnode,othernode,newr,self.mstack.newindex(),self.mcside)
                # puts("genothernodes",lastnode,othernode,"newbaonode,foreigncollision",newbaonode,foreigncollision,"cside",cside)
                if not newbaonode == None:
                    break
                else:
                    if foreigncollision:
                        break

            if foreigncollision and not self.mstack.currentLayerEmpty():
                # puts("foreigncollision")
                self.mstack.stacklayer()
                self.mbaopattern.drawlayer(self.mstack.lastlayer(),self.mstack.nlayers())
                self.mbaopattern.nextlayer()
                self.miterperlayer = 0
                self.mstack.switch()
                (lastnode,othernode) = self.mstack.lastseed()
                self.mcside = -self.mcside
                # TODO: find a way to factorize the two genothernodes calls
                for othernode in CirclePackingBao.genothernodes(othernode,self.mquadtree,lastnode,self.mstack,newr):
                    # puts("genothernodes after foreigncollision",lastnode,othernode,"cside",cside)
                    (newbaonode,foreigncollision) = self.computenextnode(self.mquadtree,lastnode,othernode,newr,self.mstack.newindex(),self.mcside)
                    # puts("genothernodes after foreigncollision",lastnode,othernode,"newbaonode,foreigncollision",newbaonode,foreigncollision)
                    if not newbaonode == None:
                        break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                self.mlastindex = self.mstack.rewindtofreenode(self.mlastindex)
                # puts("no new node found, new lastindex",lastindex)
            else:
                # puts("found newbao node",newbaonode)
                othernode.retouch(True)
                self.mquadtree.add(newbaonode)
                self.mbaopattern.draw(newbaonode,newbaonode.colorindex())
                self.mlastindex = self.mstack.stack(newbaonode,othernode)

            if self.mlastindex < 1:
                break

        return self
