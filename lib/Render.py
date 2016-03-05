from color    import *
from style    import *
from geoutils import *
from circle   import *
from polygon  import *
import time
import os

def defaultoutputdir():
    return "/".join(os.path.dirname(os.path.realpath(__file__).replace("\\","/")).split("/")[:-1]) + "/output"

class ImageDim:
    def __init__(self,width,height):
        self.mwidth  = width
        self.mheight = height
        
    def width(self):
        return self.mwidth

    def height(self):
        return self.mheight

class Drawing:

    def __init__(self,shape,style):
        self.mshape = shape
        self.mstyle = style
        
    def shape(self):
        return self.mshape

    def style(self):
        return self.mstyle


class Frame:
    
    def __init__(self):
        self.mdrawings  = []

    def drawings(self):
        return self.mdrawings

    def add(self,drawing):
        self.mdrawings.append(drawing)
        return self

    def adds(self,drawings):
        for drawing in drawings:
            self.add(drawing)
        return self

    def symx(self,symx):
        return Frame().adds([Drawing(drawing.shape().symx(symx),drawing.style()) for drawing in self.drawings()])

    def draw(self,shape,style = Color.black()):
        self.add(Drawing(shape,style))

    

class Render:
    def __init__(self,viewport,imagedim,filename,backcolor=Color.white()):
        self.mimagedim  = imagedim
        self.mviewport  = viewport
        self.mfilename  = filename
        self.mbackcolor = backcolor
        self.mmargin    = 1.25
        self.selfinit()

    def outputfilepath(self,v = None):
        if v == None:
            return self.mfilename
        else:
            self.mfilename = v
            return self

    def margin(self, v = None):
        if v == None:
            return self.mmargin
        else:
            self.mmargin = v
            return self

    def draw(self, shape, style = None ):
        if type(shape) == list:
            shapes = shape
            for shape in shapes:
                self.draw(shape,style)
        else:
            if isinstance(shape,Frame):
                for drawing in shape.drawings():
                    # puts("shape",shape,"drawing",drawing)
                    self.draw(drawing.shape(),drawing.style())
            else:
                if isinstance(shape,Circle):
                    self.drawcircle(shape,style)
                elif isinstance(shape,Polygon):
                    self.drawpolygon(shape,style)
        return self

    def drawpolygon( self, polygon, style = None ):
        self.drawpolygonpicture(polygon,style)

    def drawpolygonpicture( self, polygon, style ):
        puts("Render drawpolygonpicture not defined")

    def initpicture(self):
        puts("Render initpicture not defined")

    def endpicture(self):
        puts("endpicture")

    def strokepolygon(self, polygon, width, colorc):
        self.drawpolygon(line(polygon.points(),width),colorc)

    def end(self):
        self.endpicture()

    def strokepolygons(self,polylines,width,color):
        for polygon in polygons:
            self.strokepolygon(polygon,width,color)
        
    def drawpolygons(self,polygons,color):
        for poly in polygons:
            self.drawpolygon(poly,color)

    def drawcircle(self,circle,style):
        ratio = iff(style == None, 1.0, style.sizeratio())
        self.drawpolygon(circle.scale(ratio).polygon(30),style)

    def drawcircles(self,circles,style):
        for circle in circles:
            self.drawcircle(circle,style)

    def drawcirclescolors(self,circles,styles):
        for i in range(len(circles)):
            self.drawcircle(circles[i],circular(styles,i))



