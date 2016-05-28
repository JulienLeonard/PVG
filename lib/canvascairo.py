from canvas      import *
from renderCairo import *

class Canvas(CanvasInterface):

    def render(self):
        if self.mrender == None:
            self.mrender = RenderCenter(self.msizes,self.mbackground).outputfilepath(self.moutputfilename).margin(self.mmargin)
        return self.mrender

class CanvasPDF(CanvasInterface):
    
    def render(self):
        if self.mrender == None:
            self.mrender = RenderPDF(self.msizes,self.mbackground).outputfilepath(self.moutputfilename).margin(self.mmargin)
        return self.mrender

#
# generate a list of circles for animation in javascript
#
class CanvasJS(CanvasInterface):
    
    def render(self):
        if self.mrender == None:
            self.mrender = RenderJS(self.msizes,self.mbackground).outputfilepath(self.moutputfilename).margin(self.mmargin)
        return self.mrender

