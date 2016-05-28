from utils         import *
from geoutils      import *
from tangentutils  import *
from quadtree      import *
from circleadj     import *
from circlepacking import *

class BaoNode(Circle):

    def __init__(self,packing,circle,colorindex,index):
        self.mpacking     = packing
        self.mcenter      = circle.center()
        self.mradius      = circle.radius()
        self.mbbox        = circle.bbox()
        self.mretouch     = False
        self.mnotfound    = False
        self.mcolorindex  = colorindex
        self.mindex       = index
        self.mcoords      = circle.coords()
        
    def colorindex(self):
        return self.mcolorindex

    def index(self):
        return self.mindex

    def packing(self,v = None):
        if v == None:
            return self.mpacking
        else:
            self.mpacking = v
            return self

    def retouch(self,v = None):
        if v == None:
            return self.mretouch
        else:
            self.mretouch = v
            return self

    def notfound(self,v = None):
        if v == None:
            return self.mnotfound
        else:
            self.mnotfound = v
            return self

    @staticmethod
    def nodes(nodes,startindex = None):
        result = []
        if startindex == None:
            cindex = -1
        else:
            cindex = startindex + 1
        for node in nodes:
            newindex = iff(startindex == None,-1,cindex)
            result.append(BaoNode(node,cindex,newindex))
            cindex += 1
        return result

    @staticmethod
    def fromcircle(circle,packing=None):
        x,y,r = circle.coords()
        return [BaoNode(packing,Circle().coords((x-r/2.0,y,r/2.0)),0,0),BaoNode(packing,Circle().coords((x+r/2.0,y,r/2.0)),1,1)]

    @staticmethod
    def fromsegment(segment,packing=None,radius=None):
        radius  = iff(radius == None, segment.length()/2.0, radius)
        offset = radius / (segment.length())
        center1 = segment.sample(0.5 - offset).add(segment.normal().scale(-radius))
        center2 = segment.sample(0.5 + offset).add(segment.normal().scale(-radius))
        return [BaoNode(packing,Circle(center1,radius),0,0),BaoNode(packing,Circle(center2,radius),0,1)]

    @staticmethod
    def baonodes0(packing=None):
        return [BaoNode(packing,Circle().coords((0.0,0.0,1.0)),0,0),BaoNode(packing,Circle().coords((2.0,0.0,1.0)),1,1)]

class BaoStack(object):
    
    def __init__(self,nodes):
        self.mnodes         = nodes
        self.mlastnode      = nodes[-1]
        self.mlastlastnode  = nodes[-2]
        self.mothernode     = nodes[-2]
        self.mlast3node     = None
        self.mprevdirection = 1.0
        
    def set(self,nodes,lastindex):
        self.mlastnode     = iff(self.mprevdirection > 0.0, nodes[lastindex], nodes[lastindex])
        self.mlastlastnode = iff(self.mprevdirection > 0.0, nodes[lastindex-1], nodes[lastindex+1])
        self.mothernode    = self.mlastlastnode
        self.mlast3node    = None

    def lastindex(self):
        return len(self.mnodes) - 1 

    def stack(self,newnode,othernode):
        self.mnodes.append(newnode)
        self.mlast3node    = self.mlastlastnode
        self.mlastlastnode = self.mlastnode
        self.mlastnode     = newnode
        self.mothernode    = othernode
        return self.lastindex()

    def lastnodes(self):
        return [self.mlastnode,self.mlastlastnode,self.mlast3node]
    
    def lastseed(self):
        return (self.mlastnode,self.mothernode)

    def excludednodes(self,othernode):
        return self.lastnodes() + [othernode]


    def findlastfreenode(self,nodes,lastindex):
        freenode = nodes[lastindex]
        while ((freenode.retouch() or freenode.notfound()) and lastindex > 0):
            lastindex = lastindex - 1
            freenode = nodes[lastindex]
        return (freenode,lastindex)

    def rewindtofreenode(self,lastindex):
        (freenode,lastindex) = self.findlastfreenode(self.mnodes,lastindex)
        self.set(self.mnodes,lastindex)
        return lastindex

    def nodes(self):
        return self.mnodes

    def newindex(self):
        return len(self.mnodes)

    def node(self,index):
        for node in self.mnodes:
            if node.index() == index:
                return node
        return None

    def nextothernode(self,othernode):
        return self.node(iff(self.mprevdirection > 0.0, othernode.index() + 1, othernode.index() - 1))

    def switch(self):
        self.mlastnode      = self.mlastnode
        self.mothernode     = self.mlastlastnode
        self.mlastlastnode  = None
        self.mlast3node     = None
        self.mprevdirection = -self.mprevdirection


class CirclePackingBao:

    def __init__(self,boundaries=None,nodes=None,baopattern_=None,side=1.0,quadtree=None):
        self.mstack       = BaoStack(nodes)
        self.mlastindex   = self.mstack.lastindex()
        self.mquadtree    = iff(quadtree==None,QuadTree(),quadtree)
        self.mbaopattern  = baopattern_
        self.mside        = side
        self.mquadtree.adds( boundaries + nodes )
        for node in nodes:
            node.packing(self)

    def computenextnode(self,quadtree,node2,node1,newr,index,iside):
        newcircle = circles2tangentout(node2,node1,newr,iside)
        if not newcircle == None and not quadtree.iscolliding(newcircle):
            newbaonode = BaoNode(self,newcircle,node2.colorindex() + 1,index + 1)
            return newbaonode
        return None


    @staticmethod
    def findnewother(quadtree,lastnode,excludenodes,newr):
        bigcircle   = lastnode.scale( (lastnode.r() + newr * 2.1)/ lastnode.r() )
        collidings  = quadtree.colliding(bigcircle)
        ccollidings = lsubstract(collidings,excludenodes)
        ccollidings = [c for c in ccollidings if isinstance(c,BaoNode)]
        ccollidings = lremove([node if (node.index() >= 0) else None for node in ccollidings],None)
        sortlist = [(n.index,n) for n in ccollidings]
        sortlist.sort()
        return [item[1] for item in sortlist]

    #
    # lazy method to avoid calling findnewother if othernode exist and is successful
    #
    @staticmethod
    def genothernodes(othernode,quadtree,lastnode,stack,newr):
        if not othernode == None:
            #puts("yield other node")
            yield othernode
        if not othernode == None:
            #puts("yield next other node")
            nextothernode = stack.nextothernode(othernode)
            if not nextothernode == None:
                yield nextothernode
        ccollidings = CirclePackingBao.findnewother(quadtree,lastnode,stack.excludednodes(othernode),newr)
        for othernode in ccollidings:
            if isinstance(othernode,BaoNode):
                #puts("yield colliding baonode")
                yield othernode

    def iter(self,niter=1):
        
        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            (lastnode,othernode) = self.mstack.lastseed()
            newr                 = self.mbaopattern.next().radius()

            # compute new node if possible
            newbaonode = None

            for othernode in CirclePackingBao.genothernodes(othernode,self.mquadtree,lastnode,self.mstack,newr):
                # puts("genothernodes",lastnode,othernode)
                newbaonode = self.computenextnode(self.mquadtree,lastnode,othernode,newr,self.mstack.newindex(),self.mside)
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
            
        return self
