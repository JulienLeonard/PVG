from utils    import *

# from stackoverflow
def hsv_to_rgb(h,s,v):
    if s == 0.0: return [v, v, v]
    i = int(h*6.) # XXX assume int() truncates!
    f = (h*6.)-i; p,q,t = v*(1.-s), v*(1.-s*f), v*(1.-s*(1.-f)); i%=6
    if i == 0: return [v, t, p]
    if i == 1: return [q, v, p]
    if i == 2: return [p, v, t]
    if i == 3: return [p, q, v]
    if i == 4: return [t, p, v]
    if i == 5: return [v, p, q]

# from stackoverflow
def hslv2rgb(p, q, t):
    if t < 0.0:
        t += 1.0
    if t > 1.0:
        t -= 1.0
    if t < 1.0/6.0: 
        return p + (q - p) * 6.0 * t
    if t < 0.5: 
        return q
    if t < 2.0/3.0:
        return p + (q - p) * (2.0/3.0 - t) * 6.0
    return p


def hsl_to_rgb(h, s, l):
    r = 0.0
    g = 0.0 
    b = 0.0

    if s == 0.0:
        r = 1.0
        g = 1.0
        b = 1.0
    else:
        q = iff(l <= 0.5, l * (1.0 + s), l + s - l * s)
        p = 2.0 * l - q
        r = hslv2rgb(p, q, h + 1.0/3.0)
        g = hslv2rgb(p, q, h)
        b = hslv2rgb(p, q, h - 1.0/3.0)


    return [r, g ,b]



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
        return Color(v,v,v,a)

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
            if result[i] < 0.0:
                result[i] = 0.0
            elif result[i]>1.0:
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

        r,g,b = hsl_to_rgb(h,s,l)
        return Color(r,g,b,a)

    @staticmethod
    def hue2color(hue):
        return Color.hsv(hue, 1.0, 1.0,1.0)

    @staticmethod
    def index2color(period,index):
        return Color.hue2color(float(index%period)/(float(period)))



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


