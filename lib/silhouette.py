from bezier  import *
from polygon import *

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
            self.mviewbox  = bbunions([bezier.viewbox() for bezier in self.mbeziers])

    def size(self):
        self.compute()
        return self.mviewbox.size()

    def viewport(self,factor=1.1):
        self.compute()
        return self.mviewbox.viewport(factor)

    def levels(self,circleboxfactor = 0.0,addedpolygons = []):
        if self.mlevels == {}:
            self.compute()
            minviewport = self.mviewbox.viewport()
            allbeziers = self.mbeziers
            if not circleboxfactor == 0.0:
                circlebox  = minviewport.circle().scale(circleboxfactor).polygon(250).close()
                allbeziers = allbeziers + [circlebox]
            if not len(addedpolygons) == 0:
                allbeziers = allbeziers + addedpolygons
            self.mlevels = computeshapelevels(allbeziers)
            self.mpolys  = { level: [bezier.polygon() for bezier in self.mlevels[level]] for level in self.mlevels["levels"]}
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
        return [(point[0],point[1],rc) for level in self.mlevels["levels"] for poly in self.mpolys[level] for point in poly.lengthsamples(rc)]

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

    #
    # return the first polygon of first level
    #
    def polygon(self):
        return self.polygons(0)[0]
