from Render import *

class RenderSVG(Render):
    def initpicture(self,imagedim,filename,backcolor):
        self.mimagedim = imagedim
        self.mfilename = filename
        self.mfile     = open(self.mfilename,'w+')
        self.mfile.write("<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"" + str(imagedim.width()) + "\" height=\"" + str(imagedim.height()) + "\" ")

        # set background
        # TODO

    def setviewport(self,viewport):
        svgViewport = "viewBox=\"" + str(viewport.center().x() - viewport.radius()) + " " + str(viewport.center().y() - viewport.radius()) + " " + str(viewport.radius() * 2.0) + " " + str(viewport.radius() * 2.0) + "\"" 
        self.mfile.write(svgViewport + " >\n")

    def selfinit(self):
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.mviewport)

    def endpicture(self):
        self.mfile.write("</svg>\n")
        self.mfile.close()

    def drawpolygonpicture(self,polygon,colorc):
        ir = int(255.0 * colorc.r())
        ig = int(255.0 * colorc.g())
        ib = int(255.0 * colorc.b())
        
        svgrgb = str(ir) + "," + str(ig) + "," + str(ib)
        svgStyleFillColor = "style=\"fill:rgb(" + svgrgb + ");fill-opacity:" + str(colorc.a()) + ";stroke-width:0\""

        svgPoints = ""
        for p in polygon.points():
            svgPoints  = svgPoints + str(p.x()) + "," + str(p.y()) + " "

        svgPolygon = "<polygon points=\"" + svgPoints + "\" " + svgStyleFillColor + "/>\n"

        self.mfile.write(svgPolygon)

    def drawcirclepicture(self,circle,style):
        colorc = style.color()
        ir = int(255.0 * colorc.r())
        ig = int(255.0 * colorc.g())
        ib = int(255.0 * colorc.b())
        
        svgrgb = str(ir) + "," + str(ig) + "," + str(ib)
        svgStyleFillColor = "style=\"fill:rgb(" + svgrgb + ");fill-opacity:" + str(colorc.a()) + ";stroke-width:0\""

        # svgPolygon = "<polygon points=\"" + svgPoints + "\" " + svgStyleFillColor + "/>\n"
        svgPolygon = "<circle cx=\"" + str(circle.x()) + "\" cy=\"" + str(circle.y()) + "\" r=\"" + str(circle.r()) + "\" " + svgStyleFillColor + "/>\n"

        self.mfile.write(svgPolygon)

    
        
class RenderCenterSVG(RenderSVG):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor
        self.mmargin = 1.0

    def drawcircle( self, circle, style = None):
        if not circle == None:
            self.mdrawings.append(Drawing(circle,style))


    def drawpolygon( self, polygon, style = None):
        if not polygon == None:
            self.mdrawings.append(Drawing(polygon,style))

    def end(self):
        puts("RenderCenter(RenderCairo end start")
        self.initpicture(self.mimagedim,self.outputfilepath(),self.mbackcolor)
        self.setviewport(self.viewport())
        puts("RenderCenter(RenderCairo start drawing")
        for drawing in self.mdrawings:
            shape = drawing.shape()
            if isinstance(shape,Polygon):
                self.drawpolygonpicture(shape,drawing.style())
            if isinstance(shape,Circle):
                self.drawcirclepicture(shape,drawing.style())
                
        self.endpicture()

    def viewport(self):
        return bbunions([drawing.shape().bbox() for drawing in self.mdrawings]).resize(self.margin()).viewport()
            
