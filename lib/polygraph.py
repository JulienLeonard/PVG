from geoutils import *
from polyface import *

#
# adjacent graph of polyfaces
#
class Polygraph:

    def __init__(self,polyfaces):
        self.mpolyfaces = polyfaces
        self.madj = None
    

    def polyfaces(self):
        return self.mpolyfaces

    def adj(self):
        if self.madj == None:
            self.madj = self.computeadj()
        return self.madj
        

    def computeadj(self):
        arcs = {}
        for polyface in self.polyfaces():
            for arc in polyface.arcs():
                if not arc in arcs:
                    arcs[arc] = []
                arcs[arc].append(polyface)
        
        adj = {}
        for arc in arcs.keys():
            if len(arcs[arc]) == 1:
                polyface1 = arcs[arc]
                adj[polyface1] = []
            elif len(arcs[arc]) == 2:
                (polyface1,polyface2) = arcs[arc]
                adj[polyface1] = [polyface2]
                adj[polyface2] = [polyface1]
            else:
                puts("error: arc",arc,"is contained by the following polyfaces",arcs[arc])
        return adj

    def adjacents(self,polyface):
        if not polyface in self.adj():
            puts("polyface",polyface,"not in polygraph")
            return None
        return self.adj()[polyface]
        
