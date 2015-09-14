from geoutils  import *
from polyface  import *
from edgegraph import *

#
# adjacent graph of polyfaces
#
class Polygraph:

    def __init__(self,edgegraph):
        self.mpolyfaces = None
        self.mfaces     = None
        self.mfaceexts  = None
        result = self.computepolygraph(edgegraph) 
        (self.mpolyfaces,self.mfaces,self.mfaceexts) = result

    def polyfaces(self):
        return self.mpolyfaces

    def faces(self):
        return self.mfaces

    def faceextremities(self):
        return self.mfaceexts

    #
    # return the border polyfaces, ie with one face no neighbours, according to their adjacency
    #
    def borders(self):
        # first find all faces with a border
        borderlist = []
        for polyface in self.polyfaces():
            if polyface.isBorder():
                borderlist.append(polyface)

        if len(borderlist) == 0:
            return []
        
        puts("borderlist",len(borderlist))

        # then order according to adjacency
        # WARNING: only work for single contour
        front = [borderlist[0]]
        while len(front) < len(borderlist):
            cface = front[-1]
            puts("cface",cface)
            for adj in cface.adjacents():
                if adj in borderlist and not adj in front:
                    front.append(adj)
                    break

        front = borderlist

        puts("front",len(front))
        
        return front


    @staticmethod
    def computepolygraph(edgegraph):

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

        # then compute faceextremities
        faceexts = {}
        for face in faces.values():
            (p1,p2) = (face.points()[0],face.points()[-1])
            for p in (p1,p2):
                if not p in faceexts:
                    faceexts[p] = FaceExtremity(p)
                face.add_extremity(face,faceexts[p])
                faceexts[p].add_face(face)
                    
        # then compute polyfaces
        polyfaces = [Polyface([faces[arc] for arc in arccycle.arcs()]) for arccycle in edgegraph.clockwise_arccycles()]

        return (polyfaces,faces.values(),faceexts.values())
