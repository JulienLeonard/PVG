from utils         import *
from drawutils     import *
from geoutils      import *
from tangentutils  import *
from quadtree      import *
from circleadj     import *
from circlepacking import *

#
# Class to control execution of several circlepackings algorithm at the same time
# Can be recursive :)
#
class CirclePackingSequencer:

    def __init__(self,packings = []):
        self.mpackings = []
        self.mquadtree = None

    def add(self,packing):
        self.mpackings.append(packing)

    def adds(self,packings):
        self.mpackings.extend(packings)

    def packings(self):
        return self.mpackings

    def iter(self,niter=1,boundaries=None,quadtree=None):
        if not quadtree == None:
            self.mquadtree = None
        else:
            if self.mquadtree == None:
                self.mquadtree = Quadtree()
        if not boundaries == None:
            self.mquadtree.adds(boundaries)
            
        r = Roller(self.mpackings)
        for i in range(niter):
            r.next().iter(niter=1,quadtree=self.mquadtree)
