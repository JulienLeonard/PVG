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
        
            
