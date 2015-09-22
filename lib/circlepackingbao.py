from utils         import *
from drawutils     import *
from geoutils      import *
from tangentutils  import *
from quadtree      import *
from circleadj     import *
from circlepacking import *

class BaoNode(Circle):

    def __init__(self,circle,colorindex,index):
        self.mcenter      = circle.center()
        self.mradius      = circle.radius()
        self.mretouch     = False
        self.mnotfound    = False
        self.mcolorindex  = colorindex
        self.mindex       = index

    def colorindex(self):
        return self.mcolorindex

    def index(self):
        return self.mindex

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
    def fromcircle(circle):
        x,y,r = circle.coords()
        return [BaoNode(Circle().coords((x-r/2.0,y,r/2.0)),0,0),BaoNode(Circle().coords((x+r/2.0,y,r/2.0)),1,1)]

    @staticmethod
    def fromsegment(segment):
        radius  = segment.length()/2.0
        center1 = segment.sample(0.0).add(segment.normal().scale(-radius))
        center2 = segment.sample(1.0).add(segment.normal().scale(-radius))
        return [BaoNode(Circle(center1,radius),0,0),BaoNode(Circle(center2,radius),0,1)]


def baonodes0():
    return [BaoNode(Circle().coords((0.0,0.0,1.0)),0,0),BaoNode(Circle().coords((2.0,0.0,1.0)),1,1)]

class BaoStack:
    
    def __init__(self,nodes):
        self.mnodes        = nodes
        self.mlastnode     = nodes[-1]
        self.mlastlastnode = nodes[-2]
        self.mothernode    = nodes[-2]
        self.mlast3node    = None

    def set(self,nodes,lastindex):
        self.mlastnode     = nodes[lastindex]
        self.mlastlastnode = nodes[lastindex-1]
        self.mothernode    = None
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
        return self.node(othernode.index() + 1)

class CirclePackingBao:
    

    @staticmethod
    def computenextnode(quadtree,node2,node1,newr,index):
        allsides = [1.0,-1.0]
        for iside in allsides:
            newcircle = circles2tangentout(node2,node1,newr,iside)
            if not newcircle == None and not quadtree.iscolliding(newcircle):
                newbaonode = BaoNode(newcircle,node2.colorindex() + 1,index + 1)
                return newbaonode
        return None


    @staticmethod
    def findnewother(quadtree,lastnode,excludenodes,newr):
        bigcircle   = lastnode.scale( (lastnode.r() + newr * 2.1)/ lastnode.r() )
        collidings  = quadtree.colliding(bigcircle)
        ccollidings = lsubstract(collidings,excludenodes)
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
            yield othernode
        if not othernode == None:
            yield stack.nextothernode(othernode)
        ccollidings = CirclePackingBao.findnewother(quadtree,lastnode,stack.excludednodes(othernode),newr)
        for othernode in ccollidings:
            yield othernode

    @staticmethod
    def iter(boundaries,nodes,baopattern,niter):
        nodes       = BaoNode.nodes(nodes,0)
        boundaries  = BaoNode.nodes(boundaries)        
        stack       = BaoStack(nodes)
        lastindex   = stack.lastindex()
        quadtree    = QuadTree().adds( boundaries + nodes )
        
        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            (lastnode,othernode) = stack.lastseed()
            newr                 = baopattern.next().radius()

            # compute new node if possible
            newbaonode = None

            for othernode in CirclePackingBao.genothernodes(othernode,quadtree,lastnode,stack,newr):
                newbaonode = CirclePackingBao.computenextnode(quadtree,lastnode,othernode,newr,stack.newindex())
                if not newbaonode == None:
                    break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                lastindex = stack.rewindtofreenode(lastindex)
            else:
                othernode.retouch(True)
                quadtree.add(newbaonode)
                baopattern.draw(newbaonode,newbaonode.colorindex())
                lastindex = stack.stack(newbaonode,othernode)

            if lastindex < 1:
                break
            
        return stack.nodes()
