from PVG           import *
from circlepacking import *
from seed          import *

#
# Packing result structure: contain the result of a maximum packing result from a set of seeds (usually from a contour)
#
#
class SeedMaxResult:

    def __init__(self, seed, circle,collider = None):
        self.mseed     = seed
        self.mcircle   = circle
        self.mcollider = collider

    def seed(self):
        return self.mseed

    def circle(self):
        return self.mcircle

    def collider(self):
        return self.mcollider



class MaxPackingResult:
    def __init__(self):
        self.mresults = []

    def add(self,result):
        self.mresults.append(result)

    def circles(self):
        return [result.circle() for result in self.mresults]

    def result(self,index):
        if not index < len(self.result):
            return None
        return self.mresult[index]

    def circle(self,index = None):
        if index == None:
            index = 0
        return self.result(0).circle()


def fidentity(v):
    return v

SeedToCompute  = None
SeedImpossible = -1

#
# compute the maximum sized circles from the seeds and not colliding with the quadtree content
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
# seeds are a list of seed objects
#
def maxcirclesfromseeds(boundaries, seeds, bbox, niter = 1, ftransform = None, frecursive = None):
    quadtree = QuadTree(bbox.resize(20.0))
    quadtree.adds(boundaries)

    rrange   = R(bbox.size()/1000.0,bbox.size())
    result   = MaxPackingResult()
    
    for seed in seeds:
        seed.mresult = None

    for iiter in range(niter):
        puts("iter",iiter)
        rallmax  = 0.0
        maxseed  = None

        # first recompute the max circle from the invalidate seeds
        for seed in seeds:
            if seed.mresult == SeedToCompute and not seed.mresult == SeedImpossible:
                seed.mresult = seed.maxcircle(rrange,quadtree)

        # then compute the new max
        for seed in seeds:
            if not seed.mresult == SeedImpossible:
                if not seed.mresult == SeedToCompute:
                    rrmax =  seed.mresult.circle().radius()
                    if rrmax > rallmax:
                        # puts("new seed max",seed.mresult.circle().coords())
                        rallmax  = rrmax
                        maxseed  = seed
                        
                else:
                    # puts("seed",seed,"no use, mark it")
                    seed.mresult = SeedImpossible
                
        
        # add the new max circle 
        if not maxseed == None:
            # puts("new max circle",crallmax)
            crallmax = maxseed.mresult.circle()
            if frecursive == None:
                if not ftransform == None:
                    crallmax = ftransform(crallmax)
                newcs = [crallmax]
            else:
                (newcs,newseeds) = maxseed.recursive(frecursive,cfcircle)

            for newc in newcs:
                result.add(SeedMaxResult(maxseed,newc))
                quadtree.add(newc)
            
            if not frecursive == None:
                newseeds = TODO
                seeds.extend(newseeds)
                for newseed in newseeds:
                    newseed.mresult = SeedToCompute


            # invalidate the seed circles colliding
            for seed in seeds:
                if not seed.mresult == SeedToCompute and not seed.mresult == SeedImpossible:
                    for newc in newcs:
                        if Shape.intersect(newc,seed.mresult.circle()):
                            # puts("invalidate seed",seed)
                            seed.mresult = SeedToCompute
                            break
        else:
            puts("no more new max circle, stop")
            break
    
    return result


#
# compute tha maximum sized circle from the seeds and not colliding with the quadtree content
#
def maxcirclefromseeds(boundaries,seeds,rrange):
    return maxcirclesfromseeds(boundaries,seeds,rrange).circle()


#
# compute tha maximum sized circles from the seeds and not colliding with the quadtree content, and add in place of the new circles seeds if contour, or normal circle if new seeds
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
def maxcirclesfromseedsrecursive(seeds,quadtree,dmax,niter,ftransformcontour,ftransformpacking):
    rallmax = 0.0
    crallmax = ""
    result = []
    cache = {}
    seedstype = {}

    # init cache
    for seed in seeds:
        cache[seed] = ""
        seedstype[seed] = "contour"

    for iiter in range(niter):
        puts("iter",iiter)
        crallmax = ""
        rallmax = 0.0
        maxseed = ""

        newcache = { seed : cache[seed] for seed in cache if cache[seed] != -1}
        cache = newcache

        # first recompute the max circle from the invalidate seeds
        for seed in cache:
            if cache[seed] == "":
                cache[seed] = computemaxcirclefromseed(quadtree,seed,dmax)

        # then compute the new max
        for seed in cache:
            if cache[seed] != "":
                rrmax =  cradius(cache[seed])
                if rrmax > rallmax and (seedstype[seed] == "contour" or rrmax > 0.25 * min(cradius(seed[0]),cradius(seed[1]))):
                    # puts("new seed max",cache[seed])
                    rallmax  = rrmax
                    crallmax = cache[seed]
                    maxseed  = seed
            else:
                puts("seed",seed,"no use, mark it")
                cache[seed] = -1
                
        
        # add the new max circle 
        if crallmax != "":
            if seedstype[maxseed] == "contour":
                puts("new max circle",crallmax)
                newcs = ftransformcontour(crallmax,maxseed)
                # newcs = [(cfcircle[0] - cradius(cfcircle)/2.0,cfcircle[1],cradius(cfcircle)/2.0),(cfcircle[0] + cradius(cfcircle)/2.0,cfcircle[1],cradius(cfcircle)/2.0)]
                result.extend(newcs)
                quadtree.adds(newcs)
                cache[maxseed] = -1
                newseeds = [(newcs[0],newcs[1],1.0),(newcs[0],newcs[1],-1.0)]
            else:
                cfcircle = ftransformpacking(crallmax,maxseed)
                newcs = [cfcircle]
                result.append(cfcircle)
                quadtree.add(cfcircle)
                cache[maxseed] = -1
                # newseeds = [(cfcircle,maxseed[0],1.0),(cfcircle,maxseed[1],1.0),(cfcircle,maxseed[0],-1.0),(cfcircle,maxseed[1],-1.0)]
                # newseeds = [(cfcircle,maxseed[0],maxseed[-1]),(cfcircle,maxseed[1],-maxseed[-1])]
                newseeds = [(cfcircle,maxseed[0],-maxseed[-1]),(cfcircle,maxseed[1],maxseed[-1])]
            
            for newseed in newseeds:
                cache[newseed] = ""
                seedstype[newseed] = "packing"

            # invalidate the seed circles colliding
            for seed in cache:
                if cache[seed] != "" and cache[seed] != -1:
                    for newc in newcs:
                        if circleintersect(newc,cache[seed]):
                            # puts("invalidate seed",seed)
                            cache[seed] = ""
                            break
        else:
            puts("no more new max circle, stop")
            break
    
    return result


#
# compute tha maximum sized circles from the seeds and not colliding with the quadtree content, and add in place of the new circles seeds if contour, or normal circle if new seeds
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
def maxcirclepacking(seeds,quadtree,dmax,niter,ftransformpacking,minradius):
    rallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}

    # init cache
    for seed in seeds:
        cache[seed] = ""

    for iiter in range(niter):
        if iiter % 100 == 0:
            puts("iter",iiter,"cache size",len(cache))
        crallmax = ""
        rallmax = 0.0
        maxseed = ""

        newcache = { seed : cache[seed] for seed in cache if cache[seed] != -1}
        cache = newcache

        # puts("first recompute the max circle from the invalidate seeds")
        for seed in cache:
            if cache[seed] == "":
                cache[seed] = computemaxcirclefromseed(quadtree,seed,dmax)
                if len(cache[seed]) == 0 or cradius(cache[seed]) < minradius:
                    cache[seed] = -1

        # puts("then compute the new max")
        for seed in cache:
            if cache[seed] != "" and cache[seed] != -1:
                rrmax =  cradius(cache[seed])
                if rrmax > rallmax:
                    # puts("new seed max",cache[seed])
                    rallmax  = rrmax
                    crallmax = cache[seed]
                    maxseed  = seed
            else:
                # puts("seed",seed,"no use, mark it")
                cache[seed] = -1
                
        
        # puts("add the new max circle if not empty")
        if crallmax != "":
            # puts("add the new max circle as not empty")
            cfcircle = ftransformpacking(crallmax,maxseed)
            newcs = [cfcircle]
            # result.append(cfcircle)
            result.addcircleadj(maxseed[0],cfcircle)
            result.addcircleadj(maxseed[1],cfcircle)
            # puts("add in quad tree",cfcircle)
            quadtree.add(cfcircle)
            # puts("added in quad tree")
            cache[maxseed] = -1
            newseeds = [(cfcircle,maxseed[0],1.0),(cfcircle,maxseed[1],1.0),(cfcircle,maxseed[0],-1.0),(cfcircle,maxseed[1],-1.0)]
            # newseeds = [(cfcircle,maxseed[0],maxseed[-1]),(cfcircle,maxseed[1],-maxseed[-1])]
            # newseeds = [(cfcircle,maxseed[0],-maxseed[-1]),(cfcircle,maxseed[1],maxseed[-1])]
            
            for newseed in newseeds:
                cache[newseed] = ""
            
            # puts("invalidate the seed circles colliding")
            for seed in cache:
                if cache[seed] != "" and cache[seed] != -1:
                    for newc in newcs:
                        if circleintersect(newc,cache[seed]):
                            # puts("invalidate seed",seed)
                            cache[seed] = ""
                            break
        else:
            puts("no more new max circle, stop")
            break
    
    return result

#
# compute the maxcircle from a seed
#
def computemaxcirclefromseedcollision(quadtree,seed,dmax,dmin=0.0001):
    rrange = (dmin,dmax)
    crmin = circles2tangent(seed[0],"OUT",seed[1],"OUT",rrange[0], seed[2])
    if quadtree.iscolliding(crmin):
        puts("no circlemin")
        return ""

    lastgoodcircle = ""
    maxcollision = ""

    for j in range(10):
        rrmiddle = lmean(rrange)
        crmiddle = circles2tangent(seed[0],"OUT",seed[1],"OUT",rrmiddle, seed[2])
        if quadtree.iscolliding(crmiddle):
            rrange = (rrange[0],rrmiddle)
            maxcollision = nearestcircle(seed[0],quadtree.colliding(crmiddle),[seed[0],seed[1]])
        else:
            lastgoodcircle = crmiddle
            rrange = (rrmiddle,rrange[1])

    if lastgoodcircle == "":
        return ""
    # puts("computemaxcirclefromseedcollision result",(lastgoodcircle,maxcollision))
    return (lastgoodcircle,maxcollision)


def defaultaddnewcircle(circletype,newcircle):
    circletype[newcircle] = "seed"
    return circletype

#
# return circletype
#
def defaultrefreshcircletype(circletype):
    return circletype

def leveladdnewcircle(circletype,newcircle):
    circletype[newcircle] = "newseed"
    return circletype

def levelrefreshcircletype(circletype):
    for c in circletype:
        if circletype[c] == "newseed":
            circletype[c] = "seed"
    return circletype


#
# compute tha maximum sized circles from the seeds and not colliding with the quadtree content
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
def maxcirclepackingcollision(boundaries,seeds,rseeds,rrange,niter,ftransform,minsize, faddnewcircle = defaultaddnewcircle, frefreshcircletype = defaultrefreshcircletype):
    seeds = elaborateseeds(seeds)

    quadtree   = QuadTree(100000.0,100000.0)
    quadtree.adds(boundaries)
    quadtree.adds(rseeds)
    (dmin,dmax) = rrange
    rallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}
    circletype = {}


    # init cache
    for seed in seeds:
        cache[seed] = ""
    for c in boundaries:
        circletype[c] = "boundary"

    for rseed in rseeds:
        circletype[rseed] = "seed"

    for iiter in range(niter):
        puts("iter",iiter)
        crallmax = ""
        rallmax = 0.0
        maxseed = ""
        maxcollision = ""
        breakonce = False

        # first recompute the max circle from the invalidate seeds
        for seed in seeds:
            if cache[seed] == "" and cache[seed] != -1:
                cache[seed] = seed.maxcircle(rrange,quadtree,withmaxcollision = True)
                if not cache[seed] == "" and cradius(cache[seed][0]) < minsize:
                    cache[seed] = -1
                

        # then compute the new max
        for seed in seeds:
            if cache[seed] != -1:
                if cache[seed] != "":
                    # puts("cache[seed]",cache[seed])
                    rrmax =  cradius(cache[seed][0])
                    if rrmax > rallmax and cache[seed][1] in circletype and (circletype[cache[seed][1]] == "seed"):
                        # puts("new seed max",cache[seed])
                        rallmax  = rrmax
                        crallmax = cache[seed][0]
                        maxseed  = seed
                        maxcollision = cache[seed][1]
                        
                else:
                    # puts("seed",seed,"no use, mark it")
                    cache[seed] = -1
                
        
        # add the new max circle 
        if crallmax != "":
            breakonce = False
            # puts("new max circle",crallmax)
            cfcircle = ftransform(crallmax,maxseed,maxcollision,circletype[maxcollision])
            # result.append(cfcircle)
            quadtree.add(cfcircle)
            # puts("add notseed circle",cfcircle)
            circletype = faddnewcircle(circletype,cfcircle)
            result.addcircleadj(cfcircle,maxcollision)

            # invalidate the seed circles colliding
            for seed in seeds:
                if cache[seed] != "" and cache[seed] != -1:
                    if circleintersect(cfcircle,cache[seed][0]):
                        # puts("invalidate seed",seed)
                        cache[seed] = ""
        else:
            if breakonce == True:
                puts("no more new max circle, stop")
                break
            else:
                puts("level exhausted: refresh seeds")
                breakonce = True
                circletype = frefreshcircletype(circletype)
                

    
    return result


#
# radial maxcircle computation with recursive seed
# seeds is a list of single circles
# quadtree must be filled with contour, and with rseeds
#
def maxcirclespackingangles(seeds,quadtree,dmax,ftransform,niter,nangles,dmin):
    rallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}

    # init cache
    cache = {}
    for seed in seeds:
        cache.update({(seed,angle) : "" for angle in R.angle().samples(nangles+1)[:-1]})

    for iiter in range(niter):
        if iiter % 100 == 0:
            puts("iter",iiter,"cache size",len(cache))
        crallmax = ""
        rallmax = 0.0
        maxseed = ""

        newcache = { seed : cache[seed] for seed in cache if cache[seed] != -1}
        cache = newcache

        # first recompute the max circle from the invalidate seeds
        for seed in cache:
            if cache[seed] == "":
                cache[seed] = computemaxcirclefromseedangle(quadtree,seed,dmax,dmin)

        # then compute the new max
        for seed in cache:
            if cache[seed] != "":
                rrmax =  cradius(cache[seed])
                if rrmax > rallmax:
                    # puts("new seed max",cache[seed])
                    rallmax  = rrmax
                    crallmax = cache[seed]
                    maxseed  = seed
            else:
                # puts("seed",seed,"no use, mark it")
                cache[seed] = -1
                
        
        # add the new max circle 
        if crallmax != "":
            # puts("new max circle",crallmax)
            newc = ftransform(crallmax,maxseed)
            result.addcircleadj(maxseed[0],newc)
            quadtree.add(newc)
            cache[maxseed] = -1
            newseeds = [(newc,angle) for angle in R.angle().samples(nangles+1)[:-1]]
            
            for newseed in newseeds:
                cache[newseed] = ""


            # invalidate the seed circles colliding
            for seed in cache:
                if cache[seed] != "" and cache[seed] != -1:
                    if circleintersect(newc,cache[seed]):
                        # puts("invalidate seed",seed)
                        cache[seed] = ""
        else:
            puts("no more new max circle, stop")
            break
    
    return result



#
#
#
#
def computemaxthreadfromseedangle(quadtree,seed,dmax,dmin):
    ratio = 0.9
    (cseed,aseed) = seed
    newc = nextadjcircle(cseed, aseed, cradius(cseed) * ratio)
    # newc = nextadjcircle(cseed, aseed, 1.0)
    vmax = 0.0
    cresult = []
    maxiter = 100

    while not quadtree.iscolliding(newc) and len(cresult) < maxiter:
        vmax += cradius(newc)
        cresult.append(newc)
        newc = nextadjcircle(newc, aseed, cradius(newc) * ratio)
        # newc = nextadjcircle(newc, aseed, 1.0)
    
    if vmax == 0.0:
        return ""

    cresult = computemaxcirclefromseedangle(quadtree,seed,dmax,dmin)
    if cresult == "":
        return ""

    return (vmax,[cresult])


#
#
# 
#
def maxcirclespackingangleslines(seeds,quadtree,dmax,ftransform,niter,nangles,dmin):
    vallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}

    # init cache
    for seed in seeds:
        cache = {(seed,angle) : "" for angle in R.angle.samples(nangles+1)[:-1]}

    for iiter in range(niter):
        if iiter % 10 == 0:
            puts("iter",iiter,"cache size",len(cache))
        crallmax = ""
        vallmax = 0.0
        maxseed = ""

        newcache = { seed : cache[seed] for seed in cache if cache[seed] != -1}
        cache = newcache

        # first recompute the max circle from the invalidate seeds
        for seed in cache:
            if cache[seed] == "":
                cache[seed] = computemaxthreadfromseedangle(quadtree,seed,dmax,dmin)

        # then compute the new max
        for seed in cache:
            if cache[seed] != "":
                vmax =  cache[seed][0]
                if vmax > vallmax:
                    # puts("new seed max",cache[seed])
                    vallmax  = vmax
                    crallmax = cache[seed][1]
                    maxseed  = seed
            else:
                # puts("seed",seed,"no use, mark it")
                cache[seed] = -1
                
        
        # add the new max circle 
        if crallmax != "":
            # puts("new max circle",len(crallmax))
            newcs = [ftransform(newc,maxseed) for newc in crallmax]
            result.addcircleadj(maxseed[0],newcs[0])
            for (c1,c2) in pairs(newcs):
                result.addcircleadj(c1,c2)
            quadtree.adds(newcs)
            cache[maxseed] = -1
            newseeds = []
            for newc in newcs:
                newseeds = newseeds + [(newc,angle) for angle in R.angle().samples(nangles+1)[:-1]]
            
            for newseed in newseeds:
                cache[newseed] = ""


            # invalidate the seed circles colliding
            for seed in cache:
                if cache[seed] != "" and cache[seed] != -1:
                    intersect = False
                    for newc in newcs:
                        for cachec in cache[seed][1]:
                            # puts("newc",newc,"cachec",cachec)
                            if circleintersect(newc,cachec):
                                # puts("invalidate seed",seed)
                                cache[seed] = ""
                                intersect = True
                                break
                        if intersect:
                            break
        else:
            puts("no more new max circle, stop")
            break
    
    return result

def cacher(vcache):
    if vcache == "":
        return ""
    else:
        return cradius(vcache)
    

#
# find the minimum max circles of a contour
# algo: compute the max circles for all the seeds, then travel the seeds and detect local minimum as result
#
# Prerequisites:
# - seeds must be in sequence
# - if necessary, seeds must be added to quadtree before calling this function
#
def computeminmaxcircles(seeds,quadtree,dmax):
    cache = {}

    # init cache
    for seed in seeds:
        cache[seed] = computemaxcirclefromseed(quadtree,seed,dmax)

    # then travel along the seeds sequence to detect local minimum
    currentminimum = cache[seeds[0]]
    currentmaximum = cache[seeds[0]]
    result = []
    
    for seed in seeds[1:]:
        puts("seed",cacher(cache[seed]),"currentminimum",cacher(currentminimum),"currentmaximum",cacher(currentmaximum))
        if cache[seed] == "":
            puts("max circle empty: nothing to do")
        else:
            if  not currentminimum == "" and cradius(cache[seed]) < cradius(currentminimum):
                currentminimum = cache[seed]
            elif  cradius(cache[seed]) > cradius(currentmaximum):
                currentmaximum = cache[seed]
            elif cradius(cache[seed]) > cradius(currentminimum) and cradius(cache[seed]) < cradius(currentmaximum):
                puts("local minimum detected: add it")
                result.append(currentminimum)
                currentminimum = cache[seed]
                currentmaximum = cache[seed]
            elif cradius(cache[seed]) > cradius(currentminimum) and cradius(cache[seed]) > cradius(currentmaximum):
                currentminimum = cache[seed]
                currentmaximum = cache[seed]
                
    return result

#
# use crossvector to compute if change direction 
#
def computeminmaxcircles2(cstring,side,quadtree,dmax,pathlength = 4):
    cache = []
    # first compute crossproduct aggregation for each path
    ccstring = cstring + cstring[0:pathlength-1]
    for index in range(len(ccstring)-pathlength):
        substring = ccstring[index:index+pathlength]
        
        vsum = 0.0
        for j in range(len(substring)-2):
            (c1,c2,c3)  = substring[j:j+3]
            # puts("c1,c2,c3",c1,c2,c3)
            vsum += pcrossproduct(ccenter(c1),ccenter(c2),ccenter(c3))
        
        cache.append((index,vsum))
        # puts("index",vsum)

    # then return the nmins
    sortlist = sorted(cache,key = lambda pair : pair[1])

    result = []
    for item in lreverse(sortlist):
        # puts("item",item)
        if item[1] > 1.0:
            index = item[0]
            substring = ccstring[index:index+pathlength]
            maxcircle = ""
            cindex = 0
            while maxcircle == "" and cindex < len(substring) - 1:
                maxcircle= computemaxcirclefromseed(quadtree,(substring[cindex],substring[cindex+1],side),dmax)
                cindex += 1
            if not maxcircle == "" :
                result.append(maxcircle)
            else:
                puts("error: place to have min circle but cannot compute it")
                
    return result


#
# compute tha maximum sized circles from the seeds and not colliding with the quadtree content
#
# the difference here is that only one seed at a time can be the seed
#
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
def maxcirclepackingcollisioniter(seeds,rseeds,quadtree,dmax,niter,ftransform,minsize):
    rallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}
    seedtype = {}
    newnodes = rseeds[:]
    resetindex = 0

    # init cache
    for seed in seeds:
        cache[seed] = ""
        (c1,c2,r) = seed
        #puts("add seed type",c1)
        #puts("add seed type",c2)
        seedtype[c1] = "notseed"
        seedtype[c2] = "notseed"
        quadtree.adds([c1,c2])
        result.addcircleadj(seed[0],seed[1])

    for rseed in rseeds:
        seedtype[rseed] = "notseed"
        quadtree.add(rseed)

    for iiter in range(niter):
        puts("iter",iiter)
        crallmax = ""
        rallmax = 0.0
        maxseed = ""
        maxcollision = ""

        # first recompute the max circle from the invalidate seeds
        for seed in seeds:
            if cache[seed] == "" and cache[seed] != -1:
                cache[seed] = computemaxcirclefromseedcollision(quadtree,seed,dmax)

        # then compute the new max
        for seed in seeds:
            if cache[seed] != -1:
                if cache[seed] != "" and cradius(cache[seed][0]) > minsize:
                    # puts("cache[seed]",cache[seed])
                    rrmax =  cradius(cache[seed][0])
                    if rrmax > rallmax and (seedtype[cache[seed][1]] == "notseed"):
                        # puts("new seed max",cache[seed])
                        rallmax  = rrmax
                        crallmax = cache[seed][0]
                        maxseed  = seed
                        maxcollision = cache[seed][1]
                        
                else:
                    # puts("seed",seed,"no use, mark it")
                    cache[seed] = -1
                
        
        # add the new max circle 
        if crallmax != "" and cradius(crallmax) > minsize:
            # puts("new max circle",crallmax)
            cfcircle = ftransform(crallmax,maxseed,maxcollision,seedtype[maxcollision])
            # result.append(cfcircle)
            quadtree.add(cfcircle)
            # puts("add notseed circle",cfcircle)
            seedtype[cfcircle] = "notseed"
            seedtype[maxcollision] = "notseed"
            result.addcircleadj(cfcircle,maxcollision)
            newnodes.append(cfcircle)
            
            for side in [1.0,-1.0]:
                seeds.append((maxcollision,cfcircle,side))
                cache[(maxcollision,cfcircle,side)] = ""

            # invalidate the seed circles colliding
            for seed in seeds:
                if cache[seed] != "" and cache[seed] != -1:
                    if circleintersect(cfcircle,cache[seed][0]):
                        # puts("invalidate seed",seed)
                        cache[seed] = ""
        else:
            puts("no more new max circle, restart")
            # for rseed in rseeds:
            #    seedtype[rseed] = "notseed"
            # for newnode in newnodes:
            #    seedtype[newnode] = "notseed"
            
            #if resetindex >= len(newnodes):
            #    resetindex = 0
            # seedtype[newnodes[resetindex]] = "notseed"
            # resetindex += 1
            break

            for seed in seedtype:
                if seedtype[seed] == "seed":
                    seedtype[seed] = "notseed"
                else:
                    seedtype[seed] = "seed"


    
    return result


def isdirectionchange(circlestring,newc):
    if len(circlestring) < 3 or newc == "":
        return False

    circleseq = circlestring[-2:] + [newc]
    pointseq  = [ccenter(c) for c in circleseq]
    v1 = vnorm(vector(pointseq[0],pointseq[1]))
    v2 = vnorm(vector(pointseq[1],pointseq[2]))
    p0 = (0.0,0.0)
    p1 = padd(p0,v1)
    p2 = padd(p1,v2)

    dv = pcrossproduct(p0,p1,p2)
    puts("dv",dv)

    if abs(dv) > 0.9:
        return True
    return False

#
# compute tha maximum sized circles from the seeds and not colliding with the quadtree content
#
# the difference here is that only one seed at a time can be the seed
#
# Algo:
# - for each step:
#    - compute the maxcircle of the invalidated seeds
#    - sort out the maxcircle from all the seeds 
#    - transform the new maxcircleto add it in the quadtree
#    - invalidate the seeds colliding with the new circle
#
def maxcirclepackingcollisionlane(seeds,rseeds,quadtree,dmax,niter,ftransform,minsize):
    rallmax = 0.0
    crallmax = ""
    result = CircleAdj()
    cache = {}
    seedtype = {}
    newnodes = rseeds[:]
    resetindex = 0
    currentlane = []

    # init cache
    for seed in seeds:
        cache[seed] = ""
        (c1,c2,r) = seed
        #puts("add seed type",c1)
        #puts("add seed type",c2)
        seedtype[c1] = "seed"
        seedtype[c2] = "seed"
        quadtree.adds([c1,c2])
        result.addcircleadj(seed[0],seed[1])

    for rseed in rseeds:
        seedtype[rseed] = "seed"
        quadtree.add(rseed)

    for iiter in range(niter):
        puts("iter",iiter)
        crallmax = ""
        rallmax = 0.0
        maxseed = ""
        maxcollision = ""

        # first recompute the max circle from the invalidate seeds
        for seed in seeds:
            if cache[seed] == "" and cache[seed] != -1:
                cache[seed] = computemaxcirclefromseedcollision(quadtree,seed,dmax)

        # then compute the new max
        for seed in seeds:
            if cache[seed] != -1:
                if cache[seed] != "" and cradius(cache[seed][0]) > minsize:
                    # puts("cache[seed]",cache[seed])
                    rrmax =  cradius(cache[seed][0])
                    if rrmax > rallmax and (cache[seed][1] in seedtype) and (seedtype[cache[seed][1]] == "seed"):
                        # puts("new seed max",cache[seed])
                        rallmax  = rrmax
                        crallmax = cache[seed][0]
                        maxseed  = seed
                        maxcollision = cache[seed][1]
                        
                else:
                    # puts("seed",seed,"no use, mark it")
                    cache[seed] = -1
                
        
        # add the new max circle 
        puts("crallmax",crallmax,"directionchange",isdirectionchange(currentlane,crallmax))            
        if crallmax != "" and cradius(crallmax) > minsize:
            # puts("new max circle",crallmax)
            cfcircle = ftransform(crallmax,maxseed,maxcollision,seedtype[maxcollision])
            # result.append(cfcircle)
            quadtree.add(cfcircle)
            # puts("add notseed circle",cfcircle)
            seedtype[cfcircle] = "seed"
            seedtype[maxcollision] = "oldseed"
            result.addcircleadj(cfcircle,maxcollision)
            newnodes.append(cfcircle)
            currentlane.append(cfcircle)
            
            #for side in [1.0,-1.0]:
            #    seeds.append((maxcollision,cfcircle,side))
            #    cache[(maxcollision,cfcircle,side)] = ""

            # invalidate the seed circles colliding
            for seed in seeds:
                if cache[seed] != "" and cache[seed] != -1:
                    if circleintersect(cfcircle,cache[seed][0]):
                        # puts("invalidate seed",seed)
                        cache[seed] = ""
        else:
            puts("no more new max circle, restart")
            if len(currentlane) == 0:
                resetindex += 1
            currentlane = []
            for seed in seedtype:
                seedtype[seed] = "seed"
            seedtype[newnodes[resetindex]] = "seed"
    
    return result


#
#
#
def seedsfrompointnormals(pns,sides,size):
    return [(pn[0],pn[1],side,size) for pn in pns for side in sides]


def psplitevenly(p1,p2,maxdist):
    nsplit = int(dist(p1,p2) / maxdist) + 1
    return Segment(p1,p2).samples(nsplit)
    
    
#
# rangeseg must be the number of segments for the shape
#
def seedsfrompolypointnormals(poly,sides,size,rangelseg=""):
    polyline = Polyline(poly)
    if rangelseg == "":
        rangelseg = (500,500)
    rangelseg = (polyline.length()/float(rangelseg[1]),polyline.length()/float(rangelseg[0]))
        
    initpns = polyline.rootnormals()
    result = [initpns[0]]
    for pn in initpns[1:]:
        (lp,ln) = result[-1]
        (p,n)   = pn
        if dist(lp,p) < rangelseg[0]:
            continue
        else:
            if dist(lp,p) > rangelseg[1]:
                ps = psplitevenly(lp,p,rangelseg[1])
                result = result + [(p,n) for p in ps][1:]
            else:
                result.append(pn)
    
    return [(pn[0],pn[1],side,size) for pn in result for side in sides]

#
# define segment seeds as a segment + side
#
def segments2seeds(segments,sides=[-1.0,1.0]):
    return [SegmentSeed().seeddef((segment,side)) for segment in segments for side in sides]

#
# define segment seeds as a segment + side
#
def segments2normalseeds(segments,maxsize=None,sides=[-1.0,1.0],nitems = None):
    result = []
    for seg in segments:
        for segment in seg.splitmaxsize(maxsize):
            for side in sides:
                result.append(SeedNormal(segment.middle(),segment.normal(),side))
    if not nitems == None:
        result = litems(result,int(float(len(result))/float(nitems)))
    return result

#
# compute the n max circles inside a polygon
#
def polygonmaxcircles(self, niter = 1, ftransform = None, frecursive = None, seedpolygon = None):
    base = self.clockwise()
    if not base.isclosed():
        base = base.close()
    
    segments = base.segments()
    if seedpolygon == None:
        seedpolygon = base
    seedsegments = seedpolygon.segments()
    seeds    = segments2normalseeds(seedsegments,seedpolygon.length()/100.0,[-1.0])
    # puts("segments",[seg.coords() for seg in segments])
    # puts("seeds",len(seeds),[seed.coords() for seed in seeds])
    return maxcirclesfromseeds(segments, seeds, base.bbox(), niter,ftransform,frecursive).circles()

Polygon.maxcircles = polygonmaxcircles
