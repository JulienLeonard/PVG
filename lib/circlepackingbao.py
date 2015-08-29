from utils         import *
from drawutils     import *
from geoutils      import *
from tangentutils  import *
from quadtree      import *
from circleadj     import *
from circlepacking import *

def index2color(period,index):
    return color.hue2color((index%period)/(float(period)))

def nextadjcircle(node1,node2,newr,side):
    return circles2tangent(node1,"OUT",node2,"OUT",newr,side)

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
            cindex = 0
        else:
            cindex = startindex + 1
        for node in nodes:
            newindex = iff(startindex == None,0,cindex)
            result.append(BaoNode(node,cindex,newindex))
            cindex += 1
        return result


def baonodes0():
    return [BaoNode(Circle().coords((0.0,0.0,1.0)),0,0),BaoNode(Circle().coords((2.0,0.0,1.0)),1,1)]

class BaoStack:
    
    def __init__(self,lastnode,lastlastnode):
        self.mlastnode     = lastnode
        self.mlastlastnode = lastlastnode
        self.mothernode    = lastlastnode
        self.mlast3node    = None

    def set(self,nodes,lastindex):
        self.mlastnode     = nodes[lastindex]
        self.mlastlastnode = nodes[lastindex-1]
        self.mothernode    = None
        self.mlast3node    = None

    def context(self):
        return (self.mlastnode,self.mlastlastnode,self.mlast3node,self.mothernode)

    def rotate(self,newnode,othernode):
        self.mlast3node    = self.mlastlastnode
        self.mlastlastnode = self.mlastnode
        self.mlastnode     = newnode
        self.mothernode    = othernode

    def lastnodes(self):
        return [self.mlastnode,self.mlastlastnode,self.mlast3node]
    
    def seed(self):
        return (self.mlastnode,self.mothernode)

class CirclePackingBao:
    

    @staticmethod
    def computenextnode(quadtree,node2,node1,newr,index):
        allsides = [1.0,-1.0]
        for iside in allsides:
            newcircle = nextadjcircle(node2,node1,newr,iside)
            if not newcircle == None and not quadtree.iscolliding(newcircle):
                newbaonode = BaoNode(newcircle,node2.colorindex() + 1,index + 1)
                return newbaonode
        return None

    @staticmethod
    def findlastfreenode(nodes,lastindex):
        freenode = nodes[lastindex]
        while ((freenode.retouch() or freenode.notfound()) and lastindex > 0):
            lastindex = lastindex - 1
            freenode = nodes[lastindex]
        return (freenode,lastindex)

    @staticmethod
    def findnewother(quadtree,lastnode,excludenodes,newr):
        bigcircle   = lastnode.scale( (lastnode.r() + newr * 2.1)/ lastnode.r() )
        collidings  = quadtree.colliding(bigcircle)
        ccollidings = lsubstract(collidings,excludenodes)
        sortlist = [(n.index,n) for n in ccollidings]
        sortlist.sort()
        return [item[1] for item in sortlist]


    @staticmethod
    def iter(boundaries,inodes,baopattern,niter):
        nodes       = BaoNode.nodes(inodes,0)
        boundaries  = BaoNode.nodes(boundaries)        
        stack       = BaoStack(nodes[-1],nodes[-2])
        lastindex   = 1
        quadtree    = QuadTree().adds( boundaries + nodes )
        
        for iiter in range(niter):
            ifputs(iiter % 1000 == 0,"niter",iiter)

            # get current paramaters
            (lastnode,othernode) = stack.seed()
            newr                 = baopattern.next().radius()

            # compute new node if possible
            newbaonode = None

            if not othernode == None:
                newbaonode = CirclePackingBao.computenextnode(quadtree,lastnode,othernode,newr,len(nodes))

            if newbaonode == None:
                ccollidings = CirclePackingBao.findnewother(quadtree,lastnode,(stack.lastnodes() + [othernode]),newr)
                    
                for othernode in ccollidings:
                    newbaonode = CirclePackingBao.computenextnode(quadtree,lastnode,othernode,newr,len(nodes))
                    if not newbaonode == None:
                        break

            # update according to result
            if newbaonode == None:
                lastnode.notfound(True)
                (freenode,lastindex) = CirclePackingBao.findlastfreenode(nodes,lastindex)
                stack.set(nodes,lastindex)
            else:
                othernode.retouch(True)
                quadtree.add(newbaonode)
                nodes.append(newbaonode)
                baopattern.draw(newbaonode,lastindex)
                lastindex = len(nodes)-1
                stack.rotate(newbaonode,othernode)

            if lastindex < 1:
                break
            
        return nodes
