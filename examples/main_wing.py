import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from color      import *

render = Canvas("main_wing.png").render()

paths  = svgPaths("wing.svg")
paths = [path for path in paths if (not path.fillcolor()  == None)]
silhouette = svgpaths2silhouette(paths)
render.drawpolygons(silhouette.polygons(0),Color.green())
render.drawpolygons(silhouette.polygons(1),Color.red())
render.end()
