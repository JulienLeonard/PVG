from utils import *
# from circleiter import *
from circleadj import *
from color import *
# from circlestring import *


##############################################################################################
# 
# abstract class representing a plug, that is a link between a bpattern and a subbpattern
# if subpattern None, represents a hook to where a subpattern can be grown
# must be able to compute a new circle from a radius (first circle of the new pattern)
# 
##############################################################################################
class BPlug:

    def __init__(self,parentpattern,subpattern = None):
        self.mparentpattern   = parentpattern
        self.msubpattern      = subpattern

    # get circles from definition
    def circles(self):
        return []

    def newcircle(self, radius):
        return None
    

##############################################################################################
# 
# class representing a 2-plug, that is a site to create a link between pattern and subpatterns
# used to compute a next circle from a radius
# used by junction to link a parent pattern and a sub pattern
#
##############################################################################################
class BPlug2(BPlug):

    def __init__(self,parentpattern,subpattern = None, c1 = None, c2 = None, side = None):
        self.mparentpattern   = parentpattern
        self.msubpattern      = subpattern
        self.mc1        = c1
        self.mc2        = c2
        self.mside      = side
        self.mnewcircle = None

    def load(self,c1,c2,side):
        self.mc1        = c1
        self.mc2        = c2
        self.mside      = side

    def circles(self):
        return [self.mc1,self.mc2]

    def newcircle(self, radius):
        result = circles2tangent(self.mc1,"OUT",self.mc2,"OUT",radius, self.mside)
        self.mnewcircle = result
        return result

    def c1(self,value=None):
        if value == None:
            return self.mc1
        else:
            self.mc1 = value
            return self

    def c2(self,value=None):
        if value == None:
            return self.mc2
        else:
            self.mc2 = value
            return self

    def side(self,value=None):
        if value == None:
            return self.mside
        else:
            self.mside = value
            return self

    def dirv(self,newcircle):
        c1 = self.mc1
        c2 = self.mc2
        ortho = Vector().points(c1.center(),c2.center())
        tangentp = c1.center().add(ortho.normalize().scale(c1.radius()))
        dirv = Vector().points(tangentp,newcircle.center()).normalize()
        return dirv

    def anglenewcircle(self,newcircle):
        return vangle(self.dirv(newcircle))

    def adjs(self):
        return [(self.mc1,self.mnewcircle),(self.mnewcircle,self.mc2)]

    def croots(self):
        return [self.mc1,self.mc2]

    def seed(self):
        return [self.mc1,self.mc2,self.mside]


##################################################################################################
#
# class representing a 1-plug, that is a link between a bpattern an a sub bpattern
# must be able to compute itself and launch computation of the attached sub bpattern
#
##################################################################################################
class BPlugSingle(BPlug):
    def __init__(self,parentpattern,subpattern=None, c = None, angle = None):
        self.mparentpattern   = parentpattern
        self.msubpattern      = subpattern
        self.mc     = c
        self.mangle = angle
        self.mnewcircle = None

    def circles(self):
        return [self.mc]

    def newcircle(self, radius):
        result = nextadjcircle(self.mc, self.mangle, radius )
        self.mnewcircle = result
        return result 

    def c(self,value=None):
        if value == None:
            return self.mc
        else:
            self.mc = value
            return self

    def angle(self,value=None):
        if value == None:
            return self.mangle
        else:
            self.mangle = value
            return self

    def anglenewcircle(self,newcircle):
        return self.angle()

    def dirv(self):
        return Vector(1.0,0.0).rotate(self.angle())


    def adjs(self):
        return [(self.mc,self.mnewcircle)]

def fradiusmin(circles):
    return lmin([c.radius() for c in circles])

#################################################################################################
#
# class to define and compute the subpattern from a parent plug
#
#################################################################################################
class JunctionDef:

    def __init__(self):
        self.mrtype   = "relative"
        self.mfradius = fradiusmin
        self.mratio   = 1.0
        self.mnextpatterndefs = None
        self.mtimes = 1

    def rtype(self,value=None):
        if value == None:
            return self.mrtype
        else:
            self.mrtype = value
            return self

    def fradius(self,value=None):
        if value == None:
            return self.mfradius
        else:
            self.mfradius = value
            return self

    def ratio(self,value=None):
        if value == None:
            return self.mratio
        else:
            self.mratio = value
            return self

    def nextpatterndefs(self,value=None):
        if value == None:
            return self.mnextpatterndefs
        else:
            self.mnextpatterndefs = value
            return self

    def times(self,value=None):
        if value == None:
            return self.mtimes
        else:
            self.mtimes = value
            return self

    def radiusfactor(self,plug):
        # puts("radiusfactor plug circles",plug.circles())
        return self.mfradius(plug.circles()) * self.mratio

    def gen(self,plug):
        return (plug,self)

    def compute(self,quadtree,ocontext,plug):
        # puts("Junction.compute: nextpatterndefs",self.mjunctiondef.nextpatterndefs())
        for nextpatterndef in self.nextpatterndefs():
            result = nextpatterndef.compute(quadtree,ocontext,self,plug)
            if result:
                return result
        return None

    def radius(self,plug):
        return self.radiusfactor(plug)




#
# plugset are functors that pass to each other (pattern,plugs), for generation or filter
#
class PlugSet:

    def __init__(self,pattern,plugs=None):
        self.mpattern = pattern
        self.mplugs = plugs

    def plugs(self):
        return self.mplugs

    @staticmethod
    def plug2s(sides=[1,-1]):
        def result(pattern):
            return PlugSet(pattern,[BPlug2(pattern,None,c1,c2,side) for side in sides  for circlestring in pattern.circlestrings() for (c1,c2) in pairs(circlestring)])
        return result

    @staticmethod
    def plug2sparents(sides=[1,-1]):
        def result(pattern):
            return PlugSet(pattern,[BPlug2(pattern,None,c1,c2,side)  for (c1,c2) in pattern.adjpairs() for side in sides])
        return result

    #def plug2s(pattern,sides=[-1,1]):
    #    return PlugSet(pattern,[BPlug2(pattern,None,c1,c2,side) for side in sides for circlestring in pattern.circlestrings() for (c1,c2) in pairs(circlestring)])

    @staticmethod
    def singleext(pattern):
        lastangle = pattern.lastangle()
        ccstrings = pattern.circlestrings()
        if lastangle == None or len(ccstrings) == 0 or len(ccstrings[0]) == 0:
            return PlugSet(pattern,[])
    
        return PlugSet(pattern,[BPlugSingle(pattern,None,pattern.circlestrings()[0][-1],pattern.lastangle())])
        


#################################################################################################
#
# class to define and compute junctions from a pattern
#
# gen is:
# pattern -> plugselector -> plugs -> junctiondef -> junctions
#
#################################################################################################
class JunctionGen:

    def __init__(self):
        self.flist = []

    def add(self,plugselector,junctiondef):
        self.flist = self.flist + [(plugselector,junctiondef)]
        return self

    # generate junctions = (plug,patterndefs)
    def gen(self,pattern):
        return [junctiondef.gen(plug) for (plugselector,junctiondef) in self.flist for plug in plugselector(pattern).plugs()]


#################################################################################################
#
# BWorld: bpattern environment: to trigger in order the bpatterns
#
#################################################################################################
class BWorld:

    def __init__(self,render,quadtree):
        self.mrender      = render
        self.mquadtree    = quadtree 
        self.mocontext    = OContext()
        self.madj         = CircleAdj()
        self.mpatterns    = []
        self.moldpatterns = []

    def initwithpatterns(self,patterns):
        self.mpatterns = self.mpatterns + patterns
        return self

    def popnextpattern(self):
        result         = self.mpatterns[0]
        self.mpatterns = self.mpatterns[1:]
        # self.moldpatterns.append(result)
        return result

    def updatefrombresult(self,cpattern,bresult,niter):
        if bresult:
            # puts("updatefrombresult ncircles",len(bresult.circles()))
            for newcircle in bresult.circles():
                self.mquadtree.add(newcircle)
            
            for adj1,adj2 in bresult.adjs():
                self.madj.addcircleadj(adj1,adj2)
            
            # puts("updatefrombresult bresult pattern",bresult.mpattern)
            if not bresult.mpattern is None:
                if not bresult.mpattern in self.mpatterns:
                    self.mpatterns.append(bresult.mpattern)

            # puts("bworld pattern stack",len(self.mpatterns),"niter +",bresult.mniter)
            niter += bresult.mniter

        if cpattern.hasplugjunction():
            self.mpatterns.append(cpattern)
        else:
            self.moldpatterns.append(cpattern)
        
        #puts("patterns",self.mpatterns)
        #puts("oldpatterns",self.moldpatterns)
            
        return niter

    def compute(self,nitermax,minsize=0.0001):
        niter = 0
        while len(self.mpatterns):
            cpattern = self.popnextpattern()
            #puts("current pattern",cpattern)
            if cpattern.hasplugjunction():
                (plug,junctiondef) = cpattern.nextplugjunction()
                # for (plug,junctiondef) in cpattern.junctiongen().gen(cpattern):
                bresult = junctiondef.compute(self.mquadtree,self.mocontext,plug)
                niterold = niter
                niter    = self.updatefrombresult(cpattern,bresult,niter)

                if bresult:
                    
                    # bresult = cplug.compute(self.mrender,self.mquadtree,self.mocontext,self.mpatternmap,minsize)
                
                    if not ((niter-niter%1000)/1000 == (niterold-niterold%1000)/1000):
                        puts("niter",niter,"niterold",niterold)
                    if niter > nitermax:
                        break
            else:
                self.moldpatterns.append(cpattern)
                
            if niter > nitermax:
                break
        return self

    #
    # trigger global drawing for patterns
    # 
    def draw(self,render):
        patterns = self.moldpatterns + self.mpatterns
        # puts("bworld draw patterns numbers",len(patterns))
        for pattern in patterns:
            pattern.drawall(render)
        

######################################################################################################
#
# global object to save context for circles and avoid changing method parameters
#
######################################################################################################
class OContext:
    def __init__(self):
        self.mcontexts    = {} 

    def add(self,c,key,value):
        if not c in self.mcontexts:
            self.mcontexts[c] = {}
        self.mcontexts[c][key] = value

    def container(self,c):
        return self.mcontexts[c]["container"]

    def get(self,key1,key2):
        return self.mcontexts[key1][key2]

    def has(self,c):
        return (c in self.mcontexts)


    def hass(self,c,key):
        if not (c in self.mcontexts):
            return False
        else:
            return (key in self.mcontexts[c])


def brancheabs(number,withlast=True):
    result = samples((0.0,1.0),number+1)[1:]
    if not withlast:
        result = result[:-1]
    return result

############################################################################################################
#
# Computation result: to store the result of the last computation of a pattern def
#
#############################################################################################################
class ComputationResult:
    
    def __init__(self,circles,adjs):
        self.mcircles = circles
        self.madjs    = adjs

    def circles(self):
        return self.mcircles

    def adjs(self):
        return self.madjs

#####################################################################################
#
# result of a bpattern computation
#
# contains only the result of the computation, not the whole result of the corresponding pattern (different if pattern is persistent)
#
#####################################################################################
class Bresult:

    def __init__(self,pattern=None,niter=0):
        self.mpattern = pattern
        self.mniter   = niter

    def circles(self):
        if self.mpattern is None or self.mpattern.lastcomputation() is None:
            return []
        return self.mpattern.lastcomputation().circles()

    def adjs(self):
        if self.mpattern is None or self.mpattern.lastcomputation() is None:
            return []
        return self.mpattern.lastcomputation().adjs()



############################################################################################################
#
# class to store a pattern, and to compute plugs from a pattern
# is the result of the patterndef computation
# Edge of a pattern graph, whose nodes are plugs, and edges are bpattern
#
#############################################################################################################
class BPattern:

    def __init__(self,patterndef,junctiondef,plug,adj=CircleAdj(),lastangle=None):
        self.mpatterndef      = patterndef
        self.mjunctiondef     = junctiondef
        self.mplug            = plug
        self.madj             = adj
        self.mlastangle       = lastangle
        self.mlastcomputation = None
        self.mplugjunctions   = None
        
    def patterndef(self):
        return self.mpatterndef
    
    def junctiongen(self):
        return self.patterndef().junctiongen()

    def hasplug(self):
        # result = (len(self.mplugs) > 0)
        # puts("pattern", self, "hasplug",result)
        return True

    def adj(self):
        return self.madj

    #def plugs2(self):
    #    return [Plug2(c1,c2,side) for side in [-1.0,1.0] for (c1,c2) in self.madj.alladjacencies()]

    # to compute plugs
    def circlestrings(self):
        return [self.madj.circles()]

    def adjpairs(self):
        c0 = self.madj.circles()[0]
        parentplugs = []
        if self.mplug:
            parentplugs = [(c,c0) for c in self.mplug.circles()]
        # puts("parentplugs",parentplugs)
        return  parentplugs + [(c1,c2) for (c1,c2) in self.madj.alladjacencies()]
    
    def lastangle(self):
        return self.mlastangle

    #
    # last computation result
    #
    def lastcomputation(self,value = None):
        if value == None:
            return self.mlastcomputation
        else:
            self.mlastcomputation = value
            return self

    def drawall(self,canvas):
        canvas.draw(self.madj.circles(),self.mpatterndef.mstyle)
    
    def nextplugjunction(self):
        if self.mplugjunctions == None:
            self.mplugjunctions = self.junctiongen().gen(self)
        nextplugjunction    = self.mplugjunctions[0]
        self.mplugjunctions = self.mplugjunctions[1:]
        return nextplugjunction

    def hasplugjunction(self):
        if self.mplugjunctions == None or len(self.mplugjunctions) > 0:
            return True
        return False

        
class RootPattern(BPattern):

    def __init__(self,circlepairs=[(Circle(Point(-1.0,0.0),1.0),Circle(Point(1.0,0.0),1.0))]):
        self.mpatterndef      = self
        self.mparentjunction  = None
        self.mjunctiongen     = None
        self.madj             = CircleAdj()
        for (c1,c2) in circlepairs:
            self.madj.addcircleadj(c1,c2)
        self.mlastangle = None
        self.mstyle = None
        self.mplug  = None
        self.mplugjunctions   = None
        
    def junctiongen(self,value = None):
        if value == None:
            return self.mjunctiongen
        else:
            self.mjunctiongen = value
            return self

    def style(self, value = None):
        if value == None:
            return self.mstyle
        else:
            self.mstyle = value
            return self

############################################################################################################
#
# class to specify and render/draw a pattern
#
#############################################################################################################

class BPatternRenderer:

    #
    # to be overloaded: draw the circles contained in result
    #
    def draw(self,render,ocontext,bplugcontext,pattern):
        return pattern
        
    
    #
    # hook to be overloaded if need to draw everything from pattern
    #
    def drawall(self,render,pattern):
        puts("_Bpattern to be overloaded")

    #
    # utilitary method to draw all the circles from a pattern and seeds with the arcs
    # to be overloaded to change color and size parameters
    #
    def drawallwitharcs(self,render,seeds,pattern):
        ccagraph = computecircleadjgraph(seeds,pattern.adj())

        minr = lmin([c[-1] for c in pattern.adj().circles()])

        for (arc,circle) in ccagraph.arcs():
            render.drawpolyline(arc,circle[-1]*0.2,color.white())
        
        for (leaf,adj) in ccagraph.leaves():
            circle = (leaf[0],leaf[1],adj[-1] * 0.5)
            render.drawcircle(circle,color.white(),0.5)



############################################################################################################
#
# class to specify and compute a pattern
#
#############################################################################################################

class BPatternDef:

    def __init__(self):
        self.mncircles = 1
        self.mangles   = [0.0]
        self.mrratios = (1.0,1.0)
        self.mrrelative = True
        self.mlratios = []
        self.mvangleincr = 0.0
        self.msangleincr = 1.0
        self.mpartial = False
        self.mstyle = {"color":Color.black(),"sizeratio":1.0}

        self.mlastangle = None

        self.mjunctiongen = None
        

    def junctiongen(self,value = None):
        if value == None:
            return self.mjunctiongen
        else:
            self.mjunctiongen = value
            return self


    def ncircles(self,value = None):
        if value == None:
            return self.mncircles
        else:
            self.mncircles = value
            return self

    def angles(self,value = None):
        if value == None:
            return self.mangles
        else:
            self.mangles = value
            return self

    def rratios(self,value = None):
        if value == None:
            return self.mrratios
        else:
            self.mrratios = value
            return self

    def lratios(self,value = None):
        if value == None:
            return self.mlratios
        else:
            self.mlratios = value
            return self
    
    def vangleincr(self,value = None):
        if value == None:
            return self.mvangleincr
        else:
            self.mvangleincr = value
            return self

    def sangleincr(self,value = None):
        if value == None:
            return self.msangleincr
        else:
            self.msangleincr = value
            return self

    def style(self,value = None):
        if value == None:
            return self.mstyle
        else:
            self.mstyle = value
            return self

    def partial(self, value = None):
        if value == None:
            return self.mpartial
        else:
            self.mpartial = value
            return self

    def rrelative(self, value = None):
        if value == None:
            return self.mrrelative
        else:
            self.mrrelative = value
            return self


    # base method to compute the pattern, defined by the parameters
    # TODO: optimize to compute once the pattern then copy/paste with homotecy
    def compute(self, quadtree, ocontext, junctiondef, plug):
        ncirclenumber = self.ncircles()
        angles        = self.angles()
        rratios       = self.rratios()
        lratios       = self.lratios()
        vangleincr    = self.vangleincr()
        sangleincr    = self.sangleincr()
        partial       = self.partial()

        newradius = junctiondef.radius(plug)
        # TODO: if radius absolute, need to overwrite newradius
        newcircle = plug.newcircle(newradius)
        if newcircle == None:
            return None

        dangle    = plug.anglenewcircle(newcircle)

        result =  None
        for angle in angles:
            angleincr  = sangleincr * vangleincr

            ncircles = [newcircle]
            cangle = angle + dangle
            newradius = newcircle.radius()
            if not self.rrelative():
                newradius = 1.0
            if len(rratios):
                newradiuses = [newradius * ir for ir in samples(rratios,ncirclenumber-1)]
            else:
                newradiuses = [newradius * ir for ir in lratios[1:]]


            for newradius in newradiuses:
                n2circle = nextadjcircle(ncircles[-1],cangle,newradius)
                cangle += angleincr
                if not quadtree.iscolliding(n2circle):
                    ncircles.append(n2circle)
                else:
                    if partial == False:
                        ncircles = []
                    break

            if len(ncircles) == ncirclenumber or (len(ncircles) > 1 and partial):
                newpattern = BPattern(self,junctiondef,plug,CircleAdj().circles(ncircles),cangle)

                for c in ncircles:
                    ocontext.add(c,"container",self)
                ncircleadjs = [adj for adj in pairs(ncircles)]

                newpattern.lastcomputation(ComputationResult(ncircles,ncircleadjs))

                result =  Bresult(pattern = newpattern, niter = len(ncircles))
                break

        return result





###############################################################################################################
#
# utilitary class to create root patterns
# can be created from circles or plugs
#
###############################################################################################################
# class PlugPattern(Bpattern):
    
#     def loadwithplug(self,plug):
#         self.mplugs.append(plug)
        
#         nodes = plug.circles()
#         for i in range(len(nodes)):
#             for j in range(i):
#                 if arecirclestangent(nodes[i],nodes[j]):
#                     self.madj.addcircleadj(nodes[i],nodes[j])

#         return self
