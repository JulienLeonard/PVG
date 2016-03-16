from utils       import *
from geoutils    import *
from color       import *
from Render      import *

class CanvasInterface:
    def __init__(self,filename = "temp.png"):
        self.mrender           = None
        self.moutputfilename   = filename
        self.msizes            = ImageDim(1000,1000)
        self.mbackground       = Color.white()
        self.moutputdir        = defaultoutputdir()
        self.mmargin           = 1.25

    def outputdir(self,outdir):
        self.moutputdir = outdir
        return self

    def output(self,filename):
        self.moutputfilename = filename
        return self

    def size(self,size):
        self.msizes = ImageDim(size,size)
        return self

    def background(self,background):
        self.mbackground = background
        return self

    def margin(self,margin):
        self.mmargin = margin
        return self

    # to be overloaded by backend
    def render(self):
        return None

    def save(self,outputfilepath=None):
        if not outputfilepath == None:
            self.render().outputfilepath(outputfilepath)
        self.render().end()

    def draw(self,shape,style = None):
        self.render().draw(shape,style)
        return self

    
