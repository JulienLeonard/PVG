from geoutils import *

class Polyline:
    def __init__(self,points):
        self.mpoints  = points[:]
        self.mlengths = []
        self.mlength  = -1

    def points(self):
        return self.mpoints

    def samples(self,npoints):
        return [self.point(abs) for abs in samples((0.0,1.0),npoints)]

    def lengthsamples(self,size):
        result = []
        cabs = 0.0
        while cabs < self.length():
            result.append(self.point(cabs))
            cabs += size
        result.append(self.point(1.0))
        return result
    
    def lengths(self):
        self.checklengths()
        return self.mlengths

    def length(self):
        self.checklengths()
        return self.mlength
        
    def checklengths(self):
        if len(self.mlengths) == 0:
            self.computelengths()
        
    def computelengths(self):
        result = [[0.0,self.mpoints[0]]]
        mylength = 0.0
        for p1,p2 in pairs(self.mpoints):
            mylength += vlength(vector(p1,p2))
            result.append([mylength,p2])
            
        self.mlength = mylength
        if self.mlength == 0.0:
            self.mlengths.append([0.0,self.mpoints[0]])
            for p in self.mpoints[1:]:
                self.mlengths.append([1.0,p])
        else:
            for item in result:
                self.mlengths.append([item[0]/mylength,item[1]])

    def segment(self,t):
        self.checklengths()
        # print "lengths",self.lengths
        if (t >= 1.0):
            return [self.mlengths[-2],self.mlengths[-1]]
        elif (t <= 0.0):
            return [self.mlengths[0],self.mlengths[1]]
        for i1,i2 in pairs(self.mlengths):
            # print "i1",i1,"i2",i2
            if (i1[0] <= t and t < i2[0]):
                return (i1,i2)

    def curvabscissa(self,pointindex):
        self.checklengths()
        return self.mlengths[pointindex][0]

    def point(self,t):
        if len(self.mpoints) == 1:
            return self.mpoints[0]
        i1,i2 = self.segment(t)
        result = self._point(t,i1,i2)
        return result

    def _point(self,t,i1,i2):
        return psample((i1[1],i2[1]),abscissa((i1[0],i2[0]),t))

    def tangent(self,t):
        if len(self.mpoints) == 1:
            return (0.0,0.0)
        i1,i2 = self.segment(t)
        return self._tangent(t,i1,i2)

    def _tangent(self,t,i1,i2):
        return vector(i1[1],i2[1])

    def normal(self,t):
        if len(self.mpoints) == 1:
            return (0.0,0.0)
        return vortho(self.tangent(t))

    def frame(self,t):
        i1,i2 = self.segment(t)
        return (self._point(t,i1,i2),self._tangent(t,i1,i2))

    def segments(self):
        return [(p1,p2) for (p1,p2) in pairs(self.mpoints)]

    # return list of subsegments due to intersection
    def subpolylinesfromintersection(self,polyline2):
        segs1 = self.segments()
        segs2 = polyline2.segments()
        result = []
        subresult = []
        differror = min(self.length(),polyline2.length())/10000.0
        isfirstpointinter = False
        firstpoint = self.mpoints[0]
        for seg1 in segs1:
            p11,p12 = seg1
            if len(subresult) == 0 or pdiff(subresult[-1], p11,differror):
                subresult.append(p11)
            inters = []
            for seg2 in segs2:
                p21,p22 = seg2
                inter = raw_intersection(p11,p12,p21,p22)
                if len(inter):
                    print "inter",inter
                    inters.append(inter)
            
            if len(inters):
                # puts("inters",inters)
                sortinter = [(vlength(vector(p11,inter)),inter) for inter in inters]
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

        if pdiff(subresult[-1], p12,differror):
            # print "subresult[-1]",subresult[-1],"p12",p12
            subresult.append(p12)
            result.append(subresult)
        if self.isclosed() and not isfirstpointinter and len(result) > 1:
            # print "merge first and last segments"
            result[-1].extend(result[0])
            result = result[1:]
        return [Polyline(ps) for ps in result]

    def isclosed(self):
        differror = self.length()/10000.0        
        if pequal(self.mpoints[0], self.mpoints[-1],differror):
            return True
        return False
    
    def close(self):
        newpoints = self.mpoints[:]
        if not self.isclosed():
            newpoints.append(self.mpoints[0])
        return Polyline(newpoints)

    def closures(self,polyline2):
        sub1s = self.subpolylinesfromintersection(polyline2)
        sub2s = polyline2.subpolylinesfromintersection(self)
        result = []
        differror = min(self.length(),polyline2.length())/10000.0
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

    def concat(self,polyline2):
        newpoints = self.mpoints[:]
        newpoints.extend(polyline2.points())
        return Polyline(newpoints)


    def rootframes(self):
        result = []
        for p1,p2 in self.segments():
            result.append((p1,vector(p1,p2)))
        result.append((p2,vector(p1,p2)))
        return result              

    def rootnormals(self):
        result = []
        for p1,p2 in self.segments():
            pm = pmiddle([p1,p2])
            result.append((pm,vortho(vnorm(vector(p1,p2)))))
        return result

    def _pointoffset(self,rf,size):
        return padd(rf[0],vscale(vnorm(vortho(rf[1])),size))

    def pointoffset(self,t,size):
        return self._pointoffset(self.frame(t),size)

    def checkoffsetintersections(self,points):
        # now filter according to intersections
        # - build consecutives segs
        segs = [(p1,p2) for p1,p2 in pairs(points)]
        # - then compute intersections
        index = 0
        while index < len(segs)-2:
            s1 = segs[index]
            for (ni,ns) in enumerate(segs[index+2:]):
                #puts("s1",s1,"ns",ns)
                i = raw_intersection(s1[0],s1[1],ns[0],ns[1])
                #puts("intersection point",i)
                if len(i) > 0:
                    if i[0] == 'all':
                        puts("error: offset segs cannot be identicals")
                    else:
                        segs[index]   = (s1[0],i)
                        segs[index+2+ni] = (i,ns[1])
                        segs = lconcat(segs[:index+1],segs[index+2+ni:])
            else:
                index += 1

        newresult = [s[0] for s in segs]
        newresult.append(segs[-1][1])
        return newresult

    def offset(self,size):
        result = []
        for p1,p2 in pairs(self.mpoints):
            v = vector(p1,p2)
            if vlength(v) > 0.0001:
                v = vscale(vnorm(vortho(v)),size)
                result.append(padd(p1,v))
                result.append(padd(p2,v))
        
        newresult = [result[0]]
        for p in result[1:]:
            if (vlength(vector(newresult[-1],p)) > 0.01):
                newresult.append(p)
        
        result = self.checkoffsetintersections(newresult)

        newresult = [result[0]]
        for p in result[1:]:
            if (vlength(vector(newresult[-1],p)) > 0.01):
                newresult.append(p)


        # print "newresult",newresult
        return Polyline(newresult)

    def offsetf(self,f):
        result = []
        index = 0;
        # points = [self.point(t) for t in usamples(30)]
        for p1,p2 in pairs(self.mpoints):
            if not pequal(p1,p2,0.01):
                v = vnorm(vortho(vector(p1,p2)))
                v1 = vscale(v,f.y(self.curvabscissa(index)))
                v2 = vscale(v,f.y(self.curvabscissa(index+1)))
                result.append(padd(p1,v1))
                result.append(padd(p2,v2))
            index += 1
        newresult = [result[0]]
        for p in result[1:]:
            if not pequal(newresult[-1],p,0.001):
                newresult.append(p)
        
        #result = self.checkoffsetintersections(newresult)
        #newresult = result

        if False:
            newresult = [result[0]]
            for p in result[1:]:
                if (vlength(vector(newresult[-1],p)) > 0.01):
                    newresult.append(p)
            result = newresult

            newresult = [result[0]]
            cdist = dist(result[0],result[-1])
            index = 1
            for p in result[1:]:
                if dist(p,newresult[-1]) < cdist/100.0:
                    newresult.append(p)
                else:
                    if index < len(result) -1:
                        newresult.append(pmiddle([result[index-1],result[index+1]]))
                index +=1
        # print "newresult",newresult
        return Polyline(newresult)

    def reverse(self):
        newpoints = self.mpoints[:]
        newpoints.reverse()
        return Polyline(newpoints)

    def edges(self):
        return [(i,j) for (i,j) in pairs(self.mpoints)]

    def subline(self,t1_,t2_):
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
        for (t,p) in self.mlengths:
            if (t > t1 and t < t2): 
                result.append(p)
        pointend = self.point(t2)
        result.append(pointend)
        if sens < 0.0:
            result = lreverse(result)
        return Polyline(result)

    def sublines(self,ts):
        return [self.subline(t1,t2) for (t1,t2) in pairs(ts)]
                
    def addline(self,size):
        result = self.mpoints[:]
        p1 = result[-2]
        p2 = result[-1]
        newp = padd(p2,vscale(vnorm(vector(p1,p2)),size))
        result.append(newp)
        return Polyline(result)
    
    def reduce(self,factor):
        return Polyline(preduce(self.mpoints,factor))

    def y(self,t):
        return self.point(t)[1]

    def translate(self,v):
        return Polyline([padd(p,v) for p in self.points()])

    def rotate(self,center,angle):
        return Polyline([protate(p,center,angle) for p in self.points()])
    
    def scale(self,center,factor):
        return Polyline([padd(center,vscale(vector(center,p),factor)) for p in self.points()])

    def symx(self,x):
        return Polyline([(2.0*x-p[0],p[1])for p in self.points()])

    def viewbox(self):
        return viewboxpoints(self.points())


def polylinefromradiusangle(origin,radiuss,angles):
    result = [origin]
    for r,a in zip(radiuss,angles):
        result.append(padd(result[-1],(r*math.cos(a),r*math.sin(a))))
    return Polyline(result)
    
