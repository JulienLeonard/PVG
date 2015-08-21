from drawutils import *
import cairo

class RenderCairo(Render):
    def initpicture(self,imagedim,filename,backcolor):
        self.mimagedim = imagedim
        self.msurface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, imagedim.width(), imagedim.height())
        self.mctx      = cairo.Context(self.msurface)
        self.mfilename = filename

        # set background
        self.mctx.rectangle(0.0, 0.0, imagedim.width(), imagedim.height())
	self.mctx.set_source_rgb(backcolor.r(), backcolor.g(), backcolor.b())
	self.mctx.fill()

    def setviewport(self,viewport):
        ctx = self.mctx
        # ctx.translate(viewport.center().x(), viewport.center().y())
        ctx.scale(self.mimagedim.width()/(viewport.radius() * 2.0), self.mimagedim.height()/(viewport.radius() * 2.0))
        ctx.translate(-viewport.center().x() + viewport.radius(), -viewport.center().y() + viewport.radius())
        # ctx.scale(self.mimagedim.width(), self.mimagedim.height())

    def selfinit(self):
        self.initpicture(self.mimagedim,self.mfilename,self.mbackcolor)
        self.setviewport(self.mviewport)

    def endpicture(self):
        self.msurface.write_to_png (self.mfilename)

    def drawpolygonpicture(self,polygon,colorc):
        ctx = self.mctx

        # first draw path
        pointcoords = polygon.coords()
        if len(pointcoords) > 1:
            ctx.move_to(pointcoords[0], pointcoords[1])
        for (x,y) in foreach2(pointcoords[2:]):
            ctx.line_to(x, y)

        # then fill with color
        ctx.set_source_rgba(colorc.r(), colorc.g(),colorc.b(),colorc.a())
        ctx.fill()


class RenderCenter(RenderCairo):
    def __init__(self,imagedim,filename,backcolor=Color.white()):
        self.mitems    = []
        self.mimagedim = imagedim
        self.filename  = filename
        self.backcolor = backcolor

    def drawpolygon( self, polygon, colorc ):
        if not polygon == None:
            self.mitems.append((polygon,colorc))

    def end(self):
        self.initpicture(self.mimagedim,self.filename,self.backcolor)
        self.setviewport(self.viewport())
        for item in self.mitems:
            polygon,color = item
            self.drawpolygonpicture(polygon,color)
        self.endpicture()

    def viewport(self):
        return polygons2bbox([item[0] for item in self.mitems]).resize(1.25).viewport()
        
            
