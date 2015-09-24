from geoutils  import *
from polygon   import *
from edgegraph import *
from geoquad   import *

class FaceExtremity:

    def __init__(self,point):
        self.mpoint = point
        self.mfaces = []

    def point(self):
        return self.mpoint

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

    def vertexes(self):
        return [faceext.point() for faceext in self.faceextremities()]

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
        # puts("face",self,"add ext",ext)
        self.mfaceextremities.append(ext)

    def polygonfrom(self,point):
        if point == self.mfaceextremities[0].point():
            return self.polygon()
        else:
            return self.polygon().reverse()

    @staticmethod
    def joined_polygon(faces):
        points = None
        for face in faces:
            if points == None:
                points = face.points()[:]
            else:
                facepoints = face.points()[:]
                if not points[-1] == facepoints[0] and not points[-1] == facepoints[-1]:
                    points.reverse()
                if points[-1] == facepoints[-1]:
                    facepoints.reverse()
                if not points[-1] == facepoints[0]:
                    puts("Polyface joined_polygon def error")
                    
                points.extend(facepoints[1:])
        result = Polygon(points)
        return result

    def xs(self):
        return [p.x() for p in self.vertexes()]

    def ys(self):
        return [p.y() for p in self.vertexes()]

    def miny(self):
        return lmin(self.ys())

    def minx(self):
        return lmin(self.xs())

    def maxy(self):
        return lmax(self.ys())

    def maxx(self):
        return lmax(self.xs())

    def middley(self):
        return lmean(self.ys())

    def middlex(self):
        return lmean(self.xs())

    def maxmiddlex(self):
        return -self.middlex()

    def minmiddlex(self):
        return self.middlex()


#
# Polyface is a circular list of Faces, computed by polygraph
#
class Polyface:

    def __init__(self,faces):
        self.mfaces    = faces
        for face in faces:
            face.add_polyface(self)
        self.mpolygon  = None
        self.mfacepolygon = {}

    def faces(self):
        return self.mfaces

    def polygon(self):
        if self.mpolygon == None:
            points = None
            face0 = None
            for face in self.faces():
                if points == None:
                    points = face.points()[:]
                    face0 = face
                else:
                    facepoints = face.points()[:]
                    if not points[-1] == facepoints[0] and not points[-1] == facepoints[-1]:
                        points.reverse()
                    if self.mfacepolygon == {}:
                        self.mfacepolygon[face0] = Polygon(points[:])
                    if points[-1] == facepoints[-1]:
                        facepoints.reverse()
                    if not points[-1] == facepoints[0]:
                        puts("Polyface def error")

                    self.mfacepolygon[face] = Polygon(facepoints)
                    points.extend(facepoints[1:])
            self.mpolygon = Polygon(points)
        return self.mpolygon

    def faceexts(self):
        result = []
        faces = self.faces()
        face0 = faces[0]
        face1 = faces[1]
        ext00,ext01  = face0.faceextremities()
        ext10,ext11  = face1.faceextremities()
        
        result.append(iff(ext00 == ext10 or ext00 == ext11,ext01,ext00))
        for face in faces[1:-1]:
            ext1,ext2 = face.faceextremities()
            result.append(iff(ext1 == result[-1],ext2,ext1))
        return result


    def vertexes(self):
        return [faceext.point() for faceext in self.faceexts()]

    def length(self):
        return self.polygon().length()

    def xs(self):
        return map(Point.x,self.vertexes())

    def ys(self):
        return map(Point.y,self.vertexes())

    def miny(self):
        return lmin(self.ys())

    def minx(self):
        return lmin(self.xs())

    def maxy(self):
        return lmax(self.ys())

    def maxx(self):
        return lmax(self.xs())

    def middley(self):
        return lmean(self.ys())

    def middlex(self):
        return lmean(self.xs())

    def sortedfaces(self,fkey):
        return sorted(self.faces(),key=fkey)

    def sortedface(self,fkey):
        return sorted(self.faces(),key=fkey)[0]
                    
    def face(self,fkey,reverse = False):
        sortedfaces = self.sortedfaces(fkey)
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
        return [face for face in self.faces() if face.isBorder()]

    def border(self):
        return self.borderFaces()[0]

    def facepolygon(self,face):
        if self.mfacepolygon == {}:
            self.polygon()
        if not face in self.mfacepolygon:
            return None
        return self.mfacepolygon[face]

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

    #
    # compute a quad by having the specified face as left, the 2 adjacent faces as up and down, and the other(s) as right
    #
    # self.mfaces must be in clockwise 
    def quadfromface(self,rootface):
        # puts("quadfromface faces",[(face.points()[0],face.points()[-1]) for face in self.mfaces])
        if not rootface in self.mfaces:
            return None
        face_up     = lcircularnext(self.mfaces,rootface)
        face_down   = lcircularnext(self.mfaces,rootface,-1)
        face_rights = lcircularitems(self.mfaces,face_up,face_down)
        
        polygon_left   = rootface.polygon()
        polygon_up     = face_up.polygonfrom(polygon_left.points()[-1])
        polygon_down   = face_down.polygonfrom(polygon_left.points()[0])

        if len(face_rights) == 0:
            polygon_right = Polygon([polygon_up.points()[-1]])
        else:
            polygon_right = Polyface.faces2polygon(face_rights).reverse()

        if polygon_left.points()[-1] != polygon_up.points()[0] and  polygon_left.points()[-1] != polygon_up.points()[-1]:
            polygon_left = polygon_left.reverse()
        if polygon_up.points()[0] != polygon_left.points()[-1]:
            polygon_up = polygon_up.reverse()
        if polygon_down.points()[0] != polygon_left.points()[0]:
            polygon_down = polygon_down.reverse()
        if polygon_right.points()[-1] != polygon_up.points()[-1]:    
            polygon_right = polygon_right.reverse()

        # puts("quadfromface: faces",self.mfaces,"rootface",rootface,"result",face_up,face_rights,face_down)

        return GeoQuad(polygon_left,polygon_up,polygon_right,polygon_down)

    #
    # compute a quad by having the specified face as left, the 2 adjacent faces as up and down, and the other(s) as right
    #
    # self.mfaces must be in clockwise 
    def quadfromleftrightfaces(self,face_left,face_right):
        puts("quadfromleftrightfaces faces",face_left,face_right)
        if not face_left in self.mfaces or not face_right in self.mfaces:
            return None
        face_ups     = lcircularitems(self.mfaces,face_left,face_right)
        face_downs   = lcircularitems(self.mfaces,face_right,face_left)

        puts("quadfromleftrightfaces face_ups",face_ups,"face_downs",face_downs)
        
        polygon_left    = face_left.polygon()
        polygon_right   = face_right.polygon()
        polygon_up      = Polyface.faces2polygon(face_ups)
        polygon_down    = Polyface.faces2polygon(face_downs)

        if polygon_left.points()[-1] != polygon_up.points()[0] and  polygon_left.points()[-1] != polygon_up.points()[-1]:
            polygon_left = polygon_left.reverse()
        if polygon_up.points()[0] != polygon_left.points()[-1]:
            polygon_up = polygon_up.reverse()
        if polygon_down.points()[0] != polygon_left.points()[0]:
            polygon_down = polygon_down.reverse()
        if polygon_right.points()[-1] != polygon_up.points()[-1]:    
            polygon_right = polygon_right.reverse()

        # puts("quadfromface: faces",self.mfaces,"rootface",rootface,"result",face_up,face_rights,face_down)

        return GeoQuad(polygon_left,polygon_up,polygon_right,polygon_down)



    @staticmethod
    def faces2polygon(faces):
        polygons = Polyface.faces2polygons(faces)

        if len(polygons) == 0:
            return None

        result = polygons[0]
        for polygon in polygons[1:]:
            result = result.concat(polygon)

        return result

    @staticmethod
    def faces2polygons(faces):
        if len(faces) == 0:
            return []
        if len(faces) == 1:
            return [faces[0].polygon()]

        result = [Polygon(faces[0].polygon().points()[:])]
        next1  = Polygon(faces[1].polygon().points()[:])
        if result[0].ext2() != next1.ext1() and result[0].ext2() != next1.ext2():
            result = [result[0].reverse()]
        for face in faces[1:]:
            newpolygon = Polygon(face.polygon().points()[:])
            if newpolygon.ext1() != result[-1].ext2():
                newpolygon = newpolygon.reverse()
            result.append(newpolygon)
        return result
        
        
