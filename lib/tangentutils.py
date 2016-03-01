from utils    import *
from geoutils import *
from quadtree import *

def nextadjcircle(circle, angle, radius):
    newcenter = circle.center().add(Vector.VX0().rotate(angle).scale(circle.radius() + radius))
    # newcenter = circle.center().add(Vector.VX0().rotate(angle).scale(radius))
    return Circle(newcenter,radius)

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
    x1,y1,r1 = c1.coords()
    x2,y2,r2 = c2.coords()
    s3 = vector(c2.center(),c1.center())
    # l3 = r1 + r2
    l3 = s3.length()
    isens = 1.0
    if type1 == "IN" or type2 == "IN":
        isens = -1.0
    l1 = r1 + isens*radius
    l2 = r2 + radius
    denom = (2.0 * l2 * l3)
    if denom == 0.0:
        # puts("circles2tangent: error with circles",c1.coords(),c2.coords())
        return None
    cosv = (l3 * l3 - l1 * l1 + l2 * l2)/denom
    if cosv < -1.0 or cosv > 1.0:
        # print "cosv ",cosv
        return None
    angle = math.acos( cosv ) * side
    vnew  = s3.rotate(angle).normalize().scale(l2)
    newcenter = c2.center().add(vnew)
    return Circle(newcenter,radius)

def circles2tangentout(c1,c2,radius,side):
    return circles2tangent(c1,"OUT",c2,"OUT",radius,side)

def arecirclestangent(c1,c2,sensitivity=0.01):
    return circleintersect(c1,c2,sensitivity)

# compute the relative distance between two circles
def distcircle(c1,c2):
    #puts("distcircle c1",c1,"c2",c2)
    return dist(c1.center(),c2.center())-(c1.radius()+c2.radius())

# computation by optimization
def tritangent(c1,c2,target):
    #puts("tritangent c1",c1,"c2",c2,"target",target)
    pmiddle12 = Segment(c1.center(),c2.center()).middle()
    maxradius = 100.0*vector(pmiddle12,target.center()).length()/2.0
    minradius = (vector(c1.center(),target.center()) - c1.radius() - target.radius())/2.0
    if minradius <= c1.radius()/100.0:
        minradius = c1.radius()/100.0

    # compute best side
    t1a = circles2tangentout(c1,c2,c1.radius(), 1.0)
    if t1a == None:
        return None
    dist1a = distcircle(t1a,target)

    t1b = circles2tangentout(c1,c2,c1.radius(),-1.0)
    if t1b == None:
        return None
    dist1b = distcircle(t1b,target)

    if abs(dist1a) < abs(dist1b): 
        bside = 1.0
    else:
        bside = -1.0;
    #puts("bside",bside,"c1",c1,"minradius",minradius,"maxradius",maxradius)
    
    # then optimize
    tmax = circles2tangentout(c1,c2,maxradius, bside)
    if tmax == None:
        return None
    distmax = distcircle(tmax,target)

    tmin = circles2tangentout(c1,c2,minradius, bside)
    if tmin == None:
        return None
    distmin = distcircle(tmin,target)

    
    rrange = R(minradius,maxradius)
    erange = R(abs(distmin),abs(distmax))
    error  = lmin([abs(distmin),abs(distmax)])
    criteria = target.radius() / 1000.0
    niter = 0
    #puts("criteria",criteria)
    while(lmin(erange) > criteria):
        newr   = rrange.mean()
        newdist = distcircle(circles2tangentout(c1,c2,newr, bside),target)
        if newdist > 0.0:
            rrange = R(newr,rrange.v2())
            erange = R(abs(newdist),erange.v2()) 
        else:
            rrange = R(rrangen.v1(),newr)
            erange = R(erange.v1(),abs(newdist))
        #puts ("newdist",newdist)
        niter += 1
        if niter > 100:
            return []
        

    if erange.v1()<erange.v2():
        rradius = rrange.v1()
    else:
        rradius = rrange.v2()

    result = circles2tangentout(c1,c2,rradius, bside) 
    #puts("tritangent result",result)
    return result

def buildcrown(c,v,rlist,angle0 = 0.0):
    centerr = r
    newr    = v*rlist[0]
    fcenter = c.center().add( V0.rotate(angle0).scale(centerr + newr))
    fcircle = Circle(fcenter,newr)
    result = [fcircle]
    ncircle = fcircle[:]
    for r in rlist[1:]:
        ncircle = circles2tangentout(c,ncircle,r*v, 1.0)
        result.append(ncircle)
    return result


def crown_dist(c,v,rlist):
    centerr = c.radius()
    if v < 0.0001:
        result = centerr * 1000.0
    else:
        ccs = buildcrown(c,v,rlist)
        rsum = sum([cc.radius() for cc in ccs])
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
                cc = circles2tangentout(c,cc,cc.radius(), 1.0)
                result += 1.0
        # puts("crow_dist result",result)
    puts("crown_dist",v,result)
    return result



def crown(c,radiuslist,angle0 = 0.0):
    # compute ratio factor to make it a crown
    from scipy.optimize import minimize_scalar
    centerr = c.radius()
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
    quadtree    =  QuadTree(c.bbox())
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
    cc1 = c1.center()
    cc2 = c2.center()
    v = vector(cc1,cc2)
    r2 = (v.length() - c1.radius() - c2.radius())/2.0
    newcc = cc1.add(v.scale((c1.radius() + r2) / (c1.radius() + c2.radius() + r2 * 2.0)))
    return Circle(newcc,r2)

def segment2circletangent(segment,radius,side):
    v  = segment.vector().normalize().ortho().scale(side * radius)
    cc = segment.middle().add(v)
    return Circle(cc,radius)
