from utils                  import *
from circlepackingbao       import *
from circlepackingbaoswitch import *
from baopattern             import *

class BaoPatternLayer(BaoPattern):
    def __init__(self):
        self.mradiuspattern = [1.0]
        self.mcolorpattern  = [Color.black()]
        self.mindex         = 0
        self.mfdraw         = None
        self.mfdrawlayer    = None

    def fdrawlayer(self, v = None):
        if v == None:
            return self.mfdrawlayer
        else:
            self.mfdrawlayer = v
            return self

    def draw(self,newnode,index):
        if not self.fdraw() == None:
            self.fdraw()(newnode,index,self.color(index))

    def drawlayer(self,nodes):
        if not self.fdrawlayer() == None:
            self.fdrawlayer()(nodes)


class CirclePackingBaoLayer(CirclePackingBao):


    @staticmethod
    def computenextnode(quadtree,node2,node1,newr,index,side):
        result = (None,False)
        newcircle = circles2tangentout(node2,node1,newr,side)
        if not newcircle == None:
            collidings  = lsubstract(quadtree.colliding(newcircle),[node1,node2])
            # puts("newcircle",newcircle.coords(),"collidings",[(c,c.coords()) for c in collidings])
            if len(collidings) == 0:
                newbaonode = BaoNode(newcircle,node2.colorindex() + 1,index + 1)
                return (newbaonode,False)
            else:
                endlayer = False
                for colliding in collidings:
                    if not isinstance(colliding,BaoNode):
                        endlayer = True
                        break
                result = (None,endlayer)
        return result

    
    @staticmethod
    def iter(boundaries,nodes,baopattern,niter,side0):
        stack       = BaoStack(nodes)
        lastindex   = stack.lastindex()
        quadtree    = QuadTree().adds( boundaries + nodes )
        clayer      = nodes[:]

        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            (lastnode,othernode) = stack.lastseed()
            newr                 = baopattern.next().radius()
            # puts("current paramaters",lastnode,othernode)

            # compute new node if possible
            newbaonode = None

            foreigncollision = False
            for othernode in CirclePackingBao.genothernodes(othernode,quadtree,lastnode,stack,newr):
                (newbaonode,foreigncollision) = CirclePackingBaoLayer.computenextnode(quadtree,lastnode,othernode,newr,stack.newindex(),side0)
                # puts("genothernodes",lastnode,othernode,"newbaonode,foreigncollision",newbaonode,foreigncollision,"side0",side0)
                if not newbaonode == None:
                    break
                else:
                    if foreigncollision:
                        break

            if foreigncollision and len(clayer) > 0:
                # puts("foreigncollision")
                baopattern.drawlayer(clayer)
                clayer = []
                stack.switch()
                (lastnode,othernode) = stack.lastseed()
                side0 = -side0
                # TODO: find a way to factorize the two genothernodes calls
                for othernode in CirclePackingBao.genothernodes(othernode,quadtree,lastnode,stack,newr):
                    # puts("genothernodes after foreigncollision",lastnode,othernode,"side0",side0)
                    (newbaonode,foreigncollision) = CirclePackingBaoLayer.computenextnode(quadtree,lastnode,othernode,newr,stack.newindex(),side0)
                    # puts("genothernodes after foreigncollision",lastnode,othernode,"newbaonode,foreigncollision",newbaonode,foreigncollision)
                    if not newbaonode == None:
                        break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                lastindex = stack.rewindtofreenode(lastindex)
                # puts("no new node found, new lastindex",lastindex)
            else:
                # puts("found newbao node",newbaonode)
                othernode.retouch(True)
                quadtree.add(newbaonode)
                clayer.append(newbaonode)
                baopattern.draw(newbaonode,newbaonode.colorindex())
                lastindex = stack.stack(newbaonode,othernode)

            if lastindex < 1:
                break

        return stack.nodes()
