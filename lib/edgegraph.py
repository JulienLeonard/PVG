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
        self.mprevs.remove(prevedge)
        return self

    def remove_next(self,nextedge):
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

    @staticmethod
    def addadj(edge1,edge2):
        edge1.add_next(edge2)
        edge2.add_prev(edge1)

class EdgeGraph:

    def __init__(self):
        self.medges = []

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
    
    def loadwithpoints(self,points):
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
    def cutedges(self):
        # sortlist = []
        # for edge in self.medges:
        #     sortlist.append((edge.p1().x(),edge,True))
        #     sortlist.append((edge.p2().x(),edge,False))
        # sortlist.sort()

        # stack = []
        # alias = {}
        # for item in sortlist:
        #     if 
        
        for i in range(len(self.medges)):
            for j in range(i,len(self.medges)):
                inter = self.medges[i].intersection(self.medges[j])
                if not inter == None:
                    if isinstance(inter,Point):
                        edge1 = self.medges[i]
                        edge2 = self.medges[j]
                        
                        newedge11 = Edge(edge1.p1(),inter)
                        newedge12 = Edge(inter,edge1.p2())

                        newedge21 = Edge(edge2.p1(),inter)
                        newedge22 = Edge(inter,edge2.p2())
                        
                        prevedges1 = edge1.prevs()
                        nextedges1 = edge1.nexts()

                        prevedges2 = edge2.prevs()
                        nextedges2 = edge2.nexts()

                        for prevedge1 in prevedges1:
                            prevedge1.remove_next(edge1)
                            prevedge1.add_next(newedge11)
                        for nextedge1 in nextedges1:
                            nextedge1.remove_prev(edge1)
                            nextedge1.add_prev(newedge12)
                            
                        prevedges2 = edge2.prevs()
                        nextedges2 = edge2.nexts()
                        for prevedge2 in prevedges2:
                            prevedge2.remove_next(edge2)
                            prevedge2.add_next(newedge21)
                        for nextedge2 in nextedges2:
                            nextedge2.remove_prev(edge2)
                            nextedge2.add_prev(newedge22)
                        
                        Edge.addadj(newedge11,newedge12)
                        Edge.addadj(newedge11,newedge22)
                        
                        Edge.addadj(newedge21,newedge22)
                        Edge.addadj(newedge21,newedge12)

                        self.remove(edge1)
                        self.remove(edge2)
                        
                        self.add(newedge11)
                        self.add(newedge12)
                        self.add(newedge21)
                        self.add(newedge22)
                        
                    # else: TODO: edge intersection
                            


    
