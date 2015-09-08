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
        self.polygon().length()

    def rightface(self):
        sortedarcs = sorted(self.arccycle().arcs(),key=Arc.aggx)
        return Polygon(sortedarcs[-1].points())




    #
    # if number of arcs > 3, get a 4 sides polyface by computing the two smallest faces, then aggregating in between
    # if number of arcs == 3, compute the smallest on, and create a one-point face
    # if number of arcs == 2, create two one-point faces 
    #
    def longintercurves(self):
        sortlist = sorted(self.arccycle().arcs(),Arc.length)
        # TODO

        
def edgegraph_polyfaces(self):
    return [Polyface(arccycle) for arccycle in self.arccycles()]

EdgeGraph.polyfaces = edgegraph_polyfaces
