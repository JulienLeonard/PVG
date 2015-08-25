from color    import *
from geoutils import *
from circle   import *
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
    

class Render:
    def __init__(self,viewport,imagedim,filename,backcolor=Color.white()):
        self.mimagedim  = imagedim
        self.mviewport  = viewport
        self.mfilename  = filename
        self.mbackcolor = backcolor
        self.selfinit()

    def drawpolygon( self, polygon, colorc = Color.black() ):
        self.drawpolygonpicture(polygon,colorc)

    def drawpolygonpicture( self, polygon, colorc ):
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

    def drawcircle(self,circle,color=Color.black(),ratio=1.0):
        self.drawpolygon(circle.scale(ratio).polygon(30),color)

    def drawcircles(self,circles,color=Color.black(),ratio = 1.0):
        for circle in circles:
            self.drawcircle(circle,color,ratio)

    def drawcirclescolors(self,circles,colors):
        for i in range(len(circles)):
            self.drawcircle(circles[i],circular(colors,i))



