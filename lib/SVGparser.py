from xml.dom import minidom
from silhouette import *
from color      import *

class SVGStyle:

    def __init__(self,svgstyle):
        self.msvgstyle = svgstyle
        self.mfillcolor     = None                

    def _parsestyle(self):
        fillcolor   = None
        fillopacity = 1.0
        for pair in self.msvgstyle.split(";"):
            keyvalue = pair.split(":")
            key   = keyvalue[0]
            value = keyvalue[1]
            
            if key == "fill":
                fillcolor = value
            if key == "fill-opacity":
                fillopacity = value

        self.mfillcolor = self._parsecolor(fillcolor,fillopacity)

    def _parsecolor(self,svgcolor,svgopacity):
        if svgcolor == "none":
            return None
        else:
            r = svgcolor[1:3]
            g = svgcolor[3:5]
            b = svgcolor[5:7]
            vs = [r,g,b]
            vs = [(float(int(v,16)) / 255.0) for v in vs]
            return Color(vs[0],vs[1],vs[2],svgopacity)

    def fillcolor(self):
        self._parsestyle()
        return self.mfillcolor


class SVGPath:

    def __init__(self,pathstring,stylestring):
        self.mpathstring  = pathstring
        self.mstyle       = SVGStyle(stylestring)

    def fillcolor(self):
        return self.mstyle.fillcolor()

    def silhouette(self):
        # puts("pathstring",self.mpathstring)
        return Silhouette(self.mpathstring)

class SVGParser:
    
    def __init__(self,filepath=None):
        self.mfilepath = filepath
        self.mpaths    = None

    def parse(self,filepath=None):
        if filepath != None:
            self.mfilepath = filepath
        doc = minidom.parse(filepath)
        path_strings  = [path.getAttribute('d')     for path in doc.getElementsByTagName('path')]
        style_strings = [path.getAttribute('style') for path in doc.getElementsByTagName('path')]
        doc.unlink()
        self.mpaths = [SVGPath(path,style) for (path,style) in zip(path_strings,style_strings)]
        return self

    def paths(self):
        if self.mpaths == None and self.mfilepath != None:
            self.parse()
        return self.mpaths

def svgPaths(filepath):
    return SVGParser().parse(filepath).paths()

    
