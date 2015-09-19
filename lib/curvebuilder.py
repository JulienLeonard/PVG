from utils     import *
from geoutils  import *
from polygon   import *
from bezier    import *

class CurveBuilder:

    @staticmethod
    def enveloppebezierparams(points,factor,angle0,angleend):
        pvs = []
        # compute first 
        p0 = points[0]
        p1 = points[1]
        v0 = vector(p0,p1).rotate(angle0).scale(1.0/factor)
        pvs.extend([p0,v0])

        for p0,p1,p2 in triplets(points):
            v = vector(p1,p0).normalize().add(vector(p1,p2).normalize()).normalize().ortho()
            pvs.extend([p1,v.scale( vector(p1,p0).length() / factor)])
            pvs.extend([p1,v.scale(-vector(p1,p2).length() / factor)])

        # compute last
        p0 = points[-2]
        p1 = points[-1]
        vend = vector(p1,p0).rotate(angleend).scale(1.0/factor)
        pvs.extend([p1,vend])
        return pvs


    @staticmethod
    def enveloppe(points,factor,angle0,angleend):
        pvs = CurveBuilder.enveloppebezierparams(points,factor,angle0,angleend)
        ppoints = [point for (p0,v0,p1,v1) in lsplit(pvs,4) for point in  bezierfrompointvector(p0,v0,p1,v1).polygon().points()[:-1]]
        return Polygon(ppoints)

    @staticmethod
    def smooth(points):
        pvs = []
        p0 = points[0]
        p1 = points[1]
        mp01 = pmiddle([p0,p1])
        v = vscale(vector(p0,p1),0.5*1.0/3.0)
        pvs.extend([p0,v,mp01,vscale(v,-1.0)])

        for p0,p1,p2 in triplets(points):
            mp01 = pmiddle([p0,p1])
            mp12 = pmiddle([p1,p2])
            v01  = vscale(vector(p1,p0),-0.5*1.0/3.0)
            v02  = vscale(vector(p1,p2),-0.5*1.0/3.0)
            pvs.extend([mp01,v01,mp12,v02])

        p0 = points[-2]
        p1 = points[-1]
        mp01 = pmiddle([p0,p1])
        v = vscale(vector(p0,p1),0.5*1.0/3.0)
        pvs.extend([mp01,v,p1,vscale(v,-1.0)])

            
        ppoints = [bezierfrompointvector(p0,v0,p1,v1).polygon().points[:-1] for (p0,v0,p1,v1) in lsplit(pvs,4)]
        return Polygon(lflatten(ppoints))

    @staticmethod
    def extensionbezier(bezier):
        # algo: extend bezier curve by a regular curve
        fpoint  = bezier.firstpoint()
        lpoint  = bezier.lastpoint()
        lvector = vscale(bezier.lastvector(),1.0)
        newvector = vscale(lvector,-1.0)
        pv        = vector(lpoint,fpoint)
        angle     = vsangle(lvector,pv)
        newpoint  = padd(lpoint,vscale( vnorm(vrotate(newvector,angle)) ,vlength(lvector) * 3.0))
        newlvector = vscale(vrotate(vnorm(vector(newpoint,lpoint)),angle),vlength(lvector))
        return bezierfrompointvector(lpoint,newvector,newpoint,newlvector)

    @staticmethod
    def extensionline(bezier):
        # algo: extend bezier curve by a regular curve
        fpoint   = bezier.firstpoint()
        lpoint   = bezier.lastpoint()
        lvector  = vscale(bezier.lastvector(),-1.0)
        newpoint = padd(lpoint,vscale(lvector,3.0)) 
        return bezierfrompointvector(lpoint,lvector,newpoint,lvector)

    @staticmethod
    def interline(line1,line2,t):
        return Polygon([Segment(line1.point(i),line2.point(i)).sample(t) for i in usamples(100)])

    @staticmethod
    def interlinemap(up,down,left,right,factor):
        polygon = CurveBuilder.interline(up,down,factor)
        result   = CurveBuilder.mapline(polygon,left.point(factor),right.point(factor))
        return result

    @staticmethod
    def mapline(polygon,ext1,ext2):
        v1 = vector(polygon.points()[0],polygon.points()[-1])
        v2 = vector(ext1,ext2)
        center = polygon.points()[0]
        result1 = polygon.translate(vector(center,ext1))
        #print "translate points ",result1.points()
        angle = vsangle(v2,v1)
        #print "angle ",angle
        result2 = result1.rotate(ext1,angle)
        #print "rotate points ",result2.points()
        if v1.length() == 0.0:
            factor = 0.0
        else:
            factor = v2.length()/v1.length()
        #print "factor ",factor
        result = result2.scale(factor,ext1)
        #print "scale points ",result.points()
        return result


    @staticmethod
    def smoothintercurve(poly1,poly2,t12,t23,reverse=1.0):
        pb1 = poly1.point(1.0-t12)
        pb2 = poly2.point(t23)
        v1  = vscale(vnorm(poly1.tangent(1.0-t12)),vlength(vector(pb1,pb2)) * reverse *1.0/3.0)
        v2  = vscale(vnorm(poly2.tangent(t23)),vlength(vector(pb1,pb2)) * reverse *-1.0/3.0)
        return [poly1.subline(0.0,1.0-t12),bezierfrompointvector(pb1,v1,pb2,v2).polygon(),poly2.subline(t23,1.0)]

    @staticmethod
    def closingbezier(poly1,poly2):
        f1 = poly1.frame(1.0)
        f2 = poly2.frame(0.0)
        p1,v1 = f1
        p2,v2 = f2
        tan1 = vscale(vnorm(v1),vlength(vector(p1,p2))*1.0/3.0)
        tan2 = vscale(vnorm(v2),vlength(vector(p1,p2))*-1.0/3.0)
        bezier = bezierfrompointvector(p1,tan1,p2,tan2)
        return bezier.polygon()

    @staticmethod
    def multiinterline(abslines,t):
        for (v1,v2) in pairs(abslines):
            if t < v1[0]:
                return v1[1]
            elif t < v2[0]:
                absc = abscissa((v1[0],v2[0]),t)
                return cls.interline(v1[1],v2[1],absc)
        return abslines[-1][-1]

    @staticmethod
    def ondulation(support,absoffsets):
        offrames = [(support.pointoffset(t,offset * support.length()),support.tangent(t)) for (t,offset) in absoffsets]
        pvs = []
        for (o1,o2) in offrames:
            pvs = lconcat(pvs,[o1,o2])
        return regularbezierpolygonfrompointsvectors(pvs)

    @staticmethod
    def rounded(facepolygons,ratio):
        result      = []
        for (poly1,poly2) in pairs(facepolygons[1:] + [facepolygons[0]]):
            result.append(poly1.subline(ratio,1.0-ratio))
            result.append(Bezier(poly1.point(1.0-ratio),poly1.point(1.0),poly2.point(0.0),poly2.point(ratio)).polygon())
        return Polygon.allconcat(result)
    
    @staticmethod
    def symy(curve,extremityend=True,join=False):
        if extremityend:
            result =  curve.symy(curve.point2().y())
        else:
            result =  curve.symy(curve.point1().y())
            
        if join:
            if extremityend:
                result = curve.concat(result)
            else:
                result = result.concat(curve)
        return result

    @staticmethod
    def symx(curve,extremitxend=True,join=False):
        if extremitxend:
            result =  curve.symx(curve.point2().x())
        else:
            result =  curve.symx(curve.point1().x())
            
        if join:
            if extremitxend:
                result = curve.concat(result)
            else:
                result = result.concat(curve)
        return result


    #
    # build a hump between 2 points
    #
    @staticmethod
    def hump(p1,p2,heightratio = 0.1,abscissa = 0.5):
        s = Segment(p1,p2)
        
        pnew = s.sample(abscissa).add(s.vector().ortho().scale(heightratio))

        vbup   = s.vector().scale(1.0/6.0)
        vbdown = vbup.scale(-1.0)

        beziers = [Bezier(p1,p1.add(vbup),pnew.add(vbdown),pnew), Bezier(pnew,pnew.add(vbup),p2.add(vbdown),p2)]
        return Polygon.allconcat(map(Bezier.polygon,beziers))


#
# curve range
#
class CR:    

    def __init__(self,c1,c2):
        self.mv1 = c1
        self.mv2 = c2

    def sample(self,t):
        return CurveBuilder.interline(self.mv1,self.mv2,t)

    def samples(self,ncurves=None,abscissas=None):
        if not ncurves == None:
            return [self.sample(t) for t in usamples(ncurves)]
        if not abscissas == None:
            return [self.sample(t) for t in abscissas]
        return None

    def lines(self,ncurves=None,abscissas=None):
        return [line.line() for line in self.samples(ncurves,values)]


def curveRange(self,abs1 = 0.0, abs2 = 0.5):
    base = self
    if not self.isclosed():
        base = self.close()
    line1 = base.subline(abs1,abs2)
    line2 = base.subline(1.0,abs2)
    return CR(line1,line2)

Polygon.curveRange = curveRange


def polygon_maponpoints(self,p1,p2):
    return CurveBuilder.mapline(self,p1,p2)

Polygon.maponpoints = polygon_maponpoints
