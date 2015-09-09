from utils     import *
from geoutils  import *
from polygon   import *

class Voronoi:
    def __init__(self,points):
        self.mpoints   = lunique([p.coords() for p in points])
        self.mcontext  = None
        self.mpolygons = []
        self.compute(self.mpoints)

    def compute(self,points):
        import voronoi
        self.mcontext  = voronoi.voronoi(points)

        self.medges    = self.buildtriforedges()

        self.mvertices = self.buildtriforvertices(self.medges)

        self.mexts     = self.buildextseqsforvertices(self.mvertices)

       # centers = buildcentersfortri(context)

        self.mpolygons = self.buildpolygonsfromexts(self.mpoints,self.mexts)

    def voronoipolygons(self):
        return (self.mcontext,self.mpolygons)
        
    def polygons(self):
        return [Polygon([Point().coords(p) for p in polypoints]) for polypoints in self.mpolygons]

    def trianglescoords(self):
        result = [[self.mpoints[i] for i in tri] for tri in self.mcontext.triangles]
        return result

    def buildtriforedges(self):
        edges = {}
        for (i1,i2,i3) in self.mcontext.triangles:
            # print i1,i2,i3
            tri = [i1,i2,i3]
            tri.sort()
            for (ip1,ip2) in circlepairs(tri):
                e1 = min(ip1,ip2)
                e2 = max(ip1,ip2)
                if not (e1,e2) in edges:
                    edges[(e1,e2)] = []
                edges[(e1,e2)].append(tri)
        return edges

    def buildtriforvertices(self,edges):
        vertices = {}
        for (i1,i2) in edges.keys():
            for i in [i1,i2]:
                if not i in vertices:
                    vertices[i] = []
                for tri in edges[(i1,i2)]:
                    if (vertices[i].count(tri) == 0):
                        vertices[i].append(tri)
        return vertices

    def buildextseqsforvertices(self,vertices):
        exts = {}
        for i in vertices.keys():
            vextlist = {}
            for tri in vertices[i]:
                sextlist = [p for p in tri if p != i]
                for (e1,e2) in circlepairs(sextlist):
                    if not e1 in vextlist:
                        vextlist[e1] = []
                    vextlist[e1].append(e2)


            # here vextlist contain adjacency of exts
            # now just follow the trail
            extlist = [vextlist.keys()[0]]
            while(1):
                cext = extlist[-1]
                oexts = [e for e in  vextlist[cext] if not (len(extlist) > 1 and (e == extlist[-2]))]
                if not len(oexts):
                    exts[i] = []
                    # print "no poly for",i
                    extlist = []
                    break
                else:
                    oext = oexts[0]
                    if oext == extlist[0]:
                        # print "poly over for ",i,":",extlist
                        break
                    else:
                        extlist.append(oext)

            exts[i] = extlist
        return exts

    def buildpolygonsfromexts(self,points,exts):
        # puts("voronoi polygons exts keys",exts.keys(),"values",exts.values())
        polygons = []
        cindex = 0
        for v in exts.keys():
            if (len(exts[v])):
                a = points[v]
                polypoints = []
                for (b, c) in circlepairs(exts[v]):
                    ax,ay = a
                    bx,by = points[b]
                    cx,cy = points[c]

                    D = 2*(ax*(by-cy) + bx*(cy-ay)+cx*(ay-by))
                    px = ((ax*ax+ay*ay)*(by-cy) + (bx*bx+by*by)*(cy-ay) + (cx*cx+cy*cy)*(ay-by))/D
                    py = ((ax*ax+ay*ay)*(cx-bx) + (bx*bx+by*by)*(ax-cx) + (cx*cx+cy*cy)*(bx-ax))/D

                    # print "px",px,"py",py
                    polypoints.append((px,py))
                polygons.append(polypoints)
        return polygons

    def polygonfromvertice(self,vi):
        v = self.mcontext.vertices[vi]
        for poly in self.mpolygons:
            for p in poly:
                if pequal(p,v,0.00001):
                    return poly
        return None

    def boundarypoints(self):
        result = [self.mcontext.vertices[i] for (l,i) in self.boundarylines()]
        return result

    def boundarylines(self):
        result = []
        for (l,v1,v2) in self.mcontext.edges:
            if v1 == -1 or v2 == -1:
                if v1 != -1:
                    verti = v1
                else:
                    verti = v2                
                result.append((l,verti))
        return result

    def boundaryedges(self,bbox):
        result = []
        (xmin,ymin,xmax,ymax) = bbox
        for (l,verti) in self.boundarylines():
            a,b,c = self.mcontext.lines[l]
            # print "a,b,c",a,b,c
            if abs(0.0-b) < 0.0001:
                ys = [ymin,ymax]
                xs = [(c/a - b/a * y) for y in ys]
                points = [(xs[i],ys[i]) for i in range(len(xs))]
            else:
                xs = [xmin,xmax]
                ys = [(c/b - a/b * x) for x in xs]
                points = [(xs[i],ys[i]) for i in range(len(xs))]
            vertcoords = self.mcontext.vertices[verti]
            extpoints = []
            for epoint in points:
                eresult = True
                poly = self.polygonfromvertice(verti)
                if poly != None:
                    for (p1,p2) in circlepairs(poly):
                        if pdiff(p1,vertcoords,0.000001) and pdiff(p2,vertcoords,0.000001):
                            inter = raw_intersection(p1,p2,vertcoords,epoint) 
                            print "inter",inter,"p1,p2,vertcoords,epoint",p1,p2,vertcoords,epoint
                            if len(inter):
                                eresult = False
                else:
                    print "no poly",poly
                if eresult:
                    extpoints.append(epoint)

            if len(extpoints) == 1:
                result.append([vertcoords,extpoints[0]])
        return result
