from geoutils import *
from circle   import *
from shape    import *

class Quad:
    def __init__(self,bbox):
        self.mbbox    = bbox
        self.msubquads = []
        self.mshapemap = {}
        self.mmaxshapenumber = 10

    def descr(self):
        (xmin,ymin,xmax,ymax) = self.mbbox.coords()
        return "( " + str(self.xmin) + ", " + str(self.ymin) + ", " + str(self.xmax) + " , " + str(self.ymax) + " )"

    def shapes(self):
        result = []
        for subquad in self.msubquads:
            result = lconcat(result,subquad.shapes())
        result = lconcat(result,self.ownshapes())
        return result

    def intersect(self,bbox):
        return self.mbbox.intersect(bbox)

    def add(self,shape,push):
        bbox = shape.bbox()
        if not self.intersect(bbox):
            self.mbbox = bbunion(self.mbbox,bbox)
            self.insert(shape,push)
        else:
            self.addwithoutcheck(shape,push)
        
    def pop(self,push):
        if push in self.mshapemap:
            self.mshapemap.pop(push)
        for subquad in self.msubquads:
            subquad.pop(push)

    def addwithoutcheck(self,shape,push):
        # puts("addwithoutcheck subquads len",len(self.subquads),"quad",self.descr())
        if len(self.msubquads):
            self.dispatch(shape,push)
        else:
            self.insert(shape,push)
        
    def dispatch(self,shape,push):
        bbox = shape.bbox()
        for subquad in self.msubquads:
            # puts("dispatch subquad",subquad.descr(),"shape",shape)
            if subquad.intersect(bbox):
                subquad.addwithoutcheck(shape,push)

    def nshapes(self):
        return sum([len(self.mshapemap[i]) for i in self.mshapemap.keys()])

    def ownshapes(self):
        return [item for key in self.mshapemap.keys() for item in self.mshapemap[key]]

    def insert(self,shape,push):
        if not push in self.mshapemap:
            self.mshapemap[push] = []

        for c in self.ownshapes():
            if Shape.intersect(shape,c):
                self.mmaxshapenumber += 1

        self.mshapemap[push].append(shape)
        
        if self.nshapes() > self.mmaxshapenumber:
            self.split()

    def split(self):
        newsubquads  = [Quad(bbox) for bbox in self.mbbox.split4()]
        self.msubquads.extend(newsubquads)
        
        for push in self.mshapemap.keys():
            for shape in self.mshapemap[push]:
                self.dispatch(shape,push)

        self.mshapemap.clear()
        
    def hascollision(self, newbbox, newshape ):
        if not self.intersect(newbbox):
            return False
        else:
            # if len(self.msubquads) > 0:
            for subquad in self.msubquads:
                if subquad.hascollision(newbbox,newshape):
                    return True
            # return False
            # else:
            for push in self.mshapemap:
                for oshape in self.mshapemap[push]:
                    if Shape.intersect(newshape,oshape):
                        return True
                return False

        
    def mayintersect(self,newbbox):
        #print "mayintersect",self.bbox(),"nshape",len(self.shapemap),"shape",newshape
        result = []
        if self.intersect(newbbox):
            if len(self.msubquads):
                for subquad in self.msubquads:
                    if subquad.intersect(newbbox):
                        subresult = subquad.mayintersect(newbbox)
                        result.extend(subresult)
            else:
                for push in self.mshapemap:
                    result.extend( self.mshapemap[push] )
        return result

    def bbox(self):
        return self.mbbox

#
# Generic Quadtree, using Shape.intersect 
#
class QuadTree:
    def __init__(self,bbox0=None):
        if bbox0 == None:
            bbox0 = BBox(-1000.0,-1000.0,1000.0,1000.0)
        self.mrootquad = Quad(bbox0)
        self.mpush = 0

    def push(self):
        self.mpush += 1

    def pop(self):
        self.mrootquad.pop(self.mpush)
        self.mpush += -1

    def add(self,shape):
        self.mrootquad.add(shape,self.mpush)

    def adds(self,shapes):
        for shape in shapes:
            self.add(shape)
        return self

    def iscolliding(self,newshape):
        newbbox = newshape.bbox()
        return self.mrootquad.hascollision( newbbox, newshape )

    def colliding(self,newshape):
        newbbox = newshape.bbox()
        shapes = lunique(self.mrootquad.mayintersect( newbbox ))
        return [shape for shape in shapes if Shape.intersect(shape,newshape)]

    def shapes(self):
        return self.mrootquad.shapes()
