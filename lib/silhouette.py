from bezier import *
from polyline import *

class Silhouette:
    def __init__(self,svgdef):
        self.mdef      = svgdef
        self.mbeziers  = []
        self.mlevels   = {}
        self.mcstrings = {}
        self.levels()

    def compute(self):
        if self.mbeziers == []:
            (fpoints,beziers)  = svg2bezier(self.mdef)
            self.mbeziers  = [bezier.clockwise().reverse() for bezier in beziers]
            self.mviewbox  = unionviewboxes([bezier.viewbox() for bezier in self.mbeziers])

    def size(self):
        self.compute()
        return viewportfromviewbox(self.mviewbox,1.0)[2]

    def viewport(self,factor=1.1):
        self.compute()
        return viewportfromviewbox(self.mviewbox,factor)

    def levels(self,circleboxfactor = 0.0,addedpolylines = []):
        if self.mlevels == {}:
            self.compute()
            minviewport = viewportfromviewbox(self.mviewbox,1.0)
            allbeziers = self.mbeziers
            if not circleboxfactor == 0.0:
                circlebox = Polyline(circlepolygon((minviewport[0],minviewport[1],minviewport[2]*circleboxfactor),250)).close()
                allbeziers = allbeziers + [circlebox]
            if not len(addedpolylines) == 0:
                allbeziers = allbeziers + addedpolylines
            self.mlevels = computeshapelevels(allbeziers)
            self.mpolys  = { level: [bezier.points() for bezier in self.mlevels[level]] for level in self.mlevels["levels"]}
        return self

    def getlevels(self):
        if self.mlevels == {}:
            puts("error: you need to define levels first")
            return ""
        return [level for level in self.mlevels["levels"]]


    def allpoints(self):
        if self.mlevels == {}:
            puts("error: you need to define levels first")
            return ""
        return [point for level in self.mlevels["levels"] for poly in self.mpolys[level] for point in poly]

    def allpointcircles(self,rc):
        return [(point[0],point[1],rc) for level in self.mlevels["levels"] for poly in self.mpolys[level] for point in Polyline(poly).lengthsamples(rc)]

    def polygonlevel(self,polygon):
        if self.mlevels == {}:
            puts("error: you need to define levels first")
            return ""

        for level in lreverse(self.mlevels["levels"]):
            if ispolyinsidecontours(polygon,self.mpolys[level]):
                return level
        return ""

    def pointlevel(self,point):
        for level in lreverse(self.mlevels["levels"]):
            if ispointinsidecontours(point,self.mpolys[level]):
                return level
        return ""

    def polygons(self,level=0):
        if self.mlevels == {}:
            puts("error: you need to define levels first")
            return ""
        
        if not level in self.mlevels:
            puts("error: no level",level)
            return ""

        return self.mpolys[level]
