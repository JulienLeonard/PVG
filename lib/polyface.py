from geoutils  import *
from polygon   import *
from edgegraph import *

#
# a Face is a non-oriented arc
#
class Face:

    def __init__(self,points):
        self.mpolygon = Polygon(points)

    def polygon(self):
        return self.mpolygon

    def points(self):
        return self.mpolygon.points()

    def length(self):
        return self.mpolygon.length()


#
# Polyface is a circular list of Faces, computed by polygraph
#
class Polyface:

    def __init__(self,faces):
        self.mfaces    = faces
        self.mpolygon  = None
        self.madj      = {face: None for face in faces}

    def faces(self):
        return self.mfaces

    def add_adj(self,face,polyface):
        # puts("add_adj",self,face,polyface)
        self.madj[face] = polyface

    @staticmethod
    def add_adjacence(face,polyface1,polyface2):
        polyface1.add_adj(face,polyface2)
        polyface2.add_adj(face,polyface1)

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
        return lremove([self.adjacent(face) for face in self.faces()],None)

    def adjacent(self,face):
        if not face in self.madj:
            return None
        return self.madj[face]

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
