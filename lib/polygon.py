from geoutils  import *
from pointabscissarange import *

#
# class used to manage a seuqnce of points
#
class Polygon:
    def __init__(self,points):
        self.mpoints    = points
        # puts("createpolygon",[p.coords() for p in points])
        self.msegments  = [Segment(p1,p2) for (p1,p2) in pairs(self.mpoints)]
        self.mparanges  = None
        self.mlength    = None

    def points(self,npoints=None,abscissas=None,bylength=None):
        if npoints == None and abscissas == None and bylength == None:
            return self.mpoints
        if not npoints  == None:
            return [self.point(abs) for abs in usamples(npoints)]
        if not abscissas == None:
            return [self.point(abs) for abs in abscissas]
        if not bylength == None:
            return self.lengthsamples(bylength)
        return None

    def point1(self):
        return self.mpoints[0]

    def point2(self):
        return self.mpoints[-1]

    def ext1(self):
        return self.point1()

    def ext2(self):
        return self.point2()

    def pointextremities(self):
        return (self.point1(),self.point2())

    def miny(self):
        return min(self.point1().y(),self.point2().y())

    def minx(self):
        return min(self.point1().y(),self.point2().y())

    def maxy(self):
        return max(self.point1().y(),self.point2().y())

    def maxx(self):
        return max(self.point1().x(),self.point2().x())

    def segments(self,nsegments=None,abscissas=None,bylength=None):
        if nsegments == None and abscissas == None and bylength == None:
            return self.msegments
        if not nsegments == None:
            return [Segment(p1,p2) for (p1,p2) in pairs(self.points(nsegments+1))]
        if not abscissas == None:
            return [Segment(p1,p2) for (p1,p2) in pairs(self.points(abscissas=abscissas))]
        if not bylength == None:
            return [Segment(p1,p2) for (p1,p2) in pairs(self.points(bylength=bylength))]
        return None

    def segment(self,t):
        return self._pointabscissarange(t).segment()
    
    def paranges(self):
        if self.mparanges == None:
            self._computeparanges()
        return self.mparanges

    def bbox(self):
        return points2bbox(self.mpoints)

    def sample(self,t):
        return self.point(t)

    def samples(self,npoints=None,abscissas=None,bylength=None):
        return self.points(npoints,abscissas,bylength)
        
    def lengthsamples(self,size):
        result = []
        cabs = 0.0
        rlength = R(0.0,self.length())
        while cabs < self.length():
            result.append(self.point(rlength.abscissa(cabs)))
            cabs += size
        result.append(self.point(1.0))
        return result
    
    def length(self):
        if self.mlength == None:
            self._computeparanges()
        return self.mlength
        
    def _computeparanges(self):
        self.mparanges = []
        result  = []
        olength = 0.0
        for seg in self.segments():
            # puts("seg",seg,"coords",seg.coords())
            clength = olength + seg.length()
            result.append((olength,clength,seg))
            olength = clength
            
        finallength = olength
        self.mlength = finallength
        if self.mlength == 0.0:
            self.mparanges.append(PointAbscissaRange(0.0,1.0,Segment(self.points()[0],self.points()[0])))
            for seg in self.segments()[1:]:
                self.mparanges.append(PointAbscissaRange(1.0,1.0,seg))
        else:
            for (t1,t2,seg) in result:
                self.mparanges.append(PointAbscissaRange(t1/finallength,t2/finallength,seg))

    def _pointabscissarange(self,t):
        if (t >= 1.0):
            return self.paranges()[-1]
        elif (t <= 0.0):
            return self.paranges()[0]
        for parange in self.paranges():
            if parange.contain(t):
                return parange
        return None

    # def curveabscissa(self,pointindex):
    #     if pointindex == 0:
    #         return 0.0
    #     else:
    #         return self.paranges()[pointindex].a2()

    def point(self,t):
        if len(self.mpoints) == 1:
            return self.mpoints[0]
        return self._pointabscissarange(t).sample(t)

    def tangent(self,t):
        if len(self.mpoints) == 1:
            return Vector(0.0,0.0)
        return self._pointabscissarange(t).vector()

    def normal(self,t):
        if len(self.mpoints) == 1:
            return Vector(0.0,0.0)
        return self.tangent(t).ortho()

    def frame(self,t):
        parange = self._pointabscissarange(t)
        return (parange.point(t),parange.vector())


    # return list of subsegments due to intersection
    def subpolygonsfromintersection(self,polygon2):
        segs1 = self.segments()
        segs2 = polygon2.segments()
        result = []
        subresult = []
        differror = min(self.length(),polygon2.length())/10000.0
        isfirstpointinter = False
        firstpoint = self.mpoints[0]
        for seg1 in segs1:
            p11 = seg1.p1()
            if len(subresult) == 0 or pdiff(subresult[-1], p11,differror):
                subresult.append(p11)
            inters = []
            for seg2 in segs2:
                inter = Segment.intersection(seg1,seg2)
                if not inter == None:
                    print "inter",inter.coords()
                    inters.append(inter)

            # puts("seg1",seg1.coords(),"inters",inters)
            if len(inters):
                sortinter = [(vector(p11,inter).length(),inter) for inter in inters]
                sortinter.sort()
                llo = 0.0
                if sortinter[0][0] == 0.0 and p11 == firstpoint:
                    isfirstpointinter = True
                for ll,inter in sortinter:
                    if ll - llo > differror:
                        subresult.append(inter)
                        # print "append subresult len",len(subresult),subresult[0],subresult[-1]
                        result.append(subresult[:])
                        subresult = [inter]
                    llo = ll

        p11 = seg1.p2()
        if pdiff(subresult[-1], p12,differror):
            # print "subresult[-1]",subresult[-1],"p12",p12
            subresult.append(p12)
            result.append(subresult)
        if self.isclosed() and not isfirstpointinter and len(result) > 1:
            # print "merge first and last segments"
            result[-1].extend(result[0])
            result = result[1:]

        puts("subpolygonsfromintersection result",len(result))
        return [Polygon(ps) for ps in result]

    def isclosed(self):
        differror = self.length()/10000.0        
        if pequal(self.mpoints[0], self.mpoints[-1],differror):
            return True
        return False
    
    def close(self):
        newpoints = self.mpoints[:]
        if not self.isclosed():
            newpoints.append(self.mpoints[0])
        return Polygon(newpoints)

    #
    # TOCHECK
    #
    def closures(self,polygon2):
        sub1s = self.subpolygonsfromintersection(polygon2)
        sub2s = polygon2.subpolygonsfromintersection(self)
        result = []
        differror = min(self.length(),polygon2.length())/10000.0
        for sub1 in sub1s:
            p1a,p1b = [sub1.points()[0],sub1.points()[-1]]
            for sub2 in sub2s:
                p2a,p2b = [sub2.points()[0],sub2.points()[-1]]
                # print "p1a",p1a,"p1b",p1b,"p2a",p2a,"p2b",p2b,"l1",self.length(),"l2",self.length()
                if pequal(p1a,p2a,differror) and pequal(p1b,p2b,differror):
                    result.append((sub1,sub2.reverse()))
                elif pequal(p1a,p2b,differror) and pequal(p1b,p2a,differror):
                    result.append((sub1,sub2))
        return result

    def concat(self,polygon2):
        oldpoints = self.mpoints[:]
        newpoints = polygon2.points()[:]
        if pequal(oldpoints[-1],newpoints[0]):
            newpoints = newpoints[1:]
        return Polygon(oldpoints + newpoints)

    def rootframes(self):
        result = []
        for seg in self.segments():
            result.append((seg.p1(),seg.vector()))
        result.append((seg.p2(),seg.vector()))
        return result              

    def rootnormals(self):
        result = []
        for seg in self.segments():
            result.append((seg.middle(),seg.vector().normalize().ortho()))
        return result

    def _pointoffset(self,rf,size):
        return rf[0].add(rf[1].ortho().normalize().scale(size))

    def pointoffset(self,t,size):
        return self._pointoffset(self.frame(t),size)

    def checkoffsetintersections(self,points):
        # now filter according to intersections
        # - build consecutives segs
        segs = [Segment(p1,p2) for (p1,p2) in pairs(points)]
        # - then compute intersections
        index = 0
        while index < len(segs)-2:
            s1 = segs[index]
            for (ni,ns) in enumerate(segs[index+2:]):
                #puts("s1",s1,"ns",ns)
                inter = Segment.intersection(s1,ns)
                #puts("intersection point",i)
                if not inter == None:
                    if isinstance(i,Segment):
                        puts("error: offset segs cannot be identicals")
                    else:
                        segs[index]      = Segment(s1.p1(),inter)
                        segs[index+2+ni] = Segment(inter,ns.p2())
                        segs = lconcat(segs[:index+1],segs[index+2+ni:])
            else:
                index += 1

        newresult = [s.p1() for s in segs]
        newresult.append(segs[-1].p2())
        return newresult

    def offset(self,size):
        if self.length() == 0:
            return self
        result = []
        for seg in self.segments():
            v = seg.vector().ortho().normalize().scale(size)
            result.extend([seg.p1().add(v),seg.p2().add(v)])
        
        newresult = [result[0]]
        for p in result[1:]:
            if (vector(newresult[-1],p).length()) > 0.01:
                newresult.append(p)
        
        # result = self.checkoffsetintersections(newresult)
        result = newresult

        newresult = [result[0]]
        for p in result[1:]:
            if (vector(newresult[-1],p).length() > 0.01):
                newresult.append(p)


        # print "newresult",newresult
        return Polygon(newresult)

    # def offsetf(self,f):
    #     result = []
    #     index = 0;
    #     # points = [self.point(t) for t in usamples(30)]
    #     for seg in self.segments():
    #         if not seg.length() < 0.01:
    #             v  = seg.vector().ortho().normalize()
    #             v1 = v.scale(f(self.curveabscissa(index)))
    #             v2 = v.scale(f(self.curveabscissa(index+1)))
    #             result.append(p1.add(v1))
    #             result.append(p2.add(v2))
    #         index += 1
    #     newresult = [result[0]]
    #     for p in result[1:]:
    #         if not pequal(newresult[-1],p,0.001):
    #             newresult.append(p)
        
    #     # print "newresult",newresult
    #     return Polygon(newresult)

    def reverse(self):
        return Polygon(lreverse(self.mpoints))

    def edges(self):
        return self.segments()

    def subline(self,t1_,t2_):
        # puts("subline",t1_,t2_)
        if t1_ < t2_:
            t1 = t1_
            t2 = t2_
            sens = 1.0
        else:
            t1 = t2_
            t2 = t1_
            sens = -1.0
        point0  = self.point(t1)
        result = [point0]
        toadd = False
        for pa in self.mparanges:
            if pa.a2() >= t1 and pa.a2() <= t2 and not pequal(result[-1],pa.point2()):
                result.append(pa.point2())
        pointend = self.point(t2)
        if not pequal(pointend,result[-1]):
            result.append(pointend)
        # puts("result",[p.coords() for p in result])
        if sens < 0.0:
            result = lreverse(result)
        return Polygon(result)

    def sublines(self,ts):
        return [self.subline(t1,t2) for (t1,t2) in pairs(ts)]

    def split(self,ntimes=None,abscissa=None):
        if not ntimes == None:
            return [self.subline(t1,t2) for (t1,t2) in pairs(usamples(ntimes+1))]
        if not abscissa == None:
            return [self.subline(t1,t2) for (t1,t2) in pairs([0.0,abscissa,1.0])]

    def addline(self,size):
        result = self.mpoints[:]
        p1 = result[-2]
        p2 = result[-1]
        newp = p2.add(vector(p1,p2).normalize().scale(size))
        result.append(newp)
        return Polygon(result)
    
    def reduce(self,factor):
        return Polygon(preduce(self.mpoints,factor))

    def x(self,t):
        return self.point(t).x()

    def y(self,t):
        return self.point(t).y()

    def translate(self,v):
        return Polygon([p.add(v) for p in self.points()])

    def rotate(self,center,angle):
        return Polygon([p.rotate(center,angle) for p in self.points()])
    
    def scale(self,factor,center = None):
        if center == None:
            center = self.middle()
        return Polygon([center.add(vector(center,p).scale(factor)) for p in self.points()])

    def symx(self,x):
        return Polygon([Point(2.0*x-p.x(),p.y())for p in self.points()])

    def symy(self,y):
        return Polygon([Point(p.x(),2.0*y-p.y())for p in self.points()])

    def scalex(self,rx):
        middle = self.middle()
        return Polygon([middle.add(vector(middle,p).scalex(rx)) for p in self.points()])

    def scaley(self,ry):
        middle = self.middle()
        return Polygon([middle.add(vector(middle,p).scaley(ry)) for p in self.points()])

    def movex(self,mx):
        return self.translate(Vector(mx,0.0))

    def movey(self,my):
        return self.translate(Vector(0.0,my))

    def viewbox(self):
        return points2bbox(self.points())

    def coords(self):
        return [coord for p in self.points() for coord in p.coords()]

    def signedArea(self):
        signedArea = 0
        for seg in self.segments():
            # TODO: TOCHECK
            signedArea += (seg.p1().x() * seg.p2().y() - seg.p2().x() * seg.p1().y())
        return signedArea / 2
        
    def isClockwise(self):
        return (self.signedArea() < 0.0)

    def clockwise(self):
        if self.isClockwise():
            return self
        else:
            return self.reverse()

    def containpoint(self,point):
        if not self.viewbox().contain(point):
            return False
        else:
            pps = self.points()
            i = 0
            j = len(pps)-1
            result = False
            for i in range(len(pps)):
                if ( ((pps[i].y() > point.y()) != (pps[j].y() > point.y())) and
                     (point.x() < ((pps[j].x() - pps[i].x()) * (point.y() - pps[i].y()) / (pps[j].y() - pps[i].y()) + pps[i].x()) ) ):
                    result = iff(result == False, True, False)
                j = i
            return result
        
    def middle(self):
        return pmiddle(self.points())

    def line(self,width=None):
        if width == None:
            width = self.length()/100.0
        return self.offset(width/2.0).concat(self.offset(-width/2.0).reverse())

    @staticmethod
    def ispolyinside(poly1,poly2):
        for p in poly1.points():
            if not poly2.containpoint(p):
                return False
        return True

    @staticmethod
    def hierachy(polygons):
        containgraph = {}
        for i in range(len(polygons)-1):
            for j in range(i+1,len(polygons)):
                if Polygon.ispolyinside(polygons[i],polygons[j]):
                    containgraph[polygons[i]] = polygons[j]
                elif Polygon.ispolyinside(polygons[j],polygons[i]):
                    containgraph[polygons[j]] = polygons[i]
        
        # TODO: to finish

    @staticmethod
    def fromcoords(coords):
        points = [Point(x,y) for (x,y) in foreach2(coords)]
        return Polygon(points)


    @staticmethod
    def fromRadiusAngle(origin,radiuss,angles):
        result = [origin]
        for r,a in zip(radiuss,angles):
            result.append(result[-1].add(angle2vector(a).scale(r)))
        return Polygon(result)
    
    @staticmethod
    def square(center = Point.P0(), size = 1.0):
        return Polygon([Point(center.x()-size/2.0,center.y()-size/2.0),
                        Point(center.x()-size/2.0,center.y()+size/2.0),
                        Point(center.x()+size/2.0,center.y()+size/2.0),
                        Point(center.x()+size/2.0,center.y()-size/2.0)]).close()
    
    @staticmethod
    def rectangle(x1,y1,x2,y2):
        return Polygon([Point(x1,y1),Point(x2,y1),Point(x2,y2),Point(x1,y2)]).close()

    @staticmethod
    def middlex(polygon):
        return polygon.middle().x()

    #
    # WARNING: only works for convex polygons
    #
    @staticmethod
    def contain(poly1,poly2):
        for p in poly2.points():
            if not poly1.containpoint(p):
                return False
        return True
            
    #
    # shift polygon description by abscissa (for closed polygons)
    #
    def shift(self,abscissa):
        return self.subline(abscissa,1.0).concat(self.subline(0.0,abscissa))


    @staticmethod
    def allconcat(polygons):
        if len(polygons) < 1:
            return None
        result = polygons[0]
        for polygon in polygons[1:]:
            result = result.concat(polygon)
        return result


Polygon.Unitary = Polygon([Point(1.0,0.5),Point(1.0,0.0),Point(0.0,0.0),Point(0.0,1.0),Point(1.0,1.0)]).close()
