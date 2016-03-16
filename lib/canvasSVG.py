from canvas      import *
from renderSVG   import *

class CanvasSVG(CanvasInterface):
    
    def render(self):
        if self.mrender == None:
            self.mrender = RenderCenterSVG(self.msizes,self.mbackground)
        return self.mrender

    def save(self,outputfilepath):
        self.render()
        self.mrender.mfilename = outputfilepath
        self.render().end()
