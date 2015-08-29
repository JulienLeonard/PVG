from geoutils import *
from circle   import *

class Quad:
    def __init__(self,viewbox,xmin,ymin,xmax,ymax,fshapeintersect):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.subquads  = []
        self.shapemap = {}
        self.mviewbox = viewbox
        self.mmaxshapenumber = 10
        self.mfshapeintersect = fshapeintersect

    def descr(self):
        return "( " + str(self.xmin) + ", " + str(self.ymin) + ", " + str(self.xmax) + " , " + str(self.ymax) + " )"

    def shapes(self):
        result = []
        for subquad in self.subquads:
            result = lconcat(result,subquad.shapes())
        result = lconcat(result,self.ownshapes())
        return result

    def intersect(self,shape):
        xmin,ymin,xmax,ymax = self.mviewbox(shape)
        result = 0
        if (xmin <= self.xmax and xmax >= self.xmin and ymin <= self.ymax and ymax >= self.ymin):
            result = 1
        # print "intersect",self.bbox(),"shape",shape,"result",result
        return result

    def add(self,shape,push):
        if not self.intersect(shape):
            xmin,ymin,xmax,ymax = self.mviewbox(shape)
            self.xmin = min(self.xmin,xmin)
            self.xmax = max(self.xmax,xmax)
            self.ymin = min(self.ymin,ymin)
            self.ymax = max(self.ymax,ymax)
            
            self.insert(shape,push)
        else:
            self.addwithoutcheck(shape,push)
        
    def pop(self,push):
        if push in self.shapemap:
            self.shapemap.pop(push)
        for subquad in self.subquads:
            subquad.pop(push)

    def addwithoutcheck(self,shape,push):
        # puts("addwithoutcheck subquads len",len(self.subquads),"quad",self.descr())
        if len(self.subquads):
            self.dispatch(shape,push)
        else:
            self.insert(shape,push)
        
    def dispatch(self,shape,push):
        for subquad in self.subquads:
            # puts("dispatch subquad",subquad.descr(),"shape",shape)
            if subquad.intersect(shape):
                subquad.addwithoutcheck(shape,push)

    def nshapes(self):
        return sum([len(self.shapemap[i]) for i in self.shapemap.keys()])

    def ownshapes(self):
        result = []
        for i in self.shapemap.keys():
            result = lconcat(result,self.shapemap[i])
        return result

    def insert(self,shape,push):
        # puts("quad ",self.descr(),"insert shape",shape,"nshapes",self.nshapes())

        if not push in self.shapemap:
            self.shapemap[push] = []

        for c in self.ownshapes():
            if self.mfshapeintersect(shape,c):
                self.mmaxshapenumber += 1

        self.shapemap[push].append(shape)
        
        if self.nshapes() > self.mmaxshapenumber:
            self.split()

    def split(self):
        # puts("quad ",self.xmin,self.ymin,self.xmax,self.ymax,"split")
        middlex = (self.xmin + self.xmax)/2.0
        middley = (self.ymin + self.ymax)/2.0
        
        self.subquads.append( Quad(self.mviewbox,self.xmin,self.ymin,middlex,middley,self.mfshapeintersect) )
        self.subquads.append( Quad(self.mviewbox,self.xmin,middley,middlex, self.ymax,self.mfshapeintersect) )
        self.subquads.append( Quad(self.mviewbox,middlex,middley,self.xmax, self.ymax,self.mfshapeintersect) )
        self.subquads.append( Quad(self.mviewbox,middlex,self.ymin,self.xmax, middley,self.mfshapeintersect) )
        
        for push in self.shapemap.keys():
            for shape in self.shapemap[push]:
                self.dispatch(shape,push)

        self.shapemap.clear()
        
    def mayintersect(self,newshape):
        #print "mayintersect",self.bbox(),"nshape",len(self.shapemap),"shape",newshape
        result = []
        if self.intersect(newshape):
            if len(self.subquads):
                for subquad in self.subquads:
                    if subquad.intersect(newshape):
                        subresult = subquad.mayintersect(newshape)
                        result.extend(subresult)
            else:
                for push in self.shapemap:
                    result.extend( self.shapemap[push] )
        return result

    def bbox(self):
        return [self.xmin,self.ymin,self.xmax,self.ymax]

class QuadTree:
    def __init__(self,width=10000.0,height=10000.0,fshapeintersect=circleintersect):
        self.rootquad = Quad(circleviewbox,-width,-height,width,height,fshapeintersect)
        self.mpush = 0
        self.mfshapeintersect = circleintersect

    def push(self):
        self.mpush += 1

    def pop(self):
        self.rootquad.pop(self.mpush)
        self.mpush += -1

    def add(self,shape):
        # puts("quadtree add",shape)
        self.rootquad.add(shape,self.mpush)

    def adds(self,shapes):
        for shape in shapes:
            self.add(shape)
        return self

    def iscolliding(self,newshape):
        shapes = self.rootquad.mayintersect( newshape )
        for shape in shapes:
            if self.mfshapeintersect(shape,newshape):
                return 1
        return 0

    def colliding(self,newshape):
        shapes = lunique(self.rootquad.mayintersect( newshape ))
        # puts("mayhem",mayhem)
        # shapes = list(set(self.rootquad.mayintersect( newshape )))
        # print "mayintersect",shapes
        return [shape for shape in shapes if self.mfshapeintersect(shape,newshape)]

    def shapes(self):
        return self.rootquad.shapes()

class QuadTreeSeg:
    def __init__(self,width,height):
        self.rootquad = Quad(segviewbox,-width,-height,width,height)
        self.mpush = 0

    def push(self):
        self.mpush += 1

    def pop(self):
        self.rootquad.pop(self.mpush)
        self.mpush += -1

    def add(self,seg):
        self.rootquad.add(seg,0)

    def iscolliding(self,newseg):
        segs = self.rootquad.mayintersect( newseg )
        for seg in segs:
            if len(raw_intersection(newseg[0],newseg[1],seg[0],seg[1])):
                return 1
        return 0

    def colliding(self,newseg):
        segs = list(set(self.rootquad.mayintersect( newseg )))
        # print "mayintersect",shapes
        return [seg for seg in segs if len(raw_intersection(newseg[0],newseg[1],seg[0],seg[1]))]
