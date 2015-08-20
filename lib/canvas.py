from utils     import *
from drawutils import *
from geoutils  import *
from color     import *


class Canvas():
    def __init__(self,outputfilename):
        self.mrender           = None
        self.moutputfilename   = outputfilename
        self.msizes            = ImageDim(1000,1000)
        self.mbackground       = Color.white()
        self.moutputdir        = "/".join(os.path.dirname(os.path.realpath(__file__).replace("\\","/")).split("/")[:-1]) + "/output"

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
