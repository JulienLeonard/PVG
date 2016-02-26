from PVG import *

#
# Seed definitions: a seed is a geometric structure to compute a next circle, given a radius
#                   and from a quadtree and a radius range, it can compute a maximu circle
#

class Seed:
    def __init__(self):
        self.mtype = ""
        self.mdef  = ""

    def seeddef(self,seeddef):
        self.mdef = seeddef
        return self
        
    def type(self,value=-1):
        if value == -1:
            return self.mtype
        else:
            self.mtype = value
            return self

    def computecircle(self,radius):
        print "to be overloaded"

    @classmethod
    def isdefmatching(cls,tempdef):
        print "to be overloaded : must return true if def ok"

    def c(self):
        print "to be overloaded: must give a circle from the seed"

    def cs(self):
        print "to be overloaded: must give all the circles from the seed"

    def maxcircle(self,rrange,quadtree,withmaxcollision = False):
        crmin = self.computecircle(rrange.minv())
        if quadtree.iscolliding(crmin):
            # puts("no circlemin")
            return None

        lastgoodcircle = crmin
        maxcollision   = None

        for j in range(20):
            rrmiddle = rrange.middle()
            crmiddle = self.computecircle(rrmiddle)
            if quadtree.iscolliding(crmiddle):
                rrange = R(rrange.minv(),rrmiddle)
                if withmaxcollision:
                    maxcollision = nearestcircle(self.c(),quadtree.colliding(crmiddle),self.cs())
            else:
                lastgoodcircle = crmiddle
                rrange = R(rrmiddle,rrange.maxv())

        if withmaxcollision:
            return SeedMaxResult(self,lastgoodcircle,maxcollision)
        else:
            return SeedMaxResult(self,lastgoodcircle,None)

    #
    # when given new circle, compute the new seeds to use as recursive
    #
    def recursive(self,frecursive,newcircle):
        print "to be overloaded : mut return a list of new seeds"
        
#
# Seed defined byt 2 adjacent circles
#

class Seed2(Seed):
    def c1(self):
        return self.mdef[0]
    def c2(self):
        return self.mdef[1]
    def side(self):
        return self.mdef[2]

    def c(self):
        return self.c1()

    def cs(self):
        return [self.c1(),self.c2()]

    def computecircle(self,radius):
        return circles2tangentout(self.c1(),self.c2(),radius, self.side())

    @classmethod
    def isdefmatching(cls,tempdef):
        if isinstance(tempdef[0],Circle) and isinstance(tempdef[1],Circle) and type(tempdef[2]) is float:
            return True
        return False

    def recursive(self,frecursive,newcircle):
        return frecursive([Seed2().seeddef([self.c1(),newcircle,1.0]),
                           Seed2().seeddef([self.c2(),newcircle,1.0]),
                           Seed2().seeddef([self.c1(),newcircle,-1.0]),
                           Seed2().seeddef([self.c2(),newcircle,-1.0])])

seed20 = Seed2().seeddef([Circle(Point(0.0,-0.5),1.0),Circle(Point(0.0,0.5),1.0),1.0])

#
# Seed defined by a circle and an angle
#    
class SeedAngle(Seed):
    def c(self):
        return self.mdef[0]
    def angle(self):
        return self.mdef[1]
    
    def cs(self):
        return [self.c()]

    def computecircle(self,radius):
        return nextadjcircle(self.c(), self.angle(), radius)

    @classmethod
    def isdefmatching(cls,tempdef):
        if isinstance(tempdef[0],Circle) and type(tempdef[1]) is float:
            return True
        return False

#
# Seed defined by a Segment and a Side
#
class SeedSegment(Seed):
    def p1(self):
        return self.segment().p1()

    def p2(self):
        return self.segment().p2()
    
    def side(self):
        return self.mdef[1]

    def center(self):
        return self.segment().middle()

    def size(self):
        return self.segment().length()

    def c(self):
        return Circle(self.center(),self.size()/100.0)

    def cs(self):
        return [Circle(self.p1(),self.size()/100.0), Circle(self.p2(),self.size()/100.0)]

    def segment(self):
        return self.mdef[0]

    def computecircle(self,radius):
        return segment2circletangent(self.segment(), radius, self.side())

    @classmethod
    def isdefmatching(cls,tempdef):
        if isinstance(tempdef[0]) == Segment and type(tempdef[1]) is float:
            return True
        return False

#
# Define a Seed by a point and a vector and a side
#
class SeedNormal(Seed):
    def __init__(self,point,normal,side):
        self.mpoint  = point
        self.mnormal = normal.normalize()
        self.mside   = side

    def p(self):
        return self.mpoint

    def point(self):
        return self.mpoint

    def normal(self):
        return self.mnormal
    
    def side(self):
        return self.mside

    def computecircle(self,radius):
        newcenter = self.p().add(self.normal().scale(self.side() * radius))
        return Circle(newcenter,radius)

    def coords(self):
        return self.p().coords() + self.normal().coords() + (self.side(),"")

    @classmethod
    def isdefmatching(cls,tempdef):
        if isinstance(tempdef[0],Point) and isinstance(tempdef[1],Vector) and type(tempdef[2]) is Float:
            return True
        return False


#
# method to autobuild seeds if not objects
# how to do it better: cannot iterate on class array :(
#
def elaborateseeds(seeds):
    result = []
    for seed in seeds:
        if isinstance(seed,Seed):
            result.append(seed)
        else:
            for klass in [Seed2,SeedAngle,SeedSegment,SeedNormal]:
                if klass.isdefmatching(seed):
                    result.append(klass().seeddef(seed))

    # puts("elaborateseeds result ",len(result))
    return result            

