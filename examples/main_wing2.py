import sys
sys.path.insert(0, './../lib')

from utils      import *
from canvas     import *
from SVGparser  import *
from silhouette import *
from color      import *

render = Canvas("main_wing2.png").render()

paths  = svgPaths("wing2.svg")
silhouette = svgpaths2silhouette(paths)
render.drawpolygons(silhouette.polygons(0),Color.black())
render.drawpolygons(silhouette.polygons(1),Color.white())
render.end()
