from geoutils   import *
from geomatcher import *
from polygon    import *

#
# class to build edges graph (linked by pointnodes)
#  - an edge is oriented (ie reversing the nodes give the opposite edge)
#  - an edge belongs to one and only one arc
#
class Edge:

    def __init__(self,node1,node2):
        self.mnode1    = node1
        self.mnode2    = node2
        self.marc      = None
        self.mopposite = None


    def opposite(self,v=None):
        if v == None:
            return self.mopposite
        else:
            self.mopposite = v
            return self

    def arc(self,v=None):
        if v == None:
            return self.marc
        else:
            self.marc = v
            return self

    def node1(self):
        return self.mnode1

    def node2(self):
        return self.mnode2

    def point1(self):
        return self.node1().p()

    def point2(self):
        return self.node2().p()

    def nodes(self):
        return [self.node1(),self.node2()]

    def points(self):
        return [self.point1(),self.point2()]

    def vector(self):
        return vector(self.point1(),self.point2())

    def othernode(self,node):
        if node == self.node1():
            return self.node2()
        elif node == self.node2():
            return self.node1()
        return None
    
    def bbox(self):
        return points2bbox([self.point1(),self.point2()])

    def coords(self):
        return self.point1().coords() + self.point2().coords()

    def intersection(self,oedge):
        return raw_intersection(self.point1(),self.point2(),oedge.point1(),oedge.point2())

#
# nodes of edgegraph
#
class PointNode:
    def __init__(self,point):
        self.mp     = point
        self.mnextedges = []
        self.mprevedges = []
        
    def p(self):
        return self.mp

    def point(self):
        return self.mp

    def coords(self):
        return self.p().coords()

    def nextedges(self):
        return self.mnextedges

    def add_nextedge(self,edge):
        self.mnextedges.append(edge)

    def remove_nextedge(self,edge):
        if edge in self.mnextedges:
            self.mnextedges.remove(edge)

    def prevedges(self):
        return self.mprevedges

    def add_prevedge(self,edge):
        self.mprevedges.append(edge)

    def remove_prevedge(self,edge):
        if edge in self.mprevedges:
            self.mprevedges.remove(edge)

#
# An arc is a sequence of edges with no bifurcation
# And arc is oriented from first point to last point
# An arc is at most part of one arccycle
#
class Arc:
    def __init__(self,edges):
        self.medges    = edges
        self.mnext     = None
        self.mopposite = None
        for edge in self.medges:
            edge.arc(self)
        self.marccycle = None
        self.mpolygon  = None

    def edges(self):
        return self.medges

    def next(self,next=None):
        if next == None:
            return self.mnext
        else:
            self.mnext = next
            return self

    def firstvector(self):
        return self.medges[0].vector()

    def lastvector(self):
        return self.medges[-1].vector()

    def edge1(self):
        return self.medges[0]

    def edge2(self):
        return self.medges[-1]
    
    def node1(self):
        return self.edge1().node1()

    def node2(self):
        return self.edge2().node2()

    def extremities(self):
        return (self.node1(),self.node2())

    def point1(self):
        return self.node1().p()

    def point2(self):
        return self.node2().p()

    def points(self):
        return [self.point1()] + [edge.point2() for edge in self.medges]
    
    def opposite(self,v=None):
        if v == None:
            return self.mopposite
        else:
            self.mopposite = v
            return self

    def coords(self):
        return [p.coords() for p in self.points()]

    def arccycle(self, v = None):
        if v == None:
            return self.marccycle
        else:
            self.marccycle = v
            return self

    def aggx(self):
        return self.point1().x() + self.point2().x()

    def polygon(self):
        if self.mpolygon == None:
            self.mpolygon = Polygon(self.points())
        return self.mpolygon

    def length(self):
        return sum([vector(p1,p2).length() for (p1,p2) in pairs(self.points())])

    def pointextremities(self):
        return (self.point1(),self.point2())

#
# An arccycle is a right oriented cycle of arcs
# An arc can be at most part of one arccycle
# Arccycles are adjacent if they share at least one opposite arc
#
class ArcCycle:

    def __init__(self,arcs):
        self.marcs = arcs
        self.madjs = []
        for arc in self.marcs:
            arc.arccycle(self)

    def arcs(self):
        return self.marcs

    # list of points
    # first point = last point by definition
    def points(self):
        result = []
        for arc in self.marcs:
            points = arc.points()
            if len(result) == 0:
                result = points
            else:
                result.extend(points[1:])
        return result
        
    #
    # return the list of (arc,adjarccycle) 
    #
    def adjs(self):
        result = []
        for arc in self.marcs:
            result.append((arc,arc.opposite().arccycle()))

    #
    # return the list of adj arccycles (not duplicated)
    #
    def adjcycles(self):
        return lremove(lunique([item[1] for item in self.adjs()]),None)

    #
    # 
    #
    def isClockwise(self):
        return Polygon(self.points()).isClockwise()
        
#
# an edge graph is a structure to compute closed polygons from a set of segments  
#
class EdgeGraph:

    def __init__(self):
        self.mnodes     = []
        self.medges     = []
        self.marcs      = None
        self.marccycles = None

    def nodes(self):
        return self.mnodes

    def node(self,index):
        return self.mnodes[index]

    def add_node(self,node):
        self.mnodes.append(node)
        return self

    def edges(self):
        return self.medges

    def add_edge(self,edge):
        self.medges.append(edge)

    def createedges(self,n1,n2):
        edge12 = Edge(n1,n2)
        edge21 = Edge(n2,n1)

        edge12.opposite(edge21)
        edge21.opposite(edge12)
        
        n1.add_nextedge(edge12)
        n1.add_prevedge(edge21)
        
        n2.add_nextedge(edge21)
        n2.add_prevedge(edge12)
        
        self.add_edge(edge12)
        self.add_edge(edge21)
        return self

    def arccycles(self):
        if self.marccycles == None:
            self.computearccycles()
        return self.marccycles

    def add_arccycle(self,arccycle):
        self.marccycles.append(arccycle)

    def clockwise_arccycles(self):
        return [arccycle for arccycle in self.arccycles() if arccycle.isClockwise()]

    #
    # load a sequence of points
    #
    def loadwithpointsequence(self,points):
        if len(points) < 1:
            return self

        segments = [Segment(p1,p2) for (p1,p2) in pairs(points)]

        firstnode = None
        for seg in segments:
            if firstnode == None:
                firstnode = PointNode(seg.p1())
                self.add_node(firstnode)
                prevnode = firstnode
            if seg.p2() == firstnode.p():
                self.createedges(prevnode,firstnode)
            else:
                newnode = PointNode(seg.p2())
                self.createedges(prevnode,newnode)
                self.add_node(newnode)
                prevnode = newnode
        return self

    #
    # load a set of segments (with no particular order)
    #
    def loadwithsegments(self,segments_):
        # manage float problems and unify same points
        segments = GeoMatcher().checksegments(segments_)

        # build adjacency and nodes
        nodes = {}
        for seg in segments:
            for p in seg.points():
                if not p in nodes:
                    nodes[p] = PointNode(p)
                    self.add_node(nodes[p])

            (p1,p2) = seg.points()
            self.createedges(nodes[p1],nodes[p2])

        # TODO: check adjacency with preexisting edges too !
        return self

    #
    # get arcs of the edgegraph
    #
    def arcs(self):
        if self.marcs == None:
            self._computearcs()
        return self.marcs

    #
    # explore each node graph up to a point with more than 2 nexts (or no more next)
    # each edge has one and only one arc
    # WARNING: TODO: do not compute fot the moment the merge of arcs (ie if some edges have already been computed with arcs)
    #
    def _computeedgearc(self,edge):
        # puts("computeedgearc",edge.coords())
        
        # first find origin or arc, ie point with more or less than one prevedge
        node0    = edge.node1()
        onode    = node0
        prevedge = edge
        while True:
            prevedges = lremove(onode.prevedges(),prevedge.opposite())
            # puts("onode",onode.p().coords(),"prevedges",[edge.coords() for edge in prevedges])
            if len(prevedges) == 1:
                prevedge = prevedges[0]
                onode    = prevedge.node1()
                if onode == node0: # to deal with circular arcs
                    edge0 = prevedge
                    break
            else:
                edge0 = prevedge
                break

        # here onode is origin of arc, so just run amon the nextedges
        # puts("node0",onode.p().coords())
        arcedges = [edge0]
        cnode    = edge0.node2()
        while True:
            nextedges = lremove(cnode.nextedges(),arcedges[-1].opposite())
            # puts("cnode",cnode.p().coords(),"nextedges",[edge.coords() for edge in nextedges])
            if len(nextedges) == 1:
                nextedge = nextedges[0]
                arcedges.append(nextedge)
                cnode     = nextedge.node2()
                if cnode == onode: # to deal with circular arcs
                    break
            else:
                break

        return arcedges 

    #
    # compute all the arcs contained in the edge graph
    #
    def _computearcs(self):
        self.marcs = []
        for edge in self.medges:
            if edge.arc() == None:
                arcedges = self._computeedgearc(edge)
                newarc1 = Arc(arcedges)
                newarc2 = Arc(lreverse([edge.opposite() for edge in arcedges]))
                
                newarc1.opposite(newarc2)
                newarc2.opposite(newarc1)

                self.marcs.append(newarc1)
                self.marcs.append(newarc2)
        return self

    #
    # return for each node the number of arcs after (for debug purpose)
    #
    def nodenarcs(self):
        nodearcs = {}
        for arc in self.arcs():
            for node in arc.extremities():
                if not node in nodearcs:
                    nodearcs[node] = []
            node1 = arc.node1()
            nodearcs[node1].append(arc)

        return [(node,nodearcs[node]) for node in nodearcs.keys()]
        

    #
    # explore the arc graph from arc and get all paths going back to arc
    #
    def computecyclearcs(self,arcgraph,arc0):
        result = [arc0]
        carc   = arc0
        while True:
            #puts("carc",carc.coords())
            if arcgraph[carc] == None:
                return None
            else:
                newarc = arcgraph[carc]
                if newarc == arc0:
                    return result
                if newarc.opposite() in result:
                    return None
                    #newnewarc = arcgraph[newarc]
                    #result = lstop(result,newarc.opposite())
                    #newarc = newnewarc
                elif newarc in result:
                    return None
                else:
                    result.append(newarc)
                    carc= newarc
        return result

    #
    # from the computed arcs, remove the one that are not inside a cycle
    # TODO: to generalize with subtrees not in cycles
    #
    def prunearcs(self):
        nodearcs = {}
        for arc in self.arcs():
            for node in arc.extremities():
                if not node in nodearcs:
                    nodearcs[node] = []
            node1 = arc.node1()
            nodearcs[node1].append(arc)

        prunearcs = []
        for arc in self.arcs():
            if not (len(nodearcs[arc.node2()]) == 1 or len(nodearcs[arc.opposite().node2()]) == 1): # only the opposite
                prunearcs.append(arc)
        return prunearcs
        # puts("arcs",len(self.arcs()),"prunearcs",len(prunearcs))


    #
    # compute a graph with arc oriented, and with the next arc the righest
    # TODO: refactor as not resilient with trees pruning
    #
    def computearcgraph(self):
        # first compute the graph node => arc

        #
        prunearcs = self.prunearcs()
        nodearcs = {}
        for arc in prunearcs:
            for node in arc.extremities():
                if not node in nodearcs:
                    nodearcs[node] = []
            node1 = arc.node1()
            nodearcs[node1].append(arc)
                

        #
        # then for each arc, compute the most right next arc
        #
        arcgraph = {}    
        for arc in prunearcs:
            #puts("compute most right next arc for arc",arc.coords())
            nextarcs = nodearcs[arc.node2()]
            # if len(nextarcs) > 1:
            nextarcs = lremove(nextarcs,arc.opposite())
            #puts("compute most right next arc for arc",arc.coords(),"nextarcs",[nextarc.coords() for nextarc in nextarcs])
            # sortlist = [(arc.lastvector().normalize().cross(nextarc.firstvector().normalize()),nextarc) for nextarc in nextarcs]
            sortlist = [(vsanglepos(arc.lastvector(),nextarc.firstvector()),nextarc) for nextarc in nextarcs]
            sortlist.sort()
            sortlist.reverse()
            #puts("arc",arc.coords(),"sortlist",[(anglepos,carc.coords()) for (anglepos,carc) in sortlist])
            if len(sortlist) == 0:
                #puts("compute most right next arc for arc",arc.coords(),"None")
                arcgraph[arc] = None
            else:
                arcgraph[arc] = sortlist[0][1]
                #puts("compute most right next arc for arc",arc.coords(),"next",arcgraph[arc].coords())
        return arcgraph


    #
    # compute all the arc cycles (minimal) of a arcs
    #
    def computearccycles(self):
        self.marccycles = []
        arcgraph = self.computearcgraph()
        
        for arc in arcgraph.keys():
            if arc.arccycle() == None:
                arcs = self.computecyclearcs(arcgraph,arc)
                if not arcs == None:
                    self.add_arccycle(ArcCycle(arcs))
        return self.marccycles
            
    def polygons(self):
        return [Polygon(arccycle.points()) for arccycle in self.arccycles()]

