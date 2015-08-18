from utils     import *
from colorsys import *

def name(name):
    if name == "red":
        return red()
    if name == "green":
        return green()
    if name == "white":
        return white()
    if name == "blue":
        return blue()
    if name == "yellow":
        return yellow()
    if name == "orange":
        return orange()
    if name == "black":
        return black()

def parse(spec):
    specs = spec.split(" ") 
    if len(specs) == 1:
        return name(spec)
    else:
        return specs

def white(a=1.0):
    return [1.0,1.0,1.0,a]

def red(a=1.0):
    return [1.0,0.0,0.0,a]

def blue(a=1.0):
    return [0.0,0.0,1.0,a]

def yellow(a=1.0):
    return [1.0,1.0,0.0,a]

def green(a=1.0):
    return [0.0,1.0,0.0,a]

def orange(a=1.0):
    return [1.0,0.5,0.0,a]

def black(a=1.0):
    return [0.0,0.0,0.0,a]

def grey(v=0.5,a=1.0):
    return [v,v,v,a]

def colorrandom(a=1.0):
    return [random.uniform(0.0,1.0),random.uniform(0.0,1.0),random.uniform(0.0,1.0),a]

def rand(a=1.0):
    return colorrandom(a)

def trimcolor(color):
    result = color[:]
    for i in range(4):
        if color[i] < 0.0:
            result[i] = 0.0
        elif color[i]>1.0:
            result[i] = 1.0
    return result
           

def hsv(h,s=1.0,v=1.0,a=1.0):
    if h > 1.0:
        h -= 1.0
    elif h < 0.0:
        h += 1.0

    r,g,b = hsv_to_rgb(h,s,v)
    return [r,g,b,a]

def hsl(h,s=1.0,l=1.0,a=1.0):
    if h > 1.0:
        h -= 1.0
    elif h < 0.0:
        h += 1.0

    r,g,b = hls_to_rgb(h,l,s)
    return [r,g,b,a]

def hue2color(hue):
    return hsv(hue, 1.0, 1.0,1.0)

def a(color,v=None):
    if v == None:
        return color[-1]
    else:
        return color[:-1] + [v]

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


