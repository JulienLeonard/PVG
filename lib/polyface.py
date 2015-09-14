from geoutils  import *
from polygon   import *
from edgegraph import *

class FaceExtremity:

    def __init__(self,point):
        self.mpoint = point
        self.mfaces = []

    def add_face(self,face):
        self.mfaces.append(face)

    def face_adjacents(self,face):
        if not face in self.mfaces:
            return None
        return lremove(self.mfaces,face)

#
# a Face is a non-oriented arc
#
class Face:

    def __init__(self,points):
        self.mpolygon         = Polygon(points)
        self.mpolyfaces       = []
        self.mfaceextremities = []

    def polygon(self):
        return self.mpolygon
    
    def polyfaces(self):
        return self.mpolyfaces

    def polyface(self):
        return self.mpolyfaces[0]

    def faceextremities(self):
        return self.mfaceextremities

    def points(self):
        return self.mpolygon.points()

    def length(self):
        return self.mpolygon.length()

    def isBorder(self):
        return len(self.mpolyfaces) == 1

    def other_polyface(self,polyface):
        if not polyface in self.mpolyfaces:
            return None
        if len(self.mpolyfaces) == 1:
            return None
        return iff(self.mpolyfaces[0] == polyface, self.mpolyfaces[1], self.mpolyfaces[0])

    def add_polyface(self,polyface):
        self.mpolyfaces.append(polyface)

    def add_faceextremity(self,ext):
        self.mfaceextremities.append(ext)

#
# Polyface is a circular list of Faces, computed by polygraph
#
class Polyface:

    def __init__(self,faces):
        self.mfaces    = faces
        for face in faces:
            face.add_polyface(self)
        self.mpolygon  = None

    def faces(self):
        return self.mfaces

    def polygon(self):
        if self.mpolygon == None:
            points = None
            for face in self.faces():
                if points == None:
                    points = face.points()[:]
                else:
                    facepoints = face.points()[:]
                    if not points[-1] == facepoints[0] and not points[-1] == facepoints[-1]:
                        points.reverse()
                    if points[-1] == facepoints[-1]:
                        facepoints.reverse()
                    if not points[-1] == facepoints[0]:
                        puts("Polyface def error")
                    
                    points.extend(facepoints[1:])
            self.mpolygon = Polygon(points)
        return self.mpolygon

    def vertexes(self):
        result = None
        for face in self.faces():
            if result == None:
                result = [face.points()[0]]
            else:
                newp = face.points()[0]
                if result[-1] == newp:
                    newp = face.points()[-1]
                result.append(newp)
        return result

    def length(self):
        return self.polygon().length()

    def face(self,fkey,reverse = False):
        sortedfaces = sorted(self.faces(),key=fkey)
        result = iff(reverse,sortedfaces[-1],sortedfaces[0])
        return result

    def adjacents(self):
        return lremove([face.other_polyface(self) for face in self.faces()],None)

    def adjacent(self,face):
        if not face in self.mfaces:
            return None
        return face.other_polyface(self)

    def isBorder(self):
        for face in self.mfaces:
            if face.isBorder():
                return True
        return False

    def borderFaces(self):
        return [face for face in self.madj if face.isBorder()]

    #
    # if number of arcs > 3, get a 4 sides polyface by computing the two smallest faces, then aggregating in between
    # if number of arcs == 3, compute the smallest on, and create a one-point face
    # if number of arcs == 2, create two one-point faces 
    #
    def longitudes(self):
        nodes = {}
        for face in self.faces():
            polygon = face.polygon()
            # puts("face",face,"points",polygon.points())
            p1,p2   = polygon.pointextremities()
            mp      = iff (p1.x() <= p2.x(), p1, p2)
            op      = iff (mp == p1,          p2, p1)
            polygon = iff (mp == p1,          polygon, polygon.reverse())
            for p in [p1,p2]:
                if not p in nodes:
                    nodes[p] = []
            nodes[mp].append(polygon)

        #for p in nodes.keys():
        #    puts("p",p,"nexts",len(nodes[p]))
        sortlist = sorted(nodes.keys(),key=Point.x)
        p0   = sortlist[0]
        pend = sortlist[-1]
        polypaths = [[poly] for poly in nodes[p0]]
        #puts("polypaths",polypaths)

        
        newpaths = []
        for path in polypaths:
            newpath = path
            while True:
                cpoly = newpath[-1]
                p2   = cpoly.point2()
                if cpoly.point2() == pend:
                    break
                # puts("followings",nodes[p2])
                newpoly = nodes[p2][0]
                newpath.append(newpoly)
            newpaths.append(newpath)
        polypaths = newpaths

        newfronts = []
        sides     = []
        for polypath in polypaths:
            if len(polypath) > 1:
                poly0 = polypath[0]
                if abs(poly0.point1().x() - poly0.point2().x()) < poly0.length() * 0.1:
                    sides.append(poly0)
                    polypath = polypath[1:]
                    
            if len(polypath) > 1:
                polyend = polypath[-1]
                if abs(polyend.point1().x() - polyend.point2().x()) < polyend.length() * 0.1:
                    sides.append(polyend)
                    polypath = polypath[:-1]

            newfronts.append(polypath)

            
        polypaths = [Polygon([polypath[0].point1()] + [p for poly in polypath for p in poly.points()[1:]]) for polypath in newfronts]
            
        return (polypaths,sides)
    
