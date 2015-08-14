from utils         import *
from drawutils     import *
from geoutils      import *
from tangentutils  import *
from quadtree      import *
from circleadj     import *
from circlepacking import *

def index2color(period,index):
    return color.hue2color((index%period)/(float(period)))


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

class CirclePackingBaoSwitch:
    
    def __init__(self,sides,nradiuss,inodes,fdraw):
        self.lastindex = 1
        self.nodes    = inodes
        self.sides    = sides
        self.nradiuss = nradiuss
        
        cindex = 0
        for node in self.nodes:
            node.index = 0
            node.retouch = False
            node.notfound = False
            node.colorindex = cindex
            cindex += 1

        self.mlastnode  = self.nodes[1]
        self.othernode = self.nodes[0]
        self.lastlastnode = self.nodes[0]
        self.last3node = ""

        self.fdraw = fdraw
        self.collisionmargin = 0.0001

    def sortdist(self,anode):
        def result(a,b):
            return (dist2(a,anode) - dist2(b,anode));
        return result

    def computenextnode(self,quadtree,node1,node2,newr,side):
        circle = circles2tangent(node1,"OUT",node2,"OUT",newr,side)
        if circle == None:
            return None
        else:
            return circle

    def lastnode(self):
        return self.nodes[-1]

    def iter(self,render,boundaries,nsubiter):
        maxnsubiter = nsubiter
        lastindex = self.lastindex
        nodes     = self.nodes
        sides     = self.sides
        nradiuss  = self.nradiuss
        result    = [] 
        quadtree = QuadTree()
        quadtree.adds(boundaries)
        
        for isubiter in range(maxnsubiter):
            if isubiter > 0 and isubiter % 1000 == 0:
                puts("niter",isubiter)

            if lastindex > 1 or len(self.nodes) == 2:
                lastnode     = self.mlastnode
                othernode    = self.othernode
                lastlastnode = self.lastlastnode
                last3node    = self.last3node
        
                newr = lcircular(nradiuss,lastindex)
                
                bigr    = lastnode.r() + newr * 2.1
                bignode = lastnode.scale(bigr)
                side    = lcircular(sides,len(nodes))
                lastside = lcircular(sides,len(nodes)-1)

                found = False
                incrradiusfactor = 1.0

                if side != lastside or lastindex == 1:
                    othernode = lastlastnode
                
                if othernode != "":
                    allsides = [side,-side]
                    for iside in allsides:
                        # puts("circles2tangent1")
                        newnode = self.computenextnode(quadtree,lastnode,othernode,newr,iside)
                        
                        if newnode != None:
                            if not quadtree.iscolliding(newnode):
                                # puts("newnode added1",newnode.list())
                                nodes.append(newnode)
                                newnode.retouch  = False
                                newnode.notfound = False
                                newnode.index    = len(nodes)
                                newnode.colorindex = lastnode.colorindex + 1
                                
                                self.nodes = nodes
                                self.last3node = self.lastlastnode
                                self.lastlastnode = self.mlastnode
                                self.mlastnode = newnode
                                self.othernode = othernode
                                
                                self.othernode.retouch = True
                                
                                quadtree.add(newnode)

                                self.fdraw(render,self,lastindex)

                                found = True
                                result.append(newnode)
                                break

                
                if found == False:
                    fsort = self.sortdist(lastnode)
                    ccollidings = lsubstract(quadtree.colliding(bignode),[lastlastnode,last3node])
                    # TODO: sort accodring to fsort
                    
                    for ccolliding in ccollidings:
                        if not lastnode == ccolliding:
                            allsides = [side,-side]
                            for iside in allsides:
                                # puts("circles2tangent2")
                                newnode = self.computenextnode(quadtree,lastnode,ccolliding,newr,iside)
                                # puts("newnode2",newnode,"newr",newr,"lastnode",lastnode.list(),"ccolliding",ccolliding)
                                if newnode != None:
                                    if not quadtree.iscolliding(newnode):
                                        # puts("newnode added2",newnode.list())
                                        newnode.retouch = False
                                        newnode.notfound = False
                                        newnode.index = len(nodes)
                                        newnode.colorindex = lastnode.colorindex + 1
                                        nodes.append(newnode)
                                        
                                        self.nodes = nodes
                                        self.last3node = self.lastlastnode
                                        self.lastlastnode = self.mlastnode
                                        self.mlastnode = newnode
                                        self.othernode = ccolliding
                                        
                                        self.othernode.retouch = True

                                        quadtree.add(newnode)

                                        self.fdraw(render,self,lastindex)

                                        found = True
                                        result.append(newnode)
                                        break
                        if found:
                            break
                        
                if not found:
                    freenode = nodes[lastindex]
                    freenode.notfound = True
                    while ((freenode.retouch or freenode.notfound) and lastindex > 0):
                        lastindex = lastindex - 1
                        freenode = nodes[lastindex]
                    
                    self.mlastnode = nodes[lastindex]
                    self.lastlastnode = nodes[lastindex-1]
                    self.othernode = ""
                else:
                    lastindex = len(nodes)-1
                self.lastindex = lastindex
            
            if self.lastindex < 2:
                # puts("no more iteration")
                break
        
        return result
