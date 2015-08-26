from geoutils   import *
from geomatcher import *

#
# class to build edges graph (linked by points)
# 
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

    def vector(self):
        return Vector(self.point1(),self.poin2())

    def othernode(self,node):
        if node == self.node1():
            return self.node2()
        elif node == self.node2():
            return self.node1()
        return None
    
    def bbox(self):
        return points2bbox([self.point1(),self.point1()])

    def coords(self):
        return self.point1().coords() + self.point2().coords()

    def intersection(self,oedge):
        return raw_intersection(self.point1(),self.point2(),oedge.point1(),oedge.point2())

class PointNode:
    def __init__(self,point):
        self.mp     = point
        self.mnextedges = []
        self.mprevedges = []
        
    def p(self):
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
# Arc is oriented from first point to last point
#

class Arc:
    def __init__(self,edges):
        self.medges = edges
        self.mnext  = None
        for edge in self.medges:
            edge.arc(self)

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

    def points(self):
        return [self.point1()] + [edge.node2().p() for edge in self.medges[1:]]

class EdgeGraph:

    def __init__(self):
        self.mnodes = []
        self.medges = []
        self.marcs  = []

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

    #
    # TODO: optimize by making a map
    #
    def nodes2edge(self,node1,node2):
        for edge in self.medges:
            if (edge.node1() == node1 and edge.node2() == node2):
                return edge
        return None

    def createedges(self,p1,p2):
        edge12 = Edge(p1,p2)
        edge21 = Edge(p2,p1)

        edge12.opposite(edge21)
        edge21.opposite(edge12)
        
        p1.add_nextedge(edge12)
        p1.add_prevedge(edge21)
        
        p2.add_nextedge(edge21)
        p2.add_prevedge(edge12)
        
        self.add_edge(edge12)
        self.add_edge(edge21)
        return self

    
    def loadwithpointsequence(self,points):
        if len(points) < 1:
            return self
        pointpairs = GeoMatcher().checksegments([(p1,p2) for (p1,p2) in pairs(points)])

        firstnode = None
        for (p1,p2) in pointpairs:
            if firstnode == None:
                firstnode = PointNode(p1)
                self.add_node(firstnode)
                prevnode = firstnode
            if p2 == firstnode.p():
                self.createedges(prevnode,firstnode)
            else:
                newnode = PointNode(p2)
                self.createedges(prevnode,newnode)
                self.add_node(newnode)
                prevnode = newnode
        return self
    
    def loadwithpointpairs(self,pointpairs):
        # manage float problems and unify same points
        pointpairs = GeoMatcher().checksegments(pointpairs)

        # build adjacency and nodes
        nodes = {}
        for (p1,p2) in pointpairs:
            for p in [p1,p2]:
                if not p in nodes:
                    nodes[p] = PointNode(p)
                    self.add_node(nodes[p])

            self.createedges(nodes[p1],nodes[p2])

        # TODO: check adjacency with preexisting edges too !
        return self

    #
    # compute arcs from edges
    # an arc is a string of edges without bifurcation, oriented                
    #
    # algo:                 
    def arcs(self):
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
        for edge in self.medges:
            if edge.arc() == None:
                arcedges = self._computeedgearc(edge)
                self.marcs.append(Arc(arcedges))
        return self

    #
    # explore the arc graph from arc and get all paths going back to arc
    #
    def computearccycle(self,arcgraph,arc0):
        result = [arc0]
        carc   = arc0
        while True:
            if arcgraph[carc] == None:
                return None
            else:
                carc = arcgraph[carc]
                if carc == arc0:
                    return result
                else:
                    result.append(carc)
        return result

    #
    # compute a graph with arc oriented, and with the next arc the righest
    #
    #
    def computearcgraph(self):
        #
        # first compute the graph node => arc
        #
        nodearcs = {}
        for arc in self.marcs:
            for node in arc.extremities():
                if not node in nodearcs:
                    nodearcs[node] = []
            node1 = arc.node1()
            nodearcs[node1].append(arc)

        #
        # then for each arc, compute the most right next arc
        #
        arcgraph = {}    
        for arc in self.marcs:
            nextarcs = nodearcs[arc.p2()]
            sortlist = [(arc.lastvector().normalize().cross(nextarc.firstvector().normalize()),nextarc)]
            sortlist.sort()
            if len(sortlist) == 0:
                argraph[arc] = None
            else:
                argraph[arc] = sortlist[0][1]

        return arcgraph

    #
    # compute all the arc cycles (minimal) of a arcs
    #
    def computearccycles(self):
        arcgraph = self.computearcgraph()

        for arc in arcnodegraph.keys():
            if not arc in touched:
                arccycle = self.computearccycle(arcgraph,arc)
                if not arccycle == None:
                    result.append(arccycle)
                    touched.extend(arccycle)
        return result


    def arccycle2polygon(self,arccycle):
        result = []
        for arc in arccycle:
            points = arc.points()
            if len(result) == 0:
                result = points
            else:
                result.extend(points[1:])
        return result
                
    #
    # a closed polygon is a cycle in the arc graph
    # 
    #
    def closedpolygons(self):
        touched = []
        result  = []

        arccycles = self.computearccycles()
        result = [self.arccycle2polygon(arccycle) for arccycle in arccycles]
        return result
            



    # def managedEdgeIntersectionPoint(self,edge1,edge2,inter):
    #     newedge11 = Edge(edge1.p1(),inter)
    #     newedge12 = Edge(inter,edge1.p2())
        
    #     newedge21 = Edge(edge2.p1(),inter)
    #     newedge22 = Edge(inter,edge2.p2())
        
    #     prevedges1 = edge1.prevs()
    #     nextedges1 = edge1.nexts()
        
    #     prevedges2 = edge2.prevs()
    #     nextedges2 = edge2.nexts()
        
    #     for prevedge1 in prevedges1:
    #         prevedge1.remove_next(edge1)
    #         prevedge1.add_next(newedge11)
    #     for nextedge1 in nextedges1:
    #         nextedge1.remove_prev(edge1)
    #         nextedge1.add_prev(newedge12)
                            
    #     prevedges2 = edge2.prevs()
    #     nextedges2 = edge2.nexts()
    #     for prevedge2 in prevedges2:
    #         prevedge2.remove_next(edge2)
    #         prevedge2.add_next(newedge21)
    #     for nextedge2 in nextedges2:
    #         nextedge2.remove_prev(edge2)
    #         nextedge2.add_prev(newedge22)
                        
    #     Edge.addadj(newedge11,newedge12)
    #     Edge.addadj(newedge11,newedge22)
        
    #     Edge.addadj(newedge21,newedge22)
    #     Edge.addadj(newedge21,newedge12)

    #     self.remove(edge1)
    #     self.remove(edge2)
        
    #     self.add(newedge11)
    #     self.add(newedge12)
    #     self.add(newedge21)
    #     self.add(newedge22)

    #     return ((newedge11,newedge12),(newedge21,newedge22))
        

    #
    # compute non interesecting edge graph, by splitting intersecting edges 
    #
    # Algo: 
    # - order edges by x abscissa
    # - iterate the items in the ordered list:
    #   - if item is stop, remove the edge from the stack
    #   - if item is start, add edge to the stack
    #      and check if intersection:
    #      - if intersection, create the new edges, and refresh the adjacent edges
    #
    # def cutedges(self):
        # sortlist = []
        # for edge in self.medges:
        #     # TODO: to improve: 1,2 to have stop after start for vertical segments
        #     sortlist.append((edge.p1().x(),edge,1))
        #     sortlist.append((edge.p2().x(),edge,2))
        # sortlist.sort()

        # stack = []
        # alias = {}
        # for item in sortlist:
        #     (dum,edge,isstart) = item
        #     puts("stack",[cedge.coords() for cedge in stack])
        #     if isstart == 1:
        #         alias[edge] = edge
        #         newstack = []
        #         for stackedge in stack:
        #             inter = edge.intersection(stackedge)
        #             puts("edge",edge.coords(),"stackedge",stackedge.coords(),"inter",inter)
        #             if not inter == None:
        #                 if isinstance(inter,Point):
        #                     (newedges,newstackedges) = self.managedEdgeIntersectionPoint(edge,stackedge,inter)
        #                     newedge      = iff(newedges[0].p1().x() > newedges[1].p1().x(), newedges[0],newedges[1])
        #                     newstackedge = iff(newstackedges[0].p1().x() > newstackedges[1].p1().x(), newstackedges[0],newstackedges[1])
                             
        #                     alias[edge]      = newedge
        #                     alias[stackedge] = newstackedge
                            

        #             else:
        #                 stack.append(edge)

        #     else:
        #         stack = lremove(stack,edge)
