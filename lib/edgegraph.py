from geoutils import *

#
# class to build edges graph (linked by points)
# 
#

class Edge:

    def __init__(self,p1,p2):
        self.mp1    = p1
        self.mp2    = p2
        self.mprevs = []
        self.mnexts = []
        self.marc    = None

    def arc(self,v=None):
        if v == None:
            return self.marc
        else:
            self.marc = v
            return self

    def p1(self):
        return self.mp1

    def p2(self):
        return self.mp2
    
    def add_prev(self,prevedge):
        self.mprevs.append(prevedge)
        return self

    def add_next(self,nextedge):
        self.mnexts.append(nextedge)
        return self

    def remove_prev(self,prevedge):
        if prevedge in self.mprevs:
            self.mprevs.remove(prevedge)
        return self

    def remove_next(self,nextedge):
        if nextedge in self.mnexts:
            self.mnexts.remove(nextedge)
        return self        

    def nexts(self):
        return self.mnexts

    def prevs(self):
        return self.mprevs

    def bbox(self):
        return points2bbox([self.p1(),self.p2()])

    def coords(self):
        return self.p1().coords() + self.p2().coords()

    def intersection(self,oedge):
        return raw_intersection(self.p1(),self.p2(),oedge.p1(),oedge.p2())

    @staticmethod
    def addadj(edge1,edge2):
        edge1.add_next(edge2)
        edge2.add_prev(edge1)

class Arc:
    def __init__(self,edges):
        self.medges = edges
        self.mprevs = []
        self.mnexts = []
        for edge in self.medges:
            edge.arc(self)

    def edges(self):
        return self.medges

class EdgeGraph:

    def __init__(self):
        self.medges = []
        self.marcs  = []

    def edges(self):
        return self.medges

    def edge(self,index):
        return self.medges[index]

    def add(self,edge):
        self.medges.append(edge)
        return self

    def remove(self,edge):
        self.medges.remove(edge)
        for prevedge in edge.prevs():
            prevedge.remove_next(edge)
        for nextedge in edge.nexts():
            nextedge.remove_prev(edge)
        return self
    
    def loadwithpointsequence(self,points):
        if len(points) < 2:
            return self
        firstedge = Edge(points[0],points[1])
        self.add(firstedge)
        prevedge = firstedge
        for (p1,p2) in pairs(points[1:]):
            newedge = Edge(p1,p2)
            Edge.addadj(prevedge,newedge)
            self.add(newedge)
            prevedge = newedge
        if prevedge.p2() == firstedge.p1():
            Edge.addadj(prevedge,firstedge)
        return self

    def loadwithpointpairs(self,pointpairs):
        # first unify points
        points = {}
        for (p1,p2) in pointpairs:
            for p in [p1,p2]:
                if not p.coords() in points:
                    points[p.coords()] = p

        # created edges
        newedges = []
        for (p1,p2) in pointpairs:
            newp1 = points[p1.coords()]
            newp2 = points[p2.coords()]
            newedge = Edge(newp1,newp2)
            newedges.append(newedge)
    
        # build adjacency
        edgestart = {}
        for newedge in newedges:
            p1 = newedge.p1()
            p2 = newedge.p2()
            if not p1 in edgestart:
                edgestart[p1] = []
            edgestart[p1].append(newedge)

        # build newdeges adjs
        for newedge in newedges:
            p1 = newedge.p1()
            if p2 in edgestart:
                for nextedge in edgestart[p2]:
                    Edge.addadj(newedge,nextedge)

        # TODO: check adjacency with preexisting edges too !
        self.medges.extend(newedges)
        return self

    #
    # compute arcs from edges
    # an arc is a string of edges without bifurcation                
    #
    # algo:                 
    def arcs(self):
        self.computearcs()
        return self.marcs


    def computearcs(self):
        for edge in self.medges:
            if edge.arc() == None:
                # first find the beginning of the arc (warning: can be a cycle)
                edge0 = edge
                cedge = edge
                while True:
                    if len(cedge.prevs()) == 1:
                        cedge = cedge.prevs()[0]
                        if cedge == edge:
                            edge0 = edge
                            break
                    else:
                        edge0 = cedge
                        break
                puts("edge",edge.coords(),"edge0",edge0.coords())

                # then compute the sequence of nexts
                newarcedges = [edge0]
                cedge       =  edge0
                while True:
                    puts("cedge",cedge.coords(),"len(cedge.nexts())",len(cedge.nexts()))
                    if len(cedge.nexts()) == 1 and not cedge.nexts()[0] == edge0:
                        cedge = cedge.nexts()[0]
                        newarcedges.append(cedge)
                    else:
                        break

                # then create the new arc
                puts("new arc nedges",len(newarcedges))
                self.marcs.append(Arc(newarcedges))


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
