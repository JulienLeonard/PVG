from canvas        import *
from renderSunflow import *

class CanvasSunflow(CanvasInterface):

    def render(self):
        if self.mrender == None:
            self.mrender = RenderSunflow(self.msizes,self.mbackground).outputfilepath(self.moutputfilename).margin(self.mmargin)
        return self.mrender
