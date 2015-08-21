from bezier  import *
from polygon import *

class Silhouette:
    def __init__(self):
        self.mbeziers  = []
        self.mlevels   = {}
        self.mcstrings = {}
        self.mviewbox = None

    def beziers(self):
        return self.mbeziers

    def add(self,polybezier):
        puts("add bezier")
        self._add(polybezier)
        self.computelevels()

    def _add(self,polybezier):
        self.mbeziers.append(polybezier.clockwise().reverse())
        if self.mviewbox == None:
            self.mviewbox = polybezier.viewbox()
        else:
            self.mviewbox = bbunions([self.mviewbox,polybezier.viewbox()])
        
    def loadsvgstring(self,svgstring):
        (fpoints,beziers)  = svg2bezier(svgstring)
        for bezier in beziers:
            self._add(bezier)
        self.computelevels()
        return self

    def size(self):
        return self.mviewbox.size()

    def viewport(self,factor=1.1):
        return self.mviewbox.viewport(factor)

    def computelevels(self):
        puts("computelevels")
        allbeziers = self.mbeziers
        self.mlevels = computeshapelevels(allbeziers)
        self.mpolys  = { level: [bezier.polygon() for bezier in self.mlevels[level]] for level in self.mlevels["levels"]}
        return self

    def getlevels(self):
        return [level for level in self.mlevels["levels"]]

    def allpoints(self):
        return [point for level in self.mlevels["levels"] for poly in self.mpolys[level] for point in poly]

    def allpointcircles(self,rc):
        return [(point[0],point[1],rc) for level in self.mlevels["levels"] for poly in self.mpolys[level] for point in poly.lengthsamples(rc)]

    def polygonlevel(self,polygon):
        for level in lreverse(self.mlevels["levels"]):
            if ispolyinsidecontours(polygon,self.mpolys[level]):
                return level
        return None

    def pointlevel(self,point):
        for level in lreverse(self.mlevels["levels"]):
            if ispointinsidecontours(point,self.mpolys[level]):
                return level
        return None

    def polygons(self,level=0):
        if not level in self.mlevels:
            puts("error: no level",level)
            return []

        return self.mpolys[level]

    #
    # return the first polygon of first level
    #
    def polygon(self):
        return self.polygons(0)[0]

    @staticmethod
    def merge(silhouettes):
        result = Silhouette()
        for silhouette in silhouettes:
            for bezier in silhouette.beziers():
                result.add(bezier)
        return result

def svgpaths2silhouette(svgPaths):
    result = Silhouette.merge([path.silhouette() for path in svgPaths])
