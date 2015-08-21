from utils       import *
from geoutils    import *
from color       import *
from renderCairo import *

class Canvas():
    def __init__(self,outputfilename):
        self.mrender           = None
        self.moutputfilename   = outputfilename
        self.msizes            = ImageDim(1000,1000)
        self.mbackground       = Color.white()
        self.moutputdir        = defaultoutputdir()

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

    def render(self):
        self.mrender = RenderCenter(self.msizes,self.moutputdir + "/" + self.moutputfilename,self.mbackground)
        return self.mrender
