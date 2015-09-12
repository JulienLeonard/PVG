from geoutils  import *
from polyface  import *
from edgegraph import *

#
# adjacent graph of polyfaces
#
class Polygraph:

    def __init__(self,edgegraph):
        self.mpolyfaces = Polygraph.computepolyfaces(edgegraph) 

    def polyfaces(self):
        return self.mpolyfaces

    @staticmethod
    def computepolyfaces(edgegraph):

        # first compute faces
        faces = {}
        newfaces = [list]
        for arccycle in edgegraph.clockwise_arccycles():
            for arc in arccycle.arcs():
                if not arc in faces:
                    newface = Face(arc.points())
                    newfaces.append(newface)
                    for carc in [arc,arc.opposite()]:
                        faces[carc] = newface
                    
        # then compute polyfaces
        result = [Polyface([faces[arc] for arc in arccycle.arcs()]) for arccycle in edgegraph.clockwise_arccycles()]

        # then compute adjacents faces
        result = Polygraph.computeadj(result)

        return result

    @staticmethod
    def computeadj(polyfaces):
        faces = {}
        for polyface in polyfaces:
            for face in polyface.faces():
                if not face in faces:
                    faces[face] = []
                faces[face].append(polyface)
        
        for face in faces.keys():
            # puts("face",face,"polyfaces",faces[face])
            if len(faces[face]) == 2:
                (polyface1,polyface2) = faces[face]
                Polyface.add_adjacence(face,polyface1,polyface2)

        return polyfaces
