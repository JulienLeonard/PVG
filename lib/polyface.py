from geoutils  import *
from polygon   import *
from edgegraph import *

#
# a Face is a non-oriented arc
#
class Face:

    def __init__(self,points):
        self.mpoints = points

#
# Polyface is a circular list of Faces, computed by polygraph
#
class Polyface:

    def __init__(self,faces):
        self.mfaces    = faces
        self.mpolygon  = None
        self.madj      = {face: [] for face in faces}

    def faces(self):
        return self.mfaces

    def add_adj(self,face,polyface):
        self.madj[face].append(polyface)

    @staticmethod
    def add_adjacence(face,polyface1,polyface2):
        polyface1.add_adj(face,polyface2)
        polyface2.add_adj(face,polyface1)

    def polygon(self):
        if self.mpolygon == None:
            self.mpolygon = Polygon([p for face in self.faces() for p in face.points()])
        return self.mpolygon

    def vertexes(self):
        return [face.points()[0] for face in self.faces()]

    def length(self):
        return self.polygon().length()

    def face(self,fkey,reverse = False):
        sortedfaces = sorted(self.faces(),key=fkey)
        result = iff(reverse,sortedfaces[-1],sortedfaces[0])
        return result


    #
    # if number of arcs > 3, get a 4 sides polyface by computing the two smallest faces, then aggregating in between
    # if number of arcs == 3, compute the smallest on, and create a one-point face
    # if number of arcs == 2, create two one-point faces 
    #
    def longitudes(self):
        nodes = {}
        for face in self.faces():
            puts("face",face,"points",len(face.points()))
            p1,p2 = face.pointextremities()
            p  = iff (p1.x() <= p2.x(), p1, p2)
            op = iff (p == p1, p2, p1)
            for pi in (p1,p2):
                if not pi in nodes:
                    nodes[pi] = []
            nodes[p].append(face)

        for p in nodes.keys():
            puts("p",p,"nexts",len(nodes[p]))
        sortlist = sorted(nodes.keys(),key=Point.x)
        p0   = sortlist[0]
        pend = sortlist[-1]
        facepaths = [[face] for face in nodes[p0]]
        
        newpaths = []
        for path in facepaths:
            newpath = path
            while True:
                cface = newpath[-1]
                p2   = cface.point2()
                if cface.point2() == pend:
                    break
                puts("followings",nodes[p2])
                newface = nodes[p2][0]
                newpath.append(newface)
            newpaths.append(newpath)
        facepaths = newpaths

        newfronts = []
        sides     = []
        for facepath in facepaths:
            if len(facepath) > 1:
                face0 = facepath[0]
                if abs(face0.point1().x() - face0.point2().x()) < face0.length() * 0.1:
                    sides.append(face0)
                    facepath = facepath[1:]
                    
            if len(facepath) > 1:
                faceend = facepath[-1]
                if abs(faceend.point1().x() - faceend.point2().x()) < faceend.length() * 0.1:
                    sides.append(faceend)
                    facepath = facepath[:-1]

            newfronts.append(facepath)

            
        polypaths = [Polygon([facepath[0].point1()] + [p for face in facepath for p in face.points()[1:]]) for facepath in newfronts]
            
        return (polypaths,sides)
