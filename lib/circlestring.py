from utils import *
from geoutils import *
from tangentutils import *
from polyline import *

def circlestring(polyline,circlesize):
    incr = circlesize/polyline.length()
    sabs = 0.0
    point = polyline.point(sabs)
    result = []
    while (sabs <= 1.0):
        newabs   = sabs + incr
        newpoint = polyline.point(newabs) 
        ncenter = pmiddle([point,newpoint])
        r = vlength(vector(point,newpoint))/2.0
        if len(result) != 0:
            pcenter = (result[-1][0],result[-1][1])
            nr = vlength(vector(pcenter,ncenter))-result[-1][2]
            if nr > 0.8 * r:
                r = nr
        result.append((ncenter[0],ncenter[1],r))
        sabs = newabs
        point = newpoint 
        # print "sabs ",sabs
    return result

def circlestring2(polygon,circlesize):
    ncircles = int(polygon.length()/circlesize)
    points   = polygon.samples(ncircles+1)
    # puts("points",points)
    result = [circlefromdiameter(p1,p2) for (p1,p2) in pairs(points)]
    return result

def circlestring3(polygon,ncircles):
    points = polylgon.samples(ncircles + 1)
    # puts("points",points)
    result = [circlefromdiameter(p1,p2) for (p1,p2) in pairs(points)]
    return result


def circlestringfrompattern(polyline,sizelist):
    totalsum = sum(sizelist)
    sabs = 0.0
    point = polyline.point(sabs)
    result = []
    for newsize in sizelist:
        newabs   = sabs + (newsize / totalsum)
        newpoint = polyline.point(newabs) 
        ncenter = pmiddle([point,newpoint])
        r = vlength(vector(point,newpoint))/2.0
        if len(result) != 0:
            pcenter = (result[-1][0],result[-1][1])
            nr = vlength(vector(pcenter,ncenter))-result[-1][2]
            if nr > 0.8 * r:
                r = nr
        result.append((ncenter[0],ncenter[1],r))
        sabs = newabs
        point = newpoint 
        # print "sabs ",sabs
    return result




def closecirclestring(circlestring):
    return lconcat(circlestring,[circlebetween(circlestring[0],circlestring[-1])])
        
def seedsfromcircles(circles,sides):
    result = []
    for (c1,c2) in pairs(circles):
        if arecirclestangent(c1,c2):
            for side in sides:
                result.append([c1,c2,side])
    return result

def seedsfromcirclesall(circles,sides):
    result = []
    for i in range(len(circles)-1):
        ci = circles[i]
        for cj in circles[i+1:]:
            if arecirclestangent(ci,cj):
                for side in sides:
                    result.append([ci,cj,side])
    return result

def seedsfromcircleadj(adj,sides):
    result = []
    for ci in adj.circles():
        for cj in adj.adjcircles(ci):
            for side in sides:
                result.append([ci,cj,side])
    return result


def seedsfromcirclestring(circles,sides,n=2):
    result = []
    for cs in foreachn(circles,n):
        c1,c2 = cs[0:2]
        if arecirclestangent(c1,c2):
            for side in sides:
                result.append((c1,c2,side))
    return result
