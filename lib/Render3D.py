from color    import *
from style    import *
from geoutils3D import *
from sphere   import *
from circle   import *
from polygon  import *
import time
import os

def defaultoutputdir():
    return "/".join(os.path.dirname(os.path.realpath(__file__).replace("\\","/")).split("/")[:-1]) + "/output"

class ImageDim3D:
    def __init__(self,width,height,depth):
        self.mwidth  = width
        self.mheight = height
        self.mdepth  = depth
        
    def width(self):
        return self.mwidth

    def height(self):
        return self.mheight

    def depth(self):
        return self.mdepth

    
class Drawing3D:

    def __init__(self,shape,style):
        self.mshape = shape
        self.mstyle = style
        
    def shape(self):
        return self.mshape

    def style(self):
        return self.mstyle


class Frame3D:
    
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
        return Frame3D().adds([Drawing3D(drawing.shape().symx(symx),drawing.style()) for drawing in self.drawings()])

    def draw(self,shape,style = Color.black()):
        self.add(Drawing3D(shape,style))

    

class Render3D:
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
            if isinstance(shape,Frame3D):
                for drawing in shape.drawings():
                    # puts("shape",shape,"drawing",drawing)
                    self.draw(drawing.shape(),drawing.style())
            else:
                if isinstance(shape,Polygon):
                    self.drawpolygon(shape,style)
                elif isinstance(shape,Sphere):
                    self.drawsphere(shape,style)
                elif isinstance(shape,Circle):
                    self.drawcircle(shape,style)
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

    def drawsphere(self,sphere,style=None):
        if style == None:
            style = Style()
        # self.drawpolygon(circle.scale(ratio).polygon(30),style)
        # TODO

    def drawspheres(self,spheres,style=None):
        for sphere in spheres:
            self.drawsphere(sphere,style)

    def drawspherescolors(self,spheres,styles):
        for i in range(len(spheres)):
            self.drawsphere(spheres[i],circular(styles,i))

    def drawcircle(self,circle,style=None):
        if style == None:
            style = Style()
        self.drawcirclepicture(circle,style)

    def drawcircles(self,circles,style=None):
        for circle in circles:
            self.drawcircle(circle,style)

    def drawcirclescolors(self,circles,styles):
        for i in range(len(circles)):
            self.drawcircle(circles[i],circular(styles,i))

            
class RenderCenter3D(Render3D):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor

    def drawsphere( self, sphere, style = None):
        if not sphere == None:
            self.mdrawings.append(Drawing3D(sphere,style))

    def drawcircle( self, circle, style = None):
        if not circle == None:
            self.mdrawings.append(Drawing3D(circle,style))
            
    def drawpolygon( self, polygon, style = None):
        if not polygon == None:
            self.mdrawings.append(Drawing3D(polygon,style))

    def end(self):
        mnspheres = 0
        puts("RenderCenter(RenderCairo end start")
        self.initpicture(self.mimagedim,self.mbackcolor)
        self.setviewport(self.viewport())
        puts("RenderCenter(RenderCairo start drawing")
        for drawing in self.mdrawings:
            shape = drawing.shape()
            if isinstance(shape,Polygon):
                self.drawpolygonpicture(shape,drawing.style())
            if isinstance(shape,Sphere):
                self.drawspherepicture(shape,drawing.style())
                mnspheres+=1
            if isinstance(shape,Circle):
                self.drawcirclepicture(shape,drawing.style())
                mnspheres+=1

        puts("N spheres to draw",mnspheres)
        self.endpicture()

    def viewport(self):
        return bbunions3D([drawing.shape().bbox() for drawing in self.mdrawings]).resize(self.margin()).viewport()

