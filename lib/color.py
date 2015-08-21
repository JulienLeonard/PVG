from utils     import *
from colorsys import *

class Color:

    def __init__(self,r=0.0,g=0.0,b=0.0,a=1.0):
        self.mr = r
        self.mg = g
        self.mb = b
        self.ma = a

    def values(self):
        return [self.mr, self.mg, self.mb, self.ma]


    def r(self,v=None):
        if v == None:
            return self.mr
        else:
            return Color(v,self.g(),self.b(),self.a())

    def g(self,v=None):
        if v == None:
            return self.mg
        else:
            return Color(self.r(),v,self.b(),self.a())

    def b(self,v=None):
        if v == None:
            return self.mb
        else:
            return Color(self.r(),self.g(),v,self.a())


    def a(self,v=None):
        if v == None:
            return self.ma
        else:
            return Color(self.r(),self.g(),self.b(),v)


    @staticmethod
    def name(name):
        if name == "red":
            return Color.red()
        if name == "green":
            return Color.green()
        if name == "white":
            return Color.white()
        if name == "blue":
            return Color.blue()
        if name == "yellow":
            return Color.yellow()
        if name == "orange":
            return Color.orange()
        if name == "black":
            return Color.black()

    @staticmethod
    def parse(spec):
        specs = spec.split(" ") 
        if len(specs) == 1:
            return name(spec)
        else:
            return Color(specs)

    @staticmethod
    def white(a=1.0):
        return Color(1.0,1.0,1.0,a)

    @staticmethod
    def red(a=1.0):
        return Color(1.0,0.0,0.0,a)

    @staticmethod
    def blue(a=1.0):
        return Color(0.0,0.0,1.0,a)

    @staticmethod
    def yellow(a=1.0):
        return Color(1.0,1.0,0.0,a)

    @staticmethod
    def green(a=1.0):
        return Color(0.0,1.0,0.0,a)

    @staticmethod
    def orange(a=1.0):
        return Color(1.0,0.5,0.0,a)

    @staticmethod
    def black(a=1.0):
        return Color(0.0,0.0,0.0,a)

    @staticmethod
    def grey(v=0.5,a=1.0):
        return COlor(v,v,v,a)

    @staticmethod
    def random(a=1.0):
        return Color(random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0),a)

    @staticmethod
    def rand(a=1.0):
        return Color.random(a)

    @staticmethod
    def trimcolor(color):
        result = color.values()
        for i in range(4):
            if color[i] < 0.0:
                result[i] = 0.0
            elif color[i]>1.0:
                result[i] = 1.0
        return Color(result[0],result[1],result[2],result[3])


    @staticmethod
    def hsv(h,s=1.0,v=1.0,a=1.0):
        if h > 1.0:
            h -= 1.0
        elif h < 0.0:
            h += 1.0

        r,g,b = hsv_to_rgb(h,s,v)
        return  Color(r,g,b,a)

    @staticmethod
    def hsl(h,s=1.0,l=1.0,a=1.0):
        if h > 1.0:
            h -= 1.0
        elif h < 0.0:
            h += 1.0

        r,g,b = hls_to_rgb(h,l,s)
        return Color(r,g,b,a)

    @staticmethod
    def hue2color(hue):
        return Color.hsv(hue, 1.0, 1.0,1.0)



#
# compute a palette object from a base: base is the accent color
#

class Palette:
    def __init__(self):
        self.maccent      = ""
        self.mbackground  = ""
        self.mbackground2 = ""
        self.mbase        = ""

    def setaccenthue(self,accenthue):
        self.maccent      = hsl(accenthue,1.0,0.5,1.0)
        self.mbackground  = hsl(accenthue + 0.5,0.5,0.9,1.0)
        self.mbackground2 = hsl(accenthue + 0.5,0.1,0.5,1.0)
        self.mbase        = hsl(accenthue + 0.5,0.5,0.1,1.0)
        return self

    def background(self):
        return self.mbackground

    def background2(self):
        return self.mbackground2

    def accent(self):
        return self.maccent

    def base(self):
        return self.mbase


def tricolor(accenthue):
    return Palette().setaccenthue(accenthue)


