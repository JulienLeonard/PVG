from utils         import *
from geoutils      import *
from color         import *
from style         import *

class BaoPattern:
    def __init__(self):
        self.mradiuspattern = [1.0]
        self.mcolorpattern  = [Color.black()]
        self.mindex         = 0
        self.mfdraw         = None

    #
    # return (RatioRadius,Color)
    #
    def next(self):
        self.mindex += 1
        # return (self.nextradius(),self.nextcolor())
        return self

    def radiuspattern(self,radiuspattern):
        self.mradiuspattern = radiuspattern
        return self

    def colorpattern(self,colorpattern):
        self.mcolorpattern = colorpattern
        return self

    def fdraw(self, v = None):
        if v == None:
            return self.mfdraw
        else:
            self.mfdraw = v
            return self

    def draw(self,newnode,index):
        self.fdraw()(newnode,index,Style(self.color(index)))

    def radius(self):
        return lcircular(self.mradiuspattern,self.mindex)

    def color(self,index=None):
        if index == None:
            index = self.mindex
        return lcircular(self.mcolorpattern,index)
    
