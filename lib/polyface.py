from geoutils  import *
from polygon   import *
from edgegraph import *

class Polyface:

    def __init__(self,arccycle):
        self.marccycle = arccycle
        self.mpolygon  = None
        
    def arccycle(self):
        return self.marccycle

    def polygon(self):
        if self.mpolygon == None:
            self.mpolygon = Polygon(self.arccycle().points())
        return self.mpolygon

    def faces(self):
        return [Polygon(arc.points()) for arc in self.arccycle().arcs()]

    def vertexes(self):
        return [arc.points()[0] for arc in self.arccycle().arcs()]

    def length(self):
        return self.polygon().length()

    def face(self,fkey,reverse = False):
        sortedarcs = sorted(self.arccycle().arcs(),key=fkey)
        result = iff(reverse,sortedarcs[-1],sortedarcs[0])
        return result


    #
    # if number of arcs > 3, get a 4 sides polyface by computing the two smallest faces, then aggregating in between
    # if number of arcs == 3, compute the smallest on, and create a one-point face
    # if number of arcs == 2, create two one-point faces 
    #
    def longitudes(self):
        nodes = {}
        for arc in self.arccycle().arcs():
            puts("arc",arc,"points",len(arc.points()))
            p1,p2 = arc.pointextremities()
            p  = iff (p1.x() <= p2.x(), p1, p2)
            op = iff (p == p1, p2, p1)
            for pi in (p1,p2):
                if not pi in nodes:
                    nodes[pi] = []
            nodes[p].append((arc,op))

        for p in nodes.keys():
            puts("p",p,"nexts",len(nodes[p]))
        sortlist = sorted(nodes.keys(),Point.x)
        p0   = sortlist[0]
        pend = sortlist[-1]
        (front1,front2) = [[item] for item in nodes[p0]]
        for front in (front1,front2):
            (arc,p2) = front[-1]
            if not p2 == pend:
                newarc = nodes[p][0]
                op     = iff (newarc.p1() == p2, newarc.p2(), newarc.p1())
                front.append((newarc,op))

        for front in (front1,front2):
            front = [arc for (arc,p2) in front]

        for front in (front1,front2):
            if len(front) > 1:
                arc0 = front[0]
                if abs(arc0.point1().x() - arc0.point2().x()) < arc0.length() * 0.1:
                    front = front[1:]
            if len(front) > 1:
                arcend = front[-1]
                if abs(arcend.point1().x() - arcend.point2().x()) < arcend.length() * 0.1:
                    front = front[:-1]

        return (front1,front2)
                


        
def edgegraph_polyfaces(self):
    allpolyfaces = [Polyface(arccycle) for arccycle in self.arccycles()]
    return [polyface for polyface in allpolyfaces if polyface.polygon().isClockwise()]

EdgeGraph.polyfaces = edgegraph_polyfaces
