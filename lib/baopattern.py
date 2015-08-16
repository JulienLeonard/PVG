from utils         import *
from geoutils      import *
import color

class BaoPattern:
    def __init__(self):
        self.msidepattern   = [1.0]
        self.mradiuspattern = [1.0]
        self.mcolorpattern  = [color.black()]
        self.mindex   = 0

    #
    # return (Side,RatioRadius,Color)
    #
    def next(self):
        self.mindex += 1
        return (lcircular(self.msidepattern,self.mindex),lcircular(self.mradiuspattern,self.mindex),lcircular(self.mcolorpattern,self.mindex))

    def sidepattern(self,sidepattern):
        self.msidepattern = sidepattern
        return self

    def radiuspattern(self,radiuspattern):
        self.mradiuspattern = radiuspattern
        return self

    def colorpattern(self,colorpattern):
        self.mcolorpattern = colorpattern
        return self
        

    
