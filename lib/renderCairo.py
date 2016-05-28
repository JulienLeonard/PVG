from   Render import *
# import cairo
import cairocffi as cairo

class RenderCairo(Render):
    
    def initpicture(self,imagedim,backcolor):
        self.mimagedim = imagedim
        self.msurface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, imagedim.width(), imagedim.height())
        self.mctx      = cairo.Context(self.msurface)

        # set background
        self.mctx.rectangle(0.0, 0.0, imagedim.width(), imagedim.height())
	self.mctx.set_source_rgb(backcolor.r(), backcolor.g(), backcolor.b())
	self.mctx.fill()

    def setviewport(self,viewport):
        ctx = self.mctx
        # ctx.translate(viewport.center().x(), viewport.center().y())
        puts("viewport radius",viewport.radius())
        ctx.scale(self.mimagedim.width()/(viewport.radius() * 2.0), self.mimagedim.height()/(viewport.radius() * 2.0))
        ctx.translate(-viewport.center().x() + viewport.radius(), -viewport.center().y() + viewport.radius())
        # ctx.scale(self.mimagedim.width(), self.mimagedim.height())

    def selfinit(self):
        self.initpicture(self.mimagedim,self.mbackcolor)
        self.setviewport(self.mviewport)

    def endpicture(self):
        self.msurface.write_to_png (self.outputfilepath())

    def drawcirclepicture(self,circle,style):
        # puts("RenderCairo drawcirclepicture style sizeratio",style.sizeratio())
        if style == None:
            style = Style()

        ctx = self.mctx

        ctx.arc(circle.x(),circle.y(),circle.r() * style.sizeratio(),0.0, 2.0 * 3.14159)

        # then fill with color
        colorc = style.color()
        ctx.set_source_rgba(colorc.r(), colorc.g(),colorc.b(),colorc.a())
        ctx.fill()

    def drawpolygonpicture(self,polygon,style):
        # puts("RenderCairo drawpolygonpicture style sizeratio",style.sizeratio())
        ctx = self.mctx

        # first draw path
        pointcoords = polygon.coords()
        if len(pointcoords) > 1:
            ctx.move_to(pointcoords[0], pointcoords[1])
        for (x,y) in foreach2(pointcoords[2:]):
            ctx.line_to(x, y)

        # then fill with color
        colorc = style.color()
        ctx.set_source_rgba(colorc.r(), colorc.g(),colorc.b(),colorc.a())
        ctx.fill()


class RenderCenter(RenderCairo):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor

    def drawcircle( self, circle, style = None):
        if not circle == None:
            self.mdrawings.append(Drawing(circle,style))


    def drawpolygon( self, polygon, style = None):
        if not polygon == None:
            self.mdrawings.append(Drawing(polygon,style))

    def end(self):
        mncircles = 0
        puts("RenderCenter(RenderCairo end start")
        self.initpicture(self.mimagedim,self.mbackcolor)
        self.setviewport(self.viewport())
        puts("RenderCenter(RenderCairo start drawing")
        for drawing in self.mdrawings:
            shape = drawing.shape()
            if isinstance(shape,Polygon):
                self.drawpolygonpicture(shape,drawing.style())
            if isinstance(shape,Circle):
                self.drawcirclepicture(shape,drawing.style())
                mncircles+=1

        puts("N circles to draw",mncircles)
        self.endpicture()

    def viewport(self):
        return bbunions([drawing.shape().bbox() for drawing in self.mdrawings]).resize(self.margin()).viewport()
        
class RenderPDF(RenderCenter):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor
        self.mmargin    = 1.0

    def margin(self, v = None):
        if v == None:
            return self.mmargin
        else:
            self.mmargin = v
            return self

    def initpicture(self,imagedim,backcolor):
        self.mimagedim = imagedim
        self.msurface  = cairo.PDFSurface(self.mfilename, imagedim.width(), imagedim.height())
        self.mctx      = cairo.Context(self.msurface)

        # set background
        self.mctx.rectangle(0.0, 0.0, imagedim.width(), imagedim.height())
	self.mctx.set_source_rgb(backcolor.r(), backcolor.g(), backcolor.b())
	self.mctx.fill()
    
    def endpicture(self):
        # nothing to do
        v = 1

def f2d(val):
    return '{0:.1f}'.format(val)

#
# dump everythin as a huge circles array for animation
#
class RenderJS(RenderCenter):
    def __init__(self,imagedim,backcolor=Color.white()):
        self.mdrawings  = []
        self.mimagedim  = imagedim
        self.mbackcolor = backcolor
        self.mmargin    = 1.0

    def margin(self, v = None):
        if v == None:
            return self.mmargin
        else:
            self.mmargin = v
            return self

    def initpicture(self,imagedim,backcolor):
        self.mimagedim = imagedim
        self.mcontent  = []

    def drawcirclepicture(self,circle,style):
        # puts("RenderJS drawcirclepicture style sizeratio",style.sizeratio())
        if style == None:
            style = Style()
        colorc = style.color()
        self.mcontent.append("[" + ",".join([f2d(circle.x()),f2d(circle.y()),f2d(circle.r() * style.sizeratio()),f2d(colorc.r()), f2d(colorc.g()),f2d(colorc.b()),f2d(colorc.a())]) + "]")
    
    def end(self):
        mncircles = 0
        puts("RenderJS end start")
        self.initpicture(self.mimagedim,self.mbackcolor)
        # self.setviewport(self.viewport())
        puts("RenderCenter(RenderJS start drawing")
        for drawing in self.mdrawings:
            shape = drawing.shape()
            if isinstance(shape,Polygon):
                self.drawpolygonpicture(shape,drawing.style())
            if isinstance(shape,Circle):
                self.drawcirclepicture(shape,drawing.style())
                mncircles+=1

        puts("N circles to draw",mncircles)
        self.endpicture()

    def endpicture(self):
        outputfilepath = self.outputfilepath().replace(".ppm",".js")
        puts("RenderJS output",outputfilepath)
        fput(outputfilepath,",\n".join(self.mcontent))
        fput(self.outputfilepath(),",\n".join(self.mcontent))
