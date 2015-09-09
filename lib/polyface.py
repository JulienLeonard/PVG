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
            arc = iff (p == p1, arc, arc.opposite())
            nodes[p].append(arc)

        for p in nodes.keys():
            puts("p",p,"nexts",len(nodes[p]))
        sortlist = sorted(nodes.keys(),key=Point.x)
        p0   = sortlist[0]
        pend = sortlist[-1]
        arcpaths = [[arc] for arc in nodes[p0]]
        
        newpaths = []
        for path in arcpaths:
            newpath = path
            while True:
                carc = newpath[-1]
                p2   = carc.point2()
                if carc.point2() == pend:
                    break
                puts("followings",nodes[p2])
                newarc = nodes[p2][0]
                newpath.append(newarc)
            newpaths.append(newpath)
        arcpaths = newpaths

        newfronts = []
        sides     = []
        for arcpath in arcpaths:
            if len(arcpath) > 1:
                arc0 = arcpath[0]
                if abs(arc0.point1().x() - arc0.point2().x()) < arc0.length() * 0.1:
                    sides.append(arc0)
                    arcpath = arcpath[1:]
                    
            if len(arcpath) > 1:
                arcend = arcpath[-1]
                if abs(arcend.point1().x() - arcend.point2().x()) < arcend.length() * 0.1:
                    sides.append(arcend)
                    arcpath = arcpath[:-1]

            newfronts.append(arcpath)

            
        polypaths = [Polygon([arcpath[0].point1()] + [p for arc in arcpath for p in arc.points()[1:]]) for arcpath in newfronts]
            
        return (polypaths,sides)
                


        
def edgegraph_polyfaces(self):
    allpolyfaces = [Polyface(arccycle) for arccycle in self.arccycles()]
    return [polyface for polyface in allpolyfaces if polyface.polygon().isClockwise()]

EdgeGraph.polyfaces = edgegraph_polyfaces
