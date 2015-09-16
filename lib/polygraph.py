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
    #
    #
    def border_faces(self):
        # find first face as border
        for face in self.mfaces:
            if face.isBorder():
                face0 = face
                break
        
        # then run along border to get them all
        front = [face0]
        while True:
            cface = front[-1]
            added = False
            for faceext in cface.faceextremities():
                for adjface in faceext.face_adjacents(cface):
                    if not adjface in front and adjface.isBorder():
                        front.append(adjface)
                        added = True
                        break
                if added:
                    break
            if not added:
                break

        return front


    def border_polyfaces(self):
        return [face.polyface() for face in self.border_faces()]

    def border_polygon(self):
        return Face.joined_polygon(self.border_faces())


    @staticmethod
    def computepolygraph(edgegraph):

        # first compute faces
        faces = {}
        newfaces = []
        for arccycle in edgegraph.clockwise_arccycles():
            for arc in arccycle.arcs():
                if not arc in faces:
                    newface = Face(arc.points())
                    newfaces.append(newface)
                    for carc in [arc,arc.opposite()]:
                        faces[carc] = newface

        # then compute faceextremities
        faceexts = {}
        for face in newfaces:
            (p1,p2) = (face.points()[0],face.points()[-1])
            for p in (p1,p2):
                if not p in faceexts:
                    faceexts[p] = FaceExtremity(p)
                face.add_faceextremity(faceexts[p])
                faceexts[p].add_face(face)
                    
        # then compute polyfaces
        polyfaces = [Polyface([faces[arc] for arc in arccycle.arcs()]) for arccycle in edgegraph.clockwise_arccycles()]

        return (polyfaces,newfaces,faceexts.values())
