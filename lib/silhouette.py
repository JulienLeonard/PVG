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
        self._add(polybezier)
        self.computelevels()
        return self

    def adds(self,polybeziers):
        for polybezier in polybeziers:
            self._add(polybezier)
        self.computelevels()
        return self


    def _add(self,polybezier):
        self.mbeziers.append(polybezier.clockwise().reverse())
        if self.mviewbox == None:
            self.mviewbox = polybezier.viewbox()
        else:
            self.mviewbox = bbunions([self.mviewbox,polybezier.viewbox()])
        
    def loadsvgstring(self,svgstring):
        (fpoints,beziers)  = svg2bezier(svgstring)
        self.adds(beziers)
        return self

    def size(self):
        return self.mviewbox.size()

    def bbox(self,factor=1.1):
        return self.mviewbox.resize(factor)

    def viewport(self,factor=1.1):
        return self.mviewbox.resize(factor).viewport(factor)

    def computelevels(self):
        # puts("computelevels nbeziers",len(self.mbeziers))
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

    def levels(self):
        return self.mlevels

    def polygons(self,level=0):
        if not level in self.mlevels:
            # puts("error: no level",level)
            return []

        return self.mpolys[level]

    #
    # return the first polygon of first level
    #
    def polygon(self):
        return self.polygons(0)[0]

    def allpolygons(self):
        return [poly for level in self.mpolys.keys() for poly in self.mpolys[level]]

    def allsegments(self,lengthsample = None):
        if not lengthsample == None:
            return [Segment(p1,p2) for poly in self.allpolygons() for (p1,p2) in pairs(poly.lengthsamples(lengthsample))]
        else:
            return [seg for poly in self.allpolygons() for seg in poly.segments()]

    @staticmethod
    def merge(silhouettes):
        result = Silhouette()
        for silhouette in silhouettes:
            for bezier in silhouette.beziers():
                result.add(bezier)
        return result

    def symx(self,symx):
        return Silhouette().adds([bezier.symx(symx) for bezier in self.beziers()])


def svgpaths2silhouette(svgPaths):
    result = Silhouette()
    beziers = [item for path in svgPaths for item in path.silhouette().beziers()]
    result.adds(beziers)
    return result
