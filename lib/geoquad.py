from utils        import *
from geoutils     import *
from curvebuilder import *
from circle       import *

class GeoQuadNode:

    def __init__(self,geoquad,bbox):
        self.mgeoquad  = geoquad
        self.mbbox     = bbox
        self.msubnodes = []

    def contain(self,point):
        return self.mgeoquad.containpoint(point)

    def split(self):
        subgeoquads = self.mgeoquad.xysplit()
        subbboxes   = self.mbbox.split4()
        for (subgeoquad,subbox) in zip(subgeoquads,subbboxes):
            self.msubnodes.append(GeoQuadNode(subgeoquad,subbox))

    def leaf(self,point,minsize):
        if not self.contain(point):
            return None

        if self.mgeoquad.length() > minsize:
            self.split()
    
            for subnode in self.msubnodes:
                containsubresult = subnode.leaf(point,minsize)
                if containsubresult != None:
                    return containsubresult
        else:
            return self.mbbox

class GeoQuadTree:

    def __init__(self,geoquad):
        self.mroot   = GeoQuadNode(geoquad,BBox(0.0,0.0,1.0,1.0))

    def leaf(self,point,minsize):
        return self.mroot.leaf(point,minsize)

#
# Geometric contour defined by 2 x 2 curves
#
class GeoQuad:

    def __init__(self,left,up,right,down):
        self.mleft  = left
        self.mup    = up
        self.mright = right
        self.mdown  = down
        self.interx = CR(self.mleft,self.mright)
        self.intery = CR(self.mdown,self.mup)
        self.mpolygon = self.mleft.concat(self.mup).concat(self.mright.reverse()).concat(self.mdown.reverse())
        self.mgeoquadtree = None

    def polygon(self):
        return self.mpolygon

    def polygons(self):
        return [self.mleft,self.mup,self.mright.reverse(),self.mdown.reverse()]

    def length(self):
        return self.polygon().length()

    def xcurve(self,x):
        return self.interx.sample(x).maponpoints(self.mdown.sample(x),self.mup.sample(x))

    def ycurve(self,y):
        return self.intery.sample(y).maponpoints(self.mleft.sample(y),self.mright.sample(y))

    def xpoint(self,p):
        return self.xcurve(p.x()).sample(p.y())

    def ypoint(self,p):
        return self.ycurve(p.y()).sample(p.x())

    def containpoint(self,point):
        return self.polygon().containpoint(point)

    @staticmethod
    def square(center = Point(0.5,0.5),size = 1.0,npointsperface = 10):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.square(center,size).points())]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())

    @staticmethod
    def rectangle(x1,y1,x2,y2,npointsperface):
        faces = [Polygon(Polygon([p1,p2]).points(npointsperface)) for (p1,p2) in pairs(Polygon.rectangle(x1,y1,x2,y2).points())]
        return GeoQuad(faces[0],faces[1],faces[2].reverse(),faces[3].reverse())

    @staticmethod
    def circle(center = Point(0.5,0.5),size = 1.0,npointsperface = 10):
        polygon = Circle(center,size/2.0).polygon(npointsperface*4).close()
        return GeoQuad(polygon.subline(0.0,0.25),polygon.subline(0.25,0.5),polygon.subline(0.5,0.75).reverse(),polygon.subline(0.75,1.0).reverse())


    #
    # split the quad in 2 horizontally, returning 2 subquads
    #
    def ysplit(self,abscissa=0.5):
        (newleft1,newleft2)   = self.mleft.split(abscissa=abscissa)
        (newright1,newright2) = self.mright.split(abscissa=abscissa)
        newup1 = self.ycurve(abscissa)
        return (GeoQuad(newleft1,newup1,newright1,self.mdown),GeoQuad(newleft2,self.mup,newright2,newup1))

    def xsplit(self,abscissa=0.5):
        (newup1,newup2)     = self.mup.split(abscissa=abscissa)
        (newdown1,newdown2) = self.mdown.split(abscissa=abscissa)
        newleft1 = self.xcurve(abscissa)
        return (GeoQuad(self.mleft,newup1,newleft1,newdown1),GeoQuad(newleft1,newup2,self.mright,newdown2))

    def xysplit(self,x=0.5,y=0.5):
        newx1,newx2 = self.xsplit(x)
        result = []
        for newx in self.xsplit(x):
            ysplit = newx.ysplit(y)
            result.extend([ysplit[0],ysplit[1]])
        return result

    def reduce(self,amount):
        margin = (1.0 - amount) * 0.5
        frame = [self.xcurve(margin), 
                 self.ycurve(1.0-margin),
                 self.xcurve(1.0-margin),
                 self.ycurve(margin)]
        frame = [curve.subline(margin,1.0-margin) for curve in frame]
        return GeoQuad(frame[0],frame[1],frame[2],frame[3])

    #
    # mapping
    #
    def mappolygon(self,polygon):
        return Polygon([self.ypoint(p) for p in polygon.points()])

    def unmappolygon(self,polygon):
        newpoints = [self.unmappoint(point) for point in polygon.points()]
        return Polygon(newpoints)

    def unmappoint(self,point):
        if self.mgeoquadtree == None:
            puts("build mgeoquadtree")
            self.mgeoquadtree = GeoQuadTree(self)
            puts("mgeoquadtree built")
        leaf = self.mgeoquadtree.leaf(point,self.mpolygon.length()/1000.0)
        if leaf != None:
            puts("point ", point.coords(),"found")
            return leaf.center()
        return None


