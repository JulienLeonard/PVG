from shape  import *

class ShapeNode:

    def __init__(self,shape):
        self.mshape    = shape
        self.msubnodes = []

    def shape(self):
        return self.mshape

    def subnodes(self):
        return self.msubnodes

    def subshapes(self):
        return [node.shape() for node in self.subnodes()]

    def shapes(self):
        result = []
        if self.mshape != None:
            result.append(self.mshape)
        result.extend([shape for node in self.subnodes() for shape in node.shapes()])
        return result

    #
    # WARNING: shapes cannot be enclosed in 2 different shapes
    #
    def add(self,newshape):
        for node in self.subnodes():
            if Shape.contain(node.shape(),newshape):
                node.add(newshape)
                return self
        self.msubnodes.append(ShapeNode(newshape))
        return self

    def bbox(self):
        if self.mshape == None:
            return bbunions([node.bbox() for node in self.subnodes()])
        else:
            return self.mshape.bbox()

    def shapesbylevel(self,level):
        if level == 0:
            return [self.mshape]
        return [shape for node in self.subnodes() for shape in node.shapesbylevel(level-1)]
        


class ShapeHierarchy:
    def __init__(self):
        self.mlevel0  = ShapeNode(None)

    def shapes(self):
        return self.mlevel0.shapes()

    def shapes0(self):
        return self.mlevel0.subshapes()

    def add(self,shape):
        self.mlevel0.add(shape)
        return self

    def adds(self,shapes):
        for shape in shapes:
            self.add(shape)
        return self

    def viewbox(self):
        return self.mlevel0.viewbox()

    def size(self):
        return self.viewbox().size()

    def bbox(self,factor=1.1):
        return self.viewbox().resize(factor)

    def viewport(self,factor=1.1):
        return self.viewbox().resize(factor).viewport(factor)

    def points(self):
        return self.mlevel0.allpoints()

    def shape(self):
        return self.mlevel0.subshapes()[0]

    def shapesbylevel(self,level):
        return self.mlevel0.shapesbylevel(level)

    @staticmethod
    def merge(ohierarchies):
        return ShapeHierarchy().adds([shape for ohier in ohierarchies for shape in ohier.shapes()])

    def symx(self,symx):
        return ShapeHierarchy().adds([shape.symx(symx) for shape in self.shapes()])

    def sortedshapes(self,level):
        sortlist = [(shape.length(),shape) for shape in self.shapes(level)]
        sortlist.sort()
        return [shape for (dum,shape) in sortlist][:-1]
