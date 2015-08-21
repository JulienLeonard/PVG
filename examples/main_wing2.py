import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from color      import *

render = Canvas("main_wing2.ppm").render()

paths  = svgPaths("wing2.svg")
silhouettes = [path.silhouette() for path in paths if (not path.fillcolor() == None and path.fillcolor().r() > 0.5)]
for (silhouette,ccolor) in lzip(silhouettes,[Color.green(0.5),Color.red(0.5),Color.yellow(0.5)] * 10):
    render.drawpolygons(silhouette.polygons(0),ccolor)
    

render.end()
