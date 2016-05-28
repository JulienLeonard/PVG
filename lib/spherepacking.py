from utils     import *
from geoutils3D  import *
from tangentutils3D import *
from quadtree3D import *
from circle import *
from sphere import *
from sphereadj import *
from seed3D      import *
from math import sqrt

class SphereNode(Sphere):
    def __init__(self,center = None, radius = 1.0):
        self.mcenter  = center
        self.mr       = radius
        self.mcontent = None

def radiusfmin3D(r1,r2,r3):
    return min(r1,r2,r3)*random.uniform(1.15,0.85)

def nodes03D():
    ps = Circle().samples(4)
    return [SphereNode().coords((p.x(),p.y(),0.0,0.5*sqrt(3.0))) for p in ps]

def oseeds3D():
    return nodes03D()

def allsides():
    return [-1.0,1.0]

def sphere2nodetriplet(sphere):
    ps = Circle().coords((sphere.x(),sphere.y(),sphere.r())).samples(4)
    return [SphereNode().coords((p.x(),p.y(),sphere.z(),sphere.r()/2.0*sqrt(3.0))) for p in ps]


def spherepackingall3D(seeds,quadtree,radiusff,nitermax,minsize=0.0001):
    return SpherePacking().radiusf(radiusff).compute(seeds,quadtree,nitermax,minsize).spheres()

def spherepackingalladj3D(seeds,quadtree,radiusff,nitermax):
    return SpherePacking().radiusf(radiusff).compute(seeds,quadtree,nitermax)

# def circlestring(polyline,circlesize):
#     incr = circlesize/polyline.length()
#     sabs = 0.0
#     point = polyline.point(sabs)
#     result = []
#     while (sabs <= 1.0):
#         newabs   = sabs + incr
#         newpoint = polyline.point(newabs) 
#         ncenter = pmiddle([point,newpoint])
#         r = vlength(vector(point,newpoint))/2.0
#         if len(result) != 0:
#             pcenter = (result[-1][0],result[-1][1])
#             nr = vlength(vector(pcenter,ncenter))-result[-1][2]
#             if nr > 0.8 * r:
#                 r = nr
#         result.append((ncenter[0],ncenter[1],r))
#         sabs = newabs
#         point = newpoint 
#         # print "sabs ",sabs
#     return result

# def checkcollidingcircles(circlestring):
#     quadtree = QuadTree(100.0,100.0)
#     result = []
#     for circle in circlestring:
#         if not quadtree.iscolliding(circle):
#             quadtree.add(circle)
#             result.append(circle)
#     return result

# def seedsfromcircles(circles,sides):
#     result = []
#     for (c1,c2) in pairs(circles):
#         if arecirclestangent(c1,c2):
#             for side in sides:
#                 result.append((c1,c2,side))
#     return result

# def seedsfromcirclesplit(circles,sides=[-1.0,1.0]):
#     result = []
#     for c in circles:
#         newcs = []
#         for offset in [1.0,-1.0]:
#             newcc = padd(ccenter(c),(offset * cradius(c)/2.0,0.0))
#             newc  = (newcc[0],newcc[1],cradius(c)/2.0)
#             newcs.append(newc)
            
#         for side in sides:
#             result.append((newcs[0],newcs[1],side))
#     return result

# def seedsfromcirclestring(circles,sides,n=2):
#     result = []
#     for cs in foreachn(circles,n):
#         c1,c2 = cs[0:2]
#         if arecirclestangent(c1,c2):
#             for side in sides:
#                 result.append((c1,c2,side))
#     return result


def makeradiusmin3Df(v1,v2):
  def result(r1,r2,r3):
     return min(r1,r2,r3)*random.uniform(v1,v2)
  return result

def makeradiusrandom3D(vlist):
  def result(r1,r2,r3):
     return lshuffle(vlist)[0]
  return result

def makeradiusroller3D(vlist):
    r = Roller(vlist)
    def result(r1,r2,r3):
        return r.next()
    return result


def makeradiuses3Df(v1,v2,nsamples):
  def result(r1,r2,r3):
     return R(min(r1,r2,r3)*v1,min(r1,r2,r3)*v2).samples(nsamples)
  return result

# def makeradiuscontextangle3Df(v1,v2):
#   def result(s1,s2,s3):
#       p1 = s1.center()
#       p2 = s2.center()
#       v = vanglepos(vector(p1,p2)) / 2* 3.14159
#       return multisamples([(0.0,v1),(0.25,v2),(0.5,v1),(0.75,v2),(1.0,v1)],v + 0.25) * rrandom(cradius(c1),cradius(c2))
#       # return multisamples([(0.0,v1),(0.5,v2),(1.0,v2)],v + 0.25) * lmin([cradius(c1),cradius(c2)])
#   return result


def makerangeradius3df(v1,v2):
    def result(r1,r2,r3):
        return random.uniform(v1,v2)
    return result

def makeradiusalternate3D(v1,v2):
    def result(r1,r2,r3):
        if r1 == v1 and r2 == v1:
            return v2
        else:
            return v1
    return result

def makeradiusalternate33D(v1,v2,v3):
    def result(r1,r2,r3):
        return lfront(lsubstract([v1,v2,v3],[r1,r2,r3])) 
    return result

def makeradiusdiff3D(vlist):
    def result(r1,r2,r3):
        return lfront(lsubstract(vlist,[r1,r2,r3]))
    return result


radiusmin3Df = makeradiusmin3Df(0.92,1.1)

def makeradiuseslist3D(vlist):
    def result(r1,r2,r3):
        return vlist
    return result

def makeradiusesroller3D(vlist,nsamples):
    r = Roller(vlist)
    def result(r1,r2,r3):
        return [r.next() for i in range(nsamples)]
    return result


def frontnextadj(front):
    return [front[0],front[1:]]

def allsides():
    return [-1.0,1.0]

def oneside():
    return [1.0]

def lappend(front,item):
    front.append(item)
    return front

def lappendfront(front,item):
    result = lconcat([item],front)
    return result

def lappendrandom(front,item):
    index = int(random.uniform(0.0,float(len(front))))
    result = lconcat(lconcat(front[0:index],[item]),front[index:])
    return result

def lidentity(list):
    return list[:]

class SpherePacking:
    
    def __init__(self):
        self.mradiusf          = radiusmin3Df
        self.mradiusesf        = makeradiuses3Df(1.0,0.9,3)
        # self.mradiuscontextf   = makeradiuscontextanglef(1.0,0.5)
        self.mfrontorderf      = lidentity
        self.mnextadjf         = frontnextadj
        self.mnextsidesf       = allsides
        self.minsertnewf       = lappend
        self.madj = SphereAdj()

    def radiusf(self,f):
        self.mradiusf = f
        return self

    def radiuscontextf(self,f):
        self.mradiuscontextf = f
        return self


    def radiusesf(self,f):
        self.mradiusesf = f
        return self
    
    def frontorderf(self,f):
        self.mfrontorderf = f
        return self

    def nextadjf(self,f):
        self.mnextadjf = f
        return self

    def nextsidesf(self,f):
        self.mnextsidesf = f
        return self
    
    def insertnewf(self,f):
        self.minsertnewf = f
        return self

    def adj(self):
        return self.madj

    def compute(self,seeds,quadtree,nitermax,minsize=0.0001):
        self.madj = SphereAdj()
        for seed in seeds:
            # c1,c2,side = seed
            # puts("c1",c1,"c2",c2)
            for (s1,s2) in seed.adjspheres():
                self.madj.addsphereadj(s1,s2)
        front = seeds[:]
        niter = 0
        front = self.mfrontorderf(front)
        while len(front):
            nfront, front = self.mnextadjf(front)
            s1,s2,s3,side = nfront.mdef
            radius = self.mradiusf(s1.radius(),s2.radius(),s3.radius())
            newsphere = adjsphere(s1,s2,s3,radius, side)
            # print "newsphere",newsphere
            if not quadtree.iscolliding(newsphere) and newsphere.radius() > minsize:
                # print "add sphere"
                self.madj.addsphereadj(s1,newsphere)
                self.madj.addsphereadj(s2,newsphere)
                self.madj.addsphereadj(s3,newsphere)
                quadtree.add(newsphere)
                for side in self.mnextsidesf():
                    front = self.minsertnewf(front,Seed3D3().seeddef([newsphere,s1,s2,side]))
                    if niter % 24 == 0:
                        front = self.minsertnewf(front,Seed3D3().seeddef([s2,s3,newsphere,side]))
                        front = self.minsertnewf(front,Seed3D3().seeddef([s3,s1,newsphere,side]))
            niter += 1
            if niter%1000 == 0:
                puts("niter",niter)
            if niter > nitermax:
                break
        return self.madj

#     def computefull(self,seeds,quadtree,nitermax,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             self.madj.addcircleadj(c1,c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         while len(front):
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             radius = self.mradiusf(c1[-1],c2[-1])
#             newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#             #print "newcircle",newcircle
#             if not quadtree.iscolliding(newcircle) and newcircle[-1] > minsize:
#                 #print "add circle"
#                 self.madj.addcircleadj(c1,newcircle)
#                 self.madj.addcircleadj(c2,newcircle)
#                 collicircle = circles2tangent(c1,"OUT",c2,"OUT",radius*1.1, side)
#                 collisions  = quadtree.colliding(collicircle)
#                 self.madj.completeadjacency(newcircle,collisions)
#                 quadtree.add(newcircle)
#                 for side in self.mnextsidesf():
#                     front = self.minsertnewf(front,[c1,newcircle,side])
#                     front = self.minsertnewf(front,[c2,newcircle,side])
#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj

#     def computetries(self,seeds,quadtree,nitermax,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             self.madj.addcircleadj(c1,c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         while len(front):
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             for radius in self.mradiusesf(c1[-1],c2[-1]):
#                 newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#                 #print "newcircle",newcircle
#                 if not quadtree.iscolliding(newcircle) and newcircle[-1] > minsize:
#                    #print "add circle"
#                     self.madj.addcircleadj(c1,newcircle)
#                     self.madj.addcircleadj(c2,newcircle)
#                     #collicircle = circles2tangent(c1,"OUT",c2,"OUT",radius*1.1, side)
#                     #collisions  = quadtree.colliding(collicircle)
#                     #self.madj.completeadjacency(newcircle,collisions)
#                     quadtree.add(newcircle)
#                     for side in self.mnextsidesf():
#                         front = self.minsertnewf(front,[c1,newcircle,side])
#                         front = self.minsertnewf(front,[c2,newcircle,side])
#                     break
#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj

#     def computeoptim(self,seeds,quadtree,nitermax,collisize,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             self.madj.addcircleadj(c1,c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         #puts("init front length",len(front))
#         while len(front):
#             #puts("\nniter",niter)
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             #puts("c1",c1,"c2",c2,"side",side)
#             radius = self.mradiusf(cradius(c1),cradius(c2))
#             collicircle = circles2tangent(c1,"OUT",c2,"OUT",radius*collisize, side)
#             collisions  = quadtree.colliding(collicircle)
#             nearest = []
#             #puts("collisions length",len(collisions))
#             if len(collisions) == 0:
#                 newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#                 nearest = []
#             else:
#                 nearest = collisions[0]
#                 distmin = abs(distcircle(collicircle,nearest))
#                 for collider in collisions[1:]:
#                     cdist = abs(distcircle(collicircle,collider))
#                     if cdist < distmin:
#                         distmin = cdist
#                         nearest = collider
                        
#                 #puts("nearest",nearest)
#                 # here we have the nearest neighbour: compute now the triadjacent
#                 # puts ("c1",c1,"c2",c2,"nearest",nearest)
#                 tricircle = tritangent(c1,c2,nearest)
#                 #puts("tricircle",tricircle)
#                 if len(tricircle) > 0 and cradius(tricircle) > 0.8*radius:
#                     newcircle = tricircle
#                     #puts("tricircle newcircle OK",newcircle)
#                 else:
#                     #puts("no next circle")
#                     newcircle = []
#                     nearest = []
#             if len(newcircle) > 0:
#                 newcollidings = quadtree.colliding(newcircle)
#                 if len(newcollidings) > 0:
#                     newcircle = (newcircle[0],newcircle[1],newcircle[2]*0.99)
#                 if not quadtree.iscolliding(newcircle):
#                     #puts("add circle",newcircle)
#                     self.madj.addcircleadj(c1,newcircle)
#                     self.madj.addcircleadj(c2,newcircle)
#                     quadtree.add(newcircle)
#                     for side in self.mnextsidesf():
#                         #puts("add normal adj side",side)
#                         front = self.minsertnewf(front,[c1,newcircle,side])
#                         front = self.minsertnewf(front,[c2,newcircle,side])
#                     if len(nearest) > 0:
#                         self.madj.addcircleadj(nearest,newcircle)
#                         for side in self.mnextsidesf():
#                             #puts("add nearest adj side",side)
#                             front = self.minsertnewf(front,[nearest,newcircle,side])

#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj


#     def computeoptimpair(self,seeds,quadtree,nitermax,minradiusfactor,collisize,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             self.madj.addcircleadj(c1,c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         #puts("init front length",len(front))
#         while len(front):
#             #puts("\nniter",niter)
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             #puts("c1",c1,"c2",c2,"side",side)
#             radius = self.mradiusf(cradius(c1),cradius(c2))
#             collicircle = circles2tangent(c1,"OUT",c2,"OUT",radius*collisize, side)
#             if not len(collicircle) > 0:
#                 continue
#             collisions  = quadtree.colliding(collicircle)
#             nearest = []
#             #puts("collisions length",len(collisions))
#             if len(collisions) == 0:
#                 newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#                 nearest = []
#             else:
#                 nearest = collisions[0]
#                 distmin = abs(distcircle(collicircle,nearest))
#                 for collider in collisions[1:]:
#                     cdist = abs(distcircle(collicircle,collider))
#                     if cdist < distmin:
#                         distmin = cdist
#                         nearest = collider
                        
#                 #puts("nearest",nearest)
#                 # here we have the nearest neighbour: compute now the triadjacent
#                 # puts ("c1",c1,"c2",c2,"nearest",nearest)
#                 tricircle = tritangent(c1,c2,nearest)
#                 #puts("tricircle",tricircle)
#                 if len(tricircle) > 0 and cradius(tricircle) > minradiusfactor*radius:
#                     newcircle = tricircle
#                     #puts("tricircle newcircle OK",newcircle)
#                 elif len(tricircle) > 0 and cradius(tricircle) > 0.01*radius:
#                     # do not add circle, but add new front, if one is already adjacent to the currents
#                     #puts("try to add pairs")
#                     ca1s = self.madj.adjcircles(c1)
#                     ca2s = self.madj.adjcircles(c2)
#                     if nearest in ca1s and not nearest in ca2s:
#                         #puts("add nearest",nearest," to c2",c2)
#                         for side in self.mnextsidesf():
#                             front = self.minsertnewf(front,[c2,nearest,side])
#                     if nearest in ca2s and not nearest in ca1s:
#                         for side in self.mnextsidesf():
#                             front = self.minsertnewf(front,[c1,nearest,side])
#                             #puts("add nearest",nearest," to c1",c1)
#                     newcircle = []
#                     nearest = []
#             if len(newcircle) > 0:
#                 newcollidings = quadtree.colliding(newcircle)
#                 if len(newcollidings) > 0:
#                     newcircle = (newcircle[0],newcircle[1],newcircle[2]*0.98)
#                 if not quadtree.iscolliding(newcircle):
#                     #puts("add circle",newcircle)
#                     self.madj.addcircleadj(c1,newcircle)
#                     self.madj.addcircleadj(c2,newcircle)
#                     quadtree.add(newcircle)
#                     for side in self.mnextsidesf():
#                         #puts("add normal adj side",side)
#                         front = self.minsertnewf(front,[c1,newcircle,side])
#                         front = self.minsertnewf(front,[c2,newcircle,side])
#                     if len(nearest) > 0:
#                         self.madj.addcircleadj(nearest,newcircle)
#                         for side in self.mnextsidesf():
#                             #puts("add nearest adj side",side)
#                             front = self.minsertnewf(front,[nearest,newcircle,side])

#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj


#     def computecontext(self,seeds,quadtree,nitermax,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             # puts("c1",c1,"c2",c2)
#             self.madj.addcircleadj(c1,c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         while len(front):
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             if side > 0.0:
#                 c1b, c2b = c1,c2
#                 c1, c2 = c2b, c1b
#                 side = -side
#             radius = self.mradiuscontextf(c1,c2)
#             newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#             #print "newcircle",newcircle
#             if not quadtree.iscolliding(newcircle) and newcircle[-1] > minsize:
#                 #print "add circle"
#                 self.madj.addcircleadj(c1,newcircle)
#                 self.madj.addcircleadj(c2,newcircle)
#                 quadtree.add(newcircle)
#                 for side in self.mnextsidesf():
#                     front = self.minsertnewf(front,[c1,newcircle,side])
#                     front = self.minsertnewf(front,[c2,newcircle,side])
#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj

#     def metacompute(self,seeds,quadtree,fcomputenext,nitermax,minsize=0.0001):
#         self.madj = CircleAdj()
#         for seed in seeds:
#             c1,c2,side = seed
#             puts("c1",c1,"c2",c2)
#             self.madj.addcircleadj(c1,c2)
#             quadtree.add(c1)
#             quadtree.add(c2)
#         front = seeds[:]
#         niter = 0
#         front = self.mfrontorderf(front)
#         while len(front):
#             nfront, front = self.mnextadjf(front)
#             c1,c2,side = nfront
#             radius = self.mradiusf(c1[-1],c2[-1])
#             newcircles, newadjs, newfronts = fcomputenext(quadtree,c1,c2,radius,side,minsize)

#             for newcircle in newcircles:
#                 quadtree.add(newcircle)
            
#             for adj1,adj2 in newadjs:
#                 self.madj.addcircleadj(adj1,adj2)

#             for newfront1,newfront2 in newfronts:
#                 for side in self.mnextsidesf():
#                     front = self.minsertnewf(front,[newfront1,newfront2,side])

#             #print "newcircle",newcircle
#             niter += 1
#             if niter%1000 == 0:
#                 puts("niter",niter)
#             if niter > nitermax:
#                 break
#         return self.madj



        
# def fcomputenextsimple(quadtree,c1,c2,radius,side,minsize):
#     newcircle = circles2tangent(c1,"OUT",c2,"OUT",radius, side)
#     if not quadtree.iscolliding(newcircle) and cradius(newcircle) > minsize:
#         return ([newcircle],[(c1,newcircle),(c2,newcircle)],[(c1,newcircle),(c2,newcircle)])
#     return ([],[],[])
