from geoutils   import *
from geomatcher import *

#
# class to build edges graph (linked by points)
# 
#

class Edge:

    def __init__(self,node1,node2):
        self.mnode1   = node1
        self.mnode2   = node2
        self.marc     = None

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

    def nodes(self):
        return [self.node1(),self.node2()]

    def othernode(self,node):
        if node == self.node1():
            return self.node2()
        elif node == self.node2():
            return self.node1()
        return None
    
    def bbox(self):
        return points2bbox([self.node1().p(),self.node2().p()])

    def coords(self):
        return self.node1().p().coords() + self.node2().p().coords()

    def intersection(self,oedge):
        return raw_intersection(self.node1().p(),self.node2().p(),oedge.node1().p(),oedge.node2().p())

class PointNode:
    def __init__(self,point):
        self.mp     = point
        self.mnexts = []

    def p(self):
        return self.mp

    def nexts(self):
        return self.mnexts

    def add_next(self,p):
        self.mnexts.append(p)

    def remove_next(self,p):
        if p in self.mnexts:
            self.mnexts.remove(p)

    @staticmethod
    def addadj(node1,node2):
        node1.add_next(node2)
        node2.add_next(node1)


class Arc:
    def __init__(self,edges):
        self.medges = edges
        for edge in self.medges:
            edge.arc(self)

    def edges(self):
        return self.medges

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

    def remove_node(self,node):
        self.mnodes.remove(node)
        for onode in node.nexts():
            onode.remove_next(node)
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
            if (edge.node1() == node1 and edge.node2() == node2) or (edge.node2() == node1 and edge.node1() == node2):
                return edge
        return None
    
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
                PointNode.addadj(prevnode,firstnode)
                self.add_edge(Edge(prevnode,firstnode))
            else:
                newnode = PointNode(p2)
                PointNode.addadj(prevnode,newnode)
                self.add_edge(Edge(prevnode,newnode))
                self.add_node(newnode)
                prevnode = newnode
        return self
    
    def loadwithpointpairs(self,pointpairs):
        # manage float problems and unify same points
        pointpairs = GeoMatcher().checksegments(pointpairs)

        # build adjacency and nodes
        pnode = {}
        adj   = {}
        for (p1,p2) in pointpairs:
            for p in [p1,p2]:
                if not p in pnode:
                    pnode[p] = PointNode(p)
                    self.add_node(pnode[p])
                if not pnode[p] in adj:
                    adj[pnode[p]] = []
            
            PointNode.addadj(pnode[p1],pnode[p2])            
            self.add_edge(Edge(pnode[p1],pnode[p2]))

        # TODO: check adjacency with preexisting edges too !
        return self

    #
    # compute arcs from edges
    # an arc is a string of edges without bifurcation                
    #
    # algo:                 
    def arcs(self):
        self.computearcs()
        return self.marcs

    #
    # explore each node graph up to a point with more than 2 nexts (or no more next)
    # WARNING: TODO: do not compute fot the moment the merge of arcs (ie if some edges have already been computed with arcs)
    #
    def computeedgearc(self,edge):
        semiarcs = []
        for node in edge.nodes():
            semiarc  = []
            prevnode = edge.othernode(node)
            nodes    = [node]
            while True:
                cnode = nodes[-1]
                if len(cnode.nexts()) == 0:
                    puts("Error: single node",cnode.p().coords())
                    break
                else:
                    nexts = lremove(cnode.nexts(),prevnode)
                    if len(nexts) == 0:
                        break
                    elif len(nexts) == 1:
                        nextnode = nexts[0]
                        semiarc.append(self.nodes2edge(cnode,nextnode))
                        if nextnode in nodes:
                            # circular arc
                            break
                        else:
                            prevnode = cnode
                            nodes.append(nextnode)
                    else:
                        # bifurcation: break
                        break
            semiarcs.append(semiarc)
        return lreverse(semiarcs[0]) + [edge] + semiarcs[1]


    def computearcs(self):
        for edge in self.medges:
            if edge.arc() == None:
                arcedges = self.computeedgearc(edge)
                self.marcs.append(Arc(arcedges))
        return self


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
