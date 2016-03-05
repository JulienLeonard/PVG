from utils       import *
from color       import *

class Style:
    def __init__(self,color = Color.black(), sizeratio = 1.0):
        self.mcolor = color
        self.msizeratio = sizeratio

    def color(self,value = None):
        if value == None:
            return self.mcolor
        else:
            self.mcolor = value
            return self

    def sizeratio(self,value = None):
        if value == None:
            return self.msizeratio
        else:
            self.msizeratio = value
            return self

        
