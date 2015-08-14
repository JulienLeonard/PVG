import math
import random
from geoutils import *
from quadtree import *

def nextadjcircle(circle, angle, radius):
    x,y,r = circlecoords(circle)
    length = r + radius
    newx = x + length*math.cos(angle)
    newy = y + length*math.sin(angle)
    return (newx,newy,radius)

def seqcircle(seed,radiuss,angles):
    circles = [seed]
    for radius,angle in zip(radiuss,angles):
        circles.append( nextadjcircle( circles[-1],angle,radius))

    result = []
    angles.extend("")
    for circle,angle in zip(circles,angles):
        result.append((circle,angle))
    return result

def lrepeatadd(seq,seq2):
    result = []
    for item2 in seq2:
        result.extend([(item + item2) for item in seq])
    return result

def circles2tangent(c1,type1,c2,type2,radius,side):
    x1,y1,r1 = circlecoords(c1)
    x2,y2,r2 = circlecoords(c2)
    s3 = Vector().points(c2.center(),c1.center())
    # l3 = r1 + r2
    l3 = s3.length()
    isens = 1.0
    if type1 == "IN" or type2 == "IN":
        isens = -1.0
    l1 = r1 + isens*radius
    l2 = r2 + radius
    denom = (2.0 * l2 * l3)
    if denom == 0.0:
        puts("circles2tangent: error with circles",c1.list(),c2.list())
        return None
    cosv = (l3 * l3 - l1 * l1 + l2 * l2)/denom
    if cosv < -1.0 or cosv > 1.0:
        # print "cosv ",cosv
        return None
    angle = math.acos( cosv ) * side
    vnew = s3.rotate(angle).normalize().scale(l2)
    newcenter = c2.center().add(vnew)
    return Circle(newcenter,radius)

def arecirclestangent(c1,c2,sensitivity=0.01):
    return circleintersect(c1,c2,sensitivity)

# compute the relative distance between two circles
def distcircle(c1,c2):
    #puts("distcircle c1",c1,"c2",c2)
    return dist(ccenter(c1),ccenter(c2))-(cradius(c1)+cradius(c2))

# computation by optimization
def tritangent(c1,c2,target):
    #puts("tritangent c1",c1,"c2",c2,"target",target)
    pmiddle12 = pmiddle([ccenter(c1),ccenter(c2)])
    maxradius = 100.0*dist(pmiddle12,ccenter(target))/2.0
    minradius = (dist(ccenter(c1),ccenter(target)) - cradius(c1) - cradius(target))/2.0
    if minradius <= cradius(c1)/100.0:
        minradius = cradius(c1)/100.0

    # compute best side
    t1a = circles2tangent(c1,"OUT",c2,"OUT",cradius(c1), 1.0)
    if not len(t1a) > 0:
        return []
    dist1a = distcircle(t1a,target)
    t1b = circles2tangent(c1,"OUT",c2,"OUT",cradius(c1),-1.0)
    if not len(t1b) > 0:
        return []
    dist1b = distcircle(t1b,target)
    if abs(dist1a) < abs(dist1b): 
        bside = 1.0
    else:
        bside = -1.0;
    #puts("bside",bside,"c1",c1,"minradius",minradius,"maxradius",maxradius)
    
    # then optimize
    tmax = circles2tangent(c1,"OUT",c2,"OUT",maxradius, bside)
    if not len(tmax) > 0:
        return []
    distmax = distcircle(tmax,target)
    tmin = circles2tangent(c1,"OUT",c2,"OUT",minradius, bside)
    if not len(tmin) > 0:
        return []
    distmin = distcircle(tmin,target)
    #puts("distmin",distmin,"distmax",distmax)

    rrange = [minradius,maxradius]
    erange = [abs(distmin),abs(distmax)]
    error = lmin([abs(distmin),abs(distmax)])
    criteria = cradius(target) / 1000.0
    niter = 0
    #puts("criteria",criteria)
    while(lmin(erange) > criteria):
        newr   = lmean(rrange)
        newdist = distcircle(circles2tangent(c1,"OUT",c2,"OUT",newr, bside),target)
        if newdist > 0.0:
            rrange[0] = newr
            erange[0] = abs(newdist) 
        else:
            rrange[1] = newr
            erange[1] = abs(newdist) 
        #puts ("newdist",newdist)
        niter += 1
        if niter > 100:
            return []
        

    if erange[0]<erange[1]:
        rradius = rrange[0]
    else:
        rradius = rrange[1]

    result = circles2tangent(c1,"OUT",c2,"OUT",rradius, bside) 
    #puts("tritangent result",result)
    return result

def buildcrown(c,v,rlist,angle0 = 0.0):
    x,y,r = circlecoords(c)
    centerr = r
    fcenter = padd((x,y),vrotate((centerr+v*rlist[0],0.0),angle0))
    fcircle = (fcenter[0],fcenter[1],v*rlist[0])
    result = [fcircle]
    ncircle = fcircle[:]
    for r in rlist[1:]:
        ncircle = circles2tangent(c,"OUT",ncircle,"OUT",r*v, 1.0)
        result.append(ncircle)
    return result


def crown_dist(c,v,rlist):
    centerr = c[-1]
    if v < 0.0001:
        result = centerr * 1000.0
    else:
        ccs = buildcrown(c,v,rlist)
        rsum = sum([cc[-1] for cc in ccs])
        distfirstlast = distcircle(ccs[0],ccs[-1])
        result = abs(distfirstlast/ccs[0][-1])*rsum
        cross = 0
        for cc in ccs[1:]:
            if distcircle(ccs[0],cc) < -0.01:
                cross = 1
            if cross == 1:
                result += 100.0
        if cross == 0:
            # puts("ccs[-1]",ccs[-1])
            cc = ccs[-1]
            while distcircle(ccs[0],cc) > 0.0:
                # puts("cc",cc)
                cc = circles2tangent(c,"OUT",cc,"OUT",cc[-1], 1.0)
                result += 1.0
        # puts("crow_dist result",result)
    puts("crown_dist",v,result)
    return result



def crown(c,radiuslist,angle0 = 0.0):
    # compute ratio factor to make it a crown
    from scipy.optimize import minimize_scalar
    centerr = c[-1]
    rlist = [float(r) for r in radiuslist]
    puts("rlist",rlist)

    def crown_f(v):
        return crown_dist(c,v/(len(rlist)*2.0),rlist)
    
    res = minimize_scalar(crown_f, method='brent')
    res.x = res.x / (2.0*len(rlist))
    puts("res factor",res.x)
    return buildcrown(c,res.x,rlist,angle0)

def crowntype2(c,radiuslist,factor):
    ccrown = buildcrown(c,factor,radiuslist)
    quadtree    =  QuadTree(100000.0,100000.0)
    for cc in ccrown:
        if not quadtree.iscolliding(cc):
            quadtree.add(cc)
        else:
            return 1
    return -1


def crown2(c,radiuslist):
    centerr = c[-1]
    rlist = [float(r) for r in radiuslist]
    puts("rlist",rlist)

    rsum0 = sum(rlist)
    scalefactor = centerr * 2 * 3.14159 / rsum0

    
    lastvalue0 = scalefactor/2.0
    lastvalue1 = scalefactor * 2.0
    

    lasttangent0 = crowntype2(c,radiuslist,lastvalue0)
    lasttangent1 = crowntype2(c,radiuslist,lastvalue1)
    #puts("lasttangent1",lasttangent1)
    rangesize = lastvalue1 - lastvalue0
    #puts("start iteration layerbao2")
    while abs(rangesize) > 0.000000000000001:
        lastvalue = lmean([lastvalue0,lastvalue1])
        tangent = crowntype2(c,radiuslist,lastvalue)
        # puts("lastvalue0",lastvalue0,"lastvalue1",lastvalue1,"lastvalue",lastvalue,"tangent",tangent)
        
        if tangent == lasttangent0:
            lastvalue0 = lastvalue

        if tangent == lasttangent1:
            lastvalue1 = lastvalue

        rangesize = lastvalue1 - lastvalue0

    return buildcrown(c,lastvalue0,rlist)



def circlebetween(c1,c2):
    cc1 = ccenter(c1)
    cc2 = ccenter(c2)
    v = vector(cc1,cc2)
    r2 = vlength(v) - cradius(c1) - cradius(c2)
    newcc = padd(cc1,vscale(v,(cradius(c1) + r2/2.0) / (cradius(c1) + cradius(c2) + r2)))
    return (newcc[0],newcc[1],r2/2.0)

def segment2circletangent(segment,radius,side):
    v = vortho(vnorm(vector(segment[0],segment[1])))
    if side == -1.0:
        v = vscale(v,-1.0)
    cc = padd(pmiddle((segment[0],segment[1])),vscale(v,radius))
    return (cc[0],cc[1],radius)
